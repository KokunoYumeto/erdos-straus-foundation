# Four tetrahedral markings over three Fable branches

This continuation constructs the fourfold marking requested in the conversation. It contains two related but distinct operations:

1. Twelve norm/metric pencil states over the fixed binary cubic: four tetrahedral numerator directions, each with three distinguished roots. Normalized factors forget the extra fourfold frame and give the original three Fable preimages. The four numerator directions also determine four coherent marked unit/product structures.
2. Four Cayley normalizations of one marked projective point, giving four cubics and twelve root-marked sheets, with exact rational transitions, inverse scales, and companion orientation.

Read `note.pdf` or the full proof source `note.tex`. The standard-library verifier is independent of previous verifiers and does not access the network.

```sh
python verify.py --out regenerated
python -O verify.py --out regenerated_optimized
```

Both receipts and all generated certificate files must agree byte for byte. Python 3.9 or later is required. No third-party packages are used.

## Certificates

`certificates/orthogonal_algebra.json`: the exact quotient algebra, primitive idempotents, roots, and trace pairing.

`certificates/tetrahedral_pencils.json`: all twelve oriented numerator/denominator pencils, normalized factor pairs, and three-to-one-face/four-to-one-Fable fibre data. The full 24-state orientation-unrestricted count is verified by the script.

`certificates/cayley_atlas.json`: all four face charts and twelve root-marked states for each of the three included ES examples. All inverse scales, derivatives, companion differences, and Fable coordinates are rational strings. The original p, R, divisor u, h, r, s, E/M tag, quotient, and raw denominator order are preserved.

`certificates/receipt.json`: exact check scopes and certificate SHA-256 hashes. `execution_receipt.json` records the actual normal and optimized execution in this session.

This package is not a prime-range search, a fourth preimage of the original Fable map, a proof of ES or RH, or a mathematical-priority claim. Equal numerical coefficients do not remove face labels. Norm-preserving sign maps become unital algebra maps only when the marked product is transported as specified in the note.

The PDF was built twice with pdfLaTeX and rendered for inspection. No Lean build is claimed; `lean_ready_plan.md` is an exact dependency plan.
