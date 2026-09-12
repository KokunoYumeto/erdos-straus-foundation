#!/usr/bin/env python3
"""Four-by-three branches, full flags, clocks, traces, and a common resolvent.
Python >=3.9; standard library; explicit guards remain active with -O.
No network and no dependence on previous verifiers. See note.tex for proofs.
"""
from __future__ import annotations
import argparse, hashlib, itertools, json
from collections import Counter
from fractions import Fraction as F
from math import gcd, prod
from pathlib import Path

COUNTS=Counter()
def check(value, message, category='finite'):
    COUNTS[category]+=1
    if not value: raise ArithmeticError(message)
def dump(path, data):
    path.write_text(json.dumps(data,indent=2,sort_keys=True,default=lambda x:str(x))+'\n',encoding='utf8')

# Exact formal multivariate polynomials. No evaluation-based identity tests.
class Poly:
    def __init__(self,n,terms=None):
        self.n=n; self.t={e:F(c) for e,c in (terms or {}).items() if c}
    def coerce(self,x):
        return x if isinstance(x,Poly) else Poly(self.n,{(0,)*self.n:F(x)})
    def __add__(self,x):
        x=self.coerce(x); d=self.t.copy()
        for e,c in x.t.items():d[e]=d.get(e,F(0))+c
        return Poly(self.n,d)
    __radd__=__add__
    def __neg__(self):return Poly(self.n,{e:-c for e,c in self.t.items()})
    def __sub__(self,x):return self+-self.coerce(x)
    def __rsub__(self,x):return self.coerce(x)+-self
    def __mul__(self,x):
        x=self.coerce(x);d={}
        for a,c in self.t.items():
            for b,e in x.t.items():
                key=tuple(u+v for u,v in zip(a,b));d[key]=d.get(key,F(0))+c*e
        return Poly(self.n,d)
    __rmul__=__mul__
    def __truediv__(self,x):return self*F(1,x)
    def __pow__(self,n):
        o=self.coerce(1)
        for _ in range(n):o=o*self
        return o
    def __eq__(self,x):return self.t==self.coerce(x).t
    def diff(self,k):
        d={}
        for a,c in self.t.items():
            if a[k]:
                e=list(a);e[k]-=1;d[tuple(e)]=c*a[k]
        return Poly(self.n,d)

def variables(n):return [Poly(n,{tuple(int(i==j) for j in range(n)):1}) for i in range(n)]
def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
           -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
           +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))
def elementary(a,k):return sum(prod(a[i] for i in inds) for inds in itertools.combinations(range(len(a)),k))
H4=((1,1,1,1),(1,1,-1,-1),(1,-1,1,-1),(1,-1,-1,1))
def had(a):return tuple(sum(r[i]*a[i] for i in range(4)) for r in H4)
def unhad(b):return tuple(F(sum(r[i]*b[i] for i in range(4)),4) for r in H4)
def resolvent(a):
    return (a[0]*a[1]+a[2]*a[3],a[0]*a[2]+a[1]*a[3],a[0]*a[3]+a[1]*a[2])
def fable(u,v,w):
    h=1+u*v
    return (h**3*w+v*v*h*(4+3*u*v),
            v+3*u*h*h*w+3*u*v*v*(4+3*u*v),
            2*u-3*u*u*v-u**3*w)

def formal_checks():
    a=variables(4);s,X,Y,Z=had(a);e2=elementary(a,2);e3=elementary(a,3);e4=prod(a);rs=resolvent(a)
    for i in range(4):
        check(sum(H4[i][j]*had(a)[j] for j in range(4))/4==a[i],'Hadamard inverse','polynomial')
    for x,r in zip((X,Y,Z),rs):check(x*x==s*s-4*e2+4*r,'resolvent square','polynomial')
    check(X*Y*Z==s**3-4*s*e2+8*e3,'signed triple product','polynomial')
    check(sum(rs)==e2,'resolvent sum','polynomial')
    check(elementary(rs,2)==s*e3-4*e4,'resolvent pair sum','polynomial')
    check(prod(rs)==e3*e3+s*s*e4-4*e2*e4,'resolvent product','polynomial')
    check(det3([[s,X,Y],[X,s,Z],[Y,Z,s]])==16*e3,'Cayley symmetroid','polynomial')
    p,x,y,z=variables(4);b=(-p,4*x,4*y,4*z);s,X,Y,Z=had(b)
    check(det3([[s,X,Y],[X,s,Z],[Y,Z,s]])==256*(4*x*y*z-p*(x*y+x*z+y*z)),
          'ES symmetroid factor 256','polynomial')
    u,v,w=variables(3);ff=fable(u,v,w)
    check(det3([[f.diff(i) for i in range(3)] for f in ff])==-2,'Fable Jacobian','polynomial')

