#!/usr/bin/env python3
"""Complete bounded original-source replay for the fibre theorem; standard library."""
from __future__ import annotations
import argparse,json,hashlib
from collections import Counter,defaultdict
from pathlib import Path
from math import gcd,isqrt
from fractions import Fraction as F
import fibres as A
CHECKS=0

def check(ok,msg):
    global CHECKS
    CHECKS+=1
    if not ok:raise ArithmeticError(msg)

def save(path,obj):path.write_bytes((json.dumps(obj,indent=2,sort_keys=True)+'\n').encode('utf-8'))
def digest(obj):return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def primes(bound):
    sieve=bytearray(b'\1')*(bound+1);sieve[:2]=b'\0\0'
    for k in range(2,isqrt(bound)+1):
        if sieve[k]:sieve[k*k::k]=b'\0'*(((bound-k*k)//k)+1)
    return [i for i in range(2,bound+1) if sieve[i]]

def run(bound,out):
    counts=Counter(); groups=defaultdict(dict); targets={}; prime_list=[p for p in primes(bound) if p%24==1]
    for p in prime_list:
        for a in range((p+3)//4,(p+1)//2):
            R=4*a-p;cq=A.carrier(a);counts['shells']+=1
            for u in A.divs(a,2):
                counts['original_divisor_words']+=1
                if (a+u)%R==0:
                    y,z=A.tails(p,a,u,'M');check(y.denominator==z.denominator==1,'integer M reconstruction')
                    W=A.target(p,a,int(min(y,z)),int(max(y,z))); key=A.target_key(W)
                    targets[key]=W;counts['oriented_M_states']+=1
                if cq is None:continue
                for channel,G in [('E',4*u+1),('M',p+4*u)]:
                    if G*G%R:continue
                    for swap in ((0,1) if channel=='E' else (0,)):
                        rec=A.source_record(p,a,u,channel,swap); W=A.forward(rec);key=A.target_key(W)
                        check(A.source_key(rec) not in groups[key],'source label unique')
                        groups[key][A.source_key(rec)]=rec;targets[key]=W
                        counts['ordered_mixed_'+channel]+=1
                        counts['proper_ordered_mixed_'+channel]+=int(rec['defect']>1)
    all_fibres=[]; seen_sources=[]
    for key,W in sorted(targets.items()):
        inv=A.inverse_fibre(W); got={A.source_key(v) for v in inv}; expected=set(groups[key])
        check(got==expected,f'full bare fibre {key}')
        check(len(inv)%2==0,'even ordered fibre size')
        for rec in inv:
            old=groups[key][A.source_key(rec)]
            check(all(rec[k]==old[k] for k in old),'full original coordinate inverse')
            h,r,s=rec['h'],rec['r'],rec['s']
            check(A.box(rec['a'],rec['u'])==rec['box'],'original exponent ledger')
        nE=sum(v['channel']=='E' for v in inv); nM=len(inv)-nE
        counts['image_targets']+=bool(inv);counts['empty_target_fibres']+=not inv
        counts['cross_channel_targets']+=bool(nE and nM)
        counts['kernel_rank']+=max(0,len(inv)-1)
        counts['targets_without_t1_source']+=bool(inv and all(v['t']>1 for v in inv))
        all_fibres.append(dict(target=W,E_sources=nE,M_sources=nM,sources=inv))
        seen_sources.extend([list(A.source_key(v)) for v in inv])
    check(len(seen_sources)==sum(len(g) for g in groups.values()),'global source partition')
    examples=[]
    for vals in [(1009,255,24216,686120),(1129,308,3387,1043196),
                 (1249,326,7494,610761),(6841,1866,20523,12765306)]:
        W=A.target(*vals); inv=A.inverse_fibre(W)
        check(len(inv)==(2 if vals[0] in (1009,1129) else 4),'displayed fibre size')
        if vals[0] in (1009,1129):check(all(r['t']>1 for r in inv),'t=1 not in mixed source')
        else:check({r['channel'] for r in inv}=={'E','M'},'cross-channel collision')
        examples.append(dict(target=W,sources=inv))
    controls={}
    # A general automatic-ray section is not a mixed-carrier section.
    controls['t1_section_outside_carrier']=A.carrier(255) is None and A.carrier(285) is None
    # An extra factor of source s was the corrected intake formula error.
    src=A.source_record(6841,2454,1636,'E');p=src['p'];r=src['r'];s=src['s'];de=A.squarefree_part(src['R']);H=(de+1)//(4*r*s);J=(p*r+s)//de
    wrong=[F(H*s*J),F(p*H*s*J*r),F(p*H*s*r)]
    controls['old_extra_s_denominator_rejected']=sum((1/z for z in wrong),F())!=F(4,p)
    W=A.forward(src)
    controls['residual_not_cofactor']=W['R']!=de
    controls['carrier_not_dropped']=A.carrier(841) is None
    for k,v in controls.items():check(v,k)
    out.mkdir(parents=True,exist_ok=True)
    save(out/'fibres.json',dict(bound=bound,primes=prime_list,fibres=all_fibres))
    save(out/'examples.json',dict(examples=examples,negative_controls=controls))
    report=dict(success=True,bound=bound,primes=len(prime_list),checks=CHECKS,counts=dict(sorted(counts.items())),
                source_key_sha256=digest(sorted(seen_sources)),target_count=len(targets),
                universal_ES_proved=False,independent_human_review=False)
    save(out/'fibre_summary.json',report);print(json.dumps(report,sort_keys=True))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--bound',type=int,default=10000);p.add_argument('--out',type=Path,default=Path('certificates'))
    a=p.parse_args();run(a.bound,a.out)
