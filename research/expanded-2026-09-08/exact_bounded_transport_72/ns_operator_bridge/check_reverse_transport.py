"""Exact checks of Fourier restriction, obstruction and retained-spectrum return.

The original Fourier factor tau=2*pi*i is retained symbolically. All other
coefficients belong to Q(sqrt(2)); roots of unity use integer/rational
cyclotomic arithmetic. No floating comparisons or Lean processes are used.
"""

from dataclasses import dataclass
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations, product
from pathlib import Path
from collections import Counter
import argparse
import hashlib
import json
import re


@dataclass(frozen=True)
class Q2:
    a: Q = Q(0)
    b: Q = Q(0)

    def __add__(self, other):
        other = other if isinstance(other, Q2) else Q2(Q(other))
        return Q2(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Q2(-self.a, -self.b)

    def __sub__(self, other):
        return self + -other

    def __mul__(self, other):
        other = other if isinstance(other, Q2) else Q2(Q(other))
        return Q2(self.a * other.a + 2 * self.b * other.b,
                  self.a * other.b + self.b * other.a)

    __rmul__ = __mul__

    def inverse(self):
        norm = self.a * self.a - 2 * self.b * self.b
        assert norm != 0
        return Q2(self.a / norm, -self.b / norm)

    def __truediv__(self, other):
        other = other if isinstance(other, Q2) else Q2(Q(other))
        return self * other.inverse()

    def __pow__(self, power):
        assert power >= 0
        out = Q2(Q(1))
        for _ in range(power):
            out = out * self
        return out

    def record(self):
        return {"rational": str(self.a), "sqrt2_coefficient": str(self.b)}


ZERO = Q2()
ONE = Q2(Q(1))
VECTORS = {
    "v_r": ((ONE, Q2(Q(1), Q(-1))), Q2(Q(4), Q(-1))),
    "v_t": ((Q2(Q(-1), Q(1)), ONE), Q2(Q(4), Q(1))),
}


def trim(poly):
    poly = list(poly)
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def div_monic(poly, divisor):
    poly, divisor = trim(poly), trim(divisor)
    quotient = [0] * max(1, len(poly) - len(divisor) + 1)
    while len(poly) >= len(divisor) and any(poly):
        shift, leading = len(poly) - len(divisor), poly[-1]
        quotient[shift] += leading
        for j, value in enumerate(divisor):
            poly[shift + j] -= leading * value
        poly = trim(poly)
    return trim(quotient), poly


@lru_cache(None)
def cyclotomic(n):
    polynomial = [-1] + [0] * (n - 1) + [1]
    for d in range(1, n):
        if n % d == 0:
            polynomial, remainder = div_monic(polynomial, cyclotomic(d))
            assert remainder == [0]
    return tuple(polynomial)


def reduce_roots(coefficients):
    n = len(coefficients)
    _, rational = div_monic([x.a for x in coefficients], cyclotomic(n))
    _, quadratic = div_monic([x.b for x in coefficients], cyclotomic(n))
    size = max(len(rational), len(quadratic))
    rational += [Q(0)] * (size - len(rational))
    quadratic += [Q(0)] * (size - len(quadratic))
    return tuple(Q2(a, b) for a, b in zip(rational, quadratic))


def sample_histogram(poly, point, n):
    out = [ZERO] * n
    for frequency, coefficient in poly.items():
        phase = sum(a * b for a, b in zip(frequency, point)) % n
        out[phase] += coefficient
    return out


def dft_coefficient(poly, target, n):
    histogram = [ZERO] * n
    for point in product(range(n), repeat=2):
        phase_shift = -sum(a * b for a, b in zip(target, point))
        for phase, coefficient in enumerate(sample_histogram(poly, point, n)):
            histogram[(phase + phase_shift) % n] += coefficient
    reduced = reduce_roots([x / (n * n) for x in histogram])
    assert len(reduced) == 1
    return reduced[0]


def aggregate_residues(poly, n):
    result = {}
    for frequency, coefficient in poly.items():
        residue = tuple(x % n for x in frequency)
        result[residue] = result.get(residue, ZERO) + coefficient
    return {key: value for key, value in result.items() if value != ZERO}


def jmap(point):
    return (3 * point[0] + point[1], point[0] + 5 * point[1])


def jpower(point, m):
    for _ in range(m):
        point = jmap(point)
    return point


def dot(frequency, vector):
    return sum((n * v for n, v in zip(frequency, vector)), ZERO)


def full_preimage(points):
    result = set()
    for a, b in points:
        for k in range(14):
            first = (5 * a - b + k) / 14 % 1
            second = (a - 3 * (5 * a - b + k) / 14) % 1
            result.add((first, second))
    return result


def check_restriction(n):
    checks = 0
    examples = []
    for k in ((1, 0), (0, 1), (1, -2), (-2, 3)):
        nk = tuple(n * x for x in k)
        twice = tuple(2 * x for x in nk)
        kernel_poly = {nk: ONE, (0, 0): -ONE}
        inverse_kernel = {nk: ONE, twice: -ONE}
        assert aggregate_residues(kernel_poly, n) == {}
        assert aggregate_residues(inverse_kernel, n) == {}
        for point in product(range(n), repeat=2):
            assert reduce_roots(sample_histogram(kernel_poly, point, n)) == (ZERO,)
            assert reduce_roots(sample_histogram(inverse_kernel, point, n)) == (ZERO,)
            checks += 2
        for name, (vector, _) in VECTORS.items():
            multiplier = dot(nk, vector)
            assert multiplier != ZERO
            derivative = {nk: multiplier}
            inverse = {nk: multiplier.inverse(), twice: -dot(twice, vector).inverse()}
            inverse_constant = multiplier.inverse() / 2
            for point in product(range(n), repeat=2):
                assert reduce_roots(sample_histogram(derivative, point, n)) == (multiplier,)
                assert reduce_roots(sample_histogram(inverse, point, n)) == (inverse_constant,)
                checks += 2
            examples.append({"direction": name, "k": k,
                             "derivative_restriction": {"tau_power": 1, "coefficient": multiplier.record()},
                             "inverse_restriction": {"tau_power": -1, "coefficient": inverse_constant.record()}})

    # Complete DFT recovery of every residue sum for a finite polynomial with
    # several distinct integer lifts of the same residue, including negatives.
    poly = {(0, 0): Q2(Q(2), Q(1)), (n, 0): Q2(Q(-3), Q(2)),
            (2 * n, 0): Q2(Q(1), Q(-3)), (1, -1): Q2(Q(3), Q(2)),
            (1 + n, -1): Q2(Q(-3), Q(-2)),
            (-n - 1, 2): Q2(Q(5), Q(-1))}
    aggregate = aggregate_residues(poly, n)
    for residue in product(range(n), repeat=2):
        assert dft_coefficient(poly, residue, n) == aggregate.get(residue, ZERO)
        checks += 1
    return {"N": n, "exact_sample_and_DFT_checks": checks, "obstruction_examples": examples}


def check_spectrum(n):
    residues = list(product(range(n), repeat=2))[:min(5, n * n)]
    records = []
    for shifted in (False, True):
        omega = [(r + n * (r - s + int(shifted)), s + n * (r + s))
                 for r, s in residues]
        assert len({(a % n, b % n) for a, b in omega}) == len(omega)
        coefficients = {frequency: Q2(Q(j + 1), Q(j % 3 - 1))
                        for j, frequency in enumerate(omega)}
        for frequency, coefficient in coefficients.items():
            assert dft_coefficient(coefficients, frequency, n) == coefficient
        direction_checks = 0
        for _, (vector, _) in VECTORS.items():
            derivative = {f: c * dot(f, vector) for f, c in coefficients.items()}
            for f in omega:
                assert dft_coefficient(derivative, f, n) == coefficients[f] * dot(f, vector)
                direction_checks += 1
            zero_haar = {f: c for f, c in coefficients.items() if f != (0, 0)}
            inverse = {f: c / dot(f, vector) for f, c in zero_haar.items()}
            restored = {f: c * dot(f, vector) for f, c in inverse.items()}
            assert restored == zero_haar
            for f in omega:
                assert dft_coefficient(inverse, f, n) == inverse.get(f, ZERO)
                direction_checks += 1
        records.append({"original_spectrum": omega, "original_zero_excluded": shifted,
                        "coefficient_recoveries": len(omega), "direction_checks": direction_checks})
    return {"N": n, "spectra": records}


def check_cover(n, m):
    grid = {(Q(a, n), Q(b, n)) for a, b in product(range(n), repeat=2)}
    points = grid
    for _ in range(m):
        points = full_preimage(points)
    assert len(points) == 14 ** m * n * n
    target_counts = Counter(tuple(x % 1 for x in jpower(h, m)) for h in points)
    assert set(target_counts) == grid
    assert set(target_counts.values()) == {14 ** m}
    omega = [(0, 0), (1, 0), (0, 1)] if n > 1 else [(1, 0)]
    transported = [jpower(frequency, m) for frequency in omega]
    assert len(set(transported)) == len(omega)
    fixed_aliases = []
    gram_checks = 0
    for i, left in enumerate(transported):
        for j, right in enumerate(transported):
            difference = tuple(a - b for a, b in zip(left, right))
            histogram = [ZERO] * n
            for h in points:
                phase = sum((Q(a) * b for a, b in zip(difference, h)), Q(0)) % 1
                assert (phase * n).denominator == 1
                histogram[int(phase * n)] += ONE
                original_phase = sum((Q(a - b) * y for a, b, y in
                                     zip(omega[i], omega[j], jpower(h, m))), Q(0)) % 1
                assert phase == original_phase
            average = reduce_roots([x / len(points) for x in histogram])
            assert average == (ONE if i == j else ZERO,)
            gram_checks += 1
            if i != j and all(x % n == 0 for x in difference):
                fixed_aliases.append([omega[i], omega[j]])
    eigen_checks = 0
    for _, (vector, eigenvalue) in VECTORS.items():
        for original, moved in zip(omega, transported):
            assert dot(moved, vector) == eigenvalue ** m * dot(original, vector)
            if original != (0, 0):
                assert dot(moved, vector).inverse() == (
                    eigenvalue ** m).inverse() * dot(original, vector).inverse()
            eigen_checks += 1
    return {"N": n, "m": m, "original_spectrum": omega,
            "transported_spectrum": transported, "full_preimage_points": len(points),
            "target_fibre_size": 14 ** m, "full_preimage_Gram_checks": gram_checks,
            "fixed_grid_alias_pairs": fixed_aliases, "exact_directional_checks": eigen_checks}


def check_sharp_spectrum_criterion(n):
    frequencies = list(product(range(-2, 3), repeat=2))
    derivative_pairs, inverse_pairs, colliding_pairs = 0, 0, 0
    for left, right in combinations(frequencies, 2):
        collide = all((a - b) % n == 0 for a, b in zip(left, right))
        if collide:
            colliding_pairs += 1
        for _, (vector, _) in VECTORS.items():
            difference = dot(left, vector) - dot(right, vector)
            assert difference != ZERO
            derivative_pairs += 1
            if left != (0, 0) and right != (0, 0):
                inverse_difference = dot(left, vector).inverse() - dot(right, vector).inverse()
                assert inverse_difference != ZERO
                inverse_pairs += 1
            if collide:
                at_origin = sum((dot(left, vector), -dot(right, vector)), ZERO)
                assert at_origin == difference != ZERO
    return {"N": n, "integer_frequencies": len(frequencies),
            "derivative_pairs": derivative_pairs, "inverse_pairs": inverse_pairs,
            "colliding_frequency_pairs": colliding_pairs}


def check_affine_fibres(n):
    omega = list(product(range(-2, 3), repeat=2))
    classes = {}
    for frequency in omega:
        classes.setdefault(tuple(x % n for x in frequency), []).append(frequency)
    desired = {r: Q2(Q(i + 1), Q(1 - i % 3)) for i, r in enumerate(classes)}
    coefficients = {}
    for r, frequencies in classes.items():
        representative = frequencies[0]
        for j, frequency in enumerate(frequencies[1:]):
            coefficients[frequency] = Q2(Q(j + 2, 3), Q(j - 1, 2))
        coefficients[representative] = desired[r] - sum(
            (coefficients[f] for f in frequencies[1:]), ZERO)
    assert aggregate_residues(coefficients, n) == desired
    for r in product(range(n), repeat=2):
        assert dft_coefficient(coefficients, r, n) == desired.get(r, ZERO)
    # Re-read every free coordinate and return to the identical coefficient
    # family, including all original lifts in an occupied residue fibre.
    for r, frequencies in classes.items():
        assert coefficients[frequencies[0]] == desired[r] - sum(
            (coefficients[f] for f in frequencies[1:]), ZERO)
    return {"N": n, "original_spectrum_size": len(omega),
            "occupied_classes": len(classes), "free_coefficients": len(omega) - len(classes),
            "DFT_coefficients_checked": n * n}


def check_pell_and_typed_inverse():
    """Corroborate exact sharpness identities and common/absolute factors.

    These are finite exact identities. The limit, continuity and general
    smooth-function arguments remain the explicit proofs in the TeX source.
    The common chart's factor Q^(-1-h) is retained as a formal common scalar;
    its remaining covering factor is checked without choosing Q or h.
    """
    alpha, beta = Q2(Q(1), Q(1)), Q2(Q(1), Q(-1))
    c_squared, d_squared = Q2(Q(4), Q(2)), Q2(Q(4), Q(-2))
    conjugates = {"v_r": (ONE, Q2(Q(1), Q(1))),
                  "v_t": (Q2(Q(-1), Q(-1)), ONE)}
    pell_checks, typed_checks = 0, 0
    p, q = 1, 0
    for j in range(1, 41):
        p, q = p + 2 * q, p + q
        assert p * p - 2 * q * q == (-1) ** j
        assert Q2(Q(p), Q(q)) == alpha ** j
        assert Q2(Q(p), Q(-q)) == beta ** j
        frequencies = {"v_r": (p - q, q), "v_t": (q, q - p)}
        for name, (vector, _) in VECTORS.items():
            conjugate = conjugates[name]
            frequency = frequencies[name]
            length_squared = sum(k * k for k in frequency)
            symbol, dual_symbol = dot(frequency, vector), dot(frequency, conjugate)
            assert dot(vector, conjugate) == ZERO
            assert dot(vector, vector) == d_squared
            assert dot(conjugate, conjugate) == c_squared
            assert symbol * dual_symbol == Q2(Q((-1) ** j))
            assert Q2(Q(length_squared)) == (
                alpha ** (2 * j) / c_squared
                + alpha.inverse() ** (2 * j) / d_squared)
            assert symbol * symbol * length_squared == (
                ONE / c_squared + alpha.inverse() ** (4 * j) / d_squared)
            pell_checks += 1
    for m in range(9):
        for frequency in product(range(-3, 4), repeat=2):
            if frequency == (0, 0):
                continue
            for _, (vector, eigenvalue) in VECTORS.items():
                original = dot(frequency, vector)
                absolute = dot(jpower(frequency, m), vector)
                assert absolute == eigenvalue ** m * original
                assert absolute.inverse() == eigenvalue.inverse() ** m * original.inverse()
                # Pullback of -c_m^-1 T^y equals
                # -Q^(-1-h) T^Y P_m for v_t, and the corresponding
                # exact eigenvalue identity is also retained for v_r.
                assert -(eigenvalue.inverse() ** m * original.inverse()) == -absolute.inverse()
                typed_checks += 1
    return {"pell_original_vector_identities": pell_checks,
            "typed_common_absolute_inverse_identities": typed_checks,
            "Fourier_constant": "tau=2*pi*i; inverse identities have tau exponent -1 on both sides",
            "scope": "Finite exact checks, not numerical evidence for the analytic limit or a PDE theorem"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name("CHECK_REVERSE_TRANSPORT.json"))
    args = parser.parse_args()
    restriction = [check_restriction(n) for n in range(1, 9)]
    spectra = [check_spectrum(n) for n in range(1, 9)]
    covers = [check_cover(n, m) for n in (1, 2, 3, 7) for m in range(3)]
    sharp_criteria = [check_sharp_spectrum_criterion(n) for n in range(1, 9)]
    affine_fibres = [check_affine_fibres(n) for n in range(1, 9)]
    sharp_inverse = check_pell_and_typed_inverse()
    source = Path(__file__).with_name("reverse_proof_transport.tex")
    proof_sources = [source, Path(__file__).with_name("reverse_smooth_inverse.tex")]
    proof_hashes = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in proof_sources}
    proof_statements = {
        p.name: re.findall(r"\\begin\{(theorem|lemma|proposition|corollary)\}",
                           p.read_text(encoding="utf-8")) for p in proof_sources}
    assert all(len(rows) == 5 for rows in proof_statements.values())
    payload = {
        "status": "checks_passed", "scope": "Exact finite computations; independent source review is recorded separately.",
        "arithmetic": "Q(sqrt2), rational torus coordinates and exact cyclotomic polynomial reduction; tau=2*pi*i retained symbolically with its exponent.",
        "derivative_rule": "(tau^j c_n)e_n -> tau^(j+1)(v dot n)c_n e_n",
        "inverse_rule": "(tau^j c_n)e_n -> tau^(j-1)c_n/(v dot n)e_n, original n != 0",
        "sample_and_DFT_checks": sum(r["exact_sample_and_DFT_checks"] for r in restriction),
        "obstruction_examples": sum(len(r["obstruction_examples"]) for r in restriction),
        "retained_spectra": sum(len(r["spectra"]) for r in spectra),
        "full_preimage_points": sum(c["full_preimage_points"] for c in covers),
        "full_preimage_Gram_checks": sum(c["full_preimage_Gram_checks"] for c in covers),
        "exact_directional_checks": sum(c["exact_directional_checks"] for c in covers),
        "sharp_derivative_frequency_pairs": sum(c["derivative_pairs"] for c in sharp_criteria),
        "sharp_inverse_frequency_pairs": sum(c["inverse_pairs"] for c in sharp_criteria),
        "affine_fibre_DFT_checks": sum(c["DFT_coefficients_checked"] for c in affine_fibres),
        "restriction": restriction, "spectra": spectra, "covers": covers,
        "sharp_spectrum_criteria": sharp_criteria,
        "affine_fibre_checks": affine_fibres,
        "sharp_inverse_checks": sharp_inverse,
        "source_sha256_at_check": proof_hashes[source.name],
        "proof_sources_sha256_at_check": proof_hashes,
        "proof_statement_counts": {name: len(rows) for name, rows in proof_statements.items()},
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: payload[key] for key in ("status", "sample_and_DFT_checks",
                     "obstruction_examples", "retained_spectra", "full_preimage_points",
                     "full_preimage_Gram_checks", "exact_directional_checks")}, indent=2))


if __name__ == "__main__":
    main()
