#!/usr/bin/env python3
"""Exact finite certificates for Mellin / tetrahedral / Leech transport.

Python >=3.9, standard library only. No network, no imported prior checker.
Normal and python -O executions have the same mathematical checks.
This verifies finite algebra/data, not analytic convergence or RH/ES.
The general analytic proofs and their imported hypotheses are in note.tex.
"""
from __future__ import annotations
import argparse
import hashlib
import itertools
import json
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

CHECKS=0

def require(condition: bool, message: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise ArithmeticError(message)

def save(path: Path, data) -> None:
    path.write_text(json.dumps(data, indent=2, sort_keys=True)+"\n", encoding="utf8")

P=23
INF=23  # serialization label; geometrically infinity, not the residue 23.
I=(1,0,0,1)
MINUS_I=(22,0,0,22)
C=(12,5,1,12)
J=(1,7,3,22)
T=(4,11,16,4)

def mul(A,B):
    a,b,c,d=A;e,f,g,h=B
    return ((a*e+b*g)%P,(a*f+b*h)%P,(c*e+d*g)%P,(c*f+d*h)%P)
def power(A,n):
    out=I
    for _ in range(n):out=mul(out,A)
    return out

def canonical(A):
    return min(tuple(A), tuple((-v)%P for v in A))

def pmul(A,B):return canonical(mul(A,B))
def inverse(A):
    a,b,c,d=A
    return canonical((d,(-b)%P,(-c)%P,a))

def det(A):a,b,c,d=A;return (a*d-b*c)%P

def permutation(A):
    a,b,c,d=A;out=[]
    for x in range(24):
        n,e=(a,c) if x==INF else ((a*x+b)%P,(c*x+d)%P)
        out.append(INF if e==0 else n*pow(e,-1,P)%P)
    return tuple(out)

def compose(a,b):return tuple(a[b[i]] for i in range(len(a)))

def group(gens):
    identity=canonical(I);result={identity};todo=[identity]
    while todo:
        h=todo.pop()
        for g in gens:
            k=pmul(g,h)
            if k not in result:
                result.add(k);todo.append(k)
    return sorted(result)

def porder(A):
    h=I
    for n in range(1,25):
        h=pmul(h,A)
        if h==canonical(I):return n
    raise ArithmeticError('unexpected projective order >24')

def orbit_cycle(perm,base):
    out=[];x=base
    while x not in out:
        out.append(x);x=perm[x]
    require(x==base,'cycle does not return to base')
    return out

def binary_basis(rows):
    piv={}
    for r0 in rows:
        r=r0
        while r:
            k=r.bit_length()-1
            if k in piv:r^=piv[k]
            else:piv[k]=r;break
    return [piv[k] for k in sorted(piv,reverse=True)]

def codewords(basis):
    out=[0]
    for b in basis:out += [v^b for v in out]
    return sorted(out)

def permute_word(v,p):
    out=0
    while v:
        bit=v&-v;i=bit.bit_length()-1;out|=1<<p[i];v^=bit
    return out

def lattice_member(x,code):
    m=x[0]%2
    if any(v%2!=m for v in x):return False
    if sum(x)%8 != 4*m:return False
    mask=sum(1<<i for i,v in enumerate(x) if ((v-m)//2)%2)
    return mask in code

def min_vectors(code):
    # Unscaled integer vectors; actual vectors are x/sqrt(8).
    for i,j in itertools.combinations(range(24),2):
        for a,b in itertools.product((-4,4),repeat=2):
            x=[0]*24;x[i]=a;x[j]=b;yield 1,tuple(x)
    for c in code:
        if c.bit_count()!=8:continue
        supp=[i for i in range(24) if c>>i&1]
        for signs in range(256):
            if signs.bit_count()%2:continue
            x=[0]*24
            for j,i in enumerate(supp):x[i]=-2 if signs>>j&1 else 2
            yield 2,tuple(x)
    for i in range(24):
        for c in code:
            x=[1-2*((c>>j)&1) for j in range(24)]
            x[i]*=-3
            yield 3,tuple(x)

def imatrix(perm):
    return [[int(perm[j]==i) for j in range(24)] for i in range(24)]
def mm(A,B):
    n=len(A);m=len(B[0]);k=len(B)
    return [[sum(A[i][l]*B[l][j] for l in range(k)) for j in range(m)] for i in range(n)]
def trace(A):return sum(A[i][i] for i in range(len(A)))

UNITS=(1,5,7,11)
CHARACTERS={
    'principal':(1,1,1,1),
    'chi_minus3':(1,-1,1,-1),
    'chi_minus4':(1,1,-1,-1),
    'chi_12':(1,-1,-1,1),
}

def group_certificate(out: Path, do_shell:bool):
    for A in (I,C,J,T):require(det(A)==1,'SL2 determinant')
    require(power(C,3)==MINUS_I,'C^3=-I')
    require(power(J,2)==MINUS_I,'J^2=-I')
    require(power(mul(J,C),3)==I,'(JC)^3=I')
    require(power(T,4)==C,'T^4=C before projectivization')
    require(power(T,12)==MINUS_I,'T^12=-I')
    require(power(T,24)==I,'T^24=I')
    require(porder(T)==12,'T projective order 12')
    cperm=permutation(C);tperm=permutation(T)
    require([cperm[INF],cperm[12],cperm[11]]==[12,11,INF],'root cycle')
    a4=group((J,C));full=group((J,T))
    require(len(a4)==12,'tetrahedral group order')
    require(Counter(porder(g) for g in a4)=={1:1,2:3,3:8},'A4 element orders')
    require(len(full)==6072,'generated PSL2(23)')
    # Exhaust the ambient determinant-one matrices modulo the central sign.
    ambient=set()
    for a,b,c,d in itertools.product(range(P),repeat=4):
        if (a*d-b*c)%P==1:ambient.add(canonical((a,b,c,d)))
    require(set(full)==ambient,'ambient PSL2 equality')
    v4=[I,canonical(J),pmul(pmul(C,J),inverse(C)),pmul(pmul(power(C,2),J),inverse(power(C,2)))]
    gunit=dict(zip(UNITS,v4))
    for u,v in itertools.product(UNITS,repeat=2):
        require(pmul(gunit[u],gunit[v])==canonical(gunit[(u*v)%12]),'unit/V4 homomorphism')
    sigma={1:1,5:7,7:11,11:5}
    for u in UNITS:
        require(pmul(pmul(C,gunit[u]),inverse(C))==canonical(gunit[sigma[u]]),'C semidirect action')
    labels=[]
    for sheet,base in enumerate((INF,0)):
        for u in UNITS:
            for j in range(3):
                g=pmul(gunit[u],power(C,j));point=permutation(g)[base]
                labels.append({'sheet':sheet,'base':base,'face_unit_mod12':u,'root_phase':j,'point':point,'matrix':list(g)})
    require(len({r['point'] for r in labels})==24,'two regular A4 orbits cover P1')
    lookup={r['point']:r for r in labels}
    for r in labels:
        for v in UNITS:
            q=permutation(gunit[v])[r['point']]
            got=lookup[q]
            require((got['sheet'],got['face_unit_mod12'],got['root_phase'])==(r['sheet'],v*r['face_unit_mod12']%12,r['root_phase']),'V4 equivariance')
        got=lookup[cperm[r['point']]]
        require((got['sheet'],got['face_unit_mod12'],got['root_phase'])==(r['sheet'],sigma[r['face_unit_mod12']],(r['root_phase']+1)%3),'C equivariance')
    cycles=[orbit_cycle(tperm,INF),orbit_cycle(tperm,1)]
    require(all(len(cy)==12 for cy in cycles),'two 12 cycles')
    require(set(cycles[0]).isdisjoint(cycles[1]),'disjoint 12 cycles')
    require([cycles[0][i] for i in (0,4,8)]==[INF,12,11],'half roots at phases 0,4,8')
    crossing=Counter((r['sheet'],lookup[tperm[r['point']]]['sheet']) for r in labels)
    require(any(a!=b for a,b in crossing),'T mixes tetrahedral sheets')
    qr={a*a%23 for a in range(1,23)}
    generators=[(1<<INF)|sum(1<<((r+a)%23) for r in qr) for a in range(23)]
    basis=binary_basis(generators);code=codewords(basis);cs=set(code)
    require(len(basis)==12 and len(cs)==4096,'Golay dimension')
    require(Counter(v.bit_count() for v in code)=={0:1,8:759,12:2576,16:759,24:1},'Golay weights')
    for a,b in itertools.product(basis,repeat=2):require((a&b).bit_count()%2==0,'self dual code')
    # Verify every generated permutation, not only a sampled generator.
    for g in full:
        gp=permutation(g)
        require(all(permute_word(b,gp) in cs for b in basis),'full group preserves code')
    seeds=[]
    for i in range(24):
        x=[1]*24;x[i]=-3
        require(lattice_member(x,cs),'marked seed in Leech')
        require(sum(a*a for a in x)==32,'seed norm4')
        seeds.append(x)
    for i,j in itertools.product(range(24),repeat=2):
        require(sum(seeds[i][l]*seeds[j][l] for l in range(24))==8*(4 if i==j else 2),'seed Gram')
        if i!=j:require(sum((seeds[i][l]-seeds[j][l])**2 for l in range(24))==32,'distinct mod12 via norm bound')
    for gp in (permutation(J),cperm,tperm):
        for i in range(24):
            moved=[0]*24
            for k,x in enumerate(seeds[i]):moved[gp[k]]=x
            require(moved==seeds[gp[i]],'seed equivariance')
    counts={}
    digest=hashlib.sha256()
    if do_shell:
        seen=set();counts=Counter()
        for kind,x in min_vectors(code):
            require(lattice_member(x,cs),'minimal vector belongs to lattice')
            require(sum(t*t for t in x)==32,'minimal norm exact')
            require(x not in seen,'minimal vectors unique')
            seen.add(x);counts[kind]+=1;digest.update(bytes(v+8 for v in x))
        require(dict(counts)=={1:1104,2:97152,3:98304},'complete norm4 families')
        require(len(seen)==196560,'Leech kissing shell size')
    matrices={u:imatrix(permutation(gunit[u])) for u in UNITS}
    ns={name:[[sum(vals[k]*matrices[u][i][j] for k,u in enumerate(UNITS)) for j in range(24)] for i in range(24)] for name,vals in CHARACTERS.items()}
    for name,N in ns.items():
        require(trace(N)==24,'projector rank6')
        for name2,M in ns.items():
            require(mm(N,M)==[[4*N[i][j] if name==name2 else 0 for j in range(24)] for i in range(24)],'orthogonal character projectors')
    require([[sum(N[i][j] for N in ns.values()) for j in range(24)] for i in range(24)]==[[4*int(i==j) for j in range(24)] for i in range(24)],'complete character decomposition')
    for phase in range(3):
        inds={r['point'] for r in labels if r['root_phase']==phase}
        require(len(inds)==8,'root phase rank8')
        for N in ns.values():
            require(sum(N[i][i] for i in inds)==8,'joint sector rank2')
            require(all((i in inds)==(j in inds) or N[i][j]==0 for i in range(24) for j in range(24)),'projectors commute')
    # Exact discrepancy bound for the period-12 Dirichlet coefficients.
    discrepancy={}
    for name,vals in CHARACTERS.items():
        mean=F(1,3) if name=='principal' else F(0)
        partial=0;extrema=[]
        for n in range(13):
            if n and n%12 in UNITS:partial+=vals[UNITS.index(n%12)]
            extrema.append(abs(F(partial)-mean*n))
            if n<12:extrema.append(abs(F(partial)-mean*(n+1)))
        mx=max(extrema);require(mx<=2,'Abel partial-sum bound')
        discrepancy[name]=str(mx)
    for m,n in itertools.product(range(1,145),repeat=2):
        if m%12 not in UNITS or n%12 not in UNITS:
            require(m*n%12 not in UNITS,'nonunits retained as zero coefficients')
        else:
            require(pmul(gunit[m%12],gunit[n%12])==canonical(gunit[m*n%12]),'Dirichlet coefficient multiplicativity')
    data={
        'coordinate_infinity_label':INF,'field':23,'SL2_generators':{'J':J,'C':C,'T':T},
        'powers':{'T4':power(T,4),'T12':power(T,12),'T24':power(T,24),'C3':power(C,3),'J2':power(J,2)},
        'A4_order':len(a4),'PSL2_order':len(full),'labels':labels,'T_cycles':cycles,
        'T_sheet_transition_counts':{str(k):v for k,v in crossing.items()},
        'permutations':{'J':permutation(J),'C':cperm,'T':tperm},
        'V4_unit_matrices':{str(k):v for k,v in gunit.items()},
        'code_generators':generators,'code_basis':basis,'code_weights':dict(Counter(v.bit_count() for v in code)),
        'seed_vectors_unscaled':seeds,'seed_gram_diagonal':4,'seed_gram_off_diagonal':2,
        'Leech_mod12_cardinality':12**24,
        'minimal_shell_checked':do_shell,'minimal_shell_counts':dict(counts),
        'minimal_shell_stream_sha256':digest.hexdigest() if do_shell else None,
        'character_table':CHARACTERS,'character_projector_ranks':{k:6 for k in CHARACTERS},
        'joint_character_root_ranks':2,'Abel_discrepancy_bounds':discrepancy,
        'nonclaims':['The A4 torsor is not cyclic of order12.','P1(F23) labels do not replace complex Mellin arguments.','No enumeration of all 12^24 lattice cosets is performed.']}
    save(out/'leech_branches.json',data)
    return data

# Small exact polynomial utilities: coefficients in increasing order.
def add(a,b):
    r=[F(0)]*max(len(a),len(b))
    for i,x in enumerate(a):r[i]+=x
    for i,x in enumerate(b):r[i]+=x
    while len(r)>1 and r[-1]==0:r.pop()
    return r

def scale(a,s):return [F(s)*x for x in a]
def times(a,b):
    r=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):r[i+j]+=x*y
    while len(r)>1 and r[-1]==0:r.pop()
    return r

def derivative(a):return [i*a[i] for i in range(1,len(a))] or [F(0)]
def logD_poly(poly,kappa):
    # D[u^(1/2) P(x)e^-x], D x=x/kappa.
    return add(scale(poly,F(1,2)),times([0,F(1,kappa)],add(derivative(poly),scale(poly,-1))))

def convolve(a,b,n):
    c=[0]*(n+1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<=n:c[i+j]+=x*y
    return c

def sigma(n,k):return sum(d**k for d in range(1,n+1) if n%d==0)

def analytic_algebra_certificate(out:Path):
    # Gamma recurrence for the literal source h gives w(w-1)/8.
    z=[0,F(1,2)]
    moment=scale(add(times(z,add(z,[1])),scale(z,F(-3,2))),F(1,2))
    require(moment==[0,F(-1,8),F(1,8)],'literal CCM Mellin factor')
    for k in (F(1,2),F(1),F(2),F(12)):
        got=scale(add(logD_poly(logD_poly([F(1)],k),k),[F(-1,4)]),F(1,2))
        want=[0,-(k+1)/(2*k*k),1/(2*k*k)]
        require(got==want,'canonical theta-kernel differential polynomial')
        # Mellin gamma recurrence: Gamma(w+2)-(k+1)Gamma(w+1).
        w=[0,F(1)]
        got=add(times(w,add(w,[1])),scale(w,-(k+1)))
        require(got==[0,-k,1],'Mellin theta factor w(w-k)')
    # h=(t^2-3t/2)e^-t; critical t=1/2,3 for derivative.
    require(times([F(-1,2),1],[-3,1])==[F(3,2),F(-7,2),1],'variation extrema polynomial')
    # Gamma/normalization and Leech prefactors.
    require(F(12,2)*F(65520,691)==F(393120,691),'Leech completed Dirichlet prefactor')
    require(4*F(1,8)==F(1,2),'source normalization factor4')
    require(F(1,2)/(F(12)**2)==F(1,288),'Leech differential prefactor')
    n=40
    delta=[1]+[0]*n
    from math import comb
    for m in range(1,n+1):
        f=[0]*(n+1)
        for j in range(min(24,n//m)+1):f[j*m]=(-1)**j*comb(24,j)
        delta=convolve(delta,f,n)
    delta=[0]+delta[:n]
    E4=[1]+[240*sigma(i,3) for i in range(1,n+1)]
    cube=convolve(convolve(E4,E4,n),E4,n)
    theta=[cube[i]-720*delta[i] for i in range(n+1)]
    for i in range(1,n+1):
        require(F(65520,691)*(sigma(i,11)-delta[i])==theta[i],'Leech theta two formulas')
        require(theta[i]>=0,'finite theta coefficients nonnegative')
    require(theta[:5]==[1,0,196560,16773120,398034000],'first theta coefficients')
    # Rational Mobius root cycle c(z)=(2z-3)/(4z+2), with c^3=-64 I.
    def qmul(A,B):
        return tuple(sum(A[2*i+k]*B[2*k+j] for k in range(2)) for i in range(2) for j in range(2))
    cm=(2,-3,4,2)
    require(qmul(qmul(cm,cm),cm)==(-64,0,0,-64),'rational projective three-cycle')
    require(tuple(int(F(x,4).numerator*pow(F(x,4).denominator,-1,23)%23) for x in cm)==C,'root-cycle reduction to SL2(F23)')
    # Residue-chart denominator 2 is invertible; no root collision.
    require(pow(2,-1,23)==12 and (-pow(2,-1,23))%23==11,'half-root specialization')
    data={
        'source_h_mellin_gamma_polynomial':[str(v) for v in moment],
        'source_literal_transform':'M(E h)(s) = xi(s+1/2)/4',
        'canonical_kernel':'K_L(u)=(1/2)(D_u^2-1/4)[u^(1/2) Theta_L(u^(1/kappa))]',
        'canonical_transform':'M K_L(s)=(kappa/2)(s^2-1/4) pi^(-w) Gamma(w) Z_L(w), w=kappa(s+1/2)',
        'canonical_endpoint_values':{'plus_half':'1/2','minus_half':'1/2'},
        'Leech_kappa':12,'Leech_prefactor':'393120/691','Leech_dirichlet_expression':'zeta(w) zeta(w-11) - L(Delta,w)',
        'theta_coefficients_0_to_40':theta,'Ramanujan_tau_0_to_40':delta,
        'finite_precision_or_sampling_used':False,
        'convergence_constant':'(4 C+8 V_h)/epsilon, V_h=exp(-1/2)+9 exp(-3)',
        'nonclaims':['The executable checks algebraic factors, not integrals at all complex arguments.','Theta modularity, Poisson summation and analytic convergence have written proofs or named primary dependencies.','No numerical kernel sampling certifies eigenfunction approximation.']}
    save(out/'analytic_constants.json',data)
    return data

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out',type=Path,default=Path('certificates'))
    ap.add_argument('--skip-minimal-shell',action='store_true',help='Skip the explicit 196560-vector replay; record that omission.')
    args=ap.parse_args();args.out.mkdir(parents=True,exist_ok=True)
    g=group_certificate(args.out,not args.skip_minimal_shell)
    a=analytic_algebra_certificate(args.out)
    receipt={
        'status':'PASS','exact_check_count':CHECKS,
        'A4_order':g['A4_order'],'generated_PSL2_order':g['PSL2_order'],
        'Golay_codewords':4096,'minimal_shell_vectors':sum(g['minimal_shell_counts'].values()),
        'source_normalization_factor':4,'theta_coefficients_checked':40,
        'stdlib_only':True,'network_access':False,'prior_checker_imports':False,
        'scope':'Finite exact algebra, full code/group replay, branch maps, minimal-shell membership, formal Mellin factors; no analytic theorem-prover run.'}
    save(args.out/'finite_receipt.json',receipt)
    print(json.dumps(receipt,sort_keys=True))

if __name__=='__main__':main()
