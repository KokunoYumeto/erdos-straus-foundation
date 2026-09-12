#!/usr/bin/env python3
"""Exact tetrahedral marking certificates. Python 3.9+, standard library only.
Run: python verify.py --out certificates
No network, randomness, external imports, removable assertions, or prior verifier.
Finite enumerations and formal identities have separately stated scopes.
"""
from __future__ import annotations
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from math import gcd
from pathlib import Path
import argparse, hashlib, json

COUNTS = Counter()
def check(ok, message, group="exact"):
    COUNTS[group] += 1
    if not ok:
        raise ArithmeticError(message)

class P:
    """Sparse rational Laurent polynomials, exact formal identities."""
    def __init__(self, n, terms=None):
        self.n=n
        self.d={tuple(e):Q(c) for e,c in (terms or {}).items() if c}
        if any(len(e)!=n for e in self.d): raise ValueError("exponent dimension")
    def cast(self,b):
        if isinstance(b,P):
            if b.n!=self.n: raise ValueError("different polynomial rings")
            return b
        return P(self.n,{(0,)*self.n:Q(b)})
    def __add__(self,b):
        b=self.cast(b); out=self.d.copy()
        for e,c in b.d.items(): out[e]=out.get(e,0)+c
        return P(self.n,out)
    __radd__=__add__
    def __neg__(self): return P(self.n,{e:-c for e,c in self.d.items()})
    def __sub__(self,b): return self+-self.cast(b)
    def __rsub__(self,b): return self.cast(b)+-self
    def __mul__(self,b):
        b=self.cast(b);out={}
        for e,c in self.d.items():
            for f,d in b.d.items():
                k=tuple(x+y for x,y in zip(e,f));out[k]=out.get(k,0)+c*d
        return P(self.n,out)
    __rmul__=__mul__
    def __pow__(self,k):
        if k<0:
            if len(self.d)!=1: raise ValueError("inverse requires a monomial")
            e,c=next(iter(self.d.items()))
            return P(self.n,{tuple(k*x for x in e):c**k})
        ans=self.cast(1);b=self
        while k:
            if k&1:ans=ans*b
            b=b*b;k//=2
        return ans
    def __truediv__(self,b):return self*self.cast(b)**-1
    def __rtruediv__(self,b):return self.cast(b)*self**-1
    def diff(self,i):
        out={}
        for e,c in self.d.items():
            if e[i]:
                f=list(e);f[i]-=1;out[tuple(f)]=c*e[i]
        return P(self.n,out)
    def __eq__(self,b):
        try:return self.d==self.cast(b).d
        except (ValueError,TypeError):return False

def variables(n):
    return tuple(P(n,{tuple(int(i==j) for j in range(n)):1}) for i in range(n))
def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
           -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
           +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
def pmul(a,b):
    out=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out

def fable(u,v,w):
    h=1+u*v
    return (h**3*w+v*v*h*(4+3*u*v),
            v+3*u*h*h*w+3*u*v*v*(4+3*u*v),
            2*u-3*u*u*v-u**3*w)
def ab_from_rd(r,d):
    return (-r**3/2+r*r-r*d, 2*d+Q(3,2)*r*r-4*r)
def exchange_rd(r,d):return 16/r,8+16*(d-8)/r**2
def cycle(T):r,s,t=T;return s,t,r
def exchange(T):r,s,t=T;return 16/r,-4*t/r,-4*s/r

