# Independent compliance audit of the unary and shared-variable includes

Audit date: 2026-09-08. Scope: the three requested requirements concerning information retention, complete calculation, and exact maps or computed obstructions between substantively distinguished presentations. This is not a replacement theorem-correctness review. Both specified current files were read in full. The source attachment containing equations (71)–(100) was also read in full to check the input/output distinction and the original seed domain.

Audited bytes:

- `unary_boolean_transport.tex`: SHA256 `6ee796fbc0a9ac286f9372e8f7345728dd8f785913dd79211e422ebdcf55af57`.
- `shared_variable_crt.tex`: SHA256 `e944046560f152f76a24435052ea4e63153dbaaa8ec14084a72c49dd36e9750b`.
- Source attachment `a7b3a920-42b4-454c-b1ca-ddccbfbeaafb/pasted-text.txt`: SHA256 recorded by the corpus as `69eaaa97ddceccbe6d688b8e66fe1a44fda9fc085f0ec3cc671cfacbffdfdcb1`; its source text was read, not copied into this report.

## Verdict

The two includes retain the exact bounded ES and Boolean data through their claimed bijections. No information-losing normalization, incomplete arithmetic simplification, false inverse, or unacknowledged loss in the truth/count aggregation was found. One narrow compliance gap remains at `shared_variable_crt.tex:177–181`: after distinguishing prescribed integer output classes from prime divisors of a chosen cyclotomic input, the text does not instantiate the exact surviving input/output incidence or compute a failure of the stronger implication there. The generic bounded theorem permits such a predicate, but naming that possibility is weaker than supplying the concrete map required by the user's third instruction.

This is a missing composition, not a false theorem and not a demand for universal prime coverage. The complete finite correspondence, inverse fibre parameters, positive witness return, and a source-compatible counterexample are supplied below for the parent to use. The counterexample excludes one specified prime divisor only; it does not exclude every prime divisor of that cyclotomic value.

## Retained information checked

1. **Unary coordinates, tags, and orientation.** `unary_boolean_transport.tex:69–164` gives both maps between the tagged finite exponent box and budget-valid codes, recovers `D`, `u`, every exponent, `j`, and the tag, and restricts denominator inversion to the exact ordered image. The exterior transpose and the middle coordinate exchange are explicitly retained. GCD reduction here is reversible because `g`, `D`, the shell, and the exponents are reconstructed; it is not an information-losing normalization.
2. **Truth and count projections.** Lines 166–275 define the truth map on the passing domain and retain its complete fibres. The scalar counts are computed from those retained sets, not identified with those sets. The disjoint truth union, diagonal intersection fibre product, and all union-projection multiplicities are explicit. The least-index choice is a section onto the least-index strata, not a claim that the full many-to-one coproduct projection is bijective. Lines 307–312 expressly store codes, exponents, and integer lifts in addition to counts. No extra inverse from a scalar cardinality is claimed or needed.
3. **Weighted counts.** Lines 232–241 keep the passing domain and state exactly when the half-weighted count is an unordered count: the middle selection must be invariant under complementation. A noninvariant selection is expressly allowed to produce a nonintegral half-count. Thus the orbit information is not silently discarded.
4. **Partial domains.** Unary lines 232–235 restrict `C,D,y,z` predicates to actual hits; arbitrary off-domain bits are multiplied by the zero hit indicator. Shared-variable lines 194–204 retain admissibility and require variable divisors to be positive on that domain. Consequently an appended predicate with a divisor positive only at ES hits must be instantiated on that hit domain, as the corollary's words “on these reconstructed coordinates” and its positivity proof require. The generic theorem does not authorize division by an off-hit zero divisor. No claim to the contrary appears.
5. **Canonical auxiliary fibres.** Shared-variable lines 215–283 encode signs and Euclidean division uniquely, including zero residuals, negative numerators, and inactive slack variables. The inactive-slack equations prevent auxiliary multiplicity. The original tuple is retained, and projection has precisely one auxiliary extension on its stated admissible domain.
6. **CRT reduction and all bounded lifts.** Shared-variable lines 15–94 retain coefficient GCD divisibility, zero coefficients, modulus one, noncoprime compatibility, the integer kernel, and complete positive/bounded inverse parameters. Lines 319–434 retain the full vector lattice fibre and every interval intersection; the modulus need not make the coordinate reduction injective. The example with lifts `-2,0,2` explicitly records that noninjectivity.
7. **Original ES hypotheses.** Shared-variable lines 470–562 construct the concrete full primewise rectangle, variable-positive divisors, finite coprimality predicate, canonical `C,D`, and bounds for the original ordered denominators. Prime `p`, its shell range, and both tags remain attached. The optional `A<=2` predicate is not substituted for the full domain. The output proposition uses weaker positive-seed hypotheses than the source's normalized seed; this is valid for its stated integrality conclusion, but the wider output proposition alone must not be read as a map into the normalized or full bounded shell at `q`.

## CSH-1: missing explicit input/output incidence

Locator: `shared_variable_crt.tex:177–181`, following `prop:output-crt`. Severity: narrow compliance gap in the required composition; no incorrect existing theorem identified.

Keep the exact fixed seed and constants of that proposition. Suppose its input CRT tests pass and give residue `a` and modulus `M`; this supposition is the already-computed branch of the input algorithm, not an assumed missing lift. Let the retained input interval be `U <= X <= V`, with `U>=1`. Intersecting it with `X=a+Mt` gives all inputs exactly. Empty intervals give the empty set. Because `6F` divides every input, every positive input has `X>=6`.

Write

\[
P(X)=X^4-X^2+1,\qquad
I=\{a+Mt:U\le a+Mt\le V\}.
\]

