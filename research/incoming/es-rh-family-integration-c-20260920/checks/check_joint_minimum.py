from __future__ import annotations
import sys
from itertools import combinations
import sympy as s
from core import joint_minimum,zero
from receipt import Receipt
R=Receipt('complete_source_minimum_and_allocation')

def psd_exact(A):
    if not zero(A-A.conjugate().T):return False
    for r in range(1,A.rows+1):
        for I in combinations(range(A.rows),r):
            if s.simplify(A.extract(I,I).det())<0:return False
    return True

H=s.diag(2,3,5,7,11,13,17,19)
X=s.eye(8)[:,:5]
A=s.Matrix([[1,0,1,2,-1],[0,1,1,0,2],[1,1,0,-1,1]])
J=s.eye(3).row_join(A)
bottom=s.Matrix([[0,1,0],[1,0,1],[1,0,1],[0,1,s.I],[1,1,1+s.I]])
section=(s.eye(3)-A*bottom).col_join(bottom)
data=joint_minimum(H,X,J,section)
Y=s.Matrix.hstack(X,section)
Y=s.Matrix.hstack(*Y.columnspace())
HY=Y.conjugate().T*H*Y
JY=J*Y
Gdirect=(JY*HY.inv()*JY.conjugate().T).inv()
R.equal(data['joint'],Gdirect,'complete joint quotient equals direct physical minimum')
R.equal(data['HZ'].rank(),2,'actual singular normal Gram rank')
R.equal(data['F']*(s.eye(3)-data['HZ'].pinv()*data['HZ']),s.zeros(3),'normal Gram kernel killed by values')
R.require(psd_exact(data['G']-data['joint']),'joint metric below canonical')
R.require(psd_exact(section.conjugate().T*H*section-data['joint']),'joint below section metric')
R.false(zero(data['C']), 'cross Gram is retained')
R.false(zero(data['joint']-(data['G'].inv()+(section.conjugate().T*H*section).inv()).inv()),'section is not an independent orthogonal source')
# Regularization on the actual positive range and its explicit positive floor.
HZ=data['HZ'];r=HZ.rank();trace=s.trace(HZ)
pdet=sum(HZ.extract(I,I).det() for I in combinations(range(HZ.rows),r))
lambda0=s.simplify(pdet/trace**(r-1))
R.require(lambda0>0,'explicit range floor')
# Quantifier guard for JS12: an arbitrary valid floor need not dominate the
# determinant/trace floor.  For H=[2], mu=2 and 1 is a valid weaker floor.
Hguard=s.Matrix([[2]])
mu_guard=Hguard[0,0]
chosen_floor=s.Integer(1)
det_floor_guard=Hguard.det()
R.require(0<chosen_floor<=mu_guard,'arbitrary certified floor lies below actual positive eigenvalue')
R.false(chosen_floor>=det_floor_guard,'arbitrary certified floor cannot replace determinant trace floor')
V=s.Matrix.hstack(*HZ.columnspace())
C_range=data['F']*V*(V.conjugate().T*HZ*V).inv()*V.conjugate().T*data['F'].conjugate().T
R.equal(C_range,data['covariance'],'range inverse agrees with Moore-Penrose sandwich')
for delta in [s.Rational(1,100),s.Rational(1,5),s.Rational(1)]:
    Ce=data['F']*(HZ+delta*s.eye(HZ.rows)).inv()*data['F'].conjugate().T
    theta=lambda0/(lambda0+delta)
    R.require(psd_exact(data['covariance']-Ce),'regularized covariance below exact')
    R.require(psd_exact(Ce-theta*data['covariance']),'regularized covariance lower bound')
    Ge=(data['G'].inv()+Ce).inv()
    R.require(psd_exact(Ge-data['joint']),'regularized metric above exact')
    R.require(psd_exact(data['joint']/theta-Ge),'regularized metric upper bound')
    R.require(s.factor(Ge.det()/data['joint'].det())<=theta**(-data['covariance'].rank()),'rank-aware determinant error')
