#!/usr/bin/env python3
"""Separate checker: primitive parameters, literal target divisors, direct fractions.
Imports neither verify.py nor any predecessor implementation.
"""
from __future__ import annotations
import argparse, hashlib, json, time
from collections import Counter,defaultdict
from fractions import Fraction
from functools import lru_cache
from math import gcd,isqrt,lcm,prod
from pathlib import Path
C=0
def require(ok:bool,msg:str)->None:
    global C
    C+=1
    if not ok:raise ArithmeticError(msg)
@lru_cache(None)
def fs(n:int)->tuple:
    result=[];p=2
    while p*p<=n:
        e=0
        while n%p==0:n//=p;e+=1
        if e:result.append((p,e))
        p=3 if p==2 else p+2
    if n>1:result.append((n,1))
    return tuple(result)
@lru_cache(None)
def ds(n:int,e:int=1)->tuple:
    a=[1]
    for p,f in fs(n):
        b=[]
        for x in a:
            y=x
            for i in range(e*f+1):b.append(y);y*=p
        a=b
    return tuple(sorted(a))
def isprime(n:int)->bool:
    if n<2:return False
    return all(n%d for d in range(2,isqrt(n)+1))
def budget(n:int)->int:return prod(p**((e+1)//2) for p,e in fs(n))
def squarepart(n:int)->int:return prod(p**(e//2) for p,e in fs(n))
def omega(n:int)->int:return sum(e for _,e in fs(n))
def phi(n:int)->int:return prod((p-1)*p**(e-1) for p,e in fs(n))
def square_group_order(m:int)->int:
    return prod(2**max(0,e-3) if p==2 else (p-1)*p**(e-1)//2
                for p,e in fs(m))
def fraction_pair(p,a,u,tag):
    R=4*a-p
    if tag=='E': b=a*a//u;c=p*p*u
    else:b=p*a*a//u;c=p*u
    require(b*c==(p*a)**2,'integer factor-pair product')
    return Fraction(p*a+b,R),Fraction(p*a+c,R)
def target(p,a,u,tag):
    R=4*a-p;y,z=fraction_pair(p,a,u,tag)
    require(y.denominator==z.denominator==1,'integer target denominators')
    xyz=[a,int(y),int(z)]
    require(sum(Fraction(1,x) for x in xyz)==Fraction(4,p),'target identity')
    g=gcd(a,u);h=g*g//u;r=u//g;s=a//g
    v=(p*r+s)//R if tag=='E' else (r+s)//R
    ret=dict(p=p,a=a,R=R,u=u,channel=tag,h=h,r=r,s=s,denominators=xyz)
    ret['kappa' if tag=='E' else 'lambda']=v
    require(h*r*s==a and h*r*r==u and gcd(r,s)==1,'target marking')
    num=a*a*(p if tag=='M' else 1)
    require(num==u*(R*xyz[1]-p*a),'target labelled inverse')
    return ret

def direct_outputs(p:int,a:int,u:int,tag:str)->list:
    R=4*a-p;output=[]
    for R1 in ds(R):
        if R1%4!=3:continue
        a1=(p+R1)//4
        if a1*a1%u:continue
        y,z=fraction_pair(p,a1,u,tag)
        if y.denominator!=1 or z.denominator!=1:continue
        output.append(dict(removal=R//R1,target=target(p,a1,u,tag)))
    return sorted(output,key=lambda o:o['removal'])

def check_coefficient_structure(R:int,u:int,d:int,ks:list,square_ks:list)->None:
    m=4*budget(u)
    residue_counts=Counter(v%m for v in ds(R//d))
    require(residue_counts[pow(d,-1,m)]==len(ks),
            'independent divisor coefficient')
    require(sum(residue_counts.values())==len(ds(R//d)),
            'complete divisor coefficient mass')
    t=squarepart(R);q0=budget(d)
    require(t%q0==0,'square root capacity')
    qs=[q0*v for v in ds(t//q0) if (q0*v)**2%m==1]
    require(sorted(q*q for q in qs)==square_ks,
            'independent square coefficient')
    if ks:
        require(min(omega(k//d) for k in ks)<=phi(m)-1,
                'divisor word-length bound')
    if qs:
        require(min(omega(q//q0) for q in qs)<=square_group_order(m)-1,
                'square word-length bound')
    if 36%u==0:
        require(qs==[q0*v for v in ds(t//q0)],
                'automatic complete square family')
        require(len(qs)==len(ds(t//q0)) and q0*q0 in ks,
                'automatic square multiplicity')

def check_scan(path:Path)->dict:
    data=json.loads((path/'scan.json').read_text());expected=json.loads((path/'sources.json').read_text())
    lookup={(r['p'],r['a'],r['u'],r['channel']):r for r in expected}
    require(len(lookup)==len(expected),'unique source rows')
    seen=set();total=Counter();signature=[];source_to_targets=defaultdict(set);prime_rows=[]
    for p in range(5,data['bound']+1,4):
        if not isprime(p):continue
        total['primes']+=1;pc=Counter()
        for a in range(p//4+1,(p+1)//2):
            R=4*a-p;total['shells']+=1
            for r in ds(a):
                for s in ds(a//r):
                    if gcd(r,s)!=1:continue
                    h=a//(r*s);u=h*r*r;total['original_divisor_vectors']+=1
                    for tag,n in [('E',p*r+s),('M',r+s)]:
                        # Test the literal trace denominator by integer
                        # numerator/gcd arithmetic before constructing Fractions.
                        # This preserves the direct biconditional check while
                        # avoiding millions of temporary rational objects on
                        # rejected words.
                        trace_numerator=(h if tag=='E' else p*h)*n*n
                        trace_denominator=R//gcd(R,trace_numerator)
                        trace=trace_denominator==1
                        require(trace==(n*n%R==0),'literal trace biconditional')
                        if not trace:continue
                        v=Fraction(n,R)
                        yz=(h*s*v,p*h*r*v) if tag=='E' else (p*h*s*v,p*h*r*v)
                        require((yz[0]+yz[1]).denominator==1,
                                'accepted literal trace is integral')
                        d=R//gcd(R,n);S=int(yz[0]+yz[1])
                        require(yz[0].denominator==yz[1].denominator==d,
                                'literal common denominator')
                        require(d*d==R//gcd(R,S),'trace denominator square identity')
                        require(sum((Fraction(1,a),1/yz[0],1/yz[1]))==Fraction(4,p),
                                'source identity')
                        if n%R==0:
                            total['integral_'+tag]+=1;pc['integral_'+tag]+=1
                            output=direct_outputs(p,a,u,tag)
                            ks=[o['removal'] for o in output]
                            m=4*budget(u)
                            expected_ks=[k for k in ds(R) if k%m==1]
                            require(ks==expected_ks and 1 in ks,
                                    'complete integral-source return set')
                            square_ks=[k for k in ks if isqrt(k)**2==k]
                            check_coefficient_structure(R,u,1,ks,square_ks)
                            total['integral_returned_records']+=len(ks)
                            if any(k>1 for k in ks):
                                total['integral_nontrivial_return_sources']+=1
                            continue
                        key=(p,a,u,tag);require(key in lookup and key not in seen,'source bijection')
                        seen.add(key);row=lookup[key];total['proper_'+tag]+=1;pc['proper_'+tag]+=1
                        require(row['R']==R==4*a-p,'source residual field')
                        require(d==yz[1].denominator==row['denominator'],'literal denominator')
                        require(row['square_root_part']==squarepart(R),
                                'source square-root part')
                        comp=a*a//u;cy,cz=fraction_pair(p,a,comp,tag)
                        comp_trace=(cy+cz).denominator==1
                        expected_comp=(tag=='M' or (p*p-1)%budget(R)==0)
                        require(row['complement']==comp and
                                row['complement_is_trace']==comp_trace==expected_comp,
                                'complement involution and gate')
                        require(a*a//comp==u,'complement involution')
                        if tag=='M':require((cy,cz)==(yz[1],yz[0]),'middle tail swap')
                        output=direct_outputs(p,a,u,tag)
                        require(all(o['target']['a']<a for o in output),
                                'strict decrease')
                        require(output==row['targets'],'entire target set')
                        ks=[o['removal'] for o in output]
                        require(ks==row['removals'],'removal list')
                        square_ks=[k for k in ks if isqrt(k)**2==k]
                        require(square_ks==row['square_removals'],'square subfamily')
                        m=4*budget(u)
                        require(m==row['budget_modulus'],'word budget')
                        q0=budget(d)
                        require(q0==row['minimum_square_factor'],'least square factor')
                        check_coefficient_structure(R,u,d,ks,square_ks)
                        if 36%u==0:require(q0*q0 in ks,'automatic seed return')
                        total['returned_records']+=len(ks)
                        if ks:total['repairable_'+tag]+=1;pc['repairable_'+tag]+=1
                        if row['square_removals']:total['square_repairable_'+tag]+=1
                        if 36%u==0:total['automatic_seed_sources']+=1
                        for o in output:
                            q=(p,o['target']['a'],u,tag)
                            source_to_targets[q].add((a,R,o['removal']))
                        signature.append([p,a,u,tag,d,ks])
        prime_rows.append(dict(p=p,**pc))
    require(len(seen)==len(expected),'all original sources independently reached')
    require(prime_rows==data['primes'],'complete per-prime table')
    for (p,a1,u,tag),records in source_to_targets.items():
        R1=4*a1-p;G=4*u+(1 if tag=='E' else p);m=4*budget(u)
        fibre=[k for k in range(1,(p-1)//R1+1)
               if k%m==1 and G*G%(R1*k)==0 and G%(R1*k)!=0]
        require(sorted(r[2] for r in records)==fibre,
                'independent complete inverse fibre')
    total['distinct_returned_states']=len(source_to_targets)
    total['distinct_target_fibres']=len(source_to_targets)
    require(dict(total)==data['counts'],'complete census agreement')
    signature.sort()
    return dict(bound=data['bound'],counts=dict(total),signature_sha256=hashlib.sha256(json.dumps(signature,separators=(',',':')).encode()).hexdigest())

def check_examples(path:Path)->dict:
    data=json.loads((path/'examples.json').read_text());tot=0
    expected={
        'automatic_composite':(1009,321,9,'M'),
        'mixed_square_factors':(1108801,279295,5,'M'),
        'partial_square_only':(51361,14845,5,'M'),
        'nonsquare_after_complement':(1009,286,11,'E'),
        'previous_failed_word':(1009,286,7436,'E'),
        'small_exterior':(37,16,2,'E'),
        'complement_boundary':(29,14,2,'E'),
        'sharp_failure':(48116881,12032220,8,'M'),
        'integral_multireturn_15':(41,14,1,'M'),
        'integral_multireturn_27':(173,50,4,'M'),
    }
    require(set(data)==set(expected)|{'endpoint'},'complete fixture key set')
    for name,row in data.items():
        if name=='endpoint':continue
        p,a,R,u,c=[row[k] for k in ('p','a','R','u','channel')]
        require((p,a,u,c)==expected[name],'fixed fixture identity')
        require(isprime(p),'displayed prime complete trial division')
        require(R==4*a-p and p<4*a<2*p and a*a%u==0,'displayed source')
        y,z=fraction_pair(p,a,u,c)
        require([[a,1],[y.numerator,y.denominator],[z.numerator,z.denominator]]==row['rational_denominators'],'printed source fractions')
        require((y+z).denominator==1 and y.denominator==row['denominator'],'displayed trace')
        outputs=[]
        for R1 in ds(R):
            if R1%4!=3:continue
            a1=(p+R1)//4
            if a1*a1%u:continue
            Y,Z=fraction_pair(p,a1,u,c)
            if Y.denominator==Z.denominator==1:outputs.append(dict(removal=R//R1,target=target(p,a1,u,c)))
        outputs.sort(key=lambda o:o['removal'])
        require(outputs==row['targets'],'complete displayed return')
        tot+=1
    p=48116881;a=12032220;u=8;R=11999
    comp=a*a//u
    require(4*budget(comp)>R,'complement obstruction retains budget')
    require(not any((4*w+p)%71==0 for w in ds(18,2)),'all cofactor71 words fail')
    for c,row in data['endpoint'].items():
        require(target(row['p'],row['a'],row['u'],c)==row,'independent endpoint')
    return dict(displayed_sources=tot,prime_trial_bound=isqrt(p))

def check_finite_models(path:Path)->dict:
    ab=json.loads((path/'abstract.json').read_text())
    require(isinstance(ab.get('bound'),int) and ab['bound']>=8,
            'unit-model bound')
    require([row[0] for row in ab['rows']]==list(range(1,ab['bound']+1)),
            'complete unique unit-model rows')
    for u,m,size in ab['rows']:
        require(m==4*budget(u),'unit-model modulus')
        sq={z*z%m for z in range(1,m) if gcd(z,m)==1}
        require(len(sq)==size and (len(sq)==1)==(36%u==0),'unit image classification')
    pr=json.loads((path/'progressions.json').read_text())
    require(isinstance(pr.get('bound'),int) and pr['bound']>=8,
            'progression bound')
    expected_u=[u for u in range(1,pr['bound']+1) if 36%u!=0]
    require([row['u'] for row in pr['rows']]==expected_u,
            'complete unique progression rows')
    for row in pr['rows']:
        u,m,b,delta,t,R,L,e,p0,M=[row[k] for k in ('u','m','unit','delta','t','R','L','endpoint_prime','residue','modulus')]
        require(36%u!=0 and m==4*budget(u) and L==lcm(840,m),
                'progression seed and moduli')
        require(b%4==1 and gcd(b,m)==1 and b*b%m!=1,
                'nontrivial unit square')
        require(isprime(delta) and isprime(t) and isprime(e) and t!=delta,
                'auxiliary primality and distinction')
        require(delta%4==3 and t%4==1 and e%4==3,
                'auxiliary residue classes')
        require(delta>max(u,u*u-3*u+1,7) and t>max(u,7),
                'strict auxiliary bounds')
        require(R==delta*t*t and gcd(L,R)==1 and gcd(e,L*R)==1,
                'pairwise coprime CRT moduli')
        require(p0%L==1 and (p0-(delta*t-4*u))%R==0 and (p0+1)%e==0,
                'CRT originals')
        require(gcd(p0,M)==1 and M==L*R*e,'reduced progression modulus')
        require((delta+b*b)%m==0 and (t*b-1)%m==0,
                'auxiliary square residues')
        require(row['strict_prime_lower_bound']==max(R,e,squarepart(u)*R),
                'exact strict prime lower bound')
        j=(delta+1)//4
        require(row['j']==j and j*j%u!=0,'cofactor source data')
        require(list(ds(j,2))==row['cofactor_divisors'],'entire cofactor exponent box')
        require(all((p0+4*w)%delta for w in ds(j,2)),'no cofactor hit')
        # Verify a numerical member of the progression, without pretending it prime.
        N=p0
        while N<=row['strict_prime_lower_bound']:N+=M
        require((N+R)%4==0 and N>max(R,e),'sampled source range')
        a=(N+R)//4
        require(N<4*a<2*N and a*a%u==0,'sampled original budget')
        require(gcd(R,N+4*u)==delta*t and (N+4*u)**2%R==0 and
                (N+4*u)%R!=0 and R//gcd(R,N+4*u)==t,
                'proper sampled source congruences')
        y,z=fraction_pair(N,a,u,'M')
        require((y+z).denominator==1 and y.denominator==z.denominator==t,
                'sampled literal rational trace')
        comp=a*a//u
        require(gcd(R,N+4*comp)==gcd(R,N+4*u)==delta*t,
                'complement preserves exact denominator')
        require((N+4*comp)**2%R==0 and (N+4*comp)%R!=0 and
                4*budget(comp)>R,
                'proper complemented trace and oversized budget')
        for R1 in ds(R):
            if R1%4!=3:continue
            a1=(N+R1)//4
            for w in (u,comp):
                require(a1*a1%w!=0 or (N+4*w)%R1!=0,'both source orientations blocked')
        c=(N+1)//e;je=(e+1)//4;ae=(N+e)//4;am=je*c
        require((N+1)%e==0 and (e+1)%4==0 and c%4==2,
                'endpoint integer coordinates')
        E=(ae,ae*c,N*ae*c);Mtuple=(am,N*am,N*je)
        require(N<4*ae<2*N and N<4*am<2*N,
                'endpoint first-half ranges')
        require(sum(Fraction(1,x) for x in E)==Fraction(4,N) and
                sum(Fraction(1,x) for x in Mtuple)==Fraction(4,N),
                'endpoint E and M identities')
    return dict(unit_models=len(ab['rows']),prime_progressions=len(pr['rows']))

def check_negative_controls(path:Path)->list:
    ex=json.loads((path/'examples.json').read_text())
    ab=json.loads((path/'abstract.json').read_text())
    statements={
        'Removing only a denominator always preserves the word':
            ex['mixed_square_factors']['denominator']%ex['mixed_square_factors']['budget_modulus']==1,
        'A minimal square factor always suffices':
            ex['mixed_square_factors']['minimum_square_factor']**2%20==1,
        'Removing every square always suffices':27**2%20==1,
        'Every valid deletion is a square':
            isqrt(45)**2==45,
        'Every E trace complement stays in the domain':
            ex['complement_boundary']['complement_is_trace'],
        'The previous failed divisor can be silently kept':
            bool(ex['previous_failed_word']['removals']),
        'All seeds are automatic':
            next(size for u,_,size in ab['rows'] if u==8)==1,
        'A nonempty rational trace ensures cofactor71 occupancy':
            any(w%71==8 for w in ds(18,2)),
        'The terminal source disproves ES':
            sum(Fraction(1,x) for x in ex['endpoint']['M']['denominators'])!=
            Fraction(4,ex['endpoint']['M']['p']),
        'Reducing the integer coefficient modulo two preserves its target count':
            len(ex['mixed_square_factors']['removals'])%2==
            len(ex['mixed_square_factors']['targets']),
    }
    summary=json.loads((path/'summary.json').read_text())
    require(list(statements)==summary['rejected_false_implications'],
            'complete negative-control roster')
    for name,value in statements.items():require(not value,'negative control: '+name)
    return list(statements)

def main():
    pa=argparse.ArgumentParser();pa.add_argument('--input',type=Path,default=Path('certificates'));pa.add_argument('--out',type=Path,default=Path('independent.json'))
    ar=pa.parse_args();start=time.monotonic()
    report=dict(success=True,scan=check_scan(ar.input),examples=check_examples(ar.input),models=check_finite_models(ar.input),
                negative_controls=check_negative_controls(ar.input),checks=C,
                universal_ES_proved=False,imports_predecessor_or_main=False)
    ar.out.parent.mkdir(parents=True,exist_ok=True)
    ar.out.write_bytes((json.dumps(report,sort_keys=True,indent=2)+'\n').encode('utf-8'))
    print(json.dumps(report,sort_keys=True,indent=2));print('elapsed_seconds',time.monotonic()-start)
if __name__=='__main__':main()
