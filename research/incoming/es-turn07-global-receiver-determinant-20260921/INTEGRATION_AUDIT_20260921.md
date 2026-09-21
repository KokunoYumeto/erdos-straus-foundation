# Integration audit — global literal-receiver determinant

Date: 21 September 2026
Additive repository path:
`research/incoming/es-turn07-global-receiver-determinant-20260921/`
Proof-source checkpoint:
[`6bdfce25724b95a4b30e97f0df69879a87793302`](https://github.com/KokunoYumeto/erdos-straus-foundation/commit/6bdfce25724b95a4b30e97f0df69879a87793302)

## Received material and identity

The supplied cumulative archive is preserved without modification at
`received/ES_Turns6_7_With_Global_Receiver_Determinant_20260921.zip`:

```text
bytes   18,205,125
sha256  ba225dc9f046b1d359dfb16cb5e62d83312cda978e84b79dd2b6b78ccba60d6e
```

The accompanying handoff is preserved at `received/USER_HANDOFF.txt`:

```text
bytes   20,153
sha256  88e2b9bc3b16a1a92448742c1228c2c35da56803218a57779fcce8df8a6682c7
```

The outer archive contained a preserved predecessor archive with SHA-256
`8e3527bbecb8658021d10f94b49ac98ee202bbca755b5bfb8c750b61606b6481`
and the current inner archive with SHA-256
`99592eb9a649bdadb6c58add9e01b10d4558209883b38c43474dd3107aaca620`.
Every one of the current inner manifest's 48 entries was independently hashed;
all 48 byte counts and SHA-256 values matched.  The received manifest is kept
as `received/CURRENT_INNER_MANIFEST.json`; it is distinct from the final
integrated manifest.

## Literature read and used

The human-source coordinate antecedent is Christian Elsholtz and Terence Tao,
*Counting the number of solutions to the Erdős–Straus equation on unit
fractions*, arXiv:1107.1010v6, Section 2, Propositions 2.2 and 2.6.  The
original author TeX is preserved at
`literature/Elsholtz_Tao_2013_arxiv_1107.1010v6/egyptian-count18.tex`, SHA-256
`b0469a67a737b7f4e77778310c87e22f5783ae9704f70aa55919a4a40104611c`.
Lines 487–625 were read at content level: both Type I/II varieties, their maps,
hypotheses and the proofs of Propositions 2.2 and 2.6.

The direct programme antecedents were also read rather than inferred from
titles:

- the [original odd receiver, determinant polynomial and ES pullback](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/49976b17491ba927df8bc7f2c2f81d39dfb15ce8/research/incoming/es-fable-zeta-bridge-20260920/ODD_RECEIVER_ES_PULLBACK.tex#L19-L215);
- the [three-character sufficient theorem](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/49976b17491ba927df8bc7f2c2f81d39dfb15ce8/research/incoming/es-rh-continuation-b-20260920/RESEARCH_CONTINUATION.md#L44-L254);
- the [current original-divisor occupancy boundary](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/1400e6301429cf9c66d8071e107be9dc41f5b907/research/incoming/es-turn07-divisor-descent-20260921/core.tex#L1-L16).

`source_reading.json` records the exact versions, hashes, line ranges and use.
No historical-priority conclusion is drawn from the bounded search.

## Mathematical result accepted after rederivation

For every prime \(p\equiv1\pmod {12}\) and every positive integral witness

\[
\frac4p=\frac1x+\frac1y+\frac1z,
\]

retain \(\ell=(p,x,y,z)\), \(S=\sum_j\ell_j\),
\(H(T)=-S^{-1}\prod_j(T-\ell_j)\), and the original signed receiver \(O\).
The integrated proof establishes

\[
\mathfrak N=S^6F<-\frac{125873811}{262144}p^8<0.
\]

For \(p\equiv1\pmod {24}\), the constant improves to
\(327448292668/47045881\). With the applicable constant \(c\),

\[
|\det O|>\frac{4cp^8}{S^3},
\qquad
\|O^{-1}\|_2<\frac{360S^9}{cp^8},
\]

where the norm is the operator norm for the standard Hermitian norm on
\(\mathbb C^4\). The exact determinant phase is

\[
\epsilon=A^2\prod_{i<j}(\ell_j-\ell_i)\prod_j\xi_j\in\{1,-1\},
\qquad
\det O=-4\epsilon\mathfrak N/S^3.
\]

The proof covers the complete integral witness domain.  It proves the unique
first-half denominator, the exhaustive exterior/middle split, both ordered
inverses and gates, the exterior character bound and the middle integral gap.
The universal sign then follows from three positive 221-coefficient exterior
arrays and a middle comparison with 191 positive nonconstant coefficients.

## Repairs applied during integration

The received argument was strengthened before publication in the following
ways.

- The receiver, coefficient and evaluation matrices are typed in
  \(M_4(\mathbb C)\); the norm is typed as the standard Hermitian operator norm.
- The complete coefficient matrix is displayed, together with
  \(\det\mathsf C_H=4F/A\), \(\det U=\epsilon/A^2\), the exact phase and the
  Lagrange inverse.
- The first-half proof now displays factor positivity, the exact valuation
  alternatives, every divisibility step, both E/M assignments and the
  exhaustion of all witnesses.
- Jacobi symbols modulo composite \(R\) and Legendre symbols modulo prime \(p\)
  are distinguished explicitly.
- The middle strictness coefficients are checked, not only stated.
- The \(p\le3000\), \(p\equiv1\pmod {12}\) census domain and complete valuation
  histogram are stated exactly.
- The gate-failing value \(S^6F\) is identified as rational rather than as an
  integer numerator.
- The theorem's conditional-on-an-existing-witness scope is stated at every
  public entry point.
- Two reproducible TikZ figures show the exact arithmetic coordinate domains
  and the typed determinant/inverse mechanism.  Their final render was
  inspected after removing all overlap.

## Separate mathematical rechecks and negative controls

Four separately tasked rechecks covered the determinant algebra and inverse,
the complete arithmetic domain, both polynomial certificates, and the examples
and counterdomains.  Their consolidated calculations are in
`independent_audits/MATHEMATICAL_RECHECKS.md`.  The executable independent
checker imports neither the main verifier nor a predecessor implementation.

The strongest negative control is the exact positive-real family

\[
p=1,\qquad b=t,\qquad c=t+\frac1{10},
\qquad a=\frac{bc}{4bc-b-c},qquad3\le t\le4.
\]

Its degree-18 numerator has exactly one zero,

\[
3053/1000<t_0<1527/500,
\qquad t_0\approx3.05367681075890,
\]

while all four roots remain distinct. Its \(1/10\) tail gap excludes the
middle integral domain and both exterior words lie below the exterior cone.
The raw source \((p,a,R,u)=(1009,321,275,9)\) supplies the other necessary
control: its receiver is nonsingular but its exterior gate fails because
\(275\nmid37\). Receiver invertibility therefore does not create an integral
source.

## Reproducibility and artifact checks

The fresh command

```text
python run_all.py --bound 3000 --directory reproduced/normal
```

completed in ordinary and optimized Python.  It recorded 48,542 main checks
and 30,245 separately implemented checks per mode.  Every mathematical JSON
output was byte-identical across the two interpreter modes.  The finite census
contains 99 primes, 34,287 shells, 868,359 original divisor words, 2,451 E
states and 2,054 M states.  Its receiver-numerator valuation histogram is
((E,0):2447), ((E,1):4), ((M,2):2054).  These finite counts test the
implementations; the theorem comes from the universal algebraic identities and
coefficient certificates.

The public workbench compiled twice to nine pages, SHA-256
`84efbaefd0b15dbbe7687989fb280a898660066010c3f6e4fa14a52cf4af914c`.
The short preprint compiled twice to four pages, SHA-256
`36b7fd105548e3dcc2cce070d22f8b9511eb71556faf8b46deb0f8ee7d204584`.
Neither final log has an overfull box, undefined reference, fatal error or
other TeX warning.  All thirteen final pages were rendered to PNG and visually
inspected.  `render_receipt.json` records every final page hash.

## Scope and remaining obligation

This module proves global integral nonvanishing of the supplied odd receiver
and an explicit inverse bound.  It does not prove universal Erdős--Straus
occupancy, an RH statement, a global Jacobian-conjecture statement, a Lean
build, human peer review or historical priority.  The remaining arithmetic
obligation is still to prove that every prescribed hard prime has at least one
original integral E or M state.  `HANDOFF_TURN_7_REMAINDER.md` keeps that
boundary explicit.
