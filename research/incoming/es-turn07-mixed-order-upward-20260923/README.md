# Affine channels, mixed-order coefficient sections, and an upward shell return

This continuation remains at Stage 7. It does not prove that the complete
Erdős–Straus source is occupied at every prime.

## Mathematical results

1. On the exact common-trace locus, the E and M fine coordinates differ by the
   affine shift `(p-1)/K` in `Z/D`. The labelled two-channel count is
   `J=(I+T_omega)C`. Because `D` is odd, this operator is injective, has a
   signed alternating inverse on every translation orbit, and has cokernel
   `(Z/2)^gcd(D,omega)`. Uniform paired positivity is exactly the support-cover
   condition `supp(C) union (supp(C)+omega)=Z/D`; total mass alone cannot prove it.
2. A mixed-order chain that stops at a proper divisor `g` reduces the paired
   problem to an exact quotient coefficient `Q` on `Z/g`. Its complete-block
   subsource covers every paired target exactly when
   `supp(Q)+{0,omega mod g}=Z/g`. The sharp support threshold is
   `(g+gcd(g,omega))/2`; if all residual steps lie in a proper subgroup, the
   certificate cannot close. Terminal intervals are retained separately.
3. The original additive coefficient polynomial has a constructive mixed-order
   lower bound along a strict chain of cyclic subgroups. Nonunit directions are
   retained. A backward digit algorithm returns an actual bounded original word;
   its cyclic carries, integer multiplicities and inverse are explicit.
4. The strongest bound of this specified chain form is computed on the divisor
   DAG of the actual defect D, with at most n*tau(D) candidate edges. Failure of
   that criterion is not a proof that the coefficient vanishes.
5. Two actual hard-prime packet families witness that the structural criterion
   is strictly stronger than the previous unit-width test: every fine coefficient
   is two while that earlier criterion fails. The second uses two
   nonunit selected directions. All other original divisor words remain present.
6. Decreasing the last quotient capacity by one can remove an entire fine-defect
   subgroup, including zero, in actual hard-prime packets. This arithmetic
   sharpness construction does not furnish or claim an ES counterexample. The
   finite `p=3904062961` shell has coefficient vector
   `(0,1,1,0,1,1,0,1,1)` and stabilizer `{0,3,6}`; a separately certified
   `R=3` exterior word proves that the same prime satisfies Erdős--Straus.
7. The invariant 4a+s, with s|a, gives an exact finite source-changing relation.
   It repairs the critical p=67369 M trace by a'=a+1, changing its prime-factor
   support, and extends to an explicitly reduced infinite hard-prime progression.
   A p=97 control has no full state anywhere in its fixed invariant fibre.

The core proof is `core.tex`; `workbench.tex` builds the complete paper.
`preprint.tex` is a shorter standalone account. The inherited square-zero
coordinate theorem and the p=67369 obstruction are credited to the preceding
supplied tranche. The subgroup-chain argument is elementary and no priority
claim is made for the abstract cyclic statement or the arithmetic continuation.
The `figures/` sources display the exact affine channel operator, the
`9 -> 3 -> 1` carried digit section, and the complete four-cell plus-factor
fibre at `p=67369`.

## Reproduce

    python run_all.py --bound 10000 --directory reproduced

This runs the main implementation, optimized Python, and the separate checker,
then compares exact UTF-8/LF JSON bytes. All code uses the standard library.
The separate checker imports neither the main implementation nor predecessor
software. Its factor/primality checks are distinct from the discovery tests.

Public upward return:

    python arithmetic.py --p 67369 --a 16849 --u 4067 --channel M

The complete original replay is bounded by p<=10000 and p=1 mod24. Isolated
larger primes are listed in `certificates/prime_certificates.json`, with a
recursive complete-order proof; they are not a new overall ES verification range.
The abstract lane contains 161887 finite polynomials, checked against both the
original convolution and a separately implemented ordered-chain optimizer.
The hardened independent checker also reconstructs every serialized chain,
packet word, progression, stabilizer, plus-factor cell, source state and
complete-order prime root used by the claims.

The two positive isolated packet primes are 271575361 and 4755800916721.
Their original scalar factors are H=29 and H=101. These values are results of
an explicitly bounded deterministic search and are independently certified;
they are not assumed prime because a progression is reduced.

## Source and publication status

The integration base is `6c064a07298cdba38352998364ce6b7cb3efa973`, which
adds the verified square-zero/Pell tranche to the earlier mixed-fibre and
middle-spectrum revision. This continuation uses the recorded supplied archive
and the integrated proof source, not an inferred version. See
`READING_AND_DELTA.md`, `source_reading.json`, and `publication_receipt.json`.

`verification.json` records observed replay outcomes. `MANIFEST.json` describes
exact packaged bytes. The cumulative ZIP preserves the preceding cumulative
archive byte-for-byte; it is not a fresh mathematical audit of that history.
