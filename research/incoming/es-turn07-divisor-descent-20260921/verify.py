#!/usr/bin/env python3
"""Exact ES divisor descent; standard library, no assertion-based validations."""
from __future__ import annotations
import argparse, hashlib, json, time
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from math import gcd, isqrt, lcm, prod
from pathlib import Path

CHECKS=0
SAFE=(1,2,3,4,6,9,12,18,36)
HARD={1,121,169,289,361,529}
def check(x:bool,message:str)->None:
    global CHECKS
    CHECKS+=1
    if not x:raise ArithmeticError(message)
@lru_cache(None)
def factors(n:int)->tuple:
    if n<1:raise ValueError('positive integer required')
    ans=[];q=2
    while q*q<=n:
        if n%q==0:
            e=0
            while n%q==0:n//=q;e+=1
            ans.append((q,e))
        q=3 if q==2 else q+2
    if n>1:ans.append((n,1))
    return tuple(ans)
@lru_cache(None)
def divisors(n:int,power:int=1)->tuple:
    out=[1]
    for q,e in factors(n):out=[d*q**i for d in out for i in range(power*e+1)]
    return tuple(sorted(out))
def K(n:int)->int:return prod(q**((e+1)//2) for q,e in factors(n))
def squarepart(n:int)->int:return prod(q**(e//2) for q,e in factors(n))
def omega(n:int)->int:return sum(e for _,e in factors(n))
def phi(n:int)->int:return prod((q-1)*q**(e-1) for q,e in factors(n))
def square_group_order(m:int)->int:
    return prod(2**max(0,e-3) if q==2 else (q-1)*q**(e-1)//2 for q,e in factors(m))
def prime(n:int)->bool:
    if n<2:return False
    if n%2==0:return n==2
    return all(n%d for d in range(3,isqrt(n)+1,2))
def sieve(n:int)->list:
    a=bytearray(b'\x01')*(n+1);a[0:2]=b'\x00\x00'
    for q in range(2,isqrt(n)+1):
        if a[q]:a[q*q:n+1:q]=b'\x00'*((n-q*q)//q+1)
    return [i for i in range(2,n+1) if a[i]]
def enc(x:Fraction)->list:return [x.numerator,x.denominator]
def G_value(p:int,u:int,c:str)->int:return 4*u+(1 if c=='E' else p)
def triple(p:int,a:int,u:int,c:str)->tuple:
    R=4*a-p
    if c=='E':return (Fraction(a),Fraction(p*a+a*a//u,R),Fraction(p*a+p*p*u,R))
    return (Fraction(a),Fraction(p*(a+a*a//u),R),Fraction(p*(a+u),R))
def state(p:int,a:int,u:int,c:str)->dict:
    R=4*a-p
    check(p<4*a<2*p and a*a%u==0,'original state domain')
    g=gcd(a,u);h=g*g//u;r=u//g;s=a//g
    check(h*r*s==a and h*r*r==u and gcd(r,s)==1,'normalization')
    if c=='E':
        check((p*r+s)%R==0,'E gate');v=(p*r+s)//R
        xyz=(a,h*s*v,p*h*r*v);name='kappa'
    else:
        check((r+s)%R==0,'M gate');v=(r+s)//R
        xyz=(a,p*h*s*v,p*h*r*v);name='lambda'
    check(all(x>0 for x in xyz),'positive return')
    check(4*prod(xyz)==p*(xyz[0]*xyz[1]+xyz[0]*xyz[2]+xyz[1]*xyz[2]),'identity')
    N=a*a*(p if c=='M' else 1);D=R*xyz[1]-p*a
    check(D>0 and N==u*D,'labelled inverse')
    return dict(p=p,a=a,R=R,u=u,channel=c,h=h,r=r,s=s,**{name:v},denominators=list(xyz))
def residue_poly(n:int,m:int,power:int=1)->dict:
    c={1:1}
    for q,e in factors(n):
        z=Counter()
        for g,v in c.items():
            for j in range(e+1):z[g*pow(q,power*j,m)%m]+=v
        c=dict(z)
    return c

def repairs(p:int,a:int,u:int,c:str,detailed:bool=False)->dict:
    R=4*a-p;G=G_value(p,u,c);m=4*K(u)
    check(p<4*a<2*p and a*a%u==0 and G*G%R==0,'relaxed source')
    d=R//gcd(R,G);t=squarepart(R);q0=K(d)
    check(R%(d*d)==0 and t%q0==0,'denominator range')
    ks=[d*v for v in divisors(R//d) if d*v%m==1]
    poly=residue_poly(R//d,m)
    check(poly.get(pow(d,-1,m),0)==len(ks),'coefficient count')
    check(sum(poly.values())==len(divisors(R//d)),'geometric multiplicities')
    qs=[q0*v for v in divisors(t//q0) if (q0*v)**2%m==1]
    sp=residue_poly(t//q0,m,2)
    check(sp.get(pow(q0*q0,-1,m),0)==len(qs),'square coefficient')
    check([k for k in ks if isqrt(k)**2==k]==sorted(q*q for q in qs),'square subset')
    if ks:check(min(omega(k//d) for k in ks)<=phi(m)-1,'word length bound')
    if qs:check(min(omega(q//q0) for q in qs)<=square_group_order(m)-1,'square word length')
    if 36%u==0:
        check(qs==[q0*v for v in divisors(t//q0)],'automatic square domain')
        check(len(qs)==prod(e+1 for _,e in factors(t//q0)),'automatic multiplicity')
        check(q0*q0 in ks,'automatic descent')
    xyz=triple(p,a,u,c)
    check(sum(1/x for x in xyz)==Fraction(4,p),'rational identity')
    check((xyz[1]+xyz[2]).denominator==1,'first trace')
    check(xyz[1].denominator==xyz[2].denominator==d,'exact denominator')
    targets=[]
    for k in ks:
        R1=R//k;a1=(p+R1)//4
        check(R1%4==3 and (p+R1)%4==0 and a1*a1%u==0,'target budget')
        check(G%R1==0 and (d==1 or a1<a),'full gate and descent')
        ret=state(p,a1,u,c)
        old=dict(factors(a));new=dict(factors(a1));uf=dict(factors(u))
        for ell in set(old)|set(new)|set(uf):
            f=uf.get(ell,0)
            check(f<=2*old.get(ell,0) and f<=2*new.get(ell,0),'actual exponents')
        targets.append(dict(removal=k,target=ret))
    ustar=a*a//u
    comp=G_value(p,ustar,c)**2%R==0
    check(comp==(c=='M' or (p*p-1)%K(R)==0),'complement domain')
    if c=='M':check(triple(p,a,ustar,c)[1:]==(xyz[2],xyz[1]),'orientation')
    row=dict(p=p,a=a,R=R,u=u,channel=c,denominator=d,budget_modulus=m,
             square_root_part=t,minimum_square_factor=q0,removals=ks,
             square_removals=[q*q for q in qs],complement=ustar,
             complement_is_trace=comp,targets=targets)
    if detailed:
        row.update(rational_denominators=[enc(x) for x in xyz],
            tail_trace=enc(xyz[1]+xyz[2]),original_a_factors=list(factors(a)),
            word_factors=list(factors(u)),original_R_factors=list(factors(R)),
            coefficient_table=sorted(poly.items()),square_coefficient_table=sorted(sp.items()))
    return row

def scan(bound:int)->tuple:
    total=Counter();rows=[];prs=[]
    for p in sieve(bound):
        if p%4!=1:continue
        total['primes']+=1;pc=Counter()
        for R in range(3,p,4):
            a=(p+R)//4;total['shells']+=1
            for u in divisors(a,2):
                total['original_divisor_vectors']+=1
                for c in ('E','M'):
                    G=G_value(p,u,c)
                    if G%R==0:
                        total['integral_'+c]+=1;pc['integral_'+c]+=1
                        state(p,a,u,c)
                        full=repairs(p,a,u,c)
                        check(full['denominator']==1 and 1 in full['removals'],
                              'integral-source identity return')
                        total['integral_returned_records']+=len(full['removals'])
                        if any(k>1 for k in full['removals']):
                            total['integral_nontrivial_return_sources']+=1
                        continue
                    if G*G%R:continue
                    row=repairs(p,a,u,c);check(row['denominator']>1,'proper marking')
                    rows.append(row);total['proper_'+c]+=1;pc['proper_'+c]+=1
                    if row['removals']:
                        total['repairable_'+c]+=1;pc['repairable_'+c]+=1
                        total['returned_records']+=len(row['removals'])
                    if row['square_removals']:total['square_repairable_'+c]+=1
                    if 36%u==0:total['automatic_seed_sources']+=1
        prs.append(dict(p=p,**pc))
    rows.sort(key=lambda x:(x['p'],x['R'],x['u'],x['channel']))
    total['distinct_returned_states']=len({(r['p'],t['target']['a'],r['u'],r['channel']) for r in rows for t in r['targets']})
    # Verify the complete inverse fibres, not only the forward aggregate.
    fibres={}
    for row in rows:
        for t in row['targets']:
            key=(row['p'],t['target']['R'],row['u'],row['channel'])
            fibres.setdefault(key,[]).append(t['removal'])
    for (p,R1,u,c),oldks in fibres.items():
        G=G_value(p,u,c);m=4*K(u)
        expected=[k for k in range(1,(p-1)//R1+1) if k%m==1 and
                  G*G%(R1*k)==0 and G%(R1*k)!=0]
        check(sorted(oldks)==expected,'complete inverse fibre')
    total['distinct_target_fibres']=len(fibres)
    return dict(total),rows,prs

def crt_pair(a:int,m:int,b:int,n:int)->tuple:
    g=gcd(m,n)
    if (b-a)%g:raise ValueError('incompatible CRT')
    v=n//g;k=((b-a)//g*pow(m//g,-1,v))%v if v>1 else 0
    return (a+m*k)%(m*v),m*v

def progression(seed:int)->dict:
    m=4*K(seed)
    if 36%seed==0:raise ValueError('automatic seed')
    b=next(b for b in range(1,m,4) if gcd(b,m)==1 and b*b%m!=1)
    threshold=max(seed,seed*seed-3*seed+1,7)
    delta=(-b*b)%m
    delta+=max(0,(threshold+1-delta+m-1)//m)*m
    while not prime(delta):delta+=m
    t=pow(b,-1,m)
    t+=max(0,(max(seed,7)+1-t+m-1)//m)*m
    while not prime(t) or t==delta:t+=m
    L=lcm(840,m);R=delta*t*t
    e=3
    while not prime(e) or gcd(e,L*R)>1:e+=4
    a0,mod=crt_pair(1,L,delta*t-4*seed,R)
    a0,mod=crt_pair(a0,mod,-1,e)
    check(gcd(a0,mod)==1 and gcd(L,R)==1,'reduced progression')
    check(delta%4==3 and t%4==1 and delta>threshold,'auxiliary primes')
    check((delta*t*t+1)%m==0 and (delta+1)%m!=0 and (delta*t+1)%m!=0,'three budget phases')
    check(gcd(R,a0+4*seed)==delta*t,'single exact pole')
    check(a0%840==1 and (a0+1)%e==0,'hard and endpoint')
    j=(delta+1)//4
    check(j*j%seed!=0,'unavailable canonical cofactor word')
    check(not any(w%delta==seed for w in divisors(j,2)),'entire fixed cofactor box empty')
    return dict(u=seed,m=m,unit=b,delta=delta,t=t,R=R,L=L,endpoint_prime=e,
                residue=a0,modulus=mod,strict_prime_lower_bound=max(R,e,squarepart(seed)*R),
                j=j,cofactor_divisors=list(divisors(j,2)))

def fixtures()->dict:
    inputs=[('automatic_composite',1009,321,9,'M'),
            ('mixed_square_factors',1108801,279295,5,'M'),
            ('partial_square_only',51361,14845,5,'M'),
            ('nonsquare_after_complement',1009,286,11,'E'),
            ('previous_failed_word',1009,286,7436,'E'),
            ('small_exterior',37,16,2,'E'),
            ('complement_boundary',29,14,2,'E'),
            ('sharp_failure',48116881,12032220,8,'M'),
            ('integral_multireturn_15',41,14,1,'M'),
            ('integral_multireturn_27',173,50,4,'M')]
    out={}
    for name,p,a,u,c in inputs:
        check(prime(p),'fixture primality by complete trial division')
        out[name]=repairs(p,a,u,c,True)
    check(out['automatic_composite']['removals']==[25],'automatic example')
    check(not any(G_value(1009,u,c)%275==0 for u in divisors(321,2) for c in ('E','M')),'old shell empty')
    check(out['mixed_square_factors']['square_removals']==[441],'mixed square resource')
    check(out['partial_square_only']['square_removals']==[81],'partial square resource')
    check(out['nonsquare_after_complement']['removals']==[45],'nonsquare deletion')
    check(out['previous_failed_word']['removals']==[] and out['previous_failed_word']['complement']==11,'old word obstruction')
    check(out['integral_multireturn_15']['denominator']==1 and
          out['integral_multireturn_15']['removals']==[1,5],
          'integral source with nontrivial divisor return at residual 15')
    check(out['integral_multireturn_27']['denominator']==1 and
          out['integral_multireturn_27']['removals']==[1,9],
          'integral source with nontrivial divisor return at residual 27')
    fail=out['sharp_failure'];p=fail['p'];a=fail['a'];u=fail['u']
    check(fail['removals']==[] and fail['denominator']==13,'terminal original word')
    ustar=a*a//u
    check(gcd(fail['R'],G_value(p,ustar,'M'))==
          gcd(fail['R'],G_value(p,u,'M'))==71*13,
          'terminal complement exact denominator')
    mstar=4*a//squarepart(u)
    check(mstar>fail['R'] and mstar==4*K(a*a//u),'terminal complement modulus')
    check(not any(k%(mstar)==1 and k%13==0 for k in divisors(fail['R'])),'terminal complement')
    delta=71;j=18
    table=[[w,w%delta] for w in divisors(j,2)]
    check(all(res!=8 for _,res in table),'complete cofactor71 box')
    c=(p+1)//11
    out['endpoint']=dict(E=state(p,(p+11)//4,(p+11)//4,'E'),M=state(p,3*c,3,'M'))
    out['sharp_failure']['cofactor_table']=table
    out['sharp_failure']['complement_budget_modulus']=mstar
    out['sharp_failure']['prime_trial_bound']=isqrt(p)
    return out

def abstract_checks(limit:int)->dict:
    rows=[]
    for u in range(1,limit+1):
        m=4*K(u);units=[v for v in range(m) if gcd(v,m)==1]
        sq={v*v%m for v in units}
        check((len(sq)==1)==(36%u==0),'exact automatic seed classification')
        check(len(sq)==square_group_order(m),'square group order')
        check((24%m==0)==(36%u==0),'budget divisors24')
        rows.append([u,m,len(sq)])
    return dict(bound=limit,rows=rows)

def negatives(ex:dict)->list:
    tests=[]
    def reject(name,statement):
        check(not statement,'false implication not rejected: '+name);tests.append(name)
    reject('Removing only a denominator always preserves the word',3%ex['mixed_square_factors']['budget_modulus']==1)
    reject('A minimal square factor always suffices',ex['mixed_square_factors']['minimum_square_factor']**2%20==1)
    reject('Removing every square always suffices',27**2%20==1)
    reject('Every valid deletion is a square',isqrt(45)**2==45)
    reject('Every E trace complement stays in the domain',ex['complement_boundary']['complement_is_trace'])
    reject('The previous failed divisor can be silently kept',bool(ex['previous_failed_word']['removals']))
    reject('All seeds are automatic',16 in [r[1] for r in abstract_checks(8)['rows'] if r[2]==1])
    reject('A nonempty rational trace ensures cofactor71 occupancy',any(w%71==8 for w in divisors(18,2)))
    end=ex['endpoint']['M']
    reject('The terminal source disproves ES',
           sum(Fraction(1,x) for x in end['denominators'])!=Fraction(4,end['p']))
    mixed=ex['mixed_square_factors']
    reject('Reducing the integer coefficient modulo two preserves its target count',
           len(mixed['removals'])%2==len(mixed['targets']))
    return tests

def write(path:Path,obj)->None:
    """Write canonical UTF-8/LF JSON on every supported platform."""
    path.write_bytes((json.dumps(obj,sort_keys=True,indent=2)+'\n').encode('utf-8'))
def main()->None:
    parser=argparse.ArgumentParser();parser.add_argument('--bound',type=int,default=3000)
    parser.add_argument('--seed-bound',type=int,default=100);parser.add_argument('--out',type=Path,default=Path('certificates'))
    args=parser.parse_args()
    if args.bound<5 or args.seed_bound<8:raise ValueError('bounds too small')
    start=time.monotonic();args.out.mkdir(parents=True,exist_ok=True)
    counts,rows,prs=scan(args.bound)
    ex=fixtures();ab=abstract_checks(200)
    pro=[progression(u) for u in range(1,args.seed_bound+1) if 36%u]
    check(next(x for x in pro if x['u']==8)['residue']==48116881,'printed progression')
    neg=negatives(ex)
    write(args.out/'sources.json',rows);write(args.out/'scan.json',dict(bound=args.bound,counts=counts,primes=prs))
    write(args.out/'examples.json',ex);write(args.out/'progressions.json',dict(bound=args.seed_bound,rows=pro))
    write(args.out/'abstract.json',ab)
    hashes={name:hashlib.sha256((args.out/name).read_bytes()).hexdigest() for name in ('sources.json','scan.json','examples.json','progressions.json','abstract.json')}
    summary=dict(success=True,bound=args.bound,counts=counts,checks=CHECKS,rejected_false_implications=neg,
                 mathematical_sha256=hashes,universal_ES_proved=False,universal_trace_source_occupancy_proved=False)
    write(args.out/'summary.json',summary)
    write(args.out/'execution.json',dict(elapsed_seconds=time.monotonic()-start,checks=CHECKS,success=True))
    print(json.dumps(summary,sort_keys=True,indent=2))
if __name__=='__main__':main()
