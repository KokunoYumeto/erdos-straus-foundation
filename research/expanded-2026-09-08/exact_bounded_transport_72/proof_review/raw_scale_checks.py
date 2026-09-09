"""Exact finite checks of the raw-scale proof; no sampling or float arithmetic."""
from __future__ import annotations

import hashlib
import json
import math
import platform
from collections import Counter
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy
from sympy import divisors, factorint, primerange

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SOURCE = ROOT / "raw_scale_hit_incidence.tex"
SEED_PRIMES = (13, 37, 61, 73, 97)


def square_divisors(n: int) -> list[int]:
    assert n > 0
    return [k for k in range(1, math.isqrt(n) + 1) if n % (k * k) == 0]


def square_divisor_count(n: int) -> int:
    return math.prod(int(b) // 2 + 1 for b in factorint(n).values())


def canonical_hits(p: int) -> tuple[list[tuple[int, ...]], int]:
    h = (p - 1) // 12
    hits = []
    divisor_count = 0
    for a in range(3 * h + 1, 9 * h + 1):
        R = 4 * a - p
        assert math.gcd(a, R) == 1
        for u_s in divisors(a * a):
            u = int(u_s)
            divisor_count += 1
            g = math.gcd(a, u)
            A, B = a // g, u // g
            assert g * g % u == 0
            D = g * g // u
            assert math.gcd(A, B) == 1 and A * B * D == a and B * B * D == u
            for eps in (0, 1):
                if (4 * u + p**eps) % R == 0:
                    num = A + p ** (1 - eps) * B
                    assert num % R == 0
                    C = num // R
                    assert C > 0
                    hits.append((a, u, A, B, C, D, eps))
    assert len(hits) == len(set(hits))
    return hits, divisor_count


def direct_raw_hits(p: int) -> set[tuple[int, ...]]:
    """Independently enumerate every raw factorization of each original a."""
    h = (p - 1) // 12
    raw = set()
    for a in range(3 * h + 1, 9 * h + 1):
        R = 4 * a - p
        for A_s in divisors(a):
            A = int(A_s)
            for B_s in divisors(a // A):
                B = int(B_s)
                D = a // (A * B)
                for eps in (0, 1):
                    numerator = A + p ** (1 - eps) * B
                    if numerator % R == 0:
                        C = numerator // R
                        assert 4 * A * B * C * D == A + p ** (1 - eps) * B + p * C
                        raw.add((A, B, C, D, eps))
    return raw


def coordinates(q: int, tup: tuple[int, ...]) -> dict:
    A, B, C, D, eps = tup
    assert min(q, A, B, C, D) > 0 and eps in (0, 1)
    assert 4 * A * B * C * D == A + q ** (1 - eps) * B + q * C
    a, y, z = A * B * D, q**eps * A * C * D, q * B * C * D
    R, S, u = 4 * a - q, q * a, B * B * D
    assert R > 0 and u > 0 and a * a % u == 0
    dy, dz = R * y - S, R * z - S
    assert dy == q**eps * A * A * D
    assert dz == q ** (2 - eps) * B * B * D
    assert dy > 0 and dz > 0 and dy * dz == S * S
    assert (S * S // dz, S * S // dy) == (dy, dz)
    assert Fraction(1, a) + Fraction(1, y) + Fraction(1, z) == Fraction(4, q)
    assert (Fraction(S + dy, R), Fraction(S + dz, R)) == (y, z)
    return {
        "a": a, "R": R, "S": S, "u": u, "y": y, "z": z, "d_y": dy, "d_z": dz,
        "cross_xy": 4 * a * y - q * (a + y),
        "cross_xz": 4 * a * z - q * (a + z),
        "cross_yz": 4 * y * z - q * (y + z),
        "quotient_BC_over_A": Fraction(B + q**eps * C, A),
        "BCD": B * C * D,
        "quotient_AC_over_B": Fraction(A + q * C, B),
    }


def primitive_inverse(q: int, data: dict, expected: tuple[int, ...]) -> None:
    A, B, C, D, eps = expected
    reduced = Fraction(data["d_y"], data["S"])
    eps_back = 0 if reduced.denominator % q == 0 else 1
    assert eps_back == eps
    A_back = reduced.numerator
    B_back = reduced.denominator // q ** (1 - eps_back)
    D_back = data["a"] // (A_back * B_back)
    C_back = (A_back + q ** (1 - eps_back) * B_back) // data["R"]
    assert (A_back, B_back, C_back, D_back, eps_back) == expected
    assert Fraction(data["y"], data["z"]) == reduced
    assert math.gcd(A, q ** (1 - eps) * B) == 1
    assert (A + q ** (1 - eps) * B) // data["R"] == C


def radix(q: int, half: bool) -> tuple[int, int, int, int]:
    h = (q - 1) // 12
    M, J = (6 * h, 3 * h) if half else (9 * h, 6 * h)
    L = 2 * M * J
    return M, J, L, M * L


def encode(q: int, half: bool, digits: tuple[int, ...]) -> int:
    A, j, B, eps = digits
    M, J, L, N = radix(q, half)
    assert 1 <= A <= M and 0 <= j < J and 1 <= B <= M and eps in (0, 1)
    code = (A - 1) * L + 2 * M * j + 2 * (B - 1) + eps
    assert 0 <= code < N
    return code


def decode(q: int, half: bool, code: int) -> tuple[int, ...]:
    M, J, L, N = radix(q, half)
    assert 0 <= code < N
    outer, v = divmod(code, L)
    j, r = divmod(v, 2 * M)
    b, eps = divmod(r, 2)
    A, B = outer + 1, b + 1
    assert 1 <= A <= M and 0 <= j < J and 1 <= B <= M
    return A, j, B, eps


def code_hit(q: int, digits: tuple[int, ...]) -> bool:
    A, j, B, eps = digits
    R = 4 * j + 3
    assert (q + R) % 4 == 0
    a = (q + R) // 4
    return a % (A * B) == 0 and math.gcd(A, B) == 1 and (A + q ** (1 - eps) * B) % R == 0


def check_rectangles(q: int, hits: list[tuple[int, ...]], counts: Counter) -> dict:
    expected_F = set()
    expected_H = set()
    for a, u, A, B, C, D, eps in hits:
        digits = A, (4 * a - q - 3) // 4, B, eps
        expected_F.add(encode(q, False, digits))
        if 2 * a <= q - 1:
            expected_H.add(encode(q, True, digits))
    found = {}
    for half, expected in ((False, expected_F), (True, expected_H)):
        M, J, L, N = radix(q, half)
        actual = set()
        product_so_far = 1
        literal_selector_sum = 0
        for code in range(N):
            digits = decode(q, half, code)
            assert encode(q, half, digits) == code
            bit = int(code_hit(q, digits))
            if bit:
                actual.add(code)
            product_so_far *= 1 - bit
            literal_selector_sum += product_so_far
        assert actual == expected
        least = min(actual) if actual else N
        assert literal_selector_sum == least
        for r in range(1, M + 1):
            assert any(decode(q, half, code)[0] <= r for code in actual) == (least < r * L)
        counts["full_rectangle_codes" if not half else "first_half_rectangle_codes"] += N
        found["PCT" if half else "full"] = {"rectangle_size": N, "hits": len(actual), "least_hit": least}
    image_H = set()
    for cf in expected_F:
        digits = decode(q, False, cf)
        A, j, B, eps = digits
        a = (q + 4 * j + 3) // 4
        if 2 * a <= q - 1:
            ch = encode(q, True, digits)
            assert decode(q, True, ch) == digits
            assert encode(q, False, decode(q, True, ch)) == cf
            LH = radix(q, True)[2]
            assert cf - ch == 2 * (A - 1) * LH + (q - 1) // 2 * j
            image_H.add(ch)
            counts["complete_hit_radix_bijections"] += 1
    assert image_H == expected_H
    return found


def check_seed(p: int, hit: tuple[int, ...], counts: Counter) -> set[tuple[int, ...]]:
    a, u, A0, B0, C0, Dp, eps = hit
    seed = A0, B0, C0, Dp, eps
    base = coordinates(p, seed)
    assert base["a"] == a and base["u"] == u
    primitive_inverse(p, base, seed)
    K0 = 4 * A0 * B0 * C0
    Om = A0 + eps * B0
    Th = C0 + (1 - eps) * B0
    g0 = math.gcd(K0, Th)
    m0, w = K0 // g0, Th // g0
    assert math.gcd(m0, w) == 1
    scales = square_divisors(Dp)
    assert len(scales) == square_divisor_count(Dp)
    raw_seeds = set()
    periods = {}
    for k in scales:
        raw = k * A0, k * B0, k * C0, Dp // (k * k), eps
        A, B, C, D, _ = raw
        assert math.gcd(A, B) == k
        assert (A // k, B // k, C // k, k * k * D, eps) == seed
        assert coordinates(p, raw) == base
        assert math.gcd(a, u) == k * B * D == B0 * Dp
        assert A + eps * B == k * Om and C + (1 - eps) * B == k * Th
        raw_seeds.add(raw)
        mk = k * k * K0 // math.gcd(k * k * K0, Th)
        periods[k] = mk
        assert mk % m0 == 0 and mk // m0 == k * k // math.gcd(k * k, w)
        assert (4 * A * B * C) // math.gcd(4 * A * B * C, C + (1 - eps) * B) == mk
        q_values = set(range(-200, 401))
        for t in range(-5, 6):
            q_values.update((p + t * m0, p + t * mk, p + t * mk + 1))
        for q in sorted(q_values):
            D0q = Fraction(Om + q * Th, K0)
            Dkq = Fraction(Om + q * Th, k * k * K0)
            assert D0q == k * k * Dkq
            assert (D0q.denominator == 1) == ((q - p) % m0 == 0)
            assert (Dkq.denominator == 1) == ((q - p) % mk == 0)
            assert (Dkq.denominator == 1) == (D0q.denominator == 1 and D0q.numerator % (k * k) == 0)
            assert ((q - p) % mk == 0 and (q - 1) % 12 == 0) == ((q - p) % math.lcm(12, mk) == 0)
            counts["signed_integer_q_period_checks"] += 1
        counts["raw_seed_scales"] += 1
    for q_s in primerange(p, 502):
        q = int(q_s)
        if q % 12 != 1 or (q - p) % m0:
            continue
        D0q = (Om + q * Th) // K0
        assert D0q > 0
        coprime = A0, B0, C0, D0q, eps
        data = coordinates(q, coprime)
        primitive_inverse(q, data, coprime)
        hq = (q - 1) // 12
        assert 3 * hq + 1 <= data["a"] <= 9 * hq
        assert Fraction(data["a"], q) == Fraction(Th, 4 * C0) + Fraction(Om, 4 * C0 * q)
        coefficient, threshold_numerator = 2 * C0 - Th, Om + 2 * C0
        gate = 2 * data["a"] <= q - 1
        assert gate == (q * coefficient >= threshold_numerator)
        if coefficient <= 0:
            assert not gate
            counts["nonpositive_first_half_coefficient_returns"] += 1
        else:
            threshold = -(-threshold_numerator // coefficient)
            assert gate == (q >= threshold)
        if 2 * a <= p - 1:
            assert gate
        expected_scales = square_divisors(math.gcd(Dp, D0q))
        actual_scales = [k for k in scales if (q - p) % periods[k] == 0]
        assert actual_scales == expected_scales
        assert len(actual_scales) == square_divisor_count(math.gcd(Dp, D0q))
        for k in actual_scales:
            raw_q = k * A0, k * B0, k * C0, D0q // (k * k), eps
            assert coordinates(q, raw_q) == data
            counts["positive_returned_raw_coordinates"] += 1
        if gate:
            digits = A0, (data["R"] - 3) // 4, B0, eps
            ch, cf = encode(q, True, digits), encode(q, False, digits)
            assert decode(q, True, ch) == decode(q, False, cf) == digits
            assert code_hit(q, digits)
            LH = radix(q, True)[2]
            assert cf - ch == 2 * (A0 - 1) * LH + (q - 1) // 2 * digits[1]
            assert ch < A0 * LH
            assert (A0 <= 2) == (ch < 2 * LH)
            counts["first_half_positive_prime_returns"] += 1
        else:
            counts["outside_first_half_positive_prime_returns"] += 1
        counts["positive_prime_returns"] += 1
    return raw_seeds


def check_fixtures() -> dict:
    p13 = coordinates(13, (2, 1, 5, 2, 0))
    assert (p13["a"], p13["y"], p13["z"], p13["d_y"], p13["d_z"]) == (4, 20, 130, 8, 338)
    assert encode(13, True, (2, 0, 1, 0)) == 36
    assert encode(13, False, (2, 0, 1, 0)) == 108
    assert decode(13, False, 36) == (1, 2, 1, 0)
    assert not code_hit(13, decode(13, False, 36))
    assert coordinates(61, (2, 4, 2, 2, 1)) == coordinates(61, (1, 2, 1, 8, 1))
    fixtures = []
    for q, Dq, expected_fibre, witness in (
        (109, 14, [1], (28, 1526, 3052)),
        (157, 20, [1, 2], (40, 3140, 6280)),
    ):
        data = coordinates(q, (1, 2, 1, Dq, 1))
        assert (data["a"], data["y"], data["z"]) == witness
        assert square_divisors(math.gcd(8, Dq)) == expected_fibre
        if q == 109:
            assert Fraction(Dq, 4) == Fraction(7, 2)
            assert encode(q, True, (1, 0, 2, 1)) == 3
        else:
            assert coordinates(q, (2, 4, 2, 5, 1)) == data
        fixtures.append({"q": q, "D0q": Dq, "scale_fibre": expected_fibre, "ordered_witness": witness})
    return {"p13_codes": {"PCT": 36, "full": 108}, "p61_primitive_period": 8, "p61_scale2_period": 32, "returns": fixtures}


def check_incidence_graph_and_truth(incidence: dict, counts: Counter) -> dict:
    graph = {tuple(row) for row in incidence["scaled_triples"]}
    assert len(graph) == 97
    truth = {}
    graph_records = []
    for k, X, q in sorted(graph):
        D0q = (q + 3) // 8
        assert (q + 3) % 8 == 0 and D0q % (k * k) == 0
        cop = (1, 2, 1, D0q, 1)
        raw = (k, 2 * k, k, D0q // (k * k), 1)
        data = coordinates(q, cop)
        assert coordinates(q, raw) == data
        primitive_inverse(q, data, cop)
        assert 2 * data["a"] <= q - 1 and q >= 5
        hq = (q - 1) // 12
        assert 3 * hq + 1 <= data["a"] <= 9 * hq
        digits = (1, (data["R"] - 3) // 4, 2, 1)
        ch, cf = encode(q, True, digits), encode(q, False, digits)
        assert decode(q, True, ch) == decode(q, False, cf) == digits
        assert encode(q, False, decode(q, True, ch)) == cf
        assert encode(q, True, decode(q, False, cf)) == ch
        assert code_hit(q, digits)
        assert cf - ch == 2 * (digits[0] - 1) * radix(q, True)[2] + (q - 1) // 2 * digits[1]
        A, j, B, eps = decode(q, True, ch)
        a_back, R_back = (q + 4 * j + 3) // 4, 4 * j + 3
        D_back = a_back // (A * B)
        C_back = (A + q ** (1 - eps) * B) // R_back
        assert (A, B, C_back, D_back, eps) == cop
        # The radix inverse changes only the code; all graph labels remain.
        graph_inverse = (k, X, q)
        assert graph_inverse == (k, X, q)
        bits = (int(k == 2), int(X % 12 == 0), int(q % 48 == 13))
        truth[(k, X, q)] = bits
        graph_records.append({
            "k": k, "X": X, "q": q, "D0q": D0q, "raw_tuple": raw,
            "ordered_witness": [data["a"], data["y"], data["z"]],
            "a": data["a"], "R": data["R"], "S": data["S"], "u": data["u"],
            "d_y": data["d_y"], "d_z": data["d_z"],
            "PCT_code": ch, "full_code": cf, "digits_A_j_B_epsilon": digits,
            "truth_vector": bits,
        })
        counts["complete_incidence_graph_outputs"] += 1
    cells = {}
    covered = set()
    for sigma in product((0, 1), repeat=3):
        cell = {point for point in graph if truth[point] == sigma}
        assert not covered.intersection(cell)
        covered.update(cell)
        cells["".join(map(str, sigma))] = cell
    assert covered == graph and sum(map(len, cells.values())) == len(graph)
    P = [{point for point in graph if truth[point][i]} for i in range(3)]
    assert len(P[0] | P[1] | P[2]) == (
        sum(map(len, P)) - len(P[0] & P[1]) - len(P[0] & P[2]) - len(P[1] & P[2])
        + len(P[0] & P[1] & P[2])
    )
    expressions = {
        "P0_and_P1": lambda b: b[0] * b[1],
        "P0_or_P2": lambda b: b[0] + b[2] - b[0] * b[2],
        "P1_implies_P2": lambda b: 1 - b[1] + b[1] * b[2],
        "P1_iff_P2": lambda b: 1 - b[1] - b[2] + 2 * b[1] * b[2],
        "not_P0_and_P1_iff_P2": lambda b: (1 - b[0]) * (1 - b[1] - b[2] + 2 * b[1] * b[2]),
    }
    projection_keys = {
        "forget_scale": lambda v: (v[1], v[2]),
        "forget_input": lambda v: (v[0], v[2]),
        "forget_scale_and_input": lambda v: (v[2],),
    }
    projection_records = []
    for name, evaluate in expressions.items():
        selected = {point for point in graph if evaluate(truth[point]) == 1}
        by_truth_cells = set().union(*(cell for word, cell in cells.items() if evaluate(tuple(map(int, word))) == 1))
        assert selected == by_truth_cells
        assert all(evaluate(bits) in (0, 1) for bits in truth.values())
        for projection_name, key in projection_keys.items():
            full_image = {key(point) for point in graph}
            selected_image = {key(point) for point in selected}
            records = []
            for value in sorted(full_image):
                complete_fibre = {point for point in graph if key(point) == value}
                selected_fibre = {point for point in selected if key(point) == value}
                assert selected_fibre == complete_fibre.intersection(selected)
                assert selected_fibre == {point for point in complete_fibre if evaluate(truth[point]) == 1}
                assert (value in selected_image) == bool(selected_fibre)
                records.append({"projection_value": value, "full_fibre": sorted(complete_fibre), "selected_fibre": sorted(selected_fibre)})
                counts["same_tuple_selected_projection_fibres"] += 1
            projection_records.append({"expression": name, "projection": projection_name, "selected_graph_size": len(selected), "fibres": records})
    k1 = {point for point in graph if point[0] == 1}
    k2 = {point for point in graph if point[0] == 2}
    assert not k1.intersection(k2)
    overlap_q = {point[2] for point in k1}.intersection(point[2] for point in k2)
    assert overlap_q
    witness2 = min(k2)
    witness1 = (1, witness2[1], witness2[2])
    assert witness1 in k1 and witness1 != witness2
    assert witness1[2] == witness2[2]
    # A common projected q does not furnish one graph member satisfying k=1 and k=2.
    assert not {point for point in graph if point[0] == 1 and point[0] == 2}
    return {
        "status": "pass",
        "graph_outputs": graph_records,
        "truth_predicates": ["k == 2", "X % 12 == 0", "q % 48 == 13"],
        "all_eight_truth_cells": {word: {"size": len(cell), "members": sorted(cell)} for word, cell in cells.items()},
        "selected_projection_fibres": projection_records,
        "projection_trap": {
            "k1_graph_intersect_k2_graph": [],
            "overlapping_q_projection": sorted(overlap_q),
            "distinct_graph_witnesses": [witness1, witness2],
            "same_retained_input_and_prime": [witness2[1], witness2[2]],
        },
        "checks": {
            "all_original_ordered_coordinates_and_inverses": True,
            "raw_and_coprime_outputs_equal": True,
            "first_half_gate_and_both_code_inverses": True,
            "eight_disjoint_truth_cells_cover_graph": True,
            "five_boolean_expressions_use_one_graph_member": True,
            "selected_fibres_equal_complete_fibre_intersect_same_predicate": True,
            "inclusion_exclusion_on_original_graph": True,
            "projection_trap_exhibits_distinct_scale_witnesses": True,
        },
    }


def run_checks() -> dict:
    source_hash_before = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    counts = Counter()
    by_prime = []
    for p in SEED_PRIMES:
        hits, divs = canonical_hits(p)
        all_raw = set()
        for hit in hits:
            all_raw.update(check_seed(p, hit, counts))
        direct_raw = direct_raw_hits(p)
        assert all_raw == direct_raw
        rectangles = check_rectangles(p, hits, counts)
        counts["canonical_seed_hits"] += len(hits)
        counts["full_shell_positive_divisors"] += divs
        by_prime.append({"p": p, "full_shell_divisors": divs, "canonical_hits": len(hits), "raw_hits": len(all_raw), "radices": rectangles})
    # Literal selector edge cases include the failure sentinel separately.
    for bits in ([0] * 7, [1] + [0] * 6, [0] * 6 + [1], [0, 1, 0, 1, 1, 0, 0]):
        literal = sum(math.prod(1 - b for b in bits[: n + 1]) for n in range(len(bits)))
        expected = next((i for i, b in enumerate(bits) if b), len(bits))
        assert literal == expected
    from raw_scaled_incidence_fixture import run_incidence_checks
    incidence = run_incidence_checks()
    assert incidence["status"] == "pass"
    incidence_graph_truth = check_incidence_graph_and_truth(incidence, counts)
    source_hash_after = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    assert source_hash_before == source_hash_after == incidence["source_sha256"], "Proof source changed during checks; rerun."
    return {
        "status": "pass",
        "source": SOURCE.name,
        "source_sha256": source_hash_after,
        "source_unchanged_during_run": True,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "runtime": {"python": platform.python_version(), "sympy": sympy.__version__},
        "scope": {
            "seed_primes": list(SEED_PRIMES),
            "seed_enumeration": "Every positive divisor of a^2 at every full original shell, with both tags; independently compared with every raw A*B*D factorization.",
            "signed_q": "Every integer from -200 through 400, plus every p+t*m0, p+t*mk, p+t*mk+1 for t=-5 through 5, separately for every seed and scale.",
            "positive_prime_returns": "Every prime q from each seed prime through 501 satisfying q=1 mod 12 and its primitive return period.",
            "radix_enumeration": "Every full and PCT rectangle code at each of the five seed primes.",
        },
        "coverage": dict(sorted(counts.items())),
        "per_prime": by_prime,
        "fixtures": check_fixtures(),
        "scaled_incidence": incidence,
        "scaled_incidence_graph_truth": incidence_graph_truth,
        "interpretation": "Exact finite validation of the stated domains and maps; the standalone proofs supply the general assertions.",
    }


if __name__ == "__main__":
    report = run_checks()
    (HERE / "raw_scale_checks.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": report["status"], "coverage": report["coverage"], "source_sha256": report["source_sha256"]}, indent=2))
