# Turn 7 continuation: exact capacity completion and original channel returns

The universal ES existence milestone remains unresolved. This is not a Turn 8
witness-guaranteed algorithm. It completes a narrower unbounded arithmetic
problem that arose in the preceding negative-square channel transfer.

## Main results

For h=4j-1>t, every divisor W of j^2 in class t is uniquely canonical, an
unbounded companion, or one of the explicit finite templates in Theorem 3.1.
The finite templates satisfy the sharp h <= t^2-3t+1 bound. Canonical failure
can only be repaired in that finite range; beyond it all same-grade returns
are decided exactly by t|j^2. The companion is not incorrectly subjected to
the finite bound.

These words return original E-to-M states at negative-four-integer shape
coordinates. The original equations force the divisor budget on alpha
coefficients 1,2,3 and all beta coefficients dividing 36, without requiring
those coefficients to be squares. A reduced prime progression realizes the
sharp finite-repair bound in original hard-prime E states for unbounded t.
Conversely every fixed alpha coefficient t>=4 has infinitely many original
hard-prime states whose complete old-grade middle box is empty. They have the
constructed E solution, so this is not an ES counterexample.

The proof also corrects the predecessor's textual alpha inverse domain by
restoring the original E gate. The predecessor executable already checked it.

## Files

- `output/workbench.pdf`, `workbench.tex`, `core.tex`: complete proof.
- `output/preprint.pdf`, `preprint.tex`: shorter self-contained research note.
- `verify.py`: standard-library complete fixed-target and original-state replay.
- `check_independent.py`: separate implementation; no import of the first.
- `build_live_receipts.py`: deterministic manifest and repaired build receipt.
- `certificates/*.json`: actual original coordinates and finite results.
- `MORPHISMS.md`, `CORRECTION.md`, `HANDOFF_TURN_7_REMAINDER.md`.
- `claims.json`: stable records SZ-20260920-040 through SZ-20260920-044.
- `INTEGRATION_AUDIT_20260920.md`: source identity, corrections, mathematical
  review, replay scope and attribution.
- `figures/`: exact capacity partition and sharp-bound diagrams in PDF and PNG.
- `received/`: unchanged outer ZIP and pasted continuation. The supplied
  `MANIFEST.json` and `verification.json` remain historical records of the
  received package; the live manifest and verification receipt describe the
  repaired tree.

## Reproduction

```sh
python verify.py --bound 3000 --target-bound 120 --j-bound 5000 --out certificates
python -O verify.py --bound 3000 --target-bound 120 --j-bound 5000 --out certificates_optimized
python check_independent.py --input certificates --out certificates/independent.json
pdflatex -interaction=nonstopmode -halt-on-error workbench.tex
pdflatex -interaction=nonstopmode -halt-on-error workbench.tex
pdflatex -interaction=nonstopmode -halt-on-error preprint.tex
pdflatex -interaction=nonstopmode -halt-on-error preprint.tex
```

Original source boxes are not replaced by subgroups. The complete state tables
keep channel, a,u,R,h,r,s,k, the ordered denominators, and each occupied a's
factorization. Its exponent box is [-e_l,e_l] and its vector is v_l(u)-e_l.
Larger fixed examples include those boxes explicitly. Geometric fibres, residue
support and original integer multiplicity are not interchangeable.

The incoming patch is additive. This archive contains no assertion of a Lean
build, independent mathematical review, historical priority, or a new overall
ES verification range. The bounded runs test the proofs; they do not establish
an all-prime occupancy statement.
