#!/usr/bin/env python3
"""Separate exact replay of unit-boundary certificates. No verifier imports.
Checks original divisor states, prime proofs, packet integer coefficients,
relative unit images, and the stated bounded census. Not a Lean proof.
"""
from __future__ import annotations
import argparse,json
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb,gcd,isqrt,prod
from pathlib import Path
CHECKS=Counter()
def need(x,label):
    CHECKS[label]+=1
    if not x:raise ArithmeticError(label)
def read(path):return json.loads(path.read_text())
def frac(x):return Fraction(x['n'],x['d']) if isinstance(x,dict) else Fraction(x)
def prime(n):return n>=2 and all(n%i for i in range(2,isqrt(n)+1))
def sieve(n):
    out=bytearray(b'\1')*(n+1);out[:2]=b'\0\0'
    for a in range(2,isqrt(n)+1):
        if out[a]:out[a*a::a]=b'\0'*len(out[a*a::a])
    return [i for i in range(2,n+1) if out[i]]
SMALL=sieve(5000)
def factor(n):
    out=[]
    for q in SMALL:
        if q*q>n:break
        e=0
        while n%q==0:n//=q;e+=1
        if e:out.append((q,e))
    else:
        q=SMALL[-1]+2
        while q*q<=n:
            e=0
            while n%q==0:n//=q;e+=1
            if e:out.append((q,e))
            q+=2
    if n>1:out.append((n,1))
    return out

def divisors(fs):
    return sorted(prod(q**i for (q,e),i in zip(fs,es)) for es in product(*(range(e+1) for q,e in fs)))
def exponent(n,q):
    i=0
    while n%q==0:n//=q;i+=1
    return i

def state(st):
    p,R,u,a,Q=[st[x] for x in ('p','R','u','a','Q')]
    h,r,s,lam=[st[x] for x in ('h','r','s','lambda_')]
    x,y,z=st['denominators']
    need(R*Q==p+4*u and 4*a==p+R,'original_seed_factor_equations')
    need(h*r*s==a and h*r*r==u and gcd(r,s)==1,'original_divisor_normalization')
    need(R*lam==r+s and all(v>0 for v in (p,R,Q,h,r,s,lam,x,y,z)),'positive_middle_gate')
    need((x,y,z)==(a,p*h*s*lam,p*h*r*lam),'ordered_denominators')
    need(4*x*y*z==p*(x*y+x*z+y*z),'cleared_ES_identity')
    need(Fraction(p*a*a,R*y-p*a)==u,'ordered_original_inverse')

