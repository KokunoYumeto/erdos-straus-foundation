# Exact Lean-ready dependency plan (not a Lean build)

Names below are proposed obligations, not claims that matching declarations exist.
Use the project's existing coordinated toolchain and resource policy; do not silently replace its original G(R), supported-zero, or relation-quotient definitions.

## Arithmetic input
1. `shell_units`: p prime, p=1 mod4, p<4a and 2a<p imply R=4a-p positive odd and coprime to pa.
2. `divisor_exponent_equiv`: bounded beta_i in [-e_i,e_i] bijects divisors of a^2, with valuation inverse.
3. `rational_candidate_identity`: both ordered triples A2 solve the rational reciprocal equation.
4. `exact_reduced_denominators`: both nonfirst coordinates have reduced denominator R/gcd(R,g_c).
5. `normalized_hit_equiv`: A4 and A5 give complete marked forward/inverse maps, including E/M.
6. `prime_defect_product`: D=product l^(max(v_l R-v_l g,0)).

## Boundary comparison (reuse PR30's actual quotient conventions)
7. `truncated_monomial_basis`: J_d has basis multiindices 0<=b<=d.
8. `joint_shift_kernel`: intersection of multiplication-by-z_l kernels equals the top line.
9. `socle_equiv`: e_alpha -> top_alpha, inverse coefficient extraction; all support labels retained.
10. `augmentation_comparison`: epsilon o s is exactly diag(D_alpha=1).
11. `defect_degree_zero`: its rank/trace and multidegree-zero socle count equal the original canonical success count.
12. `reduction_kernel`: Q_d,d' discards precisely monomials exceeding d'.
13. `reverse_embedding`: multiply by z^(d-d'), inverse on the image; show QI is not generally identity.
14. `coefficient_transition_defect`: Q M_x - M_x' Q=(x-x')Q. Instantiate both source and coefficient defects rather than claiming naturality.
15. `supported_zero_image`: use the original G(R)-linear quotient; an annihilated class retains its receiving support, not tau.

## Source weights and previous cohomology
16. `split_addition_fibre`: W1, including nonempty intervals and full inverse set.
17. `weighted_pull_average`: W2-W4, adjoint equality and Pythagoras for the exact occurrence weights.
18. `boundary_maps_commute`: pullback and averaging commute with every prime variable, socle insertion, augmentation, and defect scalar.
19. `two_quotient_span`: old residue H0 is Q^I, success image is Q^S; prove the two explicit kernels of W5.
20. `averaged_mass_comparison`: W6, column sums one; no general isomorphism between the two quotient spaces.
21. `mixed_Gram`: full B*GI B, retaining nonzero cross terms; verify W7 by normalization.

## Finite moment theorem
22. `Gram_PSD_and_range`: both M2 Grams are PSD on the declared support and each b annihilates the kernel.
23. `singular_normal_solutions`: finite-dimensional range/kernel orthogonality yields a solution; RREF and its full nullspace is a separate executable witness.
24. `canonical_extrema`: complete square for upper and lower M3, all optimizer fibres M4.
25. `endpoint_mass_bounds`: success atoms contribute H and failure atoms have the required signs.
26. `relation_secants`: M6 from normal-equation orthogonality, primitive divisible by x-1; retain zero lower weight at x=c.
27. `nested_and_finite_exact`: monotonicity and polynomial vanishing at every nonendpoint support point.
28. `four_moment_criterion`: 2x2 negative-semidefinite equivalence; positive direction cannot vanish at x=1.
29. `Chebyshev_stopping`: M7 and unique integer recovery; no moment-computation complexity claim.
30. `signed_interval_certificate`: apply coefficientwise rational enclosures in the correct orientation.
31. `matrix_and_integer_examples`: replay exact finite certificates and original denominator inverses.

## Explicit non-imports
No proof of uniform ES occupancy, RH, purity, analytic moment identification, a full Koszul/Tor functor, or source-wide Lean certification is assumed. The source PR30 has a proved explicit kernel model; our independent multi-prime tensor model requires its own declared variables and maps. Finite numerical source reports are not substituted for any of these proofs.
