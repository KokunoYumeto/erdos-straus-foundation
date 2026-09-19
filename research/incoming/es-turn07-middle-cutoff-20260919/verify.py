#!/usr/bin/env python3
"""Exact middle-channel hyperbola cutoff and fixed-grade obstruction.
Standard library only. A finite atlas is not a proof of universal occupancy.
"""
from __future__ import annotations
import argparse, hashlib, json
from collections import Counter
from math import gcd, isqrt, prod
from pathlib import Path

HARD = {1,121,169,289,361,529}

def need(ok: bool, label: str) -> None:
    if not ok:
        raise ArithmeticError(label)

def primes_to(n: int) -> list[int]:
    mark = bytearray(b'\x01')*(n+1)
    if n >= 0: mark[0] = 0
    if n >= 1: mark[1] = 0
    for d in range(2,isqrt(n)+1):
        if mark[d]: mark[d*d:n+1:d] = b'\x00'*(((n-d*d)//d)+1)
    return [d for d in range(2,n+1) if mark[d]]

def factor(n: int) -> dict[int,int]:
    need(n>0,'positive factor input')
    out: dict[int,int] = {}
    d=2
    while d*d<=n:
        while n%d==0:
            out[d]=out.get(d,0)+1; n//=d
        d=3 if d==2 else d+2
    if n>1: out[n]=out.get(n,0)+1
    return out

def divs_factor(f: dict[int,int], multiplier: int=1) -> list[int]:
    ans=[1]
    for q,e in sorted(f.items()):
        ans=[v*q**j for v in ans for j in range(multiplier*e+1)]
    return sorted(ans)

def square_divs(n: int) -> list[int]:
    return divs_factor(factor(n),2)

def is_prime(n: int) -> bool:
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))

