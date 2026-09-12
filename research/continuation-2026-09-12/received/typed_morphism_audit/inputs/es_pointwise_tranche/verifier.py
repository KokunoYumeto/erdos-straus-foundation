#!/usr/bin/env python3
"""Deterministic certificates for the pointwise ES tranche (Python >= 3.9).

No third-party imports; no probable-prime tests; no floating-point inequalities.
Run:
  python3 verifier.py --self-test --anchors --cover-bound 2000000
  python3 verifier.py --self-test --anchors --cover-bound 10000000000
The latter uses about 80 MB for the prime flags, plus the JSON rule objects.
The search certificate is finite: it makes no assertion above 10**10.
"""
from __future__ import annotations
import argparse
import gzip
from fractions import Fraction
import hashlib
import itertools
import json
import math
from pathlib import Path
import sys
import time
from typing import Iterable

HARD = (1, 121, 169, 289, 361, 529)
SHELLS = (11, 19, 23, 39)
ANCHORS = ((11,9), (23,12), (23,18), (19,35), (39,40), (39,50), (39,64))
EXTENSIONS = {11259889:(151,785), 788653441:(7,282469), 1350237001:(3,343397)}
BASE_DIR = Path(__file__).resolve().parent


def require(ok: bool, message: str = 'certificate check failed') -> None:
    if not ok:
        raise ValueError(message)