def cert_check(cert,fs,st=None,full=True):
    k,p=cert['k'],cert['p'];o=1<<(k-2);m=1<<k;N=p+(1<<(2*k-3));base=cert['base']
    need(prod(q**e for q,e in fs)==N,'actual_factorization_input')
    A=1;seen=[]
    for bl in cert['blocks']:
        ids=bl['indices'];seen+=ids
        for ix,a,step in zip(ids,bl['offsets'],bl['steps']):
            e=fs[ix][1];L=bl['capacity']
            need(0<=a<=e and 0<=a+step*L<=e,'actual_affine_endpoints')
            A*=fs[ix][0]**a
        residue=prod(pow(fs[ix][0],step,m) for ix,step in zip(ids,bl['steps']))%m
        need(residue==pow(base,bl['log'],m),'physical_affine_step_log')
    need(sorted(seen)==list(range(len(fs))) and A==cert['constant'],'disjoint_original_coordinate_partition')
    need(pow(base,cert['phase'],m)==p%m,'actual_phase_role')
    rec=cert['certificate'];cs=rec['selected'];logs=cert['logs'];d=rec['index']
    need(1<d<o and o%d==0,'proper_nontrivial_relative_index')
    P=[0]*o
    # Direct integer enumeration, not the characteristic-two normalized-unit product.
    sets=[[v for v in range(c+1) if v&~c==0] for c in cs]
    for ts in product(*sets):P[sum(a*t for a,t in zip(logs,ts))%o]+=1
    need(all(P[i]%2==((rec['quotient_X']>>(i%d))&1) for i in range(o)),'original_packet_relative_parity')
    ft=[sum((P[i]%2)*comb(i,j) for i in range(j,o))%2 for j in range(o)]
    need(next(i for i,v in enumerate(ft) if v)==rec['weight'],'direct_binomial_exact_order')
    qt=rec['quotient_T']
    need(all(ft[o-d+j]==(qt>>j&1) for j in range(d)),'retained_unit_T_coordinates')
    g=[0]*d
    lowsets=[range(E+1) if c==0 else (0,) for c,E in zip(cs,cert['capacities'])]
    for ts in product(*lowsets):g[sum(a*t for a,t in zip(logs,ts))%d]+=1
    low=sum(g[j]*((rec['quotient_X']>>((cert['target']-j)%d))&1) for j in range(d))
    need(low==rec['lower_count'] and low>0,'integer_lower_target_mass')
    if full:
        hits=[]
        allsets=[sets[i] if c else range(cert['capacities'][i]+1) for i,c in enumerate(cs)]
        for ts in product(*allsets):
            ex=[0]*len(fs)
            for bl,t in zip(cert['blocks'],ts[:-1]):
                for ix,a,step in zip(bl['indices'],bl['offsets'],bl['steps']):ex[ix]=a+step*t
            word=prod(q**i for (q,e),i in zip(fs,ex));role=ts[-1]
            need(N%word==0 and role in (0,1),'every_integer_packet_word_available')
            if word*pow(p,-role,m)%m==m-1:
                co=word if role==0 else N//word;hits.append(co)
        need(len(hits)>=low,'lower_bound_is_on_actual_role_words')
        need(len(set(hits))*2>=len(hits),'cofactor_role_fibre_bound')
        if st is not None:need(st['Q'] in hits,'constructed_original_state_is_in_packet')
    if st is not None:state(st)
    return sum(P)

