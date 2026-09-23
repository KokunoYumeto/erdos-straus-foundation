# Prime-core trace descent and complete rational cofactor capacity

The Clankers, 21 September 2026. Additive Turn 7 continuation. No universal ES occupancy, Type-II occupancy, historical-priority determination, Lean build, or independent mathematical review is claimed.

## Mathematical results

For a prime p = 1 mod 24, every positive rational ES candidate with integer distinguished denominator p/4 < a < p/2, integral tail sum, and a = c q with q prime, gcd(c,q)=1, c in {1,2,3,6}, returns an original middle state at the same p. The inverse retains the old squared gate and both middle orientations. The E-only extension covers a = 2^e q, 1 <= e <= 4; its proof and exact availability intervals are in DYADIC_AND_FIBRES.md.

For arbitrary positive A,B,j and Q=4j-1 > max(A,B), every original divisor U of j^2 with A U = B mod Q is in one of three persistent branches (constant, linear, quadratic) or an explicitly invertible finite quotient domain n k < A B. Every finite word satisfies Q <= max(B(A-1)^2-A, A(B-1)^2-B), sharply. The A=1 case is inherited from the existing capacity-completion module, not claimed anew.

An actual rational E trace source at p=2377702849 needs the finite branch A=9, B=8, Q=503, U=3969 and returns an original M state. At p=9601, a=4*739, u=8, the complete squarefree-cofactor M box is empty; the prime has a separate integer solution. These are precise outcomes of specified maps, not ES counterexamples.

## Files and reproduction

- `preprint.tex`: standalone proof of the composite-core and full two-parameter capacity theorems, inverse fibres, examples, and boundaries.
- `DYADIC_AND_FIBRES.md`: the additional E return and its full integer availability domain.
- `check.py`: portable standard-library replay. It checks all capacity boxes A,B<=24,j<=500, all stated-core trace candidates at p<=1000, and the larger fixed examples using trial-division primality.
- `portable_receipt.json`: recorded output of that portable replay; normal and optimized output agree.

Run `python check.py` and `python -O check.py`. Build with `pdflatex preprint.tex` twice. The portable replay is narrower than the separately delivered full workbench replay (p<=3000, j<=1500), and is not represented as a human review.

## Antecedents and provenance

The input is the 21 September prime-shell trace descent (`proof.md`, exact rational source and prime-shell classification), and the original Type I/II coordinates of Elsholtz and Tao (2013), arXiv:1107.1010, Section 2. The one-coefficient predecessor is `research/incoming/es-turn07-capacity-completion-20260920/core.tex`, equations (7)-(12), read at revision `49976b17491ba927df8bc7f2c2f81d39dfb15ce8`. All results begin with their specified original arithmetic inputs; none supplies the initial trace candidate at every prime.

The larger local research tranche additionally preserves a seven-page proof, both full replay implementations, all original transfer records, the complete A,B<=24 finite-exception catalogue, and the least hard-prime failure of the stated family at p=3361. Those larger replays are not inputs to the written general proofs.

This contribution adds new paths only. Existing proofs and their historical addresses remain unchanged. New text/code follows the repository's CC0 default; cited source texts are not included.
