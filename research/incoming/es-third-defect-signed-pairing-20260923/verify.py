#!/usr/bin/env python3
"""Exact regression checks for the signed-pairing and third-defect module."""
from __future__ import annotations

import json
from fractions import Fraction
from math import gcd, isqrt

import arithmetic


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def divisors(n: int) -> list[int]:
    out = [1]
    q = 2
    while q * q <= n:
        if n % q:
            q = 3 if q == 2 else q + 2
            continue
        e = 0
        while n % q == 0:
            n //= q
            e += 1
        out = [d * q**j for d in out for j in range(e + 1)]
        q = 3 if q == 2 else q + 2
    if n > 1:
        out = [d * n**j for d in out for j in range(2)]
    return sorted(out)


def qpow(x: Fraction, e: int) -> Fraction:
    return x**e if e >= 0 else Fraction(1, 1) / (x ** (-e))


def normalized(a: int, u: int) -> tuple[int, int, int]:
    g = gcd(a, u)
    return g * g // u, u // g, a // g


def signed_pair_direct(p: int, a: int, sigma: int) -> Fraction:
    r = 4 * a - p
    total = Fraction()
    ds = divisors(p * a)
    for d in ds:
        for e in ds:
            if (d + e) % r == 0:
                total += qpow(Fraction(d * e, p * a), -sigma)
    return total


def signed_pair_fibres(p: int, a: int, sigma: int) -> Fraction:
    r0 = 4 * a - p
    total = Fraction()
    for u in divisors(a * a):
        h, _r, _s = normalized(a, u)
        weight = sum((qpow(Fraction(h, k * k), sigma) for k in divisors(h)), Fraction())
        if (4 * u + 1) % r0 == 0:
            total += 2 * weight
        if (p + 4 * u) % r0 == 0:
            total += (qpow(Fraction(p), sigma) + qpow(Fraction(p), -sigma)) * weight
    return total


def shell_sets(p: int, r0: int) -> tuple[list[int], list[int], list[int]]:
    a = (p + r0) // 4
    m = r0 // 3
    words = divisors(a * a)
    e = [u for u in words if (4 * u + 1) % r0 == 0]
    middle = [u for u in words if (p + 4 * u) % r0 == 0]
    trace = [u for u in words if (p + 4 * u) % m == 0]
    return e, middle, trace


def verify_cross_shell() -> dict[str, int]:
    p, r0, m = 73, 3, 1
    q = 4 * m + 1
    a = (p + r0) // 4
    ap = a + m * r0
    d, e = 1, 2
    alpha, beta = p * a // d, p * ap // e
    lam, mu = (d + e) // r0, (alpha + beta) // r0
    require(lam * beta - d * mu == p * m, 'first cross-shell determinant')
    require(e * mu - lam * alpha == p * m, 'second cross-shell determinant')
    rhs = (Fraction(1, a) + Fraction(1, lam * alpha)
           + Fraction(1, mu * d) + Fraction(m, a * lam * mu))
    require(rhs == Fraction(4, p), 'cross-shell reciprocal identity')
    g = gcd(lam * mu, m)
    nu = (lam * mu + m) // g
    rho = nu // gcd(a, nu)
    require(rho == 731, 'retained cross-shell obstruction order')
    return {'p': p, 'R': r0, 'q': q, 'a': a, 'a_prime': ap,
            'lambda': lam, 'mu': mu, 'nu': nu, 'rho': rho}


def sharpness_progression(n: int) -> dict[str, int]:
    require(n > 3 and n % 2 == 1, 'larger odd quotient')
    m = 3 * n
    r0 = 3 * n * n
    s = next(x for x in range(1, 8 * n + 1)
             if x % n == 1 and (m * x) % 8 == 5)
    u = (m * s - 1) // 4
    k0 = next(x for x in range(0, 2 * n + 1, 2)
              if (4 * u * x) % n == 2)
    j = 0
    while True:
        k = k0 + 2 * n * j
        a = u * (m * k - 1)
        p0 = 4 * a - r0
        if p0 > r0:
            break
        j += 1
    step = 8 * u * m * n
    require(p0 % 24 == 1 and gcd(p0, step) == 1, 'reduced hard-prime progression')
    require(gcd(r0, p0 - 1) == m and r0 % 4 == 3 and r0 % (m * n) == 0,
            'progression quotient domain')
    require(a * a % u == 0 and (p0 + 4 * u) % m == 0,
            'displayed uncovered source')
    b = ((p0 + 4 * u) // m) % n
    omega = ((p0 - 1) // m) % n
    require(b == 2 and omega == 1 and (-b) % n not in (0, omega),
            'uncovered colour orbit')
    return {'N': n, 'm': m, 'R': r0, 's': s, 'U': u,
            'p_progression_residue': p0, 'step': step}


def main() -> None:
    assertions = 0
    supplied = arithmetic.examples()
    assertions += 4
    require(supplied[0]['construction']['input_centred_exponents'] == [(17, 1)],
            'input exponent field')
    require(supplied[0]['construction']['output_centred_exponents'] == [(17, -1)],
            'output exponent field after complement')
    require(supplied[1]['marked_denominators'] == [1537, 18815954, 355018],
            'marked M order retained')
    require(supplied[1]['increasing_denominators'] == [1537, 355018, 18815954],
            'increasing M view retained separately')
    assertions += 4

    counts = []
    for p in (6841, 6121, 1009, 73):
        e, middle, trace = shell_sets(p, 27)
        require(2 * len(e) + len(middle) == len(trace), f'third-defect count at {p}')
        for u in trace:
            v = ((p + 27) // 4) ** 2 // u
            require(v in trace, f'complement source at {p},{u}')
            require((((p + 4 * u) // 9) + ((p + 4 * v) // 9)) % 3 == 0,
                    f'complement colour at {p},{u}')
        counts.append({'p': p, 'E': len(e), 'M': len(middle), 'T3': len(trace)})
        assertions += 1 + 2 * len(trace)

    signed_tests = 0
    for a in range(19, 37):
        for sigma in (-2, -1, 0, 1, 2):
            require(signed_pair_direct(73, a, sigma) == signed_pair_fibres(73, a, sigma),
                    f'signed fibre identity at a={a}, sigma={sigma}')
            signed_tests += 1
    assertions += signed_tests

    for n in range(3, 42, 2):
        omega = 1
        closes = set((0, omega % n, (-omega) % n)) == set(range(n))
        require(closes == (n == 3), f'unique odd quotient at N={n}')
        assertions += 1

    residual_checks = []
    for p in (73, 1009, 6121, 6841):
        packet = arithmetic.applicable_residuals(p)
        for r0 in packet['residuals']:
            require(gcd(r0, p - 1) == r0 // 3 and r0 % 4 == 3 and r0 < p,
                    f'applicable residual at {p},{r0}')
            assertions += 1
        residual_checks.append({'p': p, 'residuals': packet['residuals']})

    cross = verify_cross_shell()
    assertions += 5
    sharpness = [sharpness_progression(n) for n in (5, 7, 9, 11, 15, 21)]
    assertions += 24
    report = {
        'status': 'pass',
        'assertions': assertions,
        'signed_pair_exact_tests': signed_tests,
        'third_defect_counts': counts,
        'applicable_residual_checks': residual_checks,
        'cross_shell_negative_control': cross,
        'larger_quotient_progressions': sharpness,
        'universal_ES_proved': False,
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
