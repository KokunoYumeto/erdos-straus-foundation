"""Literal polynomial and moving-column diagnostics; all inputs exact."""
import sympy as s
from common import Suite,ROOT
T=Suite('literal_polynomial_and_moving_columns');i=s.I
a,y,z,w=s.symbols('a y z w')
P=s.Matrix([a**3*z+2*a**2*y-i*a,
-a**3*y**2*z-2*i*a**2*y*z+a**2*w-2*a**2*y**3-10*i*a*y**2+3*a*z+y,
2*a**3*y**3*z+6*i*a**2*y**2*z+2*a**2*w*y+4*a**2*y**4+2*i*a*w-4*i*a*y**3-2*a*y*z+2*i*z+7*y**2,
2*a**3*y**4*z+8*i*a**2*y**3*z+a**2*w*y**2+4*a**2*y**5+2*i*a*w*y+7*i*a*y**4-10*a*y**2*z-4*i*y*z-w-3*y**3])
T.equal('literal four-dimensional Jacobian',s.expand(P.jacobian([a,y,z,w]).det()),-2)
for j,pt in enumerate([(0,0,i/2,0),(i,-1,-3*i,13)]):
 T.equal(f'displayed common image {j}',P.subs(dict(zip([a,y,z,w],pt))),s.Matrix([0,0,-1,0]))
T.require('two source points remain distinct',(0,0,i/2,0)!=(i,-1,-3*i,13))
# Two simultaneous uncertainties and an actual affine monic minimization.
H0=s.Matrix([[3,1,i],[1,4,0],[-i,0,6]]);V=s.Matrix([[1,i],[i,2],[2,1-i]])
Ins=s.Matrix([[1,0],[0,1],[0,0]]);top=s.Matrix([0,0,1]);M0=Ins.conjugate().T*H0*Ins
q0=top-Ins*M0.inv()*Ins.conjugate().T*H0*top
h0=(q0.conjugate().T*H0*q0)[0]
K=V.conjugate().T*Ins*M0.inv()*Ins.conjugate().T*V
B=Ins*M0.inv()*Ins.conjugate().T*V;b=V.conjugate().T*q0
for t0,t1 in [(0,0),(-s.Rational(1,100),s.Rational(1,20)),(s.Rational(1,5),s.Rational(1,10))]:
 D=s.diag(t0,t1);H=H0+V*D*V.conjugate().T
 T.require(f'positive moving metric {t0},{t1}',all(H[:j,:j].det()>0 for j in range(1,4)))
 U=D*(s.eye(2)+K*D).inv();q=q0-B*U*b
 direct=top-Ins*(Ins.conjugate().T*H*Ins).inv()*Ins.conjugate().T*H*top
 T.equal(f'moving monic column {t0},{t1}',q,direct)
 T.equal(f'moving orthogonality {t0},{t1}',Ins.conjugate().T*H*q,s.zeros(2,1))
 T.equal(f'moving monic norm {t0},{t1}',(q.conjugate().T*H*q)[0],h0+(b.conjugate().T*U*b)[0])
T.reject('fixed-column substitution is harmless',s.simplify(q-direct)==s.zeros(3,1) and s.simplify(q-q0)==s.zeros(3,1))
# Check the large improvement with exact rational values, not logs.
import json
floor=json.loads((ROOT/'results'/'native_gram_floor.json').read_text())
row=next(v for v in floor['results'] if v['t']==20)
T.require('degree-20 floor gain exceeds 10^427 exactly',s.Rational(row['new_floor'])/s.Rational(row['old_floor'])>10**427)
T.save({'moving_parameter_cases':3,'polynomial':'literal EZ4/FC31, not an invented model',
        'moving_metric':'synthetic Gaussian-rational diagnostic, not native moment values'})