Q=23; INF=23; ID=(1,0,0,1)
C=(12,5,1,12);J=(1,7,3,22);T=(4,11,16,4);D=(3,2,18,20)
def mm(a,b):
    x,y,z,w=a;v,r,s,t=b
    return ((x*v+y*s)%Q,(x*r+y*t)%Q,(z*v+w*s)%Q,(z*r+w*t)%Q)
def canon(a):return min(a,tuple(-x%Q for x in a))
def inv(a):a,b,c,d=a;return (d,-b%Q,-c%Q,a)
def pw(a,n):
    b=ID
    for _ in range(n):b=mm(b,a)
    return b
def point(a,x):
    a,b,c,d=a;n,m=(a,c) if x==INF else ((a*x+b)%Q,(c*x+d)%Q)
    return INF if m==0 else n*pow(m,-1,Q)%Q
def perm(a):return tuple(point(a,i) for i in range(24))
def pmul(a,b):return canon(mm(a,b))
def closure(gens,projective=True):
    mul=pmul if projective else mm
    seen={ID};todo=[ID]
    while todo:
        h=todo.pop()
        for g in gens:
            k=mul(h,g)
            if k not in seen:seen.add(k);todo.append(k)
    return seen

def comp(a,b):return tuple(a[b[i]] for i in range(len(a)))
def ppw(a,n):
    o=tuple(range(len(a)))
    for _ in range(n):o=comp(o,a)
    return o
def sign(a):return (-1)**sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))
def move(x,g):
    out=[0]*len(x)
    for i,v in enumerate(x):out[g[i]]=v
    return tuple(out)
def cycle(g,base):
    out=[];x=base
    while x not in out:out.append(x);x=g[x]
    check(x==base,'cycle return')
    return out

def rank(rows):
    piv={}
    for r in rows:
        r=list(map(F,r))
        for j,b in sorted(piv.items()):
            if r[j]:
                t=r[j];r=[x-t*y for x,y in zip(r,b)]
        k=next((i for i,v in enumerate(r) if v),None)
        if k is not None:
            v=r[k];piv[k]=[x/v for x in r]
    return len(piv)
def binary_basis(rows):
    piv={}
    for r in rows:
        while r:
            k=r.bit_length()-1
            if k in piv:r^=piv[k]
            else:piv[k]=r;break
    return [piv[k] for k in sorted(piv,reverse=True)]
def words(bs):
    a=[0]
    for b in bs:a += [x^b for x in a]
    return sorted(a)
