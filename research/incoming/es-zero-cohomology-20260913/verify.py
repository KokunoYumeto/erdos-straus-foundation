#!/usr/bin/env python3
"""Supported cohomology and arithmetic weights for finite ES divisor boxes.

Standard library only. Explicit checks stay active under python -O.
No analytic theta, RH, universal ES, historical-priority or Lean claim.
"""
from __future__ import annotations
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product
from math import gcd, isqrt, prod
from pathlib import Path
import argparse, hashlib, json

CHECKS = Counter()

def require(ok, name):
    CHECKS[name] += 1
    if not ok:
        raise ArithmeticError(name)

def factors(n):
    if n < 1: raise ValueError('positive integer required')
    q, out = 2, []
    while q*q <= n:
        e = 0
        while n%q == 0: n//=q; e+=1
        if e: out.append((q,e))
        q = 3 if q == 2 else q+2
    if n > 1: out.append((n,1))
    return tuple(out)

def prime(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))

def box(b): return tuple(product(*(range(-e,e+1) for e in b)))
def add(x,y): return tuple(a+b for a,b in zip(x,y))
def residue(q,b,R): return prod(pow(p,e,R) for p,e in zip(q,b))%R

def fibre_bounds(beta,f,b):
    return tuple((max(-fi,bi-hi),min(fi,bi+hi)) for bi,fi,hi in zip(beta,f,b))

def fibre_size(beta,f,b):
    return prod(hi-lo+1 for lo,hi in fibre_bounds(beta,f,b))

def transpose(A):
    return [list(c) for c in zip(*A)] if A and A[0] else []

def dot(x,y): return sum((a*b for a,b in zip(x,y)),F())
def gram(columns, weights=None):
    if not columns: return []
    if weights is None: weights=[F(1)]*len(columns[0])
    return [[sum((h*x*y for h,x,y in zip(weights,a,b)),F()) for b in columns] for a in columns]

def rank(A):
    if not A: return 0
    a=[list(map(F,row)) for row in A]; nr,nc=len(a),len(a[0]); r=0
    for c in range(nc):
        piv=next((i for i in range(r,nr) if a[i][c]),None)
        if piv is None: continue
        a[r],a[piv]=a[piv],a[r]
        z=a[r][c]; a[r]=[x/z for x in a[r]]
        for i in range(r+1,nr):
            z=a[i][c]
            if z: a[i]=[x-z*y for x,y in zip(a[i],a[r])]
        r+=1
        if r==nr: break
    return r

def determinant(A):
    if not A: return F(1)
    a=[list(map(F,row)) for row in A]; n=len(a); val=F(1)
    require(all(len(r)==n for r in a),'square_determinant_domain')
    for c in range(n):
        piv=next((i for i in range(c,n) if a[i][c]),None)
        if piv is None: return F(0)
        if piv!=c: a[c],a[piv]=a[piv],a[c]; val=-val
        z=a[c][c]; val*=z
        for i in range(c+1,n):
            k=a[i][c]/z
            for j in range(c+1,n): a[i][j]-=k*a[c][j]
    return val

def evec(n,i,value=1):
    a=[F(0)]*n; a[i]=F(value); return a

def partition(mapping):
    p=defaultdict(list)
    for i,g in enumerate(mapping): p[g].append(i)
    return dict(p)

