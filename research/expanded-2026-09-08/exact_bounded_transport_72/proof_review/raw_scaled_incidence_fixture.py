"""Independent complete bounded test of the raw-scale incidence fibres.

Every input X = 6, 12, ..., 600 is retained.  Every N(X) is completely
factored, and the product of the prime powers is checked against N(X).
No prime-size cutoff is used.  The root computation is certified by the
identity product(T-rho) = T**4-T**2+1 over each prime field; four distinct
roots therefore comprise all roots, independently of how sqrt_mod found
them.  The CRT intervals are enumerated completely, including empty ones.

Finite exact checks supplement the universal proofs; this fixture makes
no assertion about inputs outside its specified finite interval.
"""

from collections import Counter
from fractions import Fraction
from hashlib import sha256
from math import gcd, isqrt, lcm, prod
from pathlib import Path
import json
import platform

import sympy
from sympy import factorint, isprime, sqrt_mod


BASE = Path(__file__).resolve().parent.parent
SOURCE = BASE / "raw_scale_hit_incidence.tex"


def polynomial(x):
    return x**4 - x*x + 1


def square_divisor_scales(n):
    return {k for k in range(1, isqrt(n) + 1) if n % (k*k) == 0}


def ceil_div(n, d):
    assert d > 0
    return -((-n) // d)


def complete_roots(q):
    """Return all roots, with a checked monic quartic factorization."""
    assert isprime(q) and q > 3 and q % 12 == 1
    # t = X^2 gives (2t-1)^2 = -3; both transformations are reversible.
    discriminant_roots = sorted(int(s) for s in sqrt_mod(-3, q, all_roots=True))
    assert len(discriminant_roots) == 2
    assert all((s*s + 3) % q == 0 for s in discriminant_roots)
    t_roots = sorted({(1+s) * pow(2, -1, q) % q for s in discriminant_roots})
    assert len(t_roots) == 2
    rho_by_t = {
        t: sorted(int(rho) for rho in sqrt_mod(t, q, all_roots=True))
        for t in t_roots
    }
    assert all(len(roots) == 2 for roots in rho_by_t.values())
    roots = sorted({rho for values in rho_by_t.values() for rho in values})
    assert len(roots) == 4 and all(polynomial(rho) % q == 0 for rho in roots)
    coefficients = [1]  # ascending powers of T
    for rho in roots:
        updated = [0] * (len(coefficients) + 1)
        for i, coefficient in enumerate(coefficients):
            updated[i] = (updated[i] - rho*coefficient) % q
            updated[i+1] = (updated[i+1] + coefficient) % q
        coefficients = updated
    assert coefficients == [1, 0, q-1, 0, 1]
    return roots, {
        "discriminant_roots": discriminant_roots,
        "t_roots": t_roots,
        "rho_by_t": {str(t): values for t, values in rho_by_t.items()},
        "roots": roots,
        "product_coefficients_mod_q_ascending": coefficients,
        "complete_root_factorization_verified": True,
    }


def run_incidence_checks():
    source_bytes_before = SOURCE.read_bytes()
    source_hash_before = sha256(source_bytes_before).hexdigest()
    p, A0, B0, C0, D0p, epsilon = 61, 1, 2, 1, 8, 1
    U, V, input_residue, input_modulus, output_modulus = 1, 600, 0, 6, 1
    K0, Omega0, Theta0 = 4*A0*B0*C0, A0+epsilon*B0, C0+(1-epsilon)*B0
    scales = square_divisor_scales(D0p)
    periods = {k: k*k*K0 // gcd(k*k*K0, Theta0) for k in scales}
    assert scales == {1, 2} and periods == {1: 8, 2: 32}
    assert K0*D0p == Omega0+p*Theta0
    assert 2*C0-Theta0 == 1 and Omega0+2*C0 == 5
    inputs = [X for X in range(U, V+1) if (X-input_residue) % input_modulus == 0]
    assert inputs == list(range(6, 601, 6)) and len(inputs) == 100

    factorizations = []
    factors_by_input = {}
    primitive_pairs = set()
    direct_triples = set()
    integrality_triples = set()
    all_factor_labels = set()
    for X in inputs:
        n = polynomial(X)
        factors = {int(q): int(e) for q, e in factorint(n).items()}
        assert all(e >= 1 and isprime(q) for q, e in factors.items())
        assert prod(q**e for q, e in factors.items()) == n
        factors_by_input[X] = set(factors)
        all_factor_labels.update(factors)
        factorizations.append({
            "X": X, "N_X": n,
            "prime_powers": [[q, factors[q]] for q in sorted(factors)],
            "complete_product_verified": True,
        })
        for q in sorted(factors):
            common_output_pass = (
                p < q <= polynomial(V) and q % 12 == 1
                and (q-1) % output_modulus == 0
                and q*(2*C0-Theta0) >= Omega0+2*C0
            )
            if not common_output_pass:
                continue
            D0q = Fraction(Omega0+q*Theta0, K0)
            primitive_congruence = (q-p) % periods[1] == 0
            assert primitive_congruence == (D0q.denominator == 1)
            if primitive_congruence:
                primitive_pairs.add((X, q))
            for k in scales:
                if (q-p) % periods[k] == 0:
                    direct_triples.add((k, X, q))
                Dkq = Fraction(Omega0+q*Theta0, k*k*K0)
                if Dkq.denominator == 1:
                    assert Dkq > 0
                    integrality_triples.add((k, X, q))
    assert direct_triples == integrality_triples

    projected_pairs = {(X, q) for k, X, q in direct_triples}
    assert projected_pairs == primitive_pairs
    section = {(1, X, q) for X, q in primitive_pairs}
    assert section <= direct_triples
    assert {(X, q) for _, X, q in section} == primitive_pairs
    weighted_count = 0
    scale_fibre_records = []
    for X, q in sorted(primitive_pairs):
        D0q = Fraction(Omega0+q*Theta0, K0)
        assert D0q.denominator == 1
        D0q = D0q.numerator
        retained_gcd = gcd(D0p, D0q)
        fibre = {k for kk, XX, qq in direct_triples if XX == X and qq == q for k in [kk]}
        predicted_fibre = square_divisor_scales(retained_gcd)
        assert fibre == predicted_fibre == {k for k in scales if D0q % (k*k) == 0}
        gcd_factors = {int(q0): int(e) for q0, e in factorint(retained_gcd).items()}
        fibre_weight = prod(e//2+1 for e in gcd_factors.values())
        assert fibre_weight == len(fibre)
        weighted_count += fibre_weight
        scale_fibre_records.append({
            "X": X, "q": q, "D0_q": D0q, "gcd_D0p_D0q": retained_gcd,
            "scale_fibre": sorted(fibre), "square_divisor_weight": fibre_weight,
            "raw_D_by_scale": {str(k): D0q//(k*k) for k in sorted(fibre)},
        })
    assert weighted_count == len(direct_triples)

    # Factoring every input makes this exactly the nonempty output projection.
    retained_primes = sorted({q for X, q in primitive_pairs})
    root_pair_set = set()
    root_triple_set = set()
    root_records = []
    total_branch_weight = 0
    for q in retained_primes:
        roots, root_certificate = complete_roots(q)
        compatible_scale_set = {k for k in scales if (q-p) % periods[k] == 0}
        branches = []
        q_input_fibre = set()
        for rho in roots:
            g = gcd(input_modulus, q)
            compatible = (rho-input_residue) % g == 0
            assert compatible  # here q > 61 and input_modulus = 6
            reduced_q = q//g
            correction = (
                (rho-input_residue)//g * pow(input_modulus//g, -1, reduced_q)
            ) % reduced_q if reduced_q > 1 else 0
            x0 = input_residue + input_modulus*correction
            Lq = lcm(input_modulus, q)
            t_min = ceil_div(U-x0, Lq)
            t_max = (V-x0)//Lq
            branch_inputs = [x0+Lq*t for t in range(t_min, t_max+1)]
            direct_branch_inputs = [X for X in inputs if X % q == rho]
            assert branch_inputs == direct_branch_inputs
            assert len(branch_inputs) == max(0, t_max-t_min+1)
            for X in branch_inputs:
                assert U <= X <= V and (X-input_residue) % input_modulus == 0
                assert X % q == rho and polynomial(X) % q == 0
                t_inverse = (X-x0)//Lq
                assert X == x0+Lq*t_inverse and t_min <= t_inverse <= t_max
                assert X not in q_input_fibre
                q_input_fibre.add(X)
                assert (X, q) not in root_pair_set
                root_pair_set.add((X, q))
                for k in compatible_scale_set:
                    assert (k, X, q) not in root_triple_set
                    root_triple_set.add((k, X, q))
            total_branch_weight += len(branch_inputs)*len(compatible_scale_set)
            branches.append({
                "rho": rho, "gcd_M_q": g, "compatible": compatible,
                "x0": x0, "L_q": Lq, "t_min": t_min, "t_max": t_max,
                "branch_size": len(branch_inputs), "inputs": branch_inputs,
            })
        direct_q_fibre = {X for X, qq in primitive_pairs if qq == q}
        assert q_input_fibre == direct_q_fibre
        root_records.append({
            "q": q, "compatible_scales": sorted(compatible_scale_set),
            "root_certificate": root_certificate, "branches": branches,
            "entire_input_fibre": sorted(q_input_fibre),
        })
    assert root_pair_set == primitive_pairs
    assert root_triple_set == direct_triples
    assert total_branch_weight == weighted_count == len(direct_triples)
    # Recheck each fixed (k,X) fibre against its complete factor set.
    for k in scales:
        for X in inputs:
            wanted = {
                q for q in factors_by_input[X]
                if p < q <= polynomial(V) and q % 12 == 1
                and (q-1) % output_modulus == 0 and (q-p) % periods[k] == 0
                and q*(2*C0-Theta0) >= Omega0+2*C0
            }
            actual = {q for kk, XX, q in direct_triples if kk == k and XX == X}
            assert actual == wanted

    source_bytes_after = SOURCE.read_bytes()
    source_hash_after = sha256(source_bytes_after).hexdigest()
    assert source_hash_before == source_hash_after, "Proof source changed while fixture ran; rerun."
    per_scale = Counter(k for k, X, q in direct_triples)
    fibre_cardinalities = Counter(len(record["scale_fibre"]) for record in scale_fibre_records)
    return {
        "status": "pass",
        "source": SOURCE.relative_to(BASE).as_posix(),
        "source_sha256": source_hash_after,
        "source_unchanged_during_run": True,
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "runtime": {"python": platform.python_version(), "sympy": sympy.__version__},
        "fixed_original_data": {
            "p": p, "A0": A0, "B0": B0, "C0": C0, "D0_p": D0p,
            "epsilon": epsilon, "scales": sorted(scales),
            "K0": K0, "Omega0": Omega0, "Theta0": Theta0,
            "period_by_scale": {str(k): periods[k] for k in sorted(scales)},
            "input_residue": input_residue, "input_modulus": input_modulus,
            "U": U, "V": V, "output_modulus": output_modulus,
            "first_half_gate": "q >= 5",
        },
        "counts": {
            "inputs": len(inputs), "complete_factorizations": len(factorizations),
            "all_distinct_factor_primes": len(all_factor_labels),
            "largest_factor_prime": max(all_factor_labels),
            "primitive_pairs": len(primitive_pairs), "retained_output_primes": len(retained_primes),
            "scaled_triples": len(direct_triples), "weighted_scale_count": weighted_count,
            "weighted_root_branch_count": total_branch_weight,
            "triples_by_scale": {str(k): per_scale[k] for k in sorted(scales)},
            "primitive_pairs_by_scale_fibre_size": {str(k): v for k, v in sorted(fibre_cardinalities.items())},
            "certified_roots": sum(len(record["root_certificate"]["roots"]) for record in root_records),
            "root_branches_including_empty": sum(len(record["branches"]) for record in root_records),
            "empty_root_branches": sum(not branch["inputs"] for record in root_records for branch in record["branches"]),
        },
        "checks": {
            "complete_prime_power_factorizations": True,
            "no_prime_cutoff": True,
            "scaled_congruence_equals_original_rational_integrality": True,
            "projection_onto_primitive_incidence": True,
            "specified_k1_section": True,
            "every_scale_fibre_equals_square_divisors_of_retained_gcd": True,
            "prime_factor_weight_formula": True,
            "all_modular_roots_certified_by_exact_quartic_factorization": True,
            "all_bounded_CRT_branches_and_inverse_parameters": True,
            "root_branches_disjoint": True,
            "complete_CRT_pairs_equal_direct_pairs": True,
            "complete_CRT_triples_equal_direct_triples": True,
            "all_three_scaled_counts_agree": True,
            "every_fixed_scale_input_output_fibre": True,
        },
        "factorizations": factorizations,
        "primitive_pairs": [list(pair) for pair in sorted(primitive_pairs)],
        "scaled_triples": [list(triple) for triple in sorted(direct_triples)],
        "scale_fibres": scale_fibre_records,
        "root_CRT_fibres": root_records,
        "scope": "All X divisible by 6 in [1,600], all prime factors of each X^4-X^2+1, both retained scales 1 and 2, and every corresponding bounded root branch. No assertion about other inputs or universal prime coverage.",
    }


if __name__ == "__main__":
    report = run_incidence_checks()
    destination = Path(__file__).with_suffix(".json")
    destination.write_text(json.dumps(report, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"status": report["status"], "source_sha256": report["source_sha256"], "counts": report["counts"]}, indent=2))
