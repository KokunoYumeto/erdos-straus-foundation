#!/usr/bin/env python3
"""Exact affine-factor exchange and ES top-socle certificates.

Python >= 3.9; standard library. Explicit checks remain active under -O.
Theorems are in core.tex; finite runs do not prove universal ES occupancy.
The factor/cofactor normalization and dyadic prefix routine retain the attribution
of the pinned actual-factor-socle predecessor. No imported code is executed.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import product, combinations_with_replacement
from math import gcd, isqrt, prod, comb
from pathlib import Path
import json

CHECKS=Counter()
HARD={1,121,169,289,361,529}

def check(test: bool,label: str)->None:
    CHECKS[label]+=1
    if not test:raise ArithmeticError(label)

def primes_to(n: int)->list[int]:
    if n<2:return []
    a=bytearray(b'\1')*(n+1);a[:2]=b'\0\0'
    for q in range(2,isqrt(n)+1):
        if a[q]:a[q*q::q]=b'\0'*len(a[q*q::q])
    return [i for i in range(2,n+1) if a[i]]

TRIAL=primes_to(10000)
@lru_cache(None)
def factor(n: int)->tuple[tuple[int,int],...]:
    if n<1:raise ValueError('positive integer required')
    original=n;out=[]
    for q in TRIAL:
        if q*q>n:break
        e=0
        while n%q==0:n//=q;e+=1
        if e:out.append((q,e))
    else:
        q=TRIAL[-1]+2
        while q*q<=n:
            e=0
            while n%q==0:n//=q;e+=1
            if e:out.append((q,e))
            q+=2
    if n>1:out.append((n,1))
    check(prod(q**e for q,e in out)==original,'factorization_product')
    return tuple(out)

def prime(n: int)->bool:return n>=2 and factor(n)==((n,1),)
def valuation(n: int,q: int)->int:
    if n<=0 or q<2:raise ValueError('positive value, prime base')
    e=0
    while n%q==0:n//=q;e+=1
    return e

def divisors(fs):
    result=[1]
    for q,e in fs:result=[d*q**i for d in result for i in range(e+1)]
    return sorted(result)

def inside(q: int,base: int)->bool:
    if base==3:return q%8 in (1,3)
    if base==-3:return q%8 in (1,5)
    raise ValueError('base must be 3 or -3')

@lru_cache(None)
def log3(q: int,k: int)->int:
    if k<3 or q%8 not in (1,3):raise ValueError('actual cyclic chart required')
    q%=1<<k;a=int(q%8==3)
    for r in range(4,k+1):
        if pow(3,a,1<<r)!=q%(1<<r):a+=1<<(r-3)
    check(pow(3,a,1<<k)==q,'binary_logarithm_inverse')
    return a

def chart_log(q: int,k: int,base: int)->int:
    if not inside(q,base):raise ValueError('outside selected cyclic chart')
    a=log3(q if q%8 in (1,3) else -q,k)
    check(pow(base,a,1<<k)==q%(1<<k),'chart_return')
    return a

def lowbit(a: int)->int:return a&-a

def select_counts(n: int,items):
    """Each item is a nonidentity cyclic log with its actual block capacity."""
    o=1<<n
    if n<1 or any(not 0<it['weight']<o or it['weight']&(it['weight']-1)
                   or it['limit']<0 for it in items):
        raise ValueError('proper powers of two and nonnegative capacities required')
    prefixes=[{'level':j,'available':sum(it['weight']*it['limit'] for it in items if it['weight']<=1<<j),
               'required':(1<<(j+1))-1} for j in range(n)]
    if any(row['available']<row['required'] for row in prefixes):return None,prefixes
    rem=o-1;selected=[0]*len(items)
    for i in sorted(range(len(items)),key=lambda i:(-items[i]['weight'],i)):
        selected[i]=min(items[i]['limit'],rem//items[i]['weight'])
        rem-=selected[i]*items[i]['weight']
    check(rem==0,'bounded_top_degree_selection')
    return selected,prefixes

def pair_patterns(indices,signs):
    """All disjoint singletons and same-sign pairs, with original prime labels."""
    if not indices:
        yield []
        return
    i=indices[0]
    for rest in pair_patterns(indices[1:],signs):yield [(i,)]+rest
    for j in indices[1:]:
        if signs[i]!=signs[j]:continue
        remaining=[x for x in indices[1:] if x!=j]
        for rest in pair_patterns(remaining,signs):yield [(i,j)]+rest

def block_options(indices,fs,signs,logs,o):
    """Maximal lines in each allowed mode/coset parity. All offsets are retained."""
    i=indices[0];q,e=fs[i]
    if len(indices)==1:
        if signs[i]==0:
            yield dict(indices=list(indices),mode='single',offsets=[0],steps=[1],capacity=e,
                       coset_parity=0,log=logs[i])
        else:
            for parity in (0,1):
                yield dict(indices=list(indices),mode='single',offsets=[parity],steps=[2],
                           capacity=(e-parity)//2,coset_parity=parity,log=2*logs[i]%o)
        return
    j=indices[1];r,f=fs[j];E=min(e,f)
    for mode in ('parallel','exchange'):
        for parity in ((0,1) if signs[i] else (0,)):
            if mode=='parallel':
                offsets=[0,0]
                if parity:offsets=[1,0] if e>f else [0,1]
                capacity=min(e-offsets[0],f-offsets[1]);steps=[1,1]
            else:
                total=E
                if signs[i] and total%2!=parity:total=E+1 if e!=f else E-1
                lo=max(0,total-f);hi=min(e,total)
                offsets=[lo,total-lo];capacity=hi-lo;steps=[1,-1]
            a=(steps[0]*logs[i]+steps[1]*logs[j])%o
            yield dict(indices=list(indices),mode=mode,offsets=offsets,steps=steps,
                       capacity=capacity,coset_parity=parity,log=a)

def search_certificate(p: int,k: int,fs):
    if k<3 or p%8!=1 or p<=2*(1<<(2*k-5)):
        raise ValueError('original fixed-seed range')
    o=1<<(k-2)
    for base in (3,-3):
        signs=[int(not inside(q,base)) for q,e in fs]
        if not any(signs):continue
        logs=[chart_log(-q if ep else q,k,base) for (q,e),ep in zip(fs,signs)]
        s=chart_log(p,k,base)
        for pattern in pair_patterns(list(range(len(fs))),signs):
            for blocks in product(*(tuple(block_options(bl,fs,signs,logs,o)) for bl in pattern)):
                if sum(bl['coset_parity'] for bl in blocks)%2!=1:continue
                items=[]
                for i,bl in enumerate(blocks):
                    if bl['log'] and bl['capacity']:
                        items.append(dict(block=i,log=bl['log'],weight=lowbit(bl['log']),limit=bl['capacity']))
                if s:items.append(dict(block=None,log=(-s)%o,weight=lowbit(s),limit=1))
                selected,prefixes=select_counts(k-2,items)
                if selected is not None:
                    return dict(p=p,k=k,base=base,phase=s,blocks=list(blocks),items=items,
                                selected=selected,prefixes=prefixes)
    return None

def old_socle(p,k,fs):
    o=1<<(k-2)
    for base in (3,-3):
        if all(inside(q,base) for q,e in fs):continue
        items=[]
        for q,e in fs:
            if inside(q,base):
                a=chart_log(q,k,base)
                if a:items.append(dict(weight=lowbit(a),limit=e))
        s=chart_log(p,k,base)
        if s:items.append(dict(weight=lowbit(s),limit=1))
        if select_counts(k-2,items)[0] is not None:return True
    return False

@lru_cache(None)
def previous_threshold(k,f,s):
    o=1<<(k-2);J=log3(11,k)
    pts=sorted({(J*i-t)%o for i in range(min(f,o-1)+1) for t in (0,s)})
    return max((pts[(i+1)%len(pts)]-v)%o or o for i,v in enumerate(pts))-1

def old_two_block(p,k,fs):
    ex=dict(fs)
    return any(q%8 in (5,7) for q,e in fs) and ex.get(3,0)>=previous_threshold(k,ex.get(11,0),log3(p,k))

def short_word(p,k,fs):
    m=1<<k;targets={m-1,(-p)%m}
    for i,(q,e) in enumerate(fs):
        if q%m in targets:return True
        for j in range(i,len(fs)):
            r,f=fs[j]
            if (i!=j or e>=2) and q*r%m in targets:return True
    return False

def reconstruct(p,k,Q):
    u=1<<(2*k-5);N=p+4*u;m=1<<k
    if not (p%8==1 and p>2*u and Q>0 and N%Q==0 and Q%m==m-1):
        raise ValueError('not an original target cofactor')
    R=N//Q;a=(p+R)//4;d=gcd(a,u)
    check(d*d%u==0,'integer_gcd_normalization')
    h,r,s=d*d//u,u//d,a//d
    check((r+s)%R==0,'original_middle_gate')
    lam=(r+s)//R;den=[a,p*h*s*lam,p*h*r*lam]
    check(0<R<p and p<4*a and 2*a<p and a*a%u==0,'first_half_availability')
    check(a==h*r*s and u==h*r*r and gcd(r,s)==1,'marked_factor_identities')
    check(4*prod(den)==p*(den[0]*den[1]+den[0]*den[2]+den[1]*den[2]),'positive_reciprocal_identity')
    check(Fraction(p*a*a,R*den[1]-p*a)==u,'ordered_middle_inverse')
    af=factor(a);beta=[valuation(u,q)-e for q,e in af]
    check(all(-e<=v<=e for (q,e),v in zip(af,beta)),'original_centered_box')
    return dict(p=p,k=k,N=N,R=R,Q=Q,u=u,a=a,h=h,r=r,s=s,lambda_=lam,
                channel='M',denominators=den,a_factorization=af,centered_exponents=beta)

def rotate(bits,shift,o):
    shift%=o
    return bits if not shift else ((bits<<shift)|(bits>>(o-shift)))&((1<<o)-1)

def submasks(c):
    values=[];f=c
    while True:
        values.append(f)
        if f==0:return sorted(values)
        f=(f-1)&c

def inspect_packet(cert,fs,enumerate_words=False):
    """Validate a certificate before expanding or choosing any arithmetic hit."""
    p,k,base=cert['p'],cert['k'],cert['base'];m=1<<k;o=1<<(k-2)
    blocks,items,selected=cert['blocks'],cert['items'],cert['selected']
    check(prod(q**e for q,e in fs)==p+(1<<(2*k-3)) and len(set(q for q,e in fs))==len(fs)
          and all(e>0 and prime(q) for q,e in fs),'actual_distinct_prime_inventory')
    check(len(items)==len(selected) and len({it['block'] for it in items})==len(items),'selection_shape')
    seen=set();A=1;parameters=[0]*len(blocks);limits=[0]*len(blocks);bits=[];phase_delta=0
    for bl in blocks:
        ids=bl['indices'];off=bl['offsets'];steps=bl['steps'];E=bl['capacity']
        check(E>=0 and len(ids)==len(off)==len(steps) and len(ids) in (1,2),'block_shape')
        check(not seen.intersection(ids) and len(ids)==len(set(ids)),'disjoint_original_prime_blocks')
        seen.update(ids)
        check(all(step in (-1,1,2) for step in steps),'nonconstant_block_inverse')
        ares=1;gres=1
        for ix,v,step in zip(ids,off,steps):
            q,e=fs[ix]
            check(0<=v<=e and 0<=v+step*E<=e,'actual_block_endpoint_budgets')
            A*=q**v;ares=ares*pow(q,v,m)%m;gres=gres*pow(q,step,m)%m
        check(inside(gres,base),'ratio_is_in_actual_chart')
        check(pow(base,bl['log'],m)==gres,'retained_ratio_log')
        check(int(not inside(ares,base))==bl['coset_parity'],'base_coset_tag')
    check(not inside(A,base),'outside_base_not_created_by_augmentation')
    check(sum(c*it['weight'] for c,it in zip(selected,items))==o-1,'exact_selected_top_degree')
    for it,c in zip(items,selected):
        check(0<=c<=it['limit'],'selected_capacities')
        check(it['log']%o!=0 and it['weight']==lowbit(it['log']%o),'true_nonidentity_weight')
        b=it['block']
        if b is None:
            phase_delta=c
            check(it['limit']==1 and it['log']==(-chart_log(p,k,base))%o,'phase_is_orientation')
        else:
            check(it['limit']==blocks[b]['capacity'] and it['log']==blocks[b]['log'],'block_inventory_link')
            limits[b]=c
        for bit in range(c.bit_length()):
            if c>>bit&1:bits.append(dict(block=b,power=1<<bit,shift=(it['log']<<bit)%o))
    suffix=[0]*(len(bits)+1);suffix[-1]=1
    for i in range(len(bits)-1,-1,-1):suffix[i]=suffix[i+1]^rotate(suffix[i+1],bits[i]['shift'],o)
    check(suffix[0]==(1<<o)-1,'full_cyclic_norm_from_original_blocks')
    counts=[0]*o;counts[0]=1
    for bit in bits:counts=[counts[t]+counts[(t-bit['shift'])%o] for t in range(o)]
    check(all(c%2==1 for c in counts),'every_integer_coefficient_positive_odd')
    check(sum(counts)==1<<len(bits),'no_colored_prime_copy_mass')
    target=chart_log(-pow(A,-1,m),k,base)
    current=target;epsilon=0
    for i,bit in enumerate(bits):
        if suffix[i+1]>>current&1:continue
        current=(current-bit['shift'])%o
        check(bool(suffix[i+1]>>current&1),'odd_suffix_step')
        if bit['block'] is None:epsilon+=bit['power']
        else:parameters[bit['block']]+=bit['power']
    check(current==0,'terminating_packet_inverse')
    physical_exponents=[0]*len(fs)
    for b,(bl,t,c) in enumerate(zip(blocks,parameters,limits)):
        check(t&~c==0,'original_submask_not_colored_choice')
        for ix,v,step in zip(bl['indices'],bl['offsets'],bl['steps']):physical_exponents[ix]=v+step*t
    W=prod(q**v for (q,e),v in zip(fs,physical_exponents));N=p+(1<<(2*k-3))
    check(N%W==0 and W*pow(p,-epsilon,m)%m==m-1,'available_physical_word_and_orientation')
    Q=W if not epsilon else N//W
    state=reconstruct(p,k,Q)
    # Invert the exact word with its phase and chosen block lines retained.
    recovered=Q if not epsilon else state['R']
    for bl,t in zip(blocks,parameters):
        coordinates=[]
        for ix,v,step in zip(bl['indices'],bl['offsets'],bl['steps']):
            vv=valuation(recovered,fs[ix][0]);check((vv-v)%step==0,'block_inverse_divisibility')
            coordinates.append((vv-v)//step)
        check(all(z==t for z in coordinates),'complete_affine_block_inverse')
    # Free factors are only primes on which the selected physical source is identically zero.
    used=set()
    for bl,c in zip(blocks,limits):
        for ix,v,step in zip(bl['indices'],bl['offsets'],bl['steps']):
            if v or c:used.add(ix)
    free=[fs[ix] for ix in range(len(fs)) if ix not in used]
    tau=prod(e+1 for q,e in free)
    signed=prod((e+1) if inside(q,base) else (int(e%2==0)) for q,e in free)
    mass=(tau+signed)//2
    lower=mass if not phase_delta else (mass+1)//2
    out=dict(constant_divisor=A,selected_parameters=parameters,selected_counts=limits,
             phase_selected=phase_delta,phase_used=epsilon,physical_word=W,
             physical_exponents=physical_exponents,coefficients=counts,packet_mass=sum(counts),
             target_log=target,free_factorization=free,free_inside_divisor_mass=mass,
             count_lower=lower,state=state)
    if enumerate_words:
        records=[];seenwords=set();byres=Counter()
        for ts in product(*(submasks(c) for c in limits)):
            ex=[0]*len(fs)
            for bl,t in zip(blocks,ts):
                for ix,v,step in zip(bl['indices'],bl['offsets'],bl['steps']):ex[ix]=v+step*t
            word=prod(q**f for (q,e),f in zip(fs,ex))
            check(word not in seenwords and N%word==0,'packet_source_injective_on_integer_words')
            seenwords.add(word)
            for ep in range(phase_delta+1):
                res=word*pow(p,-ep,m)%m
                check(not inside(res,base),'every_reduced_word_in_original_outside_coset')
                byres[res]+=1;records.append(dict(parameters=ts,exponents=ex,word=word,phase=ep,residue=res))
        check(len(byres)==o and all(v%2 for v in byres.values()),'physical_word_parity_cover')
        out['all_packet_words']=records
    return out

def half_turn(p,k,b,q,r):
    """One fixed outside exchange; includes its whole actual prime-power interval."""
    if not (k>=4 and p%8==1 and p>2*(1<<(2*k-5))):raise ValueError('half-turn ES domain')
    if not (prime(b) and prime(q) and prime(r) and len({b,q,r})==3 and b%8 in (3,5)):
        raise ValueError('three distinct actual primes, full-order base')
    base=3 if b%8==3 else -3;m=1<<k;o=1<<(k-2);L=o//2;N=p+(1<<(2*k-3))
    fs=dict(factor(N))
    if any(t not in fs for t in (b,q,r)) or inside(q,base) or inside(r,base):raise ValueError('unavailable outside pair')
    if q*pow(r,-1,m)%m!=pow(b,L,m):raise ValueError('pair is not a half-turn')
    e=fs[b];M=N//(b**e*q**fs[q]*r**fs[r])
    free=[t for t in divisors(factor(M)) if inside(t,base)];rows=[];states=[]
    for t in free:
        # Brute finite logarithm here is only for independent illustrative fixtures.
        target=(-pow(q*t,-1,m))%m
        j=next(j for j in range(o) if pow(b,j,m)==target)
        least=j%L
        for i in range(least,e+1,L):
            partner=q if (j-i)%o==0 else r
            Q=partner*b**i*t
            check(N%Q==0 and Q%m==m-1,'half_turn_original_word')
            states.append(reconstruct(p,k,Q))
        rows.append(dict(free_divisor=t,full_log=j,least_exponent=least,
                         count=(e-least)//L+1 if e>=least else 0))
    low=((e+1)//L)*len(free);high=((e+L)//L)*len(free)
    check(low<=len(states)<=high,'half_turn_exact_count_bounds')
    if (e+1)%L==0:check(len(states)==low==high,'half_turn_equal_interval_count')
    full=[Q for Q in divisors(tuple(fs.items())) if Q%m==m-1]
    complete=fs[q]==fs[r]==1 and all(inside(t,base) for t,_ in factor(M))
    if complete:check(sorted(x['Q'] for x in states)==full,'half_turn_complete_branch_count')
    return dict(p=p,k=k,base_prime=b,pair=[q,r],factorization=tuple(fs.items()),
                L=L,available_exponent=e,threshold=L-1,free_factor=M,
                free_inside_divisors=free,count_bounds=[low,high],states=states,
                subfamily_is_complete=complete,complete_count=len(full),log_rows=rows)

def structure_tests():
    cases=Counter()
    # The original two-prime box is the disjoint union of its anti-diagonals.
    for e in range(9):
        for f in range(9):
            cells=[]
            for c in range(e+f+1):
                lo=max(0,c-f);hi=min(e,c)
                for t in range(hi-lo+1):
                    i,j=lo+t,c-lo-t
                    check(i+j==c and i-lo==t,'antidiagonal_typed_inverse')
                    cells.append((i,j))
            check(sorted(cells)==list(product(range(e+1),range(f+1))),'whole_box_partition_no_lost_multiplicity')
            for parity in (0,1):
                for mode in ('parallel','exchange'):
                    widths=[]
                    if mode=='exchange':
                        for c in range(e+f+1):
                            if c%2==parity:widths.append(min(e,c)-max(0,c-f))
                        expected=min(e,f)-int(e==f and e%2!=parity)
                    else:
                        for d in range(-f,e+1):
                            if d%2==parity:
                                lo=max(0,-d);hi=min(f,e-d);widths.append(hi-lo)
                        expected=min(e,f)-int(e==f and parity==1)
                    check(max(widths,default=-1)==expected,'optimal_affine_line_capacity_all_parities')
            cases['boxes']+=1
    for n in range(1,6):
        for limits in product(range(4),repeat=n):
            items=[dict(weight=1<<j,limit=e) for j,e in enumerate(limits)]
            c,p=select_counts(n,items);target=(1<<n)-1;possible=1;mask=(1<<(target+1))-1
            for j,e in enumerate(limits):
                nxt=0
                for t in range(e+1):nxt|=possible<<(t*(1<<j))
                possible=nxt&mask
            check((c is not None)==bool(possible>>target&1),'prefix_iff_actual_bounded_selection')
            cases['capacity_profiles']+=1
    # Arbitrary nonidentity logs, not just chosen prime examples.
    for n,length,emax in ((1,3,3),(2,3,3),(3,3,2),(4,2,2)):
        o=1<<n
        for logs in combinations_with_replacement(range(1,o),length):
            for limits in product(range(1,emax+1),repeat=length):
                its=[dict(log=a,weight=lowbit(a),limit=e) for a,e in zip(logs,limits)]
                c,_=select_counts(n,its)
                if c is None:continue
                coeff=[0]*o;coeff[0]=1
                for a,cc in zip(logs,c):
                    coeff=[sum(coeff[(r-a*t)%o] for t in submasks(cc)) for r in range(o)]
                check(all(x%2 for x in coeff),'all_small_original_packets_odd')
                cases['cyclic_packets']+=1
    for c in range(65):check(submasks(c)==[i for i in range(c+1) if comb(c,i)%2],'Frobenius_binary_submask')
    # Half-turn interval theorem: no group-library or analytic assumption.
    for n in range(2,8):
        o=1<<n;L=o//2
        for e in range(0,2*o+1):
            for a in range(o):
                actual=sum(int((i-a)%o==0)+int((i+L-a)%o==0) for i in range(e+1))
                formula=(e-(a%L))//L+1 if e>=a%L else 0
                check(actual==formula,'half_turn_interval_all_phases')
                check((e+1)//L<=actual<=(e+L)//L,'half_turn_uniform_sharp_floor_ceiling')
        cases['half_turn_orders']+=1
    # A very large exponent count is returned symbolically/exactly, not expanded.
    big_e=10**100+37;big_L=1<<39;j=1234567
    count=(big_e-j)//big_L+1
    check(count==(big_e-j+big_L)//big_L,'huge_budget_count_without_expansion')
    return dict(cases=cases,huge_count=dict(exponent=big_e,L=big_L,target=j,count=count))

def negative_controls():
    out=[]
    def reject(label,fn):
        try:fn()
        except (ArithmeticError,ValueError):out.append(label);return
        raise ArithmeticError('invalid control accepted: '+label)
    p,k=837601,5;fs=factor(p+128);cert=search_certificate(p,k,fs)
    import copy
    bad=copy.deepcopy(cert);bad['blocks'][1]['indices']=[bad['blocks'][0]['indices'][0]]
    reject('same original prime reused in two blocks',lambda:inspect_packet(bad,fs))
    bad=copy.deepcopy(cert);bad['blocks'][2]['offsets']=[0,0]
    reject('ratio used without its compensating factor',lambda:inspect_packet(bad,fs))
    bad=copy.deepcopy(cert);bad['blocks'][2]['steps']=[1,1]
    reject('exchange replaced by product without moving its logarithm',lambda:inspect_packet(bad,fs))
    bad=copy.deepcopy(cert);bad['selected'][0]+=1
    reject('top degree replaced by an overrun',lambda:inspect_packet(bad,fs))
    reject('cross-coset quotient silently logged inside chart',lambda:chart_log(5,5,3))
    reject('zero augmentation called empty residue set',lambda:check(sum([1]*8)%2!=0,'wrong_augmentation_inference'))
    reject('printed formal phase treated as a divisor',lambda:check((837729%837601)==0,'phase_is_not_a_prime_factor'))
    reject('actual missing cofactor declared available',lambda:reconstruct(278881,5,31))
    return out

def example_tests():
    out=[]
    for p,k in ((837601,5),(1740481,5),(1794769,5),(278881,5),(852769,6),(482187176641,6)):
        check(prime(p),'deterministic_example_primality')
        N=p+(1<<(2*k-3));fs=factor(N);qs=[Q for Q in divisors(fs) if Q%(1<<k)==(1<<k)-1]
        cert=search_certificate(p,k,fs)
        packet=inspect_packet(cert,fs,True) if cert else None
        if packet:check(packet['count_lower']<=len(qs) and packet['state']['Q'] in qs,'example_original_count_and_return')
        out.append(dict(p=p,k=k,N=N,factorization=fs,old_socle=old_socle(p,k,fs),old_two_block=old_two_block(p,k,fs),
                        short_word_both_roles=short_word(p,k,fs),certificate=cert,packet=packet,
                        complete_states=[reconstruct(p,k,Q) for Q in qs]))
    first=out[0]
    check(not any(first[key] for key in ('old_socle','old_two_block','short_word_both_roles')),'strict_exchange_vs_complete_previous_baseline')
    check(len(first['complete_states'])==2 and first['packet']['count_lower']==2,'sharp_two_state_example')
    last=out[-1]
    check(last['old_two_block'] and last['certificate'] is None,'retained_two_block_complementarity')
    turns=[half_turn(837601,5,3,23,71),half_turn(1740481,5,3,13,29),half_turn(278881,5,3,29,1069)]
    check(turns[-1]['available_exponent']==turns[-1]['threshold']-1 and turns[-1]['complete_count']==0,
          'actual_prime_one_below_sharp_threshold')
    # A different seed at the threshold counterexample demonstrates it is not an ES counterexample.
    alt_p=278881;alt=None
    for k in range(3,12):
        if alt_p<=2*(1<<(2*k-5)):break
        N=alt_p+(1<<(2*k-3))
        for Q in divisors(factor(N)):
            if Q%(1<<k)==(1<<k)-1:alt=reconstruct(alt_p,k,Q);break
        if alt:break
    check(alt is not None,'empty_selected_branch_is_not_false_prime')
    return dict(examples=out,half_turns=turns,threshold_prime_alternative=alt)

def scan(bound):
    totals=Counter();sets={k:set() for k in ('short','two_block','old_socle','old_union','affine','new_union','actual')}
    rows=[];added=[];returns=sha256()
    for p in primes_to(bound):
        if p%840 not in HARD:continue
        totals['hard_primes']+=1;k=4
        while p>2*(1<<(2*k-5)):
            N=p+(1<<(2*k-3));fs=factor(N);qs=[Q for Q in divisors(fs) if Q%(1<<k)==(1<<k)-1]
            a=search_certificate(p,k,fs);old=old_socle(p,k,fs);two=old_two_block(p,k,fs);short=short_word(p,k,fs)
            original=old or two or short;new=original or a is not None
            check(not old or a is not None,'new_class_contains_every_old_socle_certificate')
            check(not new or bool(qs),'all_sufficient_tests_against_original_divisors')
            if a:
                pk=inspect_packet(a,fs)
                check(pk['state']['Q'] in qs and pk['count_lower']<=len(qs),'scan_marked_return_and_lower_count')
                returns.update(json.dumps(pk['state'],sort_keys=True,separators=(',',':')).encode())
            # Verify every actual ordered state, not merely those selected by the new theorem.
            for Q in qs:reconstruct(p,k,Q)
            flags=dict(short=short,two_block=two,old_socle=old,old_union=original,affine=a is not None,new_union=new,actual=bool(qs))
            totals['branches']+=1;totals['original_middle_states']+=len(qs)
            for key,hit in flags.items():
                totals[key+'_branches']+=int(hit)
                if hit:sets[key].add(p)
            if a and not original:added.append(dict(p=p,k=k,certificate=a,packet=inspect_packet(a,fs,True),
                                                   full_factorization=fs,complete_states=[reconstruct(p,k,Q) for Q in qs]))
            rows.append([p,k,N,fs,int(two),int(old),int(short),int(a is not None),len(qs)])
            k+=1
    for key in sets:totals[key+'_primes']=len(sets[key])
    return dict(bound=bound,scope='six hard classes modulo840; k>=4 and p>2u; canonical middle states',
                totals=totals,additional_primes=sorted(sets['new_union']-sets['old_union']),
                strict_added_branches=added,rows=rows,
                row_digest=sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest(),
                marked_return_digest=returns.hexdigest())

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--bound',type=int,default=2000000);ap.add_argument('--out',default='generated')
    args=ap.parse_args()
    if args.bound<1009:ap.error('bound must include at least1009')
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    data={'structural.json':structure_tests(),'examples.json':example_tests(),
          'negative_controls.json':negative_controls(),'scan.json':scan(args.bound)}
    data['checks.json']=dict(CHECKS)
    for name,value in data.items():(out/name).write_text(json.dumps(value,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'checks':sum(CHECKS.values()),'negative_controls':len(data['negative_controls.json']),
                      'scan':data['scan.json']['totals']},sort_keys=True))
if __name__=='__main__':main()
