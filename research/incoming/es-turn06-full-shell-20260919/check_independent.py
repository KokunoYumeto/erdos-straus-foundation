#!/usr/bin/env python3
"""Separate Turn 6 checker. Imports neither verify.py nor antecedent software.
Uses an Euler least-prime sieve, direct square-divisor trial enumeration in the
small complete atlas, literal pair comparisons, and a separate convex DP.
"""
from __future__ import annotations
import argparse, hashlib, json, sys
from array import array
from collections import Counter
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
count=0

def check(x,message):
    global count
    count+=1
    if not x:raise ArithmeticError(message)

def load(p):return json.loads(p.read_text())

def sieve(n):
    least=array('I',[0])*(n+1);primes=[]
    for i in range(2,n+1):
        if least[i]==0:least[i]=i;primes.append(i)
        for q in primes:
            z=i*q
            if z>n:break
            least[z]=q
            if q==least[i]:break
    phi=array('I',range(n+1))
    for q in primes:
        for z in range(q,n+1,q):phi[z]-=phi[z]//q
    return least,primes,phi

def factors(n,least):
    fs={}
    while n>1:
        q=least[n];fs[q]=fs.get(q,0)+1;n//=q
    return fs

def divisors(n,least):
    fs=factors(n,least);out=[1]
    for q,e in fs.items():
        old=out[:];power=1
        for unused in range(e):
            power*=q;out.extend(d*power for d in old)
    return sorted(out)

