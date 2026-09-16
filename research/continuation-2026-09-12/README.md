# Exact selectors, character energy, and integral return

This continuation connects the complete Erdős–Straus divisor test to three
structures: quadratic-character collision energy, a finite affine torsion
system, and the quartic norm in JT's cyclotomic investigation. The purpose is
to obtain structural ways to force an integral solution, while retaining the
actual prime, divisor exponents, coordinate scales, and inverse maps.

The all-prime existence question is not resolved here. The results include
general proofs, not only numerical examples. The examples test the sharpness
of the constructions and disprove several stronger proposed steps.

## Read the mathematics

- [Complete continuation reader](output/pdf/continuation.pdf) and
  [its source](reconstructed/continuation.tex).
- [Rational atlas, exact denominator defects, character energy and anchors](received/es_dual_frontier/workbench.tex).
- [Integral monodromy, cocycles, torsion covers and arithmetic return](received/es_s6_counterfactual/workbench.tex).
  Read the [compactification correction](CORRECTIONS.md) with this original.
- [Earlier typed arithmetic and geometric composition sources](received/typed_morphism_audit).
- [Source identities](received/ARTIFACT_PROVENANCE.json),
  [attribution and source coverage](PROVENANCE.md), and
  [machine-readable mathematical records](continuation.json).

The received files remain unchanged. The new reader gives complete proofs for
the Boolean/cyclotomic continuation, the character-resolved energy criterion,
the common-modulus affine and hexagonal maps, and the corrected local covering
maps. It does not silently rewrite the older papers as if they had contained
these later arguments.

## What the approaches achieve

**Exact selectors.** Every integral solution at a prime congruent to one modulo
four has its minimum denominator strictly between one quarter and one half of
that prime. The proof gives the exact connection between the older larger
shell range and JT's first-half selector. Divisor, primitive-tuple and integer
code coordinates are explicitly invertible. This proves completeness of the
selector, not its universal nonemptiness.

**Character energy.** Keeping the inversion parity of the centered divisor
box gives an exact discrete minimum for the collision energy of a distribution
that avoids all solution targets. Resolving that minimum by quadratic
characters strengthens the forcing test. At `p=1201, a=310, R=39`, the negative
Jacobi cell has mass 18 and energy 30, while target avoidance would require
energy at least 32. This forces a solution in that shell; one exact witness is
`(310, 1489240, 9608)`. The unpartitioned test does not certify this shell.

**Integral return.** The arithmetic denominator defect is exactly the order
of a specified affine cocycle. Multiplication by the original gate embeds the
compressed system back into the original modulus. The CRT inverse retains one
common divisor label; separately chosen local divisors cannot be substituted
for that label.

**Hexagonal and cyclotomic geometry.** An integral change of three coordinates
makes the order-three action cyclic. Its two-coordinate readout is the
hexagonal quadratic form, with an explicitly retained third coordinate and
index-three gluing. JT's quartic is the same form evaluated on positive
squares, and also an iterated field norm. The complete positive-square return
criterion under the dihedral action is proved. The second monodromy's exact
nonzero change of the quadratic form is retained.

**Marked cubic-surface contraction.** The six-curve cycle is related by an
actual blowdown to the cubic surface's 27 line classes. The reader gives the
Picard pushforward, pullback, kernel, all 27 images, and the six-cycle's
Cremona-permutation action. On the matching torus it is `(u,v) -> (u/v,u)`;
the exceptional projective directions also have an explicit invertible map.
The marked six-point configuration changes under this operation unless its
centres are preserved. That change is retained in the geometric statement.

**Corrections that matter.** Compactified level maps use the ratio of actual
branch-cycle lengths, not always the ratio of moduli. The completed CRT product
requires the explicitly parametrized normal model of the fibre product.
The Boolean investigation also supplies actual counterexamples to universal
endpoint selection, nontrivial short descent, automatic nonresidue cofactors,
and the gluing of different bounded divisor choices. These are failures of
specified constructions, not counterexamples to Erdős–Straus.

## Reproduce and extend

Run the commands in [VERIFY.md](VERIFY.md) from this directory. Received
certificates, freshly replayed certificates, independent regressions, and
written proofs have distinct records. No new Lean certification is claimed.
Earlier formal artifacts remain in the repository's preserved archives.

The next structural target is an operation that preserves the exact bounded
divisor conditions while forcing one of the solution residues. The present
hexagonal unit action preserves the quartic norm, and a nonempty quadratic
character cell does not by itself occupy a particular residue. The equations
and counterexamples here specify exactly what a further construction must do;
neither observation implies that the arithmetic and geometry are unrelated.

JT is credited for the Boolean, positivity, cyclotomic and prime-character
research directions identified in the supplied dialogue. The project
maintainer's directions connect these to the geometric and exact-morphism
programme. Individual assistant-derived arguments are not retrospectively
attributed to a human who merely requested them. Original mathematical
antecedents and source-specific credit remain attached to the papers.
