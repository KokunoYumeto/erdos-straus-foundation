#!/usr/bin/env python3
"""Exact all-octad inverse with the necessary-and-sufficient mod-four test.
A trace JSON is a list of 759 integers, with octads ordered by increasing bitmask.
"""
from __future__ import annotations
import argparse,json
from fractions import Fraction
from pathlib import Path
from verify_audit import golay,member,norm

def inverse(a):
    _,code=golay();octads=sorted(v for v in code if v.bit_count()==8)
    if not isinstance(a,list) or len(a)!=759 or any(type(z) is not int for z in a):
        raise ValueError('Expected exactly 759 integer trace values')
    S=sum(a);Si=[sum(v for v,B in zip(a,octads) if B>>i&1) for i in range(24)]
    x=[Fraction(23*Si[i]-7*S,1012) for i in range(24)]
    if any(Fraction(sum(x[i] for i in range(24) if B>>i&1),4)!=v for B,v in zip(octads,a)):
        raise ValueError('Trace data violate the exact real image equations')
    delta=Fraction(11*S-23*Si[0],506)
    if delta.denominator!=1:raise ArithmeticError('Compatible integral data produced a nonintegral syndrome')
    if int(delta)%4:raise ValueError(f'No Leech lift: exact obstruction is {int(delta)%4} modulo 4')
    if any(v.denominator!=1 for v in x):raise ArithmeticError('Zero syndrome did not give integral coordinates')
    z=[int(v) for v in x]
    if not member(z,code):raise ArithmeticError('Zero syndrome did not give a Leech vector')
    return {'numerator':z,'scale':'1/sqrt(8)','norm_squared':str(norm(z)),'syndrome_mod4':0,'unique':True}
def main():
    p=argparse.ArgumentParser(description=__doc__);g=p.add_mutually_exclusive_group(required=True)
    g.add_argument('--traces',type=Path);g.add_argument('--constant',type=int);g.add_argument('--self-test',action='store_true');a=p.parse_args()
    if a.self_test:
        if inverse([4]*759)['numerator']!=[2]*24:raise ArithmeticError('Constant-four inverse failed')
        try:inverse([1]*759)
        except ValueError as exc:
            if 'obstruction' not in str(exc):raise
        else:raise ArithmeticError('Constant-one obstruction was missed')
        print(json.dumps({'status':'PASS','constant_one_rejected':True,'constant_four_returned':True},sort_keys=True));return
    data=json.loads(a.traces.read_text()) if a.traces else [a.constant]*759
    print(json.dumps(inverse(data),indent=2,sort_keys=True))
if __name__=='__main__':main()
