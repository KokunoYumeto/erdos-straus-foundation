"""Exact original ES receiver and first-order asymptotic checks."""
from pathlib import Path
import itertools,json,hashlib
import sympy as s
import mpmath as mp

exact=[]; numerical=[]
def ck(b,label):
    if not bool(b):raise AssertionError(label)
    exact.append(label)
def z(v,label):
    vv=list(v) if isinstance(v,s.MatrixBase) else [v]
    ck(all(s.simplify(x)==0 for x in vv),label)
def nc(b,label,detail):
    if not bool(b):raise AssertionError((label,detail))
    numerical.append(dict(label=label,detail=detail))

t,c=s.symbols('t c',positive=True)
p=1/t;a=(p+3)/4;P=p*a;Y=(P+c)/3;Z=P*(P+c)/(3*c)
roots=[p,a,Y,Z];SS=sum(roots);AA=-1/SS
ds=[s.factor(AA*s.prod(x-y for j,y in enumerate(roots) if i!=j)) for i,x in enumerate(roots)]
scales=[t**-3,t**-3,t**-4,t**-8]
leading=[-s.Rational(1,16),s.Rational(1,16),s.Rational(1,144),-1/(2304*c*c)]
xi_powers=[s.Rational(3,2),s.Rational(3,2),s.Integer(2),s.Integer(4)]
xi_const=[4*s.I,4,12,48*s.I*c]
def trunc(v):return s.series(v,t,0,2).removeO().expand()
dnorm=[trunc(dd/(lead*scale)) for dd,lead,scale in zip(ds,leading,scales)]
xis=[xi_const[j]*t**xi_powers[j]*trunc(dnorm[j]**s.Rational(-1,2)) for j in range(4)]
dapprox=[leading[j]*scales[j]*dnorm[j] for j in range(4)]
O=s.Matrix.hstack(*(xis[j]*s.Matrix([1,-s.I*dapprox[j],AA*dapprox[j]**2+2*roots[j]*dapprox[j],s.I*(7*roots[j]**2*dapprox[j]-13*dapprox[j]**2)]) for j in range(4)))
B=s.diag(1,t**3,t**4,t**6)*O*s.diag(t**s.Rational(-3,2),t**s.Rational(-3,2),1,t**6)
B=B.applyfunc(trunc);B0=B.subs(t,0);B1=B.diff(t).subs(t,0)
expected=s.Matrix([[4*s.I,4,0,0],[-s.Rational(1,4),-s.I/4,0,0],[-s.I/2,s.Rational(1,8),s.Rational(1,72),0],[s.Rational(13,64),-13*s.I/64,-s.I/288,5/(27648*c**3)]])
z(B0-expected,'complete weighted receiver leading matrix')
z(B0.det()-5/(995328*c**3),'complete weighted determinant leading coefficient')
e0=s.Matrix([1,0,0,0]);v0=B0.inv()*e0;v1=-B0.inv()*B1*v0
z(v0-s.Matrix([-s.I/8,s.Rational(1,8),s.Rational(27,8),1728*s.I*c**3/5]),'complete exact inverse-column leading coefficient')
z(v1[:2,0]-s.Matrix([-s.I/2,-s.Rational(19,16)]),'first core inverse-column correction')
z(B1[:2,:]-s.Matrix([[20*s.I,2,0,0],[s.Rational(5,4),s.I/8,-s.I/12,0]]),'full upper-row first derivative including Y term')
z(B1[3,3]/B0[3,3]-18,'largest singular first correction')
M=B.extract([2,3],[2,3]).det().expand();M0=M.subs(t,0);M1=M.diff(t).subs(t,0)
z(M1/M0-s.Rational(33,2),'second exterior first correction')
min3=[B.extract([1,2,3],cols).det().expand() for cols in ([0,2,3],[1,2,3])]
norm3=sum(mm*s.conjugate(mm) for mm in min3)
N0=norm3.subs(t,0);N1=norm3.diff(t).subs(t,0)
z(N1/(2*N0)-s.Rational(25,4),'third exterior first correction with both core triples')
detB=B.det().expand();det0=detB.subs(t,0);det1=detB.diff(t).subs(t,0)
z(det1/det0-9,'complete determinant first correction')
z(s.Rational(25,4)-s.Rational(33,2)+s.Rational(41,4),'third singular first correction')
z(9-s.Rational(25,4)-s.Rational(11,4),'smallest singular first correction')
u0=s.Matrix([-s.I/8,s.Rational(1,8),0,0]);u1=s.Matrix([-s.I/2,-s.Rational(19,16),0,0])
z((u0.conjugate().T*u0)[0]-s.Rational(1,32),'inverse limiting norm squared')
z(2*s.re((u0.conjugate().T*u1)[0])+s.Rational(11,64),'inverse norm first correction')
z((6912*s.sqrt(2)/5)**2-s.Rational(95551488,25),'last observation exact squared coefficient')

