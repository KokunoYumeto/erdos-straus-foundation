"""Exact positive divisibility/CRT solver and independent finite verification.

Only standard-library arithmetic is used. The returned exponent choices are
complete; a residue coefficient never substitutes for a divisor witness.
This verifies finite instances of the proofs in bounded_transport.tex.
It does not decide universal Erdős--Straus positivity.
"""
from collections import defaultdict
from fractions import Fraction
from functools import reduce
from itertools import product
from math import gcd, lcm, isqrt, prod
from pathlib import Path
import hashlib
import json
import random

ROOT = Path(__file__).resolve().parent


def require(condition, context):
    if not condition:
        raise ArithmeticError(context)


def factor(n):
    require(n > 0, ("factor-positive", n))
    result = {}
    q = 2
    while q * q <= n:
        while n % q == 0:
            result[q] = result.get(q, 0) + 1
            n //= q
        q += 1
    if n > 1:
        result[n] = result.get(n, 0) + 1
    return result


def divisors(n):
    values = [1]
    for q, e in factor(n).items():
        values = [u * q ** j for u in values for j in range(e + 1)]
    return sorted(values)


def combine(r, d, s, e):
    """Full noncoprime CRT inverse; return None exactly if incompatible."""
    g = gcd(d, e)
    if (s - r) % g:
        return None
    e0 = e // g
    step = 0 if e0 == 1 else ((s - r) // g) * pow(d // g, -1, e0) % e0
    modulus = lcm(d, e)
    return (r + d * step) % modulus, modulus


def solve(bounds, mandatory=(), congruences=()):
    """Return all u>0 with u|every bound, every mandatory|u, c*u=b mod m."""
    require(bounds and all(n > 0 for n in bounds), ("bounds", bounds))
    require(all(x > 0 for x in mandatory), ("mandatory", mandatory))
    n = reduce(gcd, bounds)
    f = lcm(*mandatory) if mandatory else 1
    if n % f:
        return {"solutions": [], "failure": "mandatory_factor_exceeds_bound"}
    r, modulus = 0, 1
    reductions = []
    for c, b, m in congruences:
        require(m > 0, ("positive-modulus", m))
        g = gcd(c, m)
        if b % g:
            return {"solutions": [], "failure": "coefficient_gcd",
                    "failed_congruence": [c, b, m, g]}
        mi = m // g
        ri = 0 if mi == 1 else ((b // g) * pow(c // g, -1, mi)) % mi
        reductions.append([c, b, m, g, ri, mi])
        merged = combine(r, modulus, ri, mi)
        if merged is None:
            return {"solutions": [], "failure": "noncoprime_compatibility",
                    "failed_residue_pair": [r, modulus, ri, mi]}
        r, modulus = merged
    nf, ff = factor(n), factor(f)
    primes = list(nf)
    # Every monoid coefficient retains all exponent vectors that contribute.
    states = {1 % modulus: [()]}
    for q, upper in nf.items():
        lower = ff.get(q, 0)
        updated = defaultdict(list)
        for residue, vectors in states.items():
            for exponent in range(lower, upper + 1):
                target = residue * pow(q, exponent, modulus) % modulus
                updated[target].extend(v + (exponent,) for v in vectors)
        states = dict(updated)
    vectors = sorted(states.get(r, []))
    values = sorted(prod(q ** e for q, e in zip(primes, v)) for v in vectors)
    return {"solutions": values, "failure": None, "N": n, "mandatory_lcm": f,
            "residue": r, "modulus": modulus, "kernel": f"{modulus} Z",
            "primes": primes, "exponent_vectors": [list(v) for v in vectors],
            "coefficient": len(vectors), "reductions": reductions,
            "all_residue_coefficients": {str(x): len(v) for x, v in sorted(states.items())}}


def brute(bounds, mandatory, congruences):
    # Independent test walks positive integers, not factor vectors or residues.
    return [u for u in range(1, min(bounds) + 1)
            if all(n % u == 0 for n in bounds)
            and all(u % f == 0 for f in mandatory)
            and all((c * u - b) % m == 0 for c, b, m in congruences)]


def prime(n):
    return n >= 2 and all(n % q for q in range(2, isqrt(n) + 1))


def pair_box(s):
    # Direct divisor pairs are independent of signed-exponent reconstruction.
    ds = divisors(s)
    return [(m, n) for m in ds for n in ds if gcd(m, n) == 1]


def primitive_monoid(s, modulus):
    states = {(1 % modulus, 1 % modulus): [(1, 1)]}
    for q, budget in factor(s).items():
        choices = [(1, 1)] + [(q ** e, 1) for e in range(1, budget + 1)] + [
            (1, q ** e) for e in range(1, budget + 1)]
        updated = defaultdict(list)
        for residue, pairs in states.items():
            for xm, xn in choices:
                target = (residue[0] * xm % modulus, residue[1] * xn % modulus)
                updated[target].extend((m * xm, n * xn) for m, n in pairs)
        states = dict(updated)
    return states


def em_fixture(p, a):
    require(prime(p) and p % 12 == 1, ("prime-domain", p))
    h = (p - 1) // 12
    require(3 * h + 1 <= a <= 9 * h, ("shell-domain", p, a))
    r, s = 4 * a - p, p * a
    require(gcd(r, s) == 1, ("units", p, a))
    e = solve([a * a], congruences=[(4, -1, r)])
    m = solve([a * a], congruences=[(1, -a, r)])
    pairs = sorted((x, y) for x, y in pair_box(s) if (x + y) % r == 0)
    require(len(pairs) == 2 * len(e["solutions"]) + len(m["solutions"]),
            ("full-EM", p, a))
    triples = []
    for x, y in pairs:
        k = (x + y) // r
        yz = ((s // y) * k, (s // x) * k)
        require(Fraction(1, a) + Fraction(1, yz[0]) + Fraction(1, yz[1])
                == Fraction(4, p), ("witness", p, a, x, y, yz))
        triples.append([a, *yz])
    return {"p": p, "a": a, "R": r, "S": s, "factor_a": factor(a),
            "E": e, "M": m, "pairs": [list(x) for x in pairs], "triples": triples}


def main():
    counts = defaultdict(int)
    # Exhausts residue CRT, including unit and nonunit residues and modulus one.
    for d in range(1, 18):
        for e in range(1, 18):
            for r in range(d):
                for s in range(e):
                    found = combine(r, d, s, e)
                    exact = [x for x in range(lcm(d, e)) if x % d == r and x % e == s]
                    require((found is None and exact == []) or
                            (found is not None and exact == [found[0]]),
                            ("CRT", d, e, r, s, found, exact))
                    counts["noncoprime_residue_pairs"] += 1
    # Exhausts every single congruence in this domain, including negative and zero coefficients.
    for n in range(1, 81):
        for c in range(-3, 4):
            for m in range(1, 10):
                for b in range(m):
                    constraints = [(c, b, m)]
                    answer = solve([n], congruences=constraints)
                    require(answer["solutions"] == brute([n], (), constraints),
                            ("scalar", n, c, b, m, answer))
                    counts["single_affine_divisor_systems"] += 1
    # Mixed simultaneous constraints, with reproducible retained failing cases.
    rng = random.Random(20260908)
    sampled = []
    for i in range(6000):
        bounds = [rng.randint(1, 800) for _ in range(rng.randint(1, 3))]
        mandatory = [rng.randint(1, 16) for _ in range(rng.randint(0, 2))]
        constraints = [(rng.randint(-8, 8), rng.randint(-40, 40), rng.randint(1, 24))
                       for _ in range(rng.randint(0, 5))]
        actual = solve(bounds, mandatory, constraints)
        expected = brute(bounds, mandatory, constraints)
        require(actual["solutions"] == expected,
                ("mixed", i, bounds, mandatory, constraints, actual, expected))
        counts["mixed_simultaneous_systems"] += 1
        if i < 12 or (actual["solutions"] and len(sampled) < 28):
            sampled.append({"bounds": bounds, "mandatory": mandatory,
                            "congruences": constraints, "result": actual})
    for n in range(1, 61):
        for r in range(1, 16):
            states = primitive_monoid(n, r)
            calculated = sorted(x for values in states.values() for x in values)
            require(calculated == sorted(pair_box(n)), ("primitive-monoid", n, r))
            for residue, pairs in states.items():
                require(all((m % r, k % r) == residue for m, k in pairs),
                        ("primitive-fibres", n, r, residue))
            counts["primitive_monoid_systems"] += 1
    fixtures = [em_fixture(p, a) for p, a in [(37, 12), (37, 13), (37, 18),
                                             (241, 64), (73, 20), (73, 21),
                                             (769, 194), (769, 195)]]
    local_37 = {str(d): {"E": solve([324], congruences=[(4, -1, d)]),
                        "M": solve([324], congruences=[(1, -18, d)])}
                for d in [5, 7, 35]}
    local_241 = {str(d): {"E": solve([4096], congruences=[(4, -1, d)]),
                         "M": solve([4096], congruences=[(1, -64, d)])}
                 for d in [3, 5, 15]}
    require(96 % 35 == 26 and 4 * 96 + 1 == 385, "zero-obstruction-lift")
    require(all(not (j % 2 == 1 and j % 4 == 0) for j in range(24)),
            "nonzero-obstruction-period")
    # Full biconditional p-origin crosswalk retained in a finite independent census.
    for p in range(13, 250):
        if prime(p) and p % 12 == 1:
            h = (p - 1) // 12
            for a in range(3 * h + 1, 9 * h + 1):
                em_fixture(p, a)
                counts["full_original_shells_and_reconstructions"] += 1
    certificate = {
        "schema_version": 1, "status": "passed",
        "scope": "Finite exact tests of the stated universal elementary proofs; no universal ES positivity",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "counts": dict(counts), "fixtures": fixtures,
        "zero_obstruction_empty_budget": local_37,
        "nonzero_exponent_obstruction": local_241,
        "mixed_examples": sampled,
        "algorithms": {
            "CRT": "Bezout inverse after gcd compatibility",
            "scalar": "nonunit coefficient reduction, compatible CRT, exact bounded monoid convolution",
            "independent_oracle": "direct positive integer substitution in unreduced constraints",
            "primitive": "exclusive prime budget convolution compared with direct coprime divisor pairs"
        }
    }
    target = ROOT / "BOUNDED_CRT_CERTIFICATE.json"
    target.write_text(json.dumps(certificate, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"status": certificate["status"], "counts": counts,
                      "certificate": target.name}, indent=2))


if __name__ == "__main__":
    main()
