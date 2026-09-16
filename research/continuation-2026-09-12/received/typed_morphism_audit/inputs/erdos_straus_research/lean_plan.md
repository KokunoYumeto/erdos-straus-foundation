# Dependency-ordered Lean formalization specification

This is a lemma list and implementation plan, not a compiled Lean development.
No existing mathlib declaration names or availability of analytic theorems are
assumed. The statements below should be implemented with exact integer
arithmetic first. Classical analytic inputs must eventually be imported as
proved theorems or formalized; replacing them by new axioms would not constitute
a completed formal verification of the infinite statements.

## 0. Types and conventions

Use natural numbers for positive factor coordinates and denominators, integers
for signed companion-basis coefficients, and `ZMod m` or the unit group of that
ring for congruences. Use `Multiset` rather than `Finset` for factor occurrences.
Use an ordered triple for raw denominators. Store sorting as a separate map.

A shell contains `p R a : Nat`, proofs `Nat.Prime p`, `p % 4 = 1`, `0 < R`,
`R < p`, and `4*a = p+R`. Deduce all consequences rather than duplicating them
as unrelated assumptions: `R % 4 = 3`, `R >= 3`, `p/4 < a < p/2` in rational
arithmetic, `Nat.Coprime a R`, `Nat.Coprime p R`, and `a < p`.

An exterior state over a shell stores `h r s kappa : Nat`, positivity,
`Nat.Coprime r s`, `a=h*r*s`, and `R*kappa=p*r+s`. Its raw triple is
`(h*r*s, h*s*kappa, p*h*r*kappa)`.

A middle state stores `h r s lambda : Nat` with the same factor requirements
and `R*lambda=r+s`. Its raw triple is
`(h*r*s, p*h*s*lambda, p*h*r*lambda)`.

For the target-extraction lemmas, use a finite abelian multiplicative group `G`
and an element `tau` of exact order two. Keeping the group formulation separate
from integer factorization avoids having to redo combinatorial proofs for each
modulus.

## 1. Shell and divisor-coordinate lemmas

**S01 shell_units.** Every positive divisor of `a`, and hence each of `h,r,s`,
is coprime to `R`. Proof: a common prime divisor divides `4*a-R=p`, but is at
most `R<p`. Also prove `p` coprime to `a` from `0<a<p`.

**S02 divisor_decode_integral.** If `u>0` and `u | a^2`, put `d=gcd(a,u)`.
Then `(u/d) | d`. A prime-exponent proof is supplied in Proposition 2.2.
Prove divisions exact before rewriting them in later lemmas.

**S03 divisor_decode_equiv.** The decoding map
`u -> (d/(u/d), u/d, a/d)` is inverse to `(h,r,s) -> h*r^2`
on positive triples with `a=h*r*s` and `Coprime r s`.
Dependencies: S02 and uniqueness of prime factorization.

**S04 exterior_test_equiv.** Under the factor conditions,
`R | 4*h*r^2+1` iff `R | p*r+s`.
Use `p=4*h*r*s-R` and invert `s mod R` by S01.

**S05 middle_test_equiv.** Under the factor conditions,
`R | 4*h*r^2+p` iff `R | r+s`.
Cancel the unit `4*h*r mod R`.

**S06 reciprocal_identity_E/M.** Prove first the integer equations
`4*x*y*z=p*(x*y+x*z+y*z)` by ring normalization and the defining equations.
Then derive the rational reciprocal identity using positivity.

**S07 factor_pair_identity.** From the reciprocal equation with denominator
`a`, derive `(R*y-p*a)*(R*z-p*a)=(p*a)^2`; prove both factors strictly positive
before using natural subtraction, or work over the integers.

**S08 complete_factor_allocation.** Classify the p-adic valuations of the two
factors as `(0,2),(1,1),(2,0)`. Use `p` prime and `p` coprime to `a*R`.
Recover `u` and the channel, orienting the exterior p-divisible denominator last.

**S09 denominator_inverse.** The inverse is `a^2/(R*y-p*a)` for E and
`p*a^2/(R*y-p*a)` for M, with exact division. This proves raw injectivity.

**S10 sorting_fibres.** Prove `a<p/2` and `y,z>p/2`, so sorting recovers `a,R`.
For E prove `z/y=p*r/s>1`, `p` not dividing `y`, and `p | z`. For M prove both
are divisible by `p`; its swapping involution sends `u` to `a^2/u` and has no
fixed point, since a fixed point forces `R | 2*p`. Thus every M sorting fibre
has exactly two elements, and the two channels do not collide.

