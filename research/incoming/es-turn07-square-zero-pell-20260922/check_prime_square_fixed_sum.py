#!/usr/bin/env python3
"""Corroborate the prime-square fixed-tail-sum divisor obstruction.

The universal result is proved in core.tex.  This program independently
checks every proper prime-square source serialized by verify.py, reconstructs
the canonical (k_0, eta, F) data, and exhausts every target-eligible proper
divisor of the source residual.
"""
from __future__ import annotations

import argparse
from math import gcd, isqrt
import json
from pathlib import Path


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def divisors(n: int) -> list[int]:
    low: list[int] = []
    high: list[int] = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            low.append(d)
            if d * d != n:
                high.append(n // d)
        d += 1
    return low + high[::-1]


def source_H(channel: str, u: int, p: int, q: int) -> int:
    if channel == "E" and u == q:
        return p + q
    if channel == "E" and u == q ** 3:
        return p * q + 1
    if channel == "M" and u in (q, q ** 3):
        return q + 1
    raise AssertionError((channel, u, p, q))


def check_record(shell: dict, rec: dict) -> dict:
    p = int(shell["p"])
    q = int(shell["q"])
    R = int(shell["R"])
    u = int(rec["u"])
    channel = str(rec["channel"])
    assert is_prime(p) and is_prime(q)
    assert p % 4 == 1 and 2 * q * q < p < 4 * q * q
    assert R == 4 * q * q - p
    assert u in (q, q ** 3)
    G = 4 * u + 1 if channel == "E" else p + 4 * u
    assert G * G % R == 0 and G % R != 0
    assert rec["trace"] is True and rec["full"] is False
    N_num, N_den = map(int, rec["tail_sum"])
    assert N_den == 1
    N = N_num

    H = source_H(channel, u, p, q)
    g = gcd(R, H)
    eta = R // g
    F = H // g
    assert gcd(eta, F) == 1
    assert g % eta == 0
    k0 = g // eta
    assert R == k0 * eta * eta
    assert H == k0 * eta * F
    assert eta > 1 and eta % 2 == 1
    expected_N = q * k0 * F * F
    if channel == "M":
        expected_N *= p
    assert N == expected_N
    assert gcd(R, N) == k0

    obstruction_counts = {
        "residual_not_dividing_tail_sum": 0,
        "negative_discriminant": 0,
        "nonsquare_discriminant": 0,
        "parity_failure": 0,
    }
    tested = 0
    for S in divisors(R):
        if not (0 < S < R and (p + S) % 4 == 0):
            continue
        tested += 1
        if N % S:
            obstruction_counts["residual_not_dividing_tail_sum"] += 1
            continue
        disc = N * (N - p) - (N // S) * p * p
        if disc < 0:
            obstruction_counts["negative_discriminant"] += 1
            continue
        delta = isqrt(disc)
        if delta * delta != disc:
            obstruction_counts["nonsquare_discriminant"] += 1
            continue
        if (delta - N) % 2:
            obstruction_counts["parity_failure"] += 1
            continue
        A = (p + S) // 4
        Y = (N - delta) // 2
        Z = (N + delta) // 2
        if not (A > 0 and Y > 0 and Z > 0):
            raise AssertionError(("nonpositive reconstructed target", p, q, R, S))
        if 4 * A * Y * Z != p * (Y * Z + A * Z + A * Y):
            raise AssertionError(("identity failure", p, q, R, S))
        raise AssertionError(("counterexample", p, q, R, u, channel, S, A, Y, Z))

    assert tested == sum(obstruction_counts.values())
    return {
        "p": p,
        "q": q,
        "R": R,
        "u": u,
        "channel": channel,
        "N": N,
        "g": g,
        "eta": eta,
        "k0": k0,
        "F": F,
        "proper_divisor_residuals_tested": tested,
        "obstruction_counts": obstruction_counts,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    source = json.loads(Path(args.input).read_text(encoding="utf-8"))
    rows: list[dict] = []
    for shell in source["shells"]:
        for rec in shell["records"]:
            if rec["trace"] and not rec["full"]:
                rows.append(check_record(shell, rec))
    total_residuals = sum(row["proper_divisor_residuals_tested"] for row in rows)
    output = {
        "theorem": "prime-square fixed-sum divisor obstruction",
        "scope": {
            "source": str(Path(args.input).name),
            "prime_square_bound": source.get("square_bound"),
        },
        "proper_source_rows": len(rows),
        "proper_divisor_residuals_tested": total_residuals,
        "counterexamples": [],
        "records": rows,
        "universal_status": "proved in core.tex; this file is finite corroboration",
    }
    Path(args.out).write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps({
        "proper_source_rows": len(rows),
        "proper_divisor_residuals_tested": total_residuals,
        "counterexamples": 0,
    }, indent=2))


if __name__ == "__main__":
    main()
