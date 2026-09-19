#!/usr/bin/env python3
"""Separate arithmetic checker for channel_windows.tex; no verifier imports."""
import argparse,json,hashlib
from pathlib import Path
from math import gcd,isqrt,prod
from collections import Counter
N=0

def need(v,label):
    global N;N+=1
    if not v:raise ArithmeticError(label)
def isprime(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))
def factors(n):
    out=[]
    for q in range(2,isqrt(n)+1):
        if q*q>n:break
        e=0
        while n%q==0:e+=1;n//=q
        if e:out.append((q,e))
    if n>1:out.append((n,1))
    return out
def divisors(fs):
    if not fs:return [1]
    q,e=fs[0];ans=[]
    for v in divisors(fs[1:]):
        for j in range(e+1):ans.append(v*q**j)
    return sorted(ans)
def jac(a,n):
    s=1;a%=n
    while a:
        while a%2==0:
            a//=2
            if n%8 in (3,5):s=-s
        a,n=n,a
        if a%4==n%4==3:s=-s
        a%=n
    return s if n==1 else 0
def inverse(a,n):
    # extended Euclidean rather than modular negative powers
    b=n;x,y=1,0
    while b:q,a,b=a//b,b,a%b;x,y=y,x-q*y
    if a!=1:raise ValueError('not a unit')
    return x%n
def cycle(b,n):
    vals=[1];x=b%n
    while x!=1:vals.append(x);x=x*b%n
    return vals
