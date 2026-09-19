#!/usr/bin/env python3
"""Original exterior shape, exact collision-to-middle return, and radius-seven rigidity.
Python standard library only. A bounded verification is not universal ES existence.
"""
from __future__ import annotations
import argparse, hashlib, json, time
from collections import Counter
from fractions import Fraction
from math import gcd, isqrt, prod
from pathlib import Path

HARD={1,121,169,289,361,529}
CHECKS=Counter()

def need(ok: bool,label: str)->None:
    CHECKS[label]+=1
    if not ok: raise ArithmeticError(label)

def factor(n: int)->dict[int,int]:
    if n<1: raise ValueError('positive factor input required')
    out={};q=2
    while q*q<=n:
        while n%q==0: out[q]=out.get(q,0)+1;n//=q
        q=3 if q==2 else q+2
    if n>1:out[n]=out.get(n,0)+1
    return out

def divisors(fs: dict[int,int],multiplier: int=1)->list[int]:
    out=[1]
    for q,e in sorted(fs.items()):out=[a*q**i for a in out for i in range(multiplier*e+1)]
    return sorted(out)

def primes_to(n:int)->list[int]:
    a=bytearray(b'\1')*(n+1)
    if n>=0:a[0]=0
    if n>=1:a[1]=0
    for q in range(2,isqrt(n)+1):
        if a[q]:a[q*q:n+1:q]=b'\0'*((n-q*q)//q+1)
    return [q for q in range(2,n+1) if a[q]]

def prime(n:int)->bool:
    if n<2:return False
    if n%2==0:return n==2
    return all(n%d for d in range(3,isqrt(n)+1,2))

def leg(a:int,p:int)->int:
    z=pow(a%p,(p-1)//2,p)
    return -1 if z==p-1 else z

def es(den:list[int],p:int)->bool:
    x,y,z=den
    return min(den)>0 and 4*x*y*z==p*(x*y+x*z+y*z)

def state(p:int,a:int,u:int)->dict:
    R=4*a-p
    need(p>1 and p%4==1 and p<4*a and 2*a<p and gcd(p,a)==1,'original unit first-half domain')
    need(u>0 and a*a%u==0 and (4*u+1)%R==0,'original exterior divisor and gate')
    g=gcd(a,u);h=g*g//u;r=u//g;s=a//g;k=(p*r+s)//R
    need(g*g%u==0 and h*r*s==a and h*r*r==u and gcd(r,s)==1,'original gcd inverse')
    need((p*r+s)%R==0 and k>r,'kappa and orientation')
    v=a*a//u;D=(4*u+1)//R;al=v-R;be=v-D;B=al*be-1
    den=[a,h*s*k,p*h*r*k]
    need(es(den,p),'ordered exterior identity')
    need(a*a//(R*den[1]-p*a)==u and a*a%(R*den[1]-p*a)==0,'ordered exterior inverse')
    need(p*D+1==4*h*r*k and (p+R)**2+4*v==4*v*R*D,'retained exterior norm')
    need(v==h*s*s and D*s==r+k and h>1 and gcd(h,R)==gcd(h,D)==1,'third-coordinate structure')
    need(v!=R and v!=D and (al-be)%4==0,'shape exceptional loci')
    X=v;Y=2*a
    need(Y*Y==X**3-(al+be)*X*X+B*X,'integral shape curve')
    need(B%h==0 and (p-al)%h==0 and (p*be-1)%h==0,'grade and character residue identities')
    need(16*B*B*((al-be)**2+4)==16*B*B*((al+be)**2-4*B),'discriminant identity')
    fs=factor(a);fu=factor(u)
    return dict(p=p,channel='E',a=a,R=R,u=u,h=h,r=r,s=s,kappa=k,v=v,D=D,
                alpha=al,beta_shape=be,B=B,X=X,Y=Y,denominators=den,
                a_factors=[[q,e] for q,e in sorted(fs.items())],
                beta_original=[[q,fu.get(q,0)-e] for q,e in sorted(fs.items())])

def curve_inverse(z:dict)->dict:
    X,Y,al,be=z['X'],z['Y'],z['alpha'],z['beta_shape']
    need(X>0 and Y>0 and Y%2==0,'curve inverse positive even domain')
    R=X-al;D=X-be;a=Y//2;p=2*Y-R
    need(R>0 and D>0 and R%4==D%4==3 and Y>R,'curve inverse residual and first-half domain')
    need((R*D-1)%4==0,'curve inverse integer divisor')
    u=(R*D-1)//4
    return state(p,a,u)

def middle(p:int,h:int,r:int,s:int,lam:int)->dict:
    a=h*r*s;R=4*a-p;u=h*r*r;Q=4*h*r*lam-1
    need(h>0 and min(r,s,lam)>0 and gcd(r,s)==1 and R*lam==r+s,'middle normalization')
    need(p<4*a and 2*a<p and 0<R<p and (u+a)%R==0 and a*a%u==0,'middle original source')
    den=[a,p*h*s*lam,p*h*r*lam]
    need(es(den,p),'ordered middle identity')
    need(Q*R==p+4*u and Q%4==3 and 0<Q<p,'middle cofactor marking')
    need(p*a*a%(R*den[1]-p*a)==0 and p*a*a//(R*den[1]-p*a)==u,'middle ordered inverse')
    return dict(p=p,channel='M',a=a,R=R,u=u,h=h,r=r,s=s,lambda_=lam,Q=Q,
                denominators=den,complement_u=a*a//u,complement_denominators=[den[0],den[2],den[1]])

def squarefree_part(n:int)->tuple[int,int]:
    fs=factor(n);delta=prod(q for q,e in fs.items() if e%2);t=prod(q**(e//2) for q,e in fs.items())
    need(n==delta*t*t,'squarefree part reconstruction')
    return delta,t

def collision_rescue(z:dict)->dict:
    p,R=z['p'],z['R']
    need(p%8==1 and R==z['D'],'collision map source')
    w=(R-1)//2;delta,t=squarefree_part(w)
    need(R%8==7 and delta%4==3 and delta>=3 and t%2==1,'collision residue and squarefree markings')
    need((p+1)%delta==0 and z['a']%delta==0 and delta<R,'actual endpoint divisor')
    c=(p+1)//delta;j=(delta+1)//4
    M=middle(p,j,1,c,1)
    need(M['Q']==delta and min(M['R'],M['Q'])<R,'strict small-cofactor decrease')
    Rback=2*delta*t*t+1;aback=(p+Rback)//4;uback=(Rback*Rback-1)//4
    need(state(p,aback,uback)==z,'collision fibre inverse')
    endpoint_a=(p+delta)//4
    E=state(p,endpoint_a,endpoint_a)
    need(E['R']==delta and E['kappa']==c and E['a']<z['a'],'strict endpoint residual decrease')
    return dict(source=z,delta=delta,square_factor=t,z=w,middle=M,endpoint=E,
                inverse_domain='delta squarefree, delta=3 mod4, odd t, R=2delta*t^2+1<p, u=(R^2-1)/4 divides ((p+R)/4)^2')

def singular(n:int)->dict:
    h=4*n*n-2;p=16*n**3-4*n*n-8*n+1
    E=state(p,h*n,h*n*n)
    need(E['alpha']==E['beta_shape']==-1 and E['R']==E['D']==h+1,'singular family')
    M=middle(p,n,1,h,1)
    need(M['a']==E['a'] and M['u']==n and M['Q']==4*n-1,'same-shell singular channel crossing')
    endpoint_a=n*(h-n+1);end=state(p,endpoint_a,endpoint_a)
    need(end['R']==4*n-1 and end['kappa']==h and end['a']<E['a'],'singular endpoint decrease')
    return dict(n=n,exterior=E,middle=M,endpoint=end)

def small_profile_table()->dict:
    table=[];exceptional=[]
    for al in range(-7,8):
      if al==0:continue
      for be in range(-7,8):
        if be==0 or (al-be)%4:continue
        B=al*be-1
        if B==0:
            need((al,be) in [(1,1),(-1,-1)],'complete singular integer profiles')
            table.append(dict(alpha=al,beta=be,B=B,kind='singular'));continue
        fs=factor(abs(B));large=[q for q in fs if q>7]
        if not large:
            table.append(dict(alpha=al,beta=be,B=B,kind='all grade primes are 2,3,5,7'));continue
        need(abs(B) in {11,13,17,37} and prime(abs(B)),'complete exceptional large-prime table')
        h=abs(B);solutions=[]
        for r in range(24):
          for s in range(24):
            if (4*r*r-h*s**4+(al+be)*s*s-B//h)%48:continue
            if (h*s*s-al)%4!=3:continue
            if (4*h*r*s-h*s*s+al)%24!=1:continue
            solutions.append([r,s])
        need(not solutions,'complete modular exclusion of nonsingular hard profile')
        row=dict(alpha=al,beta=be,B=B,h=h,modulus=48,r_s_period=24,solutions=solutions)
        exceptional.append(row);table.append({**row,'kind':'explicit modular exclusion'})
    return dict(radius=7,profiles=table,exceptional_profiles=exceptional,
                scope='Complete coefficient profiles; h is forced to |B| on every exceptional profile. No height extrapolation.')

def radius8_reduction()->dict:
    surviving=[];rows=[]
    for al in range(-8,9):
      for be in range(-8,9):
        if not al or not be or (al-be)%4 or max(abs(al),abs(be))!=8:continue
        B=al*be-1
        for h in divisors(factor(abs(B))):
          if h==1 or all(q<=7 for q in factor(h)):continue
          if any(x>0 and isqrt(x)**2==x for x in (al,be)):
            rows.append(dict(alpha=al,beta=be,h=h,reason='positive-square coordinate'));continue
          residues=[]
          for r in range(24):
            for ss in range(24):
              if (4*r*r-h*ss**4+(al+be)*ss*ss-B//h)%48:continue
              if (h*ss*ss-al)%4!=3:continue
              if (4*h*r*ss-h*ss*ss+al)%24!=1:continue
              residues.append([r,ss])
          rows.append(dict(alpha=al,beta=be,h=h,residues_mod24=residues))
          if residues:surviving.append([al,be,h])
    need(surviving==[[8,-4,11]],'radius-eight unique nonsingular hard candidate')
    prefix=[];limit=200000
    for ss in range(1,limit+1,2):
        numerator=11*ss**4-4*ss*ss-3
        if numerator%4:continue
        rr=isqrt(numerator//4)
        if 4*rr*rr==numerator:
            pp=44*rr*ss-11*ss*ss+8
            prefix.append(dict(r=rr,s=ss,p=pp,p_mod840=pp%840,gcd=gcd(rr,ss),
                               hard_residue=pp%840 in HARD))
    return dict(radius=8,additional_profiles=rows,surviving_nonsingular_profiles=surviving,
                equation='4 r^2 = 11 s^4 - 4 s^2 - 3',p='44 r s - 11 s^2 + 8',
                finite_prefix=dict(s_max=limit,odd_s_only=True,points=prefix),
                nonclaim='No complete integral-point theorem or global ES conclusion is inferred from the finite prefix.')

def check_shape(z:dict,hard:bool)->None:
    p,h,al,be,B=z['p'],z['h'],z['alpha'],z['beta_shape'],z['B']
    need(leg(h,p)==-1,'original nonresidue grade')
    for x in (al,be):
        need(not (x>0 and isqrt(x)**2==x),'positive-square shape excluded')
    if B:need(h<=abs(B),'bounded-shape grade constraint')
    if hard and max(abs(al),abs(be))<=7:
        n=z['r'];S=singular(n)
        need(S['exterior']==z,'radius-seven complete singular rigidity')
        need(z['s']==1 and n%2==0,'rigidity original orientation and parity')
    if hard and max(abs(al),abs(be))<=8 and B:
        need((al,be,h)==(8,-4,11) and (p+3)%11==0,'radius8 actual-state reduction')
        M=middle(p,1,3,(p+3)//11,1)
        need(11*M['a']==3*(p+3) and M['Q']==11,'radius8 middle coefficient forced')
    if z['R']==z['D']:collision_rescue(z)
    if B:
        X=Fraction(z['v']);Y=Fraction(2*z['a'])
        xp=Fraction(B)/X;yp=Fraction(B)*Y/(X*X)
        need(yp*yp==xp**3-(al+be)*xp*xp+B*xp,'exact rational cubic involution')
        need(Fraction(B)/xp==X and Fraction(B)*yp/(xp*xp)==Y,'rational involution inverse')
        if B>0 and xp.denominator==1:
            need(z['s'] in (1,2),'integral cubic image requires s divides 2')
            if z['s']==2:need(yp.denominator==1 and yp.numerator%2==1,'s2 image loses even-Y original domain')
            else:
                rp=xp-al;dp=xp-be;pp=2*yp-rp
                need(rp.denominator==dp.denominator==pp.denominator==1 and rp.numerator%4==dp.numerator%4==1 and pp.numerator%4==3,'s1 involution changes prime residue class')


def fixed()->dict:
    rows=[]
    for p,a,u in [(48049,12090,24180),(2129,570,5700),(17,5,5),(17,6,12),(41,11,11)]:
        need(prime(p),'displayed exact trial primality')
        z=state(p,a,u);check_shape(z,p%840 in HARD);rows.append(z)
    collisions=[collision_rescue(z) for z in rows if z['R']==z['D']]
    families=[singular(n) for n in (2,4,14,24)]
    need(prime(97) and prime(929),'small singular prime examples')
    for n in range(2,102,2):singular(n)
    hard_examples=[]
    for n in range(2,1002,2):
        p=16*n**3-4*n*n-8*n+1
        if p%840 in HARD and prime(p):
            hard_examples.append(dict(prime_trial_bound=isqrt(p),**singular(n)))
            if len(hard_examples)==2:break
    radius8_return=middle(41,1,3,4,1)
    boundary_hard=middle(1009,1,3,92,1)
    small=next(z for z in rows if z['p']==17 and z['a']==5)
    need(max(abs(small['alpha']),abs(small['beta_shape']))<=7 and small['B']!=0,'hard hypothesis negative control')
    c=next(z for z in collisions if z['source']['p']==2129)
    need(c['delta']==3 and c['square_factor']==5 and c['middle']['R']>c['source']['R'],'measure is not residual alone')
    q=next(z for z in collisions if z['source']['p']==48049)
    need((q['source']['u']+q['source']['a'])%q['source']['R']!=0,'E divisor cannot be kept as M divisor')
    need(q['source']['h']!=q['middle']['h'],'channel normalization must change')
    need(isqrt(c['z']//15)**2!=c['z']//15,'radical is not squarefree part for inversion')
    for hh in range(1,13):
      for rr in range(1,13):
        for ss in range(1,13):
          if gcd(rr,ss)!=1:continue
          xx=Fraction(4*rr*rr,ss*ss)+hh*ss*ss-4*hh*rr*rr-2
          need(xx.denominator!=1 or xx<=0,'residual-one reverse source has no positive integral cubic image')
    return dict(states=rows,collision_returns=collisions,singular_examples=families,
                radius8_return=radius8_return,hard_middle_boundary=boundary_hard,
                certified_hard_singular_examples=hard_examples,
                hard_singular_search_domain='even n from 2 through 1000, stop after two exact trial-division prime examples; not a leastness assertion',
                negative_controls=['hard hypothesis cannot be dropped','residual alone need not decrease','unchanged E divisor is not the M return','h must be recomputed','radical is not the squarefree part'])

def main()->None:
    ap=argparse.ArgumentParser();ap.add_argument('--bound',type=int,default=3000);ap.add_argument('--out',type=Path,default=Path('certificates'))
    ar=ap.parse_args();need(ar.bound>=97,'declared replay domain');ar.out.mkdir(parents=True,exist_ok=True)
    start=time.monotonic();rows=[];tot=Counter()
    for p in primes_to(ar.bound):
        if p%8!=1:continue
        rec=dict(p=p,hard=p%840 in HARD,states=[]);tot['primes']+=1
        for a in range(p//4+1,(p-1)//2+1):
            tot['shells']+=1;R=4*a-p
            for u in divisors(factor(a),2):
                tot['original_divisor_vectors']+=1
                if (4*u+1)%R:continue
                z=state(p,a,u);need(curve_inverse(z)==z,'shape map inverse equality');check_shape(z,rec['hard'])
                rec['states'].append(z);tot['E_states']+=1
                if R==z['D']:tot['diagonal_states']+=1
                if rec['hard'] and max(abs(z['alpha']),abs(z['beta_shape']))<=7:tot['hard_radius7_states']+=1
        rows.append(rec)
    tables=small_profile_table();examples=fixed();extended=radius8_reduction()
    outputs={'scan.json':dict(bound=ar.bound,prime_domain='p prime and p=1 mod8',rows=rows,totals=dict(tot)),
             'profiles.json':tables,'examples.json':examples,'radius8.json':extended}
    for name,data in outputs.items():(ar.out/name).write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
    report=dict(success=True,bound=ar.bound,totals=dict(tot),checks=sum(CHECKS.values()),check_counts=dict(CHECKS),
                elapsed_seconds=time.monotonic()-start,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                output_sha256={n:hashlib.sha256((ar.out/n).read_bytes()).hexdigest() for n in outputs},
                universal_ES_proved=False,turn7_existence_milestone_completed=False)
    (ar.out/'verification.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n');print(json.dumps(report,sort_keys=True))
if __name__=='__main__':main()
