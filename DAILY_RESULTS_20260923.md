# Dated proof bulletin — 23 September 2026

This bulletin indexes the source-level structural results proved and checked on
23 September.  It is a mathematical index, not a programme chronology.  Each
entry gives the exact domain, conclusion, proof locator and boundary of the
claim.  Finite enumerations appear only when they certify sharpness or refute a
proposed universal invariant; their size is not evidence for arbitrary-prime
occupancy.

Throughout the first nine entries, let (p\equiv1\pmod4) be prime, let
(p/4<a<p/2), put (R=4a-p), and let (u\mid a^2).  With

\[
 g=\gcd(a,u),\qquad h=\frac{g^2}{u},\qquad
 r=\frac ug,\qquad s=\frac ag,
\]

one has (a=hrs), (u=hr^2), and (\gcd(r,s)=1).  The original labelled
channels are retained as

\[
 E:(a,hs\kappa,phr\kappa),\quad \kappa=\frac{pr+s}{R},
 \qquad
 M:(a,phs\lambda,phr\lambda),\quad \lambda=\frac{r+s}{R}.
\]

Write

\[
 K=\prod_{\ell^\nu\parallel R}\ell^{\lceil\nu/2\rceil},
 \qquad D=\frac RK.
\]

Then (R=KD), (D\mid K), and (K\mathbf Z/R\mathbf Z) has square zero.

## SZ-20260923-001 — exact affine E/M channel operator

The same divisor (u) is trace-admissible in both labelled channels exactly
when

\[
 K\mid(4u+1),\qquad K\mid(p-1).
\]

On this locus the full fine coordinates are

\[
 c_E\equiv\frac{4u+1}{K},\qquad
 c_M\equiv p^{-1}\frac{p+4u}{K}\pmod D,
 \qquad
 c_E=c_M-\omega,quad \omega=\frac{p-1}{K}\pmod D.
\]

For any retained coefficient vector (C=(C_x)_{x\in\mathbf Z/D}), the two
labelled channels therefore give

\[
 J=(I+T_\omega)C,qquad J_x=C_x+C_{x-\omega}.
\]

If (d=\gcd(D,\omega)) and (L=D/d), then (L) is odd and

\[
 2C_x=\sum_{j=0}^{L-1}(-1)^jJ_{x-j\omega}.
\]

The integral sequence

\[
0\longrightarrow\mathbf Z^{\mathbf Z/D}
\xrightarrow{I+T_\omega}\mathbf Z^{\mathbf Z/D}
\longrightarrow(\mathbf Z/2\mathbf Z)^d\longrightarrow0
\]

is exact, where the last map is the parity of the sum on each translation
orbit.  Thus pairing loses no rational coefficient data and is not a
positivity-producing average.

