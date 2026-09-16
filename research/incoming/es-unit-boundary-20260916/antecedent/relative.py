#!/usr/bin/env python3
"""Relative norm packets and original ES divisor lifting.
Python standard library only. All checks remain active under -O.
The antecedent module is a byte copy of the supplied factor-exchange verifier.
Its maps and old baselines are reused with explicit attribution, not rediscovered.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import product, combinations_with_replacement
from math import gcd, prod, isqrt
from pathlib import Path
import importlib.util
import json

ROOT=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('antecedent_factor_exchange',ROOT/'antecedent'/'factor_exchange.py')
V=importlib.util.module_from_spec(sp);sp.loader.exec_module(V)
CHECKS=Counter()

def check(ok,label):
    CHECKS[label]+=1
    if not ok:raise ArithmeticError(label)

def p2(n):return n>0 and n&(n-1)==0

def conv(a,b):
    if len(a)!=len(b):raise ValueError('same cyclic group required')
    o=len(a);z=[0]*o
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:z[(i+j)%o]+=x*y
    return z

def quotient(a,d):
    if len(a)%d:raise ValueError('subgroup index must divide group order')
    z=[0]*d
    for i,x in enumerate(a):z[i%d]+=x
    return z

def lift(a,o):
    d=len(a)
    if o%d:raise ValueError('subgroup index must divide group order')
    return [a[i%d] for i in range(o)]

def decode_invariant(a,d):
    if len(a)%d or any(a[i]!=a[i%d] for i in range(len(a))):
        raise ValueError('not in the invariant image; reading one coset is not a general inverse')
    return a[:d]

def relatives(logs,caps,target,n,min_order=2,include_zero=False):
    """All levels, then lower digits, then deterministic capacity choice.
    Excludes the one-point subgroup (v=n), which would merely restate a hit.
    No actual fine-modulus hit is consulted by this decision routine.
    """
    o=1<<n
    if len(logs)!=len(caps) or any(E<0 for E in caps):raise ValueError('bounded original parameters')
    for v in range(0 if include_zero else 1,n):
        d=1<<v;L=o//d
        if L<min_order:continue
        strides=[d//gcd(a,d) for a in logs]
        high=[(a*s//d)%L for a,s in zip(logs,strides)]
        upper=[dict(weight=V.lowbit(a),limit=E//s) for a,E,s in zip(high,caps,strides) if a]
        if V.select_counts(n-v,upper)[0] is None:continue
        for low in product(*(range(min(s,E+1)) for s,E in zip(strides,caps))):
            diff=target-sum(a*r for a,r in zip(logs,low))
            if diff%d:continue
            items=[dict(weight=V.lowbit(a),limit=(E-r)//s,log=a,parameter=i)
                   for i,(a,E,r,s) in enumerate(zip(high,caps,low,strides)) if a and (E-r)//s]
            selected,prefixes=V.select_counts(n-v,items)
            if selected is not None:
                return dict(level=v,index=d,subgroup_order=L,strides=strides,low_digits=list(low),
                            items=items,selected=selected,prefixes=prefixes,
                            reduced_target=(diff//d)%L)
    return None

def search(p,k,fs,min_order=2):
    if k<3 or p%8!=1 or p<=2*(1<<(2*k-5)):raise ValueError('original fixed-seed domain')
    m=1<<k;o=1<<(k-2)
    for base in (3,-3):
        signs=[int(not V.inside(q,base)) for q,e in fs]
        if not any(signs):continue
        logs=[V.chart_log(-q if s else q,k,base) for (q,e),s in zip(fs,signs)]
        phase=V.chart_log(p,k,base)
        for patt in V.pair_patterns(list(range(len(fs))),signs):
            for blocks in product(*(tuple(V.block_options(bl,fs,signs,logs,o)) for bl in patt)):
                if sum(bl['coset_parity'] for bl in blocks)%2!=1:continue
                A=prod(fs[i][0]**a for bl in blocks for i,a in zip(bl['indices'],bl['offsets']))
                ds=[bl['log'] for bl in blocks]+[(-phase)%o]
                caps=[bl['capacity'] for bl in blocks]+[1]
                target=V.chart_log(-pow(A,-1,m),k,base)
                rec=relatives(ds,caps,target,k-2,min_order)
                if rec is not None:
                    return dict(p=p,k=k,base=base,constant=A,phase=phase,blocks=list(blocks),
                                logs=ds,capacities=caps,target=target,relative=rec)
    return None

def inspect(cert,fs,expand=False):
    p,k=cert['p'],cert['k'];base=cert['base'];m=1<<k;o=1<<(k-2)
    check(prod(q**e for q,e in fs)==p+(1<<(2*k-3)),'actual_factor_inventory')
    check(len({q for q,e in fs})==len(fs) and all(V.prime(q) and e>0 for q,e in fs),'actual_prime_capacities')
    blocks=cert['blocks'];A=1;seen=set();logs=[];caps=[]
    for bl in blocks:
        ids,off,steps=bl['indices'],bl['offsets'],bl['steps'];E=bl['capacity']
        check(len(ids)==len(off)==len(steps) and 1<=len(ids)<=2 and E>=0,'block_shape')
        check(len(set(ids))==len(ids) and not seen.intersection(ids),'disjoint_prime_coordinates');seen.update(ids)
        check(any(s for s in steps),'nonconstant_affine_inverse')
        gr=1
        for i,a,s in zip(ids,off,steps):
            q,e=fs[i];check(0<=a<=e and 0<=a+s*E<=e,'available_affine_endpoints')
            A*=q**a;gr=gr*pow(q,s,m)%m
        check(V.inside(gr,base),'actual_inside_step')
        lg=V.chart_log(gr,k,base);check(lg==bl['log'],'original_step_log')
        logs.append(lg);caps.append(E)
    check(not V.inside(A,base) and A==cert['constant'],'actual_outside_constant')
    s=V.chart_log(p,k,base);logs.append((-s)%o);caps.append(1)
    check(logs==cert['logs'] and caps==cert['capacities'],'phase_role_not_prime')
    target=V.chart_log(-pow(A,-1,m),k,base);check(target==cert['target'],'original_target')
    r=cert['relative'];v=r['level'];d=r['index'];L=r['subgroup_order']
    check(1<=v<k-2 and d==1<<v and L==o//d and L>=2,'proper_nontrivial_relative_subgroup')
    strides=[d//gcd(a,d) for a in logs];check(strides==r['strides'],'minimal_actual_strides')
    low=r['low_digits'];check(len(low)==len(logs),'low_digit_shape')
    check(all(0<=b<ss and b<=E for b,ss,E in zip(low,strides,caps)),'original_lower_digits')
    diff=target-sum(a*b for a,b in zip(logs,low))
    check(diff%d==0 and r['reduced_target']==diff//d%L,'quotient_target_before_lifting')
    check(len(r['items'])==len(r['selected']) and len({it['parameter'] for it in r['items']})==len(r['items']),'relative_items_shape')
    c=[0]*len(logs);bits=[];sumweight=0
    for it,ci in zip(r['items'],r['selected']):
        i=it['parameter'];lg=logs[i]*strides[i]//d%L;cap=(caps[i]-low[i])//strides[i]
        check(lg!=0 and lg==it['log'] and cap==it['limit'] and it['weight']==V.lowbit(lg),'relative_log_and_capacity')
        check(0<=ci<=cap,'selected_high_budget');c[i]=ci;sumweight+=ci*V.lowbit(lg)
        for j in range(ci.bit_length()):
            if ci>>j&1:bits.append((i,1<<j,(lg<<j)%L))
    check(sumweight==L-1,'actual_relative_top_degree')
    suffix=[0]*(len(bits)+1);suffix[-1]=1
    for i in range(len(bits)-1,-1,-1):suffix[i]=suffix[i+1]^V.rotate(suffix[i+1],bits[i][2],L)
    check(suffix[0]==(1<<L)-1,'relative_norm_parity_not_full_norm')
    coeff=[0]*L;coeff[0]=1
    for i,power,shift in bits:coeff=[coeff[t]+coeff[(t-shift)%L] for t in range(L)]
    check(all(z>0 and z%2 for z in coeff),'original_integer_high_counts')
    z=[0]*len(logs);cur=r['reduced_target']
    for i,(ind,power,shift) in enumerate(bits):
        if suffix[i+1]>>cur&1:continue
        cur=(cur-shift)%L;z[ind]+=power
        check(suffix[i+1]>>cur&1,'high_suffix_inverse')
    check(cur==0,'high_inverse_termination')
    params=[b+ss*zz for b,ss,zz in zip(low,strides,z)]
    check(all(0<=t<=E for t,E in zip(params,caps)),'original_parameter_return')
    exps=[0]*len(fs)
    for bl,t in zip(blocks,params):
        for i,a,ss in zip(bl['indices'],bl['offsets'],bl['steps']):exps[i]=a+ss*t
    W=prod(q**b for (q,e),b in zip(fs,exps));epsilon=params[-1]
    check(epsilon in (0,1) and (W*pow(p,-epsilon,m))%m==m-1,'original_role_target')
    N=p+(1<<(2*k-3));check(N%W==0,'actual_integer_divisor')
    Q=W if not epsilon else N//W
    state=V.reconstruct(p,k,Q)
    # Complete fixed-packet inverse for the selected return.
    Wback=state['Q'] if not epsilon else state['R'];back=[]
    for bl in blocks:
        vals=[]
        for i,a,ss in zip(bl['indices'],bl['offsets'],bl['steps']):
            if ss:
                num=V.valuation(Wback,fs[i][0])-a
                check(num%ss==0,'affine_inverse_divisibility');vals.append(num//ss)
        check(vals and len(set(vals))==1,'affine_inverse_agreement');back.append(vals[0])
    back.append(epsilon)
    check(back==params,'whole_parameter_inverse')
    check(all(divmod(t,ss)==(zz,b) for t,ss,zz,b in zip(back,strides,z,low)),'mixed_radix_inverse')
    result=dict(state=state,role=epsilon,physical_word=W,physical_exponents=exps,
                parameters=params,high_parameters=z,low_digits=low,selected_counts=c,
                high_coefficient_vector=coeff,packet_size=sum(coeff))
    if expand:
        words=[]
        for zz in product(*(V.submasks(ci) for ci in c)):
            tt=[b+ss*x for b,ss,x in zip(low,strides,zz)];vv=[0]*len(fs)
            for bl,t in zip(blocks,tt):
                for i,a,ss in zip(bl['indices'],bl['offsets'],bl['steps']):vv[i]=a+ss*t
            WW=prod(q**j for (q,e),j in zip(fs,vv))
            check(N%WW==0,'every_packet_word_available')
            words.append(dict(high=zz,parameters=tt,exponents=vv,word=WW,role=tt[-1],residue=WW*pow(p,-tt[-1],m)%m))
        check(len({(w['word'],w['role']) for w in words})==len(words),'packet_source_injective_with_role')
        result['all_words']=words
    return result

def supported_reduce(coefficients,modulus):
    # Dictionary keys are the receiving presence mask, including zero amplitudes.
    return {label:value%modulus for label,value in coefficients.items()}

def supported_push(coefficients,modulus):
    out={}
    for label,value in coefficients.items():
        receiving=label%modulus
        out[receiving]=out.get(receiving,0)+value
    return out

def structure_tests():
    groups=0
    for n in range(1,8):
        o=1<<n
        for v in range(n):
            d=1<<v;L=o//d;norm=[int(i%d==0) for i in range(o)]
            poly=1
            # Binary binomial expansion of T^(o-d).
            for j in range(n):
                if (o-d)>>j&1:poly=poly^V.rotate(poly,1<<j,o)
            check(poly==sum(x<<i for i,x in enumerate(norm)),'norm_equals_relative_annihilator_generator')
            for r in range(d):
                a=[int(i==r) for i in range(d)];b=lift(a,o)
                check(decode_invariant(b,d)==a,'relative_boundary_inverse')
                check(quotient(b,d)==[L*x for x in a],'ordinary_quotient_not_boundary_inverse')
                check(all(x%2==0 for x in quotient(b,d)),'receiving_supported_zero')
            testvectors=[[int(i==r) for i in range(o)] for r in range(o)]
            testvectors += [[(i*i+3*i+1)%5-2 for i in range(o)]]
            for a in testvectors:
                check(conv(norm,a)==lift(quotient(a,d),o),'norm_quotient_lift_square')
            check(conv(norm,norm)==[L*x for x in norm],'overlapping_norms_multiply_with_multiplicity')
            sparse={i:1 for i in range(0,o,d)}
            received=supported_reduce(supported_push(sparse,d),2)
            check(received=={0:0} and received!={},'supported_zero_not_absent_after_quotient')
            check(supported_reduce({0:2},2)=={0:0} and supported_reduce({},2)=={},'amplitude_reduction_preserves_presence')
            for vv in range(v+1):
                dd=1<<vv;a=[(i+1)%3 for i in range(dd)]
                check(lift(lift(a,d),o)==lift(a,o),'relative_lift_tower_not_product')
            groups+=1
    # Complete lower/high decomposition of small exponent boxes, all original points.
    strata=0
    for o in (4,8,16):
        for d in (1,2,4,8):
            if d>=o or o%d:continue
            for logs in product(range(o),repeat=2):
                stride=[d//gcd(x,d) for x in logs]
                for E in ((0,0),(1,2),(3,3),(5,2)):
                    got={}
                    for low in product(*(range(min(s,e+1)) for s,e in zip(stride,E))):
                        caps=[(e-r)//s for e,r,s in zip(E,low,stride)]
                        for z in product(*(range(c+1) for c in caps)):
                            t=tuple(r+s*j for r,s,j in zip(low,stride,z))
                            check(t not in got,'stratum_injectivity');got[t]=(low,z)
                            check(all(divmod(x,s)==(j,r) for x,s,j,r in zip(t,stride,z,low)),'stratum_exact_inverse')
                    check(len(got)==prod(e+1 for e in E),'stratum_complete_original_mass');strata+=1
    # Relative packet criterion: independent bounded-knapsack test of the scaled prefix lemma.
    profiles=0
    for n in range(1,5):
        L=1<<n
        for caps in product(range(4),repeat=n):
            items=[dict(weight=1<<j,limit=c) for j,c in enumerate(caps)]
            selected,_=V.select_counts(n,items)
            possible=any(sum(c*(1<<j) for j,c in enumerate(cc))==L-1 for cc in product(*(range(c+1) for c in caps)))
            check((selected is not None)==possible,'relative_prefix_independent_knapsack');profiles+=1
    # A proper degree without the required high-step divisibility is insufficient.
    a=[0]*8;a[0]=1
    for lg in [1]*5+[3]:a=conv(a,[int(i==0)+int(i==lg) for i in range(8)])
    check([x%2 for x in a]!=[int(i%2==0) for i in range(8)],'low_step_unit_correction_is_retained')
    return dict(relative_groups=groups,mixed_radix_profiles=strata,knapsack_profiles=profiles,
                split_zero_example=dict(original_coefficients=[[0,1],[4,1],[8,1],[12,1]],
                    quotient_over_integers=[[0,4]],quotient_reduced_mod_two=[[0,0]],
                    receiving_support=[0],external_absence_support=[],
                    ordinary_mod_two_zero_does_not_remove_original_terms=True))

def elementary_state(p,R,u,c):
    a=(p+R)//4;d=gcd(a,u);h=d*d//u;r=u//d;s=a//d
    q=(r+s)//R if c=='M' else (p*r+s)//R
    den=[a,p*h*s*q,p*h*r*q] if c=='M' else [a,h*s*q,p*h*r*q]
    check(a*a%u==0 and 4*prod(den)==p*(den[0]*den[1]+den[0]*den[2]+den[1]*den[2]),'alternate_original_ES_witness')
    return dict(p=p,R=R,u=u,a=a,h=h,r=r,s=s,quotient=q,channel=c,denominators=den)

def prime_certificate(p):
    fs=V.factor(p-1)
    check(all(V.prime(q) for q,e in fs),'prime_certificate_factors_prime')
    g=next(g for g in range(2,2000) if pow(g,p-1,p)==1 and all(gcd(pow(g,(p-1)//q,p)-1,p)==1 for q,e in fs))
    residues=[dict(q=q,residue=pow(g,(p-1)//q,p),gcd=gcd(pow(g,(p-1)//q,p)-1,p)) for q,e in fs]
    check(pow(g,p-1,p)==1 and all(r['gcd']==1 for r in residues),'complete_order_primality_certificate')
    trial_bound=isqrt(p) if p<10**12 else None
    if trial_bound is not None:check(V.prime(p),'independent_trial_primality_in_main')
    return dict(p=p,p_minus_one=fs,base=g,power=pow(g,p-1,p),proper_powers=residues,
                trial_division_through=trial_bound,proof='complete order with fully factored p-1 and trial-checked prime factors')

def principal_log(b,target,k,h):
    if not (3<=h<k and V.valuation(b-1,2)==h and target%(1<<h)==1):
        raise ValueError('principal-unit logarithm domain')
    a=0
    for r in range(h+1,k+1):
        if pow(b,a,1<<r)!=target%(1<<r):a+=1<<(r-h-1)
        check(pow(b,a,1<<r)==target%(1<<r),'principal_binary_digit_return')
    return a

def exact_one_block(k,h,b,e,M):
    m=1<<k;L=1<<(k-h)
    if not (3<=h<k and V.prime(b) and V.valuation(b-1,2)==h and e>=0 and gcd(b,M)==1):
        raise ValueError('primitive actual high-prime block')
    check(pow(b,L,m)==1 and pow(b,L//2,m)!=1,'exact_principal_unit_generator')
    coarse=[];C=0
    for t in V.divisors(V.factor(M)):
        if t%(1<<h)!=(1<<h)-1:continue
        r=principal_log(b,-pow(t,-1,m)%m,k,h)
        n=0 if e<r else 1+(e-r)//L
        C+=n;coarse.append(dict(divisor=t,first_exponent=r,count=n))
    A=len(coarse)
    check(((e+1)//L)*A<=C<=((e+L)//L)*A,'one_block_all_multiplicity_bounds')
    N=b**e*M
    direct=[Q for Q in V.divisors(tuple(sorted(((b,e),)+V.factor(M)))) if Q%m==m-1] if e else [t for t in V.divisors(V.factor(M)) if t%m==m-1]
    check(C==len(direct),'one_block_original_divisor_count')
    if e>=L-1:check((C>0)==(A>0),'one_block_uniform_lift_equivalence')
    return dict(k=k,h=h,b=b,e=e,M=M,subgroup_order=L,coarse_count=A,coarse_states=coarse,
                count=C,cofactors=direct)

def examples():
    positive=8060861761;k=6;fs=V.factor(positive+512)
    cert=search(positive,k,fs,min_order=4)
    check(cert is not None,'strict_nontrivial_relative_example')
    packet=inspect(cert,fs,True)
    check(not V.short_word(positive,k,fs) and not V.old_two_block(positive,k,fs) and V.search_certificate(positive,k,fs) is None,'all_previous_strict_example_baselines_fail')
    original=[V.reconstruct(positive,k,Q) for Q in V.divisors(fs) if Q%64==63]
    check([w['Q'] for w in original]==[45951,175423],'strict_example_complete_two_states')
    # Quotient target exists twice but a genuinely too-short block has no lift.
    negative=9331009
    small=exact_one_block(6,4,17,2,3*229*47)
    check(small['coarse_count']==2 and small['count']==0,'coarse_success_does_not_imply_lift')
    alt=elementary_state(negative,7,857,'M')
    family=[]
    for e in range(9):
        r=exact_one_block(6,4,17,e,3*53*607)
        expected=2*max(0,1+(e-2)//4)
        check(r['count']==expected,'exact_exponent_family_for_all_tested_e');family.append(r)
    for k0 in range(5,31):
        for h0,b0 in ((3,41),(4,17),(5,97)):
            if h0>=k0:continue
            L0=1<<(k0-h0)
            for j0 in (0,1,L0//2,L0-1):
                check(principal_log(b0,pow(b0,j0,1<<k0),k0,h0)==j0,'principal_log_full_inverse_fixture')
    for i in range(5):
        check(family[i+4]['count']==family[i]['count']+2,'all_multiplicity_exact_period_increment')
    big=16689143913960961;bigfs=V.factor(big+2048)
    bigcert=search(big,7,bigfs,min_order=8)
    check(bigcert is not None,'strict_eight_residue_relative_example')
    bigpacket=inspect(bigcert,bigfs,True)
    bigstates=[V.reconstruct(big,7,Q) for Q in V.divisors(bigfs) if Q%128==127]
    lengths=[sum(V.valuation(st['Q'],q) for q,e in bigfs) for st in bigstates]
    check(len(bigstates)==2 and sorted(lengths)==[5,6],'strict_example_beyond_four_prime_words')
    check(V.search_certificate(big,7,bigfs) is None and not V.old_two_block(big,7,bigfs),'large_example_full_chart_tests_fail')
    bigdata=dict(prime=prime_certificate(big),factorization=bigfs,certificate=bigcert,
                 packet=bigpacket,all_states=bigstates,cofactor_occurrence_lengths=lengths,
                 one_block=exact_one_block(7,4,17,8,3*277*2879))
    large_e=10**100+2
    large_count=2*(1+(large_e-2)//4)
    check(large_count>0,'binary_encoded_multiplicity_formula')
    return dict(positive=dict(prime=prime_certificate(positive),factorization=fs,certificate=cert,
                              packet=packet,all_states=original,one_block=exact_one_block(6,4,17,4,3*53*607)),
                negative=dict(prime=prime_certificate(negative),one_block=small,alternative=alt),
                family=family,large_strict_family=bigdata,large_exponent=dict(e=large_e,count=large_count,
                    scope='symbolic fixed residues and factorization; enormous p not expanded or asserted prime'))

def scan(bound):
    rows=[];strict=[];tot=Counter();oldp=set();newp=set();actualp=set();relativep=set()
    for p in V.primes_to(bound):
        if p%840 not in V.HARD:continue
        tot['hard_primes']+=1;k=4
        while p>2*(1<<(2*k-5)):
            N=p+(1<<(2*k-3));fs=V.factor(N)
            Qs=[Q for Q in V.divisors(fs) if Q%(1<<k)==(1<<k)-1]
            old_aff=V.search_certificate(p,k,fs)
            short=V.short_word(p,k,fs);two=V.old_two_block(p,k,fs);old=bool(old_aff) or short or two
            # The new criterion includes the old canonical class at level zero.
            rel=search(p,k,fs) if old_aff is None else None
            newcert=old_aff is not None or rel is not None
            new=old or rel is not None
            check(not new or bool(Qs),'relative_sufficient_sound_against_every_fine_row')
            if rel:
                packet=inspect(rel,fs)
                check(packet['state']['Q'] in Qs,'scan_selected_original_return')
            else:packet=None
            if Qs:actualp.add(p)
            if old:oldp.add(p)
            if new:newp.add(p)
            if newcert:relativep.add(p)
            tot['branches']+=1;tot['states']+=len(Qs);tot['actual_branches']+=bool(Qs)
            tot['old_affine_branches']+=old_aff is not None;tot['relative_class_branches']+=newcert
            tot['old_union_branches']+=old;tot['new_union_branches']+=new
            if rel and not old:
                strict.append(dict(p=p,k=k,factorization=fs,certificate=rel,packet=packet,
                                   all_states=[V.reconstruct(p,k,Q) for Q in Qs]))
            rows.append([p,k,N,list(fs),int(old_aff is not None),int(short),int(two),
                         int(newcert),len(Qs),None if rel is None else rel['relative']['subgroup_order']])
            k+=1
    tot.update(old_union_primes=len(oldp),new_union_primes=len(newp),relative_class_primes=len(relativep),actual_primes=len(actualp))
    digest=sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()
    return dict(bound=bound,scope='six hard classes modulo840, k>=4, all original valid dyadic branches; canonical affine lines plus nontrivial relative strides',
                counts=dict(tot),rows=rows,strict_added_branches=strict,additional_primes=sorted(newp-oldp),row_digest=digest)

def fair_short_three(rows):
    shortp=set();unionp=set();shortb=unionb=0
    for p,k,N,fs,oa,sh,tw,rel,actual,subgroup in rows:
        target={(1<<k)-1,(-p)%(1<<k)};m=1<<k;hit=False
        for length in (1,2,3):
            for inds in combinations_with_replacement(range(len(fs)),length):
                counts=Counter(inds)
                if any(c>fs[i][1] for i,c in counts.items()):continue
                if prod(fs[i][0] for i in inds)%m in target:
                    hit=True;break
            if hit:break
        check(not hit or actual>0,'fair_three_word_baseline_sound')
        if hit:shortb+=1;shortp.add(p)
        if hit or oa or tw:unionb+=1;unionp.add(p)
    return dict(short_three_branches=shortb,short_three_primes=len(shortp),
                union_with_previous_tests_branches=unionb,union_with_previous_tests_primes=len(unionp),
                scope='at most three actual prime occurrences in either role; independent of any socle premise',
                beyond_this_union_added_branches=0,beyond_this_union_added_primes=0)

def negative_controls():
    out=[]
    def reject(label,fn):
        try:fn()
        except (ValueError,ArithmeticError):out.append(label);return
        raise ArithmeticError('false transformation accepted: '+label)
    reject('reading coset coordinates without image test',lambda:decode_invariant([1,0,0,0,0,0,0,0],2))
    reject('ordinary quotient called boundary inverse',lambda:check(quotient(lift([1,0],8),2)==[1,0],'wrong_inverse'))
    reject('overlapping norm product called composition',lambda:check(conv(lift([1,0],8),lift([1,0],8))==lift([1,0],8),'wrong_product'))
    x=search(8060861761,6,V.factor(8060862273));bad=json.loads(json.dumps(x))
    bad['relative']['low_digits'][0]+=100
    reject('lower digit exceeds original factor capacity',lambda:inspect(bad,V.factor(8060862273)))
    bad=json.loads(json.dumps(x));bad['constant']=1
    reject('compensating affine constant discarded',lambda:inspect(bad,V.factor(8060862273)))
    bad=json.loads(json.dumps(x));bad['relative']['subgroup_order']=1
    reject('tautological singleton called nontrivial lift',lambda:inspect(bad,V.factor(8060862273)))
    reject('coarse target used without high inventory',lambda:check(exact_one_block(6,4,17,2,3*229*47)['count']>0,'wrong_coarse_lift'))
    return out

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--bound',type=int,default=2000000);ap.add_argument('--out',default='generated');args=ap.parse_args()
    if args.bound<1009:ap.error('bound must include a hard prime')
    dest=Path(args.out);dest.mkdir(parents=True,exist_ok=True)
    records={'structural.json':structure_tests(),'examples.json':examples(),'scan.json':scan(args.bound),'negative_controls.json':negative_controls()}
    records['fair_baseline.json']=fair_short_three(records['scan.json']['rows'])
    records['checks.json']=dict(new=dict(CHECKS),antecedent_invocations=dict(V.CHECKS))
    for name,obj in records.items():(dest/name).write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')
    print(json.dumps(dict(new_checks=sum(CHECKS.values()),antecedent_checks=sum(V.CHECKS.values()),scan=records['scan.json']['counts'],negative_controls=len(records['negative_controls.json'])),sort_keys=True))
if __name__=='__main__':main()
