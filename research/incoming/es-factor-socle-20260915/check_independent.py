#!/usr/bin/env python3
"""Separate exact replay of the dyadic factor-capacity comparison.

Does not import verify.py. Actual unit-group logarithms and parity-aware bounded
knapsack replace the first program's valuation and prefix tests. Complete actual
divisor residues determine the branch hit counts. This is a second implementation,
not independent mathematical review or a new overall ES verification range.
"""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
from math import isqrt, prod
from pathlib import Path


def run(bound):
    if bound < 100:
        raise ValueError('bound >=100 required')
    mark = bytearray([1])*(bound+1)
    mark[0] = mark[1] = 0
    for d in range(2, isqrt(bound)+1):
        if mark[d]:
            for multiple in range(d*d, bound+1, d):
                mark[multiple] = 0
    trial = [d for d in range(2, isqrt(3*bound)+2) if d <= bound and mark[d]]
    def factors(value):
        initial = value
        result = []
        for d in trial:
            if d*d > value:
                break
            if value % d:
                continue
            count = 0
            while not value % d:
                count += 1; value //= d
            result.append((d, count))
        if value > 1:
            result.append((value, 1))
        if prod(q**e for q, e in result) != initial:
            raise ArithmeticError('factorization identity')
        return result
    group_cache = {}
    def coordinates(h, g):
        if (h, g) not in group_cache:
            n = 2**h; L = n//4
            d = {}
            for j in range(L):
                x = pow(g, j, n)
                w = L if j == 0 else j & -j
                d[x] = (0, w)
                d[-x % n] = (1, w)
            if len(d) != n//2:
                raise ArithmeticError('group coordinate size')
            group_cache[h, g] = d
        return group_cache[h, g]
    def tests(F, h, g):
        n = 2**h; L = n//4
        coord = coordinates(h, g)
        types = [(e, *coord[q % n]) for q, e in F]
        reach = 1
        for e, ep, w in types:
            if not ep and w < L:
                new = 0
                for f in range(e+1):
                    new |= reach << (f*w)
                reach = new & ((1 << L)-1)
        weighted = any(ep for e, ep, w in types) and bool((reach >> (L-1)) & 1)
        pivot = False
        for m in sorted({w for e, ep, w in types if ep}):
            target = L-1+m
            mask = (1 << (target+1))-1
            even, odd = 1, 0
            for e, ep, w in types:
                ne, no = 0, 0
                step = 2 if ep and w > m else 1
                for f in range(0, min(e, target//w)+1, step):
                    if ep and w == m and f % 2:
                        ne |= odd << (f*w); no |= even << (f*w)
                    else:
                        ne |= even << (f*w); no |= odd << (f*w)
                even, odd = ne & mask, no & mask
            if (odd >> target) & 1:
                pivot = True
                break
        return weighted, pivot
    checks = 0; C = Counter(); table = []
    op, np = set(), set()
    for p in range(1, bound+1, 24):
        if not mark[p] or p % 840 not in (1, 121, 169, 289, 361, 529):
            continue
        C['primes'] += 1
        for k in range(4, p.bit_length()+1):
            u = 2**(2*k-5)
            if 2*u >= p:
                break
            m, N = 2**k, p+4*u
            F = factors(N)
            ds = [1]
            for q, e in F:
                ds = [d*q**j for d in ds for j in range(e+1)]
            hits = sum(d % m == m-1 for d in ds)
            h = k-1 if p % m == 1+m//2 else k
            w3, n3 = tests(F, h, 3)
            w5, n5 = tests(F, h, 5)
            weighted, new = w3 or w5, n3 or n5
            L = 2**(h-2)
            A = sum(e for q, e in F if q % 8 == 3)
            B = sum(e for q, e in F if q % 8 == 5)
            D = sum(e for q, e in F if q % 8 == 7)
            mixed = bool(D and A+B >= L-1) or any(a <= A and L-a <= B for a in range(1, L, 2))
            phase = next(s for s in range(0, m//4, 2) if pow(3, s, m) == p % m)
            e3 = next((e for q, e in F if q == 3), 0)
            old = e3 >= max(phase, m//4-phase)-1 and any(q % 8 in (5, 7) for q, e in F)
            if (old or new or weighted or mixed) and not hits:
                raise ArithmeticError(('false positivity', p, k))
            if (weighted or mixed) and not new:
                raise ArithmeticError(('lost special case', p, k))
            # Exact coarse-modulus return count, including the reflection fibre.
            coarse = sum(d % 2**h == 2**h-1 for d in ds)
            if coarse != hits*(2 if h == k-1 else 1):
                raise ArithmeticError(('incorrect modulus fibre', p, k))
            checks += 3
            C['valid_seed_branches'] += 1
            C['original_states'] += hits
            C['occupied_branches'] += bool(hits)
            C['old_capacity_branches'] += old
            C['new_certificate_branches'] += new
            C['simple_socle_branches'] += weighted or mixed
            C['mixed_beyond_weighted_branches'] += mixed and not weighted
            C['pivot_beyond_simple_branches'] += new and not (weighted or mixed)
            C['additional_branches'] += new and not old
            if old: op.add(p)
            if new: np.add(p)
            table.append([p, k, hits, int(old), int(weighted), int(mixed), int(new)])
    C.update(old_capacity_primes=len(op), new_certificate_primes=len(np),
             union_primes=len(op | np), additional_primes=len(np-op), old_not_new_primes=len(op-np))
    digest = hashlib.sha256(json.dumps(table, separators=(',', ':')).encode()).hexdigest()
    return dict(bound=bound, checks=checks, counts=dict(C), table_sha256=digest,
                nonclaims=['No imports from main verifier', 'Separate implementation, not independent review',
                           'Factor capacities and prime scope are finite; no universal ES assertion'])


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--bound', type=int, default=2000000)
    ap.add_argument('--out', default='independent.json')
    a = ap.parse_args()
    result = run(a.bound)
    Path(a.out).write_text(json.dumps(result, indent=2, sort_keys=True)+'\n', encoding='utf8')
    print(json.dumps(result, sort_keys=True))

if __name__ == '__main__':
    main()
