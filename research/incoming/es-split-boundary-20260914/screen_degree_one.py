#!/usr/bin/env python3
"""Independent integer-only screen of first-degree sufficiency.
This is a finite converse test, not a universal theorem or new prime coverage.
Normal and optimized modes use the same explicit checks. No imports from verify.py.
"""
from collections import Counter
from functools import lru_cache
from math import gcd,isqrt
import argparse,json
from pathlib import Path

@lru_cache(None)
def divisors_square(a):
    out=[1];q=2;n=a
    while q*q<=n:
        e=0
        while n%q==0:n//=q;e+=1
        if e:out=[d*q**i for d in out for i in range(2*e+1)]
        q=3 if q==2 else q+2
    if n>1:out=[d*n**i for d in out for i in range(3)]
    return out

def screen(N):
    if N<13:raise ValueError('bound >= 13 required')
    prime=bytearray(b'\x01')*(N+1);prime[:2]=b'\0\0'
    for q in range(2,isqrt(N)+1):
        if prime[q]:prime[q*q::q]=b'\0'*len(prime[q*q::q])
    stats=Counter();counterexamples=[]
    for p in range(13,N+1,12):
        if not prime[p]:continue
        stats['primes']+=1
        for a in range((p+3)//4,(p-1)//2+1):
            R=4*a-p
            hist=Counter(gcd(R,g) for u in divisors_square(a) for g in (4*u+1,u+a))
            stats['shells']+=1;stats['canonical_states']+=sum(hist.values())
            hits=hist[R];stats['success_states']+=hits
            if not hits:stats['empty_shells']+=1;continue
            stats['occupied_shells']+=1
            S=[sum(n*d**j for d,n in hist.items()) for j in range(4)]
            A=3*S[1]-R*S[0];B=3*S[2]-R*S[1];C=3*S[3]-R*S[2]
            fails=(A<=0 and C<=0 and A*C>=B*B)
            if fails:
                stats['occupied_not_forced_degree_one']+=1
                counterexamples.append(dict(p=p,a=a,R=R,hits=hits,gcd_multiplicities=sorted(hist.items()),
                                            S=S,localizer_integer_entries=[A,B,C]))
            else:stats['occupied_forced_degree_one']+=1
    return dict(bound=N,scope='all first-half shells, prime p=1 mod12; first-degree converse only',
                counts=dict(stats),counterexamples=counterexamples,
                nonclaims=['Not a universal equivalence','Not a new ES prime coverage claim',
                           'Moments calculated from complete actual divisor enumeration',
                           'Independent implementation, not independent mathematical review'])

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--bound',type=int,default=10000)
    p.add_argument('--out',default='degree_one_screen.json');a=p.parse_args()
    result=screen(a.bound);Path(a.out).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result['counts'],sort_keys=True))
if __name__=='__main__':main()
