#!/usr/bin/env python3
"""Literal ES quartic: integral signed completion, normalization and local controls.
Python standard library only. A bounded replay is not an existence theorem.
"""
from __future__ import annotations
import argparse, hashlib, json, time
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from math import gcd, isqrt, prod
from pathlib import Path

CHECK=Counter()
HARD={1,121,169,289,361,529}

def need(ok,label):
    CHECK[label]+=1
    if not ok:raise ArithmeticError(label)

def primes_to(n):
    z=bytearray(b'\1')*(n+1)
    if n>=0:z[0]=0
    if n>=1:z[1]=0
    for d in range(2,isqrt(n)+1):
        if z[d]:z[d*d:n+1:d]=b'\0'*((n-d*d)//d+1)
    return [i for i in range(2,n+1) if z[i]]

@lru_cache(None)
def factor(n):
    if n<1:raise ValueError('positive factorization input required')
    out=[];d=2
    while d*d<=n:
        if n%d==0:
            e=0
            while n%d==0:n//=d;e+=1
            out.append((d,e))
        d=3 if d==2 else d+2
    if n>1:out.append((n,1))
    return tuple(out)

def isprime(n):return n>=2 and factor(n)==((n,1),)

@lru_cache(None)
def square_divisors(a):
    out=[1]
    for q,e in factor(a):out=[d*q**j for d in out for j in range(2*e+1)]
    return tuple(sorted(out))

def vp(x,p):
    x=F(x)
    if not x:return 10**9
    n=abs(x.numerator);d=x.denominator;e=0
    while n%p==0:n//=p;e+=1
    while d%p==0:d//=p;e-=1
    return e

def mod(x,m):
    x=F(x)
    return x.numerator*pow(x.denominator,-1,m)%m

def leg(x,p):
    x=mod(x,p)
    if not x:return 0
    return 1 if pow(x,(p-1)//2,p)==1 else -1

def enc(x):
    if isinstance(x,F):return [x.numerator,x.denominator]
    if isinstance(x,dict):return {k:enc(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [enc(v) for v in x]
    return x

def canon(x):return json.dumps(enc(x),sort_keys=True,separators=(',',':')).encode()
def sha(x):return hashlib.sha256(canon(x)).hexdigest()

def trim(a):
    a=list(map(F,a))
    while len(a)>1 and not a[-1]:a.pop()
    return a

def padd(a,b):
    z=[F(0)]*max(len(a),len(b))
    for i,x in enumerate(a):z[i]+=x
    for i,x in enumerate(b):z[i]+=x
    return trim(z)

def pmul(a,b):
    z=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]+=x*y
    return trim(z)

def pscale(a,b):return trim([F(b)*x for x in a])
def peval(a,x):
    y=F(0)
    for c in reversed(a):y=y*x+c
    return y

def poly_roots(roots):
    out=[F(1)]
    for x in roots:out=pmul(out,[-F(x),1])
    return out

def pder(a):return [i*a[i] for i in range(1,len(a))]

def interp(roots,values):
    out=[F(0)]*len(roots)
    for i,x in enumerate(roots):
        rest=[z for j,z in enumerate(roots) if j!=i]
        out=padd(out,pscale(poly_roots(rest),F(values[i])/prod(x-z for z in rest)))
    return out+[F(0)]*(len(roots)-len(out))

def inverse(a):
    n=len(a);b=[[F(z) for z in row]+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
    for k in range(n):
        pivot=next(i for i in range(k,n) if b[i][k])
        b[k],b[pivot]=b[pivot],b[k]
        v=b[k][k];b[k]=[z/v for z in b[k]]
        for i in range(n):
            if i!=k:
                v=b[i][k];b[i]=[x-v*y for x,y in zip(b[i],b[k])]
    return [row[n:] for row in b]

def mv(a,x):return [sum((v*w for v,w in zip(row,x)),F(0)) for row in a]

def matmul(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0))
             for j in range(len(B[0]))] for i in range(len(A))]

def smith_p(a,p):
    """DVR Smith exponents via integral row/column elimination over Q."""
    b=[[F(x) for x in row] for row in a];n=len(b);out=[]
    for k in range(n):
        val,i,j=min((vp(b[i][j],p),i,j) for i in range(k,n) for j in range(k,n))
        need(val<10**9,'nonsingular lattice matrix')
        b[k],b[i]=b[i],b[k]
        for row in b:row[k],row[j]=row[j],row[k]
        pivot=b[k][k];out.append(val)
        for i in range(k+1,n):
            c=b[i][k]/pivot
            need(vp(c,p)>=0,'Smith row multiplier integral')
            for j in range(k+1,n):b[i][j]-=c*b[k][j]
            b[i][k]=0
        for j in range(k+1,n):
            need(vp(b[k][j]/pivot,p)>=0,'Smith column multiplier integral')
            b[k][j]=0
    need(out==sorted(out),'ordered Smith exponents')
    return out

def state(p,a,u,ch):
    R=4*a-p
    need(ch in ('E','M') and p<4*a and 2*a<p,'original first-half domain')
    need(u>0 and a*a%u==0,'original square divisor')
    need(((4*u+1) if ch=='E' else (u+a))%R==0,'original channel gate')
    d=gcd(a,u);h=d*d//u;r=u//d;s=a//d
    need(h*r*s==a and h*r*r==u and gcd(r,s)==1,'original normalization')
    k=(p*r+s)//R if ch=='E' else (r+s)//R
    need(R*k==(p*r+s if ch=='E' else r+s),'original quotient integer')
    den=[a,h*s*k,p*h*r*k] if ch=='E' else [a,p*h*s*k,p*h*r*k]
    x,y,z=den
    need(4*x*y*z==p*(x*y+x*z+y*z),'ordered reciprocal identity')
    need(F(a*a if ch=='E' else p*a*a,R*y-p*a)==u,'ordered divisor inverse')
    need(leg(h if ch=='E' else r*s,p)==-1,'original character')
    obj=dict(p=p,channel=ch,a=a,R=R,u=u,h=h,r=r,s=s,quotient=k,denominators=den)
    if ch=='E':
        D=(4*u+1)//R;v=a*a//u
        obj.update(D=D,v=v,alpha=v-R,beta=v-D)
    return obj

def marking(st):
    st=dict(st);fu=dict(factor(st['u']))
    st['factorization']=[list(z) for z in factor(st['a'])]
    st['exponent_box']=[[q,-e,e] for q,e in factor(st['a'])]
    st['centered_exponents']=[[q,fu.get(q,0)-e] for q,e in factor(st['a'])]
    return st

def literal(p,den,ch):
    """Also accepts rational triples in the explicitly labelled control family."""
    roots=[F(p)]+list(map(F,den));S=sum(roots)
    need(len(set(roots))==4,'four distinct literal roots')
    need(vp(S,p)==0,'literal normalization scale unit')
    f=pscale(poly_roots(roots),-1/S);D,C,B,one,A=f
    need(one==1 and D==-F(p,5)*C,'literal coefficient normalization')
    need(B==-A*p*p-p-F(4,5*p)*C,'fixed-prime coefficient surface')
    need(625*A*D**3-125*C*D**2+25*B*C*C*D-4*C**4==0,'ES coefficient hypersurface')
    ds=[-prod(roots[i]-roots[j] for j in range(4) if i!=j)/S for i in range(4)]
    need(ds==[peval(pder(f),x) for x in roots],'all derivative values')
    dv=[vp(x,p) for x in ds]
    dc=[leg(x/F(p)**v,p) for x,v in zip(ds,dv)]
    disc=A**6*prod((roots[i]-roots[j])**2 for i in range(4) for j in range(i))
    ep=pscale(poly_roots(roots[1:]),1/prod(roots[0]-x for x in roots[1:]))
    need([peval(ep,x) for x in roots]==[1,0,0,0],'labelled prime idempotent')
    npoints=2*sum(v%2==0 and c==1 for v,c in zip(dv,dc))
    if ch=='E':
        need(dv==[1,0,0,1],'E derivative valuation pattern')
        need(dc[0]==dc[3] and dc[1]==dc[2],'E paired square classes')
        need([vp(z,p) for z in (A,B,C,D)]==[0,0,1,2],'E coefficient valuations')
        need(vp(disc,p)==2 and npoints in (0,4),'E discriminant and point count')
        need(min(vp(c,p) for c in ep)==-1,'E projector exact denominator')
        need(mod(roots[3]/p,p)==pow(4,-1,p),'E last root quotient')
        normal_disc=2;signed_disc=6
    else:
        a,b,c=roots[1],roots[2]/p,roots[3]/p
        need(mod(4*b*c-b-c,p)==0 and leg(b*c,p)==-1,'M actual residue character')
        need(len({1,mod(b,p),mod(c,p)})==3,'M three distinct normalized roots')
        need(dv==[2,0,2,2] and dc[1]==1,'M derivative valuation pattern')
        need([vp(z,p) for z in (A,B,C,D)]==[0,1,2,3],'M coefficient valuations')
        need(vp(disc,p)==6 and npoints in (4,8),'M discriminant and point count')
        need(min(vp(c,p) for c in ep)==-2,'M projector exact denominator')
        normal_disc=0;signed_disc=18
    # Trace discriminant for the quadratic extension of the root order.
    need(2*vp(disc,p)+sum(dv)==signed_disc,'signed discriminant tower formula')
    need((signed_disc-normal_disc)//2==(2 if ch=='E' else 9),'normalization index from discriminant')
    return dict(roots=roots,S=S,coefficients=f,derivatives=ds,derivative_valuations=dv,
                derivative_unit_symbols=dc,discriminant=disc,prime_idempotent=ep,
                rational_local_points=npoints,normalization_index_exponent=(2 if ch=='E' else 9),
                channel=ch)

def order_certificate(st):
    p=st['p'];ch=st['channel'];dat=literal(p,st['denominators'],ch)
    roots=dat['roots'];ds=dat['derivatives'];ks=[v//2 for v in dat['derivative_valuations']]
    # Normal basis (1,theta_i), theta_i=eta_i/p^k_i, in each labelled root factor.
    E=[]
    for i,x in enumerate(roots):
        E.append([x**j for j in range(4)]+[F(0)]*4)
        E.append([F(0)]*4+[F(p)**ks[i]*x**j for j in range(4)])
    Ei=inverse(E)
    for col in range(8):
        basis=[F(i==col) for i in range(8)]
        need(mv(E,mv(Ei,basis))==basis,'normalization matrix inverse')
    sv=smith_p(E,p)
    expected=[0,0,0,0,0,0,1,1] if ch=='E' else [0,0,0,1,1,2,2,3]
    need(sv==expected,'complete signed Smith invariants')
    root_eval=[[x**j for j in range(4)] for x in roots]
    root_sv=smith_p(root_eval,p)
    need(root_sv==([0,0,0,1] if ch=='E' else [0,0,1,2]),'complete root Smith invariants')
    conductors=[]
    for i in range(4):
        # The ideal p^e O_i is in the order iff both supported normal basis vectors are.
        found=None
        for e in range(4):
            vectors=[]
            for bit in (0,1):
                v=[F(0)]*8;v[2*i+bit]=F(p)**e;vectors.append(v)
            if all(all(vp(x,p)>=0 for x in mv(Ei,v)) for v in vectors):found=e;break
        need(found is not None,'finite conductor exponent found')
        # Minimality is exact; multiplying supported basis by theta stays in their span.
        exp=(1 if i in (0,3) else 0) if ch=='E' else (0 if i==1 else 3)
        need(found==exp,'labelled signed conductor exponent')
        conductors.append(found)
    # Exact original action, with the same integral basis and no fitted matrix.
    monic=poly_roots(roots);Cmat=[[F(0)]*4 for _ in range(4)]
    for j in range(3):Cmat[j+1][j]=1
    for i in range(4):Cmat[i][3]=-monic[i]
    Dmat=[[F(0)]*4 for _ in range(4)]
    power=[[F(i==j) for j in range(4)] for i in range(4)]
    for coefficient in pder(dat['coefficients']):
        for i in range(4):
            for j in range(4):Dmat[i][j]+=coefficient*power[i][j]
        power=matmul(power,Cmat)
    Tsrc=[[F(0)]*8 for _ in range(8)];Ysrc=[[F(0)]*8 for _ in range(8)]
    for i in range(4):
        for j in range(4):
            Tsrc[i][j]=Tsrc[i+4][j+4]=Cmat[i][j]
            Ysrc[i][j+4]=Dmat[i][j]
        Ysrc[i+4][i]=1
    Tnorm=[[F(0)]*8 for _ in range(8)];Ynorm=[[F(0)]*8 for _ in range(8)]
    for i in range(4):
        scale_p=F(p)**ks[i];delta=ds[i]/scale_p**2
        Tnorm[2*i][2*i]=Tnorm[2*i+1][2*i+1]=roots[i]
        Ynorm[2*i][2*i+1]=scale_p*delta;Ynorm[2*i+1][2*i]=scale_p
    need(matmul(E,Tsrc)==matmul(Tnorm,E),'original T action intertwining')
    need(matmul(E,Ysrc)==matmul(Ynorm,E),'original eta action intertwining')
    module_indices=[]
    for action in (Tnorm,Ynorm):
        power=[[F(i==j) for j in range(8)] for i in range(8)]
        first=None
        for exponent in range(1,5):
            power=matmul(power,action)
            image=matmul(Ei,power)
            if all(vp(z,p)>=0 for row in image for z in row):first=exponent;break
        module_indices.append(first)
    need(module_indices==([1,2] if ch=='E' else [3,3]),'exact nilpotent indices on normalization quotient')
    # The prime-only sign has a nonintegral eta coefficient in the ORIGINAL basis.
    signs=[-1,1,1,1]
    prime_flip_poly=interp(roots,signs)
    need(min(vp(x,p) for x in prime_flip_poly)==(-1 if ch=='E' else -2),
         'prime-sign deck map fails original integral order')
    return dict(state=marking(st),literal=dat,normal_evaluation=E,inverse_evaluation=Ei,
                theta_squares=[d/F(p)**(2*k) for d,k in zip(ds,ks)],
                signed_smith_exponents=sv,root_smith_exponents=root_sv,
                conductor_exponents=conductors,prime_flip_polynomial=prime_flip_poly,
                original_T=Tsrc,original_eta=Ysrc,normal_T=Tnorm,normal_eta=Ynorm,
                quotient_nilpotent_indices_T_eta=module_indices)

def rank_mod(M,p):
    a=[[x%p for x in row] for row in M];r=0
    if not a:return 0
    for j in range(len(a[0])):
        z=next((i for i in range(r,len(a)) if a[i][j]),None)
        if z is None:continue
        a[r],a[z]=a[z],a[r];v=pow(a[r][j],-1,p);a[r]=[x*v%p for x in a[r]]
        for i in range(len(a)):
            if i!=r:
                v=a[i][j];a[i]=[(x-v*y)%p for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return r

def mm(A,B,p):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))%p for j in range(len(B[0]))] for i in range(len(A))]