## 2. Exact positivity

**K01 lower_chamber_polynomial.** For positive `r,s`, set
`D=s^2-4*r*s-3*r^2` over the integers. Prove `r/s<alpha` iff
`D>0` and `D^2>8*r^2*(r+s)^2`, using real nonnegative square roots and recording
signs before each squaring.

**K02 upper_chamber_polynomial.** With `F=3*r^2-4*r*s-s^2`, prove `r/s>beta`
iff `r>s` and `(F>=0 or 8*r^2*(r-s)^2>F^2)`. Combine with
`r/s<1+sqrt(2)` iff `r<=s or (r-s)^2<2*s^2`.

**K03 ray_interval_positive.** Prove the strict inequalities
`beta<3/2<2<1+sqrt(2)` and `1/8<alpha`; deduce positivity of every Farey
ray in the interval and of every `(1,s)` for `s>=8`.

## 3. Three-ray algebra and finite incidence spaces

**L01 three_bezout_identities.** Ring-normalize the three displayed identities
between `2*p+1`, `3*p+2`, `5*p+3`. Deduce pairwise coprimality over the integers.

**L02 root_collision_iff_determinant.** For a prime `q` not dividing the two
first coordinates, roots coincide iff `q | r_i*s_j-r_j*s_i`. Add nonzero-root
hypotheses `q` not dividing the second coordinates.

**L03 eligibility_tables.** For each of the six hard residues, compute its
image modulo 8,24,60,120. Prove the two v3 class pairs and the common class
`-c mod 120`. Verify separately the excluded prime 7 contributes no incidence.

**L04 finite_local_polynomial.** Enumerate the nonzero residues modulo `q`;
prove exactly `q-1-t` carry no root block and one residue carries each root
block. The polynomial numerator is `q-1-t + sum_B product_{i in B} X_i`.
For three distinct roots this is `q-4+X+Y+Z`.

**L05 CRT_product_space.** Establish an equivalence between reduced residues
modulo `840*product S` above `c` and the product of the unit spaces modulo the
finitely many distinct auxiliary primes. This is entirely algebraic.

**L06 finite_model_moments.** Under uniform counting measure on that finite
product space, compute expectations, variances and cross-covariances. Cross
terms from a shared auxiliary prime are exactly `-1/(q-1)^2`.

## 4. Capacity-preserving target extraction

**G01 C2_zero_sum_two.** Every length-two multiset in C2 has a nonempty
zero-sum submultiset.

**G02 C2sq_zero_sum_three.** Every length-three multiset in C2×C2 has a
nonempty zero-sum submultiset. Split into zero, repetition, and the three
nonzero distinct elements.

**G03 C4C2_zero_sum_five.** Map C4×C2 onto C2×C2 with kernel C2. Obtain a
zero-sum subsequence of length at most two among five images and a disjoint
nonempty one among the remaining at least three images. Their lifts either
already sum to zero or have the same nonzero kernel sum; join them then.

**G04 target_extraction.** Suppose every length-d sequence in `G/<tau>` has
a nonempty zero-sum subsequence. Any multiset with an actual tau-product
submultiset has one of cardinality at most d. Choose a cardinality-minimal
submultiset; a quotient-zero proper submultiset has product 1 or tau.
Deletion or replacement contradicts minimality. Use multiset subtraction,
not a support subgroup, to preserve capacities.

**G05 explicit_unit_quotients.** Give explicit finite equivalences for
U(8)/<7> ≅ C2, U(24)/<23> ≅ C2², and U(60)/<tau> ≅ C4×C2 for tau=59,11.
For the last case use the CRT map in the note; prove its kernel and image.

**G06 automatic_residual_bound.** For hard-class primes, a target divisor of
L_i has complementary quotient at least 5,19,28 respectively. Prove the
specific residue 52/28 in the v3 cases before deducing `R<p`.

**G07 completed_ray_iff_short_pattern.** Combine G01–G06 and S04 to prove
exactly the 2/3/5 theorem. Integer prime-factor multiplicities must be retained.

**G08 exhaustive_minimal_patterns.** Define a finite nondecreasing-list
enumeration through length 2,3,5. Prove every minimal pattern occurs by G07.
Kernel-check the cardinalities 2,8,184,184. The Python dynamic program is a
certificate generator, not a substitute for the Lean enumeration proof.

