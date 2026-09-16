#!/usr/bin/env python3
"""Exact certificates for 2-adic short-relation exclusion and ES capacity.

Python >=3.9, standard library only. Checks stay active under -O.
The imported infinite estimate is Chim (2025), not proved by this program.
No 77,000,000-bit modulus is expanded. Large thresholds are symbolic powers.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import gcd, isqrt
from pathlib import Path
import json

CHECKS=Counter()
VARIANTS=(
    dict(label='A',x1=200,x2=25,x3=F(493,100),C2=5500,C=550000,H=140,
         onset=77000000,denominator=400000),
    dict(label='B',x1=5000,x2=900,x3=F(485,100),C2=3920,C=387000,H=4000,
         onset=1548000000,denominator=270000),
)

def check(ok,label):
    CHECKS[label]+=1
    if not ok: raise ArithmeticError(label)

def val2(n):
    if n==0: raise ValueError('valuation at zero is infinite, not an integer')
    return (abs(n)&-abs(n)).bit_length()-1

def dot(a,b):return a[0]*b[0]+a[1]*b[1]
def norm(a):return dot(a,a)
def det(a,b):return a[0]*b[1]-a[1]*b[0]
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def scale(c,a):return(c*a[0],c*a[1])
def nearest(x):
    x=F(x)
    return (2*x.numerator+x.denominator)//(2*x.denominator)

def log_interval(x,n=12):
    """Rational atanh-series enclosure; positive x>1."""
    x=F(x)
    if x<=1 or n<1:raise ValueError('x>1 and n>=1')
    z=(x-1)/(x+1)
    lo=2*sum((z**(2*j+1)/F(2*j+1) for j in range(n)),F())
    tail=2*z**(2*n+1)/(F(2*n+1)*(1-z*z))
    return lo,lo+tail

def constants():
    l2,u2=log_interval(2);la,ua=log_interval(F(3,2));lb,ub=log_interval(F(11,8))
    intervals={'log2':(l2,u2),'log3':(l2+la,u2+ua),'log11':(3*l2+lb,3*u2+ub)}
    coarse={'log2':(F(6931,10000),F(6932,10000)),
            'log3':(F(10986,10000),F(10987,10000)),
            'log11':(F(23978,10000),F(23980,10000))}
    for name,(lo,hi) in intervals.items():
        check(coarse[name][0]<lo<hi<coarse[name][1],'certified_log_enclosure')
    l2,u2=coarse['log2'];l3,u3=coarse['log3'];l11,u11=coarse['log11']
    coefficient=u2*(1/l11+1/l3)
    check(coefficient<1,'logarithmic_height_not_inflated')
    records=[]
    for v in VARIANTS:
        Kmax=2*v['C2']*(2*u2+v['x3'])*u3*u11/l2**3
        Hmax=max(v['x1']*u2,v['x2']*(2*u2+v['x3'])*u2)
        check(Kmax<v['C'],'Chim_coefficient_round_up')
        check(Hmax<v['H'],'Chim_fixed_height_round_up')
        check(v['C']*u2<v['denominator'],'binary_power_conversion')
        check(v['onset']==v['C']*v['H'],'onset_exact')
        records.append(dict(v,K_upper=Kmax,H_upper=Hmax,
                            binary_conversion_upper=v['C']*u2))
    return dict(series_terms=12,exact_intervals=intervals,coarse_intervals=coarse,
                bprime_times_log2_coefficient=coefficient,variants=records)

@lru_cache(None)
def lg311(k):
    """J:3^J=11 mod 2^k by an exact truncated 2-adic log ratio."""
    if k<3:raise ValueError('k>=3')
    if k==3:return 1
    n=k-3;mod=1<<n
    def normalized_log(c):
        ans=0
        for j in range(1,n+3):
            v=val2(j);s=3*(j-1)-v
            if s<n:
                term=((pow(c,j,mod)*pow(j>>v,-1,mod))<<s)%mod
                ans=(ans+(term if j&1 else -term))%mod
        return ans
    A=normalized_log(1);B=normalized_log(pow(3,-1,mod))
    check(A%2==1,'log_ratio_unit_denominator')
    J=1+2*((B*pow(A,-1,mod))%mod)
    check(0<=J<(1<<(k-2)) and pow(3,J,1<<k)==11%(1<<k),'exact_logarithm_return')
    return J

def gauss(b1,b2):
    """Exact nearest rounding, with an equality stop to avoid tie cycling."""
    b1,b2=tuple(b1),tuple(b2)
    if not det(b1,b2):raise ValueError('full-rank basis required')
    trace=[]
    while True:
        if norm(b2)<norm(b1):
            b1,b2=b2,b1;trace.append(['swap'])
        q=nearest(F(dot(b1,b2),norm(b1)))
        v=add(b2,scale(-q,b1))
        trace.append(['subtract',q])
        if norm(v)>=norm(b1):
            b2=v;break
        b2=v
    check(norm(b1)<=norm(b2) and 2*abs(dot(b1,b2))<=norm(b1),'Gauss_reduction_inequalities')
    return b1,b2,trace

@lru_cache(None)
def basis_record(k):
    J=lg311(k);o=1<<(k-2)
    b1,b2,trace=gauss((o,0),(-J,1))
    check(abs(det(b1,b2))==o,'relation_lattice_full_index')
    check(all((a+J*b)%o==0 for a,b in (b1,b2)),'basis_original_relations')
    return dict(k=k,J=J,o=o,basis=[b1,b2],widths=[abs(b1[i])+abs(b2[i]) for i in range(2)],
                shortest_squared=norm(b1),reduction_trace=trace)

def inverse_coordinates(B,x):
    b1,b2=B;D=det(b1,b2)
    if not D:raise ValueError('singular basis')
    return F(x[0]*b2[1]-x[1]*b2[0],D),F(b1[0]*x[1]-b1[1]*x[0],D)

def round_word(k,target,e,f,offset=(0,0)):
    """Choose a point of target coset in a translated available rectangle."""
    rec=basis_record(k);B=rec['basis'];o=rec['o'];J=rec['J']
    if e<rec['widths'][0] or f<rec['widths'][1]:raise ValueError('actual rectangle below basis widths')
    lo=offset;c=(F(2*lo[0]+e,2),F(2*lo[1]+f,2));v=(target%o,0)
    alpha=inverse_coordinates(B,(c[0]-v[0],c[1]-v[1]))
    z=tuple(nearest(t) for t in alpha)
    w=add(v,add(scale(z[0],B[0]),scale(z[1],B[1])))
    check(lo[0]<=w[0]<=lo[0]+e and lo[1]<=w[1]<=lo[1]+f,'rounded_word_original_box')
    check((w[0]+J*w[1]-target)%o==0,'rounded_word_original_target')
    inv=inverse_coordinates(B,(w[0]-v[0],w[1]-v[1]))
    check(inv==z,'rounding_complete_coordinate_inverse')
    return dict(word=w,basis_coordinates=z,unrounded_coordinates=alpha,
                offset=lo,budgets=(e,f),target=target%o)

def relation_valuation(a,b):
    if (a,b)==(0,0):raise ValueError('zero relation excluded')
    num=3**max(a,0)*11**max(b,0)-3**max(-a,0)*11**max(-b,0)
    return val2(num)

def valprime(n,q):
    if n<=0:raise ValueError('positive n')
    e=0
    while n%q==0:n//=q;e+=1
    return e

def middle_return(p,k,Q,origin):
    u=1<<(2*k-5);N=p+4*u;m=1<<k
    if not(p%8==1 and p>2*u and Q>0 and N%Q==0 and Q%m==m-1):
        raise ValueError('original seed/cofactor domain')
    R=N//Q;a=(p+R)//4;d=gcd(a,u)
    h=d*d//u;r=u//d;s=a//d
    check(h*r*s==a and h*r*r==u and gcd(r,s)==1,'original_divisor_normalization')
    check((r+s)%R==0 and 0<R<p and p<4*a<2*p,'original_gate_and_first_half')
    lam=(r+s)//R;den=(a,p*h*s*lam,p*h*r*lam)
    check(all(v>0 for v in den) and sum((F(1,v) for v in den),F())==F(4,p),'ES_exact_reciprocal_identity')
    check(F(p*a*a,R*den[1]-p*a)==u,'ordered_divisor_inverse')
    check((N//R,N//Q)==(Q,R),'cofactor_marking_inverse')
    return dict(p=p,k=k,u=u,N=N,Q=Q,R=R,a=a,h=h,r=r,s=s,quotient=lam,
                channel='M',denominators=den,origin=origin)

def primality_trial(n):
    if n<2:return False
    if n%2==0:return n==2
    return all(n%d for d in range(3,isqrt(n)+1,2))

def relative_word(k,v,target,e,f,r0,s0):
    h=k-v;d=1<<v
    if h<3 or not (0<=r0<d and 0<=s0<d and r0<=e and s0<=f):raise ValueError('original relative digit domain')
    J=lg311(k);diff=target-r0-J*s0
    if diff%d:raise ValueError('coarse target not satisfied')
    E=(e-r0)//d;Ff=(f-s0)//d
    high=round_word(h,diff//d,E,Ff)
    i,j=high['word'];orig=(r0+d*i,s0+d*j)
    check(0<=orig[0]<=e and 0<=orig[1]<=f,'relative_original_capacities')
    check((orig[0]+J*orig[1]-target)%(1<<(k-2))==0,'relative_fine_target')
    check((orig[0]%d,orig[1]%d,orig[0]//d,orig[1]//d)==(r0,s0,i,j),'relative_digits_and_inverse')
    return dict(k=k,relative_shift=v,effective_precision=h,d=d,original_word=orig,
                low_digits=(r0,s0),high=high)

def examples():
    p=482187176641;k=6;N=3**7*11**5*37**2
    check(N==p+512,'inherited_example_input_factorization')
    check(primality_trial(p),'inherited_prime_trial_certificate')
    log=next(j for j in range(16) if pow(3,j,64)==(-pow(37,-1,64))%64)
    rw=round_word(k,log,7,5)
    i,j=rw['word'];Q=3**i*11**j*37
    hit=middle_return(p,k,Q,dict(rw,outside_divisor=37,primality='full odd trial division through isqrt(p)'))
    allwords=[(i,j) for i in range(8) for j in range(6) if (i+7*j-log)%16==0]
    check(allwords==[(1,4),(6,1)],'complete_inherited_two_word_fibre')
    check(hit['Q'] in (296703,1625151),'inherited_ordered_state')
    # A proper-subgroup application; p is an integer, not asserted prime.
    k=8;v=2;e=28;f=20;t=31;N=3**e*11**f*31**2;p=N-(1<<(2*k-3))
    target=next(j for j in range(64) if pow(3,j,256)==(-pow(t,-1,256))%256)
    rel=relative_word(k,v,target,e,f,0,0)
    i,j=rel['original_word'];Q=3**i*11**j*t
    rh=middle_return(p,k,Q,dict(relative=rel,outside_divisor=t,primality='not asserted'))
    # Exact empty fixed-seed branch, distinct from failure at the prime.
    p0=49681;k0=6;N0=p0+512
    empty=[3**i*11**j*13**l for i in range(4) for j in range(2) for l in range(3)
           if (3**i*11**j*13**l)%64==63]
    check(N0==3**3*11*13**2 and not empty,'small_capacity_empty_branch')
    alt=(12423,56450112,9255769024)
    check(sum((F(1,x) for x in alt),F())==F(4,p0),'empty_branch_prime_has_other_witness')
    return dict(inherited_prime=hit,all_target_words=allwords,proper_relative_integer=rh,
                empty_branch=dict(p=p0,k=k0,factorization=[[3,3],[11,1],[13,2]],cofactors=empty,other_denominators=alt))

def threshold_records():
    out=[]
    for v in VARIANTS:
        k=v['onset'];D=v['denominator'];j=k//D
        check(j>=3,'threshold_binary_exponent_positive')
        check(4*j<=k-2,'power_term_dominates_sqrt_term_at_onset')
        check(4*(1<<j)>D*(j+1),'new_capacity_strictly_below_old_at_bucket_start')
        # This elementary induction extends across every later bucket.
        check(2*(j+1)>=j+2,'bucket_induction_step')
        out.append(dict(label=v['label'],onset=k,relation_lower_power=j,
                        square_capacity_power=k-1-j,
                        relation_lower='max(|a|,|b|)>2^floor(k/denominator)',
                        capacity='2^(k-1-floor(k/denominator))',denominator=D,
                        expanded_large_modulus=False))
    return out

def structural(bound_k=12):
    targets=0;fibres=0;reductions=0
    for k in range(3,bound_k+1):
        rec=basis_record(k);E,Ff=rec['widths'];o=rec['o'];J=rec['J'];B=rec['basis']
        complete=Counter((i+J*j)%o for i in range(E+1) for j in range(Ff+1))
        check(len(complete)==o,'entire_basis_rectangle_covers')
        for r in range(o):
            rw=round_word(k,r,E,Ff)
            words=[(i,j) for j in range(Ff+1) for i in range(E+1) if (i+J*j-r)%o==0]
            check(rw['word'] in words,'returned_word_in_complete_original_fibre')
            for w in words:
                z=inverse_coordinates(B,(w[0]-r,w[1]))
                check(all(t.denominator==1 for t in z),'complete_lattice_fibre_integrality')
                fibres+=1
            targets+=1
        # Translated boxes: tested separately, not inferred from targets at zero.
        for offset in ((-7,5),(13,-11),(5,9)):
            for r in (0,1,o//2,o-1):round_word(k,r,E+2,Ff+3,offset)
        # Direct shortest-vector audit in an explicitly bounded square.
        K=isqrt(rec['shortest_squared'])+1
        for b in range(-K,K+1):
            amin=(-J*b)%o
            for a in (amin-o,amin,amin+o):
                if a==b==0:continue
                check(a*a+b*b>=rec['shortest_squared'],'exact_shortest_relation_local_audit')
        if k>3:check(J%(o//2)==lg311(k-1),'logarithm_precision_compatibility')
    for k in range(4,13):
        for v in range(k-2):
            h=k-v;d=1<<v
            check(lg311(k)%(1<<(h-2))==lg311(h),'relative_no_height_inflation')
            for a,b in product(range(-7,8),repeat=2):
                lhs=(pow(3,d*a,1<<k)*pow(11,d*b,1<<k))%(1<<k)==1
                rhs=(pow(3,a,1<<h)*pow(11,b,1<<h))%(1<<h)==1
                check(lhs==rhs,'precision_division_exact_kernel')
                reductions+=1
    # Generic signed relations and axis exceptional loci, finite corroboration only.
    signcases=0
    for a,b in product(range(-50,51),repeat=2):
        if a==b==0:continue
        val=relation_valuation(a,b);B=max(abs(a),abs(b))
        check(val<550000*140,'finite_sign_fixture_coarse_imported_bound')
        if a==0 or b==0:
            x=abs(a or b)
            check(val==(1 if x%2 else 2+val2(x)),'axis_LTE_exception_handled')
        else:
            aa=F(3) if a>0 else F(1,3)
            bb=F(1,11) if b>0 else F(11)
            lam=aa**abs(a)-bb**abs(b)
            raw=F(3)**a*F(11)**b-1
            check(lam==F(11)**(-b)*raw,'all_signed_source_form_morphisms')
            check(val2(lam.numerator)-val2(lam.denominator)==val,'signed_source_valuation')
        signcases+=1
    check(relation_valuation(5,13)==13,'finite_precision_plateau_exact_relation')
    return dict(exhaustive_modulus_k_max=bound_k,target_cosets=targets,
                original_fibre_words=fibres,precision_reduction_fixtures=reductions,
                signed_relation_fixtures=signcases)

def negative_controls():
    result=[]
    def reject(name,fn):
        try:fn()
        except (ValueError,ArithmeticError):result.append(name);return
        raise ArithmeticError('negative control accepted: '+name)
    reject('zero relation is not a nonzero logarithmic form',lambda:relation_valuation(0,0))
    reject('below-capacity rounding is not certified',lambda:round_word(6,13,3,1))
    reject('improper lower digit cannot be divided',lambda:relative_word(8,2,1,28,20,0,0))
    reject('missing original outside factor',lambda:middle_return(482187176641,6,3**6*11,{}))
    reject('dependent bases cannot replace 3,11',lambda:check(3**2!=9,'multiplicative_independence_required'))
    reject('same coefficients at wrong precision',lambda:check(pow(3,5,1<<14)*pow(11,13,1<<14)%(1<<14)==1,'plateau_ends'))
    hit=examples()['inherited_prime']
    reject('changing denominator order without inverse',lambda:check(F(hit['p']*hit['a']**2,hit['R']*hit['denominators'][2]-hit['p']*hit['a'])==hit['u'],'ordered_marking_required'))
    return result

def encode(x):
    if isinstance(x,F):return dict(n=x.numerator,d=x.denominator)
    if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [encode(v) for v in x]
    return x

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out',default='generated');ap.add_argument('--small-k',type=int,default=12)
    ap.add_argument('--large-k',type=int,default=4096)
    args=ap.parse_args()
    if not 3<=args.small_k<=16:ap.error('small-k in [3,16]')
    if args.large_k<args.small_k:ap.error('large-k >= small-k')
    dest=Path(args.out);dest.mkdir(parents=True,exist_ok=True)
    c=constants();s=structural(args.small_k);ex=examples();th=threshold_records()
    ks=set(range(3,min(256,args.large_k)+1))|{k for k in (512,1024,2048,4096,args.large_k) if k<=args.large_k}
    bs=[basis_record(k) for k in sorted(ks)]
    nc=negative_controls()
    for name,obj in [('constants.json',c),('structural.json',s),('examples.json',ex),
                     ('thresholds.json',th),('bases.json',bs),('negative_controls.json',nc),
                     ('checks.json',dict(CHECKS))]:
        (dest/name).write_text(json.dumps(encode(obj),indent=2,sort_keys=True)+'\n',encoding='utf8')
    print(json.dumps(dict(checks=sum(CHECKS.values()),basis_certificates=len(bs),largest_computed_k=max(ks),
                          exhaustive_targets=s['target_cosets'],negative_controls=len(nc)),sort_keys=True))
if __name__=='__main__':main()
