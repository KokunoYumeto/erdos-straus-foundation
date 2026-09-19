#!/usr/bin/env python3
"""Turn 6: complete-shell collision bounds and original arithmetic certificates.

Standard library only. All comparisons are integer or Fraction comparisons.
Finite replays do not prove the universal ES conjecture or the analytic inequalities.
The latter have complete written proofs in core.tex. Checks remain active under -O.
"""
from __future__ import annotations
import argparse
from array import array
from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import product
from heapq import heapify, heappop, heappush
from math import gcd, isqrt, factorial
from pathlib import Path
import json
import sys
if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)  # trusted bounded exact-rational output

HARD = {1,121,169,289,361,529}
REPAIRS = [(87481,21878,2),(196561,49159,4),
           (944329,236098,13),(1915201,478836,12)]

class Checks:
    def __init__(self): self.n = 0; self.rejected = []
    def require(self, condition, message):
        self.n += 1
        if not condition: raise ArithmeticError(message)
    def reject(self, name, false_claim):
        self.require(not false_claim, 'False transformation survived: '+name)
        self.rejected.append(name)
C = Checks()

def emit(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, sort_keys=True, indent=2)+'\n')

def tables(n):
    sp = array('I', range(n+1))
    for q in range(2,isqrt(n)+1):
        if sp[q] == q:
            for j in range(q*q,n+1,q):
                if sp[j] == j: sp[j] = q
    phi = array('I',[0])*(n+1); phi[1] = 1
    tau = array('H',[0])*(n+1); tau[1] = 1
    exp = array('B',[0])*(n+1)
    for x in range(2,n+1):
        q=sp[x]; y=x//q
        if y%q == 0:
            exp[x]=exp[y]+1; phi[x]=q*phi[y]
            tau[x]=tau[y]//(exp[y]+1)*(exp[x]+1)
        else:
            exp[x]=1; phi[x]=(q-1)*phi[y]; tau[x]=2*tau[y]
    return sp,phi,tau

def factor(n, sp=None):
    if n < 1: raise ValueError('positive factor input required')
    out=[]; q=2
    while n>1:
        if sp is not None and n<len(sp): q=sp[n]
        elif q*q>n: q=n
        elif n%q:
            q=3 if q==2 else q+2; continue
        e=0
        while n%q==0: n//=q; e+=1
        out.append((int(q),e))
    return out

def divs(fa, multiple=1):
    ds=[1]
    for q,e in fa:
        ds=[d*q**j for d in ds for j in range(multiple*e+1)]
    return sorted(ds)

def phi_fact(n):
    for q,e in factor(n): n=n//q*(q-1)
    return n

def pair_data(p,a,fa=None):
    if fa is None: fa=factor(a)
    R=4*a-p; ds=divs(fa)
    words=ds+[p*x for x in ds]
    by=defaultdict(list)
    for x in words: by[x%R].append(x)
    hist={r:len(xs) for r,xs in by.items()}
    energy=sum(x*x for x in hist.values())
    target=sum(x*hist.get((-r)%R,0) for r,x in hist.items())
    return R,ds,words,by,hist,energy,target

