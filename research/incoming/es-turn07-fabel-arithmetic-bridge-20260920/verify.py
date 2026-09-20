#!/usr/bin/env python3
"""Exact reciprocal-cubic Fabel fibres and original negative-square E/M returns.
Python standard library only. Finite replay is not universal ES occupancy.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import permutations
from math import gcd,isqrt
from pathlib import Path
import argparse,hashlib,json,time
CHECK=Counter(); HARD={1,121,169,289,361,529}
def need(v,label):
    CHECK[label]+=1
    if not v: raise ArithmeticError(label)
def primes_to(n):
    b=bytearray(b'\1')*(n+1);b[:2]=b'\0\0'
    for q in range(2,isqrt(n)+1):
        if b[q]:b[q*q:n+1:q]=b'\0'*((n-q*q)//q+1)
    return [q for q in range(2,n+1) if b[q]]
@lru_cache(maxsize=100000)
def factor(n):
    if n<1:raise ValueError('positive factor input required')
    z=[];q=2
    while q*q<=n:
        if n%q==0:
            e=0
            while n%q==0:n//=q;e+=1
            z.append((q,e))
        q=3 if q==2 else q+2
    if n>1:z.append((n,1))
    return tuple(z)
@lru_cache(maxsize=50000)
def divisors(n,square=False):
    a=[1]
    for q,e in factor(n):a=[d*q**j for d in a for j in range((2 if square else 1)*e+1)]
    return tuple(sorted(a))
def prime(n):return n>=2 and factor(n)==((n,1),)
def vp_int(n,p):
    if n==0:raise ValueError('valuation of zero is not a finite integer')
    n=abs(n);e=0
    while n%p==0:n//=p;e+=1
    return e
def vp(x,p):
    x=F(x);return vp_int(x.numerator,p)-vp_int(x.denominator,p)
def residue(x,m):
    x=F(x);return x.numerator*pow(x.denominator,-1,m)%m
def leg(x,p):
    z=pow(residue(x,p),(p-1)//2,p)
    return 0 if z==0 else (1 if z==1 else -1)
def enc(x):
    if isinstance(x,F):return [x.numerator,x.denominator]
    if isinstance(x,dict):return {k:enc(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [enc(v) for v in x]
    return x

def state(p,a,u,ch):
    R=4*a-p
    need(p%4==1 and p<4*a and 2*a<p,'original prime-class and shell domain')
    need(u>0 and a*a%u==0,'original square divisor')
    need((4*u+1)%R==0 if ch=='E' else (u+a)%R==0,'original labelled gate')
    g=gcd(a,u);h=g*g//u;r=u//g;s=a//g
    need(h*r*s==a and h*r*r==u and gcd(r,s)==1,'original normalization')
    k=(p*r+s)//R if ch=='E' else (r+s)//R
    need(R*k==(p*r+s if ch=='E' else r+s),'original quotient integer')
    xyz=(a,h*s*k,p*h*r*k) if ch=='E' else (a,p*h*s*k,p*h*r*k)
    x,y,z=xyz
    need(4*x*y*z==p*(x*y+x*z+y*z),'ordered Egyptian identity')
    num=a*a if ch=='E' else p*a*a
    need(num%(R*y-p*a)==0 and num//(R*y-p*a)==u,'ordered divisor inverse')
    need(len(set(xyz))==3,'no repeated denominators in original prime source')
    need(gcd(p,h*r*s*k)==1,'all normalization factors are p-units')
    st=dict(p=p,a=a,R=R,u=u,channel=ch,h=h,r=r,s=s,k=k,denominators=list(xyz))
    if ch=='E':
        v=a*a//u;D=(4*u+1)//R
        st.update(v=v,D=D,alpha=v-R,beta=v-D)
        need(leg(h,p)==-1,'exterior nonresidue grade')
        need((k-r)%p!=0 and D%p!=0,'exterior differences stay p-units')
    return st

def local(st):
    p=st['p'];t=[F(p,x) for x in st['denominators']]
    d=[(t[i]-t[(i+1)%3])*(t[i]-t[(i+2)%3]) for i in range(3)]
    s2=t[0]*t[1]+t[0]*t[2]+t[1]*t[2];s3=t[0]*t[1]*t[2]
    disc=(t[0]-t[1])**2*(t[0]-t[2])**2*(t[1]-t[2])**2
    need(sum(t)==4 and t[0]>2 and all(0<x<2 for x in t[1:]),'original positive reciprocal roots')
    need(d[0]*d[1]*d[2]==-disc,'derivative product sign')
    vals=[vp(x,p) for x in d]
    if st['channel']=='E':
        need(vals==[1,1,0],'E exact derivative valuations')
        need([residue(x,p) for x in t]==[0,0,4],'E two colliding reciprocal roots')
        need(vp(s2,p)==1 and vp(s3,p)==2 and vp(disc,p)==2,'E coefficient valuation stratum')
        need(residue(d[0]/d[1],p)==p-1,'two ramified factors have square ratio')
        need(residue(d[2],p)==16%p,'third E derivative is square unit')
        signs=[leg(d[0]/p,p),leg(d[1]/p,p),leg(d[2],p)]
        alg='Qp^3 x ramified_quadratic^2';npoints=3
    else:
        need(vals==[0,0,0] and vp(disc,p)==0,'M unramified reduction')
        signs=[leg(x,p) for x in d]
        need(leg(st['r']*st['s'],p)==-1,'middle opposite original factor characters')
        need(signs[0]==-1 and signs.count(1)==1,'M exactly one finite split factor')
        npoints=3
        alg='Qp^3 x unramified_quadratic^2'
    return dict(roots=t,derivatives=d,target=[F(0),F(-4),s2,-s3],discriminant=disc,
                derivative_valuations=vals,unit_characters=signs,
                qp_points=npoints,geometric_affine_points=7,algebra=alg)

def marked(st):
    z=dict(st);fs=factor(st['a']);fu=dict(factor(st['u']))
    z['a_factorization']=[list(t) for t in fs]
    z['centered_exponents']=[[q,fu.get(q,0)-e] for q,e in fs]
    z['exponent_box']=[[q,-e,e] for q,e in fs]
    z['fibre']=enc(local(st));return z

# Exact four-dimensional algebra, allowing reducible quadratic polynomials.
class Ring:
    __slots__=('d','c')
    def __init__(self,d,c=0):
        self.d=F(d)
        if isinstance(c,Ring):
            if c.d!=self.d:raise ValueError('different algebras')
            self.c=c.c
        elif isinstance(c,(tuple,list)):
            if len(c)!=4:raise ValueError('four coefficients')
            self.c=tuple(F(x) for x in c)
        else:self.c=(F(c),F(0),F(0),F(0))
    def __add__(self,o):
        if isinstance(o,Jet):return NotImplemented
        o=Ring(self.d,o);return Ring(self.d,[a+b for a,b in zip(self.c,o.c)])
    __radd__=__add__
    def __neg__(self):return Ring(self.d,[-a for a in self.c])
    def __sub__(self,o):return self+-Ring(self.d,o)
    def __rsub__(self,o):return Ring(self.d,o)+-self
    def __mul__(self,o):
        if isinstance(o,Jet):return NotImplemented
        o=Ring(self.d,o);z=[F(0)]*4
        for j,a in enumerate(self.c):
            for k,b in enumerate(o.c):
                scalar=(-1 if (j&k&1) else 1)*(1/self.d if (j&k&2) else 1)
                z[j^k]+=a*b*scalar
        return Ring(self.d,z)
    __rmul__=__mul__
    def __pow__(self,n):
        if n<0:raise ValueError('negative power')
        z=Ring(self.d,1);a=self
        while n:
            if n&1:z=z*a
            a=a*a;n//=2
        return z
    def __eq__(self,o):
        try:return self.c==Ring(self.d,o).c
        except (ValueError,TypeError):return False
class Jet:
    def __init__(self,v,der):self.v=v;self.der=tuple(der)
    def lift(self,o):return o if isinstance(o,Jet) else Jet(self.v*0+o,[self.v*0]*4)
    def __add__(self,o):
        o=self.lift(o);return Jet(self.v+o.v,[a+b for a,b in zip(self.der,o.der)])
    __radd__=__add__
    def __neg__(self):return Jet(-self.v,[-a for a in self.der])
    def __sub__(self,o):return self+-self.lift(o)
    def __rsub__(self,o):return self.lift(o)+-self
    def __mul__(self,o):
        o=self.lift(o);return Jet(self.v*o.v,[a*o.v+self.v*b for a,b in zip(self.der,o.der)])
    __rmul__=__mul__
    def __pow__(self,n):
        z=self.lift(1)
        for _ in range(n):z=z*self
        return z

def P(q,I):
    A,y,z,w=q
    return (A**3*z+A**2*y*2-A*I,
    -A**3*y**2*z-A**2*y*z*(2*I)+A**2*w-A**2*y**3*2-A*y**2*(10*I)+A*z*3+y,
    A**3*y**3*z*2+A**2*y**2*z*(6*I)+A**2*w*y*2+A**2*y**4*4+A*w*(2*I)-A*y**3*(4*I)-A*y*z*2+z*(2*I)+y**2*7,
    A**3*y**4*z*2+A**2*y**3*z*(8*I)+A**2*w*y**2+A**2*y**5*4+A*w*y*(2*I)+A*y**4*(7*I)-A*y**2*z*10-y*z*(4*I)-w-y**3*3)

def det4(M):
    z=M[0][0]*0
    for perm in permutations(range(4)):
        s=(-1)**sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
        v=M[0][0]*0+s
        for i in range(4):v=v*M[i][perm[i]]
        z=z+v
    return z

def exact_fibres(st):
    f=local(st);target=f['target'];out=[]
    for j,(t,d) in enumerate(zip(f['roots'],f['derivatives'])):
        for sign in (1,-1):
            I=Ring(d,[0,1,0,0]);A=Ring(d,[0,0,sign,0]);ia=d*A
            q=(A,-t-I*ia,2*t*ia+3*I*ia**2,7*I*t*t*ia+(-4-17*t)*ia**2-13*I*ia**3)
            need(all(a==b for a,b in zip(P(q,I),target)),'literal Fabel polynomial signed inverse')
            b=I+A*q[1]
            need(-b*ia==t and A*A*d==1,'root and resultant inverse')
            J=[Jet(v,[Ring(d,int(i==k)) for k in range(4)]) for i,v in enumerate(q)]
            need(det4([x.der for x in P(J,I)])==-2,'original four-dimensional Jacobian sign')
            out.append(dict(root=j,sign=sign,d=enc(d),basis=['1','i','A','iA'],coordinates=[enc(v.c) for v in q]))
    I=Ring(1,[0,1,0,0]);u0,u2,u3,u4=target
    q=(Ring(1,0),Ring(1,u2),I*(7*u2*u2-u3)*F(1,2),Ring(1,11*u2**3-2*u2*u3-u4))
    need(all(a==b for a,b in zip(P(q,I),target)),'unique infinity chart inverse')
    jets=[Jet(v,[Ring(1,int(i==k)) for k in range(4)]) for i,v in enumerate(q)]
    need(det4([x.der for x in P(jets,I)])==-2,'original Jacobian at infinity chart point')
    out.append(dict(root='infinity',sign='b=i only',basis=['1','i','A','iA'],coordinates=[enc(v.c) for v in q]))
    return out

def hensel_sqrt(x,p,n):
    x=F(x);b=next((j for j in range(1,p) if j*j%p==residue(x,p)),None)
    if b is None:raise ValueError('nonsquare unit')
    mod=p
    for _ in range(1,n):
        err=(b*b-residue(x,mod*p))//mod
        b+=mod*((-err*pow(2*b,-1,p))%p);mod*=p
        need((b*b-residue(x,mod))%mod==0,'Hensel original digit')
    return b,mod

def integral_fibres(st,n=4):
    p=st['p'];f=local(st);ii,mod=hensel_sqrt(-1,p,n);out=[]
    for j,(t,d) in enumerate(zip(f['roots'],f['derivatives'])):
        if vp(d,p)!=0 or leg(d,p)!=1:continue
        A0,_=hensel_sqrt(1/d,p,n);rr=residue(t,mod);target=[residue(v,mod) for v in f['target']]
        for A in (A0,(-A0)%mod):
            ia=pow(A,-1,mod)
            q=[A,(-rr-ii*ia)%mod,(2*rr*ia+3*ii*ia**2)%mod,
               (7*ii*rr*rr*ia+(-4-17*rr)*ia**2-13*ii*ia**3)%mod]
            need([v%mod for v in P(q,ii)]==target,'full integral inverse modulo p power')
            out.append(dict(root=j,coordinates=q))
    need(len(out)+1==f['qp_points'],'all integral Qp branches retained')
    return dict(p=p,precision=n,modulus=mod,i_embedding=ii,finite_points=out,
                infinity_point=enc(exact_infinity(f['target'])))

def exact_infinity(target):
    _,u2,u3,u4=target
    return [0,u2,[0,(7*u2*u2-u3)/2],11*u2**3-2*u2*u3-u4]

def square_cross(st,side,c):
    need(st['channel']=='E' and st[side]==-4*c*c,'actual negative-square source')
    p,h=st['p'],st['h'];j=(h+1)//4
    need(h%4==3 and gcd(c,h)==1,'forced cofactor residue and units')
    if j%c:return None
    U=c*c if side=='alpha' else (j//c)**2
    need(j*j%U==0 and (p+4*U)%h==0,'actual cofactor square divisor and gate')
    R=(p+4*U)//h;a=(p+R)//4
    need(0<R<p and R%4==3,'middle first-half cofactor return')
    M=state(p,a,U,'M')
    g=gcd(j,U)
    need((g*g//U,U//g,R*(j//g)-U//g,j//g)==(M['h'],M['r'],M['s'],M['k']),'new prime-exponent normalization')
    need(4*M['h']*M['r']*M['k']-1==h,'original grade becomes middle cofactor')
    return M

def candidate_crosses(st):
    rows=[]
    if st['channel']!='E':return rows
    for side in ('alpha','beta'):
        z=-st[side]
        if z>0 and z%4==0:
            c=isqrt(z//4)
            if 4*c*c==z:
                out=square_cross(st,side,c)
                rows.append(dict(side=side,c=c,j=(st['h']+1)//4,
                                 available=out is not None,
                                 target=None if out is None else compact(out)))
    return rows

def inverse_source_fibre(p,h,c,side):
    out=[]
    if side=='alpha':
        need((p+4*c*c)%h==0,'alpha fibre phase')
        N=(p+4*c*c)//h
        for s in divisors(N):
            k=N//s
            if (s+k)%4:continue
            r=(s+k)//4;a=h*r*s;R=4*a-p;u=h*r*r
            if gcd(r,s)!=1 or not(p<4*a and 2*a<p) or (4*u+1)%R:continue
            e=state(p,a,u,'E')
            need(e['h']==h and e['alpha']==-4*c*c,'alpha exact fibre')
            out.append(compact(e))
    else:
        need((4*c*c*p+1)%h==0,'beta fibre phase')
        F0=(4*c*c*p+1)//h
        for s in range(1,(p-1)//(2*h)+1):
            D=h*s*s+4*c*c;delta=s*s*(D*D-p)-F0
            if delta<=0:continue
            k=isqrt(delta)
            if k*k!=delta or (s*D-k)%2:continue
            r=(s*D-k)//2
            if r<=0 or gcd(r,s)!=1:continue
            a=h*r*s
            if not(p<4*a and 2*a<p):continue
            u=h*r*r;R=4*a-p
            if (4*u+1)%R:continue
            e=state(p,a,u,'E')
            need(e['h']==h and e['beta']==-4*c*c,'beta exact fibre')
            out.append(compact(e))
    return sorted(out)

COLUMNS=['channel','a','u','R','h','r','s','k','x','y','z']
def compact(st):return [st['channel'],st['a'],st['u'],st['R'],st['h'],st['r'],st['s'],st['k']]+st['denominators']
def scan(bound):
    rows=[];tot=Counter()
    for p in primes_to(bound):
        if p%4!=1:continue
        arr=[];cross=[];ct=Counter();sources=[]
        for a in range(p//4+1,(p-1)//2+1):
            fs=factor(a);vv=divisors(a,True);ct['divisor_vectors']+=len(vv)
            sources.append([a,[list(x) for x in fs]])
            R=4*a-p
            for u in vv:
                for ch,hit in [('E',(4*u+1)%R==0),('M',(u+a)%R==0)]:
                    if not hit:continue
                    st=state(p,a,u,ch);data=local(st)
                    arr.append(compact(st));ct[ch]+=1;ct[data['algebra']]+=1
                    for z in candidate_crosses(st):
                        ct['square_'+z['side']+('_pass' if z['available'] else '_blocked')]+=1
                        cross.append(dict(source=compact(st),**z))
        rows.append(dict(p=p,hard=p%840 in HARD,source_factorizations=sources,
                         states=sorted(arr),crosses=cross,counts=dict(ct)))
        tot.update(ct)
    return dict(bound=bound,prime_domain='all primes p == 1 mod 4',columns=COLUMNS,rows=rows,totals=dict(tot))

def interpolation(xs,ys):
    coeff=[F(0),F(0),F(0)]
    for i in range(3):
        z=[xs[j] for j in range(3) if j!=i]
        d=(xs[i]-z[0])*(xs[i]-z[1])
        for k,v in enumerate((z[0]*z[1],-z[0]-z[1],F(1))):coeff[k]+=ys[i]*v/d
    return coeff

def root_order_map(source,target):
    p=source['p'];need(target['p']==p and source['channel']=='E' and target['channel']=='M','same-prime order transition')
    x=local(source)['roots'];y=local(target)['roots']
    ff=interpolation(x,y);gg=interpolation(y,x)
    for xx,yy in zip(x,y):
        need(sum(ff[k]*xx**k for k in range(3))==yy,'exact forward root interpolation')
        need(sum(gg[k]*yy**k for k in range(3))==xx,'exact backward root interpolation')
    need([vp(c,p) for c in ff]==[0,-1,-1],'sharp forward p-denominator')
    need(all(c==0 or vp(c,p)>=0 for c in gg),'integral reverse polynomial')
    need(vp(gg[1],p)==vp(gg[2],p)==0 and (gg[0]==0 or vp(gg[0],p)>=1),'reverse collapse coefficients')
    ffbar=[residue(p*c,p) for c in ff]
    need(ffbar[0]==0 and ffbar[1]==(-4*ffbar[2])%p and ffbar[2]!=0,'p times forward polynomial has exact T(T-4) reduction')
    vv=lambda rr:(rr[1]-rr[0])*(rr[2]-rr[0])*(rr[2]-rr[1])
    need(vp(vv(x),p)==1 and vp(vv(y),p)==0,'original root-order indices')
    # Integral points in the order are exactly values congruent in slots 1 and 2.
    for u,v,w in ((0,0,1),(1,1,0),(p,0,0),(0,p,0),(1,1+p,2)):
        cc=interpolation(x,[F(u),F(v),F(w)])
        need(all(c==0 or vp(c,p)>=0 for c in cc),'conductor-compatible integral tuple')
    return enc(dict(p=p,source=compact(source),target=compact(target),forward_coefficients=ff,
                    inverse_coefficients=gg,forward_p_valuations=[0,-1,-1],
                    p_forward_reduction=ffbar,source_order_index=p,target_order_index=1,
                    source_conductor_exponents=[1,1,0],root_Vandermonde_determinants=[vv(x),vv(y)]))

def examples():
    specs=[(5,2,2,'E'),(5,2,1,'M'),(5209,1330,18620,'E'),(4561,1593,43011,'E'),(3049,806,20956,'E'),
           (3361,990,17820,'E'),(1129,286,7436,'E'),(26881,8976,430848,'E'),
           (1009,276,9,'M'),(2521,636,8,'M')]
    states=[];algebra_examples={};crosses=[];fibres=[];orders=[]
    for p,a,u,ch in specs:
        need(prime(p),'displayed exact primality')
        st=state(p,a,u,ch);states.append(marked(st))
        for c in candidate_crosses(st):
            crosses.append(dict(source=compact(st),**c))
            fibre=inverse_source_fibre(p,st['h'],c['c'],c['side'])
            need(compact(st) in fibre,'original source in full inverse fibre')
            fibres.append(dict(p=p,h=st['h'],side=c['side'],c=c['c'],states=fibre))
            if c['available']:
                M=state(p,c['target'][1],c['target'][2],'M')
                states.append(marked(M));algebra_examples.setdefault(local(M)['algebra'],M)
                orders.append(root_order_map(st,M))
        algebra_examples.setdefault(local(st)['algebra'],st)
    # Find a small original M state exhibiting each local split type, without assuming it.
    for p in primes_to(100):
        if p%4!=1:continue
        for a in range(p//4+1,(p-1)//2+1):
            for u in divisors(a,True):
                if (u+a)%(4*a-p):continue
                st=state(p,a,u,'M');algebra_examples.setdefault(local(st)['algebra'],st)
    need(set(algebra_examples)=={'Qp^3 x unramified_quadratic^2','Qp^3 x ramified_quadratic^2'},'both actual local algebras exhibited')
    fabel=[]
    for key,st in sorted(algebra_examples.items()):
        fabel.append(dict(kind=key,source=marked(st),exact_branches=exact_fibres(st),
                          integral_branches=integral_fibres(st)))
    toy=root_order_map(state(5,2,2,'E'),state(5,2,1,'M'))
    need(toy['forward_coefficients']==[[17,12],[-19,10],[14,15]],'explicit rational forward map')
    need(toy['inverse_coefficients']==[[25,8],[-37,8],[7,4]],'explicit integral reverse map')
    orders.append(toy)
    p=3049;h=31;j=8
    blocked=[dict(u=u,residue=(p+4*u)%h) for u in divisors(j,True)]
    need(all(x['residue'] for x in blocked),'entire blocked cofactor box empty')
    # Same-prime positive repair exists at a different original divisor.
    repair=marked(state(p,770,5,'M'))
    I=Ring(1,[0,1,0,0]);q=(Ring(1,0),Ring(1,-4),56*I,Ring(1,-705))
    need(all(x==v for x,v in zip(P(q,I),[0,-4,0,1])),'non-ES target has infinity inverse')
    need(all(r**3-4*r*r+1!=0 for r in (-1,1)),'rational root theorem obstruction')
    return dict(states=states,crosses=crosses,inverse_fibres=fibres,local_algebras=fabel,root_order_transitions=orders,
                full_blocked_cofactor=dict(p=p,Q=h,j=j,rows=blocked,canonical_unavailable_u=36),
                alternate_middle=repair,non_ES_target=dict(coefficients=[0,-4,0,1],
                rational_root_candidates=[-1,1],infinity=[['0'],['-4'],['56i'],['-705']]))

def negative_controls(ex):
    rejected=[]
    tests=[('seven_points_are_eight',7==8),
           ('three_Qp_points_determine_ramification',len({z['kind'] for z in ex['local_algebras'] if z['source']['fibre']['qp_points']==3})==1),
           ('negative_square_supplies_its_unavailable_word',64%36==0),
           ('blocked_cofactor_has_a_different_word',any(r['residue']==0 for r in ex['full_blocked_cofactor']['rows'])),
           ('infinity_inverse_forces_rational_reciprocals',any(r**3-4*r*r+1==0 for r in (-1,1))),
           ('ramified_inverse_has_integral_first_coordinate',F(-1,2)>=0)]
    for name,value in tests:
        need(not value,'reject '+name);rejected.append(name)
    return rejected

def canonical(v):return json.dumps(v,sort_keys=True,separators=(',',':')).encode()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--bound',type=int,default=3000)
    ap.add_argument('--out',type=Path,default=Path('certificates'));args=ap.parse_args()
    if args.bound<100:ap.error('bound at least 100')
    args.out.mkdir(parents=True,exist_ok=True);start=time.monotonic()
    sc=scan(args.bound);ex=examples();neg=negative_controls(ex)
    for name,v in [('scan.json',sc),('examples.json',ex)]:
        (args.out/name).write_text(json.dumps(enc(v),indent=2,sort_keys=True)+'\n')
    report=dict(success=True,bound=args.bound,primes=len(sc['rows']),totals=sc['totals'],
                checks=sum(CHECK.values()),check_types=dict(CHECK),rejected=neg,
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                output_sha256={n:hashlib.sha256((args.out/n).read_bytes()).hexdigest() for n in ('scan.json','examples.json')},
                universal_ES_proved=False,elapsed_seconds=time.monotonic()-start)
    (args.out/'report.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
