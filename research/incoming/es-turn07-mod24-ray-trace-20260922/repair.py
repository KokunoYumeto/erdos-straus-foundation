#!/usr/bin/env python3
"""Repair an actual rational trace source in the proved c*q domain.

This command is not a solver promised to find an initial source for every p.
Inputs use exact Fraction strings. The complete marked output is JSON.
"""
from __future__ import annotations
import argparse
import json
from fractions import Fraction
from pathlib import Path
import verify as v

def repair(p: int, a: int, y: Fraction, z: Fraction) -> dict:
    if not v.prime_trial(p) or p % 24 != 1:
        raise ValueError('p must be prime and congruent to 1 modulo 24')
    if not p < 4*a < 2*p or y <= 0 or z <= 0:
        raise ValueError('positive tails and the original first-half shell are required')
    if Fraction(1,a)+1/y+1/z != Fraction(4,p) or (y+z).denominator != 1:
        raise ValueError('the exact reciprocal identity and integral tail trace are required')
    carriers=[(c,a//c) for c in (1,2,3,6)
              if a%c==0 and a//c>3 and v.prime_trial(a//c)]
    if len(carriers)!=1:
        raise ValueError('a must have the proved form c*q, c in {1,2,3,6}, q>3 prime')
    R=4*a-p
    b,c=R*y-p*a,R*z-p*a
    if b.denominator!=1 or c.denominator!=1 or b*c!=(p*a)**2 or b<=0 or c<=0:
        raise ArithmeticError('factor-source reconstruction failed')
    b,c=int(b),int(c)
    swapped=False
    if b%p:
        channel='E';u=a*a//b
    elif c%p:
        channel='E';u=a*a//c;swapped=True
    else:
        channel='M';u=p*a*a//b
    src=v.state(p,a,u,channel)
    original=list(reversed(src['denominators'][1:])) if swapped else src['denominators'][1:]
    if original != [v.fr(y),v.fr(z)]:
        raise ArithmeticError('input-order reconstruction failed')
    data=v.mixed_reduction(src,*carriers[0])
    target=data['middle']
    if swapped:
        target=v.fullstate(p,target['a'],target['a']**2//target['u'],'M')
    return dict(input=dict(p=p,a=a,y=v.fr(y),z=v.fr(z),tail_trace=v.fr(y+z)),
                input_exterior_swap=swapped,normalization_and_map=data,
                ordered_middle_return=target,universal_initial_source_claim=False)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--p',type=int,required=True);ap.add_argument('--a',type=int,required=True)
    ap.add_argument('--y',required=True);ap.add_argument('--z',required=True)
    ap.add_argument('--out',type=Path)
    ar=ap.parse_args()
    try:data=repair(ar.p,ar.a,Fraction(ar.y),Fraction(ar.z))
    except (ValueError,ArithmeticError,ZeroDivisionError) as error:ap.error(str(error))
    text=json.dumps(data,indent=2,sort_keys=True)+'\n'
    if ar.out:ar.out.parent.mkdir(parents=True,exist_ok=True);ar.out.write_text(text)
    else:print(text,end='')
if __name__=='__main__':main()
