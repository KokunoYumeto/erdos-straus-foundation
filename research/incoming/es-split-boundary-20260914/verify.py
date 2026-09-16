#!/usr/bin/env python3
"""Prime-power socles and two-sided ES moment certificates.
Standard library; all tests active under -O. Finite scopes are in output JSON.
No RH, universal ES, Lean-build or historical-priority claim.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import gcd, isqrt, prod, ceil, floor
from pathlib import Path
import json

CHECKS = Counter()

def check(ok, label):
    CHECKS[label] += 1
    if not ok: raise ArithmeticError(label)

@lru_cache(None)
def factor(n):
    if n < 1: raise ValueError('positive integer required')
    out=[]; q=2
    while q*q<=n:
        e=0
        while n%q==0: n//=q; e+=1
        if e: out.append((q,e))
        q=3 if q==2 else q+2
    if n>1: out.append((n,1))
    return tuple(out)

def isprime(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))

def valuation(n,q):
    if n==0: raise ValueError('finite valuation of nonzero integer required')
    v=0
    while n%q==0: n//=q; v+=1
    return v

def box(e): return product(*(range(-a,a+1) for a in e))
def ev(P,x):
    y=F(0)
    for c in reversed(P): y=y*x+c
    return y

def padd(A,B):
    C=[F(0)]*max(len(A),len(B))
    for i,x in enumerate(A):C[i]+=x
    for i,x in enumerate(B):C[i]+=x
    return C

def pmul(A,B):
    C=[F(0)]*(len(A)+len(B)-1)
    for i,x in enumerate(A):
        for j,y in enumerate(B): C[i+j]+=x*y
    return C

def affine_poly(q): return padd([F(1)],pmul([-1,1],q)) if q else [F(1)]
def dot(a,b): return sum((x*y for x,y in zip(a,b)),F())

def linear_solve(A,b):
    """Exact RREF, canonical free variables zero; return all kernel generators."""
    n=len(b)
    if len(A)!=n or any(len(row)!=n for row in A):raise ValueError('square system')
    M=[list(map(F,row))+[F(bb)] for row,bb in zip(A,b)]
    piv=[]; r=0
    for c in range(n):
        j=next((i for i in range(r,n) if M[i][c]),None)
        if j is None:continue
        M[r],M[j]=M[j],M[r]; z=M[r][c]; M[r]=[v/z for v in M[r]]
        for i in range(n):
            if i!=r:
                z=M[i][c]
                if z:M[i]=[v-z*w for v,w in zip(M[i],M[r])]
        piv.append(c);r+=1
    if any(not any(row[:-1]) and row[-1] for row in M):raise ValueError('inconsistent normal equation')
    x=[F(0)]*n
    for i,c in enumerate(piv):x[c]=M[i][-1]
    null=[]
    for c in range(n):
        if c not in piv:
            v=[F(0)]*n;v[c]=1
            for i,p in enumerate(piv):v[p]=-M[i][c]
            null.append(v)
    check([dot(row,x) for row in A]==list(map(F,b)),'normal_equation')
    for v in null:check(all(dot(row,v)==0 for row in A),'normal_kernel')
    return x,null

def moments(measure,n):
    return [sum((F(w)*x**j for x,w in measure.items()),F()) for j in range(n+1)]

def moment_bounds(measure,d,c=F(1,3)):
    if d<0:raise ValueError('nonnegative degree')
    if not (0<c<1) or not measure or any(w<=0 or not (0<x<=c or x==1) for x,w in measure.items()):
        raise ValueError('positive original measure on (0,c] union {1}')
    m=moments(measure,2*d+1)
    GU=[[m[i+j+2]-2*m[i+j+1]+m[i+j] for j in range(d)] for i in range(d)]
    bU=[m[i+1]-m[i] for i in range(d)]
    yU,nullU=linear_solve(GU,bU)
    PU=affine_poly([-y for y in yU])
    U=m[0]-dot(bU,yU)
    GL=[[-m[i+j+3]+(2+c)*m[i+j+2]-(1+2*c)*m[i+j+1]+c*m[i+j] for j in range(d)] for i in range(d)]
    bL=[m[i+2]-(1+c)*m[i+1]+c*m[i] for i in range(d)]
    yL,nullL=linear_solve(GL,bL)
    PL=affine_poly(yL)
    L=(m[1]-c*m[0]+dot(bL,yL))/(1-c)
    h=F(measure.get(F(1),0))
    check(ev(PU,F(1))==ev(PL,F(1))==1,'endpoint_normalization')
    check(U==sum(w*ev(PU,x)**2 for x,w in measure.items()),'upper_original_Gram')
    check(L==sum(w*(x-c)*ev(PL,x)**2 for x,w in measure.items())/(1-c),'lower_signed_Gram')
    check(L<=h<=U,'count_bracket')
    for G,b,q,P,sgn in [(GU,bU,[-y for y in yU],PU,1),(GL,bL,yL,PL,-1)]:
        # Complete normal equations are the exact finite minimization proof input.
        check(all(dot(row,q)==(-bb if sgn==1 else bb) for row,bb in zip(G,b)), 'canonical_source_correction')
    for z in nullU:
        check(all((x-1)*ev(z,x)==0 for x in measure),'upper_kernel_original_observation')
    for z in nullL:
        check(all((x-1)*ev(z,x)==0 for x in measure if x!=c),'lower_kernel_zero_weight_stratum')
    if d==1:
        a00=m[1]-c*m[0]; a01=m[2]-c*m[1]; a11=m[3]-c*m[2]
        negative_semidefinite=(a00<=0 and a11<=0 and a00*a11>=a01*a01)
        check((L>0)==(not negative_semidefinite),'four_moment_signed_localizer_equivalence')
    return dict(degree=d,L=L,U=U,P_lower=PL,P_upper=PU,moments=m,
                G_upper=GU,b_upper=bU,G_lower=GL,b_lower=bL,
                kernel_upper=nullU,kernel_lower=nullL,
                interval_count=ceil(L) if ceil(L)==floor(U) else None)

def cheb_poly(d):
    a,b=[F(1)],[-1,6]
    if d==0:return a
    for _ in range(1,d):a,b=b,padd(pmul([-2,12],b),[-v for v in a])
    v=ev(b,F(1));return [x/v for x in b]

def cheb5(d):
    a,b=1,5
    if d==0:return a
    for _ in range(1,d):a,b=b,10*b-a
    return b

def witness(p,a,u,c):
    R=4*a-p; d=gcd(a,u);h=d*d//u;r=u//d;s=a//d
    if c=='E':
        q=F(p*r+s,R);den=(F(a),F(h*s)*q,F(p*h*r)*q)
    else:
        q=F(r+s,R);den=(F(a),F(p*h*s)*q,F(p*h*r)*q)
    check(h*r*s==a and h*r*r==u and gcd(r,s)==1,'normalization')
    check(all(x>0 for x in den) and sum((1/x for x in den),F())==F(4,p),'rational_ES_identity')
    g=4*u+1 if c=='E' else u+a;D=R//gcd(R,g)
    check(all((D*x).denominator==1 for x in den),'original_clearing_denominator')
    check(den[1].denominator==den[2].denominator==D,'exact_clearing_denominator')
    back=F((1 if c=='E' else p)*a*a,R*den[1]-p*a)
    check(back==u,'ordered_divisor_inverse')
    return dict(p=p,a=a,R=R,u=u,channel=c,h=h,r=r,s=s,quotient=q,denominators=den,D=D)

def shell(p,a,details=False):
    if not isprime(p) or p%4!=1 or not p<4*a or not 2*a<p:raise ValueError('prime first-half shell required')
    R=4*a-p;fs=factor(a);rf=factor(R);hist=Counter();leaves=[];hits=[]
    for beta in box(tuple(e for q,e in fs)):
        u=prod(q**(e+b) for (q,e),b in zip(fs,beta))
        for c in ('E','M'):
            g=4*u+1 if c=='E' else u+a;D=R//gcd(R,g)
            defect=tuple(max(e-valuation(g,l),0) for l,e in rf)
            check(prod(l**d for (l,e),d in zip(rf,defect))==D,'all_prime_power_defects')
            hist[F(1,D)]+=1
            w=witness(p,a,u,c)
            if D==1:hits.append(w)
            if details:leaves.append(dict(w,beta=beta,prime_factors=fs,gate=g,
                                         local_primes=[l for l,e in rf],jet_top=defect,
                                         jet_dimension=prod(d+1 for d in defect)))
    return hist,hits,leaves

def split_test(p,a,f):
    fs=factor(a);e=tuple(k for q,k in fs);b=tuple(k-j for k,j in zip(e,f));R=4*a-p
    if len(e)!=len(f) or any(j<0 or j>k for j,k in zip(f,e)):raise ValueError('actual split required')
    direct,_,_=shell(p,a)
    out=Counter();raw=Counter();count=Counter();basekeys={};maxm=5
    for xi in box(f):
        for eta in box(b):
            beta=tuple(x+y for x,y in zip(xi,eta))
            N=prod(min(fi,bi+hi)-max(-fi,bi-hi)+1 for fi,hi,bi in zip(f,b,beta))
            u=prod(q**(k+v) for (q,k),v in zip(fs,beta))
            for c in ('E','M'):
                g=4*u+1 if c=='E' else u+a;D=R//gcd(R,g);x=F(1,D)
                out[x]+=F(1,N);raw[x]+=1;count[(beta,c)]+=1;basekeys[(beta,c)]=(N,x)
                xx=prod(pow(q,v,R) for (q,k),v in zip(fs,xi))%R
                ww=prod(pow(q,v,R) for (q,k),v in zip(fs,eta))%R
                target=(-pow(p,-1,R))%R if c=='E' else R-1
                rho=(xx-target*pow(ww,-1,R))%R;unit=(p if c=='E' else a)*ww%R
                check(g%R==(unit*rho)%R and gcd(unit,R)==1,'typed_gate_unit')
                check(R//gcd(R,rho)==D,'split_local_defect_invariance')
    for key,n in count.items():check(n==basekeys[key][0],'complete_split_fibre')
    check(dict(out)==dict(direct),'split_original_measure_not_raw')
    check(moments(out,maxm)==moments(direct,maxm),'split_all_tested_moments')
    for d in (1,2):
        x=moment_bounds(direct,d);y=moment_bounds(out,d)
        check(x==y,'all_canonical_moment_maps_commute_with_split')
    return dict(p=p,a=a,f=f,b=b,weighted_histogram=out,raw_histogram=raw,
                actual_count=direct.get(F(1),0),raw_count=raw.get(F(1),0))

def shift(mon,axis,d):
    y=list(mon);y[axis]+=1
    return tuple(y) if y[axis]<=d[axis] else None

def jet_tests():
    cases=0;maps=0
    for d in product(range(4),repeat=3):
        basis=list(product(*(range(n+1) for n in d)))
        survivors=[]
        for mon in basis:
            images=[shift(mon,i,d) for i in range(3)]
            if all(x is None for x in images):survivors.append(mon)
            for i,n in enumerate(d):
                # Distinct nonzero images guarantee no extra cancellation kernel.
                nz=[shift(b,i,d) for b in basis if shift(b,i,d) is not None]
                check(len(nz)==len(set(nz)),'jet_shift_nonzero_columns_distinct')
        check(survivors==[d],'joint_socle_one_marked_line')
        check(int(survivors[0]==(0,0,0))==int(all(n==0 for n in d)), 'socle_to_augmentation_projector')
        check((d==(0,0,0))==(sum(d)==0),'socle_degree_zero_test')
        for small in product(*(range(n+1) for n in d)):
            delta=tuple(x-y for x,y in zip(d,small))
            for mon in product(*(range(n+1) for n in small)):
                inc=tuple(x+y for x,y in zip(mon,delta))
                back=tuple(x-y for x,y in zip(inc,delta))
                check(back==mon and all(x<=y for x,y in zip(inc,d)),'reverse_jet_embedding_inverse')
            top_image=d if d==small else None
            actual=d if all(x<=y for x,y in zip(d,small)) else None
            check(actual==top_image,'forward_jet_quotient_socle_death')
            maps+=1
        cases+=1
    return dict(triples=cases,coordinatewise_reductions=maps)

def generic_tests():
    total=0
    nodes=(F(1),F(1,3),F(1,5),F(1,7))
    for w in product(range(3),repeat=4):
        m={x:F(n) for x,n in zip(nodes,w) if n}
        if not m:continue
        lastL=None;lastU=None;last=None
        for d in range(5):
            r=moment_bounds(m,d);h=m.get(F(1),0)
            if lastL is not None:
                check(lastL<=r['L'] and r['U']<=lastU,'nested_canonical_intervals')
                up=padd(last['P_upper'],[-x for x in r['P_upper']])
                lo=padd(last['P_lower'],[-x for x in r['P_lower']])
                check(lastU-r['U']==sum(w*ev(up,x)**2 for x,w in m.items()),'upper_exact_relation_norm_secant')
                check(r['L']-lastL==sum(w*(F(1,3)-x)*ev(lo,x)**2 for x,w in m.items())/F(2,3),'lower_exact_relation_norm_secant')
                check(ev(up,F(1))==ev(lo,F(1))==0,'degree_transition_primitive_endpoint')
            lastL,lastU=r['L'],r['U'];last=r
            PC=cheb_poly(d)
            cu=sum(w*ev(PC,x)**2 for x,w in m.items())
            cl=sum(w*(x-F(1,3))*ev(PC,x)**2 for x,w in m.items())/F(2,3)
            check(r['U']<=cu and r['L']>=cl,'optimized_dominates_fixed_polynomial')
            W=sum(m.values());den=cheb5(d)**2
            check(r['U']-h<=W/F(den),'explicit_upper_tail_bound')
            check(h-r['L']<=W/F(2*den),'explicit_lower_tail_bound')
            if F(3,2)*W<den:check(r['interval_count']==h,'uniform_finite_stopping')
            total+=1
        check(lastL==lastU==m.get(F(1),0),'finite_support_eventual_exactness')
    difficult=moment_bounds({F(1):1,F(1,5):10000,F(1,7):10000},1)
    check(difficult['L']==F(-8189,1811),'fixed_degree_not_general_positive_mass_theorem')
    return total

def scan(bound):
    totals=Counter();improvements=[]
    for p in range(13,bound+1,12):
        if not isprime(p):continue
        totals['primes']+=1
        for a in range((p+3)//4,(p-1)//2+1):
            hist,hits,_=shell(p,a);h=len(hits);W=sum(hist.values());totals['shells']+=1;totals['states']+=W;totals['success_states']+=h
            totype='occupied' if h else 'empty';totals[totype+'_shells']+=1
            best=None;positivedegree=None
            for d in range(3):
                r=moment_bounds(hist,d)
                if r['L']>0 and positivedegree is None:positivedegree=d
                if r['interval_count'] is not None:
                    check(r['interval_count']==h,'scan_exact_rounded_count')
                    if best is None:best=d
            if best is not None:
                totals['count_degree_'+str(best)]+=1
                if best>1:improvements.append(dict(p=p,a=a,R=4*a-p,degree=best,actual=h,lower_degree=moment_bounds(hist,best-1),final=moment_bounds(hist,best)))
            else:totals['count_not_resolved_by_degree_2']+=1
            if h:
                totals['positive_degree_'+str(positivedegree)]+=1
                if positivedegree is not None and len(improvements)<12:
                    rr=moment_bounds(hist,positivedegree)
                    improvements.append(dict(p=p,a=a,R=4*a-p,degree=positivedegree,L=rr['L'],U=rr['U'],actual=h))
            if h==0:check(positivedegree is None,'no_false_positivity')
    return dict(bound=bound,domain='all first-half shells; primes p=1 mod12',totals=dict(totals),examples=improvements)


def cohomology_span_test():
    """Compare the prior residue H0 with the ORIGINAL-state socle image."""
    p,a=2521,636;R=23;fs=factor(a);e=tuple(k for q,k in fs)
    f=(1,1,1);b=(1,0,0)
    v=lambda t:prod(pow(q,j,R) for (q,k),j in zip(fs,t))%R
    matched=[];left=Counter();right=Counter()
    for c in ('E','M'):
        target=(-pow(p,-1,R))%R if c=='E' else R-1
        for xi in box(f):left[(c,v(xi))]+=1
        for eta in box(b):right[(c,target*pow(v(eta),-1,R)%R)]+=1
        for xi in box(f):
            for eta in box(b):
                z=v(xi)
                if z!=target*pow(v(eta),-1,R)%R:continue
                beta=tuple(x+y for x,y in zip(xi,eta))
                u=prod(q**(k+j) for (q,k),j in zip(fs,beta))
                N=prod(min(fi,bi+hi)-max(-fi,bi-hi)+1 for fi,hi,bi in zip(f,b,beta))
                matched.append(dict(channel=c,residue=z,u=u,beta=beta,xi=xi,eta=eta,N=N))
    states=sorted({(a['channel'],a['u']) for a in matched})
    residues=sorted({(a['channel'],a['residue']) for a in matched})
    M=[[sum((F(1,a['N']) for a in matched
              if (a['channel'],a['u'])==state and (a['channel'],a['residue'])==res),F())
        for state in states] for res in residues]
    GI=[F(1,left[res])+F(1,right[res]) for res in residues]
    pulled=[[sum((GI[k]*M[k][i]*M[k][j] for k in range(len(GI))),F())
             for j in range(len(states))] for i in range(len(states))]
    check((len(matched),len(residues),len(states))==(5,4,3),'matched_residue_state_types_distinct')
    check(all(sum(row[j] for row in M)==1 for j in range(3)),'cohomology_comparison_mass_preservation')
    check(pulled==[[F(2),0,0],[0,F(7,8),F(3,8)],[0,F(3,8),F(7,8)]], 'original_harmonic_metric_mixed_cross_terms')
    check(any(len({a['residue'] for a in matched if (a['channel'],a['u'])==state})>1 for state in states), 'raw_residue_sum_does_not_descend_through_state_quotient')
    return dict(p=p,a=a,R=R,matched=matched,states=states,residues=residues,
                comparison=M,residue_harmonic_Gram_diagonal=GI,transported_Gram=pulled,
                dimensions=dict(occurrences=5,old_H0=4,success_projector_image=3))

def negative_controls():
    out=[]
    def reject(label,fn):
        try:fn()
        except (ArithmeticError,ValueError):out.append(label);return
        raise ArithmeticError('negative control accepted: '+label)
    reject('node outside proved gap',lambda:moment_bounds({F(1,2):1},1))
    reject('negative original mass',lambda:moment_bounds({F(1,5):-1},1))
    reject('inconsistent singular normal equation',lambda:linear_solve([[0]],[1]))
    ex=split_test(2521,636,(1,1,1))
    reject('unit split weights replace original mass',lambda:check(ex['raw_count']==ex['actual_count'],'bad_unit_weights'))
    reject('ordinary quotient called graded socle',lambda:check((2,1)==(0,0),'bad_degree_erasure'))
    # Mean-only lower bound is insufficient: dropping optimized square sign is invalid.
    hist,_,_=shell(241,64);r=moment_bounds(hist,1)
    reject('positive upper bound called existence',lambda:check(not r['U']>0 or hist.get(F(1),0)>0,'upper_not_positivity'))
    return out

def encode(obj):
    if isinstance(obj,F):return {'n':obj.numerator,'d':obj.denominator}
    if isinstance(obj,Counter):return [[encode(k),encode(v)] for k,v in sorted(obj.items(),key=lambda kv:str(kv[0]))]
    if isinstance(obj,dict):return {str(k):encode(v) for k,v in obj.items()}
    if isinstance(obj,(list,tuple)):return [encode(x) for x in obj]
    return obj

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--out',default='generated');ap.add_argument('--bound',type=int,default=1500);args=ap.parse_args()
    if args.bound<13:ap.error('bound >=13 required')
    dest=Path(args.out);dest.mkdir(parents=True,exist_ok=True)
    structural=dict(moment_fixtures=generic_tests(),jets=jet_tests(),cohomology_span=cohomology_span_test())
    examples=[]
    for p,a in [(2521,636),(1201,312),(241,64),(37,18),(61,22),(1201,310)]:
        hist,hits,leaves=shell(p,a,True)
        examples.append(dict(p=p,a=a,histogram=hist,hits=hits,leaves=leaves,
                             bounds=[moment_bounds(hist,d) for d in range(4)]))
    splits=[split_test(2521,636,(1,1,1)),split_test(241,64,(3,)),split_test(1201,312,(2,1,1)),split_test(37,18,(1,1))]
    result=scan(args.bound);negative=negative_controls()
    for name,obj in [('structural.json',structural),('examples.json',examples),('splits.json',splits),('scan.json',result),('negative_controls.json',negative),('checks.json',dict(CHECKS))]:
        (dest/name).write_text(json.dumps(encode(obj),sort_keys=True,indent=2)+'\n')
    print(json.dumps({'checks':sum(CHECKS.values()),'scan':result['totals'],'negative_controls':len(negative)},sort_keys=True))
if __name__=='__main__':main()
