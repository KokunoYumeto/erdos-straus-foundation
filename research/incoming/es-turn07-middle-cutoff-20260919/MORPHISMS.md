# Exact maps retained in Turn 7

Throughout, `p` is prime with `p ≡ 1 (mod 8)`.  An original oriented middle
state has `p/4<a<p/2`, `R=4a-p`, `u|a^2`, `R|u+a`, and `u<a`.  None of the
maps below identifies the direct residual `R` with the cofactor `Q`.

## M01 — centered exponent box to square divisor

- Domain: the complete marked box `beta_l in [-e_l,e_l]` for
  `a=product_l l^e_l`.
- Codomain: positive divisors `u|a^2`.
- Map: `u=product_l l^(e_l+beta_l)`.
- Inverse: `beta_l=v_l(u)-e_l`.
- Fibres: singleton.  Divisor complementation sends `u` to `a^2/u` and every
  `beta_l` to `-beta_l`.

## M02 — square divisor to primitive coordinates

- Domain: `(a,u)` with `u|a^2`.
- Map: with `g=gcd(a,u)`,
  `(h,r,s)=(g^2/u,u/g,a/g)`.
- Codomain: positive `(h,r,s)` with `a=hrs`, `u=hr^2`, `gcd(r,s)=1`.
- Inverse: `(h,r,s) -> (hrs,hr^2)`.
- Orientation: `u<a` is exactly `r<s`; complementation swaps `r,s`.

Primewise, if `v_l(a)=e` and `v_l(u)=f`, then
`v_l(g)=min(e,f)` and `2min(e,f)-f>=0` because `0<=f<=2e`; hence `h` is
integral.  This valuation proof is retained rather than replaced by a reduced
fraction argument.

## M03 — middle state to ordered denominators

- Extra condition: `lambda=(r+s)/R` is a positive integer.
- Map:
  `(p,h,r,s,lambda) -> (a, p*h*s*lambda, p*h*r*lambda)` with `a=hrs`.
- Identity:
  `4/p = 1/a + 1/(p*h*s*lambda) + 1/(p*h*r*lambda)`.
- Ordered inverse from `(p,a,y,z)` with the indicated order:
  `u=p*a^2/(R*y-p*a)`, followed by M02.
- Exceptional locus: reversing the last two denominators applies
  `u -> a^2/u`, so the orientation bit must be retained.

## M04 — original state to hyperbola coordinates

- Domain: M03.
- Map:
  `j=h*r*lambda`, `Q=4j-1`, `A=h*lambda^2`.
- Exact equations:
  `R*Q=p+4h*r^2`, `Q*s=p*lambda+r`,
  `Q+1<2A*R`, and
  `p=R*Q-(Q+1)^2/(4A)`.
- Codomain: positive odd `R,Q ≡ 3 (mod 4)`, `0<R,Q<p`, with the displayed
  integral coordinates and strict inequality.
- Information loss: `(R,Q,A)` alone need not recover `h,r,s,lambda`; the
  original state and the equations above are retained.  The map is used for
  inequalities, not asserted to be a parametrization by itself.

## M05 — direct atlas chart

- Domain: original oriented states with `R<=Q`.
- Small coordinate: `3<=R<=B(p)`, `R ≡ 3 (mod 4)`.
- Forward data:
  `a=(p+R)/4`, original `u|a^2`, `u<a`, `R|u+a`,
  `Q=(p+4u)/R`.
- Inverse: M02 followed by `lambda=(r+s)/R` and M03.
- Fibres: singleton after the original orientation is fixed.
- Boundary: ties `R=Q` occur only here.

## M06 — cofactor atlas chart and exact return

- Domain: original oriented states with `Q<R`.
- Forward map: `j=h*r*lambda`, `Q=4j-1`, retain the same `u=h*r^2`.
  It satisfies `1<=j<=K(p)`, `u|j^2`, `Q|p+4u`, and
  `R=(p+4u)/Q>Q`.
- Cofactor-chart domain: exactly the integers `(j,u)` satisfying those
  displayed conditions.
- Inverse: put `g=gcd(j,u)` and
  `h=g^2/u`, `r=u/g`, `lambda=j/g`, `s=R*lambda-r`,
  `a=R*j-u`.
- Returned identities:
  `j=h*r*lambda`, `u=h*r^2`, `a=h*r*s`, `gcd(r,s)=1`, `r<s`,
  `p/4<a<p/2`, and M03.
- Fibres: singleton.  Applying the forward map to the inverse returns the
  same `(j,u,R,Q)`.
- Exceptional locus: `R=Q` is excluded by `R>Q`; it is represented in M05.

The integrality of `h` follows primewise from `u|j^2`; it is not obtained by
cancelling unrecorded factors.  The proof that `gcd(r,s)=1` uses `r<p` and
`R*Q=p+4u` and keeps every shared factor candidate explicit.

## M07 — direct/cofactor chart partition

- Domain: all original oriented middle states at a hard prime.
- Map: send the state to M05 when `R<=Q`, otherwise to M06.
- Inverse: the chart-specific inverses above.
- Image: the disjoint union of the two declared chart domains.
- Fibres: singleton.  The inequalities `R<=Q` and `R>Q` prove disjointness.

## M08 — cofactor presentation versus original shell

At `p=2521`, the cofactor data `(j,u,Q,R)=(12,16,47,55)` returns
`(a,h,r,s,lambda)=(644,1,4,161,3)` by M06.  The original shell with residual
`47` instead has `a'=642`; exhaustive square-divisor residues show that its E
and M targets are empty.  Therefore swapping the labels `R,Q` is not a map of
original shells.  The exact morphism is M06, whose codomain has residual `55`
and whose retained cofactor is `47`.

## M09 — fixed-grade CRT progression

- Input: an integer grade budget `B>=1`.
- Choice: a prime `q ≡ 3 (mod 4)`, `q>max(7,4B)`, and
  `L=8 product_{l<q, l odd prime} l`.
- CRT map: the pair of residues `(1 mod L, -1 mod q)` maps to its unique
  reduced residue class modulo `Lq`.
- Prime output: Dirichlet supplies infinitely many primes `p` in that class.
- Exact arithmetic readout: all primes below `q` are quadratic residues modulo
  `p`, while `q` is a nonresidue, so the declared least-nonresidue parameters
  equal `q`.
- Endpoint inverse: `R=q`, `a=u=(p+q)/4`, `h=a`, `r=s=1`,
  `kappa=(p+1)/q`, returning denominators `(a,a*kappa,p*a*kappa)`.
- Nonclaim: this progression is solution-bearing.  It obstructs a fixed
  `h/j` inventory; it does not construct counterexamples.

## M10 — partial-factor order certificate

- Domain: a candidate integer `n`, a completely factored `F|n-1` with
  `F^2>n`, and one base `a_l` for each prime `l|F` satisfying the two displayed
  modular conditions in `core.tex`.
- Map: reduce every base modulo an arbitrary prime divisor `d|n`, take its
  multiplicative order, and read its full `l`-primary divisor.
- Output: `F|d-1` for every prime divisor `d` of `n`.
- Obstruction to a composite fibre: a composite `n` has a prime divisor
  `d<=sqrt(n)<F`, contradicting `d ≡ 1 (mod F)`.
- No probable-prime test is used in this implication.

## M11 — finite program crosswalk

`verify.py` enumerates square-divisor states and both atlas charts.
`check_independent.py` independently enumerates primitive `(h,r,s)` states,
rechecks the recorded JSON identities and validates the order certificate.
Their common output key is the complete bounded state tuple, not merely the
number of successes.  Neither finite map has codomain “all primes”.