**G09 first_two_failure_tests.** Prove the mod-8 pattern criterion and the
two mod-24 character kernels, including the fact that `L_2 mod 24=5`.

**G10 sharpness_certificates.** Verify the complete factorizations and prime
certificates at 3529,153409,6320329,2668835929. Exhaust the short finite exponent
boxes to prove the residual lists, especially uniqueness and Omega=5 at the
last prime. This establishes lower as well as upper bounds for 2,3,5.

## 5. Unimodular and channel maps

**U01 companion_unit.** If `det(v,w)=epsilon` with epsilon=±1 and `R | L_v`,
then `gcd(L_w,R)=1`, from `r*L_w-b*L_v=epsilon`.

**U02 lattice_divisibility.** In unique integer basis coordinates `Av+Cw`,
its linear form is divisible by `R` iff `R | C`. Write `C=R*B`.

**U03 lattice_primitivity.** Unimodular changes of basis preserve the gcd of
coordinate absolute values; therefore primitivity is equivalent to
`gcd(|A|,|R*B|)=1`.

**U04 same_shell_equiv.** Build the equivalence of Theorem 6.2 with the exact
positive-coordinate and product-divisibility domain. Prove the formulas for
`h'`, `kappa'`, and the signed inverse. No nonemptiness assertion is included.

**U05 positive_height_barrier.** For positive companion and positive A,B,
prove `r'*s'>=(r+R*b)*(s+R*d)`. Deduce empty domain when the right side exceeds
`a`. A mediant has second basis coefficient 1, so cannot retain `R>1`.

**U06 Farey_rows.** Induct on depth to prove adjacent determinants ±1,
primitivity, interval containment and cardinality `2^d+1`.

**T01 swap_divisor_normalization.** For `u'=s*r^2`, prove `u' | a^2` and its
normalized coordinates are `(s*g^2,r/g,h/g)` with `g=gcd(h,r)`.

**T02 cubic_transfer_iff.** From the exterior congruence and unit r modulo R,
prove `R | r+h` iff `R | 4*r^3-1`. Combine with T01 and S05.

**T03 cubic_denominators.** Compute the output triple, its exact slope `r/h`,
and preserve both p,R. Prove all divisions exact before cancellation.

**T04 inverse_fibres.** For a middle state `(H,a1,b1)`, classify every source
by `g^2 | H`, `Coprime (g*a1) (H/g^2)`, `R | 4*(g*a1)^3-1`.
Prove both compositions are identities when g is retained. Verify the two
preimages at `(389,3,49,1,2,1)` as a genuine noninjectivity certificate when g
is forgotten.

