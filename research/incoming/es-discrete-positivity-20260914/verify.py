#!/usr/bin/env python3
"""Discrete odd-defect positivity certificates for Erdős--Straus.
Python >=3.9; standard library only. All checks survive python -O.

The infinite estimates are proved in core.tex, not inferred from this finite
replay. The large prime is certified exactly. No least-counterexample,
new prime-coverage, universal ES, or independent-review claim is made.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import comb, factorial, gcd, isqrt, prod, ceil, floor
from pathlib import Path
import hashlib
import json

BASE=Path(__file__).resolve().parent

CHECKS=Counter()
PSTAR=19748674681
ASTAR=4937168704
RSTAR=135
FACTORS=((2,6),(13,4),(37,1),(73,1))


def check(statement, name):
    CHECKS[name]+=1
    if not statement:
        raise ArithmeticError(name)


def factor(n):
    if n<1: raise ValueError('positive integer required')
    out=[];q=2
    while q*q<=n:
        e=0
        while n%q==0:n//=q;e+=1
        if e:out.append((q,e))
        q=3 if q==2 else q+2
    if n>1:out.append((n,1))
    return tuple(out)


def trial_prime(n):
    if n<2:return False
    if n%2==0:return n==2
    for q in range(3,isqrt(n)+1,2):
        if n%q==0:return False
    return True


def prime_certificate():
    factors=((2,3),(3,1),(5,1),(7,1),(23510327,1))
    check(prod(q**e for q,e in factors)==PSTAR-1,'full_p_minus_one_factorization')
    for q,e in factors:check(trial_prime(q),'prime_factor_by_exhaustive_trial')
    base=11
    check(pow(base,PSTAR-1,PSTAR)==1,'Lucas_full_order_power')
    residues=[]
    for q,e in factors:
        z=pow(base,(PSTAR-1)//q,PSTAR)
        check(gcd(z-1,PSTAR)==1,'Lucas_prime_divisor_order')
        residues.append((q,z))
    check(PSTAR%840==1,'hard_class_one_mod_840')
    # Independent complete primality trial at this modest 11-digit integer.
    check(trial_prime(PSTAR),'large_prime_independent_trial')
    return dict(n=PSTAR,base=base,p_minus_one=factors,residues=residues,
                independent_trial_bound=isqrt(PSTAR),
                scope='exact primality certificate, not a probable-prime test')


def pmul(A,B):
    C=[F(0)]*(len(A)+len(B)-1)
    for i,a in enumerate(A):
        for j,b in enumerate(B):C[i+j]+=a*b
    return tuple(C)


def padd(A,B):
    C=[F(0)]*max(len(A),len(B))
    for i,a in enumerate(A):C[i]+=a
    for i,b in enumerate(B):C[i]+=b
    return tuple(C)


def ev(P,x):
    y=F(0)
    for a in reversed(P):y=y*x+a
    return y


@lru_cache(None)
def polynomial(m,s=1):
    if m<0 or s<0:raise ValueError('nonnegative filter indices required')
    P=(F(1),)
    for j in range(1,m+1):P=pmul(P,(F(-1,2*j),F(2*j+1,2*j)))
    return (F(0),)*s+P


def exact_filter(D,m,s=1):
    if D<1 or D%2==0:raise ValueError('original positive odd defect required')
    if D==1:return F(1)
    k=(D-1)//2
    if k<=m:return F(0)
    return (-1)**m*F(comb(k-1,m),D**(m+s))


def crude_error(m,s=1):
    return F(1,2**m*factorial(m)*(2*m+3)**s)


@lru_cache(None)
def sharp_error(m,s=1):
    if m<0 or s<0:raise ValueError('nonnegative filter indices required')
    if s==0:
        return dict(error=F(1,2**m*factorial(m)),supremum_at='D tends to infinity',window=None,maximizers=[])
    if m==0:
        return dict(error=F(1,3**s),supremum_at='attained',window=(1,1),maximizers=[3])
    c=F(m*(m+2),2*s)
    lo=max(m+1,floor(1+c));hi=max(m+1,ceil(m+c))
    vals={k:abs(exact_filter(2*k+1,m,s)) for k in range(lo,hi+1)}
    E=max(vals.values())
    return dict(error=E,supremum_at='attained',window=(lo,hi),
                maximizers=[2*k+1 for k,v in vals.items() if v==E])


def coefficient_intervals(P,moments,delta):
    """Common absolute input error; exact worst-case signed linear range."""
    y=sum((a*b for a,b in zip(P,moments)),F())
    err=delta*sum(abs(a) for a in P)
    return y-err,y+err


def histogram_moments(hist,degree):
    return tuple(sum((F(n,D**j) for D,n in hist.items()),F()) for j in range(degree+1))


def filter_sum(hist,m,s=1):
    return sum((n*exact_filter(D,m,s) for D,n in hist.items()),F())


def signed_score(hist,P):
    return sum((F(3,2)*n*(F(1,D)-F(1,3))*ev(P,F(1,D))**2 for D,n in hist.items()),F())


def first_degree(hist):
    mm=histogram_moments(hist,3)
    m0,m1,m2,m3=mm
    G=-m3+F(7,3)*m2-F(5,3)*m1+F(1,3)*m0
    b=m2-F(4,3)*m1+F(1,3)*m0
    check(G>=0,'first_degree_correction_Gram_nonnegative')
    if G==0:
        check(b==0,'singular_first_degree_range')
        y=F(0)
    else:y=b/G
    P=(1-y,y)
    L=F(3,2)*(m1-m0/3+b*y)
    check(signed_score(hist,P)==L,'canonical_first_degree_value')
    a=m1-m0/3;bb=m2-m1/3;c=m3-m2/3
    failed=a<=0 and c<=0 and a*c>=bb*bb
    check((L>0)==(not failed),'complete_signed_two_by_two_test')
    return dict(L=L,P=P,G=G,b=b,localizer=(a,bb,c),negative_semidefinite=failed,moments=mm)


def marked(p,a,u,c,exponents=None):
    R=4*a-p
    if c not in('E','M') or R<=0 or a*a%u:raise ValueError('actual divisor and channel required')
    d=gcd(a,u);h=d*d//u;r=u//d;s=a//d
    check(h*r*s==a and h*r*r==u and gcd(r,s)==1,'marked_primitive_normalization')
    quotient=F(p*r+s,R) if c=='E' else F(r+s,R)
    den=(F(a),h*s*quotient,p*h*r*quotient) if c=='E' else (F(a),p*h*s*quotient,p*h*r*quotient)
    check(all(t>0 for t in den),'positive_raw_denominators')
    check(sum((1/t for t in den),F())==F(4,p),'original_rational_ES_identity')
    g=4*u+1 if c=='E' else u+a;D=R//gcd(R,g)
    check(den[1].denominator==den[2].denominator==D,'exact_return_defect')
    back=F((1 if c=='E' else p)*a*a,R*den[1]-p*a)
    check(back==u,'ordered_divisor_inverse')
    return dict(p=p,a=a,R=R,u=u,channel=c,h=h,r=r,s=s,
                quotient_name='kappa' if c=='E' else 'lambda',quotient=quotient,
                denominators=den,D=D,exponents=exponents)


def divisors_marked(fs):
    for ff in product(*(range(2*e+1) for q,e in fs)):
        yield prod(q**f for (q,e),f in zip(fs,ff)),ff


def census(p,a,fs=None,retain=False):
    R=4*a-p
    if not p<4*a or not 2*a<p or gcd(p*a,R)!=1 or R%4!=3:raise ValueError('unit first-half shell required')
    fs=fs or factor(a)
    check(prod(q**e for q,e in fs)==a,'complete_a_factorization')
    check(len({q for q,e in fs})==len(fs),'distinct_factor_labels')
    hist=Counter();channels={c:Counter() for c in('E','M')};leaves=[];hits=[]
    for u,ff in divisors_marked(fs):
        for c,g in(('E',4*u+1),('M',u+a)):
            D=R//gcd(R,g);hist[D]+=1;channels[c][D]+=1
            check(D%2==1 and (D==1 or D>=3),'original_odd_defect_domain')
            if retain or D==1:
                state=marked(p,a,u,c,ff)
                state['factors']=fs;state['beta']=tuple(f-e for f,(q,e) in zip(ff,fs))
                if retain:leaves.append(state)
                if D==1:hits.append(state)
    check(sum(hist.values())==2*prod(2*e+1 for q,e in fs),'complete_canonical_state_count')
    return hist,channels,leaves,hits


def independent_modular_histogram(a,fs,R):
    coeff=Counter({1:1})
    for q,e in fs:
        nxt=Counter()
        for v,n in coeff.items():
            for f in range(2*e+1):nxt[v*pow(q,f,R)%R]+=n
        coeff=nxt
    hist=Counter();chs={c:Counter() for c in('E','M')}
    for v,n in coeff.items():
        for c,g in(('E',4*v+1),('M',v+a)):
            D=R//gcd(R,g);hist[D]+=n;chs[c][D]+=n
    return hist,chs,sorted(coeff.items())


def large_example():
    pc=prime_certificate()
    for q,e in FACTORS:check(trial_prime(q),'actual_a_primes')
    hist,channels,leaves,hits=census(PSTAR,ASTAR,FACTORS,True)
    hh,cc,group_poly=independent_modular_histogram(ASTAR,FACTORS,RSTAR)
    check(hist==hh and channels==cc,'two_independent_full_histograms')
    expected={1:1,3:79,5:107,9:160,15:137,27:288,45:488,135:846}
    check(hist==expected,'large_exact_defect_census')
    check(len(hits)==1 and hits[0]['u']==141879296 and hits[0]['channel']=='E','unique_original_success')
    whole=first_degree(hist);exterior=first_degree(channels['E']);middle=first_degree(channels['M'])
    check(whole['L']==F(-50887012,144801015),'occupied_shell_first_degree_counterexample')
    check(exterior['L']==F(1692013,5172810)>0,'retained_exterior_canonical_positivity')
    check(middle['L']==F(-49112734,72381675)<0,'middle_sector_negative_not_absent')
    P=(F(-1,35),F(36,35))
    positive=signed_score(channels['E'],P)
    check(positive==F(64376,196875)>0,'simple_fixed_exterior_certificate')
    coarse_same=signed_score(hist,P)
    check(coarse_same<0,'forgetting_channel_hides_positive_direction')
    P2=(F(0),F(-1,2),F(3,2))
    score2=signed_score(hist,P2)
    check(score2==F(145598746,184528125)>0,'simple_full_shell_degree_two_certificate')
    S=[sum(n*(RSTAR//D)**j for D,n in hist.items()) for j in range(6)]
    A=[3*S[j+1]-RSTAR*S[j] for j in range(3)]
    check(A==[-242424,-937656,-5258952] and A[0]*A[2]-A[1]**2==395697405312,'negative_definite_integer_localizer')
    scores=[]
    for m in range(10):
        ss=filter_sum(hist,m)
        check((ss<=1 if m%2 else ss>=1),'large_signed_discrete_filter')
        check(abs(ss-1)<=sum(hist.values())*sharp_error(m)['error'],'large_sharp_filter_error')
        scores.append(dict(m=m,degree=m+1,score=ss,error=sharp_error(m)['error']))
    return dict(primality=pc,p=PSTAR,a=ASTAR,R=RSTAR,factors=FACTORS,histogram=hist,
                channels=channels,original_states=leaves,hits=hits,integer_moments=S,localizer=A,
                first_degree_whole=whole,first_degree_E=exterior,first_degree_M=middle,
                simple_E_polynomial=P,simple_E_score=positive,same_polynomial_coarse_score=coarse_same,
                simple_full_polynomial=P2,simple_full_score=score2,
                group_polynomial=group_poly,discrete_filter_scores=scores,
                scope='one explicit hard prime; no claim of least failure or ES failure')



def lucas_dag_check(root, certificate):
    completed={};visiting=set()
    def visit(n):
        if n in completed:return
        if n<10000:
            check(trial_prime(n),'Lucas_small_leaf_trial');completed[n]='trial';return
        if n in visiting or str(n) not in certificate:raise ValueError('missing or circular prime proof')
        visiting.add(n);node=certificate[str(n)]
        if node['n']!=n:raise ValueError('prime proof label mismatch')
        fs=node['factorization'];base=node['base']
        check(all(2<=q<n and e>=1 for q,e in fs),'strict_prime_DAG_descent')
        check(len({q for q,e in fs})==len(fs),'distinct_Lucas_factor_labels')
        for q,e in fs:visit(q)
        check(prod(q**e for q,e in fs)==n-1,'recursive_full_factorization')
        check(pow(base,n-1,n)==1,'recursive_Lucas_power')
        for q,e in fs:check(gcd(pow(base,(n-1)//q,n)-1,n)==1,'recursive_Lucas_exact_order')
        visiting.remove(n);completed[n]=base
    visit(root)
    return dict(root=root,verified_nodes=len(completed),proof=certificate)


def second_hard_example():
    p=2671180768668258904496300170662649;a=(p+135)//4
    fs=((2,5),(431,3),(457,3),(7229,4))
    certificate=json.loads((BASE/'prime_proof.json').read_text())
    proof=lucas_dag_check(p,certificate)
    for q,e in fs:check(trial_prime(q),'second_actual_a_primes')
    check(p%840==289,'second_hard_prime_class')
    hist,chs,_,hits=census(p,a,fs)
    hh,cc,poly=independent_modular_histogram(a,fs,135)
    check(hist==hh and chs==cc,'second_independent_histograms')
    check(sum(hist.values())==9702 and len(hits)==3,'second_complete_candidate_count')
    coarse=first_degree(hist);E=first_degree(chs['E']);M=first_degree(chs['M'])
    check(coarse['L']<0 and E['L']<0 and M['L']<0,'both_channels_degree_one_can_fail')
    quartic=filter_sum(hist,3)
    check(quartic==F(54448414,66430125)>0,'quartic_repairs_second_hard_case')
    return dict(p=p,a=a,R=135,factors=fs,prime_certificate=proof,histogram=hist,
                channel_histograms=chs,coarse_degree_one=coarse,E_degree_one=E,M_degree_one=M,
                quartic_score=quartic,marked_hits=hits,group_polynomial=poly,
                scope='9702 candidates exhaust one shell; not a full-prime atlas, no leastness')


def interpolation_tests():
    count=0
    for m in range(8):
        nodes=[F(0),F(1)]+[F(1,2*j+1) for j in range(1,m+1)]
        basis=[]
        for i,x in enumerate(nodes):
            P=(F(1),)
            for j,y in enumerate(nodes):
                if j!=i:P=pmul(P,(-y/(x-y),1/(x-y)))
            check([ev(P,y) for y in nodes]==[F(i==j) for j in range(len(nodes))],'full_interpolation_inverse_columns')
            basis.append(P)
        check(basis[1]==polynomial(m),'filter_is_complete_interpolation_mark')
        for k in range(len(nodes)):
            P=(F(0),)*k+(F(1),)
            back=(F(0),)
            for i,x in enumerate(nodes):back=padd(back,tuple(ev(P,x)*c for c in basis[i]))
            expected=P+(F(0),)*(len(back)-len(P))
            check(back==expected,'interpolation_other_inverse_composition')
            count+=1
    return count

def progression(j):
    if j<0:raise ValueError('nonnegative integer parameter required')
    t=73+945*j;C=67632448;n=4*C*t-135;a=C*t
    kappa=341725215823+8847406287328*j+57265746370560*j*j
    h0=26;r0=32*t;s0=81289;d=gcd(r0,s0)
    check(n==19748674681+255650653440*j and n%840==1,'full_hard_progression')
    check(gcd(19748674681,255650653440)==1,'reduced_prime_progression')
    check(h0*r0*s0==a and 135*kappa==n*r0+s0,'integer_progression_quotient')
    check(gcd(d,135)==1 and kappa%d==0,'nonprimitive_progression_repair')
    den=(a,h0*s0*kappa,n*h0*r0*kappa)
    check(sum((F(1,x) for x in den),F())==F(4,n),'all_progression_ES_values')
    u=h0*r0*r0
    w=marked(n,a,u,'E')
    check((w['h'],w['r'],w['s'],w['quotient'])==(h0*d*d,r0//d,s0//d,F(kappa,d)),'complete_progression_gcd_normalization')
    check(w['denominators']==den,'progression_original_order')
    return dict(j=j,t=t,n=n,gcd=d,raw_h=h0,raw_r=r0,raw_s=s0,raw_kappa=kappa,witness=w)


def filter_tests():
    tables=[]
    for m in range(13):
        for s in range(5):
            P=polynomial(m,s);r=sharp_error(m,s)
            check(ev(P,F(1))==1,'retained_success_value')
            check(sum(abs(a) for a in P)==m+1,'linear_moment_coefficient_conditioning')
            check(ev(P,F(0))==(F(0) if s else F((-1)**m,2**m*factorial(m))),'relation_sector_value_at_zero')
            check(r['error']<=crude_error(m,s),'sharp_below_explicit_factorial_bound')
            for k in range(1,401):
                D=2*k+1;z=exact_filter(D,m,s)
                check(z==ev(P,F(1,D)),'complete_filter_coordinate_identity')
                check((z<=0 if m%2 else z>=0),'one_sided_discrete_sign')
                check(abs(z)<=r['error'],'finite_scalar_bounds_not_infinite_proof')
                if m>=2:
                    check(abs(z)<=abs(exact_filter(D,m-2,s)),'nested_same_parity_filters')
            if s and m:
                lo,hi=r['window'];C=F(m*(m+2),2*s)
                for k in (max(m+1,lo-1),lo,hi,hi+1,hi+100):
                    A=sum((F(2*j+1,k-j) for j in range(1,m+1)),F())
                    if k<1+C:check(A>2*s,'continuous_derivative_lower_side')
                    if k>m+C:check(A<2*s,'continuous_derivative_upper_side')
            if s==1:tables.append(dict(m=m,degree=m+1,polynomial=P,sharp=r,crude=crude_error(m,s)))
    return tables


def schedule(B,accuracy=0):
    if B<1 or accuracy<0:raise ValueError('positive mass bound and nonnegative accuracy')
    m=0
    while 2**m*factorial(m)*(2*m+3)<8*3**accuracy*B:m+=2
    return m


def row_bound(p):
    if p%4!=1 or p<5:raise ValueError('p=1 mod4 required')
    m=(p-1)//4
    return min(6*m*m,4*m*(2*m).bit_length()**2)


def bracket(hist,B,accuracy=0):
    W=sum(hist.values());H=hist.get(1,0)
    if not hist or any(D<1 or D%2==0 or n<0 or int(n)!=n for D,n in hist.items()):
        raise ValueError('nonnegative integer masses on positive odd defects required')
    if W>B:raise ValueError('actual source mass exceeds declared bound')
    m=schedule(B,accuracy)
    up=filter_sum(hist,m);lo=filter_sum(hist,m+1)
    eu=B*crude_error(m);el=B*crude_error(m+1)
    check(lo<=H<=up and up-H<=eu and H-lo<=el,'unscaled_uniform_one_sided_count')
    check(eu<=F(1,8*3**accuracy) and el<=F(1,16*3**accuracy),'uniform_count_schedule_constants')
    check(ceil(lo)==floor(up)==H,'exact_integer_filter_return')
    check((lo>0)==(H>0),'lower_filter_exact_occupancy_test')
    # Any interval moment errors bounded as below still give a unique integer.
    delta=F(1,16*(m+2)*3**accuracy)
    moments=histogram_moments(hist,m+2)
    for sign1,sign2 in ((-1,-1),(-1,1),(1,-1),(1,1)):
        errs=[delta*(sign1 if i%2 else sign2) for i in range(len(moments))]
        approx=[x+e for x,e in zip(moments,errs)]
        lrange=coefficient_intervals(polynomial(m+1),approx,delta)
        urange=coefficient_intervals(polynomial(m),approx,delta)
        lower=lrange[0];upper=urange[1]
        check(lower<=H<=upper and upper-lower<1,'certified_absolute_moment_precision')
        check(ceil(lower)==floor(upper)==H,'interval_integer_reconstruction')
    return dict(m=m,largest_moment_degree=m+2,L=lo,U=up,H=H,W=W,B=B,
                upper_error=eu,lower_error=el,absolute_moment_tolerance=delta)


def array_tests():
    out=[]
    for j in range(1,10):
        W=10**j
        for h in (0,1,2):
            hist=Counter({135:W,5:7,3:5});hist[1]=h
            B=sum(hist.values())
            r=bracket(hist,B)
            out.append(dict(growing_power=j,hit_count=h,bracket=r))
    degrees=[]
    for e in (3,6,12,24,48,96,192):
        B=10**e;m=schedule(B);k=0
        while 3**k<8*B:k+=1
        degrees.append(dict(mass_power10=e,new_degree=m+2,power_filter_degree=k+1,
                            exact_schedule=m,coefficient_sum_max=m+2))
    return dict(growing_synthetic_arrays=out,degree_comparison=degrees)


def split_test(p,a,f):
    fs=factor(a);e=tuple(k for q,k in fs);b=tuple(k-j for k,j in zip(e,f));R=4*a-p
    if len(f)!=len(e) or any(j<0 for j in f) or any(j<0 for j in b):raise ValueError('actual split budget required')
    hist,chs,_,hits=census(p,a,fs)
    weighted=Counter();raw=Counter();occ=[];fibres=Counter();fibre_sizes={}
    for xi in product(*(range(-j,j+1) for j in f)):
        for eta in product(*(range(-j,j+1) for j in b)):
            beta=tuple(x+y for x,y in zip(xi,eta))
            N=prod(min(fi,bi+hi)-max(-fi,bi-hi)+1 for fi,hi,bi in zip(f,b,beta))
            u=prod(q**(ei+bi) for (q,ei),bi in zip(fs,beta))
            for c,g in(('E',4*u+1),('M',u+a)):
                D=R//gcd(R,g);weighted[D]+=F(1,N);raw[D]+=1
                occ.append((D,N));fibres[(beta,c)]+=1;fibre_sizes[(beta,c)]=N
    check(all(fibres[k]==v for k,v in fibre_sizes.items()),'all_actual_addition_fibres')
    check(dict(weighted)==dict(hist),'all_original_split_masses')
    for m in range(7):
        v1=filter_sum(hist,m);v2=sum((exact_filter(D,m)/N for D,N in occ),F())
        check(v1==v2,'all_split_polynomial_traces_compressed')
        check(ev(polynomial(m),F(0))==0,'transported_filter_relation_complement_zero')
    return dict(p=p,a=a,f=f,b=b,original_states=sum(hist.values()),occurrences=len(occ),
                original_hits=hist.get(1,0),raw_occurrence_hits=raw.get(1,0),weighted_histogram=weighted)


def scan_rows(bound):
    counts=Counter();rows=[]
    for p in range(13,bound+1,12):
        if not trial_prime(p):continue
        m=(p-1)//4;hist=Counter();first=None
        for a in range(m+1,2*m+1):
            h,_,_,hits=census(p,a);hist.update(h);counts['shells']+=1
            if hits and first is None:first=hits[0]
        B=row_bound(p);check(sum(hist.values())<=B,'proved_original_row_mass_bound')
        rec=bracket(hist,B);rec.update(p=p,first_witness=first)
        counts['primes']+=1;counts['states']+=sum(hist.values());counts['canonical_hits']+=hist.get(1,0)
        rows.append(rec)
    return dict(bound=bound,domain='all primes p=1 mod12 up to bound, full first-half rows',counts=dict(counts),rows=rows,
                nonclaim='finite replay; no coverage beyond bound inferred')


def negative_controls():
    labels=[]
    def reject(label,fn):
        try:fn()
        except (ArithmeticError,ValueError):labels.append(label);return
        raise ArithmeticError('incorrect negative-control acceptance '+label)
    reject('even defect outside arithmetic spectrum',lambda:exact_filter(4,2))
    reject('mass normalization silently lowered bound',lambda:bracket(Counter({3:100}),1))
    reject('negative parameter in progression',lambda:progression(-1))
    reject('nondivisor as an original candidate',lambda:marked(1201,306,7,'E'))
    reject('constant-term relation sector silently discarded',lambda:check(ev(polynomial(2,0),F(0))==0,'false_no_relation_term'))
    # The positivity certificate genuinely fails when the sole original hit is removed.
    hist,chs,_,_=census(PSTAR,ASTAR,FACTORS);chs['E'][1]-=1
    reject('damaged original hit set accepted',lambda:check(signed_score(chs['E'],(F(-1,35),F(36,35)))>0,'false_positive_after_hit_deletion'))
    reject('discrete sign asserted on whole interval',lambda:check(ev(polynomial(2,0),F(1,4))>=0,'wrong_continuous_sign'))
    return labels


def encode(x):
    if isinstance(x,F):return {'numerator':x.numerator,'denominator':x.denominator}
    if isinstance(x,Counter):return [[encode(k),encode(v)] for k,v in sorted(x.items())]
    if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [encode(v) for v in x]
    return x


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--bound',type=int,default=1500)
    ap.add_argument('--out',default='generated')
    args=ap.parse_args()
    if args.bound<13:ap.error('bound must be at least 13')
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    filters=filter_tests();example=large_example();arrays=array_tests()
    interpolation=interpolation_tests();second=second_hard_example()
    splits=[split_test(2521,636,(1,1,1)),split_test(241,64,(3,)),split_test(1201,312,(2,1,1))]
    # Include both nonprimitive cases and large exact parameters in the family.
    js=sorted(set(list(range(30))+[10**3,10**6,10**12]))
    family=[progression(j) for j in js]
    check(any(v['gcd']>1 for v in family),'nonprimitive_family_inverse_actually_tested')
    rows=scan_rows(args.bound);negative=negative_controls()
    outputs={'filters.json':filters,'hard_prime.json':example,'second_hard_prime.json':second,'arrays.json':arrays,
             'interpolation.json':dict(inverse_basis_cases=interpolation),
             'splits.json':splits,'progression.json':family,'rows.json':rows,
             'negative_controls.json':negative,'checks.json':dict(CHECKS)}
    for name,v in outputs.items():
        (out/name).write_text(json.dumps(encode(v),indent=2,sort_keys=True)+'\n',encoding='utf8')
    print(json.dumps(dict(checks=sum(CHECKS.values()),row_scope=rows['counts'],
                         hard_prime=PSTAR,hard_shell_states=2106,negative_controls=len(negative)),sort_keys=True))

if __name__=='__main__':main()
