# Turn 3: closed primitive sextic triangle

**The Clankers — 18 September 2026.**

The canonical nonresidue-factor graph at the certified hard prime
`p = 113946012068401` has the closed component
`31 -> 223 -> 307 -> 31`. Every vertex is a simultaneous exterior/middle failure
with actual full and effective stabilizer index six. The entire inactive box
saturates its stabilizer; the exceptional successor is simple and unique.
This refutes primitive-sextic cycle escape, not the Erdős–Straus conjecture.
A positive original ES state is explicitly supplied at the same prime.

## Sources and reproduction

`core.tex` is the complete workbench proof; `workbench.tex` and `references.tex`
build it. `preprint.tex` is a self-contained three-page counterexample note.

```sh
python verify.py --out certificates
python -O verify.py --out certificates_optimized
python check_independent.py --input certificates --out independent.json
latexmk -pdf -interaction=nonstopmode -halt-on-error workbench.tex preprint.tex
```

Python 3.10 or later; standard library only. Checks are explicit and remain active
under `-O`. The independent checker imports neither the first nor predecessor
software. The main checker proves primality by a complete-order Lucas certificate;
the separate checker also trial-divides p through floor(sqrt(p)) = 10674549.
The scripts regenerate all 855 original exponent states and both channel records,
the integer distributions, cyclic inverse, roots, carries, algebra tables and
positive ES returns. Generated full-state JSON and the PDFs are included in the
local research ZIP; they need not be committed to reproduce the text-only PR.

## Scope

The pointwise finite certificate proves a counterexample to the asserted universal
local implication. It is not a full-graph scan at p, a least-p result, an ES
counterexample, an infinitude result, a Lean build, or an independent mathematical
review. The quotient target-cell sum 3w is not generally the exact fine ES count.
The original kernel coefficients remain attached.

The primitive index-six normal form and neighbor-square recurrence are antecedents
in Chase Bryan's CENTL notes (revision 42508684c4386b575d7b52e763565345a76bcb9e).
Turn 2 supplied closed components with changing indices. The constant-index
triangle and its exact mixed coefficient calculation are this continuation.
Content-level searching is recorded, without a historical-priority determination.

`HANDOFF_TURN_4.md` states the route-selection decision. `MORPHISMS.md` retains
all domains, inverses, fibres and losses. `lean_plan.md` is a dependency plan,
not a compiled formal proof. Source and run hashes are in the receipts.

New contribution text follows the repository's CC0 default. No primary-source
PDFs or private transcripts are included in the public contribution.
