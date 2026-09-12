"""Exact finite regressions from the Boolean investigation; standard library only.

Read before execution. No files are changed, no imports run project code, and the
output does not claim all-prime coverage. Bounds are stated in the output.
"""
from math import gcd, isqrt
from fractions import Fraction
from itertools import permutations
import json


def factors(n):
    out = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def divisors(n):
    result = [1]
    for q, v in factors(n).items():
        result = [d * q**e for d in result for e in range(v + 1)]
    return sorted(result)


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def short_pairs(p, degree):
    result = []
    for r in range(1, isqrt(p) + 1):
        for s in range(1, isqrt(p) + 1):
            if gcd(r, s) != 1:
                continue
            value = r**degree - r**(degree//2) * s**(degree//2) + s**degree
            if value % p == 0:
                result.append([r, s, value//p])
    return result


def shell(p, a):
    R = 4*a-p
    ds = divisors(a*a)
    E = [u for u in ds if (4*u+1) % R == 0]
    M = [u for u in ds if (4*u+p) % R == 0]
    pairs = [(m, r) for m in divisors(p*a) for r in divisors(p*a) if (m+r)%R == 0]
    return {'p':p,'a':a,'R':R,'E':E,'M':M,
            'residues':sorted({u%R for u in ds}),'T':len(pairs)}


def reconstruct(p,a,u,eps):
    R=4*a-p
    g=gcd(a,u)
    A,B,D=a//g,u//g,g*g//u
    assert g*g%u==0 and a==A*B*D and u==B*B*D
    C, rem=divmod(A+p**(1-eps)*B,R)
    assert rem==0
    xyz=(a,p**eps*A*C*D,p*B*C*D)
    assert sum((Fraction(1,d) for d in xyz),Fraction(0))==Fraction(4,p)
    j=(R-3)//4
    c=(A-1)*(p-1)**2//4+(p-1)*j+2*(B-1)+eps
    return {'p':p,'a':a,'u':u,'eps':eps,'ABCD':[A,B,C,D],'c':c,'xyz':xyz}


def first_layer_hits(p):
    result=[]
    for j in range((p-1)//4):
        R=4*j+3
        a=(p+R)//4
        for B in divisors(a):
            for eps in (0,1):
                if (1+p**(1-eps)*B)%R==0:
                    result.append([j,B,eps])
    return result


def permutation_fibres(p):
    """Exhaust every full-range divisor hit and both proved fibre maps."""
    h=(p-1)//12

    def inverse(triple, full):
        a,y,z=triple
        R,S=4*a-p,p*a
        d=R*y-S
        assert d>0 and S*S%d==0
        i=0
        v=d
        while v%p==0:
            i+=1
            v//=p
        assert i in (0,1)
        eps=i
        u=a*a//d if i==0 else p*a*a//d
        hit=reconstruct(p,a,u,eps)
        assert tuple(hit['xyz'])==tuple(triple)
        if full:
            A,B,C,D=hit['ABCD']
            return (A-1)*108*h*h+18*h*((R-3)//4)+2*(B-1)+eps
        return hit['c']

    full={}
    for a in range(3*h+1,9*h+1):
        R=4*a-p
        for u in divisors(a*a):
            for eps in (0,1):
                if (4*u+p**eps)%R==0:
                    triple=tuple(reconstruct(p,a,u,eps)['xyz'])
                    c=inverse(triple,True)
                    assert c not in full
                    full[c]=triple
    fibres={}
    minimal={}
    for c,triple in full.items():
        a,y,z=sorted(triple)
        assert p<4*a and 2*a<p
        d=(4*a-p)*y-p*a
        if d%(p*p)==0:
            y,z=z,y
        triple_min=(a,y,z)
        c_min=inverse(triple_min,False)
        fibres.setdefault(c_min,set()).add(c)
        minimal[c_min]=triple_min
    for c_min,triple in minimal.items():
        recovered=set()
        for b,c,d in set(permutations(triple)):
            if not (3*h+1<=b<=9*h):
                continue
            residual=(4*b-p)*c-p*b
            if residual%(p*p)==0:
                continue
            recovered.add(inverse((b,c,d),True))
        assert recovered==fibres[c_min]
    return {'p':p,'full_hits':len(full),'minimal_half_hits':len(minimal),
            'all_exact_fibres_verified':True,
            'fibre_sizes':sorted(len(values) for values in fibres.values())}


if __name__=='__main__':
    out={
      'scope':'Exact finite fixtures only; no all-prime verification and no publication.',
      'prime_checks':{p:prime(p) for p in (37,61,73,97,193,197,181,2521,3361)},
      'short_Phi12':{p:short_pairs(p,4) for p in (37,61,73,193,2521)},
      'short_Phi24':{73:short_pairs(73,8)},
      'shells':[shell(p,a) for p,a in ((37,18),(61,22),(193,50),(2521,636),(3361,847))],
      'witnesses':[reconstruct(*data) for data in ((193,50,250,0),(2521,636,50562,1),(3361,841,29,0))],
      'H1_2521':first_layer_hits(2521),
      'quadratic_181_at_2521':{'square':88**2,'quotient':(88**2-181)//2521,'legendre':pow(181,1260,2521)},
      'least_nonresidue_3361':next(t for t in range(1,3361) if pow(t,1680,3361)==3360),
      'negative_jacobi_at_3361_shell':[u for u in divisors(847**2) if u%3==2],
      'Phi12_24':{'value':24**4-24**2+1,'factorization':factors(24**4-24**2+1)},
      'permutation_fibres':[permutation_fibres(p) for p in (13,37,61)],
    }
    print(json.dumps(out,indent=2))
