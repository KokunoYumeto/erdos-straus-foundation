#!/usr/bin/env python3
"""Exact finite replay. Its bounds are regression domains, not an ES cutoff."""
from __future__ import annotations
import argparse, hashlib, json, time
from itertools import product
from math import gcd, prod, isqrt
from pathlib import Path
from fractions import Fraction
import arithmetic as A

CHECKS=0

def check(ok,msg='verification failure'):
    global CHECKS;CHECKS+=1;A.need(ok,msg)

def add_hash(H,obj):
    H.update((json.dumps(obj,separators=(',',':'),sort_keys=True)+'\n').encode())

def abstract_cases():
    for D in range(2,26):
        for steps in product(range(D),repeat=2):
            for ns in product(range(1,6),repeat=2):yield D,steps,ns
    for D in (3,5,9):
        for steps in product(range(D),repeat=3):
            for ns in product(range(1,4),repeat=3):yield D,steps,ns

def verify_abstract():
    H=hashlib.sha256();count=positive=0;by={}
    for D,ls,ns in abstract_cases():
        C=A.convolution(D,ls,ns);cert=A.best_chain(D,ls,ns);L=cert['lower'];old=A.unit_lower(D,ls,ns)
        check(sum(C)==prod(ns));check(min(C)>=max(L,old))
        if L:
            positive+=1
            # Every target, with a genuine original bounded section.
            for target in range(D):
                vec=A.section_vector(D,ls,ns,cert['indices'],target)
                check(sum(l*t for l,t in zip(ls,vec))%D==target)
            rows=cert['rows']
            if all(ns[r['index']]==r['radix'] for r in rows):
                check(len(set(C))==1)
        count+=1;by.setdefault(str(D),[0,0])[0]+=1;by[str(D)][1]+=bool(L)
        add_hash(H,[D,list(ls),list(ns),C,L,old])
    # The cyclic carry is NOT coordinatewise addition in C3 x C3.
    carry=A.decode(9,[6,1],[0,1],3)
    check(carry=={1:0,0:2})
    return dict(cases=count,positive_chain_cases=positive,by_modulus=by,sha256=H.hexdigest(),
                carry_example=dict(D=9,steps=[6,1],left=[0,2],right=[0,1],sum=[2,0]))

