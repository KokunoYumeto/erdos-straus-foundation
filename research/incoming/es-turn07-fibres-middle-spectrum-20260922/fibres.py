#!/usr/bin/env python3
"""Exact inverse fibres of the corrected mixed-trace return. Standard library.
No assertion of universal Erdős--Straus occupancy is made.
"""
from __future__ import annotations
import argparse
import json
from fractions import Fraction as F
from functools import lru_cache
from math import gcd, isqrt, prod
from typing import Any


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


@lru_cache(None)
def prime(n: int) -> bool:
    if n < 2: return False
    if n % 2 == 0: return n == 2
    return all(n % d for d in range(3, isqrt(n) + 1, 2))


@lru_cache(None)
def factors(n: int) -> tuple[tuple[int, int], ...]:
    require(n >= 1, 'factor input must be positive')
    ans = []; l = 2
    while l*l <= n:
        if n % l == 0:
            e = 0
            while n % l == 0:
                n //= l; e += 1
            ans.append((l,e))
        l = 3 if l == 2 else l+2
    if n > 1: ans.append((n,1))
    return tuple(ans)


def divs(n: int, power: int = 1) -> list[int]:
    out = [1]
    for l,e in factors(n):
        out = [d*l**k for d in out for k in range(power*e+1)]
    return sorted(out)


def squarefree_part(n: int) -> int:
    return prod(l for l,e in factors(n) if e % 2)


def oddpart(n: int) -> int:
    while n % 2 == 0: n //= 2
    return n


