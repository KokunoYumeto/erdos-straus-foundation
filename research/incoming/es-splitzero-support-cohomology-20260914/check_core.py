#!/usr/bin/env python3
"""Compact public exact checks for the two SplitZero support preprints.
Python 3.10+, standard library. No check is disabled by -O.
This is not the larger 507774-condition local verifier or independent review.
"""
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
from math import comb, gcd, isqrt
from pathlib import Path
import argparse, json

CHECKS=0

def check(ok):
    global CHECKS
    CHECKS+=1
    if not ok: raise ArithmeticError('exact certificate failed')

def rank(A):
    A=[list(map(Q,row)) for row in A]
    r=0
    if not A:return 0
    for c in range(len(A[0])):
        p=next((i for i in range(r,len(A)) if A[i][c]),None)
        if p is None:continue
        A[r],A[p]=A[p],A[r];v=A[r][c];A[r]=[x/v for x in A[r]]
        for i in range(r+1,len(A)):
            v=A[i][c];A[i]=[x-v*y for x,y in zip(A[i],A[r])]
        r+=1
        if r==len(A):break
    return r

def dot(a,b):return sum((x*y for x,y in zip(a,b)),Q())
def add(*vs):return [sum(x,Q()) for x in zip(*vs)]
def mul(c,v):return [c*x for x in v]
def observe(M,v):return [dot(row,v) for row in M]

@lru_cache(None)
def factor(n):
    if n<1:raise ValueError('positive input required')
    out=[];p=2
    while p*p<=n:
        e=0
        while n%p==0:n//=p;e+=1
        if e:out.append((p,e))
        p=3 if p==2 else p+2
    if n>1:out.append((n,1))
    return tuple(out)

@lru_cache(None)
def divisors(a):
    ds=[1]
    for p,e in factor(a):ds=[x*p**j for x in ds for j in range(2*e+1)]
    return tuple(sorted(ds))

def mixed():
    ds=divisors(118);n=len(ds);e=lambda u:[Q(v==u) for v in ds];z=[Q()]*n
    obs=[[[Q(u%p==v) for u in ds] for v in sorted({u%p for u in ds})] for p in (3,7,11)]
    U=[]
    for p,M in zip((3,7,11),obs):
        bs=[]
        for v in sorted({u%p for u in ds}):
            us=[u for u in ds if u%p==v]
            bs.extend(add(e(u),mul(-1,e(us[0]))) for u in us[1:])
        check(all(not any(observe(M,b)) for b in bs));check(len(bs)==n-rank(M));U.append(bs)
    a=add(e(13924),mul(-1,e(1)));v=add(e(3481),mul(-1,e(2)));w=add(e(6962),mul(-1,e(4)))
    b=add(v,w);r=add(e(59),mul(-1,e(4)));s=add(e(3481),mul(-1,e(236)));c=add(r,s)
    intersections=[(0,1,[a,b]),(0,2,[c]),(1,2,[])]
    for i,j,bs in intersections:
        check(all(not any(observe(obs[i]+obs[j],x)) for x in bs))
        check(len(bs)==n-rank(obs[i]+obs[j]))
        sumrank=rank(list(zip(*(U[i]+U[j]))))
        check(len(U[i])+len(U[j])-sumrank-len(bs)==0)
    B=[mul(-1,a)+a+z,mul(-1,b)+b+z,mul(-1,c)+z+c]
    g=mul(-1,add(v,r))+v+r
    check(not any(add(g[:n],g[n:2*n],g[2*n:])))
    check(all(not any(observe(obs[i],g[i*n:(i+1)*n])) for i in range(3)))
    G=[[dot(x,y) for y in B] for x in B]
    check(G==[[4,0,0],[0,8,2],[0,2,8]])
    check([dot(x,g) for x in B]==[0,5,5])
    gh=add(g,mul(Q(-1,2),B[1]),mul(Q(-1,2),B[2]))
    check(all(dot(x,gh)==0 for x in B))
    check((dot(g,g),dot(gh,gh),dot(add(g,mul(-1,gh)),add(g,mul(-1,gh))))==(8,3,5))
    check(sum(map(len,U))-rank(list(zip(*sum(U,[]))))-rank(list(zip(*B)))==1)
    idx={u:i for i,u in enumerate(ds)}
    for l,A,Bb,C in product(range(-2,3),repeat=4):
        zz=add(mul(l,g),mul(A,B[0]),mul(Bb,B[1]),mul(C,B[2]));u2=zz[n:2*n];u3=zz[2*n:]
        ll=u3[idx[59]]-u3[idx[3481]];CC=u3[idx[3481]];v2=add(u2,mul(-ll,v))
        check((ll,v2[idx[13924]],v2[idx[3481]],CC)==(l,A,Bb,C))
    target=[observe(obs[0],z),observe(obs[1],r),observe(obs[2],z)]
    for i,j,lift in [(0,1,add(v,r)),(0,2,z),(1,2,r)]:
        check(observe(obs[i],lift)==target[i] and observe(obs[j],lift)==target[j])
    M=sum(obs,[]);t=sum(target,[])
    check(rank(M)==9 and rank([row+[y] for row,y in zip(M,t)])==10)
    return {'divisors':ds,'kernel_ranks':list(map(len,U)),'boundary_Gram':G,
            'cycle':g,'harmonic_cycle':gh,'norms':[8,3,5],'mixed_rank':1,
            'local_marginals':target,'global_rank':9,'augmented_rank':10}

