#!/usr/bin/env python3
"""Turn 4: mixed square-source escape, exact finite cofactor reduction, and carries.
Standard-library verification. Original integer coefficients precede every reduction.
The cofactor enumeration is a finite proof component after the bounds in core.tex;
the bounded graph scan is corroboration and not a proof of ES or global occupancy.
"""
from __future__ import annotations
import argparse, hashlib, json
from collections import Counter,deque
from fractions import Fraction
from itertools import combinations,product
from math import gcd,isqrt,prod
from pathlib import Path
from cofactor_check import enumerate_profiles,prime_test,sigma,HARD
CHECKS=Counter()

def check(b,label):
    CHECKS[label]+=1
    if not b:raise ArithmeticError(label)

def sieve(n):
    spf=list(range(n+1))
    if n>=1:spf[1]=1
    for r in range(2,isqrt(n)+1):
        if spf[r]==r:
            for x in range(r*r,n+1,r):
                if spf[x]==x:spf[x]=r
    return spf,[r for r in range(2,n+1) if spf[r]==r]

def factor(n,spf):
    if not (0<n<len(spf)):raise ValueError('factor input outside declared sieve')
    fs=[]
    while n>1:
        r=spf[n];e=0
        while n%r==0:n//=r;e+=1
        fs.append([r,e])
    return fs

def divisors_square(fs):
    ds=[1]
    for r,e in fs:ds=[u*r**j for u in ds for j in range(2*e+1)]
    return sorted(ds)