# Exact rational verification avoids approximating any square root: O=R diag(xi).
for pp,cc in [(13,2),(37,2),(3361,29),(27721,29)]:
    aa=s.Rational(pp+3,4);PP=pp*aa;yy=(PP+cc)/3;zz=PP*(PP+cc)/(3*cc)
    rr=[s.Integer(pp),aa,yy,zz];SS=sum(rr);AA=-1/SS
    dd=[AA*s.prod(x-y for j,y in enumerate(rr) if i!=j) for i,x in enumerate(rr)]
    ck(all(s.denom(v)==1 for v in (aa,yy,zz)),f'integral family p{pp} c{cc}')
    z(1/aa+1/yy+1/zz-s.Rational(4,pp),f'exact ES reciprocal identity p{pp} c{cc}')
    e2=sum(rr[i]*rr[j] for i in range(4) for j in range(i+1,4));e3=sum(s.prod(rr[j] for j in ix) for ix in itertools.combinations(range(4),3))
    x=s.symbols('x');P2=x*x+19*SS*x/7+e2/2-10*SS*SS/7
    Rs=[s.I*(x**3+(19*SS*SS/7+e2)*x-10*SS**3/7+SS*e2/2-3*e3/4),(5*SS*SS-13*SS*x)/7,s.I*(SS-4*x)/28]
    hh=sum(P2.subs(x,r)/di**2 for r,di in zip(rr,dd));rh=[sum(Ri.subs(x,r)/di**2 for r,di in zip(rr,dd)) for Ri in Rs]
    raw=s.Matrix.hstack(*(s.Matrix([1,-s.I*di,AA*di*di+2*r*di,s.I*(7*r*r*di-13*di*di)]) for r,di in zip(rr,dd)))
    invcol=s.Matrix([P2.subs(x,r)/(di*di*hh) for r,di in zip(rr,dd)])
    z(raw*invcol-e0,f'exact original inverse zero column p{pp}')
    for nu in range(3):
        col=s.Matrix([AA/(di*di)*(Rs[nu].subs(x,r)-P2.subs(x,r)*rh[nu]/hh) for r,di in zip(rr,dd)])
        z(raw*col-s.eye(4)[:,nu+1],f'exact inverse column {nu+1} p{pp}')
    Delta=s.prod(rr[j]-rr[i] for i in range(4) for j in range(i+1,4))
    z(raw.det()-28*AA**3*Delta*s.prod(dd)*hh,f'exact determinant denominator identity p{pp}')
    ck(hh<0,f'nonzero signed inverse denominator p{pp}')
