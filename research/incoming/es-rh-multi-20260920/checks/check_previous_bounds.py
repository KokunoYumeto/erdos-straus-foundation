import sympy as s
from common import Suite
T=Suite('carried_bounds_recheck')
r,c=s.symbols('r c');cc=-s.Rational(60,431);h=r**4+r**3+c*r;d=s.diff(h,r)
pp=[s.Integer(1),-s.I*d,d*d+2*r*d,s.I*(7*r*r*d-13*d*d)]
V=s.Matrix([[s.Poly(s.rem(p,h,r),r).nth(j) for j in range(4)] for p in pp])
VT=V.copy();VT[3,:]=s.Matrix([[0,0,0,1]])
L=s.eye(4);L[3,:]=s.Matrix([[-208*s.I*c*c/21,5*c/21,-20*s.I/7,4*s.I*(431*c+60)/21]])
T.equal('preceding local cubic-moment repair',L*VT,V)
left=s.Matrix([[208*cc*cc,5*s.I*cc,60,-21*s.I]])
T.equal('preceding left null direction',left*V.subs(c,cc),s.zeros(1,4))
q=973*r*r+413*r-140
m=s.Matrix([s.Poly(s.rem(q*r**j,h.subs(c,cc),r),r).nth(3) for j in range(4)])
T.equal('preceding right null moment vector',m,s.Matrix([0,973,-560,420]))
T.equal('preceding right null',V.subs(c,cc)*m,s.zeros(4,1))
T.equal('preceding repaired null channel',VT.subs(c,cc)*m,s.Matrix([0,0,0,420]))
T.equal('preceding pole constant',420*1724,724080)
# Exact rational evaluations of the original Gamma polynomials.
for j in range(1,8):
 Y=2*j;R=[s.Integer(1),s.Integer(Y)]
 for n in range(1,34):R.append(Y*R[-1]+n*(n-s.Rational(1,2))*R[-2])
 for m in range(17):
  even=sum(R[2*n]**2/(s.factorial(2*n)*s.rf(s.Rational(1,2),2*n)) for n in range(m+1))
  odd=sum(R[2*n+1]**2/(s.factorial(2*n+1)*s.rf(s.Rational(1,2),2*n+1)) for n in range(m+1))
  low=(m+1)**(2*j)/s.rf(s.Rational(5,4),j-1)**2
  T.require(f'Gamma even degree rate j={j},r={m}',even>=low/(2*j))
  T.require(f'Gamma odd degree rate j={j},r={m}',odd>=2*j*low)
T.reject('spurious zero pole coefficient',724080==0)
T.save({'note':'Gamma checks verify exact finite kernel inequalities, not unevaluated native moment values.'})
