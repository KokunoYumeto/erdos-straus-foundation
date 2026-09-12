#!/usr/bin/env python3
"""Two-sided exact ES certificates; Python >=3.10, standard library only.
Full-scope negative certificates are never inferred from restricted searches.
No assertion is removed by optimized execution. See workbench.tex for proofs.
"""
from __future__ import annotations
import argparse, hashlib, heapq, itertools, json, sys
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as Q
from math import gcd, isqrt, prod
from pathlib import Path

CHECKS=Counter()
def check(ok, name, kind='exact'):
    CHECKS[kind]+=1
    if not ok: raise ArithmeticError(name)
def encode(x):
    if isinstance(x,Q): return {'numerator':x.numerator,'denominator':x.denominator}
    if isinstance(x,dict): return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [encode(v) for v in x]
    return x
def dump(path,obj):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(encode(obj),sort_keys=True,indent=2)+'\n',encoding='utf8')
def prime(n):
    if n<2:return False
    if n%2==0:return n==2
    return all(n%d for d in range(3,isqrt(n)+1,2))
def factor(n):
    if n<1:raise ValueError('factor requires a positive integer')
    ans={};d=2
    while d*d<=n:
        while n%d==0:ans[d]=ans.get(d,0)+1;n//=d
        d=3 if d==2 else d+2
    if n>1:ans[n]=ans.get(n,0)+1
    return ans
def divisors(f):
    out=[(1,())]
    for q,e in sorted(f.items()):
        out=[(u*q**j,es+(j,)) for u,es in out for j in range(e+1)]
    return sorted(out)
def valuation(n,q):
    if n==0:return None
    n=abs(n);e=0
    while n%q==0:e+=1;n//=q
    return e
def F(p,t):
    x,y,z=t;return 4*x*y*z-p*(x*y+x*z+y*z)
