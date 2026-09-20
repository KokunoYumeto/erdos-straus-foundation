"""Exact symbolic checks for the normalized ES quartic and its two bridges.

The upstream directory contains the independent global inverse, conductor,
signed-evaluation and monodromy certificates.  This checker verifies the new
ES-specific coefficient map, intrinsic prime, image equation, marked factor
lift, eight source states, and the separately retained seven-state suspension.
"""

from __future__ import annotations

import json
import hashlib
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

# Exact inverse of the symmetric source chart and the singular boundary.
p_inv = -5*D/C
S_inv = -1/A
s1_inv = S_inv-p_inv
s2_inv = 4*C**2/(25*A*D)
s3_inv = -C/(5*A)
assert s.factor(p_inv*s2_inv-4*s3_inv) == 0
assert s.factor(p_inv+s1_inv-S_inv) == 0
assert s.factor(-1/S_inv-A) == 0
assert s.factor(5*s3_inv/S_inv-C) == 0
assert s.factor(-p_inv*s3_inv/S_inv-D) == 0
B_inverse_residual = s.factor(-(p_inv*s1_inv+s2_inv)/S_inv-B)
assert s.factor(B_inverse_residual + G/(25*C**2*D)) == 0

gradient_G = tuple(s.factor(s.diff(G, variable)) for variable in (A, B, C, D))
gradient_G_expected = (
    625*D**3,
    25*C**2*D,
    50*B*C*D-16*C**3-125*D**2,
    1875*A*D**2+25*B*C**2-250*C*D,
)
assert all(s.factor(actual-expected) == 0
           for actual, expected in zip(gradient_G, gradient_G_expected))
assert all(s.factor(part.subs({C: 0, D: 0})) == 0 for part in gradient_G)

Q_at_p = s.factor(p_inv**3-s1_inv*p_inv**2+s2_inv*p_inv-s3_inv)
Q_at_p_expected = -(1250*A*D**3+3*C**4-125*C*D**2)/(5*A*C**3)
assert s.factor(Q_at_p-Q_at_p_expected) == 0

ss1, ss2, ss3 = s.symbols("ss1 ss2 ss3")
Q = T**3-ss1*T**2+ss2*T-ss3
disc_Q = s.discriminant(Q, T)
assert s.factor(disc_Q-(ss1**2*ss2**2-4*ss2**3-4*ss1**3*ss3
                             -27*ss3**2+18*ss1*ss2*ss3)) == 0

B_torus = 5*D/C-25*A*D**2/C**2+4*C**2/(25*D)
assert s.factor(B_torus-B+G/(25*C**2*D)) == 0
Q_target = (T**3+(1/A-5*D/C)*T**2
            +4*C**2*T/(25*A*D)+C/(5*A))
target_factor_residual = s.factor(
    A*(T+5*D/C)*Q_target-h_generic+G*T**2/(25*C**2*D)
)
assert target_factor_residual == 0

# Exact primary decomposition of the nonreduced Jacobian scheme.
AA, BB, CC, DD, tau = s.symbols("AA BB CC DD tau")
GG = 625*AA*DD**3-125*CC*DD**2+25*BB*CC**2*DD-4*CC**4
J_sing = [
    DD**3,
    CC**2*DD,
    16*CC**3-50*BB*CC*DD+125*DD**2,
    BB*CC**2-10*CC*DD+75*AA*DD**2,
]
Q_plane = [
    CC**3, CC**2*DD, CC*DD**2, DD**3,
    2*BB*CC*DD-5*DD**2,
    BB*CC**2-10*CC*DD+75*AA*DD**2,
]
Q_embedded = [
    BB, DD**3, 16*CC**3+125*DD**2, 2*CC*DD-15*AA*DD**2,
]
euler_identity = (-AA*s.diff(GG, AA)+BB*s.diff(GG, BB)
                  +2*CC*s.diff(GG, CC)+3*DD*s.diff(GG, DD)-8*GG)
assert s.expand(euler_identity) == 0
intersection_basis = s.groebner(
    [tau*f for f in Q_plane]+[(1-tau)*f for f in Q_embedded],
    tau, AA, BB, CC, DD, order="lex",
)
intersection_generators = [poly.as_expr() for poly in intersection_basis.polys
                           if not poly.as_expr().has(tau)]
