#!/usr/bin/env python3
"""Eight-seed proof certificate for every three-octad shortest-lift residue.
This independently constructs the 64 representatives, rather than trusting them.
"""
from __future__ import annotations
import argparse,itertools,json
from pathlib import Path
from fractions import Fraction
from verify_audit import BLOCKS,C,mv,act,golay,member,trace,norm,permul
R=(5,6,19,0)
def even(S,N=()):return tuple(2*int(i in S)-4*int(i in N) for i in range(24))
def odd(j,s,N=()):return tuple(3*s if i==j else 1-2*int(i in N) for i in range(24))
SEEDS={
(0,0,0):(0,)*24,
(1,0,0):odd(0,-1,(2,5,6,10,12,13,15,22)),
(1,1,0):even((0,2,7,11,12,16,19,23),(0,2)),
(1,1,1):odd(23,1,(0,1,2,3,9,12,21)),
(2,0,0):even((0,1,3,4,7,8,16,23),(0,1)),
(2,1,0):odd(16,1,(0,2,5,6,11,18,22)),
(2,1,1):even((7,8,12,13,14,16,18,23)),
(2,2,0):even((4,7,16,18,19,20,21,23)),
(2,2,1):odd(2,-1),
(2,2,2):even((0,3,4,5,6,8,9,10,12,13,15,18)),
}
def require(b,s):
    if not b:raise ArithmeticError(s)
def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--out',type=Path,default=Path(__file__).resolve().parent/'certificates'/'shortest_eight_seed.json');args=ap.parse_args()
    basis,code=golay();cp,rp=mv(C),mv(R)
    for g in (cp,rp):
        for b in basis:
            z=sum(1<<g[i] for i in range(24) if b>>i&1)
            require(z in code,'Code permutation failed')
    I=tuple(range(24));group=[I];seen={I}
    for g in group:
        for h in (cp,rp):
            z=permul(h,g)
            if z not in seen:seen.add(z);group.append(z)
    require(len(group)==24,'Trio stabilizer has wrong order')
    bs={frozenset(B):i for i,B in enumerate(BLOCKS)}
    phases={tuple(bs[frozenset(g[i] for i in B)] for B in BLOCKS) for g in group}
    require(len(phases)==6,'All phase permutations not obtained')
    for t,v in SEEDS.items():
        require(member(v,code) and trace(v)==t,'Invalid seed')
        expected=0 if t==(0,0,0) else 6 if t==(2,2,2) else 4
        require(norm(v)==expected,'Incorrect seed norm')
    rows=[]
    for r in itertools.product(range(4),repeat=3):
        a=tuple(v if v<=2 else -1 for v in r);typ=tuple(sorted(map(abs,a),reverse=True));seed=SEEDS[typ]
        found=None
        for g in group:
            v=act(seed,g)
            if trace(v)==tuple(map(abs,a)):found=v;break
        require(found is not None,'Phase transport failed')
        v=list(found)
        for j,val in enumerate(a):
            if val<0:
                for i in BLOCKS[j]:v[i]=-v[i]
        require(member(tuple(v),code) and trace(v)==a,'Signed phase transport failed')
        mu4=4*norm(v)-sum(z*z for z in a)
        require(mu4.denominator==1,'Nonintegral height numerator')
        rows.append({'residue_mod4':r,'reduced_trace':a,'representative_numerator':v,'norm':int(norm(v)),'mu_times4':int(mu4)})
    out={'status':'PASS','construction':'Eight norm-four seeds, zero, and one norm-six dodecad; signed S3 phase transport','code_basis_hex':[f'{v:06x}' for v in basis],'phase_transposition_SL2':R,'trio_stabilizer_order':len(group),'classes':rows,'minimality_proof':'Leech minimum four; parity lower bound six at (2,2,2); translation by frame vectors preserves perpendicular component.'}
    args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'status':'PASS','norm_four_seeds':8,'residues':64,'phase_permutations':6},sort_keys=True))
if __name__=='__main__':main()
