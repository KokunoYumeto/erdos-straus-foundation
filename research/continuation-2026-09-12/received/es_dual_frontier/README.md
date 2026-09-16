# Positive ES witnesses and a constructive falsity object

The Clankers research workbench. Assistant-developed continuation, 12 September 2026.

Start with `workbench.pdf` (full proofs and source crosswalk), or the two three-page notes under `preprints/`. `card.png` is a posting summary, not the proof. `morphisms.json` and `counterfactual_system.json` specify the retained maps and the object a false prime would require. The uploaded Giuga program is referenced by hash; it is not republished or claimed to have been fully executed.

## Reproduce

Python 3.10 or newer, standard library only. (The pinned lineage helper uses `int.bit_count`.) No network, package install, Lean, or floating-point arithmetic is required.

```sh
python dual_es.py --self-test --out regenerated
python -O dual_es.py --self-test --out regenerated_optimized
python dual_es.py --prime 1201 --out selected_prime
python dual_es.py --verify-negative proposed_full_negative.json
```

`--prime` requires a prime congruent to1 modulo4. It searches the complete canonical atlas and returns an actual marked witness, or constructs and independently validates a full negative certificate. Trial division and exhaustive boxes are finite algorithms, not a claim of efficiency for very large p. All existing tested primes have witnesses.

The counterexample validator demands every shell p/4<a<3p/4 and every divisor u|a² in both E/M channels. It never converts a failed restricted selector into a global counterexample. The two supplied negative prototypes concern only p241,a64,R15 and p37,a18,R35. Both primes have successful other shells.

## What was tested

Complete canonical atlases at exactly p=5,13,37,97,241,1201,2521; not a continuous prime-bound verification claim. Candidate counts are12,64,312,1216,3964,29600,73060. Energy histograms are independently checked through difference-box autocorrelations. The greatest-outside-divisor formula is independently checked on every unit cofactor b<=3000 atR19. Seven rational/integral candidate states traverse all24labels, including the repeated-root middle state. The exact numeric octonion cubic correction and joint Wilson membership are retained.

Normal/optimized outputs, hashes, timing and a fresh-extraction replay are recorded in `execution_receipt.json`. Check counts count explicit Boolean obligations, not independent reviewers or theorems. `lineage/branch_verify.py` and `lineage/aligned_isometry.json` preserve exact tested predecessor bytes; the rest of the preceding archive is not implicitly re-audited.

## Results and limits

Every canonical rational candidate has an exactly known common return denominator D. D=1 is success; D>1 is an odd obstruction. A false prime would require a finite labelled invertible defect operator and a complete prime-coloured obstruction cover. This is an exact description of what a counterexample would be, not an assertion that one exists.

On the constructive track, the integer collision bound is strictly stronger atp1201 than the ordinary Cauchy bound. The maximal-cofactor theorem improves the previous angular sufficient test and constructs a chamber-positive state atp558721 where the older uniform anchor bound does not apply. Neither is claimed to cover every prime or to establish previously unknown numerical coverage.

The full shell criterion, primitive E/M parametrizations, standard integer inequalities, and classical Leech facts are inherited. See `source_reading.json` and `novelty_review.json` for exact roles and limited novelty assessment. No historical priority, independent review, Lean compilation, global ES proof, or actual counterexample is claimed. No remote repository or publication was modified.

## Compile

```sh
pdflatex -halt-on-error workbench.tex
pdflatex -halt-on-error workbench.tex
cd preprints
pdflatex -halt-on-error denominator_defects.tex
pdflatex -halt-on-error denominator_defects.tex
pdflatex -halt-on-error exact_forcing.tex
pdflatex -halt-on-error exact_forcing.tex
```

All coordinates and JSON rational numbers are exact. Large integers must not be parsed through IEEE-754 binary64. Original source rights and source-specific attribution remain unchanged. No new license for inherited source materials is implied.
