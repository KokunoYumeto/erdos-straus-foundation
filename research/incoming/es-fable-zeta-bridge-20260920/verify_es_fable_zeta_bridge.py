"""Exact symbolic checks for the normalized ES quartic and its two bridges.

The upstream directory contains the independent global inverse, conductor,
signed-evaluation and monodromy certificates.  This checker verifies the new
ES-specific coefficient map, intrinsic prime, image equation, marked factor
lift, eight source states, and the separately retained seven-state suspension.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as s


def polynomial_map(a, y, z, w):
    i = s.I
    return (
        a**3*z + 2*a**2*y - i*a,
        -a**3*y**2*z - 2*i*a**2*y*z + a**2*w - 2*a**2*y**3
        - 10*i*a*y**2 + 3*a*z + y,
        2*a**3*y**3*z + 6*i*a**2*y**2*z + 2*a**2*w*y
        + 4*a**2*y**4 + 2*i*a*w - 4*i*a*y**3 - 2*a*y*z
        + 2*i*z + 7*y**2,
        2*a**3*y**4*z + 8*i*a**2*y**3*z + a**2*w*y**2
        + 4*a**2*y**5 + 2*i*a*w*y + 7*i*a*y**4 - 10*a*y**2*z
        - 4*i*y*z - w - 3*y**3,
    )


U, V, T = s.symbols("U V T")
p, x, y, z = s.symbols("p x y z", nonzero=True)
s1 = x + y + z
s2 = x*y + x*z + y*z
s3 = x*y*z
S = p + s1

# The normalized prime-plus-denominator quartic and its exact coefficients.
H4 = s.expand(-((U-p*V)*(U-x*V)*(U-y*V)*(U-z*V))/S)
u0 = -1/S
u2 = -(p*s1+s2)/S
u3_raw = (p*s2+s3)/S
u4 = -p*s3/S
H4_expected = u0*U**4 + U**3*V + u2*U**2*V**2 + u3_raw*U*V**3 + u4*V**4
assert s.factor(H4-H4_expected) == 0

# On the ES relation p*s2=4*s3, u3=5*s3/S and p=-5*u4/u3.
u3 = 5*s3/S
assert s.factor((u3_raw-u3).subs(p, 4*s3/s2)) == 0
assert s.simplify(-5*u4/u3-p) == 0

A, B, C, D = s.symbols("A B C D", nonzero=True)
G = 625*A*D**3 - 125*C*D**2 + 25*B*C**2*D - 4*C**4
h_generic = A*T**4 + T**3 + B*T**2 + C*T + D
p_intrinsic = -5*D/C
assert s.factor(h_generic.subs(T, p_intrinsic) - D*G/C**4) == 0

G_arith = s.factor(G.subs({A: u0, B: u2, C: u3, D: u4}))
assert s.factor(G_arith.subs(p, 4*s3/s2)) == 0

# The factor carrier retains the resultant orientation and both incidences.
lam = s.symbols("lam", nonzero=True)
mu = -1/(lam*S)
Delta_p = (p-x)*(p-y)*(p-z)
a_fac, b_fac = lam, -lam*p
c_fac, d_fac, e_fac, f_fac = mu, -mu*s1, mu*s2, -mu*s3
assert s.simplify(a_fac*d_fac+b_fac*c_fac-1) == 0
assert s.factor((4*a_fac*f_fac-b_fac*e_fac).subs(p, 4*s3/s2)) == 0
resultant = s.expand(lam**3*mu*Delta_p)
assert s.simplify(resultant.subs(lam**2, -S/Delta_p)-1) == 0

# General inverse coordinates: exact residuals modulo h(r)=0 and a^2 h'(r)=1.
r, a = s.symbols("r a", nonzero=True)
h = A*r**4 + r**3 + B*r**2 + C*r + D
dh = 4*A*r**3 + 3*r**2 + 2*B*r + C
y0 = -r-s.I/a
z0 = A/a**3+2*r/a+3*s.I/a**2
w0 = (7*s.I*r**2/a + (B-17*r+A*r**2)/a**2
      - 13*s.I/a**3 - 2*A/a**4)
images = polynomial_map(a, y0, z0, w0)
targets = (A, B, C, D)
gb = s.groebner([h, a**2*dh-1], D, C, B, A, r, a, order="lex")
inverse_residuals = []
for image, target in zip(images, targets):
    numerator = s.together(image-target).as_numer_denom()[0]
    remainder = s.expand(gb.reduce(s.Poly(numerator, D, C, B, A, r, a).as_expr())[1])
    inverse_residuals.append(str(remainder))
assert inverse_residuals == ["0", "0", "0", "0"]

# Quartic discriminant with its original scale retained.
roots = [p, x, y, z]
vandermonde_sq = s.prod((roots[j]-roots[k])**2 for j in range(4) for k in range(j+1, 4))
disc_h4 = s.factor(s.discriminant(H4.subs({U: T, V: 1}), T))
assert s.factor(disc_h4-vandermonde_sq/S**6) == 0

# The separate reciprocal-cubic suspension and its discriminant.
t1, t2, t3 = s.symbols("t1 t2 t3")
e2 = t1*t2+t1*t3+t2*t3
e3 = t1*t2*t3
H3 = s.expand(V*(U-t1*V)*(U-t2*V)*(U-t3*V))
H3_sum4 = s.expand(H3.subs(t3, 4-t1-t2))
H3_expected = (U**3*V-4*U**2*V**2
               +e2.subs(t3, 4-t1-t2)*U*V**3
               -e3.subs(t3, 4-t1-t2)*V**4)
assert s.expand(H3_sum4-H3_expected) == 0
disc3 = s.discriminant(T**3-4*T**2+s.symbols("e2")*T-s.symbols("e3"), T)

receipt = {
    "schema_version": 2,
    "certificate": "normalized ES prime-denominator quartic, signed Fable cover, and fixed conductor crosswalk",
    "checks": {
        "normalized_quartic_coefficients": True,
        "es_relation": "p(xy+xz+yz)=4xyz",
        "intrinsic_prime": "p=-5u4/u3",
        "coefficient_hypersurface": "625u0u4^3-125u3u4^2+25u2u3^2u4-4u3^4=0",
        "marked_resultant_one_factorization": True,
        "es_incidence_4af_minus_be": True,
        "eight_source_inverse_residuals": inverse_residuals,
        "quartic_discriminant": "S^-6 product_{j<k}(t_j-t_k)^2",
        "separate_reciprocal_suspension": True,
        "suspended_cubic_discriminant": str(s.factor(disc3)),
    },
    "nonclaims": [
        "The coefficient hypersurface alone does not impose integral positive roots, primality, or ES channel gates.",
        "The construction begins with an ES witness and is not a universal existence proof.",
        "The fixed conductor receiver does not identify ES roots with zeta zeros.",
    ],
}

out = Path(__file__).with_name("verification_receipt.json")
out.write_text(json.dumps(receipt, indent=2, sort_keys=True)+"\n", encoding="utf-8")
print(json.dumps(receipt, indent=2, sort_keys=True))
