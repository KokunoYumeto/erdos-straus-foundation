#!/usr/bin/env python3
"""Independent exact checker; does not import verify.py or predecessor code.
Polynomial identities are checked on full unisolvent grids with stated degree
bounds. This is not a random evaluation test. Signs are certified on the full
coefficient arrays, and the arithmetic scan uses primitive factorizations.
"""
from __future__ import annotations
import argparse, hashlib, itertools, json
from fractions import Fraction as Q
from math import comb, gcd, isqrt
from pathlib import Path

checks=0

def require(test,message):
    global checks
    checks+=1
    if not test:raise ArithmeticError(message)

def coeffs(rows):
    out={}
    for ex,c in rows:
        require(isinstance(c,int) and len(ex)==2 and all(isinstance(e,int) and e>=0 for e in ex),
                'Coefficient domain')
        require(tuple(ex) not in out,'No duplicate monomial')
        if c:out[tuple(ex)]=c
    return out

def value(poly,x,y):
    return sum(c*x**i*y**j for (i,j),c in poly.items())

def plus(P,R):
    S=dict(P)
    for k,c in R.items():S[k]=S.get(k,0)+c
    return {k:c for k,c in S.items() if c}

def times(P,R):
    S={}
    for (i,j),c in P.items():
        for (k,l),d in R.items():
            ex=(i+k,j+l);S[ex]=S.get(ex,0)+c*d
    return {k:c for k,c in S.items() if c}

def power(P,n):
    ans={(0,0):1}
    for _ in range(n):ans=times(ans,P)
    return ans

def translate_one(P):
    S={}
    for (i,j),c in P.items():
        for k in range(i+1):
            for l in range(j+1):
                ex=(k,l);S[ex]=S.get(ex,0)+c*comb(i,k)*comb(j,l)
    return {ex:c for ex,c in S.items() if c}

def source_N(rs):
    # Evaluate the unexpanded supplied receiving polynomial through literal
    # elementary symmetric coefficients. Do not reuse the integer expansion.
    e=[Q(1),Q(0),Q(0),Q(0),Q(0)]
    for r in rs:
        for j in range(4,0,-1):e[j]+=Q(r)*e[j-1]
    S=e[1];A=-1/S;B=-e[2]/S;C=e[3]/S;D=-e[4]/S
    F=(20*(3*C-B**2)+A*(87*B**3-282*B*C-51*D)
       +A**2*(-28*B**4+22*B**2*C+431*C**2+204*B*D)
       +A**3*(224*B**2*D-168*B*C**2-856*C*D)-448*A**4*D**2)
    return S**6*F

def check_universal(cert):
    P=coeffs(cert['P_E_u_w']);Ps=coeffs(cert['P_E_shifted'])
    Du=coeffs(cert['D_u_shifted']);Dw=coeffs(cert['D_w_shifted'])
    require(max(i for i,j in P)<=12 and max(j for i,j in P)<=16,'E supplied bidegree')
    # The norm numerator on four scaled roots has bidegree at most (16,16).
    # The comparison 64*u^2*P has no larger bidegree. 17x17 values establish
    # the complete polynomial identity over Q by repeated univariate uniqueness.
    for u in range(1,18):
        for w in range(1,18):
            roots=[16*w*u,4*u*(w+1),(w+1)*(4*w*u+w+1),4*w*u*(w+1+4*w*u)]
            require(source_N(roots)==-64*u*u*value(P,u,w),'Universal E grid identity')
    require(translate_one(P)==Ps,'Independent binomial translation')
    require(translate_one({ex:(ex[0]-6)*c for ex,c in P.items()})==Du,'Independent u derivative')
    require(translate_one({ex:(ex[1]-8)*c for ex,c in P.items()})==Dw,'Independent w derivative')
    for poly in (Ps,Du,Dw):
        require(len(poly)==221 and all(c>0 for c in poly.values()),'Full E positive coefficients')
    for u in range(1,14):
        f=5120*u**10+14592*u**9+7232*u**8-6400*u**7+1728*u**6+3904*u**5+432*u**4-400*u**3+113*u*u+57*u+5
        require(value(P,u,1)==16384*(2*u-1)**2*f,'Degree12 boundary identity')
    HM=coeffs(cert['H_M_shifted']);QM=coeffs(cert['middle_lower_polynomial'])
    require(max(i for i,j in HM)<=20 and max(j for i,j in HM)<=12,'M supplied degree bounds')
    # Four scaled roots have degree <=3 in X and <=2 in Y. The degree-eight
    # integer norm hence has bidegree <=(24,16). These 425 values prove identity.
    for X in range(25):
        for Y in range(17):
            b=X+2;c=X+Y+3;L=4*b*c-b-c
            require(source_N([L,b*c,b*L,c*L])==-L*L*value(HM,X,Y),'Universal M grid identity')
    LM={(2,0):4,(1,1):4,(1,0):18,(0,1):7,(0,0):19}
    expected=plus({e:47045881*c for e,c in HM.items()},
                  {e:-327448292668*c for e,c in power(LM,6).items()})
    require(expected==QM,'Independent M lower polynomial equality')
    require(len(QM)==191 and all(c>0 for c in QM.values()),'Full M nonnegative certificate')
    require(value(QM,0,0)==0,'M boundary constant')
    require(QM.get((1,0),0)>0 and QM.get((0,1),0)>0,
            'Strict M separation away from the boundary origin')
    return {'exterior_grid':[17,17],'middle_grid':[25,17],
            'grid_checks_prove_identities':True,'E_positive_coefficients_each':221,
            'M_comparison_positive_coefficients':191}

