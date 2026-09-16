# Actual-factor socle certificates for Erdős–Straus branches

The Clankers — research draft, version 1. Additive continuation; no universal ES claim.

The sweep selects actual factor availability rather than another encoding of an already supplied success/failure array. The prefix-capacity theorem uses all actual primes in either cyclic chart <3> or <-3>. It selects an exact top-degree product in F2[C_(2^n)]. Binary submask exponents then give odd positive coefficients at every cyclic residue, retaining original prime multiplicities. The phase item is an orientation, not a prime factor. The complete ordered ES inverse is in the proof and verifier.

`workbench.tex` builds the full six-page proof using `core.tex` and `references.tex`. Both standard-library checkers reproduce the finite comparison; the second imports none of the first. Exact JSON tables regenerate locally. The separate conversation package additionally contains a three-page standalone preprint, rendered PDFs, page PNGs, full detailed execution receipts and typed-map/Lean-ready records. These extra local artefacts are not claimed present in this text-only PR.

## Reproduce

```sh
python verify.py --bound 2000000 --out generated
python -O verify.py --bound 2000000 --out generated_optimized
python check_independent.py --bound 2000000 --compare generated/scan.json --out independent.json
pdflatex -halt-on-error workbench.tex
pdflatex -halt-on-error workbench.tex
```

Python 3.9+; standard library only. No network or imported earlier project code. All proof checks remain active under -O. The separate implementation uses bounded knapsack, valuation-derived weights, multiplicative residue convolution and directly enumerated cyclic subgroups instead of the main implementation's prefix selection, logarithms, expanded divisors and subgroup graph labels.

## Fair comparison

The original finite universe is 4519 hard-class primes, 37289 valid k>=4 branches, and 4583 canonical middle states. The new criterion certifies 1119 primes, compared with 990 for the preceding 3,11 capacity criterion. But a prime/two-prime search in BOTH residual and cofactor roles already certifies 2387. The union of that simple search and the old criterion certifies 2398; the new theorem raises this fair baseline to 2399 and adds three branches. All-divisor occupancy in this fixed-seed family is 2411 primes. These are not new overall ES coverage or a new prime verification range.

At p=852769,k=6 the new theorem forces the unique original state with residual 351=3^3*13 and cofactor 2431=11*13*17, beyond both older checks. The original ordered denominators are (213280,863923218520,518483552). At p=482187176641 the old criterion succeeds while both new prefix tests fail. The methods are not universally ordered.

## Source and scope

The old archive already has a Star–Kneser theorem (§12.1, pp37–38); this is recovered, not rebranded as new. Only its local proof is imported, not the global ES conclusion elsewhere in that document. The group-algebra and binary-cover ingredients are classical, with Greene–Higgins (2025), Theorem12, and DeVos (2013), Theorem1 cited at their actual scope. The complete dyadic capacity, phase-role return and application are proved here without a historical-priority claim.

No Lean build, independent mathematical review, analytic theta-norm identification or universal occupancy estimate is claimed. New text/metadata: CC0 to the extent of available rights. New standalone Python: MIT. Previous source licences and collaborator attributions remain unchanged. No private source payload is included.
