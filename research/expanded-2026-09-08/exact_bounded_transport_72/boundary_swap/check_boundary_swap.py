"""Exact finite audit of the four same-shell rational coordinate maps.

No imported project mathematics is used. The finite run is a check of the
stated formulas, not a proof for unbounded primes. Retained raw coordinates
are checked before their full scale fibre is enumerated independently.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
from math import gcd, isqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent
REVIEWED_PROOF_SHA256 = 'aa2af846808a077ce951d279da4249df742ab18c4e0d0f1880a47c3a675c60dc'


def require(condition, *context):
    if not condition:
        raise AssertionError(context)


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def divisors(n):
    low, high = [], []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            low.append(d)
            if d * d != n:
                high.append(n // d)
    return low + high[::-1]


def factored_square_divisors(n):
    """Valuation-box enumeration, independent of raw A/B factor enumeration."""
    remaining, d, result = n, 2, [1]
    while d * d <= remaining:
        e = 0
        while remaining % d == 0:
            remaining //= d
            e += 1
        if e:
            result = [x * d**t for x in result for t in range(2 * e + 1)]
        d += 1
    if remaining > 1:
        result = [x * remaining**t for x in result for t in range(3)]
    return sorted(result)


def encode(p, j, A, B, eps, half=False):
    h = (p - 1) // 12
    J, M = (3 * h, 6 * h) if half else (6 * h, 9 * h)
    require(0 <= j < J and 1 <= A <= M and 1 <= B <= M, 'code domain')
    lam, total = 2 * J * M, 2 * J * M * M
    c = (A - 1) * lam + 2 * M * j + 2 * (B - 1) + eps
    aa, rest = divmod(c, lam)
    jj, rest = divmod(rest, 2 * M)
    bb, ee = divmod(rest, 2)
    require((aa + 1, jj, bb + 1, ee) == (A, j, B, eps), 'decoder')
    require(0 <= c < total, 'code interval')
    return c, lam, total


def transform(p, R, state, swap, toggle):
    A, B, C, D, eps = state
    alpha, beta = (B, A) if swap else (A, B)
    eta = eps ^ toggle
    return alpha, beta, Fraction(alpha + p**(1 - eta) * beta, R), D, eta


def expected_denominator(p, R, eps, swap, toggle):
    if toggle:
        return R // gcd(R, p - 1)
    if swap and eps == 0:
        return R // gcd(R, p * p - 1)
    return 1


def reconstruct(p, R, state):
    A, B, C, D, eps = state
    a = A * B * D
    y, z = p**eps * A * C * D, p * B * C * D
    dy, dz = R * y - p * a, R * z - p * a
    return a, y, z, dy, dz


def json_state(state):
    return [str(x) if isinstance(x, Fraction) else x for x in state]


def audit(limit):
    counts, examples = Counter(), {}
    prime_minima = []
    for p in range(13, limit + 1, 12):
        if not prime(p):
            continue
        counts['eligible_primes'] += 1
        h = (p - 1) // 12
        a3 = 3*h+1
        r3_factors = [ell for ell in divisors(a3) if ell % 3 == 2 and prime(ell)]
        r3_least_factor = min(r3_factors) if r3_factors else None
        all_codes = [set(), set()]
        box_codes = [set(), set()]
        hit_records = {}
        for j in range(6 * h):
            a, R = 3 * h + j + 1, 4 * j + 3
            require(R == 4 * a - p and a < p, 'original shell')
            require(gcd(a, R) == 1 and gcd(p, R) == 1, 'shell units')
            counts['original_shells'] += 1
            raw_fibres = defaultdict(set)
            raw_primitive_hits = set()
            # Complete ordered raw-factor enumeration: D is uniquely forced.
            for A in divisors(a):
                for B in divisors(a // A):
                    D = a // (A * B)
                    require(A * B * D == a, 'raw product')
                    counts['raw_factor_triples'] += 1
                    for eps in (0, 1):
                        counts['raw_tagged_candidates'] += 1
                        numerator = A + p**(1 - eps) * B
                        if numerator % R:
                            continue
                        C = numerator // R
                        state = (A, B, Fraction(C), D, eps)
                        counts['raw_passing_tuples'] += 1
                        k = gcd(A, B)
                        require(C % k == 0 and gcd(k, R) == 1, 'raw scale gate')
                        A0, B0, C0, D0 = A // k, B // k, C // k, k * k * D
                        primitive = (A0, B0, C0, D0, eps)
                        require(gcd(A0, B0) == 1, 'coprime pair')
                        require((k * A0, k * B0, k * C0, D0 // (k * k), eps)
                                == (A, B, C, D, eps), 'raw inverse')
                        raw_fibres[primitive].add(k)
                        raw_primitive_hits.add((A0, B0, eps))
                        if j == 0 and B0 == 1 and eps == 0:
                            require(r3_least_factor is not None and A0 % 3 == 2,
                                    'passing residual-three boundary factor')
                            require(2*(r3_least_factor-1) <= 2*(A0-1), 'boundary-to-global decrease')
                            require((2*(r3_least_factor-1) == 2*(A0-1))
                                    == (r3_least_factor == A0), 'boundary-to-global equality fibre')
                            counts['r3_boundary_raw_source_inequalities'] += 1
                        original = reconstruct(p, R, state)
                        x, y, z, dy, dz = original
                        u, S = B * B * D, p * a
                        require((x, dy, dz) == (a, p**eps * A*A*D,
                                                  p**(2-eps) * B*B*D), 'oriented residuals')
                        require(dy * dz == S*S, 'original divisor product')
                        require(Fraction(1, x) + 1/y + 1/z == Fraction(4, p), 'original ES identity')
                        require(reconstruct(p, R, (A0, B0, Fraction(C0), D0, eps))
                                == original, 'all original coordinates at raw scale')
                        require(gcd(a, u) == k * B * D == B0 * D0, 'actual gcd')
                        integral_targets = set()
                        for swap in (0, 1):
                            for toggle in (0, 1):
                                target = transform(p, R, state, swap, toggle)
                                alpha, beta, target_C, target_D, eta = target
                                delta = expected_denominator(p, R, eps, swap, toggle)
                                counts['rational_map_rows'] += 1
                                counts[f'map_s{swap}_t{toggle}_delta_{"one" if delta == 1 else "obstructed"}'] += 1
                                require(target_C.denominator == delta, 'C obstruction order', p, j, state, swap, toggle)
                                rx, ry, rz, rdy, rdz = reconstruct(p, R, target)
                                require(ry.denominator == rz.denominator == delta, 'witness denominator obstruction')
                                require((rx, rdy, rdz) == (a, p**eta*alpha*alpha*D,
                                                            p**(2-eta)*beta*beta*D), 'target residuals')
                                require(rdy*rdz == S*S, 'target residual product')
                                require(Fraction(1, rx) + 1/ry + 1/rz == Fraction(4,p), 'rational target ES identity')
                                require(transform(p, R, target, swap, toggle) == state, 'involution')
                                for second_swap in (0, 1):
                                    for second_toggle in (0, 1):
                                        require(transform(p, R, target, second_swap, second_toggle)
                                                == transform(p, R, state, swap ^ second_swap, toggle ^ second_toggle),
                                                'complete rational composition')
                                        counts['rational_composition_checks'] += 1
                                require(gcd(alpha, beta) == k, 'retained raw gcd')
                                target0 = (alpha//k, beta//k, target_C/k, k*k*D, eta)
                                require(reconstruct(p, R, target0) == (rx, ry, rz, rdy, rdz), 'rational raw-scale morphism')
                                require((target_C/k).denominator == delta, 'primitive gate denominator')
                                # Full inverse from original ordered denominator data,
                                # carrying the original raw scale k as its fibre label.
                                ratio = Fraction(rdy, S)
                                eta_back = 0 if ratio.denominator % p == 0 else 1
                                recovered_A0 = ratio.numerator
                                recovered_B0 = ratio.denominator // p**(1-eta_back)
                                recovered_D0 = a // (recovered_A0 * recovered_B0)
                                recovered_C0 = Fraction(recovered_A0 + p**(1-eta_back)*recovered_B0, R)
                                recovered = (k*recovered_A0, k*recovered_B0, k*recovered_C0,
                                             recovered_D0//(k*k), eta_back)
                                require(recovered == target, 'ordered witness/full raw inverse')
                                target_u = beta*beta*D
                                require(target_u == (a*a//u if swap else u), 'original u image')
                                expected_dz = (Fraction(p**(2-eps-eta)*S*S, dz) if swap
                                               else Fraction(p**eps, p**eta)*dz)
                                require(rdz == expected_dz, 'exact cross-tag divisor image')
                                if not toggle:
                                    require(rdz == (Fraction(p**(2-2*eps)*S*S, dz)
                                                    if swap else dz), 'same-tag original d image')
                                order = R // gcd(R, alpha + p**(1-eta)*beta)
                                require(order == delta, 'Q/Z residue order')
                                if delta == 1:
                                    integral_targets.add((alpha//k, beta//k, eta))
                                for half in (False, True):
                                    if half and j >= 3*h:
                                        continue
                                    c, lam, total = encode(p, j, A0, B0, eps, half)
                                    target_c, target_lam, target_total = encode(p, j, alpha//k, beta//k, eta, half)
                                    require((lam, total) == (target_lam, target_total), 'same original radix')
                                    require(target_c-c == swap*(B0-A0)*(lam-2)+(eta-eps), 'exact code difference')
                                    counts['full_and_half_code_differences'] += 1
                                label = f'eps{eps}_s{swap}_t{toggle}_{"pass" if delta == 1 else "fail"}'
                                if label not in examples:
                                    examples[label] = {'p':p,'j':j,'a':a,'R':R,'raw':json_state(state),
                                                       'target':json_state(target),'delta':delta,
                                                       'original_witness':json_state(original[:3]),
                                                       'target_witness':json_state((rx,ry,rz))}
                                if k > 1 and 'nontrivial_raw_scale' not in examples:
                                    examples['nontrivial_raw_scale'] = {'p':p,'j':j,'raw':json_state(state),
                                                                       'primitive':primitive,'k':k}
                                if A == B and not toggle and swap:
                                    counts['same_tag_swap_fixed_points'] += 1
                                    if 'same_tag_swap_fixed_point' not in examples:
                                        examples['same_tag_swap_fixed_point'] = {'p':p,'j':j,'R':R,
                                                                               'raw':json_state(state)}
                        if (p-1) % R == 0:
                            expected_targets = {(aa,bb,ee) for aa,bb in ((A0,B0),(B0,A0)) for ee in (0,1)}
                            canonical = (min(A0,B0), max(A0,B0), 0)
                            counts['orbit_all_four_raw_sources'] += 1
                        elif (p*p-1) % R == 0:
                            expected_targets = {(A0,B0,eps),(B0,A0,eps)}
                            canonical = (min(A0,B0),max(A0,B0),eps)
                            counts['orbit_same_tag_pair_raw_sources'] += 1
                        elif eps == 0:
                            expected_targets = {(A0,B0,0)}
                            canonical = (A0,B0,0)
                            counts['orbit_exterior_singleton_raw_sources'] += 1
                        else:
                            expected_targets = {(A0,B0,1),(B0,A0,1)}
                            canonical = (min(A0,B0),max(A0,B0),1)
                            counts['orbit_middle_pair_raw_sources'] += 1
                        require(integral_targets == expected_targets, 'complete integral orbit')
                        for half in (False,True):
                            if half and j >= 3*h:
                                continue
                            source_code = encode(p,j,A0,B0,eps,half)[0]
                            target_codes = {encode(p,j,aa,bb,ee,half)[0] for aa,bb,ee in integral_targets}
                            require(encode(p,j,*canonical[:2],canonical[2],half)[0] == min(target_codes), 'orbit exact minimum')
                            all_codes[int(half)].add(source_code)
                            hit_records[(int(half),source_code)] = (j,A0,B0,eps)
            for primitive, scales in raw_fibres.items():
                D0 = primitive[3]
                require(scales == {k for k in range(1,isqrt(D0)+1) if D0 % (k*k) == 0}, 'complete scale fibre')
                counts['complete_raw_scale_fibres'] += 1
            # Original valuation-box sieve, independently deriving coprime A0/B0.
            box_hits = set()
            for u in factored_square_divisors(a):
                counts['original_square_divisors'] += 1
                g = gcd(a,u)
                require(g*g % u == 0, 'box D integrality')
                AA, BB, DD = a//g, u//g, g*g//u
                require((AA*BB*DD,BB*BB*DD)==(a,u) and gcd(AA,BB)==1, 'box original inverse')
                for ee in (0,1):
                    if (4*u+p**ee) % R == 0:
                        box_hits.add((AA,BB,ee))
                        for half in (False,True):
                            if not half or j < 3*h:
                                box_codes[int(half)].add(encode(p,j,AA,BB,ee,half)[0])
            require(box_hits == raw_primitive_hits, 'complete raw/box hit equality', p,j)
            counts['complete_shell_hit_set_comparisons'] += 1
            if j == 0:
                require(bool(box_hits) == bool(r3_factors), 'complete residual-three occupied-domain equivalence')
                counts['r3_occupied_shells' if box_hits else 'r3_empty_shells'] += 1
                if r3_least_factor is not None:
                    ell = r3_least_factor
                    DC = a3//ell
                    CC = (1+p*ell)//3
                    require((1,ell,0) in box_hits, 'residual-three selected prime factor')
                    selected_primitive = (1,ell,CC,DC,0)
                    require(raw_fibres[selected_primitive]
                            == {k for k in range(1,isqrt(DC)+1) if DC % (k*k) == 0},
                            'residual-three global selected complete raw-scale fibre')
                    counts['r3_selected_raw_scale_points'] += len(raw_fibres[selected_primitive])
                    require(reconstruct(p,3,(1,ell,Fraction(CC),DC,0))
                            == (a3,CC*DC,p*ell*CC*DC,DC,p*p*ell*ell*DC),
                            'residual-three displayed ordered denominators and residuals')
        require(all_codes == box_codes, 'complete prime code sets')
        # A-major, then j-major, B-major, tag-major direct search is exactly
        # the original code order. Budget failures are excluded exhaustively.
        minima = []
        for half in (False,True):
            J,M = (3*h,6*h) if half else (6*h,9*h)
            direct_first = None
            for AA in range(1,M+1):
                if direct_first is not None:
                    break
                for jj in range(J):
                    aa, RR = 3*h+jj+1,4*jj+3
                    if aa % AA:
                        continue
                    for BB in divisors(aa//AA):
                        if BB > M or gcd(AA,BB) != 1:
                            continue
                        for ee in (0,1):
                            counts['direct_least_search_budget_candidates'] += 1
                            if (AA+p**(1-ee)*BB) % RR == 0:
                                direct_first = encode(p,jj,AA,BB,ee,half)[0]
                                break
                        if direct_first is not None:
                            break
                    if direct_first is not None:
                        break
            codes = all_codes[int(half)]
            require(direct_first == (min(codes) if codes else None), 'independent exact global minimum')
            require(direct_first is not None, 'finite run unexpectedly has no hit',p,half)
            jj,AA,BB,ee = hit_records[(int(half),direct_first)]
            RR = 4*jj+3
            require(ee != 1 or AA <= BB, 'least middle order')
            require(not (ee == 0 and AA > BB) or (p*p-1) % RR != 0, 'least exterior obstruction')
            require((p-1) % RR != 0 or (ee == 0 and AA <= BB), 'least all-four canonical tag/order')
            counts['independent_full_or_half_minima'] += 1
            if r3_least_factor is not None:
                require(direct_first == 2*(r3_least_factor-1), 'residual-three actual global least code')
                require((AA,jj,BB,ee) == (1,0,r3_least_factor,0), 'residual-three global least digits')
                counts['r3_global_minimum_formula_comparisons'] += 1
            minima.append({'radix':'first_half' if half else 'full','code':direct_first,
                           'j':jj,'A0':AA,'B0':BB,'epsilon':ee,'hit_code_count':len(codes)})
        prime_minima.append({'p':p,'minima':minima})
    return counts, examples, prime_minima


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--limit',type=int,default=1000)
    args = parser.parse_args()
    counts, examples, minima = audit(args.limit)
    proof = HERE / 'boundary_swap_completion.tex'
    require(proof.exists(), 'reviewed proof source must accompany checker')
    proof_hash = hashlib.sha256(proof.read_bytes()).hexdigest()
    require(proof_hash == REVIEWED_PROOF_SHA256, 'proof source differs from independently reviewed revision')
    result = {
        'status':'pass','generated_utc':datetime.now(timezone.utc).isoformat(),
        'scope':{'prime_upper_bound':args.limit,'prime_form':'p=12h+1','shells':'0 <= j < 6h',
                 'arithmetic':'integers and fractions.Fraction; no floating-point computations',
                 'finite_check_is_not_an_unbounded_proof':True},
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'proof_source':proof.name,'proof_sha256':proof_hash,
        'proof_read_status':'independently_read_pass_at_exact_hash',
        'counts':dict(counts),'examples':examples,'all_prime_minima':minima,
        'checked_relations':[
            'All four rational maps with their full pairwise compositions and retained source inverse.',
            'Exact Q/Z obstruction order and equal reduced denominators of C, y, z.',
            'Original labelled residuals, divisor complement with every p power, and ordered ES identity.',
            'Raw gcd scale, complete square-divisor scale fibres, and witness inverse retaining k.',
            'Original full and first-half code decoders and exact signed code differences.',
            'Complete integral orbit, its code minimum, and complete original divisor-box hit equality.',
            'Global full/half least hits independently found by original code order and orbit consequences.'
        ]
    }
    (HERE/'CHECK_BOUNDARY_SWAP.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':result['status'],'counts':dict(counts),'proof_sha256':result['proof_sha256']},indent=2))


if __name__ == '__main__':
    main()
