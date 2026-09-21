# Independent audit of the nine-word divisor-descent classification

## Object audited

The audited source is
`work/turn7_divisor_descent_intake_20260921/current/core.tex`, especially
Theorem `Complete divisor-removal domain`, Proposition `Every square deletion
and its capacity`, equation `(nine)`, Theorem `Uniform one-step descent for nine
exact words`, and Theorem `Exact universal seed classification`.

For a source `(p,a,R,u,c)` the defining data used in this audit are

\[
 p\equiv1\pmod4,\qquad p/4<a<p/2,\qquad R=4a-p,
 \qquad u\mid a^2,
\]

with `c` equal to `E` or `M`,

\[
 G_E=4u+1,\qquad G_M=p+4u,
 \qquad R\mid G_c^2,
\]

and

\[
 d=\frac{R}{\gcd(R,G_c)}>1,\qquad m=4K(u),qquad
 K(n)=\prod_{\ell^e\parallel n}\ell^{\lceil e/2\rceil}.
\]

The claimed deletion domain is

\[
 \mathcal K_{p,a,R,u,c}
 =\{k:k\mid R,\ d\mid k,\ k\equiv1\pmod{4K(u)}\}.
\]

Each `k` is asserted to produce

\[
 R'=R/k,\qquad a'=(p+R')/4,
\]

with the same `p,u,c`.

## Independent derivation of the congruence and descent

Since `u|a^2`, one has `K(u)|a`, hence

\[
 p+R=4a\equiv0\pmod m.
\]

Every prime dividing `u` divides `a`; because `gcd(a,R)=1`, both `R` and every
divisor `k|R` are units modulo `m`.  Also `p` is a unit modulo `m`.  Therefore

\[
 p+R/k\equiv0\pmod m
 \iff pk+R\equiv0\pmod m
 \iff p(k-1)\equiv0\pmod m
 \iff k\equiv1\pmod m.
\]

Independently, the new full residual gate is `R/k|G_c`.  Prime by prime this is
equivalent to `d|k`, because the exponent of `d` at a prime is the excess of
the exponent in `R` over that in `G_c`.  Thus the displayed deletion domain is
both necessary and sufficient.

For a proper source, `d>1`, so every `k` in the domain satisfies `k>1`.  Hence

\[
 R'=R/k<R,
 \qquad
 a'=(p+R')/4<(p+R)/4=a.
\]

Moreover `k≡1 (mod 4)` and `R≡3 (mod 4)`, so `R'≡3 (mod 4)`; consequently
`R'≥3`, `p/4<a'<p/2`, and the target remains in the required range.  This
audits strict descent without using a numerical approximation.

## Independent derivation of the nine words

The automatic candidate is

\[
 q_0=K(d),\qquad k=q_0^2.
\]

From `d^2|R`, valuation comparison gives `q_0^2|R` and `d|q_0^2`.  Since
`gcd(R,m)=1`, `q_0` is a unit modulo `m`.  Thus this candidate belongs to the
deletion domain for every proper source exactly when every square of a unit
modulo `m` equals one.

For `m=4K(u)`, the square image is trivial exactly for

\[
 m\mid24
 \iff K(u)\mid6
 \iff u\mid36.
\]

The corresponding words are exactly

\[
 1,2,3,4,6,9,12,18,36.
\]

No gap was found in this equivalence.  In particular, `d>1` forces
`K(d)^2>1`, so the automatic map is always a strict descent rather than an
identity map.

## Exact computational challenge

The independent checker is `bruteforce_nine_words.py`.  It imports no supplied
verification code.  All divisions and Egyptian-fraction identities use Python
integers and `fractions.Fraction`.

The strongest completed run is
`report_p5000_u200_safe50000.json`:

- Every defining source with `p≤5000` and `u≤200` was enumerated directly by
  scanning `p,R,u,c`.  This produced 4,410 proper sources: 2,056 E sources and
  2,354 M sources.
- For every source, the checker compared the formula for `mathcal K` with a
  second enumeration performed entirely in target coordinates.  It then
  checked the target range, word budget, full gate, positive integral
  denominators, Egyptian-fraction identity, and strict decrease.  There were
  zero failures.
- Those records included 1,309 safe-word sources.  Every one contained the
  predicted deletion `K(d)^2`.
- A second exhaustive enumeration used the logically independent fact
  `R|G_c^2`: it enumerated every divisor `R` of `G_c^2` for every safe word and
  every prime `p≤50000`.  It found 17,635 proper sources (1,920 E and 15,715 M),
  with zero failures of the automatic deletion or the exact target-domain
  comparison.
- The unit-square image was computed for every `1≤u≤5000`.  Its image was
  `{1}` exactly for `u|36`; there were zero classification failures.
- Among `1≤u≤200`, the direct source scan found no-return witnesses for 124
  nonautomatic words.  These are expected witnesses for the negative direction,
  not counterexamples to the theorem.
- The source's CRT/Dirichlet construction was independently instantiated for
  every nonautomatic `u≤40`, giving 31 exact proper M sources.  In each case the
  generated `p` is prime, `p≡1 (mod 840)`, `d=t>1`, the formula deletion domain
  is empty, and the independently enumerated target domain is empty.

Representative small no-return witnesses found without the CRT construction
include

\[
 (p,a,R,u,c,d,m)=(313,85,27,5,M,3,20),
\]

\[
 (229,64,27,8,M,3,16),
\]

and

\[
 (61,22,27,11,E,3,44).
\]

For the first record, for example, the only divisors of `R=27` divisible by
`d=3` are `3,9,27`, and none is one modulo `20`.  Nevertheless
`27|(313+20)^2`, so it is a genuine proper M trace source with no same-word
return.

Reproducibility signatures from the strongest completed run are:

- direct source enumeration:
  `8355cec3c7d4f7343485fa812633b4c1c6c512902c002f2ab897deeae6176fa9`;
- safe gate exhaustion:
  `277f123be4447ea01c3a2861188573167c305972ad39c106355cc6eced038b55`;
- square-image rows:
  `a71a6e7ce982434574b7259220cc62cbce5aad84632430b082c399ad3d8268bb`.

## Determination

No counterexample was found in either direction.  The congruence equivalence,
the exact nine-word classification, and strict descent all survive the
independent derivation and the completed bounded searches.  The attempt to
extend exact trial-division construction beyond `u≤40` was stopped after two
minutes because some CRT progressions produce very large candidate primes; it
does not weaken the completed universal symbolic argument or the 31 exact
constructed cases.

