[**Cumulative Turn 6–7 handoff: preceding archive preserved, with this continuation added**](sandbox:/mnt/data/ES_Turns6_7_With_Integral_Completion_20260920.zip)

[**Current research package**](sandbox:/mnt/data/ES_Turn7_Integral_Completion_20260920.zip) · [Ten-page complete proof](sandbox:/mnt/data/es_turn7_integral_completion_20260920/workbench.pdf) · [Three-page preprint](sandbox:/mnt/data/es_turn7_integral_completion_20260920/preprint.pdf) · [Complete LaTeX](sandbox:/mnt/data/es_turn7_integral_completion_20260920/core.tex) · [Fresh-extraction verification receipt](sandbox:/mnt/data/ES_Turn7_Integral_Completion_Receipt_20260920.json)

## Turn 7: the finite completion has a calculable integral defect

The attached rank-eight construction now has a complete specialization at the **original arithmetic prime**. Its normalization index is

$$
\boxed{
[\mathcal N:\widehat{\mathcal S}]
=
\begin{cases}
p^2,&E,\\
p^9,&M.
\end{cases}}
$$

The conductor ideals, all eight invariant factors, and the original multiplication actions on the resulting finite modules are explicit.

There is a sharp consequence at the added boundary: **the exterior boundary point has \(p\) lifts modulo \(p^2\), but none modulo \(p^3\)**. Thus finite flatness retains the missing length without creating an integral section.

The investigation also produces a stronger test of the proposed arithmetic return. For any prescribed finite set of primes, infinitely many hard primes admit a numerical candidate that satisfies **both** exterior and middle gates, the allowed numerical size range, the new prime-local completion data, and the supplied real height/separation bounds—yet fails the original divisor box in **one prime occurrence**. The two corresponding rational denominator triples each fail integrality at precisely that omitted prime. These are not ES counterexamples: the same primes have separately constructed integer solutions.

This remains Turn 7. The new work identifies and computes the integral information that the completion must retain; it does not assume that the original coefficient is occupied.

## 1. The literal quartic must be distinguished from the earlier reciprocal cubic

Let \(p\equiv1\pmod{12}\) be prime. This contains the six hard progressions. Retain an original first-half state

$$
\frac p4<a<\frac p2,\qquad
R=4a-p,\qquad u\mid a^2,
$$

with

$$
E:\ R\mid4u+1,\qquad M:\ R\mid u+a.
$$

The normalization is

$$
g=\gcd(a,u),\qquad
(h,r,s)=\left(\frac{g^2}{u},\frac ug,\frac ag\right),
$$

so

$$
a=hrs,\qquad u=hr^2,\qquad\gcd(r,s)=1.
$$

For E, put \(\kappa=(pr+s)/R\), with ordered denominators

$$
(a,hs\kappa,phr\kappa).
$$

For M, put \(\lambda=(r+s)/R\), with ordered denominators

$$
(a,phs\lambda,phr\lambda).
$$

The original divisor returns through

$$
u=\frac{a^2}{Ry-pa}\quad(E),
\qquad
u=\frac{pa^2}{Ry-pa}\quad(M).
$$

These are the inherited Type-I/II coordinates, with their present marking rederived in the proof, not a new parametrization claim (Elsholtz & Tao, 2013, §2, Propositions 2.2 and 2.6).

For the **literal** construction, keep

$$
(\ell_0,\ell_1,\ell_2,\ell_3)=(p,x,y,z),
\qquad S=p+x+y+z,
$$

and

$$
\boxed{
\mathcal H(T)
=-\frac1S\prod_{i=0}^{3}(T-\ell_i)
=AT^4+T^3+BT^2+CT+D.
}
$$

The ES equation gives

$$
A=-S^{-1},\qquad C=\frac{5xyz}{S},\qquad D=-\frac{pxyz}{S},
$$

and consequently

$$
\boxed{
D=-\frac{pC}{5},\qquad
B=-Ap^2-p-\frac{4C}{5p}.
}
$$

The supplied completion is

