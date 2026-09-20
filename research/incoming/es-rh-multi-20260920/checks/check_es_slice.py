import sympy as s,json
from common import Suite,ROOT
T=Suite('es_frame_divisor')
r,A,B,C,D,t=s.symbols('r A B C D t')
h=A*r**4+r**3+B*r**2+C*r+D;d=s.diff(h,r)
polys=[1,-s.I*d,A*d*d+2*r*d,s.I*(7*r*r*d-13*d*d)]
V=s.Matrix([[s.Poly(s.rem(p,h,r),r).nth(j) for j in range(4)] for p in polys])
F=20*(3*C-B**2)+A*(87*B**3-282*B*C-51*D)+A**2*(-28*B**4+22*B**2*C+431*C**2+204*B*D)+A**3*(224*B**2*D-168*B*C**2-856*C*D)-448*A**4*D**2
T.equal('generic odd determinant numerator',V.det(method='domain-ge'),4*F/A)
# Original normalized ES coefficient map, for positive real t>202.
roots=[s.Integer(1),t/(4*t-402),t/202,t/200];S=sum(roots)
raw=s.Poly(s.prod(r-x for x in roots),r);mp={A:s.cancel(-1/S),B:s.cancel(-raw.nth(2)/S),C:s.cancel(-raw.nth(1)/S),D:s.cancel(-raw.nth(0)/S)}
T.equal('literal reciprocal equation',sum(1/x for x in roots[1:]),4)
T.equal('prime recovered from coefficients',-5*mp[D]/mp[C],1)
Fslice=s.factor(F.subs(mp));num,den=s.fraction(Fslice);fl=s.factor_list(num)
factors=[f for f,m in fl[1] if s.degree(f,t)>1]
print('SLICE',Fslice)
T.require('one nontrivial factor',len(factors)==1)
f=s.Poly(factors[0],t);_,f=f.primitive()
if f.LC()<0:f=-f
left,right=s.Integer(551),s.Integer(651)
T.require('negative frame determinant scalar at left',Fslice.subs(t,left)<0)
T.require('positive frame determinant scalar at right',Fslice.subs(t,right)>0)
T.require('no pole on interval',s.Poly(den,t).count_roots(left,right)==0)
T.equal('squarefree slice determinant factor',s.gcd(f,f.diff()).as_expr(),1)
T.require('unique receiving-divisor root on interval',f.count_roots(left,right)==1)
T.require('algebraic singular parameter is not rational',not any(s.degree(g,t)==1 for g,_ in s.factor_list(f.as_expr())[1]))
minor=s.factor(V.extract([0,1,2],[0,1,2]).det().subs(mp)/s.I)
minor_num,minor_den=s.fraction(minor)
T.equal('rank-three minor does not vanish at determinant root',s.gcd(f,s.Poly(minor_num,t)).as_expr(),1)
T.require('rank-three minor has no pole on interval',s.Poly(minor_den,t).count_roots(left,right)==0)
# squarefreeness of quartic is certified directly from distinct rational formulas.
for j in range(4):
 for k in range(j+1,4):
  diff=s.factor(roots[k]-roots[j]);nn,dd=s.fraction(diff)
  T.require(f'distinct roots {j},{k}',s.Poly(nn,t).count_roots(left,right)==0 and s.Poly(dd,t).count_roots(left,right)==0)
# Integer primitive defining polynomial and reproducible Sturm isolation.
intervals=s.polys.polytools.intervals(f.as_expr(),eps=s.Rational(1,10**6))
contained=[(str(a),str(b),m) for (a,b),m in intervals if left<a<right]
T.require('isolating interval generated',len(contained)==1)
T.reject('squarefreeness implies odd-frame invertibility',f.count_roots(left,right)==0)
extra={'parameter':'t','roots_at_prime_p':['p','p*t/(4*t-402)','p*t/202','p*t/200'],'interval':[551,651],'primitive_polynomial_coefficients':[int(c) for c in f.all_coeffs()],'sturm_root_count':int(f.count_roots(left,right)),'isolating_interval':contained,'slice':str(Fslice),'rank_three_minor':str(minor),'endpoint_values':[str(Fslice.subs(t,left)),str(Fslice.subs(t,right))]}
T.save(extra)
(ROOT/'results'/'es_slice_polynomial.txt').write_text(str(f.as_expr())+'\n')
