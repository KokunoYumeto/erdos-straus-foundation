import sympy as s
from common import Suite,ROOT,companion,residue_gram,poly_matrix_eval
T=Suite('residue_duality')
r=s.symbols('r');A,B,C,D=s.symbols('A B C D',nonzero=True)
h=A*r**4+r**3+B*r**2+C*r+D
J=residue_gram(h,r)
expected=s.Matrix([[0,0,0,1/A],[0,0,1/A,-1/A**2],[0,1/A,-1/A**2,1/A**3-B/A**2],[1/A,-1/A**2,1/A**3-B/A**2,-1/A**4+2*B/A**3-C/A**2]])
T.equal('generic quartic residue Gram',J,expected)
T.equal('generic residue determinant',J.det(method='domain-ge'),A**-4)
Cr=companion(h,r)
T.equal('multiplication is residue-self-adjoint',J*Cr,Cr.T*J)
trpoly=s.Matrix(4,4,lambda i,j:s.trace(Cr**(i+j)))
dCr=poly_matrix_eval(s.diff(h,r),Cr,r)
T.equal('quartic trace equals residue times derivative',J*dCr,trpoly)
# Entire 8-dimensional completed algebra: exact matrices, no branch choices.
zero=s.zeros(4);I=s.eye(4)
Meta=zero.row_join(dCr).col_join(I.row_join(zero))
Mr=s.diag(Cr,Cr)
JF=zero.row_join(J).col_join(J.row_join(zero))
T.equal('eta squared equals h prime',Meta**2,s.diag(dCr,dCr))
T.equal('r and eta commute',Mr*Meta,Meta*Mr)
T.equal('residue duality determinant',JF.det(method='domain-ge'),A**-8)
T.equal('eta self-adjoint for residue pairing',JF*Meta,Meta.T*JF)
Trace=s.diag(2*trpoly,2*trpoly*dCr)
T.equal('trace Gram = residue Gram times 2 eta cubed',JF*(2*Meta**3),Trace)
# Check determinant formula on generic symbolic quartic through the smaller 4x4 block.
disc=s.discriminant(h,r)
T.equal('norm of derivative',dCr.det(method='domain-ge'),disc/A**2)
T.equal('quartic trace determinant',trpoly.det(method='domain-ge'),disc/A**6)
# Bounded literal roots do not by themselves bound the coefficient base.
u=s.symbols('u',positive=True)
counter_roots=[1,1+u**4,-1,-1-u**4+u**3]
counter_A=-1/s.Add(*counter_roots)
counter_h=s.expand(counter_A*s.prod(r-x for x in counter_roots))
counter_d=s.factor(s.diff(counter_h,r).subs(r,1))
T.equal('bounded-root boundary example has eta squared tending to zero',s.limit(counter_d,u,0,dir='+'),0)
T.equal('bounded-root boundary example has divergent third scaled coordinate term',s.limit(u*counter_A*counter_d**2,u,0,dir='+'),-16)
T.reject('bounded roots alone do not force eta q to e1',s.limit(u*counter_A*counter_d**2,u,0,dir='+')==0)
# Exact universal local fibres and trace ranks.  Only m=2,3,4 occur in the
# quartic application; m=5,6,7 check the same generalized degree-m model.
local=[]
for m in range(2,8):
    e=s.symbols('e');Cm=companion(e**m,e);dm=m*3*Cm**(m-1)
    M=s.zeros(m).row_join(dm).col_join(s.eye(m).row_join(s.zeros(m)))
    Euler=2*M**3
    T.require(f'm={m} length',M.rows==2*m)
    T.require(f'm={m} trace-map rank one',Euler.rank()==1)
    T.equal(f'm={m} eta^4 zero',M**4,s.zeros(2*m))
    T.require(f'm={m} eta^3 nonzero',M**3!=s.zeros(2*m))
    local.append({'multiplicity':m,'length':2*m,'trace_rank':1})
# Explicit moment carrier for rational simple roots: no radicals needed to test U U^T.
roots=[s.Rational(1),s.Rational(2),s.Rational(4),s.Rational(9)]
a=-1/sum(roots); hh=a*s.prod(r-x for x in roots);V=s.Matrix(4,4,lambda n,j:roots[j]**n)
di=[s.diff(hh,r).subs(r,x) for x in roots]
T.equal('signed moment carrier square equals residue Gram',V*s.diag(*[1/x for x in di])*V.T,residue_gram(hh,r))
T.reject('trace pairing is not invertible on double root', (2*s.Matrix([[0,1,0,0],[0,0,1,0],[0,0,0,1],[0,0,0,0]])**3).det()!=0)
(ROOT/'results'/'residue_matrices.txt').write_text('J_h =\n'+str(J)+'\ntrace discriminant = 256 Disc(h)^3/A^14\n')
T.save({'trace_determinant':'256*Disc(h)^3/A^14','residue_determinant':'A^(-8)','local_fibres':local})
