#!/usr/bin/env python3
"""Independent reconstruction checker; Python >= 3.10, standard library only.

No downloaded module is imported or executed. Checks use explicit exceptions,
so -O does not remove them. Output is confined to the selected --out directory.
The source argument to provenance is read for hashes only, never executed.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
from functools import lru_cache
import hashlib
import heapq
from itertools import product
import json
from math import gcd, isqrt, prod
from pathlib import Path
import platform
import sys
from time import perf_counter


CHECKS = Counter()
INF = None


def check(condition, name):
    CHECKS[name] += 1
    if not condition:
        raise ArithmeticError(name)


@lru_cache(maxsize=None)
def factors(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("positive integer required")
    answer = []
    q = 2
    while q * q <= n:
        e = 0
        while n % q == 0:
            n //= q
            e += 1
        if e:
            answer.append((q, e))
        q = 3 if q == 2 else q + 2
    if n > 1:
        answer.append((n, 1))
    return tuple(answer)


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


@lru_cache(maxsize=None)
def squares(ell):
    return frozenset(x * x % ell for x in range(1, ell))


def local_character(g, ell):
    if g % ell == 0:
        raise ValueError("a unit is required")
    return 1 if g % ell in squares(ell) else -1


@lru_cache(maxsize=None)
def group_data(R):
    if R < 3 or R % 2 == 0:
        raise ValueError("odd modulus at least three required")
    f = factors(R)
    units = tuple(g for g in range(1, R) if gcd(g, R) == 1)
    inverse = {g: pow(g, -1, R) for g in units}
    full = {g: tuple(local_character(g, ell) for ell, _ in f) for g in units}
    jacobi = {g: (prod(c ** e for c, (_, e) in zip(full[g], f)),) for g in units}
    return units, inverse, {"unpartitioned": {g: () for g in units},
                            "jacobi": jacobi, "quadratic": full}


def targets(p, R):
    return frozenset(((-1) % R, (-p) % R, (-pow(p, -1, R)) % R))


def slot_floor(N, pairs, involutions, has_identity, identity_forbidden=False):
    """Exact relaxed minimum, None meaning +infinity, all counts integral."""
    if any(not isinstance(x, int) or x < 0 for x in (N, pairs, involutions)):
        raise ValueError("nonnegative integral mass and slot counts required")
    if identity_forbidden:
        return INF
    base = int(has_identity)
    if N < base or (N - base) % 2:
        return INF
    budget = (N - base) // 2
    heap = []
    index = 0
    for count, first, step in ((pairs, 2, 4), (involutions, 4, 8),
                               (base, 8, 8)):
        for _ in range(count):
            heap.append((first, index, step))
            index += 1
    if budget and not heap:
        return INF
    heapq.heapify(heap)
    energy = base
    for _ in range(budget):
        cost, index, step = heapq.heappop(heap)
        energy += cost
        heapq.heappush(heap, (cost + step, index, step))
    return energy


def exhaustive_floor(N, pairs, involutions, has_identity,
                     identity_forbidden=False):
    """Independent dynamic program using occupancy squares, no marginals."""
    if identity_forbidden:
        return INF
    choices = []
    for _ in range(pairs):
        choices.append([(2 * k, 2 * k * k) for k in range(N // 2 + 1)])
    for _ in range(involutions):
        choices.append([(2 * k, 4 * k * k) for k in range(N // 2 + 1)])
    if has_identity:
        choices.append([(1 + 2 * k, (1 + 2 * k) ** 2)
                        for k in range((N + 1) // 2)])
    state = {0: 0}
    for slot in choices:
        new = {}
        for old_mass, old_energy in state.items():
            for mass, energy in slot:
                total_mass = old_mass + mass
                if total_mass <= N:
                    total_energy = old_energy + energy
                    if total_mass not in new or total_energy < new[total_mass]:
                        new[total_mass] = total_energy
        state = new
    return state.get(N, INF)


def partition_result(p, a, histogram, name):
    R = 4 * a - p
    units, inverse, partitions = group_data(R)
    labels = partitions[name]
    forbidden = targets(p, R)
    identity_label = labels[1]
    cells = {}
    for label in sorted(set(labels.values())):
        members = tuple(g for g in units if labels[g] == label)
        allowed = tuple(g for g in members if g not in forbidden)
        check(all(inverse[g] in allowed for g in allowed), "allowed inversion closure")
        check(all(labels[inverse[g]] == label for g in members), "cell inversion closure")
        pair_list = tuple((g, inverse[g]) for g in allowed if g < inverse[g])
        involution_list = tuple(g for g in allowed if g == inverse[g] and g != 1)
        has_identity = 1 in allowed
        N = sum(histogram[g] for g in members)
        E = sum(histogram[g] ** 2 for g in members)
        forbidden_identity = label == identity_label and 1 in forbidden
        minimum = slot_floor(N, len(pair_list), len(involution_list),
                             has_identity, forbidden_identity)
        certified = minimum is INF or E < minimum
        hit = any(histogram[g] for g in members if g in forbidden)
        check(not certified or hit, "certificate has target fibre")
        check(N % 2 == int(label == identity_label), "cell mass parity")
        cells[label] = {"label": list(label), "mass": N, "energy": E,
                        "minimum": minimum, "minimum_is_infinite": minimum is INF,
                        "certified": certified, "target_present": hit,
                        "targets": sorted(set(members) & forbidden),
                        "inverse_pairs": pair_list,
                        "nonidentity_involutions": involution_list,
                        "identity_available": has_identity}
    return {"certified": any(v["certified"] for v in cells.values()),
            "cells": list(cells.values())}


def witness(p, a, beta):
    R = 4 * a - p
    f = factors(a)
    residue = prod(pow(q, b, R) for (q, _), b in zip(f, beta)) % R
    if residue == (-1) % R:
        channel = "M"
    elif residue == (-pow(p, -1, R)) % R:
        channel = "E"
    elif residue == (-p) % R:
        channel = "E"
        beta = tuple(-b for b in beta)
    else:
        raise ValueError("exponent vector does not hit a target")
    u = prod(q ** (e + b) for (q, e), b in zip(f, beta))
    complement = a * a // u
    if channel == "M":
        numbers = (a, Fraction(p * (a + complement), R), Fraction(p * (a + u), R))
        check((u + a) % R == 0, "middle gate")
    else:
        numbers = (a, Fraction(p * a + complement, R), Fraction(p * a + p * p * u, R))
        check((4 * u + 1) % R == 0, "exterior gate")
    check(all(Fraction(x).denominator == 1 and x > 0 for x in numbers),
          "positive integral witness")
    numbers = tuple(int(x) for x in numbers)
    check(sum((Fraction(1, x) for x in numbers), Fraction()) == Fraction(4, p),
          "exact reciprocal identity")
    d = gcd(a, u)
    h, r, s = d * d // u, u // d, a // d
    quotient = Fraction(r + s if channel == "M" else p * r + s, R)
    check(d * d % u == 0 and h * r * s == a and h * r * r == u and gcd(r, s) == 1,
          "marked divisor inverse")
    check(quotient.denominator == 1, "integral channel quotient")
    return {"p": p, "a": a, "R": R, "beta": beta, "u": u,
            "channel": channel, "h": h, "r": r, "s": s,
            "lambda" if channel == "M" else "kappa": int(quotient),
            "ordered_denominators": numbers}


def shell(p, a, autocorrelation=False):
    check(prime(p) and p % 4 == 1 and p // 4 < a <= 3 * (p // 4), "full shell domain")
    R = 4 * a - p
    check(gcd(a, R) == gcd(p, R) == 1, "shell units")
    f = factors(a)
    exponents = tuple(product(*(range(-e, e + 1) for _, e in f)))
    histogram = Counter()
    fibres = {}
    for beta in exponents:
        g = prod(pow(q, b, R) for (q, _), b in zip(f, beta)) % R
        histogram[g] += 1
        fibres.setdefault(g, []).append(beta)
    # Independent divisor path: inspect all divisors by trial divisibility.
    lower = [u for u in range(1, a + 1) if a * a % u == 0]
    divisors = lower + [a * a // u for u in lower if u != a]
    divisor_histogram = Counter(u * pow(a, -1, R) % R for u in divisors)
    check(histogram == divisor_histogram, "complete box versus independent divisors")
    N = prod(2 * e + 1 for _, e in f)
    E = sum(n * n for n in histogram.values())
    check(sum(histogram.values()) == N, "complete box mass")
    units, inverse, _ = group_data(R)
    forbidden = targets(p, R)
    check({inverse[t] for t in forbidden} == set(forbidden), "target inversion closure")
    check(histogram[1] % 2 == 1, "identity odd")
    for g in units:
        check(histogram[g] == histogram[inverse[g]], "histogram inversion")
        if g != 1 and g == inverse[g]:
            check(histogram[g] % 2 == 0, "nonidentity involution even")
    if autocorrelation:
        E2 = 0
        for delta in product(*(range(-2 * e, 2 * e + 1) for _, e in f)):
            if prod(pow(q, d, R) for (q, _), d in zip(f, delta)) % R == 1:
                E2 += prod(2 * e + 1 - abs(d) for (_, e), d in zip(f, delta))
        check(E2 == E, "weighted autocorrelation identity")
    results = {name: partition_result(p, a, histogram, name)
               for name in ("unpartitioned", "jacobi", "quadratic")}
    for coarse, fine in (("unpartitioned", "jacobi"), ("jacobi", "quadratic")):
        check(not results[coarse]["certified"] or results[fine]["certified"],
              "criterion monotonicity")
        fine_cells = results[fine]["cells"]
        for cell in results[coarse]["cells"]:
            children = fine_cells if coarse == "unpartitioned" else [
                c for c in fine_cells if prod(x ** e for x, (_, e) in
                                             zip(c["label"], factors(R))) == cell["label"][0]]
            check(sum(c["mass"] for c in children) == cell["mass"] and
                  sum(c["energy"] for c in children) == cell["energy"], "refinement mass and energy")
            fine_infinite = any(c["minimum_is_infinite"] for c in children)
            check(fine_infinite or (not cell["minimum_is_infinite"] and
                  cell["minimum"] <= sum(c["minimum"] for c in children)),
                  "exact refinement floor inequality")
    extracted = None
    for target in sorted(forbidden):
        if fibres.get(target):
            extracted = witness(p, a, fibres[target][0])
            break
    return {"p": p, "a": a, "R": R, "factorization": f, "N": N, "E": E,
            "targets": sorted(forbidden), "histogram": dict(sorted(histogram.items())),
            "partitions": results, "witness": extracted}


def self_test():
    # Actual occupancy enumeration validates all edge cases in this bounded box.
    for N, pairs, involutions, identity, blocked in product(
            range(20), range(4), range(4), (False, True), (False, True)):
        check(slot_floor(N, pairs, involutions, identity, blocked) ==
              exhaustive_floor(N, pairs, involutions, identity, blocked),
              "greedy versus exhaustive occupancy dynamic program")
    # Modulus 9 has nontrivial local character but identically positive Jacobi.
    _, _, partitions = group_data(9)
    check(partitions["jacobi"][2] == (1,) and partitions["quadratic"][2] == (-1,),
          "even prime exponent retains local character")
    for ell in (3, 5, 7, 11, 13, 17, 19):
        for x, y in product(range(1, ell), repeat=2):
            check(local_character(x * y, ell) ==
                  local_character(x, ell) * local_character(y, ell), "quadratic character multiplicativity")
    examples = [shell(p, a, autocorrelation=True) for p, a in
                ((5, 2), (13, 6), (37, 10), (37, 18), (37, 27),
                 (241, 64), (241, 121), (1201, 306), (1201, 310), (1201, 700))]
    special = next(s for s in examples if (s["p"], s["a"]) == (1201, 310))
    check((special["R"], special["N"], special["E"], special["targets"]) ==
          (39, 27, 39, [5, 8, 38]), "1201 global data")
    unpart = special["partitions"]["unpartitioned"]["cells"][0]
    check(unpart["minimum"] == 39 and not unpart["certified"], "1201 unpartitioned equality")
    negative = next(c for c in special["partitions"]["jacobi"]["cells"] if c["label"] == [-1])
    for partition in special["partitions"].values():
        for cell in partition["cells"]:
            check(cell["minimum"] == exhaustive_floor(
                cell["mass"], len(cell["inverse_pairs"]),
                len(cell["nonidentity_involutions"]), cell["identity_available"]),
                "1201 actual cells versus exhaustive occupancy dynamic program")
    check((negative["mass"], negative["energy"], negative["minimum"], negative["targets"]) ==
          (18, 30, 32, [38]), "1201 negative Jacobi strict inequality")
    check(len(negative["inverse_pairs"]) == 5 and len(negative["nonidentity_involutions"]) == 1,
          "1201 negative Jacobi slots")
    marked = witness(1201, 310, (0, -1, -1))
    check((marked["u"], marked["h"], marked["r"], marked["s"], marked["lambda"],
           marked["ordered_denominators"]) == (2, 2, 1, 155, 4, (310, 1489240, 9608)),
          "1201 exact marked witness")
    check(Fraction(marked["r"], marked["s"]) < Fraction(1, 8), "1201 lower chamber slope")
    special["prescribed_middle_witness"] = marked
    check(examples[3]["witness"] is None, "37 a18 retained empty shell")
    check(all(not part["certified"] for part in examples[3]["partitions"].values()),
          "37 a18 empty shell never certified")
    return examples


def scan(bound):
    if not 5 <= bound <= 1500:
        raise ValueError("this reviewed scan is explicitly bounded by 1500")
    primes = [p for p in range(5, bound + 1) if p % 12 == 1 and prime(p)]
    totals = Counter()
    rows = []
    for p in primes:
        m = (p - 1) // 4
        for a in range(m + 1, 2 * m + 1):
            result = shell(p, a)
            certified = {key: value["certified"] for key, value in result["partitions"].items()}
            totals.update(k for k, v in certified.items() if v)
            rows.append({"p": p, "a": a, "R": result["R"], "N": result["N"], "E": result["E"],
                         "certified": certified, "target_present": result["witness"] is not None})
    if bound == 1500:
        check(len(primes) == 54 and len(rows) == 9531, "complete 1500 restricted scan dimensions")
        check(dict(totals) == {"unpartitioned": 214, "jacobi": 231, "quadratic": 240},
              "1500 transcript comparison counts reproduced")
    return {"bound": bound, "scope": "primes p=1 mod12; m+1 <= a <= 2m; R<p only",
            "primes": primes, "prime_count": len(primes), "shell_count": len(rows),
            "certification_counts": dict(totals), "shells": rows}


def dump(path, obj):
    path.write_text(json.dumps(obj, sort_keys=True, indent=2) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--scan-bound", type=int, default=0)
    args = parser.parse_args()
    start = perf_counter()
    args.out.mkdir(parents=True, exist_ok=True)
    examples = self_test()
    dump(args.out / "examples.json", examples)
    scan_result = scan(args.scan_bound) if args.scan_bound else None
    if scan_result:
        dump(args.out / "energy_scan.json", scan_result)
    summary = {"status": "passed", "scope": "independent reconstruction; no universal ES claim",
               "checks": dict(sorted(CHECKS.items())), "check_total": sum(CHECKS.values()),
               "scan": None if scan_result is None else
               {k: v for k, v in scan_result.items() if k not in ("shells", "primes")}}
    dump(args.out / "mathematical_summary.json", summary)
    output_hashes = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in sorted(args.out.glob("*.json")) if p.name != "execution_receipt.json"}
    receipt = {"utc": datetime.now(timezone.utc).isoformat(), "python": sys.version,
               "platform": platform.platform(), "optimization": sys.flags.optimize,
               "command_arguments": sys.argv[1:], "elapsed_seconds": perf_counter() - start,
               "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               "mathematical_output_sha256": output_hashes}
    dump(args.out / "execution_receipt.json", receipt)
    print(json.dumps({"status": "passed", "check_total": sum(CHECKS.values()),
                      "scan": summary["scan"], "elapsed_seconds": receipt["elapsed_seconds"]},
                     sort_keys=True))


if __name__ == "__main__":
    main()
