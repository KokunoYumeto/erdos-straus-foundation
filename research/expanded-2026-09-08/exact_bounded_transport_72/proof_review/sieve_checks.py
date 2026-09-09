"""Independent exact checks of the first two original-shell factor criteria.

This supplements the complete algebraic review; finite prime tests do not
establish an unbounded positivity or prime-infinitude conclusion.
"""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import product
from math import gcd, prod
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
BASE = HERE.parent


def factor(n):
    out = []
    ell = 2
    while ell * ell <= n:
        b = 0
        while n % ell == 0:
            n //= ell
            b += 1
        if b:
            out.append((ell, b))
        ell += 1
    if n > 1:
        out.append((n, 1))
    return out


def divisors_from_original_factors(factors):
    out = [1]
    for ell, b in factors:
        out = [u * ell**e for u in out for e in range(2*b+1)]
    return sorted(out)


def seventh_criterion(factors):
    n3 = sum(b for ell, b in factors if ell % 7 == 3)
    m24 = sum(b for ell, b in factors if ell % 7 in (2, 4))
    flag56 = any(ell % 7 in (5, 6) for ell, b in factors)
    return flag56 or n3 >= 3 or (n3 >= 1 and m24 >= 1), n3, m24, flag56


def seventh_coefficients(factors):
    logs = {1: 0, 2: 2, 3: 1, 4: 4, 5: 5, 6: 3}
    coefficients = [1, 0, 0, 0, 0, 0]
    t = 0
    for ell, b in factors:
        weight = logs[ell % 7]
        new = [0]*6
        for residue, multiplicity in enumerate(coefficients):
            for e in range(2*b+1):
                new[(residue+weight*e) % 6] += multiplicity
        coefficients = new
        t = (t+weight*b) % 6
    assert sum(coefficients) == prod(2*b+1 for ell, b in factors)
    return coefficients, t


