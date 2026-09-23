#!/usr/bin/env python3
"""Original ES boxes, mixed-order sections and labelled upward factor exchange.
Python 3.9+, standard library only. No universal ES success assertion.
"""
from __future__ import annotations
from fractions import Fraction
from itertools import product
from math import gcd, isqrt, prod
from pathlib import Path
import argparse, json


def need(ok: bool, msg: str = 'verification failure') -> None:
    if not ok:
        raise ValueError(msg)


def dump(path, obj):
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes((json.dumps(obj, sort_keys=True, indent=2)+'\n').encode('utf-8'))


def sieve(n):
    need(n >= 1)
    a = bytearray(b'\1')*(n+1); a[:2] = b'\0\0'
    for q in range(2,isqrt(n)+1):
        if a[q]: a[q*q::q] = b'\0'*((n-q*q)//q+1)
    return a


def factor(n):
    need(n >= 1); f={}; q=2
    while q*q<=n:
        if n%q==0:
            e=0
            while n%q==0: n//=q; e+=1
            f[q]=e
        q=3 if q==2 else q+2
    if n>1:f[n]=1
    return f


def spf(n):
    a=list(range(n+1))
    for q in range(2,isqrt(n)+1):
        if a[q]==q:
            for t in range(q*q,n+1,q):
                if a[t]==t:a[t]=q
    return a


def factor_spf(n,table):
    f={}
    while n>1:
        q=table[n]; e=0
        while n%q==0:n//=q;e+=1
        f[q]=e
    return f


def divs_f(f):
    out=[1]
    for q,e in sorted(f.items()):out=[d*q**j for d in out for j in range(e+1)]
    return sorted(out)


def divisors(n):return divs_f(factor(n))


def trial_prime(n):
    return n>=2 and (n==2 or n%2 and all(n%q for q in range(3,isqrt(n)+1,2)))


def fr(q):
    q=Fraction(q);return [q.numerator,q.denominator]


def order(q,m):
    need(m>1 and gcd(q,m)==1)
    z=1
    for o in range(1,m+1):
        z=z*q%m
        if z==1:return o
    raise ValueError('unit order not found')


def residual(R):
    f=factor(R);D=prod(q**(e//2) for q,e in f.items());return R//D,D,R//(D*D)


def state(p,a,u,channel):
    need(p>1 and p%4==1 and p<4*a<2*p and gcd(p,a)==1)
    need(channel in ('E','M') and u>0 and a*a%u==0)
    R=4*a-p;g=gcd(a,u);h=g*g//u;r=u//g;s=a//g
    need(h*r*s==a and h*r*r==u and gcd(r,s)==1)
    if channel=='E':
        quotient=Fraction(p*r+s,R);tails=[h*s*quotient,p*h*r*quotient];G=4*u+1
    else:
        quotient=Fraction(r+s,R);tails=[p*h*s*quotient,p*h*r*quotient];G=p+4*u
    need(Fraction(1,a)+1/tails[0]+1/tails[1]==Fraction(4,p))
    K,D,delta=residual(R);z=pow(p,int(channel=='E'),R)*u*pow(a,-1,R)%R
    trace=(z+1)%K==0;defect=((z+1)//K)%D if trace else None
    need(trace==(G*G%R==0))
    f=factor(a);fu=factor(u)
    return dict(p=p,a=a,R=R,u=u,channel=channel,h=h,r=r,s=s,
        quotient_name='kappa' if channel=='E' else 'lambda',quotient=fr(quotient),
        denominators=[fr(a),*[fr(x) for x in tails]],trace=trace,full=G%R==0,
        K=K,D=D,delta=delta,defect=defect,common_denominator=R//gcd(R,G),
        exponents=[dict(prime=q,e=e,f=fu.get(q,0),beta=fu.get(q,0)-e) for q,e in sorted(f.items())])


def convolution(D,steps,lengths):
    need(D>=1 and len(steps)==len(lengths) and all(n>=1 for n in lengths))
    a=[0]*D;a[0]=1
    for l,n in zip(steps,lengths):
        b=[0]*D
        for x,c in enumerate(a):
            if c:
                for t in range(n):b[(x+l*t)%D]+=c
        a=b
    return a


def chain_data(D,steps,lengths,indices):
    need(D>=1 and len(steps)==len(lengths) and all(n>0 for n in lengths))
    need(len(set(indices))==len(indices))
    g=D;rows=[]
    for i in indices:
        need(0<=i<len(steps));d=gcd(g,steps[i]);m=g//d
        need(m>1 and lengths[i]>=m,'chain capacity fails')
        rows.append(dict(index=i,before=g,after=d,radix=m,step=steps[i]%D,
                         full_blocks=lengths[i]//m))
        g=d
    need(g==1,'chain does not reach the whole group')
    lower=prod(lengths[i] for i in range(len(steps)) if i not in indices)
    lower*=prod(z['full_blocks'] for z in rows)
    return dict(D=D,indices=list(indices),rows=rows,lower=lower)


def best_chain(D,steps,lengths):
    """Best block lower bound among every feasible strict gcd chain.
    Exact divisor DAG. Effective edges cannot reuse an earlier coordinate.
    """
    need(D>=1 and len(steps)==len(lengths) and all(n>0 for n in lengths))
    score={D:Fraction(1)};path={D:[]};edges=0
    for g in reversed(divisors(D)):
        if g not in score:continue
        for i,(l,n) in enumerate(zip(steps,lengths)):
            d=gcd(g,l);m=g//d
            if m<=1 or n<m:continue
            edges+=1;value=score[g]*Fraction(n//m,n)
            if d not in score or value>score[d] or value==score[d] and path[g]+[i]<path[d]:
                score[d]=value;path[d]=path[g]+[i]
    if 1 not in score:
        return dict(lower=0,indices=[],reachable=sorted(score),edges=edges)
    out=chain_data(D,steps,lengths,path[1]);value=prod(lengths)*score[1]
    need(value.denominator==1 and int(value)==out['lower'])
    out.update(reachable=sorted(score),edges=edges);return out


def decode(D,steps,indices,target):
    """Inverse of the literal mixed-radix digit section; carries retained."""
    g=D;rows=[]
    for i in indices:
        d=gcd(g,steps[i]);m=g//d;need(m>1)
        rows.append((i,g,d,m));g=d
    need(g==1)
    c=target%D;answer={}
    for i,before,after,m in reversed(rows):
        need(c%after==0)
        t=(c//after)*pow((steps[i]//after)%m,-1,m)%m
        answer[i]=t;c=(c-steps[i]*t)%D
        need(c%before==0)
    need(c==0 and sum(steps[i]*t for i,t in answer.items())%D==target%D)
    return answer


def section_vector(D,steps,lengths,indices,target,blocks=None,unused=None):
    """Choose full blocks and actual unused digits, then invert exactly."""
    cert=chain_data(D,steps,lengths,indices);blocks={} if blocks is None else blocks
    unused={} if unused is None else unused;vec=[0]*len(steps);offset=0
    selected=set(indices)
    for i,n in enumerate(lengths):
        if i not in selected:
            v=unused.get(i,0);need(0<=v<n);vec[i]=v;offset+=steps[i]*v
    for row in cert['rows']:
        i=row['index'];b=blocks.get(i,0)
        need(0<=b<row['full_blocks']);v=b*row['radix'];vec[i]=v;offset+=steps[i]*v
    digits=decode(D,steps,indices,target-offset)
    for i,t in digits.items():vec[i]+=t
    need(all(0<=v<n for v,n in zip(vec,lengths)))
    need(sum(l*v for l,v in zip(steps,vec))%D==target%D)
    return vec


def unit_lower(D,steps,lengths):
    if D==1:return prod(lengths)
    units=[i for i,l in enumerate(steps) if gcd(l,D)==1]
    if sum(lengths[i]-1 for i in units)<D-1:return 0
    return prod(lengths[i] for i in range(len(lengths)) if i not in units)


def tile_parts(p,a,fa=None):
    """Complete original coarse partition, not a generated support surrogate."""
    fa=factor(a) if fa is None else fa
    R=4*a-p;K,D,delta=residual(R);qs=sorted(fa);blocks=[]
    for q in qs:
        e=fa[q];o=order(q,K);by={}
        for beta in range(-e,e+1):by.setdefault(beta%o,[]).append(beta)
        lam=((pow(q,o,R)-1)//K)%D
        blocks.append([dict(base=v[0],length=len(v),order=o,step=lam) for _,v in sorted(by.items())])
    for eta in (0,1):
        for piece in product(*blocks):
            z=pow(p,eta,R)
            for q,row in zip(qs,piece):z=z*pow(q,row['base'],R)%R
            if (z+1)%K:continue
            target=((z+1)//K)%D
            yield dict(p=p,a=a,R=R,K=K,D=D,delta=delta,channel='E' if eta else 'M',
                primes=qs,exponents=[fa[q] for q in qs],parts=list(piece),target=target)


def tile_word(tile,vec):
    return prod(q**(e+b['base']+b['order']*v)
                for q,e,b,v in zip(tile['primes'],tile['exponents'],tile['parts'],vec))


def plus_cells(p,C):
    """Every original integral labelled cell in one plus-factor fibre."""
    need(p>1 and p%4==1 and C>0)
    M=p+C;out=[]
    for s in divisors(M):
        N=M//s;R=C-s
        if N%4!=1 or not 0<R<p:continue
        n=(N-1)//4;a=n*s
        need(4*a-p==R and p<4*a<2*p and n>=1)
        out.append(dict(p=p,C=C,M=M,s=s,n=n,a=a,R=R))
    return sorted(out,key=lambda x:(x['a'],x['s']))


def plus_targets(p,C):
    """Complete unit-ray E targets among the labelled cells."""
    out=[]
    for cell in plus_cells(p,C):
        if cell['M']%cell['R']:continue
        rec=state(p,cell['a'],cell['n'],'E')
        need(rec['full'] and rec['r']==1 and rec['s']==cell['s'])
        need(Fraction(*rec['quotient'])==cell['M']//cell['R']-1)
        out.append(dict(cell=cell,state=rec))
    return out


def plus_return(rec):
    """All targets after retaining C=R+s from this canonical orientation."""
    return plus_targets(rec['p'],rec['R']+rec['s'])


def plus_inverse(target,proper_only=False):
    """Complete canonical original trace inputs for a marked r=1 E target.
    M words already encode their order. E tail swapping is separately available.
    """
    need(target['full'] and target['channel']=='E' and target['r']==1)
    p=target['p'];C=target['R']+target['s'];out=[]
    for cell in plus_cells(p,C):
        for r in divisors(cell['n']):
            if gcd(r,cell['s'])!=1:continue
            u=cell['n']*r
            for tag in ('E','M'):
                rec=state(p,cell['a'],u,tag)
                if rec['trace'] and (not proper_only or not rec['full']):
                    need(rec['s']==cell['s']);out.append(rec)
    return sorted(out,key=lambda t:(t['a'],t['channel'],t['u']))


def lucas_tree(numbers):
    """Construct full n-1 order certificates; leaves are trial-division proofs."""
    nodes={}
    def add(n):
        if n in nodes:return
        need(n>=2)
        if n<10000:
            need(trial_prime(n));nodes[n]=dict(n=n,type='trial',bound=isqrt(n));return
        f=factor(n-1)
        for q in f:add(q)
        a=2
        while a<n:
            if pow(a,n-1,n)==1 and all(gcd(pow(a,(n-1)//q,n)-1,n)==1 for q in f):break
            a+=1
        need(a<n,'full-order primality certificate not found')
        nodes[n]=dict(n=n,type='order',base=a,factors=[[q,e] for q,e in sorted(f.items())],
            power=pow(a,n-1,n),gcds=[[q,gcd(pow(a,(n-1)//q,n)-1,n)] for q in sorted(f)])
    for n in numbers:add(n)
    return dict(roots=list(numbers),nodes=[nodes[n] for n in sorted(nodes)])


def main():
    p=argparse.ArgumentParser();p.add_argument('--p',type=int);p.add_argument('--a',type=int)
    p.add_argument('--u',type=int);p.add_argument('--channel',choices=['E','M'],default='M')
    args=p.parse_args();need(all(x is not None for x in [args.p,args.a,args.u]))
    rec=state(args.p,args.a,args.u,args.channel)
    need(trial_prime(args.p),'input is not prime')
    print(json.dumps(dict(source=rec,plus_targets=plus_return(rec)),indent=2,sort_keys=True))

if __name__=='__main__':main()
