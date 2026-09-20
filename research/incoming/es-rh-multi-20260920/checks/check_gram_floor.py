import sympy as s
from common import Suite,ROOT
T=Suite('native_gram_floor');x=s.symbols('x');table=[]
for n in range(0,21):
 coeff=[]
 for j in range(n+1):
  row=[(-1)**(j-k)*sum(s.binomial(j,m)*s.binomial(j+m,m)*s.binomial(m,k) for m in range(k,j+1)) for k in range(j+1)]
  coeff.append(row+[s.Integer(0)]*(n-j))
 C=s.Matrix(coeff);tau=sum((2*j+1)*sum(c*c for c in coeff[j]) for j in range(n+1))
 T.require(f't={n} positive inverse trace',tau>0)
 T.require(f't={n} elementary exponential bound',tau<=(n+1)*(2*n+1)*100**n)
 if n<=7:
  J=s.Matrix(n+1,n+1,lambda i,j:s.Rational(2**(i+j+1)-1,i+j+1))
  T.equal(f't={n} exact inverse factorization',C.T*s.diag(*[2*j+1 for j in range(n+1)])*C,J.inv())
  T.equal(f't={n} inverse trace',tau,s.trace(J.inv()))
  T.equal(f't={n} orthogonality',C*J*C.T,s.diag(*[s.Rational(1,2*j+1) for j in range(n+1)]))
 det=s.prod(s.factorial(j)**4/(s.factorial(2*j)*s.factorial(2*j+1)) for j in range(n+1))
 tr=sum(s.Rational(2**(2*j+1)-1,2*j+1) for j in range(n+1))
 old=det/tr**n;new=1/tau
 T.require(f't={n} floor not weaker than old floor',new>=old)
 if n in [0,1,2,5,10,20]:
  # Decimal exponents are diagnostics only; exact rational expressions govern.
  table.append({'t':n,'tau':str(tau),'new_floor':str(new),'old_floor':str(old),'log10_new_over_old':str(s.N(s.log(new/old,10),12))})
T.equal('t=2 inverse trace',sum((2*j+1)*sum(s.Poly(s.legendre(j,2*x-3),x).nth(k)**2 for k in range(j+1)) for j in range(3)),2685)
T.reject('dropping shifted coordinates is harmless',s.legendre(2,2*x-3)==s.legendre(2,x))
T.save(table)
