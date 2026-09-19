#!/usr/bin/env python3
"""Portable complete 846-vector local certificate. Independent of verify.py."""
import json
from itertools import product
from math import gcd,isqrt,prod
from pathlib import Path
p=12889
DATA={43:[(1,[(127,1),(1091,1)]),(3,[(37,1),(33703,1)]),(5,[(3463919,1)]),(7,[(6789281,1)]),(9,[(11223097,1)]),(11,[(23,1),(728929,1)]),(13,[(97,1),(163,1),(1481,1)]),(15,[(31175269,1)]),(17,[(61,1),(131,1),(5011,1)]),(19,[(50018987,1)]),(21,[(59,1),(107,1),(9679,1)]),(23,[(421,1),(174101,1)]),(25,[(67,1),(709,1),(1823,1)]),(27,[(1433,1),(70487,1)]),(29,[(211,1),(269,1),(2053,1)])],61:[(1,[(2,3),(73709,1)]),(3,[(2,1),(151,1),(17573,1)]),(5,[(2,1),(691,1),(10667,1)]),(7,[(2,2),(317,1),(22787,1)]),(9,[(2,2),(11940853,1)]),(11,[(2,1),(19,1),(31,1),(37,1),(1637,1)]),(13,[(2,1),(1277,1),(39019,1)])]}

def need(ok,msg):
    if not ok:raise ArithmeticError(msg)
def prime(n):return n>1 and all(n%d for d in range(2,isqrt(n)+1))
def factor(n):
    out=[];d=2
    while d*d<=n:
        e=0
        while n%d==0:n//=d;e+=1
        if e:out.append((d,e))
        d+=1
    if n>1:out.append((n,1))
    return out

def vectors(fs):
    for f in product(*(range(2*e+1) for _,e in fs)):
        yield list(f),prod(q**a for a,(q,_) in zip(f,fs))

need(prime(p),'p prime');out=[];direct=dual=0
for q,entries in DATA.items():
    sig=1 if q%4==3 else 3
    need([t for t,_ in entries]==list(range(1,isqrt((3*p-1)//(sig*q))+1,2)),'complete valid t range')
    for t,fs in entries:
        D=sig*q*t*t;A=(p+D)//4;B=(p*D+1)//4
        need(prod(q**e for q,e in fs)==B,'reciprocal factor identity')
        need(all(prime(q) for q,_ in fs),'reciprocal prime factors')
        fA=factor(A);ca=[];cb=[]
        for f,u in vectors(fA):
            need((4*u+1)%D!=0 and (u+A)%D!=0,'direct E/M no hit')
            ca.append({'u':u,'f':f,'beta':[a-e for a,(_,e) in zip(f,fA)],'E_remainder':(4*u+1)%D,'M_remainder':(u+A)%D})
        for f,w in vectors(fs):
            need((w+B)%D!=0,'reciprocal no hit')
            cb.append({'w':w,'f':f,'beta':[a-e for a,(_,e) in zip(f,fs)],'remainder':(w+B)%D})
        direct+=len(ca);dual+=len(cb)
        out.append({'p':p,'q':q,'sigma':sig,'t':t,'R0':sig*q,'D':D,'A':A,'A_factors':fA,'B':B,'B_factors':fs,'direct_vectors':ca,'reciprocal_vectors':cb})
need(direct==246 and dual==600,'complete original vector masses')
positive=[]
for tag,u in [('M',25),('E',85)]:
    a=3230;R=31;d=gcd(a,u);h=d*d//u;r=u//d;s=a//d
    if tag=='M':
        k=(r+s)//R;den=[a,p*h*s*k,p*h*r*k]
    else:
        k=(p*r+s)//R;den=[a,h*s*k,p*h*r*k]
    x,y,z=den;need(4*x*y*z==p*(x*y+x*z+y*z),'positive original reciprocal identity')
    positive.append({'channel':tag,'u':u,'a':a,'R':R,'h':h,'r':r,'s':s,'quotient':k,'denominators':den})
overlap=[]
for tag,den in [('E',[253,87032,3818056]),('M',[253,2042216,88792])]:
    x,y,z=den
    need(4*x*y*z==1009*(x*y+x*z+y*z),'positive-source shared divisor return')
    overlap.append({'p':1009,'R':3,'a':253,'u':11,'channel':tag,'denominators':den})
result={'positive_source_overlap':overlap,'success':True,'p':p,'source_boxes':44,'labelled_gate_families':66,'direct_original_vectors':direct,'reciprocal_original_vectors':dual,'rows':out,'positive_exchange':positive,'scope':'All valid square ports at q43 and q61, not a full graph or an ES counterexample.'}
path=Path(__file__).with_name('local_certificate.json');path.write_text(json.dumps(result,sort_keys=True,separators=(',',':'))+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('rows','positive_exchange')},sort_keys=True))
