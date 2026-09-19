#!/usr/bin/env python3
"""Independent direct-divisor and gcd-fibre check of Turn 5. No main-code import."""
import argparse, hashlib, json
from collections import Counter
from math import gcd,isqrt,prod
from pathlib import Path
COUNT=0

def demand(x,label):
    global COUNT
    COUNT+=1
    if not x:raise ArithmeticError(label)

def tf(n):
    result=[]
    for d in range(2,isqrt(n)+1):
        if d*d>n:break
        power=0
        while n%d==0:n//=d;power+=1
        if power:result.append((d,power))
    if n>1:result.append((n,1))
    return result

def divisors(fs):
    if not fs:return [1]
    q,e=fs[0];tail=divisors(fs[1:]);out=[]
    for t in tail:
        n=t
        for _ in range(e+1):out.append(n);n*=q
    return sorted(out)

def mu(n):
    fs=tf(n)
    return 0 if any(e>1 for _,e in fs) else (-1)**len(fs)

def tc(p,R,N):
    ds=divisors(tf(N));v=[x for d in ds for x in (d,p*d)]
    return sum((x+y)%R==0 for x in v for y in v)

def normalized(p,R,a,u,ch):
    d=gcd(a,u);h=d*d//u;r=u//d;s=a//d
    if ch=='E':
        k=(p*r+s)//R;v=[a,h*s*k,p*h*r*k]
        demand((p*r+s)%R==0,'E quotient')
    else:
        k=(r+s)//R;v=[a,p*h*s*k,p*h*r*k]
        demand((r+s)%R==0,'M quotient')
    x,y,z=v
    demand(4*x*y*z==p*(x*y+x*z+y*z),'independent reciprocal equality')
    return v

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input',default='certificates');ap.add_argument('--out',default='independent.json');args=ap.parse_args()
    root=Path(args.input);scan=json.loads((root/'scan.json').read_text());rows=[];dig=hashlib.sha256()
    bound=scan['bound']
    ps=[p for p in range(5,bound+1,4) if all(p%d for d in range(2,isqrt(p)+1))]
    for p in ps:
        qr={x*x%p for x in range(1,(p+1)//2)}
        for a in range(p//4+1,(p+1)//2):
            R=4*a-p;fs=tf(a);ds=divisors([(q,2*e) for q,e in fs]);E=M=0
            for u in ds:
                ee=(4*u+1)%R==0;mm=(u+a)%R==0
                E+=ee;M+=mm
                if ee:demand(u%p not in qr,'independent E character');normalized(p,R,a,u,'E')
                if mm:demand((u%p in qr)!=(a%p in qr),'independent M character');normalized(p,R,a,u,'M')
            small=divisors(fs)
            B0=sum((b+c)%R==0 for b in small for c in small)
            B1=sum((b+p*c)%R==0 for b in small for c in small)
            T=2*(B0+B1)
            inversion=sum(mu(d)*tc(p,R,a//d) for d in small)
            demand(inversion==2*(E+M),'independent Möbius reduction')
            row=dict(p=p,a=a,R=R,mass=len(ds),chi_a=1 if a%p in qr else -1,E=E,M=M,T=T,B0=B0,B1=B1,F=E+M)
            rows.append(row);dig.update((json.dumps(row,sort_keys=True,separators=(',',':'))+'\n').encode())
    demand(rows==scan['rows'],'every original arithmetic row')
    demand(dig.hexdigest()==scan['row_sha256'],'original row digest')
    fixture=json.loads((root/'paired_sources.json').read_text());p=fixture['p'];qr={x*x%p for x in range(1,(p+1)//2)}
    direct_mass=rec_mass=0
    for row in fixture['rows']:
        q,t,D=row['q'],row['t'],row['D'];sig=1 if q%4==3 else 3
        demand(D==sig*q*t*t and D<3*p,'all source marks and bounds')
        for key,mod,N,mode in [('original',D,(p+D)//4,'both'),('reciprocal',D,(p*D+1)//4,'sum')]:
            data=row[key];fs=tf(N);div=divisors([(q,2*e) for q,e in fs]);cells=data['cells']
            demand([list(v) for v in fs]==data['factors'],'every complete factorization')
            demand(len(cells)==len(div) and [x['u' if key=='original' else 'w'] for x in cells]==div,'all square divisors')
            demand(all(all(r%d for d in range(2,isqrt(r)+1)) for r,_ in fs),'factor prime trial division')
            demand(all((4*u+1)%mod and (u+N)%mod for u in div) if mode=='both' else all((u+N)%mod for u in div),'every complete gate fails')
            for z,u in zip(cells,div):
                demand(z['chi_p']==(1 if u%p in qr else -1),'every recorded original character')
                demand(z['centered']==u*pow(N,-1,mod)%mod,'fine original residue')
            if key=='original':direct_mass+=len(div)
            else:rec_mass+=len(div)
    demand(direct_mass==fixture['direct_mass'] and rec_mass==fixture['reciprocal_mass'],'source mass totals')
    for ch in ('E','M'):
        state=fixture['positive_exchange'][ch]
        demand(normalized(p,state['R'],state['a'],state['u'],ch)==state['denominators'],'both original positive returns')
    rec=json.loads((root/'reciprocal_atlas.json').read_text())
    for expected in rec['rows']:
        p=expected['p'];seen=Counter()
        for D in range(3,expected['D_bound']+1,4):
            B=(p*D+1)//4
            for w in divisors([(q,2*e) for q,e in tf(B)]):
                if (w+B)%D:continue
                g=gcd(B,w);h=g*g//w;r=w//g;s=B//g;lam=(r+s)//D
                if r>s:r,s=s,r
                x=h*r*lam;R=4*x-p;u=h*r*r
                demand(p<4*x<2*p and (4*u+1)%R==0,'dual to original first half')
                seen[R,u]+=1
        direct=Counter()
        for a in range(p//4+1,(p+1)//2):
            R=4*a-p
            for u in divisors([(q,2*e) for q,e in tf(a)]):
                if (4*u+1)%R==0:direct[R,u]=2
        demand(seen==direct,'independent complete dual atlas and fibre two')
    out=dict(checks=COUNT,bound=bound,rows=len(rows),row_sha256=dig.hexdigest(),paired_direct_mass=direct_mass,
             paired_reciprocal_mass=rec_mass,imports_main=False,scope='Separate direct enumeration, original gate/character checks and reciprocal atlas.')
    Path(args.out).write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n');print(json.dumps(out,sort_keys=True))
if __name__=='__main__':main()