def witnesses(a, R, factors):
    if R == 3:
        return [row for ell, b in factors if ell % 3 == 2 for row in
                [('residue2', 0, ell, {ell: 1}),
                 ('residue2_A1_middle', 1, a*ell, {ell: 1})]]
    result = []
    for ell, b in factors:
        if ell % 7 == 5:
            result.append(('residue5', 0, ell, {ell: 1}))
        if ell % 7 == 6:
            result.append(('residue6', 1, a*ell, {ell: 1}))
    threes = [ell for ell, b in factors if ell % 7 == 3 for _ in range(b)]
    if len(threes) >= 3:
        chosen = Counter(threes[:3])
        d = prod(threes[:3])
        assert a % d == 0
        result.append(('three_residue3_occurrences', 1, a*d, dict(chosen)))
    for ell, b in factors:
        if ell % 7 != 3:
            continue
        for t, bt in factors:
            if t % 7 == 2:
                result.append(('residue3_times2', 1, a*ell*t, {ell: 1, t: 1}))
            if t % 7 == 4:
                assert a % t == 0
                result.append(('residue3_over4', 1, a*ell//t, {ell: 1, t: -1}))
    return result


def code_and_original_inverse(p, j, eps, u, factors):
    h = (p-1)//12
    a, R, S = 3*h+j+1, 4*j+3, p*(3*h+j+1)
    assert a*a % u == 0
    assert (4*u+p**eps) % R == 0
    g = gcd(a, u)
    A, B = a//g, u//g
    assert g*g % u == 0
    D = g*g//u
    assert (A*B*D, B*B*D) == (a, u)
    assert gcd(A, B) == 1
    assert (A+p**(1-eps)*B) % R == 0
    C = (A+p**(1-eps)*B)//R
    y, z = p**eps*A*C*D, p*B*C*D
    assert min(a, y, z, C, D) > 0
    assert Fraction(1, a)+Fraction(1, y)+Fraction(1, z) == Fraction(4, p)
    dy, dz = R*y-S, R*z-S
    assert dy == p**eps*A*A*D
    assert dz == p**(2-eps)*u
    assert dy*dz == S*S
    assert ((S+dz)//R, (S+dy)//R) == (z, y)
    m_over_n = Fraction(R*y-S, S)
    back_eps = 0 if m_over_n.denominator % p == 0 else 1
    assert back_eps == eps
    assert (m_over_n.numerator, m_over_n.denominator//p**(1-eps)) == (A, B)
    assert B*B*(a//(A*B)) == u
    original_exponents = []
    rem = u
    for ell, b in factors:
        e = 0
        while rem % ell == 0:
            rem //= ell
            e += 1
        assert 0 <= e <= 2*b
        original_exponents.append([ell, b, e])
    assert rem == 1
    codes = {}
    for label, J, M in [('full', 6*h, 9*h), ('first_half', 3*h, 6*h)]:
        assert 0 <= j < J and 1 <= A <= M and 1 <= B <= M
        Lambda, N = 2*J*M, 2*J*M*M
        c = (A-1)*Lambda+2*M*j+2*(B-1)+eps
        assert 0 <= c < N
        recovered_A, v = 1+c//Lambda, c % Lambda
        recovered_j = v//(2*M)
        recovered_B = 1+v//2-M*recovered_j
        recovered_eps = v % 2
        assert (recovered_j, recovered_A, recovered_B, recovered_eps) == (j, A, B, eps)
        delta1 = gcd(4*A*B, p+4*j+3)//(4*A*B)
        gamma = 1//gcd(A, B)
        delta2 = gcd(R, A+p**(1-eps)*B)//R
        assert delta1*gamma*delta2 == 1
        codes[label] = {'c': c, 'Lambda': Lambda, 'N': N}
    return {'p': p, 'j': j, 'R': R, 'a': a, 'u': u, 'eps': eps,
            'A': A, 'B': B, 'C': C, 'D': D, 'triple': [a, y, z],
            'dy': dy, 'dz': dz, 'original_prime_exponents': original_exponents,
            'codes': codes}


def main():
    counts = Counter()
    examples = {}
    survivors = []
    shell_rows = []
    R7_A1_failures = []
    for p in range(13, 10001, 12):
        if factor(p) != [(p, 1)]:
            continue
        counts['eligible_primes_through_10000'] += 1
        h = (p-1)//12
        shell_failures = []
        for j, R in [(0, 3), (1, 7)]:
            a = 3*h+j+1
            assert a <= 6*h < p and R == 4*a-p and gcd(a, R) == 1
            factors = factor(a)
            divisors = divisors_from_original_factors(factors)
            E = [u for u in divisors if (4*u+1) % R == 0]
            M = [u for u in divisors if (u+a) % R == 0]
            if R == 3:
                predicted = any(ell % 3 == 2 for ell, b in factors)
                assert a % 3 == 1 and E == M
                assert bool(E) == predicted == bool(M)
                P1 = prod(2*b+1 for ell, b in factors if ell % 3 == 1)
                P2 = prod(2*b+1 for ell, b in factors if ell % 3 == 2)
                assert len(E) == P1*(P2-1)//2
                assert len(E) % 2 == 0
                assert (2*len(E)+len(M))//2 == 3*len(E)//2
                aggregates = None
            else:
                predicted, n3, m24, flag56 = seventh_criterion(factors)
                aggregates = {'n3': n3, 'm24': m24, 'factor56': flag56}
                coefficients, t = seventh_coefficients(factors)
                assert (coefficients[5], coefficients[(t+3) % 6]) == (len(E), len(M))
            assert bool(E or M) == predicted
            B_candidates = [B for B in divisors if a % B == 0]
            A1_M = [B for B in B_candidates if (1+B) % R == 0]
            A1_E = [B for B in B_candidates if (1+p*B) % R == 0]
            if R == 3:
                assert bool(A1_M) == predicted
            if R == 7 and predicted and not (A1_M or A1_E):
                R7_A1_failures.append({'p': p, 'a': a, 'factors': factors,
                                       'B_candidates': B_candidates, 'E': E, 'M': M})
            shell_failures.append(not predicted)
            counts[f'R{R}_occupied'] += predicted
            counts['all_original_divisors_tested'] += len(divisors)
            counts['all_passing_tagged_divisors'] += len(E)+len(M)
            for eps, hits in [(0, E), (1, M)]:
                for u in hits:
                    code_and_original_inverse(p, j, eps, u, factors)
            chosen = witnesses(a, R, factors)
            assert bool(chosen) == predicted
            for kind, eps, u, relative in chosen:
                assert u in (E if eps == 0 else M)
                actual_factors = dict(factors)
                if kind in ('residue2', 'residue5'):
                    exponents = {ell: relative.get(ell, 0) for ell in actual_factors}
                else:
                    exponents = {ell: b+relative.get(ell, 0) for ell, b in factors}
                assert prod(ell**e for ell, e in exponents.items()) == u
                assert all(0 <= e <= 2*actual_factors[ell] for ell, e in exponents.items())
                record = code_and_original_inverse(p, j, eps, u, factors)
                if kind in ('residue2_A1_middle', 'residue6', 'three_residue3_occurrences', 'residue3_times2'):
                    assert record['A'] == 1
                counts[f'witness_{kind}'] += 1
                if kind not in examples:
                    examples[kind] = record
            shell_rows.append({'p': p, 'j': j, 'a': a, 'R': R,
                               'factorization': factors, 'aggregates': aggregates,
                               'E_count': len(E), 'M_count': len(M),
                               'predicted_occupied': predicted})
        if all(shell_failures):
            survivors.append(p)
    # This branch does not occur in the stated prime interval. These two
    # explicitly labelled extra primes check three distinct occurrences
    # and a repeated original prime factor, respectively.
    additional_large_prime_branches = []
    for p in [153877, 226789]:
        assert p % 12 == 1 and factor(p) == [(p, 1)]
        a = (p+7)//4
        fs = factor(a)
        assert seventh_criterion(fs)[1] == 3
        branch = next(row for row in witnesses(a, 7, fs) if row[0] == 'three_residue3_occurrences')
        kind, eps, u, relative = branch
        record = code_and_original_inverse(p, 1, eps, u, fs)
        assert record['A'] == 1
        additional_large_prime_branches.append(record)
        examples.setdefault(kind, record)
    assert set(examples) == {'residue2', 'residue2_A1_middle', 'residue5', 'residue6',
                            'three_residue3_occurrences', 'residue3_times2', 'residue3_over4'}
    # Independent full bounded residue-support calculation, retaining two
    # distinct primes in residue class 3 to test aggregate multiplicities.
    labels = [2, 3, 5, 11, 13, 17, 29]
    for budgets in product(range(3), repeat=len(labels)):
        labelled = [(ell, b) for ell, b in zip(labels, budgets) if b]
        residues = {1}
        a_mod7 = 1
        for ell, b in labelled:
            residues = {r*pow(ell, e, 7) % 7 for r in residues for e in range(2*b+1)}
            a_mod7 = a_mod7*pow(ell, b, 7) % 7
        assert (5 in residues or (-a_mod7) % 7 in residues) == seventh_criterion(labelled)[0]
        coefficients, t = seventh_coefficients(labelled)
        assert bool(coefficients[5]+coefficients[(t+3) % 6]) == seventh_criterion(labelled)[0]
        counts['labelled_mod7_budget_patterns'] += 1
    counts['both_shells_empty'] = len(survivors)
    counts['R7_occupied_without_A1'] = len(R7_A1_failures)
    assert R7_A1_failures[0] == {'p': 373, 'a': 95, 'factors': [(5, 1), (19, 1)],
                                'B_candidates': [1, 5, 19, 95], 'E': [5, 19], 'M': []}
    sources = ['bounded_transport.tex', 'unary_boolean_transport.tex', 'first_two_shell_sieve.tex']
    out = {'status': 'pass', 'scope': 'The complete independently reviewed first_two_shell_sieve.tex criteria, fibres, counts and original-coordinate reconstruction maps.',
           'counts': dict(counts), 'all_original_passing_divisors_code_and_triple_inverse_checked': True,
           'both_full_and_first_half_range_labels_preserved': True,
           'first_examples_of_every_constructive_branch': examples,
           'additional_large_prime_branches': additional_large_prime_branches,
           'R3_complete_fibre_count_and_A1_middle_equivalence_checked': True,
           'R7_original_labelled_group_ring_coefficients_match_complete_counts': True,
           'R7_same_shell_A1_counterexamples': R7_A1_failures,
           'both_shells_empty_primes_through_10000': survivors,
           'per_prime_original_shells': shell_rows,
           'definition_source_hashes': {s: sha256((BASE/s).read_bytes()).hexdigest() for s in sources},
           'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
           'limitations': 'These checks supplement the complete unbounded algebraic review of the recorded source. They assert neither that sieve survivors are globally empty nor that infinitely many primes survive.'}
    (HERE/'sieve_checks.json').write_text(json.dumps(out, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: out[k] for k in ['status', 'counts', 'both_shells_empty_primes_through_10000']}, indent=2))


if __name__ == '__main__':
    main()
