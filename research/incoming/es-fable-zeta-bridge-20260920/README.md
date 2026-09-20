# Exact ES–Fable–zeta coordinate bridge

This continuation proves an exact map from every actual ordered Erdős–Straus exterior state to the generic eight-sheet signed Fable cover and then through one fixed weighted conductor. The principal readable source is [ES_FABLE_ZETA_CROSSWALK.tex](ES_FABLE_ZETA_CROSSWALK.tex).

For a solution `4/p = 1/x + 1/y + 1/z`, put `S=p+x+y+z` and

```text
H_ES(U,V) = -S^{-1}(U-pV)(U-xV)(U-yV)(U-zV).
```

Its normalized coefficient vector has

```text
u0 = -1/S,
u2 = -(p(x+y+z)+xy+xz+yz)/S,
u3 = 5xyz/S,
u4 = -pxyz/S.
```

Consequently the prime is intrinsic, `p=-5u4/u3`, and the coefficients satisfy

```text
625u0u4^3 - 125u3u4^2 + 25u2u3^2u4 - 4u3^4 = 0.
```

On the stated chart `u0u3u4 != 0` the converse is exact at the algebraic level. The equation does not itself impose positive integral roots, primality, ordering, or the original channel gates.

More strongly, this chart is exactly the `S3` quotient of the symmetric ES solution scheme.  The inverse recovers `p` and all three elementary denominator sums.  The hypersurface is irreducible, and its reduced singular support is `u3=u4=0`, disjoint from the nonzero arithmetic chart.  Root collisions are retained as separate internal divisors: positive solutions with collisions exist, so only the distinct-root locus has eight signed states.

For every actual Turn 7 exterior state, the four roots `p,x,y,z` are distinct. The target therefore lies in the genuine finite étale degree-eight locus, not in the nonproper locus. The two states marking `p` are given explicitly, and all eight source coordinates are stated in the TeX. The earlier reciprocal-cubic suspension is retained as a separate seven-state boundary map; it is not substituted for this stronger quartic.

The two quartics are nevertheless related exactly. Inversion `T -> p/T`,
deletion of the marked root, insertion of infinity and normalization give

```text
H_rec(U,V) = u4^-1 V/(U-V) H_ES(pV,U).
```

The reciprocal coefficients forget exactly one common scale. The projective
root schemes are explicitly isomorphic, collisions and discriminants transport
without suppression, and the signed covers meet in a 14-point fibre product.
A direct generic signed-cover map is obstructed by an explicit derivative-twist
square class; after adjoining its square roots, the projective correspondence
is 8-to-8, while the affine reciprocal chart loses exactly the prime sign.

The final bridge uses fixed invertible maps `Phi_*`, `Psi_*` and the original conductor `T_A,*`, with `T_A,* Phi_* = Psi_*`. `Psi_*` is a receiving coordinate map, not the conductor. No ES root is identified with a zeta zero, and no universal ES existence theorem is claimed.

The inverse moment recursion, reference-root evaluation, and the full matrix `K` are now written out.  They give explicit receiver linear forms `U0,U2,U3,U4`, the literal receiver equation `G(U0,U2,U3,U4)=0`, and a polynomial selector for exactly the two prime-marked states in a distinct-root eight-point receiver fibre.

The fixed-input continuation strengthens the domain and boundary analysis.
Every positive integral witness at a prime `p = 1 mod 12` has four distinct
literal roots, with explicit fixed-`p` lower bounds for the discriminant and
derivatives and upper bounds for all inverse coordinates.  At prescribed
nonzero `p`, over the open base
`B_p={(A,C): A C d_p Disc(g_p) != 0}`, the signed cover splits into ranks
`2+6`; its exact monodromy has order `48`, its deck group is `C2 x C2`, and
its averaged metric retains a full two-dimensional block on the two trivial
summands.

The reciprocal signed coordinate `eta=xi^-1` gives a finite flat rank-eight
completion.  A double root has local fibre `C[eta]/(eta^4)`, while the
original inverse keeps its exact meromorphic pole.  The ES boundary family
`(p;p,2p/5,2p)` admits a typed local-algebra isomorphism to the auxiliary
paired-root fibre after the displayed scaling.  This does not identify global
fibres or zeta zeros.  A separate invertible odd-moment frame factors the
original odd evaluation and identifies exactly where that evaluation loses
information.

The same source contains two further exact interfaces. An invertible
raw-cell--Lorentz matrix and its inverse transport the archived
three-dimensional tetrahedron without discarding a coordinate. The odd
receiving determinant pulls back to an explicit primitive irreducible
polynomial on the ES chart; a sign-changing rational family proves a
positive-real pairwise-distinct intersection. The stated splitting and
common-denominator criterion is exact for lifting a rational point to an
integral prime-numerator solution, but no such rational lift is asserted.

The cumulative reader now also includes the separately received fixed-target
capacity completion. It classifies every `W | j^2` in the class `t mod
(4j-1)` into canonical, companion and finite branches, proves the sharp finite
bound `h <= t^2-3t+1`, constructs infinitely many hard-prime equality states,
and constructs, for every fixed `t >= 4`, infinitely many exterior states
whose complete same-grade middle box is empty. These are not ES
counterexamples because their exterior states are already solutions.

The original integral signed completion is now included in full.  In the
literal-root basis `(p,x,y,z)`, its exterior and middle normalization matrices
have Smith exponent lists `(0,0,0,0,0,0,1,1)` and
`(0,0,0,1,1,2,2,3)`, hence indices `p^2` and `p^9`.  The source proves the
conductors, inverse lattices, reduction kernels, boundary-lift obstruction and
the exact information loss in literal-root interpolation.  A separate
crosswalk proves that these orders are the same orders used by the more
general defining-prime calculation, in the same ordered bases.

