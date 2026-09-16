## Unit-corrected boundary packets with exact word inverses

This draft adds a standalone unit-boundary continuation at `research/incoming/es-unit-boundary-20260916/`. It is based directly on `main`; it does not replay the p-adic files already preserved in PR11 and does not modify another pull-request branch.

For an available packet reduced without deleting its unit factor to `T^nu U(T)`, the source proves the integer identity

`P = J_D q_hat + 2E`, with `E >= 0`,

where `J_D` is the full integer cyclic norm. The notation is deliberately separated from the relative boundary norm `N_D`. The identity gives a targetwise lower bound after convolution with an independently available source packet while retaining the original word labels, odd representatives and paired even remainders.

The BR1 comparison is made over the actual prequotient `F2[[T]]` with its unit. The source states the inverse, its singular exception, the failure of ordinary projection to invert the boundary inclusion, the integral circulant index, the actual-word availability domain and the source quotient metric.

An explicit family has exactly one middle cofactor and requires `2^(k-5)+1` prime occurrences in both roles. The preceding declared singleton, same-coset-pair and relative-stride tests fail on that family. This is not asserted as a no-go theorem for arbitrary affine maps: a three-prime shear is supplied as a separate exact surviving correspondence. The prime members `1721521`, `1492567108321` and `2413105093468609` have deterministic complete-order certificates, unique-cofactor censuses and minimum lengths 3, 5 and 9. The auxiliary Dirichlet argument yields infinitely many integer parameters; it does not prove infinitely many derived primes.

Fresh normal and optimized replays each execute 232,268 new checks and 1,492,552 antecedent-check invocations. The separately implemented checker executes 188,717 checks without importing the main verifier or antecedent modules. Through two million, the scan covers 4,519 hard-class primes, 37,289 valid dyadic branches and 4,583 original states. Against the stronger prior union, the only added branch/prime is `(1721521, 6)`; a three-occurrence search plus the earlier tests already covers all occupied branches in that finite range.

The branch contains the full proof source, typed maps, compact certificates, deterministic verifiers, exact source ledger and a formalization plan. No proof of the Erdős–Straus conjecture, new global verification range, Lean build, source-wide analytic identification, independent mathematical review or historical-priority conclusion is claimed.
