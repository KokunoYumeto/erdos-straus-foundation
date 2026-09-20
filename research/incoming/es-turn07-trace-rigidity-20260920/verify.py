#!/usr/bin/env python3
"""Exact replay for the trace-rigidity continuation. Standard library only.

No call proves universal ES occupancy. All finite ranges are explicit in summary.json.
The checks deliberately distinguish rational roots, algebraic roots, raw gate
words, original divisor words, and ordered E/M states.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations_with_replacement
from math import gcd, isqrt, lcm, prod, factorial
from pathlib import Path
import json
import time

CHECKS = 0

def ck(value: bool, message: str = "check failed") -> None:
    global CHECKS
    CHECKS += 1
    if not value:
        raise ArithmeticError(message)

def primes_upto(n: int) -> list[int]:
    if n < 2: return []
    a = bytearray(b'\x01')*(n+1); a[0:2]=b'\x00\x00'
    for q in range(2,isqrt(n)+1):
        if a[q]: a[q*q:n+1:q]=b'\x00'*(((n-q*q)//q)+1)
    return [q for q in range(2,n+1) if a[q]]

def fac(n: int) -> dict[int,int]:
    if n < 1: raise ValueError("positive factor input required")
    out={}; q=2
    while q*q<=n:
        while n%q==0: out[q]=out.get(q,0)+1; n//=q
        q=3 if q==2 else q+2
    if n>1: out[n]=out.get(n,0)+1
    return out

def divs_from(f: dict[int,int], multiplier: int=1) -> list[int]:
    out=[1]
    for q,e in sorted(f.items()): out=[d*q**k for d in out for k in range(multiplier*e+1)]
    return sorted(out)

def divs(n: int) -> list[int]: return divs_from(fac(n))
def Kroot(n: int) -> int: return prod(q**((e+1)//2) for q,e in fac(n).items())
def vp(n: int, p: int) -> int:
    if not n: return 10**6
    e=0
    while n%p==0: n//=p; e+=1
    return e

def leg(a: int,p: int) -> int:
    a%=p
    if not a:return 0
    z=pow(a,(p-1)//2,p)
    if z not in (1,p-1): raise ValueError("prime modulus required")
    return 1 if z==1 else -1

def fq(x: Q | int) -> list[int]:
    z=Q(x);return [z.numerator,z.denominator]

def json_write(path: Path,data) -> None:
    path.write_text(json.dumps(data,sort_keys=True,indent=2)+"\n",encoding="utf-8")

def keydigest(rows) -> str:
    return sha256(json.dumps(rows,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def raw(p:int,a:int,U:int,channel:str='M') -> tuple[Q,Q,Q]:
    R=4*a-p
    if channel=='M':return Q(a),Q(p*a*(U+a),R*U),Q(p*(a+U),R)
    if channel=='E':return Q(a),Q(p*a*U+a*a,R*U),Q(p*a+p*p*U,R)
    raise ValueError(channel)

def state(p:int,a:int,u:int,ch:str) -> dict:
    R=4*a-p
    ck(p<4*a<2*p and a*a%u==0)
    g=gcd(a,u);h=g*g//u;r=u//g;s=a//g
    ck(g*g%u==0 and h*r*s==a and h*r*r==u and gcd(r,s)==1)
    k=(p*r+s)//R if ch=='E' else (r+s)//R
    ck((p*r+s if ch=='E' else r+s)%R==0)
    xyz=(a,h*s*k,p*h*r*k) if ch=='E' else (a,p*h*s*k,p*h*r*k)
    ck(4*prod(xyz)==p*(xyz[0]*xyz[1]+xyz[0]*xyz[2]+xyz[1]*xyz[2]))
    inv=Q(a*a if ch=='E' else p*a*a,R*xyz[1]-p*a)
    ck(inv==u)
    U=p*u if ch=='E' else u
    ck((a+U)%R==0 and raw(p,a,U)==tuple(Q(x) for x in xyz))
    S=p+sum(xyz);P2=p*p+sum(x*x for x in xyz)
    ck((S-a)%p==0 if ch=='M' else (S-a)%p!=0)
    ck(((S-p)**2-(P2-p*p))%8==0)
    e2=((S-p)**2-(P2-p*p))//2
    e3=p*e2//4
    ck(4*e3==p*e2)
    for x in xyz:ck(x**3-(S-p)*x*x+e2*x-e3==0)
    return {"p":p,"a":a,"R":R,"u":u,"channel":ch,"h":h,"r":r,"s":s,
            "kappa" if ch=='E' else "lambda":k,"denominators":list(xyz),"U":U,
            "literal_traces":[S,P2],"beta":[[q,vp(u,q)-e] for q,e in fac(a).items()]}

def trace_law(xs:tuple[Q,Q,Q]) -> dict:
    s1=sum(xs,Q());s2=sum((x*x for x in xs),Q())
    ck(s1.denominator==s2.denominator==1)
    ds=[x.denominator for x in xs]; d=ds[0]
    ck(len(set(ds))==1 and d%2==1 and d%9!=0)
    ck(all(q==3 or q%3==1 for q in fac(d)))
    rec=sum((1/x for x in xs),Q())
    if rec:ck(rec.numerator%(d**3)==0)
    return {"x":[fq(x) for x in xs],"d":d,"moments":[int(s1),int(s2)],"reciprocal":fq(rec)}

def allowed(d:int) -> bool:
    return d%2==1 and d%9!=0 and all(q==3 or q%3==1 for q in fac(d))

def crt(records:list[tuple[int,int]]) -> int:
    x=0;M=1
    for residue,modulus in records:
        ck(gcd(M,modulus)==1)
        x+=M*((residue-x)*pow(M,-1,modulus)%modulus);M*=modulus;x%=M
    return x

def construct_denominator(d:int) -> dict:
    if not allowed(d): raise ValueError("excluded denominator")
    if d==1:return {"d":1,"local":[],"L":1,"triple":trace_law((Q(1),Q(2),Q(3)))}
    br=[];cr=[];local=[]
    for q,e in fac(d).items():
        mod=q**(2*e+1)
        if q==3:
            ck(e==1);b=1;c=4;root=None;choice=None
        else:
            b=next(t for t in range(2,q) if (t*t+t+1)%q==0)
            cur=q;lift=[]
            for exponent in range(1,2*e):
                val=(b*b+b+1)//cur
                t=-val*pow(2*b+1,-1,q)%q
                b+=cur*t;cur*=q
                ck((b*b+b+1)%cur==0);lift.append([exponent+1,b])
            root=b;choice=None
            for t in range(q):
                cc=-1-b+(q**(2*e))*t
                e2=b+(1+b)*cc
                if vp(e2,q)==2*e:
                    c=cc%mod;choice=t;break
            if choice is None:raise ArithmeticError("no permitted lift")
        ck((1+b+c)%q**e==0 and vp(b+c+b*c,q)==2*e)
        br.append((b,mod));cr.append((c,mod))
        local.append({"prime":q,"exponent":e,"modulus":mod,"b":b,"c":c,
                      "root":root,"choice":choice})
    L=prod(m for _,m in br)
    B=crt(br)+L;C=crt(cr)+2*L
    xs=(Q(1,d),Q(B,d),Q(C,d));row=trace_law(xs)
    ck(xs[0]<xs[1]<xs[2])
    for q,e in fac(d).items():ck(vp(row['reciprocal'][0],q)==3*e)
    return {"d":d,"local":local,"L":L,"triple":row}


def general_moment_law(xs:tuple[Q,...]) -> dict:
    n=len(xs)
    if n<2 or any(x==0 for x in xs):raise ValueError("nonzero roots, n>=2")
    moments=[sum((x**k for x in xs),Q()) for k in range(1,n)]
    ck(all(z.denominator==1 for z in moments))
    ds=[x.denominator for x in xs];d=ds[0]
    ck(all(v==d for v in ds))
    rec=sum((1/x for x in xs),Q())
    if rec:
        ck(gcd(d,rec.denominator)==1)
        ck((factorial(n-1)*rec.numerator)%d**n==0)
        if n>=3 and rec.numerator in (1,2,4):ck(d==1)
    es=[Q(1)]
    for k in range(1,n):
        ek=sum(((-1)**(i-1)*es[k-i]*moments[i-1] for i in range(1,k+1)),Q())/k
        es.append(ek);ck((factorial(k)*ek).denominator==1)
    return {"n":n,"x":[fq(x) for x in xs],"d":d,
            "moments":[int(z) for z in moments],"reciprocal":fq(rec),
            "elementary_through_n_minus_one":[fq(x) for x in es]}

def general_examples() -> list[dict]:
    out=[general_moment_law((Q(5,2),Q(5,2))),
         general_moment_law(tuple(Q(a,2) for a in (1,1,1,5)))]
    for n in range(3,9):
        q=next(q for q in primes_upto(200) if q%n==1)
        root=next(z for z in range(2,q) if pow(z,n,q)==1 and
                  all(pow(z,k,q)!=1 for k in range(1,n)))
        cur=q
        for exponent in range(1,n-1):
            step=-((root**n-1)//cur)*pow(n*root**(n-1),-1,q)%q
            root+=cur*step;cur*=q
            ck((root**n-1)%cur==0)
        As=[pow(root,i,cur)+(i+1)*cur for i in range(n)]
        row=general_moment_law(tuple(Q(a,q) for a in As))
        row['root_of_unity']={"prime":q,"root":root,"modulus":cur}
        out.append(row)
    return out

def denominator_scan(bound:int) -> dict:
    found=[];inputs=0
    for d in range(1,bound+1):
        for A in range(1,2*d+1):
            for B in range(A,2*d+1):
                c0=(-A-B)%d or d
                for C in (c0,c0+d):
                    if C<B:continue
                    inputs+=1
                    if (A*A+B*B+C*C)%(d*d):continue
                    row=trace_law(tuple(Q(v,d) for v in (A,B,C)))
                    found.append({"presentation":[d,A,B,C],**row})
    return {"presentation_bound":bound,"numerator_range":"1..2d, A<=B<=C",
            "first_trace_pass_candidates":inputs,"records":found}

def full_scan(bound:int) -> dict:
    rows=[];all_states=[];tot=Counter()
    for p in primes_upto(bound):
        if p%4!=1:continue
        c=Counter()
        for a in range(p//4+1,(p+1)//2):
            R=4*a-p;D=divs_from(fac(a),2);c['shells']+=1;c['original_divisors']+=len(D)
            ms=[];es=[]
            for u in D:
                ck(gcd(u,R)==1)
                if (4*u+1)%R==0:es.append(state(p,a,u,'E'))
                if (u+a)%R==0:ms.append(state(p,a,u,'M'))
            c['E']+=len(es);c['M']+=len(ms)
            mm={z['u']:z for z in ms}
            for u,rec in mm.items():
                partner=a*a//u
                ck(partner in mm and partner!=u)
                ck(rec['literal_traces']==mm[partner]['literal_traces'])
                if u<partner:
                    w1=1+u%7;w2=1+partner%7;den=Q(1,w1)+Q(1,w2)
                    x1=Q(1,w1)/den;x2=Q(1,w2)/den
                    ck(x1+x2==1 and w1*x1*x1+w2*x2*x2==1/den)
            # A channel record is not merged merely because its trace equals
            # a trace at a different distinguished denominator a.
            groups=defaultdict(list)
            for z in es+ms:groups[z['literal_traces'][0]].append(z)
            ck(len(groups)==len(es)+len(ms)//2)
            for entries in groups.values():
                ck(len(entries)==(2 if entries[0]['channel']=='M' else 1))
                ck(len({z['channel'] for z in entries})==1)
            all_states.extend(es+ms)
        rows.append({"p":p,**c});tot.update(c)
    global_traces=defaultdict(list)
    for z in all_states:global_traces[(z['p'],*z['literal_traces'])].append(z)
    for entries in global_traces.values():
        ck(len(entries)==(2 if entries[0]['channel']=='M' else 1))
        ck(len({z['a'] for z in entries})==1)
    return {"bound":bound,"primes":len(rows),"rows":rows,"totals":dict(tot),
            "state_digest":keydigest(all_states),"states":all_states}

def raw_scan(bound:int) -> dict:
    rows=[];tot=Counter()
    for p in primes_upto(bound):
        if p%4!=1:continue
        for a in range(p//4+1,(p+1)//2):
            R=4*a-p;limit=p*a*a;start=(-a)%R
            ck(start>0)
            images={};integers=Counter();count=0;collisions=[]
            for U in range(start,limit+1,R):
                count+=1
                z=p*(a+U)//R
                yn=p*a*(U+a);yd=R*U;g=gcd(yn,yd)
                den=yd//g
                ck(den==U//gcd(U,p*a*a))
                sn=(p+a+z)*yd+yn;sg=gcd(sn,yd);key=(sn//sg,yd//sg)
                ck(key[1]==den)
                if key in images:
                    V=images[key]
                    ck(U!=V and U*V==a*a and den==1)
                    collisions.append([V,U,key[0]])
                else:images[key]=U
                if den==1:
                    ch='E' if U%p==0 else 'M'
                    ck(vp(U,p)<2)
                    ck((key[0]-a)%p==0 if ch=='M' else (key[0]-a)%p!=0)
                    integers[ch]+=1
            sd=divs_from(fac(a),2)
            E=sum((4*u+1)%R==0 for u in sd);M=sum((a+u)%R==0 for u in sd)
            ck(integers['E']==E and integers['M']==M)
            ck(count-len(images)==M//2 and len(collisions)==M//2)
            ck(sum(k[1]==1 for k in images)==E+M//2)
            row={"p":p,"a":a,"R":R,"raw_words":count,"trace_values":len(images),
                 "integer_trace_values":E+M//2,"kernel_rank":M//2,"E":E,"M":M,
                 "collisions":collisions}
            rows.append(row);tot.update({k:row[k] for k in ('raw_words','trace_values','integer_trace_values','kernel_rank','E','M')})
    return {"bound":bound,"rows":rows,"totals":dict(tot)}

def trace_relaxation(bound:int) -> dict:
    rows=[];tot=Counter();examples=[]
    for p in primes_upto(bound):
        if p%4!=1:continue
        c=Counter()
        for a in range(p//4+1,(p+1)//2):
            R=4*a-p;K=Kroot(R);n=p*a
            f=fac(a);f[p]=1
            for b in divs_from(f,2):
                if b>=n:break
                c['ordered_representatives_tested']+=1
                if (n+b)%K:continue
                cc=n*n//b;y=Q(n+b,R);z=Q(n+cc,R);N=y+z
                ck(N.denominator==1 and 1/Q(a)+1/y+1/z==Q(4,p))
                d=y.denominator
                ck(z.denominator==d and d*d==R//gcd(R,int(N)))
                P2=Q(a*a)+y*y+z*z
                ck(P2.denominator==d*d)
                ck((d==1)==((n+b)%R==0))
                if K==R:ck(d==1)
                c['trace_integral_pairs']+=1
                c['nonintegral_pairs' if d>1 else 'integral_pairs']+=1
                if d>1 and len(examples)<12:
                    examples.append({"p":p,"a":a,"R":R,"K":K,"factor":b,
                                     "tail":[fq(y),fq(z)],"denominator":d,
                                     "trace1":fq(a+N),"trace2":fq(P2)})
        rows.append({"p":p,**c});tot.update(c)
    return {"bound":bound,"rows":rows,"totals":dict(tot),"examples":examples}

def tonelli(n:int,p:int) -> int:
    n%=p
    if n==0:return 0
    if leg(n,p)!=1:raise ValueError("nonsquare")
    if p%4==3:return pow(n,(p+1)//4,p)
    s=0;q=p-1
    while q%2==0:s+=1;q//=2
    z=next(z for z in range(2,p) if leg(z,p)==-1)
    c=pow(z,q,p);r=pow(n,(q+1)//2,p);t=pow(n,q,p);m=s
    while t!=1:
        i=1;v=t*t%p
        while v!=1:v=v*v%p;i+=1
        b=pow(c,1<<(m-i-1),p);r=r*b%p;t=t*b*b%p;c=b*b%p;m=i
    return min(r,p-r)

def quadratic_template(p:int) -> dict:
    if p<1009 or p%24!=1:raise ValueError("p>=1009, p=1 mod24 required")
    a=(p+3)//4;m=(p-1)//6
    residues=[k for k in range(1,p) if leg(k,p)==leg(3*k-1,p)==-1]
    ck(len(residues)==(p-1)//4)
    k0=residues[0];K0=(m+1)**2//2+1;k=K0+(k0-K0)%p
    disc=9*k*k-4*a*k;L=3*k-m-1;H=L+1
    ck(0<L and L*L<disc<H*H)
    ck(isqrt(disc)**2!=disc and 60*k<p*p)
    ck(leg(disc,p)==1 and leg(a*k,p)==-1)
    # Monic polynomial of the three denominators.
    e1=a+3*p*k;e2=p*a*k*(p+3);e3=p*p*a*a*k
    ck(4*e3==p*e2)
    moments=[3,e1,e1*e1-2*e2]
    moments.append(e1*moments[2]-e2*moments[1]+3*e3)
    for n in range(4,17):moments.append(e1*moments[-1]-e2*moments[-2]+e3*moments[-3])
    ck(all(isinstance(v,int) and v>0 for v in moments))
    # Exact root mod p^5; no complex approximation is used.
    root=tonelli(disc,p);mod=p;lift=[root]
    for n in range(1,5):
        correction=-((root*root-disc)//mod)*pow(2*root,-1,p)%p
        root+=mod*correction;mod*=p
        ck((root*root-disc)%mod==0);lift.append(root)
    b=(3*k+root)*pow(2,-1,mod)%mod;c=(3*k-root)*pow(2,-1,mod)%mod
    ck((b+c-3*k)%mod==0 and (b*c-a*k)%mod==0)
    ck(all(v%p for v in (b,c,b-c,b-1,c-1)))
    rs=[p,a,p*b%mod,p*c%mod];S=p+e1
    der=[]
    for i in range(4):
        num=prod((rs[i]-rs[j])%mod for j in range(4) if j!=i)
        v=vp(num,p);ck(v<5);der.append(v)
    ck(der==[2,0,2,2])
    sp=(p*p+3*p)//4;Bp=p+sp*(sp+1)
    ck(S<Bp and 9*p*k<sp*(sp+1))
    ck(a+1<p and p*(a-3)>3 and disc>1)
    # Coefficient of the literal quartic is recovered from denominator e_i.
    quartic=[1,-(p+e1),e2+p*e1,-(e3+p*e2),p*e3]
    coeffvals=[0,vp(quartic[2],p),vp(quartic[3],p),vp(quartic[4],p)]
    ck(coeffvals==[0,1,2,3])
    return {"p":p,"a":a,"k0":k0,"residue_count":len(residues),"K0":K0,"k":k,
            "quadratic":[1,-3*k,a*k],"discriminant":disc,"bracketing_integers":[L,H],
            "denominator_cubic":[1,-e1,e2,-e3],"moments_0_through_16":moments,
            "literal_monic_quartic":quartic,"literal_trace":S,
            "local_sqrt_mod_p_powers":lift,"local_root_b_c_mod_p5":[b,c],
            "derivative_valuations":der,"coefficient_valuations":coeffvals,
            "height_bound":Bp,"max_denominator_strict_upper":3*p*k}

def fixtures() -> dict:
    out={}
    for prime_input in (13,193,1009,35281):
        ck(prime_input>=2 and all(prime_input%q for q in range(2,isqrt(prime_input)+1)),
           'displayed-prime certificate')
    # One-moment counterexample and the exact failed square-removal attempt.
    for p,a,R,b in [(193,55,27,5),(1009,286,135,11)]:
        n=p*a;y=Q(n+b,R);z=Q(n+n*n//b,R)
        ck(1/Q(a)+1/y+1/z==Q(4,p))
        ck((a+y+z).denominator==1 and y.denominator==z.denominator==3)
        P2=Q(a*a)+y*y+z*z;ck(P2.denominator==9)
        r=R//9;anew=(p+r)//4
        hits={ch:[u for u in divs_from(fac(anew),2) if
                    ((4*u+1)%r==0 if ch=='E' else (anew+u)%r==0)] for ch in ('E','M')}
        ck(not hits['E'] and not hits['M'])
        out[str(p)]={"a":a,"R":R,"factor":b,"triple":[fq(a),fq(y),fq(z)],
                     "trace1":fq(a+y+z),"trace2":fq(P2),"compressed_R":r,
                     "compressed_a":anew,"compressed_square_divisors":divs_from(fac(anew),2),
                     "compressed_hits":hits}
    p=35281;a=8821;U=202883
    out['foreign_prime']={}
    for ch in ('E','M'):
        xyz=raw(p,a,U,ch);S=p+sum(xyz,Q())
        ck(sum((1/x for x in xyz),Q())==Q(4,p) and S.denominator==23)
        out['foreign_prime'][ch]={"triple":[fq(x) for x in xyz],"literal_trace":fq(S)}
    out['p1009_states']=[state(1009,253,11,ch) for ch in ('E','M')]
    out['general_moment_examples']=general_examples()
    out['sharp_numerators']=[trace_law(tuple(Q(n,d) for n in ns))
                              for d,ns in [(3,[1,1,4]),(7,[1,18,30]),(13,[1,22,146])]]
    xyz=raw(13,4,5);S=13+sum(xyz,Q())
    ck(S==Q(436,5) and abs(S-round(S))==Q(1,5))
    out['strict_gap']={"p":13,"a":4,"U":5,"trace":fq(S),"distance":fq(Q(1,5))}
    # Distinct integer roots are not required by the general moment theorem.
    xs=(Q(2),Q(2),Q(3));trace_law(xs)
    return out

def negative_controls(data:dict) -> list[dict]:
    fs=data['fixtures']; controls=[]
    tests=[
        ("the n>=3 hypothesis can be dropped",fs['general_moment_examples'][0]['d']==2 and fs['general_moment_examples'][0]['reciprocal']==[4,5]),
        ("one trace forces rational integrality",fs['1009']['trace1'][1]==1 and fs['1009']['triple'][1][1]>1),
        ("square removal preserves the shell gate",not fs['1009']['compressed_hits']['E'] and not fs['1009']['compressed_hits']['M']),
        ("all raw integral M traces are canonical M",fs['p1009_states'][0]['U']%1009==0),
        ("a finite-place predicate includes global trace",fs['foreign_prime']['E']['literal_trace'][1]==23),
        ("the reciprocal numerator need not retain its cube",fs['sharp_numerators'][0]['d']==3 and fs['sharp_numerators'][0]['reciprocal']==[27,4]),
        ("the trace gap permits weak inequality",fs['strict_gap']['trace'][1]==5),
        ("all algebraic integer moment targets split rationally",data['algebraic'][0]['bracketing_integers'][0]**2<data['algebraic'][0]['discriminant']<data['algebraic'][0]['bracketing_integers'][1]**2),
    ]
    for label,witness in tests:ck(witness);controls.append({"false_claim":label,"rejected":True})
    return controls

def main() -> None:
    ap=argparse.ArgumentParser();ap.add_argument('--bound',type=int,default=3000)
    ap.add_argument('--raw-bound',type=int,default=97);ap.add_argument('--relaxation-bound',type=int,default=500)
    ap.add_argument('--denominator-bound',type=int,default=500)
    ap.add_argument('--out',type=Path,default=Path('certificates'));args=ap.parse_args()
    start=time.monotonic();args.out.mkdir(parents=True,exist_ok=True)
    full=full_scan(args.bound);rawdata=raw_scan(args.raw_bound)
    den=denominator_scan(80)
    den['constructions']=[construct_denominator(d) for d in range(1,args.denominator_bound+1) if allowed(d)]
    relax=trace_relaxation(args.relaxation_bound)
    hard={1,121,169,289,361,529}
    pp=[p for p in primes_upto(max(args.bound,1009)) if p>=1009 and p%840 in hard]
    alg=[quadratic_template(p) for p in pp]
    fx=fixtures();data={'fixtures':fx,'algebraic':alg};neg=negative_controls(data)
    tables={'scan.json':full,'raw_trace.json':rawdata,'denominators.json':den,
            'trace_relaxation.json':relax,'algebraic_targets.json':alg,'examples.json':fx,
            'negative_controls.json':neg}
    for name,row in tables.items():json_write(args.out/name,row)
    summary={"success":True,"bound":args.bound,"primes":full['primes'],"checks":CHECKS,
             "original_totals":full['totals'],"raw_bound":args.raw_bound,
             "raw_totals":rawdata['totals'],"relaxation_bound":args.relaxation_bound,
             "relaxation_totals":relax['totals'],"denominator_bound":args.denominator_bound,
             "constructive_denominators":len(den['constructions']),"algebraic_target_count":len(alg),
             "negative_controls":len(neg),"state_digest":full['state_digest'],
             "mathematical_tables_sha256":{name:sha256((args.out/name).read_bytes()).hexdigest() for name in tables},
             "scope":"Bounded verification; no universal ES occupancy, no independent mathematical review.",
             "elapsed_seconds":time.monotonic()-start}
    json_write(args.out/'summary.json',summary);print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
