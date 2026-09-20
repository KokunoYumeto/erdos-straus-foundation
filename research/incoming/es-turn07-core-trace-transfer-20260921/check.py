#!/usr/bin/env python3
"""Portable exact replay for the preprint. Standard library; no occupancy claim."""
from fractions import Fraction as F
from math import gcd, isqrt
from collections import defaultdict
import hashlib
import json

checks = 0

def test(ok, context=""):
    global checks
    checks += 1
    if not ok:
        raise ArithmeticError(context)

def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))

def factor(n):
    out = {}; d = 2
    while d*d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1; n //= d
        d += 1
    if n > 1: out[n] = 1
    return out

def square_divisors(n):
    ds = [1]
    for q, e in factor(n).items():
        ds = [x*q**k for x in ds for k in range(2*e+1)]
    return sorted(ds)

def sf(n):
    result = 1
    for q, e in factor(n).items():
        if e % 2: result *= q
    return result

def source(p, a, u, tag):
    R = 4*a-p
    test(prime(p) and p % 4 == 1 and p < 4*a < 2*p)
    test(u > 0 and a*a % u == 0)
    if tag == 'E':
        b, c = a*a//u, p*p*u
    else:
        b, c = p*a*a//u, p*u
    test(b*c == (p*a)**2 and (p*a+b)**2 % R == 0)
    y, z = F(p*a+b, R), F(p*a+c, R)
    test((y+z).denominator == 1 and y.denominator == z.denominator)
    test(F(1, a)+1/y+1/z == F(4, p))
    return R, y, z

def middle(p, Q, U):
    j = (Q+1)//4
    test(prime(p) and p % 4 == 1 and 3 <= Q < p and Q % 4 == 3)
    test(U in square_divisors(j) and (p+4*U) % Q == 0)
    R = (p+4*U)//Q; a = (p+R)//4; g = gcd(j, U)
    h, r, la = g*g//U, U//g, j//g
    s = R*la-r
    test(0 < R < p and R % 4 == 3 and min(h, r, s, la) > 0)
    test(a == h*r*s and U == h*r*r and gcd(r, s) == 1)
    test(r+s == R*la and j == h*r*la and a == j*R-U)
    xyz = (a, p*h*s*la, p*h*r*la)
    test(sum((F(1, x) for x in xyz), F()) == F(4, p))
    test(F(p*a*a, R*xyz[1]-p*a) == U)
    return xyz

def finite(A, B):
    out = defaultdict(list); AB = A*B
    H = max(B*(A-1)**2-A, A*(B-1)**2-B)
    for n in range(1, AB):
        for k in range(1, (AB-1)//n+1):
            num = B*k+A*n-2*AB; den = AB-n*k
            if num <= 0 or num % den: continue
            Q = num//den
            if Q <= max(A, B) or Q % 4 != 3: continue
            j = (Q+1)//4
            U, V = F(B+n*Q, A), F(A+k*Q, 16*B)
            if U.denominator != 1 or V.denominator != 1: continue
            test(U*V == j*j and Q <= H)
            out[j].append(int(U))
    return out

def classified(A, B, j, finite_words):
    values = []
    for u in (F(B, A), F(4*B*j, A), F(16*B*j*j, A)):
        if u.denominator == 1 and u > 0 and j*j % int(u) == 0:
            values.append(int(u))
    values += finite_words.get(j, [])
    test(len(set(values)) == len(values))
    return sorted(values)

def main():
    digest = hashlib.sha256(); boxes = 0
    for A in range(1, 25):
        for B in range(1, 25):
            tab = finite(A, B)
            for j in range(1, 501):
                Q = 4*j-1
                direct = [u for u in square_divisors(j) if (A*u-B) % Q == 0]
                if Q > max(A, B): test(direct == classified(A, B, j, tab))
                digest.update((json.dumps([A,B,j,direct], separators=(',',':'))+'\n').encode())
                boxes += 1
    repairs = [
        (1009,321,9,'M',11,9,(276,92828,3027)),
        (12049,3064,24512,'E',23,18,(3144,12627352,72294)),
        (2377702849,594440928,167186511,'E',503,3969,
         (595607481,44958019189187726,299590558974)),
    ]
    for p,a,u,tag,Q,U,expected in repairs:
        R,y,z = source(p,a,u,tag)
        test(y.denominator > 1 and sf(R) == Q and Q < R)
        test(middle(p,Q,U) == expected)
    test(prime(2064031) and 594440928 == 288*2064031)
    test([u for u in square_divisors(126) if (9*u-8) % 503 == 0] == [3969])
    test(503 == max(8*8**2-9,9*7**2-8))
    R,y,z = source(9601,2956,8,'M')
    test(prime(739) and R == 2223 and sf(R) == 247 and y.denominator == 3)
    test(all((4*u+1) % R and (2956+u) % R for u in square_divisors(2956)))
    for Q in (3,19,39,247,507,3211):
        test(9633 % Q == 0)
        test(not any((9601+4*u) % Q == 0 for u in square_divisors((Q+1)//4)))
    test(middle(9601,519,65) == (2405,46180810,1248130))
    test(all((4*u+1) % 275 and (321+u) % 275 for u in square_divisors(321)))
    # Direct, original-box validation of every c=1,2,3,6 candidate through 1000.
    transfers = 0
    for p in range(25,1001,24):
        if not prime(p): continue
        for c in (1,2,3,6):
            for a in range(p//4+1,(p-1)//2+1):
                if a % c: continue
                q = a//c
                if not prime(q) or gcd(c,q) != 1: continue
                R=4*a-p; Q=sf(R); j=(Q+1)//4
                for u in square_divisors(a):
                    for tag, n in (('E',4*u+1),('M',a+u)):
                        if n*n % R: continue
                        source(p,a,u,tag); test(j % c == 0)
                        if tag == 'E':
                            test(u % q == 0 and u % (q*q) != 0)
                            d=u//q; test(c*c % d == 0 and c*j % d == 0)
                            U=c*j//d
                        else:
                            d=u if u % q else a*a//u; test(c*c % d == 0); U=d
                        middle(p,Q,U); transfers += 1
    print(json.dumps({'success':True,'checks':checks,'capacity_boxes':boxes,
          'capacity_bound':[24,24,500],'capacity_digest':digest.hexdigest(),
          'core_trace_prime_bound':1000,'core_transfers':transfers,
          'universal_ES_proved':False},indent=2))

if __name__ == '__main__': main()
