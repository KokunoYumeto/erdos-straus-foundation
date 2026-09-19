#!/usr/bin/env python3
"""Exact Turn 5 arithmetic: character separation, pair fibres, reciprocal sources.
Standard library only. Bounded replays are not a universal ES proof.
"""
from __future__ import annotations
import argparse, hashlib, json
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from math import gcd, isqrt, prod
from pathlib import Path
CHECKS=0

def check(ok:bool,label:str)->None:
    global CHECKS
    CHECKS+=1
    if not ok: raise ArithmeticError(label)

@lru_cache(None)
def factor(n:int)->tuple[tuple[int,int],...]:
    if n<1: raise ValueError('factor input must be positive')
    out=[];d=2
    while d*d<=n:
        e=0
        while n%d==0:n//=d;e+=1
        if e:out.append((d,e))
        d=3 if d==2 else d+2
    if n>1:out.append((n,1))
    return tuple(out)

def prime(n:int)->bool:return n>1 and factor(n)==((n,1),)
def sieve(n:int)->list[int]:
    if n<2:return []
    a=bytearray(b'\1')*(n+1);a[:2]=b'\0\0'
    for d in range(2,isqrt(n)+1):
        if a[d]:a[d*d::d]=b'\0'*((n-d*d)//d+1)
    return [d for d in range(2,n+1) if a[d]]

def ds(fs)->list[int]:
    out=[1]
    for q,e in fs:out=[a*q**j for a in out for j in range(e+1)]
    return sorted(out)
@lru_cache(None)
def divs(n:int)->tuple[int,...]:return tuple(ds(factor(n)))
def square_divs(n:int)->list[int]:return ds([(q,2*e) for q,e in factor(n)])
def tau(n:int)->int:return prod(e+1 for _,e in factor(n))
def mobius(n:int)->int:
    fs=factor(n)
    return 0 if any(e>1 for _,e in fs) else (-1)**len(fs)
def leg(a:int,p:int)->int:
    z=pow(a%p,(p-1)//2,p)
    return -1 if z==p-1 else z

def jac(a:int,n:int)->int:
    if n<1 or n%2==0:raise ValueError('positive odd modulus required')
    a%=n;s=1
    while a:
        while a%2==0:
            a//=2
            if n%8 in (3,5):s=-s
        a,n=n,a
        if a%4==n%4==3:s=-s
        a%=n
    return s if n==1 else 0

def exponents(n:int,fs)->list[int]:
    out=[]
    for q,e in fs:
        k=0
        while n%q==0:n//=q;k+=1
        out.append(k)
    check(n==1,'complete exponent vector')
    return out

def norm(a:int,u:int)->tuple[int,int,int]:
    if u<1 or a*a%u:raise ValueError('original square divisor required')
    d=gcd(a,u)
    check(d*d%u==0,'integral gcd normalization')
    h,r,s=d*d//u,u//d,a//d
    check(h*r*s==a and h*r*r==u and gcd(r,s)==1,'normalization inverse')
    return h,r,s

def state(p:int,R:int,u:int,channel:str)->dict:
    a=(p+R)//4
    check(4*a==p+R and R>0 and gcd(p*a,R)==1,'original source domain')
    h,r,s=norm(a,u)
    if channel=='E':
        check((p*r+s)%R==0,'E gate')
        k=(p*r+s)//R;den=[a,h*s*k,p*h*r*k]
        check(a*a==u*(R*den[1]-p*a),'E ordered inverse')
        extra={'kappa':k}
    elif channel=='M':
        check((r+s)%R==0,'M gate')
        k=(r+s)//R;den=[a,p*h*s*k,p*h*r*k]
        check(p*a*a==u*(R*den[1]-p*a),'M ordered inverse')
        extra={'lambda':k}
    else:raise ValueError('channel E or M required')
    x,y,z=den
    check(min(den)>0 and 4*x*y*z==p*(x*y+x*z+y*z),'positive reciprocal identity')
    fs=factor(a);f=exponents(u,fs)
    return dict(p=p,R=R,a=a,u=u,h=h,r=r,s=s,channel=channel,
                denominators=den,factors=list(map(list,fs)),exponents=f,
                beta=[b-e for b,(_,e) in zip(f,fs)],**extra)

def local(p:int,R:int,record:bool=False)->dict:
    a=(p+R)//4;fs=factor(a);cells=[];hits={'E':[],'M':[]};ca=leg(a,p)
    qr=nr=0
    for u in square_divs(a):
        cu=leg(u,p);check(cu==jac(u,R),'original factorwise reciprocity')
        qr+=cu==1;nr+=cu==-1
        E=(4*u+1)%R==0;M=(4*u+p)%R==0
        if E:
            check(cu==-1,'E has negative square class')
            z=state(p,R,u,'E');check(leg(z['h'],p)==-1,'E normalized h character');hits['E'].append(z)
        if M:
            check(cu==-ca,'M has required square class')
            z=state(p,R,u,'M');check(leg(z['h'],p)==-ca,'M normalized h character');hits['M'].append(z)
        if record:
            f=exponents(u,fs)
            cells.append(dict(u=u,exponents=f,beta=[b-e for b,(_,e) in zip(f,fs)],
                              chi_p=cu,residue=u%R,centered=u*pow(a,-1,R)%R,E=E,M=M))
    total=tau(a*a);delta=prod(2*e+1 for r,e in fs if leg(r,p)==1)
    check(qr==(total+delta)//2 and nr==(total-delta)//2,'exact signed source masses')
    return dict(p=p,R=R,a=a,chi_a=ca,factors=list(map(list,fs)),mass=total,qr=qr,nr=nr,
                hits=hits,**({'cells':cells} if record else {}))

def obstruction(N:int,D:int)->dict:
    mu=Counter(u*pow(N,-1,D)%D for u in square_divs(N));W=set(mu)
    K=sorted(k for k in W if {k*w%D for w in W}==W)
    check(all(mu[r]==mu[pow(r,-1,D)] for r in W),'fine inversion multiplicities')
    return dict(support=sorted(W),fine_counts=[[r,mu[r]] for r in sorted(W)],K=K)

def dual_state(p:int,D:int,w:int)->dict:
    B=(p*D+1)//4
    check(4*B==p*D+1 and (w+B)%D==0,'reciprocal source gate')
    h,r,s=norm(B,w);rin,sin=r,s
    check((r+s)%D==0,'reciprocal coprime pair gate')
    lam=(r+s)//D;swap=r>s
    if swap:r,s=s,r
    check(r<s and lam>0 and gcd(r,lam)==gcd(s,lam)==1,'reciprocal orientation')
    x=h*r*lam;R=4*x-p
    check(p<4*x<2*p,'reciprocal return first half')
    z=state(p,R,h*r*r,'E')
    check(z['s']==lam and z['kappa']==s and z['denominators']==[x,h*s*lam,p*B], 'reciprocal coordinate return')
    check(4*z['u']+1==R*D and z['h']*z['r']*z['kappa']==B,'reciprocal inverse')
    return dict(p=p,D=D,B=B,w=w,input_h=h,input_r=rin,input_s=sin,lambda_=lam,
                swapped=swap,original=z)

def dual_local(p:int,D:int,record:bool=False)->dict:
    B=(p*D+1)//4;fs=factor(B);cells=[];hits=[]
    check(4*B==p*D+1 and gcd(p*D,B)==1,'reciprocal source units')
    check(leg(B,p)==1,'reciprocal total character')
    for w in square_divs(B):
        cw=leg(w,p);check(cw==jac(w,D),'reciprocal factorwise character')
        yes=(w+B)%D==0
        if yes:
            check(cw==-1,'reciprocal hit negative class');hits.append(dual_state(p,D,w))
        if record:
            f=exponents(w,fs)
            cells.append(dict(w=w,exponents=f,beta=[b-e for b,(_,e) in zip(f,fs)],
                              chi_p=cw,residue=w%D,centered=w*pow(B,-1,D)%D,hit=yes))
    check(len(hits)%2==0,'reciprocal complementary fibres even')
    return dict(p=p,D=D,B=B,factors=list(map(list,fs)),mass=tau(B*B),
                nr_factors=[[r,e,r<p] for r,e in fs if leg(r,p)==-1],hits=hits,
                **({'cells':cells,**obstruction(B,D)} if record else {}))

@lru_cache(None)
def pair_count(p:int,R:int,N:int)->int:
    hist=Counter(d%R for d in divs(p*N))
    return sum(c*hist.get(-r%R,0) for r,c in hist.items())

def primitive_aux(p:int,R:int,N:int)->int:
    count=0
    for u in square_divs(N):
        d=gcd(N,u);r,s=u//d,N//d
        count+=(r+s)%R==0
        count+=(p*r+s)%R==0
    return count

def pair_fibres(p:int,R:int,data:dict,record:bool=False)->dict:
    a=data['a'];counts=Counter();weights=defaultdict(Fraction);pairs=[]
    for b in divs(p*a):
        for c in divs(p*a):
            if (b+c)%R:continue
            g=gcd(b,c);x,y=b//g,c//g
            if x%p and y%p:
                ch='M';r,s=x,y;eps=int(g%p==0);d=g//(p if eps else 1)
                mark='both' if eps else 'neither'
            else:
                ch='E';d=g
                if x%p==0:r,s=x//p,y;mark='first'
                else:r,s=y//p,x;mark='second'
            check(a%(r*s)==0,'pair primitive product available')
            h=a//(r*s);u=h*r*r
            check(h%d==0,'pair common divisor fibre')
            if ch=='M':rebuilt=(d*(p if eps else 1)*r,d*(p if eps else 1)*s)
            else:rebuilt=(d*p*r,d*s) if mark=='first' else (d*s,d*p*r)
            check(rebuilt==(b,c),'pair original inverse')
            check((r+s)%R==0 if ch=='M' else (p*r+s)%R==0,'pair channel gate')
            counts[ch,u]+=1;weights[ch,u]+=Fraction(1,2*tau(h))
            if record:pairs.append(dict(left=b,right=c,gcd=g,channel=ch,u=u,h=h,r=r,s=s,
                                        common_divisor=d,p_mark=mark,fibre_size=2*tau(h)))
    expected={(ch,z['u']):2*tau(z['h']) for ch in ('E','M') for z in data['hits'][ch]}
    check(dict(counts)==expected,'full pair fibre sizes')
    check(all(w==1 for w in weights.values()),'exact fibre weights')
    T=sum(counts.values());F=sum(len(data['hits'][ch]) for ch in ('E','M'))
    check(T==pair_count(p,R,a),'histogram pair count')
    inv=sum(mobius(d)*pair_count(p,R,a//d) for d in divs(a))
    check(inv==2*F,'Mobius exact selector count')
    check(primitive_aux(p,R,a)==F,'auxiliary becomes actual only at shell')
    B0=sum((b+c)%R==0 for b in divs(a) for c in divs(a))
    B1=sum((b+p*c)%R==0 for b in divs(a) for c in divs(a))
    check(B0==sum(tau(z['h']) for z in data['hits']['M']),'M diagonal colour fibre')
    check(B1==sum(tau(z['h']) for z in data['hits']['E']),'E offdiagonal colour fibre')
    return dict(p=p,R=R,a=a,T=T,F=F,B0=B0,B1=B1,
                primitive_terms=[[d,mobius(d),pair_count(p,R,a//d)] for d in divs(a)],
                fibres=[[ch,u,n] for (ch,u),n in sorted(counts.items())],
                **({'pairs':pairs} if record else {}))

def overlap_test(p:int,D:int)->dict:
    A=(p+D)//4;B=(p*D+1)//4;g=gcd(A,B)
    check(g==gcd(A,(D*D-1)//4),'exact source intersection')
    eps=[]
    for r,e in factor(g):
        if leg(r,p)==-1:
            check(r%4==3 and (p+1)%r==0,'common nonresidue endpoint constraint')
            if r<p:eps.append(state(p,r,(p+r)//4,'E'))
    return dict(p=p,D=D,A=A,B=B,gcd=g,endpoint_returns=eps)

def square_fixture()->dict:
    p=12889;check(prime(p),'fixture hard prime');rows=[]
    for q in (43,61):
        sig=1 if q%4==3 else 3
        check(prime(q) and leg(q,p)==-1,'fixture original vertices')
        valid=range(1,isqrt((3*p-1)//(sig*q))+1,2)
        for t in valid:
            D=sig*q*t*t;A=local(p,D,True);B=dual_local(p,D,True)
            R0=sig*q
            for cell in A['cells']:
                carries={}
                for channel,eta in [('E',1),('M',p)]:
                    num=4*cell['u']+eta
                    if num%R0==0:
                        carry=num//R0;digit=carry%(t*t);quot=carry//(t*t)
                        check((R0*(digit+t*t*quot)-eta)//4==cell['u'],'original square carry inverse')
                        carries[channel]=dict(k=carry,digit=digit,quotient=quot,modulus=t*t)
                    else:carries[channel]=None
                cell['base_carries']=carries
            for cell in B['cells']:
                num=4*cell['w']+1
                if num%R0==0:
                    carry=num//R0;digit=carry%(t*t);quot=carry//(t*t)
                    check((R0*(digit+t*t*quot)-1)//4==cell['w'],'reciprocal square carry inverse')
                    cell['base_carry']=dict(k=carry,digit=digit,quotient=quot,modulus=t*t)
                else:cell['base_carry']=None
            check(not A['hits']['E'] and not A['hits']['M'] and not B['hits'],'paired complete local failure')
            check(A['chi_a']==-1,'negative square source')
            edges=[[r,e] for r,e in factor(A['a']) if leg(r,p)==-1]
            if t==1:
                check(edges==[[61 if q==43 else 43,1]],'canonical complete successor')
                check(not B['nr_factors'],'reciprocal canonical has no NR edge')
            overlap=overlap_test(p,D)
            check(not overlap['endpoint_returns'],'no nonresidue common factor')
            common=set(square_divs(overlap['gcd']))
            check(common==set(square_divs(A['a']))&set(square_divs(B['B'])),'complete paired common divisor domain')
            rows.append(dict(q=q,sigma=sig,t=t,D=D,original=A,reciprocal=B,
                             edges=edges,overlap=overlap))
    check(len(rows)==22 and sum(x['original']['mass'] for x in rows)==246,'complete source range')
    check(sum(x['reciprocal']['mass'] for x in rows)==600,'complete reciprocal source mass')
    K=local(p,31,True)
    m=next(x for x in K['hits']['M'] if x['u']==25)
    e=next(x for x in K['hits']['E'] if x['u']==85)
    check(Fraction(e['u'],m['u'])==Fraction(17,5),'actual parity changing ratio')
    check(leg(17,p)*leg(5,p)==-1 and 17*pow(5,-1,31)%31==pow(p,-1,31),'ratio sign and target')
    path=next(x for x in rows if x['q']==61 and x['t']==11)
    check(any(r==31 for r,_,_ in path['reciprocal']['nr_factors']),'actual reciprocal factor path')
    pf=pair_fibres(p,31,K,True)
    return dict(p=p,vertices=[43,61],rows=rows,direct_mass=sum(x['original']['mass'] for x in rows),
                reciprocal_mass=sum(x['reciprocal']['mass'] for x in rows),
                gate_families=66,source_boxes=44,
                positive_exchange=dict(M=m,E=e,pair_fibres=pf,ratio=[17,5],
                                       incoming=dict(q=61,t=11,D=path['D'],B=path['reciprocal']['B'],factor=31)),
                scope='All valid square ports at these two vertices only; not an all-graph failure certificate.')

def reciprocal_complete(bound:int=97)->dict:
    rows=[]
    for p in sieve(bound):
        if p%4!=1:continue
        actual=[]
        for a in range(p//4+1,p//2+1):
            R=4*a-p
            for u in square_divs(a):
                if (4*u+1)%R==0:actual.append((R,u))
        cap=(p*p+6*p+13)//12;returned=[];total=0
        for D in range(3,cap+1,4):
            B=(p*D+1)//4
            for w in square_divs(B):
                if (w+B)%D==0:
                    z=dual_state(p,D,w)['original'];returned.append((z['R'],z['u']));total+=1
        check(Counter(returned)==Counter({z:2 for z in actual}),'complete reciprocal finite atlas')
        rows.append(dict(p=p,D_bound=cap,exterior_states=len(actual),reciprocal_oriented_states=total))
    return dict(bound=bound,rows=rows)

def overlap_complete(bound:int=1000)->dict:
    rows=[]
    for p in sieve(bound):
        if p%8!=1:continue
        endpoint=[q for q,_ in factor(p+1) if q%4==3]
        found=[]
        for D in range(3,3*p,4):
            z=overlap_test(p,D)
            if z['endpoint_returns']:found.append(D)
        check(bool(endpoint)==bool(found),'overlap iff old endpoint')
        if endpoint:
            ell=min(endpoint);D=2*ell+1
            check(ell*ell<=(p+1)//2 and D<p,'bounded converse endpoint source')
            check(D in found,'converse original overlap')
        rows.append(dict(p=p,endpoint_primes=endpoint,overlap_moduli=found))
    return dict(bound=bound,rows=rows)

def Fourier_group_ring_test()->dict:
    # Exact coefficient analogue of the character formula; no complex approximations.
    ncase=0
    for mod in range(3,80,2):
        units=[x for x in range(1,mod) if gcd(x,mod)==1]
        for x in units:
            for e in range(1,6):
                def corr(e):
                    counts=Counter(pow(x,j,mod) for j in range(e+1));out=Counter()
                    for a,ca in counts.items():
                        for b,cb in counts.items():out[a*pow(b,-1,mod)%mod]+=ca*cb
                    return out
                A,B=corr(e),corr(e-1);D=Counter(pow(x,j,mod) for j in range(-e,e+1))
                check(all(A[r]-B[r]==D[r] for r in units),'Fejer difference equals original centered count')
                ncase+=1
    return dict(cases=ncase,scope='Exact group-ring local identity, not numerical Fourier rounding.')

def negative_controls()->list[str]:
    cases=[]
    def reject(label,fn):
        try:fn()
        except (ArithmeticError,ValueError,ZeroDivisionError):cases.append(label);return
        raise ArithmeticError('negative control accepted: '+label)
    p=12889
    reject('same divisor cannot change negative-source channel',lambda: check(leg(85,p)==1,'false M parity'))
    z=local(193,7);P=pair_fibres(193,7,z)
    reject('unweighted pair half-count is not original state count',lambda:check(P['T']==2*P['F'],'false raw-pair normalization'))
    reject('reciprocal NR factor does not imply reciprocal hit',lambda:check(bool(dual_local(p,387)['hits']),'false reciprocal forcing'))
    reject('dual distinguished denominator is not original shell denominator',lambda:check((p+11)//4==(p*11+1)//4,'false dual source identity'))
    reject('lcm projection does not impose residual product',lambda:check((4*1845+1)%1331==0,'false full square gate'))
    reject('selected word must stay in its exponent box',lambda:norm(3230,85*17*17))
    reject('endpoint escape cannot be forced at every prime',lambda:check(any(q%4==3 for q,_ in factor(p+1)),'false universal endpoint'))
    reject('unsigned Mobius sum is not the primitive count',lambda:check(sum(abs(mobius(d))*pair_count(193,7,50//d) for d in divs(50))==2*P['F'],'false removal of Mobius signs'))
    return cases

def write_json(path:Path,data):
    path.write_text(json.dumps(data,sort_keys=True,separators=(',',':'))+'\n')

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--bound',type=int,default=1000);ap.add_argument('--out',default='certificates');args=ap.parse_args()
    if args.bound<97:ap.error('bound must be at least 97')
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    rows=[];stats=Counter();digest=hashlib.sha256()
    for p in sieve(args.bound):
        if p%4!=1:continue
        stats['primes']+=1
        for a in range(p//4+1,p//2+1):
            R=4*a-p;L=local(p,R);P=pair_fibres(p,R,L)
            row=dict(p=p,a=a,R=R,mass=L['mass'],chi_a=L['chi_a'],E=len(L['hits']['E']),M=len(L['hits']['M']),
                     T=P['T'],B0=P['B0'],B1=P['B1'],F=P['F'])
            rows.append(row);digest.update((json.dumps(row,sort_keys=True,separators=(',',':'))+'\n').encode())
            stats['shells']+=1;stats['divisor_vectors']+=L['mass'];stats['E_states']+=row['E'];stats['M_states']+=row['M'];stats['successful_ordered_pairs']+=row['T']
            if row['E'] or row['M']:stats['occupied_shells']+=1
            if row['B1']>row['B0']:stats['indefinite_colour_matrices']+=1
    scan=dict(bound=args.bound,statistics=dict(stats),rows=rows,row_sha256=digest.hexdigest())
    write_json(out/'scan.json',scan)
    fixture=square_fixture();write_json(out/'paired_sources.json',fixture)
    rec=reciprocal_complete();write_json(out/'reciprocal_atlas.json',rec)
    ov=overlap_complete(min(args.bound,1000));write_json(out/'overlap.json',ov)
    gr=Fourier_group_ring_test();write_json(out/'group_ring.json',gr)
    neg=negative_controls();write_json(out/'negative_controls.json',neg)
    z=local(193,7,True);write_json(out/'pair_fibre_example.json',dict(source=z,pairs=pair_fibres(193,7,z,True)))
    summary=dict(checks=CHECKS,negative_controls=len(neg),statistics=dict(stats),row_sha256=digest.hexdigest(),
                 paired_source_boxes=fixture['source_boxes'],paired_direct_mass=fixture['direct_mass'],paired_reciprocal_mass=fixture['reciprocal_mass'])
    write_json(out/'summary.json',summary);print(json.dumps(summary,sort_keys=True))

if __name__=='__main__':main()
