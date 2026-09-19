# Full Turn 3 proof and replay lane

This directory is the source-first, nonduplicate portion of the complete Turn
3 tranche preserved in
`erdos_straus_cumulative_through_turn4_20260918.zip` (SHA-256
`5673df81885f134ac0d6f5d8dedf34d8651249402064d7a67213c7f7027d460f`).
The embedded Turn 3 archive has SHA-256
`0ce39f657953ca1db9dc6b64727060a2b0c5c2612bb429b394181d0255813364`.
Generated page images, PDFs, duplicate publication files, and the historical
pre-merge publication receipt remain in that cumulative archive rather than
being duplicated here.

`core.tex`, `workbench.tex`, and `references.tex` give the complete seven-page
argument. `MORPHISMS.md` records the typed maps and their retained or lost
data. `HANDOFF_TURN_4.md` states the exact surviving obligation. The two Python
implementations and deterministic certificates retain the cubic, carry,
triangle, escape, and bounded-census data.

Run from this directory:

```sh
python verify.py --bound 250000 --out reproduced
python -O verify.py --bound 250000 --out reproduced_optimized
python check_independent.py --input reproduced --out reproduced/independent.json
pdflatex -halt-on-error workbench.tex
pdflatex -halt-on-error workbench.tex
```

The fresh integration audit reproduced 165,588 main checks in each Python
mode, 1,863 checks in each independent run, 80 primality-certificate nodes,
1,215 original triangle vectors, and the census of 636 hard primes, 1,802,376
vertices, 961,554 edges, and 19 triangles. This census corroborates the code;
it is not the proof of the universal square-nine theorem and is not an
Erdős--Straus verification range.

No Erdős--Straus resolution, least-prime claim, universal selector occupancy,
Lean build, independent human review, or historical-priority determination is
asserted.
