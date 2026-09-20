from __future__ import annotations
import json
from pathlib import Path
import sympy as sp
from core import zero

class Receipt:
    def __init__(self,name): self.name=name; self.n=0; self.neg=0; self.extra={}
    def require(self,condition,label):
        if not bool(condition): raise ArithmeticError(f'{self.name}: {label}')
        self.n+=1
    def equal(self,a,b,label):self.require(zero(a-b),label)
    def false(self,condition,label):
        if bool(condition):raise ArithmeticError(f'Negative control incorrectly accepted: {label}')
        self.neg+=1
    def write(self,outdir):
        data={'suite':self.name,'status':'PASS','exact_checks':self.n,'negative_controls':self.neg,
              'scope':'Exact finite algebra and explicitly synthetic diagnostics; not a native zeta-moment evaluation or Lean proof.',
              **self.extra}
        out=Path(outdir);out.mkdir(parents=True,exist_ok=True)
        (out/f'{self.name}.json').write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
        print(json.dumps(data,sort_keys=True))
