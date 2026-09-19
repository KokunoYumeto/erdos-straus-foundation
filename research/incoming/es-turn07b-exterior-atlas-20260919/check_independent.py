#!/usr/bin/env python3
"""Independent complete primitive h,r,s enumeration. No import from main or predecessor."""
from __future__ import annotations
from pathlib import Path
from math import gcd,isqrt
import argparse,json,hashlib
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

def factor_exponents(n):
    out=[];d=2
    while d*d<=n:
        if n%d==0:
            e=0
            while n%d==0:n//=d;e+=1
            out.append(e)
        d+=1
    if n>1:out.append(1)
    return out

def tau(n):
    ans=1
    for e in factor_exponents(n):ans*=e+1
    return ans

def tau_square(n):
    ans=1
    for e in factor_exponents(n):ans*=2*e+1
    return ans

def candidate_counts(p,C):
    direct=sum(tau_square((p+R)//4) for R in range(3,C+1,4))
    reciprocal=sum((tau_square((p*D+1)//4)-1)//2 for D in range(3,C+1,4))
    norm=sum(tau(p*p+4*v) for v in range(2,C+1))
    return {'direct_divisors':direct,'reciprocal_divisors':reciprocal,
            'norm_divisors':norm}

def original_vectors(p):
    return sum(tau_square(a) for a in range(p//4+1,(p-1)//2+1))

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
    check(isinstance(u,int) and u>0,'displayed positive divisor premise')
    check(gcd(p,a)==1 and p<4*a and 2*a<p,'displayed source')
    check(a==h*r*s and u==h*r*r and v==h*s*s,'displayed coordinates')
    check(R==4*a-p and R*k==p*r+s and s*D==r+k,'displayed gate')
    check((x,y,zz)==(a,h*s*k,p*h*r*k),'displayed order')
    check(4*x*y*zz==p*(x*y+x*zz+y*zz),'displayed fractions')
    check((p+R)**2+4*v==4*v*R*D,'displayed norm')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input',type=Path,default=Path('certificates'))
    ap.add_argument('--out',type=Path,default=Path('independent.json'));args=ap.parse_args()
    scan=json.loads((args.input/'scan.json').read_text());rows=scan['rows']
    report=json.loads((args.input/'report.json').read_text())
    pp=[p for p in range(5,scan['bound']+1,4) if prime(p)]
    check([z['p'] for z in rows]==pp,'full prime domain')
    total=0;total_vectors=0
    totals={'direct_divisors':0,'reciprocal_divisors':0,'norm_divisors':0}
    for row in rows:
        p=row['p'];states=all_primitive(p);stored={tuple(x) for x in row['states']}
        check(states==stored,'full primitive equality at '+str(p));check(len(stored)==len(row['states']),'no serialized duplicates')
        check(C_of(p)==row['C'],'cutoff algorithm comparison')
        nv=original_vectors(p);cc=candidate_counts(p,row['C'])
        check(row['original_vectors']==nv,'original vector count at '+str(p))
        check(all(row['candidate_counts'].get(k,0)==v for k,v in cc.items()),
              'candidate counts at '+str(p))
        total_vectors+=nv
        for key,value in cc.items():totals[key]+=value
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
    z=ex['residue_hypothesis_boundary']
    check((z['p'],z['a'],z['u'],z['R'],z['D'],z['v'],z['w'])==(19,6,6,5,5,6,5),
          'literal residue-hypothesis boundary')
    check(z['equality_value']==576 and (z['p']+z['w'])**2==4*(z['w']+1)**2*(z['w']-1),
          'boundary equality outside p == 1 mod 4')
    for key in ('hard_exterior_not_middle_bound','noncoprime_v_D'):fixture(ex[key])
    for z in ex['small_prime_family']:fixture(z)
    z=ex['hard_exterior_not_middle_bound'];p=z['p']
    K=0
    while (6*(K+1)+2)**2<=3*p+73:K+=1
    check(p==48049 and p%840==169 and K==62,'hard example cutoff')
    check(min(z['R'],z['D'])>4*K-1,'cannot apply M cutoff to E')
    z=ex['noncoprime_v_D']
    check(z['p']==37 and (z['a'],z['u'],z['R'],z['D'],z['v'])==(12,8,11,3,18),
          'literal p37 noncoprime fixture')
    check(gcd(z['v'],z['D'])==3,'do not cancel shared v-D factors')
    rc=ex['hard_residue_classification']
    check(rc['modulus_for_n']==210 and rc['residues_for_n']==[24,164],
          'complete hard residue classes')
    check(rc['modulus_for_p']==840 and rc['residue_for_p']==289 and
          rc['universal_prime_values_claimed'] is False,'hard residue metadata')
    check(len(ex['asymptotic_integer_family'])==40,'both sampled residue branches retained')
    for z in ex['asymptotic_integer_family']:
        n=z['n'];h=z['h'];t=z['R'];p=z['p']
        check(h==4*n*n-2 and t==h+1 and z['D']==t,'integer family data')
        check(p==16*n**3-4*n*n-8*n+1 and p%840==289 and n%210 in (24,164),
              'integer family residue')
        check(t*t==4*h*n*n+1 and gcd(p,h*n)==1,'integer family exact source')
        check(min(h,t)==h and (p+h)**2>4*(h+1)**2*(h-1),'family cutoff')
        check((p+h+1)**2<=4*(h+2)**2*h,'family next integer excluded')
    p=2521;v=11
    check(prime(p),'p2521 primality')
    least=next(a for a in range(2,p) if pow(a,(p-1)//2,p)==p-1)
    check(least==11,'p2521 least quadratic nonresidue')
    hits=[R for R in range(3,p,4) if (p*p+4*v)%R==0 and (p+R)%44==0]
    meta=ex['empty_minimal_norm_grade']
    check(hits==meta['hits']==[],'full fixed grade rejection')
    check(meta['p']==p and meta['v']==v and meta['norm']==p*p+4*v and
          meta['required_residue']==31 and meta['modulus']==44,'fixed grade metadata')
    check(meta['p_is_prime'] is True and meta['least_quadratic_nonresidue']==least,
          'fixed grade prime metadata')
    check(meta['residues_below_p']==[1,3,5,9,15,45],
          'complete fixed grade divisors below p')
    check(meta['factorization']==[[3,2],[5,1],[141233,1]],
          'complete fixed grade norm factorization')
    z=ex['missing_original_availability'];p=z['p'];R=z['R'];v=z['v'];a=(p+R)//4
    check((p*p+4*v)%R==0 and a*a%v!=0,'norm without availability false')
    chart_counts={name:0 for name in ('direct','reciprocal','norm')}
    for row in rows:
        for state in row['states']:chart_counts[state[-1]]+=1
    check(report['success'] is True and report['bound']==scan['bound'],
          'main report scope and bound')
    check(report['primes']==len(pp) and report['canonical_E_states']==total and
          report['original_vectors']==total_vectors,
          'main report totals')
    check(report['chart_states']==chart_counts,'main report chart totals')
    check(report['candidate_counts']==totals,'main report candidate totals')
    actual_scan_sha=hashlib.sha256((args.input/'scan.json').read_bytes()).hexdigest()
    check(report['scan_sha256']==actual_scan_sha,'main report scan hash')
    check(report['state_domain']['u']=='positive divisor of a^2',
          'main report positive divisor domain')
    out={'success':True,'bound':scan['bound'],'primes':len(pp),'canonical_E_states':total,
         'checks':COUNT,
         'scan_sha256':actual_scan_sha,
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'independence':'No main or predecessor imports; complete primitive h,r,s enumeration.',
         'universal_ES_proved':False,'universal_E_occupancy_proved':False}
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',
                        encoding='utf-8',newline='\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
