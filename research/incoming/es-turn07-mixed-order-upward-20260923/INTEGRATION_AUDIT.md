# Integration audit: mixed-order sections and upward return

## Intake and replay

The supplied cumulative archive, current inner archive, trace paste and complete
handoff paste are identified in `RECEIVED_ARCHIVE.json`. The supplied manifest
contained 45 entries; all 45 hashes matched. A fresh normal replay through
`p <= 10000`, together with the separate checker, reproduced all nine supplied
JSON tables byte for byte before any verifier hardening. The replay counted 143
primes, 171732 first-half shells, 5616298 original words, 11466 traces, 7547
full states, 2522 squareful trace shells and 4139 trace parts. It found four
positive mixed-chain parts, five parts covered by the earlier unit-width test,
and no chain-only part inside that bounded census. The isolated packet and
upward theorems are separate exact constructions rather than inferences from
those aggregate counts.

## Mathematical determinations

1. **Mixed-order coefficient completion: accepted.** For
   `g_0=D`, `g_j=gcd(g_{j-1},lambda_{i_j})` and
   `m_j=g_{j-1}/g_j`, the reverse decoder is exact. If the selected lengths
   dominate the relative radices and the chain reaches one, every residue has
   the stated positive integer lower bound. The transported law keeps the cyclic
   carry; the digit set is not replaced by a product-group law. The divisor-DAG
   optimizer is exact within this stated chain class.

2. **Fibre statement: accepted after correction.** The decoder inverts the
   augmented residue-and-unused-digit map. The residue projection alone has
   multiple words in each bin. A free-integer kernel basis is obtained by
   choosing one reference word per bin and subtracting it from the other words.
   The rank `D(mu-1)` is unchanged. All pairwise differences generate the
   kernel but are not independent.

3. **Hard-prime packets: accepted.** At `D=9`, the exact polynomial is
   `(1+X^5)(1+X^6+X^12)(1+X+X^2)=2 sum_{j=0}^8 X^j`; the chain is
   `9 -> 3 -> 1` with steps `6,1`. At `D=15`, the exact polynomial is
   `(1+X^11)(sum_{j=0}^4 X^{6j})(1+X^10+X^20)=2 sum_{j=0}^{14} X^j`;
   the all-nonunit selected chain is `15 -> 3 -> 1` with steps `6,10`.
   The finite primes, packet words, complements, reduced progressions and
   complete-order certificates were independently recomputed.

4. **Arbitrary odd-defect sharpness: accepted after proof expansion.** The
   calculation `q_k^2 = 1-2Kc (mod R)` gives the required last step. The exact
   original residue ratio is
   `-1 + K(c beta_k - sum_{i<k} lambda_i beta_i)`. Earlier exact-radix
   intervals biject onto `H_m=m Z/D`; the last `m-1` odd exponents give every
   nonzero quotient class. Therefore the coefficient is zero on `H_m`, one on
   its complement, and its stabilizer is exactly `H_m`.

5. **Finite sharpness realization: accepted and completed.** For
   `D=9`, `(q_1,q_2)=(163,107)`, `H=523`, `a=976015801` and
   `p=3904062961`, the exact coefficient vector is
   `(0,1,1,0,1,1,0,1,1)` and the stabilizer is `{0,3,6}`. The reduced
   exact-exponent progression has modulus `2925429291933960`. The displayed
   `R=243` shell has no full original word. A separate exterior full E witness
   at `(a,R,u)=(976015741,3,89)` proves that this prime is not an Erdős--Straus
   counterexample.

6. **Plus-factor map: accepted after an omitted coprimality step was added.**
   At fixed `p,C`, the cell formulas and inverse are exact. For a unit-ray cell,
   `gcd(R',s')=gcd(4n's'-p,s')=gcd(p,s')=1`; hence the inherited gate
   `R' | (4n'+1)` is equivalent to `R' | M=(4n'+1)s'`. The incoming fibre
   enumerates every cell, every coprime divisor split, and both original square
   gates.

7. **Upward return: accepted.** At `p=67369`, the marked source
   `(a,R,u,h,r,s)=(16849,27,4067,83,7,29)` maps through the retained
   invariant `C=56`, `M=67425` to
   `(a',R',u',h',r',s',kappa')=(16850,31,674,674,1,25,2174)` and to the
   exact three denominators printed in the paper. The same formulas hold on the
   reduced prime progression `p=67369+3775800k`. The `p=97` control proves that
   a fixed plus-factor fibre may have no full state; it is not a global
   obstruction to transformations through other fibres.

8. **Ordered-tail map: typed explicitly.** The E-tail permutation is the
   involution `tau_E(a,Y,Z)=(a,Z,Y)` on ordered rational solution triples. It
   need not preserve the original E exponent box and is therefore not counted
   as another canonical incoming word. The M word already records its order.

9. **Later affine-channel suggestion: retained only as a structural theorem.**
   The supplied mixed-boundary archive's proposed E/M shift was rederived from
   the original channel formulas, without using its census. The result is the
   exact common-trace condition `K | (p-1)`, the oriented shift
   `c_E=c_M-(p-1)/K`, the injective odd-order operator `I+T`, its alternating
   inverse and orbit-parity cokernel, and the exact support-cover criterion.
   Combining it with a partial radix chain gives a quotient-support theorem and
   proves that two channel labels cannot replace a missing final radix when the
   residual steps remain in a proper subgroup. The numerical census and the
   unrelated zeta transfer are excluded; hashes and scope are recorded in
   `AFFINE_LEMMA_INPUT.json`.

## Verification hardening

The separate checker now reconstructs serialized chain metadata, exponent
parts, source words, packet progressions, prime roots, boundary stabilizers,
plus-factor cells, prefix traces and negative-control state sets. It recomputes
`K,D,delta`, defects, quotient data, ordered denominators, exponent vectors and
the exact exterior witness. The main producer now stores the boundary
stabilizer, exact-exponent progression and exterior witness, and requests prime
certificates for every packet scalar and fixed prime used by the claims.

## Literature and scope

The corpus index routed the Elsholtz--Tao and Lopez author TeX sources; exact
reading locators and uses are in `source_reading.json` and
`topic_literature_route.json`. Yamamoto and Sutherland were read from primary
PDF sources because routed author TeX was unavailable. No historical-priority
claim is made. No universal Erdős--Straus theorem, arbitrary-prime coverage,
human review, Lean proof or global termination theorem is claimed.