**T05 divisor_box_translation.** With fixed E divisor u, prove another divisor
u' is M iff `u'=p*u mod R`. Translate this into bounded exponent differences.
Do not replace the box by the whole generated subgroup.

**T06 explicit_bridge_progression.** Ring-normalize `p=232*s-31`,
`s=11+210*k`, and verify the exterior and transferred middle states. Prove
positivity and gcd(2521,48720)=1. Infinitely many prime parameters is an
analytic consequence, separate from the algebraic construction.

## 6. Finite complete obstruction certificates

**C01 selector_enumeration_complete.** Prove finite enumeration of all
`R=3 mod 4`, `0<R<p`, and all divisors of `a^2` returns exactly E_p ⊔ M_p,
using S03–S05. This is the bridge from program output to an exhaustive theorem.

**C02 stress_1201.** Kernel-check the 15-state list, 11 sorting fibres, three
positive states, and the full exterior and middle slope lists. Use interval containment to
exclude both channels on the entire infinite original Farey cone, not only computed rows.

**C03 obstruction_2521.** Kernel-check all 12 states, nine increasing triples,
and the six exterior slopes. K01–K02 prove none is positive. Thus all positive
exterior rays fail at this p, not just rays below a coordinate bound.

**C04 no_total_same_shell_transfer.** At 1201,R=71 prove the E fibre nonempty
and M fibre empty; hence no total function E_(p,R) -> M_(p,R) exists there.

**C05 primality_order_criterion.** Prove the full n-1 Lucas order criterion as
in Appendix B, then verify the supplied modular powers and trial-division
primality of the small factors. Do not use probable-prime status as a premise.

**C06 finite_hybrid_cover.** Combine the complete finite prime enumeration,
one exterior witness for each of its 4,508 covered hard primes, and the 11
middle states in Proposition 9.1. Kernel-check positivity, primitivity, shell,
quotient and ordered denominators for every record. This proves the finite
bound 2,000,000, not a universal finite-family covering theorem.

## 7. Infinite statements and analytic boundary

**A01 fixed_modulus_PNT.** The prime-counting equidistribution theorem in
reduced residue classes for each fixed modulus is the required classical input.
Its formal proof/import is an explicit boundary of this plan, not an axiom to
be concealed. Uniformity in growing moduli is not needed.

**A02 fixed_modulus_Mertens.** Prove the reciprocal-prime and log-weighted
reciprocal-prime estimates by partial summation with a suitable fixed-modulus
PNT error, or import Williams' theorem and the log-weighted estimate.

**A03 prime_limit_of_finite_model.** Apply A01 to L05 and then L04–L06. All
auxiliary primes are fixed before the prime-bound variable tends to infinity.

**A04 simultaneous_density_one.** For a fixed auxiliary cutoff T, use
Chebyshev plus a union bound. The variance bound is at most mu_T and failure
probability at most `3*mu_T/(mu_T-K)^2`. Only then send T to infinity, using
`mu_T=(1/32)*log(log T)+O(1)`. Formalize the limsup argument explicitly.

**A05 half_support_masks.** At p in [X,2X], auxiliary q<=floor(X^(1/12)), a
missed ray omits tau and cannot meet both elements of `b -> tau*b^(-1)`.
The involution has no fixed points because tau=3 mod 4. Product residuals
satisfy R<=z^2<X. Extend to a half-unit mask, choosing 1 instead of tau.

**A06 sieve_root_count.** Exclude the finite prime set dividing M, ray
coordinates, determinants, or at most 2(k+1). Prove all remaining roots are
nonzero and distinct. Including the prime-number sieve class 0 gives mean
nu(q)=1+k/2 over reduced residue classes modulo M.

**A07 Selberg_quadratic_diagonalization.** Define multiplicative g,h,G and
finite real weights lambda as in §5. Prove the exact diagonalization and
quadratic value `1/G(z)` by finite Möbius inversion and Cauchy–Schwarz.

**A08 explicit_integer_sieve_bound.** CRT counting, the weight bound
`abs(lambda_d)<=d`, and `nu(d)<=d` give `X/(M*G(z))+z^6`.
This is a finite inequality; all asymptotics enter only in A09.

**A09 G_lower_bound.** Use A02, a finite Euler-product probability measure,
and Markov's inequality to prove `G(z) >= H_y/2` for
`y=z^(1/(2*kappa0+2))`, eventually. Deduce `G(z) >> (log z)^kappa0`.

**A10 fixed_family_exception_bound.** Combine A05–A09, sum over finitely many
masks/refinements, and dyadic intervals. Constants depend on the fixed family.
Conclude exponent `1+k/2`; specialize to Farey rows and the 138-ray family.
No growing-depth uniformity or pointwise coverage theorem follows.

**A11 two_cutoff_small_residuals.** Keep sieve level z=floor(X^(1/12)) but
impose ray-root exclusions only for q<=y, where 2<=y<=z^(1/(4*k)). Primality
exclusions remain for all q<=z. Set w=z^(1/4). The Euler-product mass is at least
constant times log(w)*(log y)^(k/2), while its mean log-product is at most
log(w)+(k/2)*log(y)+O(1)<=3/8*log(z)+O(1)<=1/2*log(z), eventually and uniformly
in y. Apply Markov and A08 to obtain X/(log X*(log y)^(k/2))+O(X^(1/2)). Choosing
y=min(X^(epsilon/2),z^(1/(4*k))) proves the same fixed-family log-power bound
for Omega(R)<=2 and R<=p^epsilon. Choosing y=min((log X)^(A/2),z^(1/(4*k)))
proves the polylogarithmic-residual bound. All moduli and families remain fixed;
no uniformity in epsilon or A is asserted.

## Recommended order of implementation

First complete S01–S10, G01–G10, U01–U06, T01–T06 and C01–C05. These give the
algebraic continuation and pointwise obstruction results without formalizing
analytic number theory. Next formalize the finite local spaces L01–L06 and the
finite Selberg inequality A07–A08. The prime-density and exceptional-set limits
come last, after supplying proved versions of A01–A02.
