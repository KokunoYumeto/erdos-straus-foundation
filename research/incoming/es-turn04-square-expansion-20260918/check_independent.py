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

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--input',default='certificates')
    ap.add_argument('--out',default='independent_cofactor.json')
    args=ap.parse_args();expected=json.loads((Path(args.input)/'cofactor_certificate.json').read_text())
    demand(expected['m']==5,'published proof domain m=5')
    actual=run(5)
    for name,value in actual['counts'].items():
        demand(value==expected['counts'][name],'complete enumeration count '+name)
    demand(actual['range_profile_sha256']==expected['range_profile_sha256'],'complete range-profile digest')
    demand(actual['candidates']==[{'p':x['p'],'cycle':x['cycle']} for x in expected['cycles']],'complete cycle list')
    check_examples(expected)
    actual['explicit_checks']=CHECKS
    actual['scope']='Independent complete cofactor enumeration and three cycle exits only; not the separate bounded graph scan.'
    Path(args.out).write_text(json.dumps(actual,sort_keys=True,separators=(',',':'))+'\n')
    print(json.dumps({'counts':actual['counts'],'explicit_checks':CHECKS,'range_profile_sha256':actual['range_profile_sha256']},sort_keys=True))
if __name__=='__main__':main()
