#!/usr/bin/env python3
"""Separate standard-library checker: direct divisors, Jacobi reciprocity,
all-unit stabilizers, polynomial remainders and square-table prime characters.
Imports neither verify.py nor predecessor research code.
"""
import argparse
from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd, isqrt, prod
from pathlib import Path
import json

CHECKS=0

def must(ok,label):
    global CHECKS
    CHECKS+=1
    if not ok:raise ArithmeticError(label)

def jacobi(a,n):
    if n<=0 or not n&1:raise ValueError('odd positive Jacobi denominator')
    a%=n;out=1
    while a:
        while not a&1:
            a//=2
            if n%8 in (3,5):out=-out
        a,n=n,a
        if a%4==n%4==3:out=-out
        a%=n
    return out if n==1 else 0

def primality(cert):
    proved=set()
    for text,row in sorted(cert['nodes'].items(),key=lambda t:int(t[0])):
        n=int(text);must(n==row['n'] and n>=2,'prime node identifier')
        if row['kind']=='trial':
            must(n<=10000 and all(n%d for d in range(2,isqrt(n)+1)),'full trial primality')
        else:
            fs=row['factors'];a=row['base']
            must(len({q for q,e in fs})==len(fs) and all(q in proved and e>=1 for q,e in fs),'previously proved factor primes')
            must(prod(q**e for q,e in fs)==n-1,'complete group-order factorization')
            must(1<a<n and pow(a,n-1,n)==1,'Fermat relation')
            must(all(gcd(pow(a,(n-1)//q,n)-1,n)==1 for q,e in fs),'full primitive-order congruences')
        proved.add(n)
    must(set(cert['roots'])<=proved,'all original prime roots proved')
    return proved

def divisor_list(fs,exponent_multiplier=2):
    if not fs:return [1]
    q,e=fs[0];tail=divisor_list(fs[1:],exponent_multiplier);ans=[]
    power=1
    for _ in range(exponent_multiplier*e+1):
        ans.extend(power*v for v in tail);power*=q
    return sorted(ans)

def ord_mod(x,q):
    v=x%q;j=1
    while v!=1:v=v*x%q;j+=1
    return j

def return_check(state):
    p=state['p'];R=state['R'];a=state['a'];u=state['u'];x,y,z=state['denominators']
    must(a==x and 4*a==p+R and a*a%u==0,'ordered original source')
    must(Fraction(1,x)+Fraction(1,y)+Fraction(1,z)==Fraction(4,p),'exact Fraction reciprocal identity')
    h,r,s=state['h'],state['r'],state['s'];must(h*r*s==a and h*r*r==u and gcd(r,s)==1,'normalized coordinate inverse')
    if state['channel']=='E':
        k=state['kappa'];must(R*k==p*r+s and y==h*s*k and z==p*h*r*k,'exterior marking')
        must(Fraction(a*a,R*y-p*a)==u,'exterior ordered inverse')
    else:
        l=state['lambda'];must(R*l==r+s and y==p*h*s*l and z==p*h*r*l,'middle marking')
        must(Fraction(p*a*a,R*y-p*a)==u,'middle ordered inverse')

def triangle_check(inp,result,proved):
    p=inp['p'];Q=inp['cycle'];total=0
    must(p in proved and p%840 in {1,121,169,289,361,529},'hard prime')
    for i,q in enumerate(Q):
        row=result['nodes'][i];r=Q[(i+1)%3];a=(p+q)//4;B=a//r
        fs=sorted(inp['inactive_factorizations'][i]+[[r,1]])
        must(all(t in proved for t,e in fs) and prod(t**e for t,e in fs)==a,'full original factorization')
        ds=divisor_list(fs);total+=len(ds);mu=Counter((u*pow(a,-1,q))%q for u in ds)
        E=[u for u in ds if (4*u+1)%q==0];M=[u for u in ds if (u+a)%q==0]
        must(not E and not M,'complete local failure both gates')
        must(sorted(mu.items())==[tuple(v)for v in row['mu']],'every fine coefficient')
        must(sorted(w['u']for w in row['words'])==ds and len(set(w['u']for w in row['words']))==len(ds),'all original word labels once')
        for w in row['words']:
            actual=[]
            for t,e in fs:
                v=w['u'];j=0
                while v%t==0:v//=t;j+=1
                actual.append(j-e)
            must(actual==w['beta'] and w['residue']==w['u']*pow(a,-1,q)%q,'word exponent record')
        W=set(mu);K=[k for k in range(1,q)if {k*w%q for w in W}==W]
        must(K==row['K'] and len(K)*6==q-1,'all-unit actual stabilizer')
        Wb={u*pow(B,-1,q)%q for u in divisor_list(inp['inactive_factorizations'][i])}
        must(Wb==set(K),'actual inactive saturation')
        Gsize=1
        for g in [-1,2]+[t for t,e in fs]:
            o=ord_mod(g,q);Gsize=Gsize*o//gcd(Gsize,o)
        must(Gsize==q-1,'full coefficient group order')
        outgoing=[[t,e]for t,e in fs if jacobi(t,p)==-1]
        must(outgoing==[[r,1]] and jacobi(q,p)==-1,'all-edge closure not a selected cycle')
        target=[q-1,(-p)%q,(-pow(p,-1,q))%q]
        must(all(t not in W for t in target) and target==row['targets'],'all targets and orientations')
        must(Q[i-1]*r*r%q==row['neighbor_carry'] and all(pow(x,6,q)==row['neighbor_carry']for x in row['sixth_roots']),'retained neighbor carry')
        if q==307:must(all(ord_mod(r*k,q)%18==0 for k in K),'non-split cubic extension')
    must(total==1215,'full original divisor count')
    c=[row['B']for row in result['nodes']];D=64*prod(c);T=[1+4*c[i]+16*c[i]*c[(i+1)%3]for i in range(3)];h=gcd(*T)
    must((D-1)//h==p and [t//h for t in T]==Q,'cycle integer inverse')

def pmul(a,b):
    c=0
    while b:
        if b&1:c^=a
        a<<=1;b>>=1
    return c

def prem(a,b):
    while a and a.bit_length()>=b.bit_length():a^=b<<(a.bit_length()-b.bit_length())
    return a

def algebra_check(expected):
    f1=5;f2=21;modulus=65 # X^2+1, X^4+X^2+1, X^6+1
    must(pmul(f1,f2)==modulus,'coprime CRT factorization')
    pairs={(prem(p,f1),prem(p,f2))for p in range(64)}
    must(len(pairs)==64,'complete remainder bijection')
    P=35;E=9;e0=21
    must(prem(P,f1)==1 and prem(P,f2)==E,'cubic jet is 1+X^3, not absent')
    must(prem(pmul(E,E),f2)==0 and E!=0,'nonzero nilpotent cubic jet')
    must(prem(pmul(P,P),modulus)==e0,'squaring changes cubic jet')
    for row in expected['all_64_coordinate_maps']:
        p=sum(b<<i for i,b in enumerate(row['X_coefficients']));(a,b),(c,d)=row['dual_coordinates']
        must(prem(p,f1)==(a^b)^(b<<1),'rational dual coordinates')
        # In the cubic quotient, omega=X^4 and epsilon=1+X^3.
        cp=(c&1)^((c>>1&1)<<4);dp=(d&1)^((d>>1&1)<<4)
        must(prem(p,f2)==prem(cp^pmul(E,dp),f2),'cubic dual coordinate inverse by polynomial remainder')

def cubic_check(inp,expected):
    H=expected['primary_matrix'];K=expected['conjugate_matrix'];EE=expected['rational_norm_matrix'];Q=inp['cycle']
    for i,q in enumerate(Q):
        a,b=inp['eisenstein_primary'][i];z=expected['omega_images'][i]
        must(a%3==1 and b%3==0 and a*a-a*b+b*b==q,'primary norm and orientation')
        must((a+b*z)%q==0 and (z*z+z+1)%q==0,'Eisenstein quotient map')
        for j,r in enumerate(Q):
            if i==j:continue
            c,d=inp['eisenstein_primary'][j]
            must(pow((c+d*z)%q,(q-1)//3,q)==pow(z,H[i][j],q),'primary cubic symbol')
            must(pow((c-d-d*z)%q,(q-1)//3,q)==pow(z,K[i][j],q),'conjugate cubic symbol')
            must(pow(r,(q-1)//3,q)==pow(z,EE[i][j],q),'rational norm cubic symbol')
            must(H[i][j]==H[j][i] and (K[i][j]+K[j][i])%3==0,'reciprocity agrees with exact table')

def ports_check(inp,result,proved):
    p=inp['p'];Q=set(inp['cycle'])
    for row in result['ports']:
        q=row['q'];a=(p+9*q)//4;fs=row['factors'];ds=divisor_list(fs)
        must(all(t in proved for t,e in fs) and prod(t**e for t,e in fs)==a and a<p,'available square-source factorization')
        edges=[[t,e]for t,e in fs if jacobi(t,p)==-1]
        must(edges==row['edges'] and edges and all(t not in Q for t,e in edges),'all square successors escape old triangle')
        for tag in ('E','M'):
            hits=[u for u in ds if ((4*u+1)%(9*q)==0 if tag=='E'else(u+a)%(9*q)==0)]
            must(hits==row[tag],'complete square-port channel census')
        must(row['projected_mod_q']=={'E':[u for u in ds if (4*u+1)%q==0],'M':[u for u in ds if(u+a)%q==0]},'independent projected candidates and shared square constraint')
        for state in row['states']:return_check(state)
    return_check(result['separate_original_ES_witness'])

def spf_table(n):
    f=[0]*(n+1)
    for d in range(2,n+1):
        if f[d]==0:
            f[d]=d
            if d*d<=n:
                for x in range(d*d,n+1,d):
                    if f[x]==0:f[x]=d
    return f,[d for d in range(2,n+1)if f[d]==d]

def fac(n,f):
    ans=[]
    while n>1:
        q=f[n];e=0
        while n%q==0:n//=q;e+=1
        ans.append([q,e])
    return ans

def scan_check(expected):
    bound=expected['bound'];f,ps=spf_table(bound);counts=Counter();tri=[]
    for p in ps:
        if p%840 not in {1,121,169,289,361,529}:continue
        squares={x*x%p for x in range(1,(p+1)//2)}
        V=[q for q in ps if q<p and q%4==3 and q not in squares]
        adj={q:{r for r,e in fac((p+q)//4,f)if r%4==3 and r not in squares}for q in V}
        counts['hard_primes']+=1;counts['vertices_3mod4']+=len(V);counts['edges_3mod4']+=sum(len(v)for v in adj.values())
        for q in V:
            for r in sorted(adj[q]):
                if r<=q:continue
                for s in sorted(adj[r]):
                    if s<=q or q not in adj[s]:continue
                    C=[q,r,s];ports=[]
                    for x in C:
                        must(3*x<p,'independent triangle domain bound')
                        a=(p+9*x)//4;fs=fac(a,f);edges=[[t,e]for t,e in fs if t not in squares]
                        must(edges and all(t not in C for t,e in edges),'square-source escape for all bounded triangles')
                        ports.append({'q':x,'a':a,'factors':fs,'edges':edges})
                    tri.append({'p':p,'cycle':C,'ports9':ports});counts['triangles']+=1
    must(dict(counts)==expected['counts'],'complete triangle scan totals')
    must(tri==expected['triangles'],'every bounded triangle record independently reproduced')

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--input',default='certificates');ap.add_argument('--out',default='independent.json');args=ap.parse_args()
    here=Path(__file__).resolve().parent;src=Path(args.input);inp=json.loads((here/'input.json').read_text());cert=json.loads((here/'prime_certificates.json').read_text())
    read=lambda name:json.loads((src/(name+'.json')).read_text())
    proved=primality(cert);triangle_check(inp,read('triangle'),proved);algebra_check(read('algebra'));cubic_check(inp,read('cubic'));ports_check(inp,read('escape'),proved);scan_check(read('scan'))
    result={'checks':CHECKS,'prime_nodes':len(proved),'bound':read('scan')['bound'],'triangle_vectors':1215,'imports_predecessor_or_main':False,'status':'passed'}
    Path(args.out).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps(result,sort_keys=True))
if __name__=='__main__':main()
