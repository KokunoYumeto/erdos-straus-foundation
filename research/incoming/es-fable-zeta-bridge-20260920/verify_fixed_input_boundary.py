#!/usr/bin/env python3
"""Exact certificate for the hard-prime, fixed-input, and boundary results."""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import sympy as sp


p, R, r, w = sp.symbols("p R r w", nonzero=True)
A, B, C, D = sp.symbols("A B C D")


# Fixed-input denominator bound: verify the exact comparison identity.
S_R = p * (p + R) / 4
s_p = p * (p + 3) / 4
comparison = sp.factor(
    S_R * (S_R + 1) / R
    - s_p * (s_p + 1) / 3
    - p**2 * (R - 3) / 16 * (1 - (p**2 + 4) / (3 * R))
)
assert comparison == 0


# Fixed-p coefficient chart, factorization, and discriminant.
D_fixed = -p * C / 5
B_fixed = -A * p**2 - p - 4 * C / (5 * p)
h = A * r**4 + r**3 + B_fixed * r**2 + C * r + D_fixed
g = A * r**3 + (1 + A * p) * r**2 - 4 * C * r / (5 * p) + C / 5
d_p = 2 * A * p**3 + p**2 - 3 * C / 5
assert sp.factor(h - (r - p) * g) == 0
assert sp.factor(g.subs(r, p) - d_p) == 0
assert sp.factor(sp.discriminant(h, r) - d_p**2 * sp.discriminant(g, r)) == 0


def normalized_quartic(roots):
    """Return A*product(r-root), with r^3 coefficient one."""
    total = sp.factor(sum(roots))
    leading = -1 / total
    polynomial = sp.expand(leading * sp.prod(r - root for root in roots))
    return sp.factor(leading), polynomial


def derivative_values(roots):
    leading, polynomial = normalized_quartic(roots)
    derivative = sp.diff(polynomial, r)
    return leading, [sp.factor(derivative.subs(r, root)) for root in roots]


# The two explicit monodromy families satisfy the ES relation.
roots_14 = [
    p,
    p * (2 + w),
    p * (2 - w),
    p * (4 - w**2) / (12 - 4 * w**2),
]
assert sp.factor(4 / p - sum(1 / root for root in roots_14[1:])) == 0
A14, deriv_14 = derivative_values(roots_14)
assert sp.factor(A14 - (-4 * (w**2 - 3) / (p * (21 * w**2 - 64)))) == 0
C14 = sp.Poly(normalized_quartic(roots_14)[1], r).all_coeffs()[-2]
assert sp.factor(C14 - (
    -5 * p**2 * (w - 2) ** 2 * (w + 2) ** 2 / (21 * w**2 - 64)
)) == 0
assert sp.factor(deriv_14[0] - (
    p**2 * (w - 1) * (w + 1) * (3 * w**2 - 8)
    / (21 * w**2 - 64)
)) == 0
assert sp.factor(deriv_14[1] - (
    -2 * p**2 * w * (w + 1) * (w + 2) * (4 * w**2 - w - 10)
    / (21 * w**2 - 64)
)) == 0
assert sp.factor(deriv_14[2] - (
    2 * p**2 * w * (w - 2) * (w - 1) * (4 * w**2 + w - 10)
    / (21 * w**2 - 64)
)) == 0
assert sp.factor(deriv_14[3] - (
    -p**2 * (w - 2) * (w + 2) * (3 * w**2 - 8)
    * (4 * w**2 - w - 10) * (4 * w**2 + w - 10)
    / (16 * (w**2 - 3) ** 2 * (21 * w**2 - 64))
)) == 0