def formal_checks():
    u,v,w=variables(3);F=fable(u,v,w)
    check(det3([[f.diff(i) for i in range(3)] for f in F])==-2,"Fable Jacobian","formal")
    r,d=variables(2);a,b=ab_from_rd(r,d)
    point=(1/d,-r-d,5*d*d+3*r*d+d**3/2)
    check(fable(*point)==(a,b,Q(-1,2)),"root-derivative parametrization","formal")
    rp,dp=exchange_rd(r,d);aa,bb=ab_from_rd(rp,dp)
    check(exchange_rd(rp,dp)==(r,d),"exchange involution","formal")
    check(aa==256*a/r**4,"alpha transport","formal")
    check(bb+8==16*(b+8)/r**2,"beta transport","formal")
    check(32-2*b+a==-(r+4)*r*r*dp/16,"new derivative exceptional locus","formal")
    r,s,t=variables(3)
    check(cycle(cycle(cycle((r,s,t))))==(r,s,t),"C cubed","formal")
    check(exchange(exchange((r,s,t)))==(r,s,t),"J squared","formal")
    q=(r,s,t)
    for _ in range(3):q=exchange(cycle(q))
    check(q==(r,s,t),"(JC) cubed","formal")
    r,s=variables(2);t=4-r-s
    check(sum(exchange((r,s,t)))==4,"sum-four preservation","formal")
    dd=-(r-s)*(r-t)/4
    rr,ss,tt=exchange((r,s,t))
    check(-(rr-ss)*(rr-tt)/4==exchange_rd(r,dd)[1],"derivative transport","formal")
    alpha=r*s*t/4;beta=-(r*s+r*t+s*t)/2
    check(rr*ss*tt/4==256*alpha/r**4,"root-product transport","formal")
    check(-(rr*ss+rr*tt+ss*tt)/2==16*(beta+8)/r**2-8,"root-pair transport","formal")

def reduce_alg(a):
    a=[Q(c) for c in a]+[Q(0)]*max(0,3-len(a))
    # z^3=(8/3)z^2-(4/3)z.
    for n in range(len(a)-1,2,-1):
        c=a[n];a[n]=0;a[n-1]+=Q(8,3)*c;a[n-2]-=Q(4,3)*c
    return tuple(a[:3])
def amul(a,b):return reduce_alg(pmul(a,b))
def atrace(a):return 3*a[0]+Q(8,3)*a[1]+Q(40,9)*a[2]
def algebra_checks():
    one=(Q(1),Q(0),Q(0));zero=(Q(0),)*3
    E=[(Q(1),Q(-2),Q(3,4)),(Q(0),Q(9,4),Q(-9,8)),(Q(0),Q(-1,4),Q(3,8))]
    zvalues=[Q(0),Q(2,3),Q(2)]
    check(tuple(sum(e[j] for e in E) for j in range(3))==one,"partition of unity","algebra")
    for i,e in enumerate(E):
        for j,f in enumerate(E):
            check(amul(e,f)==(e if i==j else zero),"orthogonal idempotents","algebra")
            check(atrace(amul(e,f))==int(i==j),"trace orthogonality","algebra")
            check(sum(e[k]*zvalues[j]**k for k in range(3))==int(i==j),"CRT evaluations","algebra")
    # The marked half-units are e_i/2; no scalar merging is done.
    return {"polynomial":"z*(3*z-2)*(z-2)","affine_coordinate":"z=V/(U+V)",
            "root_labels":["infinity","1/2","-1/2"],
            "affine_values":[str(x) for x in zvalues],
            "primitive_idempotents_constant_linear_quadratic":[list(map(str,e)) for e in E],
            "trace_gram":[[int(i==j) for j in range(3)] for i in range(3)]}

def parity(perm):
    return (-1)**sum(perm[i]>perm[j] for i in range(len(perm)) for j in range(i+1,len(perm)))
def act(g,x):sign,perm=g;return tuple(sign[i]*x[perm[i]] for i in range(3))
def compose(g,h):
    s,p=g;t,q=h
    return tuple(s[i]*t[p[i]] for i in range(3)),tuple(q[p[i]] for i in range(3))
