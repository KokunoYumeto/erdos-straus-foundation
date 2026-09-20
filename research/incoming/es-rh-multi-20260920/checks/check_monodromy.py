import sympy as s
from itertools import permutations,product
from common import Suite
T=Suite('fixed_prime_monodromy')
def sign(pi):return -1 if sum(pi[i]>pi[j] for i in range(4) for j in range(i+1,4))%2 else 1
def mul(g,h):
 pg,sg=g;ph,sh=h
 return tuple(pg[ph[j]] for j in range(4)),tuple(sh[j]*sg[ph[j]] for j in range(4))
ID=(tuple(range(4)),(1,1,1,1));gens=[]
for a,b in [(1,2),(2,3)]:
 pi=list(range(4));pi[a],pi[b]=pi[b],pi[a];ss=[1]*4;ss[b]=-1;gens.append((tuple(pi),tuple(ss)))
gens.append((tuple(range(4)),(-1,-1,1,1)))
found={ID};stack=[ID]
while stack:
 h=stack.pop()
 for g in gens:
  k=mul(g,h)
  if k not in found:found.add(k);stack.append(k)
expected={(tuple([0]+list(pi)),sg) for pi in permutations([1,2,3]) for sg in product([-1,1],repeat=4) if s.prod(sg)==sign(tuple([0]+list(pi)))}
T.require('full restricted group has order 48',len(found)==48)
T.require('generators equal determinant-one prime stabilizer',found==expected)
T.require('prime orbit length two',len({(g[0][0],g[1][0]) for g in found})==2)
T.require('denominator orbit length six',len({(g[0][1],g[1][1]) for g in found})==6)
T.reject('generic group remains transitive after ES restriction',len({(g[0][0],g[1][0]) for g in found})==8)
T.save({'group_order':len(found),'orbits':[2,6]})
