#!/usr/bin/env python3
"""Independent residue-space frontier verification of the 174-profile catalogue.
No import from verify.py. It does not use logarithmic/cyclic exponent masks.
Each unoccupied capped profile is visited; every occupied boundary dominates
one of the independently verified minimal patterns. This exhausts the grid by
monotonicity. Explicit checks remain active under python -O.
"""
from collections import deque,Counter
from functools import lru_cache
from itertools import product
from math import gcd
from pathlib import Path
import json,argparse

def check(v,msg):
    if not v:raise ArithmeticError(msg)
R=27
units=tuple(g for g in range(2,R) if gcd(g,R)==1) # identity residue is inert

def order(g):
    a=1
    for k in range(1,19):
        a=a*g%27
        if a==1:return k
    raise ArithmeticError('unit order')
caps=tuple(order(g)//2 for g in units)

def mask(values):
    z=0
    for v in values:z|=1<<v
    return z

def elements(S):
    while S:
        k=S&-S;yield k.bit_length()-1;S-=k

@lru_cache(None)
def step(S,g,c):
    factors=(1,g,g*g%R) if c=='E' else (1,g,pow(g,-1,R))
    return mask(x*f%R for x in elements(S) for f in factors)

def direct(gs,es,c):
    A={1}
    for g,e in zip(gs,es):
        rng=range(2*e+1) if c=='E' else range(-e,e+1)
        A={x*pow(g,k,R)%R for x in A for k in rng}
    return A

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--catalogue',default='certificates/catalogue27.json')
    p.add_argument('--out',default='frontier_verification.json');args=p.parse_args()
    C=json.loads(Path(args.catalogue).read_text())['minimal_profiles'];patterns=[]
    for r in C:
        gs=r['residues'];es=r['capacities']
        check(len(gs)==len(es) and len(gs)==len(set(gs)) and
              all(g in units and 1<=e<=caps[units.index(g)] for g,e in zip(gs,es)),
              'invalid labelled capacity profile')
        word=r['target_word'];coords=word['coordinates'];channel=word['channel']
        check(channel in ('E','M') and len(coords)==len(gs),'invalid target word type')
        check(all((0<=v<=2*e if channel=='E' else -e<=v<=e) for v,e in zip(coords,es)),
              'target word outside the retained capacities')
        value=1
        for g,v in zip(gs,coords):value=value*pow(g,v,R)%R
        check(value==(20 if channel=='E' else 26),'invalid target word value')
        check(20 in direct(gs,es,'E') or 26 in direct(gs,es,'M'),'catalogue pattern has no original target')
        for i in range(len(es)):
            f=[e-(j==i) for j,e in enumerate(es)]
            check(20 not in direct(gs,f,'E') and 26 not in direct(gs,f,'M'),'not minimal')
        pairs=tuple(sorted((units.index(g),e) for g,e in zip(gs,es)))
        sm=sum(1<<i for i,e in pairs);patterns.append((sm,pairs))
    check(len(set(pairs for sm,pairs in patterns))==174,'duplicate catalogue')
    @lru_cache(None)
    def eligible(S):return tuple(pairs for sm,pairs in patterns if sm&S==sm)
    start=(0,)*len(units);seen={start};Q=deque([(start,1<<1,1<<1,0)]);stats=Counter()
    while Q:
        e,E,M,S=Q.popleft();stats['unoccupied_capped_profiles']+=1
        for i,g in enumerate(units):
            if e[i]==caps[i]:continue
            f=list(e);f[i]+=1;f=tuple(f)
            if f in seen:continue
            # Do not retain occupied profiles: all descendants are already occupied.
            ne=step(E,g,'E');nm=step(M,g,'M');ns=S|(1<<i)
            h=bool(ne>>20&1 or nm>>26&1)
            stats['frontier_edges_tested']+=1
            if h:
                check(any(all(f[j]>=k for j,k in pairs) for pairs in eligible(ns)),
                      'occupied boundary not covered by catalogue')
                stats['occupied_boundary_edges']+=1
            else:
                seen.add(f);Q.append((f,ne,nm,ns))
    output=dict(modulus=27,unit_residues=list(units),caps=list(caps),
                independently_verified_patterns=len(C),counts=dict(stats),
                transition_cache_entries=step.cache_info().currsize,
                proof='Every upward path from zero either stays in the listed unoccupied grid or first crosses a checked occupied boundary; occupancy is upward closed.')
    Path(args.out).write_text(json.dumps(output,indent=2,sort_keys=True)+'\n');print(json.dumps(output['counts'],sort_keys=True))
if __name__=='__main__':main()
