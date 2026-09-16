# Exact Lean-ready dependency plan

Status: no Lean compilation has been run. This is a dependency plan, not a proof certificate accepted by Lean.
The Python data are deterministic finite certificates. No theorem about ES existence may be imported as an assumption.

## Representations

Use `Fin 24 -> Int` for numerators. The actual vector is numerator / sqrt(8), so pairings can be represented as rational numbers `(sum x_i*y_i)/8`. Define the binary code over `ZMod 2` by the given 23 generators. `LeechNum` is the subtype satisfying the three congruence/code conditions in `note.tex`, equation (1). Prefer an additive subgroup realization for the infinite statements.

Separate symbols are required for (a) the Klein group of coordinate permutations, (b) the tetrahedral group, (c) the order-twelve coordinate permutation T, and (d) its homogeneous 2x2 lift. The lift has twelfth power minus identity; its coordinate permutation has twelfth power identity.

## Finite foundation

L01 `golay_generators_rank`: rank 12 by finite elimination.
L02 `golay_self_dual`: pairwise orthogonality and dimension.
L03 `golay_weight_distribution`: all 4096 words; weights 0,8,12,16,24.
L04 `leech_num_add`: closure, with all parity cases and code carries retained.
L05 `leech_num_neg`: closure under negation.
L06 `leech_pairing_integral`: derive from evenness/polarization, or congruences.
L07 `leech_norm_even`: squared norms in 2Z.
L08 `leech_minimum_four`: eliminate squared norm 2 explicitly. No external uniqueness theorem is required for this inequality.
L09 `leech_unimodular`: determinant/index calculation of the even sublattice and odd coset. This is needed only for determinant/discriminant conclusions.
L10 `C_J_T_preserve`: check generator permutations on code basis and congruences.
L11 `T_four_eq_C`, `T_twelve_eq_id`: all coordinate entries.
L12 `phase_octads`: the three concrete octads partition Fin 24 and are in the code.
L13 `phase_actions`: V4 fixes them, C cycles them.

## Three-coordinate inverse

L14 `frame_pairing`: `(w_i,w_j)=4 delta_ij`.
L15 `trace_integral`: P_i is the lattice pairing with w_i.
L16 `dual_lifts`: the three explicit b_i are members, norm four, and `(b_i,w_j)=delta_ij`.
L17 `trace_section`: `P (sigma t)=t` for all t in Z^3, by linearity from L16.
L18 `trace_fibre_equivalence`: additive equivalence between LeechNum and Z^3 x ker(P), with the displayed inverse. Do NOT claim this equivalence is isometric.
L19 `frame_primitive`: rational frame coefficients of lattice elements are integers, pairing with b_i.
L20 `kernel_rank_det`: rank 21, determinant 64; the quotient index is 64.
L21 `orthogonal_fibre`: q(t)+r(t)+K, exact Pythagorean identity.
L22 `kernel_discriminant`: r identifies (Z/4Z)^3 with K*/K. Pairing matrix 15/4 I, quadratic form modulo 2Z.

## Shortest lifts for all integer inputs

L23 `ordinary_representatives`: check the 62 supplied nonzero norm-four representatives, their exact reduced traces and lattice membership. Only these finite witnesses are needed for the existence half.
L24 `zero_representative`: zero has minimum norm in its class.
L25 `exceptional_222_lower_bound`: parity forces even numerator, write x=2y, use sum(y)=12 and y_i^2 >= |y_i| to obtain norm >=6.
L26 `exceptional_222_witness`: supplied balanced dodecad gives equality.
L27 `trace_translate_four`: translation by w_i adds four to one trace and preserves the perpendicular component.
L28 `shortest_lift_formula`: deduce the exact mu formula for EVERY t from L08, L21, and L23-L27. Do not infer it from tests of bounded t.
L29 `multiplicities`: optional complete shell enumeration plus 1232 balanced dodecads; not needed for L28.

## Retained tetrahedral action

L30 `fixed_code`: among all 64 unions of the six tetrads exactly the eight paired patterns are in the code.
L31 `fixed_trace_image`: odd V4-fixed numerators are impossible; even fixed numerators give P in 4Z^3, and the frame gives the converse.
L32 `no_equivariant_choice`: a section at e0 would be V4 fixed, contradicting L31. This applies even to a set-theoretic equivariant section.
L33 `affine_cocycle`: kappa_g(t)=g sigma(t)-sigma(rho_g t), verify its target K and composition law by expansion.
L34 `full_equivariant_fibres`: action on (t,k) is (rho_g t,gk+kappa_g(t)), with inverse and exact group law. This is the correct positive replacement for a nonexistent invariant choice.

## All twelve time views

L35 `time_relations`: P_(n+4)=rho P_n and common total trace.
L36 `pack_unpack`: the four common-sum triples are additively equivalent to Z^9.
L37 `nine_lifts`: verify nine Leech members and the exact 9x9 identity of readouts.
L38 `joint_section_and_fibres`: all common-sum input data lift, complete rank-15 kernel.
L39 `joint_Gram_det`: rational Bareiss/Gaussian certificate gives 5292; combine with primitivity/unimodularity for kernel determinant.
L40 `T_kernel_cocycle`: kernel stability and affine action using delta(a)=T sigma9(a)-sigma9(Ga); twelve-step return.
L41 `section_bound`: the supplied Gram matrix has absolute row sums <=15; derive norm <=15 sum a_i^2.

## Arithmetic return and limitations

L42 `ES_polynomial_equiv`: for p>0 and positive integer t, reciprocal equation iff F_p(t)=0; clear the positive denominator.
L43 `marked_selector_return`: E/M quotient and divisor inverses, all denominators positive and the raw order retained; preserve r,s,h and u exponents.
L44 `ES_lattice_equiv`: use L17 and L42. No existence conclusion follows unless the cubic fibre is proved nonempty.
L45 `ES_height_bound`: Cauchy on positive t plus L21 gives norm >=27p^2/64.
L46 `ES_222_impossible`: compute F modulo 8 for odd p and all t_i=2 mod4.
L47 `theta_fibre_decomposition`: absolute convergence, orthogonal coset decomposition, coefficients indexed by t mod4. This is an analytic lemma beyond the finite checker.
L48 `minimal_shell_moment`: exact symbolic-in-p sum from all 196560 finite points gives constant 737280, linear term 0, quadratic term 241920. This route does not require formalizing the full 11-design theorem.
L49 `unsuccessful_T_orbit`: use L37 with every time trace equal to (p,p,p), get a genuine lattice orbit of defect p^3. This is NOT a counterexample to ES.
L50 `single_coordinate_move`: translation by n b_i changes defect by n D_i, with exact divisibility and positivity condition. No termination statement.
L51 `positive_auxiliary_sum_implies_ES`: if a separately supplied summable nonnegative weight has a positive sum of W(1-F^2), an integral zero exists. This is a conditional certificate criterion, not the conjecture, and no such all-p weight has been constructed here.

## Imported contextual theorems, not replayed

Brouwer's standard-lattice identification, the full Leech covering-radius theorem, Cohn-Kumar's design result, and Bright-Loughran's arithmetic-geometric theorems retain their cited source scopes. The primary inverse L17/L28/L38 can be formalized from the explicit code model without using any ES existence theorem or full classification of lattices.
