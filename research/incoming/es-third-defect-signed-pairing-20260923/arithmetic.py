#!/usr/bin/env python3
"""Exact constructors for the accompanying same-shell third-defect lemma.

This is not a universal ES solver. The general map has an explicit trace
input; the R=27 map reports its complete exceptional factor types.
No floating-point arithmetic, numerical fitting, or prime-range census.
"""
from __future__ import annotations
import argparse
import json
from fractions import Fraction
from math import gcd, isqrt
from typing import Any


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, isqrt(n) + 1, 2))


def factor(n: int) -> list[tuple[int, int]]:
    require(n > 0, 'factor input must be positive')
    result: list[tuple[int, int]] = []
    q = 2
    while q * q <= n:
        e = 0
        while n % q == 0:
            n //= q
            e += 1
        if e:
            result.append((q, e))
        q = 3 if q == 2 else q + 2
    if n > 1:
        result.append((n, 1))
    return result


def applicable_residuals(p: int) -> dict[str, Any]:
    """Construct the entire exact-gcd residual family from the supplied prime."""
    require(is_prime(p) and p % 24 == 1, 'p must be prime and 1 mod 24')
    b, k, nu = p - 1, 0, 0
    while b % 2 == 0:
        b //= 2
        k += 1
    while b % 3 == 0:
        b //= 3
        nu += 1
    ds = [1]
    for q, e in factor(b):
        ds = [d * q**j for d in ds for j in range(e + 1)]
    Rs = sorted(3**(nu + 1) * d for d in ds if d % 4 == (-1)**nu % 4)
    for R in Rs:
        require(0 < R < p and R % 4 == 3 and gcd(R, p - 1) == R // 3,
                'constructed exact-gcd residual')
    return {'p': p, 'v2_p_minus_1': k, 'v3_p_minus_1': nu,
            'b': b, 'residuals': Rs,
            'source_nonemptiness_proved': False}


def normalized_state(p: int, R: int, u: int, channel: str) -> dict[str, Any]:
    a = (p + R) // 4
    require(4 * a == p + R and 0 < R < p, 'original shell domain')
    require(u > 0 and a * a % u == 0, 'original divisor domain')
    g = gcd(a, u)
    require(g * g % u == 0, 'normalization integrality')
    h, r, s = g * g // u, u // g, a // g
    require(h * r * s == a and h * r * r == u and gcd(r, s) == 1,
            'normalization identities')
    if channel == 'E':
        require((4 * u + 1) % R == 0, 'exterior gate')
        numerator = p * r + s
        require(numerator % R == 0, 'exterior quotient')
        k = numerator // R
        xyz = [a, h * s * k, p * h * r * k]
        quotient = {'kappa': k}
        inverse_numerator = a * a
    elif channel == 'M':
        require((a + u) % R == 0, 'middle gate')
        numerator = r + s
        require(numerator % R == 0, 'middle quotient')
        k = numerator // R
        xyz = [a, p * h * s * k, p * h * r * k]
        quotient = {'lambda': k}
        inverse_numerator = p * a * a
    else:
        raise ValueError('channel must be E or M')
    require(sum((Fraction(1, x) for x in xyz), Fraction()) == Fraction(4, p),
            'exact reciprocal identity')
    inverse_denominator = R * xyz[1] - p * a
    require(inverse_denominator > 0 and inverse_numerator == u * inverse_denominator,
            'ordered original divisor inverse')
    return {'p': p, 'a': a, 'R': R, 'u': u, 'channel': channel,
            'h': h, 'r': r, 's': s, **quotient,
            'marked_denominators': xyz,
            'increasing_denominators': sorted(xyz),
            'a_factors': factor(a), 'u_factors': factor(u)}


