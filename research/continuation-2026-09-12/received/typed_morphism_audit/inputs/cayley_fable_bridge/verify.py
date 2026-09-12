#!/usr/bin/env python3
"""Exact, standard-library certificates for the Cayley--Fable comparison.
No network, random sampling, removable assertions, or third-party imports.
Run: python verify.py --out certificates
"""
from __future__ import annotations
import argparse
from collections import Counter, deque
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from math import gcd, lcm
from pathlib import Path
import hashlib
import json


def require(test: bool, message: str) -> None:
    if not test:
        raise ArithmeticError(message)


class P:
    """Sparse rational Laurent polynomials; exponents are integer tuples."""
    def __init__(self, n: int, terms=None):
        self.n = n
        self.d = {tuple(e): Q(c) for e, c in (terms or {}).items() if c}
        if any(len(e) != n for e in self.d):
            raise ValueError('wrong exponent length')
    def coerce(self, b):
        if isinstance(b, P):
            if b.n != self.n: raise ValueError('incompatible rings')
            return b
        return P(self.n, {(0,)*self.n: Q(b)})
    def __add__(self, b):
        b = self.coerce(b); d = self.d.copy()
        for e, c in b.d.items(): d[e] = d.get(e, 0) + c
        return P(self.n, d)
    __radd__ = __add__
    def __neg__(self): return P(self.n, {e:-c for e,c in self.d.items()})
    def __sub__(self,b): return self + (-self.coerce(b))
    def __rsub__(self,b): return self.coerce(b) + (-self)
    def __mul__(self,b):
        b = self.coerce(b); d = {}
        for e,c in self.d.items():
            for f,k in b.d.items():
                z = tuple(a+b for a,b in zip(e,f)); d[z] = d.get(z,0)+c*k
        return P(self.n,d)
    __rmul__ = __mul__
    def __truediv__(self,b):
        if isinstance(b,P): return self * b**(-1)
        return self * (Q(1)/Q(b))
    def __pow__(self,k):
        if k<0:
            if len(self.d)!=1: raise ValueError('negative power requires a monomial')
            e,c = next(iter(self.d.items()))
            return P(self.n,{tuple(k*a for a in e):c**k})
        a=self.coerce(1);b=self
        while k:
            if k&1:a=a*b
            b=b*b;k//=2
        return a
    def diff(self,i):
        out={}
        for e,c in self.d.items():
            if e[i]:
                f=list(e);f[i]-=1;out[tuple(f)]=c*e[i]
        return P(self.n,out)
    def __eq__(self,b):
        try:return self.d==self.coerce(b).d
        except (ValueError,TypeError):return False
    def data(self):
        return [{'powers':list(e),'coefficient':str(c)} for e,c in sorted(self.d.items())]


def variables(n):
    return [P(n,{tuple(int(i==j) for j in range(n)):1}) for i in range(n)]


def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
            -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
            +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))


def fable(u,v,w):
    h=1+u*v
    return (h**3*w+v*v*h*(4+3*u*v),
            v+3*u*h*h*w+3*u*v*v*(4+3*u*v),
            2*u-3*u*u*v-u**3*w)


def disc(a,b,c,d):
    """Discriminant of a*T^3+b*T^2+c*T+d, including binary cubics."""
    return b*b*c*c-4*a*c**3-4*b**3*d-27*a*a*d*d+18*a*b*c*d


