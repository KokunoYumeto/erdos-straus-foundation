#!/usr/bin/env python3
"""Exact mixed-support ES certificates; standard library only.

Default finite scopes: the pinned 9702-state hard shell; all first-half shells
of primes p=1 mod 12 through 1500; finite matrix/filter fixtures. No universal
ES theorem, new prime-coverage result, or independent review is asserted.
Checks are explicit and remain active under python -O.
"""
from __future__ import annotations
import argparse, gzip, hashlib, json
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, product
from math import gcd, isqrt, prod
from pathlib import Path

CHECKS = Counter()
ROOT = Path(__file__).resolve().parent
P = 2671180768668258904496300170662649
FACTORS = ((2,5),(431,3),(457,3),(7229,4))
R = 135

def check(ok, label):
    CHECKS[label] += 1
    if not ok: raise ArithmeticError(label)

def transpose(A): return list(map(list,zip(*A))) if A else []
def mm(A,B):
    if not A: return []
    return [[sum((x*y for x,y in zip(row,col)),F()) for col in zip(*B)] for row in A]
def add(A,B): return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]
def scale(A,s): return [[s*x for x in row] for row in A]
def eye(n):return [[F(int(i==j)) for j in range(n)] for i in range(n)]
def qform(A,v):return sum((v[i]*A[i][j]*v[j] for i in range(len(v)) for j in range(len(v))),F())
def determinant(A):
    if not A:return F(1)
    B=[list(map(F,row)) for row in A];n=len(B);d=F(1)
    for c in range(n):
        k=next((i for i in range(c,n) if B[i][c]),None)
        if k is None:return F(0)
        if k!=c:B[k],B[c]=B[c],B[k];d=-d
        z=B[c][c];d*=z
        for i in range(c+1,n):
            t=B[i][c]/z
            for j in range(c+1,n):B[i][j]-=t*B[c][j]
    return d

def inverse(A):
    n=len(A);B=[list(map(F,row))+eye(n)[i] for i,row in enumerate(A)]
    for c in range(n):
        k=next((i for i in range(c,n) if B[i][c]),None)
        if k is None:raise ValueError('singular matrix; no inverse supplied')
        B[k],B[c]=B[c],B[k];z=B[c][c];B[c]=[x/z for x in B[c]]
        for i in range(n):
            if i!=c:
                t=B[i][c];B[i]=[x-t*y for x,y in zip(B[i],B[c])]
    X=[row[n:] for row in B]
    check(mm(A,X)==eye(n),'inverse_identity')
    return X

def inertia(A):
    """Exact congruence elimination, including zero diagonals and 2x2 pivots."""
    B=[list(map(F,row)) for row in A];pos=neg=zero=0
    while B:
        n=len(B);k=next((i for i in range(n) if B[i][i]),None)
        if k is not None:
            order=[k]+[i for i in range(n) if i!=k]
            B=[[B[i][j] for j in order] for i in order];z=B[0][0]
            pos+=z>0;neg+=z<0
            B=[[B[i][j]-B[i][0]*B[0][j]/z for j in range(1,n)] for i in range(1,n)]
        else:
            ij=next(((i,j) for i in range(n) for j in range(i+1,n) if B[i][j]),None)
            if ij is None:zero+=n;break
            i,j=ij;order=[i,j]+[k for k in range(n) if k not in (i,j)]
            B=[[B[i][j] for j in order] for i in order];z=B[0][1]
            pos+=1;neg+=1
            B=[[B[i][j]-(B[i][0]*B[1][j]+B[i][1]*B[0][j])/z
                for j in range(2,n)] for i in range(2,n)]
    return (pos,neg,zero)

def factor(n):
    if n<1:raise ValueError('positive integer')
    ans=[];q=2
    while q*q<=n:
        e=0
        while n%q==0:n//=q;e+=1
        if e:ans.append((q,e))
        q=3 if q==2 else q+2
    if n>1:ans.append((n,1))
    return ans

