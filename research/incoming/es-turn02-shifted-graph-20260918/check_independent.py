#!/usr/bin/env python3
"""Independent check: square-set characters, divisor recursion, Tarjan SCCs,
and synchronous distance relaxation. Imports no verifier or antecedent code.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction
from math import gcd,isqrt,prod
from pathlib import Path
import argparse,json,hashlib,sys
CHECKS=0

def demand(x,label):
    global CHECKS;CHECKS+=1
    if not x:raise ArithmeticError(label)

def tables(N):
    spf=list(range(N+1));spf[1]=1
    for x in range(2,isqrt(N)+1):
        if spf[x]==x:
            for y in range(x*x,N+1,x):
                if spf[y]==y:spf[y]=x
    return spf,[n for n in range(2,N+1) if spf[n]==n]

def factors(n,spf):
    out=[]
    while n>1:
        p=spf[n];e=0
        while n%p==0:n//=p;e+=1
        out.append((p,e))
    return out

def dsquare(fs):
    if not fs:return [1]
    q,e=fs[0];tail=dsquare(fs[1:]);out=[];pw=1
    for _ in range(2*e+1):
        out.extend(pw*t for t in tail);pw*=q
    return sorted(out)

def vertices(p,ps,spf):
    qr={i*i%p for i in range(1,(p+1)//2)}
    V=[q for q in ps if q<p and q not in qr];nodes={}
    for q in V:
        s=3 if q%4==1 else 1;R=s*q;a=(p+R)//4;fs=factors(a,spf);adj=[(r,e) for r,e in fs if r not in qr]
        E=[];M=[];cnt=0
        for u in dsquare(fs):
            cnt+=1
            for ch in ('E','M'):
                v=a*a//u
                Y=p*a+v if ch=='E' else p*(a+v)
                Z=p*a+p*p*u if ch=='E' else p*(a+u)
                if Y%R==Z%R==0:
                    (E if ch=='E' else M).append(u)
                    y,z=Y//R,Z//R
                    demand(4*a*y*z==p*(a*y+a*z+y*z),'independent ordered identity')
        demand(bool(adj) and sum(e for r,e in adj)%2==1,'independent all-factor parity')
        demand(all(r<p and r!=q for r,e in adj),'independent edge range')
        nodes[q]={'a':a,'R':R,'sigma':s,'factors':fs,'edges':adj,'E':E,'M':M,'mass':cnt}
    return nodes

def tarjan(nodes):
    sys.setrecursionlimit(max(10000,3*len(nodes)+100))
    idx={};low={};stack=[];active=set();comps=[]
    def visit(v):
        idx[v]=low[v]=len(idx);stack.append(v);active.add(v)
        for w,e in nodes[v]['edges']:
            if w not in idx:visit(w);low[v]=min(low[v],low[w])
            elif w in active:low[v]=min(low[v],idx[w])
        if low[v]==idx[v]:
            comp=[]
            while True:
                w=stack.pop();active.remove(w);comp.append(w)
                if w==v:break
            comps.append(sorted(comp))
    for q in nodes:
        if q not in idx:visit(q)
    return sorted(comps,key=lambda z:z[0])

def row(p,nodes):
    hit={q for q,n in nodes.items() if n['E'] or n['M']}
    dist={q:0 for q in hit}
    while True:
        add={q:1+min(dist[r] for r,e in n['edges'] if r in dist) for q,n in nodes.items() if q not in dist and any(r in dist for r,e in n['edges'])}
        if not add:break
        dist.update(add)
    bad=set(nodes)-set(dist);cc=tarjan(nodes)
    bottom=[C for C in cc if all(r in C for q in C for r,e in nodes[q]['edges'])]
    trapped=[C for C in bottom if not(hit&set(C))]
    demand(bool(bad)==bool(trapped),'independent closure criterion')
    return {'p':p,'vertices':len(nodes),'edge_support':sum(len(n['edges']) for n in nodes.values()),
            'edge_occurrences':sum(e for n in nodes.values() for r,e in n['edges']),
            'divisor_candidates':sum(n['mass'] for n in nodes.values()),'occupied_vertices':len(hit),
            'E_states':sum(len(n['E']) for n in nodes.values()),'M_states':sum(len(n['M']) for n in nodes.values()),
            'auxiliary_vertices':sum(2*n['a']>p for n in nodes.values()),
            'auxiliary_E_states':sum(len(n['E']) for n in nodes.values() if 2*n['a']>p),
            'trap_vertices':len(bad),'bottom_components':bottom,'failed_bottom_components':trapped,
            'max_escape_distance':max(dist.values(),default=0),'least_vertex':min(nodes),'least_vertex_escape':dist.get(min(nodes))},dist

def group(R,gs):
    H={1};front=[1]
    while front:
        x=front.pop()
        for g in gs:
            y=x*g%R
            if y not in H:H.add(y);front.append(y)
    return H

def detailed(input_data,spf,ps):
    for key in ('1201','2521','3361','5569'):
        p=int(key);known=input_data[key];nodes=vertices(p,ps,spf);rr,dist=row(p,nodes)
        for nn in known['nodes']:
            q=nn['q'];n=nodes[q];demand(nn['escape_distance']==dist.get(q),'independent vertex distance')
            for k in ('a','R','sigma','E','M'):demand(nn[k]==n[k],'independent source field '+k)
            demand(nn['edges']==[list(z) for z in n['edges']],'independent all edges')
            demand(nn['factors']==[list(z) for z in n['factors']],'independent factors')
            R=n['R'];mu=Counter()
            for u in dsquare(n['factors']):mu[u*pow(n['a'],-1,R)%R]+=1
            W=set(mu);K={t for t in W if all((x*t)%R in W for x in W)}
            G=group(R,[-1,2]+[r for r,e in n['factors']])
            ob=nn['obstruction'];demand(ob['K']==sorted(K),'independent stabilizer')
            demand(ob['fine_counts']==[list(z) for z in sorted(mu.items())],'independent original fine counts')
            demand(ob['Gamma_order']==len(G) and ob['effective_index']==len(G)//len(K),'independent effective index')
        if 'cycle_identity' in known:check_cycle(known['cycle_identity'])
    for key,data in input_data.items():
        if key.startswith('two_cycle_'):
            pp=data['p'];demand(spf[pp]==pp,'independent two-cycle prime');check_cycle(data['cycle_identity'])
            for nn in data['nodes']:
                ff=factors(nn['a'],spf);uu=dsquare(ff);rr=nn['R']
                demand(nn['E']==[u for u in uu if (4*u+1)%rr==0] and nn['M']==[u for u in uu if (u+nn['a'])%rr==0],'independent two-cycle complete gates')
    ev=input_data['even_NR_edge'];demand(ev['factors']==[[11,2],[13,1]] and ev['edges']==[[11,2],[13,1]],'independent even nonresidue edge')
    demand(spf[808369]==808369,'independent large displayed prime')
    # Verify the large displayed component without pretending this checks its entire graph.
    for n in input_data['808369']['nodes']:
        q=n['q'];p=808369;R=n['R'];a=(p+R)//4;fs=factors(a,spf)
        E=[];M=[]
        for u in dsquare(fs):
            if (4*u+1)%R==0:E.append(u)
            if (u+a)%R==0:M.append(u)
        qr={j*j%p for j in range(1,(p+1)//2)}
        adj=[(r,e) for r,e in fs if r not in qr]
        demand(n['E']==E and n['M']==M and n['edges']==[list(z) for z in adj],'independent 808369 exact node')
    check_cycle(input_data['808369']['cycle_identity'])
    for k in ('auxiliary_recode','multiplier_escape','shared_divisor_gate_change'):
        rec=input_data[k]
        if k=='multiplier_escape':rec=rec['witness']
        if k=='shared_divisor_gate_change':rec=rec['original_hit']
        x,y,z=rec['denominators'];p=rec['p']
        demand(4*x*y*z==p*(x*y+x*z+y*z),'independent displayed ES identity')

def check_cycle(c):
    q=c['cycle'];cs=c['cofactors'];ss=c['sigma'];p=c['p'];n=len(q)
    demand(all(p+ss[i]*q[i]==4*cs[i]*q[(i+1)%n] for i in range(n)),'independent cycle edges')
    T=[]
    for i in range(n):
        # Closed formula, not the main verifier's recurrence.
        tt=sum(prod(4*cs[(i+t)%n] for t in range(j))*prod(ss[(i+t)%n] for t in range(j+1,n)) for j in range(n))
        T.append(tt)
    H=gcd(*T);D=4**n*prod(cs);S=prod(ss)
    demand(T==c['T_rotations'] and H==c['h'] and (D-S)//H==p,'independent cycle code')
    demand([t//H for t in T]==q,'independent primitive cycle inverse')

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--input',default='certificates');ap.add_argument('--out',default='independent.json');args=ap.parse_args()
    src=Path(args.input);expected=json.loads((src/'scan.json').read_text());examples=json.loads((src/'examples.json').read_text());bound=expected['bound']
    spf,ps=tables(max(bound,808369));dig=hashlib.sha256();cnt=Counter()
    for want in expected['rows']:
        p=want['p'];demand(spf[p]==p and p%840 in {1,121,169,289,361,529},'independent scan prime')
        nodes=vertices(p,ps,spf);got,dist=row(p,nodes);demand(got==want,'independent complete scan row')
        dig.update((json.dumps(got,sort_keys=True,separators=(',',':'))+'\n').encode());cnt['primes']+=1
    demand([r['p'] for r in expected['rows']]==[p for p in ps if p<=bound and p%840 in {1,121,169,289,361,529}],'independent complete hard universe')
    demand(dig.hexdigest()==expected['rows_sha256'],'independent all-row digest')
    detailed(examples,spf,ps)
    ans={'checks':CHECKS,'bound':bound,'rows_sha256':dig.hexdigest(),'primes':cnt['primes'],
         'scope':'complete canonical graph scan rows and all detailed small graphs; listed large component only; no imported checker'}
    Path(args.out).write_text(json.dumps(ans,sort_keys=True,indent=2)+'\n');print(json.dumps(ans,sort_keys=True))
if __name__=='__main__':main()