def isotope_product(unit,x,y):return tuple(unit[i]*x[i]*y[i] for i in range(3))
def root_readout(h,k):return "infinity" if k==0 else str(h/k)
def normalized_factor(H,K):
    L=[Q(K[0]),-H[0]]
    T=pmul([Q(K[1]),-H[1]],[Q(K[2]),-H[2]])
    Quad=[-2*c for c in T]
    a,b=L;c,d,e=Quad
    R=a*a*e-a*b*d+b*b*c
    check(R!=0,"simple factor resultant","pencil")
    L=[x/R for x in L];Quad=[R*x for x in Quad]
    a,b=L;c,d,e=Quad
    check(a*a*e-a*b*d+b*b*c==1,"normalized resultant","pencil")
    check(pmul(L,Quad)==[Q(0),Q(1),Q(0),Q(-1,4)],"binary product","pencil")
    src=(a,2*b*d-a*e,-4*d*d-2*c*e-12*b*d*d-6*b*c*e+9*e)
    check(fable(*src)==(Q(-1,4),Q(0),Q(0)),"normalized source inverse","pencil")
    return L,Quad,src

def pencil_checks():
    H0=(Q(1,2),Q(1,2),Q(-1,2));K0=(Q(0),Q(1),Q(1))
    signs=[s for s in product((-1,1),repeat=3) if s[0]*s[1]*s[2]==1]
    even=[p for p in permutations(range(3)) if parity(p)==1]
    G=[(s,p) for s in signs for p in even]
    check(len(G)==12,"A4 order","group")
    for g,h in product(G,repeat=2):check(compose(g,h) in G,"group closure","group")
    faces=sorted(set(act(g,H0) for g in G));check(len(faces)==4,"four numerator faces","group")
    face_perms=[]
    for g in G:
        fp=tuple(faces.index(act(g,H)) for H in faces);face_perms.append(fp)
        check(parity(fp)==1,"even tetrahedron permutation","group")
    check(len(set(face_perms))==12,"faithful A4 face action","group")
    basis=[tuple(Q(int(i==j)) for j in range(3)) for i in range(3)]
    for H in faces:
        unit=tuple(-2*h for h in H)
        check(unit[0]*unit[1]*unit[2]==1,"unit norm","isotopes")
        for x in basis:
            check(isotope_product(unit,unit,x)==x,"isotope unit law","isotopes")
        for g in G:
            newunit=act(g,unit)
            for x,y in product(basis,repeat=2):
                check(act(g,isotope_product(unit,x,y))==isotope_product(newunit,act(g,x),act(g,y)),
                      "complete bilinear isotope equivariance","isotopes")
    for i,H in enumerate(faces):
        check(H[0]*H[1]*H[2]==Q(-1,8),"intrinsic cubic numerator level","group")
        for j,J in enumerate(faces):
            check(sum(a*b for a,b in zip(H,J))==Q(int(i==j))-Q(1,4),"tetrahedral Gram","group")
    B=[[Q(int(i==j))-Q(1,4) for j in range(4)] for i in range(4)]
    for i in range(4):
        for j in range(4):
            check(sum(B[i][k]*B[k][j] for k in range(4))==B[i][j],"centered projection","group")
        centroid=[sum(B[k][j] for k in range(4) if k!=i)/3 for j in range(4)]
        check(centroid==[Q(-1,4) if j==i else Q(1,12) for j in range(4)],"opposite face centroid","group")
    records=[]
    for g in G:
        H=act(g,H0);K=act(g,K0);L,Quad,src=normalized_factor(H,K)
        records.append({"face":faces.index(H),"signs":g[0],"permutation":g[1],
                        "numerator":list(map(str,H)),"denominator":list(map(str,K)),
                        "observed_slot":0,"observed_root":root_readout(H[0],K[0]),
                        "normalized_L":list(map(str,L)),"normalized_Q":list(map(str,Quad)),
                        "Fable_preimage":list(map(str,src))})
    check(len({(tuple(r['numerator']),tuple(r['denominator'])) for r in records})==12,"12 distinct pencils","pencil")
    for f in range(4):
        check(Counter(r['observed_root'] for r in records if r['face']==f)==Counter(["infinity","1/2","-1/2"]),"three roots per face","pencil")
    preimages=Counter(tuple(r['Fable_preimage']) for r in records)
    check(sorted(preimages.values())==[4,4,4],"four lifts per Fable preimage","pencil")
    full=[]
    for s in signs:
        for p in permutations(range(3)):
            H=act((s,p),H0);K=act((s,p),K0)
            full.append((H,K,root_readout(H[0],K[0])))
    check(len(set(full))==24,"24 unoriented pencils","pencil")
    for H in faces:
        for label in ["infinity","1/2","-1/2"]:
            check(sum(h==H and r==label for h,k,r in full)==2,"two orientation lifts","pencil")
    return {"description":"An enlarged marked pencil space, not a fourth root of the fixed cubic",
            "rotation_group_order":12,"full_tetrahedral_group_order":24,
            "faces":list(map(lambda x:list(map(str,x)),faces)),"records":records,
            "centered_tetrahedron_projection":[list(map(str,row)) for row in B],
            "fibre_counts": {"pencils":12,"faces":4,"fixed_Fable_preimages":3,"pencils_per_Fable_preimage":4}}

