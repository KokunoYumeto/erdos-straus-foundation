# Pointwise Erdős–Straus continuation

## Status

The universal infinite-exterior/four-middle-shell dichotomy is unresolved in this tranche. The manuscript proves a pointwise weighted angular-forcing theorem, exact anchor exceptions and necessary factorization inequalities. A separate deterministic certificate proves the dichotomy through 10,000,000,000, comprising exactly 14,215,707 hard primes.

The infinite exterior closure is exactly all primitive slopes in [3/2,2], together with (1,s) for every integer s>=8. Cross-mediants between disconnected chamber portions are not included.

## Files

`tranche.tex` and `tranche.pdf`: source-ready manuscript with complete proofs and primary-source crosswalk.

`verifier.py`: standalone Python 3.9+ verifier. It does not import the previous package, any third-party package, or any discovery-search program. It uses arbitrary-precision integer arithmetic, exact rational heights, deterministic trial division, and exact sieves. Explicit exceptions are raised on failed checks even with Python optimization enabled.

`cover_rules.json.gz`: gzip-compressed JSON. There are 78,332 exterior rules and 414,902 middle rules. These are untrusted inputs whose mathematical validity is checked before use. They prove coverage without storing millions of redundant denominator triples.

`certificates/anchor_certificates.json`: all seven signed boxes, all minimizing representatives, exact heights, finite bounds, exact angular exceptions, every oriented exceptional middle state, and complete repairs.

`certificates/hand_exception_tables.json`: every small outside-prime packet test for the first three anchors and complete exceptional divisor boxes.

`certificates/closure_extensions.json`: the three exact failures of the original finite family plus four shells through 10^10. Includes all 138 ray factorizations, all four middle-shell factorizations and empty middle-state lists, and fully marked infinite-closure repairs.

`certificates/variable_anchor_certificates.json`: symbolic minimum-ratio templates for the variable anchors at shell 11, with all prime instances through 10,000 checked. The universal proof is symbolic; these finite checks are not substituted for it.

`certificates/saturation_obstruction.json`: the exact p=2016361 angular obstruction, with the complete two-state fibre, actual exponent vectors and an unrelated valid hybrid witness.

`certificates/verification_summary.json` and `verification.log`: recorded successful verification and resource usage.

`lean_ready_plan.md`: exact dependency and certificate-replay specification, not a compiled Lean proof.

`sources.json`: primary references, exact locators, content-search overlap, and attribution limits.

## Reproduce

Run from any directory, using the file path to the verifier:

```sh
python3 verifier.py --self-test --anchors --cover-bound 10000000000 --out regenerated
```

The full recorded run completed successfully in approximately 34 seconds, using a peak resident set around 268 MiB in this environment. Runtime and memory vary by platform. The cover prime flags alone use about 72 MB; the remaining memory is primarily parsed JSON. No network access is required.

For a smaller coverage replay:

```sh
python3 verifier.py --self-test --anchors --cover-bound 2000000 --out regenerated_small
```

For a complete ordered witness reconstructed from a stored rule:

```sh
python3 verifier.py --witness 11259889 --out selected_witness
```

For complete infinite-closure/four-shell enumeration at one small prime:

```sh
python3 verifier.py --closure-prime 2521 --out one_prime
```

The per-prime exhaustive procedure is finite, but is not advertised as efficient for large primes. Failure of `--witness` means only that no stored rule applies; it is not a proof that the selector has no state.

Compile the manuscript with two runs of `pdflatex tranche.tex`. Only standard TeX packages are required.

## JSON conventions

All state records retain p,R,a,u,h,r,s, the channel, the appropriate quotient, the raw ordered denominators, and chamber membership. A sorted denominator list is additional data, not a replacement for the raw order. The nonapplicable quotient is null. Packet records additionally retain A,t,n,d,g when constructed by the angular map.

Exterior rule columns: `[r,s,R]`.

Middle rule columns: `[R,u,d,p_low_min,p_high_min,p_high_max]`. A zero endpoint indicates that that component is absent. The middle auxiliary d is a certificate modulus with u|d^2; it is not necessarily gcd(a,u) for a reconstructed p. Always apply the canonical decode to a,u to recover h,r,s.

JSON integers exceed 2^53 in many denominator records. A JavaScript default number parser will lose information; use arbitrary-precision integers.

## Exact finite scope

The original 138-ray family with the four middle shells has precisely these three failures through 10^10:
11259889, 788653441, 1350237001.
Their repairing rays are respectively (1,785), (1,282469), (1,343397).
Every middle fibre at each of these primes in shells 11,19,23,39 is empty even without the angle restriction.

No least counterexample to the infinite-closure statement was found; the statement is certified only through 10^10. No universal theorem is inferred from the census, and no infinitude of prime values in the balanced-factor obstruction family is assumed. Stored congruence rules remain individually valid on their explicit intervals beyond the census bound, but are not claimed to cover all later primes.

The SHA-256 manifest identifies files; hashes do not replace replay of the mathematical verifier. No historical-priority claim is made. The content search found prior unweighted signed-box saturation, which the manuscript explicitly credits rather than rebrands as an angular theorem.
