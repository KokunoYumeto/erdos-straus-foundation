# Independent audit: exact divisor descent

## Material read

- Outer archive: `C:\Users\Floris\Downloads\ES_Turns6_7_With_Divisor_Descent_20260921.zip`.
- Current inner archive SHA-256:
  `d5973df91e35d50edb5830a3ae3191358ada49ee8b37184fddf660d6769ec57f`.
- The audit used the extracted `core.tex`, `MORPHISMS.md`, `preprint.tex`,
  `verify.py`, and `check_independent.py`.

## Determination

The central composite-source divisor-descent theorem is correct.  Its exact
content is a correspondence, not a globally invertible map: after a source is
fixed, its admissible deletion factors are in bijection with its targets; after
only a target is fixed, all possible sources form the finite fibre written
below.  Two repairs are needed in the current exposition:

1. the phrase "the map and the numerical inverse" must be typed as a
   fixed-source inverse, because different sources can have the same target;
2. the paragraph claiming recovery of every rational integral-trace pair uses
   an unproved denominator identity where an algebraic-integer argument is
   required.

No counterexample was found or produced to the core valuation equivalence,
the deletion domain, the deletion map, or the fibre formula.

## 1. Exact source and target spaces

Fix a prime (p\equiv1\pmod 4), a channel (c\in\{E,M\}), and define

\[
 G_E(p,u)=4u+1,\qquad G_M(p,u)=p+4u.
\]

For a positive integer (u), put

\[
 K(u)=\prod_{\ell^f\parallel u}\ell^{\lceil f/2\rceil},
 \qquad m(u)=4K(u).
\]

The proper rational trace-source space in channel (c) is

\[
\begin{split}
 \mathscr S_c(p)=\{(a,R,u):\;&a,R,u\in\mathbb Z_{>0},\ R=4a-p,
 \ 3\le R<p,\ R\equiv3\pmod4,\\
 &u\mid a^2,\ R\mid G_c(p,u)^2,\ R\nmid G_c(p,u)\}.
\end{split}
\]

The full integral target space is

