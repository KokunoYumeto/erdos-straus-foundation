#!/usr/bin/env python3
"""Turn 2: complete shifted-factor graphs, coordinate transfers and failure traps.
Python standard library. All mathematical checks remain active under -O.
Finite scans are not an ES existence theorem. See core.tex for proofs.
"""
from __future__ import annotations
from collections import Counter, deque
from functools import lru_cache
from fractions import Fraction
from itertools import product
from math import gcd, isqrt, prod
from pathlib import Path
import argparse, hashlib, json

HARD = {1,121,169,289,361,529}
CHECKS = Counter()

def check(value: bool, label: str) -> None:
    CHECKS[label] += 1
    if not value:
        raise ArithmeticError(label)

@lru_cache(maxsize=None)
def factor(n: int) -> tuple[tuple[int,int],...]:
    if n < 1: raise ValueError('positive factor input required')
    out=[]; d=2
    while d*d<=n:
        e=0
        while n%d==0: n//=d; e+=1
        if e: out.append((d,e))
        d=3 if d==2 else d+2
    if n>1: out.append((n,1))
    return tuple(out)

def sieve(n: int) -> list[int]:
    if n<2: return []
    a=bytearray(b'\1')*(n+1); a[:2]=b'\0\0'
    for q in range(2,isqrt(n)+1):
        if a[q]: a[q*q::q]=b'\0'*len(a[q*q::q])
    return [i for i in range(2,n+1) if a[i]]

def prime(n:int) -> bool:
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))

