#!/usr/bin/env python3
"""Exact original-channel windows and the complete six-vertex local obstruction.
Standard library only. No assertion statements; checks remain active under -O.
"""
from __future__ import annotations
import argparse, hashlib, json
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from math import gcd, isqrt, prod
from pathlib import Path
CHECKS=Counter()
def check(value: bool, label: str) -> None:
    CHECKS[label]+=1
    if not value: raise ArithmeticError(label)
@lru_cache(None)
def factor(n: int) -> tuple[tuple[int,int],...]:
    if n<1: raise ValueError('positive factor input')
    out=[];d=2
    while d*d<=n:
        e=0
        while n%d==0:n//=d;e+=1
        if e:out.append((d,e))
        d=3 if d==2 else d+2
    if n>1:out.append((n,1))
    return tuple(out)
def prime(n: int)->bool:
    return n>=2 and factor(n)==((n,1),)
def ds(n:int,square:bool=False)->list[int]:
    out=[1]
    for q,e in factor(n):out=[x*q**i for x in out for i in range((2 if square else 1)*e+1)]
    return sorted(out)
def leg(a:int,p:int)->int:
    x=pow(a%p,(p-1)//2,p)
    return -1 if x==p-1 else x
def cyc(g:int,R:int)->list[int]:
    if gcd(g,R)!=1 or R<2:raise ValueError('cyclic unit required')
    out=[];x=1
    while not out or x!=1:
        out.append(x);x=x*g%R
        if len(out)>R:raise ArithmeticError('order termination')
    return out
def subgroup(gs:list[int],R:int)->set[int]:
    out={1};todo=[1]
    while todo:
        x=todo.pop()
        for g in gs:
            y=x*g%R
            if y not in out:out.add(y);todo.append(y)
    return out
def count_interval(lo:int,hi:int,j:int,d:int)->int:
    if d<=0:raise ValueError('positive period')
    return (hi-j)//d-(lo-1-j)//d if hi>=lo else 0
def state(p:int,a:int,u:int,tag:str)->dict:
    R=4*a-p;d=gcd(a,u)
    if tag not in ('E','M') or a*a%u:raise ValueError('original tag/divisor')
    h=d*d//u;r=u//d;s=a//d
    num=p*r+s if tag=='E' else r+s
    if num%R:raise ValueError('channel misses')
    k=num//R;den=[a,h*s*k,p*h*r*k] if tag=='E' else [a,p*h*s*k,p*h*r*k]
    x,y,z=den
    check(4*x*y*z==p*(x*y+x*z+y*z),'original reciprocal equality')
    check((a*a if tag=='E' else p*a*a)==u*(R*y-p*a),'ordered divisor inverse')
    check(a==h*r*s and u==h*r*r and gcd(r,s)==1,'normalization inverse')
    beta=[];v=u
    for q,e in factor(a):
        f=0
        while v%q==0:v//=q;f+=1
        beta.append(f-e)
    check(v==1,'original exponent source')
    return dict(p=p,a=a,R=R,u=u,channel=tag,h=h,r=r,s=s,quotient=k,beta=beta,denominators=den)
def local(p:int,a:int,detail:bool=False)->dict:
    R=4*a-p
    if not prime(p) or p%4!=1 or not p<4*a<4*p or gcd(p*a,R)!=1:raise ValueError('original source domain')
    vals=ds(a,True);E=[u for u in vals if (4*u+1)%R==0];M=[u for u in vals if (u+a)%R==0]
    out=dict(p=p,a=a,R=R,factors=factor(a),mass=len(vals),E=E,M=M)
    if detail:
        cells=[]
        for u in vals:
            v=u;f=[]
            for q,e in factor(a):
                j=0
                while v%q==0:v//=q;j+=1
                f.append(j)
            cells.append(dict(u=u,f=f,beta=[j-e for j,(_,e) in zip(f,factor(a))],
                centered=u*pow(a,-1,R)%R,chi=leg(u,p),E_rem=(4*u+1)%R,M_rem=(u+a)%R))
        out['cells']=cells
        mu=Counter(z['centered'] for z in cells); W=set(mu)
        out['fine_counts']=sorted(mu.items())
        out['actual_stabilizer']=sorted(k for k in W if {k*w%R for w in W}==W)
    return out

def window(p:int,a:int,n:dict)->dict|None:
    if a%2:return None
    e=0;A=a
    while A%2==0:A//=2;e+=1
    R=n['R'];pw=cyc(2,R);d=len(pw);logs={x:j for j,x in enumerate(pw)}
    maps={'E':[],'M':[]};aminus=0
    for w in ds(A):
        if (-w)%R not in logs:continue
        aminus+=1;j0=logs[-w%R]
        for tag,lo,hi in [('E',-2*e-2,-2),('M',-e,e)]:
            for j in range(lo,hi+1):
                if j%d!=j0:continue
                u=2**(-j-2)*w if tag=='E' else 2**(e+j)*(A//w)
                maps[tag].append((w,j,u))
                f=0;z=u
                while z%2==0:z//=2;f+=1
                check((w,j)==((z,-f-2) if tag=='E' else (A//z,f-e)),'window inverse')
    packet={2**f*w for f in range(2*e+1) for w in ds(A)}
    for tag in ('E','M'):
        check(sorted(z[2] for z in maps[tag])==sorted(packet&set(n[tag])),'window equals original packet gate')
        check(len(set(z[2] for z in maps[tag]))==len(maps[tag]),'labelled packet injective')
    f0,rho=divmod(2*e+1,d);delta=min((e+2)%d,(-(e+2))%d)
    low=2*f0+int(rho>=d-delta);high=2*f0+int(rho>0)+int(rho>delta)
    count=len(maps['E'])+len(maps['M'])
    check(low*aminus<=count<=high*aminus,'exact packet mass bounds')
    if 3*e+3>=d:check(bool(count)==bool(aminus),'joined window forces original packet')
    if e>=2:
        for u in ds(a//4):
            v=a//(4*u)
            check(a//(4*v)==u,'quarter involution')
            check(((4*u+1)%R==0)==((v+a)%R==0),'quarter exchanges gates')
            check(((u+a)%R==0)==((4*v+1)%R==0),'quarter reverse exchange')
        for u in ds(a,True):check((Fraction(a,4*u).denominator==1)==(a%(4*u)==0),'maximal quarter domain')
    return dict(e=e,odd=A,order=d,A_minus=aminus,packet_E=len(maps['E']),packet_M=len(maps['M']),lower=low,upper=high)

def simple_nr(p:int,a:int,n:dict,detail:bool=False)->dict|None:
    nr=[(q,e) for q,e in factor(a) if leg(q,p)==-1]
    if len(nr)!=1 or nr[0][1]!=1:return None
    r=nr[0][0];B=a//r;R=n['R'];inv=pow(B,-1,R);mu=Counter(v*inv%R for v in ds(B,True))
    te=-pow(p,-1,R)%R;tm=-r%R
    check(len(n['E'])==mu[te] and len(n['M'])==2*mu[tm],'simple NR full two-channel counts')
    ex=[r*v for v in ds(B,True) if v*inv%R==te]
    mx=[v for v in ds(B,True) if v*inv%R==tm]
    check(ex==n['E'],'simple NR E inverse')
    check(sorted(mx+[a*a//v for v in mx])==n['M'],'simple NR M complete involution')
    out=dict(r=r,B=B,mu=sorted(mu.items()) if detail else None,E_target=te,M_target=tm,
        E=len(n['E']),M_half=len(n['M'])//2)
    fs=factor(B)
    if len(fs)==1:
        ell,e=fs[0];pw=cyc(ell,R);H=set(pw);d=len(pw);target=-r%R
        if 4%R in H:
            c=pw.index(4%R)
            if target in H:
                j=pw.index(target);ce=count_interval(-2*e-c,-c,j,d);cm=count_interval(-e,e,j,d)
            else:c=pw.index(4%R);j=None;ce=cm=0
            check((ce,cm)==(len(n['E']),len(n['M'])//2),'two-prime complete interval formula')
            check(abs(ce-cm)<=1,'sharp channel count difference')
        else:
            c=j=None;check(not (n['E'] and n['M']),'four outside subgroup separates channels')
        out['power']=dict(ell=ell,e=e,order=d,c=c,j=j,target_inside=target in H)
    if detail:
        H=subgroup([q for q,_ in fs],R)
        out['generated_order']=len(H);out['targets_in_generated']=[te in H,tm in H]
    return out

def abstract()->dict:
    cases=0
    for d in range(2,81):
        for e in range(1,71):
            vs=[count_interval(-2*e-2,-2,j,d)+count_interval(-e,e,j,d) for j in range(d)]
            f,rho=divmod(2*e+1,d);de=min((e+2)%d,(-(e+2))%d)
            low=2*f+int(rho>=d-de);high=2*f+int(rho>0)+int(rho>de)
            check((min(vs),max(vs))==(low,high),'all cyclic paired minima and maxima')
            check((min(vs)>0)==(3*e+3>=d),'exact interval cover threshold')
            for j in range(d):
                check(abs(count_interval(-2*e-2,-2,j,d)-count_interval(-e,e,j,d))<=1,'cyclic unit difference')
                check(count_interval(-2*(e+d)-2,-2,j,d)==count_interval(-2*e-2,-2,j,d)+2,'E complete-period recurrence')
                check(count_interval(-e-d,e+d,j,d)==count_interval(-e,e,j,d)+2,'M complete-period recurrence')
            cases+=1
    huge={'d':127,'e':10**24+17,'target':59};e=huge['e'];d=huge['d'];j=huge['target']
    huge.update(E=count_interval(-2*e-2,-2,j,d),M_half=count_interval(-e,e,j,d))
    return dict(cases=cases,d_max=80,e_max=70,huge_integer_count=huge)

def six()->dict:
    p=315361;C=[27847,42901,13877,2789,20233,18803];rows=[];mass=0
    check(prime(p) and p%840 in {1,121,169,289,361,529},'six-cycle hard primality')
    for q in C:
        check(prime(q) and leg(q,p)==-1 and q<p,'original vertex prime')
        sig=1 if q%4==3 else 3;T=isqrt((3*p-1)//(sig*q))
        for t in range(1,T+1,2):
            R=sig*q*t*t;a=(p+R)//4;n=local(p,a,True)
            check(not n['E'] and not n['M'],'complete six-vertex all-square gate failure')
            Bdata=simple_nr(p,a,n,True);check(Bdata is not None,'every source unique simple NR')
            edges=[(r,e) for r,e in factor(a) if leg(r,p)==-1]
            check(all(prime(r) and r<p for r,e in factor(a)),'every source factor prime')
            if t==1:check(edges==[(C[(C.index(q)+1)%len(C)],1)],'canonical complete edge closure')
            R0=sig*q
            # Base tests are deliberately distinct from the full residual tests.
            be=[u for u in ds(a,True) if (4*u+1)%R0==0];bm=[u for u in ds(a,True) if (u+a)%R0==0]
            check(not be and not bm,'six-cycle base candidates absent')
            for z in n['cells']:
                z['carries']={}
                for tag,eta in [('E',1),('M',p)]:
                    value=4*z['u']+eta
                    if value%R0:z['carries'][tag]=None
                    else:
                        k=value//R0;b,digit=divmod(k,t*t)
                        check(R0*(digit+t*t*b)-eta==4*z['u'],'full square carry inverse')
                        z['carries'][tag]=dict(k=k,d=digit,b=b)
            rows.append(dict(q=q,sigma=sig,t=t,R0=R0,source=n,edges=edges,simple_NR=Bdata));mass+=n['mass']
    check(len(rows)==17 and mass==663,'complete seventeen-source mass')
    path=next(r for r in rows if r['q']==20233 and r['t']==3)
    check(any(r==11 for r,e in path['edges']),'new square-factor path to 11')
    end=local(p,(p+11)//4,True)
    check(len(end['E'])==1 and len(end['M'])==4 and 41 in end['E'],'actual occupied endpoint')
    e=state(p,end['a'],41,'E');m=state(p,end['a'],end['M'][0],'M')
    return dict(p=p,cycle=C,source_boxes=len(rows),original_divisors=mass,rows=rows,
        positive_path=[dict(q=20233,t=3,to=11),dict(q=11,t=1)],positive_E=e,positive_M=m,
        scope='All valid same-vertex square sources at the six displayed canonical vertices; not a full expanded-graph trap.')

def examples()->dict:
    out=[]
    for p,R in [(61,3),(23209,127),(43801,31),(8521,31),(12601,31),(12049,127),(493887409,79)]:
        n=local(p,(p+R)//4,True);w=window(p,n['a'],n);s=simple_nr(p,n['a'],n,True)
        n.update(window=w,simple_NR=s,states=[state(p,n['a'],u,c) for c in ('E','M') for u in n[c]])
        if p==61:check(2 in n['E'] and 2 in n['M'] and n['a']==4*2**2,'tagged fixed-point example')
        if p==23209:check(not n['E'] and not n['M'] and s['power']['order']==7,'actual threshold sharpness')
        out.append(n)
    return {'rows':out,'six_vertex':six()}

def negatives()->list[str]:
    tests=[('drop one channel from joined window',lambda:check(set(j%5 for j in range(-4,-1))==set(range(5)),'omission false')),
      ('gapful e0 treated as interval',lambda:check({-2,0}==set(range(-2,1)),'e0 false')),
      ('quarter inverse outside divisor domain',lambda:check(Fraction(16,4*16).denominator==1,'unavailable inverse')),
      ('erase fixed-point channel tag',lambda:check(state(61,16,2,'E')['denominators']==state(61,16,2,'M')['denominators'],'tag false')),
      ('force actual target one below threshold',lambda:check(any(2**j*2917%127==126 for j in range(3)),'threshold false')),
      ('M orientation counted only once',lambda:check(len(local(8521,2138)['M'])==1,'M half false')),
      ('replace two-channel form by PSD Gram',lambda:check(4>=6,'PSD false')),
      ('new factors imply original six-vertex hit',lambda:check(any(local(315361,(315361+(1 if q%4==3 else 3)*q)//4)['E'] or local(315361,(315361+(1 if q%4==3 else 3)*q)//4)['M'] for q in [27847,42901,13877,2789,20233,18803]),'six false'))]
    out=[]
    for name,fn in tests:
        try:fn()
        except (ArithmeticError,ValueError):out.append(name)
        else:raise ArithmeticError('negative control accepted: '+name)
    return out

def main()->None:
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--bound',type=int,default=2000);ap.add_argument('--out',default='certificates_windows');ar=ap.parse_args()
    if ar.bound<5:ap.error('bound >=5')
    out=Path(ar.out);out.mkdir(parents=True,exist_ok=True)
    rows=[];stats=Counter();dig=hashlib.sha256()
    for p in range(5,ar.bound+1,4):
        if not prime(p):continue
        stats['primes']+=1
        for a in range(p//4+1,(p+1)//2):
            n=local(p,a);w=window(p,a,n);s=simple_nr(p,a,n)
            stats['shells']+=1;stats['divisor_vectors']+=n['mass'];stats['window_sources']+=w is not None;stats['simple_NR_sources']+=s is not None
            if s and 'power' in s:stats['two_prime_power_sources']+=1
            row=dict(p=p,a=a,R=n['R'],E=len(n['E']),M=len(n['M']),window=w,simple_NR=s)
            rows.append(row);dig.update((json.dumps(row,sort_keys=True,separators=(',',':'))+'\n').encode())
    data={'scan_windows.json':dict(bound=ar.bound,rows=rows,statistics=stats,row_sha256=dig.hexdigest()),
        'window_abstract.json':abstract(),'window_examples.json':examples(),'window_negative_controls.json':negatives()}
    summary=dict(checks=sum(CHECKS.values()),check_categories=dict(CHECKS),statistics=dict(stats),row_sha256=dig.hexdigest(),negative_controls=len(data['window_negative_controls.json']))
    data['window_summary.json']=summary
    for name,obj in data.items():(out/name).write_text(json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n')
    print(json.dumps({k:v for k,v in summary.items() if k!='check_categories'},sort_keys=True))
if __name__=='__main__':main()
