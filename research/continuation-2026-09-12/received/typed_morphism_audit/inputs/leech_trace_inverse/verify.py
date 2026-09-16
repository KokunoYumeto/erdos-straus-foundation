#!/usr/bin/env python3
"""Exact Leech-to-trace inverses and finite certificates, Python >= 3.9.
Standard library only. No network, no prior-package imports, no removed asserts.
General existence and nonexistence proofs are in note.tex. This is not an ES proof.
"""
from __future__ import annotations
import argparse, hashlib, itertools, json, sys
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path
CHECKS=0

def need(c,msg):
    global CHECKS
    CHECKS+=1
    if not c: raise ArithmeticError(msg)

def save(p,x):
    p.write_text(json.dumps(x,sort_keys=True,indent=2)+'\n',encoding='utf8')

P=23; INF=23
ID=(1,0,0,1); C=(12,5,1,12); J=(1,7,3,22); T=(4,11,16,4)
def mm(a,b):
    e,f,g,h=a;i,j,k,l=b
    return ((e*i+f*k)%P,(e*j+f*l)%P,(g*i+h*k)%P,(g*j+h*l)%P)
def pw(a,n):
    b=ID
    for _ in range(n): b=mm(b,a)
    return b

def canon(a):return min(a,tuple(-x%P for x in a))
def inv(a):a,b,c,d=a;return (d,-b%P,-c%P,a)
def perm(a):
    a,b,c,d=a;v=[]
    for i in range(24):
        n,m=(a,c) if i==INF else ((a*i+b)%P,(c*i+d)%P)
        v.append(INF if m==0 else n*pow(m,-1,P)%P)
    return tuple(v)
def move(x,g):
    y=[0]*24
    for i,a in enumerate(x):y[g[i]]=a
    return tuple(y)
def add(x,y):return tuple(a+b for a,b in zip(x,y))
def sub(x,y):return tuple(a-b for a,b in zip(x,y))
def scale(c,x):return tuple(c*a for a in x)
def combine(cs,vs):return tuple(sum(c*v[i] for c,v in zip(cs,vs)) for i in range(24))
def inner(x,y):return Q(sum(a*b for a,b in zip(x,y)),8)
def norm(x):return inner(x,x)
ZERO=(0,)*24

def binary_basis(rows):
    piv={}
    for x in rows:
        while x:
            k=x.bit_length()-1
            if k in piv:x^=piv[k]
            else:piv[k]=x;break
    return [piv[k] for k in sorted(piv,reverse=True)]
def words(basis):
    a=[0]
    for b in basis:a += [x^b for x in a]
    return sorted(a)
