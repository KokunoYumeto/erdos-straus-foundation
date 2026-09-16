#!/usr/bin/env python3
"""Independent certificate checker: does not import verify.py.

Uses modular powering, direct digit lifting, determinant tests, explicit
cofactor enumeration and rational interval arithmetic. It does not prove
Chim's imported theorem and does not enumerate the huge threshold moduli.
"""
import argparse,json
from fractions import Fraction as Q
from math import gcd,isqrt
from pathlib import Path

COUNT=0

def require(ok,label):
    global COUNT
    COUNT+=1
    if not ok:raise ArithmeticError(label)

def dec(x):
    if isinstance(x,dict):
        if set(x)=={'n','d'}:return Q(x['n'],x['d'])
        return {k:dec(v) for k,v in x.items()}
    if isinstance(x,list):return [dec(v) for v in x]
    return x

def dot(a,b):return a[0]*b[0]+a[1]*b[1]
def cross(a,b):return a[0]*b[1]-a[1]*b[0]

def lift(k):
    j=1
    for n in range(4,k+1):
        if pow(3,j,1<<n)!=11%(1<<n):j+=1<<(n-3)
        require(pow(3,j,1<<n)==11%(1<<n),'direct_digit_lift')
    return j

def log_enclosure(x,n):
    z=(x-1)/(x+1);P=z;s=Q()
    for j in range(n):
        s+=P/Q(2*j+1);P*=z*z
    return 2*s,2*s+2*P/(Q(2*n+1)*(1-z*z))

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--input',default='certificates')
    ap.add_argument('--out',default='independent.json');args=ap.parse_args();root=Path(args.input)
    read=lambda f:dec(json.loads((root/f).read_text()))
    constants=read('constants.json')
    a,b=log_enclosure(Q(2),16);c,d=log_enclosure(Q(3,2),16);e,f=log_enclosure(Q(11,8),16)
    enclosures={'log2':(a,b),'log3':(a+c,b+d),'log11':(3*a+e,3*b+f)}
    for name,(lo,hi) in enclosures.items():
        L,U=constants['coarse_intervals'][name]
        require(L<lo<hi<U,'separate_log_series_constants')
    l2,u2=constants['coarse_intervals']['log2'];l3,u3=constants['coarse_intervals']['log3'];l11,u11=constants['coarse_intervals']['log11']
    for row in constants['variants']:
        coef=2*row['C2']*(2*u2+row['x3'])*u3*u11/l2**3
        maximum=max(row['x1']*u2,row['x2']*(2*u2+row['x3'])*u2)
        require(coef<row['C'] and maximum<row['H'],'specialization_bounds')
        require(row['onset']==row['C']*row['H'] and row['C']*u2<row['denominator'],'exact_cutoff_parameters')
    require(u2*(1/l11+1/l3)<1,'original_heights')
    bases=read('bases.json');nwords=0
    for row in bases:
        k=row['k'];m=1<<k;o=1<<(k-2);j=row['J'];v,w=row['basis']
        require(0<=j<o and pow(3,j,m)==11%m,'large_exact_log_certificate')
        require(row['o']==o and abs(cross(v,w))==o,'exact_full_lattice_index')
        require(all((a+j*b)%o==0 for a,b in (v,w)),'coordinate_relations')
        require(dot(v,v)<=dot(w,w) and 2*abs(dot(v,w))<=dot(v,v),'reduction_conditions')
        require(row['shortest_squared']==dot(v,v),'shortest_metadata')
        widths=[abs(v[i])+abs(w[i]) for i in range(2)]
        require(widths==row['widths'],'retained_widths')
        # Verify the unimodular construction trace against the original basis.
        x,y=(o,0),(-j,1)
        for op in row['reduction_trace']:
            if op==['swap']:x,y=y,x
            else:
                require(op[0]=='subtract','trace_opcode')
                y=(y[0]-op[1]*x[0],y[1]-op[1]*x[1])
        require([list(x),list(y)]==row['basis'],'full_basis_trace_inverse')
        if k<=128:require(lift(k)==j,'independent_log_not_log_series')
        if k<=12:
            residues=set()
            for r in range(widths[0]+1):
                for s in range(widths[1]+1):
                    residues.add((pow(3,r,m)*pow(11,s,m))%m);nwords+=1
            expected={a for a in range(1,m,2) if a%8 in (1,3)}
            require(residues==expected,'literal_multiplicative_full_coverage')
    ex=read('examples.json')
    for label in ('inherited_prime','proper_relative_integer'):
        st=ex[label];p=st['p'];k=st['k'];u=st['u'];N=p+4*u;R=st['R'];q=st['Q'];a=st['a']
        require(u==1<<(2*k-5) and N==st['N'] and N==R*q,'original_factor_return')
        require(q%(1<<k)==(1<<k)-1 and a==(p+R)//4,'original_shell')
        h,r,s,L=st['h'],st['r'],st['s'],st['quotient'];x,y,z=st['denominators']
        require((h*r*s,h*r*r,r+s)==(a,u,R*L),'normalization_and_gate')
        require((x,y,z)==(a,p*h*s*L,p*h*r*L),'ordered_denominators')
        require(4*x*y*z==p*(x*y+x*z+y*z),'cleared_ES_identity')
        require(Q(p*a*a,R*y-p*a)==u,'original_divisor_inverse')
    p=ex['inherited_prime']['p']
    require(all(p%d for d in range(2,isqrt(p)+1)),'separate_full_primality_trial')
    actual=[(i,j,3**i*11**j*37) for i in range(8) for j in range(6) if (3**i*11**j*37)%64==63]
    require([(i,j) for i,j,q in actual]==[(1,4),(6,1)],'full_original_example_fibre')
    rel=ex['proper_relative_integer']['origin']['relative'];k=rel['k'];v=rel['relative_shift'];d=rel['d'];h=k-v
    require(d==1<<v and h==rel['effective_precision'],'relative_precisions')
    i,j=rel['high']['word'];r,s=rel['low_digits'];I,J=rel['original_word']
    require((I,J)==(r+d*i,s+d*j),'original_relative_digit_return')
    require((pow(3,I,1<<k)*pow(11,J,1<<k)*31)%(1<<k)==(1<<k)-1,'relative_original_target_direct')
    bad=ex['empty_branch'];P=bad['p'];N=P+512
    ds=[3**i*11**j*13**s for i in range(4) for j in range(2) for s in range(3)]
    require(N==3**3*11*13**2 and all(q%64!=63 for q in ds),'empty_branch_exhaustive')
    x,y,z=bad['other_denominators'];require(4*x*y*z==P*(x*y+x*z+y*z),'empty_branch_not_ES_counterexample')
    out=dict(checks=COUNT,basis_certificates=len(bases),largest_verified_k=max(x['k'] for x in bases),
             direct_words=nwords,imports_main=False,
             scope='Verifies certificates, not imported Chim theorem; no giant threshold modulus expanded')
    Path(args.out).write_text(json.dumps(out,sort_keys=True,indent=2)+'\n');print(json.dumps(out,sort_keys=True))
if __name__=='__main__':main()
