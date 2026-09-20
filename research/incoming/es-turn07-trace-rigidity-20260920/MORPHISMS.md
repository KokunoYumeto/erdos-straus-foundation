# Exact source maps

## 1. Rational roots to Newton traces
Domain: labelled nonzero rational x_i with first n-1 power sums integral.
Observation: s_k=sum x_i^k. Newton's identities supply j!*e_j integral for j<n.
The valuation argument proves a common reduced denominator d; it is not an
extra input. The reduced reciprocal numerator m then satisfies d^n | (n-1)!m.
At reciprocal numerator dividing four and n>=3, d=1. Rationality is indispensable.

## 2. Length-three denominator construction
Domain: d odd, v_3(d)<=1, every other denominator prime 1 mod3.
Coordinates: one labelled CRT record at each q^(2e+1), with A=1, local B,C.
At q=3 use (1,1,4) mod27. At the other primes lift a nontrivial cubic root and
retain the choice making the pair sum have exact valuation 2e.
Inverse of the resulting record reads d and the original numerator residues.
The construction is not claimed to parametrize every triple: it proves every
permitted denominator is attained with the sharp reciprocal numerator valuations.

## 3. Raw full M gate to rational denominators
Domain: prime p=1 mod4, p/4<a<p/2, R=4a-p, U positive integer,
R | a+U. Map:
(a, pa(U+a)/(RU), p(a+U)/R).
Exact literal trace denominator: U/gcd(U,p*a^2).
An integral trace is equivalent to U|p*a^2. The finite bound U<=p*a^2 is
therefore a proved consequence for every integral return, not a heuristic cutoff.

## 4. Original tag and normalization
vp(U)=0: original M divisor u=U. vp(U)=1: original E divisor u=U/p.
No higher p valuation is possible. The complete gcd normalization gives h,r,s
and lambda/kappa; the formulas in core.tex retain all ordered denominators.
E inverse u=a^2/(Ry-pa); M inverse u=pa^2/(Ry-pa).
The integral literal trace S also gives M iff S=a modp, otherwise E.

## 5. Trace fibres
At fixed p,a, equality S(U)=S(V) is U=V or UV=a^2.
The latter has no fixed point in the full raw gate. It yields exactly the two
original M orientations. E and nonintegral trace fibres are singletons.
The inverse from S solves the displayed quadratic and retains positivity,
integer input, range and the original sum gate.

## 6. Integer coefficient pushforward
Phi: Z^Omega -> Z^Theta sends e_U to e_S(U). Its kernel basis is
{e_U-e_(a^2/U): original M divisor U<a}. Rank = |M|/2.
Each original coordinate has integer count one. Coarse integral trace values
number |E|+|M|/2; their full multiplicity is |E|+|M|.
Different distinguished denominators a are not merged by the one-trace map.

## 7. Weighted quotient
For retained positive source weights w_U, the quotient norm is
sum_S |z_S|^2 / sum_(S(U)=S)(1/w_U).
The minimum-norm section has coefficient z_S/(w_U*sum(1/w_V)).
It is generally not integral. Selecting a representative gives an integral
section with a different norm. No analytic Gamma norm is silently replaced.
A two-word coefficient reduces to zero mod2 without becoming an absent source.

## 8. Integral first tail trace to a factor pair
Domain: original integer p,a,R but arbitrary rational y,z with reciprocal
sum R/(pa), N=y+z integral. Exact denominators are both d, with
 d^2=R/gcd(R,N).
Set b=Ry-pa,c=Rz-pa. They are positive integer divisors with bc=(pa)^2.
Inverse: y=(pa+b)/R,z=(pa+c)/R. First-trace integrality is precisely
K(R)|pa+b; full integrality is R|pa+b. Second trace has exact denominator d^2.
The pair orientation b<->c is retained. Replacing R by R/d^2 changes a and its
factor inventory; the p1009 example proves that this replacement need not hit.

## 9. Literal coefficient traces
For H=A*T^4+T^3+B*T^2+C*T+D with roots (p,x,y,z), the original root-algebra
traces are N1=-1/A and N2=1/A^2-2B/A. Their rank-eight completed traces are
exactly twice these numbers. They are not the weighted analytic shift moments.
Given p,N1,N2, the denominator cubic is the explicit TR20a polynomial.
Its rational, positive, correctly ranged roots return the entire original
state, one orientation for E and two for M. The rational splitting test remains.

## 10. The all-prime algebraic extension
For every hard prime, choose k0 by its two exact nonresidue conditions. CRT is
not used: k is the first integer >=K0 in that residue modulo the original p.
The adjacent-square bounds prove the quadratic root field is genuinely
quadratic over Q. Hensel's exact digit maps give its two embeddings into Qp.
The roots b,c and raw words U_+,U_- are positive algebraic integers;
U_+U_-=a^2 and 3|(a+U_+) in that quadratic integer ring.
This does not provide an integer U in the original Z source.
The conjugation bit and the field are retained. Integer traces and the p-local
cluster signature do not erase them.

## 11. Constant-prime preservation and nonclaims
Every stated arithmetic return preserves its original p. No fixed-prime
existence follows from the fact that a supplied trace value has an inverse.
There is no proved positive lower bound on the integer trace image or Phi's
kernel for every p. This tranche completes an integrality comparison, not the
universal Turn 7 milestone.
