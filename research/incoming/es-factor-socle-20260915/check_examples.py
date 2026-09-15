#!/usr/bin/env python3
"""Independent direct checks of the three displayed actual-factor certificates.

Standard library. Checks are active with -O. All divisor words and integer
coefficients are explicit; a zero parity is never read as an absent source.
This is a worked-example checker, not a universal search or prime theorem.
"""
import argparse
from collections import Counter
from fractions import Fraction
from itertools import product
import json
from math import gcd, isqrt, prod
from pathlib import Path


def check(value, message):
    if not value:
        raise ArithmeticError(message)


def prime(n):
    return n >= 2 and all(n % q for q in range(2, isqrt(n)+1))


def divisor_list(F):
    out = [1]
    for q, e in F:
        out = [d*q**j for d in out for j in range(e+1)]
    return sorted(out)


def return_state(p, k, Q):
    u, m = 2**(2*k-5), 2**k
    N = p+4*u
    check(p % 8 == 1 and p > 2*u and Q % m == m-1 and N % Q == 0, 'factor atlas domain')
    R = N//Q
    check((p+R) % 4 == 0 and 3 <= R < p and 3 <= Q < p, 'residual and range')
    a = (p+R)//4
    d = gcd(a, u)
    check(a*a % u == 0 and d*d % u == 0, 'original divisor available')
    h, r, s = d*d//u, u//d, a//d
    check((r+s) % R == 0, 'middle quotient integral')
    lam = (r+s)//R
    den = [a, p*h*s*lam, p*h*r*lam]
    check(h*r*s == a and h*r*r == u and gcd(r, s) == 1, 'normalization inverse')
    check(all(x > 0 for x in den), 'positive denominators')
    check(sum((Fraction(1, x) for x in den), Fraction()) == Fraction(4, p), 'ES reciprocal identity')
    check(Fraction(p*a*a, R*den[1]-p*a) == u, 'ordered divisor inverse')
    return dict(p=p, k=k, channel='M', u=u, N=N, R=R, Q=Q, a=a,
                h=h, r=r, s=s, lambda_middle=lam, denominators=den)


def certify(p, k, F, selected):
    check(prime(p), 'complete trial proof of p prime')
    check(all(prime(q) and e > 0 for q, e in F), 'actual prime factors')
    check(len(dict(F)) == len(F), 'distinct factor labels')
    N = p+2**(2*k-3)
    check(prod(q**e for q, e in F) == N, 'factorization product')
    f = dict(selected)
    check(all(q in dict(F) and 0 < t <= dict(F)[q] for q, t in f.items()), 'actual selected budgets')
    m = 2**k
    level = k-1 if p % m == 1+m//2 else k
    n, L = 2**level, 2**(level-2)
    check(sum(f.values()) <= L, 'reserved occurrence bound')
    blocks = [(q, j, q**(2**j)) for q, t in sorted(f.items())
              for j in range(t.bit_length()) if (t >> j) & 1]
    words = []
    for bits in product((0, 1), repeat=len(blocks)):
        d = prod(block**bit for bit, (q, j, block) in zip(bits, blocks))
        check(N % d == 0, 'word is an original divisor')
        words.append(dict(bits=list(bits), divisor=d, residue=d % n))
    check(len({w['divisor'] for w in words}) == len(words), 'binary word inverse is injective')
    counts = Counter(w['residue'] for w in words)
    check(set(counts) == set(range(1, n, 2)), 'all units actually reached')
    check(all(c % 2 == 1 for c in counts.values()), 'odd coefficients of original positive polynomial')
    targets = [w for w in words if w['residue'] == n-1]
    constructed = []
    for w in targets:
        d = w['divisor']
        Q = d if d % m == m-1 else N//d
        state = return_state(p, k, Q)
        state.update(selected_divisor=d, factor_role='cofactor' if Q == d else 'residual',
                     selected_bits=w['bits'])
        constructed.append(state)
    complete = [return_state(p, k, Q) for Q in divisor_list(F) if Q % m == m-1]
    packing = prod((e+1)//(f.get(q, 0)+1) for q, e in F)
    bound = packing if level == k else (packing+1)//2
    check(len(complete) >= bound, 'original disjoint-packing lower count')
    if p == 1794769:
        check(len(complete) == 1 and (complete[0]['R'], complete[0]['Q']) == (207, 8671), 'unique hard-example state')
        for exp in product(*(range(e+1) for q, e in F)):
            if sum(exp) <= 2:
                d = prod(q**j for (q, e), j in zip(F, exp))
                check(d % m not in (m-1, (-p) % m), 'no shorter target word')
    return dict(p=p, k=k, input_factorization=F, selected=selected,
                effective_level=level, blocks=blocks, complete_word_table=words,
                residue_counts=sorted(counts.items()), constructed=constructed,
                complete_original_states=complete, packing_blocks=packing,
                original_count_lower=bound)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', default='direct_examples.json')
    a = ap.parse_args()
    cases = [
        (1794769, 5, [(3,2),(13,1),(23,2),(29,1)], [(3,2),(13,1),(23,1)]),
        (165601, 4, [(3,1),(13,1),(31,1),(137,1)], [(3,1),(13,1),(137,1)]),
        (852769, 6, [(3,3),(11,1),(13,2),(17,1)], [(3,3),(13,1),(17,1)])]
    result = [certify(*c) for c in cases]
    Path(a.out).write_text(json.dumps(result, sort_keys=True, indent=2)+'\n', encoding='utf8')
    print(json.dumps({'examples':len(result), 'original_states':[len(x['complete_original_states']) for x in result]}))


if __name__ == '__main__':
    main()