def mask(s):return sum(1<<i for i in s)
def pmask(x,g):return sum(1<<g[i] for i in range(24) if x>>i&1)
def member(x,code):
    if any(not isinstance(a,int) for a in x):return False
    m=x[0]%2
    return (all(a%2==m for a in x) and sum(x)%8==4*m and
            sum(1<<i for i,a in enumerate(x) if ((a-m)//2)%2) in code)

def mins(code):
    for i,j in itertools.combinations(range(24),2):
        for a,b in itertools.product((-4,4),repeat=2):
            x=[0]*24;x[i]=a;x[j]=b;yield tuple(x)
    for c in code:
        if c.bit_count()!=8:continue
        sup=[i for i in range(24) if c>>i&1]
        for s in range(256):
            if s.bit_count()%2:continue
            x=[0]*24
            for j,i in enumerate(sup):x[i]=-2 if s>>j&1 else 2
            yield tuple(x)
    for i in range(24):
        for c in code:
            x=[1-2*((c>>j)&1) for j in range(24)];x[i]*=-3;yield tuple(x)

def determinant(A):
    a=[[Q(x) for x in r] for r in A];d=Q(1);n=len(a)
    for i in range(n):
        j=next((j for j in range(i,n) if a[j][i]),None)
        if j is None:return Q(0)
        if j!=i:a[i],a[j]=a[j],a[i];d=-d
        v=a[i][i];d*=v
        for j in range(i+1,n):
            c=a[j][i]/v
            for k in range(i,n):a[j][k]-=c*a[i][k]
    return d

# A norm-four, C-equivariant three-trace section: actual vector is B0/sqrt(8).
B0=(-3,1,-1,1,1,-1,-1,1,1,1,1,1,1,-1,1,1,1,1,-1,-1,-1,-1,1,1)
# Nine norm-four columns of an integral right inverse for the four-time trace map.
LIFTS9=(
(-1,-1,-1,1,3,-1,1,1,-1,-1,1,1,-1,-1,1,1,1,1,-1,-1,1,-1,1,1),
(-3,-1,-1,1,1,1,1,1,-1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,1,-1,1),
(-1,-1,-1,-1,1,-1,1,1,-1,1,1,3,-1,1,-1,1,1,1,-1,1,1,-1,-1,1),
(-2,-2,-2,0,2,0,0,0,2,0,-2,0,0,0,2,0,0,0,0,0,0,2,0,0),
(-2,0,-2,0,0,2,-2,0,0,0,0,2,0,0,0,0,2,0,2,0,0,0,-2,0),
(-2,-2,0,2,0,0,0,0,2,0,0,0,0,0,0,0,0,0,2,-2,2,-2,0,0),
(-2,-2,0,2,0,0,0,0,2,-2,0,2,0,0,2,0,0,-2,0,0,0,0,0,0),
(-2,-2,0,0,0,0,0,0,2,-2,-2,0,0,2,0,0,0,0,2,0,0,0,0,2),
(-2,0,0,0,0,0,0,2,0,0,-2,0,0,-2,2,0,0,0,2,0,2,-2,0,0))

def run(out):
    out.mkdir(parents=True,exist_ok=True)
    qr={i*i%23 for i in range(1,23)}
    bas=binary_basis([(1<<23)|mask({(a+q)%23 for q in qr}) for a in range(23)])
    code=words(bas);cs=set(code)
    need(len(bas)==12 and len(cs)==4096,'Golay dimension')
    need(Counter(x.bit_count() for x in code)=={0:1,8:759,12:2576,16:759,24:1},'Golay enumerator')
    for a,b in itertools.product(bas,repeat=2):need((a&b).bit_count()%2==0,'code self orthogonal')
    cp,tp,jp=perm(C),perm(T),perm(J)
    for g in (cp,tp,jp):
        for b in bas:need(pmask(b,g) in cs,'permutation preserves code')
    need(pw(T,4)==C and pw(T,12)==(22,0,0,22),'retained T powers')
    v4=(ID,J,mm(mm(C,J),inv(C)),mm(mm(pw(C,2),J),inv(pw(C,2))))
    groups=sorted({canon(mm(g,pw(C,n))) for g in v4 for n in range(3)})
    need(len(groups)==12,'A4 order')
    B=[]
    tetrads=[]
    for base in (23,0):
        for n in range(3):tetrads.append(sorted({perm(mm(g,pw(C,n)))[base] for g in v4}))
    for n in range(3): B.append(sorted(tetrads[n]+tetrads[n+3]))
    need(B==[[0,1,3,4,7,8,16,23],[10,12,15,18,19,20,21,22],[2,5,6,9,11,13,14,17]],'phase octad table')
    need(sorted(sum(B,[]))==list(range(24)),'partition')
    for bb in B:need(mask(bb) in cs and len(bb)==8,'phase octad in code')
    W=[tuple(2*int(i in bb) for i in range(24)) for bb in B]
    def tr(x):
        vals=[sum(x[i] for i in bb) for bb in B]
        if any(a%4 for a in vals):raise ArithmeticError('nonintegral trace input')
        return tuple(a//4 for a in vals)
    def rot(t):return (t[2],t[0],t[1])
    BS=(B0,move(B0,cp),move(move(B0,cp),cp))
    for i in range(3):
        need(move(W[i],cp)==W[(i+1)%3],'C cycles complete octads')
        need(member(W[i],cs) and member(BS[i],cs),'frame and lift members')
        need(tr(BS[i])==tuple(int(i==j) for j in range(3)),'three-column right inverse')
        for j in range(3):
            need(inner(W[i],W[j])==4*int(i==j),'orthogonal trace frame')
            need(inner(BS[i],BS[j])==4*int(i==j),'orthogonal lift frame')
            need(inner(BS[i],W[j])==int(i==j),'dual pairing')
        need(tr(move(BS[i],cp))==rot(tr(BS[i])),'cyclic trace convention')
    # Finite fixed-code calculation proves the all-vector V4 section obstruction.
    fixed=[]
    for a in itertools.product((0,1),repeat=6):
        c=mask({i for k,dd in enumerate(tetrads) if a[k] for i in dd})
        if c in cs:fixed.append(a)
    need(set(fixed)=={a+a for a in itertools.product((0,1),repeat=3)},'V4-fixed code equals unions of phase octads')
    for g in v4:
        for w in W:need(move(w,perm(g))==w,'V4 fixes trace frame')
    # Complete minimal shell, its projected distribution, and inverse representatives.
    hist=Counter();reps={};type_counts=Counter();moment=[0,0,0];shellcount=0
    def red(r):return tuple(a if a<=2 else -1 for a in r)
    for x in mins(code):
        shellcount+=1
        need(member(x,cs) and norm(x)==4,'complete minimal-vector reconstruction')
        t=tr(x);hist[t]+=1
        r=tuple(a%4 for a in t)
        if t==red(r) and r!=(0,0,0):
            if r not in reps or x<reps[r]:reps[r]=x
        a,b,c=t;prod=a*b*c;ss=a*b+a*c+b*c
        moment[0]+=16*prod*prod;moment[1]+=-8*prod*ss;moment[2]+=ss*ss
    need(shellcount==196560 and len(hist)==123,'full shell and projected support')
    need(moment==[737280,0,241920],'exact polynomial ES second moment')
    need(set(reps)==set(itertools.product(range(4),repeat=3))-{(0,0,0),(2,2,2)},'all sixty-two ordinary nonzero residue representatives')
    reps[(0,0,0)]=ZERO
    dodecs=[c for c in code if c.bit_count()==12 and all((c&mask(bb)).bit_count()==4 for bb in B)]
    need(len(dodecs)==1232,'balanced dodecads')
    reps[(2,2,2)]=tuple(2*((min(dodecs)>>i)&1) for i in range(24))
    rows=[]
    for r in itertools.product(range(4),repeat=3):
        a=red(r);x=reps[r]
        need(member(x,cs) and tr(x)==a,'reduced inverse certificate')
        mu4=int(4*norm(x)-sum(z*z for z in a))
        expected=0 if r==(0,0,0) else 12 if r==(2,2,2) else 16-sum(z*z for z in a)
        need(mu4==expected,'minimal residual norm formula')
        mult=1 if r==(0,0,0) else 1232 if r==(2,2,2) else hist[a]
        expected_multiplicities={(0,0,0):1,(0,0,1):10528,(0,1,1):5440,(1,1,1):2688,(0,0,2):1288,(0,1,2):560,(1,1,2):224,(0,2,2):28,(1,2,2):8,(2,2,2):1232}
        need(mult==expected_multiplicities[tuple(sorted(abs(z) for z in a))],'complete type multiplicities')
        rows.append({'residue_mod4':r,'reduced_trace':a,'representative_numerator':x,'mu_times4':mu4,'minimal_lift_multiplicity':mult})
    def shortest(t):
        r=tuple(a%4 for a in t);a=red(r);ns=tuple((t[i]-a[i])//4 for i in range(3))
        x=add(reps[r],combine(ns,W));need(member(x,cs) and tr(x)==t,'all-input affine inverse specialization')
        mu4=next(k['mu_times4'] for k in rows if k['residue_mod4']==r)
        need(4*norm(x)==sum(a*a for a in t)+mu4,'optimal inverse norm at tested input')
        return x
    for t in itertools.product(range(-6,7),repeat=3):shortest(t)
    # Every identity used below is linear and so is tested on its explicit basis.
    cocycles=[]
    for g in groups:
        gp=perm(g)
        for i,b in enumerate(BS):
            outtr=tr(move(b,gp));corr=sub(move(b,gp),combine(outtr,BS))
            need(tr(corr)==(0,0,0) and member(corr,cs),'retained affine A4 correction')
            cocycles.append({'matrix':g,'basis_trace':i,'output_trace':outtr,'kernel_correction_numerator':corr})
    # Four time-views; twelve steps follow from T^4=C.
    frames=[[[i for i in range(24) if perm(pw(T,n))[i] in bb] for bb in B] for n in range(4)]
    def views(x):return tuple(tuple(sum(x[i] for i in bb)//4 for bb in f) for f in frames)
    def trace9(x):
        vv=views(x);return vv[0]+vv[1][:2]+vv[2][:2]+vv[3][:2]
    def unpack(a):
        total=sum(a[:3]);return (tuple(a[:3]),)+tuple((a[i],a[i+1],total-a[i]-a[i+1]) for i in (3,5,7))
    def pack(vv):return vv[0]+vv[1][:2]+vv[2][:2]+vv[3][:2]
    def t_action(a):v=unpack(a);return pack(v[1:]+(rot(v[0]),))
    need(len(LIFTS9)==9,'nine sections')
    for j,u in enumerate(LIFTS9):
        need(member(u,cs) and norm(u)==4,'nine sections are Leech minima')
        need(trace9(u)==tuple(int(i==j) for i in range(9)),'complete right-inverse matrix')
        need(views(u)==unpack(trace9(u)),'common-sum reconstruction')
        need(trace9(move(u,tp))==t_action(trace9(u)),'T equivariance on basis')
    G9=[[int(inner(x,y)) for y in LIFTS9] for x in LIFTS9]
    need(max(sum(abs(a) for a in row) for row in G9)==15,'uniform nine-section squared-norm bound')
    functionals=[tuple(2*int(i in bb) for i in range(24)) for n,f in enumerate(frames) for bb in (f if n==0 else f[:2])]
    H9=[[int(inner(x,y)) for y in functionals] for x in functionals]
    need(determinant(H9)==5292,'rank-nine trace sublattice determinant')
    corrections=[]
    for i,u in enumerate(LIFTS9):
        a=tuple(int(i==j) for j in range(9));cor=sub(move(u,tp),combine(t_action(a),LIFTS9))
        need(trace9(cor)==(0,)*9 and member(cor,cs),'rank-fifteen affine correction')
        corrections.append(cor)
    for a in [tuple((i*j+1)%7-3 for i in range(9)) for j in range(13)]:
        x=combine(a,LIFTS9);need(member(x,cs) and trace9(x)==a,'arbitrary simultaneous data')
        y=x
        for n in range(12):
            expected=views(x)[n%4]
            for _ in range(n//4):expected=rot(expected)
            need(tr(y)==expected,'complete twelve-view covariance')
            y=move(y,tp)
        need(y==x,'literal twelve-step return')
    # Retained ES markings; no new existence inferred from their lattice lifts.
    states=[
        dict(p=5,R=3,h=2,r=1,s=1,channel='E'),
        dict(p=1201,R=23,h=17,r=1,s=18,channel='E'),
        dict(p=1201,R=39,h=2,r=1,s=155,channel='M'),
        dict(p=2521,R=31,h=11,r=2,s=29,channel='M')]
    arithmetic=[]
    for st in states:
        p,R,h,r,s=(st[k] for k in ('p','R','h','r','s'));a=h*r*s;u=h*r*r
        need(4*a-p==R and 0<R<p,'retained residual')
        if st['channel']=='E':
            need((p*r+s)%R==0,'exterior quotient');q=(p*r+s)//R;triple=(a,h*s*q,p*h*r*q);qname='kappa'
        else:
            need((r+s)%R==0,'middle quotient');q=(r+s)//R;triple=(a,p*h*s*q,p*h*r*q);qname='lambda'
        x,y,z=triple
        need(4*x*y*z==p*(x*y+x*z+y*z),'original ES equation')
        ur=Q(a*a,R*y-p*a) if st['channel']=='E' else Q(p*a*a,R*y-p*a)
        need(ur==u,'divisor inverse')
        lift=shortest(triple)
        vv=(triple,rot(triple),rot(rot(triple)),triple);aa=pack(vv);joint=combine(aa,LIFTS9)
        need(member(joint,cs) and views(joint)==vv,'marked four-view arithmetic inverse')
        arithmetic.append({**st,'u':u,qname:q,'ordered_denominators':triple,'shortest_lift_numerator':lift,'shortest_norm':int(norm(lift)),'twelve_view_lift_numerator':joint,'four_views':vv})
    # An exact unsuccessful orbit, not a counterexample to ES.
    p=1201;vv=((p,p,p),)*4;bad=combine(pack(vv),LIFTS9)
    for n in range(12):
        need(tr(bad)==(p,p,p),'bad orbit keeps prescribed positive traces')
        need(4*p**3-p*(3*p*p)==p**3,'bad orbit defect')
        bad=move(bad,tp)
    # Sharp small-shell positive observation; all trace signatures are exhaustive.
    positive={t:n for t,n in hist.items() if min(t)>0}
    need(set(positive)=={(1,1,1),(2,1,1),(1,2,1),(1,1,2),(2,2,1),(2,1,2),(1,2,2)},'positive minimal shell')
    positive_data=[{'trace':t,'count':n,'prime_parameter_as_rational':str(Q(4*t[0]*t[1]*t[2],t[0]*t[1]+t[0]*t[2]+t[1]*t[2]))} for t,n in sorted(positive.items())]
    # mod-8 rule excludes the exceptional all-2 residue for odd prime inputs.
    for p in (1,3,5,7):
        for t in itertools.product((2,6),repeat=3):
            a,b,c=t;need((4*a*b*c-p*(a*b+a*c+b*c))%8==4,'222 arithmetic obstruction')
    save(out/'trace_frame.json',{'coordinate_order':'0,...,22,infinity','scale':'all vector numerators divided by sqrt(8)','octads':B,'tetrads':tetrads,'C':C,'J':J,'T':T,'frame_W':W,'linear_lifts_B':BS,'fixed_code_patterns':fixed,'A4_cocycles':cocycles,'kernel_rank':21,'kernel_determinant':64})
    save(out/'shortest_lifts.json',{'formula':'min||lambda||^2=||t||^2/4+mu(t mod4)','classes':rows,'minimal_shell_projection':[{'trace':t,'multiplicity':n} for t,n in sorted(hist.items())],'positive_minimal_shell':positive_data,'ES_defect_square_sum_coefficients':[737280,0,241920]})
    save(out/'twelve_views.json',{'meaning':'four independent time triples; remaining eight are cyclic rotations, not four distinct A4 faces','input_order':'(t00,t01,t02,t10,t11,t20,t21,t30,t31)','inverse_frame_blocks':frames,'right_inverse_numerators':LIFTS9,'right_inverse_Gram':G9,'functional_Gram':H9,'functional_determinant':5292,'kernel_rank':15,'T_affine_kernel_corrections':corrections,'unsuccessful_orbit_example':{'p':1201,'trace_each_step':[1201]*3,'defect_each_step':1201**3,'lift_numerator':combine(pack(((1201,1201,1201),)*4),LIFTS9)}})
    save(out/'arithmetic.json',arithmetic)
    result={'checks':CHECKS,'minimal_vectors':shellcount,'projection_support':len(hist),'single_trace_residue_classes':len(rows),'nine_column_right_inverse':'exact identity','T_order':12,'claims_not_checked':['universal ES existence','full Leech-lattice uniqueness proof','Lean compilation','independent review','historical novelty']}
    save(out/'summary.json',result)
    return result

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,default=Path('certificates'));args=p.parse_args()
    print(json.dumps(run(args.out),sort_keys=True))
if __name__=='__main__':main()
