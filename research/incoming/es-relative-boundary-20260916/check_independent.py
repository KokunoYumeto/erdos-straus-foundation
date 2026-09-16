#!/usr/bin/env python3
"""Separate residue/knapsack replay; imports neither new nor antecedent verifier.
Checks the complete stated finite universe, canonical-line decisions, cofactors,
and selected relative packet words. Not independent mathematical review.
"""
from __future__ import annotations
import argparse,json
from collections import Counter
from functools import lru_cache
from fractions import Fraction
from hashlib import sha256
from itertools import product,combinations_with_replacement
from math import gcd,isqrt,prod
from pathlib import Path
C=Counter();HARD={1,121,169,289,361,529}

def ck(t,s):
    C[s]+=1
    if not t:raise ArithmeticError(s)

def sieve(n):
    a=bytearray(b'\1')*(n+1);a[:2]=b'\0\0'
    for j in range(2,isqrt(n)+1):
        if a[j]:a[j*j::j]=b'\0'*len(a[j*j::j])
    return a

def prime(n):return n>1 and all(n%d for d in range(2,isqrt(n)+1))

def order(g,m):
    g%=m;t=g;i=1
    while t!=1:t=t*g%m;i+=1
    return i

def ins(q,b):return q%8 in ((1,3) if b==3 else (1,5))

@lru_cache(None)
def table(k,b):return {pow(b,i,1<<k):i for i in range(1<<(k-2))}

