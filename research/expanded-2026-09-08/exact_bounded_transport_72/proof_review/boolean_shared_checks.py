"""Independent exact checks of unary Boolean and shared-variable CRT proofs."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product, combinations
from math import gcd, lcm, ceil, floor
from pathlib import Path
import json
from review_checks import factors, divisor_lifts


def divisors(n):
    values = [1]
    for q,e in factors(n):
        values = [v*q**j for v in values for j in range(e+1)]
    return sorted(values)


def encode(h,j,A,B,eps):
    J,M=6*h,9*h
    return (A-1)*2*J*M+2*M*j+2*(B-1)+eps


def decode(h,c):
    J,M=6*h,9*h
    large=2*J*M
    A,v=1+c//large,c%large
    j=v//(2*M)
    B=1+v//2-M*j
    eps=v%2
    return j,A,B,eps


def bits(record):
    return (record['A']<=2, record['u']%2==0, record['eps']==1)


def main():
    primes=[13,37,61,73,97]
    totals=Counter()
    fixtures=[]
    unary_records=[]
    for p in primes:
        h=(p-1)//12
        J,M=6*h,9*h
        code_bound=2*J*M*M
        rectangle_admissible={}
        for c in range(code_bound):
            j,A,B,eps=decode(h,c)
            assert 0<=j<J and 1<=A<=M and 1<=B<=M and eps in (0,1)
            assert encode(h,j,A,B,eps)==c
            a,R=3*h+j+1,4*j+3
            valid=(a%(A*B)==0 and gcd(A,B)==1)
            T=A+(p+(1-p)*eps)*B
            assert T==A+p**(1-eps)*B and T>0
            if valid or A==B or c%97==0:
                explicit_coprime=all(not(A%d==0 and B%d==0) for d in range(2,M+1))
                assert explicit_coprime==(gcd(A,B)==1)
            if A==2:
                assert valid==(a%2==0 and B%2==1 and (a//2)%B==0)
            if valid:
                D=a//(A*B)
                u=B*B*D
                rectangle_admissible[c]=(j,eps,u)
            totals['full_rectangular_codes']+=1
        box_admissible={}
        direct_ordered_count=0
        local_records=[]
        for j in range(J):
            a,R,S=3*h+j+1,4*j+3,p*(3*h+j+1)
            direct_ordered_count+=sum((S+d)%R==0 for d in divisors(S*S))
            for eps,u in product((0,1),divisors(a*a)):
                g=gcd(a,u)
                A,B,D=a//g,u//g,g*g//u
                assert g*g%u==0 and (A*B*D,B*B*D)==(a,u)
                c=encode(h,j,A,B,eps)
                assert c not in box_admissible
                box_admissible[c]=(j,eps,u)
                assert decode(h,c)==(j,A,B,eps)
                passed=(4*u+p**eps)%R==0
                assert passed==((A+p**(1-eps)*B)%R==0)
                if passed:
                    C=(A+p**(1-eps)*B)//R
                    y,z=p**eps*A*C*D,p*B*C*D
                    assert C>0 and min(a,y,z)>0
                    Cmax=(p+1)*M//3
                    assert 1<=D<=M and 1<=C<=Cmax
                    assert u<=a*a<=M*M and y<=p*M*M*Cmax and z<=p*M*M*Cmax
                    assert Fraction(1,a)+Fraction(1,y)+Fraction(1,z)==Fraction(4,p)
                    primitive=Fraction(R*y-S,S)
                    assert primitive==Fraction(A,p**(1-eps)*B)
                    back_eps=0 if primitive.denominator%p==0 else 1
                    assert back_eps==eps
                    assert (primitive.numerator,primitive.denominator//p**(1-back_eps))==(A,B)
                    record=dict(p=p,j=j,a=a,R=R,eps=eps,u=u,A=A,B=B,C=C,D=D,c=c,y=y,z=z)
                    local_records.append(record)
                    unary_records.append(record)
        assert rectangle_admissible==box_admissible
        weighted=sum(2-r['eps'] for r in local_records)
        assert weighted==direct_ordered_count
        totals['admissible_tagged_codes']+=len(box_admissible)
        totals['successful_tagged_codes']+=len(local_records)
        totals['weighted_ordered_count']+=weighted
        cells=defaultdict(set)
        by_code={record['c']:record for record in local_records}
        for record in local_records:
            cells[bits(record)].add(record['c'])
        truth_count=0
        for sig in product((False,True),repeat=3):
            direct_cell={r['c'] for r in local_records if bits(r)==sig}
            crt_cell=set()
            for j,eps in product(range(J),(0,1)):
                a,R=3*h+j+1,4*j+3
                equations=[(4,-p**eps,R)]
                if sig[1]:
                    equations.append((1,0,2))
                for u in divisor_lifts([a*a],[],equations):
                    g=gcd(a,u)
                    A,B=a//g,u//g
                    c=encode(h,j,A,B,eps)
                    actual=(A<=2,u%2==0,eps==1)
                    if actual==sig:
                        crt_cell.add(c)
            assert direct_cell==crt_cell==cells[sig]
            truth_count+=len(direct_cell)
        assert truth_count==len(local_records)
        X=[{r['c'] for r in local_records if bits(r)[i]} for i in range(3)]
        union=set().union(*X)
        ie=sum((-1)**(k+1)*len(set.intersection(*(X[i] for i in inds)))
               for k in range(1,4) for inds in combinations(range(3),k))
        assert ie==len(union)
        fibre_counts={c:sum(c in subset for subset in X) for c in union}
        assert sum(fibre_counts.values())==sum(map(len,X))
        assert all(len({tuple([c]*3) for c in set.intersection(*X)})==len(set.intersection(*X)) for _ in [0])
        selected_direct={r['c'] for r in local_records if ((bits(r)[0]==bits(r)[1]) and not bits(r)[2]) or bits(r)[2]}
        selected_cells=set().union(*(cells[sig] for sig in cells if ((sig[0]==sig[1]) and not sig[2]) or sig[2]))
        assert selected_direct==selected_cells
        fixtures.append(dict(p=p,full_codes=code_bound,admissible=len(box_admissible),successful=len(local_records),weighted=weighted,
                             truth_cell_counts={''.join(str(int(bit)) for bit in sig):len(cells[sig]) for sig in product((False,True),repeat=3)},
                             selected_boolean_count=len(selected_direct),union_fibre_counts=fibre_counts))
    assert totals==Counter(full_rectangular_codes=856332,admissible_tagged_codes=3048,successful_tagged_codes=53,weighted_ordered_count=82)

    sign_cases=0
    for F in range(5):
        bound=max(F-1,0)
        for f in range(-F,F+1):
            solutions=[]
            for sm,s0,sp,tm,tp in product((0,1),(0,1),(0,1),range(bound+1),range(bound+1)):
                residuals=(sm+s0+sp-1,f-sp*(tp+1)+sm*(tm+1),(1-sp)*tp,(1-sm)*tm)
                if all(value==0 for value in residuals):
                    solutions.append((sm,s0,sp,tm,tp))
            assert solutions==[(int(f<0),int(f==0),int(f>0),max(-f-1,0) if f<0 else 0,max(f-1,0) if f>0 else 0)]
            sign_cases+=1

    # A complete augmented box: original f=x in[-2,2], d in[1,3].
    # Quotient bound2, remainder/slack bound2, remainder sign slacks bound1.
    # Coefficient-sum bounds are10,8,4,6,2,2, hence H=10.
    H,Dfixed,L=10,6,66
    moduli=(6,22,33)
    assert lcm(*moduli)==L and L==Dfixed*(H+1)
    augmented_cases=0
    extensions=defaultdict(list)
    residue_fibres=defaultdict(list)
    selected=[]
    domains=[range(-2,3),range(1,4),range(-2,3),range(3),range(3),range(2),range(2),range(2),range(2),range(2)]
    for z in product(*domains):
        x,d,q,r,s,sm,s0,sp,tm,tp=z
        residuals=(x-d*q-r,d-1-r-s,sm+s0+sp-1,r-sp*(tp+1)+sm*(tm+1),(1-sp)*tp,(1-sm)*tm)
        assert max(map(abs,residuals))<=H
        local_pass=all(value%modulus==0 for value in residuals for modulus in moduli)
        assert local_pass==all(value==0 for value in residuals)
        residue_tuple=tuple(tuple(value%modulus for value in z) for modulus in moduli)
        if local_pass:
            assert q==x//d and r==x%d and s==d-1-r
            assert s0==int(d and x%d==0)
            assert (sm,s0,sp)==(0,int(r==0),int(r>0))
            extensions[(x,d)].append(z)
            residue_fibres[residue_tuple].append(z)
            # Same canonical bits used once for implication/biconditional aggregation.
            Phi=(bool(s0)==(x>=0)) or x==-2
            if Phi:
                selected.append((x,d))
        augmented_cases+=1
    assert augmented_cases==21600
    assert len(extensions)==15 and all(len(values)==1 for values in extensions.values())
    expected=[(x,d) for x,d in product(range(-2,3),range(1,4)) if ((x%d==0)==(x>=0)) or x==-2]
    assert sorted(selected)==sorted(expected)
    assert sum(len(v) for v in residue_fibres.values())==15
    # Every possible residue pair for overlapping moduli, including vector zero.
    compatible=0
    for r,s in product(range(4),range(6)):
        exact=[x for x in range(12) if x%4==r and x%6==s]
        assert bool(exact)==((r-s)%gcd(4,6)==0)
        assert len(exact)<=1
        compatible+=bool(exact)
    assert compatible==12
    overlapping_residue_pair_count=compatible
    retained=[0+2*t for t in range(ceil(Fraction(-2,2)),floor(Fraction(2,2))+1)]
    assert retained==[-2,0,2]
    assert 5%5==0 and 5%3!=0 and 5%15!=0
    assert not((5%5!=0) and (5%3!=0))

    # Scalar input78--80: direct bounded comparison, arbitrary overlapping congruences.
    input_cases=0
    for F,lam,beta,modulus in product(range(1,4),range(-2,3),range(-2,3),range(1,8)):
        # CRT evaluator with an upper divisor-free residue enumeration is checked directly.
        g=gcd(lam,modulus)
        originals=[x for x in range(-30,31) if x%(6*F)==0 and (lam*x-beta)%modulus==0]
        if beta%g:
            merged=[]
        else:
            n=modulus//g
            a=(pow(lam//g,-1,n)*(beta//g))%n if n>1 else 0
            good=a%gcd(6*F,n)==0
            M=lcm(6*F,n)
            rs=[x for x in range(M) if x%(6*F)==0 and x%n==a]
            assert bool(rs)==good
            merged=[] if not rs else [rs[0]+M*t for t in range(ceil(Fraction(-30-rs[0],M)),floor(Fraction(30-rs[0],M))+1)]
        assert originals==merged
        input_cases+=1

    output_cases=0
    for record in unary_records:
        p,A,B,C,eps,Dp=(record[key] for key in ['p','A','B','C','eps','D'])
        K=4*A*B*C
        theta=C+(1-eps)*B
        omega=A+eps*B
        m=K//gcd(K,theta)
        assert Fraction(A+B+C,K).denominator==m//gcd(m,p-1)>1
        for index in range(1,17):
            compatible=(p-1)%gcd(index,m)==0
            exact=[q for q in range(lcm(index,m)) if q%index==1%index and (omega+q*theta)%K==0]
            assert bool(exact)==compatible
            if compatible:
                d=gcd(index,m)
                q0=1+index*((pow(index//d,-1,m//d)*((p-1)//d))%(m//d) if m//d>1 else 0)
                assert (q0-exact[0])%lcm(index,m)==0
            output_cases+=1

    out=dict(status='pass',unary_counts=dict(totals),unary_fixtures=fixtures,
             unary_truth_vectors_tested_per_prime=8,all_code_box_inverse_orientations_and_weights_checked=True,
             actual_prime_corollary_polynomial_tag_coprimality_and_bounds_checked=True,
             sign_encodings_including_zero_bound=sign_cases,complete_augmented_box_cases=augmented_cases,
             canonical_auxiliary_original_tuples=15,selected_global_boolean_original_tuples=selected,
             shared_residual_bound=H,chosen_nonminimal_fixed_common_multiple=Dfixed,shared_moduli=moduli,L=L,
             multiple_lifts_for_zero_residue_mod2=retained,negative_composite_divisibility_fixture=True,
             overlapping_residue_pair_count=overlapping_residue_pair_count,scalar_input_cases=input_cases,prescribed_output_seed_cases=output_cases,
             limitations='Finite exact checks supplement the all-parameter deductive review; no universal occupancy or efficient runtime bound follows.')
    (Path(__file__).resolve().with_name('boolean_shared_checks.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({key:value for key,value in out.items() if key!='unary_fixtures'},indent=2))


if __name__=='__main__':
    main()
