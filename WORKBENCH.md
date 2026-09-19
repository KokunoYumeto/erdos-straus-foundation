# Erdős–Straus: the research map

The question is whether every integer $n\geq2$ admits positive integers
$x,y,z$ with $4/n=1/x+1/y+1/z$. Repeated denominators are allowed.
This workbench pursues both explicit arithmetic constructions and exact
correspondences with other mathematical structures. It has not resolved the
conjecture. The purpose of this page is to help a reader enter the full arguments,
understand why they were tried, and continue them.

Read the [86-page expanded supplement](https://zenodo.org/records/22678971/files/07_Exact_Bounded_Transport_Expanded_72_Statements_2026-09-08.pdf)
or browse its [complete TeX, proofs and checks](research/expanded-2026-09-08/exact_bounded_transport_72).
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

## Current finite source atlases

The 19 September continuation now has complete, separately typed finite atlases
for both original first-half channels:

- [Middle two-chart atlas](research/incoming/es-turn07-middle-cutoff-20260919/README.md):
  sharp square-root bounds for the least exact middle cofactor, with direct and
  cofactor inverses.
- [Exterior three-chart atlas](research/incoming/es-turn07b-exterior-atlas-20260919/README.md):
  strict cubic cutoff for the least of \((R,D,v)\), with direct, reciprocal and
  complement–norm inverses retaining the exact \(K(v)\) availability condition.

Together they decide the complete original source at any fixed prime; they do
not prove its output nonempty. The [dated proof bulletin](DAILY_RESULTS_20260919.md)
gives stable result IDs and exact locators. It is a mathematical index, not a
programme chronology.

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
