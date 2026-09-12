# Exact Lean-ready dependency plan

This is a formalization specification, not a compiled Lean file. Names below are proposed local names, not assertions that these declarations already exist in mathlib. No unproved external statement is to be hidden in an `axiom` while claiming complete verification. Each imported theorem must be formalized or explicitly exposed as a remaining dependency.

Use exact rationals for the computational tranche. Suggested basic types are `Fin 3`, functions `Fin 3 -> ℚ`, `Matrix (Fin 3) (Fin 3) ℚ`, tensors `Fin 3 -> Fin 3 -> Fin 3 -> ℚ`, and exact Gaussian rationals as a pair of rationals. Ring identities can be proved after entrywise expansion; finite certificates should be re-evaluated from definitions.

## A. Source ternary operation

A01 `spin_mul`: define `(a,u)*(b,v)=(ab+B(u,v), a*v+b*u)` for a symmetric bilinear form.
A02 `associator_formula`: prove `[(a,u),(b,v),(c,w)]=(0,B(u,v)*w-B(v,w)*u)` by bilinearity.
A03 `spin_left_kernel`: for u nonzero, kernel is `(0,w)` with B(u,w)=0.
A04 `recovery_idempotent`: when B(u,u) != 0, normalized repeated-slot associator is a projection.
A05 `recovery_image_fixed_ann`: prove equality of image, fixed space, and left annihilator (A02-A04).
A06 `blade_table`: verify the full 27 input cells; only the four listed vector cells are nonzero.
A07 `cd_table` / `tagged_mul`: define the exact recursion and C2 tag product.
A08 `seed_products`: verify XY=YX=0 and X²=Y²=-2 using A07.
A09 `seed_annihilator_fixed`: replay rational basis matrices from the certificate, including both containments and rank eight for each seed.
A10 `mobius_clutching`: use the explicit continuous half-angle frame and opposite endpoint coefficient condition to prove the annihilator line is nontrivial. Separate analytic/topological proof obligation; do not replace by sampled angles.

## B. Three marked faces

B01 `cube_eval`, `face0`, `face1`, `face2`: definitions with slots distinct.
B02 `face_edge_compatibility`: necessary conditions by evaluation.
B03 `canonical_face_lift`: define the inclusion-exclusion expression in Theorem 3.1.
B04 `canonical_face_lift_restricts`: prove all three face identities under edge compatibility.
B05 `restriction_kernel`: prove that a tensor in the kernel lies in W0 tensor W1 tensor W2, using the specified splittings.
B06 `face_image_rank19_kernel8`: field dimension argument; separately integral split version for primitive marks over Z.
B07 `gluing_inverse`: subtract canonical lift and restrict to complements; prove both inverse compositions.

## C. Explicit genus-one cube

C01 `moore_cube`: the 27 integers in equation (2).
C02 `slice_determinants`: three formal polynomial identities with -6*(x³+y³+z³-6xyz).
C03 `hesse_smooth`: gradient argument over Q and over F5,F17, checking 3 and 7 invertible.
C04 `rank_two_on_curve`: derivative/cofactor argument; rank at most one contradicts C03.
C05 `typed_kernel_incidence`: construct projective kernel maps and inverse maps using all adjugate charts, not one potentially vanishing chart.
C06 `moore_orbit`: verify all nine exact steps and all reverse-incidence checks in certificate.json.
C07 `projective_point_counts`: enumerate normalized projective points over F5 and F17, obtaining exactly 9 and 21.
C08 EXTERNAL `triangle_is_translation`: Bhargava-Ho, sections 3.2.3 and 5.1.1, following Lemma 5.3. Formalize the three degree-three line bundles and translation class. No curve-equation-only substitution.
C09 EXTERNAL `good_reduction_prime_to_torsion_injective`: prove from the separated formal-group filtration, or import an actual validated theorem. Milne, II.4.1-II.4.2, supplies the written antecedent.
C10 `rational_torsion_divides_three`: combine C03,C07,C09, including exclusion of 5- and 17-primary torsion by the other reduction.
C11 `moore_infinite_order`: combine C06,C08,C10 and H³(O) != O.
C12 `integer_return_faithful`: injectivity of n -> H^n follows from C11.

## D. Cubic norm and three-graded operators

D01 `forward_norm`: det A+det B+det C-tr(C*B*A), retaining arrow order.
D02 `pure_D`: define the three oriented cross-product blocks of equation (5).
D03 `tensor_to_operator_inverse`: equation (6), read each tensor coefficient from one specified matrix entry; all 27 coefficient identities.
D04 `pure_D_square_zero`: prove for arbitrary a,b,c by alternating volume identities.
D05 `SL3_triple_equivariance`: determinant-one changes of bases, with cube input spaces dual to the operator's tensor spaces.
D06 `pure_move_norm_basis`: formal polynomial proof for a=b=c=e1, including vanishing higher trace terms.
D07 `pure_move_norm_general`: derive via D05 and polynomial identity, or expand as an integral identity.
D08 `pure_move_inverse_integral`: I+tD and I-tD are inverse, preserve Z^27 for integral data. Do not assert this for arbitrary sums of pure tensors.
D09 `quadratic_trace_example`: verify N=30, S=31+5t, Tr=10+t for the displayed example.
D10 `graded_basis`: construct 24,27,27 exact matrices as in graded_lie.py.
D11 `graded_closure`: replay all 3003 unordered commutators and rank 24 of mixed brackets; retain basis origins.
D12 `matrix_jacobi`: use associativity of matrix multiplication to prove Jacobi.
D13 EXTERNAL `first_Tits_is_Albert` and `graded_E6_identification`: imported classical structure, not a consequence of dimension alone. The direct coordinate identities remain valid independently of this recognition.

