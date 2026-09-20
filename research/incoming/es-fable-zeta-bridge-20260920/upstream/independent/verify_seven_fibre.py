"""Exact complete-fibre elimination and the two distinct involutions."""
import sympy as s
from verify_four_labels import a, y, z, w, i, r, P, points, Q

variables = [a, y, z, w]
h = s.Matrix([0, 0, -1, 0])
J = s.diag(-1, -1, 1, -1)
Jout = s.diag(-1, -1, 1, -1)
j_sub = dict(zip(variables, J*s.Matrix(variables)))
assert (P.subs(j_sub, simultaneous=True)-Jout*P).applyfunc(s.expand) == s.zeros(4, 1)
all_points = dict(points)
all_points.update({"J"+label: J*points[label] for label in ["N", "T", "E"]})
for label, q in all_points.items():
    out = P.subs(dict(zip(variables, q))).applyfunc(s.simplify)
    assert out == h, (label, out)
    print(label, list(q), "maps to", list(out))
assert len(set(tuple(q) for q in all_points.values())) == 7

z_sol = (i-2*a*y)/a**2
w_sol = i*(7*a**2*y**2-3*i*a*y-3)/a**3
residual = (P-h).subs({z: z_sol, w: w_sol}, simultaneous=True).applyfunc(s.factor)
expected = s.Matrix([0, 0, -(3*a**2*y**2-a**2+6*i*a*y-4)/a**2,
                     -(a*y+i)*(2*a**2*y**2+4*i*a*y-3)/a**3])
assert (residual-expected).applyfunc(s.factor) == s.zeros(4, 1)
print("Exact a!=0 residual:", list(residual))

Sigma = s.Matrix([-a, y+2*i/a, 6*i/a**2-z,
                  w-14*i*y**2/a+28*y/a**2+40*i/a**3])
sigma_sub = dict(zip(variables, Sigma))
assert (Sigma.subs(sigma_sub, simultaneous=True)-s.Matrix(variables)).applyfunc(s.factor) == s.zeros(4, 1)
assert (P.subs(sigma_sub, simultaneous=True)-P).applyfunc(s.factor) == s.zeros(4, 1)

b = i+a*y
c = -i+2*a*y+a**2*z
d = -i*y-a*(i*z+2*y**2)-a**2*y*z
e = 2*z-7*i*y**2+a*w
f = i*w+3*i*y**3-4*y*z+a*(6*i*y**2*z+w*y+4*y**4)+2*a**2*y**3*z
factor_state = s.Matrix([a, b, c, d, e, f])
assert (factor_state.subs(sigma_sub, simultaneous=True)+factor_state).applyfunc(s.factor) == s.zeros(6, 1)
print("Sigma^2=identity, P Sigma=P, Phi Sigma=-Phi: exact identities passed.")
for label, partner in [("N", "JN"), ("T", "JE"), ("E", "JT")]:
    out = Sigma.subs(dict(zip(variables, points[label]))).applyfunc(s.simplify)
    assert out == all_points[partner]
    print("Sigma", label, "=", partner)

JK = (Q.inv()*J*Q).applyfunc(s.simplify)
expected_JK = s.Matrix([[1, -12, 24-8*r*i, 24+8*r*i],
                       [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]])
assert (JK-expected_JK).applyfunc(s.simplify) == s.zeros(4)
assert h == 2*i*points["M"]
print("J in the marked-column frame:", expected_JK)
print("h = 2 i q_M; all seven-point and involution checks passed.")
