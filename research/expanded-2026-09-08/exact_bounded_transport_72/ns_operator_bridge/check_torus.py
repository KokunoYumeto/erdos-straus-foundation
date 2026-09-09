"""Exact independent finite enumeration for torus_cover_lemma.tex; no Lean.

Uses rational torus points and exact cyclotomic polynomial reduction for
character averages. It preserves each original prime/exponent allocation.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
from math import gcd, lcm
from pathlib import Path
import hashlib
import json


def jmap(z, n=None):
    a = (3*z[0] + z[1], z[0] + 5*z[1])
    return tuple(v % n for v in a) if n else tuple(v % 1 for v in a)


def formula_fibre(a, b, n):
    g = gcd(n, 14)
    if (5*a-b) % g:
        return set()
    reduced_n = n//g
    x0 = 0 if reduced_n == 1 else (
        pow(14//g, -1, reduced_n)*((5*a-b)//g)) % reduced_n
    return {((x0+k*reduced_n) % n,
             (a-3*x0-3*k*reduced_n) % n) for k in range(g)}


def full_torus_fibre(z):
    a, b = z
    return {((5*a-b+k)/14 % 1,
             (a-3*(5*a-b+k)/14) % 1) for k in range(14)}


def trim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def divrem(p, divisor):
    p = p[:]
    out = [0]*max(1, len(p)-len(divisor)+1)
    assert divisor[-1] == 1
    while len(p) >= len(divisor) and any(p):
        k, c = len(p)-len(divisor), p[-1]
        out[k] = c
        for i, d in enumerate(divisor):
            p[i+k] -= c*d
        trim(p)
    return trim(out), trim(p)


@lru_cache(None)
def cyclotomic(n):
    p = [-1]+[0]*(n-1)+[1]
    for d in range(1, n):
        if n % d == 0:
            p, rem = divrem(p, list(cyclotomic(d)))
            assert rem == [0]
    return tuple(p)


def root_sum_integer(phases, expected):
    """Prove the exact root sum equals an integer by polynomial division."""
    denominator = 1
    counts = Counter(q % 1 for q in phases)
    for q in counts:
        denominator = lcm(denominator, q.denominator)
    poly = [0]*denominator
    for q, count in counts.items():
        poly[int(q*denominator)] += count
    poly[0] -= expected
    _, remainder = divrem(trim(poly), list(cyclotomic(denominator)))
    assert remainder == [0], (denominator, remainder, expected)


def characters(r):
    """Enumerate exact characters as rational phases, retaining all units."""
    units = [u for u in range(1, r) if gcd(u, r) == 1]
    subgroup, chars = {1}, [{1: Q(0)}]
    for g in units:
        if g in subgroup:
            continue
        power, order = g, 1
        while power not in subgroup:
            power = power*g % r
            order += 1
        enlarged = {h*pow(g, k, r) % r
                    for h in subgroup for k in range(order)}
        new = []
        for chi in chars:
            for k in range(order):
                alpha = (chi[power]+k)/order
                out = {}
                for h in subgroup:
                    for j in range(order):
                        u = h*pow(g, j, r) % r
                        assert u not in out
                        out[u] = (chi[h]+j*alpha) % 1
                new.append(out)
        subgroup, chars = enlarged, new
    assert subgroup == set(units) and len(chars) == len(units)
    assert len({tuple(c[u] for u in units) for c in chars}) == len(units)
    for c in chars:
        for u, v in product(units, repeat=2):
            assert c[u*v % r] == (c[u]+c[v]) % 1
    for u in units:
        root_sum_integer([c[u] for c in chars], len(units) if u == 1 else 0)
    return units, chars


def fact(n):
    out, d = [], 2
    while d*d <= n:
        v = 0
        while n % d == 0:
            n //= d
            v += 1
        if v:
            out.append((d, v))
        d += 1
    if n > 1:
        out.append((n, 1))
    return out


def packet(a, r):
    fs = fact(a)
    rows = []
    for exps in product(*(range(2*v+1) for _, v in fs)):
        value = 1
        for (prime, _), e in zip(fs, exps):
            value *= prime**e
        rows.append((exps, value, value % r))
    assert len({v for _, v, _ in rows}) == len(rows)
    assert {v for _, v, _ in rows} == {v for v in range(1, a*a+1) if a*a % v == 0}
    return rows, Counter(u for _, _, u in rows)


def ringmul(x, y):
    return x[0]*y[0]+2*x[1]*y[1], x[0]*y[1]+x[1]*y[0]


def run():
    report = {"status": "passed", "arithmetic": "integer, Fraction, exact cyclotomic remainder"}
    torsion_targets = torsion_sources = 0
    for n in range(1, 49):
        points = list(product(range(n), repeat=2))
        direct = defaultdict(set)
        for z in points:
            direct[jmap(z, n)].add(z)
        for a, b in points:
            assert direct[(a, b)] == formula_fibre(a, b, n)
            torsion_targets += 1
        assert len(direct[(0, 0)]) == gcd(n, 14)
        assert sum(bool(v) for v in direct.values()) == n*n//gcd(n, 14)
        torsion_sources += len(points)
    report["torsion"] = {"N_range": [1, 48], "targets": torsion_targets,
                          "sources": torsion_sources}

    full_points = 0
    for n in range(1, 21):
        targets = {(Q(a, n), Q(b, n)) for a, b in product(range(n), repeat=2)}
        preimage = set()
        for z in targets:
            fibre = full_torus_fibre(z)
            assert len(fibre) == 14 and all(jmap(w) == z for w in fibre)
            assert not preimage.intersection(fibre)
            preimage.update(fibre)
        assert len(preimage) == 14*n*n
        assert all((14*n*q).denominator == 1 for z in preimage for q in z)
        full_points += len(preimage)
    report["full_preimage"] = {"N_range": [1, 20], "lifted_points": full_points}

    power_targets = 0
    for n in range(1, 17):
        points = list(product(range(n), repeat=2))
        iterates = {z: z for z in points}
        recursive = {z: {z} for z in points}
        for m in range(6):
            direct = defaultdict(set)
            for source, target in iterates.items():
                direct[target].add(source)
            for target in points:
                assert direct[target] == recursive[target]
                power_targets += 1
            iterates = {z: jmap(value, n) for z, value in iterates.items()}
            recursive = {z: set().union(*(formula_fibre(*w, n) for w in values))
                         for z, values in recursive.items()}
    report["powers"] = {"N_range": [1, 16], "m_range": [0, 5], "targets": power_targets}

    eigen_tests = 0
    for m in range(7):
        for n1, n2 in product(range(-4, 5), repeat=2):
            freq = (n1, n2)
            for _ in range(m):
                freq = (3*freq[0]+freq[1], freq[0]+5*freq[1])
            for v, lam in [(((1, 0), (1, -1)), (4, -1)),
                           (((-1, 1), (1, 0)), (4, 1))]:
                before = (v[0][0]*n1+v[1][0]*n2, v[0][1]*n1+v[1][1]*n2)
                after = (v[0][0]*freq[0]+v[1][0]*freq[1],
                         v[0][1]*freq[0]+v[1][1]*freq[1])
                expected = before
                for _ in range(m):
                    expected = ringmul(expected, lam)
                assert after == expected
                assert before != (0, 0) or (n1, n2) == (0, 0)
                eigen_tests += 1
    report["directional_frequency_tests"] = eigen_tests

    fixtures = [(13, 4), (13, 5), (37, 10), (37, 11), (37, 12),
                (61, 16), (61, 17), (61, 18), (61, 19), (373, 95)]
    fixture_results = []
    for p, a in fixtures:
        assert all(p % d for d in range(2, int(p**0.5)+1))
        h, r = (p-1)//12, 4*a-p
        assert p == 12*h+1 and 3*h+1 <= a <= 9*h and gcd(a, r) == 1
        units, chars = characters(r)
        rows, coeff = packet(a, r)
        d = len(units)
        targets = [(-pow(4, -1, r)) % r, (-a) % r]
        out = {"p": p, "a": a, "R": r, "exponent_allocations": len(rows), "targets": []}
        for target in targets:
            # Evaluate the exact character sums independently of the coefficient formula.
            qs = [value*pow(target, -1, r) % r for _, _, value in rows]
            root_sum_integer([c[q] for c in chars for q in qs], d*coeff[target])
            root_sum_integer([(3*c[q]+e[q]) % 1
                              for c, e in product(chars, repeat=2) for q in qs],
                             d*d*coeff[target])
            joint = sum(coeff[target*u % r]*coeff[target*pow(u, -3, r) % r]
                        for u in units if pow(u, 14, r) == 1)
            root_sum_integer([(3*c[q]+e[q]+c[t]+5*e[t]) % 1
                              for c, e in product(chars, repeat=2)
                              for q, t in product(qs, repeat=2)], d*d*joint)
            row = (1, 0)
            power_results = []
            for m in range(6):
                dm = gcd(*row)
                predicted = sum(coeff[target*u % r] for u in units if pow(u, dm, r) == 1)
                root_sum_integer([(row[0]*c[q]+row[1]*e[q]) % 1
                                  for c, e in product(chars, repeat=2) for q in qs],
                                 d*d*predicted)
                power_results.append(predicted)
                row = (3*row[0]+row[1], row[0]+5*row[1])
            out["targets"].append({"target": target, "coefficient": coeff[target],
                                   "joint_mean": joint, "single_power_means_m0_to_m5": power_results})
        fixture_results.append(out)
    report["original_shell_fixtures"] = fixture_results
    path = Path(__file__).with_name("torus_cover_lemma.tex")
    report["source_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
    report["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    dest = Path(__file__).with_suffix(".json")
    dest.write_text(json.dumps(report, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k != "original_shell_fixtures"}, indent=2))
    print("Original shell fixtures:", len(fixture_results))


if __name__ == "__main__":
    run()
