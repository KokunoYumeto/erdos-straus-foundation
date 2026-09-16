# Typed maps and retained information

## A1. Original cofactor and marked ES state
Domain: Q|N, Q=-1 mod2^k.
Codomain: (p,k,u,N,Q,R,a,h,r,s,lambda,x,y,z).
R=N/Q, a=(p+R)/4, gcd normalization (A3).
Inverse u=pa^2/(Ry-pa), Q=N/R. Retain channel M and denominator order.

## A2. Signed arithmetic relation to the imported two-power form
Domain: (a,b) in Z^2 with ab!=0.
Codomain: (alpha1,alpha2,b1,b2,Lambda).
alpha1=3^sgn(a), alpha2=11^-sgn(b), b1=abs(a), b2=abs(b).
Signs and positive exponents recover a,b. Lambda=11^-b(3^a11^b-1); multiplier is a 2-adic unit. Axes handled separately.

## A3. Relation lattice coordinate equivalence
Domain: Z^2.
Codomain: L_k.
(c,d) -> (o*c-J_k*d,d).
Inverse (a,b)->((a+J_k*b)/o,b). Integral exactly on the declared kernel.

## A4. Finite 2-adic logarithm observation
Domain: The convergent normalized log ratio modulo2^(k-3).
Codomain: J_k in [0,2^(k-2)).
J_k=1+2[(log(11/3)/8)/(log9/8)].
Unique modular-power inverse label. The finite residue does not retain the full infinite 2-adic expansion.

## A5. Exact basis reduction
Domain: Original ordered basis ((o,0),(-J_k,1)).
Codomain: Gauss-reduced ordered basis plus trace.
Integer swaps and nearest multiple subtraction.
Each operation is unimodular; reversing the retained trace returns the original ordered basis.

## A6. Word selection by rounding
Domain: Target t and actual translated rectangle with proved widths.
Codomain: Original exponent word plus basis coordinates.
w=(t,0)+B round(B^-1(c-(t,0))).
For fixed t,B, rounding coefficient fibre z is z+[-1/2,1/2)^2. Inverse on a selected word reads B^-1(w-(t,0)); it does not recover a discarded arbitrary centre.

## A7. Complete bounded target fibre
Domain: (t,0)+L_k intersect actual rectangle.
Codomain: All original 3,11 exponent pairs at the target.
Identity on coordinates.
Integer factorization reads exponents; modular residue alone forgets the fibre.

## A8. Prime-factor word to cofactor
Domain: (t,i,j) with t|M outside H and target i+Jj.
Codomain: Q=3^i11^j t.
Multiply actual distinct-prime factors.
i=v3(Q), j=v11(Q), t=Q/(3^i11^j). Unique, no coloured copies.

## R1. Exact relative group isomorphism
Domain: H_(k-v).
Codomain: <3^(2^v)> inside H_k.
g -> g^(2^v).
Read retained cyclic exponent and divide by2^v. This identifies relation lattices at precision k-v, not arbitrary fields or heights.

## R2. Complete lower/higher digits
Domain: Actual rectangle 0<=i<=e,0<=j<=f.
Codomain: Disjoint union of actual lower-digit/high-capacity rectangles.
i=r+dI, j=s+dJ with 0<=r,s<d.
Euclidean division; higher bounds floor((e-r)/d), floor((f-s)/d). No multiplicity renormalization.

## R3. Relative target equation
Domain: One retained lower fibre meeting t-r-J_k*s=0 mod d.
Codomain: Target (t-r-J_k*s)/d mod2^(k-v-2).
Divide the actual integer difference by d.
Reverse by multiplying by d and restoring lower digits and original target representative. Incompatible lower fibres are not admitted.

## R4. Relative boundary inclusion
Domain: F2[C_d].
Codomain: ker((X+1)^d) in F2[C_o].
X^r -> X^r sum_(j<o/d) X^(d*j).
Inverse reads a coefficient per coset after the constant-coset image test. Module map, not a unital ring isomorphism.

## R5. Ordinary coefficient quotient
Domain: F2[C_o].
Codomain: F2[C_d].
Sum coefficients with same exponent modulo d.
Kernel is the corresponding coset-sum-zero subspace. pi*iota=0 for a nontrivial 2-power ratio; not the inverse of R4.

## R6. Coefficient reduction with supported zeros
Domain: Original integer coefficient counts plus original label set.
Codomain: Same support set with amplitudes mod2.
Reduce amplitudes, retain every presence label.
Many-to-one amplitudes; retain original integer vector for full return. Even positive counts become e, never automatically tau.

## C1. Disjoint-block counting lower bound
Domain: Disjoint actual exponent rectangles and outside t|M.
Codomain: Distinct original cofactors.
Choose one target word per rectangle and multiply by t.
Unique factorization and disjoint rectangles make chosen states distinct; no sum over overlapping untracked families.
