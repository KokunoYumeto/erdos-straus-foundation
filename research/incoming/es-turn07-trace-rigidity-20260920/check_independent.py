#!/usr/bin/env python3
"""Separate arithmetic checker. Does not import verify.py or predecessor code."""
from __future__ import annotations
import argparse
from collections import Counter,defaultdict
from fractions import Fraction
from math import gcd,isqrt,prod,factorial
from pathlib import Path
import json,time
NTEST=0

def require(x,why='independent check'):
    global NTEST
    NTEST+=1
    if not x:raise ArithmeticError(why)

def prime(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))

def factors(n):
    q=2;f=[]
    while q*q<=n:
        c=0
        while n%q==0:n//=q;c+=1
        if c:f.append((q,c))
        q+=1
    if n>1:f.append((n,1))
    return f

def divisors_square(n):
    out=[1]
    for q,e in factors(n):
        old=out;out=[]
        power=1
        for k in range(2*e+1):
            out.extend(power*d for d in old);power*=q
    return sorted(out)

def frac(pair):return Fraction(*pair)
def v(n,p):
    if n==0:return 10**6
    t=0
    while n%p==0:n//=p;t+=1
    return t

def canonical_signature(z):
    return (z['p'],z['a'],z['channel'],z['u'],z['h'],z['r'],z['s'],
            z.get('kappa',z.get('lambda')),tuple(z['denominators']))

