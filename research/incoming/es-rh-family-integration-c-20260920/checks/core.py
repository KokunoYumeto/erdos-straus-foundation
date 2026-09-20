"""Exact finite interfaces for the general-family integration.

These routines consume supplied finite matrices. They do not evaluate native
zeta moments, infer unavailable ranks, or change a source metric.
"""
from __future__ import annotations
from collections import defaultdict
from itertools import combinations
from math import comb
import sympy as sp


def zero(M):
    if isinstance(M, sp.MatrixBase):
        return all(sp.simplify(x)==0 for x in M)
    return sp.simplify(M)==0


def adjoint(A,G):
    return G.inv()*A.conjugate().T*G


def top_chain_data(records, eta):
    """records = [(D, positive_weight, ES_centre), ...], common RH centre 0.

    Duplicate records remain separate ambient components. The cyclic metric
    counts their actual weights. All powers are divided-jet basis powers R^j.
    """
    if not records or any(int(d)!=d or d<0 for d,_,_ in records):
        raise ValueError('Nonnegative integer chain degrees required')
    eta=sp.sympify(eta)
    Dmax=max(d for d,_,_ in records)
    dim=sum(d+1 for d,_,_ in records)
    G=sp.zeros(dim); R=sp.zeros(dim); T=sp.zeros(dim); beta=sp.zeros(dim,Dmax+1)
    offset=0
    for D,weight,theta in records:
        for j in range(D+1):
            G[offset+j,offset+j]=weight*sp.factorial(j)**2*sp.binomial(D,j)*eta**(2*j)
            beta[offset+j,j]=1
            T[offset+j,offset+j]=theta
            if j<D:
                R[offset+j+1,offset+j]=1
        offset+=D+1
    T+=R
    g=beta.T.conjugate()*G*beta
    P=beta*g.inv()*beta.T.conjugate()*G
    return G,R,T,beta,g,P


def weighted_level(records,j):
    weights=[sp.sympify(w)*sp.binomial(D,j) for D,w,_ in records]
    S=sum(weights)
    if S==0: raise ValueError('Empty level')
    ps=[sp.cancel(w/S) for w in weights]
    meanD=sum(p*D for p,(D,_,_) in zip(ps,records))
    meanT=sum(p*t for p,(_,_,t) in zip(ps,records))
    varD=sp.expand(sum(p*(D-meanD)**2 for p,(D,_,_) in zip(ps,records)))
    varT=sp.expand(sum(p*sp.conjugate(t-meanT)*(t-meanT) for p,(_,_,t) in zip(ps,records)))
    covTD=sp.expand(sum(p*(t-meanT)*(D-meanD) for p,(D,_,t) in zip(ps,records)))
    return S,meanD,meanT,sp.simplify(varD),sp.simplify(varT),sp.simplify(covTD)


def predicted_leakage_gram(records,eta):
    """Raw Gram for (I-P) T_ES^dagger beta; includes mixed covariance."""
    eta=sp.sympify(eta); d=max(D for D,_,_ in records)
    lev=[weighted_level(records,j) for j in range(d+1)]
    out=sp.zeros(d+1)
    for j in range(d+1):
        Sj=lev[j][0]; gj=sp.factorial(j)**2*eta**(2*j)*Sj
        diagonal=lev[j][4]
        if j:
            diagonal+=eta**2*lev[j-1][0]/Sj*lev[j-1][3]
        out[j,j]=sp.simplify(gj*diagonal)
        if j<d:
            out[j,j+1]=sp.simplify(gj*eta**2*(j+1)*lev[j][5])
            out[j+1,j]=sp.conjugate(out[j,j+1])
    return out


def generated_span(matrices, generators):
    """Small exact diagnostic closure, never a large native-algebra builder."""
    if generators.cols==0:return generators
    cols=generators.columnspace(); B=sp.Matrix.hstack(*cols)
    while True:
        C=sp.Matrix.hstack(B,*[A*B for A in matrices])
        independent=C.columnspace()
        if len(independent)==B.cols:return B
        B=sp.Matrix.hstack(*independent)


