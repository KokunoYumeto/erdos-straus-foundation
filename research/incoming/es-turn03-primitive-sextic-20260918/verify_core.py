#!/usr/bin/env python3
"""Portable exact checker for the prime primitive triangle and its square exits.
Standard library only; no full-graph or least-prime claim. Run beside input.json
and prime_certificates.json. The larger scan is in the complete research package.
"""
import json
from pathlib import Path
from math import gcd, isqrt, prod
from collections import Counter
from fractions import Fraction

CHECKS=0

def check(ok,label):
    global CHECKS
    CHECKS+=1
    if not ok:raise ArithmeticError(label)

def primes(cert):
    proven=set()
    for key,node in sorted(cert['nodes'].items(),key=lambda pair:int(pair[0])):
        n=int(key);check(n==node['n'] and n>=2,'prime node')
        if node['kind']=='trial':
            check(n<=10000 and all(n%d for d in range(2,isqrt(n)+1)),'trial prime')
        else:
            fs=node['factors'];a=node['base']
            check(len({q for q,e in fs})==len(fs) and all(q in proven and e>0 for q,e in fs),'prime children')
            check(prod(q**e for q,e in fs)==n-1,'full factorization')
            check(1<a<n and pow(a,n-1,n)==1,'order power')
            check(all(gcd(pow(a,(n-1)//q,n)-1,n)==1 for q,e in fs),'order gcds')
        proven.add(n)
    check(set(cert['roots'])<=proven,'all root primes')
    return proven

def divisors(fs):
    ds=[1]
    for q,e in fs:ds=[d*q**j for d in ds for j in range(2*e+1)]
    return sorted(ds)

def character(a,p):
    v=pow(a%p,(p-1)//2,p)
    check(v in (1,p-1),'nonzero quadratic character')
    return 1 if v==1 else -1

def source(p,R,fs,proven):
    check(R>0 and (p+R)%4==0,'shell')
    a=(p+R)//4
    check(a<p and gcd(a*p,R)==1 and all(q in proven and e>0 for q,e in fs),'original units and prime factors')
    check(len({q for q,e in fs})==len(fs) and prod(q**e for q,e in fs)==a,'original factorization')
    ds=divisors(fs);mu=Counter(u*pow(a,-1,R)%R for u in ds)
    E=[u for u in ds if(4*u+1)%R==0];M=[u for u in ds if(u+a)%R==0]
    check(len(ds)==len(set(ds))==prod(2*e+1 for q,e in fs),'original source multiplicity')
    return a,ds,mu,E,M

def main():
    here=Path(__file__).resolve().parent
    data=json.loads((here/'input.json').read_text())
    cert=json.loads((here/'prime_certificates.json').read_text());proved=primes(cert)
    p=data['p'];Q=data['cycle'];rows=[];total=0
    check(p in proved and p%840==121 and Q==[31,223,307],'specified hard prime')
    for i,q in enumerate(Q):
        r=Q[(i+1)%3];bfs=data['inactive_factorizations'][i];fs=sorted(bfs+[[r,1]])
        a,ds,mu,E,M=source(p,q,fs,proved);B=a//r
        K={pow(t,6,q)for t in range(1,q)};W=set(mu)
        check(not E and not M,'complete E/M failure')
        check({u*pow(B,-1,q)%q for u in divisors(bfs)}==K,'inactive saturation')
        actual={k for k in range(1,q)if {k*w%q for w in W}==W}
        check(actual==K and len(K)*6==q-1,'actual full index six')
        occupied={pow(r,j,q)*k%q for j in (-1,0,1)for k in K}
        check(W==occupied and len(W)==3*len(K),'primitive three-coset support')
        check(all(pow(r,j,q)not in K for j in range(1,6)) and pow(r,6,q)in K,'quotient generator')
        check(p*pow(r,-1,q)%q in K and 4 in K,'positive phase')
        edges=[[t,e]for t,e in fs if character(t,p)==-1]
        check(edges==[[r,1]] and character(q,p)==-1,'every eligible edge retained')
        check(all(t not in W for t in (q-1,-p%q,-pow(p,-1,q)%q)),'all target orientations')
        rows.append({'q':q,'r':r,'a':a,'B':B,'K':sorted(K),'mu':sorted(mu.items()),'candidate_count':len(ds),'E':E,'M':M})
        total+=len(ds)
    check(total==1215,'complete vector count')
    ports=[]
    for row in data['ports9']:
        q=row['q'];a,ds,mu,E,M=source(p,9*q,row['factors'],proved)
        edges=[[t,e]for t,e in row['factors']if character(t,p)==-1]
        check(3*q<p and edges and all(t not in Q for t,e in edges),'square-nine escape')
        ports.append({'q':q,'a':a,'edges':edges,'E':E,'M':M})
    w=data['separate_ES_witness'];R=w['R'];u=w['u'];a=(p+R)//4
    check(prod(q**e for q,e in w['factorization_a'])==a and all(q in proved for q,e in w['factorization_a']),'witness factorization')
    d=gcd(a,u);h=d*d//u;r=u//d;s=a//d;k=(p*r+s)//R
    check(a*a%u==0 and R*k==p*r+s,'witness gate')
    triple=[a,h*s*k,p*h*r*k]
    check(sum((Fraction(1,t)for t in triple),Fraction())==Fraction(4,p),'positive original ES identity')
    result={'p':p,'prime_nodes':len(proved),'checks':CHECKS,'triangle':rows,'square_ports':ports,'separate_ES_denominators':triple,'status':'passed','nonclaim':'No universal ES or graph-closure assertion.'}
    (here/'core_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'checks':CHECKS,'prime_nodes':len(proved),'original_vectors':total,'status':'passed'}))

if __name__=='__main__':main()