def polynomial_checks():
    u,v,w=variables(3);F=fable(u,v,w)
    require(det3([[z.diff(i) for i in range(3)] for z in F])==-2,'Jacobian')
    h=1+u*v
    q0=1-Q(3,2)*u*v-Q(1,2)*u*u*w
    q1=(v+u*h*w+3*u*v*v)/2
    q2=h*h*w+v*v*(4+3*u*v)
    require(u*q0==F[2]/2,'binary leading coefficient')
    require(u*q1+h*q0==1,'fixed mixed coefficient')
    require(u*q2+h*q1==F[1]/2,'binary linear coefficient')
    require(h*q2==F[0],'binary constant coefficient')
    require(u*u*q2-u*h*q1+h*h*q0==1,'resultant normalization')
    require(2*h*q1-u*q2==v,'factor-chart inverse v')
    require(-4*q1*q1-2*q0*q2-12*h*q1*q1-6*h*q0*q2+9*q2==w,
            'factor-chart inverse w')
    alpha,beta,gamma=variables(3)
    Delta=16*alpha-beta**2-18*alpha*beta*gamma+beta**3*gamma+27*alpha**2*gamma**2
    require(disc(gamma/2,alpha.coerce(1),beta/2,alpha)==-Delta/4,'discriminant')
    r,d,c=variables(3)
    inv=(d**(-1),-r-d,5*d*d+3*r*d-c*d**3)
    out=fable(*inv)
    require(out==(c*r**3+r*r-r*d,2*d-3*c*r*r-4*r,c),'universal inverse')
    x,y,z=variables(3)
    require((-Q(1,4)*(x*y+x*z+y*z)+x*y*z)==(4*x*y*z-x*y-x*z-y*z)/4,
            'Cayley affine equation')
    s,t=variables(2)
    M=[[0,s*t,s*t],[s*t,0,s+t],[s*t,s+t,0]]
    require(det3(M)==2*s*s*t*t*(s+t),'homogeneous quintic determinant')
    t1,t2=variables(2);t3=4-t1-t2
    e2=t1*t2+t1*t3+t2*t3;e3=t1*t2*t3
    require(disc(Q(-1,4),t1.coerce(1),-e2/4,e3/4)
            ==((t1-t2)*(t1-t3)*(t2-t3))**2/256,'ES cubic discriminant')
    r,d=variables(2)
    alpha=-r**3/2+r*r-r*d;beta=2*d+Q(3,2)*r*r-4*r;gamma=Q(-1,2)
    DD=16*alpha-beta**2-18*alpha*beta*gamma+beta**3*gamma+27*alpha**2*gamma**2
    companion=(3*r-4)**2+16*d
    require(DD==-d*d*companion/4,'companion discriminant')
    r1,r2,r3,U,V=variables(5)
    aa=2*r1*(r2-r3);bb=r1*(r2+r3)-2*r2*r3
    cc=2*(r2-r3);dd=2*r1-r2-r3
    DD=aa*dd-bb*cc
    require(DD==4*(r2-r3)*(r1-r2)*(r1-r3),'Mobius determinant')
    P1=dd*U-bb*V;P2=-cc*U+aa*V
    cubic=P2*(P1*P1-P2*P2/4)
    require(cubic==-2*DD*(U-r1*V)*(U-r2*V)*(U-r3*V),'marked cubic transport')
    return {'formal_identity_groups':10,'Jacobian':-2,
            'quintic_discriminant':'s^2*t^2*(s+t)/4',
            'target_cubic':'gamma*U^3/2 + U^2*V + beta*U*V^2/2 + alpha*V^3',
            'companion_discriminant':'(3*r-4)^2+16*d'}


def ff(q): return str(Q(q))


def branch(alpha,beta,gamma,r):
    d=Q(3,2)*gamma*r*r+2*r+beta/2
    require(d!=0,'selected root must be simple')
    u=1/d;v=-r-d;w=5*d*d+3*r*d-gamma*d**3
    require(fable(u,v,w)==(alpha,beta,gamma),'inverse branch image')
    return {'root':ff(r),'derivative':ff(d),
            'preimage':[ff(u),ff(v),ff(w)]}