def family_proofs(data):
    recs=[]
    for row in data:
        p=row['p'];k=row['k'];d=row['d'];fs=row['factorization'];q,r,s=row['auxiliary_primes'];N=row['N']
        need(all(prime(t) for t,e in fs),'actual_factor_primality')
        pc=row['primality'];a=pc['base'];pm=pc['p_minus_one']
        need(prod(t**e for t,e in pm)==p-1 and all(prime(t) for t,e in pm),'complete_order_prime_factors')
        need(pow(a,p-1,p)==1 and all(gcd(pow(a,(p-1)//t,p)-1,p)==1 for t,e in pm),'deterministic_prime_proof')
        cof=[x for x in divisors(fs) if x%(1<<k)==(1<<k)-1]
        need(cof==row['cofactors']==[3**(d//2-1)*q*s],'exhaustive_unique_cofactor')
        Q=cof[0];R=N//Q
        need(sum(exponent(Q,t) for t,e in fs)==sum(exponent(R,t) for t,e in fs)==d//2+1,'both_roles_exact_word_length')
        cert_check(row['certificate'],fs,row['returned']['state'])
        cert=row['certificate'];cs=cert['certificate']['selected'];logs=cert['logs'];o=1<<(k-2)
        original={}
        sets=[[v for v in range(c+1) if v&~c==0] for c in cs]
        for ts in product(*sets):original.setdefault(sum(a*t for a,t in zip(logs,ts))%o,[]).append(list(ts))
        returned={}
        for cell in row['returned']['complete_high_source_partition']:
            words=[] if cell['selected_norm_word'] is None else [cell['selected_norm_word']]
            words += [word for pair in cell['paired_even_words'] for word in pair]
            returned[cell['residue']]=sorted(words)
        need(returned=={r:sorted(words) for r,words in original.items()},'complete_original_even_pair_partition')
        # An independently computed complete signed-residue product confirms the symbolic formula.
        o=4*d;P=[0]*o
        for i in range(d):
            for j in (0,1):
                for ep in (0,1):P[(i+(3*d-1)*j+d*ep)%o]+=1
        q0=[int(d-1<=j<2*d) for j in range(2*d)]
        need(P==[q0[j%(2*d)]+2*int(j<d-1) for j in range(o)],'literal_family_coefficient_identity')
        recs.append(dict(p=p,k=k,Q=Q,R=R,word_length=d//2+1))
    return recs

def abstract(data):
    cases=0
    for rec in data['integral_circulants']:
        D,h=rec['D'],rec['h'];q=rec['quotient'];iv=list(map(frac,rec['inverse']))
        for i in range(D):
            need(sum(q[(i-j)%D]*iv[j] for j in range(D))==int(i==0),'full_rational_circulant_inverse')
        need(abs(frac(rec['determinant']))==h,'declared_integral_index');cases+=1
    for row in data['original_word_metrics']:
        P=row['original_coefficients'];D=8
        w=[sum((Fraction(1,P[r]) for r in range(j,len(P),D) if P[r]),Fraction()) for j in range(D)]
        need(list(map(frac,row['quotient_weights']))==w,'original_word_counting_quotient_weights')
        need(row['available_periodic_cosets']==[j for j in range(D) if all(P[r] for r in range(j,len(P),D))],'formal_inverse_actual_available_domain')
        C=[[int((i-j)%D>=3) for j in range(D)] for i in range(D)]
        expected=[[sum((C[r][i]*w[r]*C[r][j] for r in range(D)),Fraction()) for j in range(D)] for i in range(D)]
        need([[frac(x) for x in r] for r in row['transported_Gram']]==expected,'full_mixed_original_Gram')
    for row in data['family']:
        k=row['algebra']['k'];d=1<<(k-4);o=4*d
        # Formula bounds are checked independently of the source algorithm maxima.
        for s,mass in row['old_envelope']['maximal_mass']:
            envelope=2*d+2 if s==1 else d+1 if s==2 else 2*d//s if s<=d else 0
            need(mass<=envelope<o//s-1,'uniform_old_capacity_envelope')
    return cases

def census(data):
    B=data['bound'];ps=[p for p in sieve(B) if p%840 in {1,121,169,289,361,529}]
    expected=[]
    for p in ps:
        k=4
        while p>1<<(2*k-4):expected.append((p,k));k+=1
    need(expected==[(r[0],r[1]) for r in data['rows']],'complete_prime_and_seed_universe')
    lookup={};total=0
    for row in data['rows']:
        p,k,N,fs,old,new,short,two,count,minimum=row;m=1<<k
        fs0=factor(N);need(fs==[list(z) for z in fs0],'independent_actual_factorization')
        hits=[Q for Q in divisors(fs0) if Q%m==m-1]
        need(len(hits)==count,'independent_original_count')
        length=min((min(sum(exponent(Q,q) for q,e in fs0),sum(exponent(N//Q,q) for q,e in fs0)) for Q in hits),default=None)
        need(length==minimum,'complete_short_word_baseline')
        need(not(new or old or short or two) or bool(hits),'all_reported_tests_are_sufficient_in_finite_scan')
        lookup[(p,k)]=(fs0,new);total+=count
    need(len(data['new_certificates'])==sum(row[5] for row in data['rows']),'every_positive_new_test_has_retained_certificate')
    for obj in data['new_certificates']:
        c=obj['certificate'];fs,new=lookup[(c['p'],c['k'])];need(new,'certificate_in_exact_scan_domain')
        cert_check(c,fs,obj['state'],full=False)
    return dict(bound=B,primes=len(ps),branches=len(expected),states=total,new_certificates=len(data['new_certificates']))

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--input',default='certificates');ap.add_argument('--out',default='independent.json');a=ap.parse_args()
    root=Path(a.input)
    result=dict(family=family_proofs(read(root/'examples.json')),circulants=abstract(read(root/'structural.json')),
                scan=census(read(root/'scan.json')))
    result['checks']=dict(CHECKS);result['total_checks']=sum(CHECKS.values())
    Path(a.out).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'checks':result['total_checks'],'scan':result['scan']},sort_keys=True))
if __name__=='__main__':main()
