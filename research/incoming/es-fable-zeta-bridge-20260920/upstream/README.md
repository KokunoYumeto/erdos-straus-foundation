# The complete signed ES–Fable state in the original conductor

The cumulative proof is **FABLE_TO_ORIGINAL_CONDUCTOR.tex**. It contains the entire previously published FC1–71/GF1–28 finding and the complete new SE1–18/SM1–19 derivations. The nineteen-file source edition preserves the earlier published edition at commit `369f6ea9e0312bdf348ca9efd294735efc99c51d`; it does not replace that historical source.

## What is new

For the literal original quartet, the four half-differences of the eight signed inverse states form a basis with exact determinant

`1792 χ δ² γ² (2δ²γ² − δ² + γ²)`, with the retained sign `χ=±1`.

The four half-sums have rank exactly three. Their remaining kernel line, every coordinate of that line, and the entire four-dimensional graph kernel of the eight-state evaluation are calculated explicitly. Both maps pass through the unchanged original weighted conductor with their full Gamma Grams (SE1–12).

Keeping the root-label vector together with the evaluation gives an explicit invertible eight-dimensional map to two copies of the original conductor space. Its inverse, all signed-root actions, the complete mixing block and its exact ranks are proved. Every pair-sign change has a rank-two mixing block; simultaneous reversal has rank three. The original inverse-exterior bound returns through the exact direct-sum identity (SE13–18).

The actual eight-sheet cover has monodromy precisely the determinant-one signed permutation group of order192. The proof constructs its loops, all signs, and paths from the literal original quartet. Its cover and rational deck group is `{identity, Σ}`; only identity is a global polynomial deck automorphism satisfying `P∘D=P`. This last assertion is not a claim about all automorphisms commuting with P: that separate centralizer includes the earlier J (SM1–19).

## Proofs and reproducibility

The main cumulative TeX is self-contained for this finding and includes all original polynomial coordinates, receiving maps, measures, complete proofs and citations. The `independent/` directory contains full independent proofs of the global inverse, singular spectrum, monodromy and signed evaluation.

With Python and SymPy, run the following from this directory:

```
python verify_transport.py
python independent/verify_seven_fibre.py
python independent/verify_global_fibre.py
python independent/verify_escape_spectrum.py
python independent/verify_signed_root_monodromy.py
python independent/verify_signed_evaluation.py
python derive_escape_differential.py
python derive_signed_evaluation.py
python verify_signed_root_group.py
```

The scripts use exact polynomial, rational-function and finite-permutation arithmetic. `VERIFICATION_REPORT.json` records the corresponding accepted results. The mathematical proofs establish the analytic continuation and original-metric statements; discrete computations are not presented as substitutes for those proofs.

## Provenance and scope

The original four-dimensional polynomial and four marked representatives are from The Clankers' canonical version69 Erdős–Straus reader, theorem `explicit-four-time-Jacobian-collision`, source hash `678b3f70ee7d2a6d00f6c588d7778e390118ab4743a5759612dbba6430984c78`. The complete inverse, eight-state evaluation and monodromy are the new calculations here. The source preserves the distinction from the original three-dimensional example announced by Levent Alpöge with Fable and presented by Terence Tao. Original Gamma polynomial formulas retain the contributions of T. H. Koornwinder, R. Wong, R. Koekoek, R. F. Swarttouw and W. P. Reinhardt through the exact cited NIST DLMF dictionary. Full citations occur in the TeX.

These are exact nonlinear-state and original-conductor correspondences. The fixed original linear conductor remains invertible; an RH conclusion and a moving-period boundary limit are not asserted. The inherited observation-quotient calculation being pursued separately is not assumed in any theorem here.

The earlier source-local SZ result numbers require explicit programme aliases because another task used the same numbers. The publisher is recording that alias correction without changing either proof lineage; equations and source hashes remain the unambiguous proof locators.
