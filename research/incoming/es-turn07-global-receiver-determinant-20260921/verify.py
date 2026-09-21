#!/usr/bin/env python3
"""Exact universal polynomial certificates and a bounded original ES census.
Standard library only. No assert statements; python -O preserves every check.
The coefficient checks prove polynomial identities, not merely sampled signs.
The prime census is corroboration, not an ES existence theorem.
"""
from __future__ import annotations
import argparse, hashlib, itertools, json
from fractions import Fraction as F
from math import comb, gcd, isqrt
from pathlib import Path

CHECKS = 0

def check(ok: bool, message: str) -> None:
    global CHECKS
    CHECKS += 1
    if not ok:
        raise ArithmeticError(message)

# Sparse exact Laurent polynomials; negative exponents are used only in A.
class Poly:
    def __init__(self, n: int, terms=None):
        self.n = n
        self.terms = {tuple(k): F(v) for k, v in (terms or {}).items() if v}
    @classmethod
    def const(cls, n, c):
        return cls(n, {(0,)*n: c})
    @classmethod
    def var(cls, n, k):
        ex = [0]*n; ex[k] = 1
        return cls(n, {tuple(ex): 1})
    def _coerce(self, other):
        return other if isinstance(other, Poly) else Poly.const(self.n, other)
    def __add__(self, other):
        other = self._coerce(other); out = dict(self.terms)
        for k,v in other.terms.items(): out[k] = out.get(k,0)+v
        return Poly(self.n,out)
    __radd__ = __add__
    def __neg__(self): return Poly(self.n,{k:-v for k,v in self.terms.items()})
    def __sub__(self, other): return self + (-self._coerce(other))
    def __rsub__(self, other): return self._coerce(other)-self
    def __mul__(self, other):
        other=self._coerce(other); out={}
        for a,x in self.terms.items():
            for b,y in other.terms.items():
                k=tuple(i+j for i,j in zip(a,b)); out[k]=out.get(k,0)+x*y
        return Poly(self.n,out)
    __rmul__=__mul__
    def __pow__(self, n):
        if n<0: raise ValueError('Use explicit Laurent monomials for negative powers.')
        ans=Poly.const(self.n,1); base=self
        while n:
            if n&1: ans=ans*base
            base=base*base; n//=2
        return ans
    def diff(self,k):
        out={}
        for ex,c in self.terms.items():
            if ex[k]:
                e=list(ex);e[k]-=1;out[tuple(e)]=c*ex[k]
        return Poly(self.n,out)
    def substitute(self, values):
        target=values[0].n; out=Poly.const(target,0)
        cache={}
        for ex,c in self.terms.items():
            term=Poly.const(target,c)
            for i,e in enumerate(ex):
                if e<0: raise ValueError('No negative exponent in this substitution.')
                if (i,e) not in cache: cache[(i,e)]=values[i]**e
                term=term*cache[(i,e)]
            out=out+term
        return out
    def evaluate(self,*xs):
        total=F(0)
        for ex,c in self.terms.items():
            term=c
            for x,e in zip(xs,ex): term*=F(x)**e
            total+=term
        return total
    def rows(self):
        out=[]
        for ex,c in sorted(self.terms.items()):
            if c.denominator != 1: raise ArithmeticError('Noninteger serialized polynomial.')
            out.append([list(ex),c.numerator])
        return out
    def bounds(self):
        return [max((e[k] for e in self.terms),default=0) for k in range(self.n)]

def determinant(M):
    n=len(M); out=M[0][0]*0
    for perm in itertools.permutations(range(n)):
        inv=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        v=1
        for i,j in enumerate(perm):v=v*M[i][j]
        out=out+((-1)**inv)*v
    return out

def receiving_F(A,B,C,D):
    return (20*(3*C-B*B)+A*(87*B**3-282*B*C-51*D)
      +A*A*(-28*B**4+22*B*B*C+431*C*C+204*B*D)
      +A**3*(224*B*B*D-168*B*C*C-856*C*D)-448*A**4*D*D)

