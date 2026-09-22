#!/usr/bin/env python3
"""Gaussian-rational matrix arithmetic and exact first receiver jets. Standard library."""
from __future__ import annotations
from fractions import Fraction as F
from itertools import permutations,combinations
from math import prod

class G:
    __slots__=('re','im')
    def __init__(self,a=0,b=0):
        if isinstance(a,G):self.re,self.im=a.re,a.im
        else:self.re,self.im=F(a),F(b)
    def __add__(self,x):
        x=G(x);return G(self.re+x.re,self.im+x.im)
    __radd__=__add__
    def __neg__(self):return G(-self.re,-self.im)
    def __sub__(self,x):return self+-G(x)
    def __rsub__(self,x):return G(x)+-self
    def __mul__(self,x):
        x=G(x);return G(self.re*x.re-self.im*x.im,self.re*x.im+self.im*x.re)
    __rmul__=__mul__
    def conj(self):return G(self.re,-self.im)
    def norm(self):return self.re*self.re+self.im*self.im
    def __truediv__(self,x):
        x=G(x);n=x.norm()
        if not n:raise ZeroDivisionError
        return self*x.conj()*G(1/n)
    def __rtruediv__(self,x):return G(x)/self
    def __eq__(self,x):
        x=G(x);return self.re==x.re and self.im==x.im
    def __bool__(self):return bool(self.re or self.im)
    def __repr__(self):return f'G({self.re},{self.im})'
    def data(self):return [[self.re.numerator,self.re.denominator],[self.im.numerator,self.im.denominator]]
I=G(0,1)

def mm(A,B):return [[sum((A[i][k]*B[k][j] for k in range(len(B))),G()) for j in range(len(B[0]))]for i in range(len(A))]
def transpose(A):return list(map(list,zip(*A)))
def inv(A):
    n=len(A);T=[[G(v) for v in row]+[G(i==j) for j in range(n)] for i,row in enumerate(A)]
    for j in range(n):
        k=next(k for k in range(j,n) if T[k][j]);T[j],T[k]=T[k],T[j]
        v=T[j][j];T[j]=[x/v for x in T[j]]
        for k in range(n):
            if k!=j:
                v=T[k][j];T[k]=[x-v*y for x,y in zip(T[k],T[j])]
    return [r[n:] for r in T]
def det(A):
    n=len(A);out=G()
    for perm in permutations(range(n)):
        sign=(-1)**sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        v=G(sign)
        for i in range(n):v*=A[i][perm[i]]
        out+=v
    return out
def sub(A,r,c):return [[A[i][j] for j in c]for i in r]
def jetdet(A,B):
    a=det(A);b=G()
    for i in range(len(A)):
        T=[list(row) for row in A];T[i]=list(B[i]);b+=det(T)
    return a,b

# Root differences are exact Laurent polynomials. S^-1 through z^8 gives
# every normalized derivative unit at least five correct relative terms.
# Every separately rescaled receiver summand has nonnegative valuation;
# the largest prefactor z^6 still retains z^6 and z^7. Thus the constant
# and linear coefficients used below are unaffected by truncation.
LIMIT=8
class L:
    def __init__(self,x=0):
        self.d={k:F(v) for k,v in (x.items() if isinstance(x,dict) else {0:x}.items()) if v and k<=LIMIT}
    def __add__(self,x):
        x=toL(x);d=self.d.copy()
        for k,v in x.d.items():d[k]=d.get(k,F())+v
        return L(d)
    __radd__=__add__
    def __neg__(self):return L({k:-v for k,v in self.d.items()})
    def __sub__(self,x):return self+-toL(x)
    def __rsub__(self,x):return toL(x)+-self
    def __mul__(self,x):
        x=toL(x);d={}
        for i,a in self.d.items():
            for j,b in x.d.items():
                if i+j<=LIMIT:d[i+j]=d.get(i+j,F())+a*b
        return L(d)
    __rmul__=__mul__
    def __pow__(self,n):
        if n<0:return self.recip()**(-n)
        ans=L(1)
        for _ in range(n):ans=ans*self
        return ans
    def recip(self):
        v=min(self.d);a=self.d[v];c={0:1/a}
        for n in range(1,LIMIT+v+1):
            c[n]=-sum((self.d.get(v+k,F())*c[n-k] for k in range(1,n+1)),F())/a
        return L({k-v:x for k,x in c.items()})
    def __truediv__(self,x):return self*toL(x).recip()
    def __rtruediv__(self,x):return toL(x)*self.recip()
    def shift(self,n):return L({k+n:v for k,v in self.d.items()})
    def coefficient(self,n):return self.d.get(n,F())
    def inverse_sqrt_unit(self):
        if self.coefficient(0)!=1 or min(self.d)!=0:raise ValueError('unit square-root input')
        # Generalized binomial series in V-1; exact, finite in each coefficient.
        X=self-1; ans=L(1);power=L(1);coef=F(1)
        for n in range(1,LIMIT+1):
            power=power*X;coef*=F(-2*n+1,2*n);ans+=coef*power
        return ans

