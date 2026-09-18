#!/usr/bin/env python3
"""Separate direct-divisor/trial-primality check of the Turn 3 triangle.
Imports no research verifier. Standard library only. No full graph scan.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd,isqrt,prod
from pathlib import Path
import argparse,hashlib,json

P=113946012068401
QS=(31,223,307)
BS=(((2,2),(31935541499,1)),
    ((2,2),(17,1),(41,1),(33281891,1)),
    ((19,2),(269,1),(937,1),(10099,1)))
COUNT=Counter()
DIVISIONS=0

def chk(v,label):
    COUNT[label]+=1
    if not v:raise ArithmeticError(label)

def prime(n):
    global DIVISIONS
    chk(n>=2,'prime_domain')
    if n==2:return
    chk(n%2==1,'odd_prime')
    for d in range(3,isqrt(n)+1,2):
        DIVISIONS+=1
        if n%d==0:raise ArithmeticError(('composite',n,d))

def jac(a,n):
    sign=1;a%=n
    while a:
        while not a%2:
            a//=2
            if n%8 in (3,5):sign=-sign
        a,n=n,a
        if a%4==n%4==3:sign=-sign
        a%=n
    return sign if n==1 else 0

def expand(fs,power=1):
    z=[1]
    for t,e in fs:z=[u*t**f for u in z for f in range(power*e+1)]
    return z

def normalized_json(x):return json.dumps(x,sort_keys=True,indent=2)+'\n'

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--input',type=Path,default=Path('certificates'))
    ap.add_argument('--out',type=Path,default=Path('independent.json'))
    args=ap.parse_args()
    C=json.loads((args.input/'triangle.json').read_text())
    rows=json.loads((args.input/'original_states.json').read_text())
    all_primes={P,*QS,127,1949,6057173,10550556673,5}
    all_primes|={r for fs in BS for r,e in fs}
    for n in sorted(all_primes):prime(n)
    chk(P%840==121,'hard_class')
    summaries=[]
    for i,q in enumerate(QS):
        r=QS[(i+1)%3];prev=QS[i-1]
        B=prod(t**e for t,e in BS[i]);a=B*r
        fs=sorted(BS[i]+((r,1),));ds=sorted(expand(fs,2))
        chk(4*a==P+q and q<P,'actual_edge')
        chk(jac(q,P)==-1 and q%12==7,'true_NR_vertex')
        out=[(t,e) for t,e in fs if jac(t,P)==-1]
        chk(out==[(r,1)],'complete_factor_closure')
        hitsE=[u for u in ds if (4*u+1)%q==0]
        hitsM=[u for u in ds if (u+a)%q==0]
        chk(not hitsE and not hitsM,'complete_direct_divisor_failure')
        m=Counter(u*pow(a,-1,q)%q for u in ds);W=set(m)
        # No assumed power-residue subgroup is used to compute this stabilizer.
        K={t for t in range(1,q) if all(t*w%q in W for w in W)}
        expectedK={pow(t,6,q) for t in range(1,q)}
        chk(K==expectedK,'actual_stabilizer_is_sixth_powers')
        chk((q-1)//len(K)==6,'ambient_index')
        gamma={1};todo=[1]
        while todo:
            x=todo.pop()
            for g in [-1,2]+[t for t,e in fs]:
                y=x*g%q
                if y not in gamma:gamma.add(y);todo.append(y)
        chk(gamma==set(range(1,q)),'effective_equals_ambient_group')
        mb=Counter(u*pow(B,-1,q)%q for u in expand(BS[i],2))
        chk(set(mb)==K,'original_inactive_saturation')
        cosets=[{pow(r,j,q)*t%q for t in K} for j in range(6)]
        cls={x:j for j,ss in enumerate(cosets) for x in ss}
        chk(len(cls)==q-1,'all_six_cosets')
        node=C['nodes'][i]
        chk(node['q']==q and node['B']==B and node['a']==a,'certificate_original_integers')
        chk(node['factors']==[list(z) for z in fs] and node['inactive_factors']==[list(z) for z in BS[i]],'certificate_factorization')
        chk(node['outgoing']==[list(z) for z in out],'certificate_all_edges')
        chk(node['K']==sorted(K) and node['Gamma_order']==q-1,'certificate_group_sizes')
        chk(node['support']==sorted(W) and node['fine_counts']==[[t,m[t]] for t in sorted(m)],'certificate_ALL_fine_counts')
        targets={'M':q-1,'E_plus':(-pow(P,-1,q))%q,'E_minus':(-P)%q}
        chk(node['target_residues']==targets,'certificate_fine_targets')
        chk({c:cls[t] for c,t in targets.items()}=={'M':3,'E_plus':2,'E_minus':4},'joint_target_classes')
        chk([sum(m[x] for x in ss) for ss in cosets]==node['coarse_counts'],'quotient_multiplicities')
        kg=node['kernel_generator'];hp=len(K)
        chk({pow(kg,j,q) for j in range(hp)}==K,'kernel_generator_without_log_table')
        chk([mb[pow(kg,j,q)] for j in range(hp)]==node['kernel_coefficients'],'all_published_kernel_coefficients')
        delta=pow(r,6,q)
        chk(node['carry_generator']==delta,'carry_generator')
        for j,k in product(range(6),repeat=2):
            actual=pow(r,j,q)*pow(r,k,q)*pow(pow(r,(j+k)%6,q),-1,q)%q
            chk(actual==node['carry'][j][k],'all_section_multiplication_carries')
        for j in range(6):
            chk(node['fine_section_counts'][j]==[[t,m[pow(r,j,q)*t%q]] for t in sorted(K)],'fine_section_array')
        roots=[z for z in range(1,q) if pow(z,6,q)==prev*r*r%q]
        chk(roots==node['neighbor_sixth_roots'] and len(roots)==6,'actual_sixth_root_fibre')
        chk(pow(prev,(q-1)//3,q)==pow(r,(q-1)//3,q)!=1,'cubic_neighbor_recurrence')
        chk(node['homomorphic_section_lifts']==sorted(x for x in cosets[1] if pow(x,6,q)==1),'section_exceptional_locus')
        selected=[x for x in rows if x['q']==q]
        chk(sorted(x['u'] for x in selected)==ds and len(selected)==len(ds),'complete_original_state_list')
        for row in selected:
            u=row['u'];beta=row['beta'];dd=gcd(a,u);hh=dd*dd//u;rr=u//dd;ss=a//dd
            chk(row['p']==P and row['a']==a and row['R']==q,'state_marking')
            chk(prod(t**(e+z) for (t,e),z in zip(fs,beta))==u and all(-e<=z<=e for (t,e),z in zip(fs,beta)),'state_beta_inverse')
            chk((row['h'],row['r'],row['s'])==(hh,rr,ss),'state_coprime_normalization')
            for tag in ('E','M'):
                expected=(Fraction(a),(P*a+Fraction(a*a,u))/q,(P*a+P*P*u)/Fraction(q)) if tag=='E' else (Fraction(a),P*(a+Fraction(a*a,u))/q,Fraction(P*(a+u),q))
                recorded=tuple(Fraction(*v) for v in row[tag]['denominators'])
                chk(recorded==expected,'independent_factor_pair_denominators')
                chk(sum((1/x for x in recorded),Fraction())==Fraction(4,P),'state_exact_rational_identity')
                chk(row[tag]['gate_residue']==((4*u+1)%q if tag=='E' else (u+a)%q)!=0,'state_actual_gate')
        summaries.append({'q':q,'mass':len(ds),'support':len(W),'K_size':len(K),'outside':r})
    cy=C['cycle'];D=64*prod(n['B'] for n in C['nodes']);TS=[]
    for i in range(3):
        c0=C['nodes'][i]['B'];c1=C['nodes'][(i+1)%3]['B']
        TS.append(1+4*c0+16*c0*c1)
    h=gcd(*TS)
    chk(TS==cy['cyclic_numerators'] and D==cy['D'],'independent_three_cycle_formula')
    chk(P*h==D-1 and [t//h for t in TS]==list(QS),'cycle_integer_inverse')
    for rec in C['positive_returns']:
        a,u,R=rec['a'],rec['u'],rec['R'];tag=rec['channel']
        chk(R==4*a-P and a*a%u==0,'real_ES_return_domain')
        yy=(P*a+Fraction(a*a,u))/R if tag=='E' else P*(a+Fraction(a*a,u))/R
        zz=Fraction(P*a+P*P*u,R) if tag=='E' else Fraction(P*(a+u),R)
        chk(yy.denominator==zz.denominator==1,'real_ES_integrality')
        chk([a,int(yy),int(zz)]==rec['ordered_denominators'],'real_ES_ordered_denominators')
        chk(Fraction(1,a)+1/yy+1/zz==Fraction(4,P),'real_ES_identity')
    mat=json.loads((args.input/'mixed_coefficients.json').read_text())
    chk(mat['joint_matrix_per_T']==[[1,0,0],[0,1,1]],'parity_cubic_exact_matrix')
    chk(mat['cubic_marginal']==[1,1,1] and mat['quadratic_marginal']==[1,2],'nonempty_marginals_not_joint_occupancy')
    result={'method':'Independent direct divisors, Jacobi characters, literal group translates, complete trial primality',
            'p':P,'p_trial_bound':isqrt(P),'prime_trial_odd_divisions_total':DIVISIONS,
            'independent_checks':sum(COUNT.values()),'checks_by_label':dict(sorted(COUNT.items())),
            'nodes':summaries,'original_vectors':sum(x['mass'] for x in summaries),
            'input_core_sha256':hashlib.sha256(normalized_json(C).encode()).hexdigest(),
            'scope':'All three component vertices and all listed original states; no full large-p graph or leastness claim.'}
    args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(normalized_json(result))
    print(json.dumps({k:result[k] for k in ('independent_checks','prime_trial_odd_divisions_total','original_vectors','input_core_sha256')},sort_keys=True))

if __name__=='__main__':main()