def norm4(roots):
    S=sum(roots);e2=sum(roots[i]*roots[j] for i in range(4) for j in range(i+1,4))
    e3=sum(roots[i]*roots[j]*roots[k] for i in range(4) for j in range(i+1,4) for k in range(j+1,4))
    e4=roots[0]*roots[1]*roots[2]*roots[3]
    return norm_symmetric(S,e2,e3,e4)

def norm_symmetric(S,e2,e3,e4):
    return (60*e3*S**5-20*e2**2*S**4+87*e2**3*S**2-282*e2*e3*S**3
      -51*e4*S**4-28*e2**4+22*e2**2*e3*S+431*e3**2*S**2
      +204*e2*e4*S**2+224*e2**2*e4-168*e2*e3**2-856*e3*e4*S-448*e4**2)

def normalized_P(s,v):
    return (7168*v**4-(5568*s*s+5728*s-5888)*v**3
      +(320*s**4+2744*s**3+705*s*s-3350*s-903)*v*v
      +(-140*s**5-443*s**4+440*s**3+390*s*s+70*s-249)*v
      +20*s**6-7*s**5-26*s**4-7*s**3+20*s*s)

def phi(u):
    u=F(u)
    f=(5120*u**10+14592*u**9+7232*u**8-6400*u**7+1728*u**6
       +3904*u**5+432*u**4-400*u**3+113*u*u+57*u+5)
    return (2*u-1)**2*f/(4096*u**6)

C12=F(125873811,262144)
CM=F(327448292668,47045881)

def reduce_T(poly):
    # Coordinates A,B,C,D,T. T^4 = -A^-1 (T^3+B T^2+C T+D).
    out=dict(poly.terms)
    while any(e[4]>=4 for e in out):
        e=max((e for e in out if e[4]>=4),key=lambda e:e[4]);c=out.pop(e)
        base=list(e);base[0]-=1;base[4]-=4
        for shift in [(0,0,0,0,3),(0,1,0,0,2),(0,0,1,0,1),(0,0,0,1,0)]:
            k=tuple(a+b for a,b in zip(base,shift));out[k]=out.get(k,0)-c
            if out[k]==0:del out[k]
    return Poly(5,out)

