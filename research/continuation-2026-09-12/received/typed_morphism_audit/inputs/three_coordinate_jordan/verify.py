#!/usr/bin/env python3
"""Exact certificates for three-coordinate Jordan products and marked twist maps.

Python 3.9+, standard library only. Normal and -O runs are identical.
Polynomial checks are formal identities, not sampled substitution. Finite and
basis-check scopes are stated in the JSON output. No global ES assertion.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import argparse
import hashlib
import json


def need(condition, message):
    if not condition:
        raise ArithmeticError(message)

# Sparse rational polynomials in (t, x, y, gamma).
NVAR = 4
ZERO_EXP = (0,) * NVAR
class P:
    def __init__(self, terms=None):
        if isinstance(terms, (int, F)):
            terms = {ZERO_EXP: F(terms)}
        self.terms = {e: F(c) for e, c in (terms or {}).items() if c}
    def __add__(self, other):
        other = other if isinstance(other, P) else P(other)
        r = dict(self.terms)
        for e, c in other.terms.items():
            r[e] = r.get(e, F(0)) + c
        return P(r)
    __radd__ = __add__
    def __neg__(self):
        return P({e: -c for e, c in self.terms.items()})
    def __sub__(self, other):
        return self + -(other if isinstance(other, P) else P(other))
    def __rsub__(self, other):
        return (other if isinstance(other, P) else P(other)) + -self
    def __mul__(self, other):
        other = other if isinstance(other, P) else P(other)
        r = {}
        for e, a in self.terms.items():
            for f, b in other.terms.items():
                ef = tuple(i+j for i,j in zip(e,f))
                r[ef] = r.get(ef,F(0)) + a*b
        return P(r)
    __rmul__ = __mul__
    def __pow__(self, n):
        if not isinstance(n,int) or n<0:
            raise ValueError('Polynomial power must be a nonnegative integer')
        out = P(1)
        for _ in range(n): out = out*self
        return out
    def __eq__(self, other):
        other = other if isinstance(other,P) else P(other)
        return self.terms == other.terms
    def records(self):
        return [{'powers':list(e),'coefficient':str(c)} for e,c in sorted(self.terms.items())]


def mm(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))),0)
             for j in range(len(b[0]))] for i in range(len(a))]

def madd(a,b):
    return [[u+v for u,v in zip(ar,br)] for ar,br in zip(a,b)]
def mscale(s,a):
    return [[s*u for u in row] for row in a]
def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
           -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
           +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))
def left(t,x,y,g):
    return [[t,2*x,2*y],[x,t+g*x,-g*y],[y,-g*y,t-g*x]]

def symbolic_checks():
    vs=[P({tuple(int(i==j) for i in range(4)):1}) for j in range(4)]
    t,x,y,g=vs
    L=left(t,x,y,g)
    sq=[t*t+2*(x*x+y*y),2*t*x+g*(x*x-y*y),2*t*y-2*g*x*y]
    Lsq=left(*sq,g)
    comm=madd(mm(L,Lsq),mscale(-1,mm(Lsq,L)))
    factor=2*g*(g*g-1)*y*(3*x*x-y*y)
    expected=[[P(0),P(0),P(0)],[P(0),P(0),factor],[P(0),-factor,P(0)]]
    need(comm==expected,'Jordan commutator polynomial')
    L0=left(t,x,y,P(0))
    sq0=[t*t+2*(x*x+y*y),2*t*x,2*t*y]
    U=madd(mscale(2,mm(L0,L0)),mscale(-1,left(*sq0,P(0))))
    D=t*t-2*(x*x+y*y)
    need(det3(U)==D**3,'Quadratic representation determinant')
    need(det3(left(t,x,y,P(1)))==t**3-3*t*(x*x+y*y)+2*(x**3-3*x*y*y),
         'Cubic left-multiplication determinant')
    return {'kind':'formal sparse polynomial identities',
            'variables':['t','x','y','gamma'],
            'commutator_entries_checked':9,
            'nonzero_entry_polynomial':factor.records(),
            'quadratic_representation_determinant':'(t^2-2*x^2-2*y^2)^3',
            'cubic_left_multiplication_determinant_checked':True}

@dataclass(frozen=True)
class K:
    """a+b*omega, omega^2+omega+1=0, exact rational coefficients."""
    a:F=F(0)
    b:F=F(0)
    def __post_init__(self):
        object.__setattr__(self,'a',F(self.a)); object.__setattr__(self,'b',F(self.b))
    def __add__(self,w):
        w=w if isinstance(w,K) else K(w)
        return K(self.a+w.a,self.b+w.b)
    __radd__=__add__
    def __neg__(self):return K(-self.a,-self.b)
    def __sub__(self,w):return self+-(w if isinstance(w,K) else K(w))
    def __mul__(self,w):
        w=w if isinstance(w,K) else K(w)
        return K(self.a*w.a-self.b*w.b,
                 self.a*w.b+self.b*w.a-self.b*w.b)
    __rmul__=__mul__
    def __truediv__(self,s):return K(self.a/F(s),self.b/F(s))
    def bar(self):return K(self.a-self.b,-self.b)
    def real(self):return self.a-self.b/2
    def norm(self):return self.a*self.a-self.a*self.b+self.b*self.b
    def rational(self):
        need(self.b==0,'Expected rational Eisenstein value')
        return self.a
W=K(0,1); W2=W*W

def encode(q):return (sum(q,F(0))/3,(K(q[0])+W*q[1]+W2*q[2])/3)
def decode(v):
    t,z=v
    return tuple((K(t)+eta.bar()*z+eta*z.bar()).rational() for eta in [K(1),W,W2])
def prod(v,w,g=F(1)):
    t,z=v; u,zz=w
    return (t*u+2*(z*zz.bar()).real(), t*zz+u*z+g*z.bar()*zz.bar())
def add(v,w):return (v[0]+w[0],v[1]+w[1])
def scale(c,v):return (F(c)*v[0],F(c)*v[1])
def cubic(v):
    t,z=v
    return t**3-3*t*z.norm()+2*(z*z*z).real()
def adj(v):
    t,z=v
    return (t*t-z.norm(), z.bar()*z.bar()-t*z)

def coordinate_checks():
    qs=[tuple(map(F,q)) for q in product(range(-2,3),repeat=3)]
    for q in qs:
        v=encode(q)
        need(decode(v)==q,'Fourier inverse')
        t,z=v
        delta=2*sum(q)**2-3*sum(a*a for a in q)
        need(delta==9*(t*t-2*z.norm()),'Koide quadratic coordinate')
        need(cubic(v)==q[0]*q[1]*q[2],'Cubic Fourier norm')
        need(decode(adj(v))==(q[1]*q[2],q[0]*q[2],q[0]*q[1]),'Cubic adjoint')
        need(prod(v,adj(v))==(cubic(v),K()),'Cubic inverse numerator')
        T=3*t; Z=3*z
        need(T.denominator==Z.a.denominator==Z.b.denominator==1,'Integer lattice')
        need((int(T)-int(Z.a)-int(Z.b))%3==0,'Mod-three marking')
    for q in qs:
        for r in qs:
            need(decode(prod(encode(q),encode(r)))==tuple(a*b for a,b in zip(q,r)),
                 'Transported multiplication')
    inv_count=0
    for t,a,b in product(range(-3,4),repeat=3):
        v=(F(t),K(a,b))
        D=t*t-2*v[1].norm()
        if v==(F(0),K()):
            need(D==0,'Zero quadratic norm')
            continue
        need(D!=0,'Unexpected rational isotropic vector')
        inverse=(F(t)/D,-v[1]/D)
        need(prod(v,inverse,0)==(F(1),K()),'Jordan inverse first equation')
        need(prod(prod(v,v,0),inverse,0)==v,'Jordan inverse second equation')
        inv_count+=1
    residues=[[a,b,(a*a-a*b+b*b)%2] for a,b in product(range(2),repeat=2)]
    need([r[:2] for r in residues if r[2]==0]==[[0,0]],'Anisotropy parity premise')
    return {'integer_triples':len(qs),'ordered_product_pairs':len(qs)**2,
            'rational_spin_inverse_examples':inv_count,
            'parity_table':residues,
            'infinite_anisotropy_proof':'Primitive-integer parity descent in note.tex, not a bounded search claim.'}

# Octonions via Cayley-Dickson: (a,b)(c,d)=(ac-conj(d)b, da+b conj(c)).
def conjugate(a):return (a[0],)+tuple(-v for v in a[1:])
def cd(a,b):
    if len(a)==1:return (a[0]*b[0],)
    k=len(a)//2; x,y=a[:k],a[k:]; u,v=b[:k],b[k:]
    xu=cd(x,u); vy=cd(conjugate(v),y)
    vx=cd(v,x); yu=cd(y,conjugate(u))
    return tuple(i-j for i,j in zip(xu,vy))+tuple(i+j for i,j in zip(vx,yu))
OZERO=(F(0),)*8
OBASIS=[tuple(F(i==j) for i in range(8)) for j in range(8)]
OTABLE={}
for _i,_a in enumerate(OBASIS):
    for _j,_b in enumerate(OBASIS):
        _r=cd(_a,_b); _nz=[(k,c) for k,c in enumerate(_r) if c]
        need(len(_nz)==1 and abs(_nz[0][1])==1,'Octonion basis table')
        OTABLE[_i,_j]=_nz[0]
def oadd(a,b):return tuple(x+y for x,y in zip(a,b))
def oscale(c,a):return tuple(c*x for x in a)
def omul(a,b):
    out=[F(0)]*8
    for i,x in enumerate(a):
        if not x:continue
        for j,y in enumerate(b):
            if not y:continue
            k,s=OTABLE[i,j];out[k]+=s*x*y
    return tuple(out)
def oj():return tuple(OZERO for _ in range(9))
def ei(i):
    a=list(oj());a[3*i+i]=OBASIS[0];return tuple(a)
def fij(i,j,u):
    need(i<j,'Use upper-triangular Peirce coordinate')
    a=list(oj());a[3*i+j]=u;a[3*j+i]=conjugate(u);return tuple(a)
def jadd(a,b):return tuple(oadd(x,y) for x,y in zip(a,b))
def jscale(c,a):return tuple(oscale(c,x) for x in a)
def jmul(a,b):
    out=[]
    for i in range(3):
        for j in range(3):
            s=OZERO
            for k in range(3):
                s=oadd(s,omul(a[3*i+k],b[3*k+j]))
                s=oadd(s,omul(b[3*i+k],a[3*k+j]))
            out.append(oscale(F(1,2),s))
    return tuple(out)

def real_action(g,a):
    # All g used here are signed permutation matrices.
    rows=[]
    for row in g:
        nz=[(i,x) for i,x in enumerate(row) if x]
        need(len(nz)==1 and abs(nz[0][1])==1,'Signed permutation action')
        rows.append(nz[0])
    return tuple(oscale(si*sj,a[3*i+j]) for i,si in rows for j,sj in rows)

def twist_checks():
    identity=((1,0,0),(0,1,0),(0,0,1))
    d12=((-1,0,0),(0,-1,0),(0,0,1))
    d23=((1,0,0),(0,-1,0),(0,0,-1))
    d31=((-1,0,0),(0,1,0),(0,0,-1))
    cyc=((0,0,1),(1,0,0),(0,1,0))
    def mult(a,b):return tuple(tuple(row) for row in mm(a,b))
    need(mult(d12,d23)==d31 and mult(mult(d12,d23),d31)==identity,'Klein-four law')
    need(mult(mult(cyc,d12),mult(cyc,cyc))==d23,'Cyclic action on twists')
    group={identity};queue=[identity]
    while queue:
        g=queue.pop()
        for h in [d12,cyc]:
            k=mult(g,h)
            if k not in group:group.add(k);queue.append(k)
    need(len(group)==12,'Tetrahedral group order')
    vertices=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
    records=[]
    for g in sorted(group):
        need(det3(g)==1,'Proper real rotation')
        permutation=[]
        for v in vertices:
            image=tuple(sum(g[i][j]*v[j] for j in range(3)) for i in range(3))
            need(image in vertices,'Preservation of tetrahedron')
            permutation.append(vertices.index(image))
        inversions=sum(permutation[i]>permutation[j] for i in range(4) for j in range(i+1,4))
        need(inversions%2==0,'Alternating action')
        records.append({'matrix':g,'permutation_of_four_vertices':permutation})
    need(len({tuple(r['permutation_of_four_vertices']) for r in records})==12,'Faithful A4 action')
    jb=[ei(i) for i in range(3)]+[fij(i,j,u) for i,j in [(0,1),(1,2),(0,2)] for u in OBASIS]
    for g in [d12,cyc]:
        for a in jb:
            for b in jb:
                need(real_action(g,jmul(a,b))==jmul(real_action(g,a),real_action(g,b)),
                     'Albert generator automorphism on basis products')
    for a in OBASIS:
        for b in OBASIS:
            need(jmul(fij(0,1,a),fij(1,2,b))==jscale(F(1,2),fij(0,2,omul(a,b))),
                 'Mixed Peirce multiplication')
    # Exact half-angle eigenvector identities at rational unit-circle samples.
    for k in range(-10,11):
        r=F(1-k*k,1+k*k);s=F(2*k,1+k*k)
        A=((r*r-s*s,2*r*s),(2*r*s,s*s-r*r))
        need(tuple(sum(A[i][j]*v for j,v in enumerate((r,s))) for i in range(2))==(r,s),
             'Half-angle eigenvector')
        need(mm(A,A)==[[1,0],[0,1]],'Involution on eigenline sample')
    return {'tetrahedral_elements':records,'group_order':12,
            'generator_automorphism_basis_pairs':2*27*27,
            'mixed_Peirce_basis_pairs':64,'half_angle_rational_samples':21,
            'topological_scope':'The continuous half-angle/Mobius proof is in note.tex; sample checks are not a topological proof.'}

def es_checks():
    states=[dict(p=1201,R=23,h=17,r=1,s=18,kappa=53,channel='E'),
            dict(p=2521,R=31,h=11,r=2,s=29,lam=1,channel='M')]
    output=[]
    for d in states:
        p,R,h,r,s=[d[k] for k in ['p','R','h','r','s']]
        a=h*r*s;u=h*r*r
        if d['channel']=='E':
            k=d['kappa'];den=(a,h*s*k,p*h*r*k)
            need(p*r+s==R*k and (4*u+1)%R==0,'Marked exterior congruence')
        else:
            k=d['lam'];den=(a,p*h*s*k,p*h*r*k)
            need(r+s==R*k and (u+a)%R==0,'Marked middle congruence')
        need(R==4*a-p and 0<R<p and a*a%u==0,'Shell and divisor marking')
        T=sum(den);S=sum(den[i]*den[j] for i in range(3) for j in range(i+1,3));N=den[0]*den[1]*den[2]
        need(4*N==p*S,'ES cubic identity')
        v=encode(tuple(map(F,den)))
        need(cubic(v)==N and 3*(v[0]**2-v[1].norm())==S,'Jordan ES invariants')
        need(sum(decode(scale(F(1,N),adj(v))))==F(4,p),'Inverse trace')
        need((4*den[0]-p)*(4*den[1]-p)*(4*den[2]-p)==p*p*(4*T-p),'Shifted determinant identity')
        output.append({**d,'a':a,'u':u,'ordered_denominators':den,
                       'T':T,'S':S,'N':N,
                       'Fourier_t':str(v[0]),'Fourier_z':[str(v[1].a),str(v[1].b)]})
    return output

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    receipt={'schema':'three-coordinate-jordan-checks/1','status':'pass',
             'symbolic':symbolic_checks(),'coordinates':coordinate_checks(),
             'twists':twist_checks(),'marked_ES_examples':es_checks(),
             'nonclaims':['No ES existence theorem or new numerical coverage bound.',
                          'No identification of the previously mentioned unidentified Mobius passage.',
                          'No global-holonomy classification or lossless integer-winding claim for the finite A4 image.',
                          'No novelty or whole-Albert-Jordan-identity verification claim.'],
             'verifier_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    data=json.dumps(receipt,indent=2,sort_keys=True)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(data,encoding='utf-8')
    print(data,end='')
if __name__=='__main__':main()
