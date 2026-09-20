"""Independent exact checks for the integration corrections and new fixed-Q atlas.

This script does not modify the byte-preserved incoming manifest.  It reads the
incoming bounded scan, reconstructs the complete fixed-cofactor middle fibre
from its defining divisor set, compares it with every recorded original M
state, and checks the strict examples used in the corrected proof.
"""

from __future__ import annotations

import json
import hashlib
from math import gcd, isqrt
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def divisors(n: int) -> list[int]:
    small: list[int] = []
    large: list[int] = []
    for d in range(1, isqrt(n) + 1):
        if n % d:
            continue
        small.append(d)
        if d * d != n:
            large.append(n // d)
    return small + large[::-1]


def fixed_q_targets(p: int, h: int) -> list[tuple[int, int, int, int, int, int, int]]:
    assert h >= 3 and h % 4 == 3
    j = (h + 1) // 4
    out = []
    for U in divisors(j * j):
        if (p + 4 * U) % h:
            continue
        R = (p + 4 * U) // h
        assert 0 < R < p
        assert R % 4 == 3
        a = (p + R) // 4
        g = gcd(j, U)
        hm = g * g // U
        rm = U // g
        lm = j // g
        sm = R * lm - rm

        assert p < 4 * a < 2 * p
        assert R == 4 * a - p
        assert hm * rm * rm == U
        assert hm * rm * sm == a
        assert rm + sm == R * lm
        assert gcd(rm, sm) == 1
        assert a * a % U == 0
        assert (a + U) % R == 0
        assert 4 * hm * rm * lm - 1 == h
        out.append((U, a, R, hm, rm, sm, lm))
    return out


def is_negative_four_square(value: int) -> tuple[bool, int]:
    if value >= 0 or (-value) % 4:
        return False, 0
    c = isqrt((-value) // 4)
    return 4 * c * c == -value, c


scan_path = ROOT / "certificates" / "scan.json"
scan_sha256 = hashlib.sha256(scan_path.read_bytes()).hexdigest()
assert scan_sha256 == "c7758b41a41c7c6fdfef94a6945714ad70950ae46d7c827b79cbba097d2433e8"
scan = json.loads(scan_path.read_text(encoding="utf-8"))

middle_by_prime_q: dict[tuple[int, int], set[tuple[int, int, int, int, int, int, int]]] = {}
exterior_states: list[tuple[int, list[int]]] = []
for row in scan["rows"]:
    p = row["p"]
    for state in row["states"]:
        channel, a, u, R, h, r, s, k, _x, _y, _z = state
        if channel == "M":
            Q = 4 * h * r * k - 1
            middle_by_prime_q.setdefault((p, Q), set()).add((u, a, R, h, r, s, k))
        elif channel == "E":
            exterior_states.append((p, state))

eligible_sources = 0
source_target_incidences = 0
distinct_targets: set[tuple[int, int, int, int, int, int, int, int]] = set()
negative_square_sources = 0
negative_square_empty = 0
identity_checks = 0

for p, state in exterior_states:
    _, a, u, R, h, r, s, kappa, _x, _y, _z = state
    D = (4 * u + 1) // R
    assert R * D == 4 * u + 1
    assert R * kappa == p * r + s
    alpha = h * s * s - R
    beta = h * s * s - D
    neg_a, _ca = is_negative_four_square(alpha)
    neg_b, _cb = is_negative_four_square(beta)
    if neg_a or neg_b:
        negative_square_sources += 1

    if h % 4 != 3:
        continue
    eligible_sources += 1
    expected = set(fixed_q_targets(p, h))
    actual = middle_by_prime_q.get((p, h), set())
    assert expected == actual, (p, h, expected ^ actual)
    source_target_incidences += len(expected)
    for target in expected:
        distinct_targets.add((p,) + target)
        identity_checks += 9
    if (neg_a or neg_b) and not expected:
        negative_square_empty += 1

assert eligible_sources == 1293
assert source_target_incidences == 933
assert len(distinct_targets) == 511
assert identity_checks == 8397
assert negative_square_sources == 227
assert negative_square_empty == 44

# The omitted alpha gate really excludes this tempting divisor candidate.
p, h, c, s0, ell, r0 = 5209, 95, 2, 5, 11, 4
R0 = h * s0 * s0 + 4 * c * c
u0 = h * r0 * r0
assert (p + 4 * c * c) // h == s0 * ell
assert (s0 + ell) // 4 == r0
assert gcd(r0, s0) == 1 and p < 4 * h * r0 * s0 < 2 * p
assert (4 * u0 + 1) % R0 == 1299

# Strict improvement: c does not divide j, but another fixed-Q word returns.
p, h, c = 41161, 11, 5
j = (h + 1) // 4
assert j % c != 0
e_state = {
    "a": 10318,
    "R": 111,
    "u": 9678284,
    "r": 938,
    "s": 1,
    "kappa": 347829,
    "D": 348767,
}
assert e_state["a"] == h * e_state["r"] * e_state["s"]
assert e_state["u"] == h * e_state["r"] ** 2
assert p < 4 * e_state["a"] < 2 * p
assert gcd(e_state["r"], e_state["s"]) == 1
assert e_state["a"] ** 2 % e_state["u"] == 0
assert p % 840 == 1
assert e_state["R"] == 4 * e_state["a"] - p
assert e_state["R"] * e_state["D"] == 4 * e_state["u"] + 1
assert e_state["R"] * e_state["kappa"] == p * e_state["r"] + e_state["s"]
alpha = h * e_state["s"] ** 2 - e_state["R"]
beta = h * e_state["s"] ** 2 - e_state["D"]
assert (alpha, beta) == (-100, -348756)
targets_41161 = fixed_q_targets(p, h)
assert targets_41161 == [(3, 11226, 3743, 3, 1, 3742, 1)]
U, aM, RM, hM, rM, sM, lambdaM = targets_41161[0]
denominators = (aM, p * hM * sM * lambdaM, p * hM * rM * lambdaM)
x, y, z = denominators
assert 4 * x * y * z == p * (x * y + x * z + y * z)

# Lucas primality certificate for 41161 with base 22.
factor_primes = (2, 3, 5, 7)
expected_residues = (41160, 40429, 26424, 13707)
assert pow(22, p - 1, p) == 1
for q, residue in zip(factor_primes, expected_residues):
    got = pow(22, (p - 1) // q, p)
    assert got == residue
    assert gcd(got - 1, p) == 1

# A genuine empty fixed-Q negative-square slice.
p, h, c = 3049, 31, 6
j = (h + 1) // 4
e_state_3049 = {
    "a": 806,
    "R": 175,
    "u": 20956,
    "r": 26,
    "s": 1,
    "kappa": 453,
    "D": 479,
}
assert e_state_3049["a"] == h * e_state_3049["r"] * e_state_3049["s"]
assert e_state_3049["u"] == h * e_state_3049["r"] ** 2
assert e_state_3049["R"] == 4 * e_state_3049["a"] - p
assert e_state_3049["R"] * e_state_3049["D"] == 4 * e_state_3049["u"] + 1
assert e_state_3049["R"] * e_state_3049["kappa"] == p * e_state_3049["r"] + e_state_3049["s"]
assert e_state_3049["a"] ** 2 % e_state_3049["u"] == 0
assert e_state_3049["a"] ** 2 // e_state_3049["u"] == h
assert gcd(e_state_3049["r"], e_state_3049["s"]) == 1
assert p % 840 == 529
assert h * e_state_3049["s"] ** 2 - e_state_3049["R"] == -4 * c * c
x3049 = e_state_3049["a"]
y3049 = h * e_state_3049["s"] * e_state_3049["kappa"]
z3049 = p * h * e_state_3049["r"] * e_state_3049["kappa"]
assert (x3049, y3049, z3049) == (806, 14043, 1113244782)
assert 4 * x3049 * y3049 * z3049 == p * (x3049 * y3049 + x3049 * z3049 + y3049 * z3049)
# Lucas primality certificate for 3049 with base 11.
assert pow(11, p - 1, p) == 1
for q, residue in zip((2, 3, 127), (3048, 2516, 3041)):
    got = pow(11, (p - 1) // q, p)
    assert got == residue
    assert gcd(got - 1, p) == 1
assert fixed_q_targets(p, h) == []
assert {U % h for U in divisors(j * j)} == {1, 2, 4, 8, 16}
assert c * c % h == 5

receipt = {
    "schema_version": 1,
    "certificate": "Turn 7 Fabel integration corrections and complete fixed-Q atlas",
    "incoming_scan_bound": scan["bound"],
    "incoming_scan_sha256": scan_sha256,
    "incoming_scan_totals": scan["totals"],
    "checks": {
        "eligible_E_sources_h_3_mod_4": eligible_sources,
        "source_target_incidences": source_target_incidences,
        "distinct_fixed_Q_targets": len(distinct_targets),
        "fixed_Q_asserted_identities": identity_checks,
        "negative_square_sources": negative_square_sources,
        "negative_square_sources_with_empty_fixed_Q_fibre": negative_square_empty,
        "alpha_missing_gate_counterexample": {
            "p": 5209,
            "h": 95,
            "c": 2,
            "s": 5,
            "r": 4,
            "R": R0,
            "remainder": 1299,
        },
        "strict_generalization_example": {
            "p": 41161,
            "lucas_base": 22,
            "c": 5,
            "j": 3,
            "selected_word_unavailable": True,
            "fixed_Q_word": U,
            "middle_state": [aM, RM, U, hM, rM, sM, lambdaM],
            "denominators": list(denominators),
        },
        "empty_fixed_Q_example": {
            "p": 3049,
            "h": 31,
            "j": 8,
            "c": 6,
            "exterior_state": [806, 175, 20956, 31, 26, 1, 453, 479, -144, -448],
            "denominators": [806, 14043, 1113244782],
            "divisor_residues": [1, 2, 4, 8, 16],
        },
    },
    "nonclaims": [
        "The fixed-Q fibre does not supply an exterior source at an unoccupied prime.",
        "The selected c|j square words do not exhaust the complete fixed-Q fibre.",
        "The finite replay is a regression certificate for the proved formulas, not a universal ES computation.",
    ],
}

out = ROOT / "integration_extension_receipt.json"
out.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(receipt, indent=2, sort_keys=True))
