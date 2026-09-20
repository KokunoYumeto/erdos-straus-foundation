import sympy as s
from itertools import product
from common import Suite,ROOT
T=Suite('simultaneous_quotient_phase');I=s.I
H0=s.diag(2,3,5,7)
h=s.Matrix([1,I,1-I,2]);H0=(H0+h*h.conjugate().T).applyfunc(s.expand)
V=s.Matrix([[1,I],[I,1],[1+I,-1],[2,1-I]])
A=s.Matrix([[1,0,0,1],[0,1,0,I],[0,0,1,1-I]])
Lam=s.Matrix([[1,I,0],[0,1,1]])
W=s.Matrix([[1,I,1],[0,1,1-I],[1,0,2]])
P=H0.inv(method="DM").applyfunc(s.cancel);Ll=(V.conjugate().T*P*V).applyfunc(s.cancel)

def data(A):
 G=(A*P*A.conjugate().T).applyfunc(s.cancel).inv(method="DM");Z=(G*A*P*V).applyfunc(s.cancel);K=(Ll-Z.conjugate().T*G.inv(method="DM")*Z).applyfunc(s.cancel)
 return G.applyfunc(s.simplify),Z.applyfunc(s.simplify),K.applyfunc(s.simplify)
G1,Z1,K1=data(A);G2,Z2,K2=data(Lam*A)
T.equal('nested base quotient',G2,(Lam*G1.inv(method="DM")*Lam.conjugate().T).inv(method="DM"))
T.require('two uncertainty matrices fail to commute',K1*K2!=K2*K1)
for vals in [(s.Integer(0),s.Integer(0)),(s.Rational(-1,100),s.Integer(0)),(s.Integer(0),s.Rational(1,10)),(s.Rational(1,10),s.Rational(1,10))]:
 D=s.diag(*vals);H=(H0+V*D*V.conjugate().T).applyfunc(s.cancel)
 T.require(f'positive source {vals}',all(H[:j,:j].det()>0 for j in range(1,5)))
 for label,AA,G,Z,K in [('source',A,G1,Z1,K1),('observation',Lam*A,G2,Z2,K2)]:
  U=(D*(s.eye(2)+K*D).inv(method="DM")).applyfunc(s.cancel);Q=(G+Z*U*Z.conjugate().T).applyfunc(s.cancel);direct=(AA*H.inv(method="DM")*AA.conjugate().T).applyfunc(s.cancel).inv(method="DM")
  T.equal(f'{label} exact quotient {vals}',Q,direct)
  T.equal(f'{label} determinant ratio {vals}',Q.det()/G.det(),(s.eye(2)+Ll*D).det()/(s.eye(2)+K*D).det())
  B=(P-P*AA.conjugate().T*G*AA*P)*V
  Lift=P*AA.conjugate().T*G-B*U*Z.conjugate().T
  T.equal(f'{label} exact minimum lift {vals}',Lift,H.inv(method="DM")*AA.conjugate().T*direct)
  T.equal(f'{label} kernel correction {vals}',AA*B,s.zeros(AA.rows,2))
  T.equal(f'{label} Hermitian correction {vals}',U,U.conjugate().T)
  T.require(f'{label} positive kernel determinant {vals}',(s.eye(2)+K*D).det()>0)
# symbolic multiaffine numerator and degree-four current reduction.
th=s.symbols('theta_0 theta_1',real=True);D=s.diag(*th)
def numerator(G,Z,K):
 M=s.eye(2)+K*D;delta=s.expand(M.det());N=(G*delta+Z*D*M.adjugate()*Z.conjugate().T).applyfunc(s.expand)
 for e in N:
  pp=s.Poly(e,*th)
  T.require('multiaffine numerator '+str(len(T.passed)),all(pp.degree(x)<=1 for x in th))
 return delta,N
D1,N1=numerator(G1,Z1,K1);D2,N2=numerator(G2,Z2,K2)
NF=(W.conjugate().T*N1*W).applyfunc(s.expand)
NC=(W.conjugate().T*Lam.conjugate().T*N2*Lam*W).applyfunc(s.expand)
NR=(NF*D2-NC*D1).applyfunc(s.expand)
Pc=s.expand(2*s.re(s.conjugate(NC[0,2])*NC[1,2]))
Pr=s.expand(2*s.re(s.conjugate(NR[0,2])*NR[1,2]))
Px=s.expand(2*s.re(s.conjugate(NR[0,2])*NC[1,2]*D1+s.conjugate(NC[0,2])*D1*NR[1,2]))
T.require('observed numerator degree <=2 per parameter',all(s.Poly(Pc,*th).degree(x)<=2 for x in th))
T.require('kernel numerator degree <=4 per parameter',all(s.Poly(Pr,*th).degree(x)<=4 for x in th))
T.require('mixed numerator degree <=4 per parameter',all(s.Poly(Px,*th).degree(x)<=4 for x in th))
# exact common-denominator cancellation: R+C=F.
PF=s.expand(2*s.re(s.conjugate(NF[0,2])*NF[1,2]))
T.equal('three current numerators sum to full current',Pr+Pc*D1**2+Px,PF*D2**2)
T.reject('noncommuting kernel update may be reordered',K1*K2==K2*K1)
(ROOT/'results'/'synthetic_phase_polynomials.txt').write_text('Synthetic exact diagnostic; not native moment values.\nDelta_E='+str(D1)+'\nDelta_B='+str(D2)+'\nP_observed='+str(Pc)+'\nP_kernel='+str(Pr)+'\nP_mixed='+str(Px)+'\n')
T.save({'uncertainties':2,'source_dimension':4,'quotient_dimension':3,'observation_dimension':2,'sample_parameters':4,'parameter_degrees':{'observed':s.Poly(Pc,*th).degree_list(),'kernel':s.Poly(Pr,*th).degree_list(),'mixed':s.Poly(Px,*th).degree_list()}})
