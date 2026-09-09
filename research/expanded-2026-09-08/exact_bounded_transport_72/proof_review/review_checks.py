"""Small adversarial numerical audit; independent of manuscript checkers.

All output is confined to this directory.  These checks supplement the
deductive review, and do not establish unbounded arithmetic assertions.
"""
from fractions import Fraction
from itertools import product
from math import gcd, isqrt, lcm
from collections import Counter
from pathlib import Path
import json


def factors(n):
    out = []
    q = 2
    while q * q <= n:
        e = 0
        while n % q == 0:
            n //= q
            e += 1
        if e:
            out.append((q, e))
        q += 1
    if n > 1:
        out.append((n, 1))
    return out


def divisor_lifts(ns, fs, eqs):
    n = gcd(*ns) if len(ns) > 1 else ns[0]
    f = lcm(*fs) if fs else 1
    if n % f:
        return []
    r, modulus = 0, 1
    for c, b, m in eqs:
        g = gcd(c, m)
        if b % g:
            return []
        reduced = m // g
        target = (pow(c // g, -1, reduced) * (b // g)) % reduced if reduced > 1 else 0
        common = gcd(modulus, reduced)
        if (target - r) % common:
            return []
        coprime = reduced // common
        k = ((target - r) // common * pow(modulus // common, -1, coprime)) % coprime if coprime > 1 else 0
        r += modulus * k
        modulus = lcm(modulus, reduced)
        r %= modulus
    contributions = {1 % modulus: [1]}
    for q, e in factors(n):
        d, residual = 0, f
        while residual % q == 0:
            d += 1
            residual //= q
        next_contributions = {}
        for old_values in contributions.values():
            for value in old_values:
                for j in range(d, e + 1):
                    new_value = value * q ** j
                    next_contributions.setdefault(new_value % modulus, []).append(new_value)
        contributions = next_contributions
    return sorted(contributions.get(r, []))


def direct(ns, fs, eqs):
    return [u for u in range(1, min(ns) + 1)
            if all(n % u == 0 for n in ns)
            and all(u % f == 0 for f in fs)
            and all((c * u - b) % m == 0 for c, b, m in eqs)]


def main():
    count = 0
    for n, c, b, modulus in product(range(1, 21), range(-3, 4), range(-3, 4), range(1, 9)):
        case = ([n], [], [(c, b, modulus)])
        assert divisor_lifts(*case) == direct(*case), case
        count += 1
    simultaneous = 0
    eq_lists = [[], [(0, 0, 1)], [(0, 1, 2)], [(2, 2, 4), (3, 3, 6)],
                [(-2, 2, 6), (3, -3, 9)], [(0, 0, 12), (1, 0, 4)],
                [(4, -1, 5), (4, -1, 7)], [(1, 2, 4), (1, 3, 6)]]
    for ns, fs, eqs in product(([1], [12], [24, 36], [36, 60]),
                               ([], [1], [2, 3], [4, 9], [5]), eq_lists):
        case = (ns, fs, eqs)
        assert divisor_lifts(*case) == direct(*case), case
        simultaneous += 1

    ds = direct([324], [], [])
    tables = {str(modulus): {channel: [u for u in ds if (4*u+1 if channel == 'E' else u+18) % modulus == 0]
                             for channel in ['E', 'M']} for modulus in [5, 7, 35]}
    assert tables['5'] == {'E': [1, 6, 36, 81], 'M': [2, 12, 27, 162]}
    assert tables['7'] == {'E': [12, 54], 'M': [3, 108]}
    assert tables['35'] == {'E': [], 'M': []}
    assert all(pow(2, j, 15) != 11 for j in range(4))
    assert 2 % 3 == 11 % 3 and 1 % 5 == 11 % 5

    rows = [(1752, 407, 279), (1753, 759, 520), (1754, 1237, 847), (1755, 434, 297)]
    assert all(1201*k+1 == t*q and 362 < k < t for t, k, q in rows)
    assert Fraction(1201*35, 24).__ceil__() == 1752
    assert Fraction(1201*19, 13).__floor__() == 1755
    assert 1201*35//116 == 362
    for p, denominators in [(1201, (306, 15980, 172727820)),
                            (73, (20, 4380, 219)), (73, (21, 3066, 146)),
                            (13, (4, 130, 20)), (13, (5, 130, 10)),
                            (37, (12, 42, 1036)), (37, (10, 2405, 130)),
                            (1753, (440, 2313960, 115698)), (1753, (441, 1546146, 73626))]:
        assert sum((Fraction(1, n) for n in denominators), Fraction()) == Fraction(4, p)
    ds144 = direct([144], [], [])
    assert [u for u in ds144 if (4*u+1) % 11 == 0] == [8]
    assert [u for u in ds144 if (u+12) % 11 == 0] == []
    assert (12//gcd(12,8), 8//gcd(12,8), gcd(12,8)**2//8) == (3,2,2)
    assert 1753*440//20 == 38566 and 440//20 == 22 and 441//21 == 21
    assert Fraction(156*1036, 156+1036) == Fraction(20202, 149)
    assert gcd(3278, 10582) == 22
    assert (3278//22, 10582//22) == (149, 481)

    affine_count = 0
    for n, m, c in product(range(1, 17), range(1, 17), range(-4, 5)):
        target_reciprocals = {Fraction(1,v) for v in range(1,m+1) if m % v == 0}
        for u in range(1,n+1):
            if n % u:
                continue
            e = n // u
            x = Fraction(n,m*u)-Fraction(c,m)
            assert Fraction(m,n)*x+Fraction(c,n) == Fraction(1,u)
            assert (x in target_reciprocals) == (e > c and m % (e-c) == 0)
            # Complementation conjugates the affine reciprocal map to u -> u-c.
            if u != c:
                middle = Fraction(n,m)*Fraction(u,n)-Fraction(c,m)
                conjugate = 1/(m*middle)
                assert conjugate == Fraction(1,u-c)
                assert (conjugate in target_reciprocals) == (u > c and m % (u-c) == 0)
            affine_count += 1
        zero_preimage = Fraction(c,n)
        assert Fraction(n,m)*zero_preimage-Fraction(c,m) == 0
        for index in range(-5,6):
            image = Fraction(n,m)*Fraction(index,n)-Fraction(c,m)
            assert (image > 0) == (index > c)
            assert Fraction(m,n)*image+Fraction(c,n) == Fraction(index,n)
    composition_count = 0
    for n, m, last, c, d, index in product([1,2,6], [1,2,6], [1,2,6], range(-3,4), range(-3,4), range(-3,4)):
        first_image = Fraction(n,m)*Fraction(index,n)-Fraction(c,m)
        composed = Fraction(m,last)*first_image-Fraction(d,last)
        assert composed == Fraction(n,last)*Fraction(index,n)-Fraction(c+d,last)
        composition_count += 1

    # Complete finite-box vertices, followed by direct arithmetic edge tests.
    graph_edges = []
    prime_count = adjacent_shell_count = passing_source_pair_count = 0
    for prime in range(13,1754,12):
        if not all(prime%d for d in range(2,isqrt(prime)+1)):
            continue
        prime_count += 1
        h = (prime-1)//12
        for a in range(3*h+1,9*h):
            adjacent_shell_count += 1
            supply = prime*a
            residual = 4*a-prime
            pairs = [(1,1)]
            for q, budget in factors(supply):
                q_powers = [q**j for j in range(1,budget+1)]
                pairs = [(m,n) for m,n in pairs for m,n in [(m,n)]+[(m*k,n) for k in q_powers]+[(m,n*k) for k in q_powers]]
            for m,n in pairs:
                if (m+n) % residual:
                    continue
                passing_source_pair_count += 1
                target_supply = prime*(a+1)
                for kind, target in [('L',(m+n,n)), ('J',(m,m+n))]:
                    x,y = target
                    if target_supply%x == 0 and target_supply%y == 0 and gcd(x,y)==1 and (x+y)%(residual+4)==0:
                        graph_edges.append({'kind':kind,'source':(prime,a,m,n),'target':(prime,a+1,x,y)})
    incoming = Counter(edge['target'] for edge in graph_edges)
    outgoing = Counter(edge['source'] for edge in graph_edges)
    assert all(count==1 for count in incoming.values())
    assert all(count==1 for count in outgoing.values())
    assert set(incoming).isdisjoint(outgoing)
    assert len(graph_edges) == 8
    assert (prime_count, adjacent_shell_count, passing_source_pair_count) == (63,26439,3956)
    n,m,c,u,v = 440**2,441**2,1,8800,9261
    assert Fraction(n,m*u)-Fraction(c,m) == Fraction(1,v)
    assert n//u == 22 and m//v == 21
    assert Fraction(n,m*22)-Fraction(1,m) == Fraction(419,9261) != Fraction(1,21)
    assert Fraction(1,22)/(1-Fraction(1,22)) == Fraction(1,21)
    # The residue-class restriction in no-two-shears is material.
    outside_prime = 1613
    assert all(outside_prime%d for d in range(2,isqrt(outside_prime)+1))
    assert outside_prime % 12 == 5
    assert all((a+1) % (4*a-outside_prime) == 0 for a in (404,405,406))

    # The missing hypothesis really changes the lemma's truth value.
    # V=(2,2),W=(1,2): det=2 and det(V,E) is even for every E.
    assert 2*2-2*1 == 2 and gcd(2, 2) == 2
    output = {
        'status': 'pass',
        'single_affine_signed_coefficient_cases': count,
        'mixed_budgets_mandatory_factors_and_simultaneous_cases': simultaneous,
        'p37_local_tables': tables,
        'p241_nonzero_obstruction_checked': True,
        'empty_leaf_exact_rows': rows,
        'rational_witness_and_fixed_y_examples_checked': True,
        'p37_full_unary_distinction_and_p1753_strict_shear_example_checked': True,
        'affine_and_complemented_reciprocal_cases': affine_count,
        'signed_affine_composition_cases': composition_count,
        'affine_zero_fibre_and_full_positive_image_domain_checked': True,
        'matching_graph_audit': {'prime_count':prime_count,'adjacent_shell_count':adjacent_shell_count,
                                 'passing_source_pair_count':passing_source_pair_count,'edge_count':len(graph_edges),
                                 'all_indegrees_outdegrees_at_most_one':True,'no_directed_path_length_two':True,
                                 'edges':graph_edges},
        'p1753_raw_J_counterexample_and_corrected_L_J_returns_checked':True,
        'no_two_shears_hypothesis_boundary_p1613_mod12_5': 'Two consecutive L edges occur at a404,405,406; this is outside the theorem and confirms the p congruence must remain attached.',
        'missing_primitivity_counterexample_checked': True,
        'limitations': 'Finite numerical checks support, and do not replace, the deductive theorem-by-theorem review.'
    }
    target = Path(__file__).resolve().with_name('review_checks.json')
    target.write_text(json.dumps(output, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