def carrier(a: int) -> tuple[int,int] | None:
    """The unique c,q with c|6 and q>3 prime; absence is an exact failed test."""
    found = [(c,a//c) for c in (1,2,3,6)
             if a % c == 0 and a//c > 3 and prime(a//c)]
    require(len(found) <= 1, 'carrier uniqueness')
    return found[0] if found else None


def normalize(a: int, u: int) -> tuple[int,int,int]:
    require(a > 0 and u > 0 and a*a % u == 0, 'original square-divisor budget')
    g = gcd(a,u)
    require(g*g % u == 0, 'integral gcd grade')
    h,r,s = g*g//u,u//g,a//g
    require(h*r*s == a and h*r*r == u and gcd(r,s) == 1, 'normalization identities')
    return h,r,s


def tails(p: int, a: int, u: int, channel: str) -> tuple[F,F]:
    require(p < 4*a < 2*p and a*a % u == 0, 'first-half original source')
    R = 4*a-p
    if channel == 'E':
        return F(p*a+a*a//u,R),F(p*a+p*p*u,R)
    require(channel == 'M','channel must be E or M')
    return F(p*(a+a*a//u),R),F(p*(a+u),R)


def fr(x: F | int) -> list[int]:
    x=F(x);return [x.numerator,x.denominator]


def box(a: int,u: int) -> list[list[int]]:
    out=[]
    for l,e in factors(a):
        v=u;f=0
        while v%l==0: v//=l;f+=1
        out.append([l,e,f,f-e])
    return out


def source_record(p: int,a: int,u: int,channel: str,swap: int=0) -> dict[str,Any]:
    cq=carrier(a);require(cq is not None,'source is outside the mixed carrier domain')
    require(p%24==1 and prime(p),'source prime class')
    require(swap in (0,1) and (channel=='E' or swap==0),'orientation encoding')
    h,r,s=normalize(a,u); y,z=tails(p,a,u,channel); R=4*a-p
    require((y+z).denominator==1,'source trace is not integral')
    if swap:y,z=z,y
    require(F(1,a)+1/y+1/z==F(4,p),'source reciprocal identity')
    G=4*u+1 if channel=='E' else p+4*u
    d=R//gcd(R,G)
    require(y.denominator==z.denominator==d,'source exact tail denominator')
    return dict(p=p,a=a,R=R,u=u,channel=channel,swap=swap,c=cq[0],q=cq[1],
                h=h,r=r,s=s,quotient=fr(F(p*r+s if channel=='E' else r+s,R)),
                tails=[fr(y),fr(z)],defect=d,box=box(a,u))


def source_key(rec: dict[str,Any]) -> tuple[int,int,str,int,int]:
    return rec['p'],rec['a'],rec['channel'],rec['u'],rec['swap']


def target(p:int,a:int,Y:int,Z:int) -> dict[str,Any]:
    require(p%24==1 and prime(p),'target prime class')
    require(p<4*a<2*p and a<Y<Z and Y%p==Z%p==0,'target sorted M domain')
    require(F(1,a)+F(1,Y)+F(1,Z)==F(4,p),'target reciprocal identity')
    b,c=Y//p,Z//p; g=gcd(b,c); r,s=b//g,c//g
    require(a%(r*s)==0,'primitive target grade')
    h=a//(r*s); require(g%h==0,'target lambda'); lam=g//h
    require(h*r*lam==b and h*s*lam==c and r+s==(4*a-p)*lam,'target normalization')
    return dict(p=p,a=a,Y=Y,Z=Z,R=4*a-p,h=h,r=r,s=s,lam=lam,
                small_word=h*r*r,large_word=h*s*s)


def target_key(W:dict[str,Any])->tuple[int,int,int,int]:
    return W['p'],W['a'],W['Y'],W['Z']


def forward(rec:dict[str,Any])->dict[str,Any]:
    """The corrected pinned map; the final sorting intentionally forgets source orientation."""
    p,a,R,u=rec['p'],rec['a'],rec['R'],rec['u']; delta=squarefree_part(R)
    if rec['channel']=='E':
        r,s=rec['r'],rec['s']; require(6%(r*s)==0,'automatic ray')
        require((delta+1)%(4*r*s)==0 and (p*r+s)%delta==0,'E squarefree target')
        H=(delta+1)//(4*r*s); J=(p*r+s)//delta
        ap=H*s*J; yy=p*H*J*r; zz=p*H*s*r
    else:
        q=rec['q']; u0=u if u%q else a*a//u
        require(36%u0==0,'M small word')
        ap=(p+delta)//4; require(ap*ap%u0==0,'new M budget')
        yy,zz=tails(p,ap,u0,'M'); require(yy.denominator==zz.denominator==1,'new M gate')
        yy,zz=int(yy),int(zz)
    return target(p,ap,min(yy,zz),max(yy,zz))


def inverse_fibre(W:dict[str,Any]) -> list[dict[str,Any]]:
    """All ordered rational mixed inputs giving this bare sorted middle target."""
    p,a,R,h,r,s,lam=(W[k] for k in ('p','a','R','h','r','s','lam'))
    out=[]
    # E-origin branch. The unsorted source ray is (lambda,r).
    de=4*h*r*lam-1
    if 6%(r*lam)==0 and squarefree_part(de)==de:
        for t in divs(oddpart(s)):
            oldR=de*t*t
            if oldR>=p:continue
            olda=(p+oldR)//4
            if carrier(olda) is None:continue
            require(olda%(r*lam)==0,'E reverse shell budget')
            hu=olda//(r*lam); old_u=hu*lam*lam
            for swap in (0,1):
                rec=source_record(p,olda,old_u,'E',swap)
                rec.update(fibre_branch='E',t=t,delta=de)
                require(target_key(forward(rec))==target_key(W),'E reverse composition')
                out.append(rec)
    # M-origin branches; keep both possible target words before testing |36.
    if squarefree_part(R)==R:
        for nu in sorted({h*r*r,h*s*s}):
            if 36%nu:continue
            require((p+4*nu)%R==0,'target seed gate')
            A=(p+4*nu)//R
            for t in divs(A):
                oldR=R*t*t
                if t%2==0 or oldR>=p:continue
                olda=(p+oldR)//4; cq=carrier(olda)
                if cq is None or (cq[0]*cq[0])%nu:continue
                require(olda*olda%nu==0,'M reverse budget')
                for bit,old_u in enumerate((nu,olda*olda//nu)):
                    rec=source_record(p,olda,old_u,'M')
                    rec.update(fibre_branch='M',t=t,delta=R,seed=nu,complement=bit)
                    require(target_key(forward(rec))==target_key(W),'M reverse composition')
                    out.append(rec)
    require(len({source_key(x) for x in out})==len(out),'fibre disjointness')
    return sorted(out,key=source_key)


def cli()->None:
    q=argparse.ArgumentParser(description=__doc__)
    q.add_argument('--target',type=int,nargs=4,metavar=('P','A','Y','Z'),required=True)
    q.add_argument('--out',type=str)
    args=q.parse_args(); W=target(*args.target); records=inverse_fibre(W)
    ans=dict(target=W,ordered_source_count=len(records),sources=records,
             universal_occupancy_claim=False)
    data=json.dumps(ans,indent=2,sort_keys=True)+'\n'
    if args.out:
        from pathlib import Path
        Path(args.out).write_bytes(data.encode('utf-8'))
    else:print(data,end='')

if __name__=='__main__':cli()