def collision_exponents(e,f,a):
    """All singular valuation exponents for eta=|z|^a, e>=f>=1."""
    if not (isinstance(e,int) and isinstance(f,int) and e>=f>=1):
        raise ValueError('e>=f>=1 are required')
    a=sp.Rational(a)
    if a<0:raise ValueError('a must be nonnegative')
    if a<=1:
        return [a*j for j in range(e)]+[e-f+2*j-1+a*(f-j) for j in range(1,f+1)]
    out=[]
    for j in range(f):out.extend([(a+1)*j,(a+1)*j+1])
    out.extend([a*j+f for j in range(f,e)])
    return out


def collision_minors(e,f):
    """(derivative-weight sum, z-order) for each NONZERO exact minor.

    E(z)_{first,j;n}=1_{j=n}; E(z)_{second,j;n}=binom(n,j)z^(n-j).
    Each row scaling is eta^j. Factoring row and column monomials shows
    every nonzero minor has one exact monomial; the coefficient is a
    confluent evaluation minor at z=1.
    """
    n=e+f; rows=[(0,j) for j in range(e)]+[(1,j) for j in range(f)]
    def det_integer(A):
        # Exact fraction-free elimination; no floating eigenvalues are used.
        m=len(A)
        if m==0:return 1
        A=[list(row) for row in A]; prev=1; sign=1
        for k in range(m-1):
            if A[k][k]==0:
                p=next((i for i in range(k+1,m) if A[i][k]),None)
                if p is None:return 0
                A[k],A[p]=A[p],A[k];sign=-sign
            pivot=A[k][k]
            for i in range(k+1,m):
                for j in range(k+1,m):
                    numerator=A[i][j]*pivot-A[i][k]*A[k][j]
                    if numerator % prev:raise ArithmeticError('Nonexact Bareiss division')
                    A[i][j]=numerator//prev
                A[i][k]=0
            prev=pivot
        return sign*A[-1][-1]
    out={0:[(0,0)]}
    for r in range(1,n+1):
        pairs=set()
        for I in combinations(range(n),r):
            first={rows[i][1] for i in I if rows[i][0]==0}
            second=[rows[i][1] for i in I if rows[i][0]==1]
            weight=sum(rows[i][1] for i in I)
            for J in combinations(range(n),r):
                if not first.issubset(J):continue
                remaining=[m for m in J if m not in first]
                # Laplace expansion along the first-centre identity rows.
                coefficient=det_integer([[comb(m,j) if m>=j else 0 for m in remaining] for j in second])
                if coefficient:
                    order=sum(J)-weight
                    if order<0:raise ArithmeticError('Impossible negative polynomial order')
                    pairs.add((weight,order))
        out[r]=sorted(pairs)
    return out



def joint_minimum(H,X,Jphysical,R):
    """Construct the full canonical/section joint minimum in an ambient source.

    X embeds the scalar source, R is a section for Jphysical on its image.
    HZ may be singular. Equality of values on coincident physical vectors is
    required, not repaired with a numerical diagonal regularizer.
    """
    star=lambda A:A.conjugate().T
    J=Jphysical*X
    if not zero(Jphysical*R-sp.eye(R.cols)):
        raise ValueError('R is not a section of the given physical value map')
    HX=star(X)*H*X
    G=(J*HX.inv()*star(J)).inv()
    C=star(X)*H*R
    HZ=star(R)*H*R-star(C)*HX.inv()*C
    F=sp.eye(R.cols)-J*HX.inv()*C
    for v in HZ.nullspace():
        if not zero(F*v):raise ValueError('Value map does not kill the actual Gram kernel')
    Cov=F*HZ.pinv()*star(F)
    Gjoint=(G.inv()+Cov).inv()
    return {"G":G,"HX":HX,"C":C,"HZ":HZ,"F":F,"covariance":Cov,"joint":Gjoint}
