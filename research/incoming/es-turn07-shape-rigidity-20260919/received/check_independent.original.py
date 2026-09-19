#!/usr/bin/env python3
"""Separate primitive h,r,s replay. No main-code or predecessor imports."""
from __future__ import annotations
import argparse, hashlib, json
from math import gcd, isqrt
from pathlib import Path

CHECKS=0

def req(ok,label):
    global CHECKS
    CHECKS+=1
    if not ok:raise ArithmeticError(label)

def prime(n):
    if n<2:return False
    return all(n%d for d in range(2,isqrt(n)+1))

def es(p,d):
    x,y,z=d
    return min(d)>0 and 4*x*y*z==p*(x*y+x*z+y*z)

def primitive(p):
    out={}
    for r in range(1,(p-1)//2+1):
      for s in range(1,(p-1)//(2*r)+1):
        if gcd(r,s)>1:continue
        rs=r*s
        lo=p//(4*rs)+1;hi=(p-1)//(2*rs)
        for h in range(lo,hi+1):
          a=h*rs;R=4*a-p
          if (p*r+s)%R:continue
          k=(p*r+s)//R;u=h*r*r;v=h*s*s;D=(4*u+1)//R
          req((4*u+1)%R==0 and k>r,'primitive exterior domain')
          req(es(p,[a,h*s*k,p*h*r*k]),'primitive identity')
          out[(a,u)]=(R,D,v,h,r,s,k)
    return out

def inspect(z,verify_prime=True):
    p,a,u=z['p'],z['a'],z['u'];R,D,v,h,r,s,k=(z[x] for x in ('R','D','v','h','r','s','kappa'))
    if verify_prime:req(prime(p),'displayed prime exact trial')
    req(a==h*r*s and u==h*r*r and gcd(r,s)==1,'marking')
    req(R==4*a-p and R*k==p*r+s and R*D==4*u+1,'gates and cofactor')
    req(v==a*a//u and es(p,z['denominators']),'complement and denominator return')
    al,be=v-R,v-D;B=al*be-1
    req(z['alpha']==al and z['beta_shape']==be and z['B']==B,'shape observation')
    req((2*a)**2==v**3-(al+be)*v*v+B*v,'curve equation')
    req((2*(2*a)-(v-al), (2*a)//2, ((v-al)*(v-be)-1)//4)==(p,a,u),'curve inverse')
    req(B%h==0 and (p-al)%h==0 and (p*be-1)%h==0,'original grade equations')
    if R==D and p%8==1:
        z0=(R-1)//2
        b=max(t for t in range(1,isqrt(z0)+1) if z0%(t*t)==0)
        delta=z0//(b*b)
        req(delta%4==3 and (p+1)%delta==0,'independent squarefree extraction')
        j=(delta+1)//4;c=(p+1)//delta;am=j*c
        req(es(p,[am,p*am,p*j]),'independent collision M return')
        req(min(c+1,delta)<R and (am+j)%(c+1)==0,'decreased cofactor and original M gate')
    return al,be,B

def profile_exclusion():
    result=[]
    for al in range(-7,8):
      for be in range(-7,8):
        if not al or not be or (al-be)%4:continue
        B=al*be-1
        if not B:continue
        for h in range(2,abs(B)+1):
          if B%h:continue
          if not any(prime(q) and q>7 and h%q==0 for q in range(11,h+1)):continue
          req(h in (11,13,17,37) and h==abs(B),'independent exceptional grade classification')
          survivors=[]
          for r in range(48):
            for s in range(48):
              if (4*r*r-h*s**4+(al+be)*s*s-B//h)%96:continue
              if (h*s*s-al)%4!=3:continue
              if (4*h*r*s-h*s*s+al)%24!=1:continue
              survivors.append([r,s])
          req(not survivors,'independent modulus96 necessary-state exclusion')
          result.append([al,be,B,h])
    return sorted(result)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input',type=Path,default=Path('certificates'));ap.add_argument('--out',type=Path,default=Path('independent.json'));ar=ap.parse_args()
    scan=json.loads((ar.input/'scan.json').read_text());rows=scan['rows']
    req([r['p'] for r in rows]==[p for p in range(17,scan['bound']+1,8) if prime(p)],'complete prime range')
    total=0
    for row in rows:
        p=row['p'];got=primitive(p);stored={(z['a'],z['u']):z for z in row['states']}
        req(set(got)==set(stored),'all primitive states equal original square-divisor states')
        qr={t*t%p for t in range(1,p)}
        for key,z in stored.items():
            req(got[key]==tuple(z[x] for x in ('R','D','v','h','r','s','kappa')),'all retained primitive coordinates')
            al,be,B=inspect(z,False);total+=1
            req(z['h']%p not in qr,'original grade nonresidue')
            if row['hard'] and max(abs(al),abs(be))<=7:
                n=z['r'];h=4*n*n-2
                req((al,be,z['s'],z['h'])==(-1,-1,1,h),'independent actual radius7 form')
                req(es(p,[h*n,p*h*n,p*n]),'independent same-shell M return')
    profiles=json.loads((ar.input/'profiles.json').read_text())
    req(profile_exclusion()==sorted([x['alpha'],x['beta'],x['B'],x['h']] for x in profiles['exceptional_profiles']),'complete profile agreement')
    rad8=json.loads((ar.input/'radius8.json').read_text())
    recovered=[]
    for ss in range(1,rad8['finite_prefix']['s_max']+1,2):
        xx=11*ss*ss-2
        if (xx*xx-37)%11:continue
        y2=(xx*xx-37)//11
        if y2<0:continue
        yy=isqrt(y2)
        if yy*yy!=y2 or yy%2:continue
        rr=yy//2;pp=44*rr*ss-11*ss*ss+8
        recovered.append(dict(r=rr,s=ss,p=pp,p_mod840=pp%840,gcd=gcd(rr,ss),hard_residue=pp%840 in {1,121,169,289,361,529}))
    req(recovered==rad8['finite_prefix']['points'],'independent Pell-coordinate prefix')
    ex=json.loads((ar.input/'examples.json').read_text())
    for z in ex['states']:inspect(z)
    for key in ('radius8_return','hard_middle_boundary'):
        z=ex[key];p=z['p'];ss=(p+3)//11
        req(z['h']==1 and z['r']==3 and z['s']==ss and z['Q']==11,'grade11 M marking')
        req(es(p,z['denominators']) and 11*z['a']==3*(p+3),'grade11 terminal identity')
    req(5951==11*541 and es(5951,[1550,37045,5951*155*10*239]),'positive cubic image is another parameter')
    for family in ex['singular_examples']+ex['certified_hard_singular_examples']:
        n=family['n'];E=family['exterior'];M=family['middle'];endpoint=family['endpoint']
        inspect(E, family in ex['certified_hard_singular_examples'])
        req(E['p']==16*n**3-4*n*n-8*n+1 and E['alpha']==E['beta_shape']==-1,'family exact equations')
        req(es(E['p'],M['denominators']) and M['a']==E['a'] and M['u']==n,'same-shell family return')
        req(es(E['p'],endpoint['denominators']) and endpoint['R']<E['R'],'family endpoint decrease')
    out=dict(success=True,bound=scan['bound'],primes=len(rows),E_states=total,checks=CHECKS,
             scan_sha256=hashlib.sha256((ar.input/'scan.json').read_bytes()).hexdigest(),
             source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             independence='Separate primitive h,r,s enumeration; modulus96 profile test; direct trial primality; no main or predecessor import.',
             universal_ES_proved=False)
    ar.out.parent.mkdir(parents=True,exist_ok=True);ar.out.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))
if __name__=='__main__':main()
