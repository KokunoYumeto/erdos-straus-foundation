"""Exact algebraic checks for FC1--25; no numerical zeta zero is asserted."""
from pathlib import Path
import hashlib
import itertools
import json
import sympy as S

base = Path(__file__).resolve().parent
checks = {}
one = S.ones(4, 1)
Q = S.ones(4, 4)/12 - S.eye(4)/3
checks['locale_rank'] = int(Q.rank())
assert Q.nullspace() == [one]
checks['locale_kernel'] = [str(x) for x in one]
for j in range(4):
    ej = S.eye(4)[:, j]
    qa = -S.Rational(2, 3)/S.sqrt(3)*(ej-one/4)
    assert S.simplify(one/4 - 3*S.sqrt(3)*qa/2-ej) == S.zeros(4, 1)
delta, gamma = S.symbols('delta gamma', positive=True)
rho = [S.Rational(1,2)+a*delta+S.I*b*gamma
       for a,b in [(1,1),(1,-1),(-1,1),(-1,-1)]]
V = S.Matrix([[r**n for r in rho] for n in range(4)])
det = S.factor(V.det())
assert det == -64*delta**2*gamma**2*(delta**2+gamma**2)
checks['quartet_jet_determinant'] = str(det)
t = S.symbols('t1:5')
q0 = t[0]*t[3]-t[1]*t[2]
orbit = {}
stabilizer = []
for p in itertools.permutations(range(4)):
    value = S.expand(q0.xreplace(dict(zip(t,[t[j] for j in p]))))
    pair = min(str(value),str(-value))
    orbit.setdefault(pair,[]).append(p)
    if value in (q0,-q0):
        stabilizer.append(p)
assert len(orbit) == 3 and len(stabilizer) == 8
checks['pairing_orbit_size'] = len(orbit)
checks['pairing_stabilizer_size'] = len(stabilizer)
monomials = []
for k1 in range(9):
    for k2 in range(9-k1):
        for k3 in range(9-k1-k2):
            k4=8-k1-k2-k3
            monomials.append((k1,k2,k3,k4))
assert len(monomials)==165
indices = {(k1+k2,k1+k3) for k1,k2,k3,k4 in monomials}
assert len(indices)==81
checks['degree8_dimension_rank_kernel'] = [165,81,84]

# Actual weighted-shift inverse recurrence, with an order-two symbol.
# This checks the inverse formula; this explicit test symbol is not
# claimed to be the original period conductor.
D,v,b=3,2,S.Rational(1,2)
g=[S.Rational(2,3),S.Rational(-5,7),S.Rational(11,13),S.Rational(17,19)]
h=[1/g[0]]
for n in range(1,D+1):
    h.append(S.simplify(-sum(g[j]*h[n-j] for j in range(1,n+1))/g[0]))
def toeplitz(c):
    return S.Matrix(D+1,D+1,lambda i,j:c[j-i] if i<=j else 0)
weights=[S.sqrt(S.factorial(n)/S.rf(b,n)) for n in range(D+v+1)]
left=S.diag(*weights[:D+1]); right=S.diag(*weights[v:])
A=left.inv()*toeplitz(g)*right
inv=right.inv()*toeplitz(h)*left
assert S.simplify(A*inv)==S.eye(D+1)
assert S.simplify(A.det()-g[0]**(D+1)*right.det()/left.det())==0
checks['weighted_inverse_exact_test'] = True

# Prove finite instances of the order-stratum rank formula with exact
# monomial matrices. The universal proof is FC25.
count=0
for v0 in range(3):
    for DD in range(5):
        N=DD+v0
        for actual in range(v0,N+3):
            T=S.Matrix(DD+1,DD+1,lambda i,j:
                S.binomial(j+v0,actual) if i==j+v0-actual else 0)
            assert T.rank()==max(DD+1-(actual-v0),0)
            count+=1
checks['order_jump_exact_instances'] = count

(base/"verification.json").write_text(json.dumps(checks,indent=2)+"\n",encoding="utf-8")
print(json.dumps(checks,indent=2))
