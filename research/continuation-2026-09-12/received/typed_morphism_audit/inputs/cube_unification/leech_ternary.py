#!/usr/bin/env python3
"""Wilson octonionic Leech shell: all 196560 listed minimal vectors.
Coordinates are twice the actual octonion coordinates. Full joint membership and
cubic coupling are checked; this is not a new proof classifying Leech lattices.
"""
from itertools import product, combinations, permutations
from collections import Counter
from hashlib import sha256
import json
from verify import need


def table():
    T=[[None]*8 for _ in range(8)]
    for i in range(8):T[0][i]=T[i][0]=(i,1)
    for i in range(1,8):T[i][i]=(0,-1)
    for t in range(7):
        a,b,c=[1+x%7 for x in [t,t+1,t+3]]
        for i,j,k in [(a,b,c),(b,c,a),(c,a,b)]:T[i][j]=(k,1);T[j][i]=(k,-1)
    need(all(x is not None for r in T for x in r),'Fano table incomplete')
    return T

T=table();ZERO=(0,)*8

def rawmul(x,y):
    out=[0]*8
    for i,a in enumerate(x):
        if a:
            for j,b in enumerate(y):
                if b:
                    k,s=T[i][j];out[k]+=s*a*b
    return tuple(out)

def mul2(x,y):
    v=rawmul(x,y);need(all(a%2==0 for a in v),'Product needs a finer half-integral grid')
    return tuple(a//2 for a in v)

def add(*vs):return tuple(sum(xs) for xs in zip(*vs))
def scale(n,x):return tuple(n*a for a in x)
def inL(v):
    p=v[0]%2
    return all(x%2==p for x in v) and sum(v)%4==2*p
s=(-1,1,1,1,1,1,1,1);sb=(-1,-1,-1,-1,-1,-1,-1,-1)

def in_right_lattice(v,conjugate_multiplier):
    pre=rawmul(v,conjugate_multiplier)
    return all(x%4==0 for x in pre) and inL(tuple(x//4 for x in pre))

def inLambda(x,y,z):
    return (all(inL(v) for v in [x,y,z])
            and all(in_right_lattice(v,s) for v in [add(x,y),add(y,z),add(z,x)])
            and in_right_lattice(add(x,y,z),sb))

def run():
    roots=set()
    for i,j in combinations(range(8),2):
        for a,b in product([-2,2],repeat=2):
            v=[0]*8;v[i]=a;v[j]=b;roots.add(tuple(v))
    for v in product([-1,1],repeat=8):
        if sum(a<0 for a in v)%2==1:roots.add(v)
    need(len(roots)==240 and all(inL(v) and sum(x*x for x in v)==8 for v in roots),'E8 root model')
    units=[tuple(2*int(i==j) for i in range(8)) for j in range(8)]
    shells=[set(),set(),set()]
    for v in roots:
        for pos in range(3):
            tr=[ZERO,ZERO,ZERO];tr[pos]=scale(2,v);shells[0].add(tuple(tr))
        vs=mul2(v,s);vsb=mul2(v,sb)
        for j in units:
            q=mul2(vsb,j)
            for ep in [-1,1]:
                for perm in permutations((vsb,scale(ep,q),ZERO)):shells[1].add(perm)
            w=mul2(vs,j);vj=mul2(v,j)
            for k in units:
                y=mul2(v,k);z=mul2(vj,k)
                for ep,eta in product([-1,1],repeat=2):
                    for perm in permutations((w,scale(ep,y),scale(eta,z))):shells[2].add(perm)
    need([len(s) for s in shells]==[720,11520,184320],'Wilson three shape counts')
    need(all(not shells[i].intersection(shells[j]) for i,j in combinations(range(3),2)),'Shapes overlap')
    hist=Counter();digest=sha256();examples={}
    for n,shell in enumerate(shells):
        for x,y,z in sorted(shell):
            need(sum(a*a for v in [x,y,z] for a in v)==32,'Leech short-vector norm')
            need(inLambda(x,y,z),'Joint Wilson congruence failure')
            # 2 Re((x_actual*y_actual)*z_actual)=raw scalar/4.
            w=rawmul(rawmul(x,y),z)[0]
            need(w%4==0,'Cubic coupling nonintegral')
            c=w//4;hist[c]+=1;examples.setdefault(str(c),[x,y,z])
            digest.update((' '.join(str(a) for v in [x,y,z] for a in v)+'\n').encode())
    return {'format':'wilson-leech-ternary-shell/1','reference':'Wilson (2009), octoLeech1rev.pdf, sections 2--4, especially printed pages 3--4',
            'coordinate_scale':2,'wilson_squared_norm':4,'root_count':240,
            'shape_counts':[len(s) for s in shells],'total':sum(len(s) for s in shells),
            'all_joint_memberships_checked':True,'sorted_vectors_sha256':digest.hexdigest(),
            'cubic_coupling_2Re_xyz_histogram':{str(k):hist[k] for k in sorted(hist)},
            'example_for_each_cubic_value':examples,
            'interpretation':'The same quadratic Leech shell carries differing retained ternary Jordan determinants. No ES coverage or Leech-Jordan automorphism equivalence is inferred.'}

if __name__=='__main__':print(json.dumps(run(),sort_keys=True,indent=2))
