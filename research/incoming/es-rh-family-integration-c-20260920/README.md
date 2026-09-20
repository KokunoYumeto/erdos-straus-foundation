# General-family source geometry, ES-labelled jets, and collision exponents

This continuation develops four connected calculations for the existing Erdős–Straus and zeta workbench.

1. It compares the constructed tensor-section metric with the canonical arithmetic metric on the same cyclic algebra. The asymptotic separation and heat-scale formulas use the proved NG20–NG21 native compression theorem at the exact source version recorded in `SOURCE_LEDGER.md`.
2. It solves the mixed-source minimization problem at finite dimension. The joint metric is
   \[
   G_J=G^{1/2}(I+T)^{-1}G^{1/2},
   \]
   and its determinant decrease splits exactly between the observed quotient and the old kernel through the full Schur complement, including the mixed block \(T_{12}\).
3. It constructs the common reducing space for the transported zeta and ES-labelled actions, computes the centre–length covariance in the adjoint leakage Gram, and gives exact dimension, rank, and kernel formulas for the equal-multiplicity occupation fibres.
4. It evaluates every singular exponent of the two-centre divided-jet collision for \(\eta=|z|^a\). The two formulas meet at \(a=1\), where the exponents are \(0,1,\ldots,e+f-1\); CP9–CP11 give every inverse-exterior exponent and finite balanced-scale constants.

The complete proofs are in `proofs/`, the cumulative reader is `RESEARCH_CONTINUATION.md`, and the typeset version is `MANUSCRIPT.pdf`. The two figures are generated from exact formulas by the scripts in `figures/`.

## Scope

The finite source, reducing-space, covariance, and collision results are proved at their stated inputs. The canonical-metric asymptotics retain their explicit dependency on NG20–NG21 and on the stipulated off-line quartet used by that programme. This continuation does not assert that such a zeta zero exists, does not draw a conclusion about the Riemann hypothesis, does not construct an ES witness at an unoccupied prime, and does not identify the occupation-leakage kernel with the separate trace-rigidity kernel.

The received ZIP and pasted result are preserved unchanged in `received/`. `INTEGRATION_AUDIT_20260920.md` records the independent replay and two repairs made during intake: JS12 now distinguishes the actual least positive eigenvalue from an arbitrary certified lower bound, and ER7 is restricted to the generated top-chain sector, with an explicit ambient counterexample. `MANIFEST.json` records every preserved, derived, and generated file with its byte size and SHA-256 digest.

## Verification

Run:

```powershell
python checks/run_validation.py
```

The four SymPy suites execute in ordinary and optimized Python and compare their receipts byte-for-byte. They certify exact finite identities and bounded combinatorial cases; they are not Lean proofs, native zeta-moment evaluations, or finite substitutes for the written all-length and asymptotic arguments. See `results/VERIFICATION_SUMMARY.json` for the current counts, versions, and hashes.

Rebuild the cumulative Markdown, TeX, and PDF with:

```powershell
python build_manuscript.py
```

Pandoc and pdfLaTeX are required. The build does not modify the preserved received files.