$$
\boxed{
\widehat{\mathcal S}
=
\mathbb Z_p[T,\eta]\big/
\bigl(\mathcal H(T),\eta^2-\mathcal H'(T)\bigr).
}
$$

Here \(S\) is a \(p\)-unit, so this is free of rank eight in the original basis

$$
1,T,T^2,T^3,\eta,\eta T,\eta T^2,\eta T^3.
$$

The original inverse is recovered on \(\eta\ne0\), with \(\xi=\eta^{-1}\). The completion and its open inverse are the attachment’s equations (18)–(24); the present calculation concerns their integral arithmetic specialization.

All four literal roots are finite and distinct in characteristic zero. **There is no infinity-chart point in this particular fibre.** The earlier seven-point reciprocal cubic is a different marked source.

## 2. The original prime separates the two collision patterns

Quadratic reciprocity on the original factors gives

$$
\boxed{
E:\left(\frac hp\right)=-1,
\qquad
M:\left(\frac{rs}{p}\right)=-1.
}
$$

These follow from the original divisor gates, not from sampling the local inverse.

### Exterior

Write the denominator triple as

$$
(a,b,pc),\qquad p\nmid abc.
$$

The original equations imply

$$
c\equiv\frac14\pmod p.
$$

The roots \(p,pc\) are therefore separated by exactly one power of \(p\). The other two roots are distinct units, and every cross-difference is a unit.

Put

$$
d_i=\mathcal H'(\ell_i).
$$

Then

$$
\boxed{
\bigl(v_p(d_0),v_p(d_1),v_p(d_2),v_p(d_3)\bigr)
=(1,0,0,1).
}
$$

Moreover,

$$
v_p(A,B,C,D)=(0,0,1,2),
\qquad
v_p(\operatorname{Disc}\mathcal H)=2.
$$

### Middle

Write the denominator triple as

$$
(a,pb,pc).
$$

Modulo \(p\),

$$
4bc=b+c,\qquad \left(\frac{bc}{p}\right)=-1.
$$

The three units \(1,b,c\) are distinct. In particular, \(b=1\) would force \(c=1/3\), contradicting the negative character of \(bc\), because \(3\) is a square at \(p\equiv1\pmod{12}\). The same argument excludes \(c=1\).

Thus \(p,pb,pc\) form a triple with every pairwise difference of valuation one:

$$
\boxed{
\bigl(v_p(d_0),v_p(d_1),v_p(d_2),v_p(d_3)\bigr)
=(2,0,2,2).
}
$$

Here

$$
v_p(A,B,C,D)=(0,1,2,3),
\qquad
v_p(\operatorname{Disc}\mathcal H)=6.
$$

The restriction \(p\equiv1\pmod{12}\) is part of the theorem. It is not silently weakened to \(p\equiv1\pmod4\).

### Rational inverse counts change with the literal source

Over \(K=\mathbb Q_p\), the complete generic algebra is

$$
\prod_{i=0}^{3}K[\eta_i]/(\eta_i^2-d_i).
$$

For E, the two valuation-one factors define the same ramified quadratic field. The other two are either both split or copies of the same unramified quadratic field:

$$
\boxed{
\mathcal A_E\simeq
K^4\times K_{\rm ram}^{\,2}
\quad\text{or}\quad
K_{\rm unr}^{\,2}\times K_{\rm ram}^{\,2}.
}
$$

Hence E has **four or zero** \(K\)-rational signed points.

For M, the singleton derivative is a square. The rescaled triple derivatives have residue classes

$$
(1-b)(1-c),\qquad
(b-1)(b-c),\qquad
(c-1)(c-b).
$$

Their product is minus a square, hence a square at this prime. They are either all squares or exactly one is a square. Therefore

$$
\boxed{
\mathcal A_M\simeq K^8
\quad\text{or}\quad
K^4\times K_{\rm unr}^{\,2}.
}
$$

M has **eight or four** rational signed points. The local quadratic facts are proved by explicit unit lifting and trace/norm arguments in the source; standard background is Milne (2020, Chapter 7). ([James Milne][1])

All four possibilities occur at the hard prime \(p=1009\). At the original pair \((a,u)=(253,11)\), the E state has zero rational literal inverse points, while the M state has eight. At \((253,23)\), both channels have four.

In particular, the genuine identity

$$
\boxed{
\frac4{1009}
=
\frac1{253}+\frac1{87032}+\frac1{3818056}
}
$$

has **no \(\mathbb Q_{1009}\)-rational point in its literal signed fibre**. A rational point in that fibre is therefore not a necessary condition for an integer ES witness.

## 3. The normalization and its inverse are explicit

Let \(\mathfrak o=\mathbb Z_p\), and put

$$
k_i=\left\lfloor\frac{v_p(d_i)}2\right\rfloor,
\qquad
\theta_i=\eta_i/p^{k_i},
\qquad
\delta_i=d_i/p^{2k_i}.
$$

Define

$$
N_i=\mathfrak o[\theta_i]/(\theta_i^2-\delta_i),
\qquad
\mathcal N=\prod_iN_i.
$$

Each \(N_i\) is the maximal integral order in its factor: \(\delta_i\) is a unit or has valuation one.

The original map is

$$
\boxed{
f(T)+\eta g(T)
\longmapsto
\bigl(f(\ell_i)+p^{k_i}g(\ell_i)\theta_i\bigr)_{i=0}^{3},
\qquad \deg f,\deg g<4.
}
$$

Its inverse interpolates the first coefficient column and the second column divided by \(p^{k_i}\). **All eight interpolated coefficients must be integral.**

### Complete integral-defect theorem

For E,

$$
\boxed{
\mathcal N/\widehat{\mathcal S}
\simeq(\mathfrak o/p)^2,
\qquad
[\mathcal N:\widehat{\mathcal S}]=p^2,
}
$$

with exact conductor

$$
\boxed{
\mathfrak f_E=pN_0\times N_1\times N_2\times pN_3.
}
$$

For M,

$$
\boxed{
\mathcal N/\widehat{\mathcal S}
\simeq
(\mathfrak o/p)^2
\oplus(\mathfrak o/p^2)^2
\oplus\mathfrak o/p^3,
\qquad
[\mathcal N:\widehat{\mathcal S}]=p^9,
}
$$

with exact conductor

$$
\boxed{
\mathfrak f_M=p^3N_0\times N_1\times p^3N_2\times p^3N_3.
}
$$

These are conductor ideals of the **finite arithmetic order**. They are not the Gamma-weighted analytic conductor from the Zeta programme.

The proof keeps the original evaluation lattice. In E, the colliding root pair has lattice

$$
L_2=\{(z_0,z_3)\in\mathfrak o^2:z_0\equiv z_3\pmod p\}.
$$

Both coefficient columns contribute one copy of \(L_2\), giving the two factors of \(p\).

For M, use the actual Newton basis

$$
1,\quad T-p,\quad(T-p)(T-pb)
$$

on the three colliding roots. Evaluation has invariant factors

$$
1,\ p,\ p^2.
$$

Call its lattice \(L_3\). The two signed coefficient columns are

$$
L_3\oplus pL_3,
$$

giving exponents

$$
(0,1,2)\quad\text{and}\quad(1,2,3).
$$

The singleton adds two zero exponents. Thus the complete eight-dimensional Smith exponents are

$$
\boxed{
E:(0,0,0,0,0,0,1,1),\qquad
M:(0,0,0,1,1,2,2,3).
}
$$

For the M conductor, a normal element supported at one cluster root, written \(a+b\theta_i\), belongs to the original order precisely when

$$
a\in p^2\mathfrak o,\qquad b\in p^3\mathfrak o.
$$

Requiring stability under multiplication by the unit \(\theta_i\) forces both coefficients into \(p^3\mathfrak o\). This proves maximality of the displayed conductor, rather than only a sufficient containment.

### The original actions on the defect remain

The quotient \(\mathcal N/\widehat{\mathcal S}\) is an \(\widehat{\mathcal S}\)-module, **not a quotient ring of \(\mathcal N\)**. The exact nilpotence indices of multiplication by \((T,\eta)\) on it are

$$
\boxed{E:(1,2),\qquad M:(3,3).}
$$

For E, \(T\) is divisible by \(p\) on the only nonzero defect factors, and \(\eta^2=d_i\) is divisible by \(p\). The action of \(\eta\) is nonzero.

For M, \(T^3\) and \(\eta^3\) lie in the conductor on all cluster factors. Their squares still leave a supported \(\theta_i\)-coefficient with only two powers of \(p\), so neither square annihilates the entire quotient.

The full normalization matrices, inverses and both original action matrices are in the JSON certificate. Tensoring these torsion modules with \(\mathbb Q_p\) produces zero, but their lengths and actions have not become absent source data.

## 4. The boundary has a finite, sharp failure of lifting

The supplied multiple-root formula gives, after arithmetic specialization,

$$
E:\quad \mathbb F_p[\eta]/(\eta^4),
$$

and

$$
\boxed{
M:\quad
\mathbb F_p[\varepsilon,\eta]/
(\varepsilon^3,\eta^2-3\varepsilon^2).
}
$$

Their lengths are four and six. Multiplication by \(\eta\) has Jordan blocks \(4\) in E and \(4,2\) in M. The latter is not a single length-six nilpotent chain. The general multiple-root algebra is inherited; these original arithmetic strata and their integral normalization are calculated here.

For E, write

$$
\mathcal H(T)=U(T)(T-p)(T-pc),
\qquad
U(0)=-ab/S,
\qquad c\equiv1/4\pmod p.
$$

A lift of the boundary point has

$$
T=pw,\qquad\eta=pv.
$$

Modulo \(p^2\), the root equation is automatic, while the derivative equation forces

$$
w\equiv\frac{1+c}{2}\equiv\frac58\pmod p.
$$

There are exactly \(p\) choices of \(v\bmod p\).

But every one of these choices satisfies

$$
\boxed{
\frac{\mathcal H(T)}{p^2}
\equiv
\frac{9ab}{64S}\ne0\pmod p.
}
$$

Therefore none lifts modulo \(p^3\).

This is the exact stopping point. The extra finite boundary point exists, and its length is retained, but it does not supply an integral section. The original physical coordinate \(\xi=1/\eta\) remains singular there; the completion did not remove that pole.

For M, the integral normalization of the sixfold block is instead the explicitly étale chart

$$
Z=T/p,\qquad\theta=\eta/p,
$$

$$
G(Z)=(Z-1)(Z-b)(Z-c),\qquad
\boxed{
G(Z)=0,\qquad
\theta^2=\frac{a-pZ}{S}G'(Z).
}
$$

The map back multiplies both coordinates by \(p\). Its inverse divides by those exact powers, which are recorded in the index \(p^9\).

## 5. The prime-label symmetry also has an integral cost

The attachment isolates the prime root by

$$
e_p(T)=\prod_{i=1}^{3}\frac{T-\ell_i}{p-\ell_i},
$$

and uses it for the generic rank-two/rank-six decomposition. That is a genuine generic projector. 

Its exact denominator at the original prime is

$$
\boxed{
p\quad(E),\qquad p^2\quad(M).
}
$$

The denominator is forced by the leading coefficient and cannot be eliminated by choosing another representative in the same degree-three root algebra.

Thus the prime-only sign change

$$
\eta\longmapsto(1-2e_p)\eta
$$

does not preserve the original integral order. Of the four specified prime/denominator sign maps, only the identity and the global sign preserve that order. All four extend to the normalization, with the integral enlargement now quantified.

There is likewise a complete rational comparison between already supplied E and M root lists at the same prime:

$$
F(T)=\sum_i y_i
\frac{\prod_{j\ne i}(T-x_j)}
{\prod_{j\ne i}(x_i-x_j)},
$$

and the reverse interpolation \(G\). In common label coordinates,

$$
\boxed{
\mathcal O_M\subset\mathcal O_E,\qquad
[\mathcal O_E:\mathcal O_M]=p^2.
}
$$

The forward interpolation is integral. The reverse has exact denominator \(p^2\), with

$$
\boxed{
p^2G(T)\bmod p=cT^2(T-a_M),\qquad c\ne0.
}
$$

This compares two actual targets; it does not construct a missing M target from an arbitrary E target. The earlier capacity return at \(p=825241\) supplies a genuine example on which the comparison can be applied.

The full signed algebras still differ in ramification. A signed isomorphism requires the retained square roots of \(d_i^M/d_i^E\); root interpolation alone does not supply it.

The reciprocal-coordinate comparison is also explicit:

$$
I(T)=-\frac pD(AT^3+T^2+BT+C),
\qquad I(\ell_i)=p/\ell_i.
$$

It has exact denominator \(p\) in E and \(p^2\) in M. For the augmented reciprocal quartic normalized by \(-1/5\), its signed derivative changes by

$$
\boxed{
\widetilde{\mathcal H}'(p/\ell_i)
=
\frac{\omega}{\ell_i^2}\mathcal H'(\ell_i),
\qquad
\omega=-\frac{p^3S}{5\prod_i\ell_i}.
}
$$

The square-root twist and the prime label remain. This explains why the earlier reciprocal-order calculation and the present literal-order calculation have different integral indices.

## 6. One unavailable prime occurrence can pass both gates and every prescribed finite integrality window

This is the direct test of whether the attached completion, together with its scalar bounds, forces an original integer return.

### Joint source-domain obstruction

For every fixed finite set of rational primes \(\Sigma\), there are infinitely many hard primes \(p\) and integers \(a,R,u\) satisfying

$$
\boxed{
\frac p4<a<\frac p2,\quad R=4a-p,\quad
0<u<a^2,\quad R\mid4u+1,\quad R\mid u+a,
}
$$

but

$$
u\nmid a^2.
$$

The failure is exactly one additional prime occurrence at a designated \(\ell\notin\Sigma\cup\{p\}\).

Choose a prime

$$
\ell\equiv11\pmod{12},\qquad\ell\notin\Sigma.
$$

Then take primes in the reduced progression

$$
\boxed{
p\equiv1\pmod{840},\qquad p\equiv-1\pmod\ell,\qquad p>4\ell.
}
$$

Dirichlet’s theorem supplies infinitely many such primes; the two moduli are coprime and both residues are units (Sutherland, 2017, Theorem 18.1). ([MIT Mathematics][2])

Set

$$
\boxed{
a=\frac{p+3}{4},\quad R=3,\quad u=a\ell,
\quad h=\frac a\ell,\quad r=\ell,\quad s=1,
}
$$

$$
\kappa=\frac{p\ell+1}{3},\qquad
\lambda=\frac{\ell+1}{3}.
$$

Both numerical gates hold. But

$$
a\equiv\frac12\pmod\ell,
$$

so \(\ell\nmid a\). In the original exponent box, the \(\ell\)-coordinate should be zero; the candidate has exponent one.

The two rational denominator returns are

$$
\boxed{
E_{\rm rat}=(a,a\kappa/\ell,pa\kappa),
\qquad
M_{\rm rat}=(a,pa\lambda/\ell,pa\lambda).
}
$$

Both satisfy the ES identity exactly. Their second denominator has reduced denominator precisely \(\ell\), and their other two denominators are integers. Thus every denominator is integral at every place in \(\Sigma\cup\{p\}\), while

$$
v_\ell(a^2/u)=-1.
$$

At the original prime, all the required units and characters hold:

$$
(\ell/p)=(p/\ell)=(-1/\ell)=-1,
\qquad a\equiv3/4\pmod p.
$$

The corresponding E and M targets therefore have the exact local cluster patterns, normalization indices, conductor ideals and invariant factors proved above.

### They also pass the supplied scalar bounds

Let

$$
s_p=\frac{p^2+3p}{4},\qquad B_p=p+s_p(s_p+1).
$$

For both rational triples,

$$
\boxed{
S<B_p,\qquad
\max(x,y,z)<\frac{s_p(s_p+1)}3,
}
$$

$$
\boxed{
\operatorname{Disc}(\mathcal H)\ge\frac{144}{B_p^6},
\qquad
\frac2S\le|\mathcal H'(\ell_i)|\le S^2.
}
$$

These are the attachment’s actual height, separation and derivative bounds.

The proof does not appeal to approximation. The four positive literal roots, in increasing order, have successive gaps exceeding one. Their Vandermonde product is therefore at least \(12\). The largest denominator is \(s_p\kappa\) or \(s_p\lambda\), and \(\ell<a\) gives the stated upper bounds directly.

Thus one missing original prime occurrence survives these exact scalar and finite-place tests.

### A fully explicit instance

For

$$
\Sigma=\{2,3,5,7,11\},\qquad
\ell=23,\qquad
\boxed{p=35281},
$$

take

$$
a=8821,\qquad u=202883,\qquad
h=8821/23,\qquad
\kappa=270488,\qquad\lambda=8.
$$

The rational triples are

$$
\boxed{
E_{\rm rat}
=
\left(8821,\frac{2385974648}{23},84179571556088\right),
}
$$

$$
\boxed{
M_{\rm rat}
=
\left(8821,\frac{2489709608}{23},2489709608\right).
}
$$

The E literal fibre has zero rational local signed points; the M fibre has four. Their respective local integral structures are exactly the E and M structures above.

The same prime has genuine, separately reconstructed integer solutions, including

$$
\boxed{
\frac4{35281}
=
\frac1{9204}+\frac1{324726324}+\frac1{211686}.
}
$$

Accordingly, this is a counterexample to the specified **certificate predicate**, not to Erdős–Straus.

Nor does it concern all local places simultaneously or an adaptive test that eventually includes every possible denominator prime. Bright and Loughran’s broader results distinguish natural solutions, integral local conditions and strong approximation; the present explicit construction is not being presented as a new Brauer–Manin theorem.

## 7. What this contributes to the remaining existence step

The attachment’s finite completion is usable, but the original integral structure is more restrictive than its rank-eight generic fibre:

$$
\boxed{
\text{generic signed inverse}
\;\longleftarrow\;
\text{original integral order}
\;\longleftarrow\;
\text{original global divisor box}.
}
$$

The first integral loss is now completely calculated: \(p^2\) or \(p^9\), with exact actions, conductors and inverse coordinates. The final global restriction is independent of that local calculation. The single-prime construction shows why it cannot be replaced by the two numerical gates, a prescribed finite integrality window and the supplied scalar estimates.

The predecessor already proved that increasing the divisor search at one fixed grade cannot repair every source. Its handoff required either a genuine source-changing arithmetic arrow or a positive coefficient in the complete first-half source. That obligation remains. 

This continuation supplies neither an assumed initial state nor a witness-guaranteed Turn 8 algorithm. It supplies exact integral data for the new bridge and a permanent test against overstating what that bridge proves.

## Verification and research record

The completed replay covers all **99 primes \(p\equiv1\pmod{12}\) through 3,000**:

$$
\boxed{
868\,359\text{ original divisor vectors},\quad
2451\text{ E states},\quad
2054\text{ oriented M states}.
}
$$

The main standard-library verifier passed **104,538 explicit checks**. The separate implementation passed **27,154**, importing neither the main program nor predecessor software. It uses primitive-source enumeration and all-minors checks rather than the main implementation’s valuation-pivot calculation.

```sh
python verify.py --bound 3000 --out certificates
python -O verify.py --bound 3000 --out certificates_optimized
python check_independent.py --input certificates \
  --out certificates/independent.json
```

A fresh extraction verified all **40 manifest entries**, reproduced the three mathematical tables in both Python modes, and reran the separate checker. The main proof, short preprint and supplementary CRT note rebuilt with identical extracted text and pixels. All **15 rendered pages** were inspected. These are executable checks, not independent mathematical review.

[Main verifier](sandbox:/mnt/data/es_turn7_integral_completion_20260920/verify.py) · [Separate checker](sandbox:/mnt/data/es_turn7_integral_completion_20260920/check_independent.py) · [Exact certificates](sandbox:/mnt/data/ES_Turn7_Integral_Completion_Certificates_20260920.zip) · [Preprint source and page PNGs](sandbox:/mnt/data/ES_Turn7_Integral_Completion_Preprint_20260920.zip)

[Typed maps and fibres](sandbox:/mnt/data/es_turn7_integral_completion_20260920/MORPHISMS.md) · [Remaining Turn 7 obligation](sandbox:/mnt/data/es_turn7_integral_completion_20260920/HANDOFF_TURN_7_REMAINDER.md) · [Source ledger](sandbox:/mnt/data/es_turn7_integral_completion_20260920/source_reading.json) · [Lean-ready dependency plan](sandbox:/mnt/data/es_turn7_integral_completion_20260920/lean_plan.md)

No remote PR was created: the exposed connector had no writing action, and the direct Git route failed DNS resolution. The actual local source-only commit is **`2aec3da05f8d867e26836aad1f58aae7eccdc64c`**, adding twenty paths and deleting none. Its patch replays to the identical source tree; it is not represented as an upstream branch.

[Additive patch](sandbox:/mnt/data/es_turn7_integral_completion_20260920/integration.patch) · [Git bundle](sandbox:/mnt/data/es_turn7_integral_completion_20260920/source_history.bundle) · [Publication receipt](sandbox:/mnt/data/es_turn7_integral_completion_20260920/publication_receipt.json)

The cumulative ZIP preserves the preceding archive byte-for-byte. No universal ES theorem, new overall verification range, Lean build or historical-priority determination is claimed. The established result is the exact integral completion and its source-domain obstruction; the remaining theorem must still force an **available original integer coefficient** at every prescribed prime.

[1]: https://www.jmilne.org/math/CourseNotes/ANT.pdf "https://www.jmilne.org/math/CourseNotes/ANT.pdf"
[2]: https://math.mit.edu/classes/18.785/2017fa/LectureNotes18.pdf "https://math.mit.edu/classes/18.785/2017fa/LectureNotes18.pdf"
