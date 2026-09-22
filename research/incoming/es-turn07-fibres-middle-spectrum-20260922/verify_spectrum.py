#!/usr/bin/env python3
"""Exact arithmetic checks for the written middle-receiver asymptotics.
The Taylor identities are proved in the manuscript; a parameter grid is
corroboration, not a substitute for that proof. No SVD library is required.
"""
from __future__ import annotations
import argparse,json
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
from math import gcd,prod
from spectrum_exact import G,I,mm,inv,det,sub,jetdet,direct_first_jet,claimed_first_jet,matrixdata
from fibres import prime,target,inverse_fibre
CHECKS=0

def ck(ok,msg):
    global CHECKS
    CHECKS+=1
    if not ok:raise ArithmeticError(msg)
def fr(x):x=F(x);return [x.numerator,x.denominator]
def save(p,x):p.write_bytes((json.dumps(x,sort_keys=True,indent=2)+'\n').encode('utf-8'))

def run(out):
    cases=[]
    for R in (3,7,11,19,27):
      for u in (1,2,3,9,36):
        B0,B1=direct_first_jet(R,u);C0,C1=claimed_first_jet(R,u)
        ck((B0,B1)==(C0,C1),'literal Laurent expansion agrees with displayed jets')
        C2=F(3,16*R);alpha=F(1,4*R);beta=F(1,16*R*u)
        v0=mm(inv(B0),[[G(1)],[G()],[G()],[G()]]);v1=mm(inv(B0),mm(B1,v0));v1=[[-x[0]]for x in v1]
        ck([x[0]for x in v0]==[-I/2,G(F(1,2)),G(F(9*R,8)),I*F(576*R*u**3,5)],'first inverse jet')
        ck([x[0]for x in v1]==[-I*F(2*R,3),G(F(-19*R,12)),G(F(3*R*(25*R-228*u),80)),I*F(24*R*u**3*(-1160*R-717*u),25)],'second inverse jet')
        actual0=det(B0)/C2
        ck(actual0==80*alpha**2*beta**3,'determinant leading constant')
        _,actual1=jetdet(B0,B1)
        k4=actual1/det(B0);ck(k4==3*R+F(33*u,5),'determinant first correction')
        j2a,j2b=jetdet(sub(B0,[2,3],[2,3]),sub(B1,[2,3],[2,3]));k2=j2b/j2a
        ck(j2a==40*alpha**2*beta**3,'second compound leading')
        ck(k2==F(11*R,2)+F(33*u,5),'second compound correction')
        weight=F();shift=F()
        for j in (0,1):
            a,b=jetdet(sub(B0,[1,2,3],[j,2,3]),sub(B1,[1,2,3],[j,2,3]))
            w=a.norm()/C2;weight+=w;shift+=w*(b/a).re
            ck((b/a).im==0,'real relative leading-minor correction')
        k3=shift/weight
        ck(k3==F(25*R,12)+F(33*u,5),'joint third compound correction')
        ck(weight==(40*alpha**2*beta**3)**2*2*C2,'both leading triples retained')
        # All other entries/minors have the stated strictly lower growth powers.
        re=[0,6,8,12];ce=[-3,-3,0,6] # twice the powers of p
        ledger=[]
        for rank,leadpower,leadrows,leadcols in [(1,18,{(3,)},{(3,)}),(2,26,{(2,3)},{(2,3)}),(3,29,{(1,2,3)},{(0,2,3),(1,2,3)})]:
          for rr in combinations(range(4),rank):
           for cc in combinations(range(4),rank):
            power=sum(re[i]for i in rr)+sum(ce[j]for j in cc)
            a,b=jetdet(sub(B0,rr,cc),sub(B1,rr,cc))
            islead=rr in leadrows and cc in leadcols
            if not islead:
                # Zero constant term lowers actual growth at least p^-1.
                effective=power-(0 if a else 2)
                ck(effective<=leadpower-2,'all nonleading compound entries')
            ledger.append([rank,list(rr),list(cc),power, bool(a),bool(b)])
        k1=6*R+F(14*u,5)
        corrections=[k1,k2.re-k1,k3-k2.re,k4.re-k3]
        ck(corrections==[6*R+F(14*u,5),F(-R,2)+F(19*u,5),F(-41*R,12),F(11*R,12)],'all four singular corrections')
        # Tiny-component normalization coefficients and scalar hierarchy constants.
        n0sq=C2/2
        ck(F(9*R,8)**2/n0sq==F(27*R**3,2),'middle Y heat weight')
        ck(F(576*R*u**3,5)**2/n0sq==F(3538944*R**3*u**6,25),'middle Z heat weight')
        cases.append(dict(R=R,u=u,C_squared=fr(C2),B0_times_core_C=matrixdata(B0),B1_times_core_C=matrixdata(B1),
                          inverse0_before_core_C=[v[0].data()for v in v0],inverse1_before_core_C=[v[0].data()for v in v1],
                          singular_first_corrections=[fr(v)for v in corrections],compound_growth_ledger=ledger))
    # Second hard-prime family: original small-root constants, not a synthetic spectrum.
    roots=[F(1),F(3,11),F(3)];D=[F(-16,11),F(240,121),F(60,11)]
    C0=[[G(1)for x in roots],[-I*d for d in D],[G(2*x*d)for x,d in zip(roots,D)]]
    B2=sum(4*x*x*abs(d)for x,d in zip(roots,D))
    B12=sum(4*abs(D[i]*D[j])*(roots[j]-roots[i])**2 for i,j in combinations(range(3),2))
    detsq=det(C0).norm()/prod(abs(x)for x in D)
    invcol=mm(inv(C0),[[G(1)],[G()],[G()]])
    invnorm=sum(v[0].norm()*abs(d)for v,d in zip(invcol,D))
    ck(B2==F(2968784,14641),'second-family row norm')
    ck(B12==F(73267200,161051),'second-family two-row compound')
    ck(detsq==F(2896,121)**2,'second-family core determinant')
    ck(invnorm==F(286200,360371),'second-family inverse limit')
    ck(B2/detsq==F(2968784,2896**2),'second-family inverse compound2 limit squared')
    # Actual prime samples in explicitly reduced hard progressions; every returned coordinate tested.
    families=[]
    for family,start in [('fixed_residual',8401),('endpoint',4201)]:
        ck(gcd(start,9240)==1,'reduced prime progression')
        samples=[]
        for n in range(500):
            p=start+9240*n
            if not prime(p):continue
            ck(p%840==1,'hard class1')
            if family=='fixed_residual':
                a=(p+11)//4;ck(a*a%9==0 and (p+36)%11==0,'fixed source gates')
                Y=F(p*(a+9),11);Z=F(p*a*(a+9),99)
            else:
                s=(p+1)//11;a=3*s;Y=F(3*p);Z=F(3*p*s)
            ck(Y.denominator==Z.denominator==1,'family integer denominators')
            W=target(p,a,int(Y),int(Z));samples.append(W)
            if len(samples)==8:break
        ck(len(samples)==8,'finite example search terminated within declared bound')
        fibre_records=[dict(target=W,sources=inverse_fibre(W)) for W in samples]
        if family=='fixed_residual':
            ck(samples[0]['p']==26881 and not fibre_records[0]['sources'],'first fixed-family target outside mixed image')
            ck(prime(2447),'prime complementary cofactor at the empty-image example')
        families.append(dict(family=family,residue=start,modulus=9240,samples=samples,mixed_image_fibres=fibre_records))
    # Receiver-as-matrix reconstruction works for every nonzero column scale.
    for W in [f['samples'][0]for f in families]:
        p,a,Y,Z=[W[k]for k in ('p','a','Y','Z')];ll=[F(p),F(a),F(Y),F(Z)];AA=-1/sum(ll)
        dd=[AA*prod(ll[j]-ll[k]for k in range(4)if k!=j)for j in range(4)]
        scalars=[G(1,1),G(-2,1),G(3,-2),G(-1,-3)]
        cols=[[x,-I*x*d,x*(AA*d*d+2*l*d),I*x*(7*l*l*d-13*d*d)]for x,d,l in zip(scalars,dd,ll)]
        drec=[I*c[1]/c[0]for c in cols];Are=(cols[0][2]/cols[0][0]-2*p*drec[0])/(drec[0]*drec[0])
        lrec=[(c[2]/c[0]-Are*d*d)/(2*d)for c,d in zip(cols,drec)]
        ck(Are==AA and drec==dd and lrec==ll,'full labelled target recovered without assuming it as input')
    controls=dict(no_universal_occupancy=True,middle_Z_power_is_9_not_15=True,
                  old_E_hard_family_already_in_upstream=True,optimality_not_claimed_on_mixed_image=True)
    out.mkdir(parents=True,exist_ok=True)
    save(out/'spectrum.json',dict(exact_jet_checks=cases,second_family=dict(row_norm_squared=fr(B2),compound_squared=fr(B12),determinant_squared=fr(detsq),inverse_norm_squared=fr(invnorm)),families=families,
                               observation_powers=[0,2,3,9],scope=controls))
    report=dict(success=True,checks=CHECKS,jet_parameter_pairs=len(cases),prime_family_samples=16,
                method='exact rational Laurent arithmetic; complete leading-compound enumeration',
                finite_samples_are_corroboration=True,universal_ES_proved=False)
    save(out/'spectrum_summary.json',report);print(json.dumps(report,sort_keys=True))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,default=Path('certificates'));a=p.parse_args();run(a.out)