\[
\begin{split}
 \mathscr T_c(p)=\{(a',R',u):\;&a',R',u\in\mathbb Z_{>0},\ R'=4a'-p,
 \ 3\le R'<p,\ R'\equiv3\pmod4,\\
 &u\mid (a')^2,\ R'\mid G_c(p,u)\}.
\end{split}
\]

The inequalities on (a) and (a') are equivalently
(p/4<a,p/4<a'<p/2).  From (u\mid a^2), every prime of (u) is a prime
of (a).  Since (gcd(a,R)=gcd(p,R)=1), one has

\[
 \gcd(pR,m(u))=1,
 \qquad
 u\mid a^2\Longleftrightarrow K(u)\mid a
 \Longleftrightarrow p+R\equiv0\pmod{m(u)}.
\]

These are the precise source and target domains used below.

## 2. Common denominator and trace equivalence

For arbitrary positive integers (R,G), let

\[
 g=\gcd(R,G),\qquad d=R/g.
\]

For each prime (ell), write (e=v_\ell(R)) and (t=v_\ell(G)).  Then

\[
 v_\ell(d)=e-\min(e,t)=\max(e-t,0).
\]

Consequently

\[
 \boxed{R\mid G^2\quad\Longleftrightarrow\quad d^2\mid R.}
\]

Indeed, (R\mid G^2) is the family of inequalities (e\le2t), while
(d^2\mid R) is the family
(2\max(e-t,0)\le e).  If (t\ge e), both inequalities hold.  If (t<e),
the second inequality is exactly (e\le2t).

For an original word (u\mid a^2), the labelled rational tails are

\[
\begin{array}{ll}
 E:&Y_E=(pa+a^2/u)/R,\quad Z_E=(pa+p^2u)/R,\\[2mm]
 M:&Y_M=p(a+a^2/u)/R,\quad Z_M=p(a+u)/R.
\end{array}
\]

Every factor (p,a,u,4) is a unit modulo (R).  Using (p\equiv4a\pmod R),

\[
 pu+a\equiv a(4u+1)=aG_E\pmod R,
 \qquad
 4(a+u)\equiv p+4u=G_M\pmod R.
\]

Multiplication by the needed unit (u) shows separately for each of the four
integer tail numerators that its gcd with (R) is
(gcd(R,G_c)).  Hence both reduced tail denominators are exactly

\[
 \boxed{d=R/\gcd(R,G_c).}
\]

The tail sums, with every factor retained, are

\[
 Y_E+Z_E=\frac{(a+pu)^2}{Ru},
 \qquad
 Y_M+Z_M=\frac{p(a+u)^2}{Ru}.
\]

The preceding congruences and unit factors therefore give the three-way exact
equivalence

\[
 \boxed{Y_c+Z_c\in\mathbb Z
 \quad\Longleftrightarrow\quad R\mid G_c^2
 \quad\Longleftrightarrow\quad d^2\mid R.}
\]

The source is proper precisely when (d>1), equivalently (R\nmid G_c).

## 3. Complete deletion domain

For (s=(a,R,u)\in\mathscr S_c(p)), write

\[
 d_s=\frac{R}{\gcd(R,G_c(p,u))},\qquad m=4K(u).
\]

Define the decorated deletion domain

\[
 \mathscr D_c(p)=
 \{(s,k):s\in\mathscr S_c(p),\ k\in\mathbb Z_{>0},\ k\mid R,
 \ d_s\mid k,\ k\equiv1\pmod m\}.
\]

For ((s,k)\in\mathscr D_c(p)), set

\[
 R'=R/k,\qquad a'=(p+R')/4,
 \qquad F_c(s,k)=(a',R',u).
\]

Then (F_c(s,k)\in\mathscr T_c(p)), and every target obtained by keeping
(p,u,c) and replacing (R) by a positive divisor is obtained exactly once
from one (k) after the source (s) is fixed.

The proof consists of two independent equivalences.

First, prime by prime,

\[
 R/k\mid G_c
 \Longleftrightarrow
 v_\ell(k)\ge
 \max(v_\ell(R)-v_\ell(G_c),0)\text{ for every }\ell
 \Longleftrightarrow d_s\mid k.
\]

Second, the requirement that (a'=(p+R/k)/4) be an integer and that
(u\mid(a')^2) is exactly

\[
 p+R/k\equiv0\pmod m.
\]

If this target congruence holds, multiplying by (k) and subtracting the
source congruence (p+R\equiv0\pmod m) gives
(p(k-1)\equiv0\pmod m).  Since (gcd(p,m)=1), this gives
(k\equiv1\pmod m).  Conversely, (R=kR') and (k\equiv1\pmod m) give
(R\equiv R'\pmod m), so the source congruence gives
(p+R'\equiv0\pmod m).  Thus

\[
 \boxed{p+R/k\equiv0\pmod m\Longleftrightarrow k\equiv1\pmod m.}
\]

Since (m) is divisible by four, (k\equiv1\pmod4), whence
(R'=R/k\equiv3\pmod4).  Thus (R'\ge3).  Also (R'<R<p), because a
proper source has (d_s>1), so every admissible (k\ge d_s>1).  Therefore

\[
 p/4<a'=(p+R')/4<a=(p+R)/4<p/2.
\]

This proves the target domain, the full gate, the word budget, positivity, and
strict descent without discarding any prime coordinate.

## 4. Exact target coordinates

The map lands in the labelled channel triple

\[
\begin{array}{ll}
 E:&\left(a',\dfrac{pa'+(a')^2/u}{R'},
                 \dfrac{pa'+p^2u}{R'}\right),\\[3mm]
 M:&\left(a',\dfrac{p(a'+(a')^2/u)}{R'},
                 \dfrac{p(a'+u)}{R'}\right).
\end{array}
\]

To display their complete integer coordinates, let

\[
 g'=\gcd(a',u),\quad h'=(g')^2/u,\quad r'=u/g',\quad s'=a'/g'.
\]

Valuations give (a'=h'r's'), (u=h'(r')^2), and
(gcd(r',s')=1).  In channel E put

\[
 \kappa'=(pr'+s')/R';
\]

the gate (R'\mid4u+1) makes (kappa') integral, and the triple is

\[
 (a',h's'\kappa',ph'r'\kappa').
\]

In channel M put

\[
 \lambda'=(r'+s')/R';
\]

the gate (R'\mid p+4u) makes (lambda') integral, and the triple is

\[
 (a',ph's'\lambda',ph'r'\lambda').
\]

These are labelled triples.  They are not always nondecreasing triples.  The
word is recovered from the labelled first tail by

\[
 u=\frac{(a')^2}{R'Y_E-pa'}
 \quad\text{or}\quad
 u=\frac{p(a')^2}{R'Y_M-pa'}.
\]

## 5. Fixed-source inverse and global fibres

For a fixed source (s=(a,R,u)), the function

\[
 F_{c,s}:\mathcal K(s)\longrightarrow\mathscr T_c(p),
 \qquad k\longmapsto(a',R',u),
\]

is injective, because (R'=R/k), and its inverse on its image is

\[
 \boxed{k=R/R'.}
\]

There is no global inverse after (R) and (a) have been forgotten.

Fix instead a full target (t=(a',R',u)\in\mathscr T_c(p)).  Its global fibre
is in bijection with

\[
\boxed{
 \mathcal I_c(t)=\left\{k\in\mathbb Z_{>0}:
 \begin{array}{l}
 1\le k\le\left\lfloor\dfrac{p-1}{R'}\right\rfloor,\\[1mm]
 k\equiv1\pmod{4K(u)},\\[1mm]
 R'k\mid G_c(p,u)^2,\\[1mm]
 R'k\nmid G_c(p,u)
 \end{array}\right\}.}
\]

The inverse relation is

\[
 k\longmapsto
 s_k=\left(a_k,R_k,u\right),\qquad
 R_k=R'k,\qquad a_k=(p+R'k)/4,
\]

with decorated arrow ((s_k,k)).  Each displayed condition has a separate
role:

- the upper bound gives (0<R_k<p);
- (k\equiv1\pmod{4K(u)}), together with the target budget, gives
  (p+R_k\equiv0\pmod{4K(u)}), hence (a_k\in\mathbb Z) and
  (u\mid a_k^2);
- (R_k\mid G_c^2) is the trace condition;
- (R_k\nmid G_c) makes the source proper.

Because the fixed target satisfies (R'\mid G_c), write (G_c=R'H).  The
source denominator is then

\[
 d_k=\frac{R'k}{\gcd(R'k,R'H)}
     =\frac{k}{\gcd(k,H)},
\]

so (d_k\mid k), and the arrow really belongs to the deletion domain.  In the
other direction, every decorated source arrow mapping to (t) has exactly
these four properties.  This proves necessity, sufficiency, and the claimed
finite fibre without an unidentified arrow.

The map loses precisely the old pair ((R,a)), equivalently the fibre
parameter (k).  Retaining ((t,k)) recovers the source uniquely.  On free
abelian groups, the kernel of the pushforward is generated by differences of
decorated arrows in the same target fibre.

## 6. Defects and exact repairs

### A. The global inverse is not a function

`core.tex` lines 87--90 call (k=R/R') "the numerical inverse", while
lines 124--138 correctly acknowledge that different inputs can have the same
target.  Replace the earlier wording by "the inverse of the fixed-source map";
then state the global fibre as in Section 5 above.  Without the retained source
residual (R), (R/R') cannot be evaluated.

### B. The recovery of every rational integral-trace pair has a proof gap

`core.tex` lines 59--65 assert that, for arbitrary positive rational tails
(y,z) with integral (S=y+z), the quantities

\[
 b=Ry-pa,\qquad c=Rz-pa
\]

are positive integers.  The current sentence invokes
(d^2=R/\gcd(R,S)) without first defining or proving that identity, and that
identity by itself does not establish (b,c\in\mathbb Z).

The exact repair is short.  The reciprocal identity gives

\[
 yz=\frac{paS}{R}.
\]

Hence

\[
 b+c=RS-2pa\in\mathbb Z,
 \qquad
 bc=(Ry-pa)(Rz-pa)=(pa)^2\in\mathbb Z.
\]

Thus (b,c\in\mathbb Q) are roots of the monic polynomial

\[
 X^2-(RS-2pa)X+(pa)^2\in\mathbb Z[X].
\]

A rational algebraic integer is an integer, so (b,c\in\mathbb Z).  Moreover,
(1/y<R/(pa)) and (1/z<R/(pa)), so (b,c>0).  The factorization
(bc=p^2a^2), together with (p\nmid a), has exactly the (p)-valuation
pairs ((0,2),(1,1),(2,0)).  The exterior pairs give the two labelled E
orientations, and the middle pair gives the two labelled M orientations,
with (u\mid a^2).  This proves the claimed exhaustiveness.

After (b,c\in\mathbb Z) is known, the denominator identity can also be
proved.  Since (bc=(pa)^2) and (gcd(pa,R)=1), both (b,c) are units modulo
(R), and

\[
 c+pa=\frac{pa}{b}(b+pa).
\]

Thus (v_\ell(c+pa)=v_\ell(b+pa)) for every (ell\mid R).  Also

\[
 (b+pa)(c+pa)=paRS.
\]

Prime valuations now give (d^2=R/\gcd(R,S)), where (d) is the common
reduced denominator of (y,z).  This is a consequence, not the missing first
step.

### C. "Ordered" is false if it means nondecreasing

The formulas preserve a labelled tail orientation.  They do not always place
the second and third denominators in increasing order.  For the package's
(p=1009,a'=255,u=9) M target, the displayed triple is

\[
 (255,686120,24216),
\]

so the second entry exceeds the third.  Replace "ordered" by "labelled" or
"orientation-retaining" throughout.  Sorting the tails would change which
inverse formula recovers (u) and would need an explicit swap flag.

### D. Minor typing additions

- State that every divisor (k) in the deletion set is positive.
- State the full target hypotheses before the fibre formula; otherwise the
  four displayed conditions do not by themselves imply (R'\mid G_c) or the
  target word budget.
- In the coefficient formula, explicitly record that (d) and every prime
  dividing (R/d) are units modulo (m), because (gcd(R,m)=1).  This is why
  ([d^{-1}]) exists in the stated group ring.
- Rename `MORPHISMS.md` item 7 from "Target normalization" to "Target
  coordinate reconstruction".  The calculation itself retains every prime
  exponent and should be described accordingly.

