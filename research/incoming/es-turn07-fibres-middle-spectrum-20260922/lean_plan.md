# Exact Lean-ready dependency plan (no Lean build)

Lean and lake were not installed in the current runtime. The plan below is not
an axiom bundle, and none of the unresolved occupancy implications is a lemma.

A. Arithmetic types over Nat/Rat
1. Define OriginalTrace(p,a,u,channel,swap) with primality p, p=1 mod24,
   p<4a<2p, u|a², squared gate, and the exact orientation convention.
2. Define Carrier(a) using c in {1,2,3,6} and q>3 prime. Prove uniqueness.
3. Prove gcd normalization h=g²/u,r=u/g,s=a/g and primewise exponent inverses.
4. Formalize the rational factor-pair completeness and p-valuation split.
5. Import or reprove the corrected mixed return, with pHJr second denominator.
6. Define SortedMiddle target and recover its unique primitive r<s orientation.
7. Squarefree divisibility lemma: delta*t² | (delta*s)² iff t|s for odd t
   and squarefree delta. Prove via Nat.factorization or coprime exponent bounds.
8. Prove the E inverse equivalence and the source carrier test exactly.
9. Prove the M equivalence R*t² | (R*A)² iff t|A for squarefree R.
10. Prove small-seed and original complement cases; old and new a stay distinct.
11. Prove disjointness, two orientations and the finite fibre cardinality formula.
12. Implement #eval checks for the supplied finite examples, with primality
    certificates/trial-division decisions. No universal conclusion from enumeration.

B. Coefficient and receiver maps
13. Finite free Z modules: fibre sum and its basis of differences, section only on
    image, exact rank n_W-1. The metric-minimum map is separate from integral section.
14. Complex literal receiver: xi nonzero, d nonzero; prove formulas recovering
    d,A,ell from (p,O) by field_simp and ring. Preserve 16 sign frames.
15. Finite-dimensional quadratic minimization gives the quotient covariance.

C. Analytic middle spectrum
16. Define rational root family, actual branch convention and compensated B(z).
    Construct analytic square-root units near0 after exact derivative valuations.
17. Prove the printed B0,B1 via coefficient differentiation/ring identities.
18. Prove complete leading compound expansions with the enumerated row/column
    powers and the full rank-three leading row; relate compound norm to products
    of singular values in finite dimension.
19. Prove all first relative singular coefficients by ratios, and the exact
    inverse factorization. Retain fixed-R,u quantifiers for all O terms.
20. Isolated-eigenvalue block argument for the right Gram: recover tiny Y/Z
    components relatively. Deduce heat limits for tau>0 and the four row tests.
21. Prove the two CRT progressions have coprime residue/modulus and every prime
    member is a stated M witness. Dirichlet is a precisely identified classical
    external dependency. Do not replace it by a bounded prime search.
22. Obtain hard-middle exponent optimality from positive subsequential limits
    and the currently proved uniform upper bounds. No mixed-image optimality.

A machine-checked version would need a substantial matrix/singular-value analytic
layer. The delivered exact Laurent and finite arithmetic checks support the
written proof; they are not represented as this Lean formalization.
