#!/usr/bin/env python3
"""Fixed-target cofactor completion and original negative-shape returns.
Python standard library only. This does not prove universal ES occupancy.
"""
from __future__ import annotations
from collections import Counter, defaultdict
from functools import lru_cache
from math import gcd, isqrt, prod
from pathlib import Path
import argparse, hashlib, json, time
CHECK=Counter()
HARD={1,121,169,289,361,529}
ALPHA_AUTO={1,2,3}
BETA_AUTO={1,2,3,4,6,9,12,18,36}

def need(v,label):
    CHECK[label]+=1
    if not v:raise ArithmeticError(label)

def primes_to(n):
    b=bytearray(b'\x01')*(n+1)
    if n>=0:b[0]=0
    if n>=1:b[1]=0
    for q in range(2,isqrt(n)+1):
        if b[q]:b[q*q:n+1:q]=b'\0'*((n-q*q)//q+1)
    return [q for q in range(2,n+1) if b[q]]

@lru_cache(maxsize=150000)
def factor(n):
    if n<1:raise ValueError('positive factorization input required')
    out=[];q=2
    while q*q<=n:
        if n%q==0:
            e=0
            while n%q==0:n//=q;e+=1
            out.append((q,e))
        q=3 if q==2 else q+2
    if n>1:out.append((n,1))
    return tuple(out)

@lru_cache(maxsize=50000)
def divisors(n,square=False):
    out=[1]
    for q,e in factor(n):out=[v*q**k for v in out for k in range((2 if square else 1)*e+1)]
    return tuple(sorted(out))

def prime(n):return n>=2 and factor(n)==((n,1),)

def jacobi(a,n):
    if n<=0 or n%2==0:raise ValueError('odd positive Jacobi denominator required')
    a%=n;v=1
    while a:
        while a%2==0:
            a//=2
            if n%8 in (3,5):v=-v
        a,n=n,a
        if a%4==n%4==3:v=-v
        a%=n
    return v if n==1 else 0

def kernel(t):return prod(q**((e+1)//2) for q,e in factor(t))
def canon(v):return json.dumps(v,sort_keys=True,separators=(',',':')).encode()
def digest(v):return hashlib.sha256(canon(v)).hexdigest()
def compact(z):return [z['channel'],z['a'],z['u'],z['R'],z['h'],z['r'],z['s'],z['k']]+z['denominators']

def state(p,a,u,ch):
    R=4*a-p
    need(ch in ('E','M') and p%4==1 and p<4*a and 2*a<p,'original domain')
    need(u>0 and a*a%u==0,'original square divisor')
    need((4*u+1)%R==0 if ch=='E' else (u+a)%R==0,'original channel gate')
    g=gcd(a,u);h=g*g//u;r=u//g;s=a//g
    need(h*r*s==a and h*r*r==u and gcd(r,s)==1,'gcd normalization')
    k=(p*r+s)//R if ch=='E' else (r+s)//R
    need(R*k==(p*r+s if ch=='E' else r+s),'integral channel quotient')
    den=[a,h*s*k,p*h*r*k] if ch=='E' else [a,p*h*s*k,p*h*r*k]
    x,y,z=den
    need(4*x*y*z==p*(x*y+x*z+y*z),'ordered ES identity')
    num=a*a if ch=='E' else p*a*a
    need(num%(R*y-p*a)==0 and num//(R*y-p*a)==u,'ordered divisor inverse')
    st=dict(p=p,channel=ch,a=a,u=u,R=R,h=h,r=r,s=s,k=k,denominators=den)
    if ch=='E':
        v=a*a//u;D=(4*u+1)//R
        st.update(v=v,D=D,alpha=v-R,beta=v-D)
        need(p>2*h and jacobi(h,p)==-1,'actual negative grade')
        need(p*D+1==4*h*r*k and r+k==s*D,'cofactor source identities')
    return st

def marked(z):
    d=dict(z);fu=dict(factor(z['u']))
    d['a_factorization']=[list(x) for x in factor(z['a'])]
    d['exponent_box']=[[q,-e,e] for q,e in factor(z['a'])]
    d['centered_exponents']=[[q,fu.get(q,0)-e] for q,e in factor(z['a'])]
    return d

@lru_cache(None)
def templates(t):
    out=[]
    for ell in range(1,(t-2)//4+1):
        for w in divisors(ell,True):
            num=t-w;k=4*ell+1
            if num<=0 or num%k:continue
            n=num//k;V=ell*ell//w;j=ell+4*n*V;h=4*j-1;W=t+n*h
            if h<=t:continue
            need(W*V==j*j and (W-t)%h==0,'finite-template arithmetic')
            need(h<=t*t-3*t+1,'sharp exceptional grade bound')
            need(((W-t)//h,j*j//W,j-4*n*V)==(n,V,ell),'finite-template inverse')
            need((h==t*t-3*t+1)==(w==n==1 and t==4*ell+2),'exception equality classification')
            g=gcd(ell,V);HH=g*g//V;r0=V//g;lam0=ell//g
            need(HH*r0*lam0==ell and HH*r0*r0==V and gcd(r0,lam0)==1,'exception primitive budget')
            need(HH<=ell,'smaller reconstructed grade')
            out.append(dict(t=t,ell=ell,w=w,n=n,V=V,j=j,h=h,W=W,
                            canonical_available=(j*j)%t==0,
                            primitive=[HH,r0,lam0]))
    return tuple(out)

def predicted(t,j):
    h=4*j-1
    if h<=t:raise ValueError('analytic classification requires h>t')
    out=[]
    if j*j%t==0:out.append((t,'canonical'))
    if j%(4*t)==0:out.append((4*t*j,'companion'))
    for row in templates(t):
        if row['j']==j:out.append((row['W'],'finite'))
    need(len({W for W,_ in out})==len(out),'disjoint coefficient labels')
    return sorted(out)

def inverse_label(t,j,W):
    h=4*j-1
    if W==t:return dict(kind='canonical')
    n=(W-t)//h;V=j*j//W;ell=j-4*n*V
    if ell==0:
        need(n==t and j==4*t*V,'companion inverse')
        return dict(kind='companion',n=n,V=V,ell=0)
    need(ell>0 and ell*ell%V==0,'finite inverse divisor')
    w=ell*ell//V
    need(t==(4*ell+1)*n+w and n>0,'finite inverse target')
    return dict(kind='finite',n=n,V=V,ell=ell,w=w)

def capacity_scan(tmax,jmax):
    counts=Counter();sha=hashlib.sha256()
    lookup=defaultdict(list)
    for t in range(1,tmax+1):
        for row in templates(t):lookup[t,row['j']].append(row['W'])
    for j in range(1,jmax+1):
        h=4*j-1;actual=defaultdict(list)
        for W in divisors(j,True):
            t0=W%h
            if 1<=t0<=tmax:actual[t0].append(W)
        for t in range(1,min(tmax,h-1)+1):
            want=[]
            if j*j%t==0:want.append(t)
            if j%(4*t)==0:want.append(4*t*j)
            want.extend(lookup[t,j]);want.sort()
            have=actual[t]

            if want!=have:raise ArithmeticError(f'capacity mismatch t={t},j={j}: {want} != {have}')
            need(want==have,'complete fixed-target coefficient')
            for W in have:
                label=inverse_label(t,j,W);counts[label['kind']]+=1
                if j*j%t:
                    need(label['kind']=='finite' and h<=t*t-3*t+1,'missing canonical only finite repair')
                    counts['repairs']+=1
            if h>max(t,t*t-3*t+1):
                need(len(have)==int(j*j%t==0)+int(j%(4*t)==0),'eventual exact coefficient')
            sha.update(canon([t,j,have])+b'\n');counts['target_grade_pairs']+=1
    fam=[]
    for ell in range(1,101):
        t=4*ell+2;j=ell*(4*ell+1);h=4*j-1;W=(4*ell+1)**2
        need(h==t*t-3*t+1 and j*j%W==0 and W%h==t,'sharp family identity')
        need(j*j%t!=0,'sharp family canonical unavailable')
        fam.append(dict(ell=ell,t=t,j=j,h=h,W=W,V=ell*ell))
    coexist_j=1224;coexist_t=289
    coexist=[W for W in divisors(coexist_j,True) if W%(4*coexist_j-1)==coexist_t]
    need(coexist==[289,5184] and coexist_j*coexist_j%coexist_t==0,'canonical and finite word coexist')
    need(inverse_label(coexist_t,coexist_j,5184)==dict(kind='finite',n=1,V=289,ell=68,w=16),'coexisting finite label')
    return dict(target_bound=tmax,j_bound=jmax,counts=dict(counts),rows_sha256=sha.hexdigest(),
                templates=[r for t in range(1,tmax+1) for r in templates(t)],sharp_family=fam,
                coexistence=dict(t=289,j=1224,h=4895,words=coexist,coefficient=2))

def character_classes(tmax):
    rows=[]
    for t in range(1,tmax+1):
        M=4*kernel(t);units=[a for a in range(1,M) if gcd(a,M)==1]
        allowed=[a for a in units if a%4==3 and jacobi(t,a)==1]
        need(M-1 in allowed,'minus-one character class')
        is_sq=isqrt(t)**2==t
        need(len(allowed)*(2 if is_sq else 4)==len(units),'exact character-coset cardinality')
        need((allowed==[M-1])==(t in ALPHA_AUTO),'character-only maximality')
        rows.append(dict(t=t,K=kernel(t),modulus=M,square=is_sq,
                         phi=len(units),allowed=allowed,
                         alternative=next((a for a in allowed if a!=M-1),None)))
    return rows

def middle_return(E,side,t,W):
    p,h=E['p'],E['h'];j=(h+1)//4
    need(E['channel']=='E' and E[side]==-4*t,'actual shape input')
    need(h%4==3 and E['s']%2==1 and gcd(h,t)==1 and jacobi(t,h)==1,'forced source grade conditions')
    need(j*j%W==0 and (W-t)%h==0,'actual capacity word')
    U=W if side=='alpha' else j*j//W
    need(j*j%U==0 and (p+4*U)%h==0,'cofactor gate and full budget')
    R=(p+4*U)//h;a=(p+R)//4
    need(0<R<p and R%4==3,'middle source range')
    M=state(p,a,U,'M');g=gcd(j,U)
    need((g*g//U,U//g,R*(j//g)-U//g,j//g)==(M['h'],M['r'],M['s'],M['k']),'cofactor normalization inverse')
    need(4*M['h']*M['r']*M['k']-1==h,'retained source-grade cofactor')
    if W==t:
        need(all((dict(factor(M['h'])).get(q,0)-dict(factor(t)).get(q,0))%2==0
                 for q in set(dict(factor(M['h'])))|set(dict(factor(t)))),'canonical squareclass retained')
    return M

def full_scan(bound,tmax):
    rows=[];tot=Counter()
    for p in primes_to(bound):
        if p%4!=1:continue
        entries=[];crosses=[];ct=Counter();newE=set();oldE=set();autoE=set();sources={}
        for a in range(p//4+1,(p-1)//2+1):
            R=4*a-p;ds=divisors(a,True);ct['original_divisor_vectors']+=len(ds)
            for u in ds:
                for ch,hit in [('E',(4*u+1)%R==0),('M',(u+a)%R==0)]:
                    if not hit:continue
                    st=state(p,a,u,ch);entries.append(compact(st));ct[ch]+=1
                    sources[str(a)]=[list(v) for v in factor(a)]
                    if ch!='E':continue
                    for side in ('alpha','beta'):
                        val=-st[side]
                        if val<=0 or val%4:continue
                        t=val//4;h=st['h'];j=(h+1)//4
                        need(h%4==3 and st['s']%2==1 and gcd(h,t)==1 and jacobi(t,h)==1,'all actual negative-four source conditions')
                        Ws=[W for W in divisors(j,True) if (W-t)%h==0]
                        actualU=[U for U in divisors(j,True) if (p+4*U)%h==0]
                        mapped=Ws if side=='alpha' else sorted(j*j//W for W in Ws)
                        need(mapped==actualU,'complete two-branch coefficient transport')
                        if h>t and t<=tmax:
                            need([W for W,_ in predicted(t,j)]==Ws,'original source finite-capacity classification')
                        guaranteed=False
                        if p%24==1:
                            if side=='beta':
                                need(h%8==(7-4*t)%8,'beta forced two-adic residue')
                                if t%3==0:need(h%3==2,'beta forced ternary residue')
                            guaranteed=t in (ALPHA_AUTO if side=='alpha' else BETA_AUTO)
                            if guaranteed:
                                need(j*j%t==0,'unconditional original line availability');autoE.add((a,u))
                                ct['automatic_'+side]+=1
                        chosen=[]
                        if j*j%t==0:
                            chosen.append((t,'canonical'))
                            c=isqrt(t)
                            if c*c==t:oldE.add((a,u));ct['old_square_branches']+=1
                        if h>t and t<=tmax and j*j%t!=0:
                            chosen.extend((W,lab) for W,lab in predicted(t,j) if lab=='finite')
                        for W,kind in chosen:
                            M=middle_return(st,side,t,W);newE.add((a,u));ct['returned_pairs']+=1
                            crosses.append(dict(source=compact(st),side=side,t=t,j=j,W=W,kind=kind,
                                                automatic=guaranteed,target=compact(M)))
        ct['old_square_source_states']=len(oldE);ct['new_return_source_states']=len(newE)
        ct['new_source_states_beyond_old']=len(newE-oldE);ct['automatic_source_states']=len(autoE)
        rows.append(dict(p=p,hard=p%840 in HARD,states=sorted(entries),occupied_factorizations=sources,
                         transfers=crosses,counts=dict(ct)))
        tot.update(ct)
    return dict(bound=bound,target_template_bound=tmax,prime_domain='all primes p == 1 mod 4',
                columns=['channel','a','u','R','h','r','s','k','x','y','z'],rows=rows,totals=dict(tot))

def alpha_fibre(p,h,t):
    if (p+4*t)%h:return []
    N=(p+4*t)//h;out=[]
    for s in divisors(N):
        z=N//s
        if (s+z)%4:continue
        r=(s+z)//4;a=h*r*s;R=4*a-p;u=h*r*r
        if gcd(r,s)>1 or not(p<4*a and 2*a<p) or (4*u+1)%R:continue
        E=state(p,a,u,'E');need(E['h']==h and E['alpha']==-4*t,'full alpha fibre inverse');out.append(compact(E))
    return sorted(out)

def examples():
    out={}
    specs=[('finite_repair',825241,206321,2240439739,'alpha',6),
           ('beta8_failure',346201,158815,43864703,'beta',8),
           ('beta27_failure',593401,188100,39710000,'beta',27),
           ('beta5_failure',2727841,929071,464321099,'beta',5),
           ('both_square_failure',3152041,791967,50325903,'alpha',841),
           ('infinite_progression_member',7840561,1960155,89353665675,'alpha',4),
           ('old_square_success',5209,1330,18620,'alpha',4),
           ('old_square_failure',3049,806,20956,'alpha',36),
           ('beta9_automatic',4561,1593,43011,'beta',9)]
    for name,p,a,u,side,t in specs:
        need(prime(p) and p%840 in HARD,'fixed hard prime')
        E=state(p,a,u,'E');need(E[side]==-4*t,'fixed shape')
        h=E['h'];j=(h+1)//4;ds=list(divisors(j,True))
        Ws=[W for W in ds if (W-t)%h==0]
        hits=[middle_return(E,side,t,W) for W in Ws]
        out[name]=dict(source=marked(E),side=side,t=t,j=j,canonical_available=j*j%t==0,
                       complete_capacity=[dict(W=W,residue=W%h,target=t%h) for W in ds],
                       W_hits=Ws,targets=[marked(M) for M in hits])
        if name=='finite_repair':
            need(Ws==[25] and j*j%t!=0,'genuine finite repair')
            need(h==t*t-3*t+1 and compact(hits[0])[1:8]==[217170,25,43439,1,5,43434,1],'fixed sharp repair target')
        if name.endswith('failure') or name=='infinite_progression_member':need(Ws==[],'complete fixed cofactor failure')
    # Complete inverse-domain correction; the predecessor executable already rejected it.
    p=5209;h=95;t=4;s=5;r=4;a=h*r*s;R=4*a-p;u=h*r*r
    need(s*((p+4*t)//h//s)==(p+4*t)//h and (p+4*t)//h==55,'spurious fibre divisor relation')
    need(gcd(r,s)==1 and p<4*a and 2*a<p and h*s*s-R==-4*t,'spurious fibre advertised conditions')
    need((4*u+1)%R==1299,'missing gate is substantive')
    out['inverse_domain_correction']=dict(p=p,h=h,t=t,s=s,r=r,a=a,R=R,u=u,
        E_remainder=1299,correct_full_fibre=alpha_fibre(p,h,t),
        affected='predecessor prose only; predecessor inverse_source_fibre checked the E gate')
    # Explicit reduced progression from the all-t existence proof.
    base,step=1447321,2131080;residual,grade=59,43
    need(gcd(base,step)==1 and step==840*grade*residual and base%840==1,'reduced prime progression')
    need(16*4*37**2%59==1 and (base+59)//(4*43)==8415,'progression original root')
    for n in range(20):
        pp=base+step*n;rr=8415+12390*n
        need(pp==4*43*rr-59 and (4*43*rr*rr+1)%59==0,'entire progression identity')
        need(pp%840==1 and pp>2*43*rr,'entire progression range')
    need(base+3*step==7840561,'recorded prime member')
    out['progression']=dict(t=4,R=59,h=43,j=11,r0_mod_R=37,r_base=8415,r_step=12390,
                           p_base=base,p_step=step,gcd=1,prime_member_index=3,
                           prime_member=7840561,
                           no_claim='The progression contains infinitely many primes by Dirichlet; not every member is prime.')
    sharp_progressions=[]
    for z in range(6):
        t=6+420*z;ell=(t-2)//4;h=t*t-3*t+1;R=t*t+t+1;j=ell*(4*ell+1)
        rr0=(t+2*R)//4
        need(gcd(h*R,210)==1 and gcd(h,R)==1,'prime-realized sharp family CRT units')
        need((16*t*rr0*rr0-1)%R==0 and (4*h*rr0*rr0+1)%R==0,'prime-realized sharp original root')
        residue=((R+1)//4)*pow(h,-1,210)%210
        kk=(residue-rr0)*pow(R,-1,210)%210
        rb=rr0+R*kk;pb=4*h*rb-R;step=840*h*R
        need(pb%840==1 and gcd(pb,step)==1,'prime-realized sharp reduced progression')
        need(h==4*j-1 and j*j%t!=0 and j*j%((t-1)**2)==0,'prime-realized sharp missing canonical')
        sharp_progressions.append(dict(t=t,ell=ell,h=h,R=R,j=j,W=(t-1)**2,
            r_base=rb,r_step=210*R,p_base=pb,p_step=step,
            primality_of_base_claim=False,Dirichlet_reduced=True))
    out['prime_realized_sharp_progressions']=sharp_progressions
    return out

def negative_controls(ex):
    controls=[
        ('missing canonical always repaired',bool(ex['infinite_progression_member']['W_hits'])),
        ('beta8 automatically available',bool(ex['beta8_failure']['W_hits'])),
        ('beta27 automatically available',bool(ex['beta27_failure']['W_hits'])),
        ('two negative squares force grade cofactor',bool(ex['both_square_failure']['W_hits'])),
        ('all noncanonical words are finite exceptions',inverse_label(1,1000,4000)['kind']=='finite'),
        ('canonical availability necessary at small grade',ex['finite_repair']['canonical_available']),
        ('old prose fibre domain sufficient',ex['inverse_domain_correction']['E_remainder']==0),
        ('drop sharp additive one',19<=6*6-3*6),
    ]
    # A genuine unbounded companion: t1, j1000, W4000 divides j^2, residue1 mod3999.
    need(1000**2%4000==0 and 4000%3999==1 and 3999>1,'unbounded companion exists')
    labels=[]
    for label,value in controls:
        need(not value,'rejected: '+label);labels.append(label)
    return labels

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--bound',type=int,default=3000);ap.add_argument('--target-bound',type=int,default=120)
    ap.add_argument('--j-bound',type=int,default=5000);ap.add_argument('--out',type=Path,default=Path('certificates'))
    ar=ap.parse_args()
    if ar.bound<97 or ar.target_bound<6 or ar.j_bound<10:ap.error('bounds too small for fixed regressions')
    ar.out.mkdir(parents=True,exist_ok=True);start=time.monotonic()
    cap=capacity_scan(ar.target_bound,ar.j_bound);classes=character_classes(ar.target_bound)
    scan=full_scan(ar.bound,ar.target_bound);ex=examples();bad=negative_controls(ex)
    products={'capacity.json':cap,'character_classes.json':classes,'scan.json':scan,'examples.json':ex}
    for name,obj in products.items():(ar.out/name).write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')
    report=dict(success=True,bound=ar.bound,target_bound=ar.target_bound,j_bound=ar.j_bound,
        primes=len(scan['rows']),totals=scan['totals'],capacity_counts=cap['counts'],
        checks=sum(CHECK.values()),check_counts=dict(CHECK),rejected_false_transformations=bad,
        mathematical_sha256={name:hashlib.sha256((ar.out/name).read_bytes()).hexdigest() for name in products},
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        elapsed_seconds=time.monotonic()-start,universal_ES_proved=False,
        universal_TypeII_occupancy_proved=False,
        scope='Complete fixed-target capacity theorem and original branch returns; bounded replay only.')
    (ar.out/'summary.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print(json.dumps(report,sort_keys=True))
if __name__=='__main__':main()
