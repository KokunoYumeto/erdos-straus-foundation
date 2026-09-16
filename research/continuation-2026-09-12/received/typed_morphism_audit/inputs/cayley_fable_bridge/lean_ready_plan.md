# Lean-ready dependency plan — not a compiled proof

Target: characteristic-zero field results, their rational specialization, exact integer arithmetic, and executable finite permutation certificates. Keep rational/geometric/integral conclusions in separate declarations. None of the declarations below is represented as already present in mathlib or checked by Lean.

## Base definitions

Define `FablePoint k := Fin 3 → k`, `BinaryCubic k := Fin 4 → k` with ordered coefficients `(U^3,U^2V,UV^2,V^3)`, `LinearFactor k := Fin 2 → k` and `QuadraticFactor k := Fin 3 → k`. Define the homogeneous resultant explicitly as `a^2*e - a*b*d + b^2*c`; no normalization convention is implicit. Define the fixed-mixed-coefficient base and the open base `B°` by `gamma=-1/2`, `alpha≠0`, `disc≠0`.

## I. Polynomial identities

1. `fable_jacobian`: determinant of the formal derivative matrix is `-2` (`MvPolynomial` differentiation and `ring`).
2. `chart_factor_product`: four coefficient identities for `LQ=C_F`.
3. `chart_resultant_one`.
4. `chart_inverse_source`: reconstruct `u,v,w` from the normalized factor coefficients.
5. `chart_inverse_factor`: reverse composition on the two defining polynomial equations; prove on `u≠0` by `field_simp`, and on `u=0` from the constraints.
6. `binary_discriminant`: `disc C=-DeltaF/4`.
7. `root_derivative_inverse`: substitution into F from `(r,d,gamma)`, with `d≠0`.
8. `infinity_inverse`: `gamma=0` gives the unique source point with `u=0`.
9. `factor_mark_simple`: the resultant condition is equivalent to the chosen linear root being simple.
10. `geometric_fibre_equiv_simple_roots`: use projective-line roots, not just affine roots. Dependencies 2–9. Characteristic zero implies the needed inverses of 2 and 4.
11. `quarter_complete_fibre`: exactly the three displayed rational points; alternatively finite affine-case elimination plus infinity.

## II. Reciprocal arithmetic and normalized transport

12. `cayley_es_identity`: substitute `(-p,4x,4y,4z)` into `e3`.
13. `reciprocal_sum_four` and its inverse on nonzero coordinates.
14. `es_binary_coefficients`: coefficients in terms of the three roots.
15. `ordered_to_marked_fibre_two`: companion transposition; restricted to distinct roots.
16. `ordered_to_coefficients_fibre_six`: use the `Equiv.Perm (Fin 3)` action. Rational surjectivity requires a splitting hypothesis, not supplied by algebraic closure results.
17. `positive_root_region`: over R, prove the exact inequalities, with the elementary two-negative-roots contradiction and the cubic discriminant criterion stated separately.
18. `companion_discriminant`: the displayed polynomial identity and quadratic companion formula.
19. `hard_prime_no_equal_denominators`: derive `(2x-p)(4z-p)=p^2`, positivity, and residue contradiction.
20. `mobius_matrix_det`: exact determinant factorization.
21. `mobius_three_marks`: projective evaluation on infinity, plus and minus one half; all denominator nonzero conditions derived from distinctness.
22. `mobius_binary_transport`: formal five-variable identity.
23. `resultant_change_variables`: degree-(1,2) transformation by `(det G)^2`, verified by coefficient expansion.
24. `normalized_factor_transport`: product and resultant one after the separate `8/D` and `1/64` factors.
25. `normalized_factor_transport_inverse`: retain M and undo its adjugate and both scalar factors.
26. `primitive_reciprocal_return`: positivity, divisibility `4*lcm|p*sum`, and exact prime return. Prove `p0>1` from `sum≤3*lcm<4*lcm` before using primality.
27. `selector_reconstruction`: retain p, R, channel, oriented denominators and divisor u; prove E/M inverses separately. Do not quotient denominator permutations silently.

## III. Finite lattice and polynomial dictionary

Define `Pic := Fin 7 → Z`, intersection signature `(1,-1,…,-1)`, K, and all 27 class vectors. Keep line labels separate from scalar coordinates.

28. `line_classes_invariants`: distinctness, self-intersection `-1`, K-intersection `-1`, and ten incident neighbours.
29. `tritangent_classification`: all distinct triples summing to `-K` are the 30 ELQ triples or 15 perfect matchings. A finite kernel-checkable enumeration can supplement the coefficient proof.
30. `entry_dictionary_equiv`: the displayed matrices use each label exactly once; construct inverse by a finite lookup proved bijective.
31. `tits_signed_support`: exact cubic identity and 45-support equality, including all coefficients.
32. `root_reflection_action`: six roots, reflection involutions and incidence preservation.
33. `weyl_group_closure`: compute the finite subgroup of `Equiv.Perm (Fin 27)` by breadth-first closure. The certificate needs both closure under every generator and reachability of every listed element, not just an unchecked count 51840.
34. `signed_simple_lifts`: verify each sign vector separately against all 45 coefficients. Do not infer Coxeter relations for the signed lifts; preserve the displayed squares.
35. `line_stabilizer_five_pairs`: stabilizer order 1920, surjection to `Perm (Fin 5)`, 16-element even-flip kernel and orbit partition `(1,10,16)`.
36. `four_node_orbits`: four orthogonal roots, 16-element subgroup, explicit orbits of sizes `4,4,4,4,4,4,1,1,1`.

The classical identification of the generic geometric monodromy with W(E6), or of the first-Tits algebra with the Albert algebra, is an external theorem unless separately formalized. Finite enumeration of permutations does not by itself prove that geometric identification.

## IV. Geometric statements and imported dependencies

37. `reciprocal_plane_cayley`: inverse on the coordinate torus and exact basepoint/contracted-line equations.
38. `complete_quadrilateral_resolution`: six blow-ups resolve the cubic linear system; four indicated (-2)-curves contract to nodes. This requires blow-up/anticanonical-model foundations or an explicitly imported geometric theorem. The finite orbit proof does not replace this geometry.
39. `cayley_pencil`: residual conic and homogeneous determinant `s²t²(s+t)/4`; keep the root at infinity and all multiplicities.
40. `cayley_line_images`: the six exceptional images and three opposite-pair images are the nine geometric lines. Distinguish orbit cardinalities from nonreduced Hilbert-scheme lengths.

## Certificate execution boundary

The Python program has been executed in ordinary and optimized modes, but neither is a Lean kernel check. Port polynomial equalities using `ring`/`field_simp`, and finite data using proof-producing or kernel-reduced verification. A convenient path is to reflect each finite statement into decidable equality over bounded types with a verified evaluator. Do not replace external geometric theorems by axioms that are subsequently omitted from a report.
