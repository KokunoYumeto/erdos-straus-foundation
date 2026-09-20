#!/usr/bin/env python3
"""Separate replay: primitive ES sources, direct products and interpolation.
Imports neither verify.py nor any predecessor implementation.
"""
from __future__ import annotations
import argparse, hashlib, json, time
from collections import Counter
from fractions import Fraction as Rat
from itertools import combinations, permutations
from math import gcd, isqrt, prod
from pathlib import Path
from functools import lru_cache

CHECKS=Counter()
def check(ok,label):
    CHECKS[label]+=1
    if not ok:raise ArithmeticError(label)

def prime(n):return n>=2 and all(n%d for d in range(2,isqrt(n)+1))
@lru_cache(None)
def divisors(n):
    out=[]
    for d in range(1,isqrt(n)+1):
        if n%d==0:
            out.append(d)
            if d*d!=n:out.append(n//d)
    return tuple(sorted(out))

def val(x,p):
    x=Rat(x)
    if not x:return 10**9
    e=0;n=abs(x.numerator);d=x.denominator
    while n%p==0:n//=p;e+=1
    while d%p==0:d//=p;e-=1
    return e

def rmod(x,n):
    x=Rat(x)
    return (x.numerator*pow(x.denominator,-1,n))%n

def symbol(x,p):
    x=rmod(x,p)
    z=pow(x,(p-1)//2,p)
    return 0 if not x else (1 if z==1 else -1)

def unpack(x):
    # Rational entries of matrices/polynomials are encoded as two integers.
    return Rat(x[0],x[1])

def prod_poly(nodes):
    a=[Rat(1)]
    for t in nodes:
        b=[Rat(0)]*(len(a)+1)
        for j,z in enumerate(a):b[j]-=t*z;b[j+1]+=z
        a=b
    return a

def determinant(a):
    n=len(a);answer=Rat(0)
    for perm in permutations(range(n)):
        inv=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        answer+=(-1)**inv*prod(a[i][perm[i]] for i in range(n))
    return answer

def invariant_exponents(matrix,p):
    n=len(matrix);d=[0]
    for k in range(1,n+1):
        values=[]
        for I in combinations(range(n),k):
            for J in combinations(range(n),k):
                values.append(val(determinant([[matrix[i][j] for j in J] for i in I]),p))
        d.append(min(values))
    return [d[i+1]-d[i] for i in range(n)]

def info(p,den):
    roots=[Rat(p)]+list(map(Rat,den));S=sum(roots)
    d=[];v=[];sign=[]
    for i in range(4):
        z=-prod(roots[i]-roots[j] for j in range(4) if j!=i)/S
        d.append(z);e=val(z,p);v.append(e);sign.append(symbol(z/Rat(p)**e,p))
    n=2*sum(e%2==0 and s==1 for e,s in zip(v,sign))
    return roots,d,v,sign,n

def source_rows(bound):
    out=[];all_vectors=0;counts=Counter()
    for p in range(13,bound+1,12):
        if not prime(p):continue
        states=[];vectors=0
        for a in range((p+3)//4,(p+1)//2):
            R=4*a-p
            for r in divisors(a):
                for s in divisors(a//r):
                    if gcd(r,s)!=1:continue
                    h=a//(r*s);u=h*r*r;vectors+=1
                    for ch,num in [('E',p*r+s),('M',r+s)]:
                        if num%R:continue
                        k=num//R
                        den=[a,h*s*k,p*h*r*k] if ch=='E' else [a,p*h*s*k,p*h*r*k]
                        check(sum((Rat(1,x) for x in den),Rat(0))==Rat(4,p),'primitive ordered identity')
                        check(a*a%u==0,'primitive original divisor')
                        roots,ds,vs,sg,n=info(p,den)
                        check(len(set(roots))==4 and val(sum(roots),p)==0,'literal root unit and distinctness')
                        check(vs==([1,0,0,1] if ch=='E' else [2,0,2,2]),'derivative valuation theorem')
                        check(n in ((0,4) if ch=='E' else (4,8)),'local rational point alternatives')
                        check(symbol(h if ch=='E' else r*s,p)==-1,'original Legendre condition')
                        states.append([ch,a,u,R,h,r,s,k,den,vs,sg,n])
                        counts[ch]+=1;counts[ch+'_Qp_'+str(n)]+=1
        out.append(dict(p=p,original_vectors=vectors,states=sorted(states)))
        all_vectors+=vectors
    return out,all_vectors,dict(counts)

def orders_check(data):
    for entry in data:
        st=entry['state'];p=st['p'];roots,ds,vs,sg,n=info(p,st['denominators'])
        ks=[v//2 for v in vs];V=[[x**j for j in range(4)] for x in roots]
        W=[[Rat(p)**ks[i]*roots[i]**j for j in range(4)] for i in range(4)]
        vi=invariant_exponents(V,p);wi=invariant_exponents(W,p)
        check(vi==entry['root_smith_exponents'],'root Smith via all minors')
        check(sorted(vi+wi)==entry['signed_smith_exponents'],'signed Smith via two exact block minors')
        check(sum(vi+wi)==(2 if st['channel']=='E' else 9),'normalization index')
        inverse_columns=[];conductors=[]
        for i in range(4):
            rest=[roots[j] for j in range(4) if i!=j]
            lag=[z/prod(roots[i]-y for y in rest) for z in prod_poly(rest)]
            lc=min(val(x,p) for x in lag)
            conductors.append(-lc+ks[i])
            inverse_columns.append(lag+[Rat(0)]*4)
            inverse_columns.append([Rat(0)]*4+[z/Rat(p)**ks[i] for z in lag])
        inverse=[[inverse_columns[j][i] for j in range(8)] for i in range(8)]
        expected=[[unpack(x) for x in row] for row in entry['inverse_evaluation']]
        check(inverse==expected,'normalization inverse by Lagrange, not elimination')
        check(conductors==entry['conductor_exponents'],'normalization conductor supported basis')
        check(conductors==([1,0,0,1] if st['channel']=='E' else [3,0,3,3]),'conductor theorem')
        indices=[]
        for kind in ('T','eta'):
            for m in range(1,5):
                all_integral=True
                for i in range(4):
                    lag=prod_poly([roots[j] for j in range(4) if i!=j])
                    div=prod(roots[i]-roots[j] for j in range(4) if i!=j)
                    delta=ds[i]/Rat(p)**(2*ks[i])
                    for bit in (0,1):
                        if kind=='T':
                            coefficient=roots[i]**m/Rat(p)**(ks[i]*bit)
                        else:
                            parity=(m+bit)%2
                            coefficient=Rat(p)**(m*ks[i]-parity*ks[i])*delta**((m+bit)//2)
                        if any(val(coefficient*z/div,p)<0 for z in lag):all_integral=False
                if all_integral:indices.append(m);break
        check(indices==entry['quotient_nilpotent_indices_T_eta'],'independent exact defect-module actions')

def evalpoly(a,t):return sum((z*t**i for i,z in enumerate(a)),Rat(0))

def example_checks(ex):
    for name,expected in [('E_zero',0),('E_four',4),('M_eight',8),('M_four',4)]:
        st=ex[name]['state'];p=st['p'];check(prime(p),'fixture deterministic primality')
        roots,ds,vs,sg,n=info(p,st['denominators'])
        check(n==expected,'four hard-prime local alternatives')
        rec=ex[name]['reciprocal'];I=[unpack(x) for x in rec['reciprocal_map']]
        z=[Rat(p)/x for x in roots]
        check([evalpoly(I,x) for x in roots]==z,'reciprocal interpolation')
        pp=prod_poly(z);q=[-a/5 for a in pp]
        deriv=[sum((j*q[j]*x**(j-1) for j in range(1,5)),Rat(0)) for x in z]
        omega=unpack(rec['twist'])
        check(all(deriv[i]*roots[i]**2==omega*ds[i] for i in range(4)),'signed reciprocal scalar twist')
    for name in ('capacity_crossing','small_comparison'):
        row=ex[name];E=row['E'];M=row['M'];p=E['p']
        rE=[Rat(p)]+list(map(Rat,E['denominators']));rM=[Rat(p)]+list(map(Rat,M['denominators']))
        f=[unpack(x) for x in row['forward']];g=[unpack(x) for x in row['reverse']]
        check([evalpoly(f,x) for x in rE]==rM,'forward labelled map')
        check([evalpoly(g,x) for x in rM]==rE,'inverse labelled map')
        check(min(val(c,p) for c in f)>=0 and min(val(c,p) for c in g)==-2,'comparison integral domain')
    # Exhaust both equations using literal products, not primary polynomial coefficients.
    p=13;roots=[Rat(13),Rat(4),Rat(20),Rat(130)];S=sum(roots);counts={}
    for e in (2,3):
        N=p**e;count=0
        for T in range(0,N,p):
            f=-prod(T-x for x in roots)/S
            if rmod(f,N):continue
            d=-sum((prod(T-roots[j] for j in range(4) if j!=i) for i in range(4)),Rat(0))/S
            for eta in range(0,N,p):
                if (eta*eta-rmod(d,N))%N==0:count+=1
        counts[str(e)]=count
    check(counts=={'2':13,'3':0},'independent finite Hensel obstruction')
    check(counts==ex['boundary']['counts'],'full boundary count agreement')
    for row in ex['finite_place_controls']:
        p=row['p'];a=row['a'];b=row['b'];c=unpack(row['c']);bad=row['omitted_prime'];Q=row['places']
        check(prime(p) and prime(bad) and p%840==1 and p%11==10 and p%bad==1,'control progression and primes')
        check(c==Rat(a*b,3*b-a) and b%p==3,'rational source coordinates')
        den=[Rat(a),Rat(p*b),p*c]
        check(den==[unpack(x) for x in row['denominators']],'rational denominator marking')
        check(sum((1/x for x in den),Rat(0))==Rat(4,p),'rational identity independently')
        check(all(val(x,q)>=0 for x in den for q in Q+[p]),'entire declared finite local set')
        check(val(den[2],bad)==-1,'omitted local condition fails exactly')
        roots,ds,vs,sign,n=info(p,den)
        check(vs==[2,0,2,2] and sign==[-1,1,-1,1] and n==4,'same M local algebra signature')
        sp=Rat(p*p+3*p,4);B=p+sp*(sp+1)
        check(sum(roots)<B and max(den)<=sp*(sp+1)/3,'same quantitative witness bounds')
        check(all(y-x>=1 for x,y in zip(sorted(roots),sorted(roots)[1:])),'four separated real roots')
        endpoint=row['known_original_solution'];x,y,z=endpoint['denominators']
        check(4*x*y*z==p*(x*y+x*z+y*z),'original endpoint not a conjecture counterexample')
    for row in ex['single_foreign_prime_controls']:
        p=row['p'];ell=row['omitted_prime'];a=row['a'];u=row['u']
        check(prime(p) and prime(ell) and p%840==1 and p%ell==ell-1 and ell%12==11,'single-prime progression independently')
        check(a==(p+3)//4 and u==a*ell and p>4*ell,'single-prime coordinates')
        check(0<u<a*a and (u+a)%3==(4*u+1)%3==0,'both numerical gates and source range independently')
        check(a*a%u!=0 and Rat(a*a,u).denominator==ell,'exactly one unavailable prime coordinate')
        h=Rat(a,ell);k=(p*ell+1)//3;lam=(ell+1)//3
        for ch,den in [('E',[Rat(a),h*k,Rat(p*a*k)]),('M',[Rat(a),p*h*lam,Rat(p*a*lam)])]:
            check(den==[unpack(x) for x in row['targets'][ch]['denominators']],'joint control denominator data')
            check(sum((1/x for x in den),Rat(0))==Rat(4,p),'joint rational identity separately')
            check(den[1].denominator==ell and den[0].denominator==den[2].denominator==1,'only omitted place is bad')
            check(all(val(x,q)>=0 for x in den for q in row['places']+[p]),'full finite denominator window')
            roots,ds,vs,sg,n=info(p,den)
            check(vs==([1,0,0,1] if ch=='E' else [2,0,2,2]),'control respective channel degeneration')
            sp=Rat(p*p+3*p,4);B=p+sp*(sp+1)
            check(sum(roots)<B and max(den)<sp*(sp+1)/3,'joint exact height bounds')
            check(all(2/sum(roots)<=abs(d)<=sum(roots)**2 for d in ds),'joint exact derivative bounds')
        for field in ('known_original_E','known_original_M'):
            st=row[field];x,y,z=st['denominators']
            check(4*x*y*z==p*(x*y+x*z+y*z) and st['a']**2%st['u']==0,'separate genuine source at same prime')


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input',type=Path,default=Path('certificates'))
    ap.add_argument('--out',type=Path,default=Path('independent.json'));args=ap.parse_args()
    start=time.monotonic();scan=json.loads((args.input/'scan.json').read_text())
    rows,n,counts=source_rows(scan['bound'])
    check(rows==scan['rows'],'every original state row agrees')
    check(n==scan['original_vectors'] and counts==scan['counts'],'full source and counts agree')
    orders_check(json.loads((args.input/'orders.json').read_text()))
    example_checks(json.loads((args.input/'examples.json').read_text()))
    out=dict(success=True,bound=scan['bound'],primes=len(rows),original_vectors=n,counts=counts,
             checks=sum(CHECKS.values()),check_types=dict(CHECKS),elapsed_seconds=time.monotonic()-start,
             source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             imported_primary_or_predecessor_code=False,universal_ES_proved=False)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(out,sort_keys=True,indent=2)+'\n');print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__':main()
