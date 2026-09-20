"""Original eight-state evaluation, split by its proved simultaneous sign involution."""
import sympy as s
from pathlib import Path
import json
A,B,C,D,r=s.symbols('A B C D r')
h=A*r**4+r**3+B*r**2+C*r+D
d=s.diff(h,r)
even=s.Matrix([0,-r,3*s.I*d,(B-17*r+A*r**2)*d-2*A*d**2])
odd=s.Matrix([1,-s.I*d,A*d**2+2*r*d,7*s.I*r**2*d-13*s.I*d**2])
ev=even.applyfunc(lambda f:s.rem(f,h,r).expand())
od=odd.applyfunc(lambda f:s.rem(f,h,r).expand())
V=s.Matrix([[s.expand(od[j]).coeff(r,k) for k in range(4)] for j in range(4)])
E=s.Matrix([[s.expand(ev[j]).coeff(r,k) for k in range(4)] for j in range(4)])
det=s.factor(V.det())
delta,gamma=s.symbols('delta gamma', positive=True)
quartet={A:-s.Rational(1,2),B:delta**2-gamma**2-s.Rational(3,4),
 C:gamma**2-delta**2+s.Rational(1,4),
 D:-s.Rational(1,32)-(gamma**2-delta**2)/4-(delta**2+gamma**2)**2/2}
quartet_det=s.factor(det.subs(quartet))
assert s.expand(quartet_det-448*delta**2*gamma**2*(2*delta**2*gamma**2-delta**2+gamma**2))==0
minor=s.factor(E.extract([1,2,3],[1,2,3]).det())
assert s.expand(minor-6*s.I*(64*A**3*D-16*A**2*B**2-22*A**2*C+89*A*B-30))==0
quartet_minor=s.factor(minor.subs(quartet))
assert s.expand(quartet_minor-6*s.I*(16*delta**2*gamma**2-35*delta**2+35*gamma**2))==0
alpha=s.symbols('alpha', nonzero=True)
q=s.Matrix([alpha,-r-s.I/alpha,A/alpha**3+2*r/alpha+3*s.I/alpha**2,
 7*s.I*r**2/alpha+(B-17*r+A*r**2)/alpha**2-13*s.I/alpha**3-2*A/alpha**4])
dvar=s.symbols('derivative')
mean=s.Matrix([0,-r,3*s.I*dvar,(B-17*r+A*r**2)*dvar-2*A*dvar**2])
diff=alpha*s.Matrix([1,-s.I*dvar,A*dvar**2+2*r*dvar,7*s.I*r**2*dvar-13*s.I*dvar**2])
assert ((q+q.subs(alpha,-alpha))/2-mean.subs(dvar,alpha**-2)).applyfunc(s.expand)==s.zeros(4,1)
assert ((q-q.subs(alpha,-alpha))/2-diff.subs(dvar,alpha**-2)).applyfunc(s.expand)==s.zeros(4,1)
print('Odd polynomial coefficient matrix:',V)
print('Odd determinant:',det)
print('Even coefficient matrix:',E)
print('Even row minors:', [s.factor(E.extract([1,2,3],cols).det()) for cols in [(0,1,2),(0,1,3),(0,2,3),(1,2,3)]])
out={'odd_coefficient_matrix':[[str(x) for x in row] for row in V.tolist()],
 'odd_coefficient_determinant':str(det),
 'even_coefficient_matrix':[[str(x) for x in row] for row in E.tolist()],
 'quartet_odd_coefficient_determinant':str(quartet_det),
 'quartet_even_nonzero_minor':str(quartet_minor),
 'exact_sign_pair_decomposition':True,'all_assertions_passed':True}
Path(__file__).with_name('signed_evaluation_exact.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print('Quartet odd determinant:',quartet_det)
print('Quartet even nonzero minor:',quartet_minor)
print('All sign-pair, coefficient determinant, and quartet rank checks passed.')