def check_return(v):
    p,a,u,R=v['p'],v['a'],v['u'],v['R'];x,y,z=v['denominators']
    need(4*x*y*z==p*(x*y+x*z+y*z),'ordered unit fraction identity')
    h,r,s=v['h'],v['r'],v['s'];d=gcd(a,u)
    need([h,r,s]==[d*d//u,u//d,a//d] and a==h*r*s,'gcd original inverse')
    need(u*(R*y-p*a)==(a*a if v['channel']=='E' else p*a*a),'ordered seed inverse')
def check_n(p,a,record):
    R=4*a-p;fs=factors(a);vs=divisors([(q,2*e) for q,e in fs]);E=[u for u in vs if (4*u+1)%R==0];M=[u for u in vs if (u+a)%R==0]
    need((len(E),len(M))==(record['E'],record['M']),'complete source gate counts')
    if 'fine_counts' in record:
        mu=Counter(u*inverse(a,R)%R for u in vs);W=set(mu)
        need([list(z) for z in sorted(mu.items())]==record['fine_counts'],'every fine residue coefficient')
        K=sorted(h for h in W if {h*w%R for w in W}==W)
        need(K==record['actual_stabilizer'],'actual full support stabilizer')
    if record['window'] is not None:
        A=a;e=0
        while A%2==0:A//=2;e+=1
        small=divisors(factors(A));packet={2**f*w for w in small for f in range(2*e+1)}
        pe=sum(u in packet for u in E);pm=sum(u in packet for u in M)
        w=record['window'];H=cycle(2,R);m=len(H);am=sum(-x%R in H for x in small)
        need((e,A,m,am,pe,pm)==(w['e'],w['odd'],w['order'],w['A_minus'],w['packet_E'],w['packet_M']),'packet independent arithmetic')
        for x in small:
            for j in range(-2*e-2,e+1):
                if j>=0:z=pow(2,j,R)
                else:z=pow(inverse(2,R),-j,R)
                if z!=(-x)%R:continue
                if j<=-2:need(2**(-j-2)*x in E,'E window returns actual divisor')
                if j>=-e:need(2**(e+j)*(A//x) in M,'M window returns actual divisor')
        if e>=2:
            for u in vs:
                if a%(4*u)==0:
                    v=a//(4*u)
                    need((u in E)==(v in M) and (u in M)==(v in E),'independent quarter crossing')
    sn=record['simple_NR']
    if sn is not None:
        rr=[q for q,e in fs if jac(q,p)==-1]
        need(rr==[sn['r']] and dict(fs)[rr[0]]==1,'unique simple NR factor')
        r=rr[0];B=a//r;mu=Counter(v*inverse(B,R)%R for v in divisors([(q,2*e) for q,e in factors(B)]))
        need(mu[-inverse(p,R)%R]==len(E) and 2*mu[-r%R]==len(M),'fine B coefficient reduction')
        if 'power' in sn:
            pw=sn['power'];ell,e=pw['ell'],pw['e'];H=cycle(ell,R)
            need(len(H)==pw['order'] and ell**e==B,'exact prime-power subgroup')
            if 4%R in H:
                need(abs(len(E)-len(M)//2)<=1,'independent channel balance')
                if -r%R in H:
                    c=H.index(4%R);j=H.index(-r%R)
                    ce=sum((v-j)%len(H)==0 for v in range(-2*e-c,-c+1))
                    cm=sum((v-j)%len(H)==0 for v in range(-e,e+1))
                    need((ce,cm)==(len(E),len(M)//2),'independent complete interval counts')
                else:need(not E and not M,'missing subgroup targets')
            else:need(not(E and M),'distinct 4-cosets')
    return E,M

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--input',default='certificates');ap.add_argument('--out',default='windows_independent.json');ar=ap.parse_args();base=Path(ar.input)
    s=json.loads((base/'scan_windows.json').read_text());dig=hashlib.sha256();index=0;ps=[]
    for p in range(5,s['bound']+1,4):
        if not isprime(p):continue
        ps.append(p)
        for a in range(p//4+1,(p+1)//2):
            row=s['rows'][index];index+=1
            need((p,a,4*a-p)==(row['p'],row['a'],row['R']),'complete source range')
            check_n(p,a,row)
            dig.update((json.dumps(row,sort_keys=True,separators=(',',':'))+'\n').encode())
    need(index==len(s['rows']) and dig.hexdigest()==s['row_sha256'],'complete scan and digest')
    x=json.loads((base/'window_examples.json').read_text())
    for v in x['rows']:
        need(isprime(v['p']) and all(isprime(q) for q,e in v['factors']),'example and factor primes')
        check_n(v['p'],v['a'],dict(v,E=len(v['E']),M=len(v['M'])))
        for st in v['states']:check_return(st)
    six=x['six_vertex'];p=six['p'];need(isprime(p),'six p prime');C=six['cycle'];seen=[];mass=0
    # Literal quadratic residue table is independent of Euler-symbol source code.
    QR={i*i%p for i in range(1,(p+1)//2)}
    for q in C:
        need(isprime(q) and q not in QR,'vertex prime and nonresidue')
        sigma=1 if q%4==3 else 3
        t=1
        while sigma*q*t*t<3*p:
            R=sigma*q*t*t;a=(p+R)//4
            v=next(z for z in six['rows'] if z['q']==q and z['t']==t);rec=v['source'];fs=factors(a)
            need([list(z) for z in fs]==rec['factors'],'all source prime exponents')
            div=divisors([(r,2*e) for r,e in fs]);need(len(div)==rec['mass'],'original vector mass')
            need(div==[z['u'] for z in rec['cells']],'entire original divisor set')
            for u,z in zip(div,rec['cells']):
                need((4*u+1)%R and (u+a)%R,'complete E/M failure')
                need(z['E_rem']==(4*u+1)%R and z['M_rem']==(u+a)%R,'fine original remainders')
                need(z['chi']==(1 if u%p in QR else -1),'every original character')
                need(z['centered']==u*inverse(a,R)%R,'every fine residue')
            edges=[[r,e] for r,e in fs if r not in QR]
            need(edges==v['edges'],'every nonresidue edge including even weights')
            if t==1:need(edges==[[C[(C.index(q)+1)%6],1]],'actual canonical closure')
            rr=dict(rec,E=len(rec['E']),M=len(rec['M']),window=None,simple_NR=v['simple_NR'])
            check_n(p,a,rr);mass+=len(div);seen.append((q,t));t+=2
    need(len(seen)==17 and mass==663 and len(six['rows'])==17,'full bounded square-source enumeration')
    check_return(six['positive_E']);check_return(six['positive_M'])
    out=dict(checks=N,scan_rows=index,bound=s['bound'],row_sha256=dig.hexdigest(),six_source_boxes=17,six_original_divisors=mass,
        imports_verifiers=False,scope='All recorded arithmetic window rows and all examples, using direct divisors, literal square residues and separate normalization. No global ES inference.')
    Path(ar.out).write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n');print(json.dumps(out,sort_keys=True))
if __name__=='__main__':main()
