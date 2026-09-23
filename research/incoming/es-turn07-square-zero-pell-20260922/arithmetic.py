#!/usr/bin/env python3
"""Exact original ES trace boxes, square-zero defects and factor-sum returns.
Python >=3.9, standard library only. No global success assertion.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd, isqrt, prod
import json
from pathlib import Path


def need(condition: bool, message: str = 'verification failure') -> None:
    if not condition:
        raise ValueError(message)


def dump(path, obj):
    Path(path).write_bytes((json.dumps(obj, indent=2, sort_keys=True) + '\n').encode('utf-8'))


def sieve(n: int) -> bytearray:
    need(n >= 1)
    a = bytearray(b'\1') * (n+1); a[0:2] = b'\0\0'
    for q in range(2, isqrt(n)+1):
        if a[q]:
            a[q*q::q] = b'\0' * ((n-q*q)//q+1)
    return a


def spf_table(n: int):
    a = list(range(n+1))
    for q in range(2, isqrt(n)+1):
        if a[q] == q:
            for k in range(q*q, n+1, q):
                if a[k] == k: a[k] = q
    return a


def factor(n: int, spf=None) -> dict[int,int]:
    need(n >= 1)
    ans = {}
    if spf is not None and n < len(spf):
        while n > 1:
            q = spf[n]; e = 0
            while n % q == 0: n //= q; e += 1
            ans[q] = e
        return ans
    q = 2
    while q*q <= n:
        if n % q == 0:
            e = 0
            while n % q == 0: n //= q; e += 1
            ans[q] = e
        q = 3 if q == 2 else q + 2
    if n > 1: ans[n] = 1
    return ans


def is_prime(n: int) -> bool:
    if n < 2: return False
    if n % 2 == 0: return n == 2
    return all(n % q for q in range(3, isqrt(n)+1, 2))


def divs_f(f: dict[int,int]):
    ds = [1]
    for q,e in f.items(): ds = [d*q**j for d in ds for j in range(e+1)]
    return sorted(ds)


def divisors(n: int): return divs_f(factor(n))


def K(n: int) -> int:
    return prod(q**((e+1)//2) for q,e in factor(n).items())


def residual_parts(R: int):
    f = factor(R)
    D = prod(q**(e//2) for q,e in f.items())
    delta = R//(D*D)
    return R//D, D, delta


def order(a: int, m: int) -> int:
    need(m > 1 and gcd(a,m) == 1)
    x = 1
    for n in range(1, m+1):
        x = x*a % m
        if x == 1: return n
    raise ValueError('unit order not found')


def frac(x):
    z = Fraction(x)
    return [z.numerator, z.denominator]


def state(p: int, a: int, u: int, channel: str, validate_prime=False):
    need(p > 1 and p % 4 == 1 and p < 4*a < 2*p and gcd(p,a)==1)
    need(channel in ('E','M') and u > 0 and a*a % u == 0)
    if validate_prime: need(is_prime(p),'p is not prime')
    R = 4*a-p; g = gcd(a,u); h=g*g//u; r=u//g; s=a//g
    need(h*r*s == a and h*r*r == u and gcd(r,s)==1)
    if channel == 'E':
        t = Fraction(p*r+s,R); tails = (h*s*t,p*h*r*t); G=4*u+1
    else:
        t = Fraction(r+s,R); tails = (p*h*s*t,p*h*r*t); G=p+4*u
    need(sum((1/Fraction(v) for v in (a,*tails)),Fraction()) == Fraction(4,p))
    k,D,delta = residual_parts(R)
    zz = (pow(p, int(channel=='E'), R)*u*pow(a,-1,R))%R
    trace = (zz+1)%k == 0
    need(trace == (G*G%R==0))
    c = ((zz+1)//k)%D if trace else None
    d = R//gcd(R,G)
    if trace: need(d == D//gcd(D,c))
    fa = factor(a); fu = factor(u)
    record = dict(p=p,a=a,R=R,u=u,channel=channel,h=h,r=r,s=s,
        quotient_name='kappa' if channel=='E' else 'lambda', quotient=frac(t),
        denominators=[frac(a),*[frac(v) for v in tails]],
        trace=trace,full=G%R==0,tail_sum=frac(sum(tails)),
        K=k,D=D,delta=delta,defect=c,common_denominator=d,
        exponents=[dict(prime=q,e=e,f=fu.get(q,0),beta=fu.get(q,0)-e) for q,e in fa.items()])
    return record


def decode_trace(p: int,a: int,y,z):
    """Decode an actually ordered rational pair. No unconstrained orientation bit."""
    y,z=Fraction(y),Fraction(z)
    need(p%4==1 and is_prime(p) and p<4*a<2*p and gcd(p,a)==1 and min(y,z)>0)
    need(Fraction(1,a)+1/y+1/z==Fraction(4,p) and (y+z).denominator==1)
    R=4*a-p; b=R*y-p*a; c=R*z-p*a
    need(b.denominator==c.denominator==1 and b*c==(p*a)**2 and min(b,c)>0)
    b,c=int(b),int(c)
    def valuation(x):
        n=0
        while x%p==0:x//=p;n+=1
        return n
    v=(valuation(b),valuation(c));swap=False
    if v==(0,2):channel='E';u=a*a//b
    elif v==(2,0):channel='E';u=a*a//c;swap=True
    elif v==(1,1):channel='M';u=p*a*a//b
    else:raise ValueError('p valuation not in the prime-source domain')
    rec=state(p,a,u,channel)
    tails=[Fraction(*t) for t in rec['denominators'][1:]]
    if swap:tails.reverse()
    need(tails==[y,z])
    return dict(state=rec,exterior_swap=swap,ordered_input=[frac(a),frac(y),frac(z)])


def full_deletions(rec, mode='word'):
    need(rec['trace'])
    R=rec['R']; d=rec['common_denominator']
    m=4*K(rec['u']) if mode=='word' else 4*rec['r']*rec['s']
    return [k for k in divisors(R) if k % d == 0 and k % m == 1]


def mixed_combine(records, coefficients):
    need(len(records)==len(coefficients) and len(records)>0)
    p,a,R = (records[0][x] for x in ('p','a','R'))
    need(all(t['trace'] and (t['p'],t['a'],t['R'])==(p,a,R) for t in records))
    total=sum(coefficients); eta=sum(n*(t['channel']=='E') for n,t in zip(coefficients,records))
    need(total%2==1 and eta in (0,1),'wrong sum or channel exponent')
    u=Fraction(a)**(1-total)
    for n,t in zip(coefficients,records): u *= Fraction(t['u'])**n
    need(u.denominator==1 and u>0 and a*a%u.numerator==0,'outside original exponent box')
    out=state(p,a,u.numerator,'E' if eta else 'M')
    need(out['trace'])
    need(out['defect']==sum(n*t['defect'] for n,t in zip(coefficients,records))%out['D'])
    return out


def neutral_line(rec, gamma):
    need(rec['trace'])
    ex=rec['exponents']; need(len(ex)==len(gamma))
    R,k,D = rec['R'],rec['K'],rec['D']
    v=1; lower=None; upper=None
    for qd,gam in zip(ex,gamma):
        v=v*pow(qd['prime'],gam,R)%R
        b,e=qd['beta'],qd['e']
        if gam>0: lo=-((-(-e-b))//gam); hi=(e-b)//gam
        elif gam<0:
            vgam=-gam; lo=-((-(b-e))//vgam); hi=(b+e)//vgam
        else: continue
        lower=lo if lower is None else max(lower,lo)
        upper=hi if upper is None else min(upper,hi)
    need(v%k==1 and lower is not None,'not a nonzero coarse-neutral direction')
    lam=((v-1)//k)%D
    vals=[]
    for t in range(lower,upper+1):
        u=prod(qd['prime']**(qd['e']+qd['beta']+t*g) for qd,g in zip(ex,gamma))
        rr=state(rec['p'],rec['a'],u,rec['channel'])
        need(rr['trace'] and rr['defect']==(rec['defect']-lam*t)%D)
        vals.append(dict(t=t,u=u,defect=rr['defect'],full=rr['full']))
    gg=gcd(lam,D); period=D//gg
    solution=None if rec['defect']%gg else ((rec['defect']//gg)*pow(lam//gg,-1,period))%period if period>1 else 0
    predicted=[] if solution is None else [t for t in range(lower,upper+1) if (t-solution)%period==0]
    need(predicted==[x['t'] for x in vals if x['full']])
    return dict(gamma=gamma,interval=[lower,upper],lambda_direction=lam,gcd=gg,
                period=period,solution_residue=solution,points=vals)


def convolution(D, factors):
    acc=[0]*D; acc[0]=1
    for lam,N in factors:
        out=[0]*D
        for c,n in enumerate(acc):
            if n:
                for t in range(N): out[(c+lam*t)%D]+=n
        acc=out
    return acc


def coefficient_stabilizer(D,factors):
    good=[]
    for k in range(D):
        if all((k*l)%D==0 or (k*l*N)%D!=0 for l,N in factors): good.append(k)
    gg=D
    for k in good: gg=gcd(gg,k)
    return list(range(0,D,D//gg)),good


def trace_tiles(p,a):
    R=4*a-p; k,D,delta=residual_parts(R); fa=factor(a)
    qs=list(fa); es=list(fa.values()); blocks=[]
    for q,e in zip(qs,es):
        o=order(q,k); by={}
        for beta in range(-e,e+1): by.setdefault(beta%o,[]).append(beta)
        lam=((pow(q,o,R)-1)//k)%D
        blocks.append([dict(b=bs[0],N=len(bs),o=o,lam=lam) for _,bs in sorted(by.items())])
    out=[]
    for eta in (0,1):
        for tile in product(*blocks):
            z=pow(p,eta,R)
            for q,t in zip(qs,tile): z=z*pow(q,t['b'],R)%R
            if (z+1)%k: continue
            c0=((z+1)//k)%D; factors=[(t['lam'],t['N']) for t in tile]
            coeff=convolution(D,factors)
            periods,fgood=coefficient_stabilizer(D,factors)
            width=sum(t['N']-1 for t in tile if gcd(t['lam'],D)==1)
            actual=[]
            for ts in product(*(range(t['N']) for t in tile)):
                betas=[t['b']+t['o']*j for t,j in zip(tile,ts)]
                u=prod(q**(e+b) for q,e,b in zip(qs,es,betas))
                c=(c0-sum(t['lam']*j for t,j in zip(tile,ts)))%D
                full=((4*u+1 if eta else p+4*u)%R==0)
                need(full==(c==0))
                if full: actual.append(u)
            need(len(actual)==coeff[c0])
            need(periods==[b for b in range(D) if all(coeff[(i+b)%D]==coeff[i] for i in range(D))])
            if D>1 and width>=D-1:
                need(coeff[c0]>=prod(t['N'] for t in tile if gcd(t['lam'],D)!=1))
            out.append(dict(channel='E' if eta else 'M',base=[t['b'] for t in tile],
                primes=qs,exponents=es,orders=[t['o'] for t in tile],lengths=[t['N'] for t in tile],
                lambdas=[t['lam'] for t in tile],c0=c0,D=D,K=k,
                coefficient_vector=coeff,stabilizer=periods,full_words=actual,unit_width=width))
    return out


def factor_sum_returns(rec):
    """Every factor-sum arrow preserving raw r, with primitive renormalization."""
    need(rec['channel']=='M' and rec['trace'])
    h,r,s=rec['h'],rec['r'],rec['s']; delta=rec['delta']; t=rec['D']
    need(delta*t*t==rec['R'])
    n=(t*t-1)//4
    if n%r: return []
    disc=(s-h)**2+4*delta*(n//r); root=isqrt(disc)
    ans=[]
    if root*root!=disc: return ans
    for num in sorted(set([h-s-root,h-s+root])):
        if num%(2*delta): continue
        w=num//(2*delta); hp=h-delta*w; sp=s+delta*w
        need(hp>0 and sp>0 and r*(delta*w*w+(s-h)*w)==n)
        c=gcd(r,sp)
        target=state(rec['p'],hp*r*sp,hp*r*r,'M')
        need(target['full'] and target['R']==delta)
        need((target['h'],target['r'],target['s'])==(hp*c*c,r//c,sp//c))
        ans.append(dict(w=w,normalization_gcd=c,raw_target_factors=dict(h=hp,r=r,s=sp),source=rec,target=target))
    return ans


def factor_sum_inverse(target):
    """Complete finite incoming fibre, retaining both w and the lost gcd c."""
    need(target['channel']=='M' and target['full'])
    delta=target['R']; need(residual_parts(delta)[1]==1)
    h0,r0,s0=target['h'],target['r'],target['s']; p=target['p']; out=[]
    square_divisors=divs_f({q:e//2 for q,e in factor(h0).items()})
    for c in square_divisors:
        hp=h0//(c*c);r=c*r0;sp=c*s0
        lo=(-hp)//delta+1;hi=(sp-1)//delta
        for w in range(lo,hi+1):
            v=1+4*r*w*(sp-hp)-4*r*delta*w*w
            if v<=0: continue
            t=isqrt(v)
            if t*t!=v or t%2==0 or delta*t*t>=p: continue
            h=hp+delta*w;s=sp-delta*w
            if gcd(r,s)!=1 or (r+s)%(delta*t): continue
            src=state(p,h*r*s,h*r*r,'M')
            need(src['trace'] and (src['h'],src['r'],src['s'])==(h,r,s))
            out.append(dict(w=w,normalization_gcd=c,source=src))
    return out


def squareclass(n: int):
    """Return the unique positive pair (delta,v) with n=delta*v^2 and delta squarefree."""
    need(n > 0)
    ff = factor(n)
    delta = prod(q for q,e in ff.items() if e % 2)
    v = prod(q**(e//2) for q,e in ff.items())
    need(n == delta*v*v)
    return delta,v


def fixed_tail_seed(rec):
    """The shifted-factor Pell point attached to one ordered rational trace.

    This retains the numerical tail sum y+z.  It is different from
    factor_sum_returns(), which retains the raw factor sum h+s.
    """
    need(rec['trace'])
    p,a,R = (rec[k] for k in ('p','a','R'))
    y,z = (Fraction(*q) for q in rec['denominators'][1:])
    N = y+z
    need(N.denominator == 1)
    N = N.numerator
    B = R*y-p*a; C = R*z-p*a
    need(B.denominator == C.denominator == 1)
    B,C = B.numerator,C.numerator
    w = B-C; DD = N*(N-p)
    need(B*C == (p*a)**2)
    need(w*w == DD*R*R-N*p*p*R)
    U = 2*DD*R-p*p*N; V = 2*w
    need(U*U-DD*V*V == p**4*N*N)
    delta,v=squareclass(R); Delta=z-y; X=v*Delta
    need(X*X-DD*v*v == Fraction(-N*p*p,delta))
    x_integral=(X.denominator==1)
    return dict(p=p,a=a,R=R,N=N,B=B,C=C,w=w,D=DD,U=U,V=V,
                pell_norm=p**4*N*N,exact_tail_gate=(w%R==0),
                gate_residue=w%R,tail_difference_Z_minus_Y=frac(Delta),
                squareclass=dict(delta=delta,v=v,X=frac(X),
                    norm_rhs=frac(Fraction(-N*p*p,delta)),
                    v_divides_X=x_integral and X.numerator%v==0,
                    parity_gate=x_integral and (X.numerator-N*v)%(2*v)==0))


def fixed_tail_fibre(p: int, N: int):
    """Complete ordered integral first-half fibre at fixed prime p and sum N.

    For prime p and 0<rho<p, gcd(rho,p)=1.  Hence the exact identity
    rho*(Z-Y)^2=N*((N-p)*rho-p^2) forces rho|N.  Enumerating the
    divisors of N is therefore complete, not a bounded search heuristic.
    """
    need(is_prime(p) and p % 2 == 1 and N > p)
    DD = N*(N-p); candidates=[]; targets=[]
    for rho in divisors(N):
        if not (0 < rho < p and (p+rho)%4 == 0):
            continue
        disc = DD-N*p*p//rho
        row = dict(rho=rho,a=(p+rho)//4,discriminant=disc)
        if disc < 0:
            row.update(square=False,rejection='negative discriminant')
            candidates.append(row); continue
        root = isqrt(disc)
        row.update(floor_sqrt=root,square=(root*root==disc),
                   lower_gap=disc-root*root,upper_gap=(root+1)**2-disc)
        if root*root != disc:
            row['rejection']='between consecutive squares'
            candidates.append(row); continue
        if root >= N or root % 2 != N % 2:
            row['rejection']='positivity or parity gate'
            candidates.append(row); continue
        delta,v=squareclass(rho)
        signs=[0] if root==0 else [-1,1]
        ordered=[]
        for sign in signs:
            Delta=sign*root
            Y=(N-Delta)//2; Z=(N+Delta)//2
            need(Y>0 and Z>0 and Y+Z==N)
            A=(p+rho)//4
            need(Fraction(1,A)+Fraction(1,Y)+Fraction(1,Z)==Fraction(4,p))
            X=v*Delta
            need(X*X-DD*v*v == -N*p*p//delta)
            need(X%v==0 and (X-N*v)%(2*v)==0)
            target=dict(rho=rho,a=A,Y=Y,Z=Z,Delta=Delta,
                        squareclass=dict(delta=delta,v=v,X=X,
                            norm_rhs=-N*p*p//delta))
            targets.append(target); ordered.append(target)
        row['ordered_targets']=ordered
        candidates.append(row)
    return dict(p=p,N=N,D=DD,candidates=candidates,targets=targets,
                complete_reason='rho divides N because rho<p and p is prime')


def prime_square_prediction(p,q):
    a=q*q; R=4*a-p; k,D,_=residual_parts(R); out=[]
    if q%3!=2: return out
    for ch,f,g in [('E',1,4*q+1),('E',3,4*q**3+1),('M',1,q+1),('M',3,q+1)]:
        if g%k==0: out.append((ch,f,g%R==0))
    return sorted(out)


def prime_power_middle(p,q,e):
    a=q**e; R=4*a-p; k,D,_=residual_parts(R)
    betas=[b for b in range(-e,e+1) if (pow(q,b,k)+1)%k==0]
    if not betas: return dict(trace_betas=[],full_betas=[])
    o=order(q,k); need(o%2==0); b=o//2
    need(b%2==1 and pow(q,b,k)==k-1)
    dd=R//gcd(R,(pow(q,b,R)+1)%R); B=b*dd
    predicted=[v for v in range(-e,e+1) if v%b==0 and (v//b)%2==1]
    full=[v for v in range(-e,e+1) if v%B==0 and (v//B)%2==1]
    need(betas==predicted)
    need(len(betas)==2*((e+b)//(2*b)) and len(full)==2*((e+B)//(2*B)))
    need(order(q,R)==2*B)
    return dict(b=b,d_b=dd,B=B,trace_betas=betas,full_betas=full)


if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--p',type=int,required=True); ap.add_argument('--a',type=int,required=True)
    ap.add_argument('--u',type=int,required=True); ap.add_argument('--channel',choices=['E','M'],default='M')
    args=ap.parse_args(); r=state(args.p,args.a,args.u,args.channel,True)
    output=dict(source=r)
    if r['channel']=='M' and r['trace']: output['factor_sum_returns']=factor_sum_returns(r)
    print(json.dumps(output,indent=2))
