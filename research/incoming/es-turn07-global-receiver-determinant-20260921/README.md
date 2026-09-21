# A global sign for the literal Erdős–Straus receiving determinant

This research note proves that a specific complex $4\times4$ receiving matrix
is invertible at every positive integral Erdős–Straus witness for a prime
$p\equiv1\pmod {12}$. It removes the earlier three-character restriction from
that receiver question. It does not prove that every such prime has an
Erdős–Straus witness.

Read `preprint.pdf` for the short paper and `workbench.pdf` for the complete
coordinate proof, maps, coefficient certificates, examples, counterdomains and
source record. The proof source is `core.tex`.

## The theorem

Let

```text
4/p = 1/x + 1/y + 1/z,
p prime, p = 1 mod 12,
x,y,z positive integers.
```

Retain the four literal roots $\ell=(p,x,y,z)$, their order, and
$S=p+x+y+z$. Define

```text
H(T) = -S^(-1) product_j (T-l_j) = A T^4 + T^3 + B T^2 + C T + D,
d_j = H'(l_j),
xi_j in C^x with xi_j^2 d_j = 1.
```

The original odd receiver has columns

```text
o_j = xi_j (1, -i d_j, A d_j^2 + 2 l_j d_j,
            i(7 l_j^2 d_j - 13 d_j^2))^T.
```

For the explicit coefficient polynomial $F$ in `core.tex`, put
$\mathfrak N=S^6F$. Then

```text
N < -(125873811/262144) p^8 < 0.
```

If $p\equiv1\pmod {24}$, the constant improves to
$327448292668/47045881$. With the applicable constant $c$,

```text
|det O| > 4 c p^8/S^3,
||O^(-1)||_2 < 360 S^9/(c p^8).
```

The norm is the operator norm for the standard Hermitian norm on
$\mathbb C^4$. The exact phase is

```text
epsilon = A^2 product_(i<j)(l_j-l_i) product_j xi_j in {+1,-1},
det O = 4 epsilon F/A^3 = -4 epsilon N/S^3.
```

## Why the sign proof covers every integral witness

The arithmetic reduction proves that the four literal roots are distinct and
that every witness has a unique smallest denominator $a$ with
$p/4<a<p/2$. Put $R=4a-p$. The two remaining denominators give positive
factor coordinates

```text
X = R y - p a,
Z = R z - p a,
X Z = p^2 a^2.
```

Their $p$-valuation pair is either exterior, $(0,2)$ up to orientation, or
middle, $(1,1)$. These cases exhaust the integral witness domain.

In the exterior case, the original divisor word $u\mid a^2$ and
$w=p/R$ give an exact rational function

```text
-N/p^8 = P_E(u,w)/(2^26 u^6 w^8).
```

The translated polynomial $P_E(1+X,1+Y)$ and the two exact derivative
numerators each have all 221 coefficients positive. Thus the ratio increases
strictly in $u,w\ge1$. The arithmetic gate proves $u\ge2$; quadratic
reciprocity strengthens this to $u\ge5$ when $p\equiv1\pmod {24}$.

In the middle case, order the two tails as $pb<pc$ and set
$X=b-2\ge0$, $Y=c-b-1\ge0$. The exact comparison polynomial

```text
47045881 H_M(X,Y) - 327448292668 L_M(X,Y)^6
```

has zero constant term and 191 positive nonzero coefficients. Its coefficients
of $X$ and $Y$ are positive, so equality is possible only at
$(X,Y)=(0,0)$. That point would require $a=6p/19$, which is not integral for
a prime $p\equiv1\pmod {12}$. The middle inequality is therefore strict on
the original domain.

The diagrams in `figures/` show both parameter domains and the typed map from
the literal witness through (H), (O=\mathsf C_HU), the determinant, and the
inverse bound. Their TikZ sources retain all labels and constants.

## Reproduce the certificates

Python 3.10 or later and the standard library are sufficient:

```text
python run_all.py --bound 3000 --directory reproduced/normal
```

The release replay runs the main derivation and a separately implemented
checker in ordinary and optimized Python. It requires byte-identical
mathematical JSON across interpreter modes. The current replay reports:

```text
main checks per mode:        48,542
independent checks per mode: 30,245
ordinary/optimized outputs:  identical
primes p = 1 mod 12:         99
shells:                      34,287
original divisor words:      868,359
integral E states:           2,451
integral M states:           2,054
```

The finite census tests the implementation. The universal theorem comes from
the complete symbolic reductions and finite coefficient identities, not from
extrapolating the census.

Build the papers with two runs of each command:

```text
pdflatex -interaction=nonstopmode -halt-on-error workbench.tex
pdflatex -interaction=nonstopmode -halt-on-error preprint.tex
```

`certificates/polynomial_certificates.json` stores every coefficient;
`reproduced/` stores the fresh replay; `verification.json` records commands,
hashes and scope; and `MORPHISMS.md` lists domains, codomains, inverses, fibres,
signs, metrics and information loss.

## Sources and provenance

The human-source antecedent for the Type I/II coordinate framework is Christian
Elsholtz and Terence Tao, [*Counting the number of solutions to the
Erdős–Straus equation on unit fractions*](https://arxiv.org/abs/1107.1010),
arXiv:1107.1010v6, Section 2, Propositions 2.2 and 2.6. Its original author TeX
is preserved under `literature/` with its SHA-256 and exact reading range in
`source_reading.json`.

The direct programme antecedent is the pinned
[*odd receiving divisor*](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/49976b17491ba927df8bc7f2c2f81d39dfb15ce8/research/incoming/es-fable-zeta-bridge-20260920/ODD_RECEIVER_ES_PULLBACK.tex#L19-L215),
which defines the receiver, determinant polynomial, ES pullback and
positive-real counterdomain. The later
[*three-character theorem*](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/49976b17491ba927df8bc7f2c2f81d39dfb15ce8/research/incoming/es-rh-continuation-b-20260920/RESEARCH_CONTINUATION.md#L44-L254)
is the precise result strengthened here. The current Turn 7 occupancy boundary
is recorded in the pinned
[*original-divisor descent*](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/1400e6301429cf9c66d8071e107be9dc41f5b907/research/incoming/es-turn07-divisor-descent-20260921/core.tex#L1-L16).

No historical-priority determination is made.

## Exact negative controls and remaining problem

The positive-real reciprocal family

```text
p=1,
b=t,
c=t+1/10,
a=bc/(4bc-b-c)
```

has a unique collision-free receiver singularity with

```text
3053/1000 < t < 1527/500,
t approximately 3.05367681075890.
```

Its middle tail gap is $1/10$, and both exterior raw words lie below the
proved exterior cone. It therefore shows exactly why positivity over all real
reciprocal quartics is false without challenging the integral theorem.

The raw exterior source $(p,a,R,u)=(1009,321,275,9)$ also has a nonsingular
receiver while its divisibility gate fails: $275\nmid37$. Receiver
invertibility does not create an integral source.

The remaining arithmetic problem is still initial occupancy: prove that every
prescribed hard prime has at least one original integral E or M state. This
module proves what happens to the receiver once such a state exists. No Lean
build and no independent human review are claimed.