The defining-prime calculation retains all closer-pair valuations, not only
the separated exterior and middle cases.  When `p | S`, its translated chart
is related to the original chart by the exact quadratic twist
`q^2=S/(S-4 lambda)`; descent over `Q_p` is therefore controlled by the
displayed square class.  The normalized factors give the signed-label Galois
representation and the conductor-index identity

```text
2 length(normalization/original order) + a(W)
    = 6 sum_{i<j} v_p(t_i-t_j).
```

The newest arithmetic track proves a sufficient three-character condition
for odd-frame nonsingularity at every positive integral witness.  Quadratic
reciprocity gives exactly 3,456 reduced residue classes modulo 521,220.  An
independent local checker also verifies all 163 sorted witnesses at the five
diagnostic primes.  The witness `(13;4,18,468)` gives an exact signed-descent
example at `q=61`: no original signed point over `F_61`, eight over
`F_(61^2)`, and eight `F_61`-points on the specified nonsquare twist.  Its
finite-fibre zeta function is `(1-T^2)^(-4)`; this is not the Riemann zeta
function.  The adjacent determinant and heat tracks are printed with complete
proofs, while the received executable receipt for those two tracks is kept
separate because their four scripts were not in the supplied evidence packet.

## Reproduce

Run the new checker:

```powershell
python verify_es_fable_zeta_bridge.py
python ..\es-defining-prime-continuation-20260920\verify_defining_prime.py
python ..\es-rh-continuation-b-20260920\check_es_arithmetic_descent.py --out ..\es-rh-continuation-b-20260920\results\es_arithmetic_descent.json
```

The frozen upstream packet in [upstream](upstream) contains the full global inverse, conductor, signed-evaluation and monodromy proofs and their independent checkers. Its principal source SHA-256 is `bfb75ff468f35b71103ad2671e22f20fee0414df4a43d1dab5fc2d19aabbd1b6`. See [AUDIT_NOTES.md](AUDIT_NOTES.md) before quoting its endpoint-label notation.

## Files

- `ES_FABLE_ZETA_CROSSWALK.tex`: complete new derivation and exact scope.
- `verify_es_fable_zeta_bridge.py`: exact symbolic certificate.
- `FIXED_INPUT_BOUNDARY_MONODROMY.tex`: hard-prime domain theorem,
  fixed-input monodromy, finite boundary completion, local bridge, and odd
  moment frame.
- `verify_fixed_input_boundary.py`: symbolic and finite-group certificate for
  those results.
- `FABLE_ES_TETRAHEDRON.tex`: exact raw-cell--Lorentz transport and retained
  three-dimensional tetrahedron.
- `ODD_RECEIVER_ES_PULLBACK.tex`: odd receiving determinant, exact ES
  pullback, positive-real intersection and arithmetic lift criterion.
- `CAPACITY_COMPLETION.tex`: complete fixed-target capacity theorem copied
  from the separately preserved capacity package for the cumulative reader.
- `INTEGRAL_COMPLETION.tex`: complete original-lattice normalization,
  boundary and finite-place control proof.
- `DEFINING_PRIME_CONTINUATION.tex`: complete collision-stratum calculation,
  translated-chart twist, fixed-prime gluing and retained complex metric.
- `INTEGRAL_NORMALIZATION_CROSSWALK.tex`: identity of the two E/M orders,
  bases, matrices, quotients and special fibres.
- `LOCAL_GALOIS_REPRESENTATION.tex`: signed-label representation, Artin
  conductor and the `p=1201` Frobenius calculation.
- `ES_RH_MULTI_CONTINUATION.tex`: positive-real rank-three crossing,
  residue-to-trace degeneration and native Gram interfaces.
- `ES_RH_CONTINUATION_B.tex`: arithmetic-frame theorem, determinant return,
  finite heat certificates and the `q=61` descent proof.
- `fixed_input_boundary_receipt.json`: current output of that certificate.
- `INTEGRATION_AUDIT_20260920.md`: internal proof rechecks, corrections,
  and the RH-only material preserved without import into the ES theorem chain.
- `received/combined-continuation-20260920.txt`: unchanged received source,
  SHA-256 recorded in the audit and source ledger.
- `verification_receipt.json`: current checker output.
- `MORPHISMS.md`: domains, codomains, fibres, kernels and information loss.
- `claims.json`: stable result records.
- `source_reading.json`: content-level source-use ledger.
- `AUDIT_NOTES.md`: independent audit corrections and qualifications for the frozen upstream packet.
- `upstream/`: byte-preserved cumulative source packet.
- `build/`: documented, formatting-only build copy with one repaired TeX delimiter.
- `output/pdf/`: compiled cumulative reader and build receipts.
- `pdf_qa.json`: hashes, page counts, render review and checker replay receipt.
- `figure_qa.json`: proof locators, hashes, dimensions and visual inspection
  receipt for the research illustrations.

## Status

This is structural continuation, not sample collection. It proves an exact
quotient chart, its singular and collision strata, the complete generic
fibre, arithmetic inverse on the strict exterior chamber, the exact elementary
transform to the seven-state degeneration, the fixed-input order-48 cover,
the finite rank-eight boundary completion, explicit receiving equations, and
exact operator transport. It also proves the complete fixed-target capacity
classification and its sharp same-grade boundary, the original integral
indices and conductors, the defining-prime local representation, and the
three-character receiving-frame theorem. The unresolved global problem
remains existence of an original ES state at every prescribed hard prime.
