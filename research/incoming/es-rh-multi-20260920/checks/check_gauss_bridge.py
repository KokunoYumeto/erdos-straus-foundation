import sympy as s
from common import Suite,ROOT,companion,residue_gram,poly_matrix_eval
T=Suite('gauss_residue_bridge');x,z=s.symbols('x z')
nodes=[1,2,4,7,9,12];weights=[2,3,5,7,11,13]
def integ(poly):return sum(w*s.expand(poly).subs(x,a) for a,w in zip(nodes,weights))
records=[]
for n in range(1,5):
 mom=[integ(x**k) for k in range(2*n+2)]
 H=s.Matrix(n,n,lambda i,j:mom[i+j]);rhs=s.Matrix(mom[n:2*n]);coeff=-H.inv()*rhs
 h=z**n+sum(coeff[j]*z**j for j in range(n))
 Ch=companion(h,z);R=residue_gram(h,z)
 q=s.expand(sum(w*s.cancel((h-h.subs(z,a))/(z-a)) for a,w in zip(nodes,weights)))
 T.require(f'n={n} native mass retained',s.Poly(q,z).LC()==sum(weights))
 T.equal(f'n={n} positive pairing = residue times q',R*poly_matrix_eval(q,Ch,z),H)
 T.require(f'n={n} positive multiplier is a unit',poly_matrix_eval(q,Ch,z).det()!=0)
 for j in range(n):T.equal(f'n={n} orthogonality {j}',integ(h.subs(z,x)*x**j),0)
 for a in [s.Rational(4),s.Rational(16)]:
  # scalar Gauss formula from moment minimum, in original monomials.
  D=s.Matrix(n,n,lambda i,j:mom[i+j+1]);c=s.Matrix(mom[:n]);approx=(c.T*(D+a*H).inv()*c)[0]
  T.equal(f'n={n} Stieltjes rational residue formula at {a}',approx,-q.subs(z,-a)/h.subs(z,-a))
  actual=sum(s.Rational(w,b+a) for b,w in zip(nodes,weights))
  T.require(f'n={n} Gauss lower bound at {a}',actual>=approx)
 records.append({'n':n,'monic_p':str(h),'second_kind_q':str(q),'mass':sum(weights)})
# exact defect for an arbitrary non-Gauss root polynomial
h=(z-1)*(z-3)*(z-8);n=3;Ch=companion(h,z);R=residue_gram(h,z)
mom=[integ(x**j) for j in range(2*n)];H=s.Matrix(n,n,lambda i,j:mom[i+j]);k=R.inv()*s.Matrix(mom[:n]);kp=sum(k[j]*z**j for j in range(n))
Def=s.Matrix(n,n,lambda i,j:integ((s.div(z**(i+j),h,z)[0]*h).subs(z,x)))
T.equal('arbitrary-frame relation defect retained',H,R*poly_matrix_eval(kp,Ch,z)+Def)
T.require('arbitrary-frame defect nonzero',Def!=s.zeros(3))
T.reject('arbitrary roots are Gauss nodes',H==R*poly_matrix_eval(kp,Ch,z))
T.save({'diagnostic_measure':'six rational atoms; NOT the native arithmetic density','cases':records,'defect':str(Def)})