# Full observed/kernel allocation in an explicitly whitened original metric.
Ghalf=s.diag(2,3,4,5);G=Ghalf**2
U=s.Matrix([[1,1+s.I,0,2],[0,1,1-s.I,1]])
T=U.conjugate().T*U
Gjoint=Ghalf*(s.eye(4)+T).inv()*Ghalf
K=Ghalf.inv()[:,:2]
Lam=s.eye(4)[2:,:]*Ghalf
Qnew=(Lam*Gjoint.inv()*Lam.conjugate().T).inv()
T11=T[:2,:2];T12=T[:2,2:];T22=T[2:,2:]
SK=T11-T12*(s.eye(2)+T22).inv()*T12.conjugate().T
R.equal(Qnew,(s.eye(2)+T22).inv(),'actual quotient allocation')
R.equal(K.conjugate().T*Gjoint*K,(s.eye(2)+SK).inv(),'actual restricted-kernel allocation')
R.equal((s.eye(4)+T).det(),(s.eye(2)+T22).det()*(s.eye(2)+SK).det(),'complete positive determinant split')
R.require(psd_exact(SK),'Schur allocation positive')
R.false(zero(SK-T11),'mixed block cannot be deleted')
# Three exact input vectors: every complex observed/kernel Gram is retained.
W=s.Matrix([[1,s.I,1],[0,1,2],[1,2,s.I],[1-s.I,0,1]])
Full=W.conjugate().T*Gjoint*W
Obs=W.conjugate().T*Lam.conjugate().T*Qnew*Lam*W
Ker=Full-Obs
R.equal(Full,Obs+Ker,'full three-vector split')
R.require(psd_exact(Obs) and psd_exact(Ker),'full joint PSD constraints')
# Explicit orientation counterexample: same source determinant, different observation gains.
T=s.diag(9,0);I=s.eye(2)
for v,expected in [(s.Matrix([[1],[0]]),10),(s.Matrix([[0],[1]]),1),(s.Matrix([[s.Rational(3,5)],[s.Rational(4,5)]]),s.Rational(106,25))]:
    gain=1+(v.T*T*v)[0]
    R.equal(gain,expected,'orientation-dependent observed determinant')
R.false((1+T[0,0])==(1+T[1,1]),'equal total volume does not fix its split')
# A source section entirely in the old scalar space can have a changed metric but no added minimum.
H2=s.diag(2,3,5);J2=s.Matrix([[1,0,0],[0,1,0]]);X2=s.eye(3)
R2=s.Matrix([[1,0],[0,1],[3,4]])
d2=joint_minimum(H2,X2,J2,R2)
R.equal(d2['covariance'],s.zeros(2),'pure relation section adds no covariance')
R.equal(d2['joint'],d2['G'],'same source minimum retained')
R.false(zero(R2.T*H2*R2-d2['G']),'new section metric can differ despite zero joint gain')
# Sharp two-minimum-cost bound in diagonal metrics (exponentiate the logarithms).
for gc,gs in [([16,1],[1,9]),([16,4,1,1],[1,1,9,25]),([1,1,1],[3,5,7])]:
    ratios=sorted([s.Rational(b,a) for a,b in zip(gc,gs)],reverse=True)
    m=len(gc)//2
    exp_distance=s.prod(ratios[:m])/s.prod(ratios[len(gc)-m:]) if m else s.Integer(1)
    exp_cost=s.prod(gc)*s.prod(gs)
    R.require(exp_distance<=exp_cost,'complete two-minimum determinant cost')
R.equal(s.Rational(9)/(s.Rational(1,16)),144,'sharp two-dimensional cost')
R.extra['rank_deficient_fixture']={'normal_rank':int(r),'normal_positive_floor':str(lambda0),'joint_determinant':str(data['joint'].det())}
R.write(sys.argv[1])