def cohomology(left,right,ambient,weight=None,full=False):
    """C[-1]=fibre-differences, C[0]=Q^left + Q^right, C[1]=Q^ambient."""
    m,n=len(left),len(right); size=m+n
    weight=list(map(F, weight if weight is not None else [1]*size))
    if len(weight)!=size or any(w<=0 for w in weight): raise ValueError('positive diagonal Gram')
    lp,rp=partition(left),partition(right)
    shared=sorted(set(lp)&set(rp)); union=set(lp)|set(rp)
    require(union<=set(ambient),'cochain_map_domain')
    if not full:
        # Proven fibre formulas; dense basis/rank/determinant tests are run in
        # the exhaustive generic fixtures and in the four explicit examples.
        diagonal=[]
        for g in shared:
            A=sum((1/weight[i] for i in lp[g]),F())
            B=sum((1/weight[m+j] for j in rp[g]),F())
            diagonal.append(1/A+1/B)
        rel=m-len(lp)+n-len(rp)
        require(rel+len(shared)+len(union)==size,'dimension_exact_sequence_formula')
        return {'dimensions':{'Cminus1':rel,'C0':size,'C1':len(ambient),
                              'Hminus1':0,'H0':len(shared),'H1':len(set(ambient)-union)},
                'shared':shared,'Gram_diagonal':diagonal,
                'left_counts':[[g,len(lp[g])] for g in sorted(lp)],
                'right_counts':[[g,len(rp[g])] for g in sorted(rp)],
                'quotient_determinant':prod(diagonal),'source_mass':sum(weight),
                'harmonic_columns':None,'boundary_columns':None,
                'verification_mode':'proved_fibre_formulas; not dense rank replay'}
    boundaries=[]; descriptors=[]
    for side,p,offset in [('L',lp,0),('R',rp,m)]:
        for g,inds in sorted(p.items()):
            for i in inds[1:]:
                v=evec(size,offset+i); v[offset+inds[0]]-=1
                boundaries.append(v);descriptors.append((side,g,i,inds[0]))
    d0=[]
    for g in ambient:
        d0.append([F(x==g) for x in left]+[-F(y==g) for y in right])
    for b in boundaries:
        require(all(dot(row,b)==0 for row in d0),'d_squared_zero')
    harmonic=[];references=[];diagonal=[]
    for g in shared:
        L,R=lp[g],rp[g]
        A=sum((1/weight[i] for i in L),F());B=sum((1/weight[m+j] for j in R),F())
        h=[F(0)]*size
        for i in L: h[i]=1/(weight[i]*A)
        for j in R: h[m+j]=1/(weight[m+j]*B)
        c=evec(size,L[0]);c[m+R[0]]+=1
        harmonic.append(h);references.append(c);diagonal.append(1/A+1/B)
        require(all(dot(row,h)==0 for row in d0),'canonical_lift_is_cycle')
        for b in boundaries:
            require(sum((wi*hi*bi for wi,hi,bi in zip(weight,h,b)),F())==0,
                    'canonical_lift_original_Gram_orthogonal')
        # Exact boundary primitive of reference - harmonic.
        diff=[x-y for x,y in zip(c,h)]
        primitive=[diff[(0 if side=='L' else m)+i] for side,_,i,_ in descriptors]
        back=[sum((v[j]*coef for v,coef in zip(boundaries,primitive)),F()) for j in range(size)]
        require(back==diff,'reference_correction_actual_boundary_primitive')
    require(gram(harmonic,weight)==[[diagonal[i] if i==j else F(0)
                                    for j in range(len(shared))] for i in range(len(shared))],
            'canonical_cohomology_Gram')
    require(len(boundaries)+len(shared)+len(union)==size,'dimension_exact_sequence')
    require(rank(d0)==len(union),'differential_rank')
    if full:
        require(rank(transpose(boundaries))==len(boundaries),'incoming_injective')
        source=gram(references+boundaries,weight)
        relation=gram(boundaries,weight)
        require(determinant(source)==determinant(relation)*prod(diagonal),
                'source_relation_quotient_determinant')
    return {'dimensions':{'Cminus1':len(boundaries),'C0':size,'C1':len(ambient),
                          'Hminus1':0,'H0':len(shared),'H1':len(set(ambient)-union)},
            'shared':shared,'Gram_diagonal':diagonal,
            'left_counts':[[g,len(lp[g])] for g in sorted(lp)],
            'right_counts':[[g,len(rp[g])] for g in sorted(rp)],
            'quotient_determinant':prod(diagonal),'source_mass':sum(weight),
            'harmonic_columns':harmonic if full else None,
            'boundary_columns':boundaries if full else None}

def witness(p,a,q,e,beta,c):
    R=4*a-p;u=prod(x**(ei+bi) for x,ei,bi in zip(q,e,beta)); d=gcd(a,u)
    h,r,s=d*d//u,u//d,a//d
    require(h*r*s==a and h*r*r==u and gcd(r,s)==1,'normalization')
    if c=='M':
        numerator=r+s; require(numerator%R==0,'middle_gate'); k=numerator//R
        den=(a,p*h*s*k,p*h*r*k)
    else:
        numerator=p*r+s; require(numerator%R==0,'exterior_gate'); k=numerator//R
        den=(a,h*s*k,p*h*r*k)
    require(sum((F(1,x) for x in den),F())==F(4,p),'positive_ES_identity')
    back=F((p if c=='M' else 1)*a*a,R*den[1]-p*a)
    require(back==u,'ordered_divisor_inverse')
    return dict(p=p,a=a,R=R,beta=list(beta),u=u,h=h,r=r,s=s,channel=c,
                quotient=k,denominators=list(den))