def return_state(p,a,u,channel):
    R=4*a-p; d=gcd(a,u); h=d*d//u; r=u//d; s=a//d
    C.require(d*d%u==0 and h*r*s==a and h*r*r==u and gcd(r,s)==1,
              'normalization')
    if channel=='E':
        zeta=(p*r+s)//R
        C.require((p*r+s)%R==0,'E quotient')
        xyz=(a,h*s*zeta,p*h*r*zeta)
        C.require(a*a%(R*xyz[1]-p*a)==0 and a*a//(R*xyz[1]-p*a)==u,'E inverse')
    elif channel=='M':
        zeta=(r+s)//R
        C.require((r+s)%R==0,'M quotient')
        xyz=(a,p*h*s*zeta,p*h*r*zeta)
        C.require(p*a*a%(R*xyz[1]-p*a)==0 and p*a*a//(R*xyz[1]-p*a)==u,'M inverse')
    else: raise ValueError(channel)
    x,y,z=xyz
    C.require(min(x,y,z)>0 and 4*x*y*z==p*(x*y+x*z+y*z),'original ES identity')
    return {'p':p,'a':a,'R':R,'u':u,'channel':channel,'h':h,'r':r,'s':s,
            'quotient':zeta,'ordered_denominators':xyz}

def pair_return(p,a,b,c):
    R=4*a-p; n=p*a
    C.require(n%b==0 and n%c==0 and (b+c)%R==0,'pair availability')
    g=gcd(b,c); x=b//g; y=c//g
    if x%p and y%p:
        channel='M'; r=x; s=y
        bit=1 if g%p==0 else 0; d=g//p**bit
        mark={'common_p_bit':bit,'common_divisor':d}
    else:
        channel='E'; d=g
        if x%p==0: r=x//p; s=y; side=0
        else: r=y//p; s=x; side=1
        mark={'p_side':side,'common_divisor':d}
    h=a//(r*s)
    C.require(a%(r*s)==0 and h%d==0,'primitive pair fibre')
    state=return_state(p,a,h*r*r,channel)
    C.require((state['r'],state['s'],state['h'])==(r,s,h),'pair primitive inverse')
    return {'input_pair':[b,c],'pair_mark':mark,'state':state}

def first_pair(p,a,by):
    R=4*a-p
    for r in sorted(by):
        ys=by.get((-r)%R)
        if ys: return pair_return(p,a,by[r][0],ys[0])
    return None

def subgroup(R,g):
    if gcd(R,g)!=1: raise ValueError('unit generator required')
    K={1}; x=g%R
    while x not in K: K.add(x); x=x*g%R
    return sorted(K|{(-x)%R for x in K})

def cosets(R,K):
    remain={r for r in range(1,R) if gcd(r,R)==1}; result=[]
    K=set(K)
    C.require(1 in K and R-1 in K and all(x*y%R in K for x in K for y in K),'marked subgroup')
    while remain:
        rep=min(remain); cl=sorted(rep*x%R for x in K)
        C.require(len(cl)==len(K) and set(cl)<=remain,'coset partition')
        result.append((rep,cl)); remain.difference_update(cl)
    return result

def balanced(m,s):
    q,r=divmod(m,s)
    return s*q*q+r*(2*q+1)

def bound_record(p,a,g,sp=None,detail=True):
    if sp is not None: C.require(sp[p]==p,'prime example')
    fa=factor(a,sp); R,ds,words,by,hist,D,T=pair_data(p,a,fa)
    K=subgroup(R,g); classes=cosets(R,K); s=len(K)//2
    coarse=[]; pair_totals=[]
    for rep,cl in classes:
        mass=sum(hist.get(x,0) for x in cl)
        coarse.append((rep,mass))
        seen=set(); zz=[]
        for x in cl:
            if x not in seen:
                y=(-x)%R; seen.update((x,y))
                zz.append(hist.get(x,0)+hist.get(y,0))
        pair_totals.append((rep,zz))
    real=Fraction(2*sum(m*m for rep,m in coarse),len(K))-D
    integer=sum(balanced(m,s) for rep,m in coarse)-D
    rounded=4*max(0,(integer+3)//4)
    C.require(real<=integer<=T and rounded<=T,'coset lower bound')
    C.require(T%4==0,'fourfold original orbit')
    C.require(sum(m for _,m in coarse)==len(words),'coarse total')
    equality=all(max(z)-min(z)<=1 for _,z in pair_totals)
    C.require((integer==T)==equality,'integer equality locus')
    rec={'p':p,'a':a,'R':R,'factorization':fa,'generator':g,'subgroup':K,
         'index':len(classes),'mass':len(words),'energy':D,'target_count':T,
         'coset_counts':coarse,'antipodal_pair_totals':pair_totals,
         'real_lower':[real.numerator,real.denominator],
         'integer_lower':integer,'orbit_rounded_lower':rounded,
         'equality':equality,'witness':first_pair(p,a,by)}
    if detail:
        rec['original_words']=[{'d':x,'p_bit':int(x%p==0),'a_divisor':x//p if x%p==0 else x,
                                'residue':x%R} for x in words]
        rec['fine_counts']=sorted(hist.items())
        pairs=[(b,c) for r,xs in by.items() for b in xs for c in by.get((-r)%R,[])]
        rec['original_target_pairs']=[pair_return(p,a,b,c) for b,c in sorted(pairs)]
        orbits=[]; unseen=set(pairs); n=p*a
        while unseen:
            b,c=min(unseen); O={(b,c),(c,b),(n//b,n//c),(n//c,n//b)}
            C.require(len(O)==4 and O<=unseen,'free Klein orbit')
            unseen.difference_update(O); orbits.append(sorted(O))
        rec['fourfold_orbits']=orbits
    return rec

def convex_cost(m, regular, fixed):
    """Minimum 2 sum(z_i^2)+4 sum(w_i^2), sum(z_i)+sum(w_i)=m.
    Every coordinate and the selected marginal-cost word are retained.
    """
    heap=[(2,2,i,0) for i in range(regular)] + [
          (4,4,regular+i,0) for i in range(fixed)]
    if not heap:
        if m: raise ArithmeticError('nonzero mass on empty orbit space')
        return 0,[]
    heapify(heap); total=0; allocation=[0]*(regular+fixed)
    for unused in range(m):
        marginal,weight,i,x=heappop(heap)
        total+=marginal;allocation[i]=x+1
        heappush(heap,(weight*(2*x+3),weight,i,x+1))
    return total,allocation

def complement_bound(p,a,g,sp=None):
    R,ds,words,by,hist,D,T=pair_data(p,a,factor(a,sp))
    K=subgroup(R,g); classes=cosets(R,K)
    lookup={x:rep for rep,cl in classes for x in cl}; P=p*a%R
    C.require(all(hist.get(x,0)==hist.get(P*pow(x,-1,R)%R,0)
                  for x in lookup),'original divisor complementation')
    seen=set(); energy_floor=0; records=[]
    for rep,cl in classes:
        if rep in seen:continue
        other=lookup[P*pow(rep,-1,R)%R]
        m=sum(hist.get(x,0) for x in cl)
        if other!=rep:
            othermass=sum(hist.get(x,0) for x,rr in lookup.items() if rr==other)
            C.require(m==othermass,'paired coset masses')
            seen.update([rep,other]);v=2*balanced(m,len(K)//2)
            records.append({'cosets':[rep,other],'mass_each':m,'energy_floor':v})
        else:
            seen.add(rep)
            roots=[x for x in cl if x*x%R==P]
            C.require(all(hist.get(x,0)%2==0 for x in roots),'fixed-residue even count')
            fixed=len(roots)//2; regular=(len(K)//2-fixed)//2
            C.require(m%2==0 and 2*regular+fixed==len(K)//2,'self-complementary orbit sizes')
            v,allocation=convex_cost(m//2,regular,fixed)
            records.append({'cosets':[rep],'mass':m,'fixed_pair_orbits':fixed,
                            'regular_pair_orbits':regular,'minimum_allocation':allocation,
                            'energy_floor':v})
        energy_floor+=v
    old=sum(balanced(sum(hist.get(x,0) for x in cl),len(K)//2) for _,cl in classes)-D
    lower=energy_floor-D
    C.require(old<=lower<=T,'complement-aware integer bound')
    return {'p':p,'a':a,'R':R,'K':K,'complement_residue':P,
            'orbits':records,'unconstrained_integer_lower':old,
            'complement_integer_lower':lower,'T':T}

def atan_interval(x, terms):
    """Exact alternating-series interval for arctan(x), 0<x<1."""
    partial=sum(((-1)**j*x**(2*j+1)/ (2*j+1) for j in range(terms)),Fraction())
    nxt=x**(2*terms+1)/(2*terms+1)
    return (partial,partial+nxt) if terms%2==0 else (partial-nxt,partial)

def cos_interval_pi_fraction(num,den,pi_interval,terms=18):
    """Outward rational enclosure of cos(2*pi*num/den), using reflection."""
    k=num%den;k=min(k,den-k)
    lo,hi=pi_interval;x=2*lo*k/den;delta=2*(hi-lo)*k/den
    S=sum(((-1)**j*x**(2*j)/factorial(2*j) for j in range(terms)),Fraction())
    err=x**(2*terms)/factorial(2*terms)
    return S-err-delta,S+err+delta

def spectral_certificate():
    p,a,R=944329,236094,47
    _,ds,words,by,hist,D,T=pair_data(p,a)
    gen=5; logs={pow(gen,j,R):j for j in range(R-1)}
    C.require(len(logs)==46 and pow(gen,23,R)==46,'primitive order46 generator')
    coeff=[0]*23
    for w in words:coeff[logs[w%R]%23]+=1
    Q=[sum(coeff[x]*coeff[(x-j)%23] for x in range(23)) for j in range(23)]
    C.require(Q[0]==D+T and sum(Q)==len(words)**2,'original even Fourier polynomial')
    # Machin identity proved by the rational tangent formula; the angle lies in (0,1).
    x=Fraction(1,5);y=Fraction(1,239)
    t2=2*x/(1-x*x);t4=2*t2/(1-t2*t2)
    C.require((t4-y)/(1+t4*y)==1,'rational Machin tangent identity')
    C.require(4*(x-x**3/3)-y>0 and 4*x<1,'Machin angle range')
    l5,u5=atan_interval(x,18);l239,u239=atan_interval(y,18)
    pi_interval=(16*l5-4*u239,16*u5-4*l239)
    C.require(Fraction(3)<pi_interval[0]<pi_interval[1]<Fraction(22,7),'pi enclosure')
    energies=[]
    for j,integer_floor in [(1,1009),(2,24)]:
        lo=hi=Fraction(Q[0]);terms=[]
        for k in range(1,12):
            cl,cu=cos_interval_pi_fraction(j*k,23,pi_interval)
            lo+=2*Q[k]*cl;hi+=2*Q[k]*cu
            terms.append({'exponent':j*k%23,'coefficient':2*Q[k]})
        C.require(integer_floor<lo<hi<integer_floor+1,'certified cyclotomic energy interval')
        scale=10**9
        small_lo=Fraction((lo*scale).numerator//(lo*scale).denominator,scale)
        small_hi=Fraction(-((-hi*scale).numerator//(-hi*scale).denominator),scale)
        C.require(small_lo<=lo and hi<=small_hi,'outward displayed interval')
        energies.append({'mode':j,'lower':[small_lo.numerator,small_lo.denominator],
                         'upper':[small_hi.numerator,small_hi.denominator],
                         'proved_integer_interval':[integer_floor,integer_floor+1],
                         'cosine_terms':terms})
    C.require(Fraction(2*1009-732,23)>52,'three-mode threshold')
    C.require(Fraction(2*(1009+24)-732,23)==58,'five-mode threshold')
    C.require(T==60,'full target count compared separately')
    selected={0,1,22,2,21}
    C.reject('a useful selected spectrum must be a character subgroup',
             all((i+j)%23 in selected for i in selected for j in selected))
    w=first_pair(p,a,by)
    pairs=[pair_return(p,a,b,c) for b in words for c in words if (b+c)%R==0]
    unique={(r['state']['channel'],r['state']['u']):r['state'] for r in pairs}
    word_marks=[{'d':d,'p_bit':int(d%p==0),'a_divisor':d//p if d%p==0 else d,
                 'residue':d%R,'full_log_mod46':logs[d%R],
                 'even_log_mod23':logs[d%R]%23} for d in words]
    return {'p':p,'a':a,'R':R,'prime_factorization_a':factor(a),'generator':gen,
            'character_definition':'chi(5)=zeta_23, hence chi(-1)=1; retain principal and conjugate pairs',
            'mass':len(words),'collision_energy':D,'target_count':T,'original_words':word_marks,
            'original_target_pairs':pairs,'distinct_labelled_states':list(unique.values()),
            'selected_even_modes':[0,1,22,2,21],'coefficient_vector':coeff,
            'norm_polynomial_cyclic_coefficients':Q,
            'pi_identity':'pi=16 arctan(1/5)-4 arctan(1/239)',
            'atan_terms':18,'cos_terms':18,
            'pi_interval':[[pi_interval[0].numerator,pi_interval[0].denominator],
                           [pi_interval[1].numerator,pi_interval[1].denominator]],
            'energies':energies,'three_even_modes_lower_strict':[1286,23],
            'three_even_modes_rounded_target_lower':56,'five_even_modes_lower_strict':[58,1],
            'five_even_modes_rounded_target_lower':60,'all_even_modes':23,
            'witness':w,
            'scope':'A proper selected spectrum, not the complete terminal quotient. Rational interval certificates use no floating point. Universal selection not asserted.'}

def divisor_power_constants():
    """Finite exact constants for the written all-exponent tau(n) bound.
    The proof, not this finite check, supplies monotonicity past e=2m-1.
    """
    records=[]
    for m in range(3,9):
        primes=[q for q in range(2,2**m)
                if all(q%d for d in range(2,isqrt(q)+1))]
        product=Fraction(1);local=[]
        for q in primes:
            vals=[Fraction((e+1)**m,q**e) for e in range(2*m)]
            e=max(range(2*m),key=vals.__getitem__);value=vals[e]
            C.require(all(Fraction((j+1)**m,q**j)<=value for j in range(4*m)),
                      'finite divisor-power maximum')
            C.require(Fraction(2*m+1,2*m)**m<2,
                      'universal post-maximum ratio anchor')
            local.append({'q':q,'maximizing_exponent':e,
                          'maximum_power':[value.numerator,value.denominator]})
            product*=value
        lo,hi=0,1
        while hi**m*product.denominator<product.numerator:hi*=2
        while hi-lo>1:
            mid=(lo+hi)//2
            if mid**m*product.denominator>=product.numerator:hi=mid
            else:lo=mid
        C.require(hi**m*product.denominator>=product.numerator and
                  (hi-1)**m*product.denominator<product.numerator,
                  'minimal integer divisor-power constant')
        records.append({'m':m,'C_m':hi,'K_m':[product.numerator,product.denominator],
                        'local_maxima':local})
    C.require(records[1]['C_m']==9 and 12*9**2==972 and 972**2==944784,
              'square-root resolution specialization')
    C.require(Fraction(7,16)-Fraction(91,300)>Fraction(1,8),
              'general resolution negative margin')
    return records

def constants_certificate():
    # Rational remainder bounds for log 2 and e; analytic general inequalities
    # are proved in the TeX, not inferred from these finite inequalities.
    x=Fraction(1,3); terms=12
    lo=2*sum((x**(2*j+1)/ (2*j+1) for j in range(terms)),Fraction())
    hi=lo+2*x**(2*terms+1)/((2*terms+1)*(1-x*x))
    elo=sum((Fraction(1,factorial(i)) for i in range(7)),Fraction())
    ehi=elo+Fraction(1,factorial(7))*Fraction(8,7)
    C.require(lo>Fraction(2,3) and hi<Fraction(3,4),'log 2 interval')
    C.require(ehi<Fraction(14,5),'e upper interval')
    maxes={2:3,3:2,5:1,7:1}; upper={2:Fraction(2),3:Fraction(3,2),5:Fraction(6,5),7:Fraction(11,10)}
    for q,e in maxes.items():
        C.require(Fraction(e+2,e+1)**3<q,'decreasing divisor ratio after maximum')
        C.require(Fraction(e+1,e)**3>q,'increasing divisor ratio before maximum')
        C.require(Fraction(e+1)**3<=upper[q]**3*q**e,'small-prime divisor bound')
    C.require(upper[2]*upper[3]*upper[5]*upper[7]<4,'divisor constant')
    C.require(Fraction(3,2)**3<4,'half-interval power saving')
    C.require(2**20>100**3,'cubic threshold')
    C.require(Fraction(448,15)*Fraction(13,10)/100==Fraction(728,1875),'principal constant')
    C.require(Fraction(7,16)-Fraction(728,1875)>Fraction(1,24),'negative margin')
    C.require(Fraction(40,3)/16-Fraction(3,4)-Fraction(1,512)>0,'collision margin')
    return {'divisor_power_constants':divisor_power_constants(),
            'general_resolution_theorem':'For m>=3, C_m from the finite prime/exponent formula, p>=2^20 and p^(1-2/m)>=12*J*C_m^2, every raw sum retaining at most J even modes per shell is <=-p*log(p)/8. Equivalent integer condition p^(m-2)>=(12*J*C_m^2)^m.',
            'p_threshold':2**20,'full_sum_upper_coefficient':[-1,24],
            'log2_interval':[[lo.numerator,lo.denominator],[hi.numerator,hi.denominator]],
            'e_upper':[ehi.numerator,ehi.denominator],
            'small_prime_maximum_exponents':maxes,
            'adaptive_quotient_corollary':'For all integer J>=1 and p>=2^20*J^3, retain any per-shell set of at most J even characters (conjugate-closed for real observations). Their real projection lower bounds sum to <=-(1/24)*p*log(p); subgroup observations are included.',
            'claim':'For prime p=1 mod 4 and p>=2^20, sum_a L_a <= -(1/24)*p*log(p).',
            'scope':'Finite rational checks support constants; core.tex proves the infinite inequalities.'}

def abstract_checks():
    models=0
    for R in (3,5,7,9,15):
        units=[x for x in range(1,R) if gcd(x,R)==1]
        Ks={tuple(subgroup(R,g)) for g in units}
        partitions=[(K,cosets(R,K)) for K in sorted(Ks)]
        for vals in product(range(3),repeat=len(units)):
            hist=dict(zip(units,vals)); D=sum(v*v for v in vals)
            T=sum(v*hist[(-x)%R] for x,v in hist.items())
            for K,cls in partitions:
                masses=[sum(hist[x] for x in cl) for _,cl in cls]
                real=Fraction(2*sum(z*z for z in masses),len(K))-D
                integer=sum(balanced(z,len(K)//2) for z in masses)-D
                C.require(real<=integer<=T,'abstract integer/coset inequality')
            models+=1
    return {'moduli':[3,5,7,9,15],'integer_entries':[0,1,2],'coefficient_models':models,
            'scope':'All generated <-1,g> subgroups and every displayed nonnegative coefficient vector.'}

def full_scan(bound,sp,phi,tau):
    rows=[]; totals=Counter(); summaries=[]
    for p in range(5,bound+1,4):
        if sp[p]!=p: continue
        LP=Fraction(); H=0; TT=0
        for a in range(p//4+1,(p-1)//2+1):
            fa=factor(a,sp); R,ds,words,by,hist,D,T=pair_data(p,a,fa)
            C.require(len(ds)==tau[a] and len(words)==2*tau[a],'divisor multiplicity')
            E=[]; M=[]
            for u in divs(fa,2):
                totals['original_divisor_vectors']+=1
                if (4*u+1)%R==0: E.append(u)
                if (4*u+p)%R==0: M.append(u)
            hit_map={}
            for tag,us in [('E',E),('M',M)]:
                for u in us:
                    st=return_state(p,a,u,tag)
                    hit_map[(tag,st['r'],st['s'])]=st
            fibre=Counter(); pairs=set()
            for r,xs in by.items():
                for b in xs:
                    for c in by.get((-r)%R,[]):
                        pairs.add((b,c)); ans=pair_return(p,a,b,c); st=ans['state']
                        key=(st['channel'],st['r'],st['s']); fibre[key]+=1
                        C.require(key in hit_map and st['u']==hit_map[key]['u'],'pair-to-state coverage')
            C.require(len(pairs)==T and set(fibre)==set(hit_map),'complete pair/source equivalence')
            for key,number in fibre.items():
                st=hit_map[key]; th=len(divs(factor(st['h'],sp)))
                C.require(number==2*th,'original 2 tau(h) fibre')
            unseen=set(pairs); n=p*a
            while unseen:
                b,c=min(unseen); O={(b,c),(c,b),(n//b,n//c),(n//c,n//b)}
                C.require(len(O)==4 and O<=unseen,'full scan free orbit')
                unseen.difference_update(O)
            num=8*len(ds)**2-int(phi[R])*D
            C.require(Fraction(num,int(phi[R]))<=T and T%4==0,'original principal bound')
            C.require(D>=2*len(ds),'collision diagonal bound')
            rows.append([p,a,R,len(ds),D,T,len(E),len(M),num,int(phi[R])])
            LP+=Fraction(num,int(phi[R])); H+=len(E)+len(M); TT+=T
            totals['shells']+=1;totals['E_states']+=len(E);totals['M_states']+=len(M)
            totals['target_pairs']+=T;totals['occupied_shells']+=bool(T)
        C.require(H>0,'finite prime has a witness (not a universal proof)')
        summaries.append([p,H,TT,LP.numerator,LP.denominator])
        totals['primes']+=1
    return {'bound':bound,'row_fields':['p','a','R','tau(a)','D','T','E','M','L_numerator','phi(R)'],
            'rows':rows,'totals':dict(totals),'prime_summary_fields':['p','H','sum_T','sum_L_numerator','sum_L_denominator'],
            'prime_summaries':summaries}

def principal_scan(bound,sp,phi,tau):
    top=(bound-1)//2; max_tau=max(tau[1:top+1]); cap=4*max_tau
    candidates=[R for R in range(3,bound,4) if phi[R]<cap]
    misses=[]; successes=[]; hard=[]
    for p in range(1009,bound+1,4):
        if p%840 not in HARD or sp[p]!=p:continue
        hard.append(p); success=None
        for R in candidates:
            if R>=p:break
            a=(p+R)//4
            if phi[R]>=4*tau[a]:continue
            fa=factor(a,sp); _,ds,words,by,hist,D,T=pair_data(p,a,fa)
            num=8*len(ds)**2-int(phi[R])*D
            if num>0:
                w=first_pair(p,a,by)
                C.require(w is not None and num<=phi[R]*T,'principal certificate has original inverse')
                success={'p':p,'a':a,'R':R,'tau':len(ds),'D':D,'phi':int(phi[R]),
                         'L_numerator':num,'witness':w}
                break
        if success is None:misses.append(p)
        else: successes.append(success)
    if bound==2000000:
        C.require(len(hard)==4519 and misses==[87481,196561,944329,1915201],'full hard bounded principal census')
        C.require(max_tau==240 and len(candidates)==311 and max(candidates)==1995,'finite complete candidate cutoff')
    return {'bound':bound,'hard_residues':sorted(HARD),'hard_prime_count':len(hard),
            'max_tau_range':[1,top],'max_tau':int(max_tau),'max_tau_attainers':[i for i in range(1,top+1) if tau[i]==max_tau], 'necessary_phi_cap':int(cap),
            'candidate_residuals':candidates,'principal_misses':misses,'principal_successes':successes,
            'completeness':'D>=2*tau(a), so L>0 requires phi(R)<4*tau(a); all other residuals are excluded by the displayed sieve bound.'}

def failure_scan(p,sp,phi):
    rows=[]; worst=None; occupied=[]; totalL=Fraction(); max_integer=None
    for a in range(p//4+1,(p-1)//2+1):
        R,ds,words,by,hist,D,T=pair_data(p,a,factor(a,sp))
        num=8*len(ds)**2-int(phi[R])*D
        C.require(num<=0,'full-shell principal test claimed to fail')
        value=Fraction(num,int(phi[R])); totalL+=value
        if worst is None or value>worst[0]:worst=(value,a,R)
        lint=balanced(2*len(ds),int(phi[R])//2)-D
        C.require(lint<=0,'full-shell integer principal test claimed to fail')
        max_integer=lint if max_integer is None else max(max_integer,lint)
        rows.append([a,R,len(ds),D,num,int(phi[R]),lint])
        if T: occupied.append([a,R,T])
    raw=json.dumps(rows,separators=(',',':')).encode()
    return {'p':p,'complete_a_range':[p//4+1,(p-1)//2],'shells':len(rows),
            'all_rows_sha256':sha256(raw).hexdigest(),'rows':rows,
            'max_L':[worst[0].numerator,worst[0].denominator],
            'max_L_shell':[worst[1],worst[2]],'max_global_integer_lower':max_integer,
            'sum_L':[totalL.numerator,totalL.denominator],
            'occupied_shells':occupied}

def examples(sp):
    recs=[bound_record(p,a,g,sp) for p,a,g in REPAIRS]
    r=next(x for x in recs if x['p']==944329)
    C.require(r['integer_lower']==8 and r['target_count']==8,'sharp even-coefficient example')
    C.reject('a nonzero coarse source alone forces the target',pair_data(3361,847)[-1]>0)
    C.reject('a positive coarse coefficient equals its parity reduction',
             all(m==m%2 for _,m in r['coset_counts']))
    # More useful explicit negative controls: retain their calculated data.
    empty=pair_data(3361,847); m=len(empty[2]); ph=phi_fact(empty[0]); pp=Fraction(m*m,ph)
    C.require(pp>0 and empty[-1]==0,'positive principal term with exact zero target')
    C.reject('discarding the residual collision term is harmless',pp<=empty[-1])
    noK=bound_record(944329,236094,2,sp,detail=False)
    C.require(noK['R']==47 and noK['target_count']==60,'no intermediate subgroup example')
    C.require(len(noK['subgroup'])==46,'order-46 coefficient group')
    C.reject('a positive target always has positive principal lower bound',noK['integer_lower']>0)
    C.reject('coset sums are an isometry for the fine counting norm',
             sum(m*m for _,m in r['coset_counts'])==r['energy'])
    C.reject('an arbitrary coefficient array has the original fourfold orbit divisibility',
             (1*1+1*1)%4==0)
    C.reject('coset counts determine fine energy', (2*2)==(1*1+1*1))
    C.reject('the real and balanced-integer lower bounds always agree',
             r['real_lower']==[r['integer_lower'],1])
    return {'repairs':recs,'empty_shell':{'p':3361,'a':847,'R':27,'factorization':factor(847),
              'fine_counts':sorted(empty[4].items()),'mass':m,'D':empty[5],'T':empty[6],
              'principal':[pp.numerator,pp.denominator]},
            'no_nonterminal_subgroup':noK,
            'scope':'These are original arithmetic examples, not a universal proof that some quotient bound is positive.'}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--bound',type=int,default=3000)
    ap.add_argument('--hard-bound',type=int,default=2000000)
    ap.add_argument('--out',type=Path,default=Path('certificates'))
    ap.add_argument('--skip-abstract',action='store_true')
    args=ap.parse_args()
    if args.bound<5 or args.hard_bound<1009:raise ValueError('bounds too small')
    n=max(args.bound,args.hard_bound,1915201)
    sp,phi,tau=tables(n)
    constants=constants_certificate();emit(args.out/'constants.json',constants)
    abstraction=abstract_checks() if not args.skip_abstract else {'omitted':True}
    emit(args.out/'abstract.json',abstraction)
    fs=full_scan(args.bound,sp,phi,tau);emit(args.out/'full_shells.json',fs)
    print('full scan',fs['totals'],flush=True)
    ps=principal_scan(args.hard_bound,sp,phi,tau);emit(args.out/'principal_census.json',ps)
    print('principal scan',ps['hard_prime_count'],ps['principal_misses'],flush=True)
    ex=examples(sp);emit(args.out/'examples.json',ex)
    cc=[complement_bound(p,a,g,sp) for p,a,g in REPAIRS]
    cc.append(complement_bound(196561,49147,2,sp))
    emit(args.out/'complement.json',cc)
    emit(args.out/'spectral.json',spectral_certificate())
    fc=failure_scan(87481,sp,phi);emit(args.out/'failure_87481.json',fc)
    checks={'success':True,'explicit_checks':C.n,'negative_controls':C.rejected,
            'full_shell_bound':args.bound,'hard_bound':args.hard_bound,
            'no_universal_occupancy_claim':True}
    emit(args.out/'summary.json',checks);print(json.dumps(checks),flush=True)

if __name__=='__main__':main()
