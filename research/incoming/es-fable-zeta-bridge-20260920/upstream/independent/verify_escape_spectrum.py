"""Independent exact differential and compound certificate, no data imports."""
import itertools
import json
from pathlib import Path
import sympy as sp

a,y,z,w,ep=sp.symbols('a y z w epsilon', nonzero=True)
i=sp.I
P=sp.Matrix([
 a**3*z+2*a**2*y-i*a,
 -a**3*y**2*z-2*i*a**2*y*z+a**2*w-2*a**2*y**3-10*i*a*y**2+3*a*z+y,
 2*a**3*y**3*z+6*i*a**2*y**2*z+2*a**2*w*y+4*a**2*y**4+2*i*a*w-4*i*a*y**3-2*a*y*z+2*i*z+7*y**2,
 2*a**3*y**4*z+8*i*a**2*y**3*z+a**2*w*y**2+4*a**2*y**5+2*i*a*w*y+7*i*a*y**4-10*a*y**2*z-4*i*y*z-w-3*y**3])
q=sp.Matrix([-ep,2*i/ep,6*i/ep**2-i/2,40*i/ep**3])
sub=dict(zip((a,y,z,w),q))
J=P.jacobian((a,y,z,w)).subs(sub).applyfunc(sp.expand)
Jprinted=sp.Matrix([
 [9*i-3*i*ep**2/2,2*ep**2,-ep**3,0],
 [-7*i/2-30*i/ep**2,ep**2-27,-3*ep,ep**2],
 [-2/ep+104/ep**3,-i*ep-56*i/ep,-2*i,2*i*ep],
 [-4*i/ep**2+64*i/ep**4,2+28/ep**2,0,-1]])
Inv=sp.Matrix([
 [3*i*ep**2/2-i,-3*i*ep**4/2+2*i*ep**2,3*ep**5/2-5*ep**3/2,3*i*ep**6/2-3*i*ep**4],
 [-sp.Rational(3,2)+2/ep**2,3*ep**2/2-3,3*i*ep**3/2-7*i*ep/2,-3*ep**4/2+4*ep**2],
 [9*ep/4-18/ep+12/ep**3,-9*ep**3/4+39*ep/2-24/ep,-9*i*ep**4/4+81*i*ep**2/4-59*i/2,9*ep**5/4-21*ep**3+35*ep],
 [3-138/ep**2+120/ep**4,-3*ep**2+140-212/ep**2,-3*i*ep**3+141*i*ep-258*i/ep,3*ep**4-142*ep**2+303]])
assert (J-Jprinted).applyfunc(sp.simplify)==sp.zeros(4)
assert sp.expand(J.det())==-2
assert (J*Inv-sp.eye(4)).applyfunc(sp.expand)==sp.zeros(4)
assert (Inv*J-sp.eye(4)).applyfunc(sp.expand)==sp.zeros(4)
p=P.subs(sub).applyfunc(sp.expand)
assert p==sp.Matrix([-i*ep+i*ep**3/2,3*i*ep/2,-1,0])
assert (J*q.diff(ep)-p.diff(ep)).applyfunc(sp.expand)==sp.zeros(4,1)

def compound(A,r):
    ix=list(itertools.combinations(range(4),r))
    return ix,sp.Matrix([[sp.expand(A.extract(I,J).det()) for J in ix] for I in ix])

def leading(A):
    terms=[(r,c,sp.expand(A[r,c])) for r in range(A.rows) for c in range(A.cols) if A[r,c]!=0]
    minexp=min(int(term.as_powers_dict().get(ep,0)) for _,_,v in terms for term in sp.Add.make_args(v))
    lead=A.applyfunc(lambda v:sp.expand(v).coeff(ep,minexp))
    return minexp,lead

report={'J_equals_FC57':True,'inverse_equals_FC58':True,'determinant':str(J.det().expand()),'velocity_identity_FC63':True,'compounds':[]}
exponents=(-4,-5,-4,0)
fwd=(64*i,-672,240,-2)
rev=(120,336,32*i,-sp.Rational(1,2))
positions=((3,0),(5,0),(3,0),(0,0))
for r in range(1,5):
    labels,C=compound(J,r)
    _,D=compound(Inv,r)
    power,H=leading(C)
    invpower,I=leading(D)
    E=sp.zeros(len(labels)); E[positions[r-1]]=fwd[r-1]
    F=sp.zeros(len(labels)); F[positions[r-1]]=rev[r-1]
    assert power==invpower==exponents[r-1]
    assert H==E and I==F
    assert (C*D-sp.eye(len(labels))).applyfunc(sp.expand)==sp.zeros(len(labels))
    report['compounds'].append({'r':r,'minimum_laurent_exponent':power,'row_subset':[j+1 for j in labels[positions[r-1][0]]],'column_subset':[j+1 for j in labels[positions[r-1][1]]],'forward_leading_coefficient':str(fwd[r-1]),'inverse_leading_coefficient':str(rev[r-1]),'compound_inverse_check':True})
text=json.dumps(report,indent=2)
Path(__file__).with_name('verify_escape_spectrum_output.json').write_text(text+'\n',encoding='utf-8')
print(text)
