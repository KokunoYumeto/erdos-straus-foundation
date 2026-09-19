# A complement–norm cutoff for exterior Erdős–Straus states

This package proves a finite, invertible atlas for every **existing** positive
first-half exterior state of a prime \(p\equiv1\pmod4\). It does not prove that
such a state exists for every prime, and therefore does not prove the
Erdős–Straus conjecture. The purpose of the atlas is to replace an unrestricted
state search by three exact coordinate charts while retaining every original
divisibility condition and the ordered denominator return.

The complete proof is in [core.tex](core.tex), the reader PDF is
[workbench.pdf](output/pdf/workbench.pdf), and the machine-readable claim ledger
is [claims.json](claims.json).

## Retained source object

Start with positive integers \(p,a,u\) satisfying

$$
p>1,\qquad p\equiv1\pmod4,\qquad
\frac p4<a<\frac p2,\qquad \gcd(p,a)=1,
$$

$$
R=4a-p,\qquad u\mid a^2,\qquad R\mid4u+1.
$$

Define

$$
g=\gcd(a,u),\qquad
(h,r,s)=\left(\frac{g^2}{u},\frac ug,\frac ag\right),\qquad
\kappa=\frac{pr+s}{R}.
$$

Then

$$
a=hrs,\qquad u=hr^2,\qquad \gcd(r,s)=1,
$$

and the ordered denominator morphism is

$$
(a,u)\longmapsto
(x,y,z)=(a,hs\kappa,phr\kappa),
\qquad
\frac4p=\frac1x+\frac1y+\frac1z.
$$

Its ordered inverse retains the original first coordinate and is

$$
u=\frac{a^2}{Ry-pa}.
$$

No permutation of \(x,y,z\) is suppressed. Retain two further coordinates

$$
v=\frac{a^2}{u}=hs^2,\qquad
D=\frac{4u+1}{R}=\frac{r+\kappa}{s}.
$$

The proof derives, rather than assumes,

$$
pD+1=4hr\kappa,\qquad
(p+R)^2+4v=4vRD,\qquad
p+R<2vD,
$$

and proves \(v\ne R,D\). It does **not** assert
\(\gcd(v,D)=1\): the state at \(p=37\) has \((v,D)=(18,3)\).

## Strict cubic cutoff

Let

$$
w=\min\{v,R,D\}.
$$

Every retained positive source state satisfies the strict inequality

$$
\boxed{(p+w)^2>4(w+1)^2(w-1).}
$$

If \(C(p)\) is the largest positive integer satisfying this exact inequality,
then

$$
1\le C(p)<p,\qquad
\min\{v,R,D\}\le C(p),\qquad
C(p)=\left(\frac p2\right)^{2/3}+O(p^{1/3}).
$$

The strict sign uses \(p\equiv1\pmod4\). Without that hypothesis,
\((p,a,u,R,D,v,w)=(19,6,6,5,5,6,5)\) attains equality. This is a boundary
counterexample to the hypothesis-free cutoff, not an Erdős–Straus
counterexample.

The scale and leading constant are sharp on the stated integer source domain.
For \(n\ge2\), put

$$
\begin{aligned}
h&=4n^2-2,& r&=n,& s&=1,\\
R&=D=4n^2-1,& \kappa&=4n^2-n-1,\\
p&=16n^3-4n^2-8n+1,& a&=hn,& u&=hn^2.
\end{aligned}
$$

These are actual positive source states and

$$
\min\{v,R,D\}=h=C(p).
$$

The complete hard-residue calculation is

$$
p(n)\equiv289\pmod{840}
\quad\Longleftrightarrow\quad
n\equiv24\ \text{or}\ 164\pmod{210}.
$$

No infinitude of prime values of this cubic is claimed.

## Three exact inverse charts

For prime \(p\equiv1\pmod4\), set \(C=C(p)\) and

$$
K(v)=\prod_{\ell^e\parallel v}\ell^{\lceil e/2\rceil}.
$$

Prime-by-prime, \(v\mid a^2\) is equivalent to \(K(v)\mid a\). Every original
state lies in exactly one of the following charts, and every retained chart
entry reconstructs an original state.

### 1. Direct residual chart

Retain

$$
3\le R\le C,\quad R\equiv3\pmod4,\quad
a=\frac{p+R}{4},\quad
u>0,\quad u\mid a^2,\quad R\mid4u+1,
$$

together with \(R\le D\) and \(R<v\). The inverse is
\((a,u)\mapsto(4a-p,u)\); the entire \(u\)-fibre remains present.

### 2. Reciprocal chart

Retain

$$
3\le D\le C,\quad D\equiv3\pmod4,\quad
B_D=\frac{pD+1}{4},
$$

$$
w>0,\qquad w\mid B_D^2,\qquad w<B_D,\qquad D\mid w+B_D.
$$

Set

