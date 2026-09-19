# Lean-ready dependency plan (no Lean build is claimed)

All lemma names below are proposed names for this tranche, not assertions that a compiled theorem with that name already exists. The proof layer separates infinite arithmetic, finite coverage certificates and particular examples. There are no admitted Lean theorems shipped as verified results.

## Definitions

- `HardPrime p`: `Nat.Prime p` and membership of `p % 840` in the six explicit residues.
- `External p q`: prime q, q<p, and Legendre symbol -1. Fix one standard formal Legendre-symbol convention; never conflate it with a Jacobi symbol at a composite modulus.
- `vertexSigma q`, `squareSource p q j`: sigma in {1,3}, odd t=2j+1, R0=sigma*q, A=(p+R0*t^2)/4. `ValidPort` retains the exact strict range R0*t^2<3*p.
- `DivisorBox A`: the finite dependent product of exponent intervals [0,2 e_l], with its prime indexing and FTA evaluation into positive integers.
- `Channel`, `baseCarry`, `carryDigit`, `carryQuotient`: E has eta=1; M has eta=p.
- `RootSet p q d`: finite roots of the original source polynomial in `ZMod d` with chosen representatives.
- `ClosedPorts p C B`: every nonresidue factor of every valid port j<B at vertices of C lies in C. Keep this distinct from full square closure and from local E/M failure.
- `CycleWord l`: dependent vectors sigma in {1,3} and positive c, all l>=2; ordered affine numerators T_i and D-S.

## Infinite/proof-only dependencies

1. `hard_small_primes_residue`: supplementary reciprocity laws and the explicit six classes prove that2,3,5,7 are residues.
2. `external_nonempty`: FTA of a least nonresidue. `square_source_supply`: source integrality, units, range, Legendre sign and nonempty actual outgoing set. This is the inherited graph input, with squares retained.
3. `divisor_box_equiv` and `normalization_equiv`: prime valuations give the exact integer inverse. `ordered_E_return`, `ordered_M_return`, `ET_permutation_crosswalk`: cleared ring identities, divisibility and positivity.
4. `carry_euclidean_equiv`: original u iff its recorded d,b satisfy the inverse equation and original bounded divisibility. `channel_count_eq_zero_coefficient`: finite sum over exact original fibres. `common_divisor_span`: gcd of A,A' and centred coordinate translation. No independent CRT assumption.
5. `source_root_discriminant`: nonzero quadratic discriminant yields0 or2 roots; `root_reflection`: j -> -1-j with no fixed root. `simple_root_lift`: expansion at x+r^a h, unit derivative, and exact inverse reduction. `edge_weight_sum`: expand valuations as a finite sum of divisibility indicators.
6. `crt_root_tuple_equiv`: the explicit CRT map on pairwise distinct forbidden primes. `reflected_pair_prefix_error`: a rational/integer inequality in one complete period, retaining the prefix origin. `finite_inclusion_exclusion`: apply to original source indices. `source_avoidance_error`, `density_telescope`, `prefix_bound`: prove explicit b_n, including the seven separately checked small cases.
7. `mixed_reciprocity_table`: all unordered mod12 cases; `mixed_edge_budget`: finite edge counting. It must not import the all-3-mod4 no-two-cycle lemma into mixed types.
8. `canonical_cycle_in_closed_set`: finite directed graph with nonempty outgoing sets and no self-loops. Keep all edges and weights in the source; choosing a cycle is used only for a necessary condition.
9. `cycle_affine_composition`, `cycle_gcd_inverse`: integer induction for D,S,T_i, prime divisibility and gcd of distinct vertex primes. `closed_vertex_height`, `closed_prime_bound`, `minimum_cofactor_box`: exact strict inequalities before integer floor conversion. State p<16^(m^2) directly over naturals, without real logarithms.
10. `ratio_order_ideal`: write T_i=A_i x+B_i and D-S=D0*x-S; a cross-multiplied integer proof of strict decrease avoids any analytic derivative dependency. `prefix_box_exclusion` and `linear_upper_endpoint` prove the recursion covers all remaining coordinates.

## Finite proof obligation

11. `no_closed_ports_le_five` depends on a complete checked cover of the finite coefficient domain (l<=5, H=81, v<=20, all remaining c in the displayed interval). The current Python digest is a reproducibility identifier, NOT a Lean proof of coverage. A Lean implementation must either evaluate the exact bounded predicate with an explicitly declared evaluation trust boundary or verify a recursive covering certificate using lemma10. Every pruned box needs its integer inequality; every retained terminal model needs primality/rejection data. The latter list has1915 typed entries, including three rotation-distinct valid cycles. No assertion of a fast full kernel build is made.
12. `three_cycle_exits`: exact finite primality, character and factorization checks for (4201,61,3,43), (12601,409,3,23), (26209,661,3,5507). These discharge the terminal cases, not the coverage lemma.
13. `six_vertex_expansion`: induction on the number of discovered vertices, processing each vertex once. The measure6-card(C) decreases when a new vertex is supplied; before completion at most5 vertices and25 original ports are processed. This proves factor expansion, not selector termination.
14. `growing_expansion`: combine p>=16^(m^2) with the smaller-cardinality contradiction, for the explicit b_(m-1)-port graph.

## Negative and positive finite examples

15. `mixed_pair_all_square_empty`: independently enumerate all22 valid square-source boxes at p12889,q43 and61;246 distinct source-divisor pairs. Retain E/M and exact counts.
16. `noncoprime_carry_counterexample`: p1129,q=t=11,u1845. Both mod11 andmod121 pass, mod1331 fails; digit66.
17. `separate_ES_witness_12889`: verify the actual ordered triple3225,1357856150,3789366 and u9 inverse. It does not establish a universal escape-to-hit implication.

Primary mathematical imports are FTA, quadratic reciprocity and its supplementary laws, elementary CRT, finite set counting, and integer order/gcd arithmetic. The source gives proofs of the auxiliary identities used. No analytic sieve hypothesis or unproved ES selector is an import.