def toL(x):return x if isinstance(x,L) else L(x)

def direct_first_jet(R:int,u:int):
    """Derive tilde B=B diag(C,C,1,1) from the literal receiver, not printed jets."""
    p=L({-1:1});a=(p+R)/4;Y=p*(a+u)/R;Z=p*a*(a+u)/(R*u)
    roots=[p,a,Y,Z];S=sum(roots,L());AA=-1/S
    ds=[AA*prod((roots[j]-roots[k] for k in range(4) if k!=j),start=L(1)) for j in range(4)]
    C2=F(3,16*R);alpha=F(1,4*R);beta=F(1,16*R*u)
    leads=[(-3,-C2),(-3,C2),(-4,alpha**2),(-6,-beta**2)]
    shifts=[0,0,2,6];phases=[I,G(1),G(1),I];coeff=[F(1),F(1),1/alpha,1/beta]
    B=[[[G(),G()]for j in range(4)] for i in range(4)]
    for j,(val,lead) in enumerate(leads):
        if min(ds[j].d)!=val or ds[j].coefficient(val)!=lead:raise ArithmeticError('literal derivative valuation')
        unit=ds[j].shift(-val)/lead; xi=unit.inverse_sqrt_unit().shift(shifts[j])*coeff[j]
        polys=[xi,xi*ds[j],xi*(AA*ds[j]**2+2*roots[j]*ds[j]),
               xi*(7*roots[j]**2*ds[j]-13*ds[j]**2)]
        rowph=[G(1),-I,G(1),I]
        for i,rowshift in enumerate((0,3,4,6)):
            V=polys[i].shift(rowshift)
            if any(k<0 and v for k,v in V.d.items()):raise ArithmeticError('nonanalytic B entry')
            B[i][j]=[phases[j]*rowph[i]*V.coefficient(k) for k in (0,1)]
    return [[B[i][j][0]for j in range(4)]for i in range(4)],[[B[i][j][1]for j in range(4)]for i in range(4)]

def claimed_first_jet(R:int,u:int):
    R,u=F(R),F(u);C2=F(3)/(16*R);alpha=1/(4*R);beta=1/(16*R*u)
    # Both first columns multiplied by C. Every entry is now Gaussian rational.
    B0=[[I,1,0,0],[-C2,-I*C2,0,0],[-2*I*C2,C2/2,2*alpha**2,0],
        [13*C2**2,-13*I*C2**2,-6*I*alpha**3,20*beta**3]]
    B1=[[5*R*I/3,R/6,0,0],[5*R*C2/3,I*R*C2/6,-I*alpha,0],
        [I*(10*R*C2/3-C2**2/beta),5*R*C2/12-C2**2/beta,(-R+4*u)*alpha**2,-3*I*beta**2],
        [7*C2-65*R*C2**2,I*(13*R*C2**2/2+7*C2/16),I*(62*R+56*u)*alpha**3,(120*R+56*u)*beta**3]]
    return [[G(x)for x in row]for row in B0],[[G(x)for x in row]for row in B1]

def matrixdata(M):return [[x.data()for x in row]for row in M]
