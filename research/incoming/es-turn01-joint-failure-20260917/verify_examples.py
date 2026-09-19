#!/usr/bin/env python3
"""Bounded standalone certificates for the displayed original ES shells.
Uses no imports from the general scan, and no unbounded group-closure loop.
"""
import argparse,json,math,itertools,hashlib
from pathlib import Path

CASES=[
 (3361,848,[(2,4),(53,1)],[1,2,4,8,16],6,6,0,0),
 (5569,1397,[(11,1),(127,1)],[1,7,11],6,6,0,0),
 (22129,5537,[(7,2),(113,1)],[1,7,8,11,12,18],3,3,0,2),
 (29,9,[(3,2)],[1],6,6,0,0),
 (197,51,[(3,1),(17,1)],[1],6,6,0,0),
 (109,31,[(31,1)],[1],8,8,0,0),
 (37,13,[(13,1)],[1],8,8,0,0),
 (6340273,1585081,[(1259,2)],[1,35],8,16,0,0),
]
COUNT=0
def ck(ok,label):
 global COUNT
 COUNT+=1
 if not ok:raise ArithmeticError(label)
def prove_prime(p):
 ck(p>=2 and all(p%d for d in range(2,math.isqrt(p)+1)),'complete trial primality')
def make(p,a,u,tag):
 R=4*a-p;d=math.gcd(a,u);h=d*d//u;r=u//d;s=a//d
 ck(d*d%u==0 and h*r*s==a and h*r*r==u and math.gcd(r,s)==1,'normalization')
 num=p*r+s if tag=='E' else r+s
 ck(num%R==0,'channel quotient');t=num//R
 x=a;y=h*s*t*(1 if tag=='E' else p);z=p*h*r*t
 ck(4*x*y*z==p*(x*y+x*z+y*z) and min(x,y,z)>0,'reciprocal identity')
 top=a*a*(1 if tag=='E' else p)
 ck(top==(R*y-p*a)*u,'ordered inverse')
 return dict(channel=tag,u=u,h=h,r=r,s=s,quotient=t,denominators=[x,y,z])
def one(case):
 p,a,fac,expectK,de,da,ne,nm=case;R=4*a-p
 prove_prime(p)
 for q,e in fac:prove_prime(q)
 ck(math.prod(q**e for q,e in fac)==a,'original factorization')
 units=[x for x in range(1,R) if math.gcd(x,R)==1];mu={};words=[];hits=[]
 for beta in itertools.product(*(range(-e,e+1) for q,e in fac)):
  u=math.prod(q**(e+b) for (q,e),b in zip(fac,beta));v=u*pow(a,-1,R)%R
  mu[v]=mu.get(v,0)+1
  tags=[]
  if (4*u+1)%R==0:tags.append('E');hits.append(make(p,a,u,'E'))
  if (u+a)%R==0:tags.append('M');hits.append(make(p,a,u,'M'))
  words.append(dict(beta=list(beta),u=u,residue=v,channels=tags))
 W=set(mu);K=[g for g in units if {g*w%R for w in W}==W]
 ck(K==expectK,'actual stabilizer against all units')
 H={1}
 for g in [R-1,2]+[q for q,e in fac]:
  powers={pow(g,j,R) for j in range(len(units))}
  H={x*y%R for x in H for y in powers}
 ck(len(H)//len(K)==de and len(units)//len(K)==da,'effective and ambient indices')
 ck(sum(x['channel']=='E' for x in hits)==ne and sum(x['channel']=='M' for x in hits)==nm,'complete channel counts')
 ck(all(mu[g]==mu[pow(g,-1,R)] for g in W),'fine coefficient inversion')
 reps={x:min(x*k%R for k in K) for x in H};A=set(reps.values())
 qmu={c:sum(mu.get(x,0) for x in H if reps[x]==c) for c in A}
 qmu={c:n for c,n in qmu.items() if n}
 targets=dict(M=R-1,E=(-pow(p,-1,R))%R,E_inverse=(-p)%R)
 qtargets={t:reps[x] for t,x in targets.items()}
 carries=[]
 for c,d,e in itertools.product(A,repeat=3):
  omega=lambda v,w:v*w*pow(reps[v*w%R],-1,R)%R
  ck(omega(c,d)*omega(reps[c*d%R],e)%R==omega(d,e)*omega(c,reps[d*e%R])%R,'full cocycle identity')
 for c,d in itertools.product(A,repeat=2):
  omega=c*d*pow(reps[c*d%R],-1,R)%R
  carries.append([c,d,omega])
 return dict(p=p,a=a,R=R,factorization=fac,K=K,effective_index=de,ambient_index=da,mu=sorted(mu.items()),
             quotient_counts=sorted(qmu.items()),targets=targets,target_classes=qtargets,words=words,hits=hits,cocycle=carries)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--out',default='examples_standalone.json');args=ap.parse_args()
 cases=[one(c) for c in CASES]
 for i,j in itertools.product(range(6),repeat=2):
  ck(pow(2,i+j,19)==pow(2,(i+j)%6,19)*pow(7,(i+j)//6,19)%19,'power section C18 carry')
 # No homomorphic section: every lift of 2K has order 18, never order 6.
 for k in (1,7,11):
  g=2*k%19;order=next(n for n in range(1,19) if pow(g,n,19)==1)
  ck(order==18,'nonsplit C18 extension')
 out=dict(status='passed',checks=COUNT,scope='eight explicitly displayed shells; complete positive divisor lists, all unit stabilizers, all cocycle triples, deterministic trial primality',cases=cases)
 Path(args.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'status':out['status'],'checks':COUNT,'shells':len(cases)}))
if __name__=='__main__':main()
