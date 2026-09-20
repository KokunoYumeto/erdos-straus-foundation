"""Exact identities underlying global inverse/fibre/nonproper calculations."""
import sympy as s
from verify_four_labels import a, y, z, w, i, P

r, A, B, C, D, x = s.symbols("r A B C D x")
Qparam = s.Matrix([
    a,
    -r-i/a,
    A/a**3+2*r/a+3*i/a**2,
    7*i*r**2/a+(B-17*r+A*r**2)/a**2-13*i/a**3-2*A/a**4,
])
u3 = a**-2-4*A*r**3-3*r**2-2*B*r
u4 = 3*A*r**4+2*r**3+B*r**2-r/a**2
target = s.Matrix([A, B, u3, u4])
actual = P.subs(dict(zip([a, y, z, w], Qparam)), simultaneous=True)
assert (actual-target).applyfunc(s.factor) == s.zeros(4, 1)
assert s.factor(Qparam.jacobian([a, r, A, B]).det()) == -1/a**5
assert s.factor(target.jacobian([a, r, A, B]).det()) == 2/a**5
print("Complete inverse parameterization verified.")
print("Source parameter Jacobian=-a^-5; target parameter Jacobian=2a^-5.")

q_inf = s.Matrix([0, B, i*(7*B**2-C)/2, 11*B**3-2*B*C-D])
assert (P.subs(dict(zip([a, y, z, w], q_inf)), simultaneous=True)
        -s.Matrix([0, B, C, D])).applyfunc(s.expand) == s.zeros(4, 1)
print("Entire u0=0 chart section verified.")

h = A*x**4+x**3+B*x**2+C*x+D
disc = s.discriminant(h, x)
assert s.expand(disc.subs(A, 0)-s.discriminant(x**3+B*x**2+C*x+D, x)) == 0
sq_h = A*(x**2+x/(2*A)+C)**2
assert s.expand(h.subs({B: 1/(4*A)+2*A*C, D: A*C**2})-sq_h) == 0
print("Discriminant boundary and omitted square surface verified.")

delta, gamma = s.symbols("delta gamma", positive=True)
u_rho = {
    A: -s.Rational(1, 2),
    B: delta**2-gamma**2-s.Rational(3, 4),
    C: gamma**2-delta**2+s.Rational(1, 4),
    D: -s.Rational(1, 32)-(gamma**2-delta**2)/4-(delta**2+gamma**2)**2/2,
}
h_rho = -s.Rational(1, 2)*((x-s.Rational(1, 2))**4
                 +2*(gamma**2-delta**2)*(x-s.Rational(1, 2))**2
                 +(delta**2+gamma**2)**2)
assert s.expand(h.subs(u_rho)-h_rho) == 0
assert s.factor(disc.subs(u_rho)-64*delta**4*gamma**4*(delta**2+gamma**2)**2) == 0
for eps in [-1, 1]:
    for eta in [-1, 1]:
        root = s.Rational(1, 2)+eps*delta+i*eta*gamma
        assert s.expand(h_rho.subs(x, root)) == 0
        assert s.expand(s.diff(h_rho, x).subs(x, root)
                        -4*delta*gamma*(eps*gamma-i*eta*delta)) == 0
print("All four original quartet roots, signed scaling equations, and discriminant verified.")
print("All global inverse identity checks passed.")
