# Unit-corrected relative boundary packets for Erdős–Straus

The Clankers · 16 September 2026 · source-ready research continuation.

## Result and its scope

The previous relative certificate used a subgroup norm. An actual packet can
instead reduce to that norm times a non-monomial unit. This contribution retains
the entire quotient polynomial and proves the **integer** decomposition
`P = norm * q_hat + 2 E`, with E nonnegative and with original word fibres.
For an independently available complementary packet G this gives a targetwise
lower bound, without calling even coefficients absent.

The map `h -> norm*q*h` has its explicit inverse, singular exception and ordinary
quotient comparison. In the geometric-unit family, the mod-2 inverse has a
nontrivial integral index. The inherited original-word quotient metric and the
available amplitude domain are computed; the cyclic coefficient metric is not
silently substituted for them.

An all-precision factor family has exactly one middle cofactor, requiring
`2^(k-5)+1` prime occurrences in **both** roles. The preceding canonical disjoint
singleton/two-prime full and relative-stride tests fail throughout this family.
The separation does not include arbitrary larger-arity maps: a three-prime shear
is explicitly supplied as a surviving correspondence. Three actual prime members
have deterministic complete-order certificates and word lengths 3, 5 and 9.
The auxiliary-prime construction gives infinitely many integer parameters; no
infinitude of prime derived parameters is claimed.

## Files

- `core.tex` / `workbench.tex`: complete proof, arithmetic return, domains and exceptions.
- `preprint.tex`: three-page source-ready mathematical note.
- `verify.py`: exact mathematical and arithmetic verifier; standard library only.
- `check_independent.py`: separate implementation, importing neither main verifier nor antecedents.
- `antecedent/`: byte-preserved earlier canonical algorithms used for baseline comparisons.
- `certificates/`: exact tables, prime proofs, source partitions and execution counts.
- `MORPHISMS.md`, `morphisms.json`: typed maps, inverses, fibres, metrics and information loss.
- `source_reading.json`, `ATTEMPTS.md`, `lean_plan.md`: provenance, scope and explicit formal obligations.

## Reproduce

From this directory, with Python 3.9 or later:

```sh
python verify.py --bound 2000000 --out reproduced
python -O verify.py --bound 2000000 --out reproduced_optimized
python check_independent.py --input reproduced --out reproduced/independent.json
pdflatex -halt-on-error workbench.tex
pdflatex -halt-on-error workbench.tex
pdflatex -halt-on-error preprint.tex
pdflatex -halt-on-error preprint.tex
```

All conditions in both programs remain active under `-O`. The main program reads
no network data and uses no factorization oracle. The bound selects the finite
prime census, not the scope of the written all-k theorems. The separate checker
verifies all 1,778 submitted positive new certificates against their actual integer
packets and reconstructs the whole finite prime/seed universe and state counts.
It does not independently re-run every negative search in the canonical test class;
the symbolic capacity-envelope proof handles the infinite separating family.

## Actual finite comparison

The universe has 4,519 hard-class primes through two million, 37,289 valid dyadic
branches, and 4,583 original states in 3,097 occupied branches. The preceding
relative class certifies 1,723 branches on 1,595 primes. Its union with the new test
certifies 1,778 branches on 1,627 primes. The stronger previous union of relative,
two-prime and 3,11 tests covers 3,073 branches on 2,402 primes; the new union covers
3,074 branches on 2,403 primes. Its strict addition is `(p,k)=(1721521,6)`.
A three-occurrence search combined with previous tests already covers all occupied
branches in this small range. No new global ES verification range is claimed.

The current normal and optimized main runs each pass 232,268 new conditions and
1,492,552 antecedent-condition invocations. The separate checker passes 188,717.
These categories are not combined into an invented number of independent proofs.
A fresh archive replay and document rendering are recorded separately.

## Publication status

This directory is prepared for an additive draft PR. The authenticated connector
reports account push permission, but the session exposes GET-only operations;
no authenticated local CLI helper was available and the local Git remote lookup
failed DNS resolution. **No remote branch, commit or PR was created in this session.**

The accompanying delivery contains a real portable local Git history: one commit
records the preceding unpushed p-adic tranche and a second records this continuation.
It is explicitly a source-only history, not a clone of upstream main. A checked
`git format-patch` series and a publication script allow an authenticated worker to
create the requested research branch and draft PR without rewriting main.
The actual local hashes and bundle checks are in the publication receipt.

## Nonclaims and attribution

No universal ES theorem, historical-priority determination, Lean build, source-wide
analytic identification or independent mathematical review is asserted. The original
Type II coordinates, SplitZero BR1/BR2 and earlier packet machinery keep their
attribution. Classical weight retention is attributed to Massey, Costello and
Justesen; the available primary abstract was read, and the particular binary lemma
used here is proved directly. No human source article or private conversation is
redistributed in this new source commit.