def nilpotents(p,m,k):
    # epsilon^m=0, eta^2=k epsilon^(m-1), basis epsilon^a eta^b, b=0,1.
    n=2*m;X=[[0]*n for _ in range(n)];Y=[[0]*n for _ in range(n)]
    for b in range(2):
        for a in range(m):
            j=b*m+a
            if a+1<m:X[b*m+a+1][j]=1
            if b==0:Y[m+a][j]=1
            elif a+m-1<m:Y[a+m-1][j]=k%p
    require_xy=mm(X,Y,p)==mm(Y,X,p)
    need(require_xy,'local multiplication commutes')
    ranks=[];A=[[int(i==j) for j in range(n)] for i in range(n)]
    for power in range(5):
        ranks.append(rank_mod(A,p));A=mm(A,Y,p)
    need(ranks==([4,3,2,1,0] if m==2 else [6,4,2,1,0]),'eta Jordan blocks')
    xr=[];A=[[int(i==j) for j in range(n)] for i in range(n)]
    for power in range(m+1):xr.append(rank_mod(A,p));A=mm(A,X,p)
    need(xr==[2*(m-i) for i in range(m+1)],'epsilon two Jordan blocks')
    return dict(p=p,m=m,coefficient=k,epsilon_matrix=X,eta_matrix=Y,eta_ranks=ranks,epsilon_ranks=xr)

