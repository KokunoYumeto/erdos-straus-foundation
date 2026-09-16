#!/usr/bin/env python3
"""Independent finite coefficient check for the two fixed-modulus Dirichlet series.
No numerical evaluation of infinite series and no third-party imports.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction
from math import gcd,isqrt
from pathlib import Path
import argparse,json

def require(ok,label):
    if not ok:raise ArithmeticError(label)

def primes(N):
    return [p for p in range(2,N+1) if all(p%d for d in range(2,isqrt(p)+1))]

def conv(A,B,R):
    out=Counter()
    for x,v in A.items():
        for y,w in B.items():out[x*y%R]+=v*w
    return dict(out)

def check(N):
    counts=Counter()
    for R in (3,7,11,15,23,27,35):
        for c in ('E','M'):
            # Local geometric-product coefficients: two nonnegative indices and one bit.
            source={1:{1:1}}
            for p in primes(N):
                if R%p==0:continue
                local=[];pe=1;e=0
                while pe<=N:
                    P=Counter()
                    for eps in (0,1):
                        for j in range(e+1):
                            k=e-j-eps
                            if k<0:continue
                            exponent=2*k+eps if c=='E' else j-k
                            P[pow(p,exponent,R)]+=1
                    require(sum(P.values())==2*e+1,'local original mass')
                    local.append((pe,dict(P)));pe*=p;e+=1
                new={}
                for n,Q in source.items():
                    for pe,P in local:
                        if n*pe<=N:new[n*pe]=conv(Q,P,R)
                source=new
            for a in range(1,N+1):
                if gcd(a,R)!=1:
                    require(a not in source,'nonunit integer excluded');continue
                brute=Counter()
                for u in range(1,a*a+1):
                    if a*a%u==0:
                        g=u%R if c=='E' else u*pow(a,-1,R)%R
                        brute[g]+=1
                require(source[a]==dict(brute),'finite Euler coefficients equal original divisor counts')
                counts['integers_per_channel_modulus']+=1
            # Formal character identity using a generic unit h, so no floating roots.
            for g in range(1,R):
                if gcd(g,R)!=1:continue
                for e in range(10):
                    # E: numerator (1-z^2 h^2) against three geometric factors.
                    if c=='E':
                        rhs=Counter()
                        for offset,sign in ((0,1),(2,-1)):
                            for i in range(e-offset+1):
                                for j in range(e-offset-i+1):
                                    k=e-offset-i-j
                                    rhs[pow(g,j+2*k+offset,R)]+=sign
                    else:
                        # (1+z)/((1-z h)(1-z/h))
                        rhs=Counter()
                        for eps in (0,1):
                            for j in range(e-eps+1):
                                k=e-eps-j
                                rhs[pow(g,j-k,R)]+=1
                    rhs={x:n for x,n in rhs.items() if n}
                    orig=Counter(pow(g,j,R) for j in (range(2*e+1) if c=='E' else range(-e,e+1)))
                    require(rhs==dict(orig),'character Euler factor identity')
                    counts['local_factor_coefficients']+=1
    return {'bound':N,'scope':'exact Dirichlet coefficients for a<=bound; fixed residuals 3,7,11,15,23,27,35',
            'counts':dict(counts),'nonclaims':['No numerical infinite sum used','No pointwise occupancy inferred from an Euler product']}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--bound',type=int,default=120);ap.add_argument('--out',default='dirichlet_verification.json');a=ap.parse_args()
    if a.bound<2:ap.error('bound >=2 required')
    out=check(a.bound);Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out['counts'],sort_keys=True))
if __name__=='__main__':main()
