#!/usr/bin/env python3
"""Exact certificate for the odd receiving divisor on the ES coefficient locus."""

from __future__ import annotations

import json

import flint
import sympy as sp


p, s1, s2, s3 = sp.symbols("p s1 s2 s3", nonzero=True)
S, b, c, d = sp.symbols("S b c d", nonzero=True)
A, B, C, D = sp.symbols("A B C D")
T, Z, X, w, delta = sp.symbols("T Z X w delta")

Dodd = (
    20 * (3 * C - B**2)
    + A * (87 * B**3 - 282 * B * C - 51 * D)
    + A**2 * (-28 * B**4 + 22 * B**2 * C + 431 * C**2 + 204 * B * D)
    + A**3 * (224 * B**2 * D - 168 * B * C**2 - 856 * C * D)
    - 448 * A**4 * D**2
)

P_tilde = (
    60 * c * S**5
    - (20 * b**2 + 51 * d) * S**4
    - 282 * b * c * S**3
    + (87 * b**3 + 431 * c**2 + 204 * b * d) * S**2
    + (22 * b**2 * c - 856 * c * d) * S
    - 28 * b**4 + 224 * b**2 * d - 168 * b * c**2 - 448 * d**2
)

theta = {A: -1/S, B: -b/S, C: c/S, D: -d/S}
assert sp.factor(Dodd.subs(theta) - P_tilde / S**6) == 0

Phi = (
    -7168 * Z**4
    + 32 * (174*T**2 + 179*T - 184) * Z**3
    + (-320*T**4 - 2744*T**3 - 705*T**2 + 3350*T + 903) * Z**2
    + (140*T**5 + 443*T**4 - 440*T**3 - 390*T**2 - 70*T + 249) * Z
    - T**2 * (T - 1)**2 * (20*T**2 + 33*T + 20)
)

scale_sub = {
    S: p * (1 + T),
    b: p**2 * (T + 4*Z),
    c: 5 * p**3 * Z,
    d: p**4 * Z,
}
assert sp.factor(P_tilde.subs(scale_sub)/(p*(1+T))**6
                 - p**2*Phi/(1+T)**6) == 0

# The RH-strand regular witness is not on the normalized ES hypersurface.
G = 625*A*D**3 - 125*C*D**2 + 25*B*C**2*D - 4*C**4
target_value = sp.factor(G.subs({A: 1, B: 0, C: -sp.Rational(60, 431), D: 0}))
assert target_value == -sp.Rational(51840000, 34507149121)

# A concrete ES point shows that the pullback is not identically zero.
def es_coefficients(prime, denominators):
    x, y, z = denominators
    es1 = x + y + z
    es2 = x*y + x*z + y*z
    es3 = x*y*z
    eS = prime + es1
    return {
        A: -1/eS,
        B: -(prime*es1 + es2)/eS,
        C: (prime*es2 + es3)/eS,
        D: -(prime*es3)/eS,
    }

state_5 = es_coefficients(sp.Integer(5), (sp.Integer(2), sp.Integer(4), sp.Integer(20)))
assert sp.factor(sp.Rational(4, 5) - sum(sp.Rational(1, q) for q in (2, 4, 20))) == 0
state_5_value = sp.factor(Dodd.subs(state_5))
assert state_5_value != 0

# Exact positive-real crossing on the reciprocal line.
t1 = sp.Rational(1, 4) - delta
t2 = sp.Rational(1, 4) + delta
t3 = sp.Rational(7, 2)
x_line, y_line, z_line = 1/t1, 1/t2, 1/t3
assert sp.factor(t1 + t2 + t3 - 4) == 0
line_coeffs = es_coefficients(sp.Integer(1), (x_line, y_line, z_line))
line_value = sp.factor(Dodd.subs(line_coeffs))
Q = (
    319186534400*w**6 + 12383961481216*w**5
    - 26262983737344*w**4 - 1257389244416*w**3
    + 1383887871744*w**2 + 2670303991200*w - 90309375
)
assert sp.factor(line_value - (-8*Q.subs(w, delta**2)/(144*delta**2 - 65)**6)) == 0
q_left = sp.factor(Q.subs(w, sp.Rational(1, 10**6)))
q_right = sp.factor(Q.subs(w, sp.Rational(1, 10**4)))
assert q_left < 0 < q_right

# The scale-free cubic has roots x/p,y/p,z/p exactly on the ES relation.
cubic = X**3 - T*X**2 + 4*Z*X - Z
scaled_cubic = sp.expand(
    (X - sp.symbols("x")/p)
    * (X - sp.symbols("y")/p)
    * (X - sp.symbols("z")/p)
)
# Its coefficient statement is checked symbolically using elementary sums.
assert sp.expand(cubic.subs({T: s1/p, Z: s3/p**3})
                 - (X**3 - s1*X**2/p + s2*X/p**2 - s3/p**3)
                 .subs(s2, 4*s3/p)) == 0

# Primitive irreducibility certificate: independent SymPy/python-flint
# factorization over Z and irreducible reduction modulo 11.
content, factors_q = sp.factor_list(Phi, T, Z)
assert len(factors_q) == 1 and factors_q[0][1] == 1
assert sp.expand(content * factors_q[0][0] - Phi) == 0
assert sp.Poly(factors_q[0][0], T, Z).total_degree() == 6
phi_poly = sp.Poly(Phi, T, Z)
phi_dict = {tuple(map(int, monom)): int(coeff)
            for monom, coeff in phi_poly.terms()}
ctx_z = flint.fmpz_mpoly_ctx.get(("T", "Z"), "lex")
phi_flint = ctx_z.from_dict(phi_dict)
content_flint, factors_flint = phi_flint.factor()
assert len(factors_flint) == 1 and factors_flint[0][1] == 1
assert content_flint * factors_flint[0][0] == phi_flint
ctx_11 = flint.fmpz_mod_mpoly_ctx.get(("T", "Z"), 11, "lex")
phi_dict_11 = {monom: coeff % 11 for monom, coeff in phi_dict.items()
               if coeff % 11}
phi_11 = ctx_11.from_dict(phi_dict_11)
content_11, factors_11 = phi_11.factor()
assert len(factors_11) == 1 and factors_11[0][1] == 1
reconstructed_11 = ctx_11.constant(content_11) * factors_11[0][0]
assert reconstructed_11 == phi_11

receipt = {
    "schema_version": 1,
    "status": "pass",
    "checks": {
        "coefficient_pullback_identity": True,
        "scale_free_phi_identity": True,
        "phi_primitive_irreducible_over_Q": True,
        "phi_independent_python_flint_factorization": True,
        "phi_irreducible_mod_11": True,
        "rh_regular_target_not_on_es_hypersurface": str(target_value),
        "state_p5_pullback_nonzero": str(state_5_value),
        "positive_real_line_identity": True,
        "Q_1e_minus_6_sign": "negative",
        "Q_1e_minus_4_sign": "positive",
        "split_cubic_criterion": True,
    },
    "exact_endpoint_values": {
        "Q(10^-6)": str(q_left),
        "Q(10^-4)": str(q_right),
    },
}
print(json.dumps(receipt, indent=2, sort_keys=True))
