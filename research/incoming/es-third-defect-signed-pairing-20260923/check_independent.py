#!/usr/bin/env python3
"""Independent integer audit; imports no programme implementation."""
from __future__ import annotations

import json
from math import gcd, isqrt


def need(ok: bool, label: str) -> None:
    if not ok:
        raise AssertionError(label)


def prime(n: int) -> bool:
    if n < 2 or (n % 2 == 0 and n != 2):
        return False
    return all(n % j for j in range(3, isqrt(n) + 1, 2))


def factor(n: int) -> list[tuple[int, int]]:
    ans = []
    j = 2
    while j * j <= n:
        exponent = 0
        while n % j == 0:
            n //= j
            exponent += 1
        if exponent:
            ans.append((j, exponent))
        j = 3 if j == 2 else j + 2
    if n > 1:
        ans.append((n, 1))
    return ans


def divs(n: int) -> list[int]:
    ans = [1]
    for q, exponent in factor(n):
        ans = [d * q**j for d in ans for j in range(exponent + 1)]
    return sorted(ans)


def independent_r27(p: int) -> dict[str, object]:
    need(prime(p) and p % 216 in (73, 145), 'R27 prime domain')
    a = (p + 27) // 4
    words = divs(a * a)
    trace = [u for u in words if u % 9 == 2]
    exterior = [u for u in words if (4 * u + 1) % 27 == 0]
    middle = [u for u in words if (p + 4 * u) % 27 == 0]
    need(2 * len(exterior) + len(middle) == len(trace), 'independent R27 count')
    for u in trace:
        v = a * a // u
        need(v in trace, 'independent complement membership')
        bu = ((p + 4 * u) // 9) % 3
        bv = ((p + 4 * v) // 9) % 3
        need((bu + bv) % 3 == 0, 'independent colour reversal')
    fs = factor(a)
    first = all(q % 3 == 1 for q, _e in fs)
    five_count = sum(e for q, e in fs if q % 9 == 5)
    second = five_count == 2 and all(q % 9 in (1, 5) for q, _e in fs)
    need((len(trace) == 0) == (first or second), 'independent factor classification')
    return {'p': p, 'a': a, 'E': len(exterior), 'M': len(middle),
            'T3': len(trace), 'exception_A': first, 'exception_B': second}


def residuals(p: int) -> list[int]:
    need(prime(p) and p % 24 == 1, 'hard prime')
    n = p - 1
    k = 0
    while n % 2 == 0:
        n //= 2
        k += 1
    eta = 0
    while n % 3 == 0:
        n //= 3
        eta += 1
    answer = []
    for d in divs(n):
        r0 = 3 ** (eta + 1) * d
        if d % 4 == ((-1) ** eta) % 4:
            need(r0 < p and r0 % 4 == 3 and gcd(r0, p - 1) == r0 // 3,
                 'independent residual construction')
            answer.append(r0)
    direct = [r0 for r0 in range(3, p, 4) if gcd(r0, p - 1) == r0 // 3]
    need(answer == direct, 'complete residual list')
    need(k >= 3 and eta >= 1, 'hard-prime valuations')
    return answer


def cross_check() -> dict[str, int]:
    p, r0, m = 73, 3, 1
    a, ap = 19, 22
    d, e = 1, 2
    alpha, beta = 1387, 803
    lam, mu = 1, 730
    need(d * alpha == p * a and e * beta == p * ap, 'actual complements')
    need(r0 * lam == d + e and r0 * mu == alpha + beta, 'actual quotients')
    need(lam * beta - d * mu == p * m, 'determinant')
    # Cross multiplication keeps all four summands visible.
    lhs = 4 * a * lam * mu * alpha * d
    rhs = (p * lam * mu * alpha * d
           + p * a * mu * d
           + p * a * lam * alpha
           + p * m * alpha * d)
    need(lhs == rhs, 'four-term cross multiplication')
    lprod = lam * mu
    g = gcd(lprod, m)
    nu = (lprod + m) // g
    ell = lprod // g
    need(gcd(nu, ell) == 1 and nu == 731 and a % nu != 0, 'fusion obstruction')
    rho = nu // gcd(a, nu)
    need(rho == 731, 'obstruction order')
    return {'p': p, 'R': r0, 'lambda': lam, 'mu': mu,
            'nu': nu, 'rho': rho}


def main() -> None:
    packets = [independent_r27(p) for p in (73, 1009, 6121, 6841)]
    families = {str(p): residuals(p) for p in (73, 1009, 6121, 6841)}
    for n in range(3, 102, 2):
        need((set((0, 1, n - 1)) == set(range(n))) == (n == 3),
             'three-colour uniqueness')
    report = {
        'status': 'pass',
        'r27_packets': packets,
        'residual_families': families,
        'cross_shell': cross_check(),
        'imports_active_implementation': False,
        'universal_ES_proved': False,
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