def arithmetic_checks():
    base=(Q(-1,4),Q(0),Q(0))
    points=[(Q(0),Q(0),Q(-1,4)),(Q(1),Q(-3,2),Q(13,2)),
            (Q(-1),Q(3,2),Q(13,2))]
    require(all(fable(*q)==base for q in points),'special fibre points')
    require(disc(Q(0),Q(1),Q(0),Q(-1,4))==1,'special fibre discriminant')
    rows=[]
    states=[{'p':5,'denominators':[2,4,20]},
            {'p':1201,'R':23,'channel':'E','u':17,'h':17,'r':1,'s':18,'kappa':53,
             'denominators':[306,16218,1082101]}]
    for state in states:
        p=state['p'];den=state['denominators'];tt=[Q(p,n) for n in den]
        require(sum(tt)==4 and len(set(tt))==3,'ES positive distinct roots')
        a=tt[0]*tt[1]*tt[2]/4
        b=-sum(tt[i]*tt[j] for i,j in combinations(range(3),2))/2
        c=Q(-1,2)
        branches=[branch(a,b,c,r) for r in tt]
        for r,B in zip(tt,branches):
            d=Q(B['derivative']);D=(3*r-4)**2+16*d
            other=[x for x in tt if x!=r]
            require(D==(other[0]-other[1])**2,'companion discriminant exact')
        L=lcm(*(r.denominator for r in tt));abc=[int(r*L) for r in tt]
        g=gcd(gcd(abc[0],abc[1]),abc[2]);abc=[x//g for x in abc]
        prod=lcm(*abc);p0=4*prod//gcd(4*prod,sum(abc))
        require(p0==p,'exact reciprocal primitive return')
        row=dict(state)
        rr1,rr2,rr3=tt
        mm=[[2*rr1*(rr2-rr3),rr1*(rr2+rr3)-2*rr2*rr3],
            [2*(rr2-rr3),2*rr1-rr2-rr3]]
        md=mm[0][0]*mm[1][1]-mm[0][1]*mm[1][0]
        require(md!=0,'marked Mobius invertibility')
        require(mm[0][0]/mm[1][0]==rr1,'Mobius infinity')
        require((mm[0][0]+2*mm[0][1])/(mm[1][0]+2*mm[1][1])==rr2,'Mobius plus half')
        require((mm[0][0]-2*mm[0][1])/(mm[1][0]-2*mm[1][1])==rr3,'Mobius minus half')
        base_pairs=[((Q(0),Q(1)),(Q(1),Q(0),Q(-1,4))),
                    ((Q(1),Q(-1,2)),(Q(0),Q(1),Q(1,2))),
                    ((Q(-1),Q(-1,2)),(Q(0),Q(-1),Q(1,2)))]
        ma,mb=mm[0];mc,md0=mm[1]
        transported=[]
        for ((l0,l1),(q0,q1,q2)),br in zip(base_pairs,branches):
            ln=((8/md)*(l0*md0-l1*mc),(8/md)*(-l0*mb+l1*ma))
            qn=((q0*md0*md0-q1*md0*mc+q2*mc*mc)/64,
                (-2*q0*md0*mb+q1*(md0*ma+mb*mc)-2*q2*mc*ma)/64,
                (q0*mb*mb-q1*mb*ma+q2*ma*ma)/64)
            l0,l1=ln;q0,q1,q2=qn
            require((l0*q0,l0*q1+l1*q0,l0*q2+l1*q1,l1*q2)
                    ==(c/2,Q(1),b/2,a),'full transported coefficient vector')
            require(l0*l0*q2-l0*l1*q1+l1*l1*q0==1,'transported resultant')
            uv=l0;vv=2*l1*q1-uv*q2
            wv=-4*q1*q1-2*q0*q2-12*l1*q1*q1-6*l1*q0*q2+9*q2
            require([ff(v) for v in (uv,vv,wv)]==br['preimage'],
                    'transported factor inverse equals selected Fable branch')
            # Undo the same marked matrix and both normalization scalars.
            ia,ib,ic,id0=ma/md,mb/md,mc/md,md0/md
            back_l=((md/8)*(l0*ia+l1*ic),(md/8)*(l0*ib+l1*id0))
            back_q=(64*(q0*ia*ia+q1*ia*ic+q2*ic*ic),
                    64*(2*q0*ia*ib+q1*(ia*id0+ib*ic)+2*q2*ic*id0),
                    64*(q0*ib*ib+q1*ib*id0+q2*id0*id0))
            original=base_pairs[len(transported)]
            require((back_l,back_q)==original,'full marked transport inverse')
            transported.append({'linear':[ff(v) for v in ln],
                                'quadratic':[ff(v) for v in qn],
                                'resultant':'1'})
        row['transported_factor_pairs']=transported
        row['Mobius_matrix']=[[ff(v) for v in rr] for rr in mm]
        row['Mobius_determinant']=ff(md)
        row.update({'reciprocal_roots':[ff(t) for t in tt],
                    'fable_target':[ff(a),ff(b),ff(c)],'three_branches':branches,
                    'primitive_reciprocal_triple':abc,'p0':p0})
        if state.get('channel')=='E':
            x,y,z=den;R=state['R'];uu=Q(x*x,R*y-p*x)
            require(uu==state['u'],'retained exterior inverse')
        rows.append(row)
    return {'special_target':[ff(x) for x in base],
            'special_fibre':[[ff(x) for x in q] for q in points],
            'special_discriminant':1,'marked_ES_examples':rows}


def addv(*vs):return tuple(sum(c) for c in zip(*vs))
def scale(a,v):return tuple(a*x for x in v)
def dot(v,w):return v[0]*w[0]-sum(a*b for a,b in zip(v[1:],w[1:]))


def parity(p):return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))


