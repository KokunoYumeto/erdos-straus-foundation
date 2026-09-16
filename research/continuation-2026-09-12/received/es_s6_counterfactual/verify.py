#!/usr/bin/env python3
"""Exact ES denominator atlases and (3,4,infinity) affine torsion covers.
Python 3.10+, standard library only. No removable assertions.
The general orbit/genus claims are proved in workbench.tex. This program
replays finite certificates; it does not certify the entire S6 manuscript.
"""
from __future__ import annotations
import argparse, gzip, hashlib, itertools, json, sys, time
from collections import Counter
from fractions import Fraction as F
from math import gcd, isqrt, prod
from pathlib import Path

CHECKS=Counter()
def require(ok, name, kind='exact'):
    CHECKS[kind]+=1
    if not ok: raise ArithmeticError(name)
def enc(v):
    if isinstance(v,F): return {'numerator':v.numerator,'denominator':v.denominator}
    if isinstance(v,dict): return {str(k):enc(x) for k,x in v.items()}
    if isinstance(v,(list,tuple)): return [enc(x) for x in v]
    return v
def json_bytes(v): return (json.dumps(enc(v),sort_keys=True,separators=(',',':'))+'\n').encode()
def save(path,v,compact=False):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    if path.suffix=='.gz':path.write_bytes(gzip.compress(json_bytes(v),compresslevel=9,mtime=0))
    else:path.write_text(json.dumps(enc(v),sort_keys=True,indent=None if compact else 2)+'\n')
def load(path):
    path=Path(path);b=path.read_bytes()
    return json.loads(gzip.decompress(b) if path.suffix=='.gz' else b)
def prime(n):
    return n>=2 and (n==2 or n%2 and all(n%d for d in range(3,isqrt(n)+1,2)))
def factor(n):
    if n<1:raise ValueError('factor domain: n>=1')
    out=[];q=2
    while q*q<=n:
        e=0
        while n%q==0:n//=q;e+=1
        if e:out.append((q,e))
        q=3 if q==2 else q+2
    if n>1:out.append((n,1))
    return out
def valuation(n,q):
    if n==0:raise ValueError('finite valuation requires nonzero input')
    e=0
    while n%q==0:e+=1;n//=q
    return e
def divisor_box(fs):
    for exps in itertools.product(*(range(2*e+1) for q,e in fs)):
        yield prod(q**e for (q,_),e in zip(fs,exps)),exps

def matmul(a,b,mod=None):
    c=tuple(tuple(sum(x*y for x,y in zip(row,col)) for col in zip(*b)) for row in a)
    return tuple(tuple(x%mod for x in row) for row in c) if mod else c
def trans(a):return tuple(zip(*a))
def eye(n):return tuple(tuple(int(i==j) for j in range(n)) for i in range(n))
def power(a,n,mod=None):
    z=eye(len(a))
    while n:
        if n&1:z=matmul(z,a,mod)
        a=matmul(a,a,mod);n//=2
    return z

def det(a):
    # Determinant by permutations: all matrices here have size <=4.
    n=len(a);ans=0
    for s in itertools.permutations(range(n)):
        inv=sum(s[i]>s[j] for i in range(n) for j in range(i+1,n))
        ans+=(-1)**inv*prod(a[i][s[i]] for i in range(n))
    return ans

T1=((1,0,-6,2),(0,-1,1,1),(0,-1,0,1),(0,0,0,1))
T2=((1,6,0,-3),(0,0,-1,1),(0,1,0,0),(0,0,0,1))
A1=((1,0,0,0),(6,0,1,0),(-6,-1,-1,0),(-2,1,0,1))
A2=((1,0,0,0),(0,0,-1,0),(-6,1,0,0),(3,0,1,1))
AI=((1,0,0,0),(0,1,0,0),(0,1,1,0),(-1,0,0,1))
I4=eye(4)

def move(k,v,D):
    x,y,z=v
    if k==0:return ((6+y)%D,(-6-x-y)%D,(z-2+x)%D)
    if k==1:return ((-y)%D,(x-6)%D,(z+3+y)%D)
    if k==2:return (x%D,(y+x)%D,(z-1)%D)
    raise ValueError('generator index 0,1,2')
def inverse_move(k,v,D):
    if k==0:return move(0,move(0,v,D),D)
    if k==1:return move(1,move(1,move(1,v,D),D),D)
    x,y,z=v
    return (x%D,(y-x)%D,(z+1)%D)