def trial_divs(n):
    ds=[]
    for x in range(1,isqrt(n)+1):
        if n%x==0:
            ds.append(x)
            if x*x!=n:ds.append(n//x)
    return sorted(ds)

def stats(p,a,least,literal=False):
    R=4*a-p; ds=trial_divs(a) if literal else divisors(a,least)
    words=sorted(ds+[p*d for d in ds]);hist=Counter(x%R for x in words)
    if literal:
        D=sum((x-y)%R==0 for x in words for y in words)
        T=sum((x+y)%R==0 for x in words for y in words)
    else:
        D=sum(v*v for v in hist.values())
        T=sum(hist.get(-x%R,0) for x in words)
    return len(ds),D,T,hist,words

def balanced(m,s):
    # Construct the actual balanced vector, rather than using the closed formula.
    low=m//s;high_count=m%s
    return (s-high_count)*low*low+high_count*(low+1)*(low+1)

def convex_dp(m,r,f):
    dp=[0]+[10**100]*m
    for w in [2]*r+[4]*f:
        dp=[min(dp[z-x]+w*x*x for x in range(z+1)) for z in range(m+1)]
    return dp[m]

def original_state(s):
    p=s['p'];a=s['a'];R=s['R'];u=s['u'];h=s['h'];r=s['r'];t=s['s'];j=s['quotient']
    check(R==4*a-p and 4*a>p and 2*a<p,'first-half marking')
    check(a==h*r*t and u==h*r*r and gcd(r,t)==1,'state normalization')
    if s['channel']=='E':
        check(R*j==p*r+t and (4*u+1)%R==0,'E gate')
        expected=[a,h*t*j,p*h*r*j]
    else:
        check(R*j==r+t and (4*u+p)%R==0,'M gate')
        expected=[a,p*h*t*j,p*h*r*j]
    check(s['ordered_denominators']==expected,'ordered denominators')
    x,y,z=expected;check(4*x*y*z==p*(x*y+x*z+y*z),'cleared ES identity')

def witness(w):
    s=w['state'];p=s['p'];a=s['a'];R=s['R'];b,c=w['input_pair']
    check((p*a)%b==0 and (p*a)%c==0 and (b+c)%R==0,'original pair')
    original_state(s)
    g=gcd(b,c);x,y=b//g,c//g
    if s['channel']=='E':
        side=w['pair_mark']['p_side'];d=w['pair_mark']['common_divisor']
        pair=[p*d*s['r'],d*s['s']]
        if side:pair.reverse()
        check([b,c]==pair and s['h']%d==0,'E pair inverse')
    else:
        eps=w['pair_mark']['common_p_bit'];d=w['pair_mark']['common_divisor']
        check([b,c]==[p**eps*d*s['r'],p**eps*d*s['s']] and s['h']%d==0,'M pair inverse')

def alternate_atan(x,n=50):
    total=Fraction(0)
    power=x
    for j in range(n):
        total+=power/(2*j+1) if j%2==0 else -power/(2*j+1)
        power*=x*x
    rem=power/(2*n+1)
    return total-rem,total+rem

def independent_spectrum(rec,least):
    p,a,R=rec['p'],rec['a'],rec['R'];t,D,T,hist,words=stats(p,a,least,literal=True)
    logs={};z=1
    for j in range(46):logs[z]=j;z=z*5%47
    check(len(logs)==46 and z==1,'independent primitive generator')
    counts=[0]*23;corr=[0]*23
    for w in words:counts[logs[w%R]%23]+=1
    for x in words:
        for y in words:corr[(logs[x%R]-logs[y%R])%23]+=1
    check(counts==rec['coefficient_vector'] and corr==rec['norm_polynomial_cyclic_coefficients'],
          'independent original norm polynomial')
    # pi=4*(arctan(1/2)+arctan(1/3)), with a different convergent series.
    x,y=Fraction(1,2),Fraction(1,3)
    check((x+y)/(1-x*y)==1,'alternative rational tangent identity')
    a0,a1=alternate_atan(x);b0,b1=alternate_atan(y)
    lowpi,highpi=4*(a0+b0),4*(a1+b1)
    center=(lowpi+highpi)/2;pierror=(highpi-lowpi)/2
    intervals=[]
    for j,floor in [(1,1009),(2,24)]:
        total=Fraction(corr[0]);radius=Fraction(0)
        for k in range(1,12):
            h=(j*k)%23;h=min(h,23-h);arg=2*center*h/23
            term=Fraction(1);value=term
            for n in range(1,21):
                term*= -arg*arg/Fraction((2*n-1)*(2*n));value+=term
            rem=abs(term)*arg*arg/Fraction(41*42)
            total+=2*corr[k]*value
            radius+=2*corr[k]*(rem+2*pierror*h/23)
        check(floor<total-radius and total+radius<floor+1,'independent exact spectral enclosure')
        intervals.append([floor,floor+1])
    check(D==132 and T==60 and rec['three_even_modes_rounded_target_lower']==56
          and rec['five_even_modes_rounded_target_lower']==60,'actual five-mode sharp certificate')
    witness(rec['witness'])
    check([d['d'] for d in rec['original_words']]==words,'full spectral word source')
    for d in rec['original_words']:
        check(pow(5,d['full_log_mod46'],47)==d['residue'] and d['even_log_mod23']==d['full_log_mod46']%23,
              'full logarithmic inverse mark')
    expected={(x,y) for x in words for y in words if (x+y)%R==0}
    check(expected=={tuple(w['input_pair']) for w in rec['original_target_pairs']},'complete spectral target fibre')
    for w in rec['original_target_pairs']:witness(w)
    for st in rec['distinct_labelled_states']:original_state(st)
    return {'p':p,'R':R,'intervals':intervals,'method':'pi=4*(atan(1/2)+atan(1/3)); separate rational Taylor series; literal original word differences'}

def independent_power_constants(records):
    out=[]
    for row in records:
        m=row['m'];prod=Fraction(1);local=[]
        for q in range(2,2**m):
            if any(q%d==0 for d in range(2,q)):continue
            vals=[Fraction((e+1)**m,q**e) for e in range(4*m)]
            peak=max(vals);where=vals.index(peak)
            check(where<2*m and Fraction(2*m+1,2*m)**m<2,
                  'independent eventual ratio and finite maximum')
            prod*=peak
            local.append({'q':q,'maximizing_exponent':where,
                          'maximum_power':[peak.numerator,peak.denominator]})
        c=1
        while c**m*prod.denominator<prod.numerator:c+=1
        check([prod.numerator,prod.denominator]==row['K_m'] and c==row['C_m']
              and local==row['local_maxima'],'independent finite divisor constant')
        out.append([m,c])
    check(Fraction(7,16)-Fraction(91,300)>Fraction(1,8),
          'independent general negative margin')
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input',type=Path,default=Path('certificates'))
    ap.add_argument('--out',type=Path,default=Path('independent.json'));args=ap.parse_args()
    powers=independent_power_constants(load(args.input/'constants.json')['divisor_power_constants'])
    mainrows=load(args.input/'full_shells.json');pc=load(args.input/'principal_census.json')
    n=max(pc['bound'],1915201,mainrows['bound']);least,primes,phi=sieve(n)
    # Full small atlas, directly comparing original pairs and square divisors.
    outrows=[];totals=Counter()
    for p in primes:
        if p>mainrows['bound']:break
        if p%4!=1:continue
        totals['primes']+=1
        for a in range(p//4+1,(p-1)//2+1):
            R=4*a-p;t,D,T,hist,words=stats(p,a,least,literal=True)
            ud=trial_divs(a*a);E=sum((4*u+1)%R==0 for u in ud);M=sum((4*u+p)%R==0 for u in ud)
            row=[p,a,R,t,D,T,E,M,8*t*t-phi[R]*D,int(phi[R])];outrows.append(row)
            check(T%4==0 and (T>0)==(E+M>0),'direct atlas equivalence')
            totals['shells']+=1;totals['original_divisor_vectors']+=len(ud)
            totals['E_states']+=E;totals['M_states']+=M;totals['target_pairs']+=T;totals['occupied_shells']+=bool(T)
    check(outrows==mainrows['rows'] and dict(totals)==mainrows['totals'],'complete small row equality')
    # Independent divisor-sieve proof of the finite phi cutoff.
    top=pc['max_tau_range'][1];dt=array('H',[0])*(top+1)
    for d in range(1,top+1):
        for z in range(d,top+1,d):dt[z]+=1
    mx=max(dt)
    check(mx==pc['max_tau'] and [i for i in range(1,top+1) if dt[i]==mx]==pc['max_tau_attainers'], 'independent full divisor cap')
    check([R for R in range(3,pc['bound'],4) if phi[R]<4*mx]==pc['candidate_residuals'],'independent complete residual cutoff')
    # Complete hard universe: every positive certificate, then EVERY shell at each miss.
    hard={q for q in primes if q<=pc['bound'] and q%840 in {1,121,169,289,361,529}}
    seen=set();certificate_ps=set()
    for row in pc['principal_successes']:
        p=row['p'];a=row['a'];R=row['R']
        check(p in hard and p not in seen,'hard prime certificate identity');seen.add(p)
        check(R==4*a-p and 0<R<p,'certificate source')
        t,D,T,_,_=stats(p,a,least)
        num=8*t*t-phi[R]*D
        check([t,D,int(phi[R]),num]==[row['tau'],row['D'],row['phi'],row['L_numerator']]
              and num>0 and num<=phi[R]*T,'positive collision certificate')
        witness(row['witness']);certificate_ps.add(p)
    misses=sorted(hard-seen)
    check(misses==pc['principal_misses'],'universe minus positive certificates')
    failed=[]
    first=load(args.input/'failure_87481.json')
    for p in misses:
        rows=[];occupied=[];best=None;max_integer=None
        for a in range(p//4+1,(p-1)//2+1):
            R=4*a-p;t,D,T,hist,words=stats(p,a,least)
            num=8*t*t-phi[R]*D
            check(num<=0,'full first-half principal failure')
            val=Fraction(num,int(phi[R]))
            if best is None or val>best:best=val
            lint=balanced(2*t,int(phi[R])//2)-D
            max_integer=lint if max_integer is None else max(max_integer,lint)
            if p==87481:check(lint<=0,'full integer principal failure')
            rows.append([a,R,t,D,num,int(phi[R]),lint])
            if T:occupied.append([a,R,T])
        digest=hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()
        if p==87481:
            check(rows==first['rows'] and digest==first['all_rows_sha256'] and occupied==first['occupied_shells'],
                  'least displayed failure full independent replay')
        failed.append({'p':p,'shells':len(rows),'max_L':[best.numerator,best.denominator],
                       'occupied_shell_count':len(occupied),'all_rows_sha256':digest,'max_global_integer_lower':max_integer})
    check(seen|set(misses)==hard,'complete hard universe covered by positive/failure certificates')
    # All detailed coset and pair examples.
    example_data=load(args.input/'examples.json')
    for rec in example_data['repairs']+[example_data['no_nonterminal_subgroup']]:
        p,a,R=rec['p'],rec['a'],rec['R'];t,D,T,hist,words=stats(p,a,least)
        check(least[p]==p,'prime example')
        K=set(rec['subgroup']);units={x for x in range(1,R) if gcd(x,R)==1}
        check(1 in K and R-1 in K and all(x*y%R in K for x in K for y in K),'original subgroup')
        cls=[];remain=set(units)
        while remain:
            rep=min(remain);cl={rep*x%R for x in K};remain-=cl;cls.append((rep,cl))
        masses=[(rep,sum(hist[x] for x in cl)) for rep,cl in cls]
        L=sum(balanced(z,len(K)//2) for _,z in masses)-D
        check(D==rec['energy'] and T==rec['target_count'] and L==rec['integer_lower'] and L<=T,'exact coset count')
        check([list(x) for x in masses]==rec['coset_counts'],'all coset counts')
        if rec['witness']:witness(rec['witness'])
        if 'original_target_pairs' in rec:
            target={(x,y) for x in words for y in words if (x+y)%R==0}
            check(target=={tuple(w['input_pair']) for w in rec['original_target_pairs']},'complete target pair list')
            for w in rec['original_target_pairs']:witness(w)
            flat=[tuple(z) for O in rec['fourfold_orbits'] for z in O]
            check(len(flat)==len(set(flat)) and set(flat)==target,'complete disjoint four-orbit list')
    # Complement-aware minimum is checked by independent dynamic programming.
    for rec in load(args.input/'complement.json'):
        p,a,R=rec['p'],rec['a'],rec['R'];t,D,T,hist,words=stats(p,a,least)
        K=set(rec['K']);lookup={};remain={x for x in range(1,R) if gcd(x,R)==1}
        while remain:
            rep=min(remain);cl={rep*x%R for x in K}
            for x in cl:lookup[x]=rep
            remain-=cl
        P=p*a%R;seen=set();floor=0
        for rep in sorted(set(lookup.values())):
            if rep in seen:continue
            cl=[x for x in lookup if lookup[x]==rep];m=sum(hist[x] for x in cl)
            other=lookup[P*pow(rep,-1,R)%R]
            if other!=rep:
                seen|={rep,other};floor+=2*balanced(m,len(K)//2)
            else:
                seen.add(rep);f=sum(x*x%R==P for x in cl)//2;r=(len(K)//2-f)//2
                check(m%2==0,'even original complement fibre')
                floor+=convex_dp(m//2,r,f)
        check(floor-D==rec['complement_integer_lower'] and floor-D<=T,'independent convex minimum')
    empty=example_data['empty_shell'];_,D,T,hist,_=stats(empty['p'],empty['a'],least)
    check(T==0 and D==empty['D'],'empty shell negative control')
    spectral=independent_spectrum(load(args.input/'spectral.json'),least)
    result={'divisor_power_constants_check':powers,'spectral_check':spectral,'success':True,'explicit_checks':count,'small_atlas':dict(totals),
            'hard_bound':pc['bound'],'hard_prime_count':len(hard),'positive_certificates':len(certificate_ps),
            'full_failure_replays':failed,'small_rows_sha256':hashlib.sha256(json.dumps(outrows,separators=(',',':')).encode()).hexdigest(),
            'scope':'No main/antecedent imports; full small atlas, all hard positive certificates, all first-half shells of every listed principal miss, examples, independent convex DP, a separate rational spectral interval, and finite divisor-power constants. Not an independent mathematical review.'}
    args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print(json.dumps(result,sort_keys=True))
if __name__=='__main__':main()