def primes_to(n: int) -> list[int]:
    if n < 2:
        return []
    flags = bytearray(b'\1') * (n+1)
    flags[:2] = b'\0\0'
    for q in range(2, math.isqrt(n)+1):
        if flags[q]:
            start=q*q
            flags[start:n+1:q] = b'\0' * ((n-start)//q+1)
    return [q for q in range(2,n+1) if flags[q]]


_SMALL_PRIMES = primes_to(300000)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for q in _SMALL_PRIMES:
        if q*q > n:
            return True
        if n % q == 0:
            return n == q
    # Deterministic fallback, used only if the supplied integer is larger.
    q = _SMALL_PRIMES[-1] + 2
    while q*q <= n:
        if n % q == 0:
            return False
        q += 2
    return True


def factor(n: int) -> dict[int,int]:
    require(n >= 1, 'factor expects a positive integer')
    out: dict[int,int] = {}
    for q in _SMALL_PRIMES:
        if q*q > n:
            break
        if n % q == 0:
            e=0
            while n % q == 0:
                n//=q; e+=1
            out[q]=e
    else:
        q=_SMALL_PRIMES[-1]+2
        while q*q <= n:
            if n % q == 0:
                e=0
                while n % q == 0:
                    n//=q; e+=1
                out[q]=e
            q+=2
    if n > 1:
        out[n]=out.get(n,0)+1
    return out


def divisors_from_factor(fs: dict[int,int], square: bool=False) -> list[int]:
    ds=[1]
    for q,e in sorted(fs.items()):
        ds=[d*q**j for d in ds for j in range((2*e if square else e)+1)]
    return sorted(ds)


def positive_chamber(r: int, s: int) -> bool:
    """Exact strict membership in (0,alpha) union (beta,1+sqrt(2))."""
    require(r > 0 and s > 0)
    D=s*s-4*r*s-3*r*r
    low=D>0 and D*D>8*r*r*(r+s)*(r+s)
    below_top=r<=s or (r-s)*(r-s)<2*s*s
    E=3*r*r-4*r*s-s*s
    above_bottom=r>s and (E>=0 or 8*r*r*(r-s)*(r-s)>E*E)
    return low or (below_top and above_bottom)


def in_closure(r: int, s: int) -> bool:
    return (r > 0 and s > 0 and math.gcd(r,s)==1
            and ((3*s <= 2*r <= 4*s) or (r==1 and s>=8)))


def farey_row(depth: int) -> list[tuple[int,int]]:
    row=[(2,1),(3,2)]
    for _ in range(depth):
        new=[]
        for v,w in zip(row,row[1:]):
            new += [v,(v[0]+w[0],v[1]+w[1])]
        row=new+[row[-1]]
    return row


BASE_RAYS = tuple(farey_row(4)+[(1,s) for s in range(8,129)])
BASE_SET = set(BASE_RAYS)


def decode(a: int, u: int) -> tuple[int,int,int]:
    require(a>0 and u>0 and a*a % u==0)
    d=math.gcd(a,u); r=u//d; s=a//d
    require(d % r==0)
    h=d//r
    require(h*r*s==a and h*r*r==u and math.gcd(r,s)==1)
    return h,r,s


def state(p: int, R: int, u: int, channel: str) -> dict:
    require(p>R>0 and R%4==3 and p%4==1 and (p+R)%4==0)
    a=(p+R)//4
    require(math.gcd(a,R)==1)
    h,r,s=decode(a,u)
    if channel=='E':
        require((4*u+1)%R==0 and (p*r+s)%R==0)
        kappa=(p*r+s)//R; lam=None
        ds=(a,h*s*kappa,p*h*r*kappa)
    elif channel=='M':
        require((4*u+p)%R==0 and (r+s)%R==0)
        kappa=None;lam=(r+s)//R
        ds=(a,p*h*s*lam,p*h*r*lam)
    else:
        raise ValueError('unknown channel')
    x,y,z=ds
    require(min(ds)>0 and 4*x*y*z==p*(x*y+x*z+y*z))
    return {'p':p,'R':R,'a':a,'u':u,'channel':channel,'h':h,'r':r,'s':s,
            'kappa':kappa,'lambda':lam,'denominators_raw':list(ds),
            'denominators_increasing':sorted(ds),'positive_chamber':positive_chamber(r,s)}


def middle_states(p: int, R: int) -> list[dict]:
    require(p>R and (p+R)%4==0)
    a=(p+R)//4
    return [state(p,R,u,'M') for u in divisors_from_factor(factor(a),True)
            if (u+a)%R==0]


def ray_states(p: int, r: int, s: int) -> list[dict]:
    require(math.gcd(r,s)==1 and min(r,s)>0)
    m=4*r*s
    return [state(p,R,((p+R)//m)*r*r,'E')
            for R in divisors_from_factor(factor(r*p+s))
            if 0<R<p and (p+R)%m==0]


def first_base_witness(p: int) -> dict | None:
    for R in SHELLS:
        for st in middle_states(p,R):
            if st['positive_chamber']:
                return st
    for r,s in BASE_RAYS:
        ss=ray_states(p,r,s)
        if ss:
            return ss[0]
    return None


def closure_states(p: int) -> Iterable[dict]:
    """Complete terminating enumeration, with no finite Farey-depth cutoff.

    For testing large primes this is deliberately not claimed to be efficient.
    It enumerates at most (p-1)//4 shells, each with explicitly bounded u.
    """
    require(is_prime(p) and p%840 in HARD)
    for R in range(3,p,4):
        a=(p+R)//4
        u0=(3*R-1)//4
        lo=(3*a+1)//2;hi=2*a
        first=lo+(u0-lo)%R
        for u in range(first,hi+1,R):
            if a*a%u==0:
                st=state(p,R,u,'E')
                require(in_closure(st['r'],st['s']))
                yield st
        if R <= (p+8)//23:
            for u in range(u0,a//8+1,R):
                if a%u==0:
                    st=state(p,R,u,'E')
                    require(st['r']==1 and st['s']>=8)
                    yield st


def exterior_hyperbola(p: int, R: int, u: int) -> dict:
    """Forward bijection; its inverse is hyperbola_inverse below."""
    st=state(p,R,u,'E')
    k=(4*u+1)//R;D=(k*p+1)//4
    require(k%4==3 and (k*p+1)%4==0 and u==k*st['a']-D)
    require(D*D%u==0 and math.gcd(k,u)==1)
    return {'p':p,'k':k,'D':D,'u':u}


def hyperbola_inverse(p: int, k: int, D: int, u: int) -> dict:
    require(p%4==1 and k>0 and k%4==3 and D==(k*p+1)//4)
    require(u>0 and D*D%u==0 and (u+D)%k==0)
    require((4*u+1)%k==0)
    R=(4*u+1)//k
    return state(p,R,u,'E')



def closure_states_hyperbola(p: int, cutoff: int) -> list[dict]:
    """Exact disjoint two-pass enumeration of the infinite exterior closure."""
    require(is_prime(p) and p%840 in HARD and 0<=cutoff<p)
    out=[]
    for R in range(3,min(cutoff,p-1)+1,4):
        a=(p+R)//4
        for u in divisors_from_factor(factor(a),True):
            if (4*u+1)%R:continue
            h,r,s=decode(a,u)
            if in_closure(r,s):out.append(state(p,R,u,'E'))
    K=(4*p-3)//(cutoff+1)
    for k in range(3,K+1,4):
        D=(k*p+1)//4
        for u in divisors_from_factor(factor(D),True):
            if (u+D)%k:continue
            R=(4*u+1)//k
            if not cutoff<R<p:continue
            st=hyperbola_inverse(p,k,D,u)
            if in_closure(st['r'],st['s']):out.append(st)
    keys=[(x['R'],x['u']) for x in out]
    require(len(keys)==len(set(keys)))
    return sorted(out,key=lambda x:(x['R'],x['u']))


def anchor_box(R: int, A: int) -> tuple[set[int],list[dict]]:
    """Actual signed exponent box, not generated-subgroup closure."""
    fs=factor(A);qs=list(fs)
    packets=[]
    for es in itertools.product(*(range(-fs[q],fs[q]+1) for q in qs)):
        n=math.prod(q**max(e,0) for q,e in zip(qs,es))
        d=math.prod(q**max(-e,0) for q,e in zip(qs,es))
        require(math.gcd(n,d)==1 and A%(n*d)==0)
        packets.append({'n':n,'d':d,'signed_exponents':list(es),
                        'residue':n*pow(d,-1,R)%R})
    H={z['residue'] for z in packets}
    G={j for j in range(1,R) if math.gcd(j,R)==1}
    require(2*len(H)==len(G) and 1 in H and R-1 not in H)
    require(all(x*y%R in H for x in H for y in H))
    require(all(q%R in H for q in fs))
    return H,packets



def anchor_height(R: int, A: int) -> tuple[Fraction,list[dict]]:
    H,packets=anchor_box(R,A)
    reps=[min((z for z in packets if z['residue']==h),
              key=lambda z:Fraction(z['d'],z['n'])) for h in sorted(H)]
    return max(Fraction(z['d'],z['n']) for z in reps),reps



def variable_anchor_certificate(bound: int = 10000) -> dict:
    """Check the symbolic representative table on a finite prime range.

    The universal argument is the nine-monomial comparison in the manuscript;
    this finite check is not substituted for that argument.
    """
    checked=[]
    for ell in primes_to(bound):
        c=ell%11
        if ell<=3 or c not in (3,4,5,9):continue
        expected_pairs={
            3:[(ell,3),(ell,1),(1,3),(1,3*ell),(3*ell,1)],
            4:[(3*ell,1),(3,1),(ell,1),(ell,3),(3,ell)],
            5:[(1,1),(3,1),(3*ell,1),(ell,1),(ell,3)],
            9:[(1,1),(ell,3),(1,3),(3*ell,1),(ell,1)]
        }[c]
        height,reps=anchor_height(11,3*ell)
        expected_height={3:Fraction(3*ell),4:Fraction(ell,3),
                         5:Fraction(1),9:Fraction(3)}[c]
        require(height==expected_height)
        require([(z['n'],z['d']) for z in reps]==expected_pairs)
        checked.append({'ell':ell,'residue_11':c,
                        'height':[height.numerator,height.denominator]})
    return {'finite_check_bound':bound,'primes_checked':len(checked),
            'H_order':[1,3,4,5,9],
            'minimum_d_over_n_templates':{
                '3':['3/ell','1/ell','3','3*ell','1/(3*ell)'],
                '4':['1/(3*ell)','1/3','1/ell','3/ell','ell/3'],
                '5':['1','1/3','1/(3*ell)','1/ell','3/ell'],
                '9':['1','3/ell','3','1/(3*ell)','1/ell']},
            'checked_instances':checked,
            'nonclaim':'Finite tests do not prove the universal table; see the symbolic proof.'}


def packet_state(p: int, R: int, A: int, t: int, n: int, d: int) -> dict:
    a=(p+R)//4
    require((p+R)%4==0 and a%A==0 and (a//A)%t==0)
    require(min(t,n,d)>0 and A%(n*d)==0 and math.gcd(n,d)==1)
    require((t*n+d)%R==0 and t*n>8*d)
    g=math.gcd(d,t*n)
    r=d//g;s=t*n//g
    require(a%(d*t*n)==0)
    h=a*g*g//(d*t*n)
    st=state(p,R,h*r*r,'M')
    require((st['h'],st['r'],st['s'])==(h,r,s))
    require(8*r<s and st['positive_chamber'])
    st['anchor_packet']={'A':A,'t':t,'n':n,'d':d,'g':g}
    return st


def packet_inverse_fibre(st: dict, A: int) -> list[dict]:
    require(st['channel']=='M')
    p,R,a,r,s=(st[k] for k in ('p','R','a','r','s'))
    require(a%A==0)
    _,packets=anchor_box(R,A)
    out=[]
    for z in packets:
        n,d=z['n'],z['d']
        if (d*s)%(n*r):continue
        t=d*s//(n*r)
        if t<1 or (a//A)%t or t*n<=8*d:continue
        if (t*n+d)%R:continue
        image=packet_state(p,R,A,t,n,d)
        require(image['u']==st['u'])
        out.append(image['anchor_packet'])
    return out


def force_anchor_state(p: int, R: int, A: int) -> dict:
    a=(p+R)//4
    height,reps=anchor_height(R,A);threshold=max(Fraction(1),8*height)
    require((p+R)%4==0 and a%A==0)
    H,_=anchor_box(R,A);b=a//A
    require(b>threshold if b%R not in H else b>threshold*threshold)
    qs=[q for q in factor(b) if q%R not in H]
    require(qs, 'the forcing theorem requires an actual non-H prime factor')
    if b%R not in H:t=b
    else:
        q=min(qs)
        t=q if q>threshold else b//q
    require(b%t==0 and t>threshold and t%R not in H)
    target=(-pow(t,-1,R))%R
    z=next(z for z in reps if z['residue']==target)
    return packet_state(p,R,A,t,z['n'],z['d'])


def enumerate_anchor_exceptions() -> list[dict]:
    rows=[]
    for R,A in ANCHORS:
        H,packets=anchor_box(R,A)
        height,reps=anchor_height(R,A);threshold=max(Fraction(1),8*height)
        b_bound=math.floor(threshold*threshold)
        exceptions=[];count=nr_count=0
        for b in range(1,b_bound+1):
            a=A*b;p=4*a-R
            if p<=R or p%840 not in HARD or not is_prime(p):continue
            count+=1;fs=factor(a)
            if all(q%R in H for q in fs):continue
            nr_count+=1;ss=middle_states(p,R)
            if any(st['positive_chamber'] for st in ss):continue
            rep=first_base_witness(p)
            require(rep is not None, 'unrepaired angular exception')
            exceptions.append({'p':p,'a':a,'factorization_a':fs,
                               'middle_states':ss,'hybrid_repair':rep})
        rows.append({'R':R,'A':A,'H':sorted(H),'signed_box':packets,
                     'height':[height.numerator,height.denominator],'optimal_representatives':reps,
                     'b_bound':b_bound,'a_bound':A*b_bound,'p_bound':4*A*b_bound-R,
                     'hard_primes_tested':count,'with_nonH_prime_factor':nr_count,
                     'exceptions':exceptions})
    return rows


def hand_exception_tables() -> list[dict]:
    specs=[(11,9,[2,19],[171,513,3249,9747]),
           (23,12,[5],[60,300]),(23,18,[17],[306,5202])]
    out=[]
    for R,A,bad_expected,exception_a in specs:
        H,packets=anchor_box(R,A); tests=[];bad=[]
        for q in primes_to(8*A):
            if math.gcd(q,R)>1 or q%R in H:continue
            hits=[]
            for z in packets:
                n,d=z['n'],z['d']
                if (q*n+d)%R==0:
                    for rr,ss in ((q*n,d),(d,q*n)):
                        if positive_chamber(rr,ss):hits.append([n,d,rr,ss])
            if not hits:bad.append(q)
            tests.append({'q':q,'positive_packets':hits})
        require(bad==bad_expected)
        exceptional=[]
        for a in exception_a:
            p=4*a-R
            ss=middle_states(p,R)
            require(not any(st['positive_chamber'] for st in ss))
            exceptional.append({'a':a,'p':p,'factorization_p':factor(p),
                                'hard_prime':p%840 in HARD and is_prime(p),
                                'middle_states':ss})
        out.append({'R':R,'A':A,'bad_small_primes':bad,'small_prime_tests':tests,
                    'exceptional_a':exceptional})
    return out


def extension_certificates() -> list[dict]:
    rows=[]
    for p,(R,s) in sorted(EXTENSIONS.items()):
        require(is_prime(p) and p%840 in HARD)
        require((p+R)%(4*s)==0)
        st=state(p,R,(p+R)//(4*s),'E')
        require(st['r']==1 and st['s']==s and in_closure(1,s))
        boxes=[]
        for rr in SHELLS:
            a=(p+rr)//4;ss=middle_states(p,rr)
            require(not any(t['positive_chamber'] for t in ss))
            boxes.append({'R':rr,'a':a,'factorization_a':factor(a),'middle_states':ss})
        rays=[]
        for r0,s0 in BASE_RAYS:
            fs=factor(r0*p+s0)
            ds=divisors_from_factor(fs)
            require(not [q for q in ds if q<p and (p+q)%(4*r0*s0)==0])
            rays.append({'r':r0,'s':s0,'L':r0*p+s0,'factorization_L':fs})
        support=[]
        a3=(p+3)//4
        a3_split=all(q%3==1 for q in factor(a3))
        for rr,A in ANCHORS:
            a=(p+rr)//4
            if a%A==0:
                H,_=anchor_box(rr,A)
                require(all(q%rr in H for q in factor(a)))
                support.append({'R':rr,'A':A,'factorization_a':factor(a)})
        rows.append({'p':p,'residue_840':p%840,'p_minus_one_factorization':factor(p-1),
                     'extension_state':st,'middle_shell_failures':boxes,
                     'base_ray_failures':rays,'a3_factorization':factor(a3),'a3_all_split':a3_split,
                     'applicable_support_obstructions':support})
    return rows


def saturation_obstruction() -> dict:
    p=2016361;R=11;a=(p+R)//4
    require(is_prime(p) and p%840 in HARD and factor(a)=={3:1,113:1,1487:1})
    ss=middle_states(p,R)
    require(len(ss)==2 and not any(st['positive_chamber'] for st in ss))
    require(sorted((st['r'],st['s']) for st in ss)==[(339,1487),(1487,339)])
    packets=[]
    for ex in itertools.product((-1,0,1),repeat=3):
        residue=1
        for q,e in zip((3,113,1487),ex):residue=residue*pow(q,e,R)%R
        if residue==R-1:packets.append(list(ex))
    require(packets==[[-1,-1,1],[1,1,-1]])
    return {'p':p,'R':R,'a':a,'factorization_a':factor(a),
            'prime_1487_nonH':1487%R,'available_signed_exponents':[-1,0,1],
            'target_exponent_vectors':packets,'middle_states':ss,
            'separate_hybrid_witness':first_base_witness(p)}


def hard_prime_flags(bound: int) -> tuple[bytearray,int]:
    """One flag for 840*k+c, ordered by k then the six increasing c's."""
    require(bound>=2)
    K=bound//840
    flags=bytearray(b'\1')*(6*(K+1))
    for j,c in enumerate(HARD):
        if c<2:flags[j]=0
        for k in range(max(0,(bound-c)//840+1),K+1):flags[6*k+j]=0
    for q in primes_to(math.isqrt(bound)):
        if 840%q==0:continue
        inv=pow(840,-1,q)
        for j,c in enumerate(HARD):
            root=(-c*inv)%q
            lo=max(0,(q*q-c+839)//840)
            first=lo+(root-lo)%q
            last=(bound-c)//840
            if first<=last:
                cnt=(last-first)//q+1
                flags[6*first+j:6*last+j+1:6*q]=b'\0'*cnt
    return flags,sum(flags)


def mark_progression(flags: bytearray, bound: int, residue: int, modulus: int,
                     low: int, high: int | None) -> None:
    require(modulus>=1)
    hi=min(bound,high if high is not None else bound);lo=max(2,low)
    if lo>hi:return
    g=math.gcd(840,modulus);period=modulus//g
    inv=pow(840//g,-1,period) if period>1 else 0
    for j,c in enumerate(HARD):
        if (residue-c)%g:continue
        root=(((residue-c)//g)*inv)%period if period>1 else 0
        kl=max(0,(lo-c+839)//840);kh=(hi-c)//840
        first=kl+(root-kl)%period
        if first<=kh:
            cnt=(kh-first)//period+1
            flags[6*first+j:6*kh+j+1:6*period]=b'\0'*cnt


def cover_verify(bound: int, path: Path) -> dict:
    start=time.monotonic()
    with gzip.open(path,'rt',encoding='utf8') as f:cert=json.load(f)
    require(cert['schema']=='es-pointwise-cover-v1' and cert['hard_residues']==list(HARD))
    require(2<=bound<=cert['bound'])
    flags,count=hard_prime_flags(bound)
    if bound==cert['bound']:require(count==cert['hard_prime_count'])
    if bound==2000000:require(count==4519)
    print(f'Prime sieve: {count} hard primes through {bound}',flush=True)
    extras=[];ecount=mcount=0
    for r,s,R in cert['E_rules']:
        require(in_closure(r,s) and positive_chamber(r,s) and R>0 and R%4==3)
        m=4*r*s
        require(math.gcd(m*r,R)==1)
        t=(-s*pow(m*r,-1,R))%R
        residue=(-R+m*t)%(m*R)
        require((residue+R)%m==0 and (r*residue+s)%R==0)
        if (r,s) in BASE_SET:
            mark_progression(flags,bound,residue,m*R,R+1,None)
        else:
            require((r,s) in {(1,x[1]) for x in EXTENSIONS.values()})
            extras.append((residue,m*R,R+1,None))
        ecount+=1
    for R,u,d,pl,ph0,ph1 in cert['M_rules']:
        require(R in SHELLS and min(u,d)>0 and d*d%u==0 and math.gcd(d,R)==1)
        require(pl>0 or (ph0>0 and ph1>=ph0))
        a0=d*((-u*pow(d,-1,R))%R)
        modulus=4*d*R;residue=(4*a0-R)%modulus
        for p in (pl,ph0,ph1):
            if not p:continue
            require(p>R and (p+R)%4==0)
            a=(p+R)//4
            require(a%d==0 and (u+a)%R==0 and positive_chamber(u,a))
        if pl:
            require(u<(pl+R)//4)  # lower component, decreasing in p
            mark_progression(flags,bound,residue,modulus,pl,None)
        if ph0:
            require(u>(ph1+R)//4 and ph1>=ph0) # upper component throughout
            mark_progression(flags,bound,residue,modulus,ph0,ph1)
        mcount+=1
    remaining=[840*(i//6)+HARD[i%6] for i,v in enumerate(flags) if v]
    expected=[p for p in cert['base_hybrid_misses'] if p<=bound]
    require(remaining==expected,f'base covering gap: {remaining[:20]}')
    # Exhaustiveness at the three gaps is independently established by
    # extension_certificates(), not merely by noncoverage by these rules.
    for rule in extras:mark_progression(flags,bound,*rule)
    require(not any(flags),'extended covering gap')
    answer={'bound':bound,'hard_prime_count':count,'base_hybrid_misses':remaining,
            'exterior_rules_checked':ecount,'middle_rules_checked':mcount,
            'uncovered_after_extensions':0,'seconds':round(time.monotonic()-start,3)}
    print(json.dumps(answer,sort_keys=True),flush=True)
    return answer



def witness_from_cover(p: int, path: Path) -> dict | None:
    require(is_prime(p) and p%840 in HARD)
    with gzip.open(path,'rt',encoding='utf8') as f:cert=json.load(f)
    for index,(r,s,R) in enumerate(cert['E_rules']):
        m=4*r*s
        if p>R and (p+R)%m==0 and (p*r+s)%R==0:
            st=state(p,R,((p+R)//m)*r*r,'E')
            st['certificate_rule']={'channel':'E','index':index}
            return st
    for index,(R,u,d,pl,ph0,ph1) in enumerate(cert['M_rules']):
        if p<=R:continue
        a=(p+R)//4
        if a%d or (u+a)%R:continue
        if (pl and p>=pl) or (ph0 and ph0<=p<=ph1):
            st=state(p,R,u,'M')
            require(st['positive_chamber'])
            st['certificate_rule']={'channel':'M','index':index}
            return st
    return None


def self_tests() -> dict:
    require(len(BASE_RAYS)==138 and len(BASE_SET)==138)
    require(positive_chamber(1,8) and not positive_chamber(1,7))
    require(all(in_closure(*rs) and positive_chamber(*rs) for rs in BASE_RAYS))
    # Exact normalization, involution, and hyperbola inverse tests on all
    # bounded states at these small hard primes (not a coverage assumption).
    states=0;packets_checked=0
    for p in (1009,1201,2521,3361):
        require(is_prime(p) and p%840 in HARD)
        for R in range(3,p,4):
            a=(p+R)//4
            for u in divisors_from_factor(factor(a),True):
                h,r,s=decode(a,u)
                require((r*a)==(s*u))
                if (4*u+1)%R==0:
                    st=state(p,R,u,'E');co=exterior_hyperbola(p,R,u)
                    require(hyperbola_inverse(**co)==st);states+=1
                if (4*u+p)%R==0:
                    st=state(p,R,u,'M');rev=state(p,R,a*a//u,'M')
                    require((rev['r'],rev['s'])==(s,r))
                    require(rev['denominators_raw']==[st['denominators_raw'][0],
                                                     st['denominators_raw'][2],
                                                     st['denominators_raw'][1]])
                    states+=1
    for p in (1009,1201,2521):
        direct=sorted(closure_states(p),key=lambda x:(x['R'],x['u']))
        require(closure_states_hyperbola(p,math.isqrt(p))==direct)
    # Packet map/inverse/collision tests, including nontrivial gcds.
    for R,A in ANCHORS:
        H,box=anchor_box(R,A)
        tested=0
        height,_=anchor_height(R,A);limit=math.floor(max(Fraction(1),8*height)**2)
        for b in range(limit+1,limit+300):
            a=A*b;p=4*a-R
            if math.gcd(a,R)>1 or all(q%R in H for q in factor(b)):continue
            st=force_anchor_state(p,R,A)
            fibre=packet_inverse_fibre(st,A)
            require(st['anchor_packet'] in fibre)
            for x,y in itertools.combinations(fibre,2):
                require(x['t']*x['n']*y['d']==y['t']*y['n']*x['d'])
            packets_checked+=1;tested+=1
            if tested==12:break
        require(tested==12)
    # Independently compare the compact hard-prime sieve with ordinary sieve.
    fs,n=hard_prime_flags(2000000)
    actual=[840*(i//6)+HARD[i%6] for i,x in enumerate(fs) if x]
    expected=[p for p in primes_to(2000000) if p%840 in HARD]
    require(actual==expected and n==4519)
    return {'bounded_states_tested':states,'anchor_packet_tests':packets_checked,
            'hard_sieves_agree_through':2000000}


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value,indent=2,sort_keys=False)+'\n',encoding='utf8')


def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--self-test',action='store_true')
    ap.add_argument('--anchors',action='store_true')
    ap.add_argument('--cover-bound',type=int)
    ap.add_argument('--witness',type=int,help='reconstruct a fully marked state from a valid stored rule')
    ap.add_argument('--closure-prime',type=int,help='exhaustive infinite-closure shell enumeration')
    ap.add_argument('--out',type=Path,default=BASE_DIR/'regenerated')
    ap.add_argument('--rules',type=Path,default=BASE_DIR/'cover_rules.json.gz')
    args=ap.parse_args()
    if not(args.self_test or args.anchors or args.cover_bound or args.closure_prime or args.witness):
        ap.error('select --self-test, --anchors, --cover-bound, or --closure-prime')
    args.out.mkdir(parents=True,exist_ok=True)
    results={}
    if args.self_test:
        results['self_test']=self_tests()
        write_json(args.out/'hand_exception_tables.json',hand_exception_tables())
        write_json(args.out/'saturation_obstruction.json',saturation_obstruction())
        write_json(args.out/'variable_anchor_certificates.json',variable_anchor_certificate())
        write_json(args.out/'closure_extensions.json',extension_certificates())
        print('Self-tests, hand tables, extension failures and repairs verified.',flush=True)
    if args.anchors:
        rows=enumerate_anchor_exceptions()
        require([[z['p'] for z in row['exceptions']] for row in rows]
                ==[[],[],[1201],[837601],[],[3361],[]])
        write_json(args.out/'anchor_certificates.json',rows)
        results['anchors']=[{k:row[k] for k in ('R','A','hard_primes_tested','with_nonH_prime_factor')}
                            | {'exception_primes':[z['p'] for z in row['exceptions']]} for row in rows]
        print('All seven anchor exception boxes exhausted.',flush=True)
    if args.cover_bound:
        results['cover']=cover_verify(args.cover_bound,args.rules)
    if args.witness:
        st=witness_from_cover(args.witness,args.rules)
        write_json(args.out/f'witness_{args.witness}.json',st)
        results['witness']=st if st is not None else 'No stored rule applies; not a nonexistence certificate.'
    if args.closure_prime:
        p=args.closure_prime;ss=list(closure_states(p))
        mids=[st for R in SHELLS for st in middle_states(p,R) if st['positive_chamber']]
        write_json(args.out/f'closure_{p}.json',{'p':p,'exterior_closure_states':ss,
                    'positive_middle_fixed_shell_states':mids})
        results['closure']={'p':p,'exterior_states':len(ss),'middle_states':len(mids)}
    write_json(args.out/'verification_summary.json',results)
    print(json.dumps(results,indent=2),flush=True)


if __name__=='__main__':
    main()
