# Exact Lean-ready dependency plan

This is a formalization specification; no Lean compilation was run. Use positive rational denominators until the D=1 gate. Do not formalize a restricted atlas as the whole conjecture.

## Arithmetic layer (no imported conjecture)

1. `scaled_solution`: a witness at a divisor parameter scales to a witness at a multiple.
2. `minimal_false_is_prime`: well ordering and 1 imply prime minimal counterexample.
3. `small_congruence_witnesses`: the displayed p=2, p=3 mod4, p=2 mod3 and p=13 mod24 formulas.
4. `full_minimum_shell`: positivity and choosing a minimum give p/4<a<=3p/4.
5. `shell_units`: prime p and 0<a<p imply gcd(a,R)=gcd(p,R)=1.
6. `divisor_box_equiv`: vectors 0<=f_q<=2e_q biject with u|a².
7. `primitive_coordinates`: g,r,s,h maps, integrality, gcd and inverse.
8. `rational_E_identity`, `rational_M_identity`: positive rational maps and residual products.
9. `factor_pair_inverse`: d_Y*d_Z=p²a² and v_p(d_Y) in{0,1,2}; exact E-swap/M inverse.
10. `atlas_completeness`: 4,6,8,9 imply global witness iff some integral atlas leaf.
11. `atlas_size`: divisor pairing implies cardinal<= (p-1)².
12. `gcd_scaled_by_unit`: gcd(R,cN)=gcd(R,N) when gcd(R,c)=1.
13. `common_denominator_E`, `common_denominator_M`: use 12 and explicit congruences.
14. `least_clearing_factor`: first coordinate integral, last denominators equal D.
15. `cleared_solution`: X=Dq is integral at pD; exact F_p(X)=p(D-1)S(X).
16. `recover_clearing_from_trace`: D=4prod(X)/(pS(X)), positivity nonzero S.
17. `canonical_collision`: exterior distinct; middle repeated iff u=a, with D=R.
18. `same_shell_defect`: u_M=p*u_E modR implies equal D.
19. `middle_complement_defect`: inverse involution preserving D.

## Counterfactual object / validator

20. Define canonical tagged `Candidate` as finite dependent sum, retaining all valuations.
21. Define `DefectAtlas` and `FullNegativeCertificate`; separate type for a restricted certificate.
22. `negative_certificate_sound`: a positive valuation deficit for every full leaf excludes every witness via 10.
23. `negative_certificate_complete`: if every leaf fails, choose least prime divisor of D.
24. `unit_iff_no_witness`: finite coordinate algebra multiplier delta=(D-1)/2.
25. `bounded_inverse`: inverse coordinate 2/(D-1) in(0,1].
26. `polynomial_success_projector`: evaluate product_{j=1}^{p-2}(1-H/j) coordinatewise.
27. `counterfactual_support_filters`: residual3 and residual7 direct proofs, plus ray(1,1) factor ofp+1.
28. `restricted_graph_components`: computational reflection on the explicitp241a64 graph, not a claim for allp.

## Positive forcing

29. `signed_box_inversion`: inverse residue fibres equal; only zero exponent vector fixed.
30. `paired_collision_count`: derive the product multiplicities in the difference box.
31. `balanced_integer_energy`: exchange argument for N balls in M bins; exact remainder formula.
32. `symmetric_energy_minimum`: parity of involution bins and least marginal-cost greedy proof.
33. `energy_forces_marked_hit`: contraposition plus explicit exponent inverse, no density input.
34. `actual_anchor_box`: primitive signed factor pairs, exact costs and minimizing representatives.
35. `largest_outside_divisor`: quotient group C2; complementary divisor contains a least outside prime occurrence.
36. `angular_packet_integrality`: nd|A,t|b -> dtn|a; gcd and all quotient formulas.
37. `angular_inverse_fibres`: t=ds/(nr), g=d/r and exact finite anchor-pair conditions.
38. `positive_koide_subinterval`: rational radical bounds prove1/8<alpha.

## Retained geometric and lattice layers

39. `cayley_scaling`: all24typed face roots invariant under common D scaling; affine scale carries the return.
40. `labelled_factor_collision`: full unnormalized factors always; resultant normalization only at d!=0.
41. `fable_coordinate_inverse`: rational identities on simple-root locus; keep d,eta,scale and flags.
42. `resolvent_scale`: degree-two scaling under a->D a.
43. `Leech_section_inverse`: pinned b_i membership and P b_i=e_i; complete fibre sigma(t)+kerP.
44. `all_octad_inverse_and_syndrome`: inherited theorem; certificate checks its instances, no theorem promotion from those instances.
45. `Wilson_signed_inverse`: full signed dictionary and exact joint lattice conditions.
46. `Albert_defect_correction`: explicit octonion multiplication and all norm terms retained.
47. `marked_conjugacy`: coordinate bijections intertwine multiplication operators; noninjective projections keep fibre.
48. `trace_spectral_alternative`: on l² of positive trace states, maximal-domain F² multiplier is self-adjoint; false case bounded inverse, true case infinite kernel along kerP.

## Imported human results and trust boundaries

Yamamoto/Monks--Velingker/Elsholtz--Tao: provenance for 8--10, but required coordinate claims are reproved. Wilson's infinite model theorem and the preceding integral Leech sections require their own formal proofs or explicitly declared imports. Bright--Loughran Theorem1.8 is an external arithmetic-geometric restriction, not a premise needed by 1--38. No hypothesis asserting a good shell exists may be introduced in `energy_forces_marked_hit` or the counterexample type.

The finite certificate checker must recompute all exponents and primality, reject omitted leaves, distinguish scope tags, and avoid relying on a stored zero hit count. Use exact integers/rationals; the supplied Python code uses no removable assertions.
