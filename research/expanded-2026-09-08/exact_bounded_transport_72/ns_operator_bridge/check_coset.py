"""Independent exact finite-character checks for sieve_character_cover.tex.

Only integers and fractions are used. Character sums are accumulated as
integer exponent histograms and reduced in Z[X]/Phi_N(X); no floating point
or pre-assumed character-orthogonality predicate evaluates those sums.
Every packet entry keeps its complete, original labelled exponent tuple.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from pathlib import Path


def trim(poly):
    poly = list(poly)
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def div_monic(dividend, divisor):
    dividend, divisor = trim(dividend), trim(divisor)
    assert divisor[-1] == 1
    quotient = [0] * max(1, len(dividend) - len(divisor) + 1)
    while len(dividend) >= len(divisor) and any(dividend):
        shift = len(dividend) - len(divisor)
        leading = dividend[-1]
        quotient[shift] += leading
        for i, coefficient in enumerate(divisor):
            dividend[shift + i] -= leading * coefficient
        dividend = trim(dividend)
    return trim(quotient), dividend


@lru_cache(None)
def cyclotomic(n):
    assert n >= 1
    polynomial = [-1] + [0] * (n - 1) + [1]
    for d in range(1, n):
        if n % d == 0:
            polynomial, remainder = div_monic(polynomial, cyclotomic(d))
            assert remainder == [0]
    return tuple(polynomial)


def exact_average(histogram, denominator):
    """Return the complete rational coefficient vector modulo Phi_N."""
    _, remainder = div_monic(histogram, cyclotomic(len(histogram)))
    return tuple(Fraction(x, denominator) for x in remainder)


def integer_value(histogram, denominator):
    value = exact_average(histogram, denominator)
    assert len(value) == 1, (histogram, denominator, value)
    assert value[0].denominator == 1, value
    return int(value[0])


@dataclass(frozen=True)
class Group:
    orders: tuple[int, ...]

    def __post_init__(self):
        assert self.orders and all(n >= 1 for n in self.orders)

    @property
    def elements(self):
        return tuple(itertools.product(*(range(n) for n in self.orders)))

    @property
    def zero(self):
        return tuple(0 for _ in self.orders)

    @property
    def order(self):
        return math.prod(self.orders)

    @property
    def exponent(self):
        return math.lcm(*self.orders)

    def add(self, a, b):
        return tuple((x + y) % n for x, y, n in zip(a, b, self.orders))

    def mul(self, k, a):
        return tuple(k * x % n for x, n in zip(a, self.orders))

    def sub(self, a, b):
        return self.add(a, self.mul(-1, b))

    def phase(self, alpha, g):
        return sum(
            a * x * (self.exponent // n)
            for a, x, n in zip(alpha, g, self.orders)
        ) % self.exponent

    def J(self, alpha, beta):
        return (self.add(self.mul(3, alpha), beta),
                self.add(alpha, self.mul(5, beta)))


def coset_representatives(group, subgroup):
    unseen = set(group.elements)
    representatives = []
    while unseen:
        representative = min(unseen)
        representatives.append(representative)
        coset = {group.add(representative, h) for h in subgroup}
        assert coset <= unseen
        unseen -= coset
    return tuple(representatives)


def packet_entries(group, factors):
    """factors entries are (original label, original bound, group image)."""
    entries = []
    for exponents in itertools.product(*(range(bound + 1) for _, bound, _ in factors)):
        residue = group.zero
        for exponent, (_, _, generator) in zip(exponents, factors):
            residue = group.add(residue, group.mul(exponent, generator))
        entries.append((exponents, residue))
    return tuple(entries)


def inspect_histories(group, representatives, delta):
    """Count explicit labelled histories, keeping every rho coordinate."""
    domain = tuple(itertools.product(group.elements, repeat=2))
    maximum_length = 3 if group.order <= 8 else 2
    # The largest direct product case is still checked at length two,
    # including all 614,656 original starting-state/history combinations.
    records = []
    for length in range(maximum_length + 1):
        counts = Counter()
        expansion_count = 0
        for history in itertools.product(representatives, repeat=length):
            for initial in domain:
                state = initial
                for rho in history:
                    first, second = group.J(*state)
                    state = (first, group.add(second, rho))
                counts[state] += 1
                # Check the closed expression without using the recurrence.
                initial_term = initial
                for _ in range(length):
                    initial_term = group.J(*initial_term)
                first_sum, second_sum = initial_term
                for j, rho in enumerate(history):
                    term = (group.zero, rho)
                    for _ in range(length - 1 - j):
                        term = group.J(*term)
                    first_sum = group.add(first_sum, term[0])
                    second_sum = group.add(second_sum, term[1])
                assert state == (first_sum, second_sum)
                expansion_count += 1
        assert len(counts) == len(domain)
        assert set(counts.values()) == {delta ** length}
        assert sum(counts.values()) == len(domain) * delta ** length
        records.append({"length": length, "original_histories_checked": expansion_count,
                        "output_count": len(counts), "each_fibre_size": delta ** length})
    return records


def inspect_group(name, orders, factors, full_targets=False):
    group = Group(tuple(orders))
    elements = group.elements
    domain = tuple(itertools.product(elements, repeat=2))
    image_fibres = {}
    for alpha, beta in domain:
        image_fibres.setdefault(group.J(alpha, beta), []).append((alpha, beta))
    torsion = tuple(g for g in elements if group.mul(14, g) == group.zero)
    subgroup = {group.mul(14, g) for g in elements}
    delta = len(torsion)
    representatives = coset_representatives(group, subgroup)
    assert len(representatives) == delta
    for first, second in domain:
        condition = group.sub(second, group.mul(5, first)) in subgroup
        fibre = image_fibres.get((first, second), [])
        assert bool(fibre) == condition
        assert len(fibre) == (delta if condition else 0)
        reconstructed = []
        for alpha in elements:
            if group.mul(-14, alpha) == group.sub(second, group.mul(5, first)):
                reconstructed.append((alpha, group.sub(first, group.mul(3, alpha))))
        assert set(reconstructed) == set(fibre)
    assert set(image_fibres[(group.zero, group.zero)]) == {
        (g, group.mul(-3, g)) for g in torsion
    }

    # Equality for every indicator function F, hence the full finite average.
    cover_counts = Counter()
    for rho in representatives:
        for alpha, beta in domain:
            first, second = group.J(alpha, beta)
            cover_counts[(first, group.add(second, rho))] += 1
    assert len(cover_counts) == group.order ** 2
    assert set(cover_counts.values()) == {delta}

    @lru_cache(None)
    def pair_averages(g1, g2):
        bare_histogram = [0] * group.exponent
        direct_histogram = [0] * group.exponent
        for alpha, beta in domain:
            first, second = group.J(alpha, beta)
            bare_histogram[(group.phase(first, g1) + group.phase(second, g2))
                           % group.exponent] += 1
            direct_histogram[(group.phase(alpha, g1) + group.phase(beta, g2))
                             % group.exponent] += 1
        covered_histogram = [0] * group.exponent
        for rho in representatives:
            shift = group.phase(rho, g2)
            for exponent, count in enumerate(bare_histogram):
                covered_histogram[(exponent + shift) % group.exponent] += count
        bare = integer_value(bare_histogram, len(domain))
        direct = integer_value(direct_histogram, len(domain))
        covered = integer_value(covered_histogram, delta * len(domain))
        expected_bare = int(g1 in torsion and g2 == group.mul(-3, g1))
        expected_direct = int(g1 == group.zero and g2 == group.zero)
        assert bare == expected_bare
        assert direct == expected_direct == covered
        return bare, direct, covered

    # Character-basis tests are exhaustive, including non-packet frequencies.
    for g1, g2 in domain:
        pair_averages(g1, g2)

    entries = packet_entries(group, factors)
    counts = Counter(residue for _, residue in entries)
    if full_targets:
        targets = domain
    else:
        candidates = (elements[0], elements[-1], elements[len(elements) // 2])
        targets = tuple(dict.fromkeys(itertools.product(candidates, repeat=2)))
    polynomial_terms_checked = 0
    alias_examples = []
    for t1, t2 in targets:
        bare_polynomial = {}
        covered_polynomial = {}
        true_polynomial = {}
        alias_polynomial = {}
        for e1, r1 in entries:
            for e2, r2 in entries:
                monomial = (e1, e2)
                bare, direct, covered = pair_averages(
                    group.sub(r1, t1), group.sub(r2, t2))
                if bare:
                    bare_polynomial[monomial] = bare
                if covered:
                    covered_polynomial[monomial] = covered
                if r1 == t1 and r2 == t2:
                    true_polynomial[monomial] = 1
                for g in torsion:
                    if r1 == group.add(t1, g) and r2 == group.sub(t2, group.mul(3, g)):
                        alias_polynomial[monomial] = alias_polynomial.get(monomial, 0) + 1
                assert direct == int(r1 == t1 and r2 == t2)
                polynomial_terms_checked += 1
        assert covered_polynomial == true_polynomial
        assert bare_polynomial == alias_polynomial
        bare_count = sum(bare_polynomial.values())
        true_count = counts[t1] * counts[t2]
        assert sum(covered_polynomial.values()) == true_count
        assert bare_count == sum(counts[group.add(t1, g)] *
                                 counts[group.sub(t2, group.mul(3, g))] for g in torsion)
        if bare_count != true_count and len(alias_examples) < 3:
            alias_examples.append({"target1": t1, "target2": t2,
                                   "bare": bare_count, "true": true_count})

    # A direct evaluation of the first packet under J composed with itself.
    J2_results = []
    for target in tuple(dict.fromkeys(t for pair in targets for t in pair)):
        total_histogram = [0] * group.exponent
        for alpha, beta in domain:
            first, second = group.J(*group.J(alpha, beta))
            for _, residue in entries:
                phase = group.phase(first, group.sub(residue, target))
                total_histogram[phase] += 1
        actual = integer_value(total_histogram, len(domain))
        predicted = sum(count for residue, count in counts.items()
                        if group.mul(10, group.sub(residue, target)) == group.zero
                        and group.mul(8, group.sub(residue, target)) == group.zero)
        assert actual == predicted
        J2_results.append({"target": target, "bare_J2_first_packet": actual,
                           "true_first_packet": counts[target]})

    return {
        "name": name, "cyclic_orders": orders, "order": group.order,
        "character_exponent": group.exponent,
        "delta": delta, "coset_representatives": representatives,
        "image_size": len(image_fibres), "map_fibres_checked": len(domain),
        "character_basis_pairs_checked": len(domain),
        "packet_factors": [{"label": label, "original_exponent_bound": bound,
                            "group_image": image} for label, bound, image in factors],
        "packet_exponent_vectors": len(entries),
        "target_pairs_checked": len(targets),
        "full_polynomial_terms_checked": polynomial_terms_checked,
        "alias_examples": alias_examples, "J2_first_packet": J2_results,
        "finite_history_checks": inspect_histories(group, representatives, delta),
    }, group, entries, pair_averages


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name("COSET_CHECKS.json"))
    args = parser.parse_args()
    cases = [
        ("trivial", [1], [("label_A", 2, (0,))], True),
        ("U(3), p=13 a=4 R=3", [2], [("prime_2", 4, (1,))], True),
        ("U(7)", [6], [("prime_2", 2, (2,)), ("prime_3", 2, (1,))], True),
        ("U(15), p=97 a=28 R=15", [4, 2], [("prime_2", 4, (1, 0)),
                                            ("prime_7", 2, (3, 1))], True),
        ("U(8)", [2, 2], [("prime_3", 2, (1, 0)),
                            ("prime_5", 2, (0, 1))], True),
        ("C7", [7], [("label_A", 3, (1,)), ("label_B", 2, (3,))], True),
        ("C14", [14], [("label_A", 2, (1,)), ("label_B", 2, (5,))], False),
        ("C4 x C6", [4, 6], [("label_A", 2, (1, 2)),
                                ("label_B", 2, (2, 1))], False),
        ("C2 x C14", [2, 14], [("label_A", 2, (1, 1)),
                                  ("label_B", 2, (0, 5))], False),
        ("C3 x C5", [3, 5], [("label_A", 2, (1, 1)),
                                ("label_B", 2, (2, 1))], False),
        ("C2 x C2 x C2", [2, 2, 2], [("label_A", 2, (1, 0, 1)),
                                        ("label_B", 2, (0, 1, 1))], True),
    ]
    records = []
    fixture = None
    unit_coordinates = {
        "U(3), p=13 a=4 R=3": (3, [2]),
        "U(7)": (7, [3]),
        "U(15), p=97 a=28 R=15": (15, [2, 14]),
        "U(8)": (8, [3, 5]),
    }
    for name, orders, factors, full_targets in cases:
        result, group, entries, averages = inspect_group(name, orders, factors, full_targets)
        if name in unit_coordinates:
            modulus, generators = unit_coordinates[name]
            residue_map = {
                coordinate: math.prod(pow(g, e, modulus) for g, e in zip(generators, coordinate)) % modulus
                for coordinate in group.elements
            }
            units = {r for r in range(modulus) if math.gcd(r, modulus) == 1}
            assert len(set(residue_map.values())) == group.order
            assert set(residue_map.values()) == units
            for left, right in itertools.product(group.elements, repeat=2):
                assert residue_map[group.add(left, right)] == residue_map[left] * residue_map[right] % modulus
            for label, _, coordinate in factors:
                prime = int(label.removeprefix("prime_"))
                assert residue_map[coordinate] == prime % modulus
            result["unit_group_coordinates"] = {
                "modulus": modulus, "generators": generators,
                "map": [{"coordinate": coord, "unit": value} for coord, value in residue_map.items()],
            }
        records.append(result)
        if name == "U(3), p=13 a=4 R=3":
            target = (1,)
            bare_terms, covered_terms = [], []
            for e1, r1 in entries:
                for e2, r2 in entries:
                    bare, _, covered = averages(group.sub(r1, target), group.sub(r2, target))
                    if bare:
                        bare_terms.append([list(e1), list(e2)])
                    if covered:
                        covered_terms.append([list(e1), list(e2)])
            j2 = next(x for x in result["J2_first_packet"] if tuple(x["target"]) == target)
            assert len(bare_terms) == 13 and len(covered_terms) == 4
            assert j2["bare_J2_first_packet"] == 5 and j2["true_first_packet"] == 2
            fixture = {"p": 13, "a": 4, "R": 3, "unit_group_target": 2,
                       "additive_character_coordinate_target": [1],
                       "original_prime": 2, "original_exponents": list(range(5)),
                       "original_divisors": [2 ** e for e in range(5)],
                       "exterior_hit_exponents": [1, 3],
                       "exterior_hit_divisors": [2, 8],
                       "bare_pair": 13, "true_pair": 4, "covered_pair": 4,
                       "bare_pair_complete_exponent_fibre": bare_terms,
                       "covered_pair_complete_exponent_fibre": covered_terms,
                       "bare_J2_first_packet": 5, "true_first_packet": 2}
    source = Path(__file__).with_name("sieve_character_cover.tex")
    payload = {
        "status": "checks_passed",
        "scope": "Finite exact computations; not an independent manuscript proof review.",
        "arithmetic": "Integer exponent histograms reduced modulo exact monic cyclotomic polynomials, with rational average denominators.",
        "groups_checked": len(records),
        "map_fibres_checked": sum(r["map_fibres_checked"] for r in records),
        "character_basis_pairs_checked": sum(r["character_basis_pairs_checked"] for r in records),
        "target_pairs_checked": sum(r["target_pairs_checked"] for r in records),
        "full_polynomial_terms_checked": sum(r["full_polynomial_terms_checked"] for r in records),
        "original_histories_checked": sum(h["original_histories_checked"]
                                          for r in records for h in r["finite_history_checks"]),
        "manuscript_sha256_at_check": hashlib.sha256(source.read_bytes()).hexdigest() if source.exists() else None,
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "p13_a4_fixture": fixture,
        "cases": records,
    }
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: payload[k] for k in ("status", "groups_checked", "map_fibres_checked",
          "character_basis_pairs_checked", "target_pairs_checked", "full_polynomial_terms_checked",
          "original_histories_checked")}, indent=2))


if __name__ == "__main__":
    main()
