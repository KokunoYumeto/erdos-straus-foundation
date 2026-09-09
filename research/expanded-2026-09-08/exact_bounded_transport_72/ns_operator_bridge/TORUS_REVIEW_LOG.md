# Bounded independent torus-cover construction — 8 September 2026

The task was to prove the exact connection between the source matrix `J=[[3,1],[1,5]]`, its torus covering map, fixed finite torsion restrictions, and original ES factor-packet counting. The source used is the preserved 165-page manuscript, Section 6, equation (6.2), printed page 63, and Lemma 6.2/equation (6.19), printed page 67. The manuscript's own displayed author is OpenAI; broader attribution is being checked by the parent's provenance agent. The source does not supply an independently verified PDE theorem for this calculation, and none is used.

The construction retains original eigenvectors, eigenvalues, and Fourier factors `2πi`, and proves the exact directional operator and inverse intertwining on finite trigonometric polynomials. It proves every fibre of the cover and every fibre of its restriction to N-torsion, as well as the full inverse-image averaging operator, its adjoint, kernel and fibres. It explicitly embeds the actual dual of each finite ES unit group into a torus by a retained generator tuple and proves the image equations and inverse.

A real discrepancy was found. The unchanged finite sampling domain creates nonidentity 14-torsion terms in joint packet averages, and repeated covers can change even a single packet count. In the original shell p=13, a=4, R=3, the coefficient at each original target is 2; the one-step joint mean is 13, while the independent count is 4; the twice-covered first-coordinate mean is 5. The proof identifies every extra exponent-pair fibre. Full inverse-image sampling recovers the original count at every cover level. The parent is also constructing a finite quotient-coset sampling repair.

Independent algebra review by `independent reviewer` accepted all finite-group, Fourier and full-preimage formulas, emphasizing that uniform coordinate marginals do not imply uniform joint distribution. Parent review found the exact formulas correct and identified two TeX layout defects; both were repaired before freezing.

The checker uses only Python standard-library integers, rational torus points, and exact cyclotomic-polynomial remainder calculations. Its successful final run covered:

- 38,024 source/target pairs on fixed torsion for 1 ≤ N ≤ 48;
- 40,180 full-preimage torus points for 1 ≤ N ≤ 20;
- 8,976 power-fibre targets for 1 ≤ N ≤ 16 and 0 ≤ m ≤ 5;
- 1,134 exact quadratic-ring directional/frequency identities;
- 10 original prime-shell fixtures, preserving all exponent allocations, with exact character sums for both channel targets, joint means, and cover levels 0 through 5.

Frozen source SHA-256: `4f4fae9611f87d10896b6019342370d11f9d35e8f9a5a90bde844cd7dfd66704`.
Checker SHA-256: `0f7bf5d0e91649fc9d2c6d94bb039fffd3c431c228f89738a6d0e962fe12a466`.
Results are stored in `check_torus.json` and carry both hashes.

The source contains seven labelled mathematical statements and one section label. No global ES occupancy, global ES counterexample, or PDE conclusion is claimed. This historical review precedes the cumulative PDF QA recorded separately.
