#!/usr/bin/env python3
"""Separate direct-divisor check of the supplied Turn-1 arithmetic ledger.
Imports neither verify.py nor predecessor software. Standard library only.
This recomputes each supplied row but does not independently enumerate the
prime/shell domain or certify that the input ledger is complete.
"""
import argparse,json,math,hashlib
from pathlib import Path
from collections import Counter
from functools import lru_cache
C=Counter()
def test(ok,label):
    C[label]+=1
    if not ok:raise ArithmeticError(label)
@lru_cache(None)
def decomposition(n):
    r=[];q=2
    while q*q<=n:
        e=0
        while n%q==0:n//=q;e+=1
        if e:r.append((q,e))
        q=3 if q==2 else q+2
    if n>1:r.append((n,1))
    return r

def divisors_square(a):
    D=[1]
    for q,e in decomposition(a):D=[d*q**j for d in D for j in range(2*e+1)]
    return D

def subgroup(gens,R):
    # Add complete cosets of the existing subgroup, not a BFS on generators.
    H={1}
    for g in gens:
        g%=R
        if g in H:continue
        old=set(H);v=g
        while v not in old:
            H.update(v*x%R for x in old);v=v*g%R
    return H

def qorder(g,R,K):
    v=g;d=1
    while v not in K:v=v*g%R;d+=1
    return d

def classify(Gamma,K,fac,p,R):
    # Only small quotients need element-order classification. This guard is
    # before order enumeration; the complete arithmetic row was checked above.
    d=len(Gamma)//len(K)
    if d>8:return None
    rep=lambda x:min(x*k%R for k in K)
    A={rep(x) for x in Gamma}
    active=[(q,e,rep(q)) for q,e in fac if q%R not in K]
    E=sum(e for q,e,g in active);alpha=rep(R-1);z=rep(2);eta=rep(p)
    order=lambda g:qorder(g,R,K)
    exponent=max(order(g) for g in A)
    if d>8:return None
    if not active:
        if d==2:out='P2';ok=eta==1
        elif d==4:out='P4_V4';ok=exponent==2 and eta==1
        elif d==6:out='P6';ok=order(eta)==3
        elif exponent==8:out='P8_C8';ok=order(z)==8 and eta==rep(z*z)
        else:out='P8_C4xC2';ok=d==8 and exponent==4 and order(z)==4 and alpha not in {rep(pow(z,j,R)) for j in range(4)}
    else:
        g=active[0][2];inv=rep(pow(g,-1,R));allpair=all(h in {g,inv} for q,e,h in active)
        if d==6:
            out='A6_single' if E==1 else 'A6_double'
            ok=order(g)==6 and allpair and ((E==1 and eta in {g,inv}) or (E==2 and eta==1))
        elif d==8 and exponent==8:
            if E==1 and order(g)==4:out='A8_order4';ok=eta==1
            elif E==1:out='A8_single';ok=order(g)==8 and eta in {g,inv}
            else:out='A8_double';ok=E==2 and order(g)==8 and allpair and eta==1
        else:
            out='A8_product_single';ok=d==8 and exponent==4 and E==1 and order(g)==4 and eta in {g,inv} and alpha not in {rep(pow(g,j,R)) for j in range(4)}
    test(ok,'separate low-index conditions')
    B=math.prod(q**e for q,e in fac if q%R in K)
    WB={u*pow(B,-1,R)%R for u in divisors_square(B)}
    test(WB==K and E<=2,'separate saturated inactive source')
    return out