def boundary_certificate():
    p=13;st=state(p,4,2,'E');data=literal(p,st['denominators'],'E')
    f=data['coefficients'];fp=pder(f);counts={}
    for e in (2,3):
        modulus=p**e
        fc=[mod(c,modulus) for c in f];dc=[mod(c,modulus) for c in fp]
        def evalmod(cs,t):
            z=0
            for x in reversed(cs):z=(z*t+x)%modulus
            return z
        count=0
        for t in range(0,modulus,p):
            if evalmod(fc,t):continue
            d=evalmod(dc,t)
            for eta in range(0,modulus,p):
                if (eta*eta-d)%modulus==0:count+=1
        counts[str(e)]=count
    need(counts=={'2':p,'3':0},'sharp E boundary lift obstruction')
    x,y=data['roots'][1:3];S=data['S']
    mean=5*pow(8,-1,p)%p
    unit=mod(peval(f,p*mean)/p**2,p)
    need(unit==mod(F(9)*x*y/(64*S),p) and unit!=0,'nonzero third-digit obstruction')
    g0=mod(-x*y/S,p)
    return dict(state=marking(st),counts=counts,second_digit=mean,third_digit_obstruction=unit,
                E_special=nilpotents(p,2,2*g0),M_special=nilpotents(p,3,3))