ck(s.gcd(3361,24360)==1 and 3361%840==1 and 3361%116==113,'coprime original hard-residue progression')
ck(s.isprime(3361),'initial displayed prime')
ck((3361*(3361+3)//4+29)//3==942210,'initial displayed Y')
ck((3361*(3361+3)//4)*942210//29==91836266490,'initial displayed Z')

mp.mp.dps=110
def receiver(pp,cc=None,u=None):
    pp=mp.mpf(pp); aa=(pp+3)/4
    if cc is not None:
        yy=(pp*aa+cc)/3;zz=pp*aa*(pp*aa+cc)/(3*cc)
    else:
        yy=(pp*aa+aa*aa/u)/3;zz=(pp*aa+pp*pp*u)/3
    rr=[pp,aa,yy,zz];SS=sum(rr);AA=-1/SS
    dd=[AA*mp.fprod(x-y for j,y in enumerate(rr) if i!=j) for i,x in enumerate(rr)]
    xx=[1/mp.sqrt(dd[j]) if dd[j]>0 else 1j/mp.sqrt(-dd[j]) for j in range(4)]
    O=mp.matrix(4)
    for j in range(4):
        di=dd[j];r=rr[j];col=[1,-1j*di,AA*di*di+2*r*di,1j*(7*r*r*di-13*di*di)]
        for i in range(4):O[i,j]=xx[j]*col[i]
    return O,rr
coeffs=[mp.mpf(18),-mp.mpf(3)/2,-mp.mpf(41)/4,mp.mpf(11)/4]
for cc in (2,29):
    for pp in (10000,20000,40000):
        O,rr=receiver(pp,cc=cc);U,ss,V=mp.svd(O)
        lead=[mp.mpf(5)/(27648*cc**3)*pp**12,mp.mpf(1)/72*pp**4,mp.mpf(1)/(2*mp.sqrt(2))*pp**mp.mpf('1.5'),4*mp.sqrt(2)*pp**mp.mpf('-1.5')]
        residuals=[float(pp*(ss[j]/lead[j]-1)-coeffs[j]) for j in range(4)]
        nc(max(abs(v) for v in residuals)<2000/pp,f'all four first corrections c{cc} p{pp}',residuals)
        soft=float(pp*(pp**3*ss[3]**2-32)-176)
        nc(abs(soft)<50000/pp,f'soft energy first correction c{cc} p{pp}',soft)
        dv=mp.det(O);dr=float(pp*(dv.real/(mp.mpf(5)/(995328*cc**3)*pp**16)-1)-9)
        nc(abs(dr)<2000/pp,f'full determinant first correction c{cc} p{pp}',dr)
        inv=O**-1; col=inv[:,0];ncol=mp.sqrt(sum(abs(v)**2 for v in col));phase=mp.conj(col[1])/abs(col[1]);col=col*phase/ncol
        # Right singular vector of O, aligned by its positive a-coordinate.
        slow=V[3,:].transpose_conj();slow=slow*(mp.conj(slow[1])/abs(slow[1]))
        zconst=6912*mp.sqrt(2)*1j*cc**3/5
        zr=float(abs(slow[3]*pp**mp.mpf('7.5')/zconst-1))
        nc(zr<200/pp,f'relative last-label singular-vector asymptotic c{cc} p{pp}',zr)
        ycor=mp.mpf(pp)*(slow[2]*pp**mp.mpf('1.5')/(27*mp.sqrt(2)/2)-1)-mp.mpf(21)/4
        zcor=mp.mpf(pp)*(slow[3]*pp**mp.mpf('7.5')/zconst-1)+mp.mpf(105)/4
        nc(abs(ycor)<5000/pp and abs(zcor)<5000/pp,f'both relative tail-vector first corrections c{cc} p{pp}',[float(abs(ycor)),float(abs(zcor))])
        tau=mp.mpf('.125');expsoft=mp.exp(-tau*pp**3*ss[3]**2)
        hy=pp**3*abs(slow[2])**2*expsoft/(mp.mpf(729)/2*mp.exp(-32*tau))
        hz=pp**15*abs(slow[3])**2*expsoft/(mp.mpf(95551488)*cc**6/25*mp.exp(-32*tau))
        ery=pp*(hy-1)-(mp.mpf(21)/2-176*tau);erz=pp*(hz-1)-(-mp.mpf(105)/2-176*tau)
        nc(abs(ery)<10000/pp and abs(erz)<10000/pp,f'both rare-label heat first corrections c{cc} p{pp}',[float(abs(ery)),float(abs(erz))])
        # This compares the exact auxiliary inverse column to the true slow direction.
        diff=mp.norm(slow-col)
        nc(diff<mp.mpf(1000000)*pp**-6,f'actual inverse column to slow direction c{cc} p{pp}',float(diff))
        if cc==2 and pp in (10000,40000):
            RG=mp.matrix([[2,1j/3,mp.mpf('.2'),0],[0,1,1j/5,mp.mpf('.1')],[0,0,mp.mpf('1.5'),1j/7],[0,0,0,mp.mpf('.8')]])
            RQ=mp.matrix([[mp.mpf('1.3'),1j/4,0,mp.mpf('.1')],[0,mp.mpf('.9'),1j/8,0],[0,0,2,mp.mpf('.2')],[0,0,0,1]])
            GG=RG.H*RG;QQ=RQ.H*RQ
            UU,sv,VV=mp.svd(RQ*O*RG**-1);physical=RG**-1*VV[3,:].transpose_conj()
            uu0=mp.matrix([-1j/8,mp.mpf(1)/8,0,0]);uu1=mp.matrix([-1j/2,-mp.mpf(19)/16,0,0])
            ng=(uu0.H*GG*uu0)[0].real;qq=(QQ**-1)[0,0].real;lead=1/(ng*qq)
            corr=-2*(uu0.H*GG*uu1)[0].real/ng
            err=pp*(pp**3*sv[3]**2/lead-1)-corr
            nc(abs(err)<200/mp.sqrt(pp),f'fixed complex metric soft-energy first correction p{pp}',float(err))
            rows=[mp.matrix([[1j/mp.sqrt(2),1/mp.sqrt(2),0,0]]),mp.matrix([[-1j/mp.sqrt(2),1/mp.sqrt(2),0,0]]),mp.matrix([[0,0,1,0]]),mp.matrix([[0,0,0,1]])]
            nums=[abs((rows[0]*uu0)[0])**2,abs((rows[1]*uu1)[0])**2,mp.mpf(27)**2/64,(mp.mpf(1728)*cc**3/5)**2]
            errors=[abs(pp**power*abs((row*physical)[0])**2/(num/ng)-1) for row,power,num in zip(rows,[0,2,3,15],nums)]
            nc(max(errors)<500/mp.sqrt(pp),f'all four annihilation tiers in fixed complex metrics p{pp}',[float(e) for e in errors])

for pp in (24013,48013):
    O,rr=receiver(pp,u=mp.mpf(2));U,ss,V=mp.svd(O)
    nc(abs(float(pp**mp.mpf('-1.5')/ss[3])-1/(4*2**.5))<10/pp,f'u2 same inverse limit p{pp}',float(pp**mp.mpf('-1.5')/ss[3]))
    nc(abs(float(1/(ss[2]*ss[3]))-.5)<10/pp,f'u2 same second inverse exterior limit p{pp}',float(1/(ss[2]*ss[3])))
    nc(abs(float(abs(mp.det(O))/pp**10)-19159/98304)<100/pp,f'u2 different full determinant p{pp}',float(abs(mp.det(O))/pp**10))

for uu in (1,2,10,10000):
    pp=10000;ww=mp.mpf(pp)/3;O,rr=receiver(pp,u=mp.mpf(uu));U,ss,V=mp.svd(O)
    yy,zz=rr[2:];UU=yy+zz;ta=(zz-yy)/UU
    A3=mp.sqrt(ta*(yy**6*(7-13*ta)**2+zz**6*(7+13*ta)**2))
    A23=ta**2*yy**2*zz**2*UU*(40-14*yy*zz/UU**2)
    leads=[A3,A23/A3,mp.sqrt(mp.mpf(3)/8)*pp*mp.sqrt(ww),mp.sqrt(mp.mpf(32)/3)/(pp*mp.sqrt(ww))]
    errs=[float(abs(ss[j]/leads[j]-1)*ww) for j in range(4)]
    nc(max(errs)<100,f'complete uniform-tail spectrum u{uu}',errs)

here=Path(__file__).resolve().parent
receipt=dict(status='passed',exact_count=len(exact),numerical_count=len(numerical),exact=exact,numerical=numerical,script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(here/'ES_CHECKS.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
(here/'ES_FIRST_ORDER_MATRICES.txt').write_text('B0 = '+str(B0)+'\nB1 = '+str(B1)+'\nz0 = '+str(v0)+'\nz1 = '+str(v1)+'\n',encoding='utf-8')
print(json.dumps({k:receipt[k] for k in ('status','exact_count','numerical_count','script_sha256')}))
