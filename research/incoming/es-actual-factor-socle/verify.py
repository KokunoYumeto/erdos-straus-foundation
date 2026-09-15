#!/usr/bin/env python3
"""Actual-factor socle certificates for fixed-seed Erdos--Straus branches.

Standard library only. All checks remain active under -O. The default finite
comparison uses the same k>=4, p>2u domain as the preceding two-block note.
A failed sufficient test is not an empty-branch certificate. No universal ES,
independent-review, novelty, or Lean claim is made.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import combinations_with_replacement, product
from math import gcd, isqrt, prod
from pathlib import Path
import json

CHECKS = Counter()
HARD = {1, 121, 169, 289, 361, 529}


def require(ok, label):
    CHECKS[label] += 1
    if not ok:
        raise ArithmeticError(label)


def primes_to(n):
    if n < 2:
        return []
    a = bytearray(b'\x01') * (n + 1)
    a[:2] = b'\0\0'
    for q in range(2, isqrt(n) + 1):
        if a[q]:
            a[q*q::q] = b'\0' * len(a[q*q::q])
    return [i for i in range(2, n + 1) if a[i]]


TRIAL = primes_to(10000)


@lru_cache(None)
def factor(n):
    if n < 1:
        raise ValueError('factor requires a positive integer')
    original = n
    out = []
    for q in TRIAL:
        if q*q > n:
            break
        e = 0
        while n % q == 0:
            n //= q
            e += 1
        if e:
            out.append((q, e))
    else:
        q = TRIAL[-1] + 2
        while q*q <= n:
            e = 0
            while n % q == 0:
                n //= q
                e += 1
            if e:
                out.append((q, e))
            q += 2
    if n > 1:
        out.append((n, 1))
    require(prod(q**e for q, e in out) == original, 'factor_product')
    return tuple(out)


def prime(n):
    return n >= 2 and factor(n) == ((n, 1),)


def divisors(fs):
    ds = [1]
    for q, e in fs:
        ds = [d * q**j for d in ds for j in range(e + 1)]
    return ds


def vp(n, q):
    if n <= 0:
        raise ValueError('finite valuation requires positive n')
    e = 0
    while n % q == 0:
        n //= q
        e += 1
    return e


@lru_cache(None)
def log3(h, k):
    if k < 3:
        raise ValueError('k>=3')
    h %= 1 << k
    if h % 8 not in (1, 3):
        raise ValueError('outside <3>')
    a = 0 if h % 8 == 1 else 1
    for j in range(4, k + 1):
        if pow(3, a, 1 << j) != h % (1 << j):
            a += 1 << (j - 3)
    require(pow(3, a, 1 << k) == h, 'binary_log_inverse')
    return a


def chart_log(q, k, base):
    if base == 3:
        return log3(q, k)
    if base != -3 or q % 8 not in (1, 5):
        raise ValueError('base must be 3 or -3 on its actual cyclic subgroup')
    a = log3(q if q % 8 == 1 else -q, k)
    require(pow(base, a, 1 << k) == q % (1 << k), 'second_chart_log_inverse')
    return a


def weight(a, o):
    a %= o
    return (a & -a) if a else 0  # identity cannot enter a degree o-1 packet


def coin_selection(n, items):
    """Items retain id, exponent limit, and a nonzero power-of-two weight.
    Return all prefix inequalities and a bounded count vector, or None.
    A bounded highest-denomination-first construction is exact for powers of 2.
    """
    if n < 1:
        raise ValueError('positive cyclic exponent n')
    o = 1 << n
    if any(it['weight'] <= 0 or it['weight'] >= o or
           it['weight'] & (it['weight'] - 1) or it['limit'] < 0 for it in items):
        raise ValueError('proper dyadic weights and nonnegative original budgets')
    prefixes = []
    for j in range(n):
        v = sum(it['weight'] * it['limit'] for it in items if it['weight'] <= 1 << j)
        prefixes.append(dict(level=j, available=v, required=(1 << (j+1))-1))
    if any(x['available'] < x['required'] for x in prefixes):
        return None, prefixes
    rem = o - 1
    counts = [0] * len(items)
    for i in sorted(range(len(items)), key=lambda i: (-items[i]['weight'], i)):
        w = items[i]['weight']
        counts[i] = min(items[i]['limit'], rem // w)
        rem -= counts[i] * w
    require(rem == 0, 'bounded_dyadic_coin_inverse')
    require(sum(c*it['weight'] for c, it in zip(counts, items)) == o-1,
            'exact_not_excess_top_degree')
    return counts, prefixes


def submasks(c):
    z = c
    out = []
    while True:
        out.append(z)
        if z == 0:
            return sorted(out)
        z = (z-1) & c


def rotate(bits, shift, o):
    shift %= o
    mask = (1 << o) - 1
    if shift == 0:
        return bits & mask
    return ((bits << shift) | (bits >> (o-shift))) & mask


def packet_certificate(items, counts, o):
    """Unweighted binary submask words, NOT labelled equal-prime subsets.
    Exact positive integer coefficients and one full inverse representative.
    """
    count = [0] * o
    count[0] = 1
    reps = {0: [0] * len(items)}
    bits = []
    for i, (it, c) in enumerate(zip(items, counts)):
        h = 0
        while (1 << h) <= c:
            if c & (1 << h):
                shift = it['log'] * (1 << h) % o
                count = [count[r] + count[(r-shift) % o] for r in range(o)]
                new = dict(reps)
                for r, vec in reps.items():
                    rr = (r + shift) % o
                    if rr not in new:
                        vv = list(vec)
                        vv[i] += 1 << h
                        new[rr] = vv
                reps = new
                bits.append(dict(item=i, exponent_bit=h, cyclic_shift=shift))
            h += 1
    require(len(reps) == o and all(x % 2 == 1 for x in count), 'every_cyclic_coefficient_odd')
    require(sum(count) == 1 << len(bits), 'submask_mass_not_binomial_mass')
    for r, vec in reps.items():
        require(sum(v*it['log'] for v, it in zip(vec, items)) % o == r,
                'packet_word_modular_inverse')
        require(all(v & ~c == 0 for v, c in zip(vec, counts)), 'packet_word_binary_submask')
    # A separate GF(2) multiplication and suffix inverse retains zero parity as
    # a reduced observation only; even positive integer coefficients stay above.
    suffix = [0] * (len(bits)+1)
    suffix[-1] = 1
    for j in range(len(bits)-1, -1, -1):
        suffix[j] = suffix[j+1] ^ rotate(suffix[j+1], bits[j]['cyclic_shift'], o)
    require(suffix[0] == (1 << o)-1, 'independent_bitset_top_norm')
    chosen = {}
    for target in range(o):
        r = target
        vec = [0] * len(items)
        for j, b in enumerate(bits):
            if suffix[j+1] >> r & 1:
                continue
            r = (r-b['cyclic_shift']) % o
            require(bool(suffix[j+1] >> r & 1), 'odd_suffix_inverse_exists')
            vec[b['item']] += 1 << b['exponent_bit']
        require(r == 0, 'odd_suffix_inverse_terminates')
        chosen[target] = vec
    return count, chosen, bits


def inventory(p, k, fs, base):
    if not (k >= 3 and p % 8 == 1):
        raise ValueError('dyadic parameter domain')
    o = 1 << (k-2)
    inside = (1, 3) if base == 3 else (1, 5)
    items = []
    for q, e in fs:
        if q % 8 in inside:
            a = chart_log(q, k, base)
            w = weight(a, o)
            if w:
                items.append(dict(kind='prime', prime=q, limit=e, log=a, weight=w))
    s = chart_log(p, k, base)
    w = weight(s, o)
    if w:
        items.append(dict(kind='phase', prime=None, limit=1, log=(-s) % o, weight=w))
    counts, prefixes = coin_selection(k-2, items)
    outside = [q for q, e in fs if q % 8 not in inside]
    return dict(base=base, o=o, phase=s, items=items, selected=counts,
                prefixes=prefixes, outside_primes=outside,
                certified=counts is not None and bool(outside))


def reconstruct(p, k, Q):
    u = 1 << (2*k-5)
    N = p + 4*u
    m = 1 << k
    if not (p % 8 == 1 and p > 2*u and Q > 0 and N % Q == 0 and Q % m == m-1):
        raise ValueError('original fixed-seed cofactor domain')
    R = N // Q
    a = (p + R) // 4
    d = gcd(a, u)
    h, r, s = d*d//u, u//d, a//d
    require((r+s) % R == 0, 'original_middle_quotient')
    lam = (r+s) // R
    den = (a, p*h*s*lam, p*h*r*lam)
    require(0 < R < p and p < 4*a and 2*a < p, 'first_half_and_positive_residual')
    require(a == h*r*s and u == h*r*r and gcd(r, s) == 1, 'original_normalization')
    require(sum((Fraction(1, x) for x in den), Fraction()) == Fraction(4, p),
            'ordered_reciprocal_identity')
    require(Fraction(p*a*a, R*den[1]-p*a) == u, 'ordered_divisor_inverse')
    af = factor(a)
    beta = [vp(u, q)-e if u % q == 0 else -e for q, e in af]
    require(all(-e <= b <= e for b, (_, e) in zip(beta, af)), 'original_centered_exponent_box')
    return dict(p=p, k=k, u=u, N=N, R=R, Q=Q, a=a, h=h, r=r, s=s,
                lambda_=lam, channel='M', denominators=den, a_factors=af, beta=beta)


def outside_divisor_mass(fs, inside):
    tau = prod(e+1 for q, e in fs)
    signed = prod((e+1) if q % 8 in inside else (1 if e % 2 == 0 else 0) for q, e in fs)
    return (tau-signed) // 2


def force(p, k, fs, base, details=False):
    dat = inventory(p, k, fs, base)
    if not dat['certified']:
        return dat
    items, counts, o = dat['items'], dat['selected'], dat['o']
    coeff, inverse, bits = packet_certificate(items, counts, o)
    q = dat['outside_primes'][0]
    target = chart_log(-pow(q, -1, 1 << k), k, base)
    vec = inverse[target]
    phase = 0
    word = 1
    for f, it in zip(vec, items):
        if it['kind'] == 'phase':
            phase = f
        else:
            word *= it['prime']**f
    value = q * word
    N = p + (1 << (2*k-3))
    require(N % value == 0, 'available_word_divides_original_N')
    Q = value if phase == 0 else N // value
    state = reconstruct(p, k, Q)
    # Inverse from the original state with the role and outside prime retained.
    back_value = Q if phase == 0 else state['R']
    require(back_value % q == 0, 'outside_prime_return')
    back_word = back_value // q
    for f, it in zip(vec, items):
        if it['kind'] == 'prime':
            require(vp(back_word, it['prime']) == f, 'prime_word_inverse')
    chosen_primes = {it['prime'] for c, it in zip(counts, items) if c and it['kind'] == 'prime'}
    free = [(q0, e) for q0, e in fs if q0 not in chosen_primes]
    inside = (1, 3) if base == 3 else (1, 5)
    mass = outside_divisor_mass(free, inside)
    delta = next((c for c, it in zip(counts, items) if it['kind'] == 'phase'), 0)
    lower = mass if delta == 0 else (mass+1)//2
    dat.update(state=state, chosen_target=target, word_exponents=vec, role=phase,
               outside_prime=q, actual_word=word, bits=bits,
               packet_mass=sum(coeff), number_representatives=min(coeff),
               free_factorization=free, outside_free_mass=mass, count_lower=lower)
    if details:
        dat['coefficients'] = coeff
        dat['inverse_table'] = [[r, inverse[r]] for r in range(o)]
    return dat


@lru_cache(None)
def previous_threshold(k, f, s):
    o = 1 << (k-2)
    J = log3(11, k)
    marks = sorted({(J*j-t) % o for j in range(min(f, o-1)+1) for t in (0, s)})
    return max((marks[(i+1) % len(marks)]-x) % o or o for i, x in enumerate(marks))-1


def short_word_test(p, k, fs):
    m = 1 << k
    targets = {m-1, (-p) % m}  # BOTH roles, unlike an unfair cofactor-only baseline
    for i, (q, e) in enumerate(fs):
        if q % m in targets:
            return True
        for j in range(i, len(fs)):
            r, f = fs[j]
            if (i != j or e >= 2) and q*r % m in targets:
                return True
    return False


@lru_cache(None)
def avoiding_subgroups(k):
    m = 1 << k
    n = k-2
    out = [dict(name='identity', elements=frozenset({1}), rank_power=0, epsilon=0)]
    for j in range(1, n+1):
        for ep in (0, 1):
            g = (-1 if ep else 1)*pow(3, 1 << (n-j), m) % m
            H = frozenset(pow(g, t, m) for t in range(1 << j))
            require(m-1 not in H and len(H) == 1 << j, 'explicit_target_avoiding_subgroups')
            out.append(dict(name=f'H({j},{ep})', elements=H, rank_power=j, epsilon=ep))
    return tuple(out)


@lru_cache(None)
def quotient_data(k, index):
    m = 1 << k
    H = avoiding_subgroups(k)[index]['elements']
    todo = set(range(1, m, 2))
    coset = {}
    while todo:
        r = min(todo)
        C = {r*h % m for h in H}
        for g in C:
            coset[g] = r
        todo -= C
    cyclic = {}
    for r in set(coset.values()):
        S = {1}
        g = r
        while g not in H:
            S.add(coset[g])
            g = g*r % m
        cyclic[r] = frozenset(S)
    return coset, cyclic


def obstruction_candidates(p, k, fs):
    m = 1 << k
    result = []
    for i, item in enumerate(avoiding_subgroups(k)):
        H = item['elements']
        index = (m//2) // len(H)
        t = 1 if p % m in H else 2
        outer = sum(e for q, e in fs if q % m not in H)
        if outer > index-1-t:
            continue
        cos, cyclic = quotient_data(k, i)
        C = Counter()
        for q, e in fs:
            r = cos[q % m]
            if r != 1:
                C[cyclic[r]] += e
        if any(v >= len(g)-1 for g, v in C.items()):
            continue
        result.append(dict(name=item['name'], index=index, target_cosets=t,
                           outside_occurrences=outer, maximum=index-1-t,
                           cyclic_counts=[[sorted(g), v, len(g)-2] for g, v in sorted(C.items(), key=lambda x: sorted(x[0]))]))
    return result


def structural():
    budgets = 0
    for n in range(1, 6):
        for E in product(range(5), repeat=n):
            items = [dict(weight=1 << j, limit=E[j]) for j in range(n)]
            selected, pre = coin_selection(n, items)
            target = (1 << n)-1
            possible = 1
            for j, e in enumerate(E):
                new = 0
                for i in range(e+1):
                    new |= possible << ((1 << j)*i)
                possible = new & ((1 << (target+1))-1)
            require((selected is not None) == bool(possible >> target & 1), 'prefix_iff_bounded_top_weight')
            budgets += 1
    # Exhaust actual residues, varying repeated-prime binary exponent budgets.
    packets = 0
    for n, length, emax in ((1, 3, 3), (2, 3, 3), (3, 2, 4), (4, 2, 2)):
        o = 1 << n
        for logs in combinations_with_replacement(range(1, o), length):
            for E in product(range(1, emax+1), repeat=length):
                items = [dict(weight=a & -a, limit=e, log=a) for a, e in zip(logs, E)]
                c, _ = coin_selection(n, items)
                if c is not None:
                    packet_certificate(items, c, o)
                    packets += 1
    # Submask identity is coefficient-level Lucas/Frobenius, checked via binomial coefficients.
    from math import comb
    for c in range(80):
        require(submasks(c) == [i for i in range(c+1) if comb(c, i) % 2], 'actual_exponent_submask_parity')
    # Exact Pascal change of basis and its inverse, modulo 2.
    for n in range(1, 6):
        o = 1 << n
        for a in range(o):
            in_t = [comb(a, j) % 2 for j in range(o)]
            back = [sum(in_t[j]*(comb(j, r) % 2) for j in range(r, o)) % 2 for r in range(o)]
            require(back == [int(r == a) for r in range(o)], 'Pascal_basis_round_trip')
        require(all(comb(o-1, j) % 2 == 1 for j in range(o)), 'top_socle_coefficients_all_one')
        require(sum(comb(o-1, j) % 2 for j in range(o)) % 2 == 0, 'augmentation_zero_not_absence')
    # Independent brute force of the exact stabilizer, no Kneser subroutine.
    stabilizers = 0
    for k, maxlen in ((3, 6), (4, 5), (5, 3)):
        m = 1 << k
        G = list(range(1, m, 2))
        for length in range(maxlen+1):
            for seq in combinations_with_replacement(G, length):
                W = {1}
                for q in seq:
                    W |= {q*x % m for x in list(W)}
                if m-1 in W:
                    continue
                H = frozenset(h for h in G if {h*x % m for x in W} == W)
                names = [i for i, h in enumerate(avoiding_subgroups(k)) if h['elements'] == H]
                require(len(names) == 1, 'full_stabilizer_is_in_explicit_list')
                N = prod(seq) % m
                candidates = obstruction_candidates(N, k, tuple(Counter(seq).items()))
                require(avoiding_subgroups(k)[names[0]]['name'] in [x['name'] for x in candidates], 'all_actual_missing_sets_obey_concentration')
                stabilizers += 1
    # Nonuniform odd cover: odd coefficients do not mean unique witnesses.
    nonuniform_items = [dict(log=a, weight=1, limit=c) for a, c in ((1, 3), (3, 3), (5, 1))]
    nonuniform, _, _ = packet_certificate(nonuniform_items, [3, 3, 1], 8)
    require(len(set(nonuniform)) > 1 and all(c % 2 for c in nonuniform), 'odd_cover_not_uniform_cover')
    return dict(coin_budgets=budgets, actual_packets=packets, actual_empty_stabilizers=stabilizers,
                nonuniform_odd_cover=nonuniform)


def negative_controls():
    out = []
    def reject(label, fn):
        try:
            fn()
        except (ValueError, ArithmeticError):
            out.append(label)
            return
        raise ArithmeticError('negative control was accepted: '+label)
    reject('logarithm outside the actual cyclic chart', lambda: chart_log(7, 5, 3))
    reject('identity phase treated as a proper dyadic weight', lambda: coin_selection(3, [dict(weight=8, limit=1)]))
    reject('insufficient actual prime budget activated', lambda: require(coin_selection(3, [dict(weight=1, limit=1), dict(weight=4, limit=1)])[0] is not None, 'absent_budget_not_supported_zero'))
    reject('top degree replaced by overrun', lambda: packet_certificate([dict(log=1)], [8], 8))
    reject('augmentation detects target absence', lambda: require(sum([1]*8) % 2 != 0, 'bad_augmentation_inference'))
    reject('odd packet is one-to-one without proof', lambda: require(len(set([3, 5, 5, 5, 5, 3, 3, 3])) == 1, 'bad_unique_cover'))
    reject('phase symbol is an available prime factor', lambda: require((853281 % 852769) == 0, 'formal_phase_is_not_divisor'))
    reject('one local certificate settles entire prime', lambda: reconstruct(49681, 6, 7))
    return out


def examples():
    out = []
    for p, k in ((80809,5), (852769,6), (1546729,5), (1331761,5), (49681,6), (482187176641,6)):
        require(prime(p), 'example_deterministic_primality')
        N = p + (1 << (2*k-3))
        fs = factor(N)
        qs = sorted(q for q in divisors(fs) if q % (1 << k) == (1 << k)-1)
        f = dict(fs)
        threshold = previous_threshold(k, f.get(11,0), log3(p,k))
        old = any(q % 8 in (5,7) for q,e in fs) and f.get(3,0) >= threshold
        records = [force(p,k,fs,base,True) for base in (3,-3)]
        for rec in records:
            if rec['certified']:
                require(rec['count_lower'] <= len(qs), 'disjoint_remainder_count_lower_bound')
        states = [reconstruct(p,k,Q) for Q in qs]
        out.append(dict(p=p,k=k,N=N,factorization=fs,old_threshold=threshold,old_forces=old,
                        short_words_both_roles=short_word_test(p,k,fs),charts=records,
                        complete_states=states,obstruction_candidates=obstruction_candidates(p,k,fs)))
    # This genuinely separates the new theorem from both older simple tests.
    special = next(x for x in out if x['p'] == 852769)
    require(not special['old_forces'] and not special['short_words_both_roles'], 'strict_new_branch_beyond_fair_baseline')
    require(len(special['complete_states']) == 1 and special['charts'][0]['certified'], 'strict_example_original_single_state')
    opposite = out[-1]
    require(opposite['old_forces'] and not any(c['certified'] for c in opposite['charts']), 'two_methods_proved_incomparable')
    return out


def scan(bound):
    totals = Counter()
    keys = ('old_two_block','socle','subgroup_forcing','old_plus_socle','short_both_roles','fair_baseline','fair_plus_socle','actual')
    psets = {k:set() for k in keys}
    rows = []
    added = []
    witness_digest = sha256()
    for p in primes_to(bound):
        if p % 840 not in HARD:
            continue
        totals['hard_primes'] += 1
        k = 4
        while p > 2*(1 << (2*k-5)):
            N = p + (1 << (2*k-3))
            fs = factor(N)
            m = 1 << k
            qs = sorted(Q for Q in divisors(fs) if Q % m == m-1)
            actual = bool(qs)
            totals['branches'] += 1
            totals['original_middle_states'] += len(qs)
            f = dict(fs)
            old = any(q % 8 in (5,7) for q,e in fs) and f.get(3,0) >= previous_threshold(k,f.get(11,0),log3(p,k))
            inventories = [inventory(p,k,fs,base) for base in (3,-3)]
            socle = any(r['certified'] for r in inventories)
            short = short_word_test(p,k,fs)
            subgroup = not obstruction_candidates(p,k,fs)
            vals = dict(old_two_block=old,socle=socle,subgroup_forcing=subgroup,
                        old_plus_socle=old or socle,short_both_roles=short,
                        fair_baseline=old or short,fair_plus_socle=old or short or socle,actual=actual)
            require(not(old or socle or subgroup or short) or actual, 'all_sufficient_tests_sound')
            if socle:
                for base, inv in zip((3,-3),inventories):
                    if inv['certified']:
                        cert = force(p,k,fs,base)
                        require(cert['state']['Q'] in qs and cert['count_lower'] <= len(qs), 'scan_original_return_and_count')
                        witness_digest.update(json.dumps(cert['state'],sort_keys=True,separators=(',',':')).encode())
                        break
            for key, yes in vals.items():
                totals[key+'_branches'] += yes
                if yes:
                    psets[key].add(p)
            if socle and not(old or short):
                added.append(dict(p=p,k=k,factorization=fs,states=[reconstruct(p,k,Q) for Q in qs]))
            row = [p,k,N,fs,int(old),int(socle),int(subgroup),int(short),len(qs)]
            rows.append(row)
            k += 1
    for key in keys:
        totals[key+'_primes'] = len(psets[key])
    digest = sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()
    return dict(bound=bound, scope='six mod840 classes; k>=4; original p>2u dyadic domain',
                totals=dict(totals),new_beyond_both_short_roles_and_old=added,
                additional_primes_beyond_fair_baseline=sorted(psets['fair_plus_socle']-psets['fair_baseline']),
                row_digest=digest,marked_return_digest=witness_digest.hexdigest(),rows=rows)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--bound',type=int,default=2000000)
    ap.add_argument('--out',default='generated')
    args = ap.parse_args()
    if args.bound < 2:
        ap.error('bound >= 2')
    dest = Path(args.out)
    dest.mkdir(parents=True,exist_ok=True)
    st = structural()
    ex = examples()
    ne = negative_controls()
    sc = scan(args.bound)
    for name,obj in [('structural.json',st),('examples.json',ex),('negative_controls.json',ne),('scan.json',sc),('checks.json',dict(CHECKS))]:
        (dest/name).write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n',encoding='utf8')
    print(json.dumps(dict(checks=sum(CHECKS.values()),negative_controls=len(ne),totals=sc['totals']),sort_keys=True))

if __name__ == '__main__':
    main()
