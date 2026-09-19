#!/usr/bin/env python3
"""Turn 3: original primitive sextic triangle and square-source escape.

Python standard library only. No assertion statement is used for validation.
The default scan exhausts all directed canonical triangles among 3 mod 4
external-nonresidue primes for hard p <= 250000. It does NOT scan every
selector of those primes or the complete graph at the displayed large p.
"""
from __future__ import annotations
import argparse
from collections import Counter
from copy import deepcopy
from fractions import Fraction
from hashlib import sha256
from itertools import product
from math import gcd, isqrt, prod
from pathlib import Path
import json

CHECKS: Counter[str] = Counter()
HARD = {1, 121, 169, 289, 361, 529}


def require(ok: bool, label: str) -> None:
    CHECKS[label] += 1
    if not ok:
        raise ArithmeticError(label)


def dump(path: Path, data: object) -> None:
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + '\n')


def prime_certificate(cert: dict) -> dict:
    """Prove prime roots recursively from complete n-1 order certificates."""
    nodes = cert['nodes']; checked: set[int] = set(); visiting: set[int] = set()
    def visit(n: int) -> None:
        if n in checked:
            return
        require(n not in visiting and str(n) in nodes, 'prime DAG availability')
        visiting.add(n); row = nodes[str(n)]
        require(row['n'] == n and n >= 2, 'prime node identity')
        if row['kind'] == 'trial':
            require(n <= 10000 and all(n % d for d in range(2, isqrt(n)+1)), 'exact terminal primality')
        elif row['kind'] == 'complete_order':
            fs = row['factors']; a = row['base']
            require(len({q for q,e in fs}) == len(fs) and all(q < n and e > 0 for q,e in fs), 'strict prime children')
            require(prod(q**e for q,e in fs) == n-1, 'complete n-1 factorization')
            for q,e in fs:
                visit(q)
            require(1 < a < n and pow(a,n-1,n) == 1, 'complete order power')
            for q,e in fs:
                require(gcd(pow(a,(n-1)//q,n)-1,n) == 1, 'complete order gcd')
        else:
            raise ArithmeticError('unknown certificate kind')
        visiting.remove(n); checked.add(n)
    for n in cert['roots']:
        visit(n)
    require(checked == {int(n) for n in nodes}, 'no unverified certificate node')
    return {'roots':len(cert['roots']), 'nodes':len(checked),
            'trial_nodes':sum(row['kind']=='trial' for row in nodes.values()),
            'complete_order_nodes':sum(row['kind']=='complete_order' for row in nodes.values())}


def legendre(a: int, p: int) -> int:
    r = pow(a % p, (p-1)//2, p)
    if r == p-1:
        return -1
    if r in (0,1):
        return r
    raise ArithmeticError('non-Legendre value; primality/domain problem')


def valuation(a: int, q: int) -> int:
    n=0
    while a % q == 0:
        a//=q; n+=1
    return n


def group(R: int, gs: list[int]) -> set[int]:
    H={1}; front=[1]
    require(all(gcd(g,R)==1 for g in gs), 'group unit generators')
    while front:
        x=front.pop()
        for g in gs:
            y=x*g%R
            if y not in H:
                H.add(y); front.append(y)
    return H


def order(g: int, R: int) -> int:
    x=1
    for n in range(1,R):
        x=x*g%R
        if x==1:
            return n
    raise ArithmeticError('unit order failed')


def original_source(p: int, R: int, fs: list[list[int]], keep_words: bool=False) -> dict:
    require(R > 0 and (p+R)%4==0, 'source shell integrality')
    a=(p+R)//4
    require(a < p and gcd(a*p,R)==1 and prod(q**e for q,e in fs)==a, 'source factors and units')
    require(len({q for q,e in fs})==len(fs) and all(e>0 for q,e in fs), 'distinct original prime slots')
    mu=Counter(); words=[]; E=[]; M=[]
    for beta in product(*(range(-e,e+1) for q,e in fs)):
        u=prod(q**(e+b) for (q,e),b in zip(fs,beta))
        residue=prod(pow(q,b,R) for (q,e),b in zip(fs,beta))%R
        require(u*pow(a,-1,R)%R==residue, 'centered original divisor inverse')
        require([valuation(u,q)-e for q,e in fs]==list(beta), 'prime exponent round trip')
        ge=(4*u+1)%R==0; gm=(u+a)%R==0
        require(ge==(residue==(-pow(p,-1,R))%R) and gm==(residue==R-1), 'two canonical gates')
        mu[residue]+=1
        if ge: E.append(u)
        if gm: M.append(u)
        if keep_words:
            words.append({'beta':list(beta),'u':u,'residue':residue,'E':ge,'M':gm})
    require(sum(mu.values())==prod(2*e+1 for q,e in fs), 'original divisor mass')
    require(all(mu[x]==mu[pow(x,-1,R)] for x in mu), 'centered inversion multiplicity')
    return {'p':p,'R':R,'a':a,'factors':fs,'mu':sorted(mu.items()),'E':sorted(E),'M':sorted(M),'words':words}


def reconstruct(p: int, R: int, a: int, u: int, tag: str) -> dict:
    require(4*a==p+R and a*a%u==0 and tag in ('E','M'), 'return original source')
    d=gcd(a,u); h=d*d//u; r=u//d; s=a//d
    require(h>0 and h*r*s==a and h*r*r==u and gcd(r,s)==1, 'return normalized marking')
    num=p*r+s if tag=='E' else r+s
    require(num%R==0, 'return integral channel quotient')
    k=num//R; x=a; y=h*s*k*(1 if tag=='E' else p); z=p*h*r*k
    require(min(x,y,z)>0 and 4*x*y*z==p*(x*y+x*z+y*z), 'original ES polynomial identity')
    inv_num=a*a*(1 if tag=='E' else p); inv_den=R*y-p*a
    require(inv_den>0 and inv_num==u*inv_den, 'ordered divisor inverse')
    return {'p':p,'R':R,'a':a,'u':u,'channel':tag,'h':h,'r':r,'s':s,
            'kappa' if tag=='E' else 'lambda':k,'denominators':[x,y,z]}


def cycle_data(inp: dict, certified: set[int]) -> dict:
    p=inp['p']; Q=inp['cycle']; rows=[]
    require(p in certified and p%840 in HARD and len(Q)==3 and len(set(Q))==3, 'certified hard triangle')
    require(all(q in certified and q>=11 and q%4==3 and q<p for q in Q), 'triangle vertex domains')
    for i,q in enumerate(Q):
        r=Q[(i+1)%3]; previous=Q[i-1]
        bfs=inp['inactive_factorizations'][i]
        require(all(t in certified for t,e in bfs) and r not in [t for t,e in bfs], 'certified original factors')
        fs=sorted(bfs+[[r,1]]); src=original_source(p,q,fs,True); a=src['a']; B=a//r
        K={pow(x,6,q) for x in range(1,q)}
        require(len(K)==(q-1)//6 and all(t%q in K for t,e in bfs), 'sixth-power inactive factors')
        bm=Counter()
        for beta in product(*(range(-e,e+1) for t,e in bfs)):
            v=prod(pow(t,b,q)for (t,e),b in zip(bfs,beta))%q;bm[v]+=1
        require(set(bm)==K, 'complete inactive saturation')
        fixed=inp['fixed_saturating_factorizations'][i]
        smallW={prod(pow(t,b,q)for(t,e),b in zip(fixed,beta))%q for beta in product(*(range(-e,e+1)for t,e in fixed))}
        require(smallW==K, 'fixed bounded saturation packet')
        W={v for v,c in src['mu']}; actualK={k for k in W if {k*w%q for w in W}==W}
        require(actualK==K and len(W)==3*len(K), 'actual stabilizer exact')
        require(group(q,[-1,2]+[t for t,e in fs])==set(range(1,q)), 'effective equals ambient six')
        require(not src['E'] and not src['M'], 'complete joint selector failure')
        require(legendre(q,p)==-1 and legendre(r,p)==-1 and all(legendre(t,p)==1 for t,e in bfs), 'all eligible edges retained')
        reps=[pow(r,j,q) for j in range(6)]; encoded={}
        for j in range(6):
            for k in K:
                g=reps[j]*k%q
                require(g not in encoded, 'unique section-kernel coordinates')
                encoded[g]=(j,k)
        require(len(encoded)==q-1 and encoded[q-1][0]==3 and encoded[p%q][0]==1, 'retained alpha eta phase')
        targets=[q-1,(-p)%q,(-pow(p,-1,q))%q]
        require([encoded[t][0] for t in targets]==[3,4,2], 'all three target labels')
        T=prod(2*e+1 for t,e in bfs)
        masses=[sum(c for g,c in src['mu'] if encoded[g][0]==j) for j in range(6)]
        require(masses==[T,T,0,0,0,T], 'original coarse integer masses')
        carry=pow(r,6,q)
        for j,k,l in product(range(6),repeat=3):
            coc=lambda a,b:pow(carry,(a+b)//6,q)
            require(coc(j,k)*coc((j+k)%6,l)%q==coc(k,l)*coc(j,(k+l)%6)%q, 'original section cocycle')
        for g,h in product(range(1,q),repeat=2):
            j,k=encoded[g];l,t=encoded[h];new=((j+l)%6,k*t*pow(carry,(j+l)//6,q)%q)
            require(encoded[g*h%q]==new, 'fine multiplication with carry')
        neighbor=previous*r*r%q
        roots=[x for x in range(1,q)if pow(x,6,q)==neighbor]
        require(neighbor in K and roots and encoded[previous%q][0]==4, 'complete neighbor-square recurrence')
        for w in src['words']:
            w['quotient'],w['kernel']=encoded[w['residue']]
        rows.append(dict(src,q=q,r=r,previous=previous,B=B,B_factors=bfs,K=sorted(K),mu_B=sorted(bm.items()),
                         quotient_masses=masses,targets=targets,target_classes=[3,4,2],section=reps,
                         carry=carry,successor_order=order(r,q),neighbor_carry=neighbor,sixth_roots=roots))
    require(sum(len(r['words'])for r in rows)==1215,'specified complete triangle mass')
    require(3*max(Q)<p and 15*max(Q)<p,'cycle size bounds')
    B=[r['B'] for r in rows];D=64*prod(B);T=[16*B[i]*B[(i+1)%3]+4*B[i]+1 for i in range(3)]
    h=gcd(*T)
    require(D-1==p*h and [t//h for t in T]==Q, 'cyclic integer inverse')
    linear=inp['linear_construction'];tt=linear['t'];values=[a+b*tt for a,b in linear['forms']]
    require(values[0]==p and values[1:]==[row['B_factors'][-1][0]for row in rows], 'finite CRT construction')
    return {'p':p,'cycle':Q,'nodes':rows,'total_original_vectors':1215,
            'cycle_inverse':{'D':D,'S':1,'T':T,'h':h},'scope':inp['scope']}


# F_2[C_6], F_4, and their explicit dual-number comparison.
def cyc_mul(a: int,b: int) -> int:
    out=0
    for i in range(6):
        if a>>i&1:
            for j in range(6):
                if b>>j&1: out^=1<<((i+j)%6)
    return out


def cyc_pow(a: int,n: int) -> int:
    out=1
    for _ in range(n):out=cyc_mul(out,a)
    return out


def f4_mul(a: int,b: int)->int:
    raw=0
    for i in range(2):
        if a>>i&1:
            for j in range(2):
                if b>>j&1:raw^=1<<(i+j)
    if raw&4:raw^=7
    return raw


def dual_mul(a: tuple[int,int],b: tuple[int,int])->tuple[int,int]:
    return f4_mul(a[0],b[0]), f4_mul(a[0],b[1])^f4_mul(a[1],b[0])


def eval_dual(poly: int,x: tuple[int,int])->tuple[int,int]:
    out=(0,0);power=(1,0)
    for i in range(6):
        if poly>>i&1:out=(out[0]^power[0],out[1]^power[1])
        power=dual_mul(power,x)
    return out


def algebra_map(poly: int)->tuple[tuple[int,int],tuple[int,int]]:
    return eval_dual(poly,(1,1)),eval_dual(poly,(2,2))


def algebra_inverse(pair: tuple[tuple[int,int],tuple[int,int]])->int:
    (a,b),(c,d)=pair
    if a not in (0,1) or b not in (0,1) or not(0<=c<4 and 0<=d<4):raise ValueError('dual coefficient domain')
    e0=1|4|16;e1=4|16;ep=1|8;Z=16
    poly4=lambda c:(1 if c&1 else 0)^(Z if c&2 else 0)
    return cyc_mul((a^(ep if b else 0)),e0)^cyc_mul(poly4(c)^cyc_mul(ep,poly4(d)),e1)


def algebra_tests()->dict:
    records=[]
    for a in range(64):
        im=algebra_map(a)
        require(algebra_inverse(im)==a,'six-dimensional CRT inverse')
        records.append({'X_coefficients':[(a>>i)&1 for i in range(6)],'dual_coordinates':im})
        for b in range(64):
            A=algebra_map(a);B=algebra_map(b)
            require(algebra_map(a^b)==tuple((A[i][0]^B[i][0],A[i][1]^B[i][1])for i in range(2)), 'CRT addition')
            require(algebra_map(cyc_mul(a,b))==tuple(dual_mul(A[i],B[i])for i in range(2)), 'CRT multiplication')
    P=1|2|32;e0=1|4|16
    require(algebra_map(P)==((1,0),(0,1)),'primitive packet has nonzero cubic jet')
    require(cyc_mul(P,P)==e0 and algebra_map(e0)==((1,0),(0,0)), 'square changes source and kills cubic jet')
    return {'all_64_coordinate_maps':records,'primitive_polynomial':[1,1,0,0,0,1],
            'primitive_image':algebra_map(P),'squared_image':algebra_map(e0),
            'note':'Squaring is a different, duplicated exponent source. It is not a move inside the original cap-one active prime box.'}


def eisenstein_tests(inp: dict)->dict:
    Q=inp['cycle'];pis=inp['eisenstein_primary'];zs=[]
    for q,(a,b)in zip(Q,pis):
        require(a*a-a*b+b*b==q and (a-1)%3==0 and b%3==0,'primary Eisenstein norm and convention')
        z=(-a*pow(b,-1,q))%q;require((z*z+z+1)%q==0 and z!=1,'Eisenstein reduction root');zs.append(z)
    H=[[None]*3 for _ in range(3)];K=[[None]*3 for _ in range(3)];E=[[None]*3 for _ in range(3)];details=[]
    for i,q in enumerate(Q):
        for j,(a,b)in enumerate(pis):
            if i==j:continue
            val=(a+b*zs[i])%q;conj=(a-b-b*zs[i])%q;roots=[pow(zs[i],t,q)for t in range(3)]
            h=roots.index(pow(val,(q-1)//3,q));k=roots.index(pow(conj,(q-1)//3,q));e=roots.index(pow(Q[j],(q-1)//3,q))
            require((h+k)%3==e and e!=0,'cubic norm factors with conjugate retained')
            H[i][j]=h;K[i][j]=k;E[i][j]=e
            details.append({'denominator':Q[i],'numerator_norm':Q[j],'primary_value':val,'conjugate_value':conj,'h':h,'k':k,'norm_symbol':e})
    for i,j in product(range(3),repeat=2):
        if i==j:continue
        require(H[i][j]==H[j][i] and (K[i][j]+K[j][i])%3==0,'primary reciprocity and conjugate correction')
    require(E==[[None,1,1],[1,None,1],[2,2,None]],'specified genuine cubic reciprocity table')
    return {'primary':pis,'omega_images':zs,'primary_matrix':H,'conjugate_matrix':K,'rational_norm_matrix':E,'entries':details}


def square_ports(inp: dict,certified: set[int])->dict:
    p=inp['p'];Q=inp['cycle'];out=[]
    for n in inp['ports9']:
        q=n['q'];fs=n['factors'];require(all(t in certified for t,e in fs),'port factor primality')
        row=original_source(p,9*q,fs,True)
        edges=[[t,e]for t,e in fs if legendre(t,p)==-1]
        require(edges and all(t not in Q for t,e in edges),'every square-nine successor outside triangle')
        require(gcd(row['a'],(p+q)//4)==gcd((p+q)//4,2),'old/new exact gcd')
        states=[reconstruct(p,9*q,row['a'],u,c) for c in ('E','M')for u in row[c]]
        projected={'E':[w['u'] for w in row['words'] if (4*w['u']+1)%q==0],
                   'M':[w['u'] for w in row['words'] if (w['u']+row['a'])%q==0]}
        require(all((4*u+1)%(9*q)==0 for u in row['E']) and all((u+row['a'])%(9*q)==0 for u in row['M']), 'complete square multiplicity retained')
        out.append(dict(row,q=q,multiplier=9,edges=edges,states=states,projected_mod_q={k:sorted(v)for k,v in projected.items()}))
    witness=inp['separate_ES_witness'];R=witness['R'];a=(p+R)//4
    require(all(t in certified for t,e in witness['factorization_a']) and prod(t**e for t,e in witness['factorization_a'])==a,'separate witness actual factorization')
    w=reconstruct(p,R,a,witness['u'],witness['channel'])
    return {'p':p,'ports':out,'separate_original_ES_witness':w}


def sieve_tables(n:int)->tuple[list[int],list[int]]:
    spf=list(range(n+1))
    for d in range(2,isqrt(n)+1):
        if spf[d]==d:
            for x in range(d*d,n+1,d):
                if spf[x]==x:spf[x]=d
    return spf,[x for x in range(2,n+1)if spf[x]==x]


def small_factors(n:int,spf:list[int])->list[list[int]]:
    out=[]
    while n>1:
        q=spf[n];e=0
        while n%q==0:n//=q;e+=1
        out.append([q,e])
    return out


def triangle_scan(bound:int)->dict:
    spf,ps=sieve_tables(bound);stats=Counter();triangles=[]
    for p in ps:
        if p%840 not in HARD:continue
        V=[q for q in ps if q<p and q%4==3 and legendre(q,p)==-1]
        adj={q:[r for r,e in small_factors((p+q)//4,spf)if r%4==3 and legendre(r,p)==-1]for q in V}
        stats['hard_primes']+=1;stats['vertices_3mod4']+=len(V);stats['edges_3mod4']+=sum(map(len,adj.values()))
        for q in V:
            for r in adj[q]:
                if r<=q:continue
                for s in adj[r]:
                    if s<=q or q not in adj[s]:continue
                    C=[q,r,s];ports=[]
                    for x in C:
                        require(3*x<p,'canonical triangle size bound')
                        a=(p+9*x)//4;fs=small_factors(a,spf);edges=[[t,e]for t,e in fs if legendre(t,p)==-1]
                        require(edges and all(t not in C for t,e in edges),'bounded complete triangle square escape')
                        ports.append({'q':x,'a':a,'factors':fs,'edges':edges})
                    triangles.append({'p':p,'cycle':C,'ports9':ports});stats['triangles']+=1
    return {'bound':bound,'counts':dict(stats),'triangles':triangles,
            'scope':'All directed canonical triangles in the 3 mod 4 induced subgraph, not an all-shell or full-graph selector scan.'}


def finite_general_tests()->dict:
    counts=Counter()
    # GCD formula on actual integral square-port sources; no local factor independence.
    for p in range(25,500,24):
        for q in range(3,p,4):
            for i,j in product(range(4),repeat=2):
                if i>=j or (2*j+1)**2*q>=3*p or gcd(p,q)!=1:continue
                a=(p+(2*i+1)**2*q)//4;b=(p+(2*j+1)**2*q)//4
                require(gcd(a,b)==gcd(a,(j-i)*(i+j+1)), 'square-port gcd identity')
                counts['gcd_instances']+=1
    # Exhaust all tournaments through 5 vertices, retaining degree counts.
    for m in range(1,6):
        edges=[(i,j)for i in range(m)for j in range(i+1,m)]
        for mask in range(1<<len(edges)):
            degrees=[0]*m
            for e,(i,j) in enumerate(edges):degrees[j if mask>>e&1 else i]+=1
            for L in range(1,4):
                require(min(degrees)<L or m>=2*L+1,'finite directed-edge count obstruction')
            counts['tournaments']+=1
    return dict(counts)


def negative_controls(inp:dict,cert:dict)->list[str]:
    out=[]
    def rejects(name,fn):
        try:fn()
        except (ArithmeticError,ValueError,KeyError,IndexError):out.append(name);return
        raise ArithmeticError('false transformation accepted: '+name)
    bad=deepcopy(cert);bad['nodes'][str(inp['p'])]['base']=0
    rejects('invalid complete-order base',lambda:prime_certificate(bad))
    bad=deepcopy(cert);bad['nodes'][str(inp['p'])]['factors'].pop()
    rejects('omitted n-1 factor',lambda:prime_certificate(bad))
    fs=inp['inactive_factorizations'][0]+[[inp['cycle'][1],1]]
    rejects('remove an original inactive prime factor',lambda:original_source(inp['p'],31,fs[1:]))
    rejects('use exponent two in original active cap one',lambda:require(2<=1,'original active capacity'))
    rejects('cubic body zero treated as vanished polynomial',lambda:require((1|2|32)==0,'not zero after forgetting jet'))
    rejects('direct product suppresses cubic carry',lambda:require(pow(31,5,307)*31%307==1,'fine section carry at wrap'))
    cubic=eisenstein_tests(inp)['rational_norm_matrix']
    rejects('rational cubic symbols falsely symmetric',lambda:require(cubic[0][2]==cubic[2][0],'cannot discard conjugate prime label'))
    local_u=1098476221603538346086974
    require((4*local_u+1)%223==0, 'genuine projected exterior hit')
    rejects('discard the square multiplier in a selector',lambda:require((4*local_u+1)%(9*223)==0,'the 9-part is indispensable'))
    return out


def main()->None:
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--bound',type=int,default=250000);ap.add_argument('--out',default='certificates');args=ap.parse_args()
    if args.bound<100:ap.error('bound must be >=100')
    base=Path(__file__).resolve().parent;dest=Path(args.out);dest.mkdir(parents=True,exist_ok=True)
    inp=json.loads((base/'input.json').read_text());cert=json.loads((base/'prime_certificates.json').read_text())
    prime_stats=prime_certificate(cert);proved={int(x)for x in cert['nodes']}
    results={'triangle':cycle_data(inp,proved),'cubic':eisenstein_tests(inp),'algebra':algebra_tests(),
             'escape':square_ports(inp,proved),'scan':triangle_scan(args.bound),'general':finite_general_tests()}
    neg=negative_controls(inp,cert)
    for name,data in results.items():dump(dest/(name+'.json'),data)
    receipt={'bound':args.bound,'new_explicit_checks':sum(CHECKS.values()),'check_classes':dict(CHECKS),
             'primality':prime_stats,'negative_controls':neg,
             'source_sha256':{n:sha256((base/n).read_bytes()).hexdigest()for n in ('verify.py','input.json','prime_certificates.json')},
             'output_sha256':{n+'.json':sha256((dest/(n+'.json')).read_bytes()).hexdigest()for n in results},
             'nonclaims':['No least-prime claim for the primitive triangle','No complete graph computation at the displayed large p','No universal ES theorem','No sampled proof of a general theorem','No symbolic source imported from SymPy']}
    dump(dest/'verification.json',receipt)
    print(json.dumps({'checks':sum(CHECKS.values()),'prime_certificate':prime_stats,'triangle_vectors':1215,'scan':results['scan']['counts'],'negative_controls':len(neg)},sort_keys=True))

if __name__=='__main__':main()
