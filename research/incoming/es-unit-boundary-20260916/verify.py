#!/usr/bin/env python3
"""Actual-factor unit corrections in an Erdős--Straus boundary packet.
Python >=3.9, standard library. Explicit checks remain active under -O.
The written proof, not a finite experiment, supplies the all-k assertions.
"""
from __future__ import annotations
import argparse, importlib.util, json
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
from itertools import product
from math import gcd, isqrt, prod
from pathlib import Path

ROOT=Path(__file__).resolve().parent
CHECKS=Counter()
def check(ok,label):
    CHECKS[label]+=1
    if not ok: raise ArithmeticError(label)
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module
V=load('factor_exchange_antecedent',ROOT/'antecedent/factor_exchange.py')
R=load('relative_antecedent',ROOT/'antecedent/relative.py')

def submasks(c):
    if c<0:raise ValueError('nonnegative capacity required')
    t=c
    while True:
        yield t
        if not t:break
        t=(t-1)&c

def p2(x):return x>0 and x&(x-1)==0

def mul(a,b,degree):
    """Polynomial multiplication over F2, truncated at T^degree."""
    out=0
    while b:
        bit=b&-b;out^=a<<(bit.bit_length()-1);b-=bit
    return out&((1<<degree)-1)

def power(a,e,degree):
    out=1
    while e:
        if e&1:out=mul(out,a,degree)
        a=mul(a,a,degree);e>>=1
    return out

def xtot(a,degree):
    """The involution X <-> T+1; coordinates retained as bit polynomials."""
    out=0
    while a:
        bit=a&-a;i=bit.bit_length()-1
        for j in submasks(i):
            if j<degree:out^=1<<j
        a-=bit
    return out

def inv_T(q,d):
    if not q&1:raise ValueError('cannot invert a nonunit')
    ans=0;term=1
    for _ in range(d):ans^=term;term=mul(term,q^1,d)
    check(mul(q,ans,d)==1,'unit_inverse_full_truncated_ring')
    return ans

def cyclic(a,b):
    n=len(a)
    if len(b)!=n:raise ValueError('one cyclic coefficient space required')
    c=[0]*n
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:c[(i+j)%n]+=x*y
    return c

def polynomial_packet(logs,cs,o):
    a=[0]*o;a[0]=1
    for shift,c in zip(logs,cs):
        nxt=[0]*o
        for t in submasks(c):
            for j,x in enumerate(a):
                if x:nxt[(j+shift*t)%o]+=x
        a=nxt
    return a

@lru_cache(None)
def boundary_packet(logs,cs,o):
    if not p2(o) or len(logs)!=len(cs):raise ValueError('cyclic 2-power and matching arrays')
    nu=sum((a&-a)*c for a,c in zip(logs,cs))
    if nu<o//2 or nu>=o:return None
    d=1<<(o-nu-1).bit_length()
    if d==1:return None # old full-top theorem, not new certification
    z=nu-(o-d);U=1
    for a,c in zip(logs,cs):
        if not c:continue
        if not 0<a<o:raise ValueError('identity step cannot supply a positive nilpotent order')
        w=a&-a
        h=sum(1<<(j-w) for j in submasks(a) if w<=j<d+w)
        U=mul(U,power(h,c,d),d)
    qt=(U<<z)&((1<<d)-1);qx=xtot(qt,d)
    return nu,d,qt,qx

