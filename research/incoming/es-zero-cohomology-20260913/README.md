# Supported ES cohomology and original arithmetic weights

Additive integration of the owner's Zeta SplitZero programme with the
Erdős–Straus exact bounded-divisor/split-box programme. This is not a new
scalar theory and not an asserted analytic equivalence between a finite
counting norm and the zeta-derived theta norm.

## Mathematical contents

- `core.tex` / `workbench.tex`: full source-level crosswalk, all maps,
  inverses, boundary primitives, empty fibres, coarsening kernels, norms,
  original channel return, and counterfactual interpretation (seven pages).
- `preprint.tex`: standalone three-page proof of the principal finite
  constructions and arithmetic weight correction.
- `card.tex`: reproducible one-page posting summary; not a proof substitute.
- `verify.py`: standard-library verifier, independent of predecessor code.
- `morphisms.json`: domain/codomain, actual inverse/fibres and loss register.
- `source_reading.json`: exact pinned sources and inspected sections.
- `lean_plan.md`: formalization dependencies, not a compiled Lean proof.

There are two different quotients. The three-term cochain removes internal
fibre-sum relations and has H0 indexed by common channel/residue classes.
The matched-pair addition quotient instead has H0 indexed by original
canonical divisor states. Their ranks need not coincide. At p=2521,
a=636 the matching-pair count is 5, the first H0 rank is 4, and the
original canonical channel-state count is 3. Every projection has its
complete retained fibre; no bijection between these different quotients
is asserted.

The scalar tau denotes absence, while a supported zero retains its label.
This is the owner's original SplitZero convention. Arithmetic source
weights remain attached to quotient norms and to relation primitives.
In particular the genuine empty shell p=241,a=64 has H0=0 but counting
source mass 28 and a 12-dimensional raw cancellation kernel. It is not an
absent source and it is not an ES counterexample.

The count-preserving weight of a split occurrence is exactly 1/N(beta),
where N(beta) is the full bounded addition-fibre size. Every original
channel/exponent/denominator-defect monomial is recovered, not only the
Boolean existence bit. The canonical quotient metric is not silently
reset between stages. A three-stage example detects the exact erroneous
excess 1/189 when it is reset.

## Source provenance

Pinned Zeta revision: `7ea0a49945390eae14d3160a5730858899768b5f`.
Read the actual `DERIVED_MATHEMATICS.md`, `TAU_BASE_MODEL.md` and
`tau-toda-volume-formal/RESEARCH_NOTE.md` at the sections specified in the
reading ledger, not just their readmes. The prior ES split note is draft
PR 5, revision `4f17e4aa63113a063eb027c8931cee5d5cce3981`. The present
proof includes its elementary arithmetic interface, so no external code
import is required. First-half completeness remains attributed to the
current ES source and is not counted as a new result.

The owner supplied the SplitZero/arithmetic-weight integration direction;
JT's bounded-exponent/common-local-vector direction remains attributed to
the ES source. These derivations and finite code are AI-assisted under
The Clankers collective byline. General homology, least-norm projection,
finite conditional weighting and Schur complement facts are standard or
already in the cited workbench. No historical-priority claim is made.

## Reproduction

```sh
python verify.py --bound 500 --out reproduced
python -O verify.py --bound 500 --out reproduced_optimized
# Compare the four mathematical JSON outputs byte-for-byte.
pdflatex -halt-on-error -interaction=nonstopmode workbench.tex
pdflatex -halt-on-error -interaction=nonstopmode workbench.tex
pdflatex -halt-on-error -interaction=nonstopmode preprint.tex
pdflatex -halt-on-error -interaction=nonstopmode preprint.tex
pdflatex -halt-on-error -interaction=nonstopmode card.tex
```

The accepted run covers all 1,284 first-half shells of the 21 primes
p=1 mod12, p<=500, with the unsplit box and every one-occurrence peel:
3,775 splits. It records 1,827 matching occurrences and total residue-H0
rank 1,001 over that entire scan; these are not prime counts and are not
new coverage. There are 111 channel observations whose naive matching
count exceeds the original count. The unchanged exact original count is
checked across every tested split. The final code executes 703,150
explicit conditions. Counts describe this implementation, not independent
reviewers or general proofs.

All 169 pairs of maps from sets of size at most two into a three-element
set are checked with actual matrices in counting and nonconstant metrics.
Additional actual Gram/rank/determinant fixtures have common-fibre sizes
1..6 and include the four marked arithmetic examples. The larger scan
uses the proved fibre-rank formulas; it does not falsely claim dense
Gaussian elimination at every scanned shell. Both successful and failed
candidates retain their complete denominator defects. Exact rational
numbers are serialized by numerator and denominator.

## Nonclaims and next target

No universal ES theorem, new prime coverage, global theta or S6 comparison,
Deligne weight estimate, analytic norm identification, Lean build, or
independent review is asserted. The next arithmetic target is to prove a
positive canonical H0 residual in at least one shell for every required
prime, or an inequality forcing a nonzero original state coefficient.
The weight formulas do not assume that positivity.

## Integration boundary

All deliverable additions are under
`research/incoming/es-zero-cohomology-20260913/`. No existing code,
accepted claim, manuscript, license, workflow, or other branch is rewritten.
The Zeta source is linked at its immutable revision, not copied or
relicensed. The exact recovered eleven-file source patch is preserved in the
first branch commit. A second publication commit adds the five cited
certificate files, readable PDFs and page images, source-specific licensing,
the current draft-PR description and a fresh replay receipt. The branch is
published as `research/zero-cohomology-moment-gap-20260913`; `main` and the
downstream PR6 branch remain unchanged.