def prime(n):
    if n<2:return False
    return all(n%d for d in range(2,isqrt(n)+1))

def divisors(n):
    ans=[]
    for d in range(1,isqrt(n)+1):
        if n%d==0:
            ans.append(d)
            if d*d!=n:ans.append(n//d)
    return sorted(ans)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input',type=Path,default=Path('certificates'));ap.add_argument('--out',type=Path,default=Path('independent.json'))
    ar=ap.parse_args();cert=json.loads((ar.input/'polynomial_certificates.json').read_text());rep=check_universal(cert)
    supplied=json.loads((ar.input/'states.json').read_text());summary=json.loads((ar.input/'summary.json').read_text())
    bykey={(r['p'],r['a'],r['u'],r['channel']):r for r in supplied}
    require(len(bykey)==len(supplied),'Original states not duplicated')
    keys=set();total={'shells':0,'divisor_words':0,'E':0,'M':0};pp=0
    for p in range(13,summary['bound']+1,12):
        if not prime(p):continue
        pp+=1
        for a in range(p//4+1,(p-1)//2+1):
            R=4*a-p;total['shells']+=1
            for h in divisors(a):
                for r in divisors(a//h):
                    s=a//h//r
                    if gcd(r,s)!=1:continue
                    total['divisor_words']+=1;u=h*r*r
                    for tag,n in [('E',p*r+s),('M',r+s)]:
                        if n%R:continue
                        k=n//R;y=h*s*k*(p if tag=='M' else 1);z=p*h*r*k
                        key=p,a,u,tag;require(key in bykey and key not in keys,'Independent primitive state')
                        keys.add(key);d=bykey[key];total[tag]+=1
                        require(d['denominators']==[a,y,z] and [d['h'],d['r'],d['s']]==[h,r,s],'Original ordered return')
                        N=source_N([p,a,y,z]);require(N.denominator==1 and N.numerator==d['N']<0,'Independent exact norm')
                        lower=Q(327448292668,47045881) if p%24==1 else Q(125873811,262144)
                        require(-N>=lower*p**8,'Independent global determinant bound')
                        require(Q(1,a)+Q(1,y)+Q(1,z)==Q(4,p),'Rational ES equality')
                        require(len({p,a,y,z})==4,'Actual simple root domain')
    require(keys==set(bykey),'Complete primitive/source agreement')
    require(total==summary['counts'] and pp==summary['primes'],'Complete counts reproduced')
    examples=json.loads((ar.input/'examples.json').read_text())
    for key,d in examples.items():
        if 'denominators' in d:
            require(prime(d['p']),'Fixed example primality')
            require(source_N([d['p']]+d['denominators'])==d['N'],'Fixed literal determinant')
        elif key=='positive_real_curve':
            for row in d:
                rr=[Q(1),Q(row['a']),Q(row['b']),Q(row['c'])]
                require(source_N(rr)==Q(row['N']),'Positive real negative control')
        elif key=='positive_real_singularity_certificate':
            cc=d['P_coefficients_descending_t18_to_t0']
            require(len(cc)==19 and all(isinstance(c,int) for c in cc),'Real curve polynomial data')
            def pv(x):return sum(Q(c)*x**(18-i) for i,c in enumerate(cc))
            # Both sides have degree at most18 after clearing the displayed
            # denominator. Nineteen exact values prove the polynomial identity.
            for t in range(3,22):
                D=40*t*t-16*t-1;a=Q(t*(10*t+1),D)
                require(source_N([Q(1),a,Q(t),Q(10*t+1,10)])*100000*D**6==pv(Q(t)),
                        'Independent real curve polynomial identity')
            shifted=[]
            for k in range(18):
                shifted.append(sum(Q(cc[18-n])*n*Q(3)**(n-1-k)*Q(comb(n-1,k))
                                   for n in range(k+1,19)))
            require(all(c>0 for c in shifted),'Independent positive shifted derivative')
            lo,hi=Q(3053,1000),Q(1527,500)
            require(pv(lo)<0<pv(hi),'Independent exact real singularity bracket')
        else:
            require(source_N([d['p'],d['a'],Q(d['y']),Q(d['z'])])==Q(d['N']),'Gate failure retains nonzero determinant')
    rep.update({'success':True,'bound':summary['bound'],'primes':pp,'counts':total,'checks':checks,
                'imports_predecessor_or_main':False,'universal_ES_proved':False,
                'states_sha256':hashlib.sha256((ar.input/'states.json').read_bytes()).hexdigest()})
    ar.out.parent.mkdir(parents=True,exist_ok=True);ar.out.write_text(json.dumps(rep,indent=2,sort_keys=True)+'\n')
    print(json.dumps(rep,indent=2))
if __name__=='__main__':main()