If the output compatibility tests fail, define the output set to be empty. If they pass, retain the exact `q_0,L_out` of the proposition and put

\[
O=\{q\in\mathbb Z_{>0}:q=q_0+L_{\rm out}s, s\in\mathbb Z\}.
\]

The missing typed finite correspondence is

\[
\mathcal I=\{(X,q):X\in I,\ q\text{ prime},\ q\mid P(X),\ q\in O\}.
\]

The projection to an input has the complete fibre

\[
\operatorname{pr}_X^{-1}(X)=
\{(X,q):2\le q\le P(X),\ q\text{ prime},\ P(X)\equiv0\pmod q,\ q\in O\}.
\]

This is explicitly computable by division and finite primality tests. It does not assert that this fibre is nonempty. The correspondence is finite because `I` is finite and each prime divisor of the positive integer `P(X)` is at most `P(X)`.

There is also a solved CRT description of the projection to each prime output, not merely a divisibility test. For a fixed prime `q` in `O`, compute the finite root set

\[
Z_q=\{\rho\in\{0,\ldots,q-1\}:\rho^4-\rho^2+1\equiv0\pmod q\}.
\]

Set `g_q=gcd(M,q)` and `M_q=Mq/g_q`. For each root with `g_q | (rho-a)`, set

\[
h_\rho=\operatorname{rem}_{q/g_q}
\left((M/g_q)^{-1}(\rho-a)/g_q\right),
\qquad b_\rho=a+Mh_\rho,
\]

using `h_rho=0` when `q/g_q=1`. The complete fibre is the disjoint union, over those roots, of

\[
\left\{(b_\rho+M_qt,q):
\left\lceil\frac{U-b_\rho}{M_q}\right\rceil
\le t\le
\left\lfloor\frac{V-b_\rho}{M_q}\right\rfloor\right\}.
\]

For a nonprime `q` or one outside `O`, the fibre is empty. For a retained pair, its inverse root is `rho=rem_q(X)` and its inverse lift parameter is `t=(X-b_rho)/M_q`. Thus every input congruence, noncoprime modulus, positivity interval, and specified output class survives. Any further original finite budget predicate is intersected with these same pairs and same lifts; it cannot be replaced by a separately chosen local witness.

**Proof.** A pair lies in the incidence precisely when its input belongs to the original input class and its reduction modulo `q` is a root of `P`. The two-class CRT gives exactly the displayed GCD test, representative, homogeneous kernel `M_q Z`, and inverse parameter. Dividing the original input bounds by positive `M_q` gives the displayed interval. Different roots cannot represent the same input, since an integer has one residue modulo `q`; this proves disjointness and both inverse compositions. The formula for the fibre over an input follows directly by listing the positive prime divisors of that one integer. This proves the entire correspondence without assuming prime-class occupancy.

### Exact return to positive denominators

For every pair in the incidence, the already-computed output class gives the positive integer

\[
D_q=(\Omega+q\Theta)/K_0.
\]

Append the coordinates

\[
a_q=ABD_q,\quad y_q=q^\varepsilon ACD_q,
\quad z_q=qBCD_q,\quad
R_q=4a_q-q=\frac{A+q^{1-\varepsilon}B}{C}>0.
\]

The map appending these coordinates to `(X,q)` is a bijection to its graph, with inverse the retained `(X,q)` projection and singleton fibres. All three denominators are positive integers. The common denominator `qABCD_q` gives the exact numerator

\[
qC+q^{1-\varepsilon}B+A=4ABCD_q,
\]

so their reciprocals sum to `4/q`. Forgetting `X` has exactly the root/CRT fibres computed above. The triple itself recovers

\[
q=\frac{4a_qy_qz_q}{a_qy_q+a_qz_q+y_qz_q}.
\]

This denominator return needs neither a new primality theorem nor an assumption of occupancy. It is a graph construction on every actually retained pair. A further claim that `a_q` lies in a particular bounded shell must retain and prove that additional inequality. It is not part of the weaker positive-seed output proposition.

### A literal source-compatible selected-factor obstruction

Take the normalized seed

\[
p=13,\quad (A,B,C,\varepsilon,D_p)=(1,2,1,1,2).
\]

Then `a_p=4`, `13/4<4<13/2`, `K_0=8`, `Theta=1`, `Omega=3`, and `m=8`. For `D=12`, compatibility holds because `gcd(12,8)=4` divides `p-1=12`; its outputs are precisely `q=13 mod24`.

Retain the actual source input choice

\[
F=13!,\quad M=6F=37362124800,\quad
X=17M=635156121600.
\]

Direct integer division gives `X=3 mod73`. Since `P(3)=81-9+1=73`, the prime `73` divides `P(X)`. Its primality follows from trial division by `2,3,5,7`, the primes at most its square root. It satisfies `73>13` and `73=1 mod12`, but

\[
73\equiv1\pmod8\ne13\pmod8,\qquad
D_{73}=(3+73)/8=19/2\notin\mathbb Z.
\]

Thus this specified cyclotomic prime divisor does not belong to the compatible prescribed output class. All source factorial exclusions and the exact normalized seed are preserved. This does not say that every prime divisor of `P(X)` fails the class.

An independent Python integer computation verified `M`, `X`, all four roots `{3,24,49,70}` of `P` modulo `73`, the exact divisibility, and all residue/seed values. No floating-point calculation, factoring assumption, Lean run, or manuscript edit was used.

## Scope of the finding

The report does not request a universal prime-production or ES theorem. It identifies the narrow concrete incidence missing after the printed distinction and supplies its full solved fibres and positive return. The broader source-normalized propagation and cyclotomic covering research remain outside this bounded subreview. No manuscript, prior review, or other research directory was changed.
