# ES–Fable–RH multi-track continuation — 20 September 2026

This package contains five complete mathematical notes, exact-check code, reproducible receipts, and source provenance for a combined continuation of the Erdős–Straus foundation and Split-Zero/RH programme. It is not a proof of either conjecture, a global novelty claim, a whole-corpus audit, or a Lean verification.

The two source snapshots are:

- `KokunoYumeto/erdos-straus-foundation`, commit `2b5ab3b63471092624b4fcfac2ab2a0fbafa23a3`.
- `KokunoYumeto/zeta-function-research-reader`, commit `1bcdcebb766d84c6edbb42bc7d4d845e960ec325`.

The ES snapshot was unchanged from the preceding continuation. The RH snapshot adds the theta-transfer and finite complex-current-precision release. Neither repository was modified by this work.

## Read the derivations

The compiled [illustrated reader](output/reader.pdf) contains the full five-track derivation. The [integration audit](INTEGRATION_AUDIT_20260920.md) records every mathematical repair made after independent replay, and [claims.json](claims.json) gives the stable claim and dependency records.

[Track I — the positive-real ES receiving divisor](proofs/01_ES_FRAME_AND_ARITHMETIC.md) proves that an explicit positive-real ES family crosses the extra odd-frame rank-loss divisor while its four literal roots and eight inverse branches remain distinct. It gives an exact degree-twelve polynomial, isolating interval, rank certificate and a conditional polynomial inverse bound for distinct integral witnesses.

[Track II — residue, trace and the non-unit boundary element](proofs/02_RESIDUE_TRACE_AND_BOUNDARY.md) constructs a perfect residue pairing on the finite rank-eight extension and proves that its trace pairing is obtained by multiplication by `2 eta^3`. It calculates the trace determinant, local ranks and nilpotent fibres, and the precise local ES/RH map, including its nonconstant residue-unit correction and its original metric pole.

[Track III — the native Gauss pairing](proofs/03_NATIVE_GAUSS_PAIRING.md) proves the exact factorization of a native moment Gram as residue pairing times the actual second-kind polynomial multiplier. For an arbitrary ES root polynomial it calculates the full relation defect, rather than treating its roots as native Gauss nodes.

[Track IV — improved native inverse margins](proofs/04_NATIVE_INVERSE_MARGINS.md) replaces the repository's determinant-over-trace interval floor by an explicit inverse-trace floor within a factor of the dimension of the actual interval minimum eigenvalue. Its elementary lower bound loses only exponentially, not quadratically in the exponent, in the polynomial degree. It returns the improvement to the original native moment tolerances.

[Track V — simultaneous current certificates](proofs/05_MULTIPARAMETER_CURRENT_CERTIFICATES.md) carries all retained rank-one moment uncertainties through both full minima with their common parameters. It derives bounded multidegree current numerators, an exact Bernstein certificate procedure, and the complete moving-monic correction. The included matrices and polynomials are synthetic exact diagnostics; an actual native-current certificate still requires certified native moments, a correlated feasible set, the outer tail, and a proved sign margin.

[Codex/research handoff](CODEX_HANDOFF.md) gives the precise continuation targets and guards. [Source ledger](SOURCE_LEDGER.md) identifies the repository files and primary literature used, their reading scope, and the one byte-verified uploaded provider included here.

## Reproduce the checks

Python 3.11 or newer and SymPy are sufficient. The delivered receipts record the exact versions used. From the package root:

```console
python checks/run_validation.py
```

Each suite is run in ordinary Python and with `python -O`. The script requires byte-identical stdout and JSON receipts, and fails explicitly on any mismatch. Individual suites can be selected, for example:

```console
python checks/run_validation.py --suite residue
python checks/run_validation.py --suite es_slice
python checks/run_validation.py --suite lowrank
```

The check harness uses explicit runtime guards rather than removable Python assertions. Eleven deliberately false inference controls are rejected in each mode. The exact totals and suite-level hashes are in [the verification summary](results/VERIFICATION_SUMMARY.json). Check counts refer to finite equalities, inequalities and diagnostics, not to that many independently proved theorems.

The corrected live replay has ten suites, 541 exact checks and eleven negative controls in each interpreter mode. The received manifest and its 539-check summary are retained under `received/` as historical receipts; they are not hashes of the corrected live tree.

The native matrix examples in the finite Gauss and multi-parameter suites are explicitly synthetic rational or Gaussian-rational diagnostics. They are not numerical evaluations of hypothetical zeta zeros, native arithmetic moments, projected-current asymptotics, or the ES witness count at every prime. Classical infinite-dimensional or analytic hypotheses are proved or retained in the written notes, not inferred from finite tests.

## Source preservation and scope

The complete uploaded `WEIGHTED_CONDUCTOR_FORWARD.tex` provider is included with its original 25,840-byte body and SHA-256 verified against the upload. Its original phases, masses, quotient kernel and attribution are retained. Other repository files were read through the GitHub connector; no complete raw-byte archive of those repositories is claimed. Their immutable locators are in the ledger.

The package excludes exploratory scripts, raw conversation histories, internal reasoning, credentials and unrelated source collections. It is an additive research packet, not a replacement for the earlier cumulative audit or either repository.

## Main boundaries

The positive-real ES singularity is not an integral prime witness. The residue pairing is bilinear, not Hermitian. The finite flat extension is over `A != 0` and does not eliminate the physical inverse pole. The new Gram margin does not evaluate native moments or make the entire programme numerically inexpensive. A polynomial sign certificate is sufficient on a verified enclosing box; failure on that box is not a sign counterexample at the correlated native point. The closing ES occupancy and RH same-class sign/comparison theorems remain unproved here.