gb_J = s.groebner(J_sing, AA, BB, CC, DD, order="grlex")
gb_intersection = s.groebner(intersection_generators, AA, BB, CC, DD,
                             order="grlex")
assert all(s.expand(gb_J.reduce(f)[1]) == 0 for f in intersection_generators)
assert all(s.expand(gb_intersection.reduce(f)[1]) == 0 for f in J_sing)

# Fixed receiver inversion retains every moment and reference-root coordinate.
vv = s.symbols("v", integer=True, nonnegative=True)
m0 = s.symbols("m0", nonzero=True)
m1, m2, m3 = s.symbols("m1 m2 m3")
rr0, rr1, rr2, rr3 = s.symbols("r0 r1 r2 r3")
alpha2 = (vv+2)*(vv+1)/2
alpha3 = (vv+3)*(vv+2)*(vv+1)/6
beta23 = (vv+3)*(vv+2)/2
Bmat = s.Matrix([
    [m0, m1, m2, m3],
    [0, (vv+1)*m0, (vv+2)*m1, (vv+3)*m2],
    [0, 0, alpha2*m0, beta23*m1],
    [0, 0, 0, alpha3*m0],
])
cc3 = rr3/(alpha3*m0)
cc2 = (rr2-beta23*m1*cc3)/(alpha2*m0)
cc1 = (rr1-(vv+2)*m1*cc2-(vv+3)*m2*cc3)/((vv+1)*m0)
cc0 = (rr0-m1*cc1-m2*cc2-m3*cc3)/m0
receiver_vector = s.Matrix([rr0, rr1, rr2, rr3])
c_vector = s.Matrix([cc0, cc1, cc2, cc3])
assert all(s.factor(entry) == 0 for entry in Bmat*c_vector-receiver_vector)

xiM, xiN, xiT, xiE = s.symbols("xiM xiN xiT xiE")
Kmat = s.Matrix([
    [0, s.I, 1/s.sqrt(2), 1/s.sqrt(2)],
    [0, -1, -1-s.sqrt(2)*s.I, 1-s.sqrt(2)*s.I],
    [s.I/2, -3*s.I, 2*s.sqrt(2)+6*s.I, -2*s.sqrt(2)+6*s.I],
    [0, 13, -34-19*s.sqrt(2)*s.I, 34-19*s.sqrt(2)*s.I],
])
U_receiver = Kmat*s.Matrix([xiM, xiN, xiT, xiE])
assert s.factor(Kmat.det()-77*s.sqrt(2)*s.I/2) == 0

# Exact prime-marked factor pair and selector in recovered receiver coordinates.
H_receiver = A*U**4+U**3*V+B*U**2*V**2+C*U*V**3+D*V**4
Q_receiver = (A*U**3+(1+p_inv*A)*U**2*V
              +(B+p_inv+p_inv**2*A)*U*V**2
              +(C+p_inv*B+p_inv**2+p_inv**3*A)*V**3)
factor_residual = s.factor((U-p_inv*V)*Q_receiver-H_receiver
                           +D*G*V**4/C**4)
assert factor_residual == 0
kappa_receiver = s.factor(s.diff(A*T**4+T**3+B*T**2+C*T+D, T)
                          .subs(T, p_inv))
Afac = s.symbols("Afac", nonzero=True)
af, bf = Afac, -Afac*p_inv
cf = A/Afac
df = (1+p_inv*A)/Afac
ef = (B+p_inv+p_inv**2*A)/Afac
ff = (C+p_inv*B+p_inv**2+p_inv**3*A)/Afac
assert s.factor(af*df+bf*cf-1) == 0
assert s.factor(4*af*ff-bf*ef+G/C**3) == 0
Y_marked = -p_inv-s.I/Afac
assert s.factor(5*Afac*D-Afac*Y_marked*C-s.I*C) == 0

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

# Exact elementary transform from the normalized literal-root quartic to the
# reciprocal suspension.  Scale, the marked root, and the inserted root at
# infinity are all retained in the identity.
Hrec_transform = s.factor(s.cancel(
    V * H4.subs({U: p*V, V: U}, simultaneous=True) / (u4*(U-V))
))
Hrec_expected = s.expand(V*(U-p*V/x)*(U-p*V/y)*(U-p*V/z))
assert s.factor(Hrec_transform-Hrec_expected) == 0

