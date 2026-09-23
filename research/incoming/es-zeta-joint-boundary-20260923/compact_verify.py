#!/usr/bin/env python3
"""Standalone exact replay for the accompanying preprint; standard library only.
Finite examples are not a proof of universal ES. General arguments are in TeX.
"""
from fractions import Fraction as F
from itertools import product
from math import gcd,isqrt,prod
from pathlib import Path
import json
checks=0

def check(ok,msg):
    global checks
    checks+=1
    if not ok:raise ArithmeticError(msg)

def primes():
    data=json.loads(Path(__file__).with_name('prime_certificates.json').read_text());done=set()
    for n in sorted(map(int,data['nodes'])):
        c=data['nodes'][str(n)]
        if c.get('trial'):
            check(2<=n<100 and all(n%d for d in range(2,isqrt(n)+1)),'trial leaf')
        else:
            fs=c['factors'];b=c['base']
            check(prod(q**e for q,e in fs)==n-1 and all(q in done for q,e in fs),'prime dependencies')
            check(pow(b,n-1,n)==1,'order power')
            check(all(gcd(pow(b,(n-1)//q,n)-1,n)==1 for q,e in fs),'order gcds')
        done.add(n)
    check(set(data['roots'])<=done,'root primes')
    return len(done)

def state(p,a,u,ch):
    R=4*a-p
    check(p<4*a<2*p and a*a%u==0,'original box')
    g=gcd(a,u);h,r,s=g*g//u,u//g,a//g
    q=F(p*r+s,R) if ch=='E' else F(r+s,R)
    ds=[F(a),h*s*q,p*h*r*q] if ch=='E' else [F(a),p*h*s*q,p*h*r*q]
    G=4*u+1 if ch=='E' else p+4*u
    check(sum((1/d for d in ds),F())==F(4,p),'reciprocal identity')
    check(((ds[1]+ds[2]).denominator==1)==(G*G%R==0),'trace')
    full=all(d.denominator==1 for d in ds)
    check(full==(G%R==0),'integer gate')
    check(F(a*a if ch=='E' else p*a*a)/(R*ds[1]-p*a)==u,'ordered inverse')
    return dict(u=u,channel=ch,h=h,r=r,s=s,quotient=[q.numerator,q.denominator],
                full=full,denominators=[[x.numerator,x.denominator] for x in ds])

def shell(p,fs):
    a=prod(q**e for q,e in fs);out=[]
    for ex in product(*(range(2*e+1) for q,e in fs)):
        u=prod(q**v for (q,e),v in zip(fs,ex))
        for ch in ('E','M'):
            x=state(p,a,u,ch)
            if x['full']:out.append(x)
    return out

def run():
    prime_nodes=primes();orders=[]
    for n in range(2,9):
        D=3**n-2;C=(3**n-5)//2;ct=[0]*D;full=[]
        for sg in (-1,1):
            for bs in product((-1,0,1),repeat=n):
                c=(sg*C-sum(3**j*b for j,b in enumerate(bs)))%D;ct[c]+=1
                if c==0:full.append([sg,list(bs)])
        check(full==[[-1,[1]+[-1]*(n-1)],[1,[-1]+[1]*(n-1)]],'all high-order full words')
        check(min(ct)>=2 and 1+2*n<D-1 and D>3,'coverage and old-criterion failures')
        orders.append(dict(n=n,D=D,minimum=min(ct),full_digits=full))
    p=7673586546314641;fs=[(7,2),(29,1),(599,1),(5851,1),(2551,1),(151,1)]
    pos=shell(p,fs)
    check(len(pos)==2 and all(x['channel']=='M' for x in pos),'complete 1215-word positive shell')
    check({x['u'] for x in pos}=={48646799621,75652369403750354621},'positive words')
    p=34442321771655001;fs=[(101,1),(179,1),(6121,1),(8821,2)]
    negshell=shell(p,fs);a=prod(q**e for q,e in fs);ct=[0]*15
    for b1,b2 in product(range(-1,2),range(-2,3)):
        u=101*179**2*6121**(1+b1)*8821**(2+b2);s=state(p,a,u,'M')
        check(not s['full'],'missing joint zero');ct[(4-b1-b2)%15]+=1
    check(ct==[0,1,2,3,3,3,2,1,0,0,0,0,0,0,0],'negative joint distribution')
    check([sum(ct[j] for j in range(i,15,3)) for i in range(3)]==[5]*3,'mod3 uniform')
    check([sum(ct[j] for j in range(i,15,5)) for i in range(5)]==[3]*5,'mod5 uniform')
    check(len(negshell)==3 and all(x['channel']=='E' for x in negshell),'complete 135-word negative shell')
    joint=state(6841,1717,101,'E')
    check(joint['full'] and joint['denominators']==[[1717,1],[436118,1],[175499014,1]],'same-shell joint return')
    for u in [101,29189]:check(not state(6841,1717,u,'M')['full'],'proper M inputs')
    for D in range(1,18):
        for V in range(1,2*D+2):
            for s in range(1,D+1):
                if gcd(s,D)!=1:continue
                ct=[0]*D
                for j in range(V):ct[s*j%D]+=1
                b=[ct[x]-ct[(x-s)%D] for x in range(D)]
                recovered=[F(V-sum((D-j)*b[(x+j*s)%D] for j in range(1,D)),D) for x in range(D)]
                check(recovered==ct,'literal mass-boundary inverse')
                endpoint=[0]*D;endpoint[0]+=1;endpoint[s*V%D]-=1
                check(b==endpoint,'retained rank-one boundary')
                for omega in range(D):
                    d=omega*pow(s,-1,D)%D;Q,r=divmod(V,D)
                    check(min(ct[x]+ct[(x-omega)%D] for x in range(D))==2*Q+int(r>=D-min(d,D-d)),
                          'exact paired-channel minimum')
    return dict(success=True,checks=checks,prime_certificate_nodes=prime_nodes,
                arbitrary_order_tests=orders,positive_shell_full=pos,negative_shell_full=negshell,
                negative_selected_counts=[0,1,2,3,3,3,2,1,0,0,0,0,0,0,0],
                joint_return=joint,universal_ES_proved=False)

if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
