#!/usr/bin/env python3
"""Operational interface replay; imports the supplied repair implementation.

This is not the separate mathematical checker. It verifies exact JSON input
ordering and the public repair function on both orderings of every mixed trace.
"""
from __future__ import annotations
import argparse,json
from fractions import Fraction
from pathlib import Path
from repair import repair

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--input',type=Path,default=Path('certificates'))
    ap.add_argument('--out',type=Path,default=Path('interface.json'))
    ar=ap.parse_args();data=json.loads((ar.input/'scan.json').read_text());count=0
    for item in data['mixed']:
        src=item['source'];p=src['p'];a=src['a'];y,z=[Fraction(*d) for d in src['denominators'][1:]]
        for yy,zz in ((y,z),(z,y)):
            ret=repair(p,a,yy,zz)['ordered_middle_return']
            den=[Fraction(*x) for x in ret['denominators']]
            if ret['channel']!='M' or not ret['full'] or any(x.denominator!=1 for x in den):
                raise ArithmeticError('nonintegral public-interface return')
            if sum((1/x for x in den),Fraction())!=Fraction(4,p):raise ArithmeticError('identity')
            count+=1
    rejected=0
    for args in ((9601,2956,Fraction(14190278,3),Fraction(38404,3)),
                 (37,10,Fraction(10),Fraction(10))):
        try:repair(*args)
        except ValueError:rejected+=1
        else:raise ArithmeticError('out-of-domain input was accepted')
    out=dict(success=True,ordered_inputs_repaired=count,domain_rejections=rejected,
             imports_repair_implementation=True,independent_mathematical_checker=False)
    ar.out.parent.mkdir(parents=True,exist_ok=True);ar.out.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