def trial_prime(n):
    return n>=2 and (n==2 or n%2 and all(n%d for d in range(3,isqrt(n)+1,2)))

def verify_prime(proof):
    table=proof['proof'];seen={};visiting=set()
    def visit(n):
        if n in seen:return
        if str(n) not in table:
            check(n<1000000,'bounded_primality_leaf')
            check(trial_prime(n),'trial_prime_leaf');seen[n]='trial';return
        check(n not in visiting,'acyclic_primality_graph');visiting.add(n)
        node=table[str(n)];fs=node['factorization'];a=node['base']
        check(node['n']==n and prod(q**e for q,e in fs)==n-1,'complete_n_minus_one')
        check(len(set(q for q,e in fs))==len(fs) and all(e>0 for q,e in fs),'prime_factor_marking')
        check(pow(a,n-1,n)==1,'order_fermat')
        for q,e in fs:
            visit(q);check(gcd(pow(a,(n-1)//q,n)-1,n)==1,'full_order_prime_factor')
        seen[n]='full-order';visiting.remove(n)
    visit(proof['root']);check(proof['root']==P,'correct_prime_root')
    return dict(root=P,nodes=len(seen),full_order_nodes=sum(s=='full-order' for s in seen.values()),
                trial_nodes=sorted(n for n,s in seen.items() if s=='trial'))

def box(e):return product(*(range(-d,d+1) for d in e))
def shell_rows(p,fs,R=None):
    a=prod(q**e for q,e in fs);R=4*a-p if R is None else R
    check(4*a==p+R and 0<R<p and R%4==3 and gcd(p*a,R)==1,'arithmetic_shell_domain')
    out=[]
    for beta in box(tuple(e for q,e in fs)):
        u=prod(q**(e+b) for (q,e),b in zip(fs,beta))
        for channel in ('E','M'):
            gate=4*u+1 if channel=='E' else u+a
            q=gcd(R,gate);D=R//q
            out.append(dict(p=p,a=a,R=R,channel=channel,beta=beta,u=u,gate=gate,gcd=q,D=D))
    return out

def reconstruct(row):
    p,a,R,u=(row[k] for k in ('p','a','R','u'));d=gcd(a,u)
    h=d*d//u;r=u//d;s=a//d;c=row['channel']
    check(d*d%u==0 and h*r*s==a and h*r*r==u and gcd(r,s)==1,'canonical_normalization')
    quot=F(p*r+s if c=='E' else r+s,R)
    den=(F(a),h*s*quot*(p if c=='M' else 1),p*h*r*quot)
    check(all(x>0 for x in den) and sum((1/x for x in den),F())==F(4,p),'positive_rational_identity')
    check(den[1].denominator==den[2].denominator==row['D'],'exact_return_denominator')
    back=F(a*a*(p if c=='M' else 1),R*den[1]-p*a)
    check(back==u,'ordered_divisor_inverse')
    return dict(row,h=h,r=r,s=s,quotient_name='kappa' if c=='E' else 'lambda',
                quotient=quot,denominators=den)

def poly_mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

def phi_coeff(j):
    p=[F(0),F(1)]
    for n in range(1,j+1):p=poly_mul(p,[F(-1,2*n),F(2*n+1,2*n)])
    return p

def ev(p,x):
    v=F(0)
    for a in reversed(p):v=v*x+a
    return v

def feature(row,index=2):
    x=F(1,row['D']);return [F(1),x*(row['channel']=='E'),x*(row['beta'][index]>0)]

def gram(rows,weight,index=2):
    G=[[F(0)]*3 for _ in range(3)]
    for row in rows:
        f=feature(row,index);w=weight(row)
        for i in range(3):
            for j in range(i,3):G[i][j]+=w*f[i]*f[j]
    for i in range(3):
        for j in range(i):G[i][j]=G[j][i]
    return G

def cell_moments(rows,index):
    C={str((e,b)):[0]*5 for e,b in product((0,1),repeat=2)}
    H={k:Counter() for k in C}
    for row in rows:
        key=str((int(row['channel']=='E'),int(row['beta'][index]>0)));q=row['gcd']
        for j in range(5):C[key][j]+=q**j
        H[key][row['D']]+=1
    return C,H

def moment_gram(C,R):
    def S(j,pred):return sum(v[j] for key,v in C.items() if pred(key))
    all_=lambda key:True;E=lambda key:key.startswith('(1,');B=lambda key:key.endswith('1)')
    both=lambda key:E(key) and B(key)
    A0=R*R*(3*S(1,all_)-R*S(0,all_))
    a=R*(3*S(2,E)-R*S(1,E));b=R*(3*S(2,B)-R*S(1,B))
    c=3*S(3,E)-R*S(2,E);d=3*S(3,B)-R*S(2,B)
    z=3*S(3,both)-R*S(2,both)
    return [[A0,a,b],[a,c,z],[b,z,d]]

def group_certificate(fs,a,R,index):
    # Finite multiplication keeps the entire exponent-budget correlation.
    mu=Counter({(1,0):1})
    for i,(q,e) in enumerate(fs):
        part=Counter((pow(q,t,R),int(t>e) if i==index else 0) for t in range(2*e+1))
        nxt=Counter()
        for (r,b),n in mu.items():
            for (s,c),m in part.items():nxt[(r*s%R,int(b or c))]+=n*m
        mu=nxt
    C={str((e,b)):[0]*5 for e,b in product((0,1),repeat=2)}
    for (u,b),n in mu.items():
        for e,gate in ((1,4*u+1),(0,u+a)):
            q=gcd(R,gate)
            for j in range(5):C[str((e,b))][j]+=n*q**j
    return C,[[r,b,n] for (r,b),n in sorted(mu.items())]

def hard_certificate():
    for q,e in FACTORS:check(trial_prime(q),'base_factor_prime')
    rows=shell_rows(P,FACTORS,R)
    returned=[reconstruct(r) for r in rows]
    hits=[r for r in returned if r['D']==1]
    C,hists=cell_moments(rows,2);GC,gpoly=group_certificate(FACTORS,rows[0]['a'],R,2)
    check(C==GC,'full_common_vector_group_polynomial')
    N=moment_gram(C,R)
    J=gram(rows,lambda r:F(1,r['D'])-F(1,3));K=gram(rows,lambda r:F(1))
    check(scale(J,3*R**3)==N,'integer_moment_matrix')
    pairs=[]
    for I in combinations(range(3),2):
        G=[[N[i][j] for j in I] for i in I]
        check(inertia(G)==(0,2,0),'every_coordinate_pair_negative_definite')
        pairs.append(dict(indices=I,determinant=determinant(G)))
    check(inertia(N)==(1,2,0) and determinant(N)>0,'ternary_positive_direction')
    v=(-1,36,36);norm=71
    Q=F(3,2)*qform(J,v)/norm**2
    check(Q==F(607462,1890375) and 0<Q<1,'simple_positive_certificate')
    check(max(abs(v[0]+v[1]*b+v[2]*c) for b,c in product((0,1),repeat=2))==norm,'success_amplitude_bound_without_hit_selection')
    check(Q<=len(hits) and len(hits)==3,'original_hit_count')
    # Complete signed Schur coordinate transformation, first pivot negative.
    aa=-F(N[0][0]);bb=list(map(F,N[0][1:]));CC=[[F(N[i][j]) for j in (1,2)] for i in (1,2)]
    T=[[F(1),bb[0]/aa,bb[1]/aa],[F(0),F(1),F(0)],[F(0),F(0),F(1)]]
    S=[[CC[i][j]+bb[i]*bb[j]/aa for j in range(2)] for i in range(2)]
    target=[[-aa,F(0),F(0)],[F(0),*S[0]],[F(0),*S[1]]]
    check(mm(transpose(T),mm(N,T))==target,'signed_schur_congruence')
    check(mm(inverse(T),T)==eye(3),'schur_coordinate_return')
    check(S[0][0]<0 and S[1][1]<0 and determinant(S)<0,'conditional_mixed_overlap_crosses_threshold')
    # Original (positive) metric is separate from the signed form.
    Ki=inverse(K);M1=gram(rows,lambda r:F(1,r['D']));M2=gram(rows,lambda r:F(1,r['D']**2))
    defect=add(M2,scale(mm(M1,mm(Ki,M1)),-1))
    check(inertia(defect)[1]==0 and any(x for row in defect for x in row),'nonzero_functional_calculus_defect')
    # Full image inverse through three actually present coordinate readings.
    piv=[next(r for r in rows if r['channel']=='M' and r['u']==1),
         next(r for r in rows if r['channel']=='E' and r['u']==1),
         next(r for r in rows if r['channel']=='M' and r['u']==457**4)]
    pivot_matrix=[feature(r) for r in piv];pinv=inverse(pivot_matrix)
    check(mm(pinv,pivot_matrix)==eye(3),'mixed_source_image_inverse')
    baseline={}
    for channel in ('E','M','both'):
        ss=[r for r in rows if channel=='both' or r['channel']==channel]
        m=[sum((F(1,r['D']**k) for r in ss),F()) for k in range(4)]
        B=[[m[1]-m[0]/3,m[2]-m[1]/3],[m[2]-m[1]/3,m[3]-m[2]/3]]
        check(inertia(B)[0]==0,'all_scalar_degree_one_baselines_fail')
        baseline[channel]=dict(moments=m,matrix=B,inertia=inertia(B))
    return dict(p=P,a=rows[0]['a'],R=R,factors=FACTORS,index=2,support_definition='E and beta_457 > 0',
                candidates=len(rows),hits=hits,cell_gcd_moments=C,cell_defect_histograms=hists,
                residue_polynomial=gpoly,J_integer=N,J_scale=3*R**3,ordinary_Gram=K,
                pair_certificates=pairs,determinant=determinant(N),trial=v,normalizer=norm,lower=Q,
                Schur_change=T,Schur_inverse=inverse(T),Schur_remaining=S,
                pivot_leaves=piv,pivot_image_inverse=pinv,compression_defect=defect,
                scalar_baselines=baseline),returned

def split_certificate(rows):
    e=tuple(d for q,d in FACTORS);f=(5,2,2,4);b=(0,1,1,0)
    original={(r['beta'],r['channel']):r for r in rows}
    counts=Counter();raw_hits=0;mass=F(0);hit_mass=F(0)
    J=[[F(0)]*3 for _ in range(3)];K=[[F(0)]*3 for _ in range(3)]
    badJ=[[F(0)]*3 for _ in range(3)]
    for xi in box(f):
        for eta in box(b):
            beta=tuple(x+y for x,y in zip(xi,eta))
            n=prod(min(fi,be+bi)-max(-fi,be-bi)+1 for fi,bi,be in zip(f,b,beta))
            check(n>0,'split_fibre_nonempty')
            for c in ('E','M'):
                row=original[(beta,c)];counts[(beta,c)]+=1;x=F(1,row['D']);wt=F(1,n);z=feature(row)
                wrong=[F(1),x*(c=='E'),x*(xi[2]>0)]
                mass+=wt;raw_hits+=row['D']==1;hit_mass+=wt*(row['D']==1)
                for i in range(3):
                    for j in range(3):
                        K[i][j]+=wt*z[i]*z[j];J[i][j]+=wt*(x-F(1,3))*z[i]*z[j]
                        badJ[i][j]+=wt*(x-F(1,3))*wrong[i]*wrong[j]
    for (beta,c),n in counts.items():
        expected=prod(min(fi,be+bi)-max(-fi,be-bi)+1 for fi,bi,be in zip(f,b,beta))
        check(n==expected,'complete_split_fibre_size')
    check(mass==len(rows) and hit_mass==3 and raw_hits==7,'original_mass_not_occurrence_mass')
    check(K==gram(rows,lambda r:F(1)) and J==gram(rows,lambda r:F(1,r['D'])-F(1,3)),'both_mixed_Grams_preserved_by_split')
    check(badJ!=J,'support_predicate_must_use_original_beta')
    return dict(f=f,b=b,occurrences=sum(counts.values()),original_mass=mass,raw_hit_occurrences=raw_hits,
                original_hits=hit_mass,K=K,J=J,incorrect_partial_exponent_J=badJ)

def compression_counterexample():
    rows=shell_rows(37,((2,1),(3,2)),35)
    check(all(z['D']>1 for z in rows),'complete_restricted_shell_empty')
    r=[reconstruct(next(z for z in rows if z['channel']=='E' and z['u']==u)) for u in (1,12)]
    xs=[F(1,z['D']) for z in r];average=sum(xs)/2
    coeff=phi_coeff(3);original=sum(ev(coeff,x) for x in xs)/2;wrong=ev(coeff,average)
    check(xs==[F(1,7),F(1,5)] and original==0 and wrong==F(17,343000),'compression_filter_counterexample')
    variance=sum(x*x for x in xs)/2-average**2
    check(variance==F(1,1225),'original_relation_norm_for_compression')
    return dict(states=r,constant_source_Gram=2,compressed_X=average,correct_compressed_Phi3=original,
                incorrect_Phi3_of_compressed_X=wrong,quadratic_compression_defect=variance)

def fixture_tests():
    cases=0
    # All symmetric 3x3 integer forms in a fixed exact coefficient cube.
    for entries in product(range(-1,2),repeat=6):
        a,b,c,d,e,f=entries;M=[[a,b,c],[b,d,e],[c,e,f]]
        nsd=all(M[i][i]<=0 for i in range(3)) and all(determinant([[M[i][j] for j in I] for i in I])>=0 for I in combinations(range(3),2)) and determinant(M)<=0
        check(nsd==(inertia(M)[0]==0),'full_principal_minor_criterion_including_singular_boundary');cases+=1
    # Nonorthogonal, overlapping, possibly rank-deficient source maps.
    xs=[F(1),F(1,3),F(1,5),F(1,7)]
    fixture_count=0
    for Aset in product((0,1),repeat=4):
        for Bset in product((0,1),repeat=4):
            A=[[F(1),x*a,x*b] for x,a,b in zip(xs,Aset,Bset)]
            K=mm(transpose(A),A)
            hit=[[A[0][i]*A[0][j] for j in range(3)] for i in range(3)]
            signed=mm(transpose(A),[[F(3,2)*(x-F(1,3))*v for v in row] for x,row in zip(xs,A)])
            check(inertia(signed)[0]<=1,'positive_inertia_bounded_by_actual_successes')
            for n in range(5):
                coeff=phi_coeff(n);eps=F(1,2**n*__import__('math').factorial(n)*(2*n+3))
                Q=mm(transpose(A),[[ev(coeff,x)*v for v in row] for x,row in zip(xs,A)])
                diff=add(Q,scale(hit,-1));oriented=scale(diff,1 if n%2==0 else -1)
                check(inertia(oriented)[1]==0,'one_sided_mixed_filter_order')
                check(inertia(add(scale(K,eps),scale(oriented,-1)))[1]==0,'uniform_error_in_actual_source_Gram')
            fixture_count+=1
    return dict(integer_symmetric_forms=cases,mixed_filter_sources=fixture_count,filter_degrees=list(range(5)))

def scan(bound):
    stats=Counter();first=[]
    for p in range(13,bound+1,12):
        if not trial_prime(p):continue
        stats['primes']+=1
        for a in range((p+3)//4,(p-1)//2+1):
            fs=factor(a);rows=shell_rows(p,fs);R=4*a-p;H=sum(r['D']==1 for r in rows)
            stats['shells']+=1;stats['original_states']+=len(rows);stats['occupied_shells']+=H>0
            hit=False;strict=False
            for i in range(len(fs)):
                C,_=cell_moments(rows,i);N=moment_gram(C,R);sig=inertia(N);forced=sig[0]>0
                binary=all(inertia([[N[j][k] for k in I] for j in I])[0]==0 for I in combinations(range(3),2))
                three=forced and binary
                check(not forced or H>0,'scan_no_false_positive');stats['support_choices']+=1
                stats['certified_choices']+=forced;stats['strict_ternary_choices']+=three
                hit|=forced;strict|=three
                if three and len(first)<10:first.append(dict(p=p,a=a,R=R,prime=fs[i][0],H=H,N=N))
            stats['certified_shells']+=hit;stats['strict_ternary_shells']+=strict
    return dict(bound=bound,scope='all first-half shells at prime p=1 mod12; supports E and beta_q>0 for every prime q|a',counts=dict(stats),first_strict=first)

def negative_controls(cert,split,compression):
    out=[]
    def rejects(label,fn):
        try:fn()
        except (ArithmeticError,ValueError):out.append(label);return
        raise ArithmeticError('accepted a false control: '+label)
    rejects('pairwise negativity implies joint negativity',lambda:check(inertia(cert['J_integer'])[0]==0,'bad_binary_to_ternary'))
    rejects('delete mixed cross terms',lambda:check(cert['J_integer'][1][2]==0,'bad_cross_erasure'))
    rejects('raw split occurrences are original hit count',lambda:check(split['raw_hit_occurrences']==split['original_hits'],'bad_occurrence_count'))
    rejects('partial exponent is the original support predicate',lambda:check(split['incorrect_partial_exponent_J']==split['J'],'bad_partial_support'))
    rejects('functional calculus commutes with arbitrary compression',lambda:check(compression['correct_compressed_Phi3']==compression['incorrect_Phi3_of_compressed_X'],'bad_compression_order'))
    rejects('invert a singular source Gram',lambda:inverse([[1,1],[1,1]]))
    return out

def encode(x):
    if isinstance(x,F):return {'numerator':x.numerator,'denominator':x.denominator}
    if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [encode(v) for v in x]
    return x

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--out',default='generated');ap.add_argument('--bound',type=int,default=1500)
    args=ap.parse_args()
    if not 13<=args.bound<=100000:ap.error('finite scan bound must be between 13 and 100000')
    dest=Path(args.out);dest.mkdir(parents=True,exist_ok=True)
    prime=verify_prime(json.loads((ROOT/'prime_certificate.json').read_text()))
    hard,rows=hard_certificate();split=split_certificate(rows);compression=compression_counterexample()
    fixtures=fixture_tests();scanned=scan(args.bound);neg=negative_controls(hard,split,compression)
    outputs={'hard_ternary.json':hard,'split_return.json':split,'compression_counterexample.json':compression,
             'fixtures.json':fixtures,'scan.json':scanned,'primality.json':prime,'negative_controls.json':neg,'checks.json':dict(CHECKS)}
    for name,data in outputs.items():(dest/name).write_text(json.dumps(encode(data),indent=2,sort_keys=True)+'\n')
    raw=(json.dumps(encode(dict(p=P,R=R,factors=FACTORS,scope='complete single-shell canonical source; original labels retained',states=rows)),sort_keys=True,separators=(',',':'))+'\n').encode()
    (dest/'original_states.json.gz').write_bytes(gzip.compress(raw,mtime=0))
    print(json.dumps(dict(checks=sum(CHECKS.values()),candidates=len(rows),hard_lower=encode(hard['lower']),
                         negative_controls=len(neg),scan=scanned['counts']),sort_keys=True))
if __name__=='__main__':main()