def comparison(E,M):
    need(E['p']==M['p'] and E['channel']=='E' and M['channel']=='M','comparison labels')
    p=E['p'];e=literal(p,E['denominators'],'E');m=literal(p,M['denominators'],'M')
    Fwd=interp(e['roots'],m['roots']);Rev=interp(m['roots'],e['roots'])
    need([peval(Fwd,x) for x in e['roots']]==m['roots'],'labelled forward evaluation')
    need([peval(Rev,x) for x in m['roots']]==e['roots'],'labelled reverse evaluation')
    need(min(vp(x,p) for x in Fwd)>=0 and min(vp(x,p) for x in Rev)==-2,'literal comparison denominator')
    revmod=[mod(p*p*x,p) for x in Rev]
    constant=revmod[3]
    need(constant!=0 and revmod==[0,0,(-constant*M['a'])%p,constant],
         'literal comparison exact p-squared correction')
    return dict(E=marking(E),M=marking(M),forward=Fwd,reverse=Rev,p_squared_reverse_mod_p=revmod)

def reciprocal(data,p):
    roots=data['roots'];D,C,B,_,A=data['coefficients'];N=prod(roots);S=sum(roots)
    I=pscale([C,B,1,A],-F(p)/D)
    z=[F(p)/x for x in roots]
    need([peval(I,x) for x in roots]==z,'literal reciprocal root inverse')
    need(min(vp(x,p) for x in I)==(-1 if data['channel']=='E' else -2),'reciprocal exact denominator')
    g=pscale(poly_roots(z),-F(1,5));d=[peval(pder(g),x) for x in z]
    omega=-F(p**3)*S/(5*N)
    need(all(dd==omega*dl/(x*x) for dd,dl,x in zip(d,data['derivatives'],roots)),
         'reciprocal signed quadratic twist')
    disc=g[-1]**6*prod((z[i]-z[j])**2 for i in range(4) for j in range(i))
    need(vp(disc,p)==vp(data['discriminant'],p)+12-6*vp(N,p),'reciprocal discriminant valuation')
    return dict(roots=z,polynomial=g,reciprocal_map=I,twist=omega,twist_valuation=vp(omega,p),
                discriminant_valuation=vp(disc,p))

