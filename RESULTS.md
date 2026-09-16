# Results bench: mathematics that can be used without solving Erdős–Straus

This is a provisional, non-exhaustive shelf of separately usable mathematical outputs, prepared on 10 September 2026 from the owner's new Chatnotes archive and the pinned public workbench. It is not a list of claimed solutions to famous problems, and manuscript headings are not verification.

Read [the selected proof notes](results/PROOF_NOTES.md), [the result records](results/records.json), [the source map](results/SOURCES.md), and [the exact checker](results/check_selected.py). [Research directions worth continuing](RESEARCH_DIRECTIONS.md) preserves unfinished programmes separately.

## What is on this shelf

**R01 — Two different zero layers in a precise semiring.** A construction separates absence from a supported zero. Its additive identity and the older ring zero are distinct. The note proves the operations and identifies two prime ideals under explicit hypotheses. This develops the owner's split-zero question; it is not a novelty claim.

**R02 — A six-sector weighted target loses no Fourier mode.** The vector e₃ + 2e₍₃₋ₖ₎ in the complex group algebra of C₆ has every Fourier component nonzero. Its trivial component is 3, not discarded. This does not force an arithmetic support to meet that target.

**R03 — A fifteen-to-sixteen coordinate-algebra construction.** The fifteen-element prime set used in the Ogg draft has a residue partition 1 + 7 + 7. Adding a distinct level-one coordinate gives 1 + 1 + 7 + 7 and retains its own idempotent. The proved object is a finite coordinate algebra, not a Lie algebra or Monster representation.

**R04 — The actual Busy-Beaver/107 arithmetic identities.** The fixed integers 6, 21, 107, and 47,176,870 satisfy the stated relations to 8,803,369 modulo 107. These are exact computations. Their broader relationship to machine complexity remains a separate research question.

**R05 — CivQ17's affine recurrence and an odd-step Collatz consequence.** The recovered draft explicitly studies T(x)=4x+1 and θ(x)=3x+1 with θT=4θ. The note also derives that positive odd n and 4n+1 have the same next odd Collatz value. This is not a convergence proof or a novelty claim.

**R06 — The ten-point mod-107 deficit.** The specified 43-point support in Z/53Z has a ten-point progression complement D, with |D−D|=19 and 6 outside D−D. Two translated supports cover Z/53Z. The initiating observation remains credited to u/CommonCareful3149; this is one finite calculation.

**R07 — A sharp irrational-direction estimate.** For two specified directions involving √2, inf |v·k|‖k‖ over nonzero integer vectors equals 1/√(4+2√2). A conjugate-norm argument gives the bound and Pell vectors approach it. No fluid existence theorem is needed.

**R08 — A concrete three-colour lattice test.** A new calculation in this pass makes one interpretation of the owner's proposal precise: three cyclically permuted copies of a lattice, with fixed diagonal, zero-sum part, integral index and Eisenstein action. A Leech input gives a rank-72 direct sum, not a new extremal lattice or an ES equivalence.

**R09 — The finite Star–Kneser obstruction.** Kneser's addition theorem bounds a target miss in the quotient by the actual stabilizer. Its contrapositive gives a finite forcing criterion. Establishing that criterion for the required ES shells is not supplied by the criterion itself.

**R10 — Explicit order-72 glue data.** The recovered Niemeier draft contains a binary duad code and ternary tetracode. The note and exact checker reconstruct the 72-element subgroup, verify isotropy, and enumerate nonzero coset costs 4 and 6. Later moonshine maps are not certified by this finite calculation.

## What the evidence means

The ten notes supply arguments at their stated scope, with the imported Kneser theorem identified. One assistant reconstructed them. Nine families of exact finite checks ran with newly written standard-library code; normal Python and Python -O produced byte-identical outputs. **No formal prover was run, no independent reviewer was obtained, and no comprehensive novelty search was performed.** Finite examples do not replace general arguments.

Do not describe this as ten newly discovered theorems. Some statements are standard or elementary; novelty is unassessed. Newly indexed, new to this investigation, and new to mathematics are different claims.

A proof of A ⇒ B is not a proof of B until A is established for the actual application. Ordinary domain hypotheses remain part of the statement; an unresolved target-strength assumption must not be hidden in a definition or promoted away. Several draft copies and repeated model agreement do not constitute independent verification.

The workbench's [existing index of 72 statements across 15 modules](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/9a3ddfe8b38a424f1ff0426201a1f4f6f9d2772f/polyclank/claims.json) records source/proof locations, not 72 independent reviews. This selected shelf complements that larger source catalogue.

## Reuse and attribution

Preserve the source and contribution history. Initiating an idea, supplying a construction, finding an error, and proving a later consequence are separate contributions; no ranking is assigned. The owner authorizes associating KokunoYumeto with u/lepthymo. Other contributors retain their requested public handles; private aliases are omitted. See [provenance PR #1](https://github.com/KokunoYumeto/erdos-straus-foundation/pull/1).

This addition does not relicense existing sources or the private archive. It proposes CC0 for these new authored notes/metadata to the extent applicable rights are held, and MIT for the new standalone checker. Original source rights and intellectual attribution remain separate. A reusable result package should include its statement, definitions, proof, source dependencies, checking record and unresolved limitations—not merely a title or a green badge.
