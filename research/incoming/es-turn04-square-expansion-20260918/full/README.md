# Full Turn 4 proof and replay lane

This directory is the source-first, nonduplicate portion of the complete Turn
4 tranche preserved in
`erdos_straus_cumulative_through_turn4_20260918.zip` (SHA-256
`5673df81885f134ac0d6f5d8dedf34d8651249402064d7a67213c7f7027d460f`).
The embedded Turn 4 bundle has SHA-256
`f2eeb00fc0ddcf7d0aba7cf348f77b9a68f4c4bc594f905cd17e78516f0be9ff`.
Generated PDFs and page images, duplicate portable-publication files,
environment receipts, and the exploratory one-million scan remain in the
cumulative archive rather than being duplicated here.

`core.tex`, `workbench.tex`, and `references.tex` give the complete seven-page
argument. `MORPHISMS.md` and `morphisms.json` register 21 typed maps with
inverses, fibres, and information loss. `ATTEMPTS.md` records the successful
and failed routes, and `HANDOFF_TURN_5.md` states the exact remaining selector
obligation. The complete deterministic cofactor, root, example, and bounded
scan certificates are retained under `certificates/`.

Run from this directory:

```sh
python verify.py --bound 5000 --out reproduced
python -O verify.py --bound 5000 --out reproduced_optimized
python check_independent.py --input reproduced --out reproduced/independent.json
pdflatex -halt-on-error workbench.tex
pdflatex -halt-on-error workbench.tex
```

The fresh integration replay completed 169,313 main checks and 7,042 checks
in the separate implementation. It reproduced 5,922,259 range-compatible
cofactor profiles, the three surviving cycles, and the bounded scan of 13 hard
primes, 2,698 vertices, 4,460 sources, and 125,666 original divisor vectors.
The finite closed-set theorem follows from the proved reduction plus the exact
enumeration; the bounded scan is corroboration only.

Factor expansion is not selector occupancy. No Erdős--Straus resolution,
universal all-square graph occupancy, Lean build, independent human review,
or historical-priority determination is asserted.
