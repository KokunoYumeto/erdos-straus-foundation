#!/usr/bin/env python3
"""Whole-polynomial Gaussian-integer identities, without a symbolic dependency."""
from __future__ import annotations
from itertools import permutations
from pathlib import Path
import json,hashlib
Z=(0,0,0,0)
def ga(a,b):return (a[0]+b[0],a[1]+b[1])
def gm(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
class Polynomial:
    def __init__(self,z=0):
        if isinstance(z,Polynomial):self.terms=dict(z.terms)
        elif isinstance(z,dict):self.terms={k:v for k,v in z.items() if v!=(0,0)}
        elif isinstance(z,int):self.terms={Z:(z,0)} if z else {}
        else:raise TypeError(type(z))
    def __add__(self,o):
        o=Polynomial(o);r=dict(self.terms)
        for k,v in o.terms.items():r[k]=ga(r.get(k,(0,0)),v)
        return Polynomial(r)
    __radd__=__add__
    def __neg__(self):return Polynomial({k:(-v[0],-v[1]) for k,v in self.terms.items()})
    def __sub__(self,o):return self+-Polynomial(o)
    def __rsub__(self,o):return Polynomial(o)+-self
    def __mul__(self,o):
        o=Polynomial(o);r={}
        for a,v in self.terms.items():
            for b,w in o.terms.items():
                k=tuple(x+y for x,y in zip(a,b));r[k]=ga(r.get(k,(0,0)),gm(v,w))
        return Polynomial(r)
    __rmul__=__mul__
    def __pow__(self,n):
        r=Polynomial(1)
        for _ in range(n):r=r*self
        return r
    def derivative(self,j):
        r={}
        for k,v in self.terms.items():
            if k[j]:
                l=list(k);l[j]-=1;r[tuple(l)]=(v[0]*k[j],v[1]*k[j])
        return Polynomial(r)
    def __eq__(self,o):return self.terms==Polynomial(o).terms

def main():
    x=[]
    for j in range(4):
        e=[0]*4;e[j]=1;x.append(Polynomial({tuple(e):(1,0)}))
    A,y,z,w=x;I=Polynomial({Z:(0,1)})
    P=[A**3*z+2*A*A*y-I*A,
       -A**3*y*y*z-2*I*A*A*y*z+A*A*w-2*A*A*y**3-10*I*A*y*y+3*A*z+y,
       2*A**3*y**3*z+6*I*A*A*y*y*z+2*A*A*w*y+4*A*A*y**4+2*I*A*w-4*I*A*y**3-2*A*y*z+2*I*z+7*y*y,
       2*A**3*y**4*z+8*I*A*A*y**3*z+A*A*w*y*y+4*A*A*y**5+2*I*A*w*y+7*I*A*y**4-10*A*y*y*z-4*I*y*z-w-3*y**3]
    b=I+A*y;c=-I+2*A*y+A*A*z;d=-I*y-A*(I*z+2*y*y)-A*A*y*z
    e=2*z-7*I*y*y+A*w;f=I*w+3*I*y**3-4*y*z+A*(6*I*y*y*z+w*y+4*y**4)+2*A*A*y**3*z
    statements={'incidence':A*d+b*c==1,'resultant':A**3*f-A*A*b*e+A*b*b*d-b**3*c==1,
                'factor_product':[A*c,A*e+b*d,A*f+b*e,b*f]==P}
    J=[[v.derivative(j) for j in range(4)] for v in P];det=Polynomial(0)
    for perm in permutations(range(4)):
        s=(-1)**sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4));t=Polynomial(s)
        for i in range(4):t=t*J[i][perm[i]]
        det=det+t
    statements['constant_Jacobian_minus_two']=det==-2
    result={'success':all(statements.values()),'statements':statements,
            'determinant_terms':[[list(k),list(v)] for k,v in det.terms.items()],
            'arithmetic':'Sparse polynomials over Gaussian integers; all coefficients exact.',
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).with_name('polynomial_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    if not result['success']:raise ArithmeticError('a global polynomial identity failed')
if __name__=='__main__':main()