def original_scan(bound):
    primes=A.sieve(bound);spf=A.spf(bound);tables=[];hash_all=hashlib.sha256()
    counts=dict(primes=0,shells=0,words=0,trace_E=0,trace_M=0,full_E=0,full_M=0,
                squareful_trace_shells=0,parts=0,chain_positive_parts=0,
                old_unit_positive_parts=0,chain_only_parts=0)
    for p in range(25,bound+1,24):
        if not primes[p]:continue
        counts['primes']+=1
        for a in range(p//4+1,(p-1)//2+1):
            R=4*a-p;fa=A.factor_spf(a,spf);ds=A.divs_f({q:2*e for q,e in fa.items()})
            direct=set();counts['shells']+=1;counts['words']+=len(ds)
            for u in ds:
                for tag,G in [('E',4*u+1),('M',p+4*u)]:
                    g=G%R
                    if g*g%R==0:
                        direct.add((tag,u));counts['trace_'+tag]+=1
                    if g==0:counts['full_'+tag]+=1
            add_hash(hash_all,[p,a,sorted(direct)])
            if not direct:continue
            K,D,delta=A.residual(R)
            if D==1:continue
            counts['squareful_trace_shells']+=1;seen=set()
            for tile in A.tile_parts(p,a,fa):
                ls=[v['step'] for v in tile['parts']];ns=[v['length'] for v in tile['parts']]
                C=A.convolution(D,ls,ns);literal=[0]*D;full=0
                for vec in product(*(range(n) for n in ns)):
                    u=A.tile_word(tile,vec);key=(tile['channel'],u);check(key not in seen);seen.add(key)
                    eta=int(tile['channel']=='E');z=pow(p,eta,R)*u*pow(a,-1,R)%R
                    check((z+1)%K==0);c=((z+1)//K)%D
                    check(c==(tile['target']-sum(l*t for l,t in zip(ls,vec)))%D)
                    literal[sum(l*t for l,t in zip(ls,vec))%D]+=1
                    G=4*u+1 if eta else p+4*u
                    check((G%R==0)==(c==0));full+=G%R==0
                check(C==literal and full==C[tile['target']])
                best=A.best_chain(D,ls,ns);old=A.unit_lower(D,ls,ns)
                check(min(C)>=max(best['lower'],old))
                stab=[s for s in range(D) if all(C[(x+s)%D]==C[x] for x in range(D))]
                counts['parts']+=1;counts['chain_positive_parts']+=best['lower']>0
                counts['old_unit_positive_parts']+=old>0
                counts['chain_only_parts']+=best['lower']>0 and old==0
                tile.update(coefficients=C,chain=best,unit_lower=old,stabilizer=stab,
                            literal_full=full)
                if best['lower']:
                    vec=A.section_vector(D,ls,ns,best['indices'],tile['target'])
                    rec=A.state(p,a,A.tile_word(tile,vec),tile['channel']);check(rec['full'])
                    tile['returned_state']=rec
                tables.append(tile)
            check(seen==direct,'the original partition omitted or duplicated words')
    return dict(bound=bound,counts=counts,source_sha256=hash_all.hexdigest(),parts=tables)

def embedded_tile(p,a,selected,tag='M'):
    R=4*a-p;K,D,delta=A.residual(R);fa=A.factor(a);qs=sorted(fa);parts=[]
    for q in qs:
        o=A.order(q,K);lam=((pow(q,o,R)-1)//K)%D
        b,n=selected.get(q,(0,1))
        check(-fa[q]<=b and b+o*(n-1)<=fa[q])
        parts.append(dict(base=b,length=n,order=o,step=lam))
    z=A.prod(pow(q,v['base'],R) for q,v in zip(qs,parts))*pow(p,int(tag=='E'),R)%R
    check((z+1)%K==0)
    return dict(p=p,a=a,R=R,K=K,D=D,delta=delta,channel=tag,primes=qs,
                exponents=[fa[q] for q in qs],parts=parts,target=((z+1)//K)%D,
                domain='Explicit injective subpacket of the original exponent box; other words remain in the full source.')

def choose_example(qs,es,R):
    base=prod(q**e for q,e in zip(qs,es));H0=((R+1)//4)*pow(base,-1,210)%210
    if H0==0:H0=210
    for index in range(10000):
        H=H0+210*index;p=4*base*H-R
        if p>R and gcd(H,base)==1 and A.trial_prime(p):
            return dict(p=p,H=H,qs=qs,es=es,R=R,base=base,H0=H0,index=index,
                        prime_progression=[4*base*H0-R,840*base])
    raise ValueError('Declared finite example search cap exhausted')

def source_examples():
    packets=[];prime_roots=[]
    specs=[choose_example([53,163,271],[1,1,1],243),
           choose_example([89,271,1801],[1,2,1],675)]
    for sp in specs:
        p,H,qs,es,R=[sp[k] for k in ('p','H','qs','es','R')]
        check(A.trial_prime(p));prime_roots.extend([p,H]);prime_roots.extend(qs)
        base=sp['base'];a=H*base;check(4*a-p==R and p%840==1)
        allstates=[A.state(p,a,u,tag) for u in A.divs_f({q:2*e for q,e in A.factor(a).items()}) for tag in ('E','M')]
        selected={qs[0]:(-1,2),qs[1]:(-es[1],2*es[1]+1),qs[2]:(-es[2],2*es[2]+1)}
        tile=embedded_tile(p,a,selected)
        ls=[x['step'] for x in tile['parts']];ns=[x['length'] for x in tile['parts']]
        C=A.convolution(tile['D'],ls,ns);best=A.best_chain(tile['D'],ls,ns)
        check(best['lower']>0 and A.unit_lower(tile['D'],ls,ns)==0)
        check(len(set(C))==1 and C[0]==2)
        words=[]
        for vec in product(*(range(n) for n in ns)):
            rec=A.state(p,a,A.tile_word(tile,vec),tile['channel']);check(rec['trace']);words.append(rec)
        check(sum(r['full'] for r in words)==2)
        vec=A.section_vector(tile['D'],ls,ns,best['indices'],tile['target'])
        output=A.state(p,a,A.tile_word(tile,vec),tile['channel']);check(output['full'])
        for hold in (qs[1],qs[2]):
            restricted=[r for r in words if next(e['beta'] for e in r['exponents'] if e['prime']==hold)==0]
            check(restricted and not any(r['full'] for r in restricted))
        tile.update(coefficients=C,chain=best,unit_lower=0,words=words,section=vec,
                    returned_state=output,stabilizer=list(range(tile['D'])))
        p0,modulus=sp['prime_progression'];check(gcd(p0,modulus)==1 and (p-p0)==modulus*sp['index'])
        packets.append(dict(**sp,a=a,tiles=[tile],full_states=[r for r in allstates if r['full']],
                            all_original_word_count=len(allstates)//2))
    return packets,prime_roots

def upward_examples():
    p=67369;a=16849;source=A.state(p,a,4067,'M')
    check(A.trial_prime(p) and source['trace'] and not source['full'])
    C=source['R']+source['s'];cells=A.plus_cells(p,C);targets=A.plus_return(source)
    target=next(x['state'] for x in targets if x['state']['a']==16850)
    check((source['h'],source['r'],source['s'])==(83,7,29))
    check((C,p+C,target['u'],target['h'],target['r'],target['s'])==(56,67425,674,674,1,25))
    check(target['a']==a+1)
    prefix=[]
    for aa in range(p//4+1,a+2):
        states=[A.state(p,aa,u,c) for u in A.divs_f({q:2*e for q,e in A.factor(aa).items()}) for c in ('E','M')]
        full=[x for x in states if x['full']];trace=[x for x in states if x['trace']]
        if aa<=a:check(not full)
        prefix.append(dict(a=aa,R=4*aa-p,words=[dict(u=u, E=(4*u+1)%(4*aa-p), M=(p+4*u)%(4*aa-p))
            for u in A.divs_f({q:2*e for q,e in A.factor(aa).items()})],traces=trace,full=full))
    inverse=A.plus_inverse(target)
    check(any((x['a'],x['u'],x['channel'])==(a,4067,'M') for x in inverse))
    for rec in inverse:
        check(any(x['state']==target for x in A.plus_return(rec)))
    # All forward targets have the original ordered inverse.
    for row in targets:
        out=row['state'];den=[Fraction(*x) for x in out['denominators']]
        check(out['a']**2/(out['R']*den[1]-p*out['a'])==out['u'])
    # The whole p+C fibre is finite but need not have an E terminal.
    no=A.state(97,40,2,'M');empty=A.plus_cells(97,no['R']+no['s'])
    check(no['trace'] and not no['full'] and not A.plus_return(no))
    failures=[]
    for row in empty:
        aa=row['a'];states=[A.state(97,aa,u,c) for u in A.divs_f({q:2*e for q,e in A.factor(aa).items()}) for c in ('E','M')]
        check(not any(x['full'] for x in states))
        failures.append(dict(cell=row,states=states))
    # Unbounded linear progression: no polynomial-prime assumption.
    progression=[];k=0
    while len(progression)<8:
        h=83+4650*k;pp=812*h-27
        if A.trial_prime(pp):
            rec=A.state(pp,203*h,49*h,'M');check(rec['trace'] and not rec['full'] and rec['common_denominator']==3)
            targeta=203*h+1;hh=targeta//25
            out=A.state(pp,targeta,hh,'E');check(out['full'] and out['a']==rec['a']+1)
            check(pp%840==169 and targeta%25==0 and (pp+25)%31==0)
            check(any(x['state']==out for x in A.plus_return(rec)))
            # All old divisor-deletion candidates explicitly fail.
            for d in A.divisors(27):
                if d%3:continue
                check(d%(4*rec['r']*rec['s'])!=1)
                word_mod=4*prod(q**((e+1)//2) for q,e in A.factor(rec['u']).items())
                check(d%word_mod!=1)
            check(((3*3-1)//4)%rec['r']!=0)
            progression.append(dict(index=k,source=rec,target=out))
        k+=1
    check(gcd(67369,3775800)==1)
    return dict(critical_source=source,critical_target=target,C=C,M=p+C,cells=cells,
        targets=targets,inverse=inverse,prefix=prefix,
        progression=dict(residue=67369,modulus=3775800,prime_samples=progression),
        nonclosure=dict(source=no,complete_cells=failures)),[p]+[x['source']['p'] for x in progression]

def controls():
    examples=[]
    for D,ls,ns in [(9,[3,1],[2,2]),(3,[1,1],[2,2]),(5,[1],[2])]:
        C=A.convolution(D,ls,ns);best=A.best_chain(D,ls,ns)
        examples.append(dict(D=D,steps=ls,lengths=ns,coefficients=C,chain=best,
                             unit_lower=A.unit_lower(D,ls,ns)))
    check(gcd(9,*[3,1])==1 and examples[0]['coefficients'][2]==0)
    check(examples[1]['chain']['lower']==0 and min(examples[1]['coefficients'])==1)
    check(examples[2]['chain']['lower']==0 and examples[2]['coefficients'][1]==1)
    # Exactly D original words are a cardinality-sharp uniform section.
    sharp=[]
    for D,ls,ns in [(9,[6,1],[3,3]),(15,[6,10],[5,3]),(27,[9,3,1],[3,3,3])]:
        C=A.convolution(D,ls,ns);check(C==[1]*D)
        lost=[]
        for i in range(len(ns)):
            n=ns.copy();n[i]-=1;c=A.convolution(D,ls,n);check(0 in c and sum(c)<D);lost.append(dict(index=i,coefficients=c))
        sharp.append(dict(D=D,steps=ls,lengths=ns,coefficients=C,shortened=lost))
    return dict(nonimplications=examples,cardinality_sharpness=sharp,
        note='Shortened abstract boxes are not asserted to be separate ES counterexamples.')

def arithmetic_boundary():
    sp=choose_example([163,107],[1,2],243)
    p,H,R=sp['p'],sp['H'],sp['R'];a=sp['base']*H
    check(A.trial_prime(p) and p%840==1 and 4*a-p==R)
    tile=embedded_tile(p,a,{163:(-1,3),107:(-1,2)})
    words=[];bins=[0]*9
    for vec in product(*(range(row['length']) for row in tile['parts'])):
        rec=A.state(p,a,A.tile_word(tile,vec),'M');check(rec['trace'] and not rec['full'])
        bins[rec['defect']]+=1;words.append(rec)
    check(len(words)==6 and bins==[0,1,1,0,1,1,0,1,1])
    stabilizer=[t for t in range(9) if bins[t:]+bins[:t]==bins]
    check(stabilizer==[0,3,6])
    ls=[row['step'] for row in tile['parts']];ns=[row['length'] for row in tile['parts']]
    check(A.best_chain(9,ls,ns)['lower']==0)
    tile.update(words=words,defect_bins=bins,coefficients=bins,
                stabilizer=stabilizer,chain=A.best_chain(9,ls,ns))
    full=[A.state(p,a,u,c) for u in A.divs_f({q:2*e for q,e in A.factor(a).items()})
          for c in ('E','M') if ((4*u+1) if c=='E' else p+4*u)%R==0]
    witness=A.state(p,976015741,89,'E')
    check(witness['full'] and witness['R']==3)
    exact_progression=[p,840*sp['base']*sp['base']]
    check(gcd(*exact_progression)==1)
    return dict(**sp,a=a,part=tile,other_full_states=full,
                exact_exponent_progression=exact_progression,
                external_shell_witness=witness,
                nonclaim='The specified shell is empty, but the recorded R=3 exterior witness proves this prime satisfies Erdős--Straus.'),[p,H,*sp['qs']]

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--bound',type=int,default=10000)
    parser.add_argument('--out',default='certificates');args=parser.parse_args();out=Path(args.out)
    start=time.monotonic();abstract=verify_abstract();A.dump(out/'abstract.json',abstract)
    original=original_scan(args.bound);A.dump(out/'source_parts.json',original)
    packets,roots=source_examples();upward,other=upward_examples();roots+=other
    boundary,boundary_roots=arithmetic_boundary();roots.extend(boundary_roots);A.dump(out/'arithmetic_boundary.json',boundary)
    A.dump(out/'packets.json',packets);A.dump(out/'upward.json',upward);A.dump(out/'negative_controls.json',controls())
    A.dump(out/'prime_certificates.json',A.lucas_tree(sorted(set(roots))))
    files=['arithmetic_boundary.json','abstract.json','source_parts.json','packets.json','upward.json','negative_controls.json','prime_certificates.json']
    summary=dict(success=True,bound=args.bound,checks=CHECKS,source_counts=original['counts'],
        abstract_cases=abstract['cases'],source_sha256=original['source_sha256'],
        tables={name:hashlib.sha256((out/name).read_bytes()).hexdigest() for name in files},
        universal_ES_proved=False)
    A.dump(out/'summary.json',summary)
    print(json.dumps(dict(summary=summary,elapsed_seconds=round(time.monotonic()-start,3)),sort_keys=True))

if __name__=='__main__':main()
