#!/usr/bin/env python3
"""Checked three-trace / four-view inverse; Python standard library only.
All external certificate fields are untrusted. Verifies all twelve time readings.
Numerators represent lattice vectors divided by sqrt(8).
"""
from __future__ import annotations
import argparse,json
from fractions import Fraction
from pathlib import Path
from verify_audit import BLOCKS,LIFTS9,T,mv,act,trace,trace9,member,golay,norm,combine
BASE=Path(__file__).resolve().parent/'inputs'/'leech_trace_inverse'/'certificates'
def require(ok:bool,message:str)->None:
    if not ok:raise ValueError(message)
def load(base:Path,name:str):
    return json.loads((base/name).read_text(encoding='utf8'))
def require_vector(x):
    require(isinstance(x,(list,tuple)) and len(x)==24 and all(type(v) is int for v in x),'Invalid integral 24-coordinate certificate')
def expected_mu4(r):
    a=[v if v<=2 else -1 for v in r]
    return a,0 if all(v==0 for v in r) else 12 if all(v==2 for v in r) else 16-sum(v*v for v in a)
def all_views(x):
    ans=[];g=mv(T)
    for _ in range(12):ans.append(trace(x));x=act(x,g)
    return ans

def inverse_trace(t,base,code):
    r=[v%4 for v in t];a,mu4=expected_mu4(r)
    certs=load(base,'shortest_lifts.json')['classes']
    matches=[c for c in certs if c.get('residue_mod4')==r]
    require(len(matches)==1,'Missing or duplicate residue certificate')
    c=matches[0];v=c['representative_numerator'];require_vector(v)
    require(c.get('reduced_trace')==a and c.get('mu_times4')==mu4,'Wrong reduced trace or shortest-height constant')
    require(member(v,code),'Representative is outside the Leech lattice')
    require(trace(v)==tuple(a),'Representative has wrong reduced trace')
    require(norm(v)==Fraction(sum(q*q for q in a)+mu4,4),'Representative fails the exact shortest norm theorem')
    frame=load(base,'trace_frame.json');W=frame['frame_W']
    expected=[[2*int(i in b) for i in range(24)] for b in BLOCKS]
    require(W==expected and frame['octads']==list(map(list,BLOCKS)),'Frame convention differs from the proved inverse')
    n=[(t[i]-a[i])//4 for i in range(3)];z=combine(n,W)
    x=tuple(u+v for u,v in zip(v,z))
    require(member(x,code) and trace(x)==tuple(t),'Failed full three-trace return')
    require(norm(x)==Fraction(sum(v*v for v in t)+mu4,4),'Returned vector has incorrect optimal height')
    return x,{'trace':list(t),'norm_is_minimal_in_trace_fibre':True,'mu':str(Fraction(mu4,4))}

def inverse_four(four,base,code):
    require(len({sum(v) for v in four})==1,'The four triples must have the same sum')
    rows=load(base,'twelve_views.json')['right_inverse_numerators']
    require(isinstance(rows,list) and len(rows)==9,'Missing nine-column inverse')
    for i,row in enumerate(rows):
        require_vector(row)
        require(member(row,code),'Right-inverse column is outside the Leech lattice')
        require(trace9(row)==tuple(int(i==j) for j in range(9)),'Right-inverse column fails the complete nine-coordinate identity')
    a=tuple(four[0])+tuple(four[1][:2])+tuple(four[2][:2])+tuple(four[3][:2]);x=combine(a,rows)
    require(member(x,code),'Returned four-view vector is outside the lattice')
    actual=all_views(x)
    def rotate(v,k):
        for _ in range(k):v=(v[2],v[0],v[1])
        return tuple(v)
    expected=[rotate(tuple(four[n%4]),n//4) for n in range(12)]
    require(actual==expected,'Returned vector fails a requested time view')
    return x,{'four_independent_time_triples':four,'all_twelve_time_triples':actual,'norm_is_minimal_in_trace_fibre':False}

def main():
    p=argparse.ArgumentParser(description=__doc__);g=p.add_mutually_exclusive_group(required=True)
    g.add_argument('--trace',nargs=3,type=int);g.add_argument('--four',nargs=12,type=int)
    p.add_argument('--cert-dir',type=Path,default=BASE);p.add_argument('--p',type=int);args=p.parse_args()
    _,code=golay()
    if args.trace is not None:x,out=inverse_trace(args.trace,args.cert_dir,code)
    else:x,out=inverse_four([args.four[3*i:3*i+3] for i in range(4)],args.cert_dir,code)
    out.update(numerator=x,scale='1/sqrt(8)',norm_squared=str(norm(x)))
    if args.p is not None:
        a,b,c=trace(x);n=args.p;f=4*a*b*c-n*(a*b+a*c+b*c)
        out.update(p=n,ES_defect=f,positive_ES_identity=n>0 and min(a,b,c)>0 and f==0)
    print(json.dumps(out,sort_keys=True,indent=2))
if __name__=='__main__':main()
