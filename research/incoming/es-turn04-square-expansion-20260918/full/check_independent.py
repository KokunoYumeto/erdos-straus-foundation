#!/usr/bin/env python3
"""Second implementation of the finite mixed square-source reduction.
No imports from the main verifier or its arithmetic modules. Positive cofactor
boxes are cut by binary search of the proved monotone inequalities, not by the
main implementation's affine coefficient calculation.
"""
from __future__ import annotations
import argparse, hashlib, json
from collections import Counter
from functools import reduce,lru_cache
from itertools import product
from math import gcd,isqrt,prod
from pathlib import Path
HARD={1,121,169,289,361,529}
CHECKS=0

def demand(test,message):
    global CHECKS
    CHECKS+=1
    if not test: raise ArithmeticError(message)

def inverse(ss,cs):
    """Expand one affine numerator; recover others from the original equations."""
    right=prod(ss);S=right;left=1;T0=0
    for s,c in zip(ss,cs):
        right//=s;T0+=left*right;left*=4*c
    den=left-S;ts=[T0]
    for s,c in zip(ss[:-1],cs[:-1]):
        ts.append((den+s*ts[-1])//(4*c))
    return den,ts

@lru_cache(None)
def prime(n):
    if n<2:return False
    return all(n%d for d in range(2,isqrt(n)+1))

def run(m):
    H=(2*m-1)**2;dig=hashlib.sha256();counts=Counter();candidates=set();typed=[]
    for ell in range(2,m+1):
        for ss in product((1,3),repeat=ell):
            for v in range(1,(H+2)//4+1):
                cap=(v*H-1)//(4*v-3)
                counts['ambient_profiles']+=(cap-v+1)**(ell-1)
                def fits(pre):
                    den,ts=inverse(ss,pre+(v,)*(ell-len(pre)))
                    return all(s*H*T>=3*den for s,T in zip(ss,ts))
                def visit(pre):
                    if not fits(pre):return
                    if len(pre)<ell:
                        lo=v;hi=cap+1
                        while lo<hi:
                            mid=(lo+hi)//2
                            if fits(pre+(mid,)):lo=mid+1
                            else:hi=mid
                        for x in range(v,lo):visit(pre+(x,))
                        return
                    counts['range_profiles']+=1
                    dig.update(bytes((ell,)+ss+pre))
                    den,ts=inverse(ss,pre);h=reduce(gcd,ts)
                    if den%h:return
                    p=den//h;qs=tuple(x//h for x in ts)
                    if p<1009 or p%840 not in HARD:return
                    counts['hard_profiles']+=1
                    if len(set(qs))!=ell or any(q<11 or q>=p or (1 if q%4==3 else 3)!=s for q,s in zip(qs,ss)):return
                    counts['typed_profiles']+=1;typed.append((p,qs,ss,pre))
                    demand(all(p+ss[i]*qs[i]==4*pre[i]*qs[(i+1)%ell] for i in range(ell)),'actual cycle equations')
                    if not prime(p) or not all(prime(q) for q in qs):return
                    counts['prime_profiles']+=1
                    qr={i*i%p for i in range(1,(p+1)//2)}
                    if any(q in qr for q in qs):return
                    counts['nonresidue_profiles']+=1
                    idx=qs.index(min(qs));cyc=qs[idx:]+qs[:idx];candidates.add((p,cyc))
                visit((v,))
    return {'m':m,'counts':dict(counts),'range_profile_sha256':dig.hexdigest(),
      'candidates':[{'p':p,'cycle':list(c)} for p,c in sorted(candidates)],
      'typed_sha256':hashlib.sha256(json.dumps(typed,separators=(',',':')).encode()).hexdigest()}

def check_examples(expected):
    for item in expected['cycles']:
        p=item['p'];C=item['cycle'];e=item['escape'];q=e['q'];t=e['t']
        demand(prime(p) and p%840 in HARD,'hard prime')
        qr={i*i%p for i in range(1,(p+1)//2)}
        demand(all(prime(r) and r not in qr for r in C),'all original vertices')
        for i,r in enumerate(C):
            s=1 if r%4==3 else 3
            a=(p+s*r)//4
            demand(a%C[(i+1)%len(C)]==0,'canonical edge')
        R=(1 if q%4==3 else 3)*q*t*t;A=(p+R)//4
        demand(t==3 and R==e['R'] and A==e['a'] and R<3*p,'marked source')
        demand(prod(r**v for r,v in e['factorization'])==A,'complete factorization product')
        demand(all(prime(r) for r,v in e['factorization']),'source factors prime')
        actual=[r for r,v in e['factorization'] if r not in qr and r not in C]
        demand(actual==e['outside_nonresidues'] and actual,'actual outgoing factor')
        demand(len(C)==5,'five vertices plus a new one')

def direct_divisors(a):
    """Different original-box implementation using literal divisibility."""
    return [d for d in range(1,a+1) if a*a%d==0]+[a*a//d for d in range(1,a) if a*a%d==0]

def extra_examples(folder):
    path=folder/'examples.json'
    if not path.exists():return {'status':'examples file absent; not checked'}
    data=json.loads(path.read_text());totals=Counter()
    for item in data['pair_all_square_sources']:
        p=item['p'];q=item['q'];t=item['t'];R=item['R'];A=item['a'];R0=(1 if q%4==3 else 3)*q
        demand(prime(p) and prime(q),'example primality')
        demand(R==R0*t*t and 4*A==p+R and R<3*p,'complete square source')
        ds=sorted(set(direct_divisors(A)))
        demand(len(ds)==item['divisor_count'],'complete distinct divisor count')
        for ch,eta in [('E',1),('M',p)]:
            projections=[];full=[]
            for u in ds:
                numerator=4*u+eta
                if numerator%R0:continue
                carry=numerator//R0;digit=carry%(t*t)
                projections.append({'u':u,'carry':carry,'digit':digit,'quotient':carry//(t*t)})
                if digit==0:full.append(u)
            demand(projections==item['channels'][ch]['base_candidates'],'complete carry coefficients')
            demand(full==item['channels'][ch]['hits']==[],'all valid squares locally empty')
            totals['base_candidates']+=len(projections)
        mu=Counter(u*pow(A,-1,R)%R for u in ds);W=set(mu)
        K=sorted(h for h in W if all(h*w%R in W for w in W))
        demand(K==item['obstruction']['K'],'actual fine stabilizer')
        demand(sorted(map(list,mu.items()))==item['obstruction']['fine_counts'],'original fine integer coefficients')
        totals['sources']+=1;totals['divisors']+=len(ds)
    bad=data['noncoprime_projection'];N=bad['source'];u=bad['u']
    demand(N['a']**2%u==0 and (4*u+1)%121==0 and (4*u+1)%1331!=0,'noncoprime projection failure')
    demand((4*u+1)//11==671 and 671%121==66,'retained extra valuation')
    for w in data['positive_states']:
        x,y,z=w['denominators'];p=w['p']
        demand(4*x*y*z==p*(x*y+x*z+y*z),'ordered ES identity')
        demand([w['ET_image'][i] for i in w['ET_to_original_permutation']]==w['denominators'],'literature order crosswalk')
        eta=1 if w['channel']=='E' else p
        demand(w['a']*w['a']%w['u']==0 and (4*w['u']+eta)%w['R']==0,'original gate')
    for ex in data['six_vertex_expansions']:
        p=ex['p'];seen={ex['start']};processed=[]
        for rec in ex['sources']:
            q=rec['q'];t=rec['t'];R=(1 if q%4==3 else 3)*q*t*t
            demand(q in seen and t in (1,3,5,7,9) and R<3*p,'available five-port expansion')
            A=(p+R)//4;fs=rec['factorization']
            demand(prod(r**e for r,e in fs)==A and all(prime(r) for r,e in fs),'expansion complete factor source')
            nr=[r for r,e in fs if pow(r,(p-1)//2,p)==p-1]
            demand(nr==[r for r,e in rec['edges']],'all expansion nonresidue factors')
            seen.update(nr)
        demand(sorted(seen)==ex['vertices'] and len(seen)>=6 and len(ex['sources'])<=25,'six distinct reachable vertices')
    return dict(totals)

def check_roots_and_scan(folder):
    answer={}
    fp=folder/'root_coefficients.json'
    if fp.exists():
        data=json.loads(fp.read_text());count=0
        for fixture in data['avoidance_fixtures']:
            p=fixture['p'];q=fixture['q'];ss=1 if q%4==3 else 3;N=fixture['N'];C=fixture['C']
            direct=[j for j in range(N) if all(((p+ss*q*(2*j+1)**2)//4)%r for r in C)]
            demand(direct==fixture['free_indices'],'independent literal C-free prefix')
            total=0
            for term in fixture['terms']:
                ds=term['primes'];mod=term['modulus'];zs=term['roots']
                demand(prod(ds)==mod,'root modulus product')
                demand(all(0<=x<mod and all(((p+ss*q*(2*x+1)**2)//4)%r==0 for r in ds) for x in zs),'all CRT roots')
                demand(len(set(zs))==len(zs)==2**len(ds),'complete CRT root cardinality')
                c=sum(1 for j in range(N) if all(((p+ss*q*(2*j+1)**2)//4)%r==0 for r in ds))
                demand(c==term['count'],'literal intersection count')
                total+=(-1)**len(ds)*c
            demand(total==len(direct),'independent inclusion exclusion')
            count+=1
        answer['root_fixtures']=count
    fp=folder/'scan.json'
    if fp.exists():
        expected=json.loads(fp.read_text());bound=expected['bound']
        primes=[n for n in range(2,bound+1) if prime(n)];rows=[];digest=hashlib.sha256()
        def factor_local(n):
            result=[]
            for r in primes:
                if r*r>n:break
                if n%r==0:
                    e=0
                    while n%r==0:n//=r;e+=1
                    result.append([r,e])
            if n>1:result.append([n,1])
            return result
        for p in primes:
            if p%840 not in HARD:continue
            qr={x*x%p for x in range(1,(p+1)//2)}
            V=[q for q in primes if q<p and q not in qr]
            adj={q:set() for q in V};hit=set();st=Counter()
            for q in V:
                sig=1 if q%4==3 else 3;R0=sig*q
                for t in range(1,isqrt((3*p-1)//R0)+1,2):
                    R=R0*t*t;A=(p+R)//4;fs=factor_local(A);ds=sorted(set(direct_divisors(A)))
                    edges=[[r,e] for r,e in fs if r not in qr];adj[q].update(r for r,e in edges)
                    channels={}
                    for ch,eta in [('E',1),('M',p)]:
                        co=Counter();hits=[]
                        for u in ds:
                            n=4*u+eta
                            if n%R0==0:co[(n//R0)%(t*t)]+=1
                            if n%R==0:hits.append(u)
                        channels[ch]={'hits':hits,'base_count':sum(co.values()),'carry_counts':sorted(co.items())}
                    rec={'p':p,'q':q,'sigma':sig,'t':t,'R':R,'a':A,'factorization':fs,'edges':edges,
                         'divisor_count':len(ds),'channels':channels}
                    digest.update(json.dumps(rec,sort_keys=True,separators=(',',':')).encode()+b'\n')
                    if channels['E']['hits'] or channels['M']['hits']:hit.add(q)
                    st['sources']+=1;st['divisor_vectors']+=len(ds)
                    st['edge_occurrences']+=sum(e for r,e in edges);st['port_edges']+=len(edges)
                    st['E']+=len(channels['E']['hits']);st['M']+=len(channels['M']['hits'])
            dist={q:0 for q in hit};level=0
            while True:
                new=[q for q in V if q not in dist and any(r in dist for r in adj[q])]
                if not new:break
                level+=1
                for q in new:dist[q]=level
            row={'p':p,'vertices':len(V),'hit_vertices':len(hit),'trapped_vertices':len(V)-len(dist),
                 'max_distance':max(dist.values(),default=0),**dict(st)}
            rows.append(row)
        demand(rows==expected['rows'],'complete bounded scan row equality')
        demand(digest.hexdigest()==expected['source_sha256'],'complete original square-source digest')
        answer['scan_primes']=len(rows);answer['scan_source_sha256']=digest.hexdigest()
    direct={}
    for m in (2,3,4):
        fp=folder/('cofactor_small_'+str(m)+'.json')
        if not fp.exists():continue
        e=json.loads(fp.read_text());H=(2*m-1)**2;d=hashlib.sha256();rawcount=0;accepted=0
        for ell in range(2,m+1):
            for ss in product((1,3),repeat=ell):
                for v in range(1,(H+2)//4+1):
                    cap=(v*H-1)//(4*v-3)
                    for tail in product(range(v,cap+1),repeat=ell-1):
                        cs=(v,)+tail;rawcount+=1;den,ts=inverse(ss,cs)
                        if all(sig*H*T>=3*den for sig,T in zip(ss,ts)):
                            accepted+=1;d.update(bytes((ell,)+ss+cs))
        demand(rawcount==e['counts']['ambient_profiles'],'unpruned small domain count')
        demand(accepted==e['counts']['range_profiles'] and d.hexdigest()==e['range_profile_sha256'],'unpruned small range digest')
        direct[str(m)]={'raw_profiles':rawcount,'range_profiles':accepted}
    answer['unpruned_small_domains']=direct
    return answer

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--input',default='certificates')
    ap.add_argument('--out',default='independent.json');args=ap.parse_args();folder=Path(args.input)
    expected=json.loads((folder/'cofactor_certificate.json').read_text());got=run(expected['m'])
    for key,val in got['counts'].items():demand(val==expected['counts'][key],'full enumeration '+key)
    demand(got['range_profile_sha256']==expected['range_profile_sha256'],'all range profile digest')
    demand(got['candidates']==[{'p':c['p'],'cycle':c['cycle']} for c in expected['cycles']],'all surviving cycles')
    check_examples(expected);got['example_counts']=extra_examples(folder);got['additional_replays']=check_roots_and_scan(folder);got['explicit_checks']=CHECKS
    got['imports_main_implementation']=False
    Path(args.out).write_text(json.dumps(got,sort_keys=True,separators=(',',':'))+'\n')
    print(json.dumps({'counts':got['counts'],'checks':CHECKS,'examples':got['example_counts']},sort_keys=True))
if __name__=='__main__':main()
