#!/usr/bin/env python3
"""Finite exact checks; Python 3.10+ and SymPy. No network or source writes.
The README's all-degree proof is not replaced by these finite instances.
"""
import json
import sympy as s

rows = []
def check(name, value):
    entries = list(value) if isinstance(value, s.MatrixBase) else [value]
    if any(s.simplify(s.expand(e)) != 0 for e in entries):
        raise RuntimeError(name)
    rows.append({"name": name, "entries": len(entries), "pass": True})

def shift(n, H):
    d = H.rows
    T = s.zeros(n*d)
    for j in range(n-1):
        T[(j+1)*d:(j+2)*d, j*d:(j+1)*d] = s.eye(d)
    T[:d, (n-1)*d:n*d] = H
    return T

h, z = s.symbols('h z')
for n in range(1, 9):
    T = shift(n, s.Matrix([[h]]))
    check(f'full turn n={n}', T**n-h*s.eye(n))
    check(f'determinant n={n}', (s.eye(n)-z*T).det()-(1-h*z**n))
H = s.Matrix([[2, 1], [0, 3]])
for n in range(1, 5):
    T = shift(n, H)
    check(f'matrix full turn n={n}', T**n-s.diag(*([H]*n)))
    check(f'matrix determinant n={n}', (s.eye(2*n)-z*T).det()-(s.eye(2)-z**n*H).det())
for m, n in [(2, 2), (2, 3), (3, 2), (3, 3)]:
    P = s.zeros(m*n)
    for a in range(m):
        for b in range(n):
            P[a+m*b, a*n+b] = 1
    check(f'composition {m},{n}', P*shift(m, shift(n, s.Matrix([[h]])))*P.T-shift(m*n, s.Matrix([[h]])))

a, b, c, t = s.symbols('a b c t', real=True)
w = (-1+s.sqrt(3)*s.I)/2
T = a+b+c
Z = a+w*b+w**2*c
Delta = 4*(a*b+a*c+b*c)-a*a-b*b-c*c
check('character defect', Delta-T*T+2*Z*s.conjugate(Z))
for j, qj in enumerate([a, b, c]):
    check(f'character inverse {j}', (T+w**(-j)*Z+w**j*s.conjugate(Z))/3-qj)
check('cyclic action', c+w*a+w**2*b-w*Z)
check('cubic character invariant', 27*a*b*c-(T**3-3*T*Z*s.conjugate(Z)+Z**3+s.conjugate(Z)**3))
D = -1-6*a*a+6*a*b-b*b+4*b
L = 2-4*b
q = s.Matrix([(-D-L)/D, -L*a/D, -L*(b-a)/D])
check('original chart level', s.factor(2*sum(q)**2-3*q.dot(q)+1))
check('original a recovered', s.factor(q[1]/(q[0]+1)-a))
check('original b recovered', s.factor((q[1]+q[2])/(q[0]+1)-b))
ct = (1-t*t)/(1+t*t)
st = 2*t/(1+t*t)
R = s.Matrix([[ct, -st, 0], [st, ct, 0], [0, 0, 1]])
Dq = s.diag(a, b, c)
X = R*Dq*R.T
check('rotation is orthogonal', R.T*R-s.eye(3))
check('rotation determinant', R.det()-1)
check('trace preserved', s.trace(X)-T)
check('quadratic trace preserved', s.trace(X*X)-a*a-b*b-c*c)
check('cubic determinant preserved', X.det()-a*b*c)
check('defect preserved', 2*s.trace(X)**2-3*s.trace(X*X)-Delta)
check('ordered inverse', R.T*X*R-Dq)
Xexample = s.Matrix([[s.Rational(62,175),-s.Rational(12,25),0],[-s.Rational(12,25),s.Rational(13,175),0],[0,0,s.Rational(10,7)]])
check('literal rational example', X.subs({a:-s.Rational(2,7),b:s.Rational(5,7),c:s.Rational(10,7),t:s.Rational(1,2)})-Xexample)
check('literal example level', 2*s.trace(Xexample)**2-3*s.trace(Xexample*Xexample)+1)
print(json.dumps({"status":"pass","sympy":s.__version__,"groups":len(rows),"scalar_entries":sum(r["entries"] for r in rows),"checks":rows,"scope":"Finite exact identities only; not a GRH, ES, physical-mass or Lean proof."},indent=2))
