"""Independent canonical orchard fixture, integer arithmetic only."""
import json
from fractions import Fraction
from math import gcd
from pathlib import Path

def det(v,w): return v[0]*w[1]-v[1]*w[0]

def bezout(a,b):
    if b==0: return (1,0)
    u,v=bezout(b,a%b)
    return (v,u-(a//b)*v)

def inside(v,w,x):
    return det(v,x)>=0 and det(x,w)>=0

def main():
    p=1201
    V=(31,11)
    W=(7,24)
    qk=(23,9)
    pt=(1201,470)
    assert det(V,W)==667 and det(qk,pt)==1
    assert V[0]**2+2*V[1]**2==p+2
    assert W[0]**2+2*W[1]**2==p
    assert inside(V,W,qk) and inside(V,W,pt)
    nodes=[]
    leaves=[]
    def split(v,w):
        D=det(v,w)
        assert D>0
        if D==1:
            leaves.append(dict(v=v,w=w,determinant=D,
                               contains_first=inside(v,w,qk),contains_second=inside(v,w,pt)))
            return
        u0,v0=bezout(*v)
        assert v[0]*u0+v[1]*v0==1
        e0=(-v0,u0)
        assert det(v,e0)==1
        a0=det(w,e0)
        assert tuple(a0*v[j]+D*e0[j] for j in (0,1))==w
        r=a0%D
        k=(a0-r)//D
        e=tuple(e0[j]+k*v[j] for j in (0,1))
        z=tuple(v[j]+e[j] for j in (0,1))
        assert 1<=r<D and gcd(r,D)==1
        assert tuple(r*v[j]+D*e[j] for j in (0,1))==w
        assert tuple(D*z[j] for j in (0,1))==tuple((D-r)*v[j]+w[j] for j in (0,1))
        assert det(v,z)==1 and det(z,w)==D-r
        assert all(0<z[j]<=max(V[j],W[j]) for j in (0,1))
        A=z[0]*pt[1]-z[1]*pt[0]
        B=qk[0]*z[1]-qk[1]*z[0]
        assert tuple(A*qk[j]+B*pt[j] for j in (0,1))==z
        assert not(A>0 and B>0)
        nodes.append(dict(v=v,w=w,D=D,bezout_e0=e0,a0=a0,r=r,k=k,e=e,z=z,
                          children_determinants=[1,D-r],return_coordinates=[A,B]))
        split(v,z)
        split(z,w)
    split(V,W)
    occupied=[i for i,leaf in enumerate(leaves) if leaf['contains_first'] and leaf['contains_second']]
    assert len(occupied)==1
    assert all(leaf['contains_first']==leaf['contains_second'] for leaf in leaves)
    vertices={tuple(leaf[key]) for leaf in leaves for key in ['v','w']}
    assert (24,35) not in vertices and (13,19) not in vertices
    t_min=(p*V[1]+V[0]-1)//V[0]
    t_max=p*W[1]//W[0]
    k_max=p*V[1]//(4*V[1]-V[0])
    assert (t_min,t_max,k_max)==(427,4117,1016)
    all_returns=[]
    leaf_counts=[0]*len(leaves)
    for t in range(t_min,t_max+1):
        if gcd(p,t)!=1: continue
        k0=(-pow(p,-1,t))%t
        assert 0<k0<t
        for k in range(k0,k_max+1,t):
            q=(p*k+1)//t
            assert q*t-p*k==1
            if (q+p)%(4*k): continue
            b=(q+p)//(4*k)
            assert b>=1
            if not (inside(V,W,(q,k)) and inside(V,W,(p,t))): continue
            matching=[i for i,leaf in enumerate(leaves)
                      if inside(leaf['v'],leaf['w'],(q,k)) and inside(leaf['v'],leaf['w'],(p,t))]
            assert len(matching)==1
            leaf=matching[0]
            leaf_counts[leaf]+=1
            witness=[b*k,b*t,p*b*k*t]
            assert sum((Fraction(1,d) for d in witness),Fraction())==Fraction(4,p)
            all_returns.append(dict(q=q,k=k,t=t,b=b,tag=p,leaf_index_zero_based=leaf,
                                    witness=witness))
    assert any((ret['q'],ret['k'],ret['t'],ret['b'])==(23,9,470,34) for ret in all_returns)
    alternate=[]
    for k in range(1,k_max+1):
        b_min=(W[1]*p+W[0]*k+4*W[1]*k-1)//(4*W[1]*k)
        b_max=(V[1]*p+V[0]*k)//(4*V[1]*k)
        for b in range(b_min,b_max+1):
            q=4*b*k-p
            assert q>0 and inside(V,W,(q,k))
            if (p*k+1)%q: continue
            t=(p*k+1)//q
            if not inside(V,W,(p,t)): continue
            alternate.append((q,k,t,b))
    assert sorted(alternate)==sorted((r['q'],r['k'],r['t'],r['b']) for r in all_returns)
    out=dict(format_version=1,p=p,original_norm_p_vector=W,original_norm_p_plus_2_vector=V,
             orientation_determinant_original=-667,oriented_cone=[V,W],
             coordinate_upper_bounds=[max(V[0],W[0]),max(V[1],W[1])],
             canonical_splits=nodes,canonical_leaves=leaves,canonical_leaf_count=len(leaves),
             complete_return_enumeration=dict(tag_1_count=0,tag_1_reason='upper slope31/11<3 forces k<1',
                 tag_p_bounds=dict(t_min=t_min,t_max=t_max,k_max=k_max),tag_p_count=len(all_returns),
                 canonical_leaf_counts=leaf_counts,returns=all_returns,
                 independent_k_b_enumeration=alternate),
             supplied_return=dict(matrix=[[23,1201],[9,470]],tag=1201,b=34,
                                  witness=[306,15980,172727820],unique_leaf_index_zero_based=occupied[0],
                                  unique_leaf=leaves[occupied[0]]),
             known_empty_subcone=dict(v=[24,35],w=[13,19],is_canonical_leaf=False,
                                     reason='first boundary has second coordinate35>canonical bound24; neither boundary appears among canonical vertices'))
    here=Path(__file__).resolve().parent
    (here/'orchard_partition_fixture.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({key:out[key] for key in ['canonical_leaf_count','supplied_return']}
                     |dict(complete_tag_p_count=len(all_returns),canonical_leaf_counts=leaf_counts),indent=2))

if __name__=='__main__': main()