def solve_mod2(rows,n):
    """Rows are (bitmask,rhs). Return a deterministic solution with free bits 0."""
    piv={}
    for bits,rhs in rows:
        while bits:
            j=bits.bit_length()-1
            if j not in piv:
                piv[j]=(bits,rhs);break
            b,c=piv[j];bits^=b;rhs^=c
        else:
            require(rhs==0,'inconsistent signed lift')
    x=0
    for j in sorted(piv):
        bits,rhs=piv[j]
        if ((bits&x).bit_count()&1)^rhs: x|=1<<j
    return [(-1 if x>>i&1 else 1) for i in range(n)]


def line_checks():
    h=(1,0,0,0,0,0,0)
    e=[tuple(int(i==j) for j in range(7)) for i in range(1,7)]
    K=addv(scale(-3,h),*e);anti=scale(-1,K)
    lines={}
    for i in range(6):lines[f'E{i+1}']=e[i]
    for i,j in combinations(range(6),2):
        lines[f'L{i+1}{j+1}']=addv(h,scale(-1,e[i]),scale(-1,e[j]))
    for i in range(6):lines[f'Q{i+1}']=addv(scale(2,h),*(scale(-1,e[j]) for j in range(6) if j!=i))
    names=list(lines);vectors=list(lines.values());index={v:i for i,v in enumerate(vectors)}
    require(len(index)==27,'distinct lines')
    require(all(dot(v,v)==dot(K,v)==-1 for v in vectors),'line classes')
    require(all(sum(dot(v,w)==1 for w in vectors)==10 for v in vectors),'intersection degrees')
    tri={tuple(ids) for ids in combinations(range(27),3) if addv(*(vectors[i] for i in ids))==anti}
    require(len(tri)==45,'45 anticanonical triples')
    matrices={
      'A':[['L14','L24','L34'],['L15','L25','L35'],['L16','L26','L36']],
      'B':[['Q4','Q5','Q6'],['E4','E5','E6'],['L56','L46','L45']],
      'C':[['E1','Q1','L23'],['E2','Q2','L13'],['E3','Q3','L12']]}
    require(sorted(sum((sum(m,[]) for m in matrices.values()),[]))==sorted(names),'27-block bijection')
    coeff={}
    for M in matrices.values():
        for p in permutations(range(3)):
            ids=tuple(sorted(names.index(M[i][p[i]]) for i in range(3)))
            require(ids not in coeff,'determinant monomials unique')
            coeff[ids]=parity(p)
    A=matrices['A'];B=matrices['B'];C=matrices['C']
    for i,j,k in product(range(3),repeat=3):
        ids=tuple(sorted([names.index(C[i][k]),names.index(B[k][j]),names.index(A[j][i])]))
        require(ids not in coeff,'mixed monomial unique');coeff[ids]=-1
    require(set(coeff)==tri,'Cartan monomial / tritangent equality')
    roots=[addv(e[i],scale(-1,e[i+1])) for i in range(5)]
    roots.append(addv(h,*(scale(-1,e[j]) for j in range(3))))
    require(all(dot(r,r)==-2 and dot(K,r)==0 for r in roots),'E6 roots')
    gens=[];signed=[]
    for alpha in roots:
        g=bytes(index[addv(v,scale(dot(v,alpha),alpha))] for v in vectors)
        require(all(g[g[i]]==i for i in range(27)),'reflection involution')
        require({tuple(sorted(g[i] for i in t)) for t in tri}==tri,'tritangent permutation')
        rows=[]
        for ids,c in coeff.items():
            target=tuple(sorted(g[i] for i in ids));rhs=int(c!=coeff[target])
            rows.append((sum(1<<i for i in ids),rhs))
        signs=solve_mod2(rows,27)
        for ids,c in coeff.items():
            target=tuple(sorted(g[i] for i in ids))
            require(coeff[target]*signs[ids[0]]*signs[ids[1]]*signs[ids[2]]==c,'signed norm lift')
        gens.append(g);signed.append({'permutation':list(g),'signs':signs,
                                     'squared_signs':[signs[i]*signs[g[i]] for i in range(27)]})
    tables=[g+bytes(range(27,256)) for g in gens]
    identity=bytes(range(27));group={identity};queue=deque([identity])
    while queue:
        p=queue.popleft()
        for table in tables:
            q=p.translate(table)
            if q not in group:group.add(q);queue.append(q)
    require(len(group)==51840,'W(E6) group order')
    selected=names.index('E6');stab=[g for g in group if g[selected]==selected]
    require(len(stab)==1920,'line stabilizer order')
    pairs=[frozenset([names.index(f'L{i}6'),names.index(f'Q{i}')]) for i in range(1,6)]
    pindex={v:i for i,v in enumerate(pairs)};actions=Counter()
    for g in stab:
        perm=tuple(pindex[frozenset(g[j] for j in pair)] for pair in pairs)
        actions[perm]+=1
    require(len(actions)==120 and set(actions.values())=={16},'five-pair quotient and kernel')
    ker=[g for g in stab if all(frozenset(g[j] for j in pair)==pair for pair in pairs)]
    require(len(ker)==16 and all(all(g[g[i]]==i for i in range(27)) for g in ker), 'kernel exponent two')
    for g in ker:
        flips=sum(g[min(pair)]!=min(pair) for pair in pairs)
        require(flips%2==0,'even pair flips')
    require({g[selected] for g in group}==set(range(27)),'27-line transitivity')
    # Complete-quadrilateral degeneration: four mutually orthogonal A1 roots.
    edge_labels=[(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]
    node_roots=[addv(h,*(scale(-1,e[j]) for j,edge in enumerate(edge_labels) if i in edge))
                for i in range(1,5)]
    require(all(dot(a,b)==(-2 if i==j else 0)
                for i,a in enumerate(node_roots) for j,b in enumerate(node_roots)), '4A1 orthogonality')
    node_gens=[bytes(index[addv(v,scale(dot(v,alpha),alpha))] for v in vectors)
               for alpha in node_roots]
    ng={identity}
    for g in node_gens:
        tab=g+bytes(range(27,256));ng |= {p.translate(tab) for p in list(ng)}
    require(len(ng)==16,'4A1 reflection subgroup')
    remaining=set(range(27));orbits=[]
    while remaining:
        j=min(remaining);orb={p[j] for p in ng};remaining-=orb
        orbits.append([names[i] for i in sorted(orb)])
    require(Counter(map(len,orbits))=={4:6,1:3},'27 to nine specialization orbits')
    return {'quadrilateral_edges':edge_labels,'four_node_roots':node_roots,
            'four_node_reflection_group_order':16,'specialization_orbits':orbits,
            'basis':['h']+[f'e{i}' for i in range(1,7)],'K':K,
            'lines':lines,'matrices':matrices,
            'signed_monomials':[{'lines':[names[i] for i in ids],'coefficient':coeff[ids]}
                                for ids in sorted(coeff)],
            'simple_roots':roots,'negative_root_Gram':[[-dot(a,b) for b in roots] for a in roots],
            'signed_reflection_lifts':signed,
            'line_order':names,'W_E6_order':len(group),'line_stabilizer_order':len(stab),
            'five_pairs':[[names[i] for i in sorted(p)] for p in pairs],
            'five_pair_quotient_order':len(actions),'even_flip_kernel_order':len(ker),
            'line_orbit_partition':[1,10,16],
            'signed_lift_scope':'Individual norm-preserving lifts verified; not a claim of a split Weyl-group section.'}


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--out',default='certificates')
    args=ap.parse_args();out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    results={'polynomial':polynomial_checks(),'arithmetic':arithmetic_checks(),'lines':line_checks()}
    hashes={}
    for name,data in results.items():
        raw=(json.dumps(data,sort_keys=True,indent=2)+'\n').encode()
        (out/(name+'.json')).write_bytes(raw);hashes[name+'.json']=hashlib.sha256(raw).hexdigest()
    receipt={'status':'PASS','runtime':'Python standard library; exact rational and integer operations',
             'formal_polynomial_groups':results['polynomial']['formal_identity_groups'],
             'special_fibre_points':3,'ES_examples':2,'ES_branch_checks':6,
             'normalized_factor_transports':6,'line_classes':27,'tritangent_triples':45,'signed_reflection_lifts':6,
             'W_E6_order':51840,'stabilizer_order':1920,'quotient_order':120,'kernel_order':16,
             'certificate_sha256':hashes,
             'nonclaims':['No universal ES existence proof','No formal-prover compilation',
                          'No deformation lifting theorem for the positive integer lattice',
                          'No identification of the special Fable point with a Cayley node']}
    text=json.dumps(receipt,sort_keys=True,indent=2)+'\n'
    (out/'receipt.json').write_text(text,encoding='utf8');print(text,end='')

if __name__=='__main__':main()
