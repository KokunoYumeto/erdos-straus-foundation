#!/usr/bin/env python3
"""Bounded exact verification. See scope.json for what is and is not exhaustively tested."""
from __future__ import annotations
from arithmetic import *
from collections import Counter
from hashlib import sha256
from itertools import product
from pathlib import Path
import argparse

checks=0

def check(cond,msg='main check failed'):
    global checks
    checks+=1; need(cond,msg)


def box_replay(bound,out):
    isp=sieve(bound); spf=spf_table(bound//2+1); counts=Counter(); tiles=[]; powers=[]
    for p in range(1,bound+1,24):
        if not isp[p]:continue
        counts['primes']+=1
        for a in range(p//4+1,(p+1)//2):
            R=4*a-p; fa=factor(a,spf); words=divs_f({q:2*e for q,e in fa.items()})
            counts['shells']+=1; counts['divisor_words']+=len(words)
            original=[]
            for ch in ['E','M']:
                for u in words:
                    G=4*u+1 if ch=='E' else p+4*u
                    if G*G%R: continue
                    counts[f'{ch}_traces']+=1
                    if G%R==0: counts[f'{ch}_full']+=1
                    else: counts[f'{ch}_proper']+=1
                    original.append((ch,u,G%R==0))
            if original:
                k,D,delta=residual_parts(R)
                if D>1:
                    ts=trace_tiles(p,a)
                    check(sum(prod(z['lengths']) for z in ts)==len(original),'trace tile partition')
                    actual=sorted((t['channel'],u) for t in ts for u in t['full_words'])
                    expected=sorted((ch,u) for ch,u,full in original if full)
                    check(actual==expected,'full tile coefficient')
                    tiles.append(dict(p=p,a=a,R=R,K=k,D=D,delta=delta,tiles=ts,
                        direct_trace_words=[[ch,u,full] for ch,u,full in original]))
                    for ch,u,_ in original:
                        rec=state(p,a,u,ch)
                        check(rec['trace'] and rec['common_denominator']==D//gcd(D,rec['defect']))
                if len(fa)==1:
                    q,e=next(iter(fa.items()))
                    if q>3:
                        pp=prime_power_middle(p,q,e)
                        check(pp['full_betas']==[f-e for f in range(2*e+1) if (q**e+q**f)%R==0])
                        powers.append(dict(p=p,q=q,e=e,R=R,classification=pp))
    counts['squareful_trace_shells']=len(tiles)
    counts['squareful_trace_tiles']=sum(len(t['tiles']) for t in tiles)
    dump(out/'box_tiles.json',dict(bound=bound,counts=dict(counts),shells=tiles,prime_power_samples=powers))
    return dict(counts)


def square_replay(bound,out):
    isp=sieve(bound); records=[]; stats=Counter()
    for q in range(5,isqrt(bound//2)+1):
        if not isp[q]:continue
        a=q*q; candidates=set()
        for g in (4*q+1,4*q**3+1,q+1):
            for R in divs_f({l:2*e for l,e in factor(g).items()}):
                p=4*a-R
                if 2*a<p<=bound and R%4==3 and p%24==1 and isp[p]: candidates.add(p)
        for p in sorted(candidates):
            R=4*a-p; actual=[]
            for ch in ['E','M']:
                for f in range(5):
                    G=4*q**f+1 if ch=='E' else p+4*q**f
                    if G*G%R==0: actual.append((ch,f,G%R==0))
            check(sorted(actual)==prime_square_prediction(p,q),'prime square classification')
            if not actual:continue
            recs=[state(p,a,q**f,ch) for ch,f,_ in actual]
            for r in recs:
                stats[(r['channel'],'full' if r['full'] else 'proper')]+=1
                if r['channel']=='M' and not r['full']:
                    check(not any(z['channel']=='E' for z in recs))
                    check(not any(z['full'] for z in recs))
                    check(full_deletions(r)==[] and full_deletions(r,'ray')==[],'terminal M square')
                if r['channel']=='E' and r['u']==q and not r['full']:
                    expected=[4*q+1] if R%(4*q+1)==0 else []
                    check(full_deletions(r)==expected,'low E square exact deletion')
            if sum(r['channel']=='E' for r in recs)==2:check(R in(3,75))
            records.append(dict(p=p,q=q,a=a,R=R,records=recs))
    records.sort(key=lambda x:(x['p'],x['q']))
    summary=dict(bound=bound,shells=len(records),state_counts={f'{c}_{v}':n for (c,v),n in sorted(stats.items())})
    dump(out/'prime_squares.json',dict(summary=summary,shells=records))
    return summary


def prefix_replay(bound,out):
    isp=sieve(bound); spf=spf_table(bound//2+1); ps=[]; exceptions=[]; details={}
    for p in range(1,bound+1,24):
        if not isp[p]:continue
        first_trace=None; first_full=None; rows=[]
        for R in range(3,p,4):
            a=(p+R)//4; fa=factor(a,spf); ds=divs_f({q:2*e for q,e in fa.items()})
            hits=[]
            for u in ds:
                for ch,G in [('E',4*u+1),('M',p+4*u)]:
                    if G*G%R==0: hits.append([ch,u,G%R==0])
            if hits and first_trace is None:first_trace=R
            if any(z[2] for z in hits):first_full=R
            rows.append(dict(R=R,a=a,word_count=len(ds),traces=hits))
            if first_full is not None:break
        check(first_full is not None,'no full witness in finite prime replay')
        rec=dict(p=p,first_trace=first_trace,first_full=first_full,shells=rows)
        ps.append(rec)
        if first_trace!=first_full:
            exceptions.append(p)
            # Serialize every word and both gate residues for the whole relevant prefix.
            rr=[]
            for row in rows:
                a,R=row['a'],row['R']; fs=factor(a)
                rr.append(dict(a=a,R=R,factorization=[[q,e] for q,e in fs.items()],
                    words=[dict(u=u,E=(4*u+1)%R,M=(p+4*u)%R) for u in divs_f({q:2*e for q,e in fs.items()})]))
            details[str(p)]=rr
    check(exceptions and exceptions[0]==67369,'least nonmonotone trace prefix')
    dump(out/'prefix_certificate.json',dict(bound=bound,scope='all primes 1 mod24 through bound; all shells through first full gate',
        primes=ps,exceptions=exceptions,full_failure_words=details))
    return dict(bound=bound,primes=len(ps),exceptions=exceptions,shells=sum(len(r['shells']) for r in ps))


def worked(out):
    inputs=[state(48049,12019,29189,'E'),state(48049,12019,119,'E'),state(48049,12019,707,'M')]
    target=mixed_combine(inputs,[1,-1,1])
    check(target['u']==173417 and target['full'])
    for r in inputs:
        check(not r['full'] and r['common_denominator']==3)
        check(full_deletions(r)==[] and full_deletions(r,'ray')==[])
    line=neutral_line(inputs[2],[-1,1,1]); check([x['t'] for x in line['points'] if x['full']]==[1])
    pell=[]
    for t,w,k in [(7,2,4),(97,28,4),(1351,390,114)]:
        delta=3;q=delta*t*k-1;p=4*q*q-delta*t*t
        check(t*t-4*delta*w*w==1 and is_prime(q) and is_prime(p))
        rec=state(p,q*q,q,'M')
        arrows=factor_sum_returns(rec); chosen=next(x for x in arrows if x['w']==w)
        check(not rec['full'] and chosen['target']['full'])
        check(full_deletions(rec)==[] and full_deletions(rec,'ray')==[])
        inv=factor_sum_inverse(chosen['target'])
        check(any(x['w']==w and x['source']['a']==q*q and x['source']['u']==q for x in inv))
        pell.append(dict(delta=delta,t=t,w=w,k=k,q=q,p=p,prime_trial_cutoffs=[isqrt(q),isqrt(p)],
             arrow=chosen,inverse=inv))
    other=[]
    for p,R,u in [(2953,175,23),(12577,207,47),(13537,375,47),(24001,207,89),(63361,207,116),(2003761,375,1916)]:
        r=state(p,(p+R)//4,u,'M'); returns=factor_sum_returns(r)
        check(returns and not r['full'] and is_prime(p))
        for x in returns:
            inv=factor_sum_inverse(x['target'])
            check(any(y['source']['u']==u and y['source']['R']==R and y['w']==x['w'] for y in inv))
            x['inverse']=inv
        other.append(dict(source=r,returns=returns))
    recurrence=[];t,w=1,0
    for n in range(25):
        check(t*t-12*w*w==1)
        q=12*t-1;p=4*q*q-3*t*t
        if n%12==1:check(p%840==529)
        recurrence.append(dict(n=n,t=t,w=w,q=q,p=p,primality_claim=False))
        t,w=7*t+24*w,2*t+7*w
    def mul(A,B):return [[sum(A[i][k]*B[k][j] for k in range(2))%840 for j in range(2)] for i in range(2)]
    A=[[7,24],[2,7]];v=[[1,0],[0,1]];mat=[]
    for n in range(1,13):v=mul(v,A);mat.append(v)
    check(v==[[1,0],[0,1]] and all(x!=v for x in mat[:-1]))
    # The first trace has no earlier full gate. A strictly decreasing arbitrary-source rule fails.
    fail=state(67369,16849,83,'E');check(fail['trace'] and not fail['full'])
    # A proposed factor-sum map has a genuine, explicitly tested obstruction too.
    rr=state(9601,2956,8,'M');check(rr['r']!=1)
    nonsquare=state(2737,(2737+135)//4,1,'M') if False else None
    dump(out/'worked_examples.json',dict(mixed=dict(inputs=inputs,coefficients=[1,-1,1],target=target,neutral_line=line),
        pell=pell,general_factor_sum=other,recurrence=recurrence,matrix_order_mod840=mat,
        nonmonotone_source=fail))
    return dict(pell_prime_examples=len(pell),general_sumshift_examples=len(other))


def local_tests(out):
    count=0;saturation=0;stabilizers=0
    for R in range(3,500,2):
        k,D,delta=residual_parts(R)
        check(k*D==R and k*k%R==0)
        for c in range(D):
            z=(-1+k*c)%R
            check(gcd(z,R)==1)
            check(R//gcd(R,z+1)==D//gcd(D,c))
            for b in range(D):
                # three signed traces; signs and the addition law must agree
                zz=pow(z,1,R)*pow((-1+k*b)%R,-1,R)*z%R
                check(zz==(-1+k*(2*c-b))%R);count+=1
    for D in range(3,16,2):
        for l1,l2 in product(range(D),repeat=2):
            for N1,N2 in product(range(1,5),repeat=2):
                fac=[(l1,N1),(l2,N2)];cs=convolution(D,fac)
                periods,_=coefficient_stabilizer(D,fac)
                check(periods==[a for a in range(D) if all(cs[(j+a)%D]==cs[j] for j in range(D))]);stabilizers+=1
                width=sum(N-1 for l,N in fac if gcd(l,D)==1)
                if width>=D-1:
                    check(min(cs)>=prod(N for l,N in fac if gcd(l,D)!=1));saturation+=1
        # exact sharp finite interval
        cs=convolution(D,[(1,D-1)]);check(cs==[1]*(D-1)+[0])
    dump(out/'local_certificates.json',dict(square_zero_triples=count,stabilizer_checks=stabilizers,
         saturated_tests=saturation,residual_bound=499,cyclic_moduli=list(range(3,16,2)),
         proof_boundary='finite corroboration only; universal proofs are in core.tex'))


def fixed_tail_sum(out):
    """Exact fixed-(p,y+z) fibre and the complete p=67369 trace census."""
    p=67369
    source=state(p,16849,1421,'M')
    check(source['trace'] and not source['full'])
    seed=fixed_tail_seed(source)
    check(seed['N']==586110300 and seed['B']==13459046189 and seed['C']==95731349)
    check(seed['w']==13363314840 and seed['gate_residue']==18 and not seed['exact_tail_gate'])
    check(seed['tail_difference_Z_minus_Y']==[-1484812760,3])
    check(seed['squareclass']['X']==[-1484812760,1])
    check(not seed['squareclass']['v_divides_X'] and not seed['squareclass']['parity_gate'])
    fibre=fixed_tail_fibre(p,seed['N'])
    check([z['rho'] for z in fibre['candidates']]==[3,15,75,87,435,2175])
    check(fibre['targets']==[])
    modular={15:[3,2],75:[7,5],87:[3,2],435:[7,3],2175:[3,2]}
    for row in fibre['candidates']:
        rho=row['rho']
        if rho==3:
            check(row['discriminant']<0)
            row['modular_or_sign_witness']=dict(kind='negative')
        else:
            modulus,residue=modular[rho]
            check(row['discriminant']%modulus==residue)
            check(residue not in {x*x%modulus for x in range(modulus)})
            row['modular_or_sign_witness']=dict(kind='quadratic nonresidue',modulus=modulus,residue=residue)

    positive=state(p,16850,674,'E')
    positive_N=Fraction(*positive['tail_sum']).numerator
    positive_fibre=fixed_tail_fibre(p,positive_N)
    check(positive_N==98750810744 and len(positive_fibre['targets'])==2)
    check({(z['rho'],z['a'],z['Y'],z['Z']) for z in positive_fibre['targets']}=={
        (31,16850,36631900,98714178844),(31,16850,98714178844,36631900)})

    # Enumerate every original word on every first-half shell at this prime.
    # The fixed-tail theorem then converts each distinct sum into a complete
    # divisor-and-square certificate, rather than a bounded target scan.
    proper=[]; full=[]
    for a in range(p//4+1,(p+1)//2):
        R=4*a-p
        for u in divisors(a*a):
            for ch,G in [('E',4*u+1),('M',p+4*u)]:
                if G*G%R: continue
                rec=state(p,a,u,ch)
                (full if rec['full'] else proper).append(rec)
    proper_by_sum={}
    for rec in proper:
        N=Fraction(*rec['tail_sum']).numerator
        proper_by_sum.setdefault(N,[]).append(dict(a=rec['a'],R=rec['R'],u=rec['u'],channel=rec['channel']))
    full_sums={Fraction(*rec['tail_sum']).numerator for rec in full}
    fibres=[]
    for N,tags in sorted(proper_by_sum.items()):
        ff=fixed_tail_fibre(p,N)
        check(ff['targets']==[])
        fibres.append(dict(N=N,source_tags=tags,candidate_residuals=[z['rho'] for z in ff['candidates']],
                           nonnegative_candidates=sum(z['discriminant']>=0 for z in ff['candidates'])))
    check(len(proper)==69 and len(proper_by_sum)==51)
    check(len(full)==47 and len(full_sums)==37 and set(proper_by_sum).isdisjoint(full_sums))
    check(sum(len(z['candidate_residuals']) for z in fibres)==507)
    check(sum(z['nonnegative_candidates'] for z in fibres)==478)
    dump(out/'fixed_tail_sum.json',dict(schema='es.fixed-tail-sum-fibre.v1',
         theorem='complete ordered integral first-half fibre at fixed prime and tail sum',
         retained_quantity='numerical tail sum y+z; not the raw factor sum h+s',source=source,seed=seed,
         N_factorization=[[q,e] for q,e in factor(seed['N']).items()],selected_fibre=fibre,
         positive_recovery_control=dict(source=positive,fibre=positive_fibre),
         p67369_census=dict(proper_trace_tags=len(proper),proper_tail_sums=len(proper_by_sum),
         integral_tags=len(full),integral_tail_sums=len(full_sums),shared_tail_sums=sorted(set(proper_by_sum)&full_sums),
         eligible_residual_candidates=507,nonnegative_discriminants=478,fibres=fibres),
         universal_ES_proved=False))
    return dict(proper_trace_tags=len(proper),proper_tail_sums=len(proper_by_sum),
                eligible_residual_candidates=507,integral_returns=0)


def sharp_packets(out):
    templates=[]
    for ell in [3,7,11,19,23,31,43]:
        R=ell**3; q=ell*ell-1
        while q<=7 or not is_prime(q): q+=R
        e=ell-1; Q=q**(e+1); L=840*ell//gcd(840,ell)
        v=(-R+4*q**e)%Q
        p0=(1+L*(((v-1)*pow(L,-1,Q))%Q))%(L*Q); modulus=L*Q
        check(gcd(p0,modulus)==1 and is_prime(q))
        sample=p0+max(0,(R+1-p0+modulus-1)//modulus)*modulus
        a=(sample+R)//4; h=a//q**e
        check(a%q**e==0 and h%q==1 and gcd(a,R)==1)
        packet=[]
        for beta in range(-e,e+1):
            value=pow(q,beta,R)
            if (value+1)%(ell*ell):continue
            c=((value+1)//(ell*ell))%ell
            u=h*q**(e+beta)
            check(c==beta%ell and c!=0 and a*a%u==0)
            packet.append(dict(beta=beta,defect=c,u=u))
        check(len(packet)==ell-1 and sorted(x['defect'] for x in packet)==list(range(1,ell)))
        record=dict(ell=ell,q=q,e=e,R=R,K=ell*ell,D=ell,
                    prime_progression=dict(residue=p0,modulus=modulus,threshold=R),
                    sample_integer=sample,sample_is_claimed_prime=False,a=a,h=h,packet=packet,
                    fine_direction=(-2)%ell,original_width=ell-2)
        if ell==3:
            pp=sample
            for j in range(200):
                if is_prime(pp):break
                pp+=modulus
            else:raise RuntimeError('finite isolated prime search exhausted')
            aa=(pp+R)//4
            record['isolated_prime']=dict(p=pp,trial_cutoff=isqrt(pp),a=aa,
                original_M_words=[state(pp,aa,(aa//q**e)*q**(e+b),'M') for b in range(-e,e+1) if b%2])
        templates.append(record)
    dump(out/'sharp_packets.json',dict(templates=templates,prime_infinitude_input='Dirichlet, after reduced CRT proof; not prime values of polynomials'))

def negative_controls(out):
    tests=[]
    def rejects(name,fn):
        try:fn()
        except ValueError:tests.append(dict(name=name,rejected=True));check(True)
        else:raise ValueError('invalid rule accepted: '+name)
    r=state(48049,12019,29189,'E')
    rejects('even number of negative trace factors',lambda:mixed_combine([r],[2]))
    rejects('reduce channel exponent modulo two',lambda:mixed_combine([r],[3]))
    records=[state(67369,16849,u,'M') for u in [1421,69803,4067]]
    check(sum(c*z['defect'] for c,z in zip([1,-1,1],records))%3==0)
    rejects('zero formal defect outside original exponent box',lambda:mixed_combine(records,[1,-1,1]))
    tests.append(dict(name='outside-box zero sum',formal_word=frac(Fraction(1421*4067,69803)),expected=[2401,29]))
    a=6853;check(a*a%83!=0)
    tests.append(dict(name='retaining old q after Pell factor-sum map',old_u=83,target_a=a,not_available=True))
    src=state(2003761,501034,1916,'M');outrec=factor_sum_returns(src)[0]['target']
    wrong=[outrec['a'],2*Fraction(*outrec['denominators'][1]),2*Fraction(*outrec['denominators'][2])]
    check(sum((1/Fraction(z) for z in wrong),Fraction())!=Fraction(4,src['p']))
    tests.append(dict(name='forgotten primitive gcd quotient',normalization_gcd=2,rejected=True))
    needfull=state(67369,16849,83,'E');check(needfull['trace'] and not needfull['full'])
    tests.append(dict(name='square gate substituted for full gate',R=27,G_residue=9,rejected=True))
    pell_seed=fixed_tail_seed(state(67369,16849,1421,'M'))
    check(pell_seed['U']**2-pell_seed['D']*pell_seed['V']**2==pell_seed['pell_norm'])
    check(not pell_seed['exact_tail_gate'] and pell_seed['gate_residue']==18)
    tests.append(dict(name='unrestricted Pell point substituted for an integer-tail return',
        R=pell_seed['R'],w=pell_seed['w'],w_mod_R=pell_seed['gate_residue'],rejected=True))
    for rec in [r,*records,src,state(27409,6889,83,'M')]:
        a=rec['a'];y,z=(Fraction(*t) for t in rec['denominators'][1:])
        d=decode_trace(rec['p'],a,y,z);check(d['state']==rec and not d['exterior_swap'])
        d2=decode_trace(rec['p'],a,z,y)
        if rec['channel']=='E':check(d2['state']==rec and d2['exterior_swap'])
        else:check(d2['state']['u']==a*a//rec['u'] and not d2['exterior_swap'])
    # All nine Type II coordinate equations at the genuinely returned state.
    r=outrec;aa,bb,cc,dd,ee,ff=r['s'],r['r'],Fraction(*r['quotient']),r['h'],r['R'],4*r['h']*r['s']*Fraction(*r['quotient'])-1
    p=r['p']
    identities=[4*aa*bb*dd==p+ee,cc*ee==aa+bb,4*aa*bb*cc*dd==aa+bb+p*cc,
        4*aa*cc*dd*ee==p+4*aa*aa*dd+ee,4*bb*cc*dd*ee==p+4*bb*bb*dd+ee,
        4*aa*cc*dd==ff+1,ee*ff==p+4*aa*aa*dd,bb*ff==p*cc+aa,
        4*cc*cc*dd*p+1==ff*(4*bb*cc*dd-1)]
    for z in identities:check(z)
    dump(out/'negative_controls.json',dict(controls=tests,decoded_order_tests=12,ET_TypeII_coordinate_equations=9))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',default='certificates')
    ap.add_argument('--bound',type=int,default=10000);ap.add_argument('--square-bound',type=int,default=2000000)
    ap.add_argument('--prefix-bound',type=int,default=67369)
    args=ap.parse_args();out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    counts=box_replay(args.bound,out);sq=square_replay(args.square_bound,out)
    pre=prefix_replay(args.prefix_bound,out);examples=worked(out);local_tests(out);fixed=fixed_tail_sum(out);sharp_packets(out);negative_controls(out)
    summary=dict(checks=checks,box=counts,prime_squares=sq,prefix=pre,examples=examples,
        fixed_tail_sum=fixed,universal_ES_proved=False,priority_claim=False)
    dump(out/'summary.json',summary);print(json.dumps(summary,indent=2))

if __name__=='__main__':main()
