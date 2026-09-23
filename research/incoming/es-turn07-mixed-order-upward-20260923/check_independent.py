#!/usr/bin/env python3
"""Separate standard-library implementation; imports no main/predecessor code."""
from fractions import Fraction
from itertools import product
from math import gcd, isqrt, prod
from pathlib import Path
import argparse, hashlib, json, time

checks=0

def ck(ok,msg='independent verification failure'):
    global checks;checks+=1
    if not ok:raise ValueError(msg)

def prime(n):
    if n<2:return False
    if n%2==0:return n==2
    d=3
    while d*d<=n:
        if n%d==0:return False
        d+=2
    return True

def factors(n):
    f=[];q=2
    while q*q<=n:
        if n%q==0:
            e=0
            while n%q==0:n//=q;e+=1
            f.append((q,e))
        q+=1 if q==2 else 2
    if n>1:f.append((n,1))
    return f

def divisors(n):
    f=factors(n)
    return sorted(prod(q**b for (q,e),b in zip(f,ex)) for ex in product(*(range(e+1) for q,e in f)))

def primitives(a):
    ds=divisors(a);ans=[]
    for r in ds:
        for s in divisors(a//r):
            if gcd(r,s)==1:
                h=a//(r*s);ans.append((h*r*r,h,r,s))
    ans.sort();return ans

def exact_counts(D,ls,ns):
    C=[0]*D
    for t in product(*(range(n) for n in ns)):
        C[sum(l*x for l,x in zip(ls,t))%D]+=1
    return C

def all_chain_best(D,ls,ns):
    # Exhaust every ordered subsequence, rather than the divisor DAG.
    best=0
    def walk(g,used,q):
        nonlocal best
        if g==1:
            L=q*prod(ns[i] for i in range(len(ns)) if i not in used)
            best=max(best,L);return
        for i,l in enumerate(ls):
            if i in used:continue
            d=gcd(g,l);m=g//d
            if m>1 and ns[i]>=m:walk(d,used+(i,),q*(ns[i]//m))
    walk(D,(),1);return best

def full_chain_certificate(D,ls,ns):
    """Exhaust every chain and reconstruct the complete stored witness."""
    best=None;best_path=None
    def walk(g,used,q,path):
        nonlocal best,best_path
        if g==1:
            value=q*prod(ns[i] for i in range(len(ns)) if i not in used)
            if best is None or value>best or value==best and path<best_path:
                best=value;best_path=path
            return
        for i,l in enumerate(ls):
            if i in used:continue
            d=gcd(g,l);m=g//d
            if m>1 and ns[i]>=m:
                walk(d,used+(i,),q*(ns[i]//m),path+(i,))
    walk(D,(),1,())

    reachable={D};edges=0
    for g in sorted(divisors(D),reverse=True):
        if g not in reachable:continue
        for l,n in zip(ls,ns):
            d=gcd(g,l);m=g//d
            if m>1 and n>=m:
                edges+=1;reachable.add(d)
    if best is None:
        return dict(lower=0,indices=[],reachable=sorted(reachable),edges=edges)
    g=D;rows=[]
    for i in best_path:
        d=gcd(g,ls[i]);m=g//d
        rows.append(dict(index=i,before=g,after=d,radix=m,step=ls[i]%D,
                         full_blocks=ns[i]//m))
        g=d
    ck(g==1)
    return dict(D=D,indices=list(best_path),rows=rows,lower=best,
                reachable=sorted(reachable),edges=edges)

def section_digits(D,ls,indices,target):
    """Independent reverse decoder for the zero-offset selected section."""
    g=D;rows=[]
    for i in indices:
        d=gcd(g,ls[i]);m=g//d
        ck(m>1);rows.append((i,g,d,m));g=d
    ck(g==1)
    c=target%D;answer={}
    for i,before,after,m in reversed(rows):
        ck(c%after==0)
        t=(c//after)*pow((ls[i]//after)%m,-1,m)%m
        answer[i]=t;c=(c-ls[i]*t)%D
        ck(c%before==0)
    ck(c==0)
    return answer

def oldbound(D,ls,ns):
    U=[i for i,l in enumerate(ls) if gcd(l,D)==1]
    return prod(ns[i] for i in range(len(ns)) if i not in U) if sum(ns[i]-1 for i in U)>=D-1 else 0

def hashline(H,x):H.update((json.dumps(x,separators=(',',':'),sort_keys=True)+'\n').encode())

def check_abstract(data):
    h=hashlib.sha256();cnt=0;pos=0
    for n,Ds,Ns in [(2,range(2,26),range(1,6)),(3,(3,5,9),range(1,4))]:
        for D in Ds:
            for ls in product(range(D),repeat=n):
                for ns in product(Ns,repeat=n):
                    C=exact_counts(D,ls,ns);B=all_chain_best(D,ls,ns);U=oldbound(D,ls,ns)
                    ck(min(C)>=max(B,U));cnt+=1;pos+=B>0
                    hashline(h,[D,list(ls),list(ns),C,B,U])
    ck(cnt==data['cases'] and pos==data['positive_chain_cases'])
    ck(h.hexdigest()==data['sha256'])
    return cnt

def check_state(t):
    p,a,R,u,h,r,s=(t[k] for k in ['p','a','R','u','h','r','s'])
    ck(p<4*a<2*p and R==4*a-p and h*r*s==a and h*r*r==u and gcd(r,s)==1)
    Q=Fraction(p*r+s,R) if t['channel']=='E' else Fraction(r+s,R)
    ck(t['quotient_name']==('kappa' if t['channel']=='E' else 'lambda'))
    ck(Fraction(*t['quotient'])==Q)
    ys=[h*s*Q,p*h*r*Q] if t['channel']=='E' else [p*h*s*Q,p*h*r*Q]
    ck([Fraction(*z) for z in t['denominators']]==[Fraction(a),*ys])
    ck(Fraction(1,a)+1/ys[0]+1/ys[1]==Fraction(4,p))
    trace=sum(ys).denominator==1;full=all(y.denominator==1 for y in ys)
    ck(trace==t['trace']);ck(full==t['full'])
    ck(max(y.denominator for y in ys)==t['common_denominator'])
    fs=factors(R);D=prod(q**(e//2) for q,e in fs);K=R//D;delta=R//(D*D)
    ck((t['K'],t['D'],t['delta'])==(K,D,delta))
    eta=int(t['channel']=='E');z=pow(p,eta,R)*u*pow(a,-1,R)%R
    ck(trace==((z+1)%K==0))
    defect=((z+1)//K)%D if trace else None
    ck(t['defect']==defect)
    G=4*u+1 if t['channel']=='E' else p+4*u
    ck(full==(G%R==0) and trace==(G*G%R==0))
    fa=dict(factors(a));fu=dict(factors(u))
    ck([e['prime'] for e in t['exponents']]==sorted(fa))
    for e in t['exponents']:
        q=e['prime'];x=a;y=u;va=vu=0
        while x%q==0:x//=q;va+=1
        while y%q==0:y//=q;vu+=1
        ck((va,vu,vu-va)==(e['e'],e['f'],e['beta']))
        ck((va,vu)==(fa[q],fu.get(q,0)))

def check_tile_structure(tile,p,a):
    """Rebuild a serialized original exponent part without main-module code."""
    R=4*a-p;fs=factors(R);D=prod(q**(e//2) for q,e in fs);K=R//D
    ck((tile['R'],tile['K'],tile['D'])==(R,K,D))
    fa=dict(factors(a));qs=sorted(fa)
    ck(tile['primes']==qs and tile['exponents']==[fa[q] for q in qs])
    ls=[];ns=[]
    for q,e,row in zip(qs,tile['exponents'],tile['parts']):
        o=1;z=q%K
        while z!=1:
            o+=1;z=z*q%K
            ck(o<=K)
        step=((pow(q,o,R)-1)//K)%D
        ck((row['order'],row['step'])==(o,step))
        members=[v for v in range(-e,e+1) if (v-row['base'])%o==0]
        ck(members==[row['base']+o*j for j in range(row['length'])])
        ls.append(step);ns.append(row['length'])
    eta=int(tile['channel']=='E');z=pow(p,eta,R)
    for q,row in zip(qs,tile['parts']):z=z*pow(q,row['base'],R)%R
    ck((z+1)%K==0 and ((z+1)//K)%D==tile['target'])
    ck(full_chain_certificate(D,ls,ns)==tile['chain'])
    return ls,ns

def selected_word(tile):
    ls=[row['step'] for row in tile['parts']]
    digits=section_digits(tile['D'],ls,tile['chain']['indices'],tile['target'])
    vec=[digits.get(i,0) for i in range(len(ls))]
    betas=[row['base']+row['order']*v for row,v in zip(tile['parts'],vec)]
    return prod(q**(e+b) for q,e,b in zip(tile['primes'],tile['exponents'],betas))

def check_source(data):
    bound=data['bound'];primes=[p for p in range(25,bound+1,24) if prime(p)]
    cache={a:primitives(a) for a in range(1,(bound-1)//2+1)}
    counts=dict(primes=len(primes),shells=0,words=0,trace_E=0,trace_M=0,full_E=0,full_M=0,
                squareful_trace_shells=0,parts=0,chain_positive_parts=0,old_unit_positive_parts=0,chain_only_parts=0)
    lookup={}
    for t in data['parts']:lookup.setdefault((t['p'],t['a']),[]).append(t)
    sourcehash=hashlib.sha256()
    for p in primes:
        for a in range(p//4+1,(p-1)//2+1):
            R=4*a-p;traces=set();counts['shells']+=1;counts['words']+=len(cache[a])
            for u,h,r,s in cache[a]:
                for tag,G in [('E',p*r+s),('M',r+s)]:
                    if G*G%R==0:traces.add((tag,u));counts['trace_'+tag]+=1
                    if G%R==0:counts['full_'+tag]+=1
            hashline(sourcehash,[p,a,sorted(traces)])
            fs=factors(R);D=prod(q**(e//2) for q,e in fs);K=R//D
            if D==1 or not traces:
                ck((p,a) not in lookup);continue
            counts['squareful_trace_shells']+=1;seen=set()
            for tile in lookup[(p,a)]:
                ls,ns=check_tile_structure(tile,p,a)
                qs=tile['primes'];es=tile['exponents'];C=exact_counts(D,ls,ns);full=0
                for vec in product(*(range(n) for n in ns)):
                    betas=[b['base']+b['order']*v for b,v in zip(tile['parts'],vec)]
                    u=prod(q**(e+b) for q,e,b in zip(qs,es,betas));key=(tile['channel'],u)
                    ck(key in traces and key not in seen);seen.add(key)
                    G=(4*u+1) if key[0]=='E' else p+4*u
                    full+=G%R==0
                ck(C==tile['coefficients'] and full==tile['literal_full']==C[tile['target']])
                best=all_chain_best(D,ls,ns);old=oldbound(D,ls,ns)
                ck(best==tile['chain']['lower'] and old==tile['unit_lower'])
                stab=[s for s in range(D) if C[s:]+C[:s]==C]
                ck(stab==tile['stabilizer'])
                counts['parts']+=1;counts['chain_positive_parts']+=best>0
                counts['old_unit_positive_parts']+=old>0;counts['chain_only_parts']+=best>0 and old==0
                if best:
                    indices=tile['chain']['indices'];g=D;digits=[]
                    for i in indices:
                        new=gcd(g,ls[i]);digits.append(g//new);g=new
                    codes=[sum(ls[i]*v for i,v in zip(indices,t))%D for t in product(*(range(d) for d in digits))]
                    ck(sorted(codes)==list(range(D)))
                    check_state(tile['returned_state'])
                    ck((tile['returned_state']['p'],tile['returned_state']['a'],
                        tile['returned_state']['channel'],tile['returned_state']['u'])
                       ==(p,a,tile['channel'],selected_word(tile)))
            ck(seen==traces)
    ck(counts==data['counts']);ck(sourcehash.hexdigest()==data['source_sha256'])
    return counts

def check_prime_tree(data):
    proved=set()
    for node in data['nodes']:
        n=node['n']
        if node['type']=='trial':ck(prime(n) and node['bound']==isqrt(n))
        else:
            f=node['factors'];base=node['base']
            ck(all(q in proved for q,e in f) and prod(q**e for q,e in f)==n-1)
            ck(pow(base,n-1,n)==1==node['power'])
            gs=[[q,gcd(pow(base,(n-1)//q,n)-1,n)] for q,e in f]
            ck(gs==node['gcds'] and all(d==1 for q,d in gs))
        proved.add(n)
    ck(all(n in proved for n in data['roots']))
    return proved,set(data['roots'])

def check_packets(data):
    required=set()
    for pack in data:
        p=pack['p'];a=pack['a'];R=pack['R'];ck(4*a-p==R and p%840==1)
        required.update([p,pack['H']]);required.update(pack['qs'])
        ck(prod(q**e for q,e in zip(pack['qs'],pack['es']))==pack['base'])
        ck(a==pack['H']*pack['base'] and gcd(pack['H'],pack['base'])==1)
        H0=((R+1)//4)*pow(pack['base'],-1,210)%210
        if H0==0:H0=210
        ck(pack['H0']==H0 and pack['H']==H0+210*pack['index'])
        ck(pack['prime_progression']==[4*pack['base']*H0-R,840*pack['base']])
        ck(gcd(*pack['prime_progression'])==1 and p==pack['prime_progression'][0]+pack['index']*pack['prime_progression'][1])
        pp=primitives(a);ck(len(pp)==pack['all_original_word_count'])
        allfull=[]
        for u,h,r,s in pp:
            for c,G in [('E',p*r+s),('M',r+s)]:
                if G%R==0:allfull.append((c,u))
        ck(sorted(allfull)==sorted((t['channel'],t['u']) for t in pack['full_states']))
        for t in pack['full_states']:check_state(t)
        for tile in pack['tiles']:
            ls,ns=check_tile_structure(tile,p,a);D=tile['D']
            ck(exact_counts(D,ls,ns)==[2]*D==tile['coefficients'])
            ck(all_chain_best(D,ls,ns)==2 and oldbound(D,ls,ns)==0)
            keys=[];expected=[]
            for vec in product(*(range(n) for n in ns)):
                betas=[z['base']+z['order']*v for z,v in zip(tile['parts'],vec)]
                expected.append(prod(q**(e+b) for q,e,b in zip(tile['primes'],tile['exponents'],betas)))
            for t in tile['words']:
                check_state(t);keys.append(t['u'])
                ck((t['p'],t['a'],t['channel'])==(p,a,tile['channel']))
            ck(keys==expected and len(keys)==2*D and len(set(keys))==len(keys))
            ck(sum(t['full'] for t in tile['words'])==2)
            for hold in pack['qs'][1:]:
                if tile['channel']!='M':continue
                restricted=[t for t in tile['words'] if next(v['beta'] for v in t['exponents'] if v['prime']==hold)==0]
                ck(restricted and not any(t['full'] for t in restricted))
            check_state(tile['returned_state'])
            ck((tile['returned_state']['p'],tile['returned_state']['a'],
                tile['returned_state']['channel'],tile['returned_state']['u'])
               ==(p,a,tile['channel'],selected_word(tile)))
    return required

def literal_cells(p,C):
    out=[]
    for a in range(p//4+1,(p-1)//2+1):
        s=C-(4*a-p)
        if s>0 and a%s==0:
            out.append(dict(p=p,C=C,M=p+C,s=s,n=a//s,a=a,R=4*a-p))
    return out

def check_upward(data):
    check_state(data['critical_source']);check_state(data['critical_target'])
    source=data['critical_source'];p=source['p'];C=data['C'];cells=literal_cells(p,C)
    ck(C==source['R']+source['s'] and data['M']==p+C==4*source['a']+source['s'])
    ck(cells==data['cells'])
    targetkeys=[(x['cell']['a'],x['state']['u']) for x in data['targets']]
    expect=[(c['a'],c['n']) for c in cells if (p+c['s'])%c['R']==0]
    ck(targetkeys==expect)
    for row in data['targets']:
        cell=row['cell'];t=row['state'];ck(cell in cells);check_state(t)
        ck((t['p'],t['a'],t['u'],t['channel'],t['h'],t['r'],t['s'])
           ==(p,cell['a'],cell['n'],'E',cell['n'],1,cell['s']))
        ck(cell['M']%cell['R']==0 and Fraction(*t['quotient'])==cell['M']//cell['R']-1)
    ck(any(row['state']==data['critical_target'] for row in data['targets']))
    inv=[]
    for cell in cells:
        for u,h,r,s in primitives(cell['a']):
            if s!=cell['s']:continue
            R=cell['R']
            for tag,G in [('E',p*r+s),('M',r+s)]:
                if G*G%R==0:inv.append((cell['a'],tag,u))
    ck(sorted(inv)==[(t['a'],t['channel'],t['u']) for t in data['inverse']])
    for t in data['inverse']:check_state(t)
    ck([row['a'] for row in data['prefix']]==list(range(p//4+1,data['critical_target']['a']+1)))
    for row in data['prefix']:
        a=row['a'];R=row['R'];expected=[]
        for u,h,r,s in primitives(a):
            expected.append(dict(u=u,E=(4*u+1)%R,M=(p+4*u)%R))
        ck(row['words']==expected)
        full=[(c,u) for u,h,r,s in primitives(a) for c,G in [('E',p*r+s),('M',r+s)] if G%R==0]
        trace=[(c,u) for u,h,r,s in primitives(a) for c,G in [('E',p*r+s),('M',r+s)] if G*G%R==0]
        ck(sorted(full)==sorted((t['channel'],t['u']) for t in row['full']))
        ck(sorted(trace)==sorted((t['channel'],t['u']) for t in row['traces']))
        for t in row['full']+row['traces']:check_state(t)
        if a<=16849:ck(not full)
    ck(gcd(data['progression']['residue'],data['progression']['modulus'])==1)
    ck((data['progression']['residue'],data['progression']['modulus'])==(67369,3775800))
    ck(len(data['progression']['prime_samples'])==8)
    required={p}
    for row in data['progression']['prime_samples']:
        s=row['source'];t=row['target'];k=row['index'];check_state(s);check_state(t)
        required.add(s['p']);ck(prime(s['p']))
        ck(s['p']==67369+3775800*k and s['h']==83+4650*k)
        ck(s['p']%840==169 and s['common_denominator']==3 and not s['full'] and t['full'])
        ck((s['a'],s['R'],s['u'],s['r'],s['s'])==(203*s['h'],27,49*s['h'],7,29))
        ck(t['a']==s['a']+1 and t['R']==31 and t['s']==25)
        ck((t['u'],t['h'],t['r'])==((203*s['h']+1)//25,(203*s['h']+1)//25,1))
        ck(Fraction(*t['quotient'])==(s['p']+25)//31)
        ck(4*s['a']+s['s']==4*t['a']+t['s'])
    ne=data['nonclosure'];check_state(ne['source']);p=97;C=83
    ck([x['cell'] for x in ne['complete_cells']]==literal_cells(p,C))
    for row in ne['complete_cells']:
        a=row['cell']['a'];states=row['states']
        expected=[(tag,u) for u,h,r,s in primitives(a) for tag in ('E','M')]
        ck([(t['channel'],t['u']) for t in states]==expected)
        ck(not any(t['full'] for t in states))
        for t in states:check_state(t)
    return required

def check_boundary(data):
    p=data['p'];a=data['a'];R=data['R'];tile=data['part'];ck(a==data['H']*163*107**2 and p==4*a-243 and p%840==1)
    ck(4*a-p==R==243)
    ls,ns=check_tile_structure(tile,p,a);bs=[0]*9;expected=[]
    for vec in product(*(range(n) for n in ns)):
        betas=[z['base']+z['order']*v for z,v in zip(tile['parts'],vec)]
        expected.append(prod(q**(e+b) for q,e,b in zip(tile['primes'],tile['exponents'],betas)))
    ck([t['u'] for t in tile['words']]==expected)
    beta_pairs=[]
    for rec in tile['words']:
        check_state(rec);ck(rec['trace'] and not rec['full']);bs[rec['defect']]+=1
        betas={e['prime']:e['beta'] for e in rec['exponents']}
        beta_pairs.append((betas[163],betas[107]))
    ck(sorted(beta_pairs)==[(-1,-1),(-1,1),(0,-1),(0,1),(1,-1),(1,1)])
    ck(bs==[0,1,1,0,1,1,0,1,1]==tile['defect_bins']==tile['coefficients'])
    stabilizer=[t for t in range(9) if bs[t:]+bs[:t]==bs]
    ck(stabilizer==[0,3,6]==tile['stabilizer'])
    ck(tile['chain']==full_chain_certificate(9,ls,ns) and tile['chain']['lower']==0)
    ck(data['exact_exponent_progression']==[p,840*(163*107**2)**2])
    ck(gcd(*data['exact_exponent_progression'])==1)
    ck(data['exact_exponent_progression'][0]==p)
    full=[(c,u) for u,h,r,s in primitives(a) for c,G in [('E',p*r+s),('M',r+s)] if G%R==0]
    ck(sorted(full)==sorted((r['channel'],r['u']) for r in data['other_full_states']))
    for rec in data['other_full_states']:check_state(rec)
    ck(not full)
    check_state(data['external_shell_witness'])
    ck(data['external_shell_witness']['full'])
    ck((data['external_shell_witness']['p'],data['external_shell_witness']['a'],
        data['external_shell_witness']['R'],data['external_shell_witness']['u'],
        data['external_shell_witness']['channel'])==(p,976015741,3,89,'E'))
    return {p,data['H'],*tile['primes']}

def check_controls(data):
    for row in data['nonimplications']:
        D=row['D']; ls=row['steps']; ns=row['lengths']
        ck(exact_counts(D,ls,ns)==row['coefficients'])
        ck(full_chain_certificate(D,ls,ns)==row['chain'])
        ck(oldbound(D,ls,ns)==row['unit_lower'])
    for row in data['cardinality_sharpness']:
        D=row['D']; ls=row['steps']; ns=row['lengths']
        ck(exact_counts(D,ls,ns)==[1]*D==row['coefficients'])
        for item in row['shortened']:
            nn=ns.copy(); nn[item['index']]-=1
            c=exact_counts(D,ls,nn)
            ck(c==item['coefficients'] and min(c)==0 and sum(c)<D)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input',default='certificates');ap.add_argument('--out',default='independent.json');args=ap.parse_args()
    path=Path(args.input);read=lambda n:json.loads((path/n).read_text())
    start=time.monotonic();ac=check_abstract(read('abstract.json'));counts=check_source(read('source_parts.json'))
    proved,roots=check_prime_tree(read('prime_certificates.json'))
    required=check_packets(read('packets.json'))
    required.update(check_boundary(read('arithmetic_boundary.json')))
    required.update(check_upward(read('upward.json')))
    ck(required<=roots<=proved);check_controls(read('negative_controls.json'))
    result=dict(success=True,checks=checks,bound=read('source_parts.json')['bound'],abstract_cases=ac,
        source_counts=counts,certified_prime_nodes=len(proved),universal_ES_proved=False,
        tables={n:hashlib.sha256((path/n).read_bytes()).hexdigest() for n in ['arithmetic_boundary.json','abstract.json','source_parts.json','packets.json','upward.json','negative_controls.json','prime_certificates.json']})
    Path(args.out).write_bytes((json.dumps(result,indent=2,sort_keys=True)+'\n').encode())
    print(json.dumps(dict(result=result,elapsed_seconds=round(time.monotonic()-start,3)),sort_keys=True))

if __name__=='__main__':main()
