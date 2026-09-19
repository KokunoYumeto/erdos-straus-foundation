#!/usr/bin/env python3
"""Independent verifier for the Turn 6b pointwise-localization results.

Only the Python standard library is used.  Every mathematical check goes
through ``Audit.check``; no Python ``assert`` statement is used, so ``python
-O`` executes exactly the same verification path.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from functools import lru_cache
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple


class VerificationError(RuntimeError):
    """Raised at the first failed mathematical check."""


class Audit:
    def __init__(self) -> None:
        self.checks = 0
        self._digest = hashlib.sha256()
        self.negative_controls: List[Dict[str, object]] = []

    def check(self, condition: bool, tag: str, *data: object) -> None:
        self.checks += 1
        payload = json.dumps(
            [tag, *data], ensure_ascii=True, separators=(",", ":"), sort_keys=True
        ).encode("ascii")
        if not condition:
            raise VerificationError(payload.decode("ascii"))
        self._digest.update(payload)
        self._digest.update(b"\n")

    def reject(self, false_claim: bool, control_id: str, detail: str) -> None:
        self.check(not false_claim, "negative-control", control_id, detail)
        self.negative_controls.append(
            {"id": control_id, "rejected": True, "detail": detail}
        )

    def hexdigest(self) -> str:
        return self._digest.hexdigest()


def primes_up_to(bound: int) -> List[int]:
    if bound < 2:
        return []
    sieve = bytearray(b"\x01") * (bound + 1)
    sieve[0:2] = b"\x00\x00"
    for q in range(2, math.isqrt(bound) + 1):
        if sieve[q]:
            start = q * q
            sieve[start : bound + 1 : q] = b"\x00" * (
                ((bound - start) // q) + 1
            )
    return [n for n in range(2, bound + 1) if sieve[n]]


def smallest_factor(n: int) -> int:
    if n < 2:
        return n
    if n % 2 == 0:
        return 2
    q = 3
    while q * q <= n:
        if n % q == 0:
            return q
        q += 2
    return n


def is_prime(n: int) -> bool:
    return n >= 2 and smallest_factor(n) == n


@lru_cache(maxsize=None)
def factorization(n: int) -> Tuple[Tuple[int, int], ...]:
    if n < 1:
        raise ValueError("factorization requires a positive integer")
    remaining = n
    factors: List[Tuple[int, int]] = []
    q = 2
    while q * q <= remaining:
        if remaining % q == 0:
            exponent = 0
            while remaining % q == 0:
                remaining //= q
                exponent += 1
            factors.append((q, exponent))
        q = 3 if q == 2 else q + 2
    if remaining > 1:
        factors.append((remaining, 1))
    return tuple(factors)


def divisors_from_factors(
    factors: Sequence[Tuple[int, int]], exponent_multiplier: int = 1
) -> Tuple[int, ...]:
    values = [1]
    for prime, exponent in factors:
        powers = [prime**e for e in range(exponent * exponent_multiplier + 1)]
        values = [old * power for old in values for power in powers]
    return tuple(sorted(values))


@lru_cache(maxsize=None)
def divisors(n: int) -> Tuple[int, ...]:
    return divisors_from_factors(factorization(n))


@lru_cache(maxsize=None)
def square_divisors(n: int) -> Tuple[int, ...]:
    return divisors_from_factors(factorization(n), exponent_multiplier=2)


def jacobi(a: int, odd_modulus: int) -> int:
    if odd_modulus <= 0 or odd_modulus % 2 == 0:
        raise ValueError("Jacobi denominator must be a positive odd integer")
    a %= odd_modulus
    result = 1
    n = odd_modulus
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a %= n
    return result if n == 1 else 0


def least_nonresidue(p: int) -> int:
    for n in range(2, p):
        if jacobi(n, p) == -1:
            return n
    raise VerificationError(f"no nonresidue found modulo {p}")


def least_three_mod_four_nonresidue(p: int) -> int:
    for n in range(3, p, 4):
        if jacobi(n, p) == -1:
            return n
    raise VerificationError(f"no 3 mod 4 nonresidue found modulo {p}")


def prime_factors_three_mod_four(n: int) -> Tuple[int, ...]:
    return tuple(q for q, _ in factorization(n) if q % 4 == 3)


def unit_fraction_identity(p: int, x: int, y: int, z: int) -> bool:
    return 4 * x * y * z == p * (x * y + x * z + y * z)


def add_generated_pair(
    generated: Dict[Tuple[int, int], int], pair: Tuple[int, int]
) -> None:
    generated[pair] = generated.get(pair, 0) + 1


def verify_prime_invariants(p: int, audit: Audit, counts: Dict[str, int]) -> Tuple[int, int, int, bool]:
    nu = least_nonresidue(p)
    m = least_three_mod_four_nonresidue(p)
    Jp = (m + 1) // 4
    hard = all(jacobi(q, p) == 1 for q in (2, 3, 5, 7))

    audit.check(nu % 2 == 1 and is_prime(nu), "least-nr-odd-prime", p, nu)
    audit.check(3 <= nu < p, "least-nr-range", p, nu)
    audit.check(nu * nu <= p, "least-nr-square-bound", p, nu)
    witness = p - 2 * nu
    audit.check(0 < witness < p, "least-nr-derived-range", p, nu, witness)
    audit.check(witness % 4 == 3, "least-nr-derived-class", p, nu, witness)
    audit.check(jacobi(witness, p) == -1, "least-nr-derived-symbol", p, nu, witness)
    audit.check(m % 4 == 3 and jacobi(m, p) == -1, "least-3mod4", p, m)
    audit.check(m <= witness < p, "least-3mod4-bound", p, m, witness)
    audit.check(4 * Jp == m + 1, "Jp-definition", p, m, Jp)
    if hard:
        counts["hard_primes"] += 1
        audit.check(nu >= 11 and m >= 11 and Jp >= 3, "hard-least-bounds", p, nu, m, Jp)

    bad_factors = prime_factors_three_mod_four(p + 1)
    if bad_factors:
        counts["endpoint_available_primes"] += 1
        ell = min(bad_factors)
        a = (p + ell) // 4
        R = ell
        kappa = (p + 1) // ell
        audit.check((p + ell) % 4 == 0, "endpoint-integral-a", p, ell)
        audit.check(4 * a - p == R and 4 * a > p and 2 * a < p, "endpoint-shell", p, a, R)
        audit.check((4 * a + 1) % R == 0, "endpoint-gate", p, a, R)
        audit.check(ell * ell <= (p + 1) // 2, "endpoint-least-square", p, ell)
        audit.check(
            unit_fraction_identity(p, a, a * kappa, p * a * kappa),
            "endpoint-return",
            p,
            ell,
            a,
            kappa,
        )
    else:
        counts["endpoint_excluded_primes"] += 1

    return nu, m, Jp, hard


def verify_shell(
    p: int,
    a: int,
    nu: int,
    m: int,
    Jp: int,
    hard: bool,
    endpoint_excluded: bool,
    audit: Audit,
    counts: Dict[str, int],
) -> None:
    R = 4 * a - p
    N = p * a
    counts["shells"] += 1
    audit.check(4 * a > p and 2 * a < p, "shell-range", p, a)
    audit.check(3 <= R < p and R % 4 == 3, "residual-range-class", p, a, R)
    audit.check(math.gcd(N, R) == 1, "residual-coprime", p, a, R)

    generated: Dict[Tuple[int, int], int] = {}
    middle_fundamental_expected = 0
    exterior_twice_fundamental_expected = 0

    for u in square_divisors(a):
        counts["square_divisors"] += 1
        d0 = math.gcd(a, u)
        audit.check((d0 * d0) % u == 0, "normalization-h-integral", p, a, u, d0)
        h = d0 * d0 // u
        r = u // d0
        s = a // d0
        audit.check(h > 0 and r > 0 and s > 0, "normalization-positive", p, a, u, h, r, s)
        audit.check(a == h * r * s, "normalization-a", p, a, u, h, r, s)
        audit.check(u == h * r * r, "normalization-u", p, a, u, h, r, s)
        audit.check(math.gcd(r, s) == 1, "normalization-coprime", p, a, u, r, s)
        audit.check(h in divisors(a), "normalization-h-divides-a", p, a, u, h)

        middle_gate = (4 * u + p) % R == 0
        middle_parameter_gate = (r + s) % R == 0
        audit.check(middle_gate == middle_parameter_gate, "middle-gate-equivalence", p, a, u, R)
        if middle_gate:
            counts["middle_states_oriented"] += 1
            audit.check(r != s, "middle-no-diagonal", p, a, u, h, r, s)
            lam = (r + s) // R
            audit.check(lam > 0 and R * lam == r + s, "middle-lambda", p, a, u, lam)
            x = a
            y = p * h * s * lam
            z = p * h * r * lam
            audit.check(unit_fraction_identity(p, x, y, z), "middle-return", p, a, u, y, z)
            inverse_denominator = R * y - p * a
            audit.check(
                inverse_denominator > 0
                and (p * a * a) % inverse_denominator == 0
                and p * a * a // inverse_denominator == u,
                "middle-denominator-inverse",
                p,
                a,
                u,
                y,
            )

            for fibre_d in divisors(h):
                for epsilon in (0, 1):
                    scale = p**epsilon * fibre_d
                    pair = (scale * r, scale * s)
                    audit.check(N % pair[0] == 0 and N % pair[1] == 0, "middle-fibre-divisors", p, a, u, pair)
                    audit.check((pair[0] + pair[1]) % R == 0, "middle-fibre-gate", p, a, u, pair)
                    add_generated_pair(generated, pair)

            if r < s:
                counts["middle_states_ordered"] += 1
                middle_fundamental_expected += len(divisors(h))
                j = h * r * lam
                Q = 4 * j - 1
                audit.check(Q * s == p * lam + r, "middle-Qs", p, a, u, j, Q)
                audit.check(Q * R == p + 4 * h * r * r, "middle-QR", p, a, u, j, Q)
                audit.check(0 < Q < p and Q % 4 == 3, "middle-Q-range", p, a, u, Q)
                audit.check(jacobi(Q, p) == -1, "middle-Q-nonresidue", p, a, u, Q)
                audit.check(Q >= m and j >= Jp, "middle-Q-minimality", p, a, u, Q, m, j, Jp)
                audit.check(h * r * r < a, "middle-oriented-u-bound", p, a, u, h, r, s)
                for J in range(1, j + 1):
                    lhs = (4 * J - 1) * a
                    rhs = J * (p + J)
                    audit.check(lhs <= rhs, "middle-localization", p, a, u, j, J, lhs, rhs)
                    if lhs == rhs:
                        audit.check(
                            h == 1
                            and lam == 1
                            and r == J
                            and p == (4 * J - 1) * s - J,
                            "middle-equality-classification",
                            p,
                            a,
                            u,
                            h,
                            r,
                            s,
                            lam,
                            J,
                        )
                if hard:
                    audit.check(11 * a <= 3 * (p + 3), "middle-hard-a", p, a, u)
                    audit.check(11 * R <= p + 36, "middle-hard-R", p, a, u, R)

        exterior_gate = (4 * u + 1) % R == 0
        exterior_parameter_gate = (p * r + s) % R == 0
        audit.check(exterior_gate == exterior_parameter_gate, "exterior-gate-equivalence", p, a, u, R)
        if exterior_gate:
            counts["exterior_states"] += 1
            kappa = (p * r + s) // R
            x = a
            y = h * s * kappa
            z = p * h * r * kappa
            audit.check(kappa > r, "exterior-kappa", p, a, u, h, r, s, kappa)
            audit.check(unit_fraction_identity(p, x, y, z), "exterior-return", p, a, u, y, z)
            inverse_denominator = R * y - p * a
            audit.check(
                inverse_denominator > 0
                and (a * a) % inverse_denominator == 0
                and a * a // inverse_denominator == u,
                "exterior-denominator-inverse",
                p,
                a,
                u,
                y,
            )

            for fibre_d in divisors(h):
                pair_one = (p * fibre_d * r, fibre_d * s)
                pair_two = (fibre_d * s, p * fibre_d * r)
                for pair in (pair_one, pair_two):
                    audit.check(N % pair[0] == 0 and N % pair[1] == 0, "exterior-fibre-divisors", p, a, u, pair)
                    audit.check((pair[0] + pair[1]) % R == 0, "exterior-fibre-gate", p, a, u, pair)
                    add_generated_pair(generated, pair)

            tau_h = len(divisors(h))
            audit.check(tau_h % 2 == 0, "exterior-h-nonsquare-tau", p, a, u, h, tau_h)
            exterior_twice_fundamental_expected += tau_h

            audit.check(jacobi(u, R) == jacobi(u, p) == -1, "exterior-reciprocity", p, a, u, R)
            audit.check(jacobi(h, p) == -1 and h >= nu, "exterior-h-nonresidue", p, a, u, h, nu)

            delta = kappa - r
            D = (4 * u + 1) // R
            H = h * delta * delta
            audit.check((r + kappa) % s == 0 and D == (r + kappa) // s, "exterior-D", p, a, u, D)
            audit.check(D % 4 == 3, "exterior-D-class", p, a, u, D)
            audit.check((H + 1) % D == 0, "exterior-b-integral", p, a, u, H, D)
            b = (H + 1) // D
            g = p - 2 * a
            audit.check(s * D == 2 * r + delta, "exterior-sD", p, a, u, s, D, r, delta)
            audit.check(b * D == H + 1, "exterior-bD", p, a, u, b, D, H)
            audit.check(p == h * s * s * D - b, "exterior-p-coordinate", p, a, u, b, D)
            audit.check(g == h * s * delta - b, "exterior-g-coordinate", p, a, u, g, b, delta)
            audit.check(
                p * b * H == 2 * g * b * H + g * g * H + (g + b) * (g + b),
                "exterior-master-identity",
                p,
                a,
                u,
                g,
                b,
                H,
            )

            general_lhs = 2 * nu * (p + 1)
            general_rhs = (2 * nu + 1) * (g + 1) * (g + 1)
            audit.check(general_lhs <= general_rhs, "exterior-gap", p, a, u, nu, g)
            if general_lhs == general_rhs:
                audit.check(
                    b == 1 and h == 2 * nu and delta == 1 and D == 2 * nu + 1,
                    "exterior-gap-equality",
                    p,
                    a,
                    u,
                    b,
                    h,
                    delta,
                    D,
                )

            if 3 * a <= p:
                audit.check((g + 1) * (g + 1) > p + 1, "exterior-small-a-stronger", p, a, u, g)
            else:
                audit.check(
                    (3 * a - p) * (r + kappa)
                    == s * (h * r * (3 * r - kappa) + 1),
                    "exterior-3a-p-identity",
                    p,
                    a,
                    u,
                    kappa,
                )
                audit.check(kappa < 3 * r, "exterior-kappa-upper", p, a, u, kappa, r)
                audit.check(
                    D * (g - b) == h * delta * (2 * r - delta) - 2,
                    "exterior-g-minus-b",
                    p,
                    a,
                    u,
                    g,
                    b,
                )
                audit.check(1 <= b < g, "exterior-b-range", p, a, u, b, g)
                audit.check((b - H) % 2 == 1, "exterior-parity", p, a, u, b, H)
                if b % 2 == 1:
                    audit.check(H >= 2 * nu, "exterior-odd-b-H", p, a, u, b, H, nu)
                    f1_numerator = 2 * nu * (2 * g + g * g) + (g + 1) * (g + 1)
                    audit.check(2 * nu * p <= f1_numerator, "exterior-F1", p, a, u, g, nu)
                else:
                    audit.check(b >= 2 and H >= nu, "exterior-even-b-H", p, a, u, b, H, nu)
                    f2_numerator = 4 * nu * g + nu * g * g + (g + 2) * (g + 2)
                    audit.check(2 * nu * p <= f2_numerator, "exterior-F2", p, a, u, g, nu)
                audit.check(nu * g * g - 2 * g - 3 > 0, "exterior-F1-greater-F2", p, a, u, g, nu)

            if endpoint_excluded:
                strict_lhs = 2 * nu * (p + 2)
                strict_rhs = (nu + 1) * (g + 2) * (g + 2)
                audit.check(strict_lhs < strict_rhs, "exterior-strict-gap", p, a, u, nu, g)
                counts["endpoint_excluded_exterior_states"] += 1

            reciprocal_numerator = (p + R) * (p + R) + 4 * nu
            reciprocal_denominator = 4 * nu * R
            audit.check(D * reciprocal_denominator <= reciprocal_numerator, "exterior-D-bound-R", p, a, u, D)
            shell_numerator = (p + 3) * (p + 3) + 4 * nu
            shell_denominator = 12 * nu
            audit.check(D <= shell_numerator // shell_denominator, "exterior-D-bound-shell", p, a, u, D)
            if hard:
                audit.check(22 * (p + 1) <= 23 * (g + 1) * (g + 1), "exterior-hard-gap", p, a, u, g)
                audit.check(D <= ((p + 3) * (p + 3) + 44) // 132, "exterior-hard-D", p, a, u, D)
                if endpoint_excluded:
                    audit.check(11 * (p + 2) < 6 * (g + 2) * (g + 2), "exterior-hard-strict-gap", p, a, u, g)

    pair_set = {
        (b, c)
        for b in divisors(N)
        for c in divisors(N)
        if (b + c) % R == 0
    }
    counts["target_pairs"] += len(pair_set)
    audit.check(len(pair_set) % 4 == 0, "fourfold-cardinality", p, a, R, len(pair_set))
    audit.check(set(generated) == pair_set, "raw-fibres-cover-pairs", p, a, R, len(generated), len(pair_set))
    audit.check(all(multiplicity == 1 for multiplicity in generated.values()), "raw-fibres-unique", p, a, R)

    unseen = set(pair_set)
    representatives: List[Tuple[int, int]] = []
    while unseen:
        b, c = min(unseen)
        orbit = {
            (b, c),
            (c, b),
            (N // b, N // c),
            (N // c, N // b),
        }
        audit.check(len(orbit) == 4, "fourfold-free", p, a, R, b, c)
        audit.check(orbit <= pair_set, "fourfold-invariant", p, a, R, b, c)
        fundamental = [pair for pair in orbit if pair[0] < pair[1] and pair[0] * pair[1] < N]
        audit.check(len(fundamental) == 1, "fourfold-fundamental-unique", p, a, R, b, c, fundamental)
        representatives.append(fundamental[0])
        unseen.difference_update(orbit)

    middle_fundamental = 0
    exterior_fundamental = 0
    for b, c in sorted(representatives):
        audit.check(b * b < N and b < p and a % b == 0, "fundamental-small-divisor", p, a, R, b, c)
        k = (b + c) // R
        audit.check(k > 0 and R * k == b + c, "fundamental-k", p, a, R, b, c, k)
        audit.check((N * k) % b == 0 and (N * k) % c == 0, "fundamental-return-integral", p, a, R, b, c)
        y = N * k // b
        z = N * k // c
        audit.check(unit_fraction_identity(p, a, y, z), "fundamental-return", p, a, R, b, c, y, z)
        if c % p == 0:
            exterior_fundamental += 1
            d = c // p
            audit.check(a % d == 0 and b * d < a and (b + p * d) % R == 0, "fundamental-E-class", p, a, R, b, d)
        else:
            middle_fundamental += 1
            audit.check(a % c == 0 and (b + c) % R == 0, "fundamental-M-class", p, a, R, b, c)

    counts["fourfold_orbits"] += len(representatives)
    audit.check(len(pair_set) == 4 * (middle_fundamental + exterior_fundamental), "fundamental-decomposition", p, a, R)
    audit.check(middle_fundamental == middle_fundamental_expected, "middle-fundamental-fibres", p, a, R, middle_fundamental, middle_fundamental_expected)
    audit.check(2 * exterior_fundamental == exterior_twice_fundamental_expected, "exterior-fundamental-fibres", p, a, R, exterior_fundamental, exterior_twice_fundamental_expected)


def verify_coordinate_example(
    audit: Audit,
    channel: str,
    p: int,
    a: int,
    R: int,
    u: int,
    h: int,
    r: int,
    s: int,
    quotient: int,
    expected_denominators: Tuple[int, int, int],
) -> Dict[str, object]:
    audit.check(is_prime(p) and p % 8 == 1, "example-prime", channel, p)
    audit.check(R == 4 * a - p and 4 * a > p and 2 * a < p, "example-shell", channel, p, a, R)
    audit.check(a == h * r * s and u == h * r * r and math.gcd(r, s) == 1, "example-normalization", channel, p, a, u, h, r, s)
    if channel == "M":
        audit.check(R * quotient == r + s and (4 * u + p) % R == 0, "example-M-gate", p, a, u, quotient)
        denominators = (a, p * h * s * quotient, p * h * r * quotient)
    elif channel == "E":
        audit.check(R * quotient == p * r + s and (4 * u + 1) % R == 0, "example-E-gate", p, a, u, quotient)
        denominators = (a, h * s * quotient, p * h * r * quotient)
    else:
        raise ValueError(f"unknown channel {channel}")
    audit.check(denominators == expected_denominators, "example-denominators", channel, p, denominators, expected_denominators)
    audit.check(unit_fraction_identity(p, *denominators), "example-unit-fraction", channel, p, denominators)
    return {
        "channel": channel,
        "p": p,
        "a": a,
        "R": R,
        "u": u,
        "h": h,
        "r": r,
        "s": s,
        "quotient": quotient,
        "denominators": list(denominators),
    }


def verify_fixed_examples(audit: Audit) -> Dict[str, object]:
    examples = []
    examples.append(
        verify_coordinate_example(
            audit, "E", 41, 18, 31, 54, 6, 3, 1, 4, (18, 24, 2952)
        )
    )
    nu_41 = least_nonresidue(41)
    audit.check(nu_41 == 3, "example-41-nu", nu_41)
    audit.check(2 * nu_41 * 42 == (2 * nu_41 + 1) * 6 * 6, "example-41-gap-equality")

    examples.append(
        verify_coordinate_example(
            audit,
            "M",
            1009,
            276,
            95,
            9,
            1,
            3,
            92,
            1,
            (276, 92828, 3027),
        )
    )
    nu_1009 = least_nonresidue(1009)
    m_1009 = least_three_mod_four_nonresidue(1009)
    audit.check((nu_1009, m_1009, (m_1009 + 1) // 4) == (11, 11, 3), "example-1009-least", nu_1009, m_1009)
    audit.check(all(jacobi(q, 1009) == 1 for q in (2, 3, 5, 7)), "example-1009-hard")
    audit.check(11 * 276 == 3 * (1009 + 3), "example-1009-middle-equality")
    audit.check(11 * 95 == 1009 + 36, "example-1009-middle-residual-equality")

    examples.append(
        verify_coordinate_example(
            audit,
            "E",
            1009,
            253,
            3,
            5819,
            11,
            23,
            1,
            7736,
            (253, 85096, 1974822872),
        )
    )
    D_1009 = (4 * 5819 + 1) // 3
    audit.check(D_1009 == 7759, "example-1009-D", D_1009)
    audit.check(132 * D_1009 == (1009 + 3) ** 2 + 44, "example-1009-D-equality", D_1009)
    g_1009 = 1009 - 2 * 253
    audit.check(not prime_factors_three_mod_four(1010), "example-1009-endpoint-excluded")
    audit.check(11 * (1009 + 2) < 6 * (g_1009 + 2) ** 2, "example-1009-hard-strict-gap", g_1009)

    examples.append(
        verify_coordinate_example(
            audit,
            "M",
            2521,
            636,
            23,
            8,
            2,
            2,
            159,
            7,
            (636, 5611746, 70588),
        )
    )
    nu_2521 = least_nonresidue(2521)
    m_2521 = least_three_mod_four_nonresidue(2521)
    audit.check((nu_2521, m_2521, (m_2521 + 1) // 4) == (11, 11, 3), "example-2521-least", nu_2521, m_2521)
    audit.check(all(jacobi(q, 2521) == 1 for q in (2, 3, 5, 7)), "example-2521-hard")
    audit.check(4 * (2 * 2 * 7) - 1 == 111, "example-2521-Q")

    target = 2521 * 2521 + 44
    audit.check(target == 6355485, "factor-control-target", target)
    audit.check(target == 3 * 3 * 5 * 141233, "factor-control-decomposition", target)
    trial_limit = math.isqrt(141233)
    audit.check(trial_limit == 375, "factor-control-limit", trial_limit)
    trial_divisors = [q for q in range(2, trial_limit + 1) if 141233 % q == 0]
    audit.check(not trial_divisors and is_prime(141233), "factor-control-prime", trial_divisors)
    small_divisors = [d for d in divisors(target) if d < 2521]
    audit.check(small_divisors == [1, 3, 5, 9, 15, 45], "factor-control-small-divisors", small_divisors)
    audit.check(2521 % 44 == 13 and all(d % 44 != 31 for d in small_divisors), "factor-control-E-lane", small_divisors)

    triples = [(3, 1, 1), (1, 3, 1), (1, 1, 3)]
    remainders = [(2521 * lam + r) % 11 for h, r, lam in triples]
    audit.check(remainders == [3, 5, 7], "factor-control-M-lane", remainders)

    n = 25
    a = 7
    R = 3
    restricted = sorted({n**epsilon * d for epsilon in (0, 1) for d in divisors(a)})
    audit.check(restricted == [1, 7, 25, 175], "odd-square-restricted-source", restricted)
    audit.check(
        not any((b + c) % R == 0 for b in restricted for c in restricted),
        "odd-square-no-restricted-pair",
        restricted,
    )
    audit.check(5 in divisors(n * a) and 5 not in restricted, "odd-square-missing-divisor", restricted)
    audit.check(unit_fraction_identity(25, 7, 350, 70), "odd-square-full-return")

    audit.reject(
        unit_fraction_identity(1009, 276, 92829, 3027),
        "mutated-middle-denominator",
        "changing 92828 to 92829 must destroy the p=1009 identity",
    )
    audit.reject(
        target % 31 == 0,
        "fake-p2521-minimal-exterior-residual",
        "R=31 has the required congruence class but does not divide p^2+44",
    )
    audit.reject(
        any((b + c) % 3 == 0 for b in restricted for c in restricted),
        "fake-odd-square-two-colour-target",
        "the restricted n=25 two-colour source has no opposite pair",
    )
    audit.reject(
        is_prime(3 * 141233),
        "composite-primality-control",
        "the primality checker must reject an explicit multiple of 141233",
    )

    return {
        "coordinate_examples": examples,
        "p2521_factorization": {
            "integer": target,
            "factors": [[3, 2], [5, 1], [141233, 1]],
            "trial_division_through": trial_limit,
            "divisors_below_p": small_divisors,
            "middle_lane_remainders": remainders,
        },
        "odd_square_control": {
            "n": 25,
            "a": 7,
            "R": 3,
            "two_colour_source": restricted,
            "full_pair": [1, 5],
            "denominators": [7, 350, 70],
        },
    }


def run(bound: int) -> Dict[str, object]:
    if bound < 2:
        raise ValueError("--bound must be at least 2")
    audit = Audit()
    counts: Dict[str, int] = {
        "primes_1_mod_8": 0,
        "hard_primes": 0,
        "endpoint_available_primes": 0,
        "endpoint_excluded_primes": 0,
        "shells": 0,
        "square_divisors": 0,
        "middle_states_oriented": 0,
        "middle_states_ordered": 0,
        "exterior_states": 0,
        "endpoint_excluded_exterior_states": 0,
        "target_pairs": 0,
        "fourfold_orbits": 0,
    }

    for p in primes_up_to(bound):
        if p % 8 != 1:
            continue
        counts["primes_1_mod_8"] += 1
        nu, m, Jp, hard = verify_prime_invariants(p, audit, counts)
        endpoint_excluded = not prime_factors_three_mod_four(p + 1)
        for a in range(p // 4 + 1, (p - 1) // 2 + 1):
            if 4 * a > p and 2 * a < p:
                verify_shell(
                    p,
                    a,
                    nu,
                    m,
                    Jp,
                    hard,
                    endpoint_excluded,
                    audit,
                    counts,
                )

    examples = verify_fixed_examples(audit)
    return {
        "schema": "es.turn06b.pointwise-localization.verification.v1",
        "status": "verified",
        "bound": bound,
        "checks": audit.checks,
        "counts": counts,
        "digest_algorithm": "sha256",
        "verification_digest": audit.hexdigest(),
        "negative_controls": audit.negative_controls,
        "examples": examples,
        "scope": {
            "prime_scan": "every prime p congruent to 1 modulo 8 through bound",
            "shell_scan": "every integer p/4<a<p/2",
            "source_scan": "every divisor u of a^2",
            "pair_scan": "every ordered divisor pair of pa satisfying R|(b+c)",
            "nonclaim": "finite enumeration does not prove universal ES occupancy",
        },
    }


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bound", type=int, default=1000)
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("localization_verification.json"),
        help="deterministic JSON receipt path",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    receipt = run(args.bound)
    rendered = json.dumps(receipt, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(rendered, encoding="utf-8", newline="\n")
    sys.stdout.write(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