def third_defect_return(p: int, R: int, u: int) -> dict[str, Any]:
    """Return an integer E/M state from a certified denominator-at-most-3 M input."""
    require(is_prime(p) and p % 24 == 1, 'p must be a prime congruent to 1 mod 24')
    require(0 < R < p and R % 4 == 3 and R % 3 == 0, 'residual domain')
    m = R // 3
    require(gcd(R, p - 1) == m, 'required exact gcd is R/3')
    require(m % 3 == 0, 'square-zero divisibility, also a theorem consequence')
    a = (p + R) // 4
    require(u > 0 and a * a % u == 0, 'u must be an original divisor of a^2')
    require((p + 4 * u) % m == 0, 'input must lie in T_3')
    v = a * a // u
    omega = ((p - 1) // m) % 3
    b = ((p + 4 * u) // m) % 3
    require(omega in (1, 2), 'nonzero affine shift')
    require((p + 4 * v) % m == 0, 'complement remains in T_3')
    bv = ((p + 4 * v) // m) % 3
    require(bv == (-b) % 3, 'actual complement law')
    if b == 0:
        chosen, channel, complemented = u, 'M', False
    elif b == omega:
        chosen, channel, complemented = u, 'E', False
    else:
        require(bv == omega, 'third residue must match at the complement')
        chosen, channel, complemented = v, 'E', True
    result = normalized_state(p, R, chosen, channel)
    result['input'] = {'u': u, 'complement': v, 'm': m,
                       'b': b, 'omega': omega, 'complemented': complemented}
    return result


def solve_r27(p: int) -> dict[str, Any]:
    """Factor-level solver for the exact theorem domain, with certified exceptions."""
    require(is_prime(p) and p % 216 in (73, 145),
            'p must be prime and congruent to 73 or 145 mod 216')
    a = (p + 27) // 4
    fs = factor(a)
    require(a % 9 == 7, 'distinguished denominator residue')
    beta: dict[int, int] = {}
    # A residue 8 supplies -1 directly.
    minus = next((q for q, e in fs if q % 9 == 8), None)
    if minus is not None:
        beta[minus] = 1
        reason = 'one residue-8 prime'
    else:
        odd = [(q, e) for q, e in fs if q % 9 in (2, 5)]
        even = [(q, e) for q, e in fs if q % 9 in (4, 7)]
        total = sum(e for q, e in odd)
        require(total % 2 == 0, 'total odd logarithm parity')
        if total == 0:
            return {'p': p, 'a': a, 'R': 27, 'a_factors': fs,
                    'status': 'empty original R=27 shell',
                    'exception': 'A: every prime factor is 1 mod 3',
                    'universal_ES_proved': False}
        if total >= 4:
            remaining = 3
            for q, e in odd:
                take = min(e, remaining)
                if take:
                    beta[q] = take if q % 9 == 2 else -take
                remaining -= take
                if remaining == 0:
                    break
            require(remaining == 0, 'three available odd occurrences')
            reason = 'three signed residue-2-or-5 occurrences'
        elif even:
            q = odd[0][0]
            ell = even[0][0]
            beta[q] = 1 if q % 9 == 2 else -1
            beta[ell] = 1 if ell % 9 == 4 else -1
            reason = 'one odd and one nonidentity even logarithm'
        else:
            require(total == 2 and all(q % 9 == 5 for q, e in odd),
                    'the total residue forces two residue-5 occurrences')
            return {'p': p, 'a': a, 'R': 27, 'a_factors': fs,
                    'status': 'empty original R=27 shell',
                    'exception': 'B: exactly two residue-5 occurrences; all other factors are 1 mod 9',
                    'universal_ES_proved': False}
    u = 1
    for q, e in fs:
        b = beta.get(q, 0)
        require(-e <= b <= e, 'retained original exponent bound')
        u *= q ** (e + b)
    require(u % 9 == 2 and sum(abs(b) for b in beta.values()) <= 3,
            'constructed trace and signed occurrence bound')
    result = third_defect_return(p, 27, u)
    complemented = result['input']['complemented']
    result['construction'] = {
        'reason': reason,
        'input_centred_exponents': sorted(beta.items()),
        'output_centred_exponents': sorted(
            (q, -b if complemented else b) for q, b in beta.items()
        ),
    }
    result['status'] = 'original integer witness'
    result['universal_ES_proved'] = False
    return result


def examples() -> list[dict[str, Any]]:
    # These checks corroborate the constructors. No range or novelty claim.
    e = solve_r27(6841)
    require(e['marked_denominators'] == [1717, 436118, 175499014], 'known E control')
    m = third_defect_return(6121, 27, 29)
    require(m['channel'] == 'M' and m['marked_denominators'][0] == 1537, 'M control')
    a = solve_r27(1009)
    b = solve_r27(73)
    require(a['exception'].startswith('A:'), 'first exceptional form')
    require(b['exception'].startswith('B:'), 'second exceptional form')
    return [e, m, a, b]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--p', type=int)
    parser.add_argument('--R', type=int)
    parser.add_argument('--u', type=int)
    parser.add_argument('--examples', action='store_true')
    parser.add_argument('--residuals', action='store_true')
    args = parser.parse_args()
    if args.examples:
        answer = examples()
    elif args.residuals and args.p is not None:
        answer = applicable_residuals(args.p)
    elif args.p is not None and args.R is None and args.u is None:
        answer = solve_r27(args.p)
    elif args.p is not None and args.R is not None and args.u is not None:
        answer = third_defect_return(args.p, args.R, args.u)
    else:
        parser.error('use --examples, --p P, or --p P --R R --u U')
    print(json.dumps(answer, indent=2, sort_keys=True))