def shell_range(p):
    if p%4!=1 or not prime(p):raise ValueError('full atlas requires a prime p=1 mod 4')
    return range(p//4+1,3*p//4+1)

@dataclass(frozen=True)
class Candidate:
    p:int;a:int;u:int;channel:str
    def __post_init__(self):
        if self.channel not in ('E','M') or self.p%4!=1 or not (self.p//4<self.a<=3*self.p//4) or self.u<1 or self.a*self.a%self.u:
            raise ValueError('outside the full canonical candidate domain')
    @property
    def R(self):return 4*self.a-self.p
    @property
    def obstruction(self):return 4*self.u+1 if self.channel=='E' else self.u+self.a
    @property
    def D(self):return self.R//gcd(self.R,self.obstruction)
    @property
    def gap(self):return (self.D-1)//2
    def coordinates(self):
        g=gcd(self.a,self.u);r=self.u//g;s=self.a//g
        h=Q(g*g,self.u)
        return h,r,s,Q(self.p*r+s,self.R) if self.channel=='E' else Q(r+s,self.R)
    def rational(self):
        p,a,u,R=self.p,self.a,self.u,self.R
        if self.channel=='E':return Q(a),Q(p*a+a*a//u,R),Q(p*a+p*p*u,R)
        return Q(a),Q(p*(a+a*a//u),R),Q(p*(a+u),R)
    def integral(self):
        vals=tuple(self.D*v for v in self.rational())
        if any(v.denominator!=1 for v in vals):raise ArithmeticError('inexact clearing factor')
        return tuple(v.numerator for v in vals)
    def record(self):
        h,r,s,k=self.coordinates();t=self.rational();D=self.D
        out={'p':self.p,'a':self.a,'R':self.R,'u':self.u,'channel':self.channel,
             'h':h,'r':r,'s':s,'kappa' if self.channel=='E' else 'lambda':k,
             'rational_ordered_denominators':t,'D':D,'gap':self.gap,
             'scaled_parameter':self.p*D,'scaled_ordered_denominators':self.integral(),
             'repeated_root_stratum':self.channel=='M' and self.u==self.a}
        if D>1:
            ell=min(factor(D));out['least_obstruction']={'prime':ell,'v_R':valuation(self.R,ell),
                  'v_residual':valuation(self.obstruction,ell)}
        return out

def candidates(p, shells=None):
    for a in (shell_range(p) if shells is None else shells):
        fs={q:2*e for q,e in factor(a).items()}
        for u,exps in divisors(fs):
            for channel in ('E','M'):yield Candidate(p,a,u,channel)

def inverse_candidate(p,R,channel,t):
    a,Y,Z=map(Q,t)
    if a.denominator!=1:raise ValueError('distinguished first denominator not integral')
    u=Q(a*a,R*Y-p*a)*(p if channel=='M' else 1)
    if u.denominator!=1:raise ValueError('not a divisor-state image')
    c=Candidate(p,int(a),int(u),channel)
    if c.R!=R or c.rational()!=(a,Y,Z):raise ValueError('inverse failed')
    return c

def check_candidate(c):
    p,a,u,R=c.p,c.a,c.u,c.R;t=c.rational();D=c.D;it=c.integral()
    check(a*a%u==0 and R>0 and gcd(a,R)==gcd(p,R)==1,'candidate units')
    h,r,s,k=c.coordinates()
    check(h.denominator==1 and h*r*s==a and h*r*r==u and gcd(r,s)==1,'primitive inverse')
    check(all(v>0 for v in t) and F(p,t)==0,'positive rational ES')
    check(t[1].denominator==t[2].denominator==D and D%2==1,'exact common denominator')
    check(gcd(p,D)==1 and 1<=D<=2*p-3 and R%D==0,'bounded scale')
    check(inverse_candidate(p,R,c.channel,t)==c,'candidate singleton inverse')
    check(F(p*D,it)==0 and F(p,it)==2*p*c.gap*(it[0]*it[1]+it[0]*it[2]+it[1]*it[2]),'scaled defect')
    check(len(set(t))<3 if c.channel=='M' and u==a else len(set(t))==3,'only collision stratum')
    if c.channel=='M':
        comp=Candidate(p,a,a*a//u,'M')
        check(comp.D==D and comp.rational()==(t[0],t[2],t[1]),'middle complement full return')
    if D>1:
        ell=min(factor(D));check(valuation(R,ell)>valuation(c.obstruction,ell),'prime obstruction')
    return c.record()

# A rejection certificate is a complete list, not a claimed empty set.
def rejection_record(p, shells=None):
    rows=[]
    for c in candidates(p,shells):
        if c.D==1:raise ValueError('requested rejection list contains an actual hit')
        rows.append({'a':c.a,'u':c.u,'channel':c.channel,'D':c.D,
                     'obstructing_prime':min(factor(c.D)),'inverse_gap':Q(1,c.gap)})
    return {'p':p,'scope':'full' if shells is None else 'restricted',
            'shells':list(shell_range(p) if shells is None else shells),'rows':rows}

def verify_rejection(obj, require_full=True):
    p=obj['p'];ar=list(shell_range(p))
    if require_full and (obj['scope']!='full' or obj['shells']!=ar):
        raise ValueError('not a full-shell counterexample certificate')
    selected=ar if require_full else obj['shells']
    expected=list(candidates(p,selected));rows=obj['rows']
    if len(rows)!=len(expected):raise ValueError('missing or extra divisor-box entry')
    for c,r in zip(expected,rows):
        if (c.a,c.u,c.channel)!=(r['a'],r['u'],r['channel']):raise ValueError('wrong leaf order/identity')
        if c.D==1 or c.D!=r['D']:raise ValueError('hit or incorrect denominator')
        ell=r['obstructing_prime']
        if not prime(ell) or c.R%ell or valuation(c.R,ell)<=valuation(c.obstruction,ell):
            raise ValueError('invalid obstruction prime')
        v=r['inverse_gap'];v=Q(v['numerator'],v['denominator']) if isinstance(v,dict) else Q(v)
        if c.gap*v!=1:raise ValueError('inverse-gap identity failed')
    return True

def integral_energy_floor(N,M):
    if M==0:return None
    q,r=divmod(N,M)
    return M*q*q+r*(2*q+1)

def symmetric_energy_floor(N,R,targets):
    """Exact minimum over nonnegative integer histograms with signed-box symmetry.
    Identity coefficient is odd; other self-inverse coefficients are even.
    This optimizes a relaxation, not the actual exponent image.
    """
    allowed={v for v in range(R) if gcd(v,R)==1}-targets
    if 1 not in allowed:return None
    singles=sorted(v for v in allowed-{1} if v*v%R==1)
    pairs=sorted((v,pow(v,-1,R)) for v in allowed if v<pow(v,-1,R))
    # one budget unit places two occurrences. Each sequence of marginal costs is increasing.
    heap=[(8,8,'identity')]+[(4,8,'s'+str(v)) for v in singles]+[(2,4,'p'+str(v)) for v,_ in pairs]
    heapq.heapify(heap);total=1
    for _ in range((N-1)//2):
        cost,step,label=heapq.heappop(heap);total+=cost
        heapq.heappush(heap,(cost+step,step,label))
    return total

def energy(p,a,with_fibres=False):
    R=4*a-p;fac=factor(a);qs=sorted(fac);mu=Counter();fib={}
    for beta in itertools.product(*(range(-fac[q],fac[q]+1) for q in qs)):
        res=prod(pow(q,j,R) for q,j in zip(qs,beta))%R
        mu[res]+=1;fib.setdefault(res,[]).append(beta)
    N=sum(mu.values());phi=sum(gcd(j,R)==1 for j in range(R))
    targets={(-1)%R,(-p)%R,(-pow(p,-1,R))%R};E=sum(n*n for n in mu.values())
    basic=(phi-len(targets))*E<N*N
    balanced=integral_energy_floor(N,phi-len(targets))
    symmetric=symmetric_energy_floor(N,R,targets)
    guaranteed=(symmetric is None or E<symmetric)
    hit=None
    for v in sorted(targets):
        if v in fib:
            beta=fib[v][0]
            if v==(-1)%R:channel='M'
            else:
                channel='E'
                if v!=(-pow(p,-1,R))%R:beta=tuple(-z for z in beta)
            u=prod(q**(fac[q]+e) for q,e in zip(qs,beta));hit=Candidate(p,a,u,channel)
            check(hit.D==1,'energy inverse extracts actual hit','energy')
            break
    check(not guaranteed or hit is not None,'energy forcing','energy')
    # Independent multiplicity-preserving autocorrelation, not support-size heuristic.
    E2=0
    for de in itertools.product(*(range(-2*fac[q],2*fac[q]+1) for q in qs)):
        if prod(pow(q,j,R) for q,j in zip(qs,de))%R==1:
            E2+=prod(2*fac[q]+1-abs(j) for q,j in zip(qs,de))
    check(E==E2,'weighted collision identity','energy')
    result={'p':p,'a':a,'R':R,'factorization':fac,'box_size':N,'group_order':phi,
       'targets':sorted(targets),'energy':E,'lhs':(phi-len(targets))*E,'rhs':N*N,
       'ordinary_cauchy_forcing':basic,'integer_balanced_floor':balanced,'signed_symmetric_floor':symmetric,
       'strict_forcing':guaranteed,'histogram':mu,'hit':None if hit is None else hit.record()}
    if with_fibres:result['fibres']=fib
    return result

def qr(R):return {a*a%R for a in range(1,R) if gcd(a,R)==1}
def anchor(R,A,H):
    if gcd(A,R)!=1 or (-1)%R in H:raise ValueError('invalid subgroup anchor')
    U={x for x in range(R) if gcd(x,R)==1}
    if len(H)*2!=len(U) or 1 not in H or {a*b%R for a in H for b in H}!=H:
        raise ValueError('not the stated index-two subgroup')
    if any(q%R not in H for q in factor(A)):raise ValueError('anchor uses outside prime')
    best={}
    for n,_ in divisors(factor(A)):
        for d,_ in divisors(factor(A//n)):
            if gcd(n,d)>1:continue
            v=n*pow(d,-1,R)%R;cost=Q(d,n)
            if v not in best or (cost,n,d)<best[v]:best[v]=(cost,n,d)
    if set(best)!=H:raise ValueError('actual signed box does not saturate subgroup')
    return best,max(v[0] for v in best.values())

def greatest_outside(b,R,H):
    outside=[q for q in factor(b) if q%R not in H]
    if b%R not in H:return b,None
    if outside:
        q=min(outside);return b//q,q
    return 0,None

def angular_witness(p,R,A,H):
    a=(p+R)//4
    if (p+R)%4 or a%A or gcd(a,R)!=1:raise ValueError('not an anchor shell')
    costs,B=anchor(R,A,H);b=a//A;t,q=greatest_outside(b,R,H)
    if not t:return None
    v=(-pow(t,-1,R))%R;cost,n,d=costs[v]
    if Q(d,t*n)>=Q(1,8):return None
    g=gcd(d,t*n);r=d//g;s=t*n//g;h=a*g*g//(d*t*n);u=a*d//(t*n)
    c=Candidate(p,a,u,'M');check(c.D==1 and c.coordinates()[:3]==(Q(h),r,s),'anchor full inverse','anchor')
    check(Q(r,s)<Q(1,8),'anchor chamber sufficient inequality','anchor')
    return {'state':c.record(),'anchor':A,'cofactor':b,'outside_divisor':t,
       'least_outside_prime':q,'n':n,'d':d,'g':g,'residue_cost':cost,'max_height':B,
       'old_uniform_sufficient':b>64*B*B,'new_uniform_sufficient':t>8*B,
       'inverse_t':Q(d*s,n*r)}

# Leech and all 24 typed factor routes use the pinned preceding coordinate implementation.
LINEAGE=Path(__file__).parent/'lineage'
sys.path.insert(0,str(LINEAGE))
import branch_verify as bv
BLOCKS=({0,1,3,4,7,8,16,23},{10,12,15,18,19,20,21,22},{2,5,6,9,11,13,14,17})
def oct_table():
    table=[[None]*8 for _ in range(8)]
    for i in range(8):table[0][i]=table[i][0]=(i,1)
    for i in range(1,8):table[i][i]=(0,-1)
    for t in range(7):
        a,b,c=[1+(t+k)%7 for k in (0,1,3)]
        for i,j,k in ((a,b,c),(b,c,a),(c,a,b)):
            table[i][j]=(k,1);table[j][i]=(k,-1)
    return table
OCT_TABLE=oct_table()
def oct_mul(x,y):
    out=[Q(0) for _ in range(8)]
    for i,a in enumerate(x):
        for j,b in enumerate(y):
            k,sign=OCT_TABLE[i][j];out[k]+=sign*a*b
    return tuple(out)
def wilson_member(zs):
    # Work in the source's doubled octonion numerator convention.
    vv=[tuple(2*t for t in z) for z in zs]
    if any(t.denominator!=1 for v in vv for t in v):return False
    vv=[tuple(int(t) for t in v) for v in vv]
    def in_L(v):
        parity=v[0]%2
        return all(t%2==parity for t in v) and sum(v)%4==2*parity
    def in_right(v,c):
        pre=oct_mul(v,c)
        return all(t.denominator==1 and t.numerator%4==0 for t in pre) and in_L(tuple(int(t)//4 for t in pre))
    if not all(in_L(v) for v in vv):return False
    s=(-1,1,1,1,1,1,1,1);sb=(-1,-1,-1,-1,-1,-1,-1,-1)
    for i,j in ((0,1),(0,2),(1,2)):
        if not in_right(tuple(a+b for a,b in zip(vv[i],vv[j])),s):return False
    return in_right(tuple(sum(v[i] for v in vv) for i in range(8)),sb)

def lattice_setup():
    residues={i*i%23 for i in range(1,23)}
    bs=bv.binary_basis([(1<<23)|sum(1<<((a+q)%23) for q in residues) for a in range(23)])
    code=set(bv.words(bs));C=bv.perm(bv.C)
    b0=bv.BASIS_TRACE;B=(b0,bv.move(b0,C),bv.move(bv.move(b0,C),C))
    check(len(code)==4096,'Golay code count','lattice')
    for i,b in enumerate(B):
        check(bv.member(b,code),'section basis membership','lattice')
        check(tuple(Q(sum(b[k] for k in bb),4) for bb in BLOCKS)==tuple(int(i==j) for j in range(3)),
              'integral trace right inverse','lattice')
    alignment=json.loads((LINEAGE/'aligned_isometry.json').read_text())
    check(alignment['denominator']==8,'pinned alignment denominator','lattice')
    mat=alignment['golay_to_wilson_numerator_matrix']
    for i in range(24):
        for j in range(24):
            check(Q(mat[i][j],8)==bv.WILSON_EPS[i]*int(j==bv.WILSON_PI[i]),
                  'full signed coordinate dictionary','lattice')
    for i,b in enumerate(B):
        octs=bv.wilson(b);zs=[octs[8*j:8*j+8] for j in range(3)]
        check(2*oct_mul(oct_mul(zs[0],zs[1]),zs[2])[0]==(-5,1,-1)[i],
              'pinned cubic convention on section basis','lattice')
    return code,B

def lifted_routes(c,code,B):
    rec=check_candidate(c);t=c.rational();D=c.D;integers=c.integral();p=c.p
    vec=tuple(sum(integers[j]*B[j][i] for j in range(3)) for i in range(24))
    check(bv.member(vec,code),'scaled trace Leech membership','lattice')
    tr=tuple(Q(sum(vec[i] for i in bb),4) for bb in BLOCKS)
    check(tr==integers and tuple(z/D for z in tr)==t,'scaled trace rational return','lattice')
    check(4*prod(tr)/(p*(tr[0]*tr[1]+tr[0]*tr[2]+tr[1]*tr[2]))==D,'clearing denominator recovered from integral trace and p','lattice')
    octs=bv.wilson(vec);check(bv.unwilson(octs)==vec,'signed octonion return','lattice')
    # Include all octad measurements, not only the non-injective three traces.
    octads=[w for w in code if w.bit_count()==8];meas={w:Q(sum(vec[i] for i in range(24) if w>>i&1),4) for w in octads}
    S=sum(meas.values());Si=[sum(v for w,v in meas.items() if w>>i&1) for i in range(24)]
    check(tuple((23*v-7*S)/1012 for v in Si)==vec,'symmetry-complete inverse','lattice')
    delta=Q(11*S-23*Si[0],506)
    check(delta.denominator==1 and delta.numerator%4==0,'integral trace syndrome','lattice')
    # Norm/S_J correction, with the cubic retained as a specified form.
    zs=[octs[8*i:8*i+8] for i in range(3)];ns=[sum(v*v for v in z) for z in zs]
    check(wilson_member(zs),'full joint Wilson membership on returned state','lattice')
    nu=2*oct_mul(oct_mul(zs[0],zs[1]),zs[2])[0]
    trS=sum(integers[i]*integers[j] for i,j in ((0,1),(0,2),(1,2)))
    normJ=prod(integers)-sum(integers[i]*ns[i] for i in range(3))+nu
    SJ=trS-sum(ns)
    correction=sum((p-4*integers[i])*ns[i] for i in range(3))+4*nu
    check(4*normJ-p*SJ==F(p,integers)+correction,'complete numeric Albert correction','lattice')
    raw=tuple([Q(-p)]+[4*v for v in t]);scaled=tuple(D*v for v in raw)
    check(bv.elementary(raw,3)==0 and scaled[0]==-p*D,'raw and scaled Cayley return','routes')
    output={'candidate':rec,'leech_numerator':vec,'leech_norm_squared':Q(sum(x*x for x in vec),8),
            'ordered_octonions':zs,'octonion_norms':ns,'octad_syndrome':delta,
            'cubic_nu':nu,'Jordan_norm':normJ,'Jordan_second_coefficient':SJ,
            'full_Albert_defect':4*normJ-p*SJ,'off_diagonal_correction':correction,
            'raw_cayley':raw,'integer_scaled_cayley':scaled}
    if len(set(raw))<4:
        check(c.channel=='M' and c.u==c.a,'exact repeated-root stratum','routes')
        output['route_domain']='collision stratum: all labelled factors retained; resultant-one normalization only at simple selected roots'
    rv=bv.resolvent(raw);rv_scaled=bv.resolvent(scaled)
    check(rv_scaled==tuple(D*D*z for z in rv),'resolvent degree-two scale','routes')
    flags=[]
    for f in itertools.permutations(range(4)):
        i,j,k,l=f;roots=tuple(-4*raw[i]/raw[q] for q in (j,k,l))
        root_scaled=tuple(-4*scaled[i]/scaled[q] for q in (j,k,l))
        check(roots==root_scaled and sum(roots)==4,'all face roots unchanged by denominator clearing','routes')
        r,s,z=roots;der=-(r-s)*(r-z)/4;eta=s-z
        rawL=[Q(1),-r];rawQ=[-v/4 for v in bv.poly_mul([1,-s],[1,-z])]
        cub=bv.cubic(roots,Q(-1,4))
        check(bv.poly_mul(rawL,rawQ)==cub and bv.resultant(rawL,rawQ)==der,'all labelled factors including zero-resultant strata','routes')
        if der:
            L=[v/der for v in rawL];QQ=[der*v for v in rawQ]
            fsource=(1/der,-r-der,5*der*der+3*r*der+Q(1,2)*der**3)
            check(bv.resultant(L,QQ)==1 and bv.poly_mul(L,QQ)==cub,'normalized factor scale','routes')
            check(bv.fable(*fsource)==(cub[3],2*cub[2],Q(-1,2)),'Fable coordinate return','routes')
        else:L=QQ=fsource=None
        back=[None]*4;back[i]=raw[i]
        for q,v in zip((j,k,l),roots):back[q]=-4*raw[i]/v
        check(tuple(back)==raw and inverse_candidate(p,c.R,c.channel,tuple(back[q]/4 for q in (1,2,3)))==c,
              'entire affine/channel return','routes')
        flags.append({'flag':f,'roots':roots,'derivative':der,'companion_difference':eta,
                      'face_scale':raw[i],'cleared_face_scale':scaled[i],
                      'unnormalized_linear':rawL,'unnormalized_quadratic':rawQ,
                      'normalization_available':bool(der),
                      'normalized_linear':L,'normalized_quadratic':QQ,'fable_source':fsource})
    check(len(flags)==24,'all orientation flags','routes')
    output.setdefault('route_domain','distinct-root')
    output.update({'resolvent':rv,'scaled_resolvent':rv_scaled,'flags':flags})
    return output

# Formal polynomial checks supplement the coordinate-level written proof.
def formal():
    P=bv.Poly;v=bv.variables
    p,a,R,u=v(4)
    # Cross-multiplied rational ES identities with u,R retained as nonzero marks.
    NY=p*a*u+a*a;NZ=p*a+p*p*u
    numerator=4*a*NY*NZ-p*(NY*NZ+a*NZ*R*u+a*NY*R)
    check(numerator==p*a*(a+p*u)**2*(4*a-p-R),'exterior rational identity numerator','polynomial')
    NY=p*(a*u+a*a);NZ=p*(a+u)
    numerator=4*a*NY*NZ-p*(NY*NZ+a*NZ*R*u+a*NY*R)
    check(numerator==p*p*a*(a+u)**2*(4*a-p-R),'middle rational identity numerator','polynomial')
    p,x,y,z,D=v(5)
    check(F(p,(D*x,D*y,D*z))-D**3*F(p,(x,y,z))==p*D*D*(D-1)*(x*y+x*z+y*z),
          'target defect under scaling','polynomial')
    x,y,z,n,p=v(5)
    check(F(p,(x+n,y,z))-F(p,(x,y,z))==n*(4*y*z-p*(y+z)),'trace translation','polynomial')
    # Correct exact CRT exponent for the uploaded local phase pair.
    for ell in (2,3,5,7,11,13):
        seen=set()
        for aa in range(ell):
            for bb in range(ell-1):
                e=((ell-1)*aa-ell*bb)%(ell*(ell-1));seen.add(e)
                check((-e)%ell==aa and (-e)%(ell-1)==bb,'phase-pair inverse signs','phase')
        check(len(seen)==ell*(ell-1),'faithful joint phase','phase')

def shell_graph(p,a):
    nodes=list(candidates(p,[a]));index={(c.channel,c.u):i for i,c in enumerate(nodes)}
    adj=[set() for _ in nodes];edges=[];R=4*a-p
    def add(i,j,tag):
        if i==j:return
        check(nodes[i].D==nodes[j].D,'defect invariant on retained transport graph','transport')
        adj[i].add(j);adj[j].add(i)
        if i<j:edges.append([i,j,tag])
    for i,c in enumerate(nodes):
        if c.channel=='M':add(i,index['M',a*a//c.u],'middle_complement')
        else:
            for j,d in enumerate(nodes):
                if d.channel=='M' and (d.u-p*c.u)%R==0:
                    add(i,j,'exterior_middle_congruence')
    left=set(range(len(nodes)));comps=[]
    while left:
        seed=min(left);stack=[seed];seen={seed};left.remove(seed)
        while stack:
            i=stack.pop()
            for j in sorted(adj[i]):
                if j not in seen:seen.add(j);left.remove(j);stack.append(j)
        Ds={nodes[i].D for i in seen};check(len(Ds)==1,'complete transport component retains denominator','transport')
        comps.append({'nodes':sorted(seen),'D':next(iter(Ds))})
    return {'p':p,'a':a,'R':R,'scope':'restricted single shell',
            'nodes':[{'channel':c.channel,'u':c.u,'D':c.D} for c in nodes],
            'undirected_edges':edges,'components':comps}

def regression_tests(prototypes):
    import copy
    out=[]
    def rejects(obj,full):
        try:verify_rejection(obj,full)
        except (ValueError,ArithmeticError,KeyError,TypeError):return True
        return False
    for proto in prototypes:
        check(verify_rejection(proto,False),'restricted certificate valid','regression')
        q=copy.deepcopy(proto);q['scope']='full'
        check(rejects(q,True),'restricted scope cannot prove global failure','regression')
        q=copy.deepcopy(proto);q['rows'].pop()
        check(rejects(q,False),'deleted leaf rejected','regression')
        q=copy.deepcopy(proto);q['rows'][0]['D']+=2
        check(rejects(q,False),'wrong denominator rejected','regression')
        out.append({'p':proto['p'],'tests':['restricted replay passed','full-scope promotion rejected','missing leaf rejected','wrong denominator rejected']})
    # Forge a complete negative certificate at an actually solved prime.
    fake={'p':5,'scope':'full','shells':list(shell_range(5)),'rows':[]}
    for c in candidates(5):fake['rows'].append({'a':c.a,'u':c.u,'channel':c.channel,'D':max(3,c.D),'obstructing_prime':3,'inverse_gap':Q(1)})
    check(rejects(fake,True),'fabricated complete counterexample rejected','regression')
    return out

def selftest(out):
    formal();code,B=lattice_setup()
    profiles=[]
    for p in (5,13,37,97,241,1201,2521):
        Ds=Counter();hits=Counter();samples={};count=0;cleared=set()
        for c in candidates(p):
            check_candidate(c);count+=1;Ds[c.D]+=1;cleared.add(c.integral())
            if c.D==1:hits[c.channel]+=1;samples.setdefault(c.channel,c.record())
        check(count<= (p-1)**2,'quadratic-size complete atlas bound')
        check(len(cleared)==count,'cleared triple retains each canonical state at fixed p')
        profiles.append({'p':p,'full_shell_range':[p//4+1,3*p//4],'canonical_slots':count,
                 'clearing_denominator_histogram':Ds,'hit_counts':hits,'first_hits':samples})
    dump(out/'full_atlas_profiles.json',profiles)
    proto=[rejection_record(241,[64]),rejection_record(37,[18])]
    for o in proto:
        ds=[r['D'] for r in o['rows']]
        if o['p']==241:check(gcd(*ds)==1 and all(d>1 for d in ds),'no illegal gcd aggregation','regression')
        # Universal interpolation inverse without a separate existence oracle.
        for row in o['rows']:
            z=(row['D']-1)//2
            proj=prod((1-Q(z,j)) for j in range(1,o['p']-1))
            check(proj==0 and Q(1-proj,z)==row['inverse_gap'],'annihilator projector','operator')
    dump(out/'restricted_negative_prototypes.json',proto)
    graphs=[shell_graph(241,64),shell_graph(37,18)]
    check(sorted((x['D'],len(x['nodes'])) for x in graphs[0]['components'])==[(3,8),(5,12),(15,6)],'three exact restricted defect components','transport')
    dump(out/'restricted_transport_graphs.json',graphs)
    dump(out/'negative_certificate_regressions.json',regression_tests(proto))
    energies=[energy(p,a,True) for p,a in [(97,25),(241,64),(37,18),(1201,306),(2521,638)]]
    check(not energies[3]['ordinary_cauchy_forcing'] and energies[3]['strict_forcing'] and energies[3]['signed_symmetric_floor']==111,'strict improvement at 1201','energy')
    # Exact small relaxation: enumerate all odd/even/symmetric histograms for R=15.
    for N in range(1,20,2):
        m=(N-1)//2;best=None
        for x0 in range(m+1):
            for x1 in range(m-x0+1):
                for x2 in range(m-x0-x1+1):
                    rem=m-x0-x1-x2
                    for y0 in range(rem+1):
                        y1=rem-y0;val=(1+2*x0)**2+4*x1*x1+4*x2*x2+2*y0*y0+2*y1*y1
                        best=val if best is None else min(best,val)
        check(best==symmetric_energy_floor(N,15,{14}),'greedy equals exhaustive relaxation minimum','energy')
    dump(out/'collision_energy.json',energies)
    same=[]
    for p,a in [(241,64),(37,18),(1201,306),(1201,308),(2521,638)]:
        R=4*a-p;ds=[u for u,_ in divisors({q:2*e for q,e in factor(a).items()})]
        for u in ds:
            for u2 in ds:
                if (u2-p*u)%R==0:
                    ce=Candidate(p,a,u,'E');cm=Candidate(p,a,u2,'M')
                    check(ce.D==cm.D,'same-shell channel transport preserves full denominator','transport')
                    if ce.D>1 and len(same)<10:same.append({'p':p,'a':a,'R':R,'u_E':u,'u_M':u2,'common_D':ce.D})
    dump(out/'same_shell_defect_transport.json',same)
    # Exact maximal-outside-divisor formula on every unit cofactor <= 3000.
    R=19;A=35;H=qr(R);costs,height=anchor(R,A,H)
    check(height==35,'anchor exact height','anchor')
    for b in range(1,3001):
        if gcd(b,R)>1:continue
        t,_=greatest_outside(b,R,H)
        actual=max([d for d,_ in divisors(factor(b)) if d%R not in H] or [0])
        check(t==actual,'largest actual non-subgroup divisor','anchor')
    found=[]
    for b in range(1,78401,6):
        p=140*b-19
        if p<5 or not prime(p) or gcd(b,R)>1 or b%R not in H:continue
        t,q=greatest_outside(b,R,H)
        if q is None or not (t>8*height):continue
        w=angular_witness(p,R,A,H)
        if w is not None:
            check(w['new_uniform_sufficient'] and not w['old_uniform_sufficient'],'strict strengthened sufficient regime','anchor')
            found.append(w)
        if len(found)>=4:break
    check(len(found)==4,'four refined positive examples','anchor')
    dump(out/'sharpened_anchor_examples.json',{'R':R,'A':A,'H':sorted(H),'height':height,'costs':costs,'examples':found})
    # Rational failures and successes both traverse the marked diagrams.
    cs=[Candidate(241,64,1,'E'),Candidate(241,64,2,'M'),Candidate(37,18,12,'E'),
        Candidate(37,18,18,'M'),Candidate(1201,306,17,'E'),Candidate(2521,638,44,'M')]
    rows=[lifted_routes(c,code,B) for c in cs]
    # Include a newly forced witness.
    st=found[0]['state'];rows.append(lifted_routes(Candidate(st['p'],st['a'],st['u'],'M'),code,B))
    dump(out/'rational_integral_geometric_routes.json',rows)
    dump(out/'checks.json',{'checks_by_kind':CHECKS,'total':sum(CHECKS.values()),'counterexample_found':False,
       'scope':'full finite atlases at the listed seven primes; two explicitly restricted negative prototypes; general proofs in TeX'})
    print(json.dumps({'checks':sum(CHECKS.values()),'by_kind':CHECKS,'counterexample_found':False},sort_keys=True))

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out',type=Path,default=Path('certificates'))
    ap.add_argument('--self-test',action='store_true')
    ap.add_argument('--prime',type=int)
    ap.add_argument('--verify-negative',type=Path)
    args=ap.parse_args()
    if args.verify_negative:
        verify_rejection(json.loads(args.verify_negative.read_text()),True)
        print('VALID FULL COUNTEREXAMPLE CERTIFICATE');return
    if args.prime is not None:
        p=args.prime
        for c in candidates(p):
            if c.D==1:
                rec=check_candidate(c);dump(args.out/f'witness_{p}.json',rec)
                print(json.dumps(encode(rec),sort_keys=True));return
        cert=rejection_record(p);verify_rejection(cert,True)
        dump(args.out/f'counterexample_{p}.json',cert)
        print('VALIDATED FULL COUNTEREXAMPLE; certificate written');return
    selftest(args.out)
if __name__=='__main__':main()
