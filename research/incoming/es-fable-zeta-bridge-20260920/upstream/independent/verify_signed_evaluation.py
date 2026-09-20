"""Independent signed-state calculation via multiplication in the quartic algebra."""
import sympy as s
import json
from pathlib import Path
A,B,C,D=s.symbols('A B C D', nonzero=True)
i=s.I
e0=s.Matrix([1,0,0,0])
R=s.Matrix([[0,0,0,-D/A],[1,0,0,-C/A],[0,1,0,-B/A],[0,0,1,-1/A]])
F=4*A*R**3+3*R**2+2*B*R+C*s.eye(4)
I=s.eye(4)
V=s.Matrix.hstack(e0,-i*F*e0,(A*F**2+2*R*F)*e0,(7*i*R**2*F-13*i*F**2)*e0).T.applyfunc(s.expand)
E=s.Matrix.hstack(s.zeros(4,1),-R*e0,3*i*F*e0,((B*I-17*R+A*R**2)*F-2*A*F**2)*e0).T.applyfunc(s.expand)
Vprinted=s.Matrix([
 [1,0,0,0],[-i*C,-2*i*B,-3*i,-4*i*A],
 [A*C**2-9*D,4*A*B*C-8*A*D-7*C,-16*A**2*D+4*A*B**2-2*A*C-5*B,-8*A**2*C+4*A*B-3],
 [-13*i*C**2+20*i*D/A,-52*i*B*C+76*i*D+20*i*C/A,208*i*A*D-52*i*B**2+5*i*C+20*i*B/A,104*i*A*C-66*i*B+20*i/A]])
assert (V-Vprinted).applyfunc(s.expand)==s.zeros(4)
delta,gamma=s.symbols('delta gamma', positive=True)
sub={A:-s.Rational(1,2),B:delta**2-gamma**2-s.Rational(3,4),C:gamma**2-delta**2+s.Rational(1,4),D:-s.Rational(1,32)-(gamma**2-delta**2)/4-(delta**2+gamma**2)**2/2}
det_general=s.factor(V.det())
det_literal=s.factor(det_general.subs(sub))
assert s.expand(det_literal-448*delta**2*gamma**2*(2*delta**2*gamma**2-delta**2+gamma**2))==0
minor=s.factor(E.extract([1,2,3],[1,2,3]).det())
assert s.expand(minor-6*i*(64*A**3*D-16*A**2*B**2-22*A**2*C+89*A*B-30))==0
minor_literal=s.factor(minor.subs(sub))
assert s.expand(minor_literal-6*i*(16*delta**2*gamma**2-35*delta**2+35*gamma**2))==0
w0,w1,w2,w3=list(E[3,:])
t=s.Matrix([3*w3-4*A*w2,0,4*A*w0-C*w3,C*w2-3*w0])
assert (E*t).applyfunc(s.expand)==s.zeros(4,1)
r,a=s.symbols('r a', nonzero=True)
der=4*A*r**3+3*r**2+2*B*r+C
q=s.Matrix([a,-r-i/a,A/a**3+2*r/a+3*i/a**2,7*i*r**2/a+(B-17*r+A*r**2)/a**2-13*i/a**3-2*A/a**4])
even=s.Matrix([0,-r,3*i/a**2,(B-17*r+A*r**2)/a**2-2*A/a**4])
odd=s.Matrix([a,-i/a,A/a**3+2*r/a,7*i*r**2/a-13*i/a**3])
assert (q-q.subs(a,-a)-2*odd).applyfunc(s.expand)==s.zeros(4,1)
assert (q+q.subs(a,-a)-2*even).applyfunc(s.expand)==s.zeros(4,1)
roots=[s.Rational(1,2)+ed*delta+eg*i*gamma for ed,eg in [(1,1),(1,-1),(-1,1),(-1,-1)]]
W=s.Matrix([[rr**k for rr in roots] for k in range(4)])
vand=s.factor(W.det())
assert s.expand(vand+64*delta**2*gamma**2*(delta**2+gamma**2))==0
product_der=s.prod([der.subs(sub).subs(r,rr) for rr in roots]).expand()
assert s.expand(product_der-s.Rational(1,16)*vand**2)==0
out={'method':'quartic companion multiplication; no root script imports','SE4_coefficient_matrix_verified':True,'odd_general_determinant':str(det_general),'odd_literal_determinant':str(det_literal),'even_minor_general':str(minor),'even_minor_literal':str(minor_literal),'even_coefficient_matrix':[[str(x) for x in row] for row in E.tolist()],'explicit_even_kernel_vector_verified':True,'exact_sign_pair_decomposition':True,'quartet_vandermonde':str(vand),'product_derivative_identity':True,'all_assertions_passed':True}
text=json.dumps(out,indent=2)
Path(__file__).with_name('verify_signed_evaluation_output.json').write_text(text+'\n',encoding='utf-8')
print(text)
