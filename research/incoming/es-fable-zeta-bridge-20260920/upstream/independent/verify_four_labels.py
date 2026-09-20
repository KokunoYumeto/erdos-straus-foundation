"""Exact arithmetic verification of the four marked source points.

The input polynomial and coordinates are transcribed from the original
ES--Fable reader, theorem explicit-four-time-Jacobian-collision.
All computations take place symbolically over Q(i, sqrt(2)); no numeric
sampling substitutes for the full Jacobian determinant calculation.
"""
import sympy as s

a, y, z, w = s.symbols("a y z w")
i, r = s.I, s.sqrt(2)
P = s.Matrix([
    a**3*z+2*a**2*y-i*a,
    -a**3*y**2*z-2*i*a**2*y*z+a**2*w-2*a**2*y**3-10*i*a*y**2+3*a*z+y,
    2*a**3*y**3*z+6*i*a**2*y**2*z+2*a**2*w*y+4*a**2*y**4
    +2*i*a*w-4*i*a*y**3-2*a*y*z+2*i*z+7*y**2,
    2*a**3*y**4*z+8*i*a**2*y**3*z+a**2*w*y**2+4*a**2*y**5
    +2*i*a*w*y+7*i*a*y**4-10*a*y**2*z-4*i*y*z-w-3*y**3,
])
points = {
    "M": s.Matrix([0, 0, i/2, 0]),
    "N": s.Matrix([i, -1, -3*i, 13]),
    "T": s.Matrix([1/r, -1-r*i, 2*r+6*i, -34-19*r*i]),
    "E": s.Matrix([1/r, 1-r*i, -2*r+6*i, 34-19*r*i]),
}
det_j = s.factor(P.jacobian([a, y, z, w]).det())
assert det_j == -2, det_j
print("Full polynomial Jacobian determinant:", det_j)
for label, q in points.items():
    output = P.subs(dict(zip([a, y, z, w], q))).applyfunc(s.simplify)
    assert output == s.Matrix([0, 0, -1, 0]), (label, output)
    print(label, "maps to", list(output))
Q = s.Matrix.hstack(*points.values())
det_q = s.simplify(Q.det())
assert s.simplify(det_q - 77*r*i/2) == 0, det_q
print("Ordered coordinate-column determinant:", det_q)

delta, gamma = s.symbols("delta gamma", real=True)
rho = [s.Rational(1, 2)+delta+i*gamma,
       s.Rational(1, 2)+delta-i*gamma,
       s.Rational(1, 2)-delta+i*gamma,
       s.Rational(1, 2)-delta-i*gamma]
V = s.Matrix([[root**n for root in rho] for n in range(4)])
det_v = s.factor(V.det())
assert s.expand(det_v + 64*delta**2*gamma**2*(delta**2+gamma**2)) == 0
print("Ordered quartet jet determinant:", det_v)
print("All exact checks passed.")
