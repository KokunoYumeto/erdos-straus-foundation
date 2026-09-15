#!/usr/bin/env python3
"""Separate residue-space checker. Does not import verify.py.

It uses bounded knapsack instead of prefix inequalities, direct modular blocks
instead of the logarithmic gap threshold, and residue convolution instead of
explicit divisor enumeration. This is a second implementation, not independent
mathematical peer review.
"""
import argparse
from collections import Counter
from functools import lru_cache
from hashlib import sha256
from math import gcd, isqrt, prod
from pathlib import Path
import json

CHECKS = 0
HARD = {1,121,169,289,361,529}


def check(x, name):
    global CHECKS
    CHECKS += 1
    if not x:
        raise ArithmeticError(name)


def sieve(n):
    a = bytearray(b'\1')*(n+1)
    a[:2] = b'\0\0'
    for i in range(2,isqrt(n)+1):
        if a[i]: a[i*i::i] = b'\0'*len(a[i*i::i])
    return [i for i in range(2,n+1) if a[i]]


TRIAL = sieve(10000)


@lru_cache(None)
def factors(n):
    out=[]
    for q in TRIAL:
        if q*q>n:break
        j=0
        while n%q==0:n//=q;j+=1
        if j:out.append((q,j))
    if n>1:out.append((n,1))
    return tuple(out)


def v2(n):
    if not n:raise ValueError('nonzero integer required')
    return (n&-n).bit_length()-1


def residue_count(fs,m):
    hist={1:1}
    for q,e in fs:
        hh=Counter()
        for r,c in hist.items():
            z=r
            for _ in range(e+1):
                hh[z]+=c
                z=z*q%m
        hist=hh
    return hist


def socle_test(p,k,fs,inside):
    n=k-2;target=(1<<n)-1
    limits=[]
    for q,e in fs:
        if q%8 not in inside:continue
        if q%8==1:
            v=v2(q-1)-2
            if v>=n:continue
            w=1<<v
        else:w=1
        limits.append((w,e))
    v=v2(p-1)-2
    if v<n:limits.append((1<<v,1))
    possible=1;mask=(1<<(target+1))-1
    for w,e in limits:
        total=0
        for j in range(min(e,target//w)+1):total|=possible<<(j*w)
        possible=total&mask
    return bool(possible>>target&1) and any(q%8 not in inside for q,e in fs)


@lru_cache(None)
def cyclic(g,m):
    r=1;H={1}
    while True:
        r=r*g%m
        if r==1:return frozenset(H)
        H.add(r)


@lru_cache(None)
def avoiding(m):
    H={cyclic(g,m) for g in range(1,m,2) if m-1 not in cyclic(g,m)}
    return sorted(H,key=lambda h:(len(h),sorted(h)))


@lru_cache(None)
def proj_cycle(q,m,H):
    return frozenset(min(a*x%m for a in H) for x in cyclic(q,m))


def subgroup_test(p,m,fs):
    for H in avoiding(m):
        d=(m//2)//len(H);t=1 if p%m in H else 2
        n=sum(e for q,e in fs if q%m not in H)
        if n>d-1-t:continue
        counts=Counter()
        for q,e in fs:
            if q%m not in H:counts[proj_cycle(q%m,m,H)]+=e
        if any(c>=len(K)-1 for K,c in counts.items()):continue
        return False
    return True


def run(bound):
    if bound < 2:
        raise ValueError('bound must be at least 2')
    global TRIAL
    TRIAL = sieve(isqrt(3*bound))
    factors.cache_clear()
    C=Counter();names=('old_two_block','socle','subgroup_forcing','old_plus_socle','short_both_roles','fair_baseline','fair_plus_socle','actual')
    P={name:set() for name in names};rows=[]
    for p in sieve(bound):
        if p%840 not in HARD:continue
        C['hard_primes']+=1;k=4
        while p>2*(1<<(2*k-5)):
            m=1<<k;N=p+(1<<(2*k-3));fs=factors(N)
            check(prod(q**e for q,e in fs)==N,'independent full factorization')
            hist=residue_count(fs,m);hits=hist.get(m-1,0)
            check(sum(hist.values())==prod(e+1 for q,e in fs),'original exponent-box mass')
            f=dict(fs)
            S={pow(3,i,m)*pow(11,j,m)%m for i in range(f.get(3,0)+1) for j in range(f.get(11,0)+1)}
            S|={x*pow(p,-1,m)%m for x in list(S)}
            H=cyclic(3,m)
            old=any(q%8 in (5,7) for q,e in fs) and S==H
            top=socle_test(p,k,fs,(1,3)) or socle_test(p,k,fs,(1,5))
            T={m-1,(-p)%m}
            short=any(q%m in T for q,e in fs) or any(q*r%m in T for i,(q,e) in enumerate(fs) for j,(r,f0) in enumerate(fs) if j>i or j==i and e>=2)
            sg=subgroup_test(p,m,fs)
            check(not(old or top or short or sg) or hits>0,'independent positive certificate')
            vals=dict(old_two_block=old,socle=top,subgroup_forcing=sg,old_plus_socle=old or top,short_both_roles=short,fair_baseline=old or short,fair_plus_socle=old or short or top,actual=hits>0)
            C['branches']+=1;C['original_middle_states']+=hits
            for name,yes in vals.items():
                C[name+'_branches']+=yes
                if yes:P[name].add(p)
            rows.append([p,k,N,fs,int(old),int(top),int(sg),int(short),hits])
            k+=1
    for key in names:C[key+'_primes']=len(P[key])
    digest=sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()
    return dict(bound=bound,checks=CHECKS,totals=dict(C),row_digest=digest,
                methods=['bounded knapsack','direct residue blocks','multiplicative residue convolution','enumerated cyclic subgroups'])


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--bound',type=int,default=2000000);p.add_argument('--out',default='independent.json');p.add_argument('--compare')
    a=p.parse_args();r=run(a.bound)
    if a.compare:
        main=json.loads(Path(a.compare).read_text())
        check(r['row_digest']==main['row_digest'] and r['totals']==main['totals'],'complete main comparison')
        r['checks']=CHECKS;r['comparison_identical']=True
    Path(a.out).write_text(json.dumps(r,indent=2,sort_keys=True)+'\n')
    print(json.dumps(r,sort_keys=True))
if __name__=='__main__':main()