def verify_row(row):
    p,a,nE,nM,Ksaved,ambient,effective,Emass,tau,normal=row
    R=4*a-p;D=divisors_square(a);ainv=pow(a,-1,R)
    mu=Counter(u*ainv%R for u in D)
    E=sum((4*u+1)%R==0 for u in D);M=sum((u+a)%R==0 for u in D)
    test((E,M)==(nE,nM),'direct original channel counts')
    if E+M:return row
    W=set(mu);K={g for g in W if {g*x%R for x in W}==W}
    test(K==set(Ksaved),'direct actual stabilizer')
    fac=decomposition(a);Gamma=subgroup([2,R-1]+[q for q,e in fac],R)
    test(len(Gamma)//len(K)==effective,'direct effective envelope')
    full_phi=R
    for q,e in decomposition(R):full_phi=full_phi//q*(q-1)
    test(full_phi//len(K)==ambient,'direct ambient index')
    rep=lambda x:min(x*k%R for k in K)
    F={rep(R-1),rep(-p%R),rep(-pow(p,-1,R)%R)}
    Eactive=sum(e for q,e in fac if q%R not in K)
    test((len(F),Eactive)==(tau,Emass),'direct labels and active capacities')
    test(2*Eactive<=effective-1-len(F),'direct joint growth inequality')
    test(classify(Gamma,K,fac,p,R)==normal,'direct low-index row')
    return row

def all_states(example):
    p=example['p'];a=example['a'];R=4*a-p;found=[]
    for u in divisors_square(a):
        for tag in ('E','M'):
            if ((4*u+1) if tag=='E' else (u+a))%R:continue
            if tag=='E':y=(p*a+a*a//u)//R;z=(p*a+p*p*u)//R
            else:y=p*(a+a*a//u)//R;z=p*(a+u)//R
            test(4*a*y*z==p*(a*y+a*z+y*z),'separate factor-pair reciprocal return')
            found.append((tag,u,(a,y,z)))
    expected=[(x['channel'],x['u'],tuple(x['denominators'])) for x in example['hits']]
    test(sorted(found)==sorted(expected),'all ordered example states')
    test(all(p%d for d in range(2,math.isqrt(p)+1)),'example trial primality')

# Complete intrinsic low-group enumeration with positive rather than centered boxes.
def finite_groups():
    records=Counter();total=0
    import itertools as I
    for dims in [(2,),(4,),(2,2),(6,),(8,),(4,2),(2,2,2)]:
        G=list(I.product(*(range(n) for n in dims)));zero=tuple(0 for _ in dims);N=len(G)
        add=lambda x,y:tuple((a+b)%m for a,b,m in zip(x,y,dims))
        times=lambda n,x:tuple(n*a%m for a,m in zip(x,dims))
        def generated(gs):
            H={zero}
            for g in gs:
                H={add(h,times(j,g)) for h in H for j in range(N)}
            return H
        # Treat the total capacity as a list of individual occurrences, then
        # retain every way to group equal generators into distinct primes.
        atoms=[(g,e) for g in G if g!=zero for e in (1,2,3)]
        for length in range(4):
            for prof in I.combinations_with_replacement(atoms,length):
                E=sum(e for g,e in prof)
                if E>3:continue
                shift=zero;V={zero}
                for g,e in prof:
                    shift=add(shift,times(-e,g))
                    V={add(x,times(j,g)) for x in V for j in range(2*e+1)}
                S={add(x,shift) for x in V}
                if any(h!=zero and {add(x,h) for x in S}==S for h in G):continue
                for alpha in G:
                    if alpha==zero or times(2,alpha)!=zero:continue
                    for z in G:
                        if len(generated([alpha,z]+[g for g,e in prof]))!=N:continue
                        eta=times(2,z)
                        for g,e in prof:eta=add(eta,times(e,g))
                        F={alpha,add(alpha,eta),add(alpha,times(-1,eta))}
                        total+=1
                        if F&S:continue
                        test(E<=2,'separate abstract occurrence bound')
                        records[str(dims)]+=1
    return dict(aperiodic_anchored_models=total,failed_by_group=dict(records))

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--input',default='certificates');ap.add_argument('--out',default='independent.json');args=ap.parse_args()
    inp=Path(args.input);scan=json.loads((inp/'scan.json').read_text());examples=json.loads((inp/'examples.json').read_text())
    rows=[verify_row(r) for r in scan['rows']]
    digest=hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()
    test(digest==scan['row_sha256'],'complete arithmetic ledger digest')
    for ex in examples:all_states(ex)
    groups=finite_groups()
    test(groups['aperiodic_anchored_models']==596 and sum(groups['failed_by_group'].values())==146,'separate complete abstract counts')
    for i in range(6):
        for j in range(6):test(pow(2,i,19)*pow(2,j,19)%19==pow(2,(i+j)%6,19)*pow(7,(i+j)//6,19)%19,'explicit C18 carry')
    report=dict(bound=scan['bound'],rows=len(rows),row_sha256=digest,checks=sum(C.values()),check_counts=dict(C),abstract=groups,
                nonclaims=['No import from main verifier or predecessor','No independent mathematical review','No ES counterexample or universal occupancy claim'])
    Path(args.out).write_text(json.dumps(report,indent=2,sort_keys=True)+'\n');print(json.dumps({k:report[k] for k in ('bound','rows','checks','row_sha256')},sort_keys=True))
if __name__=='__main__':main()