def leg(a:int,p:int) -> int:
    x=pow(a%p,(p-1)//2,p)
    return -1 if x==p-1 else x

def jac(a:int,n:int) -> int:
    if n<=0 or n%2==0: raise ValueError('positive odd denominator required')
    a%=n; sign=1
    while a:
        while a%2==0:
            a//=2
            if n%8 in (3,5): sign=-sign
        a,n=n,a
        if a%4==n%4==3: sign=-sign
        a%=n
    return sign if n==1 else 0

def sigma(q:int)->int:
    return 1 if q%4==3 else 3

def divisors(n:int, square:bool=False)->list[int]:
    out=[1]
    for q,e in factor(n):
        out=[a*q**i for a in out for i in range((2 if square else 1)*e+1)]
    return sorted(out)

def source(p:int,q:int,s:int|None=None)->dict:
    s=sigma(q) if s is None else s
    if s<=0 or (p+s*q)%4 or s*q>=3*p or leg(s,p)!=1:
        raise ValueError('invalid positive multiplier port')
    R=s*q; a=(p+R)//4; fs=factor(a)
    check(p<4*a<4*p and gcd(p*a,R)==1,'source_domain_and_units')
    check(leg(a,p)==-1,'nonresidue_source')
    nr=[(r,e) for r,e in fs if leg(r,p)==-1]
    check(bool(nr) and sum(e for r,e in nr)%2==1,'complete_NR_multiplicity_parity')
    check(all(r<p and r!=q for r,e in nr),'edge_distinct_in_range')
    hits={'E':[],'M':[]}; mu=Counter(); ai=pow(a,-1,R)
    for u in divisors(a,True):
        mu[u*ai%R]+=1
        if (4*u+1)%R==0: hits['E'].append(u)
        if (u+a)%R==0: hits['M'].append(u)
    check(sum(mu.values())==prod(2*e+1 for r,e in fs),'complete_box_mass')
    check(all(mu[x]==mu[pow(x,-1,R)] for x in mu),'centered_inversion')
    check(len(hits['M'])%2==0,'M_orientation_pair')
    if 2*a>p: check(not hits['M'],'no_large_A_middle_hits')
    for r,e in fs:
        check(jac(r,R)==leg(r,p),'factorwise_Jacobi_transfer')
    if s in (1,3):
        for r,e in nr:
            expected=-1 if s==1 else -jac(-3,r)
            check(leg(r,q)==expected,'source_prime_reciprocity')
    return {'q':q,'sigma':s,'R':R,'a':a,'factors':fs,'edges':nr,
            'E':hits['E'],'M':hits['M'],'mu':mu,'first_half':2*a<p}

def reconstruct(p:int,a:int,u:int,channel:str)->dict:
    R=4*a-p; d=gcd(a,u)
    if a*a%u or R<=0: raise ValueError('bad original divisor state')
    h=d*d//u; r=u//d; s=a//d
    check(h*r*s==a and h*r*r==u and gcd(r,s)==1,'normalization')
    num=p*r+s if channel=='E' else r+s
    if num%R: raise ValueError('gate miss')
    zeta=num//R
    xyz=(a,h*s*zeta,p*h*r*zeta) if channel=='E' else (a,p*h*s*zeta,p*h*r*zeta)
    check(min(xyz)>0 and sum((Fraction(1,x) for x in xyz),Fraction())==Fraction(4,p),'ordered_ES_return')
    inv=Fraction((1 if channel=='E' else p)*a*a,R*xyz[1]-p*a)
    check(inv==u,'ordered_divisor_inverse')
    rec={'p':p,'a':a,'R':R,'u':u,'channel':channel,'h':h,'r':r,'s':s,
         'quotient':zeta,'denominators':xyz,'first_half':2*a<p}
    if 2*a>p:
        check(channel=='E' and 4*xyz[1]>p and 2*xyz[1]<p,'auxiliary_swap_to_first_half')
        aa=xyz[1]; RR=4*aa-p; uu=Fraction(aa*aa,RR*a-p*aa)
        check(uu.denominator==1,'recode_integral_divisor')
        back=reconstruct(p,aa,int(uu),'E')
        check(tuple(back['denominators'])==(xyz[1],xyz[0],xyz[2]),'recode_retained_permutation')
        rec['first_half_return']=back;rec['permutation']=[1,0,2]
    return rec

def make_graph(p:int,ps:list[int])->dict[int,dict]:
    V=[q for q in ps if q<p and leg(q,p)==-1]
    check(bool(V) and min(V)>=11,'hard_vertex_universe')
    vs=set(V); nodes={q:source(p,q) for q in V}
    check(all(r in vs for n in nodes.values() for r,e in n['edges']),'all_edges_stay_in_universe')
    for q,n in nodes.items():
        for r,m in n['edges']:
            c=n['a']//r; B=n['a']//(r**m); t=sigma(r); an=nodes[r]['a']
            check(p+n['sigma']*q==4*c*r and c==r**(m-1)*B,'full_factor_edge_equation')
            check(4*an==(4*c+t)*r-n['sigma']*q,'successor_coordinate_formula')
            check((n['sigma']*q)%r==(-p)%r,'predecessor_target_projection')
            delta=an-n['a']; common=gcd(an,n['a'])
            check(delta==(t*r-n['sigma']*q)//4,'exact_shell_difference')
            check(gcd(n['R'],nodes[r]['R'])==(3 if n['sigma']==t==3 else 1),'common_modulus_is_only_one_or_three')
            check(delta%common==0,'common_factor_bound')
            if p<=5000:
                ds=set(divisors(n['a'],True));dt=set(divisors(an,True));dc=set(divisors(common,True))
                check(ds&dt==dc,'complete_same_divisor_transport_domain')
                for uu in dc:
                    check((uu+an)-(uu+n['a'])==delta,'middle_gate_transition')
                    for ell in {x for x,e in n['factors']}|{x for x,e in nodes[r]['factors']}:
                        ff=dict(factor(uu)).get(ell,0)
                        eq=dict(n['factors']).get(ell,0);er=dict(nodes[r]['factors']).get(ell,0)
                        check((ff-er)==(ff-eq)+eq-er,'centered_vector_transport')
            if n['sigma']==1:
                check(leg(q,r)==-jac(-1,r),'reverse_character_source_type1')
            else:
                check(leg(q,r)==-jac(-3,r),'reverse_character_source_type3')
            if q in [rr for rr,ee in nodes[r]['edges']]:
                check(not (q%4==r%4==3),'no_two_cycle_all3mod4')
                if q%4==r%4==1:check(q%3==r%3,'two_cycle_both1_constraint')
                if q%4==3 and r%4==1:check(q%3==1,'two_cycle_mixed_constraint')
            if t==3:
                ell=(n['sigma']*q-4*c*r)%(3*r)
                crt=(2*r*pow(r,-1,3)+3*(n['sigma']*q%r)*pow(3,-1,r))%(3*r)
                check(ell==crt==(-p)%(3*r),'composite_full_target_and_carry')
        for tag in ('E','M'):
            for u in n[tag]: reconstruct(p,n['a'],u,tag)
    return nodes

def closure(nodes:dict[int,dict])->tuple[dict[int,int],set[int],list[list[int]]]:
    rev={q:[] for q in nodes}
    for q,n in nodes.items():
        for r,e in n['edges']: rev[r].append(q)
    dist={q:0 for q,n in nodes.items() if n['E'] or n['M']}
    todo=deque(sorted(dist))
    while todo:
        r=todo.popleft()
        for q in rev[r]:
            if q not in dist: dist[q]=dist[r]+1; todo.append(q)
    bad=set(nodes)-set(dist)
    check(all(not(nodes[q]['E'] or nodes[q]['M']) and all(r in bad for r,e in nodes[q]['edges']) for q in bad),'greatest_closed_failure_set')
    for q,d in dist.items():
        check(d<len(nodes) and (d==0 or any(dist.get(r)==d-1 for r,e in nodes[q]['edges'])),'terminating_reachability_rank')
    # Independent fixed-point description within this checker.
    layers=[]; F={q for q,n in nodes.items() if not(n['E'] or n['M'])}
    while True:
        rem={q for q in F if any(r not in F for r,e in nodes[q]['edges'])}
        if not rem:break
        layers.append(sorted(rem));F-=rem
    check(F==bad,'BFS_equals_greatest_fixed_point')
    return dist,bad,layers

def sccs(nodes:dict[int,dict])->list[list[int]]:
    adj={q:[r for r,e in n['edges']] for q,n in nodes.items()};rev={q:[] for q in adj}
    for q,rs in adj.items():
        for r in rs:rev[r].append(q)
    seen=set();post=[]
    for root in adj:
        if root in seen:continue
        seen.add(root);stack=[(root,0)]
        while stack:
            x,i=stack[-1]
            if i==len(adj[x]):post.append(x);stack.pop();continue
            y=adj[x][i];stack[-1]=(x,i+1)
            if y not in seen:seen.add(y);stack.append((y,0))
    seen=set();out=[]
    for root in reversed(post):
        if root in seen:continue
        comp=[];stack=[root];seen.add(root)
        while stack:
            x=stack.pop();comp.append(x)
            for y in rev[x]:
                if y not in seen:seen.add(y);stack.append(y)
        out.append(sorted(comp))
    return sorted(out,key=lambda x:x[0])

def group(R:int,gens:list[int])->set[int]:
    H={1}
    for g in gens:
        if gcd(g,R)!=1:raise ValueError('nonunit generator')
        old=set(H);t=1
        while True:
            H|={x*t%R for x in old};t=t*g%R
            if t in old:break
    return H

def order(g:int,K:set[int],R:int)->int:
    x=1
    for j in range(1,R+1):
        x=x*g%R
        if x in K:return j
    raise ArithmeticError('order loop')

def obstruction(p:int,n:dict)->dict:
    R=n['R'];W=set(n['mu']);K={h for h in W if {h*w%R for w in W}==W}
    G=group(R,[-1,2]+[r for r,e in n['factors']]);targets=[R-1,(-p)%R,(-pow(p,-1,R))%R]
    reps={};cosets=[]
    for x in sorted(G):
        if x in reps:continue
        kk=sorted(x*h%R for h in K);rep=kk[0];cosets.append(kk)
        for y in kk:reps[y]=rep
    d=len(cosets);F={reps[t] for t in targets};active=[(r,e) for r,e in n['factors'] if r%R not in K]
    failed=not(n['E'] or n['M']);B=prod(r**e for r,e in n['factors'] if r%R in K)
    if failed:
        check(2*sum(e for r,e in active)<=d-1-len(F),'Turn1_joint_budget_in_auxiliary_domain')
        for r,e in active:check(order(r,K,R)>2*e+1,'Turn1_order_budget_in_auxiliary_domain')
        for size in range(1,1<<len(active)):
            chosen={r for i,(r,e) in enumerate(active) if size>>i&1}
            H=group(R,list(chosen));C={reps[x] for x in H}
            U={1}
            for r,e in n['factors']:
                if r not in chosen:U={x*pow(r,b,R)%R for x in U for b in range(-e,e+1)}
            FF={reps[t*pow(w,-1,R)%R] for t in targets for w in U}&C
            check(2*sum(e for r,e in active if r in chosen)<=len(C)-1-max(1,len(FF)),'Turn1_every_factor_cut_in_auxiliary_domain')
    if failed and d<=8:
        WB={u*pow(B,-1,R)%R for u in divisors(B,True)}
        check(WB==K and sum(e for r,e in active)<=2,'Turn1_low_order_inactive_saturation')
    if failed and n['sigma']==1 and d==6:
        check(len(active)==1 and active[0][1]==1 and len(n['edges'])==1 and n['edges'][0]==active[0],'primitive_sextic_forced_complete_edge')
    return {'K':sorted(K),'Gamma_order':len(G),'effective_index':d,
            'ambient_index':sum(gcd(x,R)==1 for x in range(1,R))//len(K),
            'support':sorted(W),'support_size':len(W),'fine_counts':sorted(n['mu'].items()),
            'targets':targets,'target_classes':[reps[t] for t in targets],
            'distinct_target_classes':len(F),'inactive_factor':B,'active':active}

def cycle_certificate(p:int,cyc:list[int],nodes:dict)->dict:
    if len(cyc)<2 or len(set(cyc))!=len(cyc):raise ValueError('simple directed cycle required')
    ell=len(cyc);cs=[];ss=[]
    for i,q in enumerate(cyc):
        r=cyc[(i+1)%ell]
        if r not in [x for x,e in nodes[q]['edges']]:raise ValueError('absent edge')
        cs.append(nodes[q]['a']//r);ss.append(nodes[q]['sigma'])
    D=4**ell*prod(cs);S=prod(ss);Ts=[]
    for shift in range(ell):
        den=1;sgn=1;t=0
        for j in range(ell):
            idx=(shift+j)%ell
            t=ss[idx]*t+den;sgn*=ss[idx];den*=4*cs[idx]
        check(den==D and sgn==S,'cycle_rotation_products')
        Ts.append(t)
    h=gcd(*Ts)
    check(D>S and (D-S)%h==0 and (D-S)//h==p,'cycle_prime_reconstruction')
    check([t//h for t in Ts]==cyc,'cycle_vertex_reconstruction')
    check(all((D-S)*q==p*t for q,t in zip(cyc,Ts)),'cycle_exact_fixed_point_equation')
    return {'cycle':cyc,'sigma':ss,'cofactors':cs,'D':D,'S':S,'T_rotations':Ts,'h':h,'p':p}

def structured_graph(p:int,ps:list[int],detailed:bool=False)->dict:
    nodes=make_graph(p,ps);dist,bad,layers=closure(nodes);comps=sccs(nodes)
    bottom=[C for C in comps if all(r in C for q in C for r,e in nodes[q]['edges'])]
    trapped=[C for C in bottom if all(not(nodes[q]['E'] or nodes[q]['M']) for q in C)]
    check(bool(bad)==bool(trapped),'sink_SCC_criterion')
    rec={'p':p,'vertices':len(nodes),'edge_support':sum(len(n['edges']) for n in nodes.values()),
         'edge_occurrences':sum(e for n in nodes.values() for r,e in n['edges']),
         'divisor_candidates':sum(sum(n['mu'].values()) for n in nodes.values()),
         'occupied_vertices':sum(bool(n['E'] or n['M']) for n in nodes.values()),
         'E_states':sum(len(n['E']) for n in nodes.values()),'M_states':sum(len(n['M']) for n in nodes.values()),
         'auxiliary_vertices':sum(not n['first_half'] for n in nodes.values()),
         'auxiliary_E_states':sum(len(n['E']) for n in nodes.values() if not n['first_half']),
         'trap_vertices':len(bad),'bottom_components':bottom,'failed_bottom_components':trapped,
         'max_escape_distance':max(dist.values(),default=0),'least_vertex':min(nodes),
         'least_vertex_escape':dist.get(min(nodes))}
    if detailed:
        rec['nodes']=[dict(n,mu=sorted(n['mu'].items()),escape_distance=dist.get(q),obstruction=obstruction(p,n)) for q,n in nodes.items()]
        rec['trap']=sorted(bad);rec['pruning_layers']=layers
    return rec,nodes

def graph_fixture_tests()->dict:
    """Exhaust finite loop-free graphs of <=4 vertices with nonempty successor sets."""
    counts=Counter()
    for n in range(2,5):
        choices=[]
        for q in range(n):
            others=[r for r in range(n) if r!=q]
            choices.append([[others[i] for i in range(n-1) if mask>>i&1] for mask in range(1,1<<(n-1))])
        for adj in product(*choices):
            for hitmask in range(1<<n):
                nodes={q:{'edges':[(r,1) for r in adj[q]],'E':[1] if hitmask>>q&1 else [],'M':[]} for q in range(n)}
                dist,bad,layers=closure(nodes);comps=sccs(nodes)
                trapped=[C for C in comps if all(r in C for q in C for r in adj[q]) and all(not(hitmask>>q&1) for q in C)]
                check(bool(bad)==bool(trapped),'abstract_sink_equivalence')
                counts[str(n)]+=1
    return dict(counts)

def negative_controls()->list[str]:
    out=[]
    def rejects(label,fn):
        try:fn()
        except (ArithmeticError,ValueError):out.append(label);return
        raise ArithmeticError('accepted negative control '+label)
    rejects('non-QR multiplier',lambda: source(2521,11,17))
    rejects('nonintegral shell',lambda:source(2521,11,3))
    # These two states are failed; positive sign or a cycle is not a witness.
    rejects('empty target advertised as a hit',lambda: reconstruct(2521,633,1,'M'))
    cyc=[11,211,683,89,17,643,113];nd=make_graph(2521,sieve(2521))
    rejects('cycle edge reversed without proof',lambda:cycle_certificate(2521,list(reversed(cyc)),nd))
    rejects('composite target replaces CRT by predecessor',lambda:check(3*89%51==(-2521)%51,'bad_target_unit'))
    rejects('failed cycle with exit called closed',lambda:check(all(r in {0,1} for q in (0,1) for r in {0:[1],1:[0,2]}[q]),'bad_closure'))
    rejects('gate zero implies absent source',lambda:check(not sum(nd[11]['mu'].values()),'supported_source_not_absent'))
    rejects('larger auxiliary range omitted',lambda:check(all(n['first_half'] for n in nd.values()),'bad_first_half_substitution'))
    return out

def main()->None:
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--bound',type=int,default=50000);ap.add_argument('--out',default='certificates');args=ap.parse_args()
    if args.bound<2521:ap.error('bound >=2521 for least-trap certificate')
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    ps=sieve(max(args.bound,808369));rows=[];stats=Counter();digest=hashlib.sha256()
    for p in ps:
        if p>args.bound:break
        if p%840 not in HARD:continue
        row,nodes=structured_graph(p,ps)
        # Turn1 extension is checked for every node through 5000, not claimed at all scan nodes.
        if p<=5000:
            for n in nodes.values(): obstruction(p,n)
        data=json.dumps(row,sort_keys=True,separators=(',',':'));digest.update((data+'\n').encode());rows.append(row)
        stats['primes']+=1
        for key in ('vertices','edge_support','edge_occurrences','divisor_candidates','occupied_vertices','E_states','M_states','auxiliary_vertices','auxiliary_E_states','trap_vertices'):
            stats[key]+=row[key]
        stats['primes_with_trap']+=bool(row['trap_vertices'])
        stats['primes_with_graph_hit']+=bool(row['occupied_vertices'])
        stats['least_start_trapped']+=row['least_vertex_escape'] is None
    examples={}
    for p in (1201,2521,3361,5569):
        check(p in ps,'displayed_graph_prime_by_sieve')
        examples[str(p)],nd=structured_graph(p,ps,True)
        if p in (2521,3361):
            cyc=[11,211,683,89,17,643,113] if p==2521 else [31,53,11,281,1051,1103]
            examples[str(p)]['cycle_identity']=cycle_certificate(p,cyc,nd)
    # Detailed known sextic chain and its eventual fully closed failed component.
    p=808369;check(p in ps,'large_example_prime_by_sieve');cyc=[19,28871,6977,8293,2003,67531];qset=[43]+cyc
    nd={q:source(p,q) for q in qset}
    examples[str(p)]={'p':p,'declared_scope':'listed nodes and the six-cycle, not the entire graph',
                      'nodes':[dict(n,mu=sorted(n['mu'].items()),obstruction=obstruction(p,n)) for n in nd.values()],
                      'cycle_identity':cycle_certificate(p,cyc,nd)}
    for q in cyc:check(all(r in cyc for r,e in nd[q]['edges']) and not(nd[q]['E'] or nd[q]['M']),'closed_808369_cycle')
    for p,pair in ((9241,(31,61)),(19609,(13,307)),(21169,(13,241))):
        nd={q:source(p,q) for q in pair}
        check(p in ps and all(q in ps for q in pair),'displayed_two_cycle_primality')
        examples['two_cycle_'+str(p)]={'p':p,'nodes':[dict(n,mu=sorted(n['mu'].items())) for n in nd.values()],
                                     'cycle_identity':cycle_certificate(p,list(pair),nd)}
    ev=source(3361,977)
    check(ev['edges']==[(11,2),(13,1)],'even_NR_factor_must_be_retained')
    examples['even_NR_edge']=dict(ev,p=3361,mu=sorted(ev['mu'].items()))
    # A real same-p extension, not an asserted automatic escape theorem.
    port=source(2521,11,5);check(16 in port['M'],'actual_multiplier5_escape')
    examples['multiplier_escape']={'source_vertex':11,'old_sigma':1,'new_sigma':5,
                                  'source':dict(port,mu=sorted(port['mu'].items())),
                                  'witness':reconstruct(2521,port['a'],16,'M')}
    # The shared raw divisor can lose its hit even when it remains available.
    n0=source(1801,19);n1=source(1801,13)
    check(13 in [r for r,e in n0['edges']] and 1 in n0['M'] and 1 not in n1['M'],'real_nonpreservation_of_a_middle_hit')
    examples['shared_divisor_gate_change']={'p':1801,'q':19,'r':13,'u':1,
        'a_source':n0['a'],'a_target':n1['a'],'R_source':n0['R'],'R_target':n1['R'],
        'common_divisors':divisors(gcd(n0['a'],n1['a']),True),'original_hit':reconstruct(1801,n0['a'],1,'M')}
    # Make the auxiliary-domain recoding present in the serialized certificates.
    n=source(1201,461)
    examples['auxiliary_recode']=reconstruct(1201,n['a'],24548,'E')
    first=next(r['p'] for r in rows if r['trap_vertices'])
    check(first==2521,'least_hard_prime_with_canonical_trap_in_complete_prefix')
    structural=graph_fixture_tests();negative=negative_controls()
    scan={'bound':args.bound,'universe':'primes in {1,121,169,289,361,529} mod840; all NR prime vertices q<p',
          'counts':dict(stats),'first_trap_prime':first,'rows_sha256':digest.hexdigest(),'rows':rows}
    trap_components=[]
    for pp in ('2521','3361','808369'):
        ee=examples[pp];cc=ee['cycle_identity'];vv=set(cc['cycle'])
        trap_components.append({'p':int(pp),'cycle_identity':cc,'nodes':[n for n in ee['nodes'] if n['q'] in vv]})
    traps={'components':trap_components,'genuine_ES_returns':[examples['multiplier_escape']['witness'],examples['shared_divisor_gate_change']['original_hit'],examples['auxiliary_recode']]}
    for name,obj in [('scan.json',scan),('examples.json',examples),('graph_fixtures.json',structural),('negative_controls.json',negative),('checks.json',dict(CHECKS)),('traps.json',traps)]:
        (out/name).write_text(json.dumps(obj,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'checks':sum(CHECKS.values()),'scan':dict(stats),'row_sha256':digest.hexdigest(),'negative_controls':len(negative)},sort_keys=True))
if __name__=='__main__':main()
