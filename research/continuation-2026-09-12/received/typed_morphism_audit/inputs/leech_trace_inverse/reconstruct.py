#!/usr/bin/env python3
"""Construct an exact Leech inverse from 3 traces or 4 common-sum triples.
Examples:
  python reconstruct.py --trace 306 16218 1082101 --p 1201
  python reconstruct.py --four 1 2 3 2 3 1 3 2 1 1 4 1
The result is a vector numerator; the actual vector is numerator/sqrt(8).
Certificates ship with this script and are independently checked by verify.py.
"""
from __future__ import annotations
import argparse,json
from fractions import Fraction
from pathlib import Path
from verify import member,binary_basis,words,mask
BASE=Path(__file__).resolve().parent/'certificates'

def code():
    qr={j*j%23 for j in range(1,23)}
    return set(words(binary_basis([(1<<23)|mask({(a+q)%23 for q in qr}) for a in range(23)])))

def read(name):return json.loads((BASE/name).read_text(encoding='utf8'))
def linear(a,rows):return [sum(c*r[i] for c,r in zip(a,rows)) for i in range(24)]

def main():
    ap=argparse.ArgumentParser(description=__doc__);g=ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--trace',type=int,nargs=3);g.add_argument('--four',type=int,nargs=12)
    ap.add_argument('--p',type=int);args=ap.parse_args()
    if args.trace is not None:
        t=args.trace;r=[x%4 for x in t];rows=read('shortest_lifts.json')['classes']
        cert=next(x for x in rows if x['residue_mod4']==r)
        a=cert['reduced_trace'];n=[(t[i]-a[i])//4 for i in range(3)]
        plus=linear(n,read('trace_frame.json')['frame_W'])
        x=[v+w for v,w in zip(cert['representative_numerator'],plus)]
        out={'trace':t,'norm_is_minimal_in_trace_fibre':True,'mu':str(Fraction(cert['mu_times4'],4))}
    else:
        views=[args.four[3*i:3*i+3] for i in range(4)]
        if len({sum(v) for v in views})!=1:raise SystemExit('The four triples must have the same sum; this is the proved exact codomain.')
        a=views[0]+views[1][:2]+views[2][:2]+views[3][:2]
        x=linear(a,read('twelve_views.json')['right_inverse_numerators'])
        t=views[0];out={'four_independent_time_triples':views,'norm_is_minimal_in_trace_fibre':False}
    if not member(x,code()):raise ArithmeticError('Certificate data failed Leech membership')
    blocks=read('trace_frame.json')['octads']
    got=[sum(x[i] for i in bb)//4 for bb in blocks]
    if got!=t:raise ArithmeticError('Certificate data failed trace return')
    out.update(numerator=x,scale='1/sqrt(8)',norm_squared=sum(a*a for a in x)//8)
    if args.p is not None:
        p=args.p;a,b,c=t;f=4*a*b*c-p*(a*b+a*c+b*c)
        out.update(p=p,ES_defect=f,positive_ES_identity=(p>0 and min(t)>0 and f==0))
    print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__':main()