def certificate_polynomials():
    A,B,C,D,T=[Poly.var(5,i) for i in range(5)]
    der=4*A*T**3+3*T*T+2*B*T+C
    original=[Poly.const(5,1),der,A*der**2+2*T*der,7*T*T*der-13*der**2]
    reduced=[reduce_T(q) for q in original]
    matrix=[]
    for q in reduced:
        row=[]
        for j in range(4):
            row.append(Poly(5,{e[:4]+(0,):c for e,c in q.terms.items() if e[4]==j}))
        matrix.append(row)
    coefficient_det=determinant(matrix)
    check(not (A*coefficient_det-4*receiving_F(A,B,C,D)).terms,'Original odd receiving determinant identity')
    root_remainders=[q.rows() for q in reduced]

    u,w=Poly.var(2,0),Poly.var(2,1)
    scale=16*w*u
    roots=[scale,4*u*(w+1),(w+1)*(4*w*u+w+1),4*w*u*(w+1+4*w*u)]
    raw=-norm4(roots)
    terms={}
    for ex,c in raw.terms.items():
        check(ex[0]>=2 and c.denominator==1 and c.numerator%64==0,'Exterior exact polynomial division')
        terms[(ex[0]-2,ex[1])]=c/64
    P=Poly(2,terms)
    check(P.bounds()==[12,16],'Exterior bidegree')
    shifts=[u+1,w+1]
    Pshift=P.substitute(shifts)
    Du=(u*P.diff(0)-6*P).substitute(shifts)
    Dw=(w*P.diff(1)-8*P).substitute(shifts)
    for name,Q in [('P_E',Pshift),('u_derivative',Du),('w_derivative',Dw)]:
        check(len(Q.terms)==221,name+' dense coefficient count')
        check(all(c>0 and c.denominator==1 for c in Q.terms.values()),name+' all coefficients positive')
    boundary=16384*(2*u-1)**2*(5120*u**10+14592*u**9+7232*u**8-6400*u**7
          +1728*u**6+3904*u**5+432*u**4-400*u**3+113*u*u+57*u+5)
    check(not (P.substitute([u,Poly.const(2,1)])-boundary).terms,'Exterior boundary polynomial')
    check(phi(2)==C12 and phi(5)>CM>C12 and phi(11)>CM,'Uniform exact constants')

    b,c=Poly.var(2,0),Poly.var(2,1)
    L=4*b*c-b-c; tt=(b+c)*L+b*c; vv=b*b*c*c
    abstract=normalized_P(b,c)
    check(not (abstract+norm_symmetric(1+b,b+4*c,5*c,c)).terms,
          "Complete normalized ES coefficient identity")
    H=Poly.const(2,0)
    for (i,j),aij in abstract.terms.items():
        check(i+j<=6,'Middle denominator power')
        H=H+aij*tt**i*vv**j*L**(6-i-j)
    HM=H.substitute([b+2,b+c+3]);LM=L.substitute([b+2,b+c+3])
    lower=CM.denominator*HM-CM.numerator*LM**6
    check(len(HM.terms)==192,'Middle coefficient count')
    check(all(z>0 for z in HM.terms.values()),'Middle polynomial positivity')
    check(len(lower.terms)==191 and all(z>0 for z in lower.terms.values()),'Exact middle lower comparison')
    check(lower.terms[(1,0)]>0 and lower.terms[(0,1)]>0,'Strict middle separation away from origin')
    check(HM.evaluate(0,0)==CM.numerator and LM.evaluate(0,0)**6==CM.denominator,'Middle constant equality')

    table=[]
    for i in range(13):
        table.append({'u_degree':i,'coefficients_per_row':17,
            'P_min':int(min(z for e,z in Pshift.terms.items() if e[0]==i)),
            'Du_min':int(min(z for e,z in Du.terms.items() if e[0]==i)),
            'Dw_min':int(min(z for e,z in Dw.terms.items() if e[0]==i))})
    middle_table=[]
    for j in range(13):
        row=[z for e,z in lower.terms.items() if e[1]==j]
        middle_table.append({'Y_degree':j,'nonzero_count':len(row),'minimum':int(min(row))})
    return {'version':1,'coefficient_convention':'sum c_ij X^i Y^j; integer values only',
       'source_remainders_A_B_C_D_T':root_remainders,
       'F_A_B_C_D_T':receiving_F(A,B,C,D).rows(),
       'P_E_u_w':P.rows(),'P_E_shifted':Pshift.rows(),
       'D_u_shifted':Du.rows(),'D_w_shifted':Dw.rows(),
       'H_M_shifted':HM.rows(),'middle_lower_polynomial':lower.rows(),
       'normalized_P_s_v':abstract.rows(),'middle_L_shifted':LM.rows(),
       'exterior_row_checks':table,'middle_row_checks':middle_table,
       'C12':[C12.numerator,C12.denominator],'C24':[CM.numerator,CM.denominator],
       'identity_status':'Universal finite coefficient equalities, not a numerical sign scan.'}