@lru_cache(None)
def knapsack(o,items):
    mask=(1<<o)-1;bits=1
    for w,E in items:
        if w==0:continue
        # Binary blocks perform bounded subset-sum, rather than the prefix lemma.
        E=min(E,(o-1)//w);j=1
        while E:
            c=min(j,E);bits=(bits|(bits<<(w*c)))&mask;E-=c;j*=2
    return bool(bits>>(o-1)&1)

def patterns(ids,sign):
    if not ids:yield [];return
    i,*rest=ids
    for p in patterns(rest,sign):yield [(i,)]+p
    for j in rest:
        if sign[j]==sign[i]:
            for p in patterns([h for h in rest if h!=j],sign):yield [(i,j)]+p

def options(bl,fs,sign,m):
    if len(bl)==1:
        i=bl[0];q,E=fs[i]
        if not sign[i]:yield (1,q%m,E)
        else:
            for r in (0,1):yield (pow(q,r,m),pow(q,2,m),(E-r)//2)
        return
    i,j=bl;q,E=fs[i];r,F=fs[j];v=min(E,F)
    for mode in ('parallel','exchange'):
        for parity in ((0,1) if sign[i] else (0,)):
            if mode=='parallel':
                aa,bb=(0,0) if not parity else ((1,0) if E>F else (0,1))
                cap=min(E-aa,F-bb);g=q*r%m
            else:
                total=v
                if sign[i] and total%2!=parity:total=v+1 if E!=F else v-1
                aa=max(0,total-F);bb=total-aa;cap=min(E,total)-aa;g=q*pow(r,-1,m)%m
            yield(pow(q,aa,m)*pow(r,bb,m)%m,g,cap)

def decisions(p,k,fs):
    m=1<<k;o=1<<(k-2);full=False;relative=False;first_order=None
    for b in (3,-3):
        sign=[not ins(q,b) for q,e in fs]
        if not any(sign):continue
        for pat in patterns(list(range(len(fs))),sign):
            for blocks in product(*(tuple(options(bl,fs,sign,m)) for bl in pat)):
                const=prod(z[0] for z in blocks)%m
                if ins(const,b):continue
                vals=[x[1] for x in blocks]+[pow(p,-1,m)]
                caps=[x[2] for x in blocks]+[1]
                it=tuple(sorted((o//order(g,m),E) for g,E in zip(vals,caps) if g!=1 and E))
                if knapsack(o,it):full=True;return True,True,None
                for v in range(1,k-2):
                    small=1<<(v+2);L=1<<(k-2-v)
                    strides=[order(g,small) for g in vals]
                    high=[pow(g,s,m) for g,s in zip(vals,strides)]
                    weights=[0 if g==1 else L//order(g,m) for g in high]
                    top=tuple(sorted((w,E//s) for w,E,s in zip(weights,caps,strides) if w and E//s))
                    if not knapsack(L,top):continue
                    for low in product(*(range(min(s,E+1)) for s,E in zip(strides,caps))):
                        if const*prod(pow(g,r,small) for g,r in zip(vals,low))%small != small-1:continue
                        it=tuple(sorted((w,(E-r)//s) for w,E,r,s in zip(weights,caps,low,strides) if w and (E-r)//s))
                        if knapsack(L,it):
                            relative=True
                            if first_order is None:first_order=L
    return full,full or relative,first_order

def divisors(fs):
    d=[1]
    for q,e in fs:d=[x*q**j for x in d for j in range(e+1)]
    return sorted(d)

def baseline_short(p,k,fs):
    targets={(1<<k)-1,(-p)%(1<<k)};m=1<<k
    for i,(q,e) in enumerate(fs):
        if q%m in targets:return True
        for j in range(i,len(fs)):
            r,f=fs[j]
            if (i!=j or e>=2) and q*r%m in targets:return True
    return False

def baseline_two(p,k,fs):
    d=dict(fs);m=1<<k;o=1<<(k-2);tab=table(k,3);s=tab[p%m];J=tab[11%m]
    pts=sorted({(J*j-sh)%o for j in range(min(d.get(11,0),o-1)+1) for sh in (0,s)})
    gap=max((pts[(i+1)%len(pts)]-x)%o or o for i,x in enumerate(pts))
    return any(q%8 in (5,7) for q,e in fs) and d.get(3,0)>=gap-1

def ret(p,k,Q):
    u=1<<(2*k-5);N=p+4*u;R=N//Q;a=(p+R)//4;d=gcd(a,u)
    ck(N%Q==0 and Q%(1<<k)==(1<<k)-1,'original_cofactor')
    h,r,s=d*d//u,u//d,a//d;lam=(r+s)//R
    den=[a,p*h*s*lam,p*h*r*lam]
    ck(a==h*r*s and u==h*r*r and gcd(r,s)==1 and lam*R==r+s,'normalization')
    ck(sum((Fraction(1,z) for z in den),Fraction())==Fraction(4,p),'independent_reciprocal_return')
    ck(Fraction(p*a*a,R*den[1]-p*a)==u,'independent_ordered_inverse')
    return den

def examples(path):
    ex=json.load(open(path/'examples.json'))
    for key in ('positive','negative','large_strict_family'):
        rec=ex[key];pc=rec['prime'];p=pc['p'];fs=pc['p_minus_one'];g=pc['base']
        ck(prod(q**e for q,e in fs)==p-1 and all(prime(q) for q,e in fs),'prime_factorization_for_order')
        ck(pow(g,p-1,p)==1 and all(gcd(pow(g,(p-1)//q,p)-1,p)==1 for q,e in fs),'prime_complete_order')
        if pc['trial_division_through'] is not None:ck(prime(p),'separate_full_trial_primality')
    rec=ex['positive'];p=rec['prime']['p'];fs=rec['factorization']
    full,rel,ordr=decisions(p,6,fs)
    ck(not full and rel,'strict_old_full_new_relative_comparison')
    qs=[q for q in divisors(fs) if q%64==63]
    ck(qs==[45951,175423],'positive_complete_cofactor_census')
    for st in rec['all_states']:ck(ret(p,6,st['Q'])==st['denominators'],'stored_integer_denominators')
    words=rec['packet']['all_words'];ck(len(set((w['word'],w['role']) for w in words))==len(words),'marked_packet_injection')
    for w in words:
        ck(prod(q**i for (q,e),i in zip(fs,w['exponents']))==w['word'],'stored_physical_exponents')
        ck(all(0<=i<=e for (q,e),i in zip(fs,w['exponents'])),'stored_exponent_bounds')
    ng=ex['negative']['one_block'];N=17**2*3*229*47
    ck(not any(q%64==63 for q in divisors([(3,1),(17,2),(47,1),(229,1)])),'complete_empty_branch')
    alt=ex['negative']['alternative'];den=alt['denominators']
    ck(sum((Fraction(1,z) for z in den),Fraction())==Fraction(4,9331009),'negative_prime_has_other_witness')
    for r in ex['family']:
        fs=[(3,1),(53,1),(607,1)]+([(17,r['e'])] if r['e'] else [])
        Q=[q for q in divisors(fs) if q%64==63]
        ck(Q==r['cofactors'] and len(Q)==2*max(0,1+(r['e']-2)//4),'family_independent_enumeration')
    big=ex['large_strict_family'];pbig=big['prime']['p'];fsbig=big['factorization']
    full,relative,_=decisions(pbig,7,fsbig)
    ck(not full and relative,'eight_residue_relative_success')
    QQ=[q for q in divisors(fsbig) if q%128==127]
    lengths=[]
    for q in QQ:
        left=q;length=0
        for b,e in fsbig:
            while left%b==0:left//=b;length+=1
        ck(left==1,'large_word_factorization');lengths.append(length)
    ck(sorted(lengths)==[5,6],'large_example_no_four_occurrence_word')
    for st in big['all_states']:ck(ret(pbig,7,st['Q'])==st['denominators'],'large_original_ordered_witness')
    # Two distinct original words become an even (supported-zero) quotient coefficient.
    high=[pow(17,j,64) for j in range(4)];t=[607,159]
    hist=Counter(a*b%64 for a in high for b in t)
    ck(hist=={15:2,31:2,47:2,63:2},'original_positive_even_relative_packet')
    return dict(positive_prime=p,cofactors=qs,supported_even_counts=sorted(hist.items()))

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--input',default='certificates');ap.add_argument('--out',default='independent.json');a=ap.parse_args();path=Path(a.input)
    source=json.load(open(path/'scan.json'));rows=source['rows'];limit=source['bound'];isp=sieve(limit)
    expected=[]
    for p in range(1009,limit+1):
        if not isp[p] or p%840 not in HARD:continue
        k=4
        while p>2*(1<<(2*k-5)):expected.append((p,k));k+=1
    ck([(r[0],r[1]) for r in rows]==expected,'entire_finite_domain_no_omitted_row')
    counts=Counter();oldp=set();newp=set();actualp=set();relativep=set();strict=[]
    short3p=set();short3union=set();short3b=short3ub=0
    for row in rows:
        p,k,N,fs,old_aff,short,two,newrel,count,suborder=row
        ck(N==p+(1<<(2*k-3)) and prod(q**e for q,e in fs)==N,'row_factorization_product')
        ck(all(e>0 and (bool(isp[q]) if q<=limit else prime(q)) for q,e in fs) and len({q for q,e in fs})==len(fs),'row_distinct_prime_factors')
        Qs=[q for q in divisors(fs) if q%(1<<k)==(1<<k)-1]
        full,relative,_=decisions(p,k,fs)
        sh=baseline_short(p,k,fs);tw=baseline_two(p,k,fs)
        ck((int(full),int(sh),int(tw),int(relative),len(Qs))==(old_aff,short,two,newrel,count),'all_finite_decisions_independent')
        old=full or sh or tw;new=old or relative
        ck(not new or bool(Qs),'positive_test_has_original_state')
        for Q in Qs:ret(p,k,Q)
        hit3=False
        for length in (1,2,3):
            for inds in combinations_with_replacement(range(len(fs)),length):
                cc=Counter(inds)
                if any(c>fs[i][1] for i,c in cc.items()):continue
                if prod(fs[i][0] for i in inds)%(1<<k) in {(1<<k)-1,(-p)%(1<<k)}:
                    hit3=True;break
            if hit3:break
        if hit3:short3b+=1;short3p.add(p)
        if hit3 or full or tw:short3ub+=1;short3union.add(p)
        if old:oldp.add(p)
        if new:newp.add(p)
        if Qs:actualp.add(p)
        if relative:relativep.add(p)
        if new and not old:strict.append((p,k))
        counts['branches']+=1;counts['states']+=len(Qs);counts['actual_branches']+=bool(Qs)
        counts['old_affine_branches']+=full;counts['relative_class_branches']+=relative
        counts['old_union_branches']+=old;counts['new_union_branches']+=new
    counts.update(old_union_primes=len(oldp),new_union_primes=len(newp),relative_class_primes=len(relativep),actual_primes=len(actualp),hard_primes=len({p for p,k in expected}))
    ck(dict(counts)==source['counts'],'all_counts_agree')
    digest=sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest();ck(digest==source['row_digest'],'canonical_row_digest')
    fair=json.load(open(path/'fair_baseline.json'))
    ck((short3b,len(short3p),short3ub,len(short3union))==(fair['short_three_branches'],fair['short_three_primes'],fair['union_with_previous_tests_branches'],fair['union_with_previous_tests_primes']),'fair_stronger_baseline')
    ex=examples(path)
    output=dict(checks=sum(C.values()),checks_by_kind=dict(C),counts=dict(counts),additional_primes=sorted(newp-oldp),strict_added_branches=strict,row_digest=digest,examples=ex,imports_main_or_antecedent=False)
    Path(a.out).write_text(json.dumps(output,sort_keys=True,indent=2)+'\n');print(json.dumps(dict(checks=sum(C.values()),counts=dict(counts),additional_primes=sorted(newp-oldp)),sort_keys=True))
if __name__=='__main__':main()
