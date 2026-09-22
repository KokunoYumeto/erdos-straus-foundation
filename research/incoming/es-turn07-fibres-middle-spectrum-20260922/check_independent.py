#!/usr/bin/env python3
"""Independent bounded arithmetic check. Imports no main or predecessor modules.
It uses original positive factor pairs for rational inputs, and primitive
(h,r,s) triples for target enumeration, rather than the main divisor-word scan.
"""
from __future__ import annotations
import argparse,json,hashlib
from math import gcd,isqrt
from fractions import Fraction as Q
from functools import lru_cache
from collections import defaultdict
from pathlib import Path
C=0

def ck(x,msg):
    global C
    C+=1
    if not x:raise ArithmeticError(msg)
@lru_cache(None)
def prime(n):return n>1 and all(n%d for d in range(2,isqrt(n)+1))
@lru_cache(None)
def ff(n):
    ans=[];d=2
    while d*d<=n:
        if n%d==0:
            e=0
            while n%d==0:n//=d;e+=1
            ans.append((d,e))
        d+=1
    if n>1:ans.append((n,1))
    return tuple(ans)
@lru_cache(None)
def divs(n):
    out=[1]
    for l,e in ff(n):
        current=[]
        for b in out:
            x=b
            for _ in range(e+1):current.append(x);x*=l
        out=current
    return sorted(out)
def sf(n):
    ans=1
    for l,e in ff(n):
        if e%2:ans*=l
    return ans
@lru_cache(None)
def cq(a):
    out=[(c,a//c)for c in (1,2,3,6)if a%c==0 and a//c>3 and prime(a//c)]
    ck(len(out)<=1,'carrier uniqueness')
    return out[0]if out else None

def norm(a,u):
    g=gcd(a,u);return g*g//u,u//g,a//g

def run(src,out):
    data=json.loads((src/'fibres.json').read_text());bound=data['bound'];groups=defaultdict(dict);targets=set();rawcount=0
    for p in range(25,bound+1,24):
        if not prime(p):continue
        for a in range(p//4+1,(p+1)//2):
            R=4*a-p
            # Primitive three-factor enumeration, including both orientations.
            for r in divs(a):
                for s in divs(a//r):
                    if gcd(r,s)!=1 or (r+s)%R:continue
                    h=a//(r*s);lam=(r+s)//R
                    yy=p*h*s*lam;zz=p*h*r*lam
                    targets.add((p,a,min(yy,zz),max(yy,zz)))
            carrier=cq(a)
            if not carrier:continue
            c,q=carrier;N=p*a
            # Enumerate the ordered literal factor pair (b,N^2/b).
            # p is prime and p does not divide a, so these are exactly all
            # divisors of N^2; no expensive re-factorization of p^2 is needed.
            for b in sorted(v*p**k for v in divs(a*a) for k in (0,1,2)):
                comp=N*N//b
                if (2*N+b+comp)%R:continue
                yy=Q(N+b,R);zz=Q(N+comp,R)
                ck(Q(1,a)+1/yy+1/zz==Q(4,p),'original factor-pair reciprocal equality')
                if b%p:
                    ch='E';u=a*a//b;swap=0
                elif comp%p:
                    ch='E';u=a*a//comp;swap=1
                else:
                    ch='M';u=p*a*a//b;swap=0
                ck(a*a%u==0,'recovered original divisor')
                h,r,s=norm(a,u);delta=sf(R)
                if ch=='E':
                    HH=(delta+1)//(4*r*s);JJ=(p*r+s)//delta
                    ap=HH*s*JJ;YY=p*HH*r*s;ZZ=p*HH*r*JJ
                else:
                    seed=u if u%q else a*a//u
                    ap=(p+delta)//4;gh=gcd(ap,seed);hh=gh*gh//seed;rr=seed//gh;ss=ap//gh
                    ck((rr+ss)%delta==0,'returned M gate')
                    ll=(rr+ss)//delta;YY=p*hh*ll*min(rr,ss);ZZ=p*hh*ll*max(rr,ss)
                ck(Q(1,ap)+Q(1,YY)+Q(1,ZZ)==Q(4,p),'actual target identity')
                key=(p,ap,YY,ZZ);sk=(p,a,ch,u,swap)
                ck(sk not in groups[key],'ordered factor-pair labels not duplicated')
                groups[key][sk]=([yy.numerator,yy.denominator],[zz.numerator,zz.denominator]);rawcount+=1
    expected_targets={tuple(f['target'][k]for k in ('p','a','Y','Z'))for f in data['fibres']}
    ck(targets==expected_targets,'complete target list by independent primitive enumeration')
    seen=[];nonempty=0;cross=0;t1missing=0
    for f in data['fibres']:
        key=tuple(f['target'][k]for k in ('p','a','Y','Z'))
        listed={(x['p'],x['a'],x['channel'],x['u'],x['swap']):x for x in f['sources']}
        ck(set(listed)==set(groups[key]),f'complete source fibre at {key}')
        nonempty+=bool(listed);cross+=set(x[2]for x in listed)=={'E','M'}
        t1missing+=bool(listed)and all(x['t']>1 for x in listed.values())
        for k,r in listed.items():
            ck(tuple(r['tails'])==groups[key][k],'original ordered rational tails retained')
            ck(r['R']==4*r['a']-r['p'] and r['R']==r['delta']*r['t']**2,'source squarefree parameter')
            oldh,oldr,olds=norm(r['a'],r['u']);ck((oldh,oldr,olds)==(r['h'],r['r'],r['s']),'normalization inverse')
            seen.append(list(k))
    sha=hashlib.sha256(json.dumps(sorted(seen),sort_keys=True,separators=(',',':')).encode()).hexdigest()
    summary=json.loads((src/'fibre_summary.json').read_text())
    ck(sha==summary['source_key_sha256'],'complete original source-key digest')
    ck(nonempty==summary['counts']['image_targets']and cross==summary['counts']['cross_channel_targets'],'image and cross-channel counts')
    ck(t1missing==summary['counts']['targets_without_t1_source'],'missing t=1 counts')
    report=dict(success=True,bound=bound,checks=C,ordered_sources=rawcount,all_M_targets=len(targets),image_targets=nonempty,
                cross_channel_targets=cross,targets_without_t1_source=t1missing,source_key_sha256=sha,
                imports_no_main_or_predecessor_code=True,universal_ES_proved=False)
    out.write_bytes((json.dumps(report,indent=2,sort_keys=True)+'\n').encode('utf-8'));print(json.dumps(report,sort_keys=True))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--input',type=Path,default=Path('certificates'));p.add_argument('--out',type=Path,default=Path('independent.json'))
    a=p.parse_args();run(a.input,a.out)
