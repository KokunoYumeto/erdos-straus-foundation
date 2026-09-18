#!/usr/bin/env python3
"""Portable exact checks for the Turn 4 examples, separate from cofactor completeness.
Only Python standard-library integer arithmetic is used. Run cofactor_check.py
and check_independent.py for the universal finite-domain enumeration.
"""
import argparse,json
from collections import Counter
from math import gcd,isqrt,prod
from pathlib import Path
CHECKS=0

def check(b,label):
    global CHECKS
    CHECKS+=1
    if not b:raise ArithmeticError(label)

def prime(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))

def sig(q):return 1 if q%4==3 else 3

def nonresidue(q,p):return pow(q,(p-1)//2,p)==p-1

def factors_check(a,fs):
    check(all(e>0 and prime(r) for r,e in fs),'prime-power input')
    check(len({r for r,e in fs})==len(fs) and prod(r**e for r,e in fs)==a,'complete factorization')

def divisors(a):
    lower=[u for u in range(1,a+1) if a*a%u==0]
    return sorted(set(lower+[a*a//u for u in lower]))

def source(p,node,counts=True):
    q,t,a=node['q'],node['t'],node['a'];R=sig(q)*q*t*t
    check(prime(q) and q<p and nonresidue(q,p),'original vertex')
    check(t>0 and t%2 and R<3*p and 4*a==p+R and gcd(p*a,R)==1,'marked source domain')
    factors_check(a,node['factorization'])
    edge=[r for r,e in node['factorization'] if nonresidue(r,p)]
    check(edge and q not in edge and all(r<p for r in edge),'actual nonresidue supply')
    if not counts:return edge
    us=divisors(a)
    E=[u for u in us if (4*u+1)%R==0]
    M=[u for u in us if (4*u+p)%R==0]
    return edge,len(us),E,M

def run(data):
    p=data['p'];check(prime(p) and p%840 in (1,121,169,289,361,529),'hard prime')
    counts=Counter();seen={q:[] for q in data['vertices']}
    for node in data['square_sources']:
        edges,n,E,M=source(p,node);seen[node['q']].append(node['t'])
        check(E==M==[],'both complete local channels empty')
        counts['sources']+=1;counts['divisor_vectors']+=n
    for q,ts in seen.items():
        required=list(range(1,isqrt((3*p-1)//(sig(q)*q))+1,2))
        check(ts==required,'no valid square source omitted')
    check(counts=={'sources':22,'divisor_vectors':246},'complete original source totals')
    for i,node in enumerate(data['path']):
        edges=source(p,node,False)
        if i+1<len(data['path']):check(data['path'][i+1]['q'] in edges,'actual path edge')
    w=data['solution'];a,u,R=w['a'],w['u'],w['R'];h,r,s,lam=w['h'],w['r'],w['s'],w['lambda']
    check(w['p']==p and w['channel']=='M' and a*a%u==0 and (4*u+p)%R==0,'original middle hit')
    check(a==h*r*s and u==h*r*r and gcd(r,s)==1 and r+s==R*lam,'normalized marking')
    den=[a,p*h*s*lam,p*h*r*lam];check(den==w['denominators'],'ordered denominator return')
    x,y,z=den;check(4*x*y*z==p*(x*y+x*z+y*z),'ES identity')
    check(p*a*a==u*(R*y-p*a),'ordered inverse')
    bad=data['noncoprime'];p0=bad['p'];q=bad['q'];t=bad['t'];a=bad['a'];u=bad['u']
    check(prime(p0) and nonresidue(q,p0),'noncoprime original prime and vertex')
    check(4*a==p0+q*t*t and a*a%u==0,'noncoprime original divisor')
    check((4*u+1)%q==0 and (4*u+1)%(t*t)==0 and (4*u+1)%(q*t*t)!=0,'lcm is not full residual')
    check(((4*u+1)//q)%(t*t)==bad['digit']==66,'retained carry digit')
    for rec in data['finite_candidates']:
        p=rec['p'];C=rec['cycle'];e=rec['escape']
        check(prime(p) and p%840 in (1,121,169,289,361,529),'finite candidate prime')
        check(len(C)==5 and len(set(C))==5 and all(prime(q) and q<p and nonresidue(q,p) for q in C),'five actual vertices')
        check(all(p+sig(q)*q==4*rec['cofactors'][i]*C[(i+1)%5] for i,q in enumerate(C)),'all cycle equations')
        edge=source(p,{'q':e['q'],'t':3,'a':e['a'],'factorization':e['factorization']},False)
        check([r for r in edge if r not in C]==e['outside_nonresidues'],'certified outside factor')
    return {'explicit_checks':CHECKS,'source_counts':dict(counts),
       'finite_candidates_checked':len(data['finite_candidates']),
       'cofactor_domain_enumeration_performed':False,
       'nonclaim':'This portable example replay does not replace cofactor_check.py for the universal finite reduction.'}

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--input',default='input.json');ap.add_argument('--out',default='example_certificate.json');args=ap.parse_args()
    result=run(json.loads(Path(args.input).read_text()))
    Path(args.out).write_text(json.dumps(result,sort_keys=True,separators=(',',':'))+'\n')
    print(json.dumps(result,sort_keys=True))