- **Proof:** [common-trace law, inverse, cokernel and support criterion](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6125e74b1aadb860965964e2ae3587c902dbbab8/research/incoming/es-turn07-mixed-order-upward-20260923/core.tex#L101-L237).
- **Strengthens:** the separate square-zero channel laws in SZ-20260923-008 by computing their exact common locus and labelled sum.
- **Nonclaim:** the theorem does not produce a common trace at an arbitrary prime.

## SZ-20260923-002 — partial-chain quotient criterion and sharp obstruction

Let (C_x) count the original bounded exponent words with fine sum (x\pmod
D).  Choose a strict gcd chain

\[
g_0=D,qquad g_j=\gcd(g_{j-1},\lambda_{i_j}),qquad
m_j=\frac{g_{j-1}}{g_j},qquad g_k=g,
\]

with each selected interval of length at least (m_j), and put

\[
B=\prod_{j=1}^k\left\lfloor\frac{N_{i_j}}{m_j}\right\rfloor.
\]

If (Q_y) counts the residual unselected words modulo (g), then every
terminal interval is retained by integers (E_x\ge0) and

\[
C_x=BQ_{x\bmod g}+E_x.
\]

Equality holds when every selected length is divisible by its radix.  With
(\delta=\omega\bmod g), the complete-block subsource covers every paired
target exactly when

\[
\operatorname{supp}(Q)\cup
\bigl(\operatorname{supp}(Q)+\delta\bigr)=\mathbf Z/g.
\]

For odd (g), if (e=\gcd(g,\delta)), this forces the sharp support bound

\[
|\operatorname{supp}(Q)|\ge\frac{g+e}{2}.
\]

If all residual steps lie in a proper subgroup, the two labelled channels meet
at most two of at least three quotient cosets, so this certificate cannot
close.

- **Proof:** [partial-chain decomposition, support cover and no-go theorem](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6125e74b1aadb860965964e2ae3587c902dbbab8/research/incoming/es-turn07-mixed-order-upward-20260923/core.tex#L281-L395).
- **Strengthens:** a full chain to (1) may be replaced by a partial chain precisely when the surviving quotient support satisfies the displayed cover.
- **Nonclaim:** a large coefficient total or generated subgroup does not imply this cover.

## SZ-20260923-003 — mixed-order bounded section with exact decoder

If the preceding gcd chain reaches (g_k=1), every fine coefficient satisfies

\[
C_x\ge
\left(\prod_{i\notin I}N_i\right)
\prod_{j=1}^k\left\lfloor\frac{N_{i_j}}{m_j}\right\rfloor.
\]

The proof supplies an integer reverse decoder through the successive quotients
(g_{j-1}\mathbf Z/D\to g_j\mathbf Z/D), retains cyclic carry, and gives
equality at the exact radix lengths.

- **Proof:** [mixed-order theorem, radix bijection and reverse decoder](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6125e74b1aadb860965964e2ae3587c902dbbab8/research/incoming/es-turn07-mixed-order-upward-20260923/core.tex#L238-L280).
- **Human lineage:** the original ES coordinates descend from Elsholtz–Tao and Yamamoto, cited below; the cyclic quotient decoder is proved in full in the linked source.
- **Nonclaim:** reaching the generated subgroup without the actual bounded radix lengths is insufficient.

## SZ-20260923-004 — exact divisor-DAG optimizer

Among certificates of the preceding strict-chain form, dynamic programming on
the divisor DAG of (D) finds the maximum displayed lower bound.  There are at
most (n\tau(D)) candidate labelled edges, and the retained predecessor data
reconstruct the optimizing chain and its integer section.

- **Proof:** [divisor-DAG proposition and reconstruction](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6125e74b1aadb860965964e2ae3587c902dbbab8/research/incoming/es-turn07-mixed-order-upward-20260923/core.tex#L396-L430).
- **Certificate:** [independent exhaustive comparison](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6125e74b1aadb860965964e2ae3587c902dbbab8/research/incoming/es-turn07-mixed-order-upward-20260923/check_independent.py).
- **Nonclaim:** failure of this optimizer is only failure of the stated chain-certificate class.

## SZ-20260923-005 — arithmetic realizations and sharp last-capacity boundary

The (D=9) and (D=15) original hard-prime packets realize positive uniform
coefficients while the earlier single-unit-width criterion fails; the
(D=15) selected chain uses two nonunit steps.  More generally, for every odd
(D>1) and strict chain ending at (1), removing one digit from the last
radix yields actual packets with coefficient (0) on
(H_m=m\mathbf Z/D) and coefficient (1) on its complement, with stabilizer
exactly (H_m).  This proves the last-capacity hypothesis sharp.

- **Proof:** [original packets and arbitrary odd-defect sharpness](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6125e74b1aadb860965964e2ae3587c902dbbab8/research/incoming/es-turn07-mixed-order-upward-20260923/core.tex#L431-L605).
- **Prime supply:** reducedness is proved before applying Dirichlet's theorem; the cited source is Sutherland, Theorem 18.1, below.
- **Nonclaim:** the finite realization is sharpness evidence for the theorem, not progress by census size and not an ES counterexample.

## SZ-20260923-006 — complete plus-factor fibre

Put (C=R+s).  The invariant

\[
M=p+C=4a+s
\]

is retained exactly.  At fixed (p,C), every labelled cell is recovered from
a divisor (s\mid C), with

\[
a=\frac{p+C-s}{4},\qquad R=C-s,
\]

together with the stated congruence, positivity, coprimality, divisor and
channel gates.  The linked theorem gives the inverse, kernels, first-denominator
displacement and the complete incoming trace fibre.

- **Proof:** [plus-factor cells, inverse and incoming fibre](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6125e74b1aadb860965964e2ae3587c902dbbab8/research/incoming/es-turn07-mixed-order-upward-20260923/core.tex#L606-L705).
- **Nonclaim:** an empty fixed-(C) fibre obstructs this map only; it is not an empty ES source box.

## SZ-20260923-007 — controlled upward return across the (p=67369) obstruction

The proper middle trace

\[
(p,a,R,u,h,r,s)=(67369,16849,27,4067,83,7,29)
\]

maps to the full exterior state

\[
(a',R',u',h',r',s',\kappa')=(16850,31,674,674,1,25,2174),
\]

with ordered denominators

\[
(16850,36631900,98714178844).
\]

The same formulas hold whenever (h=83+4650k) and
(p=67369+3775800k) is prime, with source
((203h,27,49h,h,7,29)) and target
(a'=203h+1), (R'=31), (u'=h'=(203h+1)/25), (s'=25).

- **Proof:** [exact upward family and original-gate verification](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6125e74b1aadb860965964e2ae3587c902dbbab8/research/incoming/es-turn07-mixed-order-upward-20260923/core.tex#L706-L786).
- **Strengthens:** it crosses the nonincreasing-(a) obstruction SZ-20260923-014 by changing the retained invariant.
- **Nonclaim:** the progression supplies a typed infinite family conditional only on primality of its displayed reduced class; it is not a terminating map from every trace.

## SZ-20260923-008 — square-zero trace defect and mixed exponent law

For each actual exponent part, the exact trace defect lies in the square-zero
ideal (K\mathbf Z/R\mathbf Z).  The complete integer-exponent formula retains
the original factor, its exponent, channel label and all mixed terms; reduction
to the additive fine coordinate is proved rather than substituted for the
original object.

- **Proof:** [complete source, defect and mixed law](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6c064a07298cdba38352998364ce6b7cb3efa973/research/incoming/es-turn07-square-zero-pell-20260922/core.tex#L33-L238).
- **Module alias:** `SZP-01`.
- **Nonclaim:** no initial trace-source existence follows.

## SZ-20260923-009 — complete bounded coefficient partition and sharp unit width

The full original exponent box is partitioned by finite geometric coefficient
polynomials.  Stabilizers are calculated exactly.  If an actual unit direction
has width at least (D-1), every coefficient is positive with the displayed
integer lower count; the threshold is sharp.

- **Proof:** [coefficient partition, saturation and stabilizers](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6c064a07298cdba38352998364ce6b7cb3efa973/research/incoming/es-turn07-square-zero-pell-20260922/core.tex#L239-L339).
- **Module alias:** `SZP-02`.
- **Nonclaim:** generated-subgroup support without the bounded width condition is insufficient.

## SZ-20260923-010 — prime-power and prime-square channel classification

For (a=q^e), the middle trace exponents are classified by the original gates.
For (a=q^2), both channel orientations and every trace word are classified
without replacing the divisor box by a subgroup surrogate.

- **Proof:** [prime-power and complete prime-square classification](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6c064a07298cdba38352998364ce6b7cb3efa973/research/incoming/es-turn07-square-zero-pell-20260922/core.tex#L340-L404).
- **Module alias:** `SZP-03`.
- **Nonclaim:** the classification does not supply a carrier prime at an arbitrary input.

## SZ-20260923-011 — terminality for both inherited deletion systems

Every proper middle trace at (a=q^2) has both original full gates empty at
that shell and no return under either inherited residual-divisor deletion
system.  The proof retains every residual divisor and both channel domains.

- **Proof:** [prime-square terminality theorem](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6c064a07298cdba38352998364ce6b7cb3efa973/research/incoming/es-turn07-square-zero-pell-20260922/core.tex#L405-L430).
- **Module alias:** `SZP-04`.
- **Nonclaim:** terminality for these two maps says nothing about other maps or the truth of ES.

## SZ-20260923-012 — complete factor-sum return and inverse

Retaining the raw factor sum (h+s), the source-to-target displacement is the
integer-root condition for the displayed quadratic in the proof.  Positivity,
primitive gcd reduction, target denominators, and the complete incoming fibre
over a marked full middle target are all biconditional.

- **Proof:** [factor-sum theorem, quadratic gate and inverse](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6c064a07298cdba38352998364ce6b7cb3efa973/research/incoming/es-turn07-square-zero-pell-20260922/core.tex#L431-L544).
- **Module alias:** `SZP-05`.
- **Nonclaim:** the quadratic root is tested exactly; its existence is not assumed for every trace.

## SZ-20260923-013 — Pell specialization

On the prime-square word (r=1,h=s=q), the factor-sum quadratic becomes the
displayed Pell equation.  Its recurrence, source and target maps, positivity
and isolated hard-prime examples are proved with every old and new word and ray
retained.

- **Proof:** [Pell equation, recurrence and exact returns](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6c064a07298cdba38352998364ce6b7cb3efa973/research/incoming/es-turn07-square-zero-pell-20260922/core.tex#L545-L615).
- **Module alias:** `SZP-06`.
- **Nonclaim:** infinitely many integer Pell points do not prove infinitely many prime values.

## SZ-20260923-014 — least obstruction to nonincreasing trace repair

Among primes (p\equiv1\pmod {24}), (p=67369) is the least input for which
the first rational trace precedes every original full gate.  Hence no universal
repair from every trace can require the distinguished denominator (a) to
decrease or remain fixed.

- **Proof:** [finite least-example theorem with complete prefix certificate](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6c064a07298cdba38352998364ce6b7cb3efa973/research/incoming/es-turn07-square-zero-pell-20260922/core.tex#L990-L1095).
- **Module alias:** `SZP-07`.
- **Nonclaim:** this refutes a proposed termination invariant, not ES; its finite range is used only to prove leastness.

## SZ-20260923-015 — exact fixed-tail-sum fibre

At fixed odd prime (p) and numerical tail sum (N=Y+Z), ordered positive
integral targets are in bijection with residual divisors (\rho\mid N)
satisfying the exact discriminant-square, positivity and parity gates.  The
inverse is explicit.  Splitting (\rho) into its squarefree and square parts
gives a Pell lattice together with the indispensable divisibility gates.

- **Proof:** [fixed-sum bijection, inverse and Pell lattice](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6c064a07298cdba38352998364ce6b7cb3efa973/research/incoming/es-turn07-square-zero-pell-20260922/core.tex#L616-L721).
- **Module alias:** `SZP-08`.
- **Nonclaim:** an unrestricted Pell point need not satisfy the integer-tail gates, and an empty fixed-sum fibre does not obstruct maps that change (N).

## SZ-20260923-016 — prime-square fixed-sum divisor obstruction

For every proper prime-square E or M trace with word (q) or (q^3), every
target word, both channels and both tail orders, no integral target retaining
the same numerical tail sum can have residual a proper divisor of the source
residual.  The proof is a four-case universal argument.

- **Proof:** [all-word, both-channel obstruction theorem](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6c064a07298cdba38352998364ce6b7cb3efa973/research/incoming/es-turn07-square-zero-pell-20260922/core.tex#L722-L989).
- **Module alias:** `SZP-09`.
- **Nonclaim:** a smaller residual not dividing the source residual, or a map changing the numerical tail sum, remains outside this theorem.

## Human mathematical lineage

- Christian Elsholtz and Terence Tao, [*Counting the number of solutions to the Erdős–Straus equation on unit fractions*, Section 2, Propositions 2.2 and 2.6](https://arxiv.org/abs/1107.1010), supply the Type-I/II coordinate lineage.  The modules preserve the [author TeX and read locators](research/incoming/es-turn07-square-zero-pell-20260922/source_reading.json).
- K. Yamamoto, [*On the Diophantine equation (4/n=1/x+1/y+1/z)*, Lemma 2, equation (4), printed page 38](https://www.jstage.jst.go.jp/article/kyushumfs/19/1/19_1_37/_pdf), supplies the inherited exterior congruence context.
- Miguel Angel Lopez, [*A Complete Congruence System for the Erdős–Straus Conjecture*](https://arxiv.org/abs/2404.01508), is cited for the hard residue class and solution-form context; no theorem above assumes its proposed coverage system.
- Andrew V. Sutherland, [*Dirichlet L-functions, primes in arithmetic progressions*, Theorem 18.1](https://math.mit.edu/classes/18.785/2017fa/LectureNotes18.pdf#page=1), is used only after each arithmetic progression is proved reduced.

The original formulas, exact hypotheses, complete proofs, figures, executable
certificates, source hashes and integration boundaries are retained in the two
linked standalone modules.  The next structural obligation is to prove a
quotient-support cover or construct a different source-changing morphism at
every hard prime; enlarging a finite census does not discharge it.
