#!/usr/bin/env python3
"""Exact certificates for the defining-prime continuation.

The written proof remains primary.  This script checks the coefficient map,
the full normalization matrices in representative valuation strata, the two
p=1201 witnesses, local nilpotent actions, gluing determinants, the translated
quadratic twist, and the explicit collision family.
"""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


class Checks:
    def __init__(self) -> None:
        self.count = 0

    def require(self, condition: bool, label: str) -> None:
        self.count += 1
        if not condition:
            raise AssertionError(label)


def vp(n: int, p: int) -> int:
    if n == 0:
        raise ValueError("zero has no finite valuation")
    out = 0
    n = abs(int(n))
    while n % p == 0:
        out += 1
        n //= p
    return out


def legendre(a: int, p: int) -> int:
    value = pow(a % p, (p - 1) // 2, p)
    return -1 if value == p - 1 else value


def inclusion_matrix(roots: list[int], p: int) -> tuple[sp.Matrix, list[int], list[int], list[int]]:
    b = [sum(vp(roots[i] - roots[j], p) for j in range(4) if j != i) for i in range(4)]
    m = [value // 2 for value in b]
    epsilon = [value % 2 for value in b]
    V = sp.Matrix([[roots[i] ** j for j in range(4)] for i in range(4)])
    C = sp.diag(V, sp.diag(*[p**value for value in m]) * V)
    return C, b, m, epsilon


def p_smith_exponents(matrix: sp.Matrix, p: int) -> list[int]:
    diagonal = smith_normal_form(matrix, domain=ZZ)
    values = [abs(int(diagonal[i, i])) for i in range(min(diagonal.shape))]
    return sorted(vp(value, p) if value else 10**9 for value in values)


def coefficient_checks(Ck: Checks) -> None:
    A, P, W = sp.symbols("A P W", nonzero=True)
    B = A * W - P - A * P**2
    C = -sp.Rational(5, 4) * A * P * W
    D = sp.Rational(1, 4) * A * P**2 * W
    G = 625 * A * D**3 - 125 * C * D**2 + 25 * B * C**2 * D - 4 * C**4
    Ck.require(sp.expand(G) == 0, "coefficient hypersurface map")
    monic = P**3 + A**-1 * P**2 + (B / A) * P + 4 * C / (5 * A)
    Ck.require(sp.simplify(monic) == 0, "distinguished-root monic equation")
    Ck.require(sp.simplify(D + C * P / 5) == 0, "D=-CP/5")
    Ck.require(sp.simplify(D**2 - C**2 * P**2 / 25) == 0, "D^2=C^2P^2/25")


def general_smith_checks(Ck: Checks) -> dict[str, object]:
    p = 5
    one_rows = []
    for n in range(5):
        roots = [p, 1, 2 if n == 0 else 1 + p**n, 2 * p]
        matrix, b, m, epsilon = inclusion_matrix(roots, p)
        observed = p_smith_exponents(matrix, p)
        expected = sorted([0, 0, 1, 1, 0, n // 2, n, n + n // 2])
        Ck.require(observed == expected, f"one-divisible Smith formula n={n}")
        length = sum(observed)
        Ck.require(length == 2 + 3 * n - (n % 2), f"one-divisible length n={n}")
        Ck.require(length == 3 * sum(vp(roots[i] - roots[j], p) for i in range(4) for j in range(i)) - sum(epsilon) // 2,
                   f"one-divisible discriminant length n={n}")
        one_rows.append({"n": n, "b": b, "m": m, "epsilon": epsilon, "smith": observed})

    two_rows = []
    for n in range(1, 5):
        if n == 1:
            roots = [p, 1, 2 * p, 3 * p]
        else:
            roots = [p, 1, p * (1 + p ** (n - 1)), 2 * p]
        matrix, b, m_values, epsilon = inclusion_matrix(roots, p)
        observed = p_smith_exponents(matrix, p)
        m = (n + 1) // 2
        expected = sorted([0, 0, 0, 1, 1, m + 1, n + 1, n + m + 1])
        Ck.require(observed == expected, f"two-divisible Smith formula n={n}")
        length = sum(observed)
        Ck.require(length == 3 * n + 6 - ((n + 1) % 2), f"two-divisible length n={n}")
        two_rows.append({"n": n, "b": b, "m": m_values, "epsilon": epsilon, "smith": observed})
    return {"one_divisible": one_rows, "two_divisible": two_rows}


def coefficients_mod_p(p: int, roots: list[int]) -> list[int]:
    _, x, y, z = roots
    S = sum(roots)
    A = -pow(S, -1, p) % p
    s1 = x + y + z
    s2 = x * y + x * z + y * z
    s3 = x * y * z
    return [A, A * (p * s1 + s2) % p, -5 * A * s3 % p, A * p * s3 % p]


def witness_checks(Ck: Checks) -> dict[str, object]:
    p = 1201
    examples = [
        ([p, 306, 16218, 1082101], [410, 100, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1]),
        ([p, 306, 21618, 61251], [522, 0, 0, 0], [0, 0, 0, 1, 1, 2, 2, 3]),
    ]
    records = []
    for roots, expected_coeffs, expected_smith in examples:
        _, x, y, z = roots
        Ck.require(4 * x * y * z == p * (x * y + x * z + y * z), f"witness {roots}")
        Ck.require(len(set(roots)) == 4, f"distinct roots {roots}")
        coeffs = coefficients_mod_p(p, roots)
        Ck.require(coeffs == expected_coeffs, f"coefficient vector {roots}")
        matrix, b, m, epsilon = inclusion_matrix(roots, p)
        observed_smith = p_smith_exponents(matrix, p)
        Ck.require(observed_smith == expected_smith, f"Smith vector {roots}")
        Ck.require(sum(observed_smith) == 3 * sum(vp(roots[i] - roots[j], p) for i in range(4) for j in range(i)) - sum(epsilon) // 2,
                   f"trace-discriminant length {roots}")
        records.append({"roots": roots, "coefficients_mod_p": coeffs, "b": b, "m": m, "epsilon": epsilon, "smith": observed_smith})

    first = examples[0][0]
    A1 = expected_a1 = 410
    x1, y1 = first[1] % p, first[2] % p
    local_linear = 2 * A1 * x1 * y1 % p
    Ck.require(local_linear == 200, "exterior local coefficient 200")
    second = examples[1][0]
    A2, x2 = 522, second[1] % p
    local_quadratic = -3 * A2 * x2 % p
    Ck.require(local_quadratic == 3, "middle local coefficient 3")

    x, y, z = 306, 16218, 1082101
    Z = z // p
    D_E = 3
    Ck.require(sp.Rational(x * y, x + y) == sp.Rational(Z, D_E), "exterior cofactor identity")
    S = p + x + y + z
    A_mod = -pow(S, -1, p) % p
    fp_over_p = A_mod * ((p - z) // p) * (p - x) * (p - y) % p
    rhs = -3 * pow(16 * D_E, -1, p) % p
    Ck.require(fp_over_p == rhs, "exterior derivative residue")
    Ck.require(legendre(fp_over_p * pow(D_E, -1, p), p) == 1, "exterior field square ratio")
    return {"prime": p, "examples": records, "exterior_fp_over_p": fp_over_p}


def multiplication_matrix(m: int, coefficient: int = 1) -> tuple[sp.Matrix, sp.Matrix]:
    # basis 1,r,...,r^(m-1),sigma,r sigma,...,r^(m-1) sigma
    size = 2 * m
    Mr = sp.zeros(size)
    Ms = sp.zeros(size)
    for j in range(m - 1):
        Mr[j + 1, j] = 1
        Mr[m + j + 1, m + j] = 1
    for j in range(m):
        Ms[m + j, j] = 1
        exponent = j + m - 1
        if exponent < m:
            Ms[exponent, m + j] = coefficient
    return Mr, Ms


def local_action_checks(Ck: Checks) -> dict[str, object]:
    rows = []
    for m in range(2, 8):
        Mr, Ms = multiplication_matrix(m)
        ranks = [int((Ms**power).rank()) for power in (1, 2, 3)]
        Ck.require(ranks == [m + 1, 2, 1], f"sigma ranks m={m}")
        Ck.require((Ms**4).is_zero_matrix, f"sigma nilpotence m={m}")
        Ck.require(int(Mr.rank()) == 2 * (m - 1), f"r rank m={m}")
        # Kernel-growth differences determine the nilpotent Jordan block sizes.
        nullities = [0] + [2 * m - int((Ms**power).rank()) for power in range(1, 5)]
        blocks_ge = [nullities[k] - nullities[k - 1] for k in range(1, 5)]
        exact = [blocks_ge[k - 1] - (blocks_ge[k] if k < 4 else 0) for k in range(1, 5)]
        expected_exact = [0, m - 2, 0, 1]
        Ck.require(exact == expected_exact, f"sigma Jordan list m={m}")
        rows.append({"m": m, "ranks_sigma_1_2_3": ranks, "blocks_exact_size_1_to_4": exact})
    Mr1, Ms1 = multiplication_matrix(1)
    Ck.require(int(Ms1.det()) != 0, "m=1 sigma is invertible")
    return {"multiplicity_blocks": rows}


def gluing_and_twist_checks(Ck: Checks) -> dict[str, object]:
    P, s1, s3, t = sp.symbols("P s1 s3 t", nonzero=True)
    matrix = sp.Matrix([
        [1, P, P**2, P**3],
        [1, 0, 0, s3],
        [0, 1, 0, -4 * s3 / P],
        [0, 0, 1, s1],
    ])
    R = P**3 - P**2 * s1 + 3 * s3
    Ck.require(sp.simplify(matrix.det() + R) == 0, "CRT determinant -R")

    comparison = sp.Matrix([
        [1, 0, t, 0],
        [0, 1, 0, t],
        [1, 0, -t, 0],
        [0, 1, 0, -t],
    ])
    Ck.require(sp.factor(comparison.det()) == 4 * t**2, "collision normalization determinant")
    at_zero = comparison.subs(t, 0)
    Ck.require(at_zero.rank() == 2, "specialization rank two")
    Ck.require(at_zero.nullspace() == [sp.Matrix([0, 0, 1, 0]), sp.Matrix([0, 0, 0, 1])], "specialization kernel zeta^2,zeta^3")

    lam, T, S = sp.symbols("lambda T S", nonzero=True)
    roots = sp.symbols("t0:4")
    F0 = -sp.prod(T - root for root in roots) / S
    c = S / (S - 4 * lam)
    Fl = -sp.prod(T - (root - lam) for root in roots) / (S - 4 * lam)
    Ck.require(sp.simplify(Fl - c * F0.subs(T, T + lam)) == 0, "translated polynomial twist")
    Ck.require(sp.simplify(sp.diff(Fl, T) - c * sp.diff(F0, T).subs(T, T + lam)) == 0, "translated derivative twist")
    Ck.require(legendre(2, 5) == -1, "nonsquare twist need not descend over Q_5")

    tau = sp.symbols("tau")
    x = P + tau
    y = 2 * P
    z = 2 * P * (P + tau) / (5 * P + 7 * tau)
    Ck.require(sp.simplify(1 / x + 1 / y + 1 / z - 4 / P) == 0, "explicit collision ES family")
    S0 = sp.simplify(P + x + y + z).subs(tau, 0)
    A0 = -1 / S0
    h0 = sp.simplify((P - y) * (P - z.subs(tau, 0)))
    Ck.require(sp.simplify(A0 * h0 - 3 * P / 22) == 0, "explicit H0 factor")
    return {"crt_determinant": "-R", "collision_determinant": "4*t^2", "twist_negative_control": "c=2 is nonsquare in Q_5"}


def galois_example_checks(Ck: Checks) -> dict[str, object]:
    p = 1201
    alpha = [1, 18, 51]
    units = [((a - alpha[(i + 1) % 3]) * (a - alpha[(i + 2) % 3])) % p for i, a in enumerate(alpha)]
    Ck.require(units == [850, 640, 449], "middle normalized units")
    characters = [legendre(value, p) for value in units]
    Ck.require(characters == [-1, 1, -1], "middle unit characters")
    Ck.require(legendre(42, p) == 1, "isolated derivative unit split")
    Ck.require(sum(characters) + 2 == 1, "rank-five Frobenius trace")
    return {"units": units, "characters": characters, "frobenius_polynomial": "(1-T)^3(1+T)^2", "trace": 1}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    checks = Checks()
    coefficient_checks(checks)
    smith = general_smith_checks(checks)
    witnesses = witness_checks(checks)
    actions = local_action_checks(checks)
    gluing = gluing_and_twist_checks(checks)
    galois = galois_example_checks(checks)
    result = {
        "status": "PASS",
        "exact_checks": checks.count,
        "scope": "Executable identities supporting the written defining-prime proofs",
        "smith_strata": smith,
        "witnesses": witnesses,
        "local_actions": actions,
        "gluing_and_twist": gluing,
        "galois_example": galois,
    }
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PASS", "exact_checks": checks.count}, sort_keys=True))


if __name__ == "__main__":
    main()