def affine(v,g,R):
    x,y,z=v
    return tuple(tuple(c%R for c in out) for out in
                 [(6*g+y,-6*g-x-y,z-2*g+x),(-y,x-6*g,z+3*g+y),(x,y+x,z-g)])

def shell(p,a,f,details=False):
    if not(prime(p) and p%4==1 and p<4*a and 2*a<p): raise ValueError('prime first-half shell')
    fe=factors(a);q=tuple(x for x,e in fe);e=tuple(k for x,k in fe);f=tuple(f)
    if len(f)!=len(e) or not all(0<=x<=y for x,y in zip(f,e)): raise ValueError('budget')
    b=tuple(x-y for x,y in zip(e,f)); X,Y=box(f),box(b);R=4*a-p
    ambient=[g for g in range(1,R) if gcd(g,R)==1]
    original={};allrecords=[];cdata={}
    for c,t in [('M',R-1),('E',(-pow(p,-1,R))%R)]:
        original_c={};count_lift=Counter();norm_weight=defaultdict(F);full_defect=Counter()
        for beta in box(e):
            u=prod(x**(ei+bi) for x,ei,bi in zip(q,e,beta));gate=u+a if c=='M' else 4*u+1
            D=R//gcd(R,gate);full_defect[(beta,D)]+=1
            if D==1: original_c[beta]=witness(p,a,q,e,beta,c)
        left=[residue(q,x,R) for x in X];right=[t*pow(residue(q,y,R),-1,R)%R for y in Y]
        co=cohomology(left,right,ambient,full=details and len(X)+len(Y)<=60)
        refined=defaultdict(F);pairdefect=defaultdict(F);pairs=[]
        for xi,x in zip(X,left):
            for eta,target in zip(Y,right):
                beta=add(xi,eta);n=fibre_size(beta,f,b);w=residue(q,eta,R)
                rho=(x-target)%R;u=prod(z**(ei+bi) for z,ei,bi in zip(q,e,beta))
                gate=u+a if c=='M' else 4*u+1;unit=(a*w if c=='M' else p*w)%R
                require(gcd(unit,R)==1 and gate%R==unit*rho%R,'gate_unit_exact')
                D=R//gcd(R,gate)
                require(D==R//gcd(R,rho),'all_prime_power_defects_retained')
                pairdefect[(beta,D)]+=F(1,n)
                count_lift[beta]+=1;norm_weight[beta]+=F(1,n)
                if details:
                    for v in ((0,0,0),(1,0,0),(0,1,0),(0,0,1)):
                        lhs=affine(tuple(unit*k%R for k in v),gate,R)
                        rhs=tuple(tuple(unit*k%R for k in out) for out in affine(v,rho,R))
                        require(lhs==rhs,'actual_affine_conjugacy')
                if x==target:
                    refined[beta]+=F(1,n)
                    pairs.append({'channel':c,'residue':x,'xi':xi,'eta':eta,'beta':beta,
                                  'u':u,'fibre_size':n,'canonical_count_weight':F(1,n)})
        require(pairdefect==full_defect,'complete_defect_polynomial_identity')
        require(set(count_lift)==set(box(e)),'no_exponent_lost')
        for beta in box(e):
            require(count_lift[beta]==fibre_size(beta,f,b),'actual_split_fibre_count')
            require(norm_weight[beta]==1,'all_original_weights_recovered')
        require(refined=={beta:F(1) for beta in original_c},'exact_canonical_state_polynomial')
        require(bool(co['dimensions']['H0'])==bool(original_c),'cohomology_positivity_iff_ES_shell')
        require(sum(refined.values())==len(original_c),'states_not_matching_pairs')
        cdata[c]={'raw_matches':len(pairs),'cohomology':co,'weighted_original_count':sum(refined.values()),
                  'witnesses':list(original_c.values())}
        if details:cdata[c]['matched_lifts']=pairs
        original[c]=original_c
    return {'p':p,'a':a,'R':R,'primes':q,'full_budget':e,'retained':f,'removed':b,
            'channels':cdata}

def generic_tests():
    ncases=0
    # All two-source maps of size at most two to three labels: 13^2 cases.
    maps=[x for n in range(3) for x in product(range(3),repeat=n)]
    for L in maps:
        for R in maps:
            cohomology(L,R,list(range(3)),full=True)
            cohomology(L,R,list(range(3)),weight=[i+1 for i in range(len(L)+len(R))],full=True)
            ncases+=1
    # Larger unequal, weighted fibres.
    for m in range(1,7):
        for n in range(1,7):
            cohomology([0]*m,[0]*n,[0,1],full=True)
            cohomology([0]*m,[0]*n,[0,1],weight=[F(i+2,i+1) for i in range(m+n)],full=True)
    # Full source/quotient inverse and diagonal metric changes for all small splits.
    split_cases=0
    for e in product(range(3),repeat=2):
        for f in product(*(range(k+1) for k in e)):
            b=tuple(x-y for x,y in zip(e,f));fib=defaultdict(list)
            for i,(xi,eta) in enumerate(product(box(f),box(b))):fib[add(xi,eta)].append((i,xi,eta))
            for beta,occ in fib.items():
                N=fibre_size(beta,f,b); require(N==len(occ),'weight_fibre_formula')
                a=[F((i%7)-3,i%3+1) for i,_,_ in occ];c=sum(a,F());r=[c/N]*N
                rem=[x-y for x,y in zip(a,r)]
                require(sum(rem,F())==0,'retained_boundary_sum')
                require(sum((x*x for x in a),F())==c*c/N+sum((x*x for x in rem),F()),
                        'native_Gram_pythagoras')
                require(N*sum((x*x for x in r),F())==c*c,'transported_original_Gram')
                # Primitive is every nonreference coordinate; do not erase zero sums.
                rebuilt=[-sum(rem[1:],F())]+rem[1:]
                require(rebuilt==rem,'split_boundary_primitive')
                for lam in (F(1,2),F(2),F(3)):
                    require(sum((lam/N for _ in occ),F())==lam,'all_positive_original_masses')
            split_cases+=1
    # The three-way tower, all fibres, not merely one example.
    triple=list(product(range(-1,2),repeat=3));fib3=defaultdict(list)
    for x in triple:fib3[sum(x)].append(x)
    ntwo=Counter(a+b for a,b in product(range(-1,2),repeat=2))
    zrec={}
    for beta,occ in sorted(fib3.items()):
        sums=sorted({a+b for a,b,c in occ});n3=len(occ)
        native={x:F(1,n3) for x in occ}
        reset={x:F(1,len(sums)*ntwo[x[0]+x[1]]) for x in occ}
        retained={x:F(ntwo[x[0]+x[1]],n3)/ntwo[x[0]+x[1]] for x in occ}
        require(retained==native,'coherent_weighted_tower')
        require(sum(reset.values())==1,'reset_remains_right_inverse')
        en=sum((v*v for v in reset.values()),F())
        require(en>=F(1,n3),'least_norm_vs_reset')
        if beta==0:
            require((n3,en,en-F(1,n3))==(7,F(4,27),F(1,189)),'tower_strict_defect')
            zrec={'occurrences':occ,'canonical_coefficients':[native[x] for x in occ],
                  'reset_coefficients':[reset[x] for x in occ],
                  'canonical_norm_squared':F(1,7),'reset_norm_squared':en,'excess':en-F(1,n3)}
    # Coarsening kills a nonzero supported class, with an actual primitive.
    L=R=[0,1];fine=cohomology(L,R,[0,1],full=True)
    coarse=cohomology([0,0],[0,0],[0],full=True)
    killed=[F(1),F(-1),F(1),F(-1)]
    B=coarse['boundary_columns'];primitive=[F(-1),F(-1)]
    require([sum((coef*b[j] for coef,b in zip(primitive,B)),F()) for j in range(4)]==killed,
            'coarsening_nonzero_class_actual_primitive')
    # A support-preserving amplitude calculation: cancellation stays present.
    def plus(u,v):return (u[0]|v[0],u[1]+v[1])
    a=(frozenset({'E'}),F(1));z=plus(a,(a[0],F(-1)));tau=(frozenset(),F())
    require(z==(a[0],F()) and z!=tau,'supported_zero_not_absence')
    return {'all_small_map_pairs':ncases,'small_split_budgets':split_cases,'tower':zrec,
            'coarsening':{'fine_H0':fine['dimensions']['H0'],'coarse_H0':coarse['dimensions']['H0'],
                           'killed_class':[1,-1],'nonzero_chain_image':killed,'boundary_primitive':primitive}}

def run(bound):
    tests=generic_tests();examples=[]
    for p,a,f in [(2521,636,(1,1,1)),(1201,312,(2,1,1)),(241,64,(3,)),(37,18,(1,2))]:
        examples.append(shell(p,a,f,True))
    ex=examples[0]
    require((sum(c['raw_matches'] for c in ex['channels'].values()),
             sum(c['cohomology']['dimensions']['H0'] for c in ex['channels'].values()),
             sum(c['weighted_original_count'] for c in ex['channels'].values()))==(5,4,3),
            'main_five_four_three_example')
    fail=examples[2]
    require(sum(c['cohomology']['dimensions']['H0'] for c in fail['channels'].values())==0,
            'genuine_empty_shell')
    require(sum(c['cohomology']['source_mass'] for c in fail['channels'].values())==28,
            'empty_H0_nonzero_source_mass')
    scan=Counter();first_difference=None
    for p in range(13,bound+1,12):
        if not prime(p):continue
        scan['primes']+=1
        for a in range((p+3)//4,(p-1)//2+1):
            scan['shells']+=1;e=tuple(k for _,k in factors(a))
            # Full budget plus one coordinate peeled by one occurrence, including endpoints.
            choices={e}
            for j in range(len(e)):
                f=list(e);f[j]-=1;choices.add(tuple(f))
            expected=None
            for f in sorted(choices):
                rec=shell(p,a,f);scan['splits']+=1
                counts=tuple(rec['channels'][c]['weighted_original_count'] for c in ('E','M'))
                if expected is None: expected=counts
                require(expected==counts,'split_independent_original_counts')
                for c in rec['channels'].values():
                    scan['matching_occurrences']+=c['raw_matches']
                    scan['matching_H0_rank']+=c['cohomology']['dimensions']['H0']
                    if c['raw_matches']!=c['weighted_original_count']:
                        scan['inflated_channel_observations']+=1
                        if first_difference is None:first_difference=rec
    # Joint local-to-global regression from the original labelled divisor set.
    us=sorted(prod(q**i for (q,e),i in zip(factors(18),exp))
              for exp in product(*(range(2*e+1) for q,e in factors(18))))
    five=[u for u in us if (4*u+1)%5==0];seven=[u for u in us if (4*u+1)%7==0]
    require(five==[1,6,36,81] and seven==[12,54] and not set(five)&set(seven),
            'same_leaf_CRT_not_local_H0_product')
    return {'examples':examples,'structural':tests,'scan':dict(scan),
            'first_inflation':first_difference,
            'joint_local_regression':{'p':37,'a':18,'R':35,'E_mod5':five,'E_mod7':seven,'intersection':[]},
            'bound':bound,'scope':'prime p=1 mod12, p<=bound, all first-half shells; unsplit and one-occurrence peels'}

def encode(x):
    if isinstance(x,F):return {'numerator':x.numerator,'denominator':x.denominator}
    if isinstance(x,tuple):return list(x)
    raise TypeError(type(x).__name__)

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--bound',type=int,default=200)
    ap.add_argument('--out',type=Path,default=Path('generated'));args=ap.parse_args()
    if args.bound<13:ap.error('bound >=13 required')
    args.out.mkdir(parents=True,exist_ok=True)
    data=run(args.bound)
    for name,val in [('examples.json',data.pop('examples')),('structural.json',data.pop('structural')),
                     ('scan.json',data),('checks.json',dict(CHECKS))]:
        (args.out/name).write_text(json.dumps(val,default=encode,sort_keys=True,indent=2)+'\n',encoding='utf8')
    print(json.dumps({'checks':sum(CHECKS.values()),'scan':data['scan']},sort_keys=True))
if __name__=='__main__':main()