def point_from_root(alpha,beta,r):
    d=-Q(3,4)*r*r+2*r+beta/2
    check(d!=0,"nonzero root derivative","atlas")
    src=(1/d,-r-d,5*d*d+3*r*d+d**3/2)
    check(fable(*src)==(alpha,beta,Q(-1,2)),"Fable face branch","atlas")
    return d,src

def atlas_checks():
    states=[
        dict(p=5,R=3,channel="E",u=2,h=2,r=1,s=1,kappa=2,denominators=[2,4,20]),
        dict(p=1201,R=23,channel="E",u=17,h=17,r=1,s=18,kappa=53,denominators=[306,16218,1082101]),
        dict(p=2521,R=31,channel="M",u=44,h=11,r=2,s=29,lam=1,denominators=[638,804199,55462])]
    out=[]
    for st in states:
        p=st['p'];x,y,z=st['denominators'];a=(Q(-1,4),Q(x,p),Q(y,p),Q(z,p))
        check(sum(1/v for v in a)==0,"Cayley torus","atlas")
        check(len(set(a))==4 and all(a),"atlas nondegeneracy","atlas")
        faces=[]
        for i in range(4):
            scale=-1/(4*a[i]);normalized=tuple(scale*t for t in a)
            rr={j:-4*a[i]/a[j] for j in range(4) if j!=i}
            roots=list(rr.values());check(sum(roots)==4,"face root sum","atlas")
            check(all(r!=0 and r!=-4 for r in roots) and len(set(roots))==3,"simple marked face","atlas")
            alpha=roots[0]*roots[1]*roots[2]/4
            beta=-sum(roots[j]*roots[k] for j,k in combinations(range(3),2))/2
            P0=Q(1)
            for v in a:P0*=v
            check(alpha==-16*a[i]**4/P0,"common-coordinate alpha","atlas")
            check(beta==-8*a[i]**3*(sum(a)-a[i])/P0,"common-coordinate beta","atlas")
            check(tuple(v/scale for v in normalized)==a,"normalized chart inverse","atlas")
            branches=[]
            for j,r in rr.items():
                d,src=point_from_root(alpha,beta,r)
                # Unique even ordering (i,j,k,l) completes an oriented face flag.
                k,l=[q for q in range(4) if q not in (i,j)]
                if parity((i,j,k,l))<0:k,l=l,k
                oriented=(rr[j],rr[k],rr[l])
                new=exchange(oriented)
                expected=(-4*a[j]/a[i],-4*a[j]/a[l],-4*a[j]/a[k])
                check(new==expected,"oriented reversal with companion swap","atlas")
                dd,src2=point_from_root(new[0]*new[1]*new[2]/4,
                       -sum(new[m]*new[n] for m,n in combinations(range(3),2))/2,new[0])
                check((new[0],dd)==exchange_rd(r,d),"root-derivative exchange","atlas")
                gamma=(3*r-4)**2+16*d
                check(gamma==(rr[k]-rr[l])**2,"retained companion discriminant","atlas")
                check(new[1]-new[2]==4*(rr[k]-rr[l])/r,"oriented square-root sign","atlas")
                branches.append({"root_label":j,"oriented_labels":[i,j,k,l],"root":str(r),"derivative":str(d),
                   "companion_difference":str(rr[k]-rr[l]),"Fable_preimage":list(map(str,src)),
                   "reversed_root_derivative":[str(new[0]),str(dd)],"reversed_Fable_preimage":list(map(str,src2))})
            check((beta<0)==(i==0),"physical versus mixed-sign charts","atlas")
            faces.append({"mark":i,"normalizing_scale":str(scale),"normalized_cayley":list(map(str,normalized)),
                          "roots":{str(j):str(r) for j,r in rr.items()},
                          "target":[str(alpha),str(beta),"-1/2"],"branches":branches})
        check(len({tuple(row['target']) for row in faces})==4,"four distinct arithmetic targets","atlas")
        R=st['R'];u0=Q(x*x,R*y-p*x)*(p if st['channel']=='M' else 1)
        check(u0.denominator==1 and u0==st['u'],"ordered selector inverse","atlas")
        D=gcd(x,int(u0));r=int(u0)//D;s=x//D;h=Q(D,r)
        check((h,r,s)==(st['h'],st['r'],st['s']),"selector gcd normalization","atlas")
        check(4*h*r*s-p==R and h*r*r==u0,"selector shell and divisor","atlas")
        if st['channel']=='E':
            kap=Q(p*r+s,R)
            check(kap==st['kappa'] and (h*r*s,h*s*kap,p*h*r*kap)==(x,y,z),"exterior reconstruction","atlas")
        else:
            lam=Q(r+s,R)
            check(lam==st['lam'] and (h*r*s,p*h*s*lam,p*h*r*lam)==(x,y,z),"middle reconstruction","atlas")
        out.append({"state":st,"original_cayley":list(map(str,a)),"faces":faces})
    return {"scope":"All four charts and twelve factor branches for each listed state; not a prime census",
            "states":out}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,default=Path('certificates'))
    args=parser.parse_args();args.out.mkdir(parents=True,exist_ok=True)
    formal_checks();A=algebra_checks();P0=pencil_checks();AT=atlas_checks()
    payloads={'orthogonal_algebra.json':A,'tetrahedral_pencils.json':P0,'cayley_atlas.json':AT}
    hashes={}
    for name,data in payloads.items():
        raw=(json.dumps(data,indent=2,sort_keys=True)+'\n').encode()
        (args.out/name).write_bytes(raw);hashes[name]=hashlib.sha256(raw).hexdigest()
    receipt={'result':'PASS','runtime':'Python standard library only',
       'check_counts_by_scope':dict(sorted(COUNTS.items())),
       'total_exact_conditions':sum(COUNTS.values()),'certificate_sha256':hashes,
       'scope':{'formal':'Laurent-polynomial coefficient identities',
         'algebra':'Complete three-dimensional quotient algebra CRT and trace checks',
         'group':'All 144 products in the 12-element rotation group',
         'pencil':'All 12 oriented and 24 orientation-unrestricted pencil lifts',
         'atlas':'36 marked face/root states over three listed ES witnesses'},
       'nonclaims':['No universal ES construction','No fourth preimage of the fixed Fable map',
          'No RH zero-location theorem','No independence or novelty claim','No Lean build']}
    (args.out/'receipt.json').write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
    print(json.dumps(receipt,indent=2,sort_keys=True))
if __name__=='__main__':main()
