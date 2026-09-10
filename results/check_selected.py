#!/usr/bin/env python3
"""Exact finite checks for selected PolyClank proof notes.

This standalone checker does not execute archived code or verify a full
research programme. Standard-library Python only. No assert statements;
failed conditions raise even when Python runs with -O.
"""
from __future__ import annotations
import json
from collections import Counter
from fractions import Fraction
from itertools import combinations, product


def require(condition: bool, explanation: str) -> None:
    if not condition:
        raise ValueError(explanation)


def determinant(matrix: list[list[int]]) -> Fraction:
    a = [[Fraction(v) for v in row] for row in matrix]
    n, value = len(a), Fraction(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            value *= -1
        v = a[j][j]
        value *= v
        for i in range(j + 1, n):
            ratio = a[i][j] / v
            for k in range(j, n):
                a[i][k] -= ratio * a[j][k]
    return value


def main() -> None:
    report: dict[str, object] = {
        "kind": "exact finite cross-checks, not general proof certification",
        "formal_prover_run": False,
        "external_code_executed": False,
        "independent_reviewers": 0,
        "checks": {},
    }
    checks = report["checks"]
    require(isinstance(checks, dict), "Internal report type")

    # The six shifted copies of each weighted defect are a basis over Q.
    dets = []
    for k in range(6):
        f = [0] * 6
        f[3] += 1
        f[(3-k) % 6] += 2
        m = [[f[(row-col) % 6] for col in range(6)] for row in range(6)]
        d = determinant(m)
        require(d != 0 and sum(f) == 3, "Six-sector defect check failed")
        dets.append(str(d))
    checks["R02"] = {"passed": True, "cases": 6, "translation_matrix_determinants": dets,
                      "trivial_character_value": 3}

    primes = [2,3,5,7,11,13,17,19,23,29,31,41,47,59,71]
    fibres = {r: [p for p in primes if p % 5 == r] for r in range(5)}
    sizes = [len(fibres[0]), len(fibres[1])+len(fibres[4]), len(fibres[2])+len(fibres[3])]
    require(sizes == [1,7,7] and len(set(primes)) == 15, "Ogg partition")
    checks["R03"] = {"passed": True, "residue_fibres": fibres,
                      "coarse_sizes": sizes, "after_adjoining_separate_level_one": [1,1,7,7]}

    p, r, t, u, s = 8803369, 107, 6, 21, 47176870
    a = (p+r)//4
    equalities = {"p_mod_107": p % r, "inverse_21_mod_107": pow(u,-1,r),
                  "S5_mod_107": s % r, "pa_mod_107": (p*a)%r,
                  "21_S5_mod_107": (u*s)%r, "a_mod_107": a%r,
                  "minus_21_S5_mod_107": (-u*s)%r, "11_squared_mod_107": 121%r,
                  "inverse_minus_6_S5_mod_107": pow(-t*s,-1,r)}
    require((p+r)%4 == 0 and p%r == pow(u,-1,r) == 51, "BB anchor")
    require(s%r == p*a%r == 35 and u*s%r == a%r == 93, "BB products")
    require((-u*s)%r == 121%r == 14 and pow(-t*s,-1,r) == 27, "BB signed relations")
    checks["R04"] = {"passed": True, "values": equalities,
                      "scope": "arithmetic of fixed supplied integers; no Busy Beaver maximality or complexity theorem"}

    def odd_step(n: int) -> int:
        m = 3*n+1
        while m % 2 == 0:
            m //= 2
        return m
    for n in range(1,2000,2):
        require(odd_step(4*n+1) == odd_step(n), "Odd-step fibre identity")
    residue_map = {n: (4*n+1)%12 for n in [1,3,5,7,9,11]}
    require(list(residue_map.values()) == [5,1,9,5,1,9], "Odd residue map")
    checks["R05"] = {"passed": True, "odd_examples": 1000, "mod12_map": residue_map,
                      "scope": "examples accompany a general algebraic proof; not trajectory convergence"}

    A = {(35*r+11*s+33*t)%53 for r,s,t in product(range(-2,3),range(-2,3),range(-1,2))}
    D = set(range(53))-A
    expected = {(23+42*j)%53 for j in range(10)}
    differences = {(x-y)%53 for x in D for y in D}
    require(len(A) == 43 and D == expected, "Deficit progression")
    require(len(differences) == 19 and 6 not in differences, "Difference set")
    require({(x+29)%53 for x in A}|{(x+23)%53 for x in A} == set(range(53)), "Saturation")
    checks["R06"] = {"passed": True, "input_triples": 75, "support": sorted(A),
                      "deficit": sorted(D), "differences": sorted(differences),
                      "scope": "one finite support calculation"}

    # This verifies integer recurrences, not analytic norm bounds by sampling.
    pp, qq = 1, 0
    for j in range(40):
        require(pp*pp-2*qq*qq == (-1)**j, "Pell identity")
        pp, qq = pp+2*qq, pp+qq
    checks["R07"] = {"passed": True, "pell_recurrence_cases": 40,
                      "scope": "integer ingredients only; general sharp estimate has a written proof"}

    # D, and two A2 basis vectors, in one coordinate of the triple lattice.
    basis = [[1,1,0],[1,-1,1],[1,0,-1]]
    require(abs(determinant(basis)) == 3, "Triple lattice index")
    require(determinant([[2,-1],[-1,2]]) == 3, "A2 determinant")
    checks["R08"] = {"passed": True, "one_coordinate_index": 3,
                      "scope": "basis calculation; arbitrary-rank statements proved in the note"}

    # Finite Z/6 group illustrations of Kneser's actual stabilizer bound.
    H = set(range(6)); subsets = [set(i for i in range(6) if mask>>i & 1) for mask in range(1,64)]
    tested = 0
    for X in subsets:
        for Y in subsets:
            B = {(x+y)%6 for x in X for y in Y}
            K = {k for k in H if {(b+k)%6 for b in B} == B}
            qsize = 6//len(K)
            xk = len({(x+k)%6 for x in X for k in K})//len(K)
            yk = len({(y+k)%6 for y in Y for k in K})//len(K)
            require(len(B)//len(K) >= xk+yk-1, "Kneser finite illustration")
            for t0 in H-B:
                require(1+(xk-1)+(yk-1)+1-qsize <= 0, "Miss-surplus illustration")
            tested += 1
    checks["R09"] = {"passed": True, "nonempty_subset_pairs_C6": tested,
                      "scope": "finite illustrations only; general theorem uses cited Kneser theorem"}

    c2 = [((0,0,0,0),0), ((1,1,1,1),0)]
    for a,b in combinations(range(4),2):
        c2.append((tuple(int(i in (a,b)) for i in range(4)), a^b))
    c3 = [tuple((a*u+b*v)%3 for u,v in zip((1,1,1,0),(1,2,0,1))) for a,b in product(range(3),repeat=2)]
    glue = {(tuple((3*u[i]+2*v[i])%6 for i in range(4)), y) for u,y in c2 for v in c3}
    require(len(glue) == 72, "Glue cardinality")
    for x,y in glue:
        qform = sum(Fraction(5*k*k,6) for k in x) + int(y!=0)
        require(qform.denominator == 1 and qform.numerator % 2 == 0, "Glue isotropy")
        for v,w in glue:
            require((tuple((x[i]+v[i])%6 for i in range(4)), y^w) in glue, "Glue closure")
    cost_counts = Counter(sum(Fraction(k*(6-k),6) for k in x)+int(y!=0) for x,y in glue)
    require(cost_counts == {Fraction(0):1, Fraction(4):46, Fraction(6):25}, "Glue cost multiplicities")
    costs = sorted(k for k in cost_counts if k)
    require(costs == [Fraction(4),Fraction(6)], "Nonzero glue costs")
    checks["R10"] = {"passed": True, "glue_elements": 72, "pairwise_closure_checks": 5184,
                      "nonzero_coset_costs": [str(v) for v in costs],
                      "cost_multiplicities": {str(k):v for k,v in sorted(cost_counts.items())},
                      "scope": "exact finite quadratic-module data; not all lattice or modular conclusions"}
    report["passed_check_families"] = len(checks)
    report["R01_scope"] = "Written semiring proof; no separate computational test claimed"
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
