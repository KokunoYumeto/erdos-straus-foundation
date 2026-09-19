#!/usr/bin/env python3
"""Small standalone proof checker for the displayed closed failure components.
No imports from the main verifier. Does not establish leastness or scan coverage.
"""
from pathlib import Path
from itertools import product
from math import gcd,isqrt,prod
import argparse,json
COUNT=0

def require(b,why):
    global COUNT; COUNT+=1
    if not b:raise ArithmeticError(why)

def prime(n):return n>1 and all(n%d for d in range(2,isqrt(n)+1))

def fac(n):
    ans=[];d=2
    while d*d<=n:
        e=0
        while n%d==0:e+=1;n//=d
        if e:ans.append((d,e))
        d+=1
    if n>1:ans.append((n,1))
    return ans

def subgroup(gs,R):
    known={1};todo=[1]
    while todo:
        x=todo.pop()
        for g in gs:
            y=x*g%R
            if y not in known:known.add(y);todo.append(y)
    return known

def verify(C):
    p=C['p'];cyc=C['cycle_identity']['cycle'];ns={n['q']:n for n in C['nodes']}
    require(prime(p),'parameter primality');require(len(cyc)>=2 and len(set(cyc))==len(cyc),'simple cycle')
    cs=[];sg=[];total=0
    for i,q in enumerate(cyc):
        require(prime(q) and q<p and pow(q,(p-1)//2,p)==p-1,'original NR vertex')
        n=ns[q];s=1 if q%4==3 else 3;R=s*q;a=(p+R)//4
        ff=fac(a);require(n['sigma']==s and n['R']==R and n['a']==a,'source coordinates')
        require(n['factors']==[list(z) for z in ff],'factor completeness')
        adj=[(r,e) for r,e in ff if pow(r,(p-1)//2,p)==p-1]
        require(n['edges']==[list(z) for z in adj] and all(r in cyc for r,e in adj),'all-edge closure')
        nxt=cyc[(i+1)%len(cyc)];require(nxt in [r for r,e in adj],'cycle connectivity')
        require(sum(e for r,e in adj)%2==1,'weighted character parity')
        cs.append(a//nxt);sg.append(s)
        mu={};E=[];M=[]
        for b in product(*(range(-e,e+1) for r,e in ff)):
            u=prod(r**(e+t) for (r,e),t in zip(ff,b));v=u*pow(a,-1,R)%R
            mu[v]=mu.get(v,0)+1
            if (4*u+1)%R==0:E.append(u)
            if (u+a)%R==0:M.append(u)
            require(a*a%u==0,'original availability');total+=1
        require(not E and not M,'both complete gates fail')
        require(n['mu']==[list(z) for z in sorted(mu.items())],'all original coefficients')
        W=set(mu);K={t for t in W if {t*x%R for x in W}==W};G=subgroup([-1,2]+[r for r,e in ff],R)
        ob=n['obstruction'];require(ob['K']==sorted(K) and ob['effective_index']==len(G)//len(K),'actual kernel and effective index')
    D=4**len(cyc)*prod(cs);S=prod(sg);T=[]
    for start in range(len(cyc)):
        t=0;den=1
        for i in range(len(cyc)):
            j=(start+i)%len(cyc);t=sg[j]*t+den;den*=4*cs[j]
        T.append(t)
    h=gcd(*T);require((D-S)==p*h and [t//h for t in T]==cyc,'cycle integer return')
    for key,value in [('D',D),('S',S),('T_rotations',T),('h',h),('cofactors',cs),('sigma',sg)]:require(C['cycle_identity'][key]==value,'retained cycle datum '+key)
    return {'p':p,'vertices':len(cyc),'original_divisor_vectors':total,'cycle':cyc,'effective_indices':[ns[q]['obstruction']['effective_index'] for q in cyc]}

def main():
    a=argparse.ArgumentParser(description=__doc__);a.add_argument('--input',default='certificates/traps.json');a.add_argument('--out',default='trap_check.json');arg=a.parse_args()
    data=json.loads(Path(arg.input).read_text());rows=[verify(c) for c in data['components']]
    for sol in data['genuine_ES_returns']:
        p=sol['p'];x,y,z=sol['denominators'];require(min(x,y,z)>0 and 4*x*y*z==p*(x*y+x*z+y*z),'retained ES countercontrol')
    ans={'checks':COUNT,'components':rows,'scope':'displayed closed components and genuine ES returns; not a full prime scan or leastness proof'}
    Path(arg.out).write_text(json.dumps(ans,sort_keys=True,indent=2)+'\n');print(json.dumps(ans,sort_keys=True))
if __name__=='__main__':main()