def sieve(bound):
    flags=bytearray(b'\1')*(bound+1)
    if bound>=1:flags[0:2]=b'\0\0'
    for q in range(2,isqrt(bound)+1):
        if flags[q]:flags[q*q::q]=b'\0'*(1+(bound-q*q)//q)
    return [p for p in range(2,bound+1) if flags[p]]

def factor(n):
    ans=[];q=2
    while q*q<=n:
        e=0
        while n%q==0:n//=q;e+=1
        if e:ans.append((q,e))
        q=3 if q==2 else q+2
    if n>1:ans.append((n,1))
    return ans

def divisors_square(fac):
    ds=[1]
    for q,e in fac:ds=[d*q**i for d in ds for i in range(2*e+1)]
    return sorted(ds)

def valuation(n,p):
    if n==0:raise ValueError('Valuation at zero is not finite.')
    n=abs(n);v=0
    while n%p==0:n//=p;v+=1
    return v

def census(bound):
    states=[];rows=[];totals={'shells':0,'divisor_words':0,'E':0,'M':0}; histogram={}
    for p in sieve(bound):
        if p%12!=1:continue
        row={'p':p,'shells':0,'divisor_words':0,'E':0,'M':0,'min_ratio_E':None,'min_ratio_M':None}
        minima={}
        for a in range(p//4+1,(p-1)//2+1):
            R=4*a-p;fac=factor(a);ds=divisors_square(fac)
            row['shells']+=1;row['divisor_words']+=len(ds)
            for u in ds:
                for tag,numerator in [('E',4*u+1),('M',a+u)]:
                    if numerator%R:continue
                    g=gcd(a,u);h=g*g//u;r=u//g;s=a//g
                    check(h*r*s==a and h*r*r==u and gcd(r,s)==1,'Original factor normalization')
                    quot=(p*r+s)//R if tag=='E' else (r+s)//R
                    check((p*r+s if tag=='E' else r+s)==R*quot,'Original quotient')
                    y=h*s*quot if tag=='E' else p*h*s*quot;z=p*h*r*quot
                    check(F(1,a)+F(1,y)+F(1,z)==F(4,p),'Original ES identity')
                    check((F(a*a,R*y-p*a) if tag=='E' else F(p*a*a,R*y-p*a))==u,'Ordered divisor inverse')
                    roots=[p,a,y,z];check(len(set(roots))==4,'Literal root distinctness')
                    S=sum(roots);N=norm4(roots)
                    check(isinstance(N,int) and N<0,'Global integer determinant sign')
                    ratio=F(-N,p**8)
                    if tag=='E':
                        check(u>=2 and p>R and F(z,y)>2,'Exterior original cone')
                        check(ratio>phi(u)>=C12,'Exterior exact graded lower bound')
                        check(pow(u%p,(p-1)//2,p)==p-1,'Exterior original character')
                        if p%24==1:check(u>=5 and ratio>CM,'p=1 mod24 exterior constant')
                    else:
                        bb,cc=sorted([y//p,z//p])
                        check(y%p==z%p==0 and bb>=2 and cc-bb>=1,'Middle integer separation cone')
                        check(ratio>=CM,'Middle universal lower bound')
                    check(ratio>=(CM if p%24==1 else C12),'Uniform witness lower bound')
                    signV=1
                    for i in range(4):
                        for j in range(i+1,4):signV*=1 if roots[j]>roots[i] else -1
                    eps=-signV # principal complex roots of 1/H'(ell_i)
                    det=F(-4*eps*N,S**3)
                    # A=-1/S, det O = eps*4 F/A^3 = -eps*4 N/S^3.
                    check(abs(det)==F(4*abs(N),S**3),'Signed determinant scale')
                    vp=valuation(N,p);key=tag+':'+str(vp);histogram[key]=histogram.get(key,0)+1
                    ebox=[]
                    for q,e in fac:
                        v=valuation(u,q) if u%q==0 else 0
                        ebox.append([q,e,v,v-e])
                    states.append({'p':p,'a':a,'R':R,'u':u,'channel':tag,'h':h,'r':r,'s':s,
                       'kappa' if tag=='E' else 'lambda':quot,'denominators':[a,y,z],
                       'factor_box_q_e_f_beta':ebox,'S':S,'N':N,'v_p_N':vp,
                       'principal_root_epsilon':eps,'det_O':[det.numerator,det.denominator]})
                    row[tag]+=1;minima[tag]=min(minima.get(tag,ratio),ratio)
        for tag in ['E','M']:
            if tag in minima:row['min_ratio_'+tag]=[minima[tag].numerator,minima[tag].denominator]
        for key in totals:totals[key]+=row[key]
        rows.append(row)
    return states,rows,totals,histogram

def fixed_examples():
    ans={}
    for p,a,u,tag in [(1009,253,11,'E'),(1009,253,11,'M'),(944329,236094,1444,'M')]:
        check(factor(p)==[(p,1)],'Fixed example primality')
        R=4*a-p;g=gcd(a,u);h=g*g//u;r=u//g;s=a//g
        k=(p*r+s)//R if tag=='E' else (r+s)//R
        y=h*s*k if tag=='E' else p*h*s*k;z=p*h*r*k
        check(F(1,a)+F(1,y)+F(1,z)==F(4,p),'Fixed witness')
        N=norm4([p,a,y,z]);check(N<0,'Fixed determinant')
        chars=[]
        for n in [-511,1241,-15]:
            val=pow(n%p,(p-1)//2,p);chars.append(-1 if val==p-1 else val)
        # Retain the rational Lagrange inverse of the moment evaluation map.
        # xi_j are restored through xi_j^2=1/d_j in the written signed inverse.
        rr=[p,a,y,z];SS=sum(rr)
        e2=sum(rr[i]*rr[j] for i in range(4) for j in range(i+1,4))
        e3=sum(rr[i]*rr[j]*rr[k] for i in range(4) for j in range(i+1,4) for k in range(j+1,4))
        aa,bb,cc=-F(1,SS),-F(e2,SS),F(e3,SS)
        lagrange=[]
        for ii,t in enumerate(rr):
            derivative=aa
            for kk,tt in enumerate(rr):
                if kk!=ii:derivative*=t-tt
            coefficients=[cc+bb*t+t*t+aa*t**3,bb+t+aa*t*t,1+aa*t,aa]
            for kk,tt in enumerate(rr):
                check(sum(co*tt**j for j,co in enumerate(coefficients))/derivative==int(ii==kk),
                      'Complete rational moment inverse')
            lagrange.append([[co.numerator,co.denominator] for co in coefficients])
        ans[f'{p}_{a}_{u}_{tag}']={'p':p,'a':a,'R':R,'u':u,'channel':tag,
            'h':h,'r':r,'s':s,'quotient':k,'denominators':[a,y,z],
            'N':N,'v_p_N':valuation(N,p),'old_character_tests':chars,
            'lagrange_numerator_rows':lagrange}
    expected={
      '1009_253_11_E':([253,87032,3818056],0,[-1,1,1]),
      '1009_253_11_M':([253,2042216,88792],2,[-1,1,1]),
      '944329_236094_1444_M':([236094,780326438241,4772638766],2,[1,1,1]),
    }
    for key,(denoms,vp,chars) in expected.items():
        row=ans[key]
        check(row['denominators']==denoms and row['v_p_N']==vp and row['old_character_tests']==chars,
              'Fixed example coordinates, valuation and characters')
    # A real sign-changing curve. Gap 1/10 cannot be the normalized gap of
    # two integer multiples of a prime p; endpoints are not integer ES witnesses.
    signs=[]
    for b in [F(3),F(4)]:
        c=b+F(1,10);a=b*c/(4*b*c-b-c);roots=[F(1),a,b,c];N=norm4(roots)
        check(F(1,a)+F(1,b)+F(1,c)==4 and F(1,4)<a<F(1,2),'Positive rational curve')
        signs.append({'b':str(b),'c':str(c),'a':str(a),'N':str(N),'sign':(N>0)-(N<0)})
    check(signs[0]['sign']==-1 and signs[1]['sign']==1,'Real counterdomain sign change')
    ans['positive_real_curve']=signs

    # Exact polynomial and uniqueness certificate for the positive-real receiver
    # singularity.  Scaling the four roots by 10*D clears every denominator;
    # homogeneity then gives N_scaled=1000*D^2*P.
    coeff_desc=[3617792000000000,-26154803200000000,70130040320000000,
      -88735357952000000,45725157043200000,12437702609920000,
      -28537312234432000,13617485725683200,-1729738000411520,
      -478292746960768,90264805813440,17381353732960,-951549897144,
      -455951154664,-51247817566,-3092472120,-110106797,-2195730,-19035]
    tt=Poly.var(1,0);DD=40*tt*tt-16*tt-1
    PP=Poly(1,{(18-i,):F(c) for i,c in enumerate(coeff_desc)})
    scaled=[10*DD,10*tt*(10*tt+1),10*DD*tt,DD*(10*tt+1)]
    check(not (norm4(scaled)-1000*DD**2*PP).terms,'Exact real singularity polynomial')
    dshift=PP.diff(0).substitute([tt+3])
    check(len(dshift.terms)==18 and all(c>0 for c in dshift.terms.values()),
          'Unique real singularity by positive shifted derivative')
    lo,hi=F(3053,1000),F(1527,500)
    check(PP.evaluate(lo)<0<PP.evaluate(hi),'Exact real singularity bracket')
    ans['positive_real_singularity_certificate']={
      'P_coefficients_descending_t18_to_t0':coeff_desc,
      'N_formula':'P(t)/(100000*(40*t^2-16*t-1)^6)',
      'positive_coefficients_of_P_prime_3_plus_X':len(dshift.terms),
      'exact_bracket':['3053/1000','1527/500'],
      'decimal_approximation':'3.05367681075890'}

    p,a,u=1009,321,9;R=4*a-p
    y=F(p*a+a*a//u,R);z=F(p*a+p*p*u,R);N=norm4([p,a,y,z])
    raw_expected=F(-28456858608453503750339508712505388643177415423168512,
                   1308342779541015625)
    check(a*a%u==0 and (4*u+1)%R!=0 and y==F(335338,275) and z==F(9486618,275),
          'Exact raw E gate-failure coordinates')
    check(F(1,a)+F(1,y)+F(1,z)==F(4,p) and y.denominator==z.denominator==275,
          'Raw E reciprocal identity and reduced denominators')
    check(N==raw_expected<0,'Exact raw E rational receiving quantity')
    ans['empty_original_gate_nonsingular_frame']={'p':p,'a':a,'R':R,'u':u,'channel':'E','y':str(y),'z':str(z),'N':str(N)}
    return ans

def negative_controls(examples):
    control=[]
    def record(name,ok):
        check(ok,name);control.append({'false_implication':name,'counterexample_verified':True})
    E=examples['1009_253_11_E'];M=examples['1009_253_11_M']
    record('Three negative characters are necessary for integral nonvanishing',
           E['old_character_tests']!=[-1,-1,-1] and E['N']<0)
    record('A nonzero determinant numerator is a p-adic unit',M['v_p_N']==2)
    raw=examples['empty_original_gate_nonsingular_frame']
    record('Invertible raw E receiver implies the original residual gate',
           F(raw['N'])<0 and (4*raw['u']+1)%raw['R']!=0 and F(raw['y']).denominator>1)
    curve=examples['positive_real_curve']
    record('Positive real ES roots always give negative receiving numerator',curve[1]['sign']==1)
    t=curve[1];a,b,c=F(t['a']),F(t['b']),F(t['c']);R=4*a-1
    u=a*a/(R*b-a)
    record('The exterior monotonic cone extends to every positive raw word',0<u<1 and t['sign']==1)
    return control

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--bound',type=int,default=3000);parser.add_argument('--out',type=Path,default=Path('certificates'))
    args=parser.parse_args()
    if args.bound<13:parser.error('bound must be at least13')
    args.out.mkdir(parents=True,exist_ok=True)
    poly=certificate_polynomials();states,rows,totals,hist=census(args.bound);examples=fixed_examples();controls=negative_controls(examples)
    def dump(name,data):
        (args.out/name).write_text(json.dumps(data,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    dump('polynomial_certificates.json',poly);dump('states.json',states);dump('scan.json',rows);dump('examples.json',examples);dump('negative_controls.json',controls)
    summary={'success':True,'bound':args.bound,'prime_domain':'p prime, p=1 mod12','primes':len(rows),'counts':totals,
       'determinant_valuation_histogram':hist,'checks':CHECKS,'negative_controls':len(controls),'universal_polynomial_checks':True,
       'universal_ES_proved':False,'independent_mathematical_review':False,
       'states_sha256':hashlib.sha256((args.out/'states.json').read_bytes()).hexdigest()}
    dump('summary.json',summary);print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
