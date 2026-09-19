#!/usr/bin/env python3
"""Independent bounded primitive-parameter and certificate checker.
Imports neither the main verifier nor its factorization/divisor code.
"""
from __future__ import annotations
import argparse, hashlib, json
from math import gcd, isqrt
from pathlib import Path

HARD={1,121,169,289,361,529}

def require(v,label):
    if not v:raise ArithmeticError(label)

def prime(n):
    if n<2:return False
    for d in range(2,isqrt(n)+1):
        if n%d==0:return False
    return True

def divisors(n):
    lo=[];hi=[]
    for d in range(1,isqrt(n)+1):
        if n%d:continue
        lo.append(d)
        if d*d!=n:hi.append(n//d)
    return lo+hi[::-1]

def cutoff(p,hard):
    if hard:
        k=(isqrt(3*p+73)-2)//6
        require((6*k+2)**2<=3*p+73<(6*(k+1)+2)**2,'hard cutoff floor')
    else:
        k=isqrt((p+7)//12)
        require(12*k*k<=p+7<12*(k+1)*(k+1),'general cutoff floor')
    return 4*k-1

def parameter_states(p):
    result=set()
    # hr s < p/2 and r<s => r^2 < p/2. No factorization is used.
    for r in range(1,isqrt((p-1)//2)+1):
        for s in range(r+1,(p-1)//(2*r)+1):
            if gcd(r,s)!=1:continue
            v=r*s
            for h in range(p//(4*v)+1,(p-1)//(2*v)+1):
                a=h*v;R=4*a-p
                if (r+s)%R:continue
                lam=(r+s)//R;u=h*r*r;j=h*r*lam;Q=4*j-1
                t=(a,u,R,Q,h,r,s,lam,j,a,p*h*s*lam,p*h*r*lam)
                require(4*t[9]*t[10]*t[11]==p*(t[9]*t[10]+t[9]*t[11]+t[10]*t[11]),'identity')
                result.add(t)
    return result

def chart_states(p,B,source):
    """Enumerate both raw chart domains without using serialized chart labels."""
    by_au={(t[0],t[1]):t for t in source}
    require(len(by_au)==len(source),'unique source a,u')
    direct=set();cofactor=set();direct_tests=0;cofactor_tests=0
    for R in range(3,B+1,4):
        require((p+R)%4==0,'direct a integrality')
        a=(p+R)//4
        for u in divisors(a*a):
            if u>=a:break
            direct_tests+=1
            if (a+u)%R:continue
            Q=(p+4*u)//R
            require(R*Q==p+4*u,'direct Q integrality')
            if R>Q:continue
            require((a,u) in by_au,'direct chart return')
            t=by_au[(a,u)]
            require(t[2]==R and t[3]==Q,'direct chart cofactors')
            require(t not in direct,'direct chart duplicate')
            direct.add(t)
    for Q in range(3,B+1,4):
        j=(Q+1)//4
        for u in divisors(j*j):
            cofactor_tests+=1
            if (p+4*u)%Q:continue
            R=(p+4*u)//Q
            if R<=Q:continue
            require((p+R)%4==0,'cofactor a integrality')
            a=(p+R)//4
            require(p<4*a and 2*a<p and u<a,'cofactor source inequalities')
            g=gcd(j,u)
            require(g*g%u==0,'cofactor h integrality')
            h=g*g//u;r=u//g;lam=j//g;s=R*lam-r
            require(min(h,r,s,lam)>0,'cofactor positivity')
            require(h*r*lam==j and h*r*r==u and h*r*s==a,'cofactor inverse products')
            require(gcd(r,s)==1 and r<s and R*lam==r+s,'cofactor primitive return')
            require(a*a%u==0 and (a+u)%R==0,'cofactor original gates')
            require((a,u) in by_au,'cofactor chart return')
            t=by_au[(a,u)]
            require(t[2]==R and t[3]==Q and t[4:8]==(h,r,s,lam),'cofactor tuple return')
            require(t not in cofactor,'cofactor chart duplicate')
            cofactor.add(t)
    require(direct.isdisjoint(cofactor),'cross-chart disjointness')
    require(direct|cofactor==source,'complete raw atlas')
    return direct_tests,cofactor_tests

def verify_order_certificate(c):
    n=c['p'];L=c['L'];q=c['q'];B=c['budget']
    factors=c['L_factorization'];F=1
    for r,e in factors:
        require(prime(r) and e>0,'small certified prime')
        F*=r**e
    require(F==L and (n-1)%F==0 and F>isqrt(n),'large known factor')
    base=dict(c['order_bases'])
    require(set(base)=={r for r,e in factors},'complete factor support')
    for r,e in factors:
        a=base[r]
        require(pow(a,n-1,n)==1,'order congruence')
        require(gcd(pow(a,(n-1)//r,n)-1,n)==1,'order exclusion')
    require(prime(q) and q%4==3 and q>4*B and n>q,'grade parameters')
    require(n%8==1 and n%q==q-1,'CRT endpoints')
    require(n%840 in {1,121,169,289,361,529},'hard prime class')
    for r in range(3,q,2):
        if prime(r):require(n%r==1,'all smaller prime residues')
    require(pow(q,(n-1)//2,n)==n-1,'nonresidue')
    require(c.get('least_nonresidue')==q,'least nonresidue metadata')
    require(c.get('least_negative_3mod4')==q,'least 3 mod 4 nonresidue metadata')
    require(c.get('least_j_lower_bound')==(q+1)//4,'middle grade metadata')
    a=(n+q)//4;k=(n+1)//q
    endpoint=c['endpoint']
    require(endpoint.get('R')==q and endpoint.get('a')==a and
            endpoint.get('kappa')==k,'endpoint metadata')
    x,y,z=endpoint['denominators']
    require((x,y,z)==(a,a*k,n*a*k),'endpoint marking')
    require(4*x*y*z==n*(x*y+x*z+y*z),'endpoint reciprocal identity')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input',type=Path,default=Path('certificates'))
    ap.add_argument('--out',type=Path,default=Path('independent.json'));args=ap.parse_args()
    scan=json.loads((args.input/'scan.json').read_text());rows=scan['rows'];checks=0
    expected_primes=[p for p in range(17,scan['bound']+1,8) if prime(p)]
    require([x['p'] for x in rows]==expected_primes,'complete prime domain')
    total_states=0;total_direct=0;total_cofactor=0;hard_count=0
    for row in rows:
        p=row['p'];hard=p%840 in HARD;B=cutoff(p,hard)
        require(row['hard']==hard,'hard metadata at '+str(p))
        require(row['cutoff']==B,'cutoff metadata at '+str(p))
        got=parameter_states(p)
        stored_sequence=[tuple(x) for x in row['oriented_by_r_lt_s_states']]
        require(len(stored_sequence)==len(set(stored_sequence)),'duplicate serialized state')
        stored=set(stored_sequence)
        require(got==stored,'full primitive atlas at '+str(p));checks+=1
        dt,ct=chart_states(p,B,got)
        require(row['direct_candidate_tests']==dt,'direct candidate count')
        require(row['cofactor_candidate_tests']==ct,'cofactor candidate count')
        require(row['canonical_M_states']==2*len(got),'canonical state count')
        total_states+=len(got);total_direct+=dt;total_cofactor+=ct;hard_count+=int(hard)
        for t in got:
            a,u,R,Q,h,r,s,lam,j,x,y,z=t;v=min(R,Q)
            require(3*v*v+6*v-25<=4*p,'general quadratic bound');checks+=1
            if hard:
                require(3*v*v+14*v-81<=4*p,'hard quadratic bound');checks+=1
                if 3*v*v+14*v-81==4*p:
                    require(h==1 and lam==1 and Q==R+8 and s==3*r-9 and
                            p==12*r*r-40*r+9,'hard equality forcing')
            require(v<=B,'finite cutoff')
            if Q<R:
                require(j*j%u==0 and (p+4*u)//Q==R,'small-cofactor original source')
                d=gcd(j,u)
                require((d*d//u,u//d,R*(j//d)-u//d,j//d)==(h,r,s,lam),'independent inverse')
            else:
                require(R<=B and a*a%u==0,'small-residual original source')
    examples=json.loads((args.input/'examples.json').read_text())
    for r in examples['states']:
        p=r['p'];a=r['a'];u=r['u'];R=r['R'];Q=r['Q'];h=r['h'];v=r['r'];s=r['s'];lam=r['lambda_']
        require(prime(p) and h*v*s==a and h*v*v==u,'example marking')
        require(R==4*a-p and Q==4*h*v*lam-1 and R*lam==v+s,'example cofactor')
        require(gcd(v,s)==1 and v<s and a*a%u==0,'example orientation')
        require(r['j']==h*v*lam,'example middle grade')
        expected=(a,p*h*s*lam,p*h*v*lam)
        require(tuple(r['denominators'])==expected,'example denominators')
        require(tuple(r['complement_denominators'])==(expected[0],expected[2],expected[1]),
                'example complement denominators')
        require(r['chart']==('direct' if R<=Q else 'cofactor'),'example chart label')
    p=2521;a=642;R=47
    actual=[]
    for u in range(1,a+1):
        if a*a%u:continue
        actual.extend([u] if u==a else [u,a*a//u])
    require(len(actual)==27,'all square divisors')
    require(all((4*u+1)%R and (u+a)%R for u in actual),'both gates empty')
    verify_order_certificate(json.loads((args.input/'grade_certificate.json').read_text()))
    summary=json.loads((args.input/'summary.json').read_text())
    require(summary['success'] and summary['primes']==len(rows) and
            summary['hard_primes']==hard_count,'summary prime counts')
    require(summary['M_states_with_r_lt_s']==total_states and
            summary['canonical_oriented_M_states']==2*total_states,'summary state counts')
    require(summary['direct_candidate_tests']==total_direct and
            summary['cofactor_candidate_tests']==total_cofactor,'summary candidate counts')
    for name in ('scan.json','examples.json','grade_certificate.json'):
        digest=hashlib.sha256((args.input/name).read_bytes()).hexdigest()
        require(summary['output_sha256'][name]==digest,'summary hash '+name)
    out=dict(success=True,bound=scan['bound'],primes=len(rows),state_checks=checks,
             scan_sha256=hashlib.sha256((args.input/'scan.json').read_bytes()).hexdigest(),
             independence='primitive h,r,s enumeration; no main or predecessor import',
             universal_ES_proved=False,universal_TypeII_occupancy_proved=False)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
