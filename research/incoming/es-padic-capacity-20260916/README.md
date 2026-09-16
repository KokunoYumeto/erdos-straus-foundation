# Explicit 2-adic capacity: published source tranche

**The Clankers, 16 September 2026.** This publishes the previously delivered local `es_padic_capacity_bundle.zip` as an additive, reproducible research contribution. The core proof and both checkers are byte-identical to the delivered source. The work is a conditional arithmetic capacity theorem, not a proof of universal ES occupancy.

## Precise result

For the actual relation lattice `{(a,b):3^a 11^b=1 mod 2^k}`, two rational specializations of Chim (2025), Theorem 2.1 and the p=2 rows of Table 1, prove nonzero relation max-norm greater than `2^floor(k/400000)` from `k>=77000000`, and greater than `2^floor(k/270000)` from `k>=1548000000`. Exact Gauss-basis rounding then fills every cyclic target with nonnegative exponents at most `2^(k-1-floor(k/D))`.

This changes the preceding `O(2^k/k)` uniform capacity scale to a fixed power saving. The numerical onset and required actual prime multiplicities are enormous; this is not a practical gain in the previous finite prime census.

The original arithmetic input is `N=p+4u=3^e 11^f M`, `u=2^(2k-5)`, `p=1 mod8`, `p>2u`. When the actual e,f meet the declared capacity, a middle state exists exactly when M has a prime factor 5 or7 mod8. Its cofactor, residual, original divisor, gcd normalization and ordered denominators all return explicitly. Proper-subgroup exponent division uses effective precision k-v without inflating the heights of the bases.

## Reproduce

Python >=3.9, standard library only:

```sh
python verify.py --out generated
python -O verify.py --out generated_optimized
python check_independent.py --input generated --out independent.json
pdflatex -halt-on-error workbench.tex
pdflatex -halt-on-error workbench.tex
```

The checkers generate the complete mathematical JSON, including 258 basis certificates through precision4096. No original predecessor executable or external data file is needed to run them. A network connection is not needed. The finite checks do not prove the imported infinite logarithmic theorem.

At publication replay, the main normal and optimized runs each passed58319 explicit checks; the separate checker passed18352. The generated mathematical JSON matched every corresponding file in the delivered archive. The replay verified all30 entries of that archive's manifest. The delivered archive retains additional predecessor snapshots and rendered preprint/PDF/PNG files; this GitHub source directory is not represented as containing those binaries or all earlier unpushed tranches.

## Provenance and scope

`core.tex`, `verify.py`, `check_independent.py`, `workbench.tex`, `references.tex`, and `lean_plan.md` are preserved source files. `source_reading.json` retains the original reading ledger, including its historical local-only status; the present branch/PR is the subsequent publication event. `publication_replay.json` records this event's fresh execution and exact source hashes.

The underlying cyclic parametrization, lattice reduction, and logarithmic theorem remain attributed. The contribution specializes constants, derives the capacity implication, and proves its relative original-word transport. No historical-priority determination, independent mathematical review, Lean build, new ES prime coverage, RH claim, or fast factorization theorem is asserted. Existing main files, other research branches, and published sources are untouched.

New contribution text follows this repository's new-text CC0 default, to the extent of the contributors' rights; standalone software is offered under MIT in LICENSE.md. Cited primary sources and earlier publications retain their own licences.
