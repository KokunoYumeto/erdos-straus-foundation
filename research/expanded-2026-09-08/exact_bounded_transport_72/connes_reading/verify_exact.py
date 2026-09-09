"""Reproducible finite checks of proved statements; no external packages."""
from fractions import Fraction
from itertools import combinations, product
from math import gcd, isqrt, lcm
from pathlib import Path
import hashlib
import json

BASE = Path(__file__).resolve().parent

def divisors(n):
    out = set()
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            out.update((d, n // d))
    return sorted(out)

def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))

def pairs(p, a):
    R, S = 4*a-p, p*a
    D = divisors(S)
    return {(m,n) for m in D for n in D if gcd(m,n)==1 and (m+n)%R==0}

def witness_pair(p, a, m, n):
    R, S = 4*a-p, p*a
    assert S%(m*n)==0 and (m+n)%R==0
    k = (S//(m*n))*((m+n)//R)
    B, C = k*m, k*n
    assert k>0 and gcd(B,C)==k
    assert Fraction(1,a)+Fraction(1,B)+Fraction(1,C)==Fraction(4,p)
    return [B,C]

def em(p,a):
    R=4*a-p
    out={'E':[], 'M':[]}
    for u in divisors(a*a):
        if (4*u+1)%R==0:
            B,C = Fraction(p*(a+p*u),R),Fraction(p*a+a*a//u,R)
            assert B.denominator==C.denominator==1
            assert Fraction(1,a)+1/B+1/C==Fraction(4,p)
            out['E'].append({'u':u,'denominators':[a,int(B),int(C)]})
        if (u+a)%R==0:
            B,C = Fraction(p*(a+u),R),Fraction(p*(a+a*a//u),R)
            assert B.denominator==C.denominator==1
            assert Fraction(1,a)+1/B+1/C==Fraction(4,p)
            out['M'].append({'u':u,'denominators':[a,int(B),int(C)]})
    return out

def main():
    counts={'finite_group_pairs':0,'shell_pairs':0,'primitive_witnesses':0,
            'adjacent_shell_pairs':0,'abstract_pair_return_checks':0,
            'middle_divisor_primitive_returns':0,'marked_endpoint_successor_checks':0}
    for N,M in product(range(1,101),repeat=2):
        DN,DM=set(divisors(N)),set(divisors(M))
        assert DN&DM==set(divisors(gcd(N,M)))
        retained = {(u,int(v)) for u in DN
                    if (v:=Fraction(M*u,N)).denominator==1 and int(v) in DM}
        expected={(N//d,M//d) for d in divisors(gcd(N,M))}
        assert retained==expected
        counts['finite_group_pairs']+=1
    for p in (13,37,73):
        assert prime(p) and p%12==1
        h=(p-1)//12
        shells=list(range(3*h+1,9*h+1))
        P={a:pairs(p,a) for a in shells}
        for a in shells:
            em(p,a)
            for u in divisors(a*a):
                g=gcd(u,a)
                m,n=u//g,a//g
                assert a%m==a%n==0 and gcd(m,n)==1
                assert a*m//n==u and (a*m)%n==0
                assert ((u+a)%(4*a-p)==0)==((m+n)%(4*a-p)==0)
                counts['middle_divisor_primitive_returns']+=1
            for m,n in P[a]:
                witness_pair(p,a,m,n)
                counts['primitive_witnesses']+=1
        for a,b in product(shells,repeat=2):
            D=divisors(p*gcd(a,b))
            L=lcm(4*a-p,4*b-p)
            expected={(m,n) for m in D for n in D
                      if gcd(m,n)==1 and (m+n)%L==0}
            assert P[a]&P[b]==expected
            counts['shell_pairs']+=1
            for m,n in P[a]:
                mp,np=Fraction(b*m,a),Fraction(b*n,a)
                kept=(mp.denominator==np.denominator==1 and gcd(int(mp),int(np))==1)
                assert kept==(a==b)
                counts['abstract_pair_return_checks']+=1
    occupied_adjacent=[]
    successful_marked_endpoint_maps=[]
    for p in [x for x in range(13,1000,12) if prime(x)]:
        h=(p-1)//12
        for a in range(3*h+1,9*h):
            R=4*a-p
            # Enumerate exactly the primitive divisors in the embedded intersection H_p.
            actual={(m,n) for m,n in product((1,p),repeat=2)
                    if gcd(m,n)==1 and (m+n)%R==0 and (m+n)%(R+4)==0}
            expected={(1,p),(p,1)} if (p+1)%(R*(R+4))==0 else set()
            assert actual==expected
            counts['adjacent_shell_pairs']+=1
            if actual:
                occupied_adjacent.append({'p':p,'a':a,'R':R,'pairs':sorted(actual),
                    'witnesses':{str(t):witness_pair(p,t,p,1) for t in (a,a+1)}})
            assert (4*a*a+1)%R!=0
            assert (4*(a+1)**2+1)%(R+4)!=0
            middle_both=((a*a+a)%R==0 and ((a+1)**2+a+1)%(R+4)==0)
            assert middle_both==((p+4)%(R*(R+4))==0)
            counts['marked_endpoint_successor_checks']+=1
            if middle_both:
                t=((p+4)//(R*(R+4))-1)//4
                assert t>=0 and p==R*(R+4)*(4*t+1)-4
                assert a==R*(R+5)//4-1+R*(R+4)*t
                first=witness_pair(p,a,a,1)
                second=witness_pair(p,a+1,a+1,1)
                successful_marked_endpoint_maps.append({'p':p,'a':a,'R':R,'t':t,
                    'divisor_map':[a*a,(a+1)**2],
                    'primitive_shear':[[a,1],[a+1,1]],
                    'denominator_triples':[[a,*first],[a+1,*second]]})
    example={'p':13,'a4':em(13,4),'a5':em(13,5),
             'residue_fibres_mod3':{'1':[1,4,16],'2':[2,8]},
             'retained_integral_divisor_map':[[16,25]],
             'mark_coboundary_1_16':1}
    assert [x['u'] for x in example['a4']['E']]==[2,8]
    assert [x['u'] for x in example['a4']['M']]==[2,8]
    assert [x['u'] for x in example['a5']['E']]==[5]
    assert example['a5']['M']==[]
    report={'status':'passed','scope':'finite checks of proved identities; no universal ES claim',
            'counts':counts,'example':example,'adjacent_common_pair_examples':occupied_adjacent,
            'successful_marked_endpoint_maps':successful_marked_endpoint_maps,
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (BASE/'EXACT_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':report['status'],'counts':counts,
                      'adjacent_common_pair_examples':occupied_adjacent,
                      'successful_marked_endpoint_maps':successful_marked_endpoint_maps},indent=2))

if __name__=='__main__':
    main()