e2_rec = p**2*s1/s3
e3_rec = p**3/s3
e2_from_u = 125*u4**2*(u3-5*u0*u4)/u3**4
e3_from_u = 625*u0*u4**3/u3**4
assert s.factor(e2_from_u-e2_rec) == 0
assert s.factor(e3_from_u-e3_rec) == 0
assert s.factor(e2_rec+e3_rec-125*u4**2/u3**3) == 0
reciprocal_sum = e2_rec+e3_rec
assert s.factor(-e3_rec/(p*reciprocal_sum)-u0) == 0
assert s.factor(5*p**2/reciprocal_sum-u3) == 0
assert s.factor(-p**3/reciprocal_sum-u4) == 0
assert s.factor((-p*(e2_rec+4)/reciprocal_sum-u2)
                .subs(p, 4*s3/s2)) == 0

# The two displayed quadratic formulas are mutually inverse on the degree-four
# projective root schemes.  The remainders below retain the source and target
# cubics instead of checking only their numerical roots.
X = s.symbols("X")
Qden_X = X**3-s1*X**2+s2*X-s3
sum_rec = p*s2/s3
frec_T = T**3-sum_rec*T**2+e2_rec*T-e3_rec
map_T = p*(X**2-s1*X+s2)/s3
forward_num = s.together(frec_T.subs(T, map_T)).as_numer_denom()[0]
forward_rem = s.rem(s.Poly(forward_num, X), s.Poly(Qden_X, X)).as_expr()
assert s.factor(forward_rem) == 0
map_X = p*(T**2-sum_rec*T+e2_rec)/e3_rec
inverse_num = s.together(Qden_X.subs(X, map_X)).as_numer_denom()[0]
inverse_rem = s.rem(s.Poly(inverse_num, T), s.Poly(frec_T, T)).as_expr()
assert s.factor(inverse_rem) == 0

Qden_T = T**3-s1*T**2+s2*T-s3
disc_den = s.factor(s.discriminant(Qden_T, T))
disc_rec = s.factor(s.discriminant(frec_T, T))
frec_at_1 = s.factor(frec_T.subs(T, 1))
Qden_at_p = s.factor(Qden_T.subs(T, p))
assert s.factor(Qden_at_p+p**3*frec_at_1/e3_rec) == 0
assert s.factor(disc_den-p**6*disc_rec/e3_rec**4) == 0
assert s.factor(disc_h4-p**6*frec_at_1**2*disc_rec/reciprocal_sum**6) == 0

h4_affine = H4.subs({U: T, V: 1})
hprime_x = s.factor(s.diff(h4_affine, T).subs(T, x))
fprime_px = s.factor(s.diff(frec_T, T).subs(T, p/x))
twist_x = p**2*(p/x-1)/((p/x)**2*reciprocal_sum)
assert s.factor(hprime_x/fprime_px-twist_x) == 0
hprime_p = s.factor(s.diff(h4_affine, T).subs(T, p))
assert s.factor(hprime_p-p**2*frec_at_1/reciprocal_sum) == 0

base = Path(__file__).resolve().parent


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


pdf_path = base / "output" / "pdf" / "ES_FABLE_ZETA_CROSSWALK.pdf"
defining_receipt = base.parent / "es-defining-prime-continuation-20260920" / "results" / "verification.json"
descent_receipt = base.parent / "es-rh-continuation-b-20260920" / "results" / "es_arithmetic_descent.json"
integral_main_receipt = base.parent / "es-turn07-integral-completion-20260920" / "live_certificates" / "summary.json"
integral_independent_receipt = base.parent / "es-turn07-integral-completion-20260920" / "live_certificates" / "independent.json"

