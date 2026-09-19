# Erdős–Straus proof bulletin — 19 September 2026

This is a dated index of proved mathematical results with stable locators. It
is **not** a programme timeline or a reconstruction of task chronology.

## SZ-20260919-001 — complete middle two-chart atlas

For every original oriented middle state at a prime \(p\equiv1\pmod4\), the
least exact middle cofactor obeys the sharp square-root bound proved in the
source, and the state belongs to exactly one of two disjoint charts: a direct
chart and a cofactor chart. Both charts retain the original positive divisor,
congruence, range, orientation, ordered denominator return, and inverse map.

- **Proof:** [middle core.tex](research/incoming/es-turn07-middle-cutoff-20260919/core.tex)
- **Reader:** [middle atlas](research/incoming/es-turn07-middle-cutoff-20260919/README.md)
- **Human literature:** Christian Elsholtz and Terence Tao, “Counting the
  number of solutions to the Erdős–Straus equation on unit fractions,”
  *J. Aust. Math. Soc.* 94 (2013), §2, especially Proposition 2.6
  ([arXiv:1107.1010](https://arxiv.org/abs/1107.1010)).
- **Strengthens:** the Turn 6 pointwise localization by replacing the complete
  middle source search with two proved finite inverse charts.
- **Does not prove:** universal middle occupancy or the Erdős–Straus
  conjecture.

## SZ-20260919-002 — corrected positive-divisor semantics and checker boundary

The middle atlas and its executable replay retain only positive source
divisors, preserve the original orientation, and distinguish a complete finite
atlas from a witness-guaranteed selector. Normal and optimized verifier runs are
made byte-stable, and the independent checker reconstructs the original source
without importing the main verifier.

- **Proof and corrections:** [middle package](research/incoming/es-turn07-middle-cutoff-20260919/)
- **Strengthens/corrects:** SZ-20260919-001 by fixing the executable domain and
  its public nonclaim; no theorem is inferred merely from a checker exit code.
- **Does not prove:** whole-history verification, Lean completion, or
  nonemptiness at every prime.

## SZ-20260919-003 — strict exterior cubic cutoff

For every positive first-half exterior source state with
\(p\equiv1\pmod4\), retain

$$
R=4a-p,\qquad D=\frac{4u+1}{R},\qquad v=\frac{a^2}{u},
\qquad w=\min\{R,D,v\}.
$$

Then

$$
\boxed{(p+w)^2>4(w+1)^2(w-1).}
$$

If \(C(p)\) is the largest positive integer satisfying this inequality, then

$$
1\le C(p)<p,\qquad
w\le C(p),\qquad
C(p)=\left(\frac p2\right)^{2/3}+O(p^{1/3}).
$$

The residue hypothesis is exact: the positive state
\((19,6,6,5,5,6,5)\) gives equality after \(p\equiv1\pmod4\) is removed.

- **Proof:** [exterior core.tex](research/incoming/es-turn07b-exterior-atlas-20260919/core.tex),
  “A strict cubic cutoff.”
- **Reader:** [exterior atlas](research/incoming/es-turn07b-exterior-atlas-20260919/README.md)
- **Human literature:** the source normalization is compared with the classical
  Type I parametrization in Elsholtz–Tao, §2, Proposition 2.2, and with
  M. Bello-Hernández, M. Benito, and E. Fernández, “A Divisor Parametrization
  for the Erdős–Straus Conjecture,” §3
  ([arXiv:2606.10922](https://arxiv.org/abs/2606.10922)).
- **Strengthens:** Turn 6 exterior localization by proving a uniform finite
  outer cutoff while retaining three distinct exact coordinates.
- **Does not prove:** an exterior state exists at every prime.

## SZ-20260919-004 — complete exterior three-chart atlas

For prime \(p\equiv1\pmod4\), every original exterior state belongs to exactly
one of:

1. the direct chart \(R\le C(p)\);
2. the reciprocal chart \(D\le C(p)\);
3. the complement–norm chart \(v\le C(p)\).

All three maps have proved inverses to the complete marked source. The norm
chart retains

$$
R\mid p^2+4v,\qquad
R\equiv-p\pmod{4K(v)},\qquad
K(v)=\prod_{\ell^e\parallel v}\ell^{\lceil e/2\rceil},
$$

so the original requirement \(v\mid a^2\) is not discarded. The tie rule is
exact: \(R=D<v\) is direct, while \(v<R=D\) is norm. Composite examples
\(p=21,93,25\) isolate where primality enters the three generative converses.

- **Proof:** [exterior core.tex](research/incoming/es-turn07b-exterior-atlas-20260919/core.tex),
  “Three disjoint charts with complete inverses.”
- **Typed-map index:** [MORPHISMS.md](research/incoming/es-turn07b-exterior-atlas-20260919/MORPHISMS.md)
- **Strengthens:** SZ-20260919-003 from a least-parameter inequality to an exact
  finite atlas with reconstruction.
- **Corrects:** the false shortcuts \(\gcd(v,D)=1\), “all \(R=D\) states are
  direct,” and “norm divisibility alone supplies a source state.”
- **Does not prove:** that any of the three charts is occupied for a prescribed
  prime.

## SZ-20260919-005 — exterior/middle separation and exact sharp family

At the prime \(p=48049\), the original exterior state

$$
(a,u,R,D,v,h,r,s,\kappa)
=(12090,24180,311,311,6045,6045,2,1,309)
$$

has \(R=D=311\), exceeding the preceding middle cutoff \(247\). Therefore the
middle square-root cutoff cannot be transferred unchanged to the exterior
cofactors.

For every \(n\ge2\), the integer source family

$$
p=16n^3-4n^2-8n+1,\qquad
R=D=4n^2-1,\qquad
C(p)=4n^2-2
$$

attains the exterior cutoff exactly. Its complete residue classification is

$$
p(n)\equiv289\pmod{840}
\Longleftrightarrow
n\equiv24\ \text{or}\ 164\pmod{210}.
$$

This is integer-domain sharpness and a congruence classification; it is not a
claim of infinitely many prime values. At \(p=2521\), the \(v=11\) norm lane is
provably empty, with the remaining factor \(141233\) certified prime by the
recorded Lucas data.

- **Proof:** [exterior core.tex](research/incoming/es-turn07b-exterior-atlas-20260919/core.tex),
  “An actual hard prime and an asymptotically extremal integer family.”
- **Certificates:** [certificate directory](research/incoming/es-turn07b-exterior-atlas-20260919/certificates/)
- **Strengthens/corrects:** the attempted middle-to-exterior cutoff transfer by
  giving its exact counterexample and the strongest proved replacement.
- **Does not prove:** universal exterior or middle occupancy, an infinite prime
  subfamily, or the Erdős–Straus conjecture.

## SZ-20260919-006 — exact ordered marked cubic and source inverse

Every original first-half exterior state at a prime \(p\equiv1\pmod8\) defines

$$
X=v=\frac{a^2}{u},\quad Y=2a,\quad
\alpha=v-R,\quad\beta=v-D,\quad B=\alpha\beta-1
$$

and lies on the ordered marked cubic

$$
Y^2=X^3-(\alpha+\beta)X^2+BX.
$$

The complete source inverse is

$$
R=X-\alpha,\quad D=X-\beta,\quad a=Y/2,\quad
p=2Y-R,\quad u=(RD-1)/4,
$$

with the stated positivity, parity, residue and primality image conditions.
At fixed \(p\), the additional line is \(2Y=p+X-\alpha\), so a fixed shape has
at most three original source states. The Weierstrass discriminant is

$$
16B^2\bigl((\alpha-\beta)^2+4\bigr),
$$

and the original grade obeys

$$
h\mid B,\qquad p\equiv\alpha\pmod h,\qquad p\beta\equiv1\pmod h.
$$

- **Proof:** [shape-rigidity core](research/incoming/es-turn07-shape-rigidity-20260919/core.tex),
  “Original source and the marked cubic” and “Original character constraints.”
- **Typed inverse:** [MORPHISMS.md](research/incoming/es-turn07-shape-rigidity-20260919/MORPHISMS.md)
- **Human literature:** the inherited Type-I/II source coordinates are traced
  to Elsholtz–Tao, §2, Propositions 2.2 and 2.6; quadratic reciprocity is cited
  to Hatcher, *Topology of Numbers*, §6.4.
- **Strengthens:** SZ-20260919-004 by retaining a second exact geometric
  coordinate system on every exterior chart state.
- **Does not prove:** an integral point exists on the required fixed-prime line.

## SZ-20260919-007 — every diagonal exterior state has a middle return

For an actual exterior state with \(R=D\), write

$$
\frac{R-1}{2}=\delta t^2
$$

with \(\delta\) the positive squarefree part and \(t>0\) odd. Then
\(\delta\equiv3\pmod4\), \(\delta\mid p+1\), and \(\delta<R\). With
\(c=(p+1)/\delta\) and \(j=(\delta+1)/4\), the exact original middle state is

$$
(h_M,r_M,s_M,\lambda_M)=(j,1,c,1),\quad
a_M=jc,\quad u_M=j,\quad R_M=c+1,\quad Q_M=\delta.
$$

It returns the ordered denominators \((jc,pjc,pj)\), and
\(\min(R_M,Q_M)<R\). The inverse fibre retains the positive odd integer \(t\),
so this is a typed map rather than an identification of the E and M channels.

- **Proof:** [shape-rigidity core](research/incoming/es-turn07-shape-rigidity-20260919/core.tex),
  “Every diagonal exterior source has an actual middle return.”
- **Independent derivation:** [integration receipt](research/incoming/es-turn07-shape-rigidity-20260919/integration_verification.json)
- **Strengthens/corrects:** SZ-20260919-005 by showing that its diagonal sharp
  family, and every other occupied diagonal exterior fibre, already carries a
  same-prime middle witness.
- **Does not prove:** that a diagonal exterior state exists at every hard prime.

## SZ-20260919-008 — hard-prime shape rigidity through radius eight

Here a hard prime means
\(p\bmod 840\in\{1,121,169,289,361,529\}\).
If a hard-prime exterior state satisfies
\(\max(|v-R|,|v-D|)\le7\), then it is exactly the singular family

$$
h=4n^2-2,\quad r=n,\quad s=1,\quad R=D=4n^2-1,
$$

$$
p=16n^3-4n^2-8n+1,\qquad n\ge2\text{ even}.
$$

At the same \((p,a,R)\), it has the two original middle orientations
\(u_M=n\) and \(u'_M=n(4n^2-2)^2\), returning \((a,pa,pn)\) up to the retained
last-two-denominator orientation. At radius eight the sole possible
nonsingular ordered shape is

$$
(\alpha,\beta,h)=(8,-4,11),\qquad
4r^2=11s^4-4s^2-3.
$$

Its grade congruence gives the original middle state

$$
(h_M,r_M,s_M,\lambda_M)=\left(1,3,\frac{p+3}{11},1\right),qquad u_M=9,
$$

without classifying the quartic’s integral points. Any hard source in this
radius-eight branch must in fact have \(p\bmod 840\in\{1,121\}\).

- **Proof:** [shape-rigidity core](research/incoming/es-turn07-shape-rigidity-20260919/core.tex),
  “Complete hard-prime rigidity at shape radius seven” and “The first possible
  nonsingular shape at radius eight.”
- **Certificates and strengthened independent replay:** [certificate directory](research/incoming/es-turn07-shape-rigidity-20260919/certificates/)
  and [independent checker](research/incoming/es-turn07-shape-rigidity-20260919/check_independent.py).
- **Strengthens:** SZ-20260919-005 from one sharp family to a complete
  low-shape branch classification and witness-preserving removal.
- **Does not prove:** that the radius-eight quartic has a hard-prime exterior
  point, that no such point exists, or that every remaining shape is bounded.

## SZ-20260919-009 — exact cubic involution and fixed-prime obstruction

For \(B\ne0\), the marked cubic has the rational involution

$$
\Psi(X,Y)=\left(\frac BX,\frac{BY}{X^2}\right).
$$

An integral image of an original positive state forces \(s\mid2\). The case
\(s=2\) loses evenness of \(Y\). For \(s=1\), all reconstructed coordinates are
explicit, but \(R',D'\equiv1\pmod4\), \(p'\equiv3\pmod4\), and

$$
p'-p=(4r-1)(4r^2-R-D)\ne0.
$$

Thus this is an exact correspondence of marked cubics, not a fixed-prime
selector. The displayed \(p'=5951\) image is a composite parameter record,
not a prime source.

- **Proof:** [shape-rigidity core](research/incoming/es-turn07-shape-rigidity-20260919/core.tex),
  “A natural cubic involution fails the required fixed-prime return.”
- **Strengthens/corrects:** the attempted involutive descent by proving the
  strongest actual coordinate transport and its exact obstruction.
- **Does not prove:** that other maps between the residue classes do not exist.

## Current proved frontier

SZ-20260919-001 through SZ-20260919-009 give complete finite inverse atlases for
every existing original middle or exterior state at a fixed prime and remove
the diagonal and hard-prime radius-at-most-eight exterior branches by actual
middle returns. The remaining statement is structural nonvanishing outside
those removed branches:

$$
\forall p\ \text{in the unresolved prime class},\qquad
\#E_p+\#M_p>0.
$$

No result in this bulletin assumes that statement or presents localization as
its proof.
