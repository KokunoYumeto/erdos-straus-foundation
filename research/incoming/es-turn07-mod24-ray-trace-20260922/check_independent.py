#!/usr/bin/env python3
"""Separate exact replay; imports no main or predecessor module.
Primitive h,r,s enumeration and literal denominator tests replace the main scan.
"""
from __future__ import annotations
import argparse, hashlib, json, math, time
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
C=0

def demand(x,why):
    global C
    C+=1
    if not x:raise ArithmeticError(why)

def prime(n):
    if n<2:return False
    return all(n%k for k in range(2,math.isqrt(n)+1))

@lru_cache(None)
def factors(n):
    out=[];q=2
    while q*q<=n:
        e=0
        while n%q==0:e+=1;n//=q
        if e:out.append((q,e))
        q+=1
    if n>1:out.append((n,1))
    return out

@lru_cache(None)
def divs(n):
    small=[x for x in range(1,math.isqrt(n)+1) if n%x==0]
    return sorted(set(small+[n//x for x in small]))

def factordivs(F):
    out=[1]
    for p,e in F:
        nxt=[]
        for x in out:
            for j in range(e+1):nxt.append(x*p**j)
        out=nxt
    return sorted(out)

def squarepart(n):
    delta=1;t=1
    for p,e in factors(n):
        delta*=p**(e%2);t*=p**(e//2)
    return delta,t

def record_check(z,full=False):
    p,a,R,u,h,r,s=[z[k] for k in ('p','a','R','u','h','r','s')]
    demand(p<4*a<2*p and 4*a-p==R,'shell domain')
    demand(h*r*s==a and h*r*r==u and math.gcd(r,s)==1,'normalized record')
    t=Q(*z['quotient']);ch=z['channel']
    demand(t==Q(p*r+s if ch=='E' else r+s,R),'quotient record')
    d=(Q(a),h*s*t,p*h*r*t) if ch=='E' else (Q(a),p*h*s*t,p*h*r*t)
    demand(d==tuple(Q(*x) for x in z['denominators']),'ordered denominators')
    demand(sum((1/x for x in d),Q())==Q(4,p),'reciprocal equation')
    demand(d[1].denominator==d[2].denominator==z['defect'],'tail denominator')
    if full:demand(all(x.denominator==1 and x>0 for x in d),'full integer target')
    for l,e,f,b in z['box']:
        def vp(n):
            k=0
            while n%l==0:n//=l;k+=1
            return k
        demand(vp(a)==e and vp(u)==f and f-e==b and abs(b)<=e,'original exponent box')

def source_key(z):return z['p'],z['a'],z['u'],z['channel']

def main():
    par=argparse.ArgumentParser();par.add_argument('--input',type=Path,default=Path('certificates'))
    par.add_argument('--out',type=Path,default=Path('certificates/independent.json'));arg=par.parse_args()
    start=time.monotonic();base=arg.input
    dat=json.loads((base/'scan.json').read_text());bound=dat['bound']
    Ps=[p for p in range(73,bound+1,24) if prime(p)]
    counts=Counter();tr=[];fu=[];expect_mixed=set();expect_ray=set()
    # This enumeration does not calculate u from a divisor of a^2.
    for p in Ps:
        for a in range((p+3)//4,(p-1)//2+1):
            R=4*a-p;counts['shells']+=1
            cq=[]
            for c in (1,2,3,6):
                if a%c==0 and a//c>3 and prime(a//c):cq.append((c,a//c))
            demand(len(cq)<=1,'unique prime-cofactor descriptor')
            for r in divs(a):
                for s in divs(a//r):
                    if math.gcd(r,s)!=1:continue
                    h=a//(r*s);u=h*r*r;counts['original_divisor_words']+=1
                    for ch,num in [('E',p*r+s),('M',r+s)]:
                        if num*num%R:continue
                        key=(p,a,u,ch);tr.append(key);counts['trace_'+ch]+=1
                        if num%R==0:fu.append(key);counts['full_'+ch]+=1
                        else:counts['proper_'+ch]+=1
                        # literal rational traces, not merely a modular restatement
                        v=Q(num,R)
                        den=(Q(a),h*s*v,p*h*r*v) if ch=='E' else (Q(a),p*h*s*v,p*h*r*v)
                        demand((den[1]+den[2]).denominator==1,'trace integral')
                        demand(sum((1/x for x in den),Q())==Q(4,p),'rational source identity')
                        if ch=='E' and 6%(r*s)==0:
                            expect_ray.add(key);counts['automatic_ray_traces']+=1
                            if num%R:counts['automatic_ray_proper']+=1
                        if cq:
                            expect_mixed.add(key);counts['mixed_traces']+=1
                            if num%R:counts['mixed_proper']+=1
    counts['primes']=len(Ps)
    def digest(rows):
        hh=hashlib.sha256()
        for p,a,u,ch in sorted(rows):hh.update(f'{p},{a},{u},{ch}\n'.encode())
        return hh.hexdigest()
    demand(dict(counts)==dat['counts'],'complete original source counts')
    demand(digest(tr)==dat['trace_source_sha256'],'complete original trace hash')
    demand(digest(fu)==dat['full_source_sha256'],'complete original full hash')
    demand({source_key(z['source']) for z in dat['automatic_rays']}==expect_ray,'all ray records present')
    demand({source_key(z['source']) for z in dat['mixed']}==expect_mixed,'all mixed records present')
    for rec in dat['automatic_rays']:
        src=rec['source'];record_check(src);record_check(rec['exterior'],True);record_check(rec['middle'],True)
        p,R,r,s=[src[k] for k in ('p','R','r','s')];delta,t=squarepart(R)
        demand((delta,t)==(rec['delta'],rec['t']),'squarefree mark')
        E=rec['exterior'];M=rec['middle']
        demand((E['r'],E['s'],E['R'])==(r,s,delta),'ray preserved')
        demand(M['r']==s and M['quotient']==[r,1] and 4*M['h']*s*r-1==delta,'M crossed label inverse')
        H,J=M['h'],M['s']
        expected_middle=(Q(H*s*J),Q(p*H*J*r),Q(p*H*s*r))
        demand(tuple(Q(*x) for x in M['denominators'])==expected_middle,
               'automatic E-to-M denominator formula')
        demand((4*src['u']+1)**2%R==0,'automatic source E square gate')
        demand(delta*t*t==R and (p*r+s)**2%R==0,'source recovered from fibre')
        B1={l:f-e for l,e,f,b in src['box'] if f!=e};B2={l:f-e for l,e,f,b in E['box'] if f!=e}
        demand(B1==B2,'centered coordinates preserved')
    for rec in dat['mixed']:
        src=rec['source'];record_check(src);record_check(rec['middle'],True)
        c,q=rec['c'],rec['q'];d,t=squarepart(src['R'])
        demand(prime(q) and src['a']==c*q and c in (1,2,3,6),'mixed input')
        if src['channel']=='M':
            eps=rec['orientation'];u0=src['a']**2//src['u'] if eps else src['u']
            demand(c*c%u0==0 and u0==rec['u0'],'M oriented small word')
            a1=(src['p']+d)//4
            expect=a1*a1//u0 if eps else u0
            demand(rec['middle']['u']==expect,'restored target orientation')
    # Inverse-fibre check via literal R-values in the first-half interval.
    fibres=json.loads((base/'ray_fibres.json').read_text())
    for z in fibres:
        p,r,s,T=z['p'],z['r'],z['s'],z['T'];m=4*r*s
        Rs=[R for R in range(3,p,4) if (p+R)%m==0 and T*T%R==0]
        demand(Rs==z['trace_residuals'],'independent full R-list')
        wanted={}
        for R in Rs:
            dd,tt=squarepart(R);wanted.setdefault(dd,[]).append(tt)
        got={v['delta']:v['t_values'] for v in z['fibres']}
        demand(wanted==got,'independent fibre multiplicities')
    ex=json.loads((base/'examples.json').read_text())
    for z in ex['positive']:
        record_check(z['source']);record_check(z['middle'],True)
        if 'exterior' in z:record_check(z['exterior'],True)
    neg=ex['c4_failure'];record_check(neg['source']);record_check(neg['alternative'],True)
    demand(neg['source']['a']==4*739 and prime(739),'c4 prime')
    ng=neg['source']['p']+4*neg['source']['u'];nR=neg['source']['R']
    demand(ng*ng%nR==0 and ng%nR!=0,'c4 proper M source square gate')
    aa=neg['target_a'];RR=4*aa-9601
    demand(neg['target_box']==divs(aa*aa),'complete c4 target divisor box')
    for u in neg['target_box']:demand(aa*aa%u==0 and (4*u+1)%RR and (u+aa)%RR,'complete failed c4 target')
    z=ex['third_ray_failure'];record_check(z['source']);record_check(z['alternative'],True)
    p=z['source']['p'];ff=[(2,4),(3,1),(5,2),(7,1),(830363,1)]
    demand(math.prod(q**e for q,e in ff)==p-1,'complete p-1 factors')
    for q,e in ff:demand(prime(q),'Lucas factor prime')
    demand(pow(11,p-1,p)==1,'Lucas full power')
    lucas=[]
    for q,e in ff:
        residue=pow(11,(p-1)//q,p);g=math.gcd(residue-1,p)
        demand(g==1,'Lucas order factor')
        lucas.append(dict(q=q,residue=residue,gcd=g))
    # Full factor-order certificate proves the large example prime, independently of trial through sqrt(p).
    demand(math.prod(q**e for q,e in z['ray_factorization'])==5*p+3,'ray factor product')
    for q,e in z['ray_factorization']:demand(prime(q),'ray factor prime')
    dd=factordivs(z['ray_factorization']);demand(dd==z['ray_divisors'],'full divisor box on third ray')
    demand(not [R for R in dd if R<p and (p+R)%60==0],'whole genuine third ray empty')
    aa=z['source']['a'];RR=z['source']['R']
    zg=4*z['source']['u']+1
    demand(zg*zg%RR==0 and zg%RR!=0,'large proper E source square gate')
    demand(z['old_box']==factordivs([(l,2*e) for l,e in factors(aa)]),'old a-square complete')
    for u in z['old_box']:demand((4*u+1)%RR and (u+aa)%RR,'old source gates absent')
    for fam in json.loads((base/'progressions.json').read_text()):
        r,s,m,b,t,de,R=[fam[k] for k in ('r','s','m','b','t','delta','R')]
        demand(prime(t) and prime(de) and b%4==1 and b*b%m!=1,'progression auxiliary primes')
        a,M=fam['residue'],fam['modulus']
        demand(math.gcd(a,M)==1 and a%840==1 and a%m==1,'reduced hard progression')
        demand((r*a+s)%R==de*t and (a+1)%fam['endpoint_prime']==0,'linear progression identities')
        ks=[t,t*t,de*t,de*t*t]
        demand(all(k%m!=1 for k in ks),'all potential deleting factors forbidden')
    # Explicit false transformations, each with a deterministic arithmetic rejection.
    controls={
       'same_word_not_ray':285**2%1251!=0,
       'radical_not_squarefree_part':squarepart(1863)==(23,9) and math.prod(q for q,e in factors(1863))==69,
       'drop_hard_class':(37+3)//4==10 and (4*2+1)%3==0 and 2%5!=0,
       'drop_prime_carrier':not prime(841) and 841**2%29==0 and (4*29+1)%3==0,
       'drop_R_less_p':7**3>97 and 98**2%(7**3)==0,
       'c4_sf_target_failure':not neg['target_hits'],
       'third_ray_saturation_failure':not z['ray_states'] and z['source']['proper'],
       'distinct_M_orientations':any(x.get('orientation')==1 for x in dat['mixed'])}
    # p97: R343 divides (p+1)^2 but exceeds p, and is excluded from the fibre.
    for k,v in controls.items():demand(v,'negative control '+k)
    rep=dict(success=True,bound=bound,checks=C,counts=dict(counts),
             full_source_sha256=digest(fu),trace_source_sha256=digest(tr),
             large_prime_certificate=dict(p=p,base=11,p_minus_one_factors=ff,
                                          full_power=pow(11,p-1,p),
                                          order_witnesses=lucas,
                                          sqrt_floor=math.isqrt(p)),
             negative_controls=controls,elapsed_seconds=round(time.monotonic()-start,3),
             universal_ES_proved=False)
    arg.out.parent.mkdir(parents=True,exist_ok=True);arg.out.write_text(json.dumps(rep,indent=2,sort_keys=True)+'\n')
    print(json.dumps(rep,indent=2))
if __name__=='__main__':main()