@lru_cache(None)
def algebra_search(logs,caps,target,o):
    if sum((a&-a)*E for a,E in zip(logs,caps))<o//2:return None
    choices=[range(min(E,(o-1)//(a&-a)),-1,-1) if a else (0,) for a,E in zip(logs,caps)]
    for cs in product(*choices):
        rec=boundary_packet(logs,cs,o)
        if rec is None:continue
        nu,d,qt,qx=rec
        low=[0]*d;low[0]=1;paths={0:(0,)*len(cs)}
        for idx,(a,E,c) in enumerate(zip(logs,caps,cs)):
            if c:continue # high coordinate already reserved; no reuse of its surplus
            prev=low;low=[0]*d;newpaths={}
            for pos,num in enumerate(prev):
                if not num:continue
                for t in range(E+1):
                    np=(pos+a*t)%d;low[np]+=num
                    if np not in newpaths:
                        vv=list(paths[pos]);vv[idx]=t;newpaths[np]=tuple(vv)
            paths=newpaths
        lower=sum(num*((qx>>((target-pos)%d))&1) for pos,num in enumerate(low))
        if lower:
            pos=next(pos for pos,num in enumerate(low) if num and ((qx>>((target-pos)%d))&1))
            return dict(selected=list(cs),weight=nu,index=d,quotient_T=qt,quotient_X=qx,
                        lower_parameters=list(paths[pos]),lower_count=lower,
                        coarse_complement=low)
    return None

@lru_cache(None)
def search(p,k,fs):
    o=1<<(k-2);m=1<<k
    for base in (3,-3):
        signs=[int(not V.inside(q,base)) for q,e in fs]
        if not any(signs):continue
        logs=[V.chart_log(-q if sign else q,k,base) for (q,e),sign in zip(fs,signs)]
        phase=V.chart_log(p,k,base)
        for pattern in V.pair_patterns(list(range(len(fs))),signs):
            for blocks in product(*(tuple(V.block_options(bl,fs,signs,logs,o)) for bl in pattern)):
                if sum(bl['coset_parity'] for bl in blocks)%2!=1:continue
                A=prod(fs[i][0]**a for bl in blocks for i,a in zip(bl['indices'],bl['offsets']))
                ds=tuple([bl['log'] for bl in blocks]+[(-phase)%o])
                caps=tuple([bl['capacity'] for bl in blocks]+[1])
                target=V.chart_log(-pow(A,-1,m),k,base)
                found=algebra_search(ds,caps,target,o)
                if found:return dict(p=p,k=k,base=base,constant=A,phase=phase,blocks=list(blocks),
                                     logs=ds,capacities=caps,target=target,certificate=found)
    return None

def parity_return(logs,cs,target,o):
    items=[]
    for i,(a,c) in enumerate(zip(logs,cs)):
        for j in range(c.bit_length()):
            if c>>j&1:items.append((i,1<<j,a*(1<<j)%o))
    suffix=[0]*(len(items)+1);suffix[-1]=1;mask=(1<<o)-1
    def rot(a,r):return ((a<<r)|(a>>(o-r)))&mask if r else a
    for i in range(len(items)-1,-1,-1):suffix[i]=suffix[i+1]^rot(suffix[i+1],items[i][2])
    if not suffix[0]>>target&1:raise ValueError('target coefficient is not odd')
    result=[0]*len(cs);path=[]
    for j,(idx,amount,step) in enumerate(items):
        no=suffix[j+1]>>target&1;yes=suffix[j+1]>>((target-step)%o)&1
        check(no^yes==1,'odd_suffix_has_unique_odd_return')
        use=int(yes);path.append((idx,amount,target,use))
        if use:result[idx]+=amount;target=(target-step)%o
    check(target==0,'odd_suffix_terminates_at_original_zero_word')
    check(all(t&~c==0 for t,c in zip(result,cs)),'returned_parameters_are_actual_submasks')
    return result,path

def inspect(cert,fs,expand=False):
    p=cert['p'];k=cert['k'];o=1<<(k-2);m=1<<k;N=p+(1<<(2*k-3))
    logs=tuple(cert['logs']);cs=tuple(cert['certificate']['selected'])
    low=cert['certificate']['lower_parameters'];target=(cert['target']-sum(a*t for a,t in zip(logs,low)))%o
    high,path=parity_return(logs,cs,target,o);ts=[a+b for a,b in zip(high,low)]
    check(all(0<=t<=E for t,E in zip(ts,cert['capacities'])),'all_returned_parameters_in_original_box')
    nu,d,qt,qx=boundary_packet(logs,cs,o)
    P=polynomial_packet(logs,cs,o)
    check(all(P[i]%2==((qx>>(i%d))&1) for i in range(o)),'full_packet_parity_equals_relative_quotient')
    even=[(P[i]-((qx>>(i%d))&1))//2 for i in range(o)]
    check(all(x>=0 for x in even),'even_layer_is_original_nonnegative_mass')
    inverse=None
    if qt&1:inverse=xtot(inv_T(qt,d),d)
    exp=[0]*len(fs)
    for block,t in zip(cert['blocks'],ts[:-1]):
        for ix,a,sig in zip(block['indices'],block['offsets'],block['steps']):exp[ix]=a+sig*t
    check(all(0<=x<=e for x,(q,e) in zip(exp,fs)),'actual_prime_exponent_availability')
    W=prod(q**v for (q,e),v in zip(fs,exp));role=ts[-1]
    check(role in (0,1) and N%W==0,'retained_role_and_actual_integer_word')
    Q=W if role==0 else N//W
    check(Q%m==m-1,'actual_cofactor_target_not_only_coarse_target')
    st=V.reconstruct(p,k,Q)
    check(F(4,p)==sum((F(1,x) for x in st['denominators']),F()),'independent_rational_ES_sum')
    result=dict(weight=nu,index=d,quotient_T=qt,quotient_X=qx,
                quotient_inverse_X=inverse,integer_packet=P,even_layer=even,
                high_parameters=high,lower_parameters=low,returned_parameters=ts,
                original_exponents=exp,word=W,role=role,suffix_path=path,state=st)
    if expand:
        high_fibres={r:[] for r in range(o)}
        for ts0 in product(*(tuple(sorted(submasks(c))) for c in cs)):
            high_fibres[sum(a*t for a,t in zip(logs,ts0))%o].append(ts0)
        parts=[]
        for residue,words in high_fibres.items():
            selected=None;remaining=list(words)
            if (qx>>(residue%d))&1:
                selected=tuple(parity_return(logs,cs,residue,o)[0]);remaining.remove(selected)
            pairs=list(zip(remaining[::2],remaining[1::2]))
            check(len(remaining)%2==0 and len(pairs)==even[residue],'actual_even_layer_pair_fibres')
            recovered=(([selected] if selected is not None else [])+[word for pair in pairs for word in pair])
            check(sorted(recovered)==words,'full_original_integer_source_partition_inverse')
            if words:parts.append(dict(residue=residue,selected_norm_word=selected,paired_even_words=pairs))
        result['complete_high_source_partition']=parts
        hits=[];occurrences=0;states=set()
        choices=[tuple(submasks(c)) if c else tuple(range(E+1)) for c,E in zip(cs,cert['capacities'])]
        for vv in product(*choices):
            if sum(a*t for a,t in zip(logs,vv))%o!=cert['target']:continue
            ee=[0]*len(fs)
            for block,t in zip(cert['blocks'],vv[:-1]):
                for ix,a,sig in zip(block['indices'],block['offsets'],block['steps']):ee[ix]=a+sig*t
            word=prod(q**v for (q,e),v in zip(fs,ee));ep=vv[-1];co=word if ep==0 else N//word
            check(co%m==m-1 and N%co==0,'every_counted_role_word_returns_original_state')
            hits.append(dict(parameters=vv,exponents=ee,word=word,role=ep,Q=co));states.add(co);occurrences+=1
        check(occurrences>=cert['certificate']['lower_count'],'integer_lower_bound_before_role_forgetting')
        check(len(states)*2>=occurrences,'forgetting_role_fibre_at_most_two')
        result['all_target_role_words']=hits
    return result

def inv_matrix(A):
    n=len(A);M=[[F(x) for x in row]+[F(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
    det=F(1)
    for j in range(n):
        ix=next((i for i in range(j,n) if M[i][j]),None)
        if ix is None:raise ValueError('singular matrix')
        if ix!=j:M[ix],M[j]=M[j],M[ix];det=-det
        v=M[j][j];det*=v;M[j]=[x/v for x in M[j]]
        for i in range(n):
            if i!=j:
                v=M[i][j]
                if v:M[i]=[x-v*y for x,y in zip(M[i],M[j])]
    return [row[n:] for row in M],det

def polynomial_tests():
    totals=Counter()
    for n in range(1,5):
        o=1<<n
        for fx in range(1,1<<o):
            ft=xtot(fx,o);nu=(ft&-ft).bit_length()-1
            check(xtot(ft,o)==fx,'X_T_coordinate_involution')
            check(fx.bit_count()>=1<<nu.bit_count(),'classical_exact_order_weight_retention')
            for v in range(1,n):
                d=1<<v
                if nu<o-d:continue
                qt=ft>>(o-d);qx=xtot(qt,d)
                repeated=sum(qx<<(j*d) for j in range(o//d))
                check(fx==repeated,'complete_relative_image_and_inverse')
                z=nu-(o-d)
                check((qt&-qt).bit_length()-1==z,'relative_kernel_order_retained')
                if z==0:
                    qi=inv_T(qt,d)
                    check(mul(qt,qi,d)==1,'unit_fibre_inverse')
                totals['relative_inputs']+=1
            totals['nonzero_polynomials']+=1
    for o in (4,8,16):
        for logs in product(range(1,o),repeat=2):
            for cs in product(range(4),repeat=2):
                nu=sum((a&-a)*c for a,c in zip(logs,cs))
                P=polynomial_packet(logs,cs,o);bits=sum((x%2)<<i for i,x in enumerate(P))
                ft=xtot(bits,o)
                check((ft==0) if nu>=o else ft and (ft&-ft).bit_length()-1==nu,'binomial_packet_exact_valuation')
                rec=boundary_packet(logs,cs,o)
                if rec:
                    _,d,qt,qx=rec;E=[(P[i]-((qx>>(i%d))&1))//2 for i in range(o)]
                    check(all(x>=0 for x in E),'integer_even_layer_nonnegative')
                    G=[(3*i+1)%4 for i in range(o)];PG=cyclic(P,G)
                    coarse=[sum(G[i] for i in range(j,o,d)) for j in range(d)]
                    q=[(qx>>i)&1 for i in range(d)];lower=cyclic(q,coarse)
                    tail=cyclic(E,G)
                    check(all(PG[t]==lower[t%d]+2*tail[t] for t in range(o)),'full_integer_convolution_lower_identity')
                    for target in range(o):
                        if bits>>target&1:
                            ts,_=parity_return(logs,cs,target,o)
                            check(sum(a*t for a,t in zip(logs,ts))%o==target,'odd_return_target')
                totals['bounded_two_step_packets']+=1
    return dict(totals)

def integral_tests():
    records=[]
    for D in (2,4,8,16):
        for h in range(1,D,2):
            a=pow(h,-1,D);b=(h*a-1)//D
            for shift in (0,D-1):
                q=[0]*D
                for i in range(h):q[(i+shift)%D]+=1
                inv=[-F(b,h)]*D
                for j in range(a):inv[(h*j)%D]+=1
                inv=inv[shift:]+inv[:shift] # multiply by X^(-shift)
                mat=[[q[(i-j)%D] for j in range(D)] for i in range(D)]
                exact,det=inv_matrix(mat)
                check(abs(det)==h,'integral_circulant_index_exact')
                check(cyclic(q,inv)==[1]+[0]*(D-1),'rational_geometric_inverse_with_original_denominator')
                check(exact==[[inv[(i-j)%D] for j in range(D)] for i in range(D)],'matrix_inverse_all_coordinates')
                for i in range(D):
                    y=[int(i==j) for j in range(D)];pre=cyclic(inv,y)
                    check(all(v.denominator==1 for v in pre)==(h==1),'ordinary_basis_vector_integral_image_test')
                    y[i]=h;pre=cyclic(inv,y)
                    check(all(v.denominator==1 for v in pre),'sum_divisible_sufficient_integer_image')
                qbits=sum((c%2)<<i for i,c in enumerate(q));qt=xtot(qbits,D)
                check(qt&1==1,'odd_geometric_polynomial_is_F2_unit')
                invbits=xtot(inv_T(qt,D),D)
                check([x%2 for x in cyclic(q,[(invbits>>j)&1 for j in range(D)])]==[1]+[0]*(D-1),'F2_inverse_cyclic_coefficients')
                records.append(dict(D=D,h=h,shift=shift,inverse_exponent=a,denominator_coefficient=b,
                                    determinant=det,quotient=q,inverse=inv,parity_inverse=invbits))
    return records

def original_metric_tests():
    D=8;o=16;q=[int(j>=3) for j in range(D)]
    C=[[q[(i-j)%D] for j in range(D)] for i in range(D)]
    Cinv,det=inv_matrix(C)
    cases=[]
    for P in ([2,2,2,1,1,1,1,1,0,0,0,1,1,1,1,1],
              [q[i%D]+2 for i in range(o)]):
        available=[j for j in range(D) if all(P[r]>0 for r in range(j,o,D))]
        weights=[sum((F(1,P[r]) for r in range(j,o,D) if P[r]>0),F()) for j in range(D)]
        gram=[[sum((C[r][i]*weights[r]*C[r][j] for r in range(D)),F()) for j in range(D)] for i in range(D)]
        fibres=[[None]*v for v in P]
        for j0 in available:
            y=[F(int(i==j0)) for i in range(D)]
            h=[sum((Cinv[i][r]*y[r] for r in range(D)),F()) for i in range(D)]
            read=[sum((C[i][r]*h[r] for r in range(D)),F()) for i in range(D)]
            check(read==y,'formal_unit_inverse_keeps_available_domain')
            amplitudes=[[read[r%D]/P[r]]*P[r] if P[r] else [] for r in range(o)]
            check(all(sum(v,F())==read[r%D] for r,v in enumerate(amplitudes)), 'canonical_actual_word_lift')
            norm=sum((x*x for fibre in amplitudes for x in fibre),F())
            form=sum((h[i]*gram[i][j]*h[j] for i in range(D) for j in range(D)),F())
            check(norm==form==weights[j0],'original_word_quotient_metric_not_reset')
        source=[[F((i+2*r)%5-2) for i in range(P[r])] for r in range(o)]
        total=F();canonical=F();remainder=F()
        for r,words in enumerate(source):
            if not words:continue
            mass=sum(words,F());avg=mass/len(words);res=[x-avg for x in words]
            total+=sum((x*x for x in words),F());canonical+=mass*mass/len(words);remainder+=sum((x*x for x in res),F())
            # Nonreference values are the full star-relation primitive.
            check(res[0]==-sum(res[1:],F()),'original_word_fibre_star_primitive')
        check(total==canonical+remainder,'original_word_metric_Pythagoras')
        cases.append(dict(original_coefficients=P,available_periodic_cosets=available,
                          quotient_weights=weights,formal_unit_index=det,transported_Gram=gram,
                          full_source_dimension=sum(P),occupied_residue_dimension=sum(bool(v) for v in P)))
    return cases

def family_envelope(k):
    if k<6:raise ValueError('family requires k>=6')
    d=1<<(k-4);o=4*d;m=1<<k
    residues=[3,pow(3,3*d-1,m),(-pow(3,5*d//2,m))%m,(-pow(3,d//2+2,m))%m]
    fs=tuple(zip(residues,(d-1,1,1,1)));phase_value=pow(3,3*d,m)
    maxima={1<<j:0 for j in range(k-2)};counts=0
    for base in (3,-3):
        signs=[int(not V.inside(q,base)) for q,e in fs]
        logs=[V.chart_log(-q if s else q,k,base) for (q,e),s in zip(fs,signs)]
        phase=V.chart_log(phase_value,k,base)
        for pattern in V.pair_patterns(list(range(4)),signs):
            for blocks in product(*(tuple(V.block_options(bl,fs,signs,logs,o)) for bl in pattern)):
                if sum(bl['coset_parity'] for bl in blocks)%2!=1:continue
                aa=[bl['log'] for bl in blocks]+[(-phase)%o]
                EE=[bl['capacity'] for bl in blocks]+[1];counts+=1
                for stride in maxima:
                    L=o//stride;mass=0
                    for a,E in zip(aa,EE):
                        delta=stride//gcd(stride,a);F0=E//delta;high=(a*delta//stride)%L
                        mass+=(high&-high)*F0
                    maxima[stride]=max(maxima[stride],mass)
                    bound=2*d+2 if stride==1 else d+1 if stride==2 else 2*d//stride if stride<=d else 0
                    check(mass<=bound and bound<L-1,'every_old_canonical_relative_pattern_fails_capacity')
    return dict(k=k,d=d,patterns=counts,maximal_mass=sorted(maxima.items()))

def family_algebra(k):
    d=1<<(k-4);o=4*d
    P=[0]*o
    for i in range(2*d):
        P[i]+=1;P[(i+3*d-1)%o]+=1
    q=[int(d-1<=i<2*d) for i in range(2*d)]
    E=[int(i<d-1) for i in range(o)]
    check(all(P[i]==q[i%(2*d)]+2*E[i] for i in range(o)),'family_nonmonomial_unit_exact_integer_identity')
    fx=sum((x%2)<<i for i,x in enumerate(P));ft=xtot(fx,o)
    check((ft&-ft).bit_length()-1==2*d,'family_exact_boundary_valuation')
    qx=sum(x<<i for i,x in enumerate(q));qt=xtot(qx,2*d)
    check(qt&1==1 and sum(q)==d+1,'family_unit_dimension_and_odd_index')
    target=7*d//2-2
    check(P[target]==1 and q[target%(2*d)]==1,'family_original_target_odd')
    check((3*d-1)+(d//2-1)==target,'family_original_word_exponent')
    # The explicit three-prime shear is an available surviving correspondence.
    a=d//2-1
    check(0<=a<=d-3,'three_prime_shear_lower_parameter_available')
    check((2+5*d//2-(d//2+2))%o==2*d,'three_prime_shear_exact_half_turn')
    for t in (0,1):
        ex=(a+2*t,t,1-t)
        check(0<=ex[0]<=d-1 and min(ex[1:])>=0 and sum(ex[1:])==1,'three_prime_shear_keeps_original_box')
        check(ex[0]-2*ex[1]==a,'three_prime_shear_inverse')
    return dict(k=k,d=d,cyclic_order=o,relative_index=2*d,quotient_unit_support=[d-1,2*d-1],
                target=target,cofactor_exponent=d//2-1,residual_exponent=d//2,
                least_word_length=d//2+1,original_packet=P if k<=8 else None)

def prime_cert(p,fac,base):
    check(prod(q**e for q,e in fac)==p-1,'p_minus_one_complete_factorization')
    for q,e in fac:check(V.prime(q),'prime_certificate_factor_trial_checked')
    check(pow(base,p-1,p)==1,'complete_order_final_power')
    powers=[]
    for q,e in fac:
        r=pow(base,(p-1)//q,p);g=gcd(r-1,p)
        check(g==1,'complete_order_each_proper_power')
        powers.append(dict(prime=q,power=r,gcd=g))
    return dict(p=p,base=base,p_minus_one=fac,proper_powers=powers,
                proof='Complete multiplicative order p-1 modulo each possible prime divisor; factor primes by trial division')

def examples():
    inputs=[(6,59,23,47,[(2,4),(3,3),(5,1),(797,1)],22),
            (7,17099,239,167,[(2,5),(3,1),(5,1),(281,1),(11065889,1)],17),
            (8,1259,223,599,[(2,6),(3,1),(7,1),(11,1),(61,1),(887,1),(3016691,1)],23)]
    out=[]
    for k,q,r,s,fac,base in inputs:
        d=1<<(k-4);m=1<<k;u=1<<(2*k-5);N=3**(d-1)*q*r*s;p=N-4*u
        for t in (q,r,s):check(V.prime(t),'actual_auxiliary_primes')
        check(len({3,q,r,s})==4,'all_actual_prime_indices_distinct')
        check((q%m,r%m,s%m)==(pow(3,3*d-1,m),-pow(3,5*d//2,m)%m,-pow(3,d//2+2,m)%m),'actual_family_residue_conditions')
        check(p%840 in V.HARD and p>2*u,'actual_hard_prime_domain')
        proof=prime_cert(p,fac,base)
        fs=tuple(sorted(((3,d-1),(q,1),(r,1),(s,1))))
        co=[z for z in V.divisors(fs) if z%m==m-1]
        Q=3**(d//2-1)*q*s;res=3**(d//2)*r
        check(co==[Q] and Q*res==N,'complete_family_unique_original_cofactor')
        check(sum(V.valuation(Q,t) for t,e in fs)==sum(V.valuation(res,t) for t,e in fs)==d//2+1,'exact_minimum_word_both_roles')
        cert=search(p,k,fs)
        check(cert is not None,'new_unit_corrected_criterion_succeeds')
        detail=inspect(cert,fs,True)
        check(detail['state']['Q']==Q,'selected_unit_return_is_unique_original_state')
        check(R.search(p,k,fs) is None and V.search_certificate(p,k,fs) is None,'preceding_canonical_full_and_relative_criteria_fail')
        out.append(dict(k=k,d=d,p=p,u=u,N=N,auxiliary_primes=[q,r,s],factorization=fs,
                        primality=proof,cofactors=co,least_word_length=d//2+1,
                        certificate=cert,returned=detail,old_capacity_envelope=family_envelope(k)))
    return out

def scan(bound):
    totals=Counter();rows=[];strict=[];new_certificates=[];oldps=set();newps=set();baseps=set();unionps=set();actualps=set();threeps=set()
    for p in V.primes_to(bound):
        if p%840 not in V.HARD:continue
        totals['hard_primes']+=1;k=4
        while p>2*(1<<(2*k-5)):
            m=1<<k;N=p+(1<<(2*k-3));fs=V.factor(N)
            # None of the certificate searches receives the actual occupancy result.
            old_aff=V.search_certificate(p,k,fs)
            old=old_aff if old_aff is not None else R.search(p,k,fs);new=search(p,k,fs)
            short=V.short_word(p,k,fs);two=V.old_two_block(p,k,fs)
            Qs=[Q for Q in V.divisors(fs) if Q%m==m-1]
            hit=bool(Qs);o=bool(old);n=bool(new);newunion=o or n
            baseline=o or short or two;union=baseline or n
            shortest=min((min(sum(V.valuation(Q,q) for q,e in fs),sum(V.valuation(N//Q,q) for q,e in fs)) for Q in Qs),default=None)
            three=shortest is not None and shortest<=3
            check(not(o or n or short or two) or hit,'full_scan_no_false_forcing')
            totals['branches']+=1;totals['original_states']+=len(Qs);totals['occupied_branches']+=hit
            for key,flag in [('prior_relative',o),('new_only',n),('relative_or_new',newunion),('prior_union',baseline),('union_with_new',union),('short_three_or_prior',three or baseline)]:totals[key+'_branches']+=flag
            if o:oldps.add(p)
            if newunion:newps.add(p)
            if baseline:baseps.add(p)
            if union:unionps.add(p)
            if hit:actualps.add(p)
            if three or baseline:threeps.add(p)
            if n:
                inspected=inspect(new,fs,False)
                check(inspected['state']['Q'] in Qs,'all_scan_returned_original_states')
                new_certificates.append(dict(certificate=new,state=inspected['state'],word=inspected['word'],role=inspected['role'],returned_parameters=inspected['returned_parameters']))
                if not o:strict.append(dict(p=p,k=k,factorization=fs,prior_union=baseline,certificate=new,state=inspected['state']))
            rows.append([p,k,N,[list(z) for z in fs],o,n,short,two,len(Qs),shortest])
            k+=1
    totals.update(prior_relative_primes=len(oldps),relative_or_new_primes=len(newps),prior_union_primes=len(baseps),
                  union_with_new_primes=len(unionps),occupied_primes=len(actualps),short_three_or_prior_primes=len(threeps))
    return dict(bound=bound,scope='all valid k>=4 dyadic fixed-seed branches of six hard classes mod840',
                totals=dict(totals),rows=rows,strict_additions=strict,new_certificates=new_certificates,
                strongest_new=[r for r in strict if not r['prior_union']],
                nonclaim='No universal ES theorem, no new overall prime verification range, no dominance over all larger-arity affine packets')

def negative_controls():
    accepted=[]
    def reject(label,fn):
        try:fn()
        except (ValueError,ArithmeticError):accepted.append(label);return
        raise ArithmeticError('negative control was accepted: '+label)
    reject('nonunit inversion',lambda:inv_T(2,8))
    P=[2,2,2,1,1,1,1,1,0,0,0,1,1,1,1,1];q=[0,0,0,1,1,1,1,1]
    reject('delete actual even surplus',lambda:check(P==q*2,'bad_even_layer_deletion'))
    reject('replace nonmonomial boundary unit by one',lambda:check(q[4]==int(4==0),'bad_unit_deletion'))
    reject('ordinary quotient is the inverse of boundary injection',lambda:check([2*x%2 for x in q]==q,'bad_quotient_inverse'))
    reject('source occurrence is a free negative prime exponent',lambda:check(-1>=0,'bad_unavailable_negative_exponent'))
    reject('odd target with wrong endpoint',lambda:parity_return((1,),(1,),3,8))
    empty=not any(Q%64==63 for Q in V.divisors(((3,3),(11,1),(13,2))))
    den=(12423,56450112,9255769024)
    check(empty and sum((F(1,x) for x in den),F())==F(4,49681),'empty_branch_has_other_original_solution')
    reject('empty branch called global counterexample',lambda:check(not empty or sum((F(1,x) for x in den),F())!=F(4,49681),'bad_empty_to_global_claim'))
    reject('parity inverse declared integral unimodular',lambda:check(abs(inv_matrix([[int((i-j)%8>=3) for j in range(8)] for i in range(8)])[1])==1,'bad_integral_unimodularity'))
    return accepted

def encode(obj):
    if isinstance(obj,F):return {'n':obj.numerator,'d':obj.denominator}
    if isinstance(obj,dict):return {str(k):encode(v) for k,v in obj.items()}
    if isinstance(obj,(list,tuple)):return [encode(x) for x in obj]
    return obj

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--out',default='generated');ap.add_argument('--bound',type=int,default=2000000);args=ap.parse_args()
    if args.bound<2:ap.error('positive finite census bound required')
    dest=Path(args.out);dest.mkdir(parents=True,exist_ok=True)
    structural=dict(polynomials=polynomial_tests(),integral_circulants=integral_tests(),original_word_metrics=original_metric_tests(),
                    family=[dict(algebra=family_algebra(k),old_envelope=family_envelope(k)) for k in range(6,14)])
    ex=examples();data=scan(args.bound);negative=negative_controls()
    results={'structural.json':structural,'examples.json':ex,'scan.json':data,'negative_controls.json':negative,
             'checks.json':dict(CHECKS)}
    for name,obj in results.items():(dest/name).write_text(json.dumps(encode(obj),indent=2,sort_keys=True)+'\n')
    print(json.dumps({'new_checks':sum(CHECKS.values()),'antecedent_checks':sum(V.CHECKS.values())+sum(R.CHECKS.values())+sum(R.V.CHECKS.values()),
                      'negative_controls':len(negative),'scan':data['totals']},sort_keys=True))
if __name__=='__main__':main()
