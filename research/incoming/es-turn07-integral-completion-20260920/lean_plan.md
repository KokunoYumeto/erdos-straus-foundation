# Lean-ready dependency plan (not a Lean build)

This file states exact proof dependencies. Names below are proposed new lemma
names, not claims that matching declarations already exist in a given mathlib.
No `axiom` of ES existence or of local-to-global occupancy is allowed.

## A. Original arithmetic

1. `original_normalization`: natural p,a,u with p prime, p=1 mod12,
   p<4a,2a<p,u|a^2. Set R=4a-p,g=gcd(a,u), h=g^2/u,r=u/g,s=a/g.
   Prove all divisions exact, hrs=a,hr^2=u,gcd(r,s)=1.
2. `ordered_E_return`, `ordered_M_return`: the two gate hypotheses imply the
   ordered reciprocal identity over Q and the displayed u inverse.
3. `original_character`: quadratic reciprocity and the supplementary law imply
   Jacobi(d,R)=Legendre(d,p) for d|a^2; deduce Legendre(h,p)=-1 in E and
   Legendre(rs,p)=-1 in M. Use the exact reciprocity theorem, not numerical data.
4. `literal_clusters`: establish every difference valuation and S unit in IC6/7.
   In M use Legendre(3,p)=1 explicitly to exclude b=1 or c=1 modulo p.

## B. Finite free algebra and normalization

Use a complete discretely valued field K of residue characteristic p>3, with
valuation ring o=Z_p, and all four labelled roots in o.
5. `literal_completion_free`: normalize the unit leading coefficient; the
   nested monic quotients have the eight-element basis IC9.
6. `generic_evaluation_inverse`: four distinct roots give the Lagrange inverse
   for f+eta*g. Retain two coefficients per labelled quadratic factor.
7. `quadratic_normal_order`: trace and norm prove N_i maximal for delta_i a unit
   or of valuation1. Split case uses the two evaluations; nonsplit uses the
   actual trace/norm. Standard finite local field facts are explicit imports.
8. `root_pair_lattice`: differences of valuation1 give congruence latticeL2,
   Smith factors1,p, and its supported-coordinate conductor p.
9. `root_triple_lattice`: Newton evaluation gives factors1,p,p^2 and conductorp^2.
10. `signed_normalization_E`, `signed_normalization_M`: use IC17 and k_i to
    obtain all eight elementary divisors and IC18/19, without an unspecified
    integral change of basis.
11. `signed_conductor`: calculate supported normal a+b*theta and stability under
    theta to prove exact conductor exponents, not only a sufficient ideal.
12. `defect_module_actions`: show S subset N stable under original T,eta and
    compute their exact nilpotence indices on the S-moduleN/S. Do not give N/S
    a quotient-ring structure.

## C. Boundary and source actions

13. `local_special_block`: directly reduce H and H' at root multiplicity2/3.
    Prove the displayed quotient presentations and their monomial bases.
14. `special_Jordan_shapes`: compute ranks of powers of epsilon and eta; finite
    linear algebra proves the block partitions.
15. `E_second_digit`, `E_third_digit_obstruction`: T=pw,eta=pv; count p lifts
    modulo p^2; calculate nonzero9ab/(64S) at p^3. No smooth Hensel inference.
16. `M_normalization_chart`: prove the IC24 finite etale rank-six chart and
    original map T=pZ,eta=p*theta; use the three original units for all inverses.
17. `prime_projector_denominator`: monic numerator gives exact valuation1 or2.
    Use uniqueness in IC9 to prove the generic prime sign does not preserve S.
18. `literal_interpolation_order`: prove O_M subset O_E in common labelK^4,
    indexp^2, and the IC29 leading correction of the inverse polynomial.
19. `reciprocal_polynomial` and `signed_twist`: prove IC30 and differentiate the
    exact reciprocal polynomial to obtain IC31 with its sign and p-power.

## D. Global finite-place control

20. `joint_control_source`: for primes l=11 mod12, p=1 mod840, p=-1 modl,
    p>4l, set a=(p+3)/4,u=al. Prove both gates, numerical range and failure
    of u|a^2 at exactly the new prime occurrence l.
21. `joint_control_returns`: prove both rational identities, exact denominatorl,
    and the same original-prime cluster conditions.
22. `joint_height_bounds`: establish real gaps>1, max denominator bound,
    S<B_p and consequent discriminant/derivative inequalities by products.
23. `joint_control_actual_endpoints`: construct the separate integral E and M
    states at the same prime; no appeal to universal ES.
24. `infinite_control_progression`: import the precise Dirichlet statement:
    every reduced residue class contains infinitely many primes. Prove the
    two CRT classes are reduced. For a finite set Sigma choose l outside it.
    The conclusion quantifies a fixed finite place set, not all places.

## E. Executable finite certificates

25. Native natural-number computations certify primality and every displayed
    original state. Rational polynomial and matrix equalities are exact.
26. The full bounded scan is an implementation cross-check. It is not an input
    to the universal local or finite-place theorems, and is not an ES proof.

Outstanding mathematical dependency for the overarching programme:
  forall hard prime p, an original first-half E or M square-divisor gate is occupied.
Nothing in this plan assumes, proves, or renames that missing statement.
