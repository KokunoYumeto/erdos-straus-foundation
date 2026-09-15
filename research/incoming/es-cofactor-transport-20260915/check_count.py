#!/usr/bin/env python3
"""Independent divisor enumeration of the cofactor-count theorem.
Does not import verify.py. Exact ints; ranges and output checks declared.
"""
import argparse,json
from collections import Counter
from math import isqrt
from pathlib import Path

C=Counter()
def test(b,n):
 C[n]+=1
 if not b:raise ArithmeticError(n)

def divs(n):
 small=[d for d in range(1,isqrt(n)+1) if n%d==0]
 return sorted(set(small+[n//d for d in small]))

def factors(n):
 fs=[];d=2
 while d*d<=n:
  e=0
  while n%d==0:n//=d;e+=1
  if e:fs.append((d,e))
  d=3 if d==2 else d+2
 if n>1:fs.append((n,1))
 return fs

def one(p,k):
 m=2**k;u=2**(2*k-5);N=p+4*u;o=2**(k-2);L=o//2
 ds=divs(N);R=[r for r in ds if r%m==(-p)%m]
 # Check actual original divisor and gate; not just the residue-class count.
 for r in R:
  a=(p+r)//4
  test(4*a==p+r and a*a%u==0 and (a+u)%r==0 and r<p,'independent_original_return')
 e=0;M=N
 while M%3==0:M//=3;e+=1
 dm=divs(M);A=sum(d%8 in (5,7) for d in dm)
 logs={(-pow(3,j,m))%m:j for j in range(o)}
 a=[0]*o
 for t in dm:
  if t%m in logs:a[logs[t%m]]+=1
 counts=[(e-((L-j)%o))//o+1 if (L-j)%o<=e else 0 for j in range(o)]
 direct=sum(x*y for x,y in zip(a,counts))
 test(direct==len(R),'independent_exact_count')
 test((2*(e+1)//o)*A<=2*direct<=((2*(e+1)+o-1)//o)*A,'independent_two_sided_mass')
 if (e+1)%L==0:test(o*direct==(e+1)*A,'independent_balanced_formula')
 if e>=L-1:test(bool(R)==any(q%8 in (5,7) for q,f in factors(M)),'independent_threshold_iff')
 return len(R)

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--bound',type=int,default=2000000)
 ap.add_argument('--out',default='independent.json');args=ap.parse_args()
 N=args.bound;pr=bytearray(b'\1')*(N+1);pr[:2]=b'\0\0'
 for q in range(2,isqrt(N)+1):
  if pr[q]:pr[q*q::q]=b'\0'*len(pr[q*q::q])
 stats=Counter()
 for p in range(25,N+1,48):
  if not pr[p] or p%840 not in {1,121,169,289,361,529}:continue
  h=one(p,4);stats['primes']+=1;stats['states']+=h;stats['occupied']+=bool(h)
 # All integers, not just primes, in stated progressions.
 generic=0
 for k in range(4,9):
  m=2**k;u=2**(2*k-5)
  for p in range(1+m//2,60001,m):
   if p>2*u:one(p,k);generic+=1
 # Large negative branches: enumerate their complete nine/21 factor divisors,
 # using trial division of N as an independent check, not a presumed factor list.
 for p,k in [(6185041,5),(9017211169,6)]:
  test(one(p,k)==0,'complete_sharpness_seed_failure')
 out=dict(bound=N,scope='hard p=25 mod48 for k4; all progression integers <=60000 for k4..8',
          scan=dict(stats),integer_branches=generic,checks=dict(C),total_checks=sum(C.values()))
 Path(args.out).write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
 print(json.dumps({'scan':dict(stats),'integer_branches':generic,'checks':sum(C.values())},sort_keys=True))
if __name__=='__main__':main()
