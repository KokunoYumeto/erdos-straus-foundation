#!/usr/bin/env python3
"""Separate exact implementation. Imports neither arithmetic.py nor verify.py.
Recomputes finite scopes; this is not independent human review.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import gcd, isqrt, prod
from collections import Counter
from pathlib import Path
import argparse,json

N=0

def ck(v,msg='separate checker failure'):
    global N
    N+=1
    if not v:raise RuntimeError(msg)


def prime(n):
    return n>=2 and all(n%j for j in range(2,isqrt(n)+1))


def primes(n):
    arr=[True]*(n+1);arr[0]=arr[1]=False
    for k in range(2,isqrt(n)+1):
        if arr[k]:
            for v in range(k*k,n+1,k):arr[v]=False
    return arr

@lru_cache(None)
def fac(n):
    fs=[];p=2
    while p*p<=n:
        if n%p==0:
            e=0
            while n%p==0:n//=p;e+=1
            fs.append((p,e))
        p+=1
    if n>1:fs.append((n,1))
    return tuple(fs)

@lru_cache(None)
def words(a):
    factors=fac(a)
    return tuple(sorted(prod(q**f for (q,e),f in zip(factors,exps))
         for exps in product(*(range(2*e+1) for q,e in factors))))


@lru_cache(None)
def divs(n):
    factors=fac(n)
    return tuple(sorted(prod(q**e for (q,_),e in zip(factors,exps))
         for exps in product(*(range(v+1) for _,v in factors))))


def record_check(z):
    p,a,R,u=(z[k] for k in('p','a','R','u'));h,r,s=(z[k] for k in('h','r','s'))
    ck(R==4*a-p and p<4*a<2*p and a*a%u==0 and gcd(a,R)==1)
    ck(a==h*r*s and u==h*r*r and gcd(r,s)==1)
    es=fac(a);fu=dict(fac(u));ck(z['exponents']==[dict(prime=q,e=e,f=fu.get(q,0),beta=fu.get(q,0)-e) for q,e in es])
    if z['channel']=='E':
        y=Fraction(p*a+a*a//u,R);zz=Fraction(p*a+p*p*u,R)
        quotient=Fraction(p*r+s,R);G=4*u+1
        inv=Fraction(a*a,R*y-p*a)
    else:
        y=Fraction(p*(a+a*a//u),R);zz=Fraction(p*(a+u),R)
        quotient=Fraction(r+s,R);G=p+4*u
        inv=Fraction(p*a*a,R*y-p*a)
    ck(inv==u and sum((Fraction(1,a),1/y,1/zz))==Fraction(4,p))
    ck(z['denominators']==[[a,1],[y.numerator,y.denominator],[zz.numerator,zz.denominator]])
    ck(z['quotient']==[quotient.numerator,quotient.denominator])
    ck(z['trace']==((y+zz).denominator==1) and z['full']==(y.denominator==zz.denominator==1))
    ck(y.denominator==zz.denominator==z['common_denominator'])
    k=prod(q**((e+1)//2) for q,e in fac(R));D=R//k
    value=(pow(p,z['channel']=='E',R)*u*pow(a,-1,R))%R
    ck(z['K']==k and z['D']==D)
    if z['trace']:
        c=((value+1)//k)%D
        ck(c==z['defect'] and D//gcd(D,c)==y.denominator)
    return (a,y,zz)


def square_check(data):
    B=data['summary']['bound'];isp=primes(B);actual=[]
    for q in range(5,isqrt(B//2)+1):
        if not isp[q]:continue
        a=q*q
        # Search primes in the entire integer interval, not divisors of proposed gates.
        start=2*a+1;start+=(1-start)%24
        for p in range(start,min(4*a,B+1),24):
            if not isp[p]:continue
            R=4*a-p;hits=[]
            for f in range(5):
                u=q**f
                for ch,num in [('E',(a+p*u)**2),('M',p*(a+u)**2)]:
                    if num%(R*u)==0:
                        den1=R//gcd(R,(p*a+a*a//u) if ch=='E' else p*(a+a*a//u))
                        hits.append((ch,u,den1==1))
            if hits:actual.append((p,q,sorted(hits)))
    expected=[]
    for row in data['shells']:
        hs=[]
        for rec in row['records']:
            record_check(rec);hs.append((rec['channel'],rec['u'],rec['full']))
            if rec['channel']=='M' and not rec['full']:
                R=rec['R'];u=rec['u'];p=rec['p']
                for Rnew in range(3,R+1,4):
                    if R%Rnew:continue
                    anew=(p+Rnew)//4
                    ck(not(anew*anew%u==0 and (p+4*u)%Rnew==0),'terminal square word')
        expected.append((row['p'],row['q'],sorted(hs)))
    ck(sorted(actual)==sorted(expected),'complete prime-square interval census')


def box_check(data):
    B=data['bound'];isp=primes(B);counts=Counter()
    for p in range(1,B+1,24):
        if not isp[p]:continue
        counts['primes']+=1
        for a in range(p//4+1,(p+1)//2):
            R=4*a-p;ds=words(a);counts['shells']+=1;counts['divisor_words']+=len(ds)
            for u in ds:
                for ch,nu in [('E',(a+p*u)**2),('M',p*(a+u)**2)]:
                    if nu%(R*u):continue
                    counts[ch+'_traces']+=1
                    tailnu=p*a+a*a//u if ch=='E' else p*(a+u)
                    counts[ch+('_full' if tailnu%R==0 else '_proper')]+=1
    for k,v in counts.items():ck(data['counts'][k]==v,'box census '+k)
    for row in data['shells']:
        R,p,a=row['R'],row['p'],row['a'];k,D=row['K'],row['D'];seen=[]
        for tile in row['tiles']:
            cs=[0]*D;states=[]
            for tt in product(*(range(n) for n in tile['lengths'])):
                beta=[b+o*j for b,o,j in zip(tile['base'],tile['orders'],tt)]
                u=prod(q**(e+b) for q,e,b in zip(tile['primes'],tile['exponents'],beta))
                zz=(pow(p,tile['channel']=='E',R)*u*pow(a,-1,R))%R
                ck((zz+1)%k==0)
                c=((zz+1)//k)%D
                add=sum(l*j for l,j in zip(tile['lambdas'],tt))%D
                ck(c==(tile['c0']-add)%D);cs[add]+=1
                full=(c==0);seen.append([tile['channel'],u,full])
                if full:states.append(u)
            ck(cs==tile['coefficient_vector'] and states==tile['full_words'])
            ck(tile['stabilizer']==[j for j in range(D) if all(cs[x]==cs[(x+j)%D] for x in range(D))])
        ck(sorted(seen)==sorted(row['direct_trace_words']))
    return dict(counts)


def prefix_check(data):
    B=data['bound'];isp=primes(B);expectedp=[p for p in range(1,B+1,24) if isp[p]]
    ck(expectedp==[r['p'] for r in data['primes']])
    misses=[]
    for row in data['primes']:
        p=row['p'];tr=None;fu=None
        ck([s['R'] for s in row['shells']]==list(range(3,row['first_full']+1,4)))
        for old in row['shells']:
            R=old['R'];a=(p+R)//4;hits=[]
            for u in words(a):
                for ch,num in [('E',(a+p*u)**2),('M',p*(a+u)**2)]:
                    if num%(R*u)==0:
                        tailnum=p*a+a*a//u if ch=='E' else p*(a+u)
                        hits.append([ch,u,tailnum%R==0])
            ck(sorted(hits)==sorted(old['traces']) and len(words(a))==old['word_count'])
            if hits and tr is None:tr=R
            if any(h[2] for h in hits) and fu is None:fu=R
        ck((tr,fu)==(row['first_trace'],row['first_full']))
        if tr!=fu:misses.append(p)
    ck(misses==data['exceptions']==[67369])
    for pp,rows in data['full_failure_words'].items():
        p=int(pp)
        for r in rows:
            a,R=r['a'],r['R'];ck(words(a)==tuple(x['u'] for x in r['words']))
            for x in r['words']:ck((x['E'],x['M'])==((4*x['u']+1)%R,(p+4*x['u'])%R))


def worked_check(data):
    mm=data['mixed'];values=[record_check(x) for x in mm['inputs']];record_check(mm['target'])
    p,a=mm['target']['p'],mm['target']['a']
    us=[x['u'] for x in mm['inputs']]
    ck(Fraction(us[0]*us[2],us[1])==mm['target']['u'])
    ck([x['defect'] for x in mm['inputs']]==[1,2,1] and mm['target']['defect']==0)
    for r in data['pell']:
        p,q,delta,t,w,k=(r[n] for n in('p','q','delta','t','w','k'))
        ck(prime(p) and prime(q),'Pell isolated primes')
        ck(t*t-4*delta*w*w==1 and q+1==delta*t*k)
        arrow=r['arrow'];record_check(arrow['source']);record_check(arrow['target'])
        h,s=arrow['source']['h'],arrow['source']['s'];hp,sp=arrow['target']['h'],arrow['target']['s']
        ck((hp,sp)==(h-delta*w,s+delta*w) and hp*sp==(p+delta)//4)
        want=[]
        h0,r0,s0=(arrow['target'][n] for n in ('h','r','s'))
        for c in range(1,isqrt(h0)+1):
            if h0%(c*c):continue
            hp0=h0//(c*c);rraw=c*r0;sp0=c*s0
            for b in range((-hp0)//delta+1,(sp0-1)//delta+1):
                h0s=hp0+delta*b;s0s=sp0-delta*b;R0=4*h0s*rraw*s0s-p
                if gcd(rraw,s0s)!=1 or R0<=0 or R0>=p or R0%delta:continue
                t0=isqrt(R0//delta)
                if delta*t0*t0!=R0 or (rraw+s0s)**2%R0:continue
                want.append((b,c,h0s,rraw,s0s,R0))
        got=[]
        for v in r['inverse']:
            record_check(v['source']);got.append((v['w'],v['normalization_gcd'],v['source']['h'],v['source']['r'],v['source']['s'],v['source']['R']))
        ck(got==want,'full factor-sum inverse fibre')
    for row in data['general_factor_sum']:
        src=row['source'];record_check(src)
        delta=src['delta'];t=src['D'];h,s=src['h'],src['s']
        for ar in row['returns']:
            record_check(ar['target']);w=ar['w']
            ck(src['r']*(delta*w*w+(s-h)*w)==(t*t-1)//4)
            ck(ar['normalization_gcd']==gcd(src['r'],s+delta*w))
            # Recover every incoming source from the primitive target, by a
            # separate literal product/residual enumeration (not its quadratic).
            tar=ar['target']; h0,r0,s0=(tar[n] for n in ('h','r','s'))
            want=[]
            for c in range(1,isqrt(h0)+1):
                if h0%(c*c):continue
                hr=h0//(c*c);rr=c*r0;sr=c*s0
                for shift in range((-hr)//delta+1,(sr-1)//delta+1):
                    hh=hr+delta*shift;ss=sr-delta*shift
                    residual=4*hh*rr*ss-tar['p']
                    if gcd(rr,ss)!=1 or not(0<residual<tar['p']) or residual%delta:continue
                    sq=isqrt(residual//delta)
                    if delta*sq*sq!=residual or (rr+ss)**2%residual:continue
                    want.append((shift,c,hh,rr,ss,residual))
            got=[]
            for incoming in ar['inverse']:
                rec=incoming['source'];record_check(rec)
                got.append((incoming['w'],incoming['normalization_gcd'],rec['h'],rec['r'],rec['s'],rec['R']))
            ck(got==want,'general complete inverse fibre')
    for rr in data['recurrence']:ck(rr['t']**2-12*rr['w']**2==1)


def sharp_check(data):
    for row in data['templates']:
        ell,q,e,R=(row[n] for n in ('ell','q','e','R'))
        ck(prime(ell) and prime(q) and ell%4==3 and q%R==ell*ell-1)
        P=row['prime_progression'];ck(gcd(P['residue'],P['modulus'])==1)
        ck(P['residue']%840==1 and (P['residue']+R-4*q**e)%q**(e+1)==0)
        ck(row['a']==(row['sample_integer']+R)//4 and row['h']*q**e==row['a'])
        expected=[]
        for beta in range(-e,e+1):
            z=pow(q,beta,R)
            if (z+1)%(ell*ell)==0:
                expected.append(dict(beta=beta,defect=((z+1)//(ell*ell))%ell,u=row['h']*q**(e+beta)))
        ck(row['packet']==expected and all(x['defect']!=0 for x in expected))
        if 'isolated_prime' in row:
            pp=row['isolated_prime'];ck(prime(pp['p']))
            for r in pp['original_M_words']:record_check(r)


def fixed_tail_check(data):
    """Separate derivation of the fixed numerical tail-sum fibre."""
    source=data['source'];a,y,z=record_check(source)
    p=source['p'];R=source['R'];N=y+z
    ck((p,a,R,source['u'],source['channel'])==(67369,16849,27,1421,'M'))
    ck(N==586110300)
    B=R*y-p*a;C=R*z-p*a;w=B-C;DD=int(N)*(int(N)-p)
    ck((B,C,w)==(13459046189,95731349,13363314840))
    ck(w*w==DD*R*R-int(N)*p*p*R and w%R==18)
    U=2*DD*R-p*p*int(N);V=2*w
    ck(U*U-DD*V*V==p**4*int(N)**2)

    eligible=[rho for rho in divs(int(N)) if rho<p and (p+rho)%4==0]
    ck(eligible==[3,15,75,87,435,2175])
    got=[]
    for row,rho in zip(data['selected_fibre']['candidates'],eligible):
        disc=DD-int(N)*p*p//rho
        ck(row['rho']==rho and row['discriminant']==disc)
        if disc>=0:
            root=isqrt(disc);ck(row['floor_sqrt']==root and root*root!=disc)
        got.append(rho)
    ck(data['selected_fibre']['targets']==[])

    pos=data['positive_recovery_control'];pa,py,pz=record_check(pos['source'])
    pN=py+pz;ck((pa,pos['source']['R'],pos['source']['u'],pN)==(16850,31,674,98750810744))
    want={(31,16850,36631900,98714178844),(31,16850,98714178844,36631900)}
    got={(t['rho'],t['a'],t['Y'],t['Z']) for t in pos['fibre']['targets']}
    ck(got==want)

    proper={};full_sums=set();proper_tags=0;full_tags=0
    for aa in range(p//4+1,(p+1)//2):
        rr=4*aa-p
        for u in words(aa):
            Ey=Fraction(p*aa+aa*aa//u,rr);Ez=Fraction(p*aa+p*p*u,rr)
            My=Fraction(p*(aa+aa*aa//u),rr);Mz=Fraction(p*(aa+u),rr)
            for ch,yy,zz in [('E',Ey,Ez),('M',My,Mz)]:
                NN=yy+zz
                if NN.denominator!=1:continue
                if yy.denominator==zz.denominator==1:
                    full_tags+=1;full_sums.add(NN.numerator)
                else:
                    proper_tags+=1;proper.setdefault(NN.numerator,[]).append((aa,rr,u,ch))
    ck((proper_tags,len(proper),full_tags,len(full_sums))==(69,51,47,37))
    ck(set(proper).isdisjoint(full_sums))
    candidate_count=0;nonnegative=0
    for NN in proper:
        D0=NN*(NN-p)
        for rho in divs(NN):
            if not(rho<p and (p+rho)%4==0):continue
            candidate_count+=1;disc=D0-NN*p*p//rho
            if disc>=0:
                nonnegative+=1;root=isqrt(disc);ck(root*root!=disc)
    ck((candidate_count,nonnegative)==(507,478))
    census=data['p67369_census']
    ck((census['proper_trace_tags'],census['proper_tail_sums'],census['integral_tags'],
        census['integral_tail_sums'],census['eligible_residual_candidates'],
        census['nonnegative_discriminants'])==(69,51,47,37,507,478))
    ck(census['shared_tail_sums']==[])


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input',default='certificates');ap.add_argument('--out',default='certificates/independent.json')
    a=ap.parse_args();p=Path(a.input)
    get=lambda n:json.loads((p/n).read_bytes())
    counts=box_check(get('box_tiles.json'));square_check(get('prime_squares.json'))
    prefix_check(get('prefix_certificate.json'));worked_check(get('worked_examples.json'));sharp_check(get('sharp_packets.json'))
    fixed_tail_check(get('fixed_tail_sum.json'))
    result=dict(checks=N,box_counts=counts,prime_square_interval_reproduced=True,
        prefix_least_counterexample_reproduced=True,all_worked_identities_pass=True,
        fixed_tail_sum_fibre_reproduced=True,
        imports_main_implementation=False,independent_human_review=False)
    Path(a.out).write_bytes((json.dumps(result,indent=2,sort_keys=True)+'\n').encode('utf-8'))
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