roots_15 = [
    p,
    p * (1 + w),
    sp.Rational(2, 5) * p,
    2 * p * (1 + w) / (1 + 3 * w),
]
assert sp.factor(4 / p - sum(1 / root for root in roots_15[1:])) == 0
A15, deriv_15 = derivative_values(roots_15)
assert sp.factor(A15 - (-5 * (3 * w + 1) / (p * (15 * w**2 + 51 * w + 22)))) == 0
C15 = sp.Poly(normalized_quartic(roots_15)[1], r).all_coeffs()[-2]
assert sp.factor(C15 - (
    20 * p**2 * (w + 1) ** 2 / (15 * w**2 + 51 * w + 22)
)) == 0
assert sp.factor(deriv_15[0] - 3 * p**2 * w * (w - 1) / (15 * w**2 + 51 * w + 22)) == 0
assert sp.factor(deriv_15[1] - (
    -p**2 * w * (w + 1) * (3 * w - 1) * (5 * w + 3)
    / (15 * w**2 + 51 * w + 22)
)) == 0
assert sp.factor(deriv_15[2] - (
    12 * p**2 * (w + 2) * (5 * w + 3)
    / (25 * (15 * w**2 + 51 * w + 22))
)) == 0
assert sp.factor(deriv_15[3] - (
    -4 * p**2 * (w - 1) * (w + 1) * (w + 2) * (3 * w - 1)
    / ((3 * w + 1) ** 2 * (15 * w**2 + 51 * w + 22))
)) == 0


# Enumerate the claimed order-48 signed permutation group on eight sheets.
def parity(perm):
    inversions = sum(
        perm[i] > perm[j]
        for i in range(len(perm))
        for j in range(i + 1, len(perm))
    )
    return -1 if inversions % 2 else 1


def product(values):
    out = 1
    for value in values:
        out *= value
    return out


def sheet_action(signs, denominator_perm):
    root_perm = (0,) + tuple(index + 1 for index in denominator_perm)
    action = []
    for root in range(4):
        for sign in (-1, 1):
            target_root = root_perm[root]
            target_sign = sign * signs[root]
            action.append(2 * target_root + (1 if target_sign == 1 else 0))
    return tuple(action)


group = []
for perm0 in itertools.permutations(range(3)):
    sign_perm = parity(perm0)
    for signs in itertools.product((-1, 1), repeat=4):
        if product(signs) == sign_perm:
            group.append(sheet_action(signs, perm0))
group = sorted(set(group))
assert len(group) == 48


def compose(left, right):
    return tuple(left[right[index]] for index in range(8))


identity = tuple(range(8))
orbit_prime = {action[index] for action in group for index in (0, 1)}
orbit_denominator = {action[index] for action in group for index in range(2, 8)}
assert orbit_prime == {0, 1}
assert orbit_denominator == set(range(2, 8))

centralizer = []
for candidate in itertools.permutations(range(8)):
    if all(compose(candidate, action) == compose(action, candidate) for action in group):
        centralizer.append(candidate)
assert len(centralizer) == 4


# Finite completion and exact double-root examples.
eta, epsilon, gamma, c = sp.symbols("eta epsilon gamma c", nonzero=True)

roots_p5 = [sp.Integer(5), sp.Integer(5), sp.Integer(2), sp.Integer(10)]
A_p5, h_p5 = normalized_quartic(roots_p5)
assert A_p5 == -sp.Rational(1, 22)
assert sp.factor(h_p5 + (r - 5) ** 2 * (r - 2) * (r - 10) / 22) == 0
g0_p5 = sp.factor((-sp.Rational(1, 22) * (r - 2) * (r - 10)).subs(r, 5))
assert g0_p5 == sp.Rational(15, 22)

roots_general = [p, p, sp.Rational(2, 5) * p, 2 * p]
A_general, h_general = normalized_quartic(roots_general)
g0_general = sp.factor(h_general / (r - p) ** 2).subs(r, p)
assert sp.factor(A_general + sp.Rational(5, 22) / p) == 0
assert sp.factor(g0_general - 3 * p / 22) == 0
assert sp.factor(4 / p - sum(1 / root for root in roots_general[1:])) == 0

r_plus = sp.Rational(1, 2) + sp.I * gamma
r_minus = sp.Rational(1, 2) - sp.I * gamma
h_pair = -sp.Rational(1, 2) * ((r - sp.Rational(1, 2)) ** 2 + gamma**2) ** 2
assert sp.expand(h_pair + sp.Rational(1, 2) * (r - r_plus) ** 2 * (r - r_minus) ** 2) == 0
g0_pair = -sp.Rational(1, 2) * (r_plus - r_minus) ** 2
assert sp.factor(g0_pair - 2 * gamma**2) == 0
assert sp.factor(c**2 * 4 * gamma**2 - 3 * p / 11).subs(
    c**2, 3 * p / (44 * gamma**2)
) == 0

