"""Small exact-check harness. Checks remain active under python -O."""
import json
from pathlib import Path
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]
class Suite:
    def __init__(self,name): self.name=name; self.passed=[]; self.controls=[]
    def equal(self,name,left,right=0):
        if isinstance(left,sp.MatrixBase) or isinstance(right,sp.MatrixBase):
            a=sp.Matrix(left); b=sp.zeros(*a.shape) if right==0 else sp.Matrix(right)
            ok=a.shape==b.shape and all(sp.cancel(x-y)==0 for x,y in zip(a,b))
        else: ok=sp.cancel(left-right)==0
        if not ok: raise RuntimeError(f'{self.name}: failed {name}')
        self.passed.append(name)
    def require(self,name,condition):
        if not bool(condition): raise RuntimeError(f'{self.name}: failed {name}')
        self.passed.append(name)
    def reject(self,name,condition):
        if bool(condition): raise RuntimeError(f'{self.name}: negative control accepted: {name}')
        self.controls.append(name)
    def save(self,extra=None):
        obj={'suite':self.name,'exact_checks':len(self.passed),'negative_controls':len(self.controls),'checks':self.passed,'controls':self.controls,'status':'PASS'}
        if extra is not None: obj['results']=extra
        dest=ROOT/'results'/f'{self.name}.json';dest.write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')
        print(json.dumps({'suite':self.name,'status':'PASS','exact_checks':len(self.passed),'negative_controls':len(self.controls)},sort_keys=True))
        return obj

def poly_matrix_eval(poly,C,z):
    poly=sp.Poly(poly,z);out=sp.zeros(C.rows)
    for (n,),coef in poly.terms(): out+=coef*C**n
    return out.applyfunc(sp.cancel)

def companion(h,z):
    p=sp.Poly(h,z); n=p.degree();p=p.monic();C=sp.zeros(n)
    for j in range(n-1): C[j+1,j]=1
    for j in range(n): C[j,n-1]=-p.nth(j)
    return C

def residue_gram(h,z):
    p=sp.Poly(h,z);n=p.degree();a=p.LC()
    return sp.Matrix(n,n,lambda i,j: sp.rem(z**(i+j),h,z).coeff(z,n-1)/a)
