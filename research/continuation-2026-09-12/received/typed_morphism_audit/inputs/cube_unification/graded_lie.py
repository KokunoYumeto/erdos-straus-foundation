#!/usr/bin/env python3
"""Exact matrix closure of the three-graded cubic-norm infinitesimal moves.
This optional standard-library certificate performs finite rational linear algebra.
It does not use recognition software to identify a Lie algebra by its dimension.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product, combinations
import json
from verify import need, basis3, emat, zero3, Du, flat, unflat, mm, madd, smul


def matrix_of(f):
    d={}
    for j in range(27):
        col=flat(f(unflat([int(i==j) for i in range(27)])))
        for i,x in enumerate(col):
            if x:d[i,j]=F(x)
    return d

def multiply(A,B):
    brows=defaultdict(list)
    for (k,j),x in B.items():brows[k].append((j,x))
    C=defaultdict(F)
    for (i,k),x in A.items():
        for j,y in brows[k]:C[i,j]+=x*y
    return {p:x for p,x in C.items() if x}

def bracket(A,B):
    C=multiply(A,B)
    for p,v in multiply(B,A).items():C[p]=C.get(p,0)-v
    return {p:x for p,x in C.items() if x}

class Span:
    def __init__(self):self.rows={}
    def reduce(self,A):
        A=A.copy()
        for pivot,row in sorted(self.rows.items()):
            if pivot in A:
                c=A[pivot]
                for p,x in row.items():
                    z=A.get(p,0)-c*x
                    if z:A[p]=z
                    elif p in A:del A[p]
        return A
    def insert(self,A):
        A=self.reduce(A)
        if not A:return False
        p=min(A);c=A[p]
        self.rows[p]={i:x/c for i,x in A.items()}
        return True
    def includes(self,A):return not self.reduce(A)


def gaction(X,g):
    A,B,C=X;g0,g1,g2=g
    return [madd(mm(g1,A),smul(-1,mm(A,g0))),
            madd(mm(g2,B),smul(-1,mm(B,g1))),
            madd(mm(g0,C),smul(-1,mm(C,g2)))]


def run():
    D=[matrix_of(lambda X,abc=[basis3(i),basis3(j),basis3(k)]:Du(X,abc))
       for i,j,k in product(range(3),repeat=3)]
    spans=[Span(),Span(),Span()];bases=[[],D,[]]
    for a in D:need(spans[1].insert(a),'Independent pure tensor action')
    origins=[]
    for i,j in combinations(range(27),2):
        b=bracket(D[i],D[j])
        if spans[2].insert(b):bases[2].append(b);origins.append([i,j])
    sl=[emat(i,j) for i,j in product(range(3),repeat=2) if i!=j]
    sl += [madd(emat(0,0),smul(-1,emat(1,1))),madd(emat(1,1),smul(-1,emat(2,2)))]
    for axis in range(3):
        for m in sl:
            gs=[zero3(),zero3(),zero3()];gs[axis]=m
            b=matrix_of(lambda X,g=gs:gaction(X,g))
            need(spans[0].insert(b),'Independent grade zero action');bases[0].append(b)
    need([len(s.rows) for s in spans]==[24,27,27],'Graded dimensions')
    mixed=Span()
    for a in D:
        for b in bases[2]:
            c=bracket(a,b);need(spans[0].includes(c),'Mixed bracket not grade zero')
            mixed.insert(c)
    need(len(mixed.rows)==24,'Mixed bracket does not generate grade zero')
    allbasis=[(g,b) for g in range(3) for b in bases[g]]
    checks=0
    for (g,a),(h,b) in combinations(allbasis,2):
        c=bracket(a,b);need(spans[(g+h)%3].includes(c),'Bracket not in prescribed grade')
        checks+=1
    need(checks==3003,'Full basis pair count')
    return {'format':'exact-three-graded-Lie-closure/1','dimension_by_grade':[24,27,27],
            'bracket_pairs_verified':checks,'mixed_generation_rank':24,
            'grade_two_commutator_origins':origins,
            'degree_one_tensor_order':'lexicographic (i,j,k) in range(3)^3',
            'classical_identification':'E6 via first Tits cubic norm representation; identification cites the explicit classical representation, not dimension alone.',
            'scope':'All brackets of a rational 78-element matrix basis; Jacobi is inherited from matrix commutators; not a Lean build.'}

if __name__=='__main__':print(json.dumps(run(),sort_keys=True,indent=2))
