#!/usr/bin/env python3
"""Complete exterior norm atlas. Standard library. No universal occupancy claim."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from math import gcd, isqrt
from functools import lru_cache
from collections import Counter

CHECKS=Counter()
HARD={1,121,169,289,361,529}
def need(condition, label):
    CHECKS[label]+=1
    if not condition: raise ArithmeticError(label)

def primes_to(n):
    z=bytearray(b'\x01')*(n+1)
    if n>=0:z[0]=0
    if n>=1:z[1]=0
    for r in range(2,isqrt(n)+1):
        if z[r]:z[r*r:n+1:r]=b'\0'*((n-r*r)//r+1)
    return [r for r in range(2,n+1) if z[r]]
PRIMES=primes_to(50000)
@lru_cache(maxsize=100000)
def factor(n):
    if n<1:raise ValueError('positive factor input required')
    out=[]
    for q in PRIMES:
        if q*q>n:break
        if n%q==0:
            e=0
            while n%q==0:n//=q;e+=1
            out.append((q,e))
    else:
        q=PRIMES[-1]+2
        while q*q<=n:
            if n%q==0:
                e=0
                while n%q==0:n//=q;e+=1
                out.append((q,e))
            q+=2
    if n>1:out.append((n,1))
    return tuple(out)

def divisors_fact(fs,mul=1):
    z=[1]
    for q,e in fs:z=[d*q**j for d in z for j in range(mul*e+1)]
    return sorted(z)
def divisors(n,mul=1):return divisors_fact(factor(n),mul)
def prime(n):return n>=2 and factor(n)==((n,1),)
def root_kernel(v):
    z=1
    for q,e in factor(v):z*=q**((e+1)//2)
    return z

def cutoff(p):
    """Largest integer w with (p+w)^2 > 4(w+1)^2(w-1)."""
    if p<5:raise ValueError('p must be at least five')
    lo,hi=1,p
    while lo+1<hi:
        w=(lo+hi)//2
        if (p+w)**2>4*(w+1)**2*(w-1):lo=w
        else:hi=w
    return lo

def middle_cutoff(p):
    if p%840 in HARD:
        return 4*((isqrt(3*p+73)-2)//6)-1
    return 4*isqrt((p+7)//12)-1

def state(p,a,u):
    R=4*a-p
    need(isinstance(u,int) and u>0,'positive divisor premise')
    need(p%4==1 and p<4*a and 2*a<p and gcd(p,a)==1,'original exterior domain')
    need(a*a%u==0 and (4*u+1)%R==0,'original exterior divisor gate')
    g=gcd(a,u);h=g*g//u;r=u//g;s=a//g
    need(h*r*s==a and h*r*r==u and gcd(r,s)==1,'normalization')
    need((p*r+s)%R==0,'kappa divisibility')
    k=(p*r+s)//R;D=(4*u+1)//R;v=a*a//u
    need(h>1 and k>r and D%4==3,'exterior strict and parity')
    need(D*s==r+k and p*D+1==4*h*r*k,'dual identity')
    need(v==h*s*s and (p+R)**2+4*v==4*v*R*D,'norm identity')
    need(gcd(h,R)==gcd(h,D)==1 and v not in (R,D),'grade noncollision')
    need(p+R<2*v*D,'orientation inequality')
    w=min(v,R,D)
    need((p+w)**2>4*(w+1)**2*(w-1),'strict cubic bound')
    need(w<=cutoff(p)<p,'integer cutoff')
    x,y,z=a,h*s*k,p*h*r*k
    need(4*x*y*z==p*(x*y+x*z+y*z),'ordered reciprocal identity')
    need(a*a%(R*y-p*a)==0 and a*a//(R*y-p*a)==u,'ordered inverse')
    chart='direct' if R<=D and R<v else ('reciprocal' if D<R and D<v else 'norm')
    need((chart!='norm') or (v<R and v<D),'disjoint chart')
    return (a,u,R,D,v,h,r,s,k,x,y,z,chart)

def record(p,t):
    a,u,R,D,v,h,r,s,k,x,y,z,chart=t
    fs=factor(a);fu=dict(factor(u))
    return dict(p=p,channel='E',a=a,u=u,R=R,D=D,v=v,h=h,r=r,s=s,kappa=k,
                denominators=[x,y,z],chart=chart,factorization=[list(z) for z in fs],
                beta=[[q,fu.get(q,0)-e] for q,e in fs],
                reciprocal_source=(p*D+1)//4,norm=p*p+4*v,
                root_kernel=root_kernel(v))

def full(p):
    ans=set();vectors=0
    for a in range(p//4+1,(p-1)//2+1):
        R=4*a-p
        for u in divisors(a,2):
            vectors+=1
            if (4*u+1)%R==0:ans.add(state(p,a,u))
    return ans,vectors

def atlas(p):
    C=cutoff(p);ans=set();counts=Counter()
    def emit(t,chart):
        need(t[-1]==chart,'declared chart identification')
        need(t not in ans,'chart uniqueness');ans.add(t)
    for R in range(3,C+1,4):
        a=(p+R)//4
        for u in divisors(a,2):
            counts['direct_divisors']+=1
            if (4*u+1)%R:continue
            D=(4*u+1)//R;v=a*a//u
            if R<=D and R<v:emit(state(p,a,u),'direct')
    for D in range(3,C+1,4):
        B=(p*D+1)//4
        for w in divisors(B,2):
            if w>=B:break
            counts['reciprocal_divisors']+=1
            if (w+B)%D:continue
            g=gcd(B,w);h=g*g//w;r=w//g;k=B//g
            need(h>0 and h*r*r==w and h*r*k==B and gcd(r,k)==1,
                 'reciprocal raw normalization')
            need(gcd(D,B)==1 and gcd(D,g)==1,'reciprocal source coprimality')
            need((r+k)%D==0,'reciprocal lambda')
            s=(r+k)//D;a=h*r*s;R=4*a-p;v=h*s*s
            need(s>0 and gcd(r,s)==1,'reciprocal primitive return')
            need(R*k==p*r+s and D*R==4*w+1,
                 'reciprocal residual and gate return')
            need(D*(p-2*a)==2*h*r*(k-r)-1,'reciprocal range identity')
            if D<R and D<v:
                t=state(p,a,w)
                need((h,r,s,k)==t[5:9],'reciprocal inverse normalization')
                emit(t,'reciprocal')
    for v in range(2,C+1):
        # v is the original complementary divisor a^2/u, not an available factor of p.
        if gcd(v,p)!=1:continue
        N=p*p+4*v;K=root_kernel(v)
        for R in divisors(N):
            counts['norm_divisors']+=1
            if R%4!=3 or not(v<R<p) or (p+R)%(4*K):continue
            a=(p+R)//4
            need(a*a%v==0,'norm availability equivalence')
            u=a*a//v
            need(gcd(R,4*v)==1 and (4*u+1)%R==0,'norm gate implication')
            D=(4*u+1)//R
            if v<D:emit(state(p,a,u),'norm')
    return ans,dict(counts)

def examples():
    out={}
    # The residue hypothesis in the strict cutoff cannot be deleted.
    p,a,u=19,6,6;R=4*a-p;D=(4*u+1)//R;v=a*a//u;w=min(R,D,v)
    need(prime(p) and p%4==3 and p<4*a and 2*a<p and gcd(p,a)==1,
         'residue-hypothesis boundary source')
    need(a*a%u==0 and (4*u+1)%R==0 and R==D==5 and v==6,
         'residue-hypothesis boundary coordinates')
    need((p+w)**2==4*(w+1)**2*(w-1),'residue-hypothesis strictness failure')
    out['residue_hypothesis_boundary']=dict(
        p=p,a=a,u=u,R=R,D=D,v=v,w=w,p_mod_4=p%4,
        equality_value=(p+w)**2,
        interpretation='Equality occurs when p == 3 mod 4; this is outside the theorem domain.')
    p=48049
    need(prime(p) and p%840==169,'prime hard exterior tie')
    t=state(p,12090,24180)
    need(t[2]==t[3]==311 and min(t[2],t[3])>middle_cutoff(p),'middle cutoff does not apply to E')
    need(t[9:12]==(12090,1867905,179501934690),'displayed exterior denominators')
    out['hard_exterior_not_middle_bound']=record(p,t)
    # v and D may share prime factors. Do not assert gcd(v,D)=1.
    t=state(37,12,8)
    need(t[3]==3 and t[4]==18 and gcd(t[3],t[4])==3,'noncoprime v-D retained')
    out['noncoprime_v_D']=record(37,t)
    out['small_prime_family']=[]
    for n in (2,4):
        h=4*n*n-2;t0=4*n*n-1;p=4*h*n-t0
        need(prime(p),'small family prime')
        z=state(p,h*n,h*n*n)
        need(z[2]==z[3]==t0 and z[4]==h,'family original marking')
        need(cutoff(p)==h,'prime integer-cutoff equality')
        out['small_prime_family'].append(record(p,z))
    def family_p(n):return 16*n**3-4*n*n-8*n+1
    residue_solutions=[n for n in range(210) if family_p(n)%840==289]
    need(residue_solutions==[24,164],'complete hard-residue classes modulo 210')
    need(all((family_p(n+210)-family_p(n))%840==0 for n in range(210)),
         'family polynomial period modulo 840')
    fam=[]
    for n in [c+210*k for c in (24,164) for k in range(20)]:
        h=4*n*n-2;t0=4*n*n-1;p=4*h*n-t0
        z=state(p,h*n,h*n*n)
        need(p%840==289 and gcd(p,h*n)==1,'hard-residue integer family')
        need(cutoff(p)==h,'integer family exact-cutoff equality')
        # These are identities for integer parameters. Their primality is not claimed.
        fam.append(dict(n=n,p=p,h=h,R=t0,D=t0,v=h,unit_source=True,prime_claim=False,
                        minimal_chart=z[-1]))
    out['asymptotic_integer_family']=fam
    out['hard_residue_classification']=dict(
        modulus_for_n=210,residues_for_n=residue_solutions,
        modulus_for_p=840,residue_for_p=289,
        exact_period_identity='p(n+210)-p(n)=840(12n^2+2518n+176188)',
        universal_prime_values_claimed=False)
    # Last tranche's extremal v=11 lane at p2521 remains a negative control.
    p=2521;v=11;N=p*p+4*v;K=root_kernel(v)
    need(prime(p),'p2521 primality')
    nonresidues=[a for a in range(2,p) if pow(a,(p-1)//2,p)==p-1]
    need(nonresidues[0]==11,'p2521 least quadratic nonresidue')
    roots=[R for R in divisors(N) if R%4==3 and 0<R<p and (p+R)%(4*K)==0]
    need(roots==[],'minimal complement grade can fail')
    out['empty_minimal_norm_grade']=dict(p=p,v=v,norm=N,factorization=[list(z) for z in factor(N)],
                                        residues_below_p=[R for R in divisors(N) if R<p],
                                        required_residue=(-p)%(4*K),modulus=4*K,hits=roots,
                                        p_is_prime=True,least_quadratic_nonresidue=nonresidues[0])
    # Check a state whose coarse norm divisibility alone does not make its square divisor available.
    rejected=None
    for pp in (17,41,97,1009):
        for vv in range(2,cutoff(pp)+1):
            for RR in divisors(pp*pp+4*vv):
                if RR%4==3 and 0<RR<pp:
                    aa=(pp+RR)//4
                    if aa*aa%vv:
                        rejected=dict(p=pp,v=vv,R=RR,a=aa,norm=pp*pp+4*vv,
                                      a_squared_remainder=aa*aa%vv);break
            if rejected:break
        if rejected:break
    need(rejected is not None,'norm divisibility alone is insufficient')
    out['missing_original_availability']=rejected
    return out

def canon(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--bound',type=int,default=3000)
    ap.add_argument('--out',type=Path,default=Path('certificates'))
    args=ap.parse_args();args.out.mkdir(parents=True,exist_ok=True)
    if args.bound<97:ap.error('bound must be at least 97')
    rows=[];total_vectors=0;total_states=0;chart_counts=Counter();candidate_counts=Counter()
    for p in primes_to(args.bound):
        if p%4!=1:continue
        expected,nv=full(p);found,cands=atlas(p)
        need(found==expected,'complete three-chart equality at '+str(p))
        total_vectors+=nv;total_states+=len(found);candidate_counts.update(cands)
        chart_counts.update(t[-1] for t in found)
        rows.append(dict(p=p,C=cutoff(p),states=[list(t) for t in sorted(found)],
                         original_vectors=nv,candidate_counts=cands))
    ex=examples()
    scan=dict(bound=args.bound,prime_domain='all primes p == 1 mod 4',rows=rows)
    for name,data in [('scan.json',scan),('examples.json',ex)]:
        (args.out/name).write_text(json.dumps(data,indent=2,sort_keys=True)+'\n',
                                   encoding='utf-8',newline='\n')
    report=dict(success=True,bound=args.bound,primes=len(rows),original_vectors=total_vectors,
                canonical_E_states=total_states,chart_states=dict(chart_counts),
                candidate_counts=dict(candidate_counts),checks=sum(CHECKS.values()),
                check_types=dict(CHECKS),
                scan_sha256=hashlib.sha256((args.out/'scan.json').read_bytes()).hexdigest(),
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                state_domain={'p':'integer > 1, congruent to 1 mod 4',
                              'a':'integer with p/4 < a < p/2 and gcd(p,a)=1',
                              'u':'positive divisor of a^2'},
                universal_E_occupancy_proved=False,universal_ES_proved=False,
                scope='Complete per-input atlas and necessary cutoff; finite replay is regression, not universal occupancy.')
    (args.out/'report.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n',
                                        encoding='utf-8',newline='\n')
    print(json.dumps(report,indent=2,sort_keys=True))
if __name__=='__main__':main()
