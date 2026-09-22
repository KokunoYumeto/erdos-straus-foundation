# Erdős–Straus: the research map

The question is whether every integer $n\geq2$ admits positive integers
$x,y,z$ with $4/n=1/x+1/y+1/z$. Repeated denominators are allowed.
This workbench pursues both explicit arithmetic constructions and exact
correspondences with other mathematical structures. It has not resolved the
conjecture. The purpose of this page is to help a reader enter the full arguments,
understand why they were tried, and continue them.

Read the [current 124-page ES/Fable cumulative reader](research/incoming/es-fable-zeta-bridge-20260920/output/pdf/ES_FABLE_ZETA_CROSSWALK.pdf)
with its [complete TeX, exact checks and audit](research/incoming/es-fable-zeta-bridge-20260920/README.md).
The earlier [86-page expanded supplement](https://zenodo.org/records/22678971/files/07_Exact_Bounded_Transport_Expanded_72_Statements_2026-09-08.pdf)
and its [complete TeX, proofs and checks](research/expanded-2026-09-08/exact_bounded_transport_72)
remain preserved as a separate edition.
The source files here are byte-for-byte copies of the published archive.
The [earlier readers and corrections](README.md#start-reading) remain available.
The routes below describe this supplement, not an exhaustive classification of
every historical programme in those earlier books.

## The common arithmetic object

The supplement starts with $h>0$ and a prime $p=12h+1$, then chooses
$a\in\{3h+1,\ldots,9h\}$ and defines $R_a=4a-p$, $S_a=pa$.
It retains the full sets

$$
E_a=\{u\in\mathbb Z_{>0}:u\mid a^2,\ R_a\mid4u+1\},\qquad
M_a=\{u\in\mathbb Z_{>0}:u\mid a^2,\ R_a\mid u+a\}.
$$

The full count is $Q_p=\sum_{a=3h+1}^{9h}(|E_a|+|M_a|/2)$.
The original positive-integer equation at $p$ holds exactly when $Q_p>0$.
The definitions, both directions, the ordered witness reconstruction and its
inverse are proved in [the original shell system](research/expanded-2026-09-08/exact_bounded_transport_72/bounded_transport.tex#L36).
This full finite criterion remains the common object across the following routes;
a restricted selector does not silently replace it.

## Routes through the complete proofs

| Research direction and motivation | Read the actual construction and proof | Where the investigation currently stands |
| --- | --- | --- |
| Full-shell occupancy: extract structural factor criteria while retaining the complete primewise problem. | [Residual-three and residual-seven factor sieves](research/expanded-2026-09-08/exact_bounded_transport_72/first_two_shell_sieve.tex); [all-shell packets, ordered reconstruction and no-hit criterion](research/expanded-2026-09-08/exact_bounded_transport_72/counterexample_sieve/all_shell_no_hit.tex). | The first two shells have exact factor-level tests. The all-shell criterion is necessary and sufficient at each fixed prime; these results do not establish occupancy for every prime. |
| Simultaneous constraints: determine whether local conditions lift to one tuple inside its original bounds. | [Exponent-lattice gluing and bounded divisor CRT](research/expanded-2026-09-08/exact_bounded_transport_72/bounded_transport.tex#L224); [unary and Boolean coordinates](research/expanded-2026-09-08/exact_bounded_transport_72/unary_boolean_transport.tex); [shared-variable CRT](research/expanded-2026-09-08/exact_bounded_transport_72/shared_variable_crt.tex); [input/output incidence](research/expanded-2026-09-08/exact_bounded_transport_72/input_output_incidence.tex). | Integral compatibility and intersection with the original finite box are both retained. The bounded algorithms return complete fibres; the prime-output projection is not asserted to reach every prime. |
| Witness propagation: classify the maps that actually carry an integer solution, including order, scale and codes. | [Ratio transport, shears and norm subdivision](research/expanded-2026-09-08/exact_bounded_transport_72/bounded_transport.tex#L676); [fixed-denominator successor](research/expanded-2026-09-08/exact_bounded_transport_72/exact_audit/fixed_y_successor.tex); [raw scales and both code systems](research/expanded-2026-09-08/exact_bounded_transport_72/raw_scale_hit_incidence.tex); [four swaps and exact integral orbits](research/expanded-2026-09-08/exact_bounded_transport_72/boundary_swap/boundary_swap_completion.tex). | Domains, inverse maps and failed returns are calculated. The occupied residual-three domain also has a proved global first code; it does not cover the empty residual-three domain. |
| Divisor categories and cyclic coordinates: construct exact interfaces with the literature while preserving arithmetic return. | [Embedded ordered groups, intersections and marked returns](research/expanded-2026-09-08/exact_bounded_transport_72/connes_reading/connes_primitive_intersections.tex); [affine correction for the full shear](research/expanded-2026-09-08/exact_bounded_transport_72/bounded_transport.tex#L1272); [integral augmentation and cyclic traces](research/expanded-2026-09-08/exact_bounded_transport_72/integral_cyclic_bridge.tex). | The original gluing obstruction and bounded return acquire explicit categorical and cyclic coordinates. The finite intersection still has to be occupied; the coordinate map alone does not force it. |
| Auxiliary torus and operators: apply exact covering maps to arithmetic packets, then return their sampling analysis to directional inverses. | [Literal cover and arithmetic sampling](research/expanded-2026-09-08/exact_bounded_transport_72/ns_operator_bridge/torus_cover_lemma.tex); [character-coset correction](research/expanded-2026-09-08/exact_bounded_transport_72/ns_operator_bridge/sieve_character_cover.tex); [continuous transfer and sampling fibres](research/expanded-2026-09-08/exact_bounded_transport_72/ns_operator_bridge/reverse_proof_transport.tex); [sharp directional inverse](research/expanded-2026-09-08/exact_bounded_transport_72/ns_operator_bridge/reverse_smooth_inverse.tex). | The corrected finite averaging retains the original packet coefficients. Continuous inverse estimates have full proofs and constants. This does not assert a construction of a fluid solution from a prime or independent verification of a complete fluid blowup proof. |

These are connected lines of work. The same retained bounded exponent vectors
enter the congruence calculation, the cyclic obstruction, and the finite character
packets. The witness maps determine which arithmetic records those interfaces
actually transport. The links above contain the complete maps and proofs; this
navigation page is not a replacement for them.

## Current finite source atlases and branch reductions

The 19 September continuation now has complete, separately typed finite atlases
for both original first-half channels:

- [Middle two-chart atlas](research/incoming/es-turn07-middle-cutoff-20260919/README.md):
  sharp square-root bounds for the least exact middle cofactor, with direct and
  cofactor inverses.
- [Exterior three-chart atlas](research/incoming/es-turn07b-exterior-atlas-20260919/README.md):
  strict cubic cutoff for the least of \((R,D,v)\), with direct, reciprocal and
  complement–norm inverses retaining the exact \(K(v)\) availability condition.
- [Small-shape rigidity and channel rescue](research/incoming/es-turn07-shape-rigidity-20260919/README.md):
  an exact ordered marked cubic with its full source inverse, a squarefree-part
  map from every diagonal exterior state to an original middle state, complete
  hard-prime radius-seven classification, and a middle return for the sole
  radius-eight nonsingular profile.
- [Normalized ES quartic and exact Fable--weighted-conductor bridge](research/incoming/es-fable-zeta-bridge-20260920/README.md):
  the literal root set $\{p,x,y,z\}$ gives a normalized quartic in the generic
  degree-eight signed cover, with intrinsic prime, exact image hypersurface,
  complete source fibre, Turn 7 inverse, and a fixed original conductor square.
  The reciprocal-cubic suspension is retained separately as a seven-state
  nonproper degeneration. The exact elementary transform between them,
  including its scale fibre, projective root-scheme maps, discriminant
  transport and 14-point signed fibre product, is proved rather than left as a
  presentation-level comparison. An explicit invertible raw-cell--Lorentz map
  retains the archived three-dimensional tetrahedron, while the odd receiving
  determinant has an exact irreducible ES pullback and a proved positive-real
  intersection. The same cumulative source now proves that
  every witness at a prime \(p\equiv1\pmod {12}\) lies in the eight-sheet
  domain; at fixed \(p\), over the open base
  \(\mathcal B_p=\{(A,C):ACd_p\operatorname{Disc}(g_p)\ne0\}\), the cover has
  a rank-\(2+6\) split, order-\(48\) monodromy and deck group
  \(C_2\times C_2\). Its reciprocal signed coordinate
  gives a finite flat rank-eight collision completion, and an invertible
  marked moment frame isolates the separate odd receiving divisor.
- [Prime-local fibre, root order, and negative-square transfer](research/incoming/es-turn07-fabel-arithmetic-bridge-20260920/INTEGRATION_AUDIT.md):
  the seven-state reciprocal fibre has ramified quadratic factors in the
  exterior channel and unramified quadratic factors in the middle channel,
  although both have exactly three local rational points.  Its exterior root
  order has index \(p\) in its normalization and the labelled exterior-to-middle
  interpolation loses exactly one power of \(p\).  Changing the arithmetic
  target on the negative-four-square locus gives explicit same-prime middle
  states and complete corrected inverse fibres. The complete fixed-(Q)
  theorem then classifies all such middle returns by the finite divisor set
  (U\mid((h+1)/4)^2, h\mid p+4U), including nonsquare words missed by the
  selected transfer.
- [Exact cofactor capacity completion](research/incoming/es-turn07-capacity-completion-20260920/README.md):
  the fixed-target divisor set \(\mathcal A_t(j)\) is classified exactly into
  canonical, companion and finite branches with an inverse for every word.
  The finite branch has sharp boundary \(h\le t^2-3t+1\), attained by
  infinitely many original hard-prime exterior states. Every fixed
  \(t\ge4\) also has infinitely many constructed exterior states with an
  empty complete same-grade middle box; those exterior states remain ES
  solutions.
- [ES/Fable/RH multi-track continuation](research/incoming/es-rh-multi-20260920/README.md):
  an explicit positive-real ES ray crosses the odd-frame divisor at one
  exactly isolated rank-three point while the quartic remains squarefree.
  The collision completion carries a perfect residue pairing whose trace
  degeneration is exactly multiplication by \(2\eta^3\), including the
  nonconstant local residue-unit correction. The native orthogonal-polynomial
  Gram is then recovered by its exact second-kind multiplier; an arbitrary ES
  polynomial retains a computed relation defect. The final inverse-trace and
  common-parameter Bernstein tracks are RH-facing interfaces and do not count
  as ES occupancy results.
- [Original integral completion and defining-prime normalization](research/incoming/es-turn07-integral-completion-20260920/README.md):
  the literal-root rank-eight order has exact exterior and middle indices
  (p^2) and (p^9), with all Smith factors, conductor ideals, inverse
  lattices and reduction kernels.  The
  [general defining-prime module](research/incoming/es-defining-prime-continuation-20260920/README.md)
  retains every closer-pair valuation, proves the translated-chart quadratic
  twist and fixed-prime gluing, and identifies the local signed-label
  representation and its Artin conductor.
- [Arithmetic frame nonsingularity and signed descent](research/incoming/es-rh-continuation-b-20260920/README.md):
  three quadratic characters force the original odd receiving frame to be
  invertible for every witness in (3456) reduced classes modulo (521220).
  The genuine witness ((13;4,18,468)) gives an exact descent at (q=61),
  with no original rational signed point, eight quadratic-extension points,
  and eight rational points on its specified nonsquare twist.  Separate
  determinant and finite-heat tracks retain their own proof and executable
  verification boundaries.
- [Global trace integrality and exact raw-source fibres](research/incoming/es-turn07-trace-rigidity-20260920/README.md):
  the first two power traces form a complete integrality test for rational
  three-denominator ES targets. On the complete raw integer gate, one literal
  trace has denominator $U/\gcd(U,pa^2)$, recovers the E/M channel, and has
  exactly the retained middle involution $U\leftrightarrow a^2/U$ as its
  nontrivial fibres. The same module computes the square-part residual away
  from that gate and the irrational algebraic boundary of the rational theorem.
- [General-family metric and ES-labelled tensor integration](research/incoming/es-rh-family-integration-c-20260920/README.md):
  the original scalar source and constructed tensor section have an exact
  combined minimum, complete determinant allocation, and certified range
  inverse. The two transported sum actions generate an explicitly projected
  common reducing space whose adjoint leakage retains the centre--length
  covariance. The equal-multiplicity ES-labelled model has exact dimension
  and leakage-rank formulas, and the two-centre collision calculation now has
  every singular and inverse-exterior exponent on both sides of \(a=1\).
  The canonical metric comparison consumes pinned NG20--NG21 on a stipulated
  off-line quartet and is not an RH result.
- [Original-divisor trace descent and exact nine-word boundary](research/incoming/es-turn07-divisor-descent-20260921/README.md):
  every positive same-word residual-divisor arrow is classified by the exact
  divisibility and word congruence on \(k\); the fixed-source inverse, complete
  global target fibres, group-ring coefficient and labelled kernel are all
  retained.  The unit-square image gives a uniform strict return exactly for
  \(u\mid36\), and the CRT/Dirichlet construction proves that this fixed-word
  list is maximal even after the middle complement.  Explicit E/M endpoints
  keep the method obstruction separate from the conjecture itself.
- [Sharp receiver growth, singular defect and finite heat](research/incoming/es-turn07-sharp-receiver-growth-20260921/README.md):
  every integral witness at \(p\equiv1\pmod {12}\) has one potentially
  unbounded inverse singular direction and three uniformly controlled
  directions. Exact compound bounds give the optimal powers
  \(p^{3/2},1,p^{-2}\) over this full domain; two
  \(p\equiv13\pmod {24}\) prime families prove sharpness, without proving
  optimality on the narrower \(p\equiv1\pmod {24}\) image. In the enlarged
  distinct-positive-root space, the receiver's exceptional divisor has rank
  exactly three with an explicit kernel and cokernel and is disjoint from the
  positive integral witness locus, while the
  fixed-\(c\) family supplies all four first corrections and the exhaustive
  scalar-observation hierarchy.
- [Modulo-24 mixed trace return and exact receiver composite](research/incoming/es-turn07-mod24-ray-trace-20260922/README.md):
  every rational integral-trace source with \(a=cq\), \(c\mid6\), \(q>3\)
  prime returns to an original integral middle state at the same
  \(p\equiv1\pmod {24}\). The exterior deletion map has exact domain
  \(k\mid R\), \(d\mid k\), \(k\equiv1\pmod{4rs}\), complete squarefree fibres, and a
  universal guarantee on exactly nine primitive rays. Its typed composite
  with the literal receiver retains the actual returned denominator order,
  shape parameters, and square-root choices; it records the exact source
  E-branch fibre and the information forgotten by the bare sorted map. The M
  branch historically had only a retained-\(t\) inverse; the next module closes
  that bare-fibre classification.
- [Complete mixed-return fibres and hard-middle spectra](research/incoming/es-turn07-fibres-middle-spectrum-20260922/README.md):
  every supplied sorted middle target has an exact disjoint E/M inverse fibre,
  with all square factors, carrier tests, tail orders and complementary words
  retained. The full receiver matrix reconstructs the target and selected
  frame without choosing among arithmetic preimages. A fixed-positive-\((R,u)\)
  family gives singular powers \(9,4,3/2,-3/2\), all first corrections and the
  observation hierarchy \(0,2,3,9\); two prime classes modulo \(9240\) prove the
  inherited inverse powers sharp on middle states in \(1\bmod840\).

The first two atlases decide the complete original source at any fixed prime;
the third removes specified occupied exterior branches by carrying them to
actual same-prime middle states. The fourth gives an exact structural receiver
and exact elementary transform for every occupied exterior state without
turning the receiver into an occupancy theorem. It also supplies the exact
fixed-input group action and boundary algebra without cancelling the inverse
pole. The fifth calculates the local
and integral difference between the channels and proves the complete
fixed-cofactor return fibre. Together with the earlier shape theorem this
removes every occupied exterior shape of radius at most eight, but it does not
prove the source nonempty or bound every remaining shape.
The capacity completion then determines the entire same-grade fixed-target
box, including its sharp finite boundary and exact infinite obstruction
families, without promoting those same-grade obstructions to global ES
counterexamples.
The multi-track continuation identifies the exact map that loses trace rank,
retains the perfect residue map on the same boundary algebra, and proves the
multiplier and defect needed to compare this finite algebra with the native
moment metric. It leaves integral frame nonvanishing, native moment evaluation
and the closing ES/RH statements open.
The integral and defining-prime modules then compute the complete arithmetic
lattice defect underneath that finite algebra and prove the exact morphism
between the two received E/M presentations.  The arithmetic-frame continuation
excludes the receiving divisor on an explicit infinite set of residue classes
and supplies one complete finite-field descent calculation.  None of these
post-witness classifications supplies the still-missing first positive
integral source at every hard prime.
The trace-integrality module supplies a global test for a proposed rational
source and proves its complete fibre structure. It does not manufacture the
proposed source: the remaining assertion is still that some raw word has an
integral trace at each prescribed hard prime.
The family integration identifies three maps that earlier interfaces left
implicit: the inclusion of the constructed section into the original physical
minimum, the projection from the ES-labelled common reducing space back to the
original cyclic image, and the collision map between separated and confluent
jets. Their kernels, ranges, metric costs and collision exponents are all
retained. None of these post-witness constructions supplies the still-missing
positive original source at every hard prime.
The original-divisor descent then determines every arrow from a supplied
rational trace source back into the integral original box.  It proves that the
nine automatic words are the largest fixed-word class for this arrow and gives
the exact infinite obstruction outside them.  The remaining universal question
has therefore moved upstream to trace-source occupancy or to a new source-changing
map outside the classified residual-divisor system.
The global receiver determinant continuation then proves that the original odd
receiver is nonsingular at every positive integral witness for
\(p\equiv1\pmod {12}\), without the earlier three-character filter.  It retains
the exact determinant phase and standard-Hermitian norm, supplies quantitative
determinant and inverse bounds, and isolates the unique receiver singularity in
an exact positive-real counterdomain outside the integral E/M cones.  This
closes that post-witness receiver question while leaving initial source
occupancy unchanged.  The [pinned complete proof](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6bdfce25724b95a4b30e97f0df69879a87793302/research/incoming/es-turn07-global-receiver-determinant-20260921/core.tex#L1-L488)
contains the full arithmetic reduction, coefficient certificates, inverse and
negative controls.
The sharp-growth continuation resolves the quantitative question left by that
sign theorem. It proves that only one inverse direction can become unbounded,
finds the optimal compound exponents, calculates the exact singular defect and
propagates the receiver through fixed metrics and conductors. This is still a
post-witness theorem.
The mod-$24$ trace continuation then supplies a source-changing map before the
receiver. It proves an integral return on the stated mixed prime-shell trace
domain and composes it with the sharp receiver without identifying their
different source spaces. Its infinite obstruction says exactly that the
universal ray-preserving rule stops outside the nine rays; it does not say that
other source-changing maps or ES itself fail there.
The complete-fibre continuation then inverts that source-changing map over an
arbitrary supplied middle target, identifies every collision and computes the
free-module and metric fibres. Its separate fixed-residual calculation proves
the hard-middle sharpness of all three inherited inverse exponents. This closes
the earlier M-fibre gap but leaves initial trace-source occupancy and sharpness
on the narrower mixed-return image open.

The [19 September bulletin](DAILY_RESULTS_20260919.md),
[20 September bridge bulletin](DAILY_RESULTS_20260920.md), and
[21 September arithmetic bulletin](DAILY_RESULTS_20260921.md), and
[22 September receiver/trace/fibre/spectrum bulletin](DAILY_RESULTS_20260922.md) give stable
result IDs and exact locators. They are mathematical indexes, not a programme
chronology.

## Failed steps that remain useful

The record preserves exact failures as part of the programme. In particular:

- [The $p=37,a=12$ selector example](research/expanded-2026-09-08/exact_bounded_transport_72/bounded_transport.tex#L176)
  tests a per-shell cutoff, while retaining the different successful shell of
  the same prime. It does not claim a counterexample to a global selector rule.
- [The two local-to-global examples](research/expanded-2026-09-08/exact_bounded_transport_72/bounded_transport.tex#L379)
  expose an integral congruence obstruction and a different failure of the
  original finite exponent budget. Both enter the bounded fibre calculation.
- [The positive-shear path theorem](research/expanded-2026-09-08/exact_bounded_transport_72/bounded_transport.tex#L893)
  gives the exact obstruction to composing two passing adjacent shears. The
  separate fixed-denominator successor has its own domain and is retained.
- [The finite sampling example](research/expanded-2026-09-08/exact_bounded_transport_72/ns_operator_bridge/torus_cover_lemma.tex#L473)
  records the extra character terms produced by an unchanged grid; the complete
  preimage and character-coset constructions give the corresponding exact repair.

## Attribution, checks and continuation

The arithmetic, positivity-code and prime-production contributions of
**u/UmbrellaCorp_HR** are cited in the reading edition and its bibliography.
The earlier mod-107 observation remains credited to **u/CommonCareful3149**.
[The literature guide](LITERATURE.md) identifies the human mathematical sources,
specific passages and source-attribution records. The collective byline is
**The Clankers**.

[Statement records](polyclank/claims.json) contain exact TeX and byte/line locators
for the 72 named statements in the 15 canonical proof modules, with their proof
locations or explicit theorem references. [Artifact records](polyclank/artifacts.json)
cover all 85 files in the source archive. Neither index substitutes for reading
the surrounding definitions and argument.

The [check records](polyclank/checks.json) distinguish source-identity checking,
the published fourteen-command mathematical replay and the later replay of a
fresh public archive. The supplement supplies written proofs and exact checks;
it does not claim a whole-supplement Lean verification. Earlier Lean results
retain their own statements, source packages and receipts.

The latest organizational checkpoint is 9 September 2026. Scheduled mirroring
and publication are paused at the maintainer's request. The published work remains
open to reading, checking, forking and extension. [Contribution guidance](CONTRIBUTING.md)
and [PolyClank's workbench model](POLYCLANK.md) describe how to carry a result,
attempt or whole programme forward, here or in an independent repository.
