#!/usr/bin/env python3
"""Independent exact replay for Continuation B, Tracks I and IV.

This checker reconstructs the displayed integer identities, enumerates the
five stated finite witness sets, counts the CRT classes, and verifies the
complete F_61 signed-cover example, including the original Fable polynomial
over F_61[w]/(w^2-2).
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path

import sympy as sp


class Checks:
    def __init__(self) -> None:
        self.count = 0

    def require(self, condition: bool, label: str) -> None:
        self.count += 1
        if not condition:
            raise AssertionError(label)


def vp(n: int, p: int) -> int:
    if n == 0:
        raise ValueError("the p-adic valuation of zero is not finite")
    n = abs(n)
    out = 0
    while n % p == 0:
        out += 1
        n //= p
    return out


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    value = pow(a, (p - 1) // 2, p)
    return -1 if value == p - 1 else value


def integer_N(p: int, x: int, y: int, z: int) -> int:
    S = p + x + y + z
    e2 = p * (x + y + z) + x * y + x * z + y * z
    e3 = 5 * x * y * z
    e4 = p * x * y * z
    return (
        60 * S**5 * e3
        - 20 * S**4 * e2**2
        - 51 * S**4 * e4
        - 282 * S**3 * e2 * e3
        + 87 * S**2 * e2**3
        + 204 * S**2 * e2 * e4
        + 431 * S**2 * e3**2
        + 22 * S * e2**2 * e3
        - 856 * S * e3 * e4
        - 28 * e2**4
        + 224 * e2**2 * e4
        - 168 * e2 * e3**2
        - 448 * e4**2
    )


def enumerate_sorted_witnesses(p: int) -> list[tuple[int, int, int]]:
    """Complete factor enumeration from (Rb-pa)(Rc-pa)=(pa)^2."""
    found: set[tuple[int, int, int]] = set()
    for a in range(p // 4 + 1, (3 * p) // 4 + 1):
        R = 4 * a - p
        target = (p * a) ** 2
        for u in sp.divisors(target):
            if u > p * a:
                break
            v = target // u
            if (u + p * a) % R or (v + p * a) % R:
                continue
            b = (u + p * a) // R
            c = (v + p * a) // R
            if a <= b <= c and 4 * a * b * c == p * (a * b + a * c + b * c):
                found.add((a, b, c))
    return sorted(found)


def symbolic_track_i(C: Checks) -> None:
    S, e2, e3, e4 = sp.symbols("S e2 e3 e4", nonzero=True)
    A, B, Cc, D = -1 / S, -e2 / S, e3 / S, -e4 / S
    F = (
        20 * (3 * Cc - B**2)
        + A * (87 * B**3 - 282 * B * Cc - 51 * D)
        + A**2 * (-28 * B**4 + 22 * B**2 * Cc + 431 * Cc**2 + 204 * B * D)
        + A**3 * (224 * B**2 * D - 168 * B * Cc**2 - 856 * Cc * D)
        - 448 * A**4 * D**2
    )
    N = (
        60 * S**5 * e3
        - 20 * S**4 * e2**2
        - 51 * S**4 * e4
        - 282 * S**3 * e2 * e3
        + 87 * S**2 * e2**3
        + 204 * S**2 * e2 * e4
        + 431 * S**2 * e3**2
        + 22 * S * e2**2 * e3
        - 856 * S * e3 * e4
        - 28 * e2**4
        + 224 * e2**2 * e4
        - 168 * e2 * e3**2
        - 448 * e4**2
    )
    C.require(sp.simplify(S**6 * F - N) == 0, "E1 from the receiving divisor")

    x, y = sp.symbols("x y", nonzero=True)
    type_i = sp.factor(N.subs({S: x + y, e2: x * y, e3: 0, e4: 0}))
    expected_i = -x**2 * y**2 * (x - y) ** 2 * (20 * x**2 + 33 * x * y + 20 * y**2)
    C.require(sp.expand(type_i - expected_i) == 0, "E2 Type-I reduction")
    C.require(sp.discriminant(20 * x**2 + 33 * x + 20, x) == -511, "E2 discriminant")

    p, w = sp.symbols("p w")
    y_diag = x + p * w
    T0 = 4 * x * y_diag - p * (x + y_diag)
    z_diag = p * x * y_diag / T0
    S_diag = p + x + y_diag + z_diag
    e2_diag = p * (x + y_diag + z_diag) + x * y_diag + x * z_diag + y_diag * z_diag
    e3_diag = 5 * x * y_diag * z_diag
    e4_diag = p * x * y_diag * z_diag
    N_diag = sp.cancel(N.subs({S: S_diag, e2: e2_diag, e3: e3_diag, e4: e4_diag}))
    coeff2 = sp.simplify(sp.diff(N_diag, p, 2).subs(p, 0) / 2)
    expected_coeff2 = x**6 * (sp.Rational(153, 16) - 73 * w**2)
    C.require(sp.simplify(coeff2 - expected_coeff2) == 0, "E3 diagonal p^2 coefficient")

    cleared = sp.cancel(N_diag * T0**6)
    num, den = sp.fraction(cleared)
    C.require(den == 1, "E3 cleared expression is integral polynomial")
    cleared_coeff2 = sp.Poly(sp.expand(num), p).coeff_monomial(p**2)
    C.require(
        sp.expand(cleared_coeff2 + 256 * x**18 * (1168 * w**2 - 153)) == 0,
        "E3 cleared p^2 coefficient",
    )
    C.require(153 * 1168 == 12**2 * 1241, "E3 square-class identity")

    X, Y, Z, t = sp.symbols("X Y Z t", nonzero=True)
    S_ii = p + p * X + p * Y + Z
    e2_ii = p * (p * X + p * Y + Z) + p**2 * X * Y + p * X * Z + p * Y * Z
    e3_ii = 5 * p**2 * X * Y * Z
    e4_ii = p**3 * X * Y * Z
    N_ii = sp.expand(N.subs({S: S_ii, e2: e2_ii, e3: e3_ii, e4: e4_ii}))
    ii_coeff2 = sp.Poly(N_ii, p).coeff_monomial(p**2)
    expected_ii = 20 * Z**6 * (15 * X * Y - (1 + X + Y) ** 2)
    C.require(sp.expand(ii_coeff2 - expected_ii) == 0, "E4 Type-II p^2 coefficient")
    reduced_ii = sp.expand(expected_ii.subs({X * Y: t / 4, X + Y: t}))
    # SymPy does not replace X+Y after expansion, so perform the symmetric reduction directly.
    reduced_ii = 20 * Z**6 * (15 * t / 4 - (1 + t) ** 2)
    C.require(sp.expand(reduced_ii + 5 * Z**6 * (4 * t**2 - 7 * t + 4)) == 0, "E4 symmetric reduction")
    C.require(sp.discriminant(4 * t**2 - 7 * t + 4, t) == -15, "E4 discriminant")

    S_formal = p + p**2 * X + p**2 * Y + Z
    e2_formal = p * (p**2 * X + p**2 * Y + Z) + p**4 * X * Y + p**2 * X * Z + p**2 * Y * Z
    e3_formal = 5 * p**4 * X * Y * Z
    e4_formal = p**5 * X * Y * Z
    N_formal = sp.expand(N.subs({S: S_formal, e2: e2_formal, e3: e3_formal, e4: e4_formal}))
    C.require(sp.Poly(N_formal, p).coeff_monomial(p**2) == -20 * Z**6, "E5 formal branch")


def finite_track_i(C: Checks) -> dict[str, object]:
    modulus = 521220
    classes = []
    for a in range(modulus):
        if math.gcd(a, modulus) != 1 or a % 12 != 1:
            continue
        # Here ``a`` is a residue class modulo the composite CRT modulus,
        # not a prime.  Test the reciprocity conditions (E7) at their prime
        # coordinates; a Legendre symbol with composite denominator ``a``
        # would not test (E6).
        chi_7 = legendre(a % 7, 7)
        chi_73 = legendre(a % 73, 73)
        chi_17 = legendre(a % 17, 17)
        chi_5 = legendre(a % 5, 5)
        if chi_7 * chi_73 == -1 and chi_17 * chi_73 == -1 and chi_5 == -1:
            classes.append(a)
    C.require(len(classes) == 3456, "CRT class count")
    C.require(len(set(classes)) == 3456, "CRT classes are distinct")

    primes = [97, 397, 613, 853, 997]
    expected_counts = [8, 29, 44, 34, 48]
    witness_rows: dict[str, object] = {}
    total = 0
    for p, expected in zip(primes, expected_counts):
        C.require(sp.isprime(p), f"{p} is prime")
        C.require(p % 12 == 1, f"{p} is 1 mod 12")
        symbols = [legendre(-511, p), legendre(1241, p), legendre(-15, p)]
        C.require(symbols == [-1, -1, -1], f"{p} character triple")
        rows = enumerate_sorted_witnesses(p)
        C.require(len(rows) == expected, f"{p} witness count")
        row_data = []
        for triple in rows:
            x, y, z = triple
            C.require(len({p, x, y, z}) == 4, f"{p},{triple} distinct roots")
            divisible = [v % p == 0 for v in triple]
            count = sum(divisible)
            C.require(count in (1, 2), f"{p},{triple} one or two p-divisible denominators")
            for value, flag in zip(triple, divisible):
                if flag:
                    C.require(vp(value, p) == 1, f"{p},{triple} exact denominator valuation")
            value_N = integer_N(p, x, y, z)
            C.require(value_N != 0, f"{p},{triple} N nonzero")
            value_v = vp(value_N, p)
            if count == 1:
                units = [value for value in triple if value % p]
                expected_v = 2 if units[0] % p == units[1] % p else 0
            else:
                expected_v = 2
            C.require(value_v == expected_v, f"{p},{triple} predicted N valuation")
            row_data.append({"denominators": list(triple), "v_p_N": value_v})
        witness_rows[str(p)] = row_data
        total += len(rows)
    C.require(total == 163, "five-prime witness total")
    return {"modulus": modulus, "residue_classes": classes, "witnesses": witness_rows, "witness_total": total}


@dataclass(frozen=True)
class Fq2:
    a: int
    b: int


Q = 61
NON_SQUARE = 2


def fadd(x: Fq2, y: Fq2) -> Fq2:
    return Fq2((x.a + y.a) % Q, (x.b + y.b) % Q)


def fneg(x: Fq2) -> Fq2:
    return Fq2(-x.a % Q, -x.b % Q)


def fsub(x: Fq2, y: Fq2) -> Fq2:
    return fadd(x, fneg(y))


def fmul(x: Fq2, y: Fq2) -> Fq2:
    return Fq2((x.a * y.a + NON_SQUARE * x.b * y.b) % Q, (x.a * y.b + x.b * y.a) % Q)


def fpow(x: Fq2, n: int) -> Fq2:
    out = Fq2(1, 0)
    base = x
    while n:
        if n & 1:
            out = fmul(out, base)
        base = fmul(base, base)
        n //= 2
    return out


def finv(x: Fq2) -> Fq2:
    norm = (x.a * x.a - NON_SQUARE * x.b * x.b) % Q
    if norm == 0:
        raise ZeroDivisionError
    inv_norm = pow(norm, -1, Q)
    return Fq2(x.a * inv_norm % Q, -x.b * inv_norm % Q)


def fbase(n: int) -> Fq2:
    return Fq2(n % Q, 0)


def fscale(n: int, x: Fq2) -> Fq2:
    return Fq2(n * x.a % Q, n * x.b % Q)


def fable_forward(a: Fq2, y: Fq2, z: Fq2, w: Fq2, i: Fq2) -> tuple[Fq2, Fq2, Fq2, Fq2]:
    a2, a3 = fmul(a, a), fpow(a, 3)
    y2, y3, y4, y5 = fpow(y, 2), fpow(y, 3), fpow(y, 4), fpow(y, 5)
    P0 = fsub(fadd(fmul(a3, z), fscale(2, fmul(a2, y))), fmul(i, a))
    P2 = fadd(
        fadd(
            fadd(fneg(fmul(fmul(a3, y2), z)), fscale(-2, fmul(i, fmul(fmul(a2, y), z)))),
            fmul(a2, w),
        ),
        fadd(
            fadd(fscale(-2, fmul(a2, y3)), fscale(-10, fmul(i, fmul(a, y2)))),
            fadd(fscale(3, fmul(a, z)), y),
        ),
    )
    P3 = fadd(
        fadd(
            fadd(fscale(2, fmul(fmul(a3, y3), z)), fscale(6, fmul(i, fmul(fmul(a2, y2), z)))),
            fscale(2, fmul(fmul(a2, w), y)),
        ),
        fadd(
            fadd(fscale(4, fmul(a2, y4)), fscale(2, fmul(i, fmul(a, w)))),
            fadd(
                fadd(fscale(-4, fmul(i, fmul(a, y3))), fscale(-2, fmul(fmul(a, y), z))),
                fadd(fscale(2, fmul(i, z)), fscale(7, y2)),
            ),
        ),
    )
    P4 = fadd(
        fadd(
            fadd(fscale(2, fmul(fmul(a3, y4), z)), fscale(8, fmul(i, fmul(fmul(a2, y3), z)))),
            fmul(fmul(a2, w), y2),
        ),
        fadd(
            fadd(fscale(4, fmul(a2, y5)), fscale(2, fmul(i, fmul(fmul(a, w), y)))),
            fadd(
                fadd(fscale(7, fmul(i, fmul(a, y4))), fscale(-10, fmul(fmul(a, y2), z))),
                fadd(fadd(fscale(-4, fmul(i, fmul(y, z))), fneg(w)), fscale(-3, y3)),
            ),
        ),
    )
    return P0, P2, P3, P4


def finite_track_iv(C: Checks) -> dict[str, object]:
    p, x, y, z = 13, 4, 18, 468
    C.require(4 * x * y * z == p * (x * y + x * z + y * z), "F4 witness identity")
    S = p + x + y + z
    roots_original = [p, x, y, z]
    delta = math.prod(roots_original[j] - roots_original[i] for i in range(4) for j in range(i))
    C.require((2 * S * delta) % Q != 0, "F1 good reduction at 61")

    r = sp.symbols("r")
    A = (-pow(S, -1, Q)) % Q
    poly = sp.Poly(A * sp.prod(r - (root % Q) for root in roots_original), r, modulus=Q)
    coeffs = [int(c) % Q for c in poly.all_coeffs()]
    C.require(coeffs == [4, 1, 35, 8, 28], "F4 normalized quartic")

    roots = [4, 13, 18, 41]
    derivative = sp.diff(poly.as_expr(), r)
    derivatives = [int(derivative.subs(r, root)) % Q for root in roots]
    C.require(derivatives == [18, 38, 26, 30], "F5 derivative values")
    C.require(all(legendre(value, Q) == -1 for value in derivatives), "F6 all derivatives nonsquare")
    C.require(legendre(2, Q) == -1, "twist factor 2 nonsquare")
    b_values = [6, 25, 28, 11]
    C.require([b * b % Q for b in b_values] == [(2 * d) % Q for d in derivatives], "twist square roots")

    original_count = sum(1 + legendre(d, Q) for d in derivatives)
    twist_count = sum(1 + legendre(2 * d, Q) for d in derivatives)
    C.require(original_count == 0 and twist_count == 8, "F2--F3 complementary counts")

    i = fbase(11)
    C.require(fmul(i, i) == fbase(-1), "chosen square root of -1")
    w_ext = Fq2(0, 1)
    C.require(fmul(w_ext, w_ext) == fbase(2), "quadratic extension generator")
    C.require(fpow(w_ext, Q) == fneg(w_ext), "Frobenius sends w to -w")
    inv2 = pow(2, -1, Q)
    point_records = []
    target = tuple(fbase(value) for value in [4, 35, 8, 28])
    for root, deriv, b_value in zip(roots, derivatives, b_values):
        eta0 = Fq2(0, b_value * inv2 % Q)
        C.require(fmul(eta0, eta0) == fbase(deriv), f"eta square at root {root}")
        for sign in (1, -1):
            eta = eta0 if sign == 1 else fneg(eta0)
            a = finv(eta)
            yq = fsub(fbase(-root), fmul(i, eta))
            zq = fadd(fadd(fscale(A, fpow(eta, 3)), fscale(2 * root, eta)), fscale(3, fmul(i, fpow(eta, 2))))
            wq = fadd(
                fadd(fscale(7 * root * root, fmul(i, eta)), fscale((35 - 17 * root + A * root * root), fpow(eta, 2))),
                fadd(fscale(-13, fmul(i, fpow(eta, 3))), fscale(-2 * A, fpow(eta, 4))),
            )
            C.require(fable_forward(a, yq, zq, wq, i) == target, f"F8 forward map at root {root}, sign {sign}")
            C.require(fpow(eta, Q) == fneg(eta), f"F9 Frobenius sign exchange at root {root}, sign {sign}")
            point_records.append(
                {
                    "root": root,
                    "sign": sign,
                    "eta": [eta.a, eta.b],
                    "a": [a.a, a.b],
                    "y": [yq.a, yq.b],
                    "z": [zq.a, zq.b],
                    "w": [wq.a, wq.b],
                }
            )
    C.require(len(point_records) == 8, "eight extension points")
    return {
        "prime": Q,
        "quartic_coefficients": coeffs,
        "roots": roots,
        "derivatives": derivatives,
        "original_rational_points": original_count,
        "twist_rational_points": twist_count,
        "extension_points": point_records,
        "frobenius_cycles": 4,
        "point_count_formula": "N_n=0 for odd n and 8 for even n; Z(T)=(1-T^2)^(-4)",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    checks = Checks()
    symbolic_track_i(checks)
    track_i = finite_track_i(checks)
    track_iv = finite_track_iv(checks)
    result = {
        "status": "PASS",
        "exact_checks": checks.count,
        "scope": "Independent replay of Continuation B Tracks I and IV only",
        "track_i": track_i,
        "track_iv": track_iv,
    }
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "exact_checks": checks.count, "witness_total": track_i["witness_total"]}, sort_keys=True))


if __name__ == "__main__":
    main()