$$
g=\gcd(B_D,w),\quad h=\frac{g^2}{w},\quad
r=\frac wg,\quad \kappa=\frac{B_D}{g},\quad
s=\frac{r+\kappa}{D},\quad a=hrs,\quad u=w.
$$

The retained inequalities are \(D<R\) and \(D<v\). The proof establishes
integrality, positivity, \(\gcd(r,s)=1\), the exterior gate, the first-half
range, and both directions of the inverse.

### 3. Complement–norm chart

Retain

$$
2\le v\le C,\qquad
R\mid p^2+4v,\qquad
R\equiv3\pmod4,\qquad
v<R<p,
$$

$$
\boxed{R\equiv-p\pmod{4K(v)}}.
$$

Then

$$
a=\frac{p+R}{4},\qquad
u=\frac{a^2}{v},\qquad
D=\frac{4u+1}{R},
$$

with \(v<D\). The final congruence is the exact square-divisor availability
condition; norm divisibility alone is insufficient.

The partition retains ties exactly. If \(R=D<v\), the state is direct. If
\(v<R=D\), it is norm. Both occur, respectively at
\((p,a,u,R,D,v)=(13,4,2,3,3,8)\) and \((5,2,2,3,3,2)\).

Primality is essential to the parameter-side converse maps as stated. The
composite inputs \(p=21,93,25\) give explicit failures in the direct,
reciprocal, and norm charts; the full calculations are in core.tex.

## Separating the middle and exterior cutoffs

At the prime \(p=48049\), the exterior state

$$
(a,u,R,D,v,h,r,s,\kappa)
=(12090,24180,311,311,6045,6045,2,1,309)
$$

returns

$$
\frac4{48049}
=\frac1{12090}+\frac1{1867905}+\frac1{179501934690}.
$$

Here \(R=D=311\), while the earlier middle cutoff is \(247\). Thus the middle
square-root cutoff does not transfer unchanged to the exterior cofactors. The
two channels are related through the common original equation and retained
source coordinates, but their proved finite atlases are not identical.

The least complement grade also need not be occupied. At \(p=2521\), the lane
\(v=11\) is empty: the exact divisor and residue conditions leave no
\(0<R<p\). The package supplies the full factorization and a Lucas certificate
for the remaining factor \(141233\).

## Reproduction and independent checking

From this directory:

~~~text
python verify.py --bound 3000 --out reproduced
python -O verify.py --bound 3000 --out reproduced_optimized
python check_independent.py --input reproduced --out independent.json
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf workbench.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf workbench.tex
~~~

The checked range contains 211 primes \(p\equiv1\pmod4\) through \(3000\),
1,877,004 original positive divisor vectors, and 5,700 canonical exterior
states: 2,560 direct, 1,927 reciprocal, and 1,213 norm. The main checker records
205,993 checks; the separate checker records 44,351 checks and imports neither
the main verifier nor predecessor code. Normal and optimized main runs are
byte-identical.

These finite computations verify the stated comparison and exact examples.
They are not a new overall verification range for the conjecture, a Lean proof,
human peer review, or evidence that every prime has an occupied chart.

## Provenance and literature

The received archive is byte-preserved in [received/](received/). Its archive,
source, repair, execution, and rendering identities are recorded in
[source_receipt.json](source_receipt.json),
[integration_verification.json](integration_verification.json), and
[render_receipt.json](render_receipt.json). Exact coordinate maps and their
domains and inverses are also indexed in [MORPHISMS.md](MORPHISMS.md).

The exterior presentation is compared with the classical Type I
parametrization in:

- Christian Elsholtz and Terence Tao, “Counting the number of solutions to the
  Erdős–Straus equation on unit fractions,” *Journal of the Australian
  Mathematical Society* 94 (2013), 50–105, §2, Proposition 2.2
  ([arXiv:1107.1010](https://arxiv.org/abs/1107.1010)).
- M. Bello-Hernández, M. Benito, and E. Fernández, “A Divisor Parametrization
  for the Erdős–Straus Conjecture,” §3
  ([arXiv:2606.10922](https://arxiv.org/abs/2606.10922)).

The paired middle presentation is compared with Type II in Elsholtz–Tao,
§2, Proposition 2.6. The local source-TeX readings and exact locators are
recorded in [source_reading.json](source_reading.json). The bounded search did
not locate the displayed cubic cutoff or complete three-chart inverse in those
sources; this is not a novelty or priority claim.

## Exact open obligation

The [middle two-chart atlas](../es-turn07-middle-cutoff-20260919/README.md) and
this exterior three-chart atlas decide the complete original source at each
fixed prime. They do not prove that the union is nonempty. What remains is a
structural nonvanishing theorem:

$$
\forall p\ \text{in the unresolved prime class},\qquad
\text{at least one original exterior or middle coefficient is positive}.
$$

A finite search that is permitted to return the empty set is not such a
theorem, and neither a parameter bound nor a norm factor by itself supplies the
missing witness.