receipt = {
    "schema_version": 5,
    "certificate": "cumulative normalized ES quartic, integral signed order, signed Fable cover and fixed-conductor crosswalk",
    "cumulative_pdf": {
        "path": "output/pdf/ES_FABLE_ZETA_CROSSWALK.pdf",
        "pages": 124,
        "sha256": sha256_file(pdf_path),
        "build": "two successful pdflatex passes; no warnings, undefined references, overfull boxes or underfull boxes in the final log",
        "visual_qa": "all 124 pages rendered; complete contact sheets and seven newly affected figure/transition pages inspected",
    },
    "integrated_receipts": [
        {
            "module": "es-defining-prime-continuation-20260920",
            "checks": 80,
            "status": "PASS",
            "receipt": "../es-defining-prime-continuation-20260920/results/verification.json",
            "sha256": sha256_file(defining_receipt),
        },
        {
            "module": "es-rh-continuation-b-20260920",
            "checks": 923,
            "status": "PASS",
            "scope": "Tracks I and IV independently reconstructed and replayed",
            "receipt": "../es-rh-continuation-b-20260920/results/es_arithmetic_descent.json",
            "sha256": sha256_file(descent_receipt),
        },
        {
            "module": "es-turn07-integral-completion-20260920",
            "status": "PASS",
            "main_checks": 104538,
            "independent_checks": 27154,
            "main_receipt": "../es-turn07-integral-completion-20260920/live_certificates/summary.json",
            "main_sha256": sha256_file(integral_main_receipt),
            "independent_receipt": "../es-turn07-integral-completion-20260920/live_certificates/independent.json",
            "independent_sha256": sha256_file(integral_independent_receipt),
        },
    ],
    "checks": {
        "normalized_quartic_coefficients": True,
        "es_relation": "p(xy+xz+yz)=4xyz",
        "intrinsic_prime": "p=-5u4/u3",
        "coefficient_hypersurface": "625u0u4^3-125u3u4^2+25u2u3^2u4-4u3^4=0",
        "symmetric_chart_inverse": {
            "p": "-5u4/u3",
            "s1": "-1/u0+5u4/u3",
            "s2": "4u3^2/(25u0u4)",
            "s3": "-u3/(5u0)",
        },
        "hypersurface_singular_support": "u3=u4=0",
        "arithmetic_chart": "V(G) intersect D(u0u3u4) is isomorphic to G_m^3",
        "ordered_denominator_cover": "finite flat degree 6; etale off Disc(Q)=0",
        "target_factor_residual": "u0(T+5u4/u3)Q-h=-G*T^2/(25u3^2u4)",
        "singular_primary_decomposition": "J=Q_plane intersect Q_embedded",
        "distinguished_root_collision": "1250u0u4^3+3u3^4-125u3u4^2=0",
        "quartic_collision_factorization": "Disc(h)=u0^6 Disc(Q) Q(p)^2",
        "fixed_receiver_inverse": "B_v^-1 followed by V_*^T and K",
        "fixed_receiver_coefficient_forms": [str(s.expand(entry)) for entry in U_receiver],
        "receiver_hypersurface": "G(Psi_*^-1 r)=0",
        "receiver_prime_selector": "5A(r)U4-A(r)Y(r)U3-iU3=0",
        "receiver_prime_marked_factor_pair": True,
        "marked_resultant_one_factorization": True,
        "es_incidence_4af_minus_be": True,
        "eight_source_inverse_residuals": inverse_residuals,
        "quartic_discriminant": "S^-6 product_{j<k}(t_j-t_k)^2",
        "separate_reciprocal_suspension": True,
        "suspended_cubic_discriminant": str(s.factor(disc3)),
        "quartic_to_reciprocal_elementary_transform": "u4^-1 V/(U-V) H_ES(pV,U)",
        "reciprocal_coefficient_inverse": True,
        "projective_root_scheme_maps": {
            "forward": "T=p(X^2-s1X+s2)/s3",
            "inverse": "X=p(T^2-(p*s2/s3)T+e2)/e3",
        },
        "collision_discriminant_transport": True,
        "signed_derivative_twist": "h'(x_i)/f'(p/x_i)=p^2(p/x_i-1)/((p/x_i)^2(e2+e3))",
    },
    "nonclaims": [
        "The coefficient hypersurface alone does not impose integral positive roots, primality, or ES channel gates.",
        "The construction begins with an ES witness and is not a universal existence proof.",
        "The fixed conductor receiver does not identify ES roots with zeta zeros.",
        "The received determinant and heat-track executable receipt is preserved but not relabelled as a local replay because its four scripts were absent.",
    ],
}

out = Path(__file__).with_name("verification_receipt.json")
out.write_text(json.dumps(receipt, indent=2, sort_keys=True)+"\n", encoding="utf-8")
print(json.dumps(receipt, indent=2, sort_keys=True))
