#!/usr/bin/env python3
"""Exact SplitZero scalar/inversion and bounded-divisor continuation.
Standard library only. Finite tests corroborate the accompanying proofs.
No universal ES claim. Assertions are not used; -O keeps every check.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import product, combinations_with_replacement
from math import gcd, isqrt, prod
from pathlib import Path
import argparse, json

checks=Counter()
def require(ok: bool, label: str) -> None:
    checks[label]+=1
    if not ok: raise ArithmeticError(label)

def conv(A: dict, B: dict, N: int, additive=False, keep_zero=False):
    """When keep_zero=True keys mean PRESENT, including zero amplitudes."""
    C={}
    for x,a in A.items():
        for y,b in B.items():
            z=(x+y)%N if additive else x*y%N
            C[z]=C.get(z,0)+a*b
    return C if keep_zero else {z:v for z,v in C.items() if v}

def scale(A,s): return {g:s*v for g,v in A.items() if s*v}
def plus(*As):
    C=Counter()
    for A in As:
        for g,v in A.items():C[g]+=v
    return {g:v for g,v in C.items() if v}

@lru_cache(None)
def order(g,R):
    if R<2 or gcd(g,R)!=1:raise ValueError('unit and modulus >=2 required')
    x=1
    for k in range(1,R+1):
        x=x*g%R
        if x==1:return k
    raise ArithmeticError('Lagrange finite order bound')

@lru_cache(None)
def one(g,e,R,c):
    if e<0 or c not in ('E','M'):raise ValueError('nonnegative exponent and E/M required')
    interval=range(2*e+1) if c=='E' else range(-e,e+1)
    return dict(Counter(pow(g,j,R) for j in interval))

def distribution(gs,es,R,c,fast=False):
    if len(gs)!=len(es):raise ValueError('one exponent for each marked factor')
    C={1:1}
    for g,e in zip(gs,es):
        if fast:
            o=order(g,R); k,r=divmod(e,o)
            A=plus(one(g,r,R,c),{pow(g,j,R):2*k for j in range(o)})
        else:A=one(g,e,R,c)
        C=conv(C,A,R)
    return C

def target(R,c):
    if R<3 or R%4!=3:raise ValueError('R=3 mod4 required')
    return (-pow(4,-1,R))%R if c=='E' else R-1

def count(gs,es,R,c,fast=False):return distribution(gs,es,R,c,fast).get(target(R,c),0)

def factor(n):
    if n<1:raise ValueError('positive integer required')
    out=[];q=2
    while q*q<=n:
        e=0
        while n%q==0:n//=q;e+=1
        if e:out.append((q,e))
        q=3 if q==2 else q+2
    if n>1:out.append((n,1))
    return out

def prime(n):return n>=2 and all(n%d for d in range(2,isqrt(n)+1))

def witness(n,a,u,c):
    if c not in ('E','M') or a<1 or u<1:raise ValueError('positive a,u and an E/M channel required')
    R=4*a-n
    if n<=0 or R<=0 or R%4!=3 or gcd(n*a,R)!=1 or a*a%u:
        raise ValueError('positive unit shell and actual divisor required')
    gate=4*u+1 if c=='E' else u+a
    if gate%R:raise ValueError('original gate fails')
    d=gcd(a,u);h=d*d//u;r=u//d;s=a//d
    quotient=(n*r+s)//R if c=='E' else (r+s)//R
    den=(a,h*s*quotient,n*h*r*quotient) if c=='E' else (a,n*h*s*quotient,n*h*r*quotient)
    require(gcd(r,s)==1 and h*r*s==a and h*r*r==u,'normalization_inverse')
    require(all(t>0 for t in den) and sum((F(1,t) for t in den),F())==F(4,n),'ordered_reciprocal_identity')
    back=F((1 if c=='E' else n)*a*a,R*den[1]-n*a)
    require(back==u,'ordered_divisor_return')
    fs=factor(a);beta=[];v=u
    for q,e in fs:
        f=0
        while v%q==0:v//=q;f+=1
        beta.append(f-e)
    require(v==1,'complete_prime_exponents')
    return dict(n=n,a=a,R=R,channel=c,u=u,h=h,r=r,s=s,quotient=quotient,
                beta=beta,prime_factors=fs,denominators=den)

def enumerate_shell(n,a):
    fs=factor(a);ds=[1]
    for q,e in fs:ds=[d*q**f for d in ds for f in range(2*e+1)]
    R=4*a-n;hits=[]
    for u in sorted(ds):
        for c in ('E','M'):
            if (4*u+1 if c=='E' else u+a)%R==0:hits.append(witness(n,a,u,c))
    return dict(n=n,a=a,R=R,primality_trial_bound=isqrt(n),prime=prime(n),
                candidate_count=2*len(ds),hits=hits)

def semiring_checks():
    # Supported zero is a present dictionary key; tau is a missing key.
    sample={3:F(1),1:F(2)}
    inv={3:F(1,9),1:F(-2,9),5:F(4,9)}
    P=conv(sample,inv,6,True,True)
    require(P=={0:F(1),2:F(0),4:F(0)},'ordinary_inverse_returns_present_identity')
    require(P!={0:F(1)},'present_identity_is_not_global_identity')
    sat=conv(P,sample,6,True,True)
    require(sat=={1:F(2),3:F(1),5:F(0)},'minimal_coset_saturation')
    require(conv(P,sat,6,True,True)==sat,'internal_identity_after_saturation')
    require(conv(sat,inv,6,True,True)==P,'saturated_inverse')
    require(conv(P,P,6,True,True)==P,'support_idempotent')
    # Fourier transform and its inverse on C2, with presence retained.
    def matrix_apply(M,v):
        return {i:sum((F(a)*v[j] for j,a in enumerate(row) if a and j in v),F())
                for i,row in enumerate(M) if any(a and j in v for j,a in enumerate(row))}
    H=[[1,1],[1,-1]];Hi=[[F(1,2),F(1,2)],[F(1,2),F(-1,2)]]
    ft=matrix_apply(H,{0:F(1)});ret=matrix_apply(Hi,ft)
    require(ft=={0:F(1),1:F(1)} and ret=={0:F(1),1:F(0)},'Fourier_return_activates_present_zero')
    # Exhaust support sets and both amplitude signs on small cyclic groups.
    cases=0
    for N in range(1,7):
        masks=[{i for i in range(N) if mask>>i&1} for mask in range(1<<N)]
        for S in masks:
            for T in masks:
                A={x:(-1 if x%2 else 1) for x in S}
                B={x:0 if x%3==1 else 1 for x in T}
                C=conv(A,B,N,True,True)
                require(set(C)=={(x+y)%N for x in S for y in T},'support_product_no_cancellation')
                if set(C)=={0}:require(len(S)==len(T)==1,'unit_support_singleton_necessary')
                cases+=1
    # Nonnegative coefficient products have no zero present amplitudes.
    for N in range(2,7):
        for a,b in product(range(N),repeat=2):
            C=conv({a:1},{b:1},N,True,True)
            require(all(v>0 for v in C.values()),'positive_cone_support_faithful')
    return dict(cyclic_support_pairs=cases,target=sample,ordinary_inverse=inv,
                split_product=P,saturated_target=sat,
                type='cyclic labels 0..5, additive convolution; missing keys are tau')

def recurrence_checks(max_R):
    cases=0;cap_cases=0
    for R in range(3,max_R+1,4):
        units=[g for g in range(1,R) if gcd(g,R)==1]
        for g in units:
            o=order(g,R);H={pow(g,j,R):1 for j in range(o)}
            for e in range(2*o+3):
                for c in ('E','M'):
                    D=one(g,e,R,c)
                    require(D==distribution([g],[e],R,c,True),'periodic_linear_exact_counts')
                    require(set(D)==set(one(g,min(e,o//2),R,c)),'individual_sharp_support_cap')
                    if e>=o//2:require(set(D)==set(H),'positive_subgroup_filling')
                    # Positive rational series coefficient bijections.
                    interval=range(2*e+1) if c=='E' else range(-e,e+1)
                    for z in interval:
                        if c=='E':
                            eps=z%2;k=(z-eps)//2;j=e-k-eps
                            require(j>=0 and k>=0 and e==j+k+eps and z==2*k+eps,
                                    'exterior_positive_series_bijection')
                        else:
                            eps=(e-z)%2;j=(e-eps+z)//2;k=(e-eps-z)//2
                            require(j>=0 and k>=0 and e==j+k+eps and z==j-k,
                                    'middle_positive_series_bijection')
                    if e>=2:
                        if c=='E':A={1:1};A=plus(A,{g*g%R:1});B={g*g%R:1}
                        else:A=plus({g:1},{pow(g,-1,R):1});B={1:1}
                        rhs=plus(conv(A,one(g,e-1,R,c),R),scale(conv(B,one(g,e-2,R,c),R),-1))
                        require(D==rhs,'ordinary_amplitude_series_recurrence')
                    cases+=1
        # Every pair, actual amplitudes and capped availability, at selected budgets.
        for g,h in combinations_with_replacement(units,2):
            og,oh=order(g,R),order(h,R)
            for e,f in ((0,0),(1,2),(og//2,oh//2),(og+1,oh+2)):
                for c in ('E','M'):
                    exact=distribution([g,h],[e,f],R,c)
                    quick=distribution([g,h],[e,f],R,c,True)
                    require(exact==quick,'two_factor_unbounded_formula')
                    capped=distribution([g,h],[min(e,og//2),min(f,oh//2)],R,c)
                    require(set(exact)==set(capped),'two_factor_cap_support_not_counts')
                    cap_cases+=1
    # Same residue type: one prime square and two marked primes differ in amplitude.
    A=distribution([7],[2],27,'E');B=distribution([7,7],[1,1],27,'E')
    require(set(A)==set(B) and sum(A.values())==5 and sum(B.values())==9,
            'residue_aggregation_keeps_fibre_weights')
    return dict(single_factor_instances=cases,pair_instances=cap_cases,max_residual=max_R,
                amplitude_collision=dict(one_prime_squared=A,two_distinct_primes=B))

def pred27(A,B,c):
    if c=='E':return B>=7 or (A>=1 and B>=3) or (A>=2 and B>=1)
    return B>=9 or (A>=1 and B>=5) or (A>=2 and B>=1)

def profile_checks():
    table=[]
    for A,B in product(range(5),range(10)):
        row=dict(A=A,B=B)
        for c in ('E','M'):
            n=count([7,11],[A,B],27,c)
            require(bool(n)==pred27(A,B,c),'complete_capped_27_classifier')
            row[c]=n
        table.append(row)
    for A,B in product(range(13),range(25)):
        for c in ('E','M'):
            require(bool(count([7,11],[A,B],27,c,True))==pred27(A,B,c),'27_classifier_beyond_caps')
    minima={}
    for c in ('E','M'):
        minima[c]=[(r['A'],r['B']) for r in table if r[c] and
                   (r['A']==0 or not pred27(r['A']-1,r['B'],c)) and
                   (r['B']==0 or not pred27(r['A'],r['B']-1,c))]
    require(minima=={'E':[(0,7),(1,3),(2,1)],'M':[(0,9),(1,5),(2,1)]},'minimal_profile_antichains')
    # All integer allocations in each grouped exponent fibre, exact coefficients.
    grouped=[]
    for e1,e2 in product(range(4),repeat=2):
        coeff=Counter(i+j for i in range(2*e1+1) for j in range(2*e2+1))
        require(set(coeff)==set(range(2*(e1+e2)+1)),'grouped_box_surjectivity')
        for j,n in coeff.items():
            lo=max(0,j-2*e2);hi=min(2*e1,j)
            require(n==hi-lo+1,'grouped_box_complete_fibre')
        grouped.append([e1,e2,dict(coeff)])
    large=[]
    for A,B in [(10**12,10**12+1),(10**12+3,10**12+8),(0,10**12),(10**12,0)]:
        counts={c:count([7,11],[A,B],27,c,True) for c in ('E','M')}
        mass=(2*A+1)*(2*B+1)
        for c in ('E','M'):
            require(sum(distribution([7,11],[A,B],27,c,True).values())==mass,'large_exact_original_mass')
            require(bool(counts[c])==pred27(A,B,c),'large_profile_decision')
        large.append(dict(exponents=[A,B],one_channel_original_mass=mass,counts=counts,
                          n_symbolic=f'4*7^{A}*11^{B}-27',primality='not claimed'))
    return dict(capped_table=table,minimal_antichains=minima,grouped_fibres=grouped,large_exact_counts=large)

def full_catalogue27():
    """Complete finite reduction: 2^17 supports and 14040 positive capped profiles."""
    R=27;N=18;full=(1<<N)-1
    def rot(x,k):
        k%=N
        return ((x<<k)|(x>>(N-k)))&full
    require(order(2,R)==18,'cyclic_27_generator')
    logs=list(range(1,18));cap={j:(18//gcd(j,18))//2 for j in logs}
    def masks(js,es):
        out=[]
        for c in ('E','M'):
            W=1
            for j,e in zip(js,es):
                V=0
                for k in range(0,2*e+1) if c=='E' else range(-e,e+1):V|=rot(W,k*j)
                W=V
            out.append(W)
        return tuple(out)
    def hit(js,es):
        E,M=masks(js,es)
        return bool(E>>7&1 or M>>9&1)
    E=[1]+[0]*((1<<17)-1);M=E.copy()
    minimal=[];mixed_misses=[];allmiss=1;squaremin=0
    for S in range(1,len(E)):
        low=S&-S;j=low.bit_length();U=S-low
        E[S]=E[U]|rot(E[U],j)|rot(E[U],2*j)
        M[S]=M[U]|rot(M[U],j)|rot(M[U],-j)
        js=[i+1 for i in range(17) if S>>i&1]
        h=bool(E[S]>>7&1 or M[S]>>9&1)
        if h:
            if all(not(E[S^(1<<(j-1))]>>7&1 or M[S^(1<<(j-1))]>>9&1) for j in js):
                minimal.append((js,[1]*len(js)));squaremin+=1
        else:
            allmiss+=1
            if any(j%2 for j in js):mixed_misses.append(js)
            else:require(all(j%2==0 for j in js),'pure_even_misses_all_multiplicities')
        checks['complete_squarefree_profile_cases']+=1
    finite=0
    for js in mixed_misses:
        for es in product(*(range(1,cap[j]+1) for j in js)):
            finite+=1
            if all(e==1 for e in es) or not hit(js,es):continue
            if all(not hit(js,tuple(e-(k==i) for k,e in enumerate(es))) for i in range(len(js))):
                minimal.append((js,list(es)))
    require(Counter(map(len,mixed_misses))=={1:7,2:45,3:43,4:9},
            'five_class_forcing_and_nine_maximal_masks')
    minimal.sort(key=lambda z:(sum(z[1]),len(z[0]),z))
    catalogue=[]
    for js,es in minimal:
        gs=[pow(2,j,27) for j in js]
        require(hit(js,es),'catalogue_has_target')
        require(all(not hit(js,tuple(e-(k==i) for k,e in enumerate(es))) for i in range(len(js))),
                'catalogue_each_coordinate_is_indispensable')
        found=None
        for c in ('E','M'):
            ranges=[range(2*e+1) if c=='E' else range(-e,e+1) for e in es]
            for ex in product(*ranges):
                if prod(pow(g,z,27) for g,z in zip(gs,ex))%27==target(27,c):
                    found=dict(channel=c,coordinates=list(ex));break
            if found:break
        require(found is not None,'catalogue_marked_target_word')
        catalogue.append(dict(logarithms=js,residues=gs,capacities=es,target_word=found))
    hist=Counter(len(z[0]) for z in minimal)
    require(hist=={1:9,2:99,3:66} and len(minimal)==174,'complete_catalogue_arity_counts')
    require(max(sum(z[1]) for z in minimal)==9,'nine_occurrence_bound')
    require(allmiss==360 and len(mixed_misses)==104 and finite==14040,'coverage_reduction_sizes')
    return dict(residual=27,generator=2,log_table=[pow(2,j,27) for j in range(18)],
                squarefree_supports=1<<17,squarefree_misses=allmiss,
                mixed_squarefree_misses=mixed_misses,mixed_miss_arity_histogram=dict(Counter(map(len,mixed_misses))),positive_capped_profiles=finite,
                squarefree_minimal_hits=squaremin,minimal_profiles=catalogue,
                arity_histogram=dict(hist),max_reserved_occurrences=9)

def catalogue_witness(n,a,catalogue):
    """Select original prime occurrences; preserve all surplus factors in a."""
    fs=factor(a)
    if (4*a-n)!=27 or gcd(a,27)!=1:raise ValueError('actual residual-27 shell required')
    totals=Counter()
    for q,e in fs:totals[q%27]+=e
    for entry in catalogue:
        if not all(totals[g]>=d for g,d in zip(entry['residues'],entry['capacities'])):continue
        dvec=[0]*len(fs);coordinates=[0]*len(fs)
        c=entry['target_word']['channel']
        for g,need,z in zip(entry['residues'],entry['capacities'],entry['target_word']['coordinates']):
            rem=need
            for i,(q,e) in enumerate(fs):
                if q%27==g:
                    take=min(rem,e);dvec[i]=take;rem-=take
            require(rem==0,'reserve_actual_occurrences')
            rem=abs(z);sgn=1 if z>=0 else -1
            for i,(q,e) in enumerate(fs):
                if q%27==g:
                    take=min(rem,(2 if c=='E' else 1)*dvec[i]);coordinates[i]=sgn*take;rem-=take
            require(rem==0,'allocate_original_exponent_word')
        if c=='E':u=prod(q**j for (q,e),j in zip(fs,coordinates))
        else:u=prod(q**(e+j) for (q,e),j in zip(fs,coordinates))
        w=witness(n,a,u,c)
        w['reserved_prime_exponents']=dvec;w['catalogue_entry']=entry
        require(sum(dvec)<=9 and len({q%27 for (q,e),d in zip(fs,dvec) if d})<=3,
                'actual_witness_compression_bounds')
        return w
    return None

def hard_catalogue_scan(catalogue,bound=2000000):
    sieve=bytearray(b'\x01')*(bound+1);sieve[:2]=b'\0\0'
    for q in range(2,isqrt(bound)+1):
        if sieve[q]:sieve[q*q::q]=b'\0'*len(sieve[q*q::q])
    residues={1,121,169,289,361,529};rows=[];stats=Counter()
    for p in range(29,bound+1):
        if not sieve[p] or p%840 not in residues:continue
        a=(p+27)//4;fs=factor(a);gs=[q%27 for q,e in fs];es=[e for q,e in fs]
        counts={c:count(gs,es,27,c,True) for c in ('E','M')}
        found=catalogue_witness(p,a,catalogue)
        require((found is not None)==bool(sum(counts.values())),'complete_catalogue_on_hard_primes')
        stats['hard_primes']+=1;stats['occupied_residual_27_shells']+=found is not None
        stats['E_states']+=counts['E'];stats['M_states']+=counts['M']
        nonidentity={q%27 for q,e in fs if q%27!=1}
        five=(len(nonidentity)>=5 and any(q%3==2 for q,e in fs))
        require(not five or found is not None,'five_class_pointwise_certificate')
        stats['five_class_criterion']+=five
        rows.append(dict(p=p,a=a,counts=counts,witness=found))
    require(stats['hard_primes']==4519,'independent_hard_universe')
    return dict(bound=bound,scope='all primes in six hard classes, only R=27',counts=dict(stats),rows=rows)

def arithmetic_checks():
    examples=[enumerate_shell(3361,847),enumerate_shell(23689,5929),enumerate_shell(19489,4879)]
    require(examples[0]['hits']==[] and examples[0]['prime'],'negative_prime_shell_not_negative_prime')
    require(examples[1]['prime'] and len(examples[1]['hits'])==3,'positive_prime_shell_three_hits')
    require(examples[1]['hits'][0]['denominators']==(5929,2809041620,5211580),'small_positive_order')
    require(examples[2]['prime'] and len(examples[2]['hits'])==1,'sharp_three_class_prime')
    for absent in range(3):
        budget=[1,1,1];budget[absent]=0
        require(all(count([7,17,41],budget,27,c)==0 for c in ('E','M')),
                'every_proper_three_class_subbudget_fails')
    require(all(count([23],[8],27,c)==0 for c in ('E','M')) and
            all(count([23],[9],27,c)>0 for c in ('E','M')), 'sharp_nine_occurrence_local_bound')
    # Old labels are embedded and retain their gates/defects; only new labels hit.
    old=examples[0];a=847;t=7;R=27;newa=a*t;oldfs=factor(a)
    ds=[1]
    for q,e in oldfs:ds=[d*q**j for d in ds for j in range(2*e+1)]
    transport=[]
    for u in ds:
        for c in ('E','M'):
            newu=u if c=='E' else t*u
            g=4*u+1 if c=='E' else u+a
            newg=4*newu+1 if c=='E' else newu+newa
            require(newa*newa%newu==0,'multiplicative_extension_divisor')
            require(R//gcd(R,g)==R//gcd(R,newg),'multiplicative_extension_defect_preserved')
            transport.append(dict(channel=c,u=u,newu=newu,D=R//gcd(R,g)))
    mapped={(r['channel'],r['newu']) for r in transport}
    require(all((h['channel'],h['u']) not in mapped for h in examples[1]['hits']),'all_new_hits_need_new_source_terms')
    # All first-half shells of primes <=500, independent arbitrary-alpha check.
    scan=Counter();profile_matches=[]
    for p in range(5,501,4):
        if not prime(p):continue
        scan['primes']+=1
        for a in range((p+3)//4,(p-1)//2+1):
            R=4*a-p;fs=factor(a);gs=[q%R for q,e in fs];es=[e for q,e in fs]
            ds=[1]
            for q,e in fs:ds=[u*q**j for u in ds for j in range(2*e+1)]
            scan['shells']+=1
            for c in ('E','M'):
                h=[u for u in ds if (4*u+1 if c=='E' else u+a)%R==0]
                fast=count(gs,es,R,c,True)
                require(fast==len(h),'all_small_original_shell_counts')
                scan['canonical_candidates']+=len(ds);scan['hits']+=len(h)
                for u in h:witness(p,a,u,c)
    return dict(examples=examples,old_source_transport=transport,scan=dict(scan))

def controls():
    out=[]
    def reject(label,fn):
        try:fn()
        except (ArithmeticError,ValueError):out.append(label);return
        raise ArithmeticError('negative control accepted '+label)
    reject('supported-zero inverse identified with global unit',lambda:require(
        conv({3:F(1),1:F(2)},{3:F(1,9),1:F(-2,9),5:F(4,9)},6,True,True)=={0:F(1)},'false_global_inverse'))
    reject('saturation preserves original coefficients',lambda:require(one(7,20,27,'E')==one(7,4,27,'E'),'false_mass_cap'))
    reject('two distinct same-residue primes counted as one squared prime',lambda:require(
        distribution([7,7],[1,1],27,'E')==one(7,2,27,'E'),'false_residue_count'))
    reject('known empty shell labelled hit',lambda:witness(3361,847,11,'M'))
    reject('nonunit generator admitted',lambda:order(3,27))
    return out

def enc(o):
    if isinstance(o,F):return {'numerator':o.numerator,'denominator':o.denominator}
    if isinstance(o,dict):return {str(k):enc(v) for k,v in o.items()}
    if isinstance(o,(tuple,list)):return [enc(v) for v in o]
    return o

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out',default='certificates');ap.add_argument('--max-residual',type=int,default=31)
    args=ap.parse_args()
    if args.max_residual<3:ap.error('--max-residual >=3 required')
    dest=Path(args.out);dest.mkdir(parents=True,exist_ok=True)
    catalogue=full_catalogue27()
    data=dict(catalogue27=catalogue,hard_scan=hard_catalogue_scan(catalogue['minimal_profiles']),
              split_scalar=semiring_checks(),recurrences=recurrence_checks(args.max_residual),
              profiles=profile_checks(),arithmetic=arithmetic_checks(),negative_controls=controls())
    for name,obj in data.items():(dest/(name+'.json')).write_text(json.dumps(enc(obj),indent=2,sort_keys=True)+'\n')
    (dest/'checks.json').write_text(json.dumps(dict(checks),indent=2,sort_keys=True)+'\n')
    print(json.dumps({'checks':sum(checks.values()),'scan':data['arithmetic']['scan'],
                      'negative_controls':len(data['negative_controls'])},sort_keys=True))
if __name__=='__main__':main()
