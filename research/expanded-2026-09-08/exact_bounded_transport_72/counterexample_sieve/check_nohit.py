#!/usr/bin/env python3
"""Exact finite checker for all_shell_no_hit.tex.

It enumerates literal valuation boxes, compares packet coefficients with
direct divisors, and verifies the complete original ordered-witness
bijection against every passing divisor of S^2=(pa)^2.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from pathlib import Path
def isprime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    d=3
    while d*d <= n:
        if n % d == 0: return False
        d += 2
    return True

def factorint(n):
    out={}; d=2
    while d*d <= n:
        while n % d == 0:
            out[d]=out.get(d,0)+1; n//=d
        d = 3 if d==2 else d+2
    if n>1: out[n]=out.get(n,0)+1
    return out

def divisors_from_factorization(fac):
    ds=[1]
    for ell,v in fac.items():
        ds=[d*ell**e for d in ds for e in range(v+1)]
    return ds

def packet(a,R):
    fac=factorint(a)
    counts={1:1}
    for ell,v in fac.items():
        nxt={}
        for r,c in counts.items():
            for e in range(2*v+1):
                t=(r*pow(ell,e,R))%R
                nxt[t]=nxt.get(t,0)+c
        counts=nxt
    return fac,counts

def chart(a, p, eps, u):
    """The original unswapped chart; every coordinate is retained."""
    R = 4*a-p
    assert eps in (0, 1) and a*a % u == 0
    g = math.gcd(a, u)
    A = a//g
    B = u//g
    assert g*g % u == 0
    D = g*g//u
    assert a == A*B*D and u == B*B*D and math.gcd(A, B) == 1
    numerator = A+p**(1-eps)*B
    assert numerator % R == 0
    C = numerator//R
    assert C > 0 and D > 0
    y0 = p**eps*A*C*D
    z0 = p*B*C*D
    # The first numerator is p*C, retaining the original common denominator.
    denominator = p*A*B*C*D
    assert denominator//a == p*C
    assert denominator//y0 == p**(1-eps)*B
    assert denominator//z0 == A
    assert p*C+p**(1-eps)*B+A == 4*A*B*C*D
    assert R*y0-p*a == p**eps*(a*a//u)
    assert R*z0-p*a == p**(2-eps)*u
    return g, A, B, C, D, y0, z0


def reconstruct(a, p, tag):
    eps, u, sigma = tag
    assert (eps == 0 and sigma in (0, 1)) or (eps == 1 and sigma == 0)
    *_, y0, z0 = chart(a, p, eps, u)
    y, z = (y0, z0) if sigma == 0 else (z0, y0)
    assert p*(y*z+a*z+a*y) == 4*a*y*z
    return a, y, z


def inverse(a, p, witness):
    first, y, z = witness
    assert first == a and y > 0 and z > 0
    R = 4*a-p
    S = p*a
    d = R*y-S
    other = R*z-S
    assert d > 0 and other > 0 and d*other == S*S
    v = d
    i = 0
    while v % p == 0:
        v //= p
        i += 1
    assert i in (0, 1, 2) and a*a % v == 0
    if i == 0:
        assert a*a % d == 0
        tag = 0, a*a//d, 0
    elif i == 1:
        assert p*a*a % d == 0
        tag = 1, p*a*a//d, 0
    else:
        assert d % (p*p) == 0
        tag = 0, d//(p*p), 1
    eps, u, _ = tag
    assert a*a % u == 0
    assert ((4*u+1) if eps == 0 else (u+a)) % R == 0
    return tag


def shell(a, p, stats=None):
    R=4*a-p
    fac,c=packet(a,R)
    ds=divisors_from_factorization({ell:2*v for ell,v in fac.items()})
    E={u for u in ds if (4*u+1)%R==0}
    M={u for u in ds if (u+a)%R==0}
    assert c.get((-pow(4,-1,R))%R,0)==len(E)
    assert c.get((-a)%R,0)==len(M)
    assert all(math.gcd(ell,R)==1 for ell in fac)
    # Full inverse valuation allocation.
    for u in ds:
        vf=factorint(u)
        assert all(vf.get(ell,0) <= 2*v for ell,v in fac.items())
    # Every exterior orientation, and each middle complement exactly once.
    tags = {(0, u, sigma) for u in E for sigma in (0, 1)}
    tags.update((1, u, 0) for u in M)
    image = {tag: reconstruct(a, p, tag) for tag in tags}
    assert len(image) == len(set(image.values())) == 2*len(E)+len(M)
    for tag, witness in image.items():
        assert inverse(a, p, witness) == tag

    # Independent route: factor the original S=pa, enumerate ALL divisors
    # of its original square, and use the original residual congruence.
    # This route does not select E/M or derive d from the chart coordinates.
    S = p*a
    S_factors = factorint(S)
    original_divisors = divisors_from_factorization(
        {ell: 2*v for ell, v in S_factors.items()})
    assert len(original_divisors) == math.prod(2*v+1 for v in S_factors.values())
    assert len(set(original_divisors)) == len(original_divisors)
    direct = {}
    p_cases = {0: 0, 1: 0, 2: 0}
    for d in original_divisors:
        assert S*S % d == 0
        if (d+S) % R:
            continue
        other = S*S//d
        assert (other+S) % R == 0
        y = (S+d)//R
        z = (S+other)//R
        witness = a, y, z
        assert R*y-S == d and R*z-S == other
        assert p*(y*z+a*z+a*y) == 4*a*y*z
        assert y != z
        direct[d] = witness
        tag = inverse(a, p, witness)
        assert tag in tags and reconstruct(a, p, tag) == witness
        eps, _, sigma = tag
        i = 1 if eps == 1 else 2*sigma
        assert d % p**i == 0 and (d//p**i) % p != 0
        p_cases[i] += 1
    assert set(direct.values()) == set(image.values())
    assert len(direct) == len(image)
    assert p_cases == {0: len(E), 1: len(M), 2: len(E)}

    # The order-forgetting quotient retains the full two-element fibres.
    orbits = {}
    for tag, witness in image.items():
        eps, u, sigma = tag
        swapped_tag = (0, u, 1-sigma) if eps == 0 else (1, a*a//u, 0)
        assert swapped_tag in tags and swapped_tag != tag
        swapped_witness = a, witness[2], witness[1]
        assert image[swapped_tag] == swapped_witness
        orbit = frozenset((witness, swapped_witness))
        assert len(orbit) == 2
        orbits.setdefault(orbit, set()).add(tag)
        if eps == 1:
            g, A, B, C, D, _, _ = chart(a, p, eps, u)
            gp, Ap, Bp, Cp, Dp, _, _ = chart(a, p, eps, a*a//u)
            assert g == B*D and gp == A*D
            assert (Ap, Bp, Cp, Dp) == (B, A, C, D)
    assert all(len(fibre) == 2 for fibre in orbits.values())
    assert len(M) % 2 == 0
    assert len(orbits) == len(E)+len(M)//2
    if stats is not None:
        stats["original_square_divisors"] += len(original_divisors)
        stats["passing_original_divisors"] += len(direct)
        stats["ordered_witnesses"] += len(image)
        stats["order_forgetting_fibres"] += len(orbits)
        for i, count in p_cases.items():
            stats["residual_p_exponent_counts"][str(i)] += count
    return fac,c,E,M

def primes_12_1(limit):
    return [p for p in range(13,limit+1,12) if isprime(p)]

def run(limit):
    checked=0; hits=0; nohit=0; shell_count=0
    stats = {"original_square_divisors": 0, "passing_original_divisors": 0,
             "ordered_witnesses": 0, "order_forgetting_fibres": 0,
             "residual_p_exponent_counts": {"0": 0, "1": 0, "2": 0}}
    examples=[]
    for p in primes_12_1(limit):
        h=(p-1)//12
        Q=0; O=1; first=None
        for a in range(3*h+1,9*h+1):
            R=4*a-p
            if R<3: raise AssertionError((p,a,R))
            fac,c,E,M=shell(a,p,stats)
            shell_count+=1
            Q += len(E)+len(M)//2
            if E or M:
                hits+=1
                if first is None: first=(a,sorted(E),sorted(M))
                O=0
        assert (O==1)==(Q==0)
        if O: nohit+=1; examples.append(p)
        checked+=1
    result = {"primes":checked,"shells":shell_count,"hit_shells":hits,
              "nohit_primes":nohit,"nohit_examples":examples}
    result.update(stats)
    return result


def fixture():
    a, p = 4, 13
    _, _, E, M = shell(a, p)
    assert E == M == {2, 8}
    expected = {
        (0, 2, 0): (4, 20, 130), (0, 2, 1): (4, 130, 20),
        (0, 8, 0): (4, 18, 468), (0, 8, 1): (4, 468, 18),
        (1, 2, 0): (4, 52, 26), (1, 8, 0): (4, 26, 52)}
    assert {tag: reconstruct(a, p, tag) for tag in expected} == expected
    assert {3*witness[1]-52 for witness in expected.values()} == {
        2, 8, 26, 104, 338, 1352}
    unswapped = {witness for tag, witness in expected.items() if tag[2] == 0}
    missing_before_repair = set(expected.values())-unswapped
    assert missing_before_repair == {(4, 130, 20), (4, 468, 18)}
    return {"p": p, "a": a, "R": 3, "S": 52, "E": sorted(E), "M": sorted(M),
            "ordered_witnesses": len(expected), "unordered_pairs": 3,
            "rows": [{"tag": list(tag), "witness": list(witness),
                      "d_y": 3*witness[1]-52, "d_z": 3*witness[2]-52}
                     for tag, witness in expected.items()],
            "omitted_without_exterior_swap": [list(w) for w in sorted(missing_before_repair)]}


def certificate(limit, result, fixture_result):
    folder = Path(__file__).resolve().parent
    tex = folder/"all_shell_no_hit.tex"
    script = Path(__file__).resolve()
    return {
        "theorem": "all_shell_no_hit", "status": "passed",
        "files": {"tex": tex.name, "checker": script.name},
        "test": {"command": f"python counterexample_sieve/check_nohit.py --limit {limit} --certificate",
                 "limit": limit, **result},
        "sha256": {"tex": hashlib.sha256(tex.read_bytes()).hexdigest(),
                   "checker": hashlib.sha256(script.read_bytes()).hexdigest()},
        "fixture_p13_a4": fixture_result,
        "scope": ["literal valuation boxes", "finite unit-group coefficients",
                  "exact residual fibres", "full original ordered-witness bijection",
                  "all three residual p-adic exponent branches",
                  "both inverse compositions", "direct original S squared divisor comparison",
                  "exact two-element order-forgetting fibres", "global iff obstruction"],
        "exclusions": ["no density claim", "no universal prime occupancy claim",
                       "no normalization replacing exponent budgets"],
    }

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--limit",type=int,default=200)
    ap.add_argument("--certificate",action="store_true",
                    help="Write CHECK_NOHIT.json with this run's results and current source hashes.")
    ns=ap.parse_args()
    fixture_result = fixture()
    result = run(ns.limit)
    if ns.certificate:
        target = Path(__file__).resolve().parent/"CHECK_NOHIT.json"
        target.write_text(json.dumps(certificate(ns.limit, result, fixture_result), indent=2)+"\n",
                          encoding="utf-8")
    print(json.dumps(result, indent=2))
