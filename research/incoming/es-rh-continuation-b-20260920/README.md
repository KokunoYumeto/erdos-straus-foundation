# Arithmetic frame nonsingularity and signed-cover descent

This module integrates the 20 September 2026 continuation packet without changing its preserved received files.  It contains four proof tracks, but their local verification status is deliberately separated.

## Erdős--Straus results independently replayed here

For a prime (p\equiv1\pmod {12}), let (N=S^6F\in\mathbb Z) be the exact receiving determinant numerator defined in equation E1.  If

\[
\left(\frac{-511}{p}\right)=
\left(\frac{1241}{p}\right)=
\left(\frac{-15}{p}\right)=-1,
\]

then every positive integral Erdős--Straus witness at that prime has (N\ne0), so its original odd receiving frame is invertible.  The proof exhausts the one-(p)-divisible and two-(p)-divisible denominator patterns.  In the first pattern it retains the exceptional diagonal (x\equiv y\pmod p); in the second, positivity proves that both divisible denominators have valuation exactly one.  Quadratic reciprocity gives exactly 3,456 reduced classes modulo 521,220.

The second independently replayed result is an arithmetic-descent boundary for the actual witness ((13;4,18,468)).  At (q=61) its reduced normalized quartic has roots (4,13,18,41), but all four derivative values are nonsquares.  Its original signed cover therefore has no (\mathbb F_{61})-point, has eight points over (\mathbb F_{61^2}), and the nonsquare twist (\eta^2=2h'(r)) has eight points over (\mathbb F_{61}).  The explicit base-extension isomorphism is (\eta_2=w\eta_1) after adjoining (w^2=2).  Frobenius is four disjoint transpositions and the finite-fibre zeta function is ((1-T^2)^{-4}).

Run:

```powershell
python check_es_arithmetic_descent.py --out results/es_arithmetic_descent.json
```

The current receipt is 923 exact checks with status `PASS`, including the full CRT count, all 163 sorted witnesses at (p=97,397,613,853,997), all eight (\mathbb F_{61^2}) source points, and their Frobenius action.

## Adjacent determinant and heat tracks

Tracks II and III give a sharp two-ratio determinant return and finite-dimensional heat-action remainders in the retained native metric.  Their complete proofs are preserved in `RESEARCH_CONTINUATION.md`.  The packet reports 1,121 new checks and 1,660 checks including predecessors, but the four original new-suite scripts were not supplied with these four evidence files.  That received receipt is preserved under `received/`; it is not relabelled as a local replay.  The locally generated checker covers Tracks I and IV only.

## Files

- `RESEARCH_CONTINUATION.md`: corrected working proof source.
- `received/`: byte-preserved incoming evidence.
- `check_es_arithmetic_descent.py`: independent Track I/IV reconstruction.
- `results/es_arithmetic_descent.json`: exact local receipt and complete finite data.
- `reader.tex`, `RESEARCH_CONTINUATION.tex`, `output/reader.pdf`: readable proof artifact.
- `figures/`: reproducible vector figures and inspection PNGs.
- `SOURCE_LEDGER.md`, `INTEGRATION_AUDIT.md`, `claims.json`: provenance, corrections and machine claim records.

## Boundaries

The character conditions are sufficient, not necessary.  Their failure is not a singularity certificate.  The five-prime census checks the formula but does not prove the quantified theorem.  The finite-field zeta function belongs to one reduced signed fibre and is not the Riemann zeta function.  No universal Erdős--Straus occupancy result, RH conclusion or reduction of a transcendental receiving metric modulo (61) is claimed.
