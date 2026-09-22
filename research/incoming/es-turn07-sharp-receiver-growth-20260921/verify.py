#!/usr/bin/env python3
"""Exact certificates and high-precision checks for sharp ES receiver growth.

The polynomial stage reconstructs the new inequalities from the defining
integer formulas.  The numerical stage evaluates the literal complex receiver
on two integral prime families.  Numerical SVD data corroborate, but do not
replace, the exact compound-matrix derivations in the accompanying TeX.
"""
from __future__ import annotations

import hashlib
import json
from itertools import combinations, permutations
from pathlib import Path

import mpmath as mp
import sympy as sp


HERE = Path(__file__).resolve().parent
CERT = HERE / "certificates" / "global_sign_polynomials.json"
OUT = HERE / "certificates" / "sharp_growth_verification.json"
EXPECTED_CERT_SHA256 = "3f1a7dc71435d17a74e2c96b3878723f4b40783247ab48467b2029dea26ea730"
CHECKS = 0


def check(condition: bool, label: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise ArithmeticError(label)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def integer_coefficients(expr: sp.Expr, variables: tuple[sp.Symbol, ...]) -> dict[tuple[int, ...], int]:
    poly = sp.Poly(sp.expand(expr), *variables, domain=sp.ZZ)
    return {tuple(m): int(c) for m, c in poly.terms()}


def certificate_coefficients(rows: list[list[object]]) -> dict[tuple[int, ...], int]:
    return {tuple(int(e) for e in exponents): int(coefficient) for exponents, coefficient in rows}


def full_rectangle(coeffs: dict[tuple[int, int], int], imax: int, jmax: int) -> bool:
    return set(coeffs) == {(i, j) for i in range(imax + 1) for j in range(jmax + 1)}


def full_trapezoid(coeffs: dict[tuple[int, int], int], imax: int, jmax: int, total: int) -> bool:
    target = {(i, j) for i in range(imax + 1) for j in range(jmax + 1) if i + j <= total}
    return set(coeffs) == target


def receiving_n(roots: list[sp.Expr]) -> sp.Expr:
    s = sum(roots)
    e2 = sum(roots[i] * roots[j] for i in range(4) for j in range(i + 1, 4))
    e3 = sum(
        roots[i] * roots[j] * roots[k]
        for i in range(4)
        for j in range(i + 1, 4)
        for k in range(j + 1, 4)
    )
    e4 = sp.prod(roots)
    return sp.expand(
        60 * e3 * s**5
        - 20 * e2**2 * s**4
        + 87 * e2**3 * s**2
        - 282 * e2 * e3 * s**3
        - 51 * e4 * s**4
        - 28 * e2**4
        + 22 * e2**2 * e3 * s
        + 431 * e3**2 * s**2
        + 204 * e2 * e4 * s**2
        + 224 * e2**2 * e4
        - 168 * e2 * e3**2
        - 856 * e3 * e4 * s
        - 448 * e4**2
    )


def exact_polynomial_stage() -> dict[str, object]:
    check(CERT.is_file(), "copied global-sign coefficient certificate is present")
    cert_hash = sha256(CERT)
    check(cert_hash == EXPECTED_CERT_SHA256, "global-sign coefficient certificate hash")
    data = json.loads(CERT.read_text(encoding="utf-8"))

    X, Y, u, w = sp.symbols("X Y u w")
    roots_e = [
        16 * w * u,
        4 * u * (w + 1),
        (w + 1) * (4 * w * u + w + 1),
        4 * w * u * (w + 1 + 4 * w * u),
    ]
    pe = sp.cancel(-receiving_n(roots_e) / (64 * u**2))
    check(sp.denom(pe) == 1, "exterior division is integral")
    pe = sp.expand(pe)
    pe_shift = integer_coefficients(pe.subs({u: 1 + X, w: 1 + Y}), (X, Y))
    pe_cert = certificate_coefficients(data["P_E_shifted"])
    check(pe_shift == pe_cert, "reconstructed exterior certificate equals inherited array")
    check(full_rectangle(pe_shift, 12, 16), "exterior support is the full 13 by 17 rectangle")
    check(min(pe_shift.values()) == 83_886_080, "exterior coefficient floor")

    je = 16 * w**2 * u**2 + 8 * w**2 * u + 28 * w * u + 4 * u + w**2 + 2 * w + 1
    qe = 4 * w**4 * je**6
    exterior_residual = integer_coefficients(
        449**6 * pe.subs({u: 1 + X, w: 1 + Y})
        - 1_310_720 * qe.subs({u: 1 + X, w: 1 + Y}),
        (X, Y),
    )
    check(full_rectangle(exterior_residual, 12, 16), "translated exterior residual support")
    check(all(c > 0 for c in exterior_residual.values()), "translated exterior residual positivity")

    b = 2 + X
    c = 3 + X + Y
    lm = sp.expand(4 * b * c - b - c)
    tm = sp.expand((b + c) * lm + b * c)
    vm = sp.expand(b**2 * c**2)
    ss, vv = sp.symbols("ss vv")
    pnorm = (
        7168 * vv**4
        - (5568 * ss**2 + 5728 * ss - 5888) * vv**3
        + (320 * ss**4 + 2744 * ss**3 + 705 * ss**2 - 3350 * ss - 903) * vv**2
        + (-140 * ss**5 - 443 * ss**4 + 440 * ss**3 + 390 * ss**2 + 70 * ss - 249) * vv
        + 20 * ss**6 - 7 * ss**5 - 26 * ss**4 - 7 * ss**3 + 20 * ss**2
    )
    hm = sp.cancel(lm**6 * pnorm.subs({ss: tm / lm, vv: vm / lm}))
    check(sp.denom(hm) == 1, "middle denominator clears exactly")
    hm = sp.expand(hm)
    hm_coeffs = integer_coefficients(hm, (X, Y))
    hm_cert = certificate_coefficients(data["H_M_shifted"])
    check(hm_coeffs == hm_cert, "reconstructed middle certificate equals inherited array")
    check(full_trapezoid(hm_coeffs, 18, 12, 20), "middle support is the full 192-position trapezoid")
    check(len(hm_coeffs) == 192 and min(hm_coeffs.values()) == 81_920, "middle coefficient count and floor")

    jm = sp.expand(
        8 * X**3 + 12 * X**2 * Y + 4 * X * Y**2 + 61 * X**2 + 57 * X * Y
        + 7 * Y**2 + 151 * X + 63 * Y + 120
    )
    middle_base_residual = integer_coefficients(483**6 * hm - 81_920 * jm**6, (X, Y))
    check(all(c > 0 for c in middle_base_residual.values()), "middle baseline residual positivity")

    left_gap = sp.expand((b + c) ** 2 * hm)
    left_gap_coeffs = integer_coefficients(left_gap, (X, Y))
    check(full_trapezoid(left_gap_coeffs, 20, 14, 22), "middle gap support is the full 237-position trapezoid")
    check(len(left_gap_coeffs) == 237 and min(left_gap_coeffs.values()) == 81_920,
          "middle gap coefficient count and floor")
    right_gap = sp.expand(lm**4 * (Y + 1) ** 2 * jm**4)
    gap_denominator = 4 * 52**4 * 483**4
    middle_gap_residual = integer_coefficients(gap_denominator * left_gap - 81_920 * right_gap, (X, Y))
    check(all(c > 0 for c in middle_gap_residual.values()), "middle gap residual positivity")

    c0 = sp.Rational(81_920, 483**6)
    csharp = sp.Rational(80, 6279**4)
    check(sp.Rational(81_920, gap_denominator) == csharp, "sharp constant identity")
    check(c0 > csharp, "exterior and middle constants are ordered")
    check(sp.Rational(1_310_720, 449**6) > 16 * c0, "exterior comparison exceeds required margin")

    return {
        "certificate_sha256": cert_hash,
        "P_E_terms": len(pe_shift),
        "P_E_minimum": min(pe_shift.values()),
        "translated_exterior_residual_minimum": min(exterior_residual.values()),
        "H_M_terms": len(hm_coeffs),
        "H_M_minimum": min(hm_coeffs.values()),
        "middle_gap_terms": len(left_gap_coeffs),
        "middle_gap_minimum": min(left_gap_coeffs.values()),
        "c0": [int(sp.numer(c0)), int(sp.denom(c0))],
        "c": [int(sp.numer(csharp)), int(sp.denom(csharp))],
    }


def exact_family_stage() -> dict[str, object]:
    p = sp.symbols("p", positive=True)
    a1 = (p + 3) / 4
    t1 = p * a1
    y1 = (t1 + 2) / 3
    z1 = t1 * (t1 + 2) / 6
    a2 = (3 * p + 1) / 8
    y2 = 2 * a2
    z2 = 2 * p * a2
    check(sp.cancel(1 / a1 + 1 / y1 + 1 / z1 - 4 / p) == 0, "family I ES identity")
    check(sp.cancel(1 / a2 + 1 / y2 + 1 / z2 - 4 / p) == 0, "family II ES identity")
    check(sp.expand(4 * a1 - p) == 3, "family I R")
    check(sp.expand(4 * a2 - p) == (p + 1) / 2, "family II R")
    check(sp.cancel(4 * a2 + 1 - 3 * (4 * a2 - p)) == 0, "family II exterior gate")

    n1 = int(receiving_n([sp.Integer(13), sp.Integer(4), sp.Integer(18), sp.Integer(468)]))
    n2 = int(receiving_n([sp.Integer(13), sp.Integer(5), sp.Integer(10), sp.Integer(130)]))
    check(n1 == -30_891_260_499_630_665_400, "family I p=13 numerator")
    check(n2 == -4_304_041_269_696_000, "family II p=13 numerator")

    k = sp.symbols("k", integer=True, nonnegative=True)
    p24 = 24 * k + 13
    check(sp.simplify(a1.subs(p, p24) - (6 * k + 4)) == 0, "family I a integrality")
    family_I_gate = sp.Poly(sp.expand(2 * (6 * k + 4) ** 2 + 1), k, domain=sp.ZZ)
    check(all(int(coefficient) % 3 == 0 for coefficient in family_I_gate.all_coeffs()),
          "family I exterior gate")
    family_I_tail = sp.Poly(sp.expand(p24 * (6 * k + 4) + 2), k, domain=sp.ZZ)
    check(all(int(coefficient) % 3 == 0 for coefficient in family_I_tail.all_coeffs()),
          "family I Y integrality")
    check(sp.simplify(a2.subs(p, p24) - (9 * k + 5)) == 0, "family II a integrality")

    return {
        "family_I_p13_N": n1,
        "family_II_p13_N": n2,
        "progression": "p = 24k + 13",
        "gcd_13_24": 1,
    }


def receiver_mp(prime: int, family: int) -> tuple[mp.matrix, list[mp.mpf], list[mp.mpf], int]:
    p = mp.mpf(prime)
    if family == 1:
        a = (p + 3) / 4
        t = p * a
        y = (t + 2) / 3
        z = t * (t + 2) / 6
        expected_signs = (-1, 1, 1, -1)
    elif family == 2:
        a = (3 * p + 1) / 8
        y = 2 * a
        z = 2 * p * a
        expected_signs = (1, 1, -1, -1)
    else:
        raise ValueError("family must be 1 or 2")
    roots = [p, a, y, z]
    s = sum(roots)
    A = -1 / s
    ds = []
    xis = []
    for j, root in enumerate(roots):
        d = A
        for m, other in enumerate(roots):
            if m != j:
                d *= root - other
        ds.append(d)
        check((1 if d > 0 else -1) == expected_signs[j], f"family {family} derivative sign {j}")
        xis.append(1 / mp.sqrt(d) if d > 0 else 1j / mp.sqrt(-d))
    O = mp.matrix(4, 4)
    for j, (root, d, xi) in enumerate(zip(roots, ds, xis)):
        O[0, j] = xi
        O[1, j] = -1j * xi * d
        O[2, j] = xi * (A * d**2 + 2 * root * d)
        O[3, j] = 1j * xi * (7 * root**2 * d - 13 * d**2)
    vandermonde = mp.mpf(1)
    for i in range(4):
        for j in range(i + 1, 4):
            vandermonde *= roots[j] - roots[i]
    epsilon = A**2 * vandermonde * mp.fprod(xis)
    epsilon_int = int(mp.nint(mp.re(epsilon)))
    check(abs(epsilon - epsilon_int) < mp.mpf("1e-70"), f"family {family} epsilon is a retained sign")
    return O, roots, ds, epsilon_int


def svd_values(matrix: mp.matrix) -> list[mp.mpf]:
    _, values, _ = mp.svd(matrix)
    return [mp.mpf(values[j]) for j in range(len(values))]


def normalized_singular_data(prime: int, family: int) -> dict[str, object]:
    O, roots, ds, epsilon = receiver_mp(prime, family)
    values = svd_values(O)
    if family == 1:
        exponents = [12, 4, mp.mpf(3) / 2, -mp.mpf(3) / 2]
        limits = [mp.mpf(5) / 221184, mp.mpf(1) / 72, 1 / (2 * mp.sqrt(2)), 4 * mp.sqrt(2)]
    else:
        exponents = [6, 2, 1, -1]
        limits = [mp.mpf(135) / 16, mp.sqrt(991) / 32, 5 * mp.sqrt(3) / mp.sqrt(991), 38 / (5 * mp.sqrt(3))]
    normalized = [values[j] / mp.power(prime, exponents[j]) for j in range(4)]
    return {
        "p": prime,
        "family": family,
        "epsilon": epsilon,
        "roots": [mp.nstr(x, 30) for x in roots],
        "derivative_signs": [1 if x > 0 else -1 for x in ds],
        "normalized_singular_values": [mp.nstr(x, 30) for x in normalized],
        "limits": [mp.nstr(x, 30) for x in limits],
        "relative_errors": [mp.nstr(abs(normalized[j] / limits[j] - 1), 12) for j in range(4)],
        "inverse_wedge_2": mp.nstr(1 / (values[2] * values[3]), 30),
        "scaled_inverse_wedge_3": mp.nstr(
            (prime**4 if family == 1 else prime**2) / (values[1] * values[2] * values[3]), 30
        ),
    }


def numerical_stage() -> dict[str, object]:
    mp.mp.dps = 110
    samples = []
    for prime in (13, 37, 61, 1000117):
        check(prime % 24 == 13, f"sample {prime} is in the progression")
        samples.append(normalized_singular_data(prime, 1))
        samples.append(normalized_singular_data(prime, 2))
    large1 = samples[-2]
    large2 = samples[-1]
    check(mp.mpf(large1["relative_errors"][0]) < mp.mpf("3e-5"), "family I large-prime leading scale")
    check(mp.mpf(large2["relative_errors"][0]) < mp.mpf("1e-5"), "family II large-prime leading scale")
    return {"precision_decimal_digits": mp.mp.dps, "samples": samples}


def main() -> None:
    exact_polynomials = exact_polynomial_stage()
    exact_families = exact_family_stage()
    numerical = numerical_stage()
    result = {
        "schema_version": 1,
        "status": "pass",
        "checks": CHECKS,
        "exact_polynomials": exact_polynomials,
        "exact_families": exact_families,
        "numerical_singular_values": numerical,
        "scope": (
            "Exact reconstruction of the three new coefficient comparisons, exact family identities and "
            "integrality reductions, plus high-precision evaluation of the literal complex receiver. "
            "The TeX supplies the cofactor and compound-matrix proofs."
        ),
        "nonclaims": [
            "No Erdős-Straus occupancy theorem.",
            "No Riemann-hypothesis conclusion.",
            "Numerical SVD samples do not replace the exact asymptotic proof.",
        ],
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"status": "pass", "checks": CHECKS, "output": str(OUT)}, indent=2))


if __name__ == "__main__":
    main()
