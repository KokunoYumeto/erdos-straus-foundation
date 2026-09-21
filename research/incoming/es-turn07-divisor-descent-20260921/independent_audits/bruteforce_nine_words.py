#!/usr/bin/env python3
"""Independent exact-arithmetic stress test of the nine-word descent theorem.

This script intentionally does not import the supplied verifier.  It enumerates
the defining E/M rational trace sources, computes the exact deletion domain,
validates every returned target directly, and separately tests the constructed
no-return progression for nonautomatic words whenever a small prime instance is
found.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path


SAFE = (1, 2, 3, 4, 6, 9, 12, 18, 36)


def factor(n: int) -> tuple[tuple[int, int], ...]:
    assert n >= 1
    out: list[tuple[int, int]] = []
    q = 2
    while q * q <= n:
        if n % q == 0:
            e = 0
            while n % q == 0:
                n //= q
                e += 1
            out.append((q, e))
        q = 3 if q == 2 else q + 2
    if n > 1:
        out.append((n, 1))
    return tuple(out)


def divisors(n: int) -> tuple[int, ...]:
    out = [1]
    for q, e in factor(n):
        out = [d * q**j for d in out for j in range(e + 1)]
    return tuple(sorted(out))


def divisors_of_square(n: int) -> tuple[int, ...]:
    out = [1]
    for q, e in factor(n):
        out = [d * q**j for d in out for j in range(2 * e + 1)]
    return tuple(sorted(out))


def K(n: int) -> int:
    return math.prod(q ** ((e + 1) // 2) for q, e in factor(n))


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % q for q in range(3, math.isqrt(n) + 1, 2))


def primes_1_mod_4(limit: int) -> tuple[int, ...]:
    return tuple(p for p in range(5, limit + 1, 4) if is_prime(p))


def G(p: int, u: int, channel: str) -> int:
    assert channel in ("E", "M")
    return 4 * u + (1 if channel == "E" else p)


def rational_triple(p: int, a: int, R: int, u: int, channel: str):
    if channel == "E":
        return (
            Fraction(a),
            Fraction(p * a + a * a // u, R),
            Fraction(p * a + p * p * u, R),
        )
    return (
        Fraction(a),
        Fraction(p * (a + a * a // u), R),
        Fraction(p * (a + u), R),
    )


def deletion_domain(p: int, a: int, R: int, u: int, channel: str):
    g = G(p, u, channel)
    d = R // math.gcd(R, g)
    m = 4 * K(u)
    return d, m, tuple(k for k in divisors(R) if k % d == 0 and k % m == 1)


def direct_target_valid(p: int, a: int, R: int, u: int, channel: str, k: int) -> bool:
    if R % k:
        return False
    Rp = R // k
    if (p + Rp) % 4:
        return False
    ap = (p + Rp) // 4
    if not (4 * ap > p and 2 * ap < p):
        return False
    if ap >= a or ap * ap % u:
        return False
    if G(p, u, channel) % Rp:
        return False
    xyz = rational_triple(p, ap, Rp, u, channel)
    if sum(Fraction(1, x) for x in xyz) != Fraction(4, p):
        return False
    return all(x.denominator == 1 and x > 0 for x in xyz)


def enumerate_sources(p_bound: int, u_bound: int):
    counts = Counter()
    failures: list[dict] = []
    witness_no_return: dict[int, dict] = {}
    first_source: dict[int, dict] = {}
    digest_rows: list[tuple] = []
    safe_set = set(SAFE)
    for p in primes_1_mod_4(p_bound):
        for R in range(3, p, 4):
            a = (p + R) // 4
            # K(u)|a is exactly u|a^2.  Enumerating u to u_bound is
            # deliberately independent of factoring a^2 into a supplied list.
            for u in range(1, u_bound + 1):
                if (a * a) % u:
                    continue
                for channel in ("E", "M"):
                    g = G(p, u, channel)
                    if (g * g) % R:
                        continue
                    d, m, ks = deletion_domain(p, a, R, u, channel)
                    if d == 1:
                        continue
                    counts["proper_sources"] += 1
                    counts[f"proper_{channel}"] += 1
                    row = dict(p=p, a=a, R=R, u=u, channel=channel, d=d, m=m, ks=ks)
                    first_source.setdefault(u, row)

                    # Check the reduced tail denominator and trace directly.
                    xyz = rational_triple(p, a, R, u, channel)
                    if xyz[1].denominator != d or xyz[2].denominator != d:
                        failures.append({"kind": "tail_denominator", **row, "xyz": [str(x) for x in xyz]})
                    if (xyz[1] + xyz[2]).denominator != 1:
                        failures.append({"kind": "tail_trace", **row, "xyz": [str(x) for x in xyz]})
                    if (R % (d * d)):
                        failures.append({"kind": "d_square", **row})

                    # The domain is compared to a definition made directly in
                    # target coordinates; this also audits strict descent.
                    direct = tuple(
                        k
                        for k in divisors(R)
                        if direct_target_valid(p, a, R, u, channel, k)
                    )
                    if ks != direct:
                        failures.append({"kind": "domain_mismatch", **row, "direct": direct})
                    for k in ks:
                        if not direct_target_valid(p, a, R, u, channel, k):
                            failures.append({"kind": "invalid_return", **row, "k": k})

                    automatic_candidate = K(d) ** 2
                    if u in safe_set:
                        counts["safe_sources"] += 1
                        if automatic_candidate not in ks:
                            failures.append(
                                {"kind": "safe_missing_candidate", **row, "candidate": automatic_candidate}
                            )
                    elif not ks:
                        witness_no_return.setdefault(u, row)
                    digest_rows.append((p, R, u, channel, d, ks))
    payload = json.dumps(digest_rows, separators=(",", ":"), sort_keys=False).encode()
    return {
        "p_bound": p_bound,
        "u_bound": u_bound,
        "counts": dict(sorted(counts.items())),
        "failures": failures,
        "first_sources": {str(k): v for k, v in sorted(first_source.items())},
        "no_return_witnesses": {str(k): v for k, v in sorted(witness_no_return.items())},
        "source_signature_sha256": hashlib.sha256(payload).hexdigest(),
    }


def square_image_classification(u_bound: int):
    failures = []
    rows = []
    for u in range(1, u_bound + 1):
        m = 4 * K(u)
        units = tuple(x for x in range(1, m) if math.gcd(x, m) == 1)
        image = tuple(sorted({x * x % m for x in units}))
        predicted = 36 % u == 0
        observed = image == (1,)
        if observed != predicted:
            failures.append(dict(u=u, m=m, image=image, predicted=predicted))
        rows.append((u, m, len(image), observed))
    return {"bound": u_bound, "failures": failures, "rows_sha256": hashlib.sha256(json.dumps(rows).encode()).hexdigest()}


def exhaustive_safe_by_gate(safe_p_bound: int):
    """Exhaust every safe-word source by enumerating R among divisors of G_c^2."""
    failures = []
    counts = Counter()
    digest = []
    square_divisor_cache: dict[int, tuple[int, ...]] = {}
    for p in primes_1_mod_4(safe_p_bound):
        for u in SAFE:
            for channel in ("E", "M"):
                g = G(p, u, channel)
                r_candidates = square_divisor_cache.setdefault(g, divisors_of_square(g))
                for R in r_candidates:
                    if not (3 <= R < p and R % 4 == 3):
                        continue
                    a = (p + R) // 4
                    if a * a % u:
                        continue
                    d, m, ks = deletion_domain(p, a, R, u, channel)
                    if d == 1:
                        continue
                    counts["proper_sources"] += 1
                    counts[f"proper_{channel}"] += 1
                    candidate = K(d) ** 2
                    direct = tuple(k for k in divisors(R) if direct_target_valid(p, a, R, u, channel, k))
                    if candidate not in ks or ks != direct:
                        failures.append(
                            dict(
                                p=p,
                                a=a,
                                R=R,
                                u=u,
                                channel=channel,
                                d=d,
                                m=m,
                                candidate=candidate,
                                ks=ks,
                                direct=direct,
                            )
                        )
                    digest.append((p, R, u, channel, d, candidate, ks))
    return {
        "p_bound": safe_p_bound,
        "counts": dict(sorted(counts.items())),
        "failures": failures,
        "signature_sha256": hashlib.sha256(json.dumps(digest, separators=(",", ":")).encode()).hexdigest(),
    }


def first_prime_in_progression(residue: int, modulus: int, lower: int, search_steps: int):
    n = residue % modulus
    if n <= lower:
        n += ((lower - n) // modulus + 1) * modulus
    for _ in range(search_steps):
        if is_prime(n):
            return n
        n += modulus
    return None


def constructed_no_return(u: int, search_steps: int = 200_000):
    """Build the theorem's CRT source, when small prime choices are found."""
    if 36 % u == 0:
        return {"u": u, "status": "automatic"}
    m = 4 * K(u)
    b = next(
        x
        for x in range(1, m, 4)
        if math.gcd(x, m) == 1 and x * x % m != 1
    )
    bound_delta = max(u, u * u - 3 * u + 1, 7)
    delta = first_prime_in_progression((-b * b) % m, m, bound_delta, search_steps)
    t = first_prime_in_progression(pow(b, -1, m), m, max(u, 7), search_steps)
    if delta is None or t is None:
        return {"u": u, "status": "prime_search_exhausted", "b": b, "delta": delta, "t": t}
    if delta == t:
        # Advance t in its progression to enforce the theorem's distinctness.
        t = first_prime_in_progression(pow(b, -1, m), m, t, search_steps)
    R = delta * t * t
    L = math.lcm(840, m)
    # An endpoint prime e only supplies an ES solution distinct from this local
    # obstruction.  Choose the first available 3 mod 4 prime coprime to LR.
    e = next(q for q in range(3, 10_000, 4) if is_prime(q) and math.gcd(q, L * R) == 1)

    # General CRT for pairwise coprime L,R,e.
    mods = (L, R, e)
    residues = (1, (delta * t - 4 * u) % R, e - 1)
    M = math.prod(mods)
    residue = sum(r * (M // n) * pow(M // n, -1, n) for r, n in zip(residues, mods)) % M
    lower = max(R, e, math.prod(q ** (f // 2) for q, f in factor(u)) * R)
    p = first_prime_in_progression(residue, M, lower, search_steps)
    if p is None:
        return {
            "u": u,
            "status": "p_search_exhausted",
            "m": m,
            "b": b,
            "delta": delta,
            "t": t,
            "R": R,
            "e": e,
            "residue": residue,
            "modulus": M,
        }
    a = (p + R) // 4
    channel = "M"
    d, domain_modulus, ks = deletion_domain(p, a, R, u, channel)
    direct = tuple(k for k in divisors(R) if direct_target_valid(p, a, R, u, channel, k))
    assertions = {
        "p_prime_1_mod_4": is_prime(p) and p % 4 == 1,
        "hard_mod_840": p % 840 == 1,
        "source_range": p < 4 * a < 2 * p,
        "word_budget": (a * a) % u == 0,
        "integral_trace": (G(p, u, channel) ** 2) % R == 0,
        "proper_denominator": d == t and d > 1,
        "no_formula_return": not ks,
        "no_direct_return": not direct,
        "strict_residue_checks": (1 - b * b) % m != 0 and (1 - b) % m != 0,
    }
    return {
        "u": u,
        "status": "ok" if all(assertions.values()) else "failed_assertion",
        "m": m,
        "b": b,
        "delta": delta,
        "t": t,
        "R": R,
        "e": e,
        "residue": residue,
        "modulus": M,
        "p": p,
        "a": a,
        "d": d,
        "domain_modulus": domain_modulus,
        "ks": ks,
        "direct": direct,
        "assertions": assertions,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--p-bound", type=int, default=5000)
    ap.add_argument("--u-bound", type=int, default=200)
    ap.add_argument("--abstract-bound", type=int, default=2000)
    ap.add_argument("--safe-p-bound", type=int, default=50000)
    ap.add_argument("--construct-bound", type=int, default=40)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    report = {
        "source_enumeration": enumerate_sources(args.p_bound, args.u_bound),
        "square_image_classification": square_image_classification(args.abstract_bound),
        "safe_gate_exhaustion": exhaustive_safe_by_gate(args.safe_p_bound),
        "constructed_no_return": [
            constructed_no_return(u)
            for u in range(1, args.construct_bound + 1)
            if 36 % u
        ],
    }
    report["summary"] = {
        "source_failures": len(report["source_enumeration"]["failures"]),
        "abstract_failures": len(report["square_image_classification"]["failures"]),
        "safe_gate_failures": len(report["safe_gate_exhaustion"]["failures"]),
        "constructed_ok": sum(x["status"] == "ok" for x in report["constructed_no_return"]),
        "constructed_other": Counter(x["status"] for x in report["constructed_no_return"]),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report["summary"], indent=2, sort_keys=True, default=dict))


if __name__ == "__main__":
    main()

