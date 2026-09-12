#!/usr/bin/env python3
"""Exact three-slot/Jordan/ES continuation certificates. Standard library only.

Run normally and with -O; both runs print identical JSON. All checks use runtime
exceptions, not removable assertions. Finite tests and formal polynomial identities
are labelled separately. No claim of an ES or Schanuel proof is made.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from functools import reduce
from itertools import product, permutations, combinations
from math import gcd, lcm
from pathlib import Path
import json


def need(ok, message):
    if not ok:
        raise ArithmeticError(message)


class P:
    """Sparse exact multivariate polynomial; exponent tuples, rational coefficients."""
    def __init__(self, n, terms=None):
        self.n = n
        self.d = {e: F(c) for e,c in (terms or {}).items() if c}
    @classmethod
    def scalar(cls,n,c):
        return cls(n,{(0,)*n:F(c)})
    @classmethod
    def var(cls,n,i):
        e=[0]*n;e[i]=1
        return cls(n,{tuple(e):1})
    def coerce(self,o):
        if isinstance(o,P):
            need(o.n==self.n,'Polynomial arity mismatch')
            return o
        return P.scalar(self.n,o)
    def __add__(self,o):
        o=self.coerce(o);d=self.d.copy()
        for e,c in o.d.items():d[e]=d.get(e,0)+c
        return P(self.n,d)
    __radd__=__add__
    def __neg__(self):return P(self.n,{e:-c for e,c in self.d.items()})
    def __sub__(self,o):return self+-self.coerce(o)
    def __rsub__(self,o):return self.coerce(o)+-self
    def __mul__(self,o):
        o=self.coerce(o);d={}
        for e,c in self.d.items():
            for f,b in o.d.items():
                g=tuple(x+y for x,y in zip(e,f));d[g]=d.get(g,0)+c*b
        return P(self.n,d)
    __rmul__=__mul__
    def __truediv__(self,c):return self*F(1,c)
    def __pow__(self,k):
        need(isinstance(k,int) and k>=0,'Invalid polynomial power')
        a=P.scalar(self.n,1);b=self
        while k:
            if k&1:a=a*b
            b=b*b;k>>=1
        return a
    def __eq__(self,o):return self.d==self.coerce(o).d
    def __bool__(self):return bool(self.d)
    def records(self):
        return [{'powers':list(e),'coefficient':frac(c)} for e,c in sorted(self.d.items())]


def frac(x):
    x=F(x)
    return x.numerator if x.denominator==1 else {'numerator':x.numerator,'denominator':x.denominator}


def dot(x,y):return sum(a*b for a,b in zip(x,y))
def cross(x,y):return [x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0]]
def tr(A):return sum(A[i][i] for i in range(3))
def mt(A):return [list(row) for row in zip(*A)]
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
def mv(A,x):return [dot(r,x) for r in A]
def outer(x,y):return [[a*b for b in y] for a in x]
def madd(A,B):return [[x+y for x,y in zip(r,s)] for r,s in zip(A,B)]
def smul(t,A):return [[t*x for x in r] for r in A]
def det(A):
    return sum((1 if sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2==0 else -1)
               *A[0][p[0]]*A[1][p[1]]*A[2][p[2]] for p in permutations(range(3)))
def adj(A):
    return [[(-1)**(i+j)*(A[[k for k in range(3) if k!=j][0]][[k for k in range(3) if k!=i][0]]
                              *A[[k for k in range(3) if k!=j][1]][[k for k in range(3) if k!=i][1]]
                              -A[[k for k in range(3) if k!=j][0]][[k for k in range(3) if k!=i][1]]
                              *A[[k for k in range(3) if k!=j][1]][[k for k in range(3) if k!=i][0]])
             for j in range(3)] for i in range(3)]
def zero3():return [[0]*3 for _ in range(3)]
def eye3():return [[int(i==j) for j in range(3)] for i in range(3)]
def basis3(i):return [int(i==j) for j in range(3)]
def emat(i,j):return [[int(a==i and b==j) for b in range(3)] for a in range(3)]
def flat(X):return [v for A in X for r in A for v in r]
def unflat(v):return [[list(v[9*i+3*j:9*i+3*j+3]) for j in range(3)] for i in range(3)]

def norm(X):
    A,B,C=X
    return det(A)+det(B)+det(C)-tr(mm(C,mm(B,A)))
def quadratic_trace(X):
    A,B,C=X
    return tr(adj(A))-tr(mm(C,B))

def Du(X,abc):
    A,B,C=X;a,b,c=abc
    return [outer(b,cross(a,mv(C,c))),outer(c,cross(b,mv(A,a))),outer(a,cross(c,mv(B,b)))]

def slice_matrix(T,axis,w):
    others=[i for i in range(3) if i!=axis]
    M=zero3()
    for j,k in product(range(3),repeat=2):
        for i in range(3):
            ix=[0,0,0];ix[axis]=i;ix[others[0]]=j;ix[others[1]]=k
            M[j][k]+=w[i]*T[ix[0]][ix[1]][ix[2]]
    return M

def tzero():return [[[0]*3 for _ in range(3)] for _ in range(3)]
def evaluate(T,u,v,w):return sum(T[i][j][k]*u[i]*v[j]*w[k] for i,j,k in product(range(3),repeat=3))

def primitive(x):
    xs=[F(a) for a in x];d=lcm(*(a.denominator for a in xs));xs=[int(a*d) for a in xs]
    g=reduce(gcd,xs,0);need(g!=0,'Zero projective vector')
    xs=[a//g for a in xs]
    if next(a for a in xs if a)<0:xs=[-a for a in xs]
    return tuple(xs)

def kernel_rank_two(A):
    need(det(A)==0,'Kernel map outside determinant curve')
    for i,j in combinations(range(3),2):
        v=cross(A[i],A[j])
        if any(v):
            need(all(dot(r,v)==0 for r in A),'Failed rank-two kernel')
            return primitive(v)
    raise ArithmeticError('Rank-one/zero exceptional locus')

def cube_step(T,axis,v,target):
    need(axis!=target,'Cube step needs distinct slots')
    others=[i for i in range(3) if i!=axis]
    M=slice_matrix(T,axis,v)
    return kernel_rank_two(mt(M) if target==others[0] else M)


def rref(A):
    A=[[F(x) for x in r] for r in A];row=0;piv=[]
    if not A:return A,piv
    for j in range(len(A[0])):
        pick=next((i for i in range(row,len(A)) if A[i][j]),None)
        if pick is None:continue
        A[row],A[pick]=A[pick],A[row]
        c=A[row][j];A[row]=[x/c for x in A[row]]
        for i in range(len(A)):
            if i!=row and A[i][j]:
                c=A[i][j];A[i]=[x-c*y for x,y in zip(A[i],A[row])]
        piv.append(j);row+=1
        if row==len(A):break
    return A,piv

def nullspace(A):
    R,piv=rref(A);n=len(A[0]);out=[]
    for j in range(n):
        if j in piv:continue
        v=[F(0)]*n;v[j]=1
        for row,col in enumerate(piv):v[col]=-R[row][j]
        out.append(v)
    return out


MOORE=[[[1,0,0],[0,0,2],[0,3,0]],[[0,0,3],[0,1,0],[2,0,0]],[[0,2,0],[3,0,0],[0,0,1]]]
def hesse(v):
    x,y,z=v;return x**3+y**3+z**3-6*x*y*z

def finite_hesse(p):
    points=[]
    # Unique projective representatives: first nonzero coordinate equals one.
    for v in [(1,y,z) for y,z in product(range(p),repeat=2)]+[(0,1,z) for z in range(p)]+[(0,0,1)]:
        if hesse(v)%p==0:points.append(v)
    return points

def check_moore():
    vs=[P.var(3,i) for i in range(3)]
    for ax in range(3):need(det(slice_matrix(MOORE,ax,vs))==-6*hesse(vs),'Moore determinant polynomial')
    orbit=[(1,-1,0)]
    for n in range(9):
        ax=n%3;tar=(ax+1)%3
        v=cube_step(MOORE,ax,orbit[-1],tar)
        need(hesse(v)==0,'Orbit leaves Hesse curve')
        need(cube_step(MOORE,tar,v,ax)==orbit[-1],'Kernel-map inverse lost marking')
        orbit.append(v)
    need(orbit[3]==(1817,5275,3258),'First complete turn')
    need(orbit[9]!=(1,-1,0),'Translation would be 3-torsion')
    finite={}
    for p in [5,17]:
        need(p not in [2,3,7],'Unvalidated good-reduction prime')
        pts=finite_hesse(p)
        for v in pts:
            x,y,z=v
            need(any(a%p for a in (x*x-2*y*z,y*y-2*x*z,z*z-2*x*y)),'Singular reduction')
        finite[str(p)]=[list(v) for v in pts]
    need([len(finite[str(p)]) for p in [5,17]]==[9,21],'Good reduction point counts')
    return {'tensor':MOORE,'determinant':'-6*(x^3+y^3+z^3-6xyz)',
            'orbit':[{'slot':i%3,'point':list(v)} for i,v in enumerate(orbit)],
            'good_reduction_projective_points':finite,
            'torsion_order_bound':3,
            'infinite_order_proof_inputs':'Bhargava--Ho translation theorem; prime-to-reduction torsion injection; H^3(O) != O. Finite orbit alone is not the proof.'}


def check_face_gluing():
    # e_i=(1,0,0) and ell_i = first coordinate. The general proof is in the note.
    matrices=[]
    for i,j,k in product(range(3),repeat=3):
        T=tzero();T[i][j][k]=1
        faces=[slice_matrix(T,ax,(1,0,0)) for ax in range(3)]
        matrices.append(flat(faces))
    _,piv=rref(mt(matrices))
    # mt is dimension-independent transpose despite its matrix name.
    need(len(piv)==19,'Face restriction rank')
    hidden=[(i,j,k) for i,j,k in product(range(1,3),repeat=3)]
    for ix in hidden:
        T=tzero();T[ix[0]][ix[1]][ix[2]]=1
        need(all(not any(flat([slice_matrix(T,ax,(1,0,0))])) for ax in range(3)),'Hidden basis visible')
    # Polynomial gluing of all 27 tensor basis vectors, evaluated on all basis triples.
    for loc in product(range(3),repeat=3):
        T=tzero();T[loc[0]][loc[1]][loc[2]]=1
        for i,j,k in product(range(3),repeat=3):
            a,b,c=(int(i==0),int(j==0),int(k==0))
            val=(a*T[0][j][k]+b*T[i][0][k]+c*T[i][j][0]
                 -a*b*T[0][0][k]-a*c*T[0][j][0]-b*c*T[i][0][0]+a*b*c*T[0][0][0])
            expected=T[i][j][k] if 0 in (i,j,k) else 0
            need(val==expected,'Inclusion-exclusion gluing polynomial')
    return {'restriction_rank':19,'complete_fibre_dimension':8,'hidden_basis_indices_zero_based':hidden,
            'basis_gluing_cells_checked':27**2,'scope':'Three marked contractions, not the full set of nine coordinate slices.'}


def cd_basis_table(n):
    """Cayley--Dickson: (a,b)(c,d)=(ac-dbar*b, d*a+b*cbar)."""
    if n==0:return [[(0,1)]]
    old=cd_basis_table(n-1);m=2**(n-1);table=[]
    for i in range(2*m):
        row=[]
        for j in range(2*m):
            a=i%m;b=j%m
            if i<m and j<m:k,s=old[a][b]
            elif i<m and j>=m:
                k,s=old[b][a];k+=m
            elif i>=m and j<m:
                k,s=old[a][b];s*=1 if b==0 else -1;k+=m
            else:
                k,s=old[b][a];s*=-(1 if b==0 else -1)
            row.append((k,s))
        table.append(row)
    return table

def tagged_mult(a,b,table):
    out=[F(0)]*32
    for i,x in enumerate(a):
        if not x:continue
        for j,y in enumerate(b):
            if not y:continue
            k,s=table[i%16][j%16];k+=16*((i//16)^(j//16));out[k]+=x*y*s
    return out

def vecadd(a,b):return [x+y for x,y in zip(a,b)]
def vecscale(t,a):return [t*x for x in a]
def standard(n,i):return [F(int(i==j)) for j in range(n)]

def check_associator():
    def spin(a,b):
        return [a[0]*b[0]-a[1]*b[1]-a[2]*b[2],a[0]*b[1]+a[1]*b[0],a[0]*b[2]+a[2]*b[0]]
    def asso(a,b,c):return [x-y for x,y in zip(spin(spin(a,b),c),spin(a,spin(b,c)))]
    nz=[]
    for i,j,k in product(range(3),repeat=3):
        v=asso(basis3(i),basis3(j),basis3(k))
        if any(v):nz.append({'inputs':[i,j,k],'output':v})
    need(len(nz)==4,'Blade associator nonzero cell count')
    need(asso([0,1,0],[0,1,0],[0,0,1])==[0,0,-1],'Ternary blade recovery')
    # Formal spin associator, with all scalar/vector inputs retained.
    z=[P.var(9,i) for i in range(9)];a,b,c=z[:3],z[3:6],z[6:]
    target=[0]+[-(a[1]*b[1]+a[2]*b[2])*c[i]+(b[1]*c[1]+b[2]*c[2])*a[i] for i in [1,2]]
    need(asso(a,b,c)==target,'General associator polynomial')
    # Reconstruct the original tagged 32-dimensional source seeds from blades.
    tab=cd_basis_table(4)
    def mul(a,b):return tagged_mult(a,b,tab)
    def blade(indices):
        out=standard(32,0)
        for i in indices:out=mul(out,standard(32,2**(i-1)))
        return out
    def tag(v):return v[16:]+v[:16]
    X=vecadd(blade([1]),vecscale(-1,tag(blade([1,2,3,4]))))
    Y=vecadd(blade([2]),tag(blade([3,4])))
    need(mul(X,Y)==[0]*32 and mul(Y,X)==[0]*32,'Source seed zero products')
    need(mul(X,X)==vecscale(-2,standard(32,0)),'X squared')
    need(mul(Y,Y)==vecscale(-2,standard(32,0)),'Y squared')
    recovery=[]
    for label,a in [('X',X),('Y',Y)]:
        cols=[mul(a,standard(32,i)) for i in range(32)];L=mt(cols)
        Rcols=[]
        for i in range(32):
            b=standard(32,i)
            ass=vecadd(mul(mul(a,a),b),vecscale(-1,mul(a,mul(a,b))))
            Rcols.append(vecscale(F(-1,2),ass))
        R=mt(Rcols)
        fixed=[[R[i][j]-int(i==j) for j in range(32)] for i in range(32)]
        null=nullspace(L);fix=nullspace(fixed)
        for v in null:need([dot(r,v) for r in fixed]==[0]*32,'Ann not fixed')
        for v in fix:need([dot(r,v) for r in L]==[0]*32,'Fixed not Ann')
        recovery.append({'seed':label,'annihilator_dimension':len(null),'fixed_dimension':len(fix),
                         'annihilator_basis':[[frac(x) for x in v] for v in null]})
    return {'blade_nonzero_associator_cells':nz,'source_seed_X':[frac(v) for v in X],
            'source_seed_Y':[frac(v) for v in Y],'tagged_recovery':recovery,
            'scope':'Full seed linear-algebra check in 32 dimensions; no inference from contracted spectra.'}


def zorn_mul(x,y):
    al,u,v,be=x;ga,w,r,de=y
    return (al*ga+dot(u,r),[al*w[i]+de*u[i]-cross(v,r)[i] for i in range(3)],
            [ga*v[i]+be*r[i]+cross(u,w)[i] for i in range(3)],dot(v,w)+be*de)
def zorn_norm(x):a,u,v,b=x;return a*b-dot(u,v)
def zorn_trace(x):return x[0]+x[3]

def phi(X):
    # Forward cycle (A,B,C) corresponds to standard first Tits (A,C,B).
    A,B,C=X
    diag=[A[i][i] for i in range(3)]
    pairs=[(1,2),(2,0),(0,1)]
    xs=[(A[i][j],[B[k][r] for k in range(3)],[-C[r][k] for k in range(3)],A[j][i])
        for r,(i,j) in enumerate(pairs)]
    return diag,xs

def phi_inverse(diag,xs):
    A,B,C=zero3(),zero3(),zero3()
    for i in range(3):A[i][i]=diag[i]
    for r,(i,j) in enumerate([(1,2),(2,0),(0,1)]):
        a,u,v,b=xs[r];A[i][j]=a;A[j][i]=b
        for k in range(3):B[k][r]=u[k];C[r][k]=-v[k]
    return [A,B,C]

def jordan_zorn_norm(Y):
    (a,b,c),(x,y,z)=Y
    return a*b*c-a*zorn_norm(x)-b*zorn_norm(y)-c*zorn_norm(z)+zorn_trace(zorn_mul(zorn_mul(x,y),z))


def check_graded_moves():
    n=28;variables=[P.var(n,i) for i in range(27)];t=P.var(n,27);X=unflat(variables)
    uvw=[basis3(0)]*3;DX=Du(X,uvw)
    need(all(v==0 for v in flat(Du(DX,uvw))),'Square-zero generator polynomial')
    Xnew=[madd(A,smul(t,B)) for A,B in zip(X,DX)]
    N=norm(X)
    need(norm(Xnew)==N,'Full polynomial norm preservation')
    Y=phi(X)
    need(phi_inverse(*Y)==X,'27-cell Tits/Zorn inverse')
    need(jordan_zorn_norm(Y)==N,'Tits/Zorn cubic identity')
    # Check all 27 basis tensor generators against all 27 state basis vectors.
    for i,j,k in product(range(3),repeat=3):
        abc=[basis3(i),basis3(j),basis3(k)]
        for m in range(27):
            v=unflat([int(h==m) for h in range(27)])
            need(flat(Du(Du(v,abc),abc))==[0]*27,'Basis nilpotence')
    # Read every tensor coefficient back from the full operator, with its typed slots.
    coef=[P.var(27,h) for h in range(27)]
    for i,j,k in product(range(3),repeat=3):
        m=(i+1)%3;nn=(i+2)%3
        sign=cross(basis3(i),basis3(m))[nn]
        Xc=[zero3(),zero3(),emat(m,k)]
        entry=0
        for ii,jj,kk in product(range(3),repeat=3):
            z=Du(Xc,[basis3(ii),basis3(jj),basis3(kk)])[0][j][nn]
            if z:entry=entry+coef[9*ii+3*jj+kk]*z
        need(sign*entry==coef[9*i+3*j+k],'Tensor/operator coefficient inverse')
    # Exact spectrum-changing example, polynomial in t.
    A=[[2,0,0],[0,3,0],[0,0,5]];B=zero3();C=emat(2,0)
    tt=P.var(1,0);D=Du([A,B,C],[basis3(1),basis3(0),basis3(0)])
    V=[madd(Z,smul(tt,W)) for Z,W in zip([A,B,C],D)]
    need(norm(V)==30,'Moving example norm')
    need(quadratic_trace(V)==31+5*tt,'Moving example quadratic trace')
    need(tr(V[0])==10+tt,'Moving example trace')
    return {'norm_monomials':len(N.d),'norm_polynomial_zero_verified':True,
            'zorn_norm_polynomial_zero_verified':True,'basis_nilpotence_cases':27**2,'operator_coefficient_inverses':27,
            'example':{'initial':[A,B,C],'derivative':D,'norm':30,'quadratic_trace':'31+5t','trace':'10+t'},
            'interpretation':'Integral invertible norm-preserving moves, not Jordan automorphisms fixing the unit; no positive-integral spectral return assumed.'}


def check_es():
    n=4;vv=[P.var(n,i) for i in range(4)];p=vv[0];d=vv[1:];T=tzero()
    for i,j,k in product(range(3),repeat=3):T[i][j][k]=12*d[i]*int(i==j==k)-p
    E=4*d[0]*d[1]*d[2]-p*(d[0]*d[1]+d[1]*d[2]+d[0]*d[2])
    for ax in range(3):need(det(slice_matrix(T,ax,(1,1,1)))==432*E,'Marked ES cube identity')
    states=[{'p':1201,'R':23,'h':17,'r':1,'s':18,'u':17,'channel':'E','quotient':53},
            {'p':1201,'R':31,'h':2,'r':1,'s':154,'u':2,'channel':'M','quotient':5},
            {'p':1201,'R':39,'h':2,'r':1,'s':155,'u':2,'channel':'M','quotient':4},
            {'p':2521,'R':31,'h':11,'r':2,'s':29,'u':44,'channel':'M','quotient':1}]
    for st in states:
        pp,R,h,r,s,q=[st[key] for key in ['p','R','h','r','s','quotient']]
        a=h*r*s
        ds=[a,h*s*q,pp*h*r*q] if st['channel']=='E' else [a,pp*h*s*q,pp*h*r*q]
        need(R==4*a-pp and 0<R<pp and st['u']==h*r*r,'Shell reconstruction')
        need(sum((F(1,x) for x in ds),F(0))==F(4,pp),'ES reciprocal check')
        tensor=[[[12*ds[i]*int(i==j==k)-pp for k in range(3)] for j in range(3)] for i in range(3)]
        pp2=-tensor[0][0][1];ds2=[(tensor[i][i][i]+pp2)//12 for i in range(3)]
        need((pp2,ds2)==(pp,ds),'Cube inverse')
        invu=F(a*a,R*ds[1]-pp*a)*(pp if st['channel']=='M' else 1)
        need(invu==st['u'],'Marked divisor inverse')
        dg=gcd(a,int(invu));rr=int(invu)//dg;ss=a//dg;hh=dg//rr
        need([hh,rr,ss]==[h,r,s],'Marked normalized inverse')
        reciprocal=primitive([F(1,x) for x in ds]);A,B,C=reciprocal;S=A+B+C;L=lcm(A,B,C)
        need(4*L%gcd(4*L,S)==0,'Definition integrality')
        p0=4*L//gcd(4*L,S)
        need(p0==pp,'Primitive reciprocal prime return')
        faces=[slice_matrix(tensor,ax,(1,1,1)) for ax in range(3)]
        for M in faces:
            need(kernel_rank_two(M)==reciprocal,'Cube kernel retains reciprocal ratio')
        st.update(denominators=ds,cube=tensor,primitive_reciprocal=list(reciprocal),
                  reciprocal_sum=S,reciprocal_lcm=L,prime_return=p0)
    # Homogeneous reciprocal/Cremona identity on four formal variables.
    v=[P.var(4,i) for i in range(4)]
    bs=[reduce(lambda a,b:a*b,(v[j] for j in range(4) if j!=i),1) for i in range(4)]
    aa=[reduce(lambda a,b:a*b,(bs[j] for j in range(4) if j!=i),1) for i in range(4)]
    prodv=reduce(lambda a,b:a*b,v,1)
    need(all(aa[i]==prodv**2*v[i] for i in range(4)),'Cremona inverse polynomial')
    vv=[-p,4*d[0],4*d[1],4*d[2]]
    e3=sum(reduce(lambda a,b:a*b,(vv[j] for j in range(4) if j!=i),1) for i in range(4))
    need(e3==16*E,'Cayley cubic ES identity')
    return {'marked_cube_det_factor':432,'cayley_det_factor':16,'witnesses':states,
            'new_coverage_claim':False,'exceptional_loci':'Cremona excludes coordinate hyperplanes; cube nondegeneracy is not required for ES identity; positive denominators imply rank two at an ES face.'}



def invert3(A):
    d=det(A);need(d!=0,'Singular change of basis')
    return [[F(x,d) for x in r] for r in adj(A)]

def rank_normalize(A):
    """Return U,V with U*A*V=diag(1,1,0) for a rank-two rational A."""
    M=[[F(x) for x in r] for r in A];U=[[F(x) for x in r] for r in eye3()];V=[[F(x) for x in r] for r in eye3()]
    rank=0
    for k in range(3):
        piv=next(((i,j) for i in range(k,3) for j in range(k,3) if M[i][j]),None)
        if piv is None:break
        i,j=piv
        M[k],M[i]=M[i],M[k];U[k],U[i]=U[i],U[k]
        for Z in [M,V]:
            for r in Z:r[k],r[j]=r[j],r[k]
        c=M[k][k];M[k]=[x/c for x in M[k]];U[k]=[x/c for x in U[k]]
        for i in range(3):
            if i==k:continue
            c=M[i][k];M[i]=[x-c*y for x,y in zip(M[i],M[k])];U[i]=[x-c*y for x,y in zip(U[i],U[k])]
        for j in range(3):
            if j==k:continue
            c=M[k][j]
            for Z in [M,V]:
                for r in Z:r[j]-=c*r[k]
        rank+=1
    need(rank==2,'Rank-two attachment requires a passing ES face')
    J=[[int(i==j and i<2) for j in range(3)] for i in range(3)]
    need(M==J and mm(U,mm(A,V))==J,'Rank-normalization certificate')
    return U,V

def cube_pullback(T,gs):
    return [[[evaluate(T,[gs[0][i][a] for i in range(3)],
                        [gs[1][j][b] for j in range(3)],
                        [gs[2][k][c] for k in range(3)])
              for c in range(3)] for b in range(3)] for a in range(3)]

def encode_rational(v):
    if isinstance(v,(list,tuple)):return [encode_rational(x) for x in v]
    return frac(v)

def check_marked_attachment():
    p=1201;ds=[306,16218,1082101]
    M=[[12*ds[i]*int(i==j)-3*p for j in range(3)] for i in range(3)]
    A=slice_matrix(MOORE,0,(1,-1,0))
    UA,VA=rank_normalize(A);UB,VB=rank_normalize(M)
    L=mm(invert3(UB),UA);R=mm(VA,invert3(VB))
    need(mm(L,mm(A,R))==M,'ES face attachment')
    g0=[[1,0,0],[-2,1,0],[-1,0,1]];gs=[g0,mt(L),R]
    need(mv(g0,(1,1,1))==[1,-1,0],'Marked point coordinate')
    cube=cube_pullback(MOORE,gs)
    scale=lcm(*(F(v).denominator for v in flat(cube)))
    integer_cube=[[[int(scale*v) for v in r] for r in A] for A in cube]
    need(slice_matrix(integer_cube,0,(1,1,1))==smul(scale,M),'Scaled marked face')
    back=cube_pullback(cube,[invert3(g) for g in gs])
    need(back==MOORE,'27-cell marked attachment inverse')
    v=(1,1,1);orb=[v]
    for i in range(3):v=cube_step(integer_cube,i,v,(i+1)%3);orb.append(v)
    need(orb[1]==primitive([F(1,x) for x in ds]),'First slice returns exact reciprocal triple')
    need(orb[-1]==(1817,8909,5075),'Infinite return conjugation')
    return {'p':p,'ordered_denominators':ds,'slot_basis_maps':encode_rational(gs),
            'integer_scale':scale,'integer_cube':integer_cube,'first_turn_orbit':orb,
            'status':'Explicit marked rational equivalence, integral after retaining scale. It encodes an existing ES witness and imports infinite holonomy; it does not produce witnesses for unknown primes.'}


class G:
    """Exact Gaussian rational, for the division-octonion real form."""
    def __init__(self,a=0,b=0):self.a,self.b=F(a),F(b)
    def coerce(self,x):return x if isinstance(x,G) else G(x)
    def __add__(self,x):x=self.coerce(x);return G(self.a+x.a,self.b+x.b)
    __radd__=__add__
    def __neg__(self):return G(-self.a,-self.b)
    def __sub__(self,x):return self+-self.coerce(x)
    def __rsub__(self,x):return self.coerce(x)+-self
    def __mul__(self,x):x=self.coerce(x);return G(self.a*x.a-self.b*x.b,self.a*x.b+self.b*x.a)
    __rmul__=__mul__
    def __eq__(self,x):x=self.coerce(x);return self.a==x.a and self.b==x.b
    def __bool__(self):return bool(self.a or self.b)
    def conjugate(self):return G(self.a,-self.b)
    def record(self):return [frac(self.a),frac(self.b)]

def zscale(t,z):
    a,u,v,b=z;return (t*a,[t*x for x in u],[t*x for x in v],t*b)

def zsum(zs):
    return (sum(z[0] for z in zs),[sum(z[1][i] for z in zs) for i in range(3)],
            [sum(z[2][i] for z in zs) for i in range(3)],sum(z[3] for z in zs))

def check_wilson_zorn():
    # Wilson basis 1,i0,...,i6; Zorn compact imaginary basis I,U1..U3,V1..V3.
    ii=G(0,1);one=(1,[0]*3,[0]*3,1);I=(ii,[0]*3,[0]*3,-ii)
    U=[(0,basis3(j),[-x for x in basis3(j)],0) for j in range(3)]
    V=[(0,[ii*x for x in basis3(j)],[ii*x for x in basis3(j)],0) for j in range(3)]
    images=[one,U[0],U[1],I,zscale(-1,U[2]),zscale(-1,V[1]),zscale(-1,V[2]),zscale(-1,V[0])]
    W=[[None]*8 for _ in range(8)]
    for i in range(8):W[0][i]=W[i][0]=(i,1)
    for i in range(1,8):W[i][i]=(0,-1)
    for t in range(7):
        a,b,c=[1+x%7 for x in [t,t+1,t+3]]
        for i,j,k in [(a,b,c),(b,c,a),(c,a,b)]:W[i][j]=(k,1);W[j][i]=(k,-1)
    for i,j in product(range(8),repeat=2):
        k,sg=W[i][j]
        need(zorn_mul(images[i],images[j])==zscale(sg,images[k]),'Wilson/Zorn multiplication mismatch')
    for i,z in enumerate(images):
        need(zorn_norm(z)==1,'Compact norm on Wilson basis')
        a,u,v,b=z
        cc=lambda x:G().coerce(x).conjugate()
        fixed=(cc(b),[-cc(x) for x in v],[-cc(x) for x in u],cc(a))
        need(z==fixed,'Wilson basis does not lie in compact real form')
    # Linearly independent 8 vectors over R: compare coordinates (Re a,Im a,Re u,Im u).
    mat=[]
    for a,u,v,b in images:
        a=G().coerce(a);us=[G().coerce(x) for x in u]
        mat.append([a.a,a.b]+[x.a for x in us]+[x.b for x in us])
    need(len(rref(mat)[1])==8,'Wilson/Zorn real inverse')
    return {'basis_order':'1,i0,i1,i2,i3,i4,i5,i6',
            'basis_images':'1,U1,U2,I,-U3,-V2,-V3,-V1',
            'I':'(i,0,0,-i)','Uj':'(0,e_j,-e_j,0)','Vj':'(0,i e_j,i e_j,0)',
            'multiplication_cells_verified':64,'real_rank':8,
            'compact_reality_verified':True,
            'inverse':'Read Re(alpha), Im(alpha), Re(u_j), Im(u_j) and invert the displayed signed permutation. For three octonions compose with phi_inverse, retaining zero diagonal.'}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out',type=Path,help='Write a JSON certificate as well as printing it.')
    args=ap.parse_args()
    report={'format':'three-slot-continuation-certificate/1',
            'face_gluing':check_face_gluing(),
            'associator':check_associator(),
            'moore_cube':check_moore(),
            'graded_moves':check_graded_moves(),
            'wilson_zorn_bridge':check_wilson_zorn(),
            'erdos_straus':check_es(),
            'marked_cube_attachment':check_marked_attachment(),
            'scope':{'mathematical_proof':'See note.tex; finite calculations and formal polynomial identities distinguished.',
                     'external_inputs':['Bhargava--Ho, arXiv:1306.4424v1, sections 3.2.3 and 5.1.1',
                                        'Prime-to-good-reduction torsion injectivity for elliptic curves',
                                        'Classical first Tits/Albert construction, explicit Zorn comparison'],
                     'not_claimed':['Universal ES coverage','Schanuel conjecture','Novelty or historical priority','Complete audit of uploaded archive','Lean compilation']}}
    text=json.dumps(report,ensure_ascii=False,sort_keys=True,indent=2)+'\n'
    if args.out:
        args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(text,encoding='utf-8')
    print(text,end='')

if __name__=='__main__':main()
