#!/usr/bin/env python3
"""Reproduce marked Erdos--Straus certificates, using Python's standard library.

Default finite census: primes <= 2,000,000 in six residue classes modulo 840.
The asymptotic theorems in paper.tex are NOT inferred from this computation.
Primality of every isolated large certificate is checked by trial division.
No probabilistic primality testing, floating-point chamber tests, or dependencies.

Usage:
    python3 verifier.py --out tables
    python3 verifier.py --out tables --families
    python3 verifier.py --self-test-only
Python 3.9+ (modular inverse via pow(a, -1, m)).
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
from itertools import combinations_with_replacement, product
import hashlib
import json
from math import gcd, isqrt, prod
from pathlib import Path
import time
from typing import Dict, Iterable, List, Tuple

HARD = (1, 121, 169, 289, 361, 529)
RAYS = ((2, 1), (3, 2), (5, 3))
State = Dict[str, object]


def factor(n: int) -> Dict[int, int]:
    """Exact trial factorization; loop invariant: removed factors times n = input."""
    if n < 1:
        raise ValueError('factor expects a positive integer')
    out: Dict[int, int] = {}
    q = 2
    while q*q <= n:
        while n % q == 0:
            out[q] = out.get(q, 0)+1
            n //= q
        q = 3 if q == 2 else q+2
    if n > 1:
        out[n] = out.get(n, 0)+1
    return out


def is_prime(n: int) -> bool:
    return n >= 2 and factor(n) == {n: 1}


def divisors_from_factor(f: Dict[int, int]) -> List[int]:
    ds = [1]
    for q, e in sorted(f.items()):
        ds = [d*q**j for d in ds for j in range(e+1)]
    return sorted(ds)


def divisors(n: int) -> List[int]:
    return divisors_from_factor(factor(n))


def primes_to(n: int) -> List[int]:
    if n < 2:
        return []
    sieve = bytearray(b'\x01')*(n+1)
    sieve[:2] = b'\x00\x00'
    for q in range(2, isqrt(n)+1):
        if sieve[q]:
            sieve[q*q:n+1:q] = b'\x00'*((n-q*q)//q+1)
    return [q for q in range(2, n+1) if sieve[q]]


def positive_chamber(r: int, s: int) -> bool:
    """Exact comparisons with the three specified quadratic-surd boundaries."""
    if r <= 0 or s <= 0:
        return False
    # (1+sqrt(2))*r + sqrt(2)*s < sqrt(3)*s.
    D = s*s - 4*r*s - 3*r*r
    lower = D > 0 and D*D > 8*r*r*(r+s)*(r+s)
    # r/s < 1+sqrt(2).
    top = r <= s or (r-s)*(r-s) < 2*s*s
    # (1+sqrt(2))*r > (sqrt(3)+sqrt(2))*s; here r>s.
    E = 3*r*r - 4*r*s - s*s
    high_bottom = r > s and (E >= 0 or 8*r*r*(r-s)*(r-s) > E*E)
    return lower or (top and high_bottom)


def decode(a: int, u: int) -> Tuple[int, int, int]:
    if a <= 0 or u <= 0 or a*a % u:
        raise ValueError('need a>0 and u | a^2')
    d = gcd(a, u)
    r, s = u//d, a//d
    assert d % r == 0
    h = d//r
    assert gcd(r, s) == 1 and a == h*r*s and u == h*r*r
    return h, r, s


def state(p: int, R: int, h: int, r: int, s: int, channel: str) -> State:
    """The caller supplies prime p. Every algebraic condition is rechecked."""
    assert p % 4 == 1 and 0 < R < p and min(h, r, s) > 0
    assert gcd(r, s) == 1 and p+R == 4*h*r*s
    assert channel in ('E', 'M')
    numerator = p*r+s if channel == 'E' else r+s
    assert numerator % R == 0
    k = numerator//R
    xyz = (h*r*s, h*s*k*(1 if channel == 'E' else p), p*h*r*k)
    assert 4*prod(xyz) == p*(xyz[0]*xyz[1]+xyz[0]*xyz[2]+xyz[1]*xyz[2])
    assert xyz[0]*2 < p and xyz[1]*2 > p and xyz[2]*2 > p
    if channel == 'E':
        assert xyz[0] < xyz[1] < xyz[2]
        assert xyz[1] % p != 0 and xyz[2] % p == 0
    else:
        assert xyz[1] % p == xyz[2] % p == 0 and xyz[1] != xyz[2]
    return {'p': p, 'R': R, 'a': h*r*s, 'u': h*r*r,
            'channel': channel, 'h': h, 'r': r, 's': s,
            'kappa': k if channel == 'E' else None,
            'lambda': k if channel == 'M' else None,
            'denominators_raw': list(xyz), 'denominators_increasing': sorted(xyz),
            'positive_chamber': positive_chamber(r, s)}


def full_selector(p: int) -> List[State]:
    """Exhaust the specified bounded selector: 3 <= R < p, R=3 mod 4."""
    assert is_prime(p) and p % 4 == 1
    out: List[State] = []
    for R in range(3, p, 4):
        a = (p+R)//4
        af = factor(a)
        for u in divisors_from_factor({q: 2*e for q, e in af.items()}):
            h, r, s = decode(a, u)
            if (4*u+1) % R == 0:
                out.append(state(p, R, h, r, s, 'E'))
            if (4*u+p) % R == 0:
                out.append(state(p, R, h, r, s, 'M'))
    return out


def ray_states(p: int, r: int, s: int) -> List[State]:
    return [state(p, R, (p+R)//(4*r*s), r, s, 'E')
            for R in divisors(p*r+s) if R < p and (p+R) % (4*r*s) == 0]


def residue_minimum(seq: Iterable[int], m: int, target: int) -> int:
    """Least number of selected occurrences giving target, or len(seq)+1."""
    seq = tuple(seq)
    d = {1: 0}
    for q in seq:
        old = list(d.items())
        for a, k in old:
            b = a*q % m
            d[b] = min(d.get(b, len(seq)+1), k+1)
    return d.get(target, len(seq)+1)


def minimal_patterns(m: int, target: int, bound: int) -> List[List[int]]:
    U = [a for a in range(1, m) if gcd(a, m) == 1]
    out: List[List[int]] = []
    for k in range(1, bound+1):
        for seq in combinations_with_replacement(U, k):
            if prod(seq) % m == target and residue_minimum(seq, m, target) == k:
                out.append(list(seq))
    return out


def pattern_hit(n: int, m: int, patterns: List[List[int]]) -> bool:
    capacity: Counter = Counter()
    for q, e in factor(n).items():
        if gcd(q, m) == 1:
            capacity[q % m] += e
    return any(all(capacity[a] >= e for a, e in Counter(seq).items())
               for seq in patterns)


def cubic_transfer(e: State) -> State:
    assert e['channel'] == 'E'
    p, R, h, r, s = (int(e[k]) for k in ('p', 'R', 'h', 'r', 's'))
    assert (4*r**3-1) % R == 0
    g = gcd(h, r)
    out = state(p, R, s*g*g, r//g, h//g, 'M')
    out['transfer_g'] = g
    out['source_u'] = e['u']
    return out


def cubic_inverse_fibre(m: State) -> List[State]:
    assert m['channel'] == 'M'
    p, R, H, a, b = (int(m[k]) for k in ('p', 'R', 'h', 'r', 's'))
    out = []
    for g in range(1, isqrt(H)+1):
        if H % (g*g):
            continue
        s, r, h = H//(g*g), g*a, g*b
        if gcd(r, s) != 1 or (4*r**3-1) % R:
            continue
        e = state(p, R, h, r, s, 'E')
        assert cubic_transfer(e)['u'] == m['u']
        e['transfer_g'] = g
        out.append(e)
    return out


def crt_pair(a: int, m: int, b: int, n: int) -> int:
    assert gcd(m, n) == 1
    return (a+m*((b-a)*pow(m, -1, n) % n)) % (m*n)


def local_certificates() -> Dict[str, object]:
    records = []
    for c in HARD:
        qs = [q for q in primes_to(2000) if q % 120 == (-c) % 120][:3]
        for q in qs:
            roots = [(-s*pow(r, -1, q)) % q for r, s in RAYS]
            assert len(set(roots)) == 3 and 0 not in roots
            counts: Counter = Counter()
            for a in range(1, q):
                mask = tuple(int(a == x) for x in roots)
                counts[mask] += 1
            assert counts[(0, 0, 0)] == q-4
            for i in range(3):
                assert counts[tuple(int(i == j) for j in range(3))] == 1
            records.append({'c': c, 'Q': q, 'roots': roots,
                            'counts': {','.join(map(str, k)): v for k,v in counts.items()}})
    # Exhaust a two-modulus CRT product, not a sample of primes.
    c, q, ell = 529, 71, 191
    counts = Counter()
    for a in range(1, q):
        for b in range(1, ell):
            n = crt_pair(crt_pair(c, 840, a, q), 840*q, b, ell)
            assert n % 840 == c and n % q == a and n % ell == b
            labels = tuple(next((i+1 for i,(r,s) in enumerate(RAYS) if (r*n+s) % v == 0), 0)
                           for v in (q,ell))
            counts[labels] += 1
    weights_q, weights_l = [q-4,1,1,1], [ell-4,1,1,1]
    for i,j in product(range(4), repeat=2):
        assert counts[(i,j)] == weights_q[i]*weights_l[j]
    return {'local': records, 'crt_pair': {'c':c, 'moduli':[q,ell],
            'sample_space_size':(q-1)*(ell-1),
            'joint_counts':{','.join(map(str,k)):v for k,v in sorted(counts.items())}}}


def lucas_certificate(n: int, base: int) -> Dict[str, object]:
    """Complete n-1 factorization and an elementary order certificate."""
    f = factor(n-1)
    assert prod(q**e for q,e in f.items()) == n-1
    assert all(is_prime(q) for q in f)
    assert pow(base,n-1,n) == 1
    residues = {q: pow(base,(n-1)//q,n) for q in f}
    assert all(gcd(v-1,n) == 1 for v in residues.values())
    return {'n':n,'base':base,'factorization_n_minus_1':f,
            'full_power_residue':1,'proper_power_residues':residues,
            'factor_primality_trial_bounds':{q:isqrt(q) for q in f}}


def zero_sum_certificates() -> Dict[str, int]:
    # Prove the finite group facts computationally, in addition to paper proofs.
    G = list(product(range(4), range(2)))
    checked = 0
    for seq in combinations_with_replacement(G, 5):
        assert any(sum(seq[i][0] for i in range(5) if mask>>i&1) % 4 == 0
                   and sum(seq[i][1] for i in range(5) if mask>>i&1) % 2 == 0
                   for mask in range(1,1<<5))
        checked += 1
    return {'C4xC2_five_multisets_checked': checked}


def positive_companion(r: int, s: int) -> Tuple[int, int]:
    """Return positive (b,d) with r*d-s*b=1, for a primitive positive ray."""
    assert min(r,s)>0 and gcd(r,s)==1
    b = (-pow(s,-1,r)) % r if r>1 else 0
    d = (1+s*b)//r
    if b==0:
        b += r
        d += s
    assert min(b,d)>0 and r*d-s*b==1
    return b,d


def companion_coordinates(source: State, target: State) -> Dict[str, int]:
    """Exact signed coordinates in the same-residual bijection; det=+1."""
    assert source['channel']==target['channel']=='E'
    assert (source['p'],source['R'])==(target['p'],target['R'])
    p,R,r,s = (int(source[k]) for k in ('p','R','r','s'))
    rr,ss = int(target['r']),int(target['s'])
    b,d=positive_companion(r,s)
    A,C=d*rr-b*ss, -s*rr+r*ss
    assert C%R==0
    B=C//R
    assert (rr,ss)==(A*r+R*B*b,A*s+R*B*d)
    assert gcd(A,R*B)==1 and int(source['a'])%(rr*ss)==0
    assert int(target['kappa'])==A*int(source['kappa'])+B*(b*p+d)
    rebuilt=state(p,R,int(source['a'])//(rr*ss),rr,ss,'E')
    assert rebuilt['denominators_raw']==target['denominators_raw']
    return {'companion_b':b,'companion_d':d,'A':A,'B':B,
            'height_barrier_product':(r+R*b)*(s+R*d)}


def map_certificates(tables: Iterable[List[State]]) -> List[dict]:
    """Check every same-shell E fibre and every E/M divisor translation in stress tables."""
    out=[]
    for states in tables:
        for e in states:
            p,R,a,u = (int(e[k]) for k in ('p','R','a','u'))
            y=int(e['denominators_raw'][1])
            numerator=a*a*(p if e['channel']=='M' else 1)
            assert numerator%(R*y-p*a)==0
            assert numerator//(R*y-p*a)==u
            if e['channel']=='M':
                partner=state(p,R,int(e['h']),int(e['s']),int(e['r']),'M')
                assert partner['u']==a*a//u and partner['u']!=u
                assert any(t['channel']=='M' and t['u']==partner['u'] and t['R']==R for t in states)
                inverse=cubic_inverse_fibre(e)
                expected=[t for t in states if t['channel']=='E' and t['R']==R
                          and int(t['s'])*int(t['r'])**2==u
                          and (4*int(t['r'])**3-1)%R==0]
                assert sorted(int(t['u']) for t in inverse)==sorted(int(t['u']) for t in expected)
                continue
            targets=[t for t in states if t['channel']=='E' and t['R']==R]
            fibre=[{'target_u':t['u'],**companion_coordinates(e,t)} for t in targets]
            middles=[t for t in states if t['channel']=='M' and t['R']==R]
            for m in middles:
                assert (int(m['u'])-p*u)%R==0
            # The complete divisor list verifies the translation locus in both directions.
            translated=[v for v in divisors(a*a) if (v-p*u)%R==0]
            assert sorted(translated)==sorted(int(t['u']) for t in middles)
            out.append({'p':p,'R':R,'source_u':u,'companion_fibre':fibre,
                        'middle_translation_targets':translated,
                        'cubic_transfer_exists':(4*int(e['r'])**3-1)%R==0})
    return out


def self_tests() -> Dict[str, object]:
    a = full_selector(1201)
    b = full_selector(2521)
    for states, E, M, inc in [(a,7,8,11),(b,6,6,9)]:
        assert sum(t['channel']=='E' for t in states) == E
        assert sum(t['channel']=='M' for t in states) == M
        assert len({tuple(t['denominators_raw']) for t in states}) == E+M
        assert len({tuple(t['denominators_increasing']) for t in states}) == inc
        assert sum(bool(t['positive_chamber']) for t in states) == 3
        for t in states:
            h,r,s = decode(int(t['a']),int(t['u']))
            assert (h,r,s)==(t['h'],t['r'],t['s'])
    assert not any(t['channel']=='E' and t['positive_chamber'] for t in b)
    assert not any(3*int(t['s']) <= 2*int(t['r']) <= 4*int(t['s']) for t in a)
    assert all(not ray_states(1201,r,s) for r,s in RAYS)
    e = next(t for t in b if t['channel']=='E' and t['R']==31)
    m = cubic_transfer(e)
    assert (m['h'],m['r'],m['s'],m['lambda']) == (11,2,29,1)
    assert any(t['u']==e['u'] for t in cubic_inverse_fibre(m))
    # The h=60 example tests nontrivial normalization g=2.
    p = 4*60*2*1-31
    assert p == 449 and is_prime(p)
    normalized = cubic_transfer(state(p,31,60,2,1,'E'))
    assert (normalized['h'],normalized['r'],normalized['s'],normalized['lambda']) == (4,1,30,1)
    assert not any(t['channel']=='M' and t['R']==71 for t in a)
    assert not any((4*int(t['r'])**3-1) % int(t['R']) == 0 for t in a if t['channel']=='E')
    collision = state(389,3,49,1,2,'M')
    fibre = cubic_inverse_fibre(collision)
    assert [t['transfer_g'] for t in fibre] == [1,7]
    assert all(cubic_transfer(t)['u'] == collision['u'] for t in fibre)
    # Exact divisor-box translations at the two stress-test shells.
    assert (1201*17-108) % 23 == 0
    assert (1201*1232-2) % 31 == 0
    # No square-root floating point in the positivity predicate.
    for r,s in RAYS+((1,18),(1,154),(1,155),(2,29)):
        assert positive_chamber(r,s)
    for r,s in ((3,4),(2,11),(1,2),(7,2),(17,4),(27,2)):
        assert not positive_chamber(r,s)
    sharp=[]
    for p, expected_R, degree in [(6320329,151931,4),(2668835929,5635211,5)]:
        assert is_prime(p) and p % 840 in HARD
        hits=ray_states(p,5,3)
        assert len(hits)==1 and hits[0]['R']==expected_R
        assert sum(factor(expected_R).values())==degree
        sharp.append({'p':p,'trial_division_bound':isqrt(p),
                      'factorization_L3':factor(5*p+3), 'states':hits,
                      'minimum_residual_Omega':degree})
    small_sharp=[]
    for p,ray,Rs in [(3529,(2,1),[39,543]),(153409,(3,2),[3311,10703])]:
        assert is_prime(p) and p%840 in HARD
        hits=ray_states(p,*ray)
        assert [t['R'] for t in hits]==Rs
        assert all(sum(factor(int(t['R'])).values())==ray[0] for t in hits)
        small_sharp.append({'p':p,'ray':ray,'factorization_L':factor(ray[0]*p+ray[1]),
                            'states':hits,'minimum_residual_Omega':ray[0]})
    return {'stress_1201':a,'obstruction_2521':b,
            'map_fibres':map_certificates([a,b]),
            'sharp_small_rays':small_sharp,
            'cubic_bridge':{'source':e,'target':m,'normalized_example':normalized,'collision_target':collision,'collision_fibre':fibre},
            'sharp_certificates':sharp,
            'primality_certificates':[lucas_certificate(n,b) for n,b in
                 [(1201,11),(2521,17),(3529,17),(3889,11),(17929,11),(153409,19),(6320329,41),(2668835929,13)]],
            'zero_sum':zero_sum_certificates(),
            'local':local_certificates()}


def three_ray_census(bound: int, pats: Dict[str,List[List[int]]]) -> Tuple[dict,list]:
    ps=[p for p in primes_to(bound) if p % 840 in HARD]
    rows=[]
    summary={'bound':bound,'hard_classes':HARD,'prime_count':len(ps),
             'by_ray':[], 'by_class':[], 'channels':dict()}
    channel_counts=Counter()
    for p in ps:
        ray_data=[]
        for i,(r,s) in enumerate(RAYS):
            states=ray_states(p,r,s)
            for t in states:
                t['residual_is_prime']=is_prime(int(t['R']))
            prime_states=[t for t in states if t['residual_is_prime']]
            key='8_7' if i==0 else '24_23' if i==1 else '60_'+str((-p)%60)
            assert bool(states) == pattern_hit(r*p+s,4*r*s,pats[key])
            # Validate the simpler exact prime-support tests for v1 and v2.
            if i==0:
                assert bool(states) == any(q%8 in (5,7) for q in factor(2*p+1))
            elif i==1:
                residues={q%24 for q in factor(3*p+2)}
                assert bool(states) == (not (residues <= {1,5,13,17} or residues <= {1,5,7,11}))
            for t in prime_states:
                channel_counts[f'v{i+1}_Qmod24_{int(t["R"])%24}']+=1
            ray_data.append({'ray':[r,s],'states':states,
                             'prime_residuals':[t['R'] for t in prime_states]})
        rows.append({'p':p,'c':p%840,'rays':ray_data})
    def hit(row,i,onlyprime):
        return bool(row['rays'][i]['prime_residuals'] if onlyprime else row['rays'][i]['states'])
    for i,(r,s) in enumerate(RAYS):
        degrees=Counter()
        for row in rows:
            if hit(row,i,False):
                degrees[min(sum(factor(int(t['R'])).values()) for t in row['rays'][i]['states'])]+=1
        summary['by_ray'].append({'ray':[r,s],
          'prime_residual_states':sum(len(row['rays'][i]['prime_residuals']) for row in rows),
          'prime_residual_prime_hits':sum(hit(row,i,True) for row in rows),
          'all_residual_states':sum(len(row['rays'][i]['states']) for row in rows),
          'all_residual_prime_hits':sum(hit(row,i,False) for row in rows),
          'minimum_Omega_histogram':dict(degrees)})
    for c in HARD:
        rr=[row for row in rows if row['c']==c]
        summary['by_class'].append({'c':c,'primes':len(rr),
            'old_prime_hits':sum(hit(t,0,True) or hit(t,1,True) for t in rr),
            'v3_prime_states':sum(len(t['rays'][2]['prime_residuals']) for t in rr),
            'v3_prime_hits':sum(hit(t,2,True) for t in rr),
            'v3_new_prime_hits':sum(hit(t,2,True) and not(hit(t,0,True) or hit(t,1,True)) for t in rr),
            'all_three_composite_completed_hits':sum(any(hit(t,i,False) for i in range(3)) for t in rr)})
    for onlyprime,name in [(True,'prime_residual'),(False,'all_residual')]:
        summary[name+'_old_hits']=sum(hit(t,0,onlyprime) or hit(t,1,onlyprime) for t in rows)
        summary[name+'_union_hits']=sum(any(hit(t,i,onlyprime) for i in range(3)) for t in rows)
        summary[name+'_v3_new_hits']=sum(hit(t,2,onlyprime) and not(hit(t,0,onlyprime) or hit(t,1,onlyprime)) for t in rows)
    summary['channels']=dict(channel_counts)
    summary['first_v3_new']=next((row for row in rows if hit(row,2,True) and not(hit(row,0,True) or hit(row,1,True))),None)
    summary['first_common_v3_new']=next((row for row in rows if not(hit(row,0,True) or hit(row,1,True)) and
         any(q%120==(-row['c'])%120 for q in row['rays'][2]['prime_residuals'])),None)
    if bound==2000000:
        assert len(ps)==4519
        assert summary['prime_residual_old_hits']==1668
        assert summary['prime_residual_union_hits']==1972
        assert summary['prime_residual_v3_new_hits']==304
        assert summary['all_residual_union_hits']==2835
        assert summary['all_residual_old_hits']==2588
        assert summary['all_residual_v3_new_hits']==247
        assert [t['prime_residual_states'] for t in summary['by_ray']]==[1566,838,550]
        assert [t['all_residual_states'] for t in summary['by_ray']]==[5777,2694,720]
        assert summary['first_v3_new']['p']==3889
        assert summary['first_common_v3_new']['p']==17929
    return summary,rows


def farey_row(depth: int) -> List[Tuple[int,int]]:
    vs=[(2,1),(3,2)]
    for _ in range(depth):
        vs=[w for i,v in enumerate(vs[:-1]) for w in
            (v,(v[0]+vs[i+1][0],v[1]+vs[i+1][1]))]+[vs[-1]]
    assert len(vs)==2**depth+1
    assert all(positive_chamber(*v) for v in vs)
    assert all(a*d-b*c==1 for (a,b),(c,d) in zip(vs,vs[1:]))
    return vs


def family_census(bound: int) -> Dict[str,object]:
    ps=[p for p in primes_to(bound) if p%840 in HARD]
    cache={}
    def scan(v):
        if v not in cache:
            r,s=v
            cache[v]={p:[R for R in divisors(r*p+s) if R<p and (p+R)%(4*r*s)==0] for p in ps}
        return cache[v]
    upper=[]
    for d in range(5):
        vs=farey_row(d)
        for v in vs:scan(v)
        hits={p for p in ps if any(cache[v][p] for v in vs)}
        upper.append({'depth':d,'rays':vs,'ray_count':len(vs),'prime_hits':len(hits),
                      'states':sum(len(cache[v][p]) for v in vs for p in ps),
                      'exception_log_exponent':str(Fraction(2+len(vs),2))})
    base=hits
    lower=set();lower_rows=[]
    for s in range(8,129):
        assert positive_chamber(1,s)
        low=scan((1,s))
        lower|={p for p in ps if low[p]}
        if s in (8,12,18,24,32,48,64,96,128):
            lower_rows.append({'s_max':s,'lower_ray_count':s-7,'lower_prime_hits':len(lower),
                               'with_17_upper_prime_hits':len(base|lower),
                               'remaining_primes':sorted(set(ps)-(base|lower))})
    witnesses=[]
    for p in ps:
        for v in farey_row(4)+[(1,s) for s in range(8,129)]:
            if cache[v][p]:
                r,s=v;R=cache[v][p][0]
                witnesses.append(state(p,R,(p+R)//(4*r*s),r,s,'E'))
                break
    repair_shells=(11,19,23,39)
    missing=sorted(set(ps)-{int(t['p']) for t in witnesses})
    repairs=[]
    for p in missing:
        chosen=None
        for R in repair_shells:
            if R>=p:continue
            a=(p+R)//4
            for u in divisors_from_factor({q:2*e for q,e in factor(a).items()}):
                if (4*u+p)%R:continue
                h,r,s=decode(a,u)
                if positive_chamber(r,s):
                    chosen=state(p,R,h,r,s,'M')
                    break
            if chosen is not None:break
        if chosen is not None:repairs.append(chosen)
    unhit=sorted(set(missing)-{int(t['p']) for t in repairs})
    if bound==2000000:
        assert [d['prime_hits'] for d in upper]==[2588,2835,3010,3334,3512]
        assert len(witnesses)==4508
        assert len(repairs)==11 and not unhit
    return {'bound':bound,'upper':upper,'lower':lower_rows,
            'one_witness_per_covered_prime':witnesses,
            'middle_repair_shells':repair_shells,'middle_repair_witnesses':repairs,
            'hybrid_prime_hits':len(witnesses)+len(repairs),'hybrid_uncovered_primes':unhit}


def write_json(path: Path, obj: object) -> None:
    path.write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n',encoding='utf-8')


def main() -> None:
    if not __debug__:
        raise RuntimeError('Certificates require assertions: run Python without -O or -OO.')
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--bound',type=int,default=2000000)
    ap.add_argument('--out',type=Path,default=Path('tables'))
    ap.add_argument('--families',action='store_true')
    ap.add_argument('--self-test-only',action='store_true')
    args=ap.parse_args()
    if args.bound<2:ap.error('--bound must be at least 2')
    start=time.monotonic()
    args.out.mkdir(parents=True,exist_ok=True)
    tests=self_tests()
    for name,obj in tests.items():write_json(args.out/(name+'.json'),obj)
    pats={f'{m}_{t}':minimal_patterns(m,t,k) for m,t,k in [(8,7,2),(24,23,3),(60,59,5),(60,11,5)]}
    assert len(pats['8_7'])==2 and len(pats['24_23'])==8
    assert Counter(map(len,pats['60_59']))==Counter({1:1,2:7,3:32,4:80,5:64})
    assert Counter(map(len,pats['60_11']))==Counter({1:1,2:7,3:32,4:80,5:64})
    write_json(args.out/'minimal_patterns.json',pats)
    if not args.self_test_only:
        summary,rows=three_ray_census(args.bound,pats)
        write_json(args.out/'summary.json',summary)
        write_json(args.out/'three_ray_states.json',rows)
        if args.families:write_json(args.out/'families.json',family_census(args.bound))
        print(json.dumps({k:v for k,v in summary.items() if not k.startswith('first_')},indent=2))
    files={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(args.out.glob('*.json')) if p.name!='manifest.json'}
    write_json(args.out/'manifest.json',{'sha256':files,'finite_bound':args.bound,
        'large_prime_certificates_checked_by_trial_division':True,
        'asymptotic_theorems_computationally_proved':False})
    print(f'All exact checks passed; elapsed {time.monotonic()-start:.3f} seconds.')

if __name__=='__main__':
    main()
