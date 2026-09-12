#!/usr/bin/env python3
"""Split-box ES energy certificates. Python standard library only.

All arithmetic is exact. No import of prior project code. The default scan
covers first-half shells of primes p=1 mod 12, p<=1500. It is not a proof
of a universal ES assertion. Checks remain active with python -O.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
import heapq
from itertools import product
import json
from math import gcd, isqrt, prod
from pathlib import Path

CHECKS = Counter()

def require(condition, label):
    CHECKS[label] += 1
    if not condition:
        raise ArithmeticError(label)

@lru_cache(None)
def factor(n):
    if n < 1:
        raise ValueError('factorization requires a positive integer')
    out = []
    q = 2
    while q*q <= n:
        e = 0
        while n % q == 0:
            n //= q
            e += 1
        if e:
            out.append((q,e))
        q = 3 if q == 2 else q+2
    if n > 1:
        out.append((n,1))
    return tuple(out)

@lru_cache(None)
def prime(n):
    return n >= 2 and all(n % d for d in range(2,isqrt(n)+1))

def box(budget):
    return product(*(range(-e,e+1) for e in budget))

def residue(primes, beta, R):
    return prod(pow(q,b,R) for q,b in zip(primes,beta)) % R

def distribution(primes, budget, R):
    mu = Counter()
    reps = {}
    for beta in box(budget):
        g = residue(primes,beta,R)
        mu[g] += 1
        reps.setdefault(g,beta)
    return mu,reps

@lru_cache(None)
def cells(R):
    ps = tuple(q for q,e in factor(R))
    out = defaultdict(list)
    for g in range(1,R):
        if gcd(g,R) == 1:
            sign = tuple(1 if pow(g,(q-1)//2,q)==1 else -1 for q in ps)
            out[sign].append(g)
    return tuple((key,tuple(value)) for key,value in sorted(out.items()))

def energy_minimum(R, G, forbidden, mass):
    G = set(G)
    forbidden = set(forbidden)
    if 1 in G and 1 in forbidden:
        return None, {}
    base = int(1 in G)
    if mass < base or (mass-base) % 2:
        return None, {}
    heap,seen = [],set()
    nu = {g:0 for g in G}
    if base:
        nu[1] = 1
    for g in sorted(G-forbidden):
        if g in seen:
            continue
        gi = pow(g,-1,R)
        require(gi in G-forbidden,'inverse_closed_minimum_domain')
        seen.update((g,gi))
        initial,step = (8,8) if g==1 else ((4,8) if gi==g else (2,4))
        heap.append((initial,step,g,gi))
    heapq.heapify(heap)
    units = (mass-base)//2
    if units and not heap:
        return None, {}
    energy = base
    for _ in range(units):
        cost,step,g,gi = heapq.heappop(heap)
        energy += cost
        if g == gi:
            nu[g] += 2
        else:
            nu[g] += 1
            nu[gi] += 1
        heapq.heappush(heap,(cost+step,step,g,gi))
    require(sum(nu.values())==mass,'minimum_mass')
    require(sum(v*v for v in nu.values())==energy,'minimum_attainment')
    return energy,nu

def analyze(R, mu, forbidden):
    records = []
    for sign,G in cells(R):
        mass = sum(mu[g] for g in G)
        energy = sum(mu[g]**2 for g in G)
        lower,nu = energy_minimum(R,G,forbidden,mass)
        forced = lower is None or energy < lower
        require(not forced or any(mu[g] for g in set(G)&set(forbidden)),
                'forcing_sound')
        records.append(dict(sign=list(sign),mass=mass,energy=energy,
                            lower=lower,forced=forced,
                            minimizer=[[g,nu[g]] for g in sorted(nu) if nu[g]]))
    return records

def target_labels(p,R):
    return [('M',R-1),('E-direct',(-pow(p,-1,R))%R),('E-inverse',(-p)%R)]

def gate_targets(p,R):
    return {t for name,t in target_labels(p,R)}

def expanded_targets(primes, removed, R, targets):
    labels = defaultdict(list)
    for eta in box(removed):
        w = residue(primes,eta,R)
        for name,t in targets:
            labels[t*pow(w,-1,R)%R].append((name,t,eta))
    return labels

def marked_witness(p,a,primes,e,beta,kind):
    R = 4*a-p
    g = residue(primes,beta,R)
    require(kind in dict(target_labels(p,R)), 'typed_target_domain')
    require(g==dict(target_labels(p,R))[kind], 'typed_target_value')
    original = tuple(beta)
    channel = 'M' if kind=='M' else 'E'
    if kind=='E-inverse':
        beta = tuple(-b for b in beta)
    u = prod(q**(k+b) for q,k,b in zip(primes,e,beta))
    s0 = gcd(a,u)
    r,s,h = u//s0,a//s0,s0*s0//u
    gate = u+a if channel=='M' else 4*u+1
    require(gate%R==0,'original_integral_gate')
    if channel == 'M':
        quotient = (r+s)//R
        den = (a,p*h*s*quotient,p*h*r*quotient)
    else:
        quotient = (p*r+s)//R
        den = (a,h*s*quotient,p*h*r*quotient)
    require(all(x>0 for x in den),'positive_ordered_denominators')
    require(sum((Fraction(1,x) for x in den),Fraction())==Fraction(4,p),
            'unit_fraction_identity')
    require(h*r*s==a and h*r*r==u and gcd(r,s)==1,'normalization_inverse')
    Y = den[1]
    returned = Fraction((p if channel=='M' else 1)*a*a,R*Y-p*a)
    require(returned==u,'ordered_divisor_inverse')
    j = (R-3)//4
    eps = int(channel=='M')
    code = (s-1)*(p-1)**2//4+(p-1)*j+2*(r-1)+eps
    ss,rem = divmod(code,(p-1)**2//4)
    jj,rem = divmod(rem,p-1)
    rr,ee = divmod(rem,2)
    require((ss+1,jj,rr+1,ee)==(s,j,r,eps),'bounded_code_inverse')
    return dict(p=p,a=a,R=R,primes=list(primes),exponents=list(e),
                source_beta=list(original),beta=list(beta),u=u,channel=channel,
                h=h,r=r,s=s,quotient=quotient,denominators=list(den),
                inverse_applied=kind=='E-inverse',target_label=kind,code=code)

def split_record(p,a,removed,details=False):
    if not (prime(p) and p%4==1 and p<4*a and 2*a<p):
        raise ValueError('prime first-half shell required')
    R = 4*a-p
    fe = factor(a)
    primes = tuple(q for q,e in fe)
    e = tuple(k for q,k in fe)
    require(len(e)==len(removed) and all(0<=h<=k for h,k in zip(removed,e)),
            'split_budget_domain')
    retained = tuple(k-h for k,h in zip(e,removed))
    mu,reps = distribution(primes,retained,R)
    labels = expanded_targets(primes,removed,R,target_labels(p,R))
    records = analyze(R,mu,labels)
    forced = [rec for rec in records if rec['forced']]
    witness = None
    if forced:
        choices = []
        forced_signs = {tuple(rec['sign']) for rec in forced}
        allowed = {g for sign,G in cells(R) if sign in forced_signs for g in G}
        for g in sorted(set(mu)&set(labels)&allowed):
            xi = reps[g]
            for kind,target,eta in labels[g]:
                beta = tuple(x+y for x,y in zip(xi,eta))
                choices.append((beta,kind,xi,eta,target))
        require(bool(choices),'explicit_intersection')
        beta,kind,xi,eta,target = min(choices)
        witness = marked_witness(p,a,primes,e,beta,kind)
        witness['retained_beta'] = list(xi)
        witness['removed_beta'] = list(eta)
        witness['expanded_target_source'] = target
    out = dict(p=p,a=a,R=R,primes=list(primes),full=list(e),
               retained=list(retained),removed=list(removed),
               targets=sorted(gate_targets(p,R)),target_labels=target_labels(p,R),expanded=sorted(labels),
               cells=records,witness=witness)
    if details:
        out['distribution'] = [[g,mu[g]] for g in sorted(mu)]
        out['expanded_fibres'] = [[g,[[kind,t,list(b)] for kind,t,b in labels[g]]]
                                  for g in sorted(labels)]
    return out

def structural_tests():
    # Complete small overlapping split boxes, with a second proof of weights.
    for e in product(range(3),repeat=2):
        for f in product(*(range(k+1) for k in e)):
            h = tuple(k-j for k,j in zip(e,f))
            observed = Counter(tuple(x+y for x,y in zip(xi,eta))
                               for xi in box(f) for eta in box(h))
            for beta in box(e):
                bounds = [(max(-j,b-k),min(j,b+k)) for b,j,k in zip(beta,f,h)]
                weight = prod(hi-lo+1 for lo,hi in bounds)
                require(observed[beta]==weight and weight>=1,'complete_addition_fibre')
                for xi in product(*(range(lo,hi+1) for lo,hi in bounds)):
                    eta = tuple(b-x for b,x in zip(beta,xi))
                    require(all(-k<=y<=k for y,k in zip(eta,h)),
                            'addition_inverse_range')
    # Every split in every first-half shell for these four small primes.
    for p in (13,37,61,97):
        for a in range((p+3)//4,(p-1)//2+1):
            R=4*a-p; fe=factor(a)
            primes=tuple(q for q,e in fe); e=tuple(k for q,k in fe)
            full,_=distribution(primes,e,R)
            target=gate_targets(p,R)
            for f in product(*(range(k+1) for k in e)):
                h=tuple(k-j for k,j in zip(e,f))
                left,_=distribution(primes,f,R);right,_=distribution(primes,h,R)
                conv=Counter()
                for x,n in left.items():
                    for y,m in right.items():conv[x*y%R]+=n*m
                weighted=Counter()
                for beta in box(e):
                    weight=prod(min(j,b+k)-max(-j,b-k)+1 for b,j,k in zip(beta,f,h))
                    weighted[residue(primes,beta,R)]+=weight
                require(conv==weighted,'weighted_not_uniform_convolution')
                labels=expanded_targets(primes,h,R,target_labels(p,R))
                require(bool(set(left)&set(labels))==bool(set(full)&target),
                        'all_split_support_equivalence')
    # Exhaust every inverse-closed forbidden set on several small groups;
    # compare marginal allocation with dynamic programming over all slots.
    cases = 0
    for R in (3,5,7,9,11,15):
        G = [g for g in range(1,R) if gcd(g,R)==1]
        orbits,seen = [],set()
        for g in G:
            if g not in seen:
                orb = sorted({g,pow(g,-1,R)});orbits.append(orb);seen.update(orb)
        for bits in product((0,1),repeat=len(orbits)):
            F = {g for bit,orb in zip(bits,orbits) if bit for g in orb}
            for n in range(10):
                got,_ = energy_minimum(R,G,F,n)
                if 1 in F or n<1 or n%2==0:
                    expected = None
                else:
                    K = (n-1)//2; dp = {0:0}
                    for orb in orbits:
                        if orb[0] in F:
                            continue
                        cost = (lambda k:(1+2*k)**2) if orb==[1] else (
                               (lambda k:4*k*k) if len(orb)==1 else (lambda k:2*k*k))
                        nd = {}
                        for used,E in dp.items():
                            for k in range(K-used+1):
                                value = E+cost(k);key=used+k
                                nd[key] = min(nd.get(key,value),value)
                        dp=nd
                    expected=dp.get(K)
                require(got==expected,'optimizer_independent_dynamic_program')
                cases+=1
    # Complete negative-shell tests: all integer splits, not just prime peeling.
    negative=[]
    for p,a in ((37,18),(61,22),(241,64),(3361,847)):
        e = tuple(k for q,k in factor(a)); states=0
        for h in product(*(range(k+1) for k in e)):
            rec=split_record(p,a,h)
            require(rec['witness'] is None,'restricted_negative_all_splits')
            states+=1
        negative.append(dict(p=p,a=a,R=4*a-p,splits=states,scope='one shell only'))
    # Overlap cannot be discarded: 3 decompositions of exponent zero.
    require(sum(1 for x in range(-1,2) for y in range(-1,2) if x+y==0)==3,
            'overlap_multiplicity_three_not_one')
    return dict(optimizer_cases=cases,negative_shells=negative)

def scan(bound):
    totals=Counter();extra=[]
    for p in range(13,bound+1,12):
        if not prime(p):
            continue
        totals['primes']+=1
        for a in range((p+3)//4,(p-1)//2+1):
            totals['shells']+=1
            e=tuple(k for q,k in factor(a))
            base=split_record(p,a,(0,)*len(e))
            hit0=base['witness'] is not None
            totals['baseline_certified']+=hit0
            candidates=[]
            for i,k in enumerate(e):
                for j in range(1,k+1):
                    h=[0]*len(e);h[i]=j
                    if sum(e)==j:
                        continue  # exclude the tautological retained-point endpoint
                    rec=split_record(p,a,tuple(h))
                    if rec['witness'] is not None:
                        candidates.append(rec)
            totals['combined_certified']+=hit0 or bool(candidates)
            if not hit0 and candidates:
                finite=[r for r in candidates if any(c['forced'] and c['lower'] is not None
                                                    for c in r['cells'])]
                totals['additional_finite_minimum' if finite else 'additional_infeasible_minimum']+=1
                chosen=(finite or candidates)[0]
                extra.append(dict(p=p,a=a,R=4*a-p,removed=chosen['removed'],
                                  finite=bool(finite),witness=chosen['witness']))
    return dict(bound=bound,domain='primes p=1 mod 12; p/4<a<p/2; remove one prime budget 1..e',
                totals=dict(totals),additional=extra)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',default='generated')
    parser.add_argument('--bound',type=int,default=1500)
    args=parser.parse_args()
    if args.bound<13:
        parser.error('bound must be at least 13')
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    tests=structural_tests()
    example={'baseline':split_record(1201,312,(0,0,0),True),
             'split':split_record(1201,312,(1,0,0),True)}
    require(example['baseline']['witness'] is None,'baseline_misses_example')
    neg=[c for c in example['split']['cells'] if c['sign']==[-1]][0]
    require((neg['mass'],neg['energy'],neg['lower'])==(30,46,50),'strict_example_numbers')
    require(example['split']['witness']['denominators']==[312,9608,46839],
            'strict_example_order')
    result=scan(args.bound)
    for name,data in [('structural.json',tests),('example.json',example),('scan.json',result),
                      ('checks.json',dict(CHECKS))]:
        (out/name).write_text(json.dumps(data,indent=2,sort_keys=True)+'\n',encoding='utf8')
    print(json.dumps({'checks':sum(CHECKS.values()),'scan':result['totals']},sort_keys=True))

if __name__=='__main__':
    main()
