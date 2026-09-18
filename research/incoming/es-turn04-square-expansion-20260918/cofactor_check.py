#!/usr/bin/env python3
"""Complete finite reduction for square-source closed sets of at most five vertices.
Standard library only. This proves a finite enumeration after the bounds in core.tex;
it is not an exhaustive search over primes and it does not prove Erdős--Straus.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from collections import Counter
from functools import lru_cache, reduce
from itertools import product
from math import gcd, isqrt, prod
from pathlib import Path

HARD = frozenset((1,121,169,289,361,529))

def require(b: bool, message: str) -> None:
    if not b:
        raise ArithmeticError(message)

def sigma(q: int) -> int:
    if q % 2 != 1:
        raise ValueError('an odd vertex is required')
    return 1 if q % 4 == 3 else 3

def nonresidue(a: int, p: int) -> bool:
    return pow(a % p, (p-1)//2, p) == p-1

@lru_cache(maxsize=None)
def prime_test(n: int) -> tuple[bool,int]:
    """True,0, or False with an exact proper divisor (0 for n<2)."""
    if n < 2: return False,0
    for d in (2,3):
        if n == d: return True,0
        if n % d == 0: return False,d
    d=5
    while d*d <= n:
        if n % d == 0: return False,d
        if n % (d+2) == 0: return False,d+2
        d += 6
    return True,0

def factor(n: int) -> list[list[int]]:
    if n < 1: raise ValueError('positive factorization input required')
    out=[]; d=2
    while d*d <= n:
        if n % d == 0:
            e=0
            while n % d == 0: n//=d; e+=1
            out.append([d,e])
        d=3 if d==2 else d+2
    if n>1: out.append([n,1])
    return out

def raw(ss: tuple[int,...], cs: tuple[int,...]) -> tuple[int,list[int]]:
    """Return D-S and all T_i, retaining the cyclic starting point."""
    ell=len(ss)
    D=4**ell*prod(cs); S=prod(ss)
    ts=[]
    for i in range(ell):
        den=1; num=0
        for j in range(ell):
            k=(i+j)%ell
            num=ss[k]*num+den
            den*=4*cs[k]
        ts.append(num)
    return D-S,ts

def enumerate_profiles(m: int=5) -> dict:
    if m not in (2,3,4,5):
        raise ValueError('this finite checker is certified for 2 <= m <= 5')
    H=(2*m-1)**2
    counts=Counter(); digest=hashlib.sha256(); models=[]; cycles=set()
    per_length={}
    for ell in range(2,m+1):
        before=Counter(counts)
        for ss in product((1,3),repeat=ell):
            for v in range(1,(H+2)//4+1):
                cap=(v*H-1)//(4*v-3)
                require(cap>=v,'nonempty cofactor interval')
                counts['ambient_profiles']+=(cap-v+1)**(ell-1)
                def rec(pre: tuple[int,...]) -> None:
                    counts['tree_nodes']+=1
                    cs=pre+(v,)*(ell-len(pre))
                    den,ts=raw(ss,cs)
                    if any(s*T*H < 3*den for s,T in zip(ss,ts)):
                        counts['empty_boxes']+=1; return
                    if len(pre)==ell:
                        counts['range_profiles']+=1
                        digest.update(bytes((ell,)+ss+cs))
                        h=reduce(gcd,ts)
                        if den%h: return
                        p=den//h; qs=tuple(T//h for T in ts)
                        if p<1009 or p%840 not in HARD: return
                        counts['hard_profiles']+=1
                        if len(set(qs))!=ell or any(q<11 or q>=p or sigma(q)!=s for q,s in zip(qs,ss)):
                            return
                        counts['typed_profiles']+=1
                        model={'p':p,'vertices':list(qs),'sigma':list(ss),'cofactors':list(cs)}
                        for n in (p,)+qs:
                            prime,d=prime_test(n)
                            if not prime:
                                model['rejection']={'kind':'composite','n':n,'divisor':d}
                                models.append(model); return
                        counts['prime_profiles']+=1
                        for q in qs:
                            if not nonresidue(q,p):
                                model['rejection']={'kind':'quadratic_residue','q':q,'value':pow(q,(p-1)//2,p)}
                                models.append(model); return
                        counts['nonresidue_profiles']+=1
                        for i,q in enumerate(qs):
                            require(p+ss[i]*q==4*cs[i]*qs[(i+1)%ell],'cycle reconstruction')
                        model['rejection']=None;models.append(model)
                        shift=qs.index(min(qs)); cyc=qs[shift:]+qs[:shift]
                        cycles.add((p,cyc)); return
                    position=len(pre)
                    base=pre+(0,)+(v,)*(ell-position-1)
                    unit=pre+(1,)+(v,)*(ell-position-1)
                    d0,t0=raw(ss,base); d1,t1=raw(ss,unit)
                    upper=cap
                    for s,a0,a1 in zip(ss,t0,t1):
                        coefficient=3*(d1-d0)-s*H*(a1-a0)
                        rhs=s*H*a0-3*d0
                        if coefficient>0: upper=min(upper,rhs//coefficient)
                    counts['pruned_next_values']+=max(0,cap-upper)
                    for w in range(v,upper+1): rec(pre+(w,))
                rec((v,))
        per_length[str(ell)]=dict(counts-before)
    records=[]
    for p,cyc in sorted(cycles):
        ss=[sigma(q) for q in cyc]
        cs=[(p+ss[i]*q)//(4*cyc[(i+1)%len(cyc)]) for i,q in enumerate(cyc)]
        q=cyc[0];t=3;R=sigma(q)*q*t*t;A=(p+R)//4
        require(R<3*p,'square-nine source range')
        fs=factor(A);outside=[r for r,e in fs if nonresidue(r,p) and r not in cyc]
        require(bool(outside),'actual outside factor in candidate cycle')
        require(len(cyc)==m,'outside vertex raises cardinality beyond m')
        records.append({'p':p,'cycle':list(cyc),'sigma':ss,'cofactors':cs,
            'escape':{'q':q,'t':t,'R':R,'a':A,'factorization':fs,'outside_nonresidues':outside}})
    return {'schema':1,'m':m,'H':H,'counts':dict(counts),'per_length':per_length,
        'range_profile_sha256':digest.hexdigest(),'typed_models':models,
        'cycles':records,'conclusion':'No set of cardinality at most m is closed under all its valid first-m odd-square sources at any hard prime.',
        'scope':'All bounded coefficient profiles after the proved reduction. Canonical graphs alone can have closed components; ES is not resolved.'}

def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--m',type=int,default=5);ap.add_argument('--out',default='cofactor_certificate.json')
    args=ap.parse_args();data=enumerate_profiles(args.m)
    target=Path(args.out);target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(data,sort_keys=True,separators=(',',':'))+'\n')
    print(json.dumps({'m':data['m'],'counts':data['counts'],'range_profile_sha256':data['range_profile_sha256'],
        'cycle_count':len(data['cycles'])},sort_keys=True))
if __name__=='__main__': main()
