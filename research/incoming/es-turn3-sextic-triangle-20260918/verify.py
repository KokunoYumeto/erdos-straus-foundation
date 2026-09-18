#!/usr/bin/env python3
"""Turn 3: a closed all-primitive-sextic ES factor triangle.
Only Python's standard library is used. Checks remain active under python -O.
This verifies a counterexample to local-cycle escape, NOT a counterexample to ES.
No search over the full nonresidue graph at the large prime is asserted.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd, isqrt, prod
from pathlib import Path
import argparse, hashlib, json

P = 113946012068401
VERTICES = (31, 223, 307)
# Inactive factors in cycle order. Every factorization is certified below.
B_FACTORS = (
    ((2, 2), (31935541499, 1)),
    ((2, 2), (17, 1), (41, 1), (33281891, 1)),
    ((19, 2), (269, 1), (937, 1), (10099, 1)),
)
K_GENERATORS = (2, 2, 4)
P_MINUS_ONE = ((2,4),(3,3),(5,2),(10550556673,1))
COEFFICIENTS = (
    (3,3,3,3,3),
    (1,3,4,4,5,5,4,3,2,3,4,3,4,5,3,3,4,4,4,4,4,4,3,3,5,4,3,4,3,2,3,4,5,5,4,4,3),
    (3,1,4,1,4,2,3,3,3,3,2,4,2,4,1,5,1,5,1,4,1,4,1,3,2,2,2,2,3,1,4,1,4,1,5,1,5,1,4,2,4,2,3,3,3,3,2,4,1,4,1),
)
CHECKS = Counter()


def require(ok: bool, label: str) -> None:
    CHECKS[label] += 1
    if not ok:
        raise ArithmeticError(label)


def dumps(value) -> str:
    return json.dumps(value, sort_keys=True, indent=2) + '\n'


def sha(value) -> str:
    return hashlib.sha256(dumps(value).encode()).hexdigest()


def trial_prime(n: int) -> dict:
    if n < 2:
        raise ValueError('positive prime required')
    if n == 2:
        return {'n':n,'method':'trial division','bound':1,'odd_divisors_tested':0}
    require(n % 2 == 1, 'trial_odd')
    bound = isqrt(n)
    for d in range(3,bound+1,2):
        require(n % d != 0, 'trial_no_divisor')
    return {'n':n,'method':'trial division','bound':bound,
            'odd_divisors_tested':max(0,(bound-1)//2)}


def legendre(a:int,p:int)->int:
    x=pow(a%p,(p-1)//2,p)
    require(x in (0,1,p-1),'Euler_character_value')
    return -1 if x==p-1 else x


def divisors_from(fs, multiplier=1):
    out=[1]
    for q,e in fs:
        out=[x*q**j for x in out for j in range(multiplier*e+1)]
    return sorted(out)


def generated(q:int, gens)->set[int]:
    known={1}; todo=[1]
    while todo:
        x=todo.pop()
        for g in gens:
            y=x*g%q
            if y not in known:
                known.add(y);todo.append(y)
    return known


def order(x:int,q:int)->int:
    a=1
    for n in range(1,q):
        a=a*x%q
        if a==1:return n
    raise ArithmeticError('order')


def frac(x:Fraction|int):
    x=Fraction(x)
    return [x.numerator,x.denominator]


def primality()->dict:
    auxiliary={q for fs in B_FACTORS for q,e in fs}|set(VERTICES)|{q for q,e in P_MINUS_ONE}
    auxiliary|={127,1949,6057173} # explicit outside ES witness
    proofs=[trial_prime(q) for q in sorted(auxiliary)]
    require(prod(q**e for q,e in P_MINUS_ONE)==P-1,'complete_p_minus_one_factorization')
    base=11
    require(pow(base,P-1,P)==1,'Lucas_Fermat')
    orders=[]
    for q,e in P_MINUS_ONE:
        residue=pow(base,(P-1)//q,P)
        g=gcd(residue-1,P)
        require(g==1,'Lucas_full_order')
        orders.append({'prime':q,'exponent':(P-1)//q,'residue':residue,'gcd':g})
    require(P%840==121,'hard_progression')
    return {'p':P,'method':'complete-order Lucas certificate','base':base,
            'p_minus_one':P_MINUS_ONE,'Fermat_residue':1,'orders':orders,
            'auxiliary_trial_certificates':proofs}


def coefficient_product(m:int, steps):
    cc=Counter({0:1})
    for z,e in steps:
        dd=Counter()
        for x,c in cc.items():
            for j in range(-e,e+1):dd[(x+j*z)%m]+=c
        cc=dd
    return [cc[j] for j in range(m)]


def node(i:int)->tuple[dict,list[dict]]:
    q=VERTICES[i];r=VERTICES[(i+1)%3];prev=VERTICES[(i-1)%3]
    bfac=B_FACTORS[i];B=prod(t**e for t,e in bfac);a=B*r
    require(4*a==P+q,'same_p_edge_equation')
    require(P<4*a<2*P and gcd(P*a,q)==1,'first_half_units')
    require(q%12==7 and legendre(q,P)==-1,'original_NR_vertex')
    K={x for x in range(1,q) if pow(x,(q-1)//6,q)==1}
    require(len(K)==(q-1)//6,'full_sixth_power_kernel_size')
    kg=K_GENERATORS[i];h=len(K)
    require(order(kg,q)==h and {pow(kg,j,q) for j in range(h)}==K,'explicit_kernel_generator')
    klog={pow(kg,j,q):j for j in range(h)}
    require(all(t%q in K for t,e in bfac),'all_inactive_factors_in_K')
    steps=[(klog[t%q],e) for t,e in bfac]
    coeff=coefficient_product(h,steps)
    require(tuple(coeff)==COEFFICIENTS[i],'published_exact_coefficient_vector')
    require(min(coeff)>0 and sum(coeff)==prod(2*e+1 for t,e in bfac),'saturated_original_inactive_box')
    cosets=[{pow(r,j,q)*k%q for k in K} for j in range(6)]
    require(len(set.union(*cosets))==q-1 and sum(map(len,cosets))==q-1,'active_quotient_generator')
    class_of={x:j for j,C in enumerate(cosets) for x in C}
    require(P%q in cosets[1] and 4%q in K,'first_phase_at_every_vertex')
    fs=tuple(sorted(bfac+((r,1),)))
    require(len(set(t for t,e in fs))==len(fs),'simple_distinct_active_prime')
    outgoing=[(t,e) for t,e in fs if legendre(t,P)==-1]
    require(outgoing==[(r,1)],'ALL_outgoing_NR_factors_exactly_successor')
    # Preserve each original word, normalization and both rational denominator records.
    mu=Counter();states=[];E=[];M=[]
    for beta in product(*(range(-e,e+1) for t,e in fs)):
        u=prod(t**(e+j) for (t,e),j in zip(fs,beta))
        v=prod(pow(t,j,q) for (t,e),j in zip(fs,beta))%q
        mu[v]+=1
        require(u*pow(a,-1,q)%q==v,'original_centering_inverse')
        d=gcd(a,u);hh=d*d//u;rr=u//d;ss=a//d
        require(hh*rr*ss==a and hh*rr*rr==u and gcd(rr,ss)==1,'original_valuation_normalization')
        kn=P*rr+ss;ln=rr+ss
        e_gate=(4*u+1)%q;m_gate=(u+a)%q
        if not e_gate:E.append(u)
        if not m_gate:M.append(u)
        xyzE=(Fraction(a),Fraction(hh*ss*kn,q),Fraction(P*hh*rr*kn,q))
        xyzM=(Fraction(a),Fraction(P*hh*ss*ln,q),Fraction(P*hh*rr*ln,q))
        for tag,xyz,num in [('E',xyzE,kn),('M',xyzM,ln)]:
            require(sum((1/x for x in xyz),Fraction())==Fraction(4,P),'full_rational_identity_'+tag)
            inv=Fraction((1 if tag=='E' else P)*a*a,1)/(q*xyz[1]-P*a)
            require(inv==u,'ordered_inverse_'+tag)
            require(num%q!=0 and any(x.denominator!=1 for x in xyz),'original_integrality_failure_'+tag)
        states.append({'p':P,'q':q,'R':q,'a':a,'u':u,'beta':list(beta),
            'h':hh,'r':rr,'s':ss,'unit_residue':v,
            'E':{'tag':'E','gate_residue':e_gate,'kappa_raw':[kn,q],'denominators':[frac(x) for x in xyzE]},
            'M':{'tag':'M','gate_residue':m_gate,'lambda_raw':[ln,q],'denominators':[frac(x) for x in xyzM]}})
    W=set(mu)
    actual_K={t for t in range(1,q) if {t*x%q for x in W}==W}
    Gamma=generated(q,[-1,2]+[t for t,e in fs])
    require(actual_K==K and len(Gamma)==q-1,'actual_full_and_effective_index_six')
    require(W==cosets[0]|cosets[1]|cosets[5],'full_support_exactly_three_cosets')
    require(not E and not M,'exhaustive_joint_channel_failure')
    targets={'M':q-1,'E_plus':(-pow(P,-1,q))%q,'E_minus':(-P)%q}
    require([class_of[targets[t]] for t in ('M','E_plus','E_minus')]==[3,2,4],'all_distinct_target_orientations')
    coarse=[sum(mu[x] for x in C) for C in cosets];T=sum(coeff)
    require(coarse==[T,T,0,0,0,T],'original_quotient_multiplicities')
    require(sum(mu.values())==3*T==len(states),'original_source_mass')
    require(all(mu[x]==mu[pow(x,-1,q)] for x in mu),'source_inversion')
    delta=pow(r,6,q)
    # Section j -> r^j and its full extension carry.
    carry=[[pow(delta,(j+k)//6,q) for k in range(6)] for j in range(6)]
    for j,k,l in product(range(6),repeat=3):
        require(carry[j][k]*carry[(j+k)%6][l]%q==carry[k][l]*carry[j][(k+l)%6]%q,'section_cocycle')
    muB={pow(kg,j,q):coeff[j] for j in range(h)}
    nu=[]
    for j in range(6):
        row=[]
        for x in sorted(K):
            fine=mu[pow(r,j,q)*x%q]
            expected=muB[x] if j in (0,1) else muB[delta*x%q] if j==5 else 0
            require(fine==expected,'fine_kernel_carry_coefficient')
            row.append([x,fine])
        nu.append(row)
    neighbor=prev*r*r%q
    roots=[x for x in range(1,q) if pow(x,6,q)==neighbor]
    require(len(roots)==6,'complete_neighbor_sixth_root_fibre')
    require(prev%q==(-P)%q and class_of[prev%q]==4,'previous_vertex_exact_forbidden_class')
    require(pow(prev,(q-1)//3,q)==pow(r,(q-1)//3,q)!=1,'matching_nontrivial_cubic_characters')
    # A homomorphic section is decided by checking every lift of class 1.
    split_lifts=[x for x in cosets[1] if pow(x,6,q)==1]
    require(bool(split_lifts)==(gcd(6,h)==1),'split_versus_non_split_extension')
    return {'q':q,'next':r,'previous':prev,'sigma':1,'R':q,'a':a,'B':B,
        'factors':fs,'inactive_factors':bfac,'outgoing':outgoing,'K':sorted(K),
        'kernel_generator':kg,'kernel_log_steps':steps,'kernel_coefficients':coeff,
        'Gamma_order':len(Gamma),'ambient_index':6,'effective_index':6,
        'mass':len(states),'support':sorted(W),'fine_counts':[[x,mu[x]] for x in sorted(mu)],
        'target_residues':targets,'target_classes':{'M':3,'E_plus':2,'E_minus':4},
        'coarse_counts':coarse,'section_base':r%q,'section_base_order':order(r,q),
        'carry_generator':delta,'carry_generator_order':order(delta,q),'carry':carry,
        'fine_section_counts':nu,'homomorphic_section_lifts':sorted(split_lifts),
        'neighbor_kernel_element':neighbor,'neighbor_sixth_roots':roots,
        'cubic_character_value':pow(r,(q-1)//3,q),'E':E,'M':M},states


def convolution(a,b):
    n=len(a);out=[0]*n
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[(i+j)%n]+=x*y
    return out


def matrix_record()->dict:
    d=[1,1,0,0,0,1]
    matrix=[[0]*3 for _ in range(2)]
    for j,c in enumerate(d):matrix[j%2][j%3]+=c
    require(matrix==[[1,0,0],[0,1,1]],'exact_parity_cubic_joint_matrix')
    sq=convolution(d,d)
    require(sq==[3,2,1,0,1,2],'doubled_packet_coefficients')
    pairs={t:[(i,j) for i in (-1,0,1) for j in (-1,0,1) if (i+j)%6==t] for t in (2,4)}
    require(pairs=={2:[(1,1)],4:[(-1,-1)]},'doubled_E_words_all_outside_original_active_box')
    # Exact integer marginal fibres, including the original inversion symmetry.
    fibre_counts=[]
    for T in range(25):
        tables=[]; symmetric=[]
        for u in range(T+1):
            for v in range(T-u+1):
                table=[[T-u-v,u,v],[u+v,T-u,T-v]]
                require([sum(row) for row in table]==[T,2*T], 'marginal_row_inverse')
                require([sum(table[i][j] for i in range(2)) for j in range(3)]==[T]*3,'marginal_column_inverse')
                cc=[table[j%2][j%3] for j in range(6)]
                require(cc[2]+cc[3]==u+2*v,'quotient_target_cell_sum_from_hidden_coordinates')
                tables.append(table)
                if all(cc[j]==cc[-j%6] for j in range(6)):
                    require(u==v,'inversion_reduces_kernel_to_one_coordinate')
                    symmetric.append(table)
        require(len(tables)==(T+1)*(T+2)//2 and len(symmetric)==T//2+1,'complete_marginal_fibre_count')
        fibre_counts.append([T,len(tables),len(symmetric)])
    require([1,1,0,0,0,1]==[x%2 for x in [1,3,2,4,2,3]],'parity_cannot_distinguish_even_positive_hidden_coordinate')
    # F2[C6] -> F2[eps]/eps^2 x F4[eps]/eps^2.
    # F4 bits: 1 -> 1, z -> 2, z^2=z+1 -> 3.
    def f4mul(a,b):
        z=0
        for i in range(2):
            for j in range(2):
                if (a>>i)&(b>>j)&1:z^=1<<(i+j)
        return z ^ (7 if z&4 else 0)
    zp=[1,2,3]
    def transform(bits):
        aa=bb=cc=dd=0
        for j in range(6):
            if bits>>j&1:
                aa^=1; bb^=j%2; cc^=zp[j%3]
                if j%2:dd^=zp[j%3]
        return (aa,bb,cc,dd)
    mapping={i:transform(i) for i in range(64)}
    require(len(set(mapping.values()))==64,'six_dimensional_mixed_algebra_inverse')
    for a,b in product(range(64),repeat=2):
        va=[a>>i&1 for i in range(6)];vb=[b>>i&1 for i in range(6)]
        v=convolution(va,vb);bits=sum((x%2)<<i for i,x in enumerate(v))
        a0,a1,a2,a3=mapping[a];b0,b1,b2,b3=mapping[b]
        want=(a0*b0,(a0*b1)^(a1*b0),f4mul(a2,b2),f4mul(a2,b3)^f4mul(a3,b2))
        require(mapping[bits]==want,'mixed_algebra_product')
    packed=sum(x<<j for j,x in enumerate(d))
    require(mapping[packed]==(1,0,0,1),'sextic_obstruction_is_one_and_epsilon')
    return {'joint_matrix_per_T':matrix,'quadratic_marginal':[1,2],'cubic_marginal':[1,1,1],
            'coarse_counts_per_T':d,'squared_counts_per_T_squared':sq,'doubled_target_fibres':pairs,
            'mixed_algebra_images':[[k,*mapping[k]] for k in range(64)],
            'sextic_packet_image':[1,0,0,1],
            'marginal_fibre_counts':fibre_counts,
            'inversion_symmetric_fibre':'[[T-2w,w,w],[2w,T-w,T-w]], 0<=2w<=T',
            'canonical_target_coset_sum_in_symmetric_fibre':'3w',
            'fine_count_nonclaim':'3w is a quotient-coset total, not generally the exact fine ES state count',
            'marginal_kernel_basis':[[[1,-1,0],[-1,1,0]],[[1,0,-1],[-1,0,1]]]}


def cycle_inverse(nodes)->dict:
    cs=[n['B'] for n in nodes];T=[]
    for start in range(3):
        D=1;z=0
        for j in range(3):z=z+D;D*=4*cs[(start+j)%3]
        T.append(z)
    D=64*prod(cs);h=gcd(*T)
    require((D-1)//h==P and (D-1)%h==0,'integral_cycle_reconstructs_p')
    require([x//h for x in T]==list(VERTICES) and all(x%h==0 for x in T),'integral_cycle_reconstructs_vertices')
    require(all(P+n['q']==4*n['B']*n['next'] for n in nodes),'closed_exact_original_states')
    p0=1396761361;mod=1782724440;t=63916
    require(P==p0+mod*t and gcd(p0,mod)==1,'recorded_CRT_discovery_parameter')
    linear=[]
    for q,r in zip(VERTICES,VERTICES[1:]+VERTICES[:1]):
        a=(p0+q)//(4*r);b=mod//(4*r)
        require(4*r*a==p0+q and 4*r*b==mod,'CRT_linear_inactive_factors')
        linear.append([a,b])
    return {'ordered_vertices':VERTICES,'cofactors':cs,'sigmas':[1,1,1],
        'D':D,'S':1,'cyclic_numerators':T,'h':h,
        'CRT':{'p0':p0,'modulus':mod,'parameter':t,'B_linear_coefficients':linear}}


def positive_returns()->list[dict]:
    # An original ES state outside the three-vertex component.
    a=(P+3)//4; fs=((19,1),(127,1),(1949,1),(6057173,1));u=1949
    require(prod(t**e for t,e in fs)==a,'outside_ES_denominator_factorization')
    def restore(a,u,tag):
        R=4*a-P;d=gcd(a,u);h=d*d//u;r=u//d;s=a//d
        require(a*a%u==0 and h*r*s==a and h*r*r==u,'positive_original_normalization')
        num=P*r+s if tag=='E' else r+s
        require(num%R==0,'positive_original_gate');c=num//R
        xyz=(a,h*s*c,P*h*r*c) if tag=='E' else (a,P*h*s*c,P*h*r*c)
        require(sum((Fraction(1,x) for x in xyz),Fraction())==Fraction(4,P),'positive_integer_ES_identity')
        require(Fraction((1 if tag=='E' else P)*a*a,R*xyz[1]-P*a)==u,'positive_ordered_inverse')
        return {'p':P,'R':R,'a':a,'u':u,'channel':tag,'h':h,'r':r,'s':s,
                'quotient':c,'ordered_denominators':xyz}
    first=restore(a,u,'E');first['a_factorization']=fs
    # The actual square-multiplier port 9 at q=31 repairs this example only.
    second=restore((P+9*31)//4,1991,'M');second['marked_multiplier']=9;second['vertex']=31
    require(legendre(9,P)==1 and 9*31<3*P,'legitimate_extra_port')
    return [first,second]


def negative_controls(nodes,mat):
    tests={
      'closed_sextic_component_must_hit':any(n['E'] or n['M'] for n in nodes),
      'effective_index_must_increase':any(nodes[(i+1)%3]['effective_index']>n['effective_index'] for i,n in enumerate(nodes)),
      'cubic_marginal_hole_detects_joint_failure':0 in mat['cubic_marginal'],
      'cartesian_product_of_marginal_supports_equals_joint':sum(bool(c) for row in mat['joint_matrix_per_T'] for c in row)==6,
      'doubled_E_target_returns_to_original_active_bound':any(abs(i+j)<=1 for i,j in mat['doubled_target_fibres'][2]),
      'third_extension_has_homomorphic_section':bool(nodes[2]['homomorphic_section_lifts']),
      'inactive_fine_counts_are_always_uniform':len(set(nodes[1]['kernel_coefficients']))==1,
      'edge_31_to_307_exists':any(r==307 for r,e in nodes[0]['outgoing']),
    }
    for name,claim in tests.items():require(not claim,'reject_'+name)
    return [{'false_claim':name,'rejected':True} for name in tests]


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--out',type=Path,default=Path('certificates'))
    args=ap.parse_args();args.out.mkdir(parents=True,exist_ok=True)
    pp=primality(); ns=[];states=[]
    for i in range(3):n,ss=node(i);ns.append(n);states.extend(ss)
    mat=matrix_record();cy=cycle_inverse(ns);es=positive_returns();neg=negative_controls(ns,mat)
    require(len(states)==855 and sum(n['mass'] for n in ns)==855,'all_three_complete_original_boxes')
    core={'p':P,'nodes':ns,'cycle':cy,'positive_returns':es}
    outputs={'primality.json':pp,'triangle.json':core,'original_states.json':states,
             'mixed_coefficients.json':mat,'negative_controls.json':neg}
    for name,data in outputs.items():(args.out/name).write_text(dumps(data))
    summary={'task':'Turn3 primitive sextic route-selection gate','p':P,'vertices':VERTICES,
        'original_divisor_vectors':len(states),'canonical_channel_tests':2*len(states),
        'local_hits':0,'ambient_indices':[6,6,6],'effective_indices':[6,6,6],
        'core_certificate_sha256':sha(core),'checks':sum(CHECKS.values()),
        'checks_by_label':dict(sorted(CHECKS.items())),'negative_controls':len(neg),
        'scope':'Three complete vertices only; no full graph or least-prime claim; no ES counterexample.'}
    (args.out/'summary.json').write_text(dumps(summary))
    print(json.dumps({k:summary[k] for k in ('checks','negative_controls','original_divisor_vectors','core_certificate_sha256')},sort_keys=True))

if __name__=='__main__':main()