def index(v,D):return (v[0]*D+v[1])*D+v[2]
def point(i,D):return (i//(D*D),(i//D)%D,i%D)
def cycles(perm,subset):
    seen=set();hist=Counter()
    for i in subset:
        if i in seen:continue
        j=i;n=0
        while j not in seen:
            seen.add(j);n+=1;j=perm[j]
        require(j==i,'permutation cycle closes at its start','cycles')
        hist[n]+=1
    require(len(seen)==len(subset),'cycle support complete','cycles')
    return dict(sorted(hist.items()))

def passport(D):
    if D<1 or D%2==0:raise ValueError('positive odd D required')
    def component(tag,n,f1,f2):
        require((n-f1)%3==0 and (n-f2)%4==0 and n%D==0,'passport divisibility','formulas')
        hist1={};hist2={}
        if f1:hist1[1]=f1
        if n>f1:hist1[3]=(n-f1)//3
        if f2:hist2[1]=f2
        if n>f2:hist2[4]=(n-f2)//4
        histI={D:n//D}
        chi=sum(hist1.values())+sum(hist2.values())+sum(histI.values())-n
        require((2-chi)%2==0 and chi<=2,'genus is nonnegative integer','formulas')
        return {'component':tag,'degree':n,'genus':(2-chi)//2,
                'cycles_0':hist1,'cycles_1':hist2,'cycles_infinity':histI}
    if D%3:
        ans=[component('connected',D**3,D,D)]
        require(ans[0]['genus']==(5*D**3-12*D**2-17*D+24)//24,'connected genus formula','formulas')
    else:
        n=D**3//9
        ans=[component('x=y=0 mod 3',n,0,D),component('(x,y) nonzero mod 3',8*n,D,0)]
        require(ans[0]['genus']==(5*D**3-12*D**2-81*D+216)//216,'zero genus formula','formulas')
        require(ans[1]['genus']==(5*D**3-12*D**2-9*D+27)//27,'nonzero genus formula','formulas')
    return ans

def enumerate_level(D,store=False):
    n=D**3
    ps=[[index(move(k,point(i,D),D),D) for i in range(n)] for k in range(3)]
    for i in range(n):
        v=point(i,D)
        for k in range(3):
            require(inverse_move(k,move(k,v,D),D)==v,'inverse affine map','affine_points')
        require(ps[0][ps[0][ps[0][i]]]==i,'order divides 3','affine_points')
        require(ps[1][ps[1][ps[1][ps[1][i]]]]==i,'order divides 4','affine_points')
        require(ps[0][ps[1][ps[2][i]]]==i,'product of loops','affine_points')
    done=bytearray(n);components=[]
    for i in range(n):
        if done[i]:continue
        done[i]=1;stack=[i];part=[]
        while stack:
            j=stack.pop();part.append(j)
            for perm in ps[:2]:
                k=perm[j]
                if not done[k]:done[k]=1;stack.append(k)
        h=[cycles(p,part) for p in ps]
        chi=sum(map(lambda x:sum(x.values()),h))-len(part)
        tag='connected' if D%3 else ('x=y=0 mod 3' if point(i,D)[0]%3==point(i,D)[1]%3==0 else '(x,y) nonzero mod 3')
        if D%3==0:
            require(all((point(j,D)[0]%3==point(j,D)[1]%3==0)==(tag=='x=y=0 mod 3') for j in part),'exact residue orbit','orbits')
        components.append({'component':tag,'degree':len(part),'genus':(2-chi)//2,
            'cycles_0':h[0],'cycles_1':h[1],'cycles_infinity':h[2]})
    expected=passport(D)
    require(sorted(components,key=lambda x:x['degree'])==sorted(expected,key=lambda x:x['degree']),f'orbit passport D={D}','orbits')
    out={'D':D,'degree':n,'components':components,'has_section':D==1,
         'point_index':'(x*D+y)*D+z; x,y,z in {0,...,D-1}'}
    if store:out['permutations']=ps
    return out


def matrix_checks():
    require(matmul(trans(T1),A1)==I4,'inverse transpose duality 1','matrices')
    require(matmul(trans(T2),A2)==I4,'inverse transpose duality 2','matrices')
    require(power(A1,3)==I4 and power(A2,4)==I4,'finite source orders','matrices')
    require(matmul(matmul(A1,A2),AI)==I4,'cusp inverse','matrices')
    require(all(det(a)==1 for a in [T1,T2,A1,A2,AI]),'unimodularity','matrices')
    N=tuple(tuple(AI[i][j]-I4[i][j] for j in range(4)) for i in range(4))
    require(matmul(N,N)==tuple((0,)*4 for _ in range(4)),'unipotent square zero','matrices')
    H=matmul(matmul(matmul(power(A2,2),A1),power(A2,2)),power(A1,2))
    V=matmul(matmul(A2,H),power(A2,3))
    Hinv=((1,0,0,0),(0,1,0,0),(-6,0,1,0),(6,-1,0,1))
    Vinv=((1,0,0,0),(6,1,0,0),(0,0,1,0),(-6,0,-1,1))
    central=matmul(matmul(matmul(H,V),Hinv),Vinv)
    require(H==((1,0,0,0),(0,1,0,0),(6,0,1,0),(-6,1,0,1)),'horizontal shear','matrices')
    require(V==((1,0,0,0),(-6,1,0,0),(0,0,1,0),(6,0,1,1)),'vertical shear','matrices')
    require(central==((1,0,0,0),(0,1,0,0),(0,0,1,0),(-12,0,0,1)),'central -12 commutator','matrices')
    require(matmul(H,Hinv)==matmul(V,Vinv)==I4,'shear inverses','matrices')
    return dict(T1=T1,T2=T2,A1=A1,A2=A2,A_infinity=AI,H=H,V=V,commutator=central)


def cocycle_checks():
    def split(A):
        return tuple(tuple(A[i][j] for j in range(1,4)) for i in range(1,4)), tuple(A[i][0] for i in range(1,4))
    def mv(A,x):return tuple(sum(a*b for a,b in zip(row,x)) for row in A)
    mats=[A1,A2,AI,power(A1,2),power(A2,3)]
    for A,B in itertools.product(mats,repeat=2):
        LA,bA=split(A);LB,bB=split(B);LC,bC=split(matmul(A,B))
        require(LC==matmul(LA,LB) and bC==tuple(x+y for x,y in zip(mv(LA,bB),bA)), 'extension cocycle law','cohomology')
    L,b=split(AI)
    require(b==(0,0,-1) and tuple(L[2][j]-int(j==2) for j in range(3))==(0,0,0),'primitive cusp class and zero coboundary evaluation','cohomology')
    for A,v in[(A1,(2,-4,0)),(A2,(3,-3,0))]:
        L,b=split(A)
        require(tuple(x+y for x,y in zip(mv(L,v),b))==v,'finite subgroup local section','cohomology')
    for D in range(1,80,2):
        order=next(k for k in range(1,D+1) if (-k)%D==0)
        require(order==D,'exact reduced cohomology order','cohomology')
    return {'integral_cusp_evaluation':-1,'integral_class':'primitive infinite order; splits a Z summand',
            'finite_class_order':'D','local_fixed_vectors':{'A1':[2,-4,0],'A2':[3,-3,0]},
            'cocycle_generators':{'A1':split(A1)[1],'A2':split(A2)[1],'A_infinity':split(AI)[1]},
            'arithmetic_inverse':'[k*gate mod R] -> k[c_D]; inverse k=-cusp_evaluation(class) mod D'}

def mod3_group():
    gens=[tuple(tuple(x%3 for x in row) for row in m) for m in [A1,A2]]
    seen={I4};stack=[I4]
    while stack:
        a=stack.pop()
        for b in gens:
            c=matmul(b,a,3)
            if c not in seen:seen.add(c);stack.append(c)
    require(len(seen)==216,'level-3 group order','level3_group')
    bases={};kernel=[]
    for g in seen:
        A=tuple(tuple(g[i][j] for j in (1,2)) for i in (1,2));k=g[3][0]
        require(det(A)%3==1,'SL2 projection','level3_group')
        require(all(g[i][0]==0 for i in(1,2)),'zero planar translations mod3','level3_group')
        if A in bases:require(bases[A]==k,'constant component determined by SL2','level3_group')
        else:bases[A]=k
        if A==eye(2):kernel.append(g[3][:3])
    allsl={((a,b),(c,d)) for a,b,c,d in itertools.product(range(3),repeat=4) if (a*d-b*c)%3==1}
    require(set(bases)==allsl and len(allsl)==24,'complete SL2(3)','level3_group')
    require(set(kernel)=={(0,l,m) for l,m in itertools.product(range(3),repeat=2)},'two-dimensional normal subgroup','level3_group')
    for a,ka in bases.items():
        for b,kb in bases.items():
            require(bases[matmul(a,b,3)]==(ka+kb)%3,'SL2 character and splitting','level3_group')
    # All expected matrices from the split semidirect product are present.
    model=set()
    for a,k in bases.items():
        for l,m in itertools.product(range(3),repeat=2):
            model.add(((1,0,0,0),(0,*a[0],0),(0,*a[1],0),(k,l,m,1)))
    require(model==seen,'complete semidirect-product equality','level3_group')
    return {'order':216,'group':'(F_3^2)^* semidirect SL_2(F_3), isomorphic to ASL_2(F_3)',
            'matrices':sorted(seen),'SL2_character':[{'A':a,'chi':k} for a,k in sorted(bases.items())]}


def crt(a,b,m,n):
    if gcd(m,n)!=1:raise ValueError('coprime CRT only')
    return (a+m*((b-a)*pow(m,-1,n)%n))%(m*n)
def naturality_tests():
    cases=[]
    for m,n in[(3,5),(9,5),(5,7)]:
        D=m*n
        for i in range(D**3):
            v=point(i,D);reduced=(tuple(x%m for x in v),tuple(x%n for x in v))
            require(tuple(crt(a,b,m,n) for a,b in zip(*reduced))==v,'CRT inverse','CRT')
            for k in range(3):
                w=move(k,v,D)
                require(tuple(x%m for x in w)==move(k,reduced[0],m) and tuple(x%n for x in w)==move(k,reduced[1],n),'CRT monodromy','CRT')
        cases.append([m,n])
    for E,D in[(15,3),(45,9),(25,5)]:
        counts=Counter(tuple(x%D for x in point(i,E)) for i in range(E**3))
        require(len(counts)==D**3 and set(counts.values())=={(E//D)**3},'reduction fibres','CRT')
    return {'coprime_pairs_exhausted':cases,'divisor_reductions':[[15,3],[45,9],[25,5]]}


def rational_row(p,a,u,channel,swap):
    R=4*a-p
    if channel=='E':q=(F(a),F(p*a+a*a//u,R),F(p*a+p*p*u,R));gate=4*u+1
    else:q=(F(a),F(p*(a+a*a//u),R),F(p*(a+u),R));gate=u+a
    if swap:q=(q[0],q[2],q[1])
    D=R//gcd(R,gate)
    g=gcd(a,u);h=F(g*g,u);r=u//g;s=a//g
    quotient=F(p*r+s,R) if channel=='E' else F(r+s,R)
    if h.denominator!=1:raise ArithmeticError('primitive scale not integral')
    X=tuple(D*v for v in q)
    local=[]
    for ell,e in factor(R):
        val=valuation(gate,ell);loss=max(e-val,0)
        local.append({'prime':ell,'v_R':e,'v_gate':val,'loss':loss})
    return {'p':p,'a':a,'R':R,'u':u,'channel':channel,'swap':swap,
            'h':h.numerator,'r':r,'s':s,'kappa' if channel=='E' else 'lambda':quotient,
            'Q':q,'D':D,'X':X,'new_parameter':p*D,'local_deficits':local}

def check_row(row):
    p,a,R,u,D=row['p'],row['a'],row['R'],row['u'],row['D'];q=row['Q'];X=row['X']
    require(sum((1/t for t in q),F())==F(4,p),'rational ES identity','atlas')
    require(all(t>0 for t in q) and all(t.denominator==1 for t in X),'positive integral clearing','atlas')
    require(all(q[j].denominator==D for j in[1,2]),'common minimal denominator','atlas')
    q0=q if not row['swap'] else(q[0],q[2],q[1])
    uv=F(a*a,R*q0[1]-p*a) if row['channel']=='E' else F(p*a*a,R*q0[1]-p*a)
    require(uv==u,'typed rational inverse','atlas')
    require(a==row['h']*row['r']*row['s'] and u==row['h']*row['r']**2 and gcd(row['r'],row['s'])==1,'primitive normalization','atlas')
    S=X[0]*X[1]+X[0]*X[2]+X[1]*X[2]
    require(4*prod(X)-p*S==p*(D-1)*S,'original-prime defect','atlas')
    require(prod(z['prime']**z['loss'] for z in row['local_deficits'])==D,'all local losses retained','atlas')
    require(D%2==1 and gcd(D,p)==1,'denominator domain','atlas')
    # Cyclic obstruction group: k -> k*gate mod R has order D and explicit inverse.
    gate=4*u+1 if row['channel']=='E' else u+a;d=gcd(R,gate)
    k=(u+row['swap'])%D
    image=k*gate%R
    recovered=0 if D==1 else ((image//d)*pow(gate//d,-1,D))%D
    require(recovered==k,'cyclic obstruction marked inverse','atlas')


def make_atlas(p,only_shell=None):
    if not prime(p) or p%4!=1:raise ValueError('a prime p=1 mod4 is required')
    m=(p-1)//4;alls=range(m+1,3*m+1)
    if only_shell is not None and only_shell not in alls:raise ValueError('shell outside the full interval')
    shells=[];hist=Counter();hits=[];total=0
    for a in ([only_shell] if only_shell is not None else alls):
        fs=factor(a);rows=[]
        for u,exps in sorted(divisor_box(fs)):
            for c,swap in [('E',0),('E',1),('M',0)]:
                row=rational_row(p,a,u,c,swap);check_row(row)
                row['exponents']=exps
                rows.append(row);hist[row['D']]+=1;total+=1
                if row['D']==1:hits.append((a,u,c,swap))
        shells.append({'a':a,'factorization':fs,'rows':rows})
    require(2*total<=3*(p-1)**2,'full ordered count bound','atlas')
    degree=sum(n*D**3 for D,n in hist.items())
    components=sum(n*len(passport(D)) for D,n in hist.items())
    genera=sum(n*sum(c['genus'] for c in passport(D)) for D,n in hist.items())
    return {'schema':'es-s6-affine-defect-atlas/1','p':p,
        'scope':'full' if only_shell is None else 'restricted','shell_interval':[m+1,3*m],
        'shells':shells,'row_count':total,'D_histogram':dict(sorted(hist.items())),
        'success_rows':hits,'success_count':len(hits),
        'cover_summary':{'degree':degree,'connected_components':components,'sum_of_component_genera':genera,
                         'global_sections':len(hits),'large_covers':'specified by exact formulas; not explicitly enumerated'},
        'passport_by_D':{D:passport(D) for D in sorted(hist)}}


def restricted_graph(data):
    if len(data['shells'])!=1:raise ValueError('one-shell graph certificate')
    rows=data['shells'][0]['rows'];R=rows[0]['R'];p=rows[0]['p'];a=rows[0]['a']
    edges=[];adj=[set() for _ in rows]
    for i,r in enumerate(rows):
        for j in range(i+1,len(rows)):
            t=rows[j];kind=None
            if r['channel']==t['channel']=='E' and r['u']==t['u'] and r['swap']!=t['swap']:kind='exterior order reversal'
            if r['channel']==t['channel']=='M' and r['u']*t['u']==a*a:kind='middle complement'
            if r['channel']!=t['channel']:
                E,M=(r,t) if r['channel']=='E' else(t,r)
                if (M['u']-p*E['u'])%R==0:kind='same-shell E/M correspondence'
            if kind:
                require(r['D']==t['D'],'transport preserves denominator and cover level','transport')
                edges.append({'from':i,'to':j,'kind':kind});adj[i].add(j);adj[j].add(i)
    seen=set();parts=[]
    for i in range(len(rows)):
        if i in seen:continue
        stack=[i];seen.add(i);part=[]
        while stack:
            j=stack.pop();part.append(j)
            for k in adj[j]:
                if k not in seen:seen.add(k);stack.append(k)
        parts.append({'D':rows[i]['D'],'vertices':sorted(part),'size':len(part)})
    require(sorted((c['D'],c['size']) for c in parts)==[(3,12),(5,18),(15,9)],'full ordered restricted graph components','transport')
    return {'p':p,'a':a,'R':R,'vertices':[{'u':r['u'],'channel':r['channel'],'swap':r['swap'],'D':r['D']} for r in rows],
            'edges':edges,'components':parts,'cover_transport':'identity on the three torsion coordinates; retain the source and target arithmetic labels and the edge'}

def validate_negative(data):
    """Reject restricted certificates and any omitted/altered full-atlas record."""
    if data.get('scope')!='full':raise ValueError('restricted failure is not a full ES counterexample')
    expected=enc(make_atlas(int(data['p'])))
    if data!=expected:raise ValueError('full labelled atlas differs from exact recomputation')
    if expected['success_count']:raise ValueError('positive ES witnesses are present')
    return True


def filling_tests():
    rows=[]
    for D in range(1,80,2):
        if D%3==0:continue
        l0=0;l2=1 if D%4==1 else -1;l1=-(D+3*l2)//4
        M=((-l1,3,0),(-l2,0,4),(-l0,1,1))
        minors=[abs(det(tuple(tuple(M[i][j] for j in cs) for i in rs))) for rs in itertools.combinations(range(3),2) for cs in itertools.combinations(range(3),2)]
        require(12*l0-4*l1-3*l2==D and gcd(l1,3)==gcd(l2,4)==1,'admissible twist return','fillings')
        require(abs(det(M))==D and gcd(*minors)==1,'Smith invariants 1,1,D','fillings')
        # Gamma maps to 1; solve the other two generators, since 3,4 are units mod D.
        s1=0 if D==1 else l1*pow(3,-1,D)%D
        s2=0 if D==1 else l2*pow(4,-1,D)%D
        require((3*s1-l1)%D==(4*s2-l2)%D==(s1+s2-l0)%D==0,'marked cyclic presentation map','fillings')
        rows.append({'D':D,'ell':[l0,l1,l2],'relation_matrix':M,'generators_to_ZD':[0 if D==1 else 1,s1,s2]})
    require(12*0-4*1-3*(-1)==-1,'original source twist sign','fillings')
    return rows


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out',type=Path,default=Path('certificates'))
    ap.add_argument('--prime',type=int)
    ap.add_argument('--shell',type=int)
    ap.add_argument('--validate-negative',type=Path)
    args=ap.parse_args()
    if args.validate_negative:
        validate_negative(load(args.validate_negative));print('FULL NEGATIVE CERTIFICATE VERIFIED');return
    if args.prime:
        data=make_atlas(args.prime,args.shell)
        name=f'atlas_p{args.prime}'+(f'_a{args.shell}' if args.shell else '')+'.json.gz'
        save(args.out/name,data)
        print(json.dumps(enc({k:data[k] for k in ['p','scope','row_count','D_histogram','success_count','cover_summary']}),sort_keys=True));return
    save(args.out/'source_matrices.json',matrix_checks())
    levels=[1,3,5,7,9,15,21,25,27,35,45]
    records=[]
    for D in levels:
        record=enumerate_level(D,store=(D<=9))
        records.append({k:v for k,v in record.items() if k!='permutations'})
        if D<=9:save(args.out/f'permutations_D{D}.json.gz',record)
    save(args.out/'orbit_passports.json',records)
    save(args.out/'cohomology.json',cocycle_checks())
    save(args.out/'level3_group.json',mod3_group())
    save(args.out/'naturality.json',naturality_tests())
    save(args.out/'twist_presentations.json',filling_tests())
    summaries=[]
    for p in[5,37,241,1201]:
        data=make_atlas(p)
        save(args.out/f'atlas_p{p}.json.gz',data)
        summaries.append({k:v for k,v in data.items() if k not in ['shells','passport_by_D']})
        require(data['success_count']>0,f'actual test prime {p} is not a counterexample','regressions')
    restricted=make_atlas(241,64)
    require(restricted['success_count']==0 and restricted['row_count']==39,'restricted 241/64 genuinely empty','regressions')
    require(restricted['cover_summary']['degree']==32949 and restricted['cover_summary']['connected_components']==60 and restricted['cover_summary']['sum_of_component_genera']==5448,'restricted cover totals','regressions')
    save(args.out/'restricted_p241_a64.json.gz',restricted)
    save(args.out/'restricted_transport_graph.json',restricted_graph(restricted))
    try:validate_negative(enc(restricted))
    except ValueError:require(True,'reject restricted negative','regressions')
    else:raise ArithmeticError('restricted certificate accepted as global')
    bad=enc(make_atlas(5));bad['shells'][0]['rows'].pop()
    try:validate_negative(bad)
    except ValueError:require(True,'reject missing candidate','regressions')
    else:raise ArithmeticError('omission accepted')
    try:validate_negative(enc(make_atlas(5)))
    except ValueError:require(True,'reject actual success as full negative','regressions')
    else:raise ArithmeticError('success accepted as full negative')
    save(args.out/'atlas_summaries.json',summaries)
    receipt={'status':'PASS','check_count':sum(CHECKS.values()),'checks_by_kind':dict(CHECKS),
             'explicit_levels':levels,'full_atlas_primes':[5,37,241,1201],
             'full_S6_theorem_reverified':False,'global_ES_counterexample_found':False,
             'whole_cover_fibre_limits':'Only levels listed above explicitly expanded; all atlas cover degrees/ramification use proved closed formulas.'}
    save(args.out/'checks.json',receipt)
    print(json.dumps(receipt,sort_keys=True))

if __name__=='__main__':main()