def sparse_add(*xs):
    out=Counter()
    for x in xs:
        for k,v in x.items():out[k]+=v
    return {k:v for k,v in out.items() if v}

def boundary(mask):
    out={};j=0
    for i in range(mask.bit_length()):
        if mask>>i&1:out[mask^(1<<i)]=(-1)**j;j+=1
    return out

def wedge(i,mask):
    if mask>>i&1:return {}
    return {mask|(1<<i):(-1)**((mask&((1<<i)-1)).bit_count())}

def apply(f,x):return sparse_add(*({j:v*w for j,w in f(i).items()} for i,v in x.items()))

def complexes():
    for r in range(8):
        for mask in range(1<<r):
            x={mask:Q(1)};dx=apply(boundary,x)
            check(not apply(boundary,dx))
            for average in (False,True):
                def hb(m):
                    inds=range(r) if average else range(min(r,1))
                    return sparse_add(*({j:Q(v,r if average else 1) for j,v in wedge(i,m).items()} for i in inds))
                hx=apply(hb,x)
                check(not apply(hb,hx))
                check(sparse_add(apply(boundary,hx),apply(hb,dx))==(x if r else {}))
            # Full binomial complex and all truncation errors on this block.
        for cut in range(r+1):
            E=sum((-1)**j*comb(r,j) for j in range(cut+1))
            check(E==int(r==0)+((-1)**cut*comb(r-1,cut) if r>cut else 0))
    return {'complete_failed_blocks':list(range(8)),'integral_and_average_homotopies':True}

def shell(p,a):
    R=4*a-p
    if p%4!=1 or not p<4*a or not 2*a<p or gcd(p*a,R)!=1:raise ValueError('original shell domain')
    tests=[(l,j) for l,k in factor(R) for j in range(1,k+1)]
    count=Counter();hits=[]
    for u in divisors(a):
        for ch in ('E','M'):
            g=4*u+1 if ch=='E' else u+a;D=R//gcd(R,g)
            mask=sum((g%(l**j)!=0)<<i for i,(l,j) in enumerate(tests));count[mask]+=1
            check((D==1)==(mask==0))
            if D==1:
                d=gcd(a,u);h=d*d//u;r=u//d;s=a//d
                q=(p*r+s)//R if ch=='E' else (r+s)//R
                xyz=(a,h*s*q,p*h*r*q) if ch=='E' else(a,p*h*s*q,p*h*r*q)
                check(sum((Q(1,x) for x in xyz),Q())==Q(4,p))
                check(Q((p if ch=='M' else 1)*a*a,R*xyz[1]-p*a)==u)
                hits.append(dict(p=p,a=a,R=R,c=ch,u=u,h=h,r=r,s=s,quotient=q,denominators=xyz))
    dims=[sum(n*comb(mask.bit_count(),j) for mask,n in count.items()) for j in range(len(tests)+1)]
    check(sum((-1)**j*d for j,d in enumerate(dims))==len(hits))
    return dict(p=p,a=a,R=R,tests=tests,masks=sorted(count.items()),dimensions=dims,hits=hits)

def scan(bound):
    sieve=bytearray(b'\1')*(bound+1);sieve[:2]=b'\0\0'
    for q in range(2,isqrt(bound)+1):
        if sieve[q]:sieve[q*q::q]=b'\0'*len(sieve[q*q::q])
    stats=Counter()
    for p in range(13,bound+1,12):
        if not sieve[p]:continue
        stats['primes']+=1;m=(p-1)//4
        for a in range(m+1,2*m+1):
            rec=shell(p,a);stats['shells']+=1;stats['original_states']+=rec['dimensions'][0];stats['hits']+=len(rec['hits'])
            stats['occupied_shells' if rec['hits'] else 'empty_shells']+=1
    return dict(stats)

def encode(x):
    if isinstance(x,Q):return {'n':x.numerator,'d':x.denominator}
    if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [encode(v) for v in x]
    return x

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--bound',type=int,default=1500);ap.add_argument('--out',default='public_checks.json');args=ap.parse_args()
    if args.bound<13:ap.error('bound >=13 required')
    out={'mixed':mixed(),'complexes':complexes(),'examples':[shell(1129,396),shell(2689,781),shell(1129,285)],'scan':scan(args.bound)}
    check(out['examples'][0]['dimensions']==[150,378,313,85] and not out['examples'][0]['hits'])
    check(out['examples'][1]['dimensions']==[18,36,24,5] and len(out['examples'][1]['hits'])==1)
    out['checks']=CHECKS;out['bound']=args.bound
    out['scope']='Compact exact checks only; no independent review, general arithmetic positivity, or Lean build.'
    Path(args.out).write_text(json.dumps(encode(out),sort_keys=True,indent=2)+'\n')
    print(json.dumps({'checks':CHECKS,'scan':out['scan']},sort_keys=True))
if __name__=='__main__':main()
