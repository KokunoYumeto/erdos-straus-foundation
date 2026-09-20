#!/usr/bin/env python3
"""Independent factor-free divisor/primitive-state replay. No main-module import."""
from __future__ import annotations
from collections import Counter,defaultdict
from functools import lru_cache
from math import gcd,isqrt
from pathlib import Path
import argparse,hashlib,json,time
CHECKS=0
HARD={1,121,169,289,361,529}
AA={1,2,3};BB={1,2,3,4,6,9,12,18,36}
def demand(v,label):
    global CHECKS
    CHECKS+=1
    if not v:raise ArithmeticError(label)
def canon(o):return json.dumps(o,sort_keys=True,separators=(',',':')).encode()
@lru_cache(None)
def ds(n):
    z=[]
    for d in range(1,isqrt(n)+1):
        if n%d==0:
            z.append(d)
            if d*d!=n:z.append(n//d)
    return sorted(z)
def prime(n):return n>=2 and all(n%d for d in range(2,isqrt(n)+1))
@lru_cache(None)
def fac(n):
    out=[];d=2
    while d*d<=n:
        if n%d==0:
            e=0
            while n%d==0:n//=d;e+=1
            out.append([d,e])
        d+=1
    if n>1:out.append([n,1])
    return out
def jac(a,n):
    ans=1
    for q,e in fac(n):
        z=pow(a%q,(q-1)//2,q)
        if z==0:return 0
        if z==q-1 and e%2:ans=-ans
    return ans

def compact(p,a,u,ch):
    R=4*a-p;g=gcd(a,u);h=g*g//u;r=u//g;s=a//g
    k=((p*r+s) if ch=='E' else (r+s))//R
    den=[a,h*s*k,p*h*r*k] if ch=='E' else [a,p*h*s*k,p*h*r*k]
    x,y,z=den
    demand(4*x*y*z==p*(x*y+x*z+y*z),'independent identity')
    num=a*a if ch=='E' else p*a*a
    demand(num==(R*y-p*a)*u,'independent ordered inverse')
    return [ch,a,u,R,h,r,s,k]+den

def target(p,E,side,t,W):
    a,u,R,h,r,s,k=E[1:8];j=(h+1)//4
    U=W if side=='alpha' else j*j//W
    RR=(p+4*U)//h;aa=(p+RR)//4
    demand((p+4*U)%h==0 and j*j%U==0 and 0<RR<p,'independent original cofactor return')
    demand(aa*aa%U==0 and (U+aa)%RR==0,'independent target original gate')
    return compact(p,aa,U,'M')

def capacity(data):
    tmax,jmax=data['target_bound'],data['j_bound'];tables=defaultdict(list);templates=[]
    for t in range(1,tmax+1):
        for ell in range(1,(t-2)//4+1):
            # Enumerate the complementary divisor V, not the main code's w.
            for V in ds(ell*ell):
                w=ell*ell//V;num=t-w;k=4*ell+1
                if num<=0 or num%k:continue
                n=num//k;j=ell+4*n*V;h=4*j-1
                if h<=t:continue
                W=j*j//V;g=gcd(ell,V)
                demand(j*j%V==0 and W==t+n*h and h<=t*t-3*t+1,'independent finite profile')
                row=dict(t=t,ell=ell,w=w,n=n,V=V,j=j,h=h,W=W,
                         canonical_available=j*j%t==0,primitive=[g*g//V,V//g,ell//g])
                templates.append(row);tables[t,j].append(W)
    templates.sort(key=lambda r:(r['t'],r['ell'],r['w']))
    demand(templates==data['templates'],'all independent finite templates')
    sha=hashlib.sha256();counts=Counter()
    for j in range(1,jmax+1):
        h=4*j-1;raw=defaultdict(list)
        # Trial every potential small factor of j^2, retaining both complements.
        for d in range(1,j+1):
            if j*j%d:continue
            pair=(d,) if d==j else (d,j*j//d)
            for W in pair:
                t=W%h
                if 1<=t<=tmax:raw[t].append(W)
        for t in range(1,min(tmax,h-1)+1):
            got=sorted(raw[t]);want=[]
            if j*j%t==0:want.append(t)
            if j%(4*t)==0:want.append(4*t*j)
            want.extend(tables[t,j]);want.sort()
            demand(got==want,'independent literal capacity')
            counts['target_grade_pairs']+=1
            for W in got:
                label='canonical' if W==t else ('companion' if W==4*t*j else 'finite')
                counts[label]+=1
                if j*j%t:counts['repairs']+=1
            sha.update(canon([t,j,got])+b'\n')
    demand(dict(counts)==data['counts'] and sha.hexdigest()==data['rows_sha256'],'capacity full digest and counts')
    co=data['coexistence']
    demand([d for d in ds(co['j']**2) if d%co['h']==co['t']]==co['words']==[289,5184],'independent two-word coefficient')
    for z in data['sharp_family']:
        ell=z['ell'];t=z['t'];j=z['j'];h=z['h'];W=z['W']
        demand(t==4*ell+2 and h==t*t-3*t+1 and W%h==t and j*j%W==0 and j*j%t!=0,'independent sharp family')

def full_scan(scan):
    bound=scan['bound'];tmax=scan['target_template_bound']
    ps=[p for p in range(5,bound+1,4) if prime(p)]
    demand(ps==[r['p'] for r in scan['rows']],'complete independently proved prime range')
    total=Counter()
    for row in scan['rows']:
        p=row['p'];states=[];sources={};ct=Counter();Es=[]
        for a in range(p//4+1,(p-1)//2+1):
            R=4*a-p
            # Unique coprime primitive r,s plus h, instead of factorization of a^2.
            for r in ds(a):
                for s in ds(a//r):
                    if gcd(r,s)>1:continue
                    h=a//(r*s);u=h*r*r;ct['original_divisor_vectors']+=1
                    if (p*r+s)%R==0:
                        E=compact(p,a,u,'E');states.append(E);Es.append(E);ct['E']+=1
                        sources[str(a)]=fac(a)
                    if (r+s)%R==0:
                        states.append(compact(p,a,u,'M'));ct['M']+=1;sources[str(a)]=fac(a)
        demand(sorted(states)==row['states'] and sources==row['occupied_factorizations'],'complete independent primitive source rows')
        old=set();new=set();auto=set();trans=[]
        for E in sorted(Es,key=lambda z:(z[1],z[2])):
            _,a,u,R,h,r,s,k,*_=E;v=a*a//u;D=(4*u+1)//R
            for side,val in [('alpha',R-v),('beta',D-v)]:
                if val<=0 or val%4:continue
                t=val//4;j=(h+1)//4
                demand(h%4==3 and s%2==1 and jac(t,h)==1,'independent grade character')
                available=j*j%t==0
                guarantee=False
                if p%24==1:
                    guarantee=t in (AA if side=='alpha' else BB)
                    if side=='beta':
                        demand(h%8==(7-4*t)%8,'independent beta 2-adic constraint')
                        if t%3==0:demand(h%3==2,'independent beta 3-adic constraint')
                    if guarantee:
                        demand(available,'independent forced budget');auto.add((a,u));ct['automatic_'+side]+=1
                chosen=[]
                if available:
                    chosen.append((t,'canonical'))
                    if isqrt(t)**2==t:old.add((a,u));ct['old_square_branches']+=1
                if h>t and t<=tmax and not available:
                    chosen.extend((W,'finite') for W in ds(j*j) if (W-t)%h==0)
                for W,kind in chosen:
                    M=target(p,E,side,t,W);new.add((a,u));ct['returned_pairs']+=1
                    trans.append(dict(source=E,side=side,t=t,j=j,W=W,kind=kind,automatic=guarantee,target=M))
        ct['old_square_source_states']=len(old);ct['new_return_source_states']=len(new)
        ct['new_source_states_beyond_old']=len(new-old);ct['automatic_source_states']=len(auto)
        demand(dict(ct)==row['counts'] and trans==row['transfers'],'independent original coefficient transport')
        total.update(ct)
    demand(dict(total)==scan['totals'],'independent aggregate counts')

def examples(ex):
    for name,z in ex.items():
        if 'source' not in z:continue
        E=z['source'];p=E['p'];a=E['a'];u=E['u'];h=E['h'];j=z['j'];t=z['t'];side=z['side']
        demand(prime(p) and p%840 in HARD,'displayed primality and hard class')
        demand(compact(p,a,u,'E')==[E['channel'],a,u,E['R'],h,E['r'],E['s'],E['k']]+E['denominators'],'displayed original marking')
        v=a*a//u;D=(4*u+1)//E['R']
        demand((v-E['R'] if side=='alpha' else v-D)==-4*t,'displayed shape')
        raw=ds(j*j);hits=[W for W in raw if (W-t)%h==0]
        demand(raw==[x['W'] for x in z['complete_capacity']] and hits==z['W_hits'],'complete displayed cofactor box')
        for W,M in zip(hits,z['targets']):
            mm=target(p,compact(p,a,u,'E'),side,t,W)
            demand(mm==[M['channel'],M['a'],M['u'],M['R'],M['h'],M['r'],M['s'],M['k']]+M['denominators'],'displayed target inverse')
    q=ex['inverse_domain_correction']
    demand(q['a']==q['h']*q['r']*q['s'] and q['R']==4*q['a']-q['p'] and (4*q['u']+1)%q['R']==1299,'explicit missing-gate correction')
    p,h,t=q['p'],q['h'],q['t'];N=(p+4*t)//h;got=[]
    for s in range(1,N+1):
        if N%s or (s+N//s)%4:continue
        r=(s+N//s)//4;a=h*r*s;R=4*a-p;u=h*r*r
        if gcd(r,s)!=1 or not(p<4*a and 2*a<p) or (4*u+1)%R:continue
        got.append(compact(p,a,u,'E'))
    demand(sorted(got)==q['correct_full_fibre'],'corrected full alpha fibre')
    z=ex['progression'];base=z['p_base'];step=z['p_step']
    demand(gcd(base,step)==1 and step==840*z['h']*z['R'],'reduced Dirichlet progression')
    demand(base+3*step==z['prime_member'] and prime(z['prime_member']),'certified progression prime')
    demand([d%43 for d in ds(11**2)]==[1,11,35],'all progression cofactor residues')
    for z in ex['prime_realized_sharp_progressions']:
        t=z['t'];h=z['h'];R=z['R'];j=z['j'];r=z['r_base'];p=z['p_base'];W=z['W']
        demand(t%420==6 and h==t*t-3*t+1 and R==t*t+t+1,'independent sharp progression coefficients')
        demand(gcd(p,z['p_step'])==1 and p%840==1 and p==4*h*r-R,'independent sharp Dirichlet progression')
        demand((4*h*r*r+1)%R==0 and j*j%W==0 and W%h==t and j*j%t!=0,'independent sharp prime-realizable word')

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--input',type=Path,default=Path('certificates'))
    ap.add_argument('--out',type=Path,default=Path('independent.json'));ar=ap.parse_args();start=time.monotonic()
    read=lambda n:json.loads((ar.input/n).read_text())
    cap=read('capacity.json');scan=read('scan.json');ex=read('examples.json');classes=read('character_classes.json')
    capacity(cap);full_scan(scan);examples(ex)
    for row in classes:
        t=row['t'];M=row['modulus']
        A=[a for a in range(3,M,4) if gcd(a,M)==1 and jac(t,a)==1]
        demand(A==row['allowed'] and (len(A)==1)==(t in AA),'independent character classes')
    result=dict(success=True,checks=CHECKS,bound=scan['bound'],primes=len(scan['rows']),
                target_bound=cap['target_bound'],j_bound=cap['j_bound'],totals=scan['totals'],
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                elapsed_seconds=time.monotonic()-start,independence='No main/predecessor import; trial divisors, primitive r/s enumeration, primewise Jacobi',
                universal_ES_proved=False,universal_TypeII_occupancy_proved=False)
    ar.out.parent.mkdir(parents=True,exist_ok=True);ar.out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,sort_keys=True))
if __name__=='__main__':main()
