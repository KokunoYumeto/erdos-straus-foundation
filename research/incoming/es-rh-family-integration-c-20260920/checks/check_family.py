from __future__ import annotations
import sys
import sympy as s
from core import top_chain_data,adjoint,predicted_leakage_gram,generated_span,zero,weighted_level
from receipt import Receipt
R=Receipt('family_joint_observability')
fixtures=[[(2,1,1),(2,1,4),(0,1,2)],[(3,2,1+s.I),(1,3,2-s.I),(0,1,4)],
          [(2,1,0),(2,2,0),(0,3,0)],[(1,2,1),(1,3,2),(1,5,1)],[(0,1,2),(0,2,3)]]
for n,records in enumerate(fixtures):
    eta=s.Rational(1,3)
    G,N,T,B,g,P=top_chain_data(records,eta); Id=s.eye(G.rows)
    L=(Id-P)*adjoint(T,G)*B
    actual=L.conjugate().T*G*L
    R.equal(actual,predicted_leakage_gram(records,eta),f'full covariance {n}')
    R.equal(P*P,P,f'projection {n}')
    R.equal(P.conjugate().T*G,G*P,f'adjoint projection {n}')
    Nc=g.inv()*B.conjugate().T*G*N*B
    R.equal(N*B,B*Nc,f'forward RH invariance {n}')
    F=(Id-P)*T*B
    for j in range(B.cols):
        R.equal((F.conjugate().T*G*F)[j,j],g[j,j]*weighted_level(records,j)[4],f'forward variance {n},{j}')
    span=generated_span([N,adjoint(N,G),T,adjoint(T,G)],B)
    groups=set((D,s.simplify(t)) for D,_,t in records)
    R.equal(span.cols,sum(D+1 for D,t in groups),f'minimal common reducing dimension {n}')
    R.equal((Id-P)*N*B,s.zeros(G.rows,B.cols),f'no forward nilpotent leak {n}')
    if n==1:
        R.false(zero(actual-s.diag(*actual.diagonal())), 'unequal labels and lengths can have mixed offdiagonal terms')
    if n==3:
        R.false(zero(F), 'equal lengths do not remove ES-label leakage')
# Uploaded example without a new label operator
G,N,T,B,g,P=top_chain_data([(2,1,0),(2,1,0),(0,1,0)],s.Rational(1,3))
Z=(s.eye(G.rows)-P)*adjoint(N,G)*B
raw=Z.T*G*Z
R.equal(g,s.diag(3,s.Rational(4,9),s.Rational(8,81)),'incoming metric example')
R.equal(raw,s.diag(0,s.Rational(8,243),0),'incoming raw leak example')
R.equal(g.inv()*raw,s.diag(0,s.Rational(2,27),0),'incoming relative leak example')
# sl2 and Casimir at every retained layer
for D in range(7):
    G,N,_,_,_,_=top_chain_data([(D,2,0)],s.Rational(2,5))
    E=N/s.Rational(2,5);F=adjoint(N,G)/s.Rational(2,5);H=F*E-E*F
    R.equal(H,s.diag(*[D-2*j for j in range(D+1)]),f'H {D}')
    R.equal(H*E-E*H,-2*E,f'HE {D}')
    R.equal(H*F-F*H,2*F,f'HF {D}')
    R.equal(H*H+2*H+4*E*F,D*(D+2)*s.eye(D+1),f'Casimir {D}')
# ER7 is a projector on generated top chains, not on the ambient tensor algebra.
Cambient=s.Matrix([[8,0,0,0],[0,4,4,0],[0,4,4,0],[0,0,0,8]])
singlet=s.Matrix([0,1,-1,0])
P1=(8*s.eye(4)-Cambient)/5
R.equal(Cambient*singlet,s.zeros(4,1),'ambient tensor singlet has Casimir zero')
R.equal(P1*singlet,s.Rational(8,5)*singlet,'ambient interpolation action on singlet')
R.false(zero(P1*P1-P1),'top-chain Casimir interpolation is not an ambient projector')
# Exact mixed-binomial coefficients / hypergeometric variances, no random sampling.
for k in range(2,7):
    dimension=0;nontrivial=0
    for u in range(k+1):
        for v in range(k+1):
            lo=max(0,u+v-k); hi=min(u,v)
            weights=[s.factorial(k)/(s.factorial(j)*s.factorial(u-j)*s.factorial(v-j)*s.factorial(k-u-v+j)) for j in range(lo,hi+1)]
            total=sum(weights);mean=sum(w*j for w,j in zip(weights,range(lo,hi+1)))/total
            var=s.simplify(sum(w*(j-mean)**2 for w,j in zip(weights,range(lo,hi+1)))/total)
            R.equal(total,s.binomial(k,u)*s.binomial(k,v),f'count {k},{u},{v}')
            R.equal(mean,s.Rational(u*v,k),f'mean {k},{u},{v}')
            R.equal(var,s.Rational(u*v*(k-u)*(k-v),k*k*(k-1)),f'variance {k},{u},{v}')
            dimension+=hi-lo+1; nontrivial+=int(hi>lo)
    R.equal(dimension,s.binomial(k+3,3),f'occupation dimension {k}')
    R.equal(nontrivial,(k-1)**2,f'leakage rank count {k}')
    R.equal(dimension-(k+1)**2,s.binomial(k+1,3),f'new channels {k}')
# The k=1 boundary has singleton fibres and zero leakage, without dividing by k-1.
k=1;dimension=0;nontrivial=0
for u in range(k+1):
    for v in range(k+1):
        lo=max(0,u+v-k);hi=min(u,v)
        R.equal(lo,hi,f'k=1 singleton fibre {u},{v}')
        dimension+=hi-lo+1;nontrivial+=int(hi>lo)
R.equal(dimension,4,'k=1 occupation dimension')
R.equal(nontrivial,0,'k=1 leakage rank')
# Finite native-integral section algebra: choose an explicit complete metric,
# then a section whose extra norm is realized in a full relation kernel.
H=s.diag(2,3,5,7);J=s.Matrix([[1,0,0,0],[0,1,0,0]])
R0=s.Matrix([[1,0],[0,1],[0,0],[0,0]])
section=R0+s.Matrix([[0,0],[0,0],[1,2],[3,1]])
R.equal(J*section,s.eye(2),'exact section values')
R.equal(section.T*H*section,s.diag(2,3)+s.Matrix([[1,3],[2,1]])*s.diag(5,7)*s.Matrix([[1,2],[3,1]]),'complete section Gram')
R.false(zero(section.T*H*section-s.diag(2,3)), 'section is not canonical minimum')
R.write(sys.argv[1])
