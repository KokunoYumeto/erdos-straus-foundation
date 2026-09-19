#!/usr/bin/env python3
"""Independent complete primitive h,r,s enumeration. No import from main or predecessor."""
from __future__ import annotations
from pathlib import Path
from math import gcd,isqrt
import argparse,json,hashlib,time
COUNT=0
def check(x,label):
    global COUNT;COUNT+=1
    if not x:raise ArithmeticError(label)
def prime(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))
def C_of(p):
    w=1
    while (p+w+1)**2>4*(w+2)**2*w:w+=1
    return w

def all_primitive(p):
    out=set();maxa=(p-1)//2
    for r in range(1,maxa+1):
        for s in range(1,maxa//r+1):
            if gcd(r,s)!=1:continue
            rs=r*s
            for h in range(p//(4*rs)+1,maxa//rs+1):
                a=h*rs;R=4*a-p
                if (p*r+s)%R:continue
                k=(p*r+s)//R;u=h*r*r;v=h*s*s
                check((4*u+1)%R==0,'primitive exterior gate')
                D=(4*u+1)//R
                check((r+k)%s==0 and (r+k)//s==D,'independent D return')
                x,y,z=a,h*s*k,p*h*r*k
                check(4*x*y*z==p*(x*y+x*z+y*z),'independent ordered identity')
                check(v==a*a//u and a*a%u==0,'complement integer')
                w=min(v,R,D)
                check((p+w)**2>4*(w+1)**2*(w-1),'independent strict bound')
                check(w<=C_of(p),'independent integer cutoff')
                chart='norm' if v<min(R,D) else ('direct' if R<=D else 'reciprocal')
                out.add((a,u,R,D,v,h,r,s,k,x,y,z,chart))
    return out

def fixture(z):
    p=z['p'];a=z['a'];u=z['u'];R=z['R'];D=z['D'];v=z['v']
    h=z['h'];r=z['r'];s=z['s'];k=z['kappa'];x,y,zz=z['denominators']
    check(prime(p),'displayed prime by full trial division')
    check(gcd(p,a)==1 and p<4*a and 2*a<p,'displayed source')
    check(a==h*r*s and u==h*r*r and v==h*s*s,'displayed coordinates')
    check(R==4*a-p and R*k==p*r+s and s*D==r+k,'displayed gate')
    check((x,y,zz)==(a,h*s*k,p*h*r*k),'displayed order')
    check(4*x*y*zz==p*(x*y+x*zz+y*zz),'displayed fractions')
    check((p+R)**2+4*v==4*v*R*D,'displayed norm')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input',type=Path,default=Path('certificates'))
    ap.add_argument('--out',type=Path,default=Path('independent.json'));args=ap.parse_args()
    start=time.monotonic();scan=json.loads((args.input/'scan.json').read_text());rows=scan['rows']
    pp=[p for p in range(5,scan['bound']+1,4) if prime(p)]
    check([z['p'] for z in rows]==pp,'full prime domain')
    total=0
    for row in rows:
        p=row['p'];states=all_primitive(p);stored={tuple(x) for x in row['states']}
        check(states==stored,'full primitive equality at '+str(p));check(len(stored)==len(row['states']),'no serialized duplicates')
        check(C_of(p)==row['C'],'cutoff algorithm comparison')
        for a,u,R,D,v,h,r,s,k,x,y,z,ch in states:
            if ch=='norm':
                check(v<=row['C'] and v<R and v<D,'norm chart bounds')
                check((p*p+4*v)%R==0 and a*a%v==0,'norm actual availability')
            elif ch=='direct':check(R<=row['C'] and R<=D and R<v,'direct chart bounds')
            else:
                BB=(p*D+1)//4
                check(D<=row['C'] and D<R and D<v,'reciprocal chart bounds')
                check(u<BB and BB*BB%u==0 and (u+BB)%D==0,'reciprocal original box')
        total+=len(states)
    ex=json.loads((args.input/'examples.json').read_text())
    for key in ('hard_exterior_not_middle_bound','noncoprime_v_D'):fixture(ex[key])
    for z in ex['small_prime_family']:fixture(z)
    z=ex['hard_exterior_not_middle_bound'];p=z['p']
    K=0
    while (6*(K+1)+2)**2<=3*p+73:K+=1
    check(p==48049 and p%840==169 and K==62,'hard example cutoff')
    check(min(z['R'],z['D'])>4*K-1,'cannot apply M cutoff to E')
    z=ex['noncoprime_v_D'];check(gcd(z['v'],z['D'])>1,'do not cancel shared v-D factors')
    for z in ex['asymptotic_integer_family']:
        n=z['n'];h=z['h'];t=z['R'];p=z['p']
        check(h==4*n*n-2 and t==h+1 and z['D']==t,'integer family data')
        check(p==16*n**3-4*n*n-8*n+1 and p%840==289,'integer family residue')
        check(t*t==4*h*n*n+1 and gcd(p,h*n)==1,'integer family exact source')
        check(min(h,t)==h and (p+h)**2>4*(h+1)**2*(h-1),'family cutoff')
        check((p+h+1)**2<=4*(h+2)**2*h,'family next integer excluded')
    p=2521;v=11
    hits=[R for R in range(3,p,4) if (p*p+4*v)%R==0 and (p+R)%44==0]
    check(hits==ex['empty_minimal_norm_grade']['hits']==[],'full fixed grade rejection')
    z=ex['missing_original_availability'];p=z['p'];R=z['R'];v=z['v'];a=(p+R)//4
    check((p*p+4*v)%R==0 and a*a%v!=0,'norm without availability false')
    out={'success':True,'bound':scan['bound'],'primes':len(pp),'canonical_E_states':total,
         'checks':COUNT,'elapsed_seconds':time.monotonic()-start,
         'scan_sha256':hashlib.sha256((args.input/'scan.json').read_bytes()).hexdigest(),
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'independence':'No main or predecessor imports; complete primitive h,r,s enumeration.',
         'universal_ES_proved':False,'universal_E_occupancy_proved':False}
    args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
