#!/usr/bin/env python3
"""Exact defect-preserving transport for split-box ES states.

Uses only the standard library and the accompanying exact arithmetic verifier.
No global assertion about a compactified six-manifold is used or checked.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
from itertools import product
import json
from math import gcd, prod
from pathlib import Path
import verify as arithmetic

CHECKS = Counter()
def check(ok, label):
    CHECKS[label] += 1
    if not ok:
        raise ArithmeticError(label)

def affine(g, v, R, puncture):
    x,y,z=v
    if puncture==0:
        ans=(6*g+y,-6*g-x-y,z-2*g+x)
    elif puncture==1:
        ans=(-y,x-6*g,z+3*g+y)
    elif puncture==2:
        ans=(x,y+x,z-g)
    else:
        raise ValueError('puncture must be 0, 1, or 2')
    return tuple(t%R for t in ans)

def scaling(v,k,R): return tuple(k*t%R for t in v)

def record(p,a,f,xi,eta,kind):
    fe=arithmetic.factor(a)
    qs=tuple(q for q,e in fe); e=tuple(e for q,e in fe)
    h=tuple(ei-fi for ei,fi in zip(e,f)); R=4*a-p
    check(len(f)==len(xi)==len(eta)==len(e),'typed_lengths')
    check(all(0<=fi<=ei for fi,ei in zip(f,e)),'retained_budget')
    check(all(-fi<=x<=fi for x,fi in zip(xi,f)),'retained_exponents')
    check(all(-hi<=x<=hi for x,hi in zip(eta,h)),'removed_exponents')
    targets=dict(arithmetic.target_labels(p,R))
    if kind not in targets: raise ValueError('unknown target label')
    beta=tuple(x+y for x,y in zip(xi,eta))
    x=arithmetic.residue(qs,xi,R);w=arithmetic.residue(qs,eta,R)
    residual=(x-targets[kind]*pow(w,-1,R))%R
    normalized=tuple(-b for b in beta) if kind=='E-inverse' else beta
    u=prod(q**(ei+bi) for q,ei,bi in zip(qs,e,normalized))
    if kind=='M':
        gate=u+a;unit=a*w%R
        den=(Fraction(a),Fraction(p*(a+a*a//u),R),Fraction(p*(a+u),R))
    else:
        gate=4*u+1;unit=(p*w)%R if kind=='E-direct' else pow(x,-1,R)
        den=(Fraction(a),Fraction(p*a+a*a//u,R),Fraction(p*a+p*p*u,R))
    check(gcd(unit,R)==1,'unit_multiplier')
    check(gate%R==unit*residual%R,'gate_unit_identity')
    D=R//gcd(R,gate)
    check(D==R//gcd(R,residual),'same_defect')
    check(den[1].denominator==den[2].denominator==D,'common_reduced_denominator')
    check(sum((1/t for t in den),Fraction())==Fraction(4,p),'rational_ES')
    for ell,power in arithmetic.factor(R):
        mod=ell**power
        check(mod//gcd(mod,gate)==mod//gcd(mod,residual),'same_prime_power_defect')
    for v in ((0,0,0),(1,0,0),(0,1,0),(0,0,1)):
        for j in range(3):
            check(scaling(affine(residual,v,R,j),unit,R)==
                  affine(gate,scaling(v,unit,R),R,j),'affine_intertwiner_on_basis')
        check(scaling(scaling(v,unit,R),pow(unit,-1,R),R)==v,'inverse_on_basis')
    g0=gcd(a,u);r=u//g0;s=a//g0;scale=g0*g0//u
    quotient=Fraction(r+s,R) if kind=='M' else Fraction(p*r+s,R)
    return dict(p=p,a=a,R=R,prime_factorization=[list(z) for z in fe],
                retained=list(f),removed=list(h),xi=list(xi),eta=list(eta),
                beta=list(beta),normalized_beta=list(normalized),label=kind,
                residue=x,removed_residue=w,target=targets[kind],residual=residual,
                unit=unit,inverse_unit=pow(unit,-1,R),gate=gate,defect=D,u=u,
                channel='M' if kind=='M' else 'E',h=scale,r=r,s=s,
                quotient=[quotient.numerator,quotient.denominator],
                denominators=[[t.numerator,t.denominator] for t in den])

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',default='transport.json')
    args=parser.parse_args()
    states=0; success=0; failures=0
    for p in (5,13,37,61,97):
        for a in range((p+3)//4,(p-1)//2+1):
            e=tuple(k for q,k in arithmetic.factor(a))
            for f in product(*(range(ei+1) for ei in e)):
                h=tuple(ei-fi for ei,fi in zip(e,f))
                for xi in arithmetic.box(f):
                    for eta in arithmetic.box(h):
                        for kind in ('M','E-direct','E-inverse'):
                            row=record(p,a,f,xi,eta,kind)
                            states+=1
                            if row['defect']==1: success+=1
                            else: failures+=1
    examples=[record(1201,312,(2,1,1),(-2,1,1),(-1,0,0),'M'),
              record(37,18,(1,1),(-1,-1),(0,-1),'E-direct'),
              record(37,18,(1,1),(-1,-1),(0,-1),'M'),
              record(37,18,(1,1),(-1,-1),(0,-1),'E-inverse')]
    # Exhaust all points for representative level/unit pairs, independent of
    # the basis test. This checks finite maps, not complex compactification.
    exhaustive=0
    for R in (3,5,9,15):
        units=[k for k in range(1,R) if gcd(k,R)==1]
        for unit in units:
            for g in (0,1,R-1):
                for v in product(range(R),repeat=3):
                    for j in range(3):
                        check(scaling(affine(g,v,R,j),unit,R)==
                              affine(unit*g,scaling(v,unit,R),R,j),
                              'complete_finite_affine_intertwiner')
                        exhaustive+=1
    out=Path(args.out);out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(dict(states=states,successful_states=success,
                                  failed_states=failures,complete_affine_checks=exhaustive,
                                  examples=examples,checks=dict(CHECKS)),
                              indent=2,sort_keys=True)+'\n',encoding='utf8')
    print(json.dumps(dict(states=states,checks=sum(CHECKS.values())),sort_keys=True))
if __name__=='__main__': main()