def direct_primitive(bound):
    data=[];perprime=[];tot=Counter()
    for p in range(5,bound+1,4):
        if not prime(p):continue
        counts=Counter()
        for h in range(1,(p-1)//2+1):
            for r in range(1,(p-1)//(2*h)+1):
                hr=h*r
                for s in range(p//(4*hr)+1,(p-1)//(2*hr)+1):
                    if gcd(r,s)!=1:continue
                    a=hr*s;R=4*a-p;u=hr*r
                    for tag,numerator in [('E',p*r+s),('M',r+s)]:
                        if numerator%R:continue
                        k=numerator//R
                        xyz=(a,h*s*k,p*h*r*k) if tag=='E' else (a,p*h*s*k,p*h*r*k)
                        require(sum((Fraction(1,x) for x in xyz),Fraction())==Fraction(4,p))
                        require(a*a%u==0 and all(x>0 for x in xyz))
                        tr=p+sum(xyz);second=p*p+sum(x*x for x in xyz)
                        require(((tr-p)**2-(second-p*p))%8==0)
                        e2=((tr-p)**2-(second-p*p))//2
                        require(e2==sum(xyz[i]*xyz[j] for i in range(3) for j in range(i+1,3)))
                        require(p*e2//4==prod(xyz))
                        U=u if tag=='M' else p*u
                        yy=Fraction(p*a*(U+a),R*U);zz=Fraction(p*(a+U),R)
                        require((a,yy,zz)==xyz)
                        counts[tag]+=1
                        data.append((p,a,tag,u,h,r,s,k,xyz))
        for rowtag in ('E','M'):tot[rowtag]+=counts[rowtag]
        perprime.append({'p':p,**counts})
    return sorted(data),perprime,dict(tot)

def check_raw(source):
    rebuilt=[]
    for old in source['rows']:
        p,a,R=old['p'],old['a'],old['R'];L=p*a*a
        traces={};real=Counter();pairs=[];words=0
        for U in range((-a)%R,L+1,R):
            words+=1
            y=Fraction(p*a*(U+a),R*U)
            z=Fraction(p*(a+U),R)
            trace=Fraction(p+a)+y+z
            require(y.denominator==trace.denominator)
            if trace in traces:
                V=traces[trace];require(U*V==a*a and trace.denominator==1)
                pairs.append([V,U,int(trace)])
            else:traces[trace]=U
            if trace.denominator==1:
                tag='M' if (trace-a)%p==0 else 'E'
                real[tag]+=1
        row={'p':p,'a':a,'R':R,'raw_words':words,'trace_values':len(traces),
             'integer_trace_values':sum(q.denominator==1 for q in traces),
             'kernel_rank':words-len(traces),'E':real['E'],'M':real['M'],
             'collisions':pairs}
        require(row==old,'full raw trace row mismatch');rebuilt.append(row)
    return len(rebuilt)

def check_denominators(source):
    # An independent enumeration over the prescribed integral first trace.
    records=set()
    bnd=source['presentation_bound']
    for d in range(1,bnd+1):
        for S in range(1,7):
            for A in range(1,2*d+1):
                for B in range(A,2*d+1):
                    C=d*S-A-B
                    if not B<=C<=2*d:continue
                    if (A*A+B*B+C*C)%(d*d):continue
                    records.add((d,A,B,C))
    expected={tuple(r['presentation']) for r in source['records']}
    require(records==expected,'all rational moment presentations')
    for row in source['records']+[r['triple'] for r in source['constructions']]:
        xs=[frac(vv) for vv in row['x']];d=row['d']
        require([x.denominator for x in xs]==[d]*3)
        require(sum(xs)==row['moments'][0] and sum(x*x for x in xs)==row['moments'][1])
        rec=sum(1/x for x in xs);require(rec==frac(row['reciprocal']))
        require(d%2==1 and d%9!=0 and rec.numerator%d**3==0)
        require(all(q==3 or q%3==1 for q,e in factors(d)))
    for construction in source['constructions']:
        d=construction['d'];row=construction['triple'];L=construction['L']
        for local in construction['local']:
            q,e,mod=local['prime'],local['exponent'],local['modulus']
            require(prime(q) and mod==q**(2*e+1))
            A,B,C=[frac(vv)*d for vv in row['x']]
            require(all(vv.denominator==1 for vv in (A,B,C)))
            require((B-local['b'])%mod==0 and (C-local['c'])%mod==0)
            require(v(row['reciprocal'][0],q)==3*e)
    return len(expected),len(source['constructions'])

def check_relaxation(source):
    rows=[]
    for p in range(5,source['bound']+1,4):
        if not prime(p):continue
        c=Counter()
        for a in range(p//4+1,(p+1)//2):
            R=4*a-p;n=p*a
            for b in divisors_square(n):
                if b>=n:break
                c['ordered_representatives_tested']+=1
                cc=n*n//b
                yy=Fraction(n+b,R);zz=Fraction(n+cc,R)
                S=yy+zz
                if S.denominator!=1:continue
                c['trace_integral_pairs']+=1
                d=yy.denominator
                require(d==zz.denominator)
                require(d*d==R//gcd(R,int(S)))
                require((a*a+yy*yy+zz*zz).denominator==d*d)
                c['integral_pairs' if d==1 else 'nonintegral_pairs']+=1
        rows.append({'p':p,**c})
    require(rows==source['rows'],'trace relaxation rows')
    return len(rows)

class Quadratic:
    def __init__(self,a,b,D):self.a=Fraction(a);self.b=Fraction(b);self.D=D
    def __add__(self,other):
        if not isinstance(other,Quadratic):other=Quadratic(other,0,self.D)
        return Quadratic(self.a+other.a,self.b+other.b,self.D)
    __radd__=__add__
    def __mul__(self,other):
        if not isinstance(other,Quadratic):other=Quadratic(other,0,self.D)
        return Quadratic(self.a*other.a+self.D*self.b*other.b,
                         self.a*other.b+self.b*other.a,self.D)
    __rmul__=__mul__
    def inverse(self):
        den=self.a*self.a-self.D*self.b*self.b
        return Quadratic(self.a/den,-self.b/den,self.D)
    def power(self,n):
        out=Quadratic(1,0,self.D)
        for _ in range(n):out=out*self
        return out

def check_algebraic(rows):
    for row in rows:
        p,a,k,D=row['p'],row['a'],row['k'],row['discriminant']
        require(prime(p) and p%24==1 and p>=1009)
        count=sum(pow(x,(p-1)//2,p)==p-1 and pow((3*x-1)%p,(p-1)//2,p)==p-1 for x in range(1,p))
        require(count==row['residue_count']==(p-1)//4)
        require(pow(k,(p-1)//2,p)==pow((3*k-1)%p,(p-1)//2,p)==p-1)
        lower,upper=row['bracketing_integers']
        require(lower>0 and upper==lower+1 and lower*lower<D<upper*upper)
        require(D==9*k*k-4*a*k and 60*k<p*p)
        b=Quadratic(Fraction(3*k,2),Fraction(1,2),D)
        c=Quadratic(Fraction(3*k,2),Fraction(-1,2),D)
        roots=[Quadratic(a,0,D),p*b,p*c]
        inverse=roots[0].inverse()+roots[1].inverse()+roots[2].inverse()
        require(inverse.a==Fraction(4,p) and inverse.b==0)
        for n,moment in enumerate(row['moments_0_through_16']):
            result=sum((x.power(n) for x in roots),Quadratic(0,0,D))
            require(result.a==moment and result.b==0)
        for exponent,r in enumerate(row['local_sqrt_mod_p_powers'],1):
            require((r*r-D)%p**exponent==0)
        b0,c0=row['local_root_b_c_mod_p5'];mod=p**5
        require((b0*b0-3*k*b0+a*k)%mod==0 and (c0*c0-3*k*c0+a*k)%mod==0)
        require(all(x%p for x in (b0,c0,b0-c0,b0-1,c0-1)))
        require(pow((b0*c0)%p,(p-1)//2,p)==p-1)
        roots0=[p,a,p*b0,p*c0]
        ders=[v(prod(roots0[i]-roots0[j] for j in range(4) if i!=j),p) for i in range(4)]
        require(ders==row['derivative_valuations']==[2,0,2,2])
    return len(rows)

def check_examples(examples):
    for key in ('193','1009'):
        row=examples[key];p=int(key);xs=[frac(q) for q in row['triple']]
        require(sum(1/x for x in xs)==Fraction(4,p))
        require(sum(xs)==frac(row['trace1']) and sum(x*x for x in xs)==frac(row['trace2']))
        require(xs[1].denominator==xs[2].denominator==3 and row['trace2'][1]==9)
        a,R=row['compressed_a'],row['compressed_R']
        allu=divisors_square(a)
        require(all((4*u+1)%R and (a+u)%R for u in allu))
    for row in examples['foreign_prime'].values():
        xs=[frac(x) for x in row['triple']]
        require(sum(1/x for x in xs)==Fraction(4,35281))
        require(35281+sum(xs)==frac(row['literal_trace']))
        require(row['literal_trace'][1]==23)
    for row in examples['general_moment_examples']:
        xs=[frac(x) for x in row['x']];n=row['n'];d=row['d']
        require(all(x.denominator==d for x in xs))
        require([sum(x**k for x in xs) for k in range(1,n)]==row['moments'])
        rec=sum(1/x for x in xs)
        require(rec==frac(row['reciprocal']))
        require((factorial(n-1)*rec.numerator)%d**n==0)
        # Direct subset expansion, not Newton recurrence.
        from itertools import combinations
        for k in range(1,n):
            ek=sum((prod(c) for c in combinations(xs,k)),Fraction())
            require(ek==frac(row['elementary_through_n_minus_one'][k]))
    for row in examples['sharp_numerators']:
        xs=[frac(x) for x in row['x']]
        require(sum(xs).denominator==1 and sum(x*x for x in xs).denominator==1)
        require(sum(1/x for x in xs)==frac(row['reciprocal']))
    require(frac(examples['strict_gap']['trace'])==Fraction(436,5))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input',type=Path,default=Path('certificates'))
    ap.add_argument('--out',type=Path,default=Path('independent.json'));args=ap.parse_args()
    start=time.monotonic()
    read=lambda name:json.loads((args.input/name).read_text())
    source=read('scan.json');actual,perprime,tot=direct_primitive(source['bound'])
    expected=sorted(canonical_signature(z) for z in source['states'])
    require(actual==expected,'complete ordered primitive-state list')
    require(tot=={k:source['totals'][k] for k in ('E','M')})
    r=check_raw(read('raw_trace.json'));d=check_denominators(read('denominators.json'))
    relax=check_relaxation(read('trace_relaxation.json'));alg=check_algebraic(read('algebraic_targets.json'))
    check_examples(read('examples.json'))
    result={'success':True,'bound':source['bound'],'primes':len(perprime),'states':len(actual),
            'original_counts':tot,'raw_shells':r,'moment_presentations':d[0],
            'constructed_denominators':d[1],'relaxation_primes':relax,'algebraic_targets':alg,
            'checks':NTEST,'elapsed_seconds':time.monotonic()-start,
            'scope':'Independent implementation; not independent mathematical review or universal ES proof.'}
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