def leg(a: int,p: int) -> int:
    x=pow(a%p,(p-1)//2,p)
    return -1 if x==p-1 else x

def cutoff(p: int,hard: bool) -> int:
    if hard:
        raw=(isqrt(12*p+292)-7)//3
    else:
        raw=isqrt((4*p+28)//3)-1
    return raw-(raw-3)%4

def state(p: int,a: int,u: int) -> tuple[int,...]:
    R=4*a-p
    need(p<4*a and 2*a<p and a*a%u==0 and u<a,'original oriented source')
    need((u+a)%R==0,'M gate')
    g=gcd(a,u); h=g*g//u; r=u//g; s=a//g
    need(h>0 and h*r*s==a and h*r*r==u and gcd(r,s)==1 and r<s,'gcd inverse')
    need((r+s)%R==0,'lambda divisibility')
    lam=(r+s)//R; j=h*r*lam; Q=4*j-1
    need(Q*R==p+4*u and Q*s==p*lam+r,'cofactor identities')
    need(0<Q<p and Q%4==3,'cofactor range')
    x,y,z=a,p*h*s*lam,p*h*r*lam
    need(4*x*y*z==p*(x*y+x*z+y*z),'ordered ES identity')
    need(p*a*a%(R*y-p*a)==0 and p*a*a//(R*y-p*a)==u,'ordered divisor inverse')
    return (a,u,R,Q,h,r,s,lam,j,x,y,z)

def record(p: int,t: tuple[int,...]) -> dict:
    a,u,R,Q,h,r,s,lam,j,x,y,z=t
    fa=factor(a)
    out=dict(p=p,channel='M',a=a,u=u,R=R,Q=Q,h=h,r=r,s=s,lambda_=lam,j=j,
             denominators=[x,y,z],complement_denominators=[x,z,y],
             complement_u=a*a//u,factorization=[[q,e] for q,e in fa.items()],
             beta=[[q,factor(u).get(q,0)-e] for q,e in fa.items()],
             chart='direct' if R<=Q else 'cofactor')
    return out

def full_middle(p: int) -> set[tuple[int,...]]:
    ans=set()
    for a in range(p//4+1,(p-1)//2+1):
        for u in square_divs(a):
            if u>=a: break
            if (u+a)%(4*a-p)==0: ans.add(state(p,a,u))
    return ans

def atlas(p: int,hard: bool) -> tuple[set[tuple[int,...]],dict]:
    B=cutoff(p,hard); ans=set(); direct_tests=0; cofactor_tests=0
    for R in range(3,B+1,4):
        a=(p+R)//4
        for u in square_divs(a):
            if u>=a: break
            direct_tests+=1
            if (u+a)%R: continue
            t=state(p,a,u)
            if R<=t[3]:
                need(t not in ans,'direct duplicate'); ans.add(t)
    for Q in range(3,B+1,4):
        j=(Q+1)//4
        for u in square_divs(j):
            cofactor_tests+=1
            if (p+4*u)%Q: continue
            R=(p+4*u)//Q
            if R<=Q: continue
            a=(p+R)//4
            # These are conclusions of the cofactor inverse, not filters.
            need(p<4*a and 2*a<p and u<a,'cofactor source inequalities')
            g=gcd(j,u); h=g*g//u; r=u//g; lam=j//g; s=R*lam-r
            need(h*r*lam==j and h*r*r==u and h*r*s==a,'cofactor inverse')
            t=state(p,a,u)
            need((h,r,s,lam)==t[4:8] and t[3]==Q,'chart inverse equality')
            need(t not in ans,'disjoint chart duplicate'); ans.add(t)
    return ans,dict(cutoff=B,direct_candidate_tests=direct_tests,
                    cofactor_candidate_tests=cofactor_tests)

def probable_prime(n: int) -> bool:
    """Discovery screen only; published primality uses the proof below."""
    if n<2:return False
    for q in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n%q==0:return n==q
    d=n-1;s=0
    while d%2==0:d//=2;s+=1
    for a in (2,3,5,7,11,13,17,19,23,29,31,37):
        if a>=n:continue
        x=pow(a,d,n)
        if x in (1,n-1):continue
        for _ in range(s-1):
            x=x*x%n
            if x==n-1:break
        else:return False
    return True

def build_grade_example(budget: int) -> dict:
    q=max(11,4*budget+1)
    while q%4!=3 or not is_prime(q):q+=1
    small=primes_to(q-1)
    L=8*prod(r for r in small if r!=2)
    k0=(-2*pow(L,-1,q))%q
    for index in range(10000):
        p=1+L*(k0+q*index)
        if p<=q or L*L<=p or not probable_prime(p):continue
        bases={}
        for r in small:
            for a in range(2,512):
                if pow(a,p-1,p)==1 and gcd(pow(a,(p-1)//r,p)-1,p)==1:
                    bases[r]=a;break
            else:break
        if len(bases)!=len(small):continue
        result=dict(budget=budget,q=q,L=L,index=index,k0=k0,p=p,
                    L_factorization=[[2,3]]+[[r,1] for r in small if r!=2],
                    order_bases=[[r,bases[r]] for r in small],
                    endpoint=dict(R=q,a=(p+q)//4,kappa=(p+1)//q),
                    discovery_screen='Miller-Rabin screen; not used as proof')
        verify_grade_example(result)
        return result
    raise RuntimeError('Finite discovery budget exhausted; no prime claim made.')

def verify_grade_example(c: dict) -> None:
    p,q,L=c['p'],c['q'],c['L']
    fs=c['L_factorization']
    need(all(isinstance(r,int) and isinstance(e,int) and e>0 and is_prime(r)
             for r,e in fs),'positive factor proof L')
    need(len({r for r,e in fs})==len(fs),'distinct factor support')
    need(prod(r**e for r,e in fs)==L,'factor product L')
    need((p-1)%L==0 and L*L>p,'Pocklington size')
    need({r for r,e in fs}=={r for r,b in c['order_bases']},'all prime factors certified')
    for r,a in c['order_bases']:
        need(pow(a,p-1,p)==1,'Fermat certificate')
        need(gcd(pow(a,(p-1)//r,p)-1,p)==1,'complete-order factor')
    # These conditions force every prime divisor of p to be 1 mod L > sqrt(p).
    need(p%L==1 and p%q==q-1 and q%4==3 and p>q,'CRT progression')
    need(primes_to(q-1)==[r for r,e in fs],'all smaller prime factors')
    need(all(leg(r,p)==1 for r in primes_to(q-1)) and leg(q,p)==-1,'least nonresidue')
    need(q>4*c['budget'] and p%840 in HARD,'grade and hard class')
    a=(p+q)//4; kap=(p+1)//q
    endpoint=c['endpoint']
    need(endpoint.get('R')==q and endpoint.get('a')==a and
         endpoint.get('kappa')==kap,'endpoint metadata')
    x,y,z=a,a*kap,p*a*kap
    need(4*x*y*z==p*(x*y+x*z+y*z),'endpoint identity')
    if 'denominators' in endpoint:
        need(endpoint['denominators']==[x,y,z],'endpoint denominators')
    endpoint['denominators']=[x,y,z]
    expected_fields=dict(least_nonresidue=q,least_negative_3mod4=q,
                         least_j_lower_bound=(q+1)//4)
    for key,value in expected_fields.items():
        if key in c:need(c[key]==value,key+' metadata')
        c[key]=value

def fixed_examples() -> dict:
    # p41 first equality: h2,r1,s6 => a12,u2; second h1,r3,s4 => a12,u9.
    fixtures=[(41,12,2),(41,12,9),(1801,462,196),(8929,2256,24),(2521,644,16)]
    rows=[]
    for p,a,u in fixtures:
        need(is_prime(p),'fixture prime')
        rows.append(record(p,state(p,a,u)))
    p=2521;a=642;R=47
    cells=[dict(u=u,E=(4*u+1)%R==0,M=(u+a)%R==0) for u in square_divs(a)]
    need(len(cells)==27 and not any(c['E'] or c['M'] for c in cells),'cofactor swap obstruction')
    t=state(193,52,8)
    z=min(t[2],t[3])
    need(4*193<3*z*z+14*z-81,'hard condition is necessary')
    for n in range(30):
        r=14+210*n;s=3*r-9;p=4*r*s-r-s
        need(p%840==121 and gcd(r,s)==1 and 4*p==3*(r+s)**2+14*(r+s)-81,'sharp integer family')
    return dict(states=rows,cofactor_not_original_shell=dict(p=2521,a=a,R=R,
                factorization=[[2,1],[3,1],[107,1]],cells=cells),
                nonhard_counterexample=record(193,t),
                equality_family=dict(r='14+210n',s='3r-9',p='12r^2-40r+9',
                    n_domain='all integers n>=0; no infinitude of prime values asserted'))

def main() -> None:
    ap=argparse.ArgumentParser();ap.add_argument('--bound',type=int,default=3000)
    ap.add_argument('--out',type=Path,default=Path('certificates'))
    ap.add_argument('--grade-budget',type=int,default=50)
    args=ap.parse_args();args.out.mkdir(parents=True,exist_ok=True)
    need(args.bound>=41 and args.grade_budget>=1,'positive replay bounds')
    rows=[];state_count=0;hard_count=0;direct_tests=0;cofactor_tests=0
    for p in primes_to(args.bound):
        if p%8!=1:continue
        hard=p%840 in HARD
        expected=full_middle(p);actual,stats=atlas(p,hard)
        need(expected==actual,'complete two-chart equality at p='+str(p))
        for t in expected:
            z=min(t[2],t[3])
            need(4*p>=3*z*z+6*z-25,'general hyperbola bound')
            if hard:need(4*p>=3*z*z+14*z-81,'hard hyperbola bound')
        serial=[list(t) for t in sorted(expected)]
        rows.append(dict(p=p,hard=hard,oriented_by_r_lt_s_states=serial,
                          canonical_M_states=2*len(expected),**stats))
        state_count+=len(expected);hard_count+=int(hard)
        direct_tests+=stats['direct_candidate_tests'];cofactor_tests+=stats['cofactor_candidate_tests']
    examples=fixed_examples();grade=build_grade_example(args.grade_budget)
    outputs={'scan.json':dict(bound=args.bound,rows=rows),
             'examples.json':examples,'grade_certificate.json':grade}
    for name,obj in outputs.items():
        (args.out/name).write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')
    summary=dict(success=True,bound=args.bound,primes=len(rows),hard_primes=hard_count,
                 M_states_with_r_lt_s=state_count,canonical_oriented_M_states=2*state_count,
                 direct_candidate_tests=direct_tests,cofactor_candidate_tests=cofactor_tests,
                 universal_M_occupancy_proved=False,universal_ES_proved=False,
                 proof_scope='Full state bijection and bounds; finite replay is regression only',
                 output_sha256={n:hashlib.sha256((args.out/n).read_bytes()).hexdigest() for n in outputs})
    (args.out/'summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
    print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
