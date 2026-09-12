#!/usr/bin/env python3
"""Independent cross-package checks. Python 3.10+, standard library only.
Reconstructs the code and typed coordinate maps; never executes downloaded code.
"""
from __future__ import annotations
import argparse,collections,hashlib,itertools,json,math
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent
COUNT=collections.Counter()
def check(c,label):
    COUNT[label]+=1
    if not c: raise ArithmeticError(label)
def js(x):
    if isinstance(x,Q):return str(x)
    if isinstance(x,dict):return {str(k):js(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [js(v) for v in x]
    return x
def dump(path,data):path.write_text(json.dumps(js(data),sort_keys=True,indent=2)+'\n',encoding='utf8')
P=23; C=(12,5,1,12); J=(1,7,3,22); T=(4,11,16,4)
BLOCKS=((0,1,3,4,7,8,16,23),(10,12,15,18,19,20,21,22),(2,5,6,9,11,13,14,17))
PI=(0,1,3,4,8,23,7,16,10,22,15,18,12,21,19,20,2,13,5,11,6,14,17,9)
SIG=(1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,-1,-1,-1,-1,1,1,-1,1)
B0=(-3,1,-1,1,1,-1,-1,1,1,1,1,1,1,-1,1,1,1,1,-1,-1,-1,-1,1,1)
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
OCTAD_BASIS_IDS=(197,555,724,671,582,487,580,464,333,59,49,397,55,427,249,304,329,72,195,630,672,16,180,402)
def mv(g):
    a,b,c,d=g; out=[]
    for x in range(24):
        n,m=(a,c) if x==23 else ((a*x+b)%23,(c*x+d)%23)
        out.append(23 if not m else n*pow(m,-1,23)%23)
    return tuple(out)
def act(x,g):
    y=[0]*24
    for i,j in enumerate(g):y[j]=x[i]
    return tuple(y)
def permul(g,h):return tuple(g[h[i]] for i in range(len(g)))
def mask(S):return sum(1<<i for i in S)
def pmask(b,g):return mask(g[i] for i in range(24) if b>>i&1)
def binary_basis(rows):
    b={}
    for v in rows:
        while v:
            i=v.bit_length()-1
            if i in b:v^=b[i]
            else:b[i]=v;break
    return tuple(b[i] for i in sorted(b,reverse=True))
def golay():
    qr={j*j%23 for j in range(1,23)}
    generators=[(1<<23)|mask((a+q)%23 for q in qr) for a in range(23)]
    b=binary_basis(generators);words=[0]
    for x in b:words += [w^x for w in words]
    return b,set(words)
def member(x,code):
    if len(x)!=24 or any(not isinstance(v,int) for v in x):return False
    m=x[0]%2
    return all(a%2==m for a in x) and sum(x)%8==4*m and mask(i for i,a in enumerate(x) if ((a-m)//2)%2) in code

def dot(x,y):return sum(a*b for a,b in zip(x,y))
def norm(x):return Q(dot(x,x),8)
def trace(x):
    vals=[sum(x[i] for i in b) for b in BLOCKS]
    if any(v%4 for v in vals):raise ArithmeticError('nonintegral trace')
    return tuple(v//4 for v in vals)
def combine(a,rows):return tuple(sum(c*r[i] for c,r in zip(a,rows)) for i in range(24))
def views(x):
    out=[];tp=mv(T)
    for _ in range(4):out.append(trace(x));x=act(x,tp)
    return tuple(out)
def trace9(x):
    v=views(x);return v[0]+v[1][:2]+v[2][:2]+v[3][:2]
def rank(A):
    a=[list(map(Q,row)) for row in A];r=0
    for k in range(len(a[0]) if a else 0):
        j=next((i for i in range(r,len(a)) if a[i][k]),None)
        if j is None:continue
        a[r],a[j]=a[j],a[r];z=a[r][k];a[r]=[v/z for v in a[r]]
        for i in range(r+1,len(a)):
            c=a[i][k]
            if c:a[i]=[v-c*w for v,w in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return r

def det(A):
    a=[list(map(int,row)) for row in A];n=len(a);sign=1;prev=1
    for k in range(n-1):
        j=next((i for i in range(k,n) if a[i][k]),None)
        if j is None:return 0
        if j!=k:a[k],a[j]=a[j],a[k];sign=-sign
        p=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                z=a[i][j]*p-a[i][k]*a[k][j]
                if z%prev:raise ArithmeticError('nonexact Bareiss division')
                a[i][j]=z//prev
            a[i][k]=0
        prev=p
    return sign*a[-1][-1]

# Wilson's octonions, index 0=1 and 1..7=i_0..i_6.
OT=[[None]*8 for _ in range(8)]
for i in range(8):OT[0][i]=OT[i][0]=(i,1)
for i in range(1,8):OT[i][i]=(0,-1)
for t in range(7):
    a,b,c=[1+(t+k)%7 for k in (0,1,3)]
    for i,j,k in ((a,b,c),(b,c,a),(c,a,b)):OT[i][j]=(k,1);OT[j][i]=(k,-1)
def omul(x,y):
    out=[0]*8
    for i,a in enumerate(x):
        for j,b in enumerate(y):
            if a and b:k,s=OT[i][j];out[k]+=s*a*b
    return tuple(out)
def add(x,y):return tuple(a+b for a,b in zip(x,y))
def e8(v):
    m=v[0]%2
    return all(a%2==m for a in v) and sum(v)%4==2*m
S=(-1,1,1,1,1,1,1,1);SB=(-1,-1,-1,-1,-1,-1,-1,-1)
def rightlattice(v,c):
    w=omul(v,c)
    return all(a%4==0 for a in w) and e8(tuple(a//4 for a in w))
def wmember(x):
    a,b,c=x[:8],x[8:16],x[16:]
    return all(e8(v) for v in (a,b,c)) and all(rightlattice(v,S) for v in (add(a,b),add(a,c),add(b,c))) and rightlattice(add(add(a,b),c),SB)
def golay_to_wilson(x):return tuple(SIG[i]*x[PI[i]] for i in range(24))
def wilson_to_golay(y):
    x=[0]*24
    for i in range(24):x[PI[i]]=SIG[i]*y[i]
    return tuple(x)
def cubic(x):
    y=golay_to_wilson(x)
    return Q(omul(omul(y[:8],y[8:16]),y[16:])[0],4)

# Exact Q(i) arithmetic: no floating-point complex numbers.
def gi(x):return (Q(x),Q(0)) if not isinstance(x,tuple) else x
def ga(x,y):x,y=gi(x),gi(y);return (x[0]+y[0],x[1]+y[1])
def gn(x):x=gi(x);return (-x[0],-x[1])
def gm(x,y):x,y=gi(x),gi(y);return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def gc(x):x=gi(x);return (x[0],-x[1])
def gsum(xs):
    s=gi(0)
    for x in xs:s=ga(s,x)
    return s

def zorn(q):
    q=list(map(Q,q))
    a=(q[0],q[3]);b=(q[0],-q[3])
    u=((q[1],-q[7]),(q[2],-q[5]),(-q[4],-q[6]))
    v=tuple(gn(gc(x)) for x in u)
    return a,u,v,b

def zorn_inverse(z):
    a,u,v,b=z
    if b!=gc(a) or v!=tuple(gn(gc(x)) for x in u):raise ValueError('outside compact real form')
    return (a[0],u[0][0],u[1][0],a[1],-u[2][0],-u[1][1],-u[2][1],-u[0][1])
def tits_from_golay(x,diag=(0,0,0)):
    y=golay_to_wilson(x);zs=[zorn(tuple(Q(v,2) for v in y[8*j:8*j+8])) for j in range(3)]
    A=[[gi(0) for _ in range(3)] for _ in range(3)]
    B=[[gi(0) for _ in range(3)] for _ in range(3)]
    Cc=[[gi(0) for _ in range(3)] for _ in range(3)]
    for i,a in enumerate(diag):A[i][i]=gi(a)
    for j,(p,q) in enumerate(((1,2),(2,0),(0,1))):
        a,u,v,b=zs[j];A[p][q]=a;A[q][p]=b
        for i in range(3):B[i][j]=u[i];Cc[j][i]=gn(v[i])
    return A,B,Cc

def golay_from_tits(A,B,Cc,diag_expected=None):
    if any(A[i][j]!=gc(A[j][i]) or Cc[i][j]!=gc(B[j][i]) for i in range(3) for j in range(3)):raise ValueError('real structure not retained')
    y=[]
    for j,(p,q) in enumerate(((1,2),(2,0),(0,1))):
        z=(A[p][q],tuple(B[i][j] for i in range(3)),tuple(gn(Cc[j][i]) for i in range(3)),A[q][p])
        y+=list(2*a for a in zorn_inverse(z))
    x=wilson_to_golay(y)
    if diag_expected is not None and any(A[i][i]!=gi(diag_expected[i]) for i in range(3)):raise ValueError('wrong diagonal mark')
    return x

def gdet(A):
    return gsum(gm(gm(A[0][p[0]],A[1][p[1]]),A[2][p[2]]) if sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2==0 else gn(gm(gm(A[0][p[0]],A[1][p[1]]),A[2][p[2]])) for p in itertools.permutations(range(3)))
def tits_norm(A,B,Cc):
    return ga(gsum([gdet(A),gdet(B),gdet(Cc)]),gn(gsum(gm(gm(Cc[i][j],B[j][k]),A[k][i]) for i,j,k in itertools.product(range(3),repeat=3))))
def quadratic_coefficient(A,B,Cc):
    return ga(gsum(ga(gm(A[i][i],A[j][j]),gn(gm(A[i][j],A[j][i]))) for i,j in itertools.combinations(range(3),2)),gn(gsum(gm(Cc[i][j],B[j][i]) for i,j in itertools.product(range(3),repeat=2))))

def group_elements():
    cp,jp,tp=map(mv,(C,J,T));I=tuple(range(24));seen={I};todo=[I]
    for g in todo:
        for h in (jp,tp):
            k=permul(h,g)
            if k not in seen:seen.add(k);todo.append(k)
    return todo

# Normalized Fable factor chart and all 24 marked flags.
def fable(u,v,w):
    h=1+u*v
    return (h**3*w+v*v*h*(4+3*u*v),v+3*u*h*h*w+3*u*v*v*(4+3*u*v),2*u-3*u*u*v-u**3*w)
def chart(u,v,w):
    h=1+u*v
    return (u,h),(1-Q(3,2)*u*v-u*u*w/2,(v+u*h*w+3*u*v*v)/2,h*h*w+v*v*(4+3*u*v))
def factor_inverse(L,Qq):
    u,h=L;a,b,c=Qq
    return u,2*h*b-u*c,-4*b*b-2*a*c-12*h*b*b-6*h*a*c+9*c

def branches_of_face(roots):
    a,b,c=map(Q,roots);alpha=a*b*c/4;beta=-(a*b+a*c+b*c)/2;gamma=Q(-1,2)
    rows=[]
    for r in (a,b,c):
        d=-Q(3,4)*r*r+2*r+beta/2
        if d==0:raise ValueError('multiple selected root')
        point=(1/d,-r-d,5*d*d+3*r*d+d**3/2)
        check(fable(*point)==(alpha,beta,gamma),'marked-fable-inverse')
        L,Qq=chart(*point)
        check(factor_inverse(L,Qq)==point,'factor-chart-two-sided-return')
        check(L[0]*L[0]*Qq[2]-L[0]*L[1]*Qq[1]+L[1]*L[1]*Qq[0]==1,'factor-resultant')
        check(L[0]*Qq[1]+L[1]*Qq[0]==1,'factor-affine-normalization')
        rows.append((r,d,point,L,Qq))
    return (alpha,beta,gamma),rows

def atlas_certificate(p,ds):
    a=(-Q(p),)+tuple(4*Q(d) for d in ds)
    check(sum(1/x for x in a)==0,'Cayley-full-equation')
    flags=[]
    for flag in itertools.permutations(range(4)):
        i,j,k,l=flag;roots=tuple(-4*a[i]/a[v] for v in (j,k,l))
        check(sum(roots)==4 and all(v and v!=-4 for v in roots) and len(set(roots))==3,'Cayley-open-domain')
        target,br=branches_of_face(roots);r,d,point,L,Qq=br[0]
        h=-Q(1,4)/a[i];normalized=tuple(h*x for x in a)
        back=[None]*4;back[i]=-Q(1,4)
        for n,v in zip((j,k,l),roots):back[n]=1/v
        check(tuple(x/h for x in back)==a,'four-face-scale-return')
        eta=roots[1]-roots[2]
        check(eta*eta==(3*r-4)**2+16*d,'oriented-companion-equation')
        recovered=(r,(4-r+eta)/2,(4-r-eta)/2)
        check(recovered==roots,'oriented-companion-inverse')
        newflag=(j,i,l,k);newroots=tuple(-4*a[j]/a[v] for v in (i,l,k))
        expected=(16/r,-4*roots[2]/r,-4*roots[1]/r)
        check(newroots==expected,'four-face-transition')
        _,nb=branches_of_face(newroots);dd=nb[0][1]
        check(dd==8+16*(d-8)/r**2,'derivative-transition')
        check(newroots[1]-newroots[2]==4*eta/r,'orientation-transition')
        flags.append({'flag':flag,'orientation':(-1)**sum(flag[i]>flag[j] for i in range(4) for j in range(i+1,4)), 'scale':h,'roots':roots,'target':target,'selected_branch':point,'eta':eta,'factor_L':L,'factor_Q':Qq})
    check(len(flags)==24,'complete-four-face-orientation-fibres')
    return {'p':p,'denominators':ds,'homogeneous_Cayley':a,'flags':flags}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--out',type=Path,default=ROOT/'certificates');args=ap.parse_args();out=args.out;out.mkdir(parents=True,exist_ok=True)
    basis,code=golay();octads=sorted(c for c in code if c.bit_count()==8)
    check(len(basis)==12 and len(code)==4096,'Golay-dimension')
    check(collections.Counter(v.bit_count() for v in code)=={0:1,8:759,12:2576,16:759,24:1},'Golay-enumerator')
    cp,jp,tp=map(mv,(C,J,T));I=tuple(range(24));group=group_elements()
    check(len(group)==6072,'joint-symmetry-group')
    for g in (cp,jp,tp):
        for b in basis:check(pmask(b,g) in code,'code-generator-action')
    orb={mask(BLOCKS[0])};todo=list(orb)
    for b in todo:
        for g in (jp,tp):
            a=pmask(b,g)
            if a not in orb:orb.add(a);todo.append(a)
    check(orb==set(octads),'full-octad-orbit')
    inc=[[int(c>>i&1) for i in range(24)] for c in octads]
    for i in range(24):
        for j in range(24):check(sum(r[i]*r[j] for r in inc)==(253 if i==j else 77),'incidence-Gram')
    sub=[inc[i] for i in OCTAD_BASIS_IDS];detb=det(sub)
    check(abs(detb)==2**14,'integral-octad-basis-minor')
    v=(8,-8,8,0,-8,0,-8,0,8)+(0,)*15
    check(member(v,code) and trace9(v)==(0,)*9,'hidden-nine-trace-kernel')
    jv=act(v,jp)
    check(trace9(jv)==(0,0,0,-2,-2,2,0,0,2),'nine-trace-nonclosure-witness')
    frames=[];w=[tuple(2*int(i in b) for i in range(24)) for b in BLOCKS]
    for n in range(4):
        g=I
        for _ in range(n):g=permul(tp,g)
        for b in (BLOCKS if n==0 else BLOCKS[:2]):frames.append(tuple(2*int(g[i] in b) for i in range(24)))
    check(rank(frames)==9 and rank(frames+[act(v,jp) for v in frames])==15,'trace-span-ranks')
    # Explicit generators of the full Golay-model lattice.
    gens=[]
    for i in range(23):x=[0]*24;x[i]=4;x[23]=-4;gens.append(tuple(x))
    x=[0]*24;x[23]=8;gens.append(tuple(x))
    gens += [tuple(2*int(c>>i&1) for i in range(24)) for c in basis]
    gens.append((-3,)+(1,)*23)
    check(len(gens)==37,'full-lattice-generator-count')
    def inverse_traces(a):
        S=sum(a)
        return tuple(Q(23*sum(a[k] for k,c in enumerate(octads) if c>>i&1)-7*S,1012) for i in range(24))
    def trall(x):return tuple(Q(sum(x[i] for i in range(24) if c>>i&1),4) for c in octads)
    for x in gens+[tuple(Q(1,2) for _ in range(24))]:
        check(inverse_traces(trall(x))==x,'all-octad-linear-inverse')
    check(trall((Q(1,2),)*24)==(1,)*759,'constant-trace-obstruction')
    check(not member((1,)*24,code) and member((2,)*24,code),'order-four-not-order-two')
    for g in gens:
        for n in range(4):
            x=tuple(Q(a)+Q(n,2) for a in g);a=trall(x);S=sum(a);S0=sum(a[k] for k,c in enumerate(octads) if c&1)
            syndrome=(11*S-23*S0)/506
            check(syndrome.denominator==1 and int(syndrome)%4==n,'exact-mod-four-syndrome')
    # The selected model isometry preserves each marked block, and all lattice generators.
    check(sorted(PI)==list(range(24)) and all(a in (-1,1) for a in SIG),'signed-coordinate-isometry')
    for j in range(3):check(set(PI[8*j:8*j+8])==set(BLOCKS[j]),'octad-block-alignment')
    for g in gens:
        check(member(g,code) and wmember(golay_to_wilson(g)),'all-generator-image-memberships')
        check(wilson_to_golay(golay_to_wilson(g))==g,'isometry-two-sided-return')
        abc=tits_from_golay(g)
        check(golay_from_tits(*abc,diag_expected=(0,0,0))==g,'Golay-Wilson-Zorn-Tits-return')
        check(tits_norm(*abc)==gi(cubic(g)),'exact-cubic-return')
        tt=trace(g);aug=tits_from_golay(g,tt)
        check(golay_from_tits(*aug,diag_expected=tt)==g,'augmented-Albert-return')
        yy=golay_to_wilson(g);nn=[Q(dot(yy[8*j:8*j+8],yy[8*j:8*j+8]),4) for j in range(3)]
        check(tits_norm(*aug)==gi(math.prod(tt)-sum(tt[j]*nn[j] for j in range(3))+cubic(g)),'all-cubic-mixed-corrections')
        check(quadratic_coefficient(*aug)==gi(sum(tt[i]*tt[j] for i,j in itertools.combinations(range(3),2))-sum(nn)),'quadratic-trace-corrections')
    bs=(B0,act(B0,cp),act(act(B0,cp),cp))
    check(tuple(cubic(b) for b in bs)==(-5,1,-1),'phase-isometry-not-cubic-automorphism')
    k=(-4,2,2,0,0,-2,-2,2,2,0,2,0,0,2,0,2,2,0,0,-2,-2,0,0,-4)
    check(member(k,code) and trace(k)==(0,0,0) and cubic(k)==-8,'cubic-does-not-descend-through-trace')
    # Exact coefficients of the transported cubic, from all basis triples.
    co={}
    for i,j,k0 in itertools.product(range(8),repeat=3):
        ei=tuple(int(t==i) for t in range(8));ej=tuple(int(t==j) for t in range(8));ek=tuple(int(t==k0) for t in range(8))
        a=omul(omul(ei,ej),ek)[0]
        if a:co[tuple(sorted((PI[i],PI[8+j],PI[16+k0])))]=a*SIG[i]*SIG[8+j]*SIG[16+k0]
    check(len(co)==64,'complete-ternary-cubic-coefficients')
    # Polarize in the 24-coordinate domain: checks include all diagonal/mixed cubic coefficients.
    e=[tuple(int(i==j) for i in range(24)) for j in range(24)]
    tests=e+[add(e[i],e[j]) for i,j in itertools.combinations(range(24),2)]
    tests += [tuple(a-b for a,b in zip(e[i],e[j])) for i,j in itertools.combinations(range(24),2)]
    tests += [add(add(e[i],e[j]),e[k]) for i,j,k in itertools.combinations(range(24),3)]
    for x in tests:
        check(tits_norm(*tits_from_golay(x))==gi(cubic(x)),'full-cubic-polarization-grid')
    # A homogeneous cubic in 24 variables has binomial(26,3)=2600 coefficients.
    # e_i plus both e_i+e_j and e_i-e_j separate the two repeated-index
    # coefficients; three-distinct-index sums then recover the rest.
    check(len(tests)==math.comb(26,3),'complete-cubic-test-dimension')
    section_coefficients={
        (3,0,0):-5,(2,1,0):-1,(2,0,1):-3,(1,2,0):-3,(1,1,1):2,
        (1,0,2):1,(0,3,0):1,(0,2,1):5,(0,1,2):-5,(0,0,3):-1}
    three=[tuple(int(i==j) for i in range(3)) for j in range(3)]
    tgrid=three+[add(three[i],three[j]) for i,j in itertools.combinations(range(3),2)]
    tgrid += [tuple(a-b for a,b in zip(three[i],three[j])) for i,j in itertools.combinations(range(3),2)]
    tgrid += [(1,1,1)]
    for t in tgrid:
        rhs=sum(c*math.prod(t[i]**ex[i] for i in range(3)) for ex,c in section_coefficients.items())
        check(cubic(combine(t,bs))==rhs,'full-section-cubic-identity')
    # Face/factor data: all 24 flags, all three local factors, all scale returns.
    states=[(5,(2,4,20)),(1201,(306,16218,1082101)),(2521,(638,804199,55462))]
    atlas=[atlas_certificate(p,ds) for p,ds in states]
    # True end-to-end composition, not just disconnected unit tests.
    markings=[{'channel':'E','R':3,'h':2,'r':1,'s':1,'u_ES':2,'quotient':2},
              {'channel':'E','R':23,'h':17,'r':1,'s':18,'u_ES':17,'quotient':53},
              {'channel':'M','R':31,'h':11,'r':2,'s':29,'u_ES':44,'quotient':1}]
    end_to_end=[]
    for dat,mark in zip(atlas,markings):
        p0=dat['p'];den0=dat['denominators']
        for state in dat['flags']:
            uu,vv,ww=state['selected_branch'];dd=1/uu;rr=-vv-dd
            eta=state['eta'];rootback=(rr,(4-rr+eta)/2,(4-rr-eta)/2)
            ia,ib,ic,id=state['flag'];aa=[None]*4;aa[ia]=-Q(1,4)/state['scale']
            for j,rt in zip((ib,ic,id),rootback):aa[j]=1/(state['scale']*rt)
            check(-aa[0]==p0 and tuple(a/4 for a in aa[1:])==den0,'end-to-end-Fable-to-ES')
            lam=combine(den0,bs);av=tits_from_golay(lam,den0)
            back=golay_from_tits(*av,diag_expected=den0)
            check(back==lam and trace(back)==den0,'end-to-end-Leech-Albert-trace')
            x,y,z=map(int,trace(back));R0=4*x-p0
            divisor=Q(x*x if mark['channel']=='E' else p0*x*x,R0*y-p0*x)
            check(divisor.denominator==1,'end-to-end-selector-integrality')
            div=int(divisor);g0=math.gcd(x,div);r0=div//g0;s0=x//g0;h0=g0//r0
            quot=Q(p0*r0+s0,R0) if mark['channel']=='E' else Q(r0+s0,R0)
            recovered={'channel':mark['channel'],'R':R0,'h':h0,'r':r0,'s':s0,'u_ES':div,'quotient':int(quot)}
            check(quot.denominator==1 and recovered==mark,'complete-channel-mark-return')
        end_to_end.append({'p':p0,'ordered_denominators':den0,'all_24_flags_pass':True,'original_mark':mark,'linear_Leech_lift_numerator':combine(den0,bs)})
    # A split norm-preserving pure move can leave the compact real form.
    A0=[[gi(2 if i==j==0 else 3 if i==j==1 else 5 if i==j==2 else 0) for j in range(3)] for i in range(3)]
    Btest=[[gi(0) for _ in range(3)] for _ in range(3)];Ctest=[[gi(0) for _ in range(3)] for _ in range(3)]
    Btest[2][2]=gi(-2)
    check(tits_norm(A0,Btest,Ctest)==gi(30),'split-move-retains-cubic-norm')
    try:golay_from_tits(A0,Btest,Ctest)
    except ValueError:compact_rejected=True
    else:compact_rejected=False
    check(compact_rejected,'split-to-compact-domain-guard')
    dump(out/'end_to_end_returns.json',{'arithmetic_returns':end_to_end,'split_move':{'a':[1,0,0],'b':[0,1,0],'c':[0,0,1],'t':1,'input_A_diagonal':[2,3,5],'input_B_C_zero':True,'output_B_33':-2,'output_C_zero':True,'cubic_norm':30,'compact_real_return_rejected':True}})
    # Branch table is an equivariant finite label map, never an arithmetic reconstruction by itself.
    def cflag(f):i,j,k,l=f;return (i,k,l,j)
    def jflag(f):i,j,k,l=f;return (j,i,l,k)
    fmap={(0,1,2,3):23};queue=list(fmap)
    for f in queue:
        for fun,g in ((cflag,cp),(jflag,jp)):
            h=fun(f);z=g[fmap[f]]
            if h in fmap:check(fmap[h]==z,'generator-typed-flag-equivariance')
            else:fmap[h]=z;queue.append(h)
    check(len(fmap)==12 and len(set(fmap.values()))==12,'twelve-branch-label-bijection')
    dump(out/'audit_algebra.json',{'counts':dict(COUNT),'signed_isometry':{'source_index_to_projective_index':PI,'signs':SIG,'coordinate_rule':'Wilson_raw[i]=sign[i]*Golay_raw[pi[i]]','37_generator_images':[golay_to_wilson(x) for x in gens]},'kernel_counterexamples':{'nine_trace_numerator':v,'J_nine_traces':trace9(jv),'three_trace_numerator':k,'Wilson_cubic':-8},'phase_cubic_values':[-5,1,-1],'section_cubic_coefficients':[{'exponents':ex,'coefficient':c} for ex,c in sorted(section_coefficients.items())],'four_times_cubic_monomials':[{'indices':m,'coefficient':c} for m,c in sorted(co.items())],'flag_to_projective_coordinate':[{'flag':f,'coordinate':z} for f,z in sorted(fmap.items())]})
    dump(out/'complete_octad_trace.json',{'octads':[[i for i in range(24) if c>>i&1] for c in octads],'basis_indices':OCTAD_BASIS_IDS,'basis_masks':[octads[i] for i in OCTAD_BASIS_IDS],'indicator_basis_determinant':detb,'Gram_parameters':[176,77],'inverse_denominator':1012,'linear_reconstruction':'x_i=(23*sum_{B containing i} a_B-7*sum_B a_B)/1012','integral_syndrome':'(11*sum_B a_B-23*sum_{B containing 0}a_B)/506 mod4','kernel_rank':0,'octad_sublattice_index_in_Leech':4,'all_group_orbit_octads':len(orb),'generated_group_order':len(group)})
    dump(out/'all_marked_fable_junctions.json',atlas)
    receipt={'status':'PASS','conditions':sum(COUNT.values()),'counts':dict(COUNT),'arithmetic_inputs':3,'oriented_and_reversed_flags':72,'distinct_face_local_factor_instances':216,'factor_return_evaluations_including_transition':432,'full_homogeneous_cubic_test_nodes':2600,'codewords':len(code),'octads':len(octads),'finite_group_elements':len(group),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'not_claimed':['independent reviewer','a Lean build','global ES/RH proof','full literature priority','a cubic-norm identification with trace product']}
    dump(out/'audit_receipt.json',receipt);print(json.dumps(receipt,sort_keys=True))
if __name__=='__main__':main()
