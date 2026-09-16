"""Exact finite checks for PolyClank integration results. SPDX-License-Identifier: MIT.
Standard library only. No network, subprocesses, or external source execution.
The default action prints JSON; it does not write files.
"""
import json
from fractions import Fraction
from itertools import product
P=107; N=860

def det(a,p=107):
 a=[r[:] for r in a]; d=1
 for j in range(len(a)):
  k=next((i for i in range(j,len(a)) if a[i][j]%p),None)
  if k is None:return 0
  if k!=j:a[k],a[j]=a[j],a[k];d=-d
  v=a[j][j]%p;d=d*v%p;inv=pow(v,-1,p)
  for i in range(j+1,len(a)):
   q=a[i][j]*inv%p
   for t in range(j,len(a)):a[i][t]=(a[i][t]-q*a[j][t])%p
 return d%p

def mm(a,b):return [[sum(x*y for x,y in zip(r,c))%P for c in zip(*b)] for r in a]
def eye(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def inv(a):
 n=len(a);m=[r[:]+s for r,s in zip(a,eye(n))]
 for j in range(n):
  k=next(i for i in range(j,n) if m[i][j]%P);m[j],m[k]=m[k],m[j]
  v=pow(m[j][j]%P,-1,P);m[j]=[x*v%P for x in m[j]]
  for i in range(n):
   if i!=j:
    v=m[i][j];m[i]=[(x-v*y)%P for x,y in zip(m[i],m[j])]
 return [r[n:] for r in m]

a=[0]*(N+1);a[0]=1;b=[0]*(N+1);b[0]=1
for k in range(1,N+1):
 for _ in range(5-(k%2==0)+(k%3==0)-5*(k%6==0)):
  for n in range(N,k-1,-1):a[n]=(a[n]-a[n-k])%P
 if k%6==0:
  for _ in range(4):
   for n in range(N,k-1,-1):b[n]=(b[n]-b[n-k])%P
ip=[0]*(N+1);ip[0]=1
for n in range(1,N+1):ip[n]=-sum(a[k]*ip[n-k] for k in range(1,n+1))%P
C=[0]*(N+1)
for d in range(1,N+1):
 v=d*(5-(d%2==0)+(d%3==0)-5*(d%6==0))
 for n in range(d,N+1,d):C[n]=(C[n]+v)%P

def row(n):
 T=a[n+1];J=(T+72*ip[n-1])%P;F=-2*sum(a[k]*b[n-k] for k in range(n+1))%P
 return [n%P,T,F,J,C[n]]
R=[row(n) for n in range(744,749)];invR=inv(R)
As={h:mm([row(n+h) for n in range(744,749)],invR) for h in [1,6,21,107]}
A=As[1];B=As[6];aps=[eye(5)];bps=[eye(5)]
for k in range(4):aps.append(mm(aps[-1],A));bps.append(mm(bps[-1],B))
mat=[sum(mm(x,y),[]) for x in aps for y in bps]
comm=[[x-y for x,y in zip(r,s)] for r,s in zip(mm(A,B),mm(B,A))]
o={'R':R,'detR':det(R),'A1':A,'A6':B,'trace_det':{h:[sum(As[h][i][i] for i in range(5))%P,det(As[h])] for h in As},'det_basis':det(mat),'det_commutator':det(comm),'powers289mod840':[pow(289,j,840) for j in range(6)],'cube289mod840':pow(289,3,840),'minus1mod840':839,'A6_equals_A1power6':None}
x=eye(5)
for _ in range(6):x=mm(x,A)
o['A6_equals_A1power6']=x==B


def require(condition, message):
 if not condition:
  raise RuntimeError(message)

require(o["detR"]==8,"Coefficient basis is singular or changed")
require(o["det_basis"]==32,"Word basis determinant changed")
require(o["det_commutator"]==15,"Commutator determinant changed")
require(o["trace_det"]=={1:[46,72],6:[49,40],21:[51,48],107:[21,78]},"Shift invariants differ")
require(not o["A6_equals_A1power6"],"Stationary-shift countercheck changed")
require(o["powers289mod840"]==[1,289,361,169,121,529],"Cyclic residue enumeration changed")
require(o["cube289mod840"]!=o["minus1mod840"],"Arithmetic sign distinction lost")
o["word_basis_matrix_row_major"] = mat
# Check Fourier values exactly in Z[zeta]/(zeta^2-zeta+1).
roots=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
zeros=[]
for k in range(6):
 for m in range(6):
  terms=[roots[(m*j)%6] for j in [(3+k)%6,3,(3-k)%6]]
  raw=tuple(sum(t[i] for t in terms) for i in [0,1])
  a=roots[3*m%6];b=roots[((3-k)*m)%6]
  reduced=(a[0]+2*b[0],a[1]+2*b[1])
  require((raw==(0,0))==((k*m)%6 in [2,4]),"Raw Fourier-zero classification failed")
  require(reduced!=(0,0),"Reduced target has unexpected zero")
  if raw==(0,0):zeros.append([k,m])
o["fourier_zero_pairs"]=zeros
# Determinants over Q, separate from finite-field elimination.
def rational_det(a):
 a=[[Fraction(x) for x in row] for row in a];d=Fraction(1)
 for j in range(len(a)):
  k=next((i for i in range(j,len(a)) if a[i][j]),None)
  if k is None:return Fraction(0)
  if k!=j:a[k],a[j]=a[j],a[k];d=-d
  pivot=a[j][j];d*=pivot
  for i in range(j+1,len(a)):
   q=a[i][j]/pivot
   for t in range(j,len(a)):a[i][t]-=q*a[j][t]
 return d
pencil={}
for lam in [1,2]:
 M=[[(1+lam)*int(i==j)-lam for j in range(4)] for i in range(4)]
 dv=rational_det(M); expected=Fraction((1+lam)**3*(1-3*lam))
 require(dv==expected,"Quadratic pencil determinant failed")
 nu=Fraction(1-2*lam,(1+lam)*(1-3*lam))
 pencil[lam]={"determinant":str(dv),"pointed_invariant":str(nu),"graph_abs_determinant":str(abs(16*dv))}
o["quadratic_pencil"]=pencil
# Finite-word recurrence, including the stated composition order.
word_count=0
for n in range(10):
 for digits in product([0,1],repeat=n):
  value=Fraction(0)
  for digit in reversed(digits):value=(3**digit*value+digit)/2
  ones=0;closed=Fraction(0)
  for j,digit in enumerate(digits):
   closed+=Fraction(digit*3**ones,2**(j+1));ones+=digit
  require(value==closed,"Homogenized finite-word identity failed")
  word_count+=1
o["homogenized_binary_words_checked"]=word_count
# Small-instance check of the explicitly stated diagonal model, not an infinite proof.
vals=[(Fraction(3*n+q,3))**2 for n in range(-5,6) for q in [-1,0,1] if (n,q)!=(0,0)]
require(min(vals)==Fraction(1,9),"Diagonal model gap check failed")
o["diagonal_model_small_instance_minimum"]="1/9 at rho=1"
o["checked_groups"]=["coefficient-derived frame and shifts","25-word matrix-algebra certificate","nonstationary shift distinction","mod840 arithmetic sign distinction","abstract C6 Fourier identities","rational quadratic forms","finite-word homogeneous composition","finite diagonal-model sample"]
o["scope"]="Finite checks only. General proofs are in ARGUMENTS.md. No Lean run, model voting, global ES assertion, or novelty assessment."
print(json.dumps(o,indent=2,sort_keys=True))
