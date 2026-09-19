# Turn 2 route record: shifted-factor closure

This file records why the shifted-factor graph was introduced, what was proved,
and where the route stopped. The complete arguments and coordinates are in
`core.tex`; this is not a substitute for them.

## Complete factor graph rather than a selected successor

The inherited external-nonresidue construction associates to each eligible
prime vertex (q) the integer

\[
A_q=(p+\sigma_q q)/4,
\qquad
\sigma_q=1\ (q\equiv3\bmod4),\quad
\sigma_q=3\ (q\equiv1\bmod4).
\]

The attempted descent had previously selected one factor. Turn 2 instead
retains every eligible nonresidue prime factor (r\mid A_q), its valuation,
the full original square-divisor box of (A_q^2), and both (E/M) gates. This
produces a finite directed multigraph with exact arithmetic labels.

Outcome: the greatest closed set of locally failed vertices is decidable by the
decreasing sequence (U_{j+1}=\{q\in U_j:N^+(q)\subseteq U_j\}). It is nonempty
exactly when a sink strongly connected component contains only failed vertices.
A vertex removed at rank (j) has a strictly rank-decreasing path to an actual
gate hit. This is a closure theorem for the finite graph at fixed (p), not a
uniform proof that the terminal set is empty.

## Local-closure conjecture and its counterexample

The proposed implication “every canonical closed component contains a local
selector hit” is false. At (p=2521), the seven vertices

\[
11\to211\to683\to89\to17\to643\to113\to11
\]

form a sink component of the complete graph. Every displayed successor is the
only eligible one and every complete local (E/M) selector is empty. The 75
original divisor vectors and their 71 support positions remain distinct in the
certificate. This does not refute Erdős--Straus: the same prime has a middle
solution at (R=23,u=8), and a separately marked multiplier (5) repairs the
failed (q=11) source.

The same calculation gives a closed failed six-cycle at (p=3361) beginning at
an effective-index-six vertex, and completes the known (p=808369) consecutive-
sextic component. These examples rule out local closure and defect-index growth
as well-founded descent invariants. They do not rule out enlarging the source.

## Transition and cycle-coordinate attempts

For every edge (q\to r), with (m=v_r(A_q)), (B=A_q/r^m), and
(c=r^{m-1}B), the exact transport is

\[
p+\sigma_qq=4cr,
\qquad
4A_r=(4c+\sigma_r)r-\sigma_qq.
\]

The common word domain is exactly
(\operatorname{Div}(\gcd(A_q,A_r)^2)); the exponent translation, both gate
translations, and the modulus change are all retained. No homomorphism between
the two different residue groups follows from the edge alone.

Composing the affine equations around a simple cycle gives
(Dq_i=S q_i+pT_i). With (h=\gcd_iT_i), the inverse candidates are
(p=(D-S)/h) and (q_i=T_i/h). This is an integral inverse for an ordered
coefficient word. Primality, ranges, edge types, factorizations, and all local
gates remain separate converse tests; arbitrary coefficient words are not
asserted to define cycles.

## Exact stopping point

Turn 2 disproves the canonical local/cycle implication and therefore changes
the next route. A remaining proof must either show that not every vertex is
trapped after a precisely specified source enlargement, or construct an exact
escape from the original arithmetic data. Turn 3 consequently studies the
smallest primitive sextic obstruction instead of assuming closed-component
occupancy.