## E. Octonions and real form

E01 `zorn_mul`, `zorn_norm`, `zorn_star`: exact definitions.
E02 `phi` / `phi_inverse`: all 27 entry assignments; both inverse compositions by reduction.
E03 `phi_norm`: formal 45-monomial equality with D01.
E04 `compact_sigma`: conjugate-linear involutions and their intertwining under phi.
E05 `compact_trace_positive`: fixed points have A Hermitian, C=B† and positive trace-square form; analytic real-field step.
E06 `wilson_basis_images`: equation (10), eight Gaussian-rational vectors.
E07 `wilson_zorn_products`: all 64 basis products; extend by real bilinearity.
E08 `wilson_zorn_inverse`: the signed permutation of Re(alpha),Im(alpha),Re(u_j),Im(u_j), giving rank eight.

## F. Leech short shell

F01 `wilson_table`: cyclic Fano triples (t,t+1,t+3) and conjugation.
F02 `L_membership`: doubled-coordinate parity and sum-mod-4 criterion.
F03 `right_lattice_membership`: prove inverse-right-multiplication tests for Ls and L*bar(s), including division by 4 in doubled coordinates.
F04 `leech_joint_membership`: all three individual, all three pairwise, and final three-way conditions.
F05 `wilson_roots`: enumerate all 240 roots with the specified parity.
F06 `wilson_three_shapes`: finite sets including all allowed units, signs, and coordinate permutations.
F07 `short_shell_cardinality`: disjoint counts 720,11520,184320; total 196560.
F08 `every_generated_vector_passes`: independently test F04 and norm four for every generated vector.
F09 EXTERNAL `wilson_identification_and_completeness`: Wilson's identification of this lattice and minimal-vector shell; do not replace with a dimension count.
F10 `iota_inverse_and_norm`: trace square 4 times Wilson norm and cubic 2 Re((xy)z).
F11 `leech_cubic_histogram`: replay all 196560 exact values, with counts in leech_certificate.json. Verify examples separately; checksum is identity evidence only.
F12 `leech_to_Tits`: compose E07/E08, F10, and E02. No lattice closure or full Co0-invariance assertion.

## G. Marked Erdős-Straus arithmetic

G01 `ES_cube`: tensor coefficients 12*d_i*delta_ij*delta_ik-p.
G02 `ES_cube_inverse`: recover p and each ordered denominator on the exact image.
G03 `ES_face_determinant`: all three contractions equal 432*(4xyz-p*(xy+xz+yz)).
G04 `ES_face_kernel`: positivity implies rank two at a hit, kernel the reciprocal triple.
G05 `selector_marking`: exterior and middle reconstruction; retain p,R,u,h,r,s,quotient,tag and denominator order.
G06 `selector_divisor_inverse`: exact formulas in section 7, with u|a² and 0<R<p hypotheses.
G07 `rank_two_left_right_equivalence`: deterministic exact Gaussian pivots and both inverse matrices.
G08 `infinite_cube_attachment`: use G07 on Moore M0(O) and the ES face, retain all G_i and denominator scale.
G09 `attachment_conjugates_return`: kernel maps transform by G_j^-1 phi_ij G_i; use C11 for infinite order.
G10 `p1201_attachment`: replay the 27 integer coefficients, scale 9522, all inverses and the listed turn.
G11 `equal_three_faces_return_two`: if all three marked faces are the same passing matrix and the cube is nondegenerate, incidence gives H²(e)=e. Apply only to this restricted family.

## H. Cayley integral return and exponential coefficients

H01 `Cayley_ES_identity`: e3(-p,4x,4y,4z)=16*ES_polynomial.
H02 `Cremona_inverse`: polynomial composition gives a_i*(product a_j)^2, with all a_i nonzero.
H03 `positive_primitive_reciprocals`: uniqueness of primitive A:B:C=1/x:1/y:1/z.
H04 `return_integrality`: 4*lcm(A,B,C)|p*(A+B+C) iff all reconstructed denominators are integral.
H05 `p0_prime_return`: p0>=2; for prime p, p0|p iff p0=p.
H06 `valuation_return`: exact max formula with v_l(A+B+C) retained, not replaced by separate valuations.
H07 `exponential_quotient_eval`: unconditional map from free E-ring modulo the two forced E-relations.
H08 EXTERNAL-CONDITIONAL `Terzo_kernel_SC`: explicitly Schanuel-dependent theorem 2.4.1; never used in C11 or the ES certificate.
H09 `free_cube_eval_kernel`: kernel J^27, where J is actual coefficient evaluation kernel.
H10 `period_subgroup`: varpi=2XY satisfies E(varpi)=1; evaluation proves Z*varpi torsion-free unconditionally.
H11 `period_integer_return`: marked group isomorphism n*varpi -> H^n using C12. This is not an E-ring morphism.
H12 `full_exp_kernel_SC`: only under H08, identify the full exponential kernel with Z*varpi.

## Completion boundary

The list does not contain a theorem producing p0=p for every prime. Such a theorem requires additional arithmetic, rather than an assumption named “admissibility” or a surjectivity statement silently inserted into G08. Certificates of existing witnesses and infinite return are separate from witness production. Formalizing the imported structural theorems is also distinct from replaying the finite exact calculations.