# Multiplication by epsilon=eta^2/(2g0) on C[eta]/eta^4 has two 2-blocks.
N = sp.Matrix(
    [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
    ]
)
assert N.rank() == 2
assert N**2 == sp.zeros(4)


# Exact odd-moment factorization and Lagrange inverse on a rational quartic.
sample_roots = [sp.Integer(2), sp.Integer(3), sp.Integer(5), sp.Integer(7)]
A_s, h_s = normalized_quartic(sample_roots)
poly_s = sp.Poly(h_s, r)
_, coeff_r3, B_s, C_s, D_s = poly_s.all_coeffs()
assert coeff_r3 == 1
d_s = sp.diff(h_s, r)
xis = [sp.sqrt(1 / d_s.subs(r, root)) for root in sample_roots]
vandermonde = sp.Matrix([[root**degree for root in sample_roots] for degree in range(4)])
U = vandermonde * sp.diag(*xis)
assert sp.simplify(U.det() ** 2 - A_s ** -4) == 0

component_polynomials = [
    sp.Integer(1),
    -sp.I * d_s,
    A_s * d_s**2 + 2 * r * d_s,
    sp.I * (7 * r**2 * d_s - 13 * d_s**2),
]
rows = []
for component in component_polynomials:
    remainder = sp.rem(sp.Poly(component, r), sp.Poly(h_s, r)).as_expr()
    rows.append([sp.expand(remainder).coeff(r, degree) for degree in range(4)])
V_h = sp.Matrix(rows)
O = sp.Matrix(
    [
        [
            xis[j] * component_polynomials[i].subs(r, sample_roots[j])
            for j in range(4)
        ]
        for i in range(4)
    ]
)
assert sp.simplify(O - V_h * U) == sp.zeros(4)

m0, m1, m2, m3 = sp.symbols("m0 m1 m2 m3")
mvec = sp.Matrix([m0, m1, m2, m3])
beta_formula = []
for root, xi in zip(sample_roots, xis):
    beta_formula.append(
        xi
        * (
            (C_s + B_s * root + root**2 + A_s * root**3) * m0
            + (B_s + root + A_s * root**2) * m1
            + (1 + A_s * root) * m2
            + A_s * m3
        )
    )
assert sp.simplify(U * sp.Matrix(beta_formula) - mvec) == sp.zeros(4, 1)


receipt = {
    "schema_version": 1,
    "status": "pass",
    "checks": {
        "fixed_input_bound_comparison_identity": True,
        "fixed_p_coefficient_factorization": True,
        "fixed_p_discriminant_factorization": True,
        "monodromy_path_denominator_collision": True,
        "monodromy_path_prime_collision": True,
        "monodromy_all_derivative_factors_exact": True,
        "signed_monodromy_group_order": len(group),
        "signed_sheet_orbit_sizes": [len(orbit_prime), len(orbit_denominator)],
        "deck_centralizer_order": len(centralizer),
        "p5_nilpotent_boundary": "eta^2=(15/11)epsilon",
        "rational_boundary_family": "eta^2=(3p/11)epsilon",
        "paired_root_boundary": "eta^2=4gamma^2 epsilon",
        "local_scaling": "c^2=3p/(44gamma^2)",
        "double_root_jordan_blocks": [2, 2],
        "odd_moment_factorization": True,
        "odd_moment_inverse": True,
    },
    "nonclaims": [
        "The fixed-input bounds do not prove witness occupancy.",
        "The order-48 paths are complex algebraic ES paths, not paths of positive integral witnesses.",
        "The local ES--paired-root isomorphism does not identify global fibres or zeta zeros.",
    ],
}

output = Path(__file__).with_name("fixed_input_boundary_receipt.json")
output.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(receipt, indent=2, sort_keys=True))
