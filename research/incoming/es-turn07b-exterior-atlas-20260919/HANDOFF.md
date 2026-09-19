# Handoff: the finite source atlas is complete; occupancy is not

## What is proved

For every positive first-half exterior state

$$
R=4a-p,\qquad D=\frac{4u+1}{R},\qquad v=\frac{a^2}{u},
$$

with \(p\equiv1\pmod4\), the least retained parameter
\(w=\min\{R,D,v\}\) obeys

$$
(p+w)^2>4(w+1)^2(w-1).
$$

The resulting exact cutoff satisfies

$$
C(p)=\left(\frac p2\right)^{2/3}+O(p^{1/3}).
$$

For prime \(p\equiv1\pmod4\), every original exterior state is recovered by
exactly one of three invertible charts:

1. a direct chart with \(R\le C(p)\);
2. a reciprocal chart with \(D\le C(p)\);
3. a complement–norm chart with \(v\le C(p)\), retaining both
   \(R\mid p^2+4v\) and \(R\equiv-p\pmod{4K(v)}\).

The last congruence is equivalent to the original availability condition
\(v\mid a^2\); it cannot be dropped. The ordered denominators, inverse maps,
fibres, gcd conditions, tie rules, and primality dependencies are proved in
[core.tex](core.tex).

The family

$$
p(n)=16n^3-4n^2-8n+1,\qquad C(p(n))=4n^2-2
$$

attains the cutoff exactly on the full stated integer source domain. No
infinite prime-value assertion is made. The prime \(p=48049\) has
\(R=D=311\), above the preceding middle cutoff \(247\), so the middle
square-root bound cannot be substituted for the exterior theorem.

## What the preceding work supplies

- [Turn 6 pointwise localization](../es-turn06b-pointwise-localization-20260919/)
  supplies the retained original exterior and middle sources and the
  \(p=2521\) fixed-grade negative control.
- [Turn 7 middle atlas](../es-turn07-middle-cutoff-20260919/) proves the complete
  square-root two-chart localization of every existing middle state.
- This package supplies the complementary complete three-chart localization of
  every existing exterior state.

Together, those results give a finite decision procedure at each fixed prime.
They do not give a witness-guaranteed procedure.

## Exact remaining theorem

The current frontier is not another cutoff. It is the nonvanishing statement

$$
\forall p\ \text{in the unresolved prime class},\qquad
\#E_p+\#M_p>0,
$$

where \(E_p\) and \(M_p\) are the original exterior and middle source fibres,
with all original integrality, divisibility, range, and orientation conditions
retained.

Equivalently, one must prove that at least one of the five exact charts—three
exterior and two middle—is occupied for every such prime. An admissible finite
atlas may be empty, so its finiteness alone cannot discharge this obligation.
A proposed continuation must therefore produce one of:

- a proved nonzero coefficient in the original \(E/M\) pair sum;
- an exact transport that maps a known occupied fibre into one of the five
  charts for the prescribed prime, with domain and inverse proved;
- or a complete finite exceptional-prime theorem together with certified
  verification of the entire remaining domain.

Do not replace the obligation by assuming positivity, by selecting the smallest
permitted grade, by using \(R\mid p^2+4v\) without the \(K(v)\) gate, or by
claiming that a parameter cutoff bounds possible counterexample primes.

## Replay boundary

The two Python programs compare the original positive source with the complete
atlas through the recorded finite bound and independently re-enumerate the
primitive \(h,r,s\) source. They certify the declared bounded comparison and
literal examples. They do not constitute a Lean proof, a human review, a
historical-priority determination, or a proof of universal Erdős–Straus
occupancy.
