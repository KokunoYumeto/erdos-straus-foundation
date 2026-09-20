#!/usr/bin/env python3
"""Separate primitive-parameter enumeration and factor-incidence verification.
Imports neither the main verifier nor preceding research software.
"""
from __future__ import annotations
from fractions import Fraction
from math import gcd,isqrt,prod
from pathlib import Path
from collections import Counter
import argparse,json,hashlib,time
CHECKS=0

def req(v,label):
    global CHECKS;CHECKS+=1
    if not v:raise ArithmeticError(label)
def isprime(n):return n>=2 and all(n%d for d in range(2,isqrt(n)+1))
def fval(n,p):
    req(n!=0,'nonzero derivative numerator');n=abs(n);e=0
    while n%p==0:n//=p;e+=1
    return e

def primitive(p):
    out=[]
    for r in range(1,(p-1)//2+1):
        for s in range(1,(p-1)//(2*r)+1):
            if gcd(r,s)!=1:continue
            rs=r*s
            for h in range(p//(4*rs)+1,(p-1)//(2*rs)+1):
                a=h*rs;R=4*a-p;u=h*r*r
                for ch,num in [('E',p*r+s),('M',r+s)]:
                    if num%R:continue
                    k=num//R
                    xyz=[a,h*s*k,p*h*r*k] if ch=='E' else [a,p*h*s*k,p*h*r*k]
                    req(4*prod(xyz)==p*(xyz[0]*xyz[1]+xyz[0]*xyz[2]+xyz[1]*xyz[2]),'primitive reciprocal identity')
                    out.append([ch,a,u,R,h,r,s,k]+xyz)
    return sorted(out)

def local_check(p,t):
    ch,a,u,R,h,r,s,k,*xyz=t
    C=[p*k,p*r,s] if ch=='E' else [p*k,r,s]
    H=h*r*s*k
    req(gcd(H,p)==1,'common reciprocal scale is a p-unit')
    req([Fraction(v,H) for v in C]==[Fraction(p,x) for x in xyz],'full numerator and scale marking')
    nums=[(C[j]-C[(j+1)%3])*(C[j]-C[(j+2)%3]) for j in range(3)]
    vals=[fval(v,p) for v in nums]
    squares={x*x%p for x in range(1,(p+1)//2)}
    if ch=='E':
        req(vals==[1,1,0],'independent E derivative valuations')
        req(nums[2]*pow(H*H,-1,p)%p==16%p,'independent E split pair')
        req((nums[0]//p)*pow(nums[1]//p,-1,p)%p in squares,'independent shared ramified square class')
        return 'Qp^3 x ramified_quadratic^2'
    req(vals==[0,0,0] and (r*s)%p not in squares,'independent M nonsquare first factor')
    req(sum(v%p in squares for v in nums)==1,'independent M unique split pair')
    return 'Qp^3 x unramified_quadratic^2'

# Independent sparse two-generator quotient arithmetic.
class Alg:
    def __init__(self,d,z=0):
        self.d=Fraction(d)
        if isinstance(z,Alg):self.z=dict(z.z)
        elif isinstance(z,dict):self.z={k:Fraction(v) for k,v in z.items() if v}
        else:self.z={(0,0):Fraction(z)} if z else {}
    def cast(self,x):return x if isinstance(x,Alg) else Alg(self.d,x)
    def __add__(self,x):
        x=self.cast(x);z=dict(self.z)
        for k,v in x.z.items():z[k]=z.get(k,0)+v
        return Alg(self.d,z)
    __radd__=__add__
    def __neg__(self):return Alg(self.d,{k:-v for k,v in self.z.items()})
    def __sub__(self,x):return self+-self.cast(x)
    def __rsub__(self,x):return self.cast(x)+-self
    def __mul__(self,x):
        x=self.cast(x);z={}
        for (i,j),v in self.z.items():
            for (k,l),w in x.z.items():
                key=((i+k)%2,(j+l)%2)
                value=v*w*(-1)**((i+k)//2)/self.d**((j+l)//2)
                z[key]=z.get(key,0)+value
        return Alg(self.d,z)
    __rmul__=__mul__
    def __pow__(self,n):
        z=Alg(self.d,1)
        for _ in range(n):z=z*self
        return z
    def __eq__(self,x):return self.z==self.cast(x).z

def F(x):return Fraction(*x) if isinstance(x,list) else Fraction(x)
def factor_map(q,I):
    A,y,z,w=q
    b=I+A*y;c=-I+2*A*y+A*A*z
    d=-I*y-A*(I*z+2*y*y)-A*A*y*z
    e=2*z-7*I*y*y+A*w
    f=I*w+3*I*y**3-4*y*z+A*(6*I*y*y*z+w*y+4*y**4)+2*A*A*y**3*z
    return [A,b,c,d,e,f]

def fibre_records(ex):
    for row in ex['local_algebras']:
        target=[F(x) for x in row['source']['fibre']['target']]
        points=row['exact_branches'];req(len(points)==7,'all signed affine branches')
        for pt in points:
            d=F(pt['d']) if pt.get('d') is not None else Fraction(1)
            qq=[]
            for co in pt['coordinates']:
                z={(0,0):F(co[0]),(1,0):F(co[1]),(0,1):F(co[2]),(1,1):F(co[3])}
                qq.append(Alg(d,z))
            I=Alg(d,{(1,0):1});A,b,c,dd,e,f=factor_map(qq,I)
            req(A*dd+b*c==1,'original factor incidence')
            req(A**3*f-A*A*b*e+A*b*b*dd-b**3*c==1,'original resultant constant')
            req([A*c,A*e+b*dd,A*f+b*e,b*f]==target,'independent original factor product')
            if pt['root']=='infinity':req(A==0 and b==I,'only one infinity sign in chart')
            else:
                root=F(row['source']['fibre']['roots'][pt['root']])
                req(b==-A*root and A*A*d==1,'all root and sign data retained')
        ip=row['integral_branches'];p=ip['p'];mod=ip['modulus'];I=ip['i_embedding']
        req(mod==p**ip['precision'] and (I*I+1)%mod==0,'fixed local embedding and precision')
        req(len(ip['finite_points'])==2,'exactly two finite Qp points')
        for pt in ip['finite_points']:
            q=pt['coordinates'];A,b,c,dd,e,f=factor_map(q,I)
            expected=[(v.numerator*pow(v.denominator,-1,mod))%mod for v in target]
            req([x%mod for x in [A*c,A*e+b*dd,A*f+b*e,b*f]]==expected,'independent Hensel factor product')


def fixed_fibre(p,h,c,side):
    out=[]
    for s in range(1,(p-1)//(2*h)+1):
        for r in range(p//(4*h*s)+1,(p-1)//(2*h*s)+1):
            if gcd(r,s)!=1:continue
            a=h*r*s;u=h*r*r;R=4*a-p
            if (p*r+s)%R:continue
            k=(p*r+s)//R;v=h*s*s;D=(r+k)//s
            if (v-R if side=='alpha' else v-D)!=-4*c*c:continue
            out.append(['E',a,u,R,h,r,s,k,a,h*s*k,p*h*r*k])
    return sorted(out)

def check_crosses(p,records):
    for row in records:
        src=row['source'];ch,a,u,R,h,r,s,k,*_=src;c=row['c'];j=row['j'];side=row['side']
        req(ch=='E' and j==(h+1)//4 and h%4==3,'retained crossing source')
        req(h*s*s-(R if side=='alpha' else (r+k)//s)==-4*c*c,'actual negative-square shape')
        req(row['available']==(j%c==0),'complete chosen-word availability domain')
        if not row['available']:continue
        U=c*c if side=='alpha' else (j//c)**2
        RR=(p+4*U)//h;aa=(p+RR)//4;g=gcd(j,U)
        H=g*g//U;rr=U//g;lam=j//g;ss=RR*lam-rr
        target=['M',aa,U,RR,H,rr,ss,lam,aa,p*H*ss*lam,p*H*rr*lam]
        req(target==row['target'],'independent crossing coordinates')
        req(p<4*aa and 2*aa<p and aa*aa%U==0 and (U+aa)%RR==0,'crossing returns original M divisor')
        req(gcd(rr,ss)==1 and RR*lam==rr+ss,'crossing primitive normalization')


def order_transitions(ex):
    for z in ex['root_order_transitions']:
        p=z['p'];src=z['source'];dst=z['target']
        xx=[Fraction(p,v) for v in src[8:11]];yy=[Fraction(p,v) for v in dst[8:11]]
        ff=[F(c) for c in z['forward_coefficients']];gg=[F(c) for c in z['inverse_coefficients']]
        req(all(sum(ff[k]*x**k for k in range(3))==y for x,y in zip(xx,yy)),'independent forward root isomorphism')
        req(all(sum(gg[k]*y**k for k in range(3))==x for x,y in zip(xx,yy)),'independent inverse root isomorphism')
        val=lambda c:fval(c.numerator,p)-fval(c.denominator,p)
        req([val(c) for c in ff]==[0,-1,-1],'independent sharp interpolation denominator')
        req(all(not c or val(c)>=0 for c in gg),'independent integral reverse interpolation')
        req(z['source_order_index']==p and z['target_order_index']==1,'original order index record')
        req(z['source_conductor_exponents']==[1,1,0],'root-order conductor')

def finite_field_fibre(target,p):
    I=next(x for x in range(1,p) if (x*x+1)%p==0);ans=[]
    for A in range(p):
        for y in range(p):
            for z in range(p):
                if (A**3*z+2*A*A*y-I*A-target[0])%p:continue
                for w in range(p):
                    aa,b,c,d,e,f=factor_map([A,y,z,w],I)
                    if [(aa*c)%p,(aa*e+b*d)%p,(aa*f+b*e)%p,(b*f)%p]==[x%p for x in target]:
                        ans.append([A,y,z,w])
    return dict(p=p,i=I,target=target,points=ans)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input',type=Path,default=Path('certificates'))
    ap.add_argument('--out',type=Path,default=Path('independent.json'));args=ap.parse_args();start=time.monotonic()
    data=json.loads((args.input/'scan.json').read_text());ex=json.loads((args.input/'examples.json').read_text())
    ps=[p for p in range(5,data['bound']+1,4) if isprime(p)]
    req(ps==[r['p'] for r in data['rows']],'complete original prime domain')
    total=Counter()
    for row in data['rows']:
        p=row['p'];actual=primitive(p)
        req(actual==row['states'],'complete primitive state replay at '+str(p))
        c=Counter()
        for st in actual:c[st[0]]+=1;c[local_check(p,st)]+=1
        vec=0
        req([a for a,fs in row['source_factorizations']]==list(range(p//4+1,(p-1)//2+1)),'complete source shells')
        for a,fs in row['source_factorizations']:
            req(prod(q**e for q,e in fs)==a and all(e>0 and isprime(q) for q,e in fs),'actual source factorization')
            req(len({q for q,e in fs})==len(fs),'distinct prime indices')
            vec+=prod(2*e+1 for q,e in fs)
        req(vec==row['counts']['divisor_vectors'],'original exponent-box multiplicities')
        check_crosses(p,row['crosses'])
        for cross in row['crosses']:c['square_'+cross['side']+('_pass' if cross['available'] else '_blocked')]+=1
        c['divisor_vectors']=vec
        req(dict(c)==row['counts'],'all labelled counters')
        total.update(c)
    req(dict(total)==data['totals'],'complete totals')
    for st in ex['states']:
        req(isprime(st['p']),'fixed example primality by trial division')
        vals=[st['channel'],st['a'],st['u'],st['R'],st['h'],st['r'],st['s'],st['k']]+st['denominators']
        local_check(st['p'],vals)
        xyz=st['denominators'];req(sum((Fraction(1,x) for x in xyz),Fraction())==Fraction(4,st['p']),'fixed example rational identity')
    for row in ex['inverse_fibres']:
        req(fixed_fibre(row['p'],row['h'],row['c'],row['side'])==row['states'],'complete original crossing inverse fibre')
    fibre_records(ex)
    order_transitions(ex)
    p=3049;req([d for d in range(1,65) if 64%d==0]==[x['u'] for x in ex['full_blocked_cofactor']['rows']],'complete blocked cofactor square box')
    req(all((p+4*d)%31 for d in range(1,65) if 64%d==0),'all blocked cofactor words fail')
    E=finite_field_fibre([0,-4,0,0],17)
    # M at p17,a5,u1: roots 0,12,9 modulo17.
    M=finite_field_fibre([0,-4,6,0],17)
    req(len(E['points'])==len(M['points'])==3,'literal affine finite-field fibre count')
    result=dict(success=True,bound=data['bound'],primes=len(ps),totals=dict(total),checks=CHECKS,
                finite_field_fibres=[E,M],elapsed_seconds=time.monotonic()-start,
                scan_sha256=hashlib.sha256((args.input/'scan.json').read_bytes()).hexdigest(),
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                independence='Primitive parameter enumeration; sparse factor algebra; no verifier/predecessor import.',
                universal_ES_proved=False)
    args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
