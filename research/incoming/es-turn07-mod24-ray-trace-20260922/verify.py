#!/usr/bin/env python3
"""Exact original-source checks. Standard library; finite runs do not prove ES."""
from __future__ import annotations
import argparse, hashlib, json, math, time
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
CHECKS=0
HARD={1,121,169,289,361,529}
RAYS=[(r,s) for r in range(1,7) for s in range(1,7) if math.gcd(r,s)==1 and 6%(r*s)==0]
def ck(c,msg):
    global CHECKS
    CHECKS+=1
    if not c:raise ArithmeticError(msg)
def primes(N):
    b=bytearray(b'\1')*(N+1);b[:2]=b'\0\0'
    for x in range(2,math.isqrt(N)+1):
        if b[x]:b[x*x:N+1:x]=b'\0'*((N-x*x)//x+1)
    return [x for x in range(2,N+1) if b[x]]
def prime_trial(n):
    if n<2:return False
    if n%2==0:return n==2
    return all(n%d for d in range(3,math.isqrt(n)+1,2))
@lru_cache(None)
def factor(n):
    if n<1:raise ValueError('positive integer required')
    out=[];d=2
    while d*d<=n:
        if n%d==0:
            e=0
            while n%d==0:n//=d;e+=1
            out.append((d,e))
        d=3 if d==2 else d+2
    if n>1:out.append((n,1))
    return tuple(out)
def divisors_f(F,scale=1):
    out=[1]
    for l,e in F:out=[d*l**f for d in out for f in range(scale*e+1)]
    return sorted(out)
def divisors(n):return divisors_f(factor(n))
def valuation(n,l):
    e=0
    while n%l==0:n//=l;e+=1
    return e
def sf(n):return math.prod(l for l,e in factor(n) if e%2)
def K(n):return math.prod(l**((e+1)//2) for l,e in factor(n))
def fr(x):
    x=Fraction(x);return [x.numerator,x.denominator]
def raw(p,a,u,ch):
    R=4*a-p
    if ch=='E':return (Fraction(a),Fraction(p*a+a*a//u,R),Fraction(p*a+p*p*u,R))
    return (Fraction(a),Fraction(p*(a+a*a//u),R),Fraction(p*(a+u),R))
def normalization(a,u):
    g=math.gcd(a,u);ck(g*g%u==0,'integer grade')
    return g*g//u,u//g,a//g
def state(p,a,u,ch,verify=True):
    R=4*a-p;ck(p<4*a<2*p and a*a%u==0,'original shell and divisor')
    h,r,s=normalization(a,u);G=4*u+1 if ch=='E' else p+4*u
    tails=raw(p,a,u,ch);quot=Fraction(p*r+s if ch=='E' else r+s,R)
    if verify:
        ck(sum((1/x for x in tails),Fraction())==Fraction(4,p),'reciprocal identity')
        ck(h*r*s==a and h*r*r==u and math.gcd(r,s)==1,'normalization inverse')
        ck((sum(tails[1:]).denominator==1)==(G*G%R==0),'first trace iff square gate')
        ck(tails[1].denominator==tails[2].denominator==R//math.gcd(R,G),'exact denominator')
    box=[[l,e,valuation(u,l),valuation(u,l)-e] for l,e in factor(a)]
    return dict(p=p,a=a,R=R,u=u,channel=ch,h=h,r=r,s=s,quotient=fr(quot),
                denominators=[fr(x) for x in tails],full=G%R==0,proper=G%R!=0,
                box=box,defect=R//math.gcd(R,G))
def fullstate(p,a,u,ch):
    z=state(p,a,u,ch)
    ck(z['full'] and all(x[1]==1 for x in z['denominators']),'integral target')
    y=z['denominators'][1][0];num=a*a*(p if ch=='M' else 1);den=z['R']*y-p*a
    ck(num%den==0 and num//den==u,'ordered inverse')
    return z
def ray_reduction(src):
    p,R,r,s=src['p'],src['R'],src['r'],src['s'];m=4*r*s;T=p*r+s
    delta=sf(R);t=math.isqrt(R//delta)
    ck(R==delta*t*t and T*T%R==0,'ray trace input');ck(t*t%m==1,'ray square budget')
    ap=(p+delta)//4;hp=ap//(r*s);out=fullstate(p,ap,hp*r*r,'E')
    ck((out['r'],out['s'])==(r,s),'ray retained')
    ck(ap<=src['a'] and (not src['proper'] or ap<src['a']),'strict proper E descent')
    B1={x[0]:x[3] for x in src['box'] if x[3]};B2={x[0]:x[3] for x in out['box'] if x[3]}
    ck(B1==B2,'centered exponents retained')
    ans=dict(delta=delta,t=t,exterior=out)
    if (delta+1)%m==0:
        H=(delta+1)//m;Tq=T//delta;RM=(s+Tq)//r;aM=H*s*Tq;uM=H*s*s
        mid=fullstate(p,aM,uM,'M')
        ck((mid['h'],mid['r'],mid['s'],mid['quotient'])==(H,s,Tq,[r,1]),'M coordinate return')
        ck(mid['R']==RM and 4*H*s*r-1==delta,'retained cofactor')
        if src['proper']:ck(min(RM,delta)<R,'cofactor descent')
        ans['middle']=mid
    return ans
def mixed_reduction(src,c,q):
    p,a,R,u=src['p'],src['a'],src['R'],src['u']
    ck(p%24==1 and c in (1,2,3,6) and q>3 and prime_trial(q) and a==c*q,'mixed domain')
    ck(pow(q,(p-1)//2,p)==p-1,'carrier nonresidue')
    delta=sf(R);ap=(p+delta)//4
    if src['channel']=='E':
        ck(u%q==0 and (u//q) in divisors(c*c),'carrier exponent one')
        ans=ray_reduction(src);ck('middle' in ans and 6%(src['r']*src['s'])==0,'mixed E allowed')
        return dict(c=c,q=q,source=src,kind='E-ray',**ans)
    eps=int(u%(q*q)==0);u0=a*a//u if eps else u
    ck(u0 in divisors(c*c) and 36%u0==0,'M small word')
    mid0=fullstate(p,ap,u0,'M');up=ap*ap//u0 if eps else u0;out=fullstate(p,ap,up,'M')
    ck(ap<=a and (not src['proper'] or ap<a),'strict proper M descent')
    if eps:ck(out['denominators'][1:]==list(reversed(mid0['denominators'][1:])),'M orientation')
    return dict(c=c,q=q,source=src,kind='M-word',delta=delta,t=math.isqrt(R//delta),
                orientation=eps,u0=u0,middle=out)
def shell_hits(p,a):
    R=4*a-p;out=[]
    for u in divisors_f(factor(a),2):
        if (4*u+1)%R==0:out.append(['E',u])
        if (p+4*u)%R==0:out.append(['M',u])
    return out
def CRT(a,m,b,n):
    ck(math.gcd(m,n)==1,'CRT coprime')
    return (a+m*((b-a)*pow(m,-1,n)%n))%(m*n),m*n
def nextprime_class(b,m,lower):
    z=lower+1+(b-lower-1)%m
    while not prime_trial(z):z+=m
    return z
def family(r,s):
    m=4*r*s;b=next(x for x in range(1,m,4) if math.gcd(x,m)==1 and x*x%m!=1)
    low=max(7,r,s,abs(r*r-s*s));t=nextprime_class(b,m,low)
    delta=nextprime_class(-pow(b*b,-1,m)%m,m,max(low,t));R=delta*t*t;L=math.lcm(840,m)
    e=next(l for l in (11,19,23,31,43,47,59,67,71,79,83) if math.gcd(l,L*R)==1)
    target=((delta*t-s)*pow(r,-1,R))%R
    res,mod=CRT(1,L,target,R);res,mod=CRT(res,mod,-1,e)
    threshold=max(R,(s*R*R)//(4*r)+1,e+4)
    ck(math.gcd(res,mod)==1 and R%m==m-1,'reduced prime progression')
    ck(t%4==1 and delta%4==3,'residual prime types')
    ck(not [k for k in divisors(R) if k%t==0 and k%m==1],'ray return absent')
    sample=res+mod*max(0,(threshold-res)//mod+1)
    h=(sample+R)//m;a=h*r*s;u=h*r*r
    ck(math.gcd(R,sample*r+s)==delta*t,'exact trace defect')
    ck(4*K(u)>R,'fixed word budget too large')
    ck(((4*(a*a//u)+1)**2)%R!=0,'E complement not trace')
    return dict(r=r,s=s,m=m,b=b,t=t,delta=delta,R=R,endpoint_prime=e,residue=res,
                modulus=mod,lower_threshold=threshold,sample_integer=sample,
                sample_primality_not_asserted=True)
def exact_examples():
    ex=[]
    for p,c,q,a,u in [(1129,3,139,417,1251),(2689,2,569,1138,569),
                       (6841,6,409,2454,1636),(1009,3,107,321,9)]:
        ch='M' if (p,a,u)==(1009,321,9) else 'E'
        ck(prime_trial(p) and prime_trial(q),'example primes');src=state(p,a,u,ch)
        ck(src['proper'] and sum((Fraction(*x) for x in src['denominators'][1:]),Fraction()).denominator==1,
           'proper trace example')
        rec=mixed_reduction(src,c,q);rec['old_shell_hits']=shell_hits(p,a)
        rec['word_deletions']=[k for k in divisors(src['R']) if k%src['defect']==0 and k%(4*K(u))==1]
        ex.append(rec)
    p=9601;a=2956;u=8;delta=sf(4*a-p);ap=(p+delta)//4
    ck(prime_trial(p) and prime_trial(739) and a==4*739,'c4 primes')
    neg=dict(source=state(p,a,u,'M'),c=4,q=739,delta=delta,target_a=ap,
             target_box=divisors_f(factor(ap),2),target_hits=shell_hits(p,ap),
             alternative=fullstate(p,(p+19)//4,65,'M'))
    ck(not neg['target_hits'],'c4 sf target both channels empty')
    p=6975049201;R=378359;r=5;s=3;h=(p+R)//60;a=h*r*s;u=h*r*r;T=p*r+s
    ck(prime_trial(p),'large prime certified by trial division')
    ck(factor(T)==((2,3),(71,1),(73,1),(841097,1)),'whole ray factors')
    raystates=[d for d in divisors(T) if d<p and (p+d)%60==0]
    ck(not raystates,'whole third ray empty');oldhits=shell_hits(p,a);ck(not oldhits,'whole old shell empty')
    src=state(p,a,u,'E');kr=[k for k in divisors(R) if k%src['defect']==0 and k%60==1]
    kw=[k for k in divisors(R) if k%src['defect']==0 and k%(4*K(u))==1]
    ck(not kr and not kw,'both fixed-data descents fail');c=(p+1)//11;j=3
    large=dict(source=src,prime_trial_cutoff=math.isqrt(p),ray_integer=T,ray_factorization=factor(T),
               ray_divisors=divisors(T),ray_states=raystates,old_box=divisors_f(factor(a),2),
               old_hits=oldhits,ray_deletions=kr,word_deletions=kw,
               canonical_progression=[3479012041,3496037160],canonical_progression_index=1,
               alternative=fullstate(p,j*c,j,'M'))
    ck(p==3479012041+3496037160,'progression point')
    controls={}
    for p in (2521,3361):
        packs=[]
        for c in (1,2,3,6):
            for q in primes((p-1)//(2*c)):
                if q<=3 or 4*c*q<=p:continue
                a=c*q;RR=4*a-p
                tr=[(ch,u) for u in divisors_f(factor(a),2)
                    for ch,G in [('E',4*u+1),('M',p+4*u)] if G*G%RR==0]
                packs.append(dict(c=c,q=q,a=a,R=RR,traces=tr))
        ck(all(not z['traces'] for z in packs),'initial mixed-source control')
        rr=[]
        for r,s in RAYS:
            TT=p*r+s;m=4*r*s
            rr.append(dict(r=r,s=s,T=TT,factors=factor(TT),residues=[v for v in divisors(TT) if v<p and (p+v)%m==0]))
        if p==3361:ck(all(not z['residues'] for z in rr),'initial nine-ray control')
        controls[str(p)]=dict(prime_shells=packs,rays=rr)
    return dict(positive=ex,c4_failure=neg,third_ray_failure=large,initial_source_controls=controls)
def scan(bound):
    Ps=[p for p in primes(bound) if p%24==1];counts=Counter();mixed=[];arays=[]
    fh=hashlib.sha256();th=hashlib.sha256();per=[]
    boxes={a:divisors_f(factor(a),2) for a in range(1,bound//2+1)}
    for p in Ps:
        row=Counter();row['p']=p
        for a in range(p//4+1,(p-1)//2+1):
            R=4*a-p;counts['shells']+=1;cq=None
            for c in (1,2,3,6):
                if a%c==0 and a//c>3 and prime_trial(a//c):cq=(c,a//c);break
            for u in boxes[a]:
                counts['original_divisor_words']+=1
                for ch,G in [('E',4*u+1),('M',p+4*u)]:
                    if G*G%R:continue
                    src=state(p,a,u,ch);key=f'{p},{a},{u},{ch}\n'.encode();th.update(key)
                    counts['trace_'+ch]+=1
                    if src['full']:fh.update(key);counts['full_'+ch]+=1;row['full_'+ch]+=1
                    else:counts['proper_'+ch]+=1;row['proper_'+ch]+=1
                    if ch=='E':
                        m=4*src['r']*src['s'];T=p*src['r']+src['s'];d=src['defect'];lhs=[];rhs=[]
                        for k in divisors(R):
                            Rp=R//k
                            if k%d==0 and k%m==1:lhs.append(k)
                            if (p+Rp)%m==0 and T%Rp==0:rhs.append(k)
                        ck(lhs==rhs,'complete ray deletion criterion')
                        if 6%(src['r']*src['s'])==0:
                            ans=ray_reduction(src);ck('middle' in ans,'M partner')
                            arays.append(dict(source=src,**ans));counts['automatic_ray_traces']+=1
                            if src['proper']:counts['automatic_ray_proper']+=1
                    if cq:
                        mixed.append(mixed_reduction(src,*cq));counts['mixed_traces']+=1
                        if src['proper']:counts['mixed_proper']+=1
        per.append(dict(row))
    counts['primes']=len(Ps)
    return dict(bound=bound,counts=dict(counts),full_source_sha256=fh.hexdigest(),trace_source_sha256=th.hexdigest(),
                per_prime=per,mixed=mixed,automatic_rays=arays)
def ray_fibres(bound):
    out=[]
    for p in (p for p in primes(bound) if p%24==1):
        for r,s in RAYS:
            T=p*r+s;m=4*r*s;A=T//2**valuation(T,2)
            direct=[R for R in divisors_f(factor(A),2) if R<p and (p+R)%m==0];fib=[];reb=[]
            for delta in divisors(math.prod(l for l,e in factor(A))):
                if delta%m!=m-1:continue
                ck(delta<p,'automatic bounded delta')
                ts=[t for t in divisors(A//delta) if delta*t*t<p];reb.extend(delta*t*t for t in ts)
                fib.append(dict(delta=delta,t_values=ts,count=len(ts)))
            ck(sorted(reb)==direct,'all marked squarefree fibres')
            out.append(dict(p=p,r=r,s=s,T=T,trace_residuals=direct,fibres=fib))
    return out
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--bound',type=int,default=10000)
    ap.add_argument('--out',type=Path,default=Path('certificates'));args=ap.parse_args()
    if not 73<=args.bound<=100000:ap.error('bound must be between 73 and 100000')
    start=time.monotonic();args.out.mkdir(parents=True,exist_ok=True)
    run=scan(args.bound);fibs=ray_fibres(args.bound);ex=exact_examples()
    fam=[family(r,s) for r in range(1,9) for s in range(1,9) if math.gcd(r,s)==1 and 6%(r*s)!=0]
    for m in range(4,401,4):
        trivial=all(x*x%m==1 for x in range(1,m) if math.gcd(x,m)==1)
        ck(trivial==(24%m==0),'unit-square classification')
    for p in primes(args.bound):
        if p%24==13:
            den=[(p+3)//4,(p+3)*(3*p+1)//32,p*(3*p+1)//4]
            ck(sum((Fraction(1,d) for d in den),Fraction())==Fraction(4,p),'mod13 formula')
    summary=dict(success=True,bound=args.bound,checks=CHECKS,counts=run['counts'],
                 full_source_sha256=run['full_source_sha256'],trace_source_sha256=run['trace_source_sha256'],
                 automatic_rays=RAYS,progression_templates=len(fam),
                 elapsed_seconds=round(time.monotonic()-start,3),universal_ES_proved=False,
                 universal_TypeII_proved=False)
    for name,data in [('scan.json',run),('ray_fibres.json',fibs),('examples.json',ex),('progressions.json',fam),('summary.json',summary)]:
        (args.out/name).write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
    print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
