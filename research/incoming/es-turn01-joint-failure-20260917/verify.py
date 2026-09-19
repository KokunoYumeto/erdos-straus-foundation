#!/usr/bin/env python3
"""Exact Turn-1 ES joint-obstruction verifier. Python >=3.9, standard library.
Checks are active under -O. No universal occupancy or formal-verification claim.
"""
from __future__ import annotations
import argparse, hashlib, itertools as it, json, math
from collections import Counter
from functools import lru_cache
from pathlib import Path

CHECKS=Counter()
def check(ok,name):
    CHECKS[name]+=1
    if not ok: raise ArithmeticError(name)
def require(ok,msg):
    if not ok: raise ValueError(msg)

@lru_cache(None)
def factor(n):
    require(n>=1,'positive factorization input')
    out=[];q=2
    while q*q<=n:
        e=0
        while n%q==0:n//=q;e+=1
        if e:out.append((q,e))
        q=3 if q==2 else q+2
    if n>1:out.append((n,1))
    return tuple(out)
def prime(n):return n>=2 and factor(n)==((n,1),)
def phi(n):
    x=n
    for q,e in factor(n):x=x//q*(q-1)
    return x
def prime_list(B):
    x=bytearray(b'\1')*(B+1)
    x[:2]=b'\0\0'
    for q in range(2,math.isqrt(B)+1):
        if x[q]:x[q*q::q]=b'\0'*(((B-q*q)//q)+1)
    return [q for q in range(2,B+1) if x[q]]
def closure(gens,R):
    H={1}
    for g in sorted(set(x%R for x in gens)):
        require(math.gcd(g,R)==1,'unit group generator')
        if g in H:
            continue
        old=set(H)
        v=g
        translates=[]
        for _ in range(R):
            if v in old:
                break
            translates.append(v)
            v=v*g%R
        else:
            raise ArithmeticError('finite unit order bound')
        for v in translates:
            for x in old:
                H.add(v*x%R)
    return H

def counts(fac,R):
    out={1:1}
    for q,e in fac:
        local=Counter(pow(q,b,R) for b in range(-e,e+1))
        nxt=Counter()
        for x,n in out.items():
            for y,m in local.items():nxt[x*y%R]+=n*m
        out=dict(nxt)
    return out

def words(fac):
    for beta in it.product(*(range(-e,e+1) for q,e in fac)):
        yield beta,math.prod(q**(e+b) for (q,e),b in zip(fac,beta))

def state(p,a,u,tag):
    R=4*a-p
    require(p%4==1 and p<4*a<2*p and math.gcd(a,p*R)==1,'first-half shell')
    require(tag in ('E','M') and u>0 and a*a%u==0,'original divisor')
    require((4*u+(1 if tag=='E' else p))%R==0,'original channel gate')
    d=math.gcd(a,u);require(d*d%u==0,'normalization integrality')
    h=d*d//u;r=u//d;s=a//d
    require(h*r*s==a and h*r*r==u and math.gcd(r,s)==1,'normalization inverse')
    num=p*r+s if tag=='E' else r+s
    require(num%R==0,'integer channel quotient');q=num//R
    xyz=(a,h*s*q,p*h*r*q) if tag=='E' else (a,p*h*s*q,p*h*r*q)
    x,y,z=xyz
    require(min(xyz)>0 and 4*x*y*z==p*(x*y+x*z+y*z),'reciprocal identity')
    v=a*a if tag=='E' else p*a*a
    require(R*y-p*a>0 and v%(R*y-p*a)==0 and v//(R*y-p*a)==u,'ordered inverse')
    ef=dict(factor(u));af=factor(a)
    return dict(p=p,a=a,R=R,u=u,channel=tag,h=h,r=r,s=s,
                **({'kappa':q} if tag=='E' else {'lambda':q}),
                beta=[ef.get(l,0)-e for l,e in af],factorization=af,denominators=xyz)

def stab(W,R):
    # Complete: every period lies in W because 1 is in W.
    return {g for g in W if all(g*w%R in W for w in W)}

def low_classification(A,alpha,z,eta,active,rep,R):
    d=len(A);require(d<=8,'low-index domain')
    def order(g):
        x=1
        for j in range(1,d+1):
            x=rep(x*g%R)
            if x==1:return j
        raise ArithmeticError('quotient order')
    def cyc(g):return {rep(pow(g,j,R)) for j in range(order(g))}
    E=sum(e for q,e,g in active);exponent=max(order(g) for g in A)
    if E==0:
        if d==2:
            check(eta==1,'P2');return 'P2'
        if d==4:
            check(exponent==2 and eta==1,'P4');return 'P4_V4'
        if d==6:
            check(exponent==6 and order(eta)==3,'P6');return 'P6'
        if d==8 and exponent==8:
            check(order(z)==8 and order(eta)==4,'P8 cyclic');return 'P8_C8'
        if d==8 and exponent==4:
            check(order(z)==4 and alpha not in cyc(z) and order(eta)==2,'P8 product');return 'P8_C4xC2'
        raise ArithmeticError('unclassified pure low-index profile')
    g=active[0][2];pair={g,rep(pow(g,-1,R))}
    if d==6:
        check(order(g)==6 and all(h in pair for q,e,h in active),'C6 directions')
        if E==1:
            check(eta in pair,'C6 single phase');return 'A6_single'
        check(E==2 and eta==1,'C6 double phase');return 'A6_double'
    if d==8 and exponent==8:
        if E==1 and order(g)==4:
            check(eta==1,'C8 order4 phase');return 'A8_order4'
        if E==1 and order(g)==8:
            check(eta in pair,'C8 single phase');return 'A8_single'
        check(E==2 and order(g)==8 and all(h in pair for q,e,h in active) and eta==1,'C8 double phase')
        return 'A8_double'
    if d==8 and exponent==4:
        check(E==1 and order(g)==4 and alpha not in cyc(g) and eta in pair,'C4xC2 single')
        return 'A8_product_single'
    raise ArithmeticError('unclassified active low-index profile')

def analyze(p,a,detail=False,cuts=True):
    R=4*a-p
    require(p%4==1 and p<4*a<2*p and math.gcd(a,p*R)==1,'shell conditions')
    fac=factor(a);mu=counts(fac,R);W=set(mu)
    tM=R-1;tE=(-pow(p,-1,R))%R;tI=(-p)%R
    nE=mu.get(tE,0);nM=mu.get(tM,0)
    check(sum(mu.values())==math.prod(2*e+1 for q,e in fac),'original box mass')
    check(all(mu[x]==mu[pow(x,-1,R)] for x in mu),'inversion multiplicity')
    check(mu.get(tE,0)==mu.get(tI,0),'exterior inversion count')
    check(nM%2==0,'middle orientation pairing')
    info=dict(p=p,a=a,R=R,factorization=fac,E=nE,M=nM,box_mass=sum(mu.values()),failure=(nE+nM==0))
    if detail:
        allwords=[];hits=[]
        for beta,u in words(fac):
            v=u*pow(a,-1,R)%R
            tags=[]
            for tag,gate in [('E',4*u+1),('M',u+a)]:
                if gate%R==0:tags.append(tag);hits.append(state(p,a,u,tag))
            allwords.append(dict(beta=beta,u=u,residue=v,channels=tags))
        check(len(hits)==nE+nM,'all original witness inverses')
        info.update(mu=sorted(mu.items()),words=allwords,hits=hits)
    if not info['failure'] and not detail:return info
    K=stab(W,R)
    Gamma=closure([R-1,2]+[q for q,e in fac],R)
    check(K<=W<=Gamma,'effective envelope and period inclusion')
    check(K==closure(K,R),'actual period subgroup')
    # Homogeneous coset coordinates, not an assumed splitting.
    repmap={x:min(x*h%R for h in K) for x in Gamma}
    rep=lambda x:repmap[x%R]
    A=set(repmap.values());S={rep(w) for w in W}
    check(len(Gamma)==len(A)*len(K),'quotient size')
    check(len(W)==len(S)*len(K),'support saturation only')
    alpha=rep(R-1);z=rep(2);eta=rep(p%R)
    gs=[rep(q%R) for q,e in fac]
    F={alpha,rep((-p)%R),rep((-pow(p,-1,R))%R)}
    check(rep(4*math.prod(pow(q,e,R) for q,e in fac)%R)==eta,'p=4a arithmetic marking')
    qmu=Counter()
    for x,n in mu.items():qmu[rep(x)]+=n
    info.update(K=sorted(K),Gamma=sorted(Gamma) if detail else None,
                effective_index=len(A),ambient_index=phi(R)//len(K),S=sorted(S),
                alpha=alpha,two=z,eta=eta,target_classes=dict(M=alpha,E=rep(tE),E_inverse=rep(tI)),
                quotient_counts=sorted(qmu.items()) if detail else None)
    if not info['failure']:return info
    check(alpha!=1 and rep(alpha*alpha%R)==1,'distinguished nontrivial involution')
    check(eta!=alpha,'p=-1 period class forces hit')
    tau=1 if eta==1 else (2 if rep(eta*eta%R)==1 else 3)
    check(len(F)==tau and not F&S,'complete quotient collision law')
    check(len(A)%2==0,'failure effective index even')
    check({g for g in S if all(rep(g*x%R) in S for x in S)}=={1},'quotient aperiodic')
    active=[(q,e,g) for (q,e),g in zip(fac,gs) if g!=1]
    E=sum(e for q,e,g in active)
    check((E==0)==(W==K),'pure support equivalence')
    check(1+2*E<=len(S)<=len(A)-tau,'joint growth bound')
    def order(g):
        x=1
        for j in range(1,len(A)+1):
            x=rep(x*g%R)
            if x==1:return j
        raise ArithmeticError('order outside finite group')
    for q,e,g in active:check(order(g)>2*e+1,'local saturation exclusion')
    grouped={}
    for q,e,g in active:
        C=frozenset(rep(pow(g,j,R)) for j in range(order(g)))
        grouped[C]=grouped.get(C,0)+e
    for C,ee in grouped.items():check(2*ee<=len(C)-2,'cyclic concentration')
    allcuts=[]
    if cuts:
        for mask in range(1,1<<len(active)):
            selected=[x for i,x in enumerate(active) if mask>>i&1]
            other=[x for i,x in enumerate(active) if not mask>>i&1]
            C={rep(x) for x in closure([g for q,e,g in selected],R)}
            SJ={1};U={1}
            for target,rows in [(SJ,selected),(U,other)]:
                for q,e,g in rows:
                    new={rep(x*pow(g,b,R)%R) for x in target for b in range(-e,e+1)}
                    target.clear();target.update(new)
            TJ={rep(t*pow(x,-1,R)%R) for t in F for x in U}&C
            mass=2*sum(e for q,e,g in selected)
            rhs=len(C)-1-max(1,len(TJ))
            check(not SJ&TJ and 1 not in TJ,'all-block pullback avoids source')
            check(len(SJ)<len(C) and mass<=rhs,'all-block sharpened budget')
            if detail:allcuts.append(dict(primes=[q for q,e,g in selected],C=sorted(C),source=sorted(SJ),
                                         complement=sorted(U),forbidden=sorted(TJ),mass=mass,rhs=rhs))
    low=None
    if len(A)<=8:
        low=low_classification(A,alpha,z,eta,active,rep,R)
        Bfac=tuple((q,e) for (q,e),g in zip(fac,gs) if g==1)
        nu=counts(Bfac,R)
        check(set(nu)==K,'low-index inactive block saturation')
        check(E<=2,'low-index at most two occurrences')
        if detail:info.update(inactive_factor=math.prod(q**e for q,e in Bfac),inactive_counts=sorted(nu.items()))
    check(not(E>0 and len(A)<6),'non-subgroup minimum six')
    check(not(E>0 and tau==2 and len(A)<12),'two-target-collision active minimum twelve')
    info.update(active=active,active_mass=E,collision_count=tau,low_class=low,
                cuts=allcuts if detail else None)
    return info

def cocycle_case(p,a):
    d=analyze(p,a,True);R=d['R'];K=d['K'];G=d['Gamma']
    rep={x:min(x*k%R for k in K) for x in G};A=sorted(set(rep.values()))
    mul=lambda c,e:rep[c*e%R]
    omega=lambda c,e:c*e*pow(mul(c,e),-1,R)%R
    for c,e in it.product(A,repeat=2):check(omega(c,e) in K,'carry lies in actual kernel')
    for c,e,f in it.product(A,repeat=3):
        check(omega(c,e)*omega(mul(c,e),f)%R==omega(e,f)*omega(c,mul(e,f))%R,'exact cocycle')
    for x,y in it.product(G,repeat=2):
        c=rep[x];e=rep[y];k=x*pow(c,-1,R)%R;l=y*pow(e,-1,R)%R
        check(mul(c,e)*k*l*omega(c,e)%R==x*y%R,'twisted product inverse')
    return dict(p=p,a=a,R=R,K=K,cosets=A,
                section=[[c,c] for c in A],cocycle=[[c,e,omega(c,e)] for c,e in it.product(A,repeat=2)])

# Abstract additive groups, independent of residue-modulus existence.
def abstract_tests():
    totals=Counter();rows=Counter()
    types=[(2,),(4,),(2,2),(6,),(8,),(4,2),(2,2,2)]
    for dims in types:
        G=tuple(it.product(*(range(n) for n in dims)));zero=(0,)*len(dims);d=len(G)
        add=lambda x,y:tuple((a+b)%n for a,b,n in zip(x,y,dims))
        neg=lambda x:tuple(-a%n for a,n in zip(x,dims))
        scale=lambda e,x:tuple(e*a%n for a,n in zip(x,dims))
        def generated(gs):
            C={zero};queue=[zero]
            while queue:
                x=queue.pop()
                for g in gs:
                    y=add(x,g)
                    if y not in C:C.add(y);queue.append(y)
            return C
        def order(g):
            for j in range(1,d+1):
                if scale(j,g)==zero:return j
        invol=[x for x in G if x!=zero and scale(2,x)==zero]
        # Up to three occurrences is exhaustive for failed actual quotient <=8 by growth.
        atoms=[(g,e) for g in G if g!=zero for e in range(1,4)]
        profiles=[()]
        for l in range(1,4):
            profiles.extend(p for p in it.combinations_with_replacement(atoms,l) if sum(e for g,e in p)<=3)
        for prof in profiles:
            S={zero};center=zero
            for g,e in prof:
                S={add(x,scale(j,g)) for x in S for j in range(-e,e+1)}
                center=add(center,scale(e,g))
            if {g for g in G if {add(g,x) for x in S}==S}!={zero}:continue
            for alpha,z in it.product(invol,G):
                if generated([alpha,z]+[g for g,e in prof])!=set(G):continue
                eta=add(scale(2,z),center)
                F={alpha,add(alpha,eta),add(alpha,neg(eta))}
                totals['aperiodic_anchored_models']+=1
                if F&S:continue
                totals['failed_models']+=1;E=sum(e for g,e in prof)
                check(d%2==0 and E<=2,'abstract low mass')
                if not prof:
                    if d==2:code='P2';ok=eta==zero
                    elif d==4:code='P4_V4';ok=dims==(2,2) and eta==zero
                    elif d==6:code='P6';ok=order(eta)==3
                    elif dims==(8,):code='P8_C8';ok=order(z)==8 and order(eta)==4
                    elif dims==(4,2):code='P8_C4xC2';ok=order(z)==4 and alpha not in generated([z]) and order(eta)==2
                    else:code='bad';ok=False
                else:
                    g=prof[0][0];pair={g,neg(g)}
                    if d==6:
                        ok=order(g)==6 and all(h in pair for h,e in prof)
                        if E==1:code='A6_single';ok &= eta in pair
                        else:code='A6_double';ok &= E==2 and eta==zero
                    elif dims==(8,):
                        if E==1 and order(g)==4:code='A8_order4';ok=eta==zero
                        elif E==1 and order(g)==8:code='A8_single';ok=eta in pair
                        else:code='A8_double';ok=E==2 and order(g)==8 and all(h in pair for h,e in prof) and eta==zero
                    elif dims==(4,2):
                        code='A8_product_single';ok=E==1 and order(g)==4 and alpha not in generated([g]) and eta in pair
                    else:code='bad';ok=False
                check(ok,'abstract full normal form')
                rows[(dims,code)]+=1
    return dict(totals=dict(totals),profiles=[dict(group=list(d),normal_form=c,count=n) for (d,c),n in sorted(rows.items())])

def negative_controls(examples):
    out=[]
    def reject(name,condition):
        if condition:raise ArithmeticError('bad formula accepted: '+name)
        out.append(name)
    d=next(x for x in examples if x['p']==3361 and x['a']==848)
    reject('support period implies equal coefficient division',len({n for x,n in d['mu'] if x in d['K']})==1)
    r=next(x for x in examples if x['p']==22129)
    reject('exterior-only miss is a joint miss',r['E']==0 and r['M']==0)
    d=next(x for x in examples if x['p']==109)
    reject('two exterior orientations are three distinct classes',len(set(d['target_classes'].values()))==3)
    R=19;left=pow(2,5,R);right=pow(2,1,R)
    reject('nonsplit quotient multiplication has no carry',(left*right)%R==1)
    # In C4, an arbitrary eta=0 would give a false failure; eta=2z+1 never does.
    valid_failure=any(not {2,(2+(2*z+1))%4,(2-(2*z+1))%4}&{0,1,3} for z in range(4))
    reject('phase p can be chosen independently of 4a',valid_failure)
    divs=[u for b,u in words(factor(18))]
    local5={u for u in divs if (4*u+1)%5==0};local7={u for u in divs if (4*u+1)%7==0}
    check(bool(local5) and bool(local7),'negative CRT local antecedents')
    reject('independent local divisors glue inside the box',bool(local5&local7))
    a=next(x for x in examples if x['p']==29);b=next(x for x in examples if x['p']==197)
    reject('one square prime and two simple primes have equal mass',a['box_mass']==b['box_mass'])
    x=next(x for x in examples if x['p']==6340273)
    reject('effective and full ambient indices are interchangeable',x['effective_index']==x['ambient_index'])
    return out

def scan(B):
    totals=Counter();hist=Counter();rows=[];first=[]
    for p in prime_list(B):
        if p%4!=1:continue
        totals['primes']+=1
        for a in range((p+3)//4,(p-1)//2+1):
            d=analyze(p,a)
            totals['shells']+=1;totals['original_divisor_states']+=d['box_mass']
            totals['E_states']+=d['E'];totals['M_states']+=d['M']
            if d['failure']:
                totals['joint_empty_shells']+=1
                if d['active_mass']==0:totals['subgroup_support_failures']+=1
                else:totals['non_subgroup_failures']+=1
                hist[(d['effective_index'],d['collision_count'],d['active_mass'])]+=1
                if d['low_class']:totals[d['low_class']]+=1
                row=[p,a,d['E'],d['M'],d['K'],d['ambient_index'],d['effective_index'],d['active_mass'],d['collision_count'],d['low_class']]
            else:
                totals['occupied_shells']+=1
                row=[p,a,d['E'],d['M'],None,None,None,None,None,None]
            rows.append(row)
    digest=hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()
    return dict(bound=B,scope='every prime p=1 mod4; every p/4<a<p/2; all original divisors and both channels',
                totals=dict(totals),columns=['p','a','E','M','K_if_empty','ambient_index','effective_index','active_mass','collision_count','normal_form'],
                rows=rows,row_sha256=digest,
                obstruction_histogram=[[list(k),v] for k,v in sorted(hist.items())])

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--bound',type=int,default=3000);ap.add_argument('--out',default='certificates');args=ap.parse_args()
    require(args.bound>=5,'bound >=5')
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    examples=[]
    for p,a in [(3361,848),(5569,1397),(22129,5537),(29,9),(197,51),(109,31),(37,13),(6340273,1585081),(37,18),(1201,306),(1201,312),(2521,636)]:
        check(prime(p),'example deterministic primality')
        examples.append(analyze(p,a,True))
    cocycles=[cocycle_case(5569,1397),cocycle_case(3361,848)]
    abstract=abstract_tests();result=scan(args.bound);negative=negative_controls(examples)
    data={'examples.json':examples,'cocycles.json':cocycles,'abstract.json':abstract,'scan.json':result,'negative_controls.json':negative,'checks.json':dict(CHECKS)}
    for name,obj in data.items():(out/name).write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')
    print(json.dumps(dict(checks=sum(CHECKS.values()),negative_controls=len(negative),scan=result['totals'],row_sha256=result['row_sha256']),sort_keys=True))
if __name__=='__main__':main()