def pmask(x,g):return sum(1<<g[i] for i in range(24) if x>>i&1)
def member(x,code):
    if len(x)!=24 or any(not isinstance(a,int) for a in x):return False
    m=x[0]%2
    return (all(a%2==m for a in x) and sum(x)%8==4*m and
        sum(1<<i for i,a in enumerate(x) if ((a-m)//2)%2) in code)

UNITS=(1,5,7,11);SIGMA={1:1,5:7,7:11,11:5};TAU={1:1,5:5,7:11,11:7}
def sg(u,j):
    for _ in range(j%3):u=SIGMA[u]
    return u
def flag_mul(a,b):
    u,j,e=a;v,k,f=b
    return (u*sg(TAU[v] if e else v,j)%12,(j+(-1)**e*k)%3,(e+f)%2)
PAIRINGS=(frozenset((frozenset((0,1)),frozenset((2,3)))),
          frozenset((frozenset((0,2)),frozenset((1,3)))),
          frozenset((frozenset((0,3)),frozenset((1,2)))))
def matching_index(f):
    return PAIRINGS.index(frozenset(frozenset(f[i] for i in s) for s in PAIRINGS[0]))

BASIS_TRACE=(-3,1,-1,1,1,-1,-1,1,1,1,1,1,1,-1,1,1,1,1,-1,-1,-1,-1,1,1)
LIFTS9=(
(-1,-1,-1,1,3,-1,1,1,-1,-1,1,1,-1,-1,1,1,1,1,-1,-1,1,-1,1,1),
(-3,-1,-1,1,1,1,1,1,-1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,1,-1,1),
(-1,-1,-1,-1,1,-1,1,1,-1,1,1,3,-1,1,-1,1,1,1,-1,1,1,-1,-1,1),
(-2,-2,-2,0,2,0,0,0,2,0,-2,0,0,0,2,0,0,0,0,0,0,2,0,0),
(-2,0,-2,0,0,2,-2,0,0,0,0,2,0,0,0,0,2,0,2,0,0,0,-2,0),
(-2,-2,0,2,0,0,0,0,2,0,0,0,0,0,0,0,0,0,2,-2,2,-2,0,0),
(-2,-2,0,2,0,0,0,0,2,-2,0,2,0,0,2,0,0,-2,0,0,0,0,0,0),
(-2,-2,0,0,0,0,0,0,2,-2,-2,0,0,2,0,0,0,0,2,0,0,0,0,2),
(-2,0,0,0,0,0,0,2,0,0,-2,0,0,-2,2,0,0,0,2,0,2,-2,0,0))

# Previously certified signed Golay-to-Wilson dictionary; inverse is written below.
WILSON_PI=(0,1,3,4,8,23,7,16,10,22,15,18,12,21,19,20,2,13,5,11,6,14,17,9)
WILSON_EPS=(1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,-1,-1,-1,-1,1,1,-1,1)
def wilson(x):return tuple(F(WILSON_EPS[i]*x[WILSON_PI[i]],2) for i in range(24))
def unwilson(y):
    x=[F(0)]*24
    for i,v in enumerate(y):x[WILSON_PI[i]]=2*WILSON_EPS[i]*v
    return tuple(x)


def structural_checks(out):
    minus=tuple(-x%23 for x in ID)
    check(pw(D,2)==minus,'orientation SL lift square','group')
    check(mm(mm(D,C),inv(D))==inv(C),'orientation reverses C with exact sign','group')
    check(mm(mm(D,J),inv(D))==tuple(-x%23 for x in J),'orientation conjugates J to -J','group')
    check(pw(T,4)==C and pw(T,12)==minus and pw(T,24)==ID,'clock central return','group')
    gs={1:ID,5:J,7:mm(mm(C,J),inv(C)),11:mm(mm(pw(C,2),J),inv(pw(C,2)))}
    c4=(0,2,3,1);j4=(1,0,3,2);d4=(0,1,3,2);id4=tuple(range(4))
    gv={1:id4,5:j4,7:comp(comp(c4,j4),ppw(c4,2)),11:comp(comp(ppw(c4,2),j4),c4)}
    rows=[];lookup={};matrices={};fp={}
    for u,j,e in itertools.product(UNITS,range(3),range(2)):
        label=(u,j,e);A=mm(mm(gs[u],pw(C,j)),pw(D,e))
        flag=comp(comp(gv[u],ppw(c4,j)),ppw(d4,e));x=point(A,INF)
        check(matching_index(flag)==j,'phase is opposite-edge matching','flags')
        check(sign(flag)==(-1)**e,'orientation parity','flags')
        check((A[0]*A[3]-A[1]*A[2])%23==1,'determinant one','flags')
        rows.append({'label':label,'flag':flag,'coordinate':x,'SL_matrix':A,'phase':j})
        lookup[x]=label;matrices[label]=A;fp[label]=flag
    check(len(lookup)==24 and len(set(fp.values()))==24,'full regular flag bijection','flags')
    signs=[]
    for a,b in itertools.product(matrices,repeat=2):
        k=flag_mul(a,b)
        check(comp(fp[a],fp[b])==fp[k],'S4 normal-form multiplication','group')
        ab=mm(matrices[a],matrices[b]);base=matrices[k]
        eps=1 if ab==base else -1
        check(ab==base or ab==tuple(-x%23 for x in base),'retained central cocycle','group')
        signs.append(eps)
    H=closure([J,C]);N=closure([J,C,D]);G=closure([J,T]);clock={canon(pw(T,i)) for i in range(12)}
    check(len(H)==12 and len(N)==24 and len(closure([J,C,D],False))==48,'A4 S4 binary lift sizes','group')
    ambient={canon((a,b,c,d)) for a,b,c,d in itertools.product(range(23),repeat=4) if (a*d-b*c)%23==1}
    check(G==ambient and len(G)==6072,'full generated PSL2(23)','group')
    normalizer={g for g in G if all(canon(mm(mm(g,h),inv(g))) in H for h in (J,C))}
    check(normalizer==N,'exact A4 normalizer','group')
    check(clock&N=={canon(pw(C,j)) for j in range(3)},'clock / tetrahedron intersection','group')
    # Exact comparison with the earlier two-A4-orbit convention based at infinity and zero.
    for u,j in itertools.product(UNITS,range(3)):
        old=point(mm(gs[u],pw(C,j)),0)
        check(lookup[old]==(u*sg(11,j)%12,j,1),'old second-orbit label conversion','flags')
    tp,cp,jp,dp=map(perm,(T,C,J,D))
    cycles=[cycle(tp,INF),cycle(tp,1)]
    check([cycles[0][j] for j in (0,4,8)]==[INF,12,11],'three roots at clock positions','flags')
    transitions=[]
    stabilizer={g for g in G if point(g,INF)==INF}
    check(len(stabilizer)==253 and len(stabilizer&N)==1,'regular subgroup / point-stabilizer factorization','group')
    for gamma in G:
        label=lookup[point(gamma,INF)];representative=matrices[label]
        carry=mm(inv(representative),gamma)
        check(point(carry,INF)==INF and mm(representative,carry)==gamma,'all group elements have explicit unique frame factorization','group')
    carries={}
    for i in range(24):
        a=lookup[i];b=lookup[tp[i]]
        carry=mm(mm(inv(matrices[b]),T),matrices[a]);carries[a]=carry
        check(carry[2]==0 and mm(matrices[b],carry)==mm(T,matrices[a]),'exact SL clock stabilizer carry','group')
        transitions.append({'from':a,'to':b,'from_coordinate':i,'to_coordinate':tp[i],'retained_SL_stabilizer_carry':carry})
    for start in matrices:
        a=start;carry=ID
        for _ in range(12):
            carry=mm(carries[a],carry);a=lookup[point(T,point(matrices[a],INF))]
        check(a==start and carry==minus,'twelve-step carry retains central minus identity','group')
    crossing=Counter((lookup[i][2],lookup[tp[i]][2]) for i in range(24))
    check(crossing=={(0,0):6,(0,1):6,(1,0):6,(1,1):6},'clock mixes orientations six each way','flags')
    qr={r*r%23 for r in range(1,23)}
    bs=binary_basis([(1<<23)|sum(1<<((r+a)%23) for r in qr) for a in range(23)])
    code=set(words(bs))
    check(len(bs)==12 and Counter(x.bit_count() for x in code)=={0:1,8:759,12:2576,16:759,24:1},'Golay complete enumerator','code')
    for g in (cp,jp,tp,dp):
        for b in code:check(pmask(b,g) in code,'code invariance','code')
    blocks=[sorted(i for i,lab in lookup.items() if lab[1]==j) for j in range(3)]
    for bb in blocks:check(sum(1<<i for i in bb) in code,'matching phase is octad','code')
    # All readouts use column-vector convention: (g x)[g(i)] = x[i].
    readouts=[[F(int(ppw(tp,n)[i] in blocks[j]),4) for i in range(24)] for n in range(4) for j in range(3)]
    idx=(0,1,2,3,4,6,7,9,10);P9=[readouts[i] for i in idx]
    P9J=[[row[jp[i]] for i in range(24)] for row in P9]
    r9=rank(P9);r15=rank(P9+P9J)
    check((r9,r15)==(9,15),'time-readout ranks','trace')
    def trace(x):return tuple(F(sum(x[i] for i in b),4) for b in blocks)
    B=(BASIS_TRACE,move(BASIS_TRACE,cp),move(BASIS_TRACE,ppw(cp,2)))
    for i,b in enumerate(B):
        check(member(b,code),'three-trace section membership','trace')
        check(trace(b)==tuple(int(i==j) for j in range(3)),'three-trace section inverse','trace')
    for i,u in enumerate(LIFTS9):
        check(member(u,code),'P9 section membership','trace')
        check([sum(row[k]*u[k] for k in range(24)) for row in P9]==[int(j==i) for j in range(9)],'P9 complete right inverse','trace')
    witness=(8,-8,8,0,-8,0,-8,0,8)+(0,)*15
    check(member(witness,code),'invisible vector in lattice','trace')
    check(all(sum(row[i]*witness[i] for i in range(24))==0 for row in P9),'P9 witness vanishes','trace')
    jw=[sum(row[i]*witness[i] for i in range(24)) for row in P9J]
    check(jw==[0,0,0,-2,-2,2,0,0,2],'P9 witness after J','trace')
    octads={c for c in code if c.bit_count()==8};obase=sum(1<<i for i in blocks[0])
    orbit={obase};todo=[obase]
    while todo:
        b=todo.pop()
        for g in (jp,tp):
            d=pmask(b,g)
            if d not in orbit:orbit.add(d);todo.append(d)
    check(orbit==octads,'generated full octad orbit','trace')
    allrows=[[int(b>>i&1) for i in range(24)] for b in sorted(octads)]
    check(rank(allrows)==24,'full symmetry-complete rank','trace')
    for i,j in itertools.product(range(24),repeat=2):
        check(sum(row[i]*row[j] for row in allrows)==176*int(i==j)+77,'octad incidence gram','trace')
    for label,A in matrices.items():
        g=perm(A)
        phase_perm=[matching_index(comp(fp[label],ppw(c4,j))) for j in range(3)]
        for j,b in enumerate(blocks):check(sorted(g[i] for i in b)==blocks[phase_perm[j]],'S4 quotient action on trace blocks','trace')
    source_bytes=(Path(__file__).resolve().parent/'lineage/aligned_isometry.json').read_bytes()
    check(hashlib.sha256(source_bytes).hexdigest()=='cb454d2a94f1b57cdd4fa15774c58f2c92f0db62004873eadeb61aa3b4cd1d14','pinned predecessor coordinate source','transport')
    source=json.loads(source_bytes);source_pi=[];source_eps=[]
    for row in source['golay_to_wilson_numerator_matrix']:
        nz=[i for i,v in enumerate(row) if v]
        check(len(nz)==1,'source signed coordinate row','transport')
        source_pi.append(nz[0]);source_eps.append(F(row[nz[0]],source['denominator']))
    check(tuple(source_pi)==WILSON_PI and tuple(source_eps)==WILSON_EPS,'Wilson table matches actual inherited source','transport')
    check(set(WILSON_PI)==set(range(24)),'Wilson coordinate permutation','transport')
    for i in range(24):
        x=tuple(int(i==j) for j in range(24))
        check(unwilson(wilson(x))==x,'Wilson coordinate inverse on basis','transport')
    data={'matrices':{'C':C,'J':J,'T':T,'D':D},'infinity_serialization':23,
          'flags':rows,'clock_cycles':cycles,'clock_transitions':transitions,
          'old_second_orbit_to_new':'(u,j,1) -> (u*sigma^j(11),j,1)',
          'central_product_signs_row_major':signs,'central_product_label_order':list(matrices),
          'phase_octads':blocks,'code_basis':bs,'group_sizes':{'A4':12,'S4':24,'SL_lift':48,'generated_PSL':6072},
          'trace_ranks':[3,9,15,24],'P9_rows':P9,'nine_integral_section_columns':LIFTS9,
          'invisible_vector':witness,'image_after_J':jw,'Wilson_pi':WILSON_PI,'Wilson_signs':WILSON_EPS}
    dump(out/'flags_and_traces.json',data)
    return rows,blocks,code,B

# Homogeneous polynomials below are dense in descending U-degree.
def poly_mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out
def poly_power(a,n):
    o=[F(1)]
    for _ in range(n):o=poly_mul(o,a)
    return o
def poly_subst(a,M):
    # f(M*(U,V)); degree = len(a)-1.
    r,s,t,u=M;d=len(a)-1;out=[F(0)]*(d+1)
    for j,c in enumerate(a):
        q=poly_mul(poly_power([r,s],d-j),poly_power([t,u],j))
        out=[x+c*y for x,y in zip(out,q)]
    return out
def matmul(a,b):
    x,y,z,w=a;r,s,t,u=b
    return (x*r+y*t,x*s+y*u,z*r+w*t,z*s+w*u)
def adj(a):a,b,c,d=a;return(d,-b,-c,a)
def determinant(a):a,b,c,d=a;return a*d-b*c
def triple_map(t):
    a,b,c=t
    return (2*a*(b-c),a*(b+c)-2*b*c,2*(b-c),2*a-b-c)
def mobius(A,x):
    a,b,c,d=A;check(c*x+d!=0,'finite Möbius return','arithmetic');return (a*x+b)/(c*x+d)
def cubic(roots,lead):
    o=[F(lead)]
    for r in roots:o=poly_mul(o,[F(1),-r])
    return o
def resultant(L,Qd):
    a,b=L;c,d,e=Qd;return a*a*e-a*b*d+b*b*c

def arithmetic_checks(out,flags,blocks,code,B):
    states=[dict(p=5,R=3,channel='E',u=2,h=2,r=1,s=1,kappa=2,denominators=[2,4,20]),
       dict(p=1201,R=23,channel='E',u=17,h=17,r=1,s=18,kappa=53,denominators=[306,16218,1082101]),
       dict(p=2521,R=31,channel='M',u=44,h=11,r=2,s=29,lam=1,denominators=[638,804199,55462])]
    output=[]
    for state in states:
        p=state['p'];d=state['denominators'];a=tuple(map(F,(-p,*(4*t for t in d))))
        check(elementary(a,3)==0 and len(set(a))==4 and all(a),'Cayley arithmetic domain','arithmetic')
        hh=had(a);s=hh[0];e2=elementary(a,2);e4=prod(a);rv=resolvent(a)
        check(e2>0 and len(set(rv))==3,'common resolvent simple and normalized','arithmetic')
        common=cubic(rv,-1/e2)
        check(common==[-1/e2,F(1),4*e4/e2,e4*(s*s-4*e2)/e2],'Cayley common resolvent coefficients','arithmetic')
        rows=[];face_maps={}
        for rec in flags:
            f=rec['flag'];i,j,k,l=f
            t=tuple(-4*a[i]/a[q] for q in (j,k,l))
            mids=[matching_index((i,q,*[z for z in range(4) if z not in (i,q)])) for q in (j,k,l)]
            target=tuple(rv[z] for z in mids)
            source=cubic(t,F(-1,4));N=matmul(triple_map(target),adj(triple_map(t)))
            nd=determinant(N);check(nd!=0,'invertible face to resolvent','arithmetic')
            check(tuple(mobius(N,z) for z in t)==target,'all three typed roots transported','arithmetic')
            pulled=poly_subst(source,adj(N));kappa=pulled[0]/common[0]
            check(kappa!=0 and pulled==[kappa*q for q in common],'entire cubic transport with scale','arithmetic')
            # Canonical projective matrix is independent of companion order for a fixed face.
            first=next(z for z in N if z);nn=tuple(z/first for z in N)
            if i in face_maps:check(face_maps[i]==nn,'one map per face, not per ordering','arithmetic')
            else:face_maps[i]=nn
            r=t[0];der=-(r-t[1])*(r-t[2])/4
            L=[1/der,-r/der];QQ=poly_mul([1,-t[1]],[1,-t[2]]);QQ=[-der*q/4 for q in QQ]
            check(resultant(L,QQ)==1 and poly_mul(L,QQ)==source,'source normalized factor','arithmetic')
            AA=kappa/nd**2;BB=nd**2/kappa**2
            LL=[AA*x for x in poly_subst(L,adj(N))];QQQ=[BB*x for x in poly_subst(QQ,adj(N))]
            check(resultant(LL,QQQ)==1 and poly_mul(LL,QQQ)==common,'resultant-preserving common factor','arithmetic')
            r2=target[0];der2=3*common[0]*r2*r2+2*r2+common[2]
            src=(1/der2,-r2-der2,5*der2**2+3*r2*der2-2*common[0]*der2**3)
            check(fable(*src)==(common[3],2*common[2],2*common[0]),'common Fable coordinates','arithmetic')
            invN=adj(N);back=tuple(mobius(invN,z) for z in target)
            check(back==t,'Möbius all-root inverse','arithmetic')
            ar=[None]*4;ar[i]=a[i]
            for q,v in zip((j,k,l),back):ar[q]=-4*a[i]/v
            check(tuple(ar)==a,'scale and labels return full Cayley point','arithmetic')
            # Integral common-resolvent trace lift and all coordinates through Wilson/Albert.
            rvi=tuple(int(z) for z in target)
            check(tuple(map(F,rvi))==target,'integral resolvent trace','arithmetic')
            numer=tuple(sum(rvi[h]*B[h][q] for h in range(3)) for q in range(24))
            check(member(numer,code),'resolvent Leech lift','arithmetic')
            check(tuple(F(sum(numer[q] for q in bb),4) for bb in blocks)==target,'resolvent trace return','arithmetic')
            z=wilson(numer);backnum=unwilson(z)
            check(backnum==numer,'full off-diagonal Albert coordinate return','arithmetic')
            # Standard denominator lift uses the same integral section but remains a distinct state.
            denom_lift=tuple(sum(d[h]*B[h][q] for h in range(3)) for q in range(24))
            check(member(denom_lift,code),'denominator lift','arithmetic')
            ps=tuple(F(sum(denom_lift[q] for q in bb),4) for bb in blocks)
            check(ps==tuple(d),'ordered denominators recovered','arithmetic')
            u=F(d[0]**2,state['R']*d[1]-p*d[0])*(p if state['channel']=='M' else 1)
            check(u==state['u'],'retained channel divisor recovered','arithmetic')
            gg=gcd(d[0],int(u));r0=int(u)//gg;s0=d[0]//gg;h=F(gg,r0)
            check((h,r0,s0)==(state['h'],state['r'],state['s']),'primitive coordinates recovered','arithmetic')
            check(4*h*r0*s0-p==state['R'],'residual recovered','arithmetic')
            rows.append({'flag':f,'leech_coordinate_label':rec['coordinate'],'face_roots':t,
                         'matching_indices':mids,'common_roots_in_flag_order':target,'matrix':N,'matrix_determinant':nd,
                         'cubic_scale':kappa,'linear_scale':AA,'quadratic_scale':BB,
                         'normalized_L':LL,'normalized_Q':QQQ,'common_Fable_source':src,
                         'face_scale':a[i],'resolvent_trace_lift_numerator':numer})
        check(len(face_maps)==4,'four explicit common cubic gauges','arithmetic')
        check(len(set(tuple(q['common_Fable_source']) for q in rows))==3,'24 flags over three actual sources','arithmetic')
        output.append({'state':state,'raw_cayley':a,'Hadamard':hh,'resolvent_roots':rv,
                       'common_cubic':common,'four_face_maps':face_maps,'flag_routes':rows})
    dump(out/'common_resolvent_routes.json',output)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,default=Path('certificates'))
    args=parser.parse_args();args.out.mkdir(parents=True,exist_ok=True)
    formal_checks();flags,blocks,code,B=structural_checks(args.out)
    arithmetic_checks(args.out,flags,blocks,code,B)
    report={'checks':dict(sorted(COUNTS.items())),'total':sum(COUNTS.values()),'status':'passed',
            'scope':'exact polynomial identities, full 24-flag/group/code checks, exact ranks and 72 marked arithmetic routes; no ES existence theorem or Lean build',
            'verifier_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    dump(args.out/'checks.json',report);print(json.dumps(report,sort_keys=True))
if __name__=='__main__':main()
