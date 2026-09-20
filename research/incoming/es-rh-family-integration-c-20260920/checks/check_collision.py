from __future__ import annotations
import sys
import sympy as s
from core import collision_minors,collision_exponents,zero
from receipt import Receipt
R=Receipt('collision_complete_phase_diagram'); table=[]
for e in range(1,6):
    for f in range(1,e+1):
        if e+f>7:continue
        minors=collision_minors(e,f)
        for a in [s.Rational(0),s.Rational(1,5),s.Rational(1,2),s.Rational(1),s.Rational(3,2),s.Rational(2),s.Rational(3)]:
            orders=[min(a*w+v for w,v in minors[r]) for r in range(e+f+1)]
            actual=[orders[j+1]-orders[j] for j in range(e+f)]
            predicted=collision_exponents(e,f,a)
            R.require(actual==predicted,f'complete minor valuation e={e},f={f},a={a}')
            R.require(all(predicted[j]<=predicted[j+1] for j in range(e+f-1)),'ordered scales')
            R.equal(sum(predicted),e*f+a*(e*(e-1)+f*(f-1))/2,'determinant exponent')
            if a==0:
                for r in range(1,e+f+1):
                    p=min(r,f)
                    R.equal(sum(predicted[-r:]),p*(e+f-p),'original exterior return')
            if a==1:
                R.require(predicted==list(range(e+f)),'balanced diagonal powers')
            table.append({'e':e,'f':f,'a':str(a),'exponents':[str(x) for x in predicted]})
R.false(collision_exponents(2,2,2)==collision_exponents(2,2,0),'eta weights cannot be omitted')
R.false(collision_exponents(3,1,s.Rational(1,2))==[0,0,0,3],'noncolliding derivative rows also scale')
# Exact balanced-ray factorization and Gram constants, retaining factorial weights.
z=s.symbols('z',positive=True)
for e,f in [(2,1),(2,2),(3,1),(3,2)]:
    n=e+f;E=s.zeros(n);B=s.zeros(n)
    coeff=[]
    for block,D in [(0,e-1),(1,f-1)]:
        for j in range(D+1):coeff.append(s.factorial(j)**2*s.binomial(D,j))
    rows=[(0,j) for j in range(e)]+[(1,j) for j in range(f)]
    for i,(block,j) in enumerate(rows):
        for m in range(n):
            v=int(m==j) if block==0 else s.binomial(m,j)
            B[i,m]=s.sqrt(coeff[i])*v
            E[i,m]=(s.sqrt(coeff[i])*z**j*int(m==j) if block==0
                    else s.sqrt(coeff[i])*s.binomial(m,j)*z**m)
    R.equal(E,B*s.diag(*[z**j for j in range(n)]),'balanced factorization')
    gram=B.T*B
    R.equal(gram.det(),s.prod(coeff),'complete factorial-weight determinant')
    R.require(gram.det()>0 and s.trace(gram)>0,'explicit positive constants')
R.extra['phase_table']=table
R.write(sys.argv[1])
