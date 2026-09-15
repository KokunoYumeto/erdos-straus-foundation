#!/usr/bin/env python3
"""Exact fixed-parameter cofactor transport and dyadic capacity certificates.
Python standard library only. Counts refer to original middle states at a fixed
u, summed over residuals; they do not count unrelated local choices as witnesses.
Normal and -O modes keep every check active. No universal ES claim.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import gcd, isqrt, prod
from pathlib import Path
import json

CHECKS=Counter()
HARD={1,121,169,289,361,529}

def require(ok,label):
    CHECKS[label]+=1
    if not ok: raise ArithmeticError(label)

@lru_cache(None)
def factor(n):
    if n<1: raise ValueError('factor: positive input required')
    ans=[];q=2
    while q*q<=n:
        e=0
        while n%q==0:n//=q;e+=1
        if e:ans.append((q,e))
        q=3 if q==2 else q+2
    if n>1:ans.append((n,1))
    return tuple(ans)

def prime(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))

def vp(n,q):
    if n<=0 or q<2:raise ValueError('positive n and q>=2 required')
    e=0
    while n%q==0:n//=q;e+=1
    return e

def divisors_from_factor(fs):
    out=[1]
    for q,e in fs:out=[d*q**i for d in out for i in range(e+1)]
    return sorted(out)

def divisors(n):return divisors_from_factor(factor(n))
def K_of(u):return prod(q**((e+1)//2) for q,e in factor(u))

def inverse_label(p,u,R):
    K=K_of(u);N=p+4*u
    if p%4!=1 or p<=2*u or gcd(p,u)!=1:raise ValueError('original parameter domain')
    if N%R or R<=0:raise ValueError('positive factor required')
    Q=N//R
    if Q%(4*K)!=4*K-1:raise ValueError('wrong cofactor residue')
    require(3<=R<p and R%4==3,'original_first_half_residual')
    a=(p+R)//4
    require(4*a==p+R and a%K==0 and a*a%u==0,'original_divisor_availability')
    d=gcd(a,u);h=d*d//u;r=u//d;s=a//d
    require(h*r*s==a and h*r*r==u and gcd(r,s)==1,'normalization')
    require((r+s)%R==0,'middle_quotient_integral')
    lam=(r+s)//R
    den=(a,p*h*s*lam,p*h*r*lam)
    require(all(x>0 for x in den) and sum((F(1,x) for x in den),F())==F(4,p),'ordered_ES_identity')
    require(F(p*a*a,R*den[1]-p*a)==u,'ordered_inverse_divisor')
    ar=(p+Q)//4
    require(4*ar==p+Q and 3<=Q<p,'reflected_shell_range')
    eK=K//gcd(K,ar);eu=u//gcd(u,ar*ar)
    B=(p-1)//4
    require(eK==K//gcd(K,B),'constant_root_divisor_defect')
    require(eu==u//gcd(u,B*B),'constant_full_divisor_defect')
    require((eu==1)==(p%(4*K)==1),'reflection_exact_return_locus')
    require((p+4*u)%Q==0,'reflected_gate_still_zero')
    fs=factor(a)
    beta=[vp(u,q)-e for q,e in fs]
    require(prod(q**(e+b) for (q,e),b in zip(fs,beta))==u,'complete_exponent_return')
    return dict(p=p,u=u,K=K,m=4*K,N=N,R=R,Q=Q,a=a,channel='M',
                h=h,r=r,s=s,lambda_=lam,denominators=list(den),
                a_factorization=fs,centered_beta=beta,
                reflected_a=ar,reflection_K_defect=eK,reflection_u_defect=eu,
                lower_chamber_sufficient=(8*r<s))

def seed_states(p,u):
    K=K_of(u);N=p+4*u
    if p%4!=1 or p<=2*u or gcd(p,u)!=1:raise ValueError('fixed seed domain')
    return [inverse_label(p,u,N//Q) for Q in divisors(N) if Q%(4*K)==4*K-1]

def log3(y,k):
    if k<3 or y%8 not in (1,3):raise ValueError('logarithm domain')
    j=0 if y%8==1 else 1
    for r in range(4,k+1):
        m=1<<r
        if pow(3,j,m)!=y%m:j+=1<<(r-3)
        require(pow(3,j,m)==y%m,'exact_2adic_logarithm_lift')
    require(0<=j<1<<(k-2) and pow(3,j,1<<k)==y%(1<<k),'logarithm_inverse')
    return j

def chi8(n):
    if n%2==0:raise ValueError('odd argument required')
    return 1 if n%8 in (1,3) else -1

def outside_mass(fs):
    tau=prod(e+1 for q,e in fs)
    signed=prod((e+1 if chi8(q)==1 else int(e%2==0)) for q,e in fs)
    require((tau-signed)%2==0,'quadratic_mass_parity')
    return (tau-signed)//2

def profile_distribution(fs,m):
    """Exact bounded multiplicities, including repeated prime powers."""
    mu={1:1}
    for q,e in fs:
        fac=Counter(pow(q,j,m) for j in range(e+1))
        nxt=Counter()
        for x,a in mu.items():
            for y,b in fac.items():nxt[x*y%m]+=a*b
        mu=dict(nxt)
    return mu

def dyadic(p,k,details=True):
    if k<4:raise ValueError('k>=4 required')
    m=1<<k;o=1<<(k-2);L=o//2;u=1<<(2*k-5)
    if p<=2*u or p%m!=1+(m//2):raise ValueError('dyadic arithmetic progression and size required')
    N=p+4*u;e=vp(N,3);M=N//3**e;fs=factor(M)
    require(gcd(N,2)==1 and M%3!=0,'retained_prime_occurrences')
    require(pow(3,L,m)==p%m and pow(3,o,m)==1,'dyadic_half_period')
    mu=profile_distribution(fs,m);A=outside_mass(fs)
    require(A==sum(v for q,v in mu.items() if chi8(q)==-1),'character_mass_direct')
    aj=[mu.get((-pow(3,j,m))%m,0) for j in range(o)]
    counts=[sum((i+j-L)%o==0 for i in range(e+1)) for j in range(o)]
    C=sum(a*c for a,c in zip(aj,counts))
    lo=F((2*(e+1)//o)*A,2)
    hi=F(((2*(e+1)+o-1)//o)*A,2)
    require(lo<=C<=hi,'all_multiplicity_count_bounds')
    for j in range(o):
        require(aj[j]==aj[(L-e-j)%o],'actual_divisor_complement_symmetry')
    if (e+1)%L==0:require(C==F((e+1)*A,o),'exact_balanced_mass')
    qlist=[q for q,f in fs if chi8(q)==-1]
    require(bool(qlist)==(A>0),'actual_prime_vs_divisor_mass')
    short=None
    if e>=2*o-2 and qlist:
        q=min(qlist);j=log3(-q,k);i=(L-j)%o;R=3**i*q
        require(q*q<=M and i<=e and R*R<=N,'deep_capacity_square_root_bound')
        short=inverse_label(p,u,R)
        short.update(chosen_prime=q,three_exponent=i)

    if e>=L-1:require((C>0)==bool(qlist),'bounded_capacity_forcing_iff')
    actual=seed_states(p,u)
    require(C==len(actual),'cofactor_count_original_states')
    for w in actual:require(w['reflection_u_defect']==w['reflection_K_defect']==2,'one_missing_factor_two')
    chosen=[]
    if e>=L-1:
        for q in qlist:
            j=log3(-q,k);iQ=(-j)%o;iR=(L-j)%o
            require((iQ<L)!=(iR<L),'one_half_period_choice')
            if iQ<L:i=iQ;tag='cofactor';Q=3**i*q;R=N//Q
            else:i=iR;tag='residual';R=3**i*q;Q=N//R
            require(i<=e and R*Q==N and Q%m==m-1,'actual_one_prime_word')
            w=inverse_label(p,u,R)
            w.update(chosen_prime=q,chosen_prime_occurrences=1,three_exponent=i,
                     logarithm=j,word_role=tag)
            chosen.append(w)
    result=dict(p=p,k=k,u=u,m=m,order=o,half_order=L,N=N,e=e,M=M,
                M_factorization=fs,outside_divisor_mass=A,
                count=C,lower_bound=lo,upper_bound=hi,
                threshold=L-1,threshold_met=e>=L-1,deep_short=short,
                exact_formula=(e+1)%L==0,chosen=chosen)
    if details:result.update(outside_log_multiplicities=aj,exponent_availability=counts,all_states=actual)
    return result

def original_shell_test(bound=300):
    checked=0
    for p in range(5,bound+1,4):
        if not prime(p):continue
        direct=Counter()
        for a in range((p+3)//4,(p-1)//2+1):
            R=4*a-p
            for u in divisors(a*a):
                if 2*u<p and (a+u)%R==0:direct[(u,R)]+=1
        indirect=Counter()
        for u in range(1,(p-1)//2+1):
            if gcd(p,u)!=1:continue
            for w in seed_states(p,u):indirect[(u,w['R'])]+=1
        require(direct==indirect,'complete_original_shell_vs_factor_atlas')
        checked+=sum(indirect.values())
    return dict(prime_bound=bound,returned_states=checked,scope='all seeds 2u<p; all first-half shells')

def reflection_tests():
    total=0;aligned=0
    smallseeds=(1,2,3,4,6,9,12,18,36)
    examples={}
    for p in range(5,501,4):
        if not prime(p):continue
        for u in range(1,min(65,(p+1)//2)):
            if p<=2*u:continue
            states=seed_states(p,u)
            for w in states:
                if p%(4*K_of(u))==1:
                    v=inverse_label(p,u,w['Q'])
                    require((v['R'],v['Q'])==(w['Q'],w['R']),'valid_reflection_involution')
                    aligned+=1
                total+=1
            if p%24==1 and u in smallseeds and states:
                w=min(states,key=lambda w:w['R']);Rf=factor(w['R'])
                rank={4:1,8:2,12:2,24:3}[w['m']]
                require(w['R']**2<=w['N'],'small_seed_sqrt_residual')
                require(all(e==1 for q,e in Rf) and len(Rf)<=rank,'small_seed_prime_factor_bound')
    for R in (31,39):examples[str(R)]=inverse_label(1201,2,R)
    return dict(states=total,aligned_reflections=aligned,examples=examples)

def cyclic_capacity_tests():
    records=[]
    for k in range(4,10):
        m=1<<k;o=1<<(k-2);L=o//2
        H={pow(3,j,m) for j in range(o)}
        require(len(H)==o and m-1 not in H,'half_group_order')
        require(H=={v for v in range(1,m,2) if v%8 in (1,3)},'half_group_quadratic_kernel')
        for y in H:require(pow(3,log3(y,k),m)==y,'all_logs_inverse')
        for e in range(2*o+2):
            n=[sum((i+j-L)%o==0 for i in range(e+1)) for j in range(o)]
            fl=(2*(e+1))//o;ce=(2*(e+1)+o-1)//o
            for j in range(o):
                jp=(L-e-j)%o
                require(fl<=n[j]+n[jp]<=ce,'complete_paired_interval_bound')
                require((L-e-jp)%o==j,'complement_involution_indices')
                if e>=L-1:require(n[j]+n[jp]>=1,'threshold_all_classes')
        # Threshold-minus-one misses the sole outside residue -3.
        if k>=5:
            e=L-2
            require(all((i+1-L)%o for i in range(e+1)),'threshold_sharp_formal_word')
        records.append(dict(k=k,modulus=m,order=o,exponents_tested=2*o+2))
    return records

def find_witness(p,maxu=128):
    for u in range(1,min(maxu,(p-1)//2)+1):
        if gcd(p,u)==1:
            got=seed_states(p,u)
            if got:return min(got,key=lambda w:w['R'])
    raise ArithmeticError('specified search found no alternate witness')

def examples():
    out=[]
    # Exact primality tests are deliberately independent trial division.
    for p,k in ((2542201,4),(6185041,5),(9017211169,6),(653881,4)):
        require(prime(p),'example_prime_trial_division')
        require(p%840 in HARD,'example_hard_class')
        rec=dyadic(p,k)
        rec['trial_bound']=isqrt(p);rec['hard_class']=p%840
        for q,e in rec['M_factorization']:require(prime(q),'cofactor_prime_trial_division')
        if rec['count']==0:
            rec['other_seed_witness']=find_witness(p)
        out.append(rec)
    r=out[0]
    require(r['count']==1 and r['all_states'][0]['R']==22903,'unique_long_residual')
    require(r['all_states'][0]['R']**2>r['N'],'no_unsupported_sqrt_bound')
    require(out[1]['e']==out[1]['threshold']-1 and out[1]['count']==0,'actual_sharp_k5')
    require(out[2]['e']==out[2]['threshold']-1 and out[2]['count']==0,'actual_sharp_k6')
    # Find small actual hard primes satisfying the higher thresholds, bounded explicitly.
    for k in (5,6):
        m=1<<k;u=1<<(2*k-5);th=(1<<(k-3))-1
        z=3**th
        first=next(t for t in range(1+m//2,m*z,m) if (t+4*u)%z==0)
        tested=0
        for p in range(first,first+200*m*z,m*z):
            tested+=1
            if p<=2*u or p%840 not in HARD or not prime(p):continue
            rec=dyadic(p,k)
            if rec['count']:
                rec['prime_trial_bound']=isqrt(p);rec['CRT_index_checks']=tested
                out.append(rec);break
        else:raise ArithmeticError('positive higher-level example not found in declared range')
    return out

def sieve(N):
    spf=list(range(N+1))
    for q in range(2,isqrt(N)+1):
        if spf[q]==q:
            for n in range(q*q,N+1,q):
                if spf[n]==n:spf[n]=q
    return spf

def factor_spf(n,spf):
    ans=[]
    while n>1:
        q=spf[n];e=0
        while n%q==0:n//=q;e+=1
        ans.append((q,e))
    return tuple(ans)

def scan(bound):
    spf=sieve(bound+32);stats=Counter();rows=[]
    for p in range(25,bound+1,48):
        if spf[p]!=p or p%840 not in HARD:continue
        stats['hard_primes_in_scope']+=1
        N=p+32;e=vp(N,3);M=N//3**e;fs=factor_spf(M,spf)
        mass=outside_mass(fs)
        ds=divisors_from_factor(factor_spf(N,spf));R=[d for d in ds if d%16==7]
        C=len(R)
        require((C>0)==(mass>0),'complete_hard_scan_factor_criterion')
        lo=F(((e+1)//2)*mass,2);hi=F(((e+2)//2)*mass,2)
        require(lo<=C<=hi,'complete_hard_scan_mass_bound')
        if e%2:require(C==F((e+1)*mass,4),'complete_hard_scan_exact_count')
        stats['middle_states']+=C;stats['occupied_seed8_branches']+=bool(C)
        stats['empty_seed8_branches']+=not C
        stats['exact_balanced_formula_branches']+=e%2
        if C:
            minimal=min(R)
            w=inverse_label(p,8,minimal)
            stats['min_residual_above_sqrt']+=minimal*minimal>N
            q=min(q for q,f in fs if chi8(q)==-1)
            role={7:'residual',13:'residual',15:'cofactor',5:'cofactor'}[q%16]
            word=q*(3 if q%16 in (5,13) else 1)
            ret=word if role=='residual' else N//word
            require(ret in R,'explicit_k4_table_return')
            rows.append(dict(p=p,N=N,e=e,M_factors=fs,mass=mass,count=C,min_R=minimal,
                             q=q,role=role,constructed_R=ret))
    return dict(bound=bound,scope='primes p=25 mod48 and hard mod840; fixed u=8',
                counts=dict(stats),occupied=rows)

def negative_tests(ex):
    rejected=[]
    def reject(name,fn):
        try:fn()
        except (ValueError,ArithmeticError):rejected.append(name);return
        raise ArithmeticError('accepted wrong claim: '+name)
    reject('gate alone implies reflected availability',lambda:require(ex[0]['all_states'][0]['reflection_u_defect']==1,'bad_reflection'))
    reject('same branch always has sqrt residual',lambda:require(ex[0]['all_states'][0]['R']**2<=ex[0]['N'],'bad_square_root'))
    reject('outside prime alone removes exponent threshold',lambda:require(ex[1]['count']>0,'bad_missing_three_occurrence'))
    reject('one actual q squared counts as two independent primes',lambda:require(outside_mass(((829,2),))==outside_mass(((829,1),(29,1))),'bad_multiplicity'))
    reject('wrong dyadic logarithm carrier',lambda:log3(5,5))
    reject('wrong fixed-seed cofactor class',lambda:inverse_label(2542201,8,111))
    return rejected

def encode(x):
    if isinstance(x,F):return {'num':x.numerator,'den':x.denominator}
    if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [encode(v) for v in x]
    return x

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--bound',type=int,default=2000000);ap.add_argument('--out',default='generated')
    args=ap.parse_args()
    if args.bound<100:ap.error('bound >=100 required')
    dest=Path(args.out);dest.mkdir(parents=True,exist_ok=True)
    cyc=cyclic_capacity_tests();base=original_shell_test();reflect=reflection_tests();ex=examples()
    neg=negative_tests(ex);ss=scan(args.bound)
    data={'structural.json':dict(cyclic=cyc,original_atlas=base,reflection=reflect),
          'examples.json':ex,'scan.json':ss,'negative_controls.json':neg,'checks.json':dict(CHECKS)}
    for name,obj in data.items():(dest/name).write_text(json.dumps(encode(obj),sort_keys=True,indent=2)+'\n')
    print(json.dumps(dict(checks=sum(CHECKS.values()),scan=ss['counts'],negative_controls=len(neg)),sort_keys=True))

if __name__=='__main__':main()