def crt(pairs):
    a=0;n=1
    for b,m in pairs:
        if gcd(n,m)!=1:raise ValueError('coprime CRT moduli required')
        a+=n*((b-a)*pow(n,-1,m)%m);n*=m;a%=n
    return a,n

def rational_control(p,small=(2,3,5,7,11),bad=13):
    need(isprime(p) and p%840==1 and p%bad==1 and p%11==10,'control prime progression')
    need(all(isprime(q) and q!=p and q!=bad for q in small) and isprime(bad) and bad>=13,'control prime places')
    budget=bad*bad*prod(small)
    need(p*p>=128*budget and p>max(small,default=1),'control quantitative threshold')
    a=(p+3)//4
    pairs=[(3,p)]+[(1 if a%q==0 else 0,q) for q in small]
    pairs.append(((a+bad)*pow(3,-1,bad*bad)%(bad*bad),bad*bad))
    b,modulus=crt(pairs);need(modulus==p*budget,'control full CRT modulus')
    b+=modulus;c=F(a*b,3*b-a);den=[F(a),F(p*b),p*c]
    need(sum((1/z for z in den),F(0))==F(4,p),'positive rational control identity')
    need(F(a,3)<c<F(a,2) and a<p<den[2]<den[1],'control positivity and original real order')
    need(all(vp(x,q)>=0 for x in den for q in list(small)+[p]),'all declared local denominators integral')
    need(vp(den[2],bad)==-1 and den[2].denominator>1,'exact omitted-prime denominator')
    need(vp(3*b-a,bad)==1 and vp(a*b,bad)==0,'bad-prime cancellation excluded')
    data=literal(p,den,'M')
    need(data['derivative_unit_symbols']==[-1,1,-1,1] and data['rational_local_points']==4,
         'control identical M local signature')
    roots=data['roots'];S=data['S'];sp=F(p*p+3*p,4);Bp=p+sp*(sp+1)
    need(S<Bp and max(den)<=sp*(sp+1)/3,'all inherited scalar height inequalities')
    ordered=sorted(roots)
    need(all(ordered[i+1]-ordered[i]>=1 for i in range(3)),'literal real root gaps')
    need(data['discriminant']>=F(144)/Bp**6,'inherited discriminant separation')
    need(all(F(2)/S<=abs(d)<=S*S for d in data['derivatives']),'inherited derivative separation')
    endpoint=state(p,(p+11)//4,(p+11)//4,'E')
    return dict(p=p,places=list(small),omitted_prime=bad,budget=budget,CRT=pairs,
                a=a,b=b,c=c,denominators=den,denominator_bad_valuation=-1,
                literal=data,height_bound=Bp,known_original_solution=marking(endpoint),
                claim='Rational target, not a positive integral ES state; p itself has the recorded original solution.')

def foreign_prime_control(p,ell=23,places=(2,3,5,7,11)):
    """One unavailable prime occurrence; both numerical gates still pass."""
    need(isprime(p) and isprime(ell) and ell%12==11 and p%840==1 and p%ell==ell-1,
         'single-prime control progression')
    need(p>4*ell and ell not in places,'single-prime range and omitted place')
    a=(p+3)//4;u=a*ell;h=F(a,ell);r=ell;s=1
    k=(p*ell+1)//3;lam=(ell+1)//3
    need(0<u<a*a and (u+a)%3==0 and (4*u+1)%3==0,'both gates and original numerical range')
    need(gcd(a,u)==a and gcd(a,ell)==1 and a*a%u!=0,'one missing original exponent')
    need(h*r*s==a and h*r*r==u and gcd(r,s)==1,'all rational normalization identities')
    need(h.denominator==ell and r<a and s<a and lam<p,'only grade integrality is lost')
    out=dict(p=p,omitted_prime=ell,places=list(places),a=a,u=u,R=3,h=h,r=r,s=s,
             kappa=k,lambda_value=lam,is_original_state=False,
             failed_original_condition='u does not divide a^2; its only extra prime occurrence is ell',
             original_a_factorization=factor(a),candidate_u_factorization=factor(u),targets={})
    sp=p*a;Bp=p+sp*(sp+1)
    for ch,den in [('E',[F(a),h*k,F(p*a*k)]),('M',[F(a),p*h*lam,F(p*a*lam)])]:
        need(sum((1/x for x in den),F(0))==F(4,p),'joint rational control identity')
        need(den[1].denominator==ell and den[0].denominator==den[2].denominator==1,
             'one and only one denominator prime is missing')
        need(all(vp(x,q)>=0 for x in den for q in list(places)+[p]),'joint control local integrality')
        need(all(vp(F(a*a,u),q)>=0 for q in list(places)+[p]),'local original divisor condition')
        data=literal(p,den,ch);roots=data['roots'];S=sum(roots)
        need(S<Bp and max(den)<F(sp*(sp+1),3),'full original scalar size bounds for both gates')
        sorted_roots=sorted(roots)
        need(all(sorted_roots[i+1]-sorted_roots[i]>1 for i in range(3)),'joint control separated literal roots')
        need(data['discriminant']>=F(144,Bp**6),'joint control discriminant bound')
        need(all(F(2,S)<=abs(d)<=S*S for d in data['derivatives']),'joint control derivative bounds')
        out['targets'][ch]=dict(denominators=den,literal=data)
    e=state(p,(p+ell)//4,(p+ell)//4,'E')
    j=(ell+1)//4;c=(p+1)//ell
    m=state(p,j*c,j,'M')
    out['known_original_E']=marking(e);out['known_original_M']=marking(m)
    out['height_bound']=Bp
    return out

def fixtures():
    out={};orders=[]
    cases=[('E_zero',1009,253,11,'E'),('E_four',1009,253,23,'E'),
           ('M_eight',1009,253,11,'M'),('M_four',1009,253,23,'M')]
    for name,p,a,u,ch in cases:
        need(isprime(p),'fixture primality by trial division')
        st=state(p,a,u,ch);cert=order_certificate(st)
        out[name]=dict(state=marking(st),literal=cert['literal'],reciprocal=reciprocal(cert['literal'],p))
        orders.append(cert)
    E=state(825241,206321,2240439739,'E');M=state(825241,217170,25,'M')
    need(isprime(825241) and 825241%840 in HARD,'inherited crossing prime')
    need(E['h']==19 and E['alpha']==-24 and M['u']==25,'inherited noncanonical capacity crossing')
    out['capacity_crossing']=comparison(E,M)
    out['small_comparison']=comparison(state(1009,253,11,'E'),state(1009,253,11,'M'))
    out['boundary']=boundary_certificate()
    prime_controls=[]
    for p in range(87361,87361+120120*25,120120):
        if isprime(p) and p*p>=128*390390:
            prime_controls.append(rational_control(p))
            if len(prime_controls)==3:break
    need(len(prime_controls)==3,'three exact control primes found in finite search')
    out['finite_place_controls']=prime_controls
    out['single_foreign_prime_controls']=[foreign_prime_control(p) for p in (35281,54601)]
    need(out['single_foreign_prime_controls'][0]['u']==202883,'single forbidden exponent fixture')
    printed=out['single_foreign_prime_controls'][0]['targets']
    need(printed['E']['denominators']==[F(8821),F(2385974648,23),F(84179571556088)],'IC35 printed E triple')
    need(printed['M']['denominators']==[F(8821),F(2489709608,23),F(2489709608)],'IC35 printed M triple')
    need((printed['E']['literal']['rational_local_points'],printed['M']['literal']['rational_local_points'])==(0,4),'IC35 printed point counts')
    # Exact negative controls, each addresses a distinct false inference.
    need(out['E_zero']['literal']['rational_local_points']==0,'reject literal-cover rational-point necessity')
    need(out['M_eight']['literal']['rational_local_points']==8,'reject reciprocal-cubic point-count substitution')
    need(orders[0]['signed_smith_exponents']!=orders[2]['signed_smith_exponents'],'reject rank equality as integral equality')
    need(out['boundary']['counts']['2']>0 and out['boundary']['counts']['3']==0,'reject unsmooth Hensel inference')
    need(out['boundary']['M_special']['eta_ranks']!=[6,5,4,3,2],'reject triple block as one length-six chain')
    need(vp(out['small_comparison']['reverse'][-1],1009)==-2,'reject unit rational inverse')
    need(prime_controls[0]['denominators'][2].denominator!=1,'reject finite-place plus height integrality')
    need(vp(out['E_zero']['reciprocal']['twist'],1009)==1,'reject untwisted signed reciprocal identification')
    return out,orders

def full_scan(bound):
    rows=[];vectors=0;states=0;counts=Counter()
    for p in primes_to(bound):
        if p%12!=1:continue
        row=[];nv=0
        for a in range(p//4+1,(p+1)//2):
            R=4*a-p
            for u in square_divisors(a):
                nv+=1
                for ch,hit in [('E',(4*u+1)%R==0),('M',(u+a)%R==0)]:
                    if not hit:continue
                    st=state(p,a,u,ch);dat=literal(p,st['denominators'],ch)
                    row.append([ch,a,u,R,st['h'],st['r'],st['s'],st['quotient'],
                                st['denominators'],dat['derivative_valuations'],dat['derivative_unit_symbols'],
                                dat['rational_local_points']])
                    counts[ch]+=1;counts[ch+'_Qp_'+str(dat['rational_local_points'])]+=1
        rows.append(dict(p=p,original_vectors=nv,states=sorted(row)))
        vectors+=nv;states+=len(row)
    return dict(bound=bound,domain='primes p == 1 mod 12; complete original first-half E/M boxes',
                rows=rows,original_vectors=vectors,states=states,counts=dict(counts))

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--bound',type=int,default=3000)
    parser.add_argument('--out',type=Path,default=Path('certificates'))
    args=parser.parse_args()
    if args.bound<13:parser.error('bound must be at least 13')
    start=time.monotonic();args.out.mkdir(parents=True,exist_ok=True)
    scan=full_scan(args.bound);examples,orders=fixtures()
    for name,data in [('scan.json',scan),('examples.json',examples),('orders.json',orders)]:
        (args.out/name).write_text(json.dumps(enc(data),indent=2,sort_keys=True)+'\n')
    summary=dict(success=True,bound=args.bound,primes=len(scan['rows']),original_vectors=scan['original_vectors'],
                 counts=scan['counts'],checks=sum(CHECK.values()),check_types=dict(CHECK),
                 elapsed_seconds=time.monotonic()-start,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                 scan_sha256=sha(scan),universal_ES_proved=False,novelty_claim=False,
                 scope='Exact local specialization, finite certificates, and written global statements. Finite scan is not universal occupancy.')
    (args.out/'summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
    print(json.dumps(summary,indent=2,sort_keys=True))

if __name__=='__main__':main()