def leg(a,p):
    t=pow(a%p,(p-1)//2,p)
    return -1 if t==p-1 else t

def budget(n):
    if n<0:raise ValueError('nonnegative forbidden-prime count required')
    small=(1,2,3,4,5,6,9,15)
    return small[n] if n<8 else ((2*n+9)*(3**n-1)+17)//18

def interval_count(N,d,r):
    if N<0 or not(0<=r<d):raise ValueError('prefix residue input')
    return (N-1-r)//d+1

def CRT(a,m,b,n):
    if gcd(m,n)!=1:raise ValueError('coprime CRT inputs only')
    return (a+m*((b-a)*pow(m,-1,n)%n))%(m*n)

def polynomial(p,q,j):
    return (p+sigma(q)*q)//4+sigma(q)*q*j*(j+1)

def roots(p,q,r):
    return [j for j in range(r) if polynomial(p,q,j)%r==0]

def exact_avoidance(p,q,C,N):
    active=[];raw=[]
    for r in sorted(set(C)-{q}):
        z=roots(p,q,r);raw.append([r,z])
        check(len(z)==1+leg(-sigma(q)*q*p,r),'quadratic discriminant root count')
        check(len(z) in (0,2),'unit discriminant')
        if z:
            check((z[0]+z[1]+1)%r==0,'paired source roots')
            active.append((r,z))
    terms=[];total=0
    for mask in range(1<<len(active)):
        d=1;zs=[0];selected=[]
        for i,(r,z) in enumerate(active):
            if mask>>i&1:
                zs=[CRT(a,d,b,r) for a in zs for b in z];d*=r;selected.append(r)
        zs.sort();count=sum(interval_count(N,d,z) for z in zs)
        sign=(-1)**len(selected);total+=sign*count
        terms.append({'primes':selected,'modulus':d,'roots':zs,'count':count,'sign':sign})
    P=prod(C);direct=[j for j in range(N) if gcd(polynomial(p,q,j),P)==1]
    check(total==len(direct),'exact inclusion exclusion')
    delta=prod((Fraction(r-2,r) for r,z in active),start=Fraction(1))
    n=len(active)
    if n:check(abs(Fraction(total)-N*delta)<Fraction(3**n-1,2),'reflected root-pair discrepancy')
    else:check(total==N,'no excluded root')
    check(delta>=Fraction(9,2*n+9),'explicit density lower bound')
    if N>=budget(n):check(total>0,'uniform C-free prefix')
    return {'p':p,'q':q,'C':sorted(C),'N':N,'active_roots':raw,
        'density':[delta.numerator,delta.denominator],'terms':terms,'free_indices':direct}

def state(p,a,u,channel):
    R=4*a-p;d=gcd(a,u);h=d*d//u;r=u//d;s=a//d
    check(d*d%u==0 and h*r*s==a and h*r*r==u and gcd(r,s)==1,'divisor normalization')
    if channel=='E':
        value=(p*r+s)//R
        check((p*r+s)%R==0,'exterior quotient')
        den=[a,h*s*value,p*h*r*value];inverse=a*a//(R*den[1]-p*a)
        check((r+value)%s==0,'ET exterior sixth coordinate integral')
        ee=(r+value)//s
        et=[r,value,s,h,ee,R];etimage=[den[2],den[0],den[1]];permutation=[1,2,0]
        check(4*r*value*h==p*ee+1 and ee*R==4*r*r*h+1,'ET Type I equations')
        quotient={'kappa':value}
    else:
        value=(r+s)//R
        check((r+s)%R==0,'middle quotient')
        den=[a,p*h*s*value,p*h*r*value];inverse=p*a*a//(R*den[1]-p*a)
        ff=4*r*value*h-1
        et=[r,s,value,h,R,ff];etimage=[den[0],den[2],den[1]];permutation=[0,2,1]
        check(value*R==r+s and R*ff==p+4*r*r*h,'ET Type II equations')
        quotient={'lambda':value}
    x,y,z=den
    check(min(den)>0 and 4*x*y*z==p*(x*y+x*z+y*z),'positive ordered ES identity')
    check(inverse==u,'ordered original divisor inverse')
    return dict(p=p,R=R,a=a,u=u,h=h,r=r,s=s,channel=channel,denominators=den,ET_coordinates=et,ET_image=etimage,ET_to_original_permutation=permutation,**quotient)

def source(p,q,t,spf,detail=False):
    R0=sigma(q)*q;R=R0*t*t
    if t<=0 or t%2==0 or R>=3*p:raise ValueError('invalid square-source range')
    A=(p+R)//4;fs=factor(A,spf);ds=divisors_square(fs)
    check(4*A==p+R and p<4*A<4*p and gcd(A*p,R)==1,'original source units and range')
    check(leg(A,p)==-1,'source nonresidue')
    edges=[[r,e] for r,e in fs if leg(r,p)==-1]
    check(edges and all(r<p and r!=q for r,e in edges),'all-edge factor supply')
    check(sum(e for r,e in edges)%2==1,'original outgoing multiplicity parity')
    channels={};fine=[]
    for channel,eta in [('E',1),('M',p)]:
        hits=[];candidates=[];counts=Counter()
        for u in ds:
            numerator=4*u+eta
            if numerator%R0:continue
            carry=numerator//R0;digit=carry%(t*t);quotient=carry//(t*t)
            check(R0*(digit+t*t*quotient)-eta==4*u,'integer carry inverse')
            counts[digit]+=1
            if detail:candidates.append({'u':u,'carry':carry,'digit':digit,'quotient':quotient})
            if digit==0:
                hits.append(u)
                check(numerator%R==0,'full prime-power residual')
                state(p,A,u,channel)
        check(len(hits)==counts.get(0,0),'original target coefficient')
        if channel=='M' and 2*A>p:check(not hits,'no upper-half middle state')
        channels[channel]={'hits':hits,'base_count':sum(counts.values()),'carry_counts':sorted(counts.items())}
        if detail:channels[channel]['base_candidates']=candidates
    check(not (set(channels['E']['hits'])&set(channels['M']['hits'])),'separate channel targets')
    if detail:
        for u in ds:
            beta=[]
            for r,e in fs:
                w=u;v=0
                while w%r==0:w//=r;v+=1
                beta.append(v-e)
            residue=u*pow(A,-1,R)%R
            fine.append({'u':u,'beta':beta,'residue':residue})
    ans={'p':p,'q':q,'sigma':sigma(q),'t':t,'R':R,'a':A,'factorization':fs,
        'edges':edges,'divisor_count':len(ds),'channels':channels}
    if detail:
        ans['original_words']=fine
        mu=Counter(w['residue'] for w in fine);W=set(mu)
        K={x for x in W if {x*w%R for w in W}==W}
        G={1};front=[1];gens=[R-1,2]+[r for r,e in fs]
        for z in front:
            for g in gens:
                y=z*g%R
                if y not in G:G.add(y);front.append(y)
        check(len(G)%len(K)==0 and K<=G,'actual stabilizer in coefficient group')
        targets=[R-1,(-p)%R,(-pow(p,-1,R))%R]
        classes=[min(t*k%R for k in K) for t in targets]
        phi=R
        for l,e in factor(R,spf):phi=phi//l*(l-1)
        ans['obstruction']={'fine_counts':sorted(mu.items()),'K':sorted(K),
            'Gamma_order':len(G),'effective_index':len(G)//len(K),
            'ambient_index':phi//len(K),'targets':targets,'target_classes':classes,
            'distinct_target_classes':len(set(classes))}

    return ans

def expand_six(p,q,spf):
    if not (prime_test(p)[0] and p%840 in HARD and prime_test(q)[0] and 11<=q<p and leg(q,p)==-1):
        raise ValueError('hard prime and original external prime required')
    seen={q};todo=deque([q]);processed=[];records=[]
    while len(seen)<6 and todo:
        a=todo.popleft();processed.append(a)
        for t in (1,3,5,7,9):
            if sigma(a)*a*t*t>=3*p:continue
            rec=source(p,a,t,spf)
            records.append(rec)
            for b,e in rec['edges']:
                if b not in seen:seen.add(b);todo.append(b)
            if len(seen)>=6:break
    check(len(seen)>=6 and len(processed)<=5 and len(records)<=25,'unconditional six-vertex expansion')
    return {'p':p,'start':q,'vertices':sorted(seen),'processed':processed,'sources':records}

def root_tests(spf,ps):
    count=0
    for d in range(3,80,2):
        for a in range((d-1)//2):
            b=d-1-a
            for N in range(3*d+1):
                z=interval_count(N,d,a)+interval_count(N,d,b)
                check(abs(d*z-2*N)<d,'reflected pair exact prefix bound');count+=1
    for n in range(0,201):
        B=budget(n);check(B<=4**n,'prefix length exponential upper bound')
        if n>=8:check(Fraction(9*B,2*n+9)>=Fraction(3**n-1,2),'prefix constant proof')
        if n:check(B>budget(n-1),'prefix constants monotone')
    fixtures=[]
    for p in (1009,1129,1201,2521,3361,12889):
        V=[q for q in ps if q<p and leg(q,p)==-1]
        for q in V[:4]:
            for n in range(5):
                C={q,*[r for r in V if r!=q][:n]}
                for N in (1,budget(n),budget(n)+3):fixtures.append(exact_avoidance(p,q,C,N))
        # The exact prime-power lift on every first outgoing prime.
        for q in V[:3]:
            A=polynomial(p,q,0)
            for r,e in factor(A,spf):
                if r<11 or r==q:continue
                z=roots(p,q,r);M=r;all_layers=[]
                for power in range(1,4):
                    check(all(polynomial(p,q,x)%M==0 for x in z),'prime-power root equations')
                    if M<=4000:
                        check(z==[x for x in range(M) if polynomial(p,q,x)%M==0],'complete literal root list')
                    all_layers.append([M,z[:]])
                    nxt=[]
                    for x in z:
                        der=sigma(q)*q*(2*x+1)
                        check(gcd(der,r)==1,'simple root derivative')
                        h=-(polynomial(p,q,x)//M)*pow(der,-1,r)%r
                        nxt.append(x+M*h)
                    M*=r;z=sorted(nxt)
                N=11;bound=polynomial(p,q,N-1);mass=0;mod=r;zs=roots(p,q,r)
                while mod<=bound:
                    mass+=sum(interval_count(N,mod,x) for x in zs)
                    nxt=[]
                    for x in zs:
                        h=-(polynomial(p,q,x)//mod)*pow(sigma(q)*q*(2*x+1),-1,r)%r
                        nxt.append(x+mod*h)
                    mod*=r;zs=sorted(nxt)
                direct=0
                for j in range(N):
                    val=polynomial(p,q,j)
                    while val%r==0:direct+=1;val//=r
                check(mass==direct,'exact prime multiplicity over all sources')
    # Abstract reciprocal orientation table, without inventing a residue-group map.
    allowed={(1,1),(5,5),(1,7),(5,7)}
    for q,r in combinations([v for v in ps if 11<=v<=300],2):
        a=leg(q,r)==-leg(-sigma(q),r)
        b=leg(r,q)==-leg(-sigma(r),q)
        pair=tuple(sorted((q%12,r%12)))
        if pair in allowed:check(a==b,'mixed type mutual-or-empty')
        else:check(a!=b,'mixed type exactly one orientation')
    return {'reflected_pair_cases':count,'avoidance_fixtures':fixtures,
      'prefix_constants':[[n,budget(n)] for n in range(21)],
      'mutual_type_pairs':sorted([list(x) for x in allowed])}

def examples(spf):
    p=12889;qs=(43,61);records=[]
    for q in qs:
        max_t=isqrt((3*p-1)//(sigma(q)*q))
        for t in range(1,max_t+1,2):
            rec=source(p,q,t,spf,True)
            check(not rec['channels']['E']['hits'] and not rec['channels']['M']['hits'],'all squares at mixed pair locally fail')
            records.append(rec)
    check(len(records)==22,'all valid mixed-pair squares counted')
    # Full common original domains, with unchanged base carry and translated centres.
    for q in qs:
        ss=[r for r in records if r['q']==q]
        for x,y in combinations(ss,2):
            j=(x['t']-1)//2;k=(y['t']-1)//2
            g=gcd(x['a'],y['a'])
            check(g==gcd(x['a'],(k-j)*(k+j+1)),'same-prime source gcd')
            dx={z['u'] for z in x['original_words']};dy={z['u'] for z in y['original_words']}
            check(dx&dy==set(divisors_square(factor(g,spf))),'complete common divisor domain')
            for u in dx&dy:
                for eta in (1,p):
                    if (4*u+eta)%(sigma(q)*q)==0:
                        K=(4*u+eta)//(sigma(q)*q)
                        check((K%(x['t']**2)==0)==((4*u+eta)%x['R']==0),'first original carry criterion')
                        check((K%(y['t']**2)==0)==((4*u+eta)%y['R']==0),'second original carry criterion')
    path=[source(p,43,3,spf,True),source(p,3319,1,spf,True),source(p,1013,1,spf,True),source(p,11,1,spf,True)]
    for i in range(3):check(path[i+1]['q'] in [r for r,e in path[i]['edges']],'actual escape path')
    check(9 in path[-1]['channels']['M']['hits'],'path terminal original middle hit')
    witness=state(p,path[-1]['a'],9,'M')
    # Non-coprime prime-power projection fails at an available original divisor.
    nc=source(1129,11,11,spf,True);u=1845
    check(nc['a']==615 and (4*u+1)%121==0 and (4*u+1)%1331!=0,'noncoprime CRT negative example')
    check(nc['a']**2%u==0 and ((4*u+1)//11)%121==66,'noncoprime carry digit')
    one=exact_avoidance(3361,977,{977,11},1)
    ns=source(3361,977,1,spf,True)
    check(not one['free_indices'] and [13,1] in ns['edges'],'C-free test not equivalent to no escape')
    return {'pair_all_square_sources':records,'positive_escape_path':path,'positive_states':[witness],
      'noncoprime_projection':{'source':nc,'u':u,'numerator':4*u+1,'base_carry':(4*u+1)//11,'digit':66},
      'C_free_not_necessary':{'avoidance':one,'source':ns},'six_vertex_expansions':[expand_six(12889,43,spf),expand_six(4201,61,spf),expand_six(2521,11,spf)]}

def scan(bound,spf,ps):
    rows=[];dig=hashlib.sha256();stats=Counter()
    for p in ps:
        if p>bound:break
        if p%840 not in HARD:continue
        V=[q for q in ps if q<p and leg(q,p)==-1];adj={q:set() for q in V};hit=set();st=Counter()
        for q in V:
            maxt=isqrt((3*p-1)//(sigma(q)*q))
            for t in range(1,maxt+1,2):
                rec=source(p,q,t,spf)
                adj[q].update(r for r,e in rec['edges'])
                if rec['channels']['E']['hits'] or rec['channels']['M']['hits']:hit.add(q)
                st['sources']+=1;st['divisor_vectors']+=rec['divisor_count']
                st['edge_occurrences']+=sum(e for r,e in rec['edges'])
                st['port_edges']+=len(rec['edges'])
                st['E']+=len(rec['channels']['E']['hits']);st['M']+=len(rec['channels']['M']['hits'])
                dig.update(json.dumps(rec,sort_keys=True,separators=(',',':')).encode()+b'\n')
        rev={q:[] for q in V}
        for q,rs in adj.items():
            for r in rs:rev[r].append(q)
        dist={q:0 for q in hit};todo=deque(sorted(hit))
        while todo:
            r=todo.popleft()
            for q in rev[r]:
                if q not in dist:dist[q]=dist[r]+1;todo.append(q)
        trapped=set(V)-set(dist)
        check(all(adj[q]<=trapped for q in trapped),'actual all-square failure closure')
        check(not trapped or len(trapped)>=6,'finite corollary no small failed closed set')
        row={'p':p,'vertices':len(V),'hit_vertices':len(hit),'trapped_vertices':len(trapped),
             'max_distance':max(dist.values(),default=0),**dict(st)}
        rows.append(row);stats.update(st);stats['primes']+=1;stats['vertices']+=len(V)
    return {'bound':bound,'rows':rows,'totals':dict(stats),'source_sha256':dig.hexdigest(),
            'scope':'Complete valid square sources at every external prime vertex for these bounded hard primes only.'}

def negative_controls(ex):
    names=[]
    def reject(label,predicate):
        if predicate():raise ArithmeticError('unrejected false transformation: '+label)
        names.append(label)
    reject('mixed canonical graph has no opposite edges',lambda: not ((12889+43)//4%61==0 and (12889+3*61)//4%43==0))
    reject('separate q and square congruences imply their product',lambda:(4*1845+1)%1331==0)
    reject('a new prime guarantees local selector occupancy',lambda:any(ex['positive_escape_path'][0]['channels'][c]['hits'] for c in ('E','M')))
    reject('multiplicity can be discarded in source count',lambda:2*2+1==3)
    reject('base carry digit can be omitted',lambda:671%121==0)
    reject('range boundaries may be rounded upwards',lambda:3*11*1001**2<3*12889)
    reject('reflected-prefix error bound holds at every translated interval',lambda:abs(11*2-2*2)<11)
    return names

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--bound',type=int,default=5000)
    ap.add_argument('--out',default='certificates');ap.add_argument('--reuse-cofactor',action='store_true')
    args=ap.parse_args()
    if args.bound<1009:ap.error('bound must contain the first hard prime')
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True);spf,ps=sieve(max(args.bound,50000))
    if not args.reuse_cofactor:
        cert=enumerate_profiles(5);(out/'cofactor_certificate.json').write_text(json.dumps(cert,sort_keys=True,separators=(',',':'))+'\n')
    else:
        cert=json.loads((out/'cofactor_certificate.json').read_text())
        check(cert['m']==5,'reused finite enumeration explicit scope')
    for m in (2,3,4):
        small=enumerate_profiles(m)
        check(not small['cycles'],'smaller fixed-port closed sets excluded')
        (out/f'cofactor_small_{m}.json').write_text(json.dumps(small,sort_keys=True,separators=(',',':'))+'\n')
    check(cert['range_profile_sha256']=='5df2c1b996bf1562d3add24203a92928ffbd314d21c3c5700c97601ea6455ded','finite range profile certificate')
    results={'root_coefficients':root_tests(spf,ps),'examples':examples(spf),'scan':scan(args.bound,spf,ps)}
    neg=negative_controls(results['examples'])
    for name,data in results.items():(out/(name+'.json')).write_text(json.dumps(data,sort_keys=True,separators=(',',':'))+'\n')
    summary={'checks':dict(sorted(CHECKS.items())),'explicit_checks':sum(CHECKS.values()),'negative_controls':neg,
      'cofactor_enumeration_rerun':not args.reuse_cofactor,'cofactor_counts':cert['counts'],'scan_totals':results['scan']['totals'],
      'pair_square_sources':len(results['examples']['pair_all_square_sources']),
      'nonclaims':['No ES resolution','No universal all-square graph occupancy','No complexity bound for arbitrary integer factorization','No Lean build','No independent mathematical review']}
    (out/'verification.json').write_text(json.dumps(summary,sort_keys=True,separators=(',',':'))+'\n')
    print(json.dumps(summary,sort_keys=True))
if __name__=='__main__':main()
