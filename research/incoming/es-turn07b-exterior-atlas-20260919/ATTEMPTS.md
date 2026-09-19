# Exterior-atlas attempt ledger

This ledger records what each calculation was intended to establish, what
survived, and what did not. It is not a substitute for the proofs in
[core.tex](core.tex).

## Transfer the middle square-root cutoff

- **Aim.** Use the earlier middle bound unchanged for the exterior residual
  \(R\) or exterior cofactor \(D\).
- **Reason.** Both channels arise from the same ordered unit-fraction equation,
  so a common small outer coordinate would have yielded one uniform atlas.
- **Result.** The proposed transfer is false. At the prime \(p=48049\), the
  original exterior state has \(R=D=311\), while the middle cutoff is \(247\).
- **Surviving relation.** Both channels retain exact maps back to the same
  ordered equation, but the exterior channel has its own complement–norm
  identity and cubic cutoff.

## Bound the least of three retained exterior coordinates

- **Aim.** Preserve \(R\), \(D=(4u+1)/R\), and \(v=a^2/u\), then prove a bound
  for \(\min\{R,D,v\}\).
- **Result.** Successful. The exact identity
  \((p+R)^2+4v=4vRD\), the strict inequality \(p+R<2vD\), and the
  nonidentities \(v\ne R,D\) yield
  \[
  (p+w)^2>4(w+1)^2(w-1),\qquad w=\min\{R,D,v\}.
  \]
- **Boundary.** The strict sign depends on \(p\equiv1\pmod4\). The positive
  state at \(p=19\) gives equality outside that residue hypothesis.
- **Sharpness.** The family \(p=16n^3-4n^2-8n+1\) has
  \(C(p)=4n^2-2\), so the \(p^{2/3}\) scale and leading constant are real on the
  stated integer source domain.

## Direct residual inversion

- **Aim.** Reconstruct every state whose least retained coordinate is \(R\).
- **Result.** Successful with the full positive divisor fibre:
  \(a=(p+R)/4\), \(u\mid a^2\), and \(R\mid4u+1\), retaining
  \(R\le D\) and \(R<v\).
- **Exact inverse.** \((R,u)\leftrightarrow(a,u)\) through \(R=4a-p\).
- **Dependency.** The generative converse uses primality to obtain
  \(\gcd(p,a)=1\). Composite \(p=21\) is an exact counterexample if that
  dependency is removed.

## Reciprocal cofactor inversion

- **Aim.** Reconstruct every state whose least retained coordinate is \(D\).
- **Result.** Successful from
  \[
  B_D=\frac{pD+1}{4},\qquad
  w\mid B_D^2,\qquad w<B_D,\qquad D\mid w+B_D.
  \]
  The gcd normalization recovers \(h,r,\kappa,s,a,u,R,v\) and proves all
  original source conditions.
- **Orientation retained.** The complementary divisor corresponds to the
  opposite \(r,\kappa\) orientation and is not silently identified with this
  chart.
- **Dependency.** Composite \(p=93\) passes the displayed arithmetic data but
  reconstructs \(a=30\) with \(\gcd(p,a)>1\).

## Norm-divisor chart without square-divisor availability

- **Aim.** Generate the complement chart from \(R\mid p^2+4v\) alone.
- **Result.** Failed. Norm divisibility does not imply that
  \(u=a^2/v\) is an integer.
- **Exact repair.** Retain
  \[
  K(v)=\prod_{\ell^e\parallel v}\ell^{\lceil e/2\rceil},
  \qquad R\equiv-p\pmod{4K(v)}.
  \]
  This is exactly \(K(v)\mid a\), equivalently \(v\mid a^2\).
- **Dependency.** Primality and \(R<p\) are used to prove
  \(\gcd(R,4v)=1\) before cancellation. Composite \(p=25,v=5,R=15\) shows
  the failure when that unit is absent.

## Coprimality and tie shortcuts

- **Rejected shortcut.** \(\gcd(v,D)=1\) is false; \(p=37\) gives
  \((v,D)=(18,3)\).
- **Correct cancellation.** In the norm chart, \(\gcd(R,4v)=1\) follows from
  norm divisibility, primality, and \(R<p\).
- **Tie correction.** The sentence “\(R=D\) is direct” was too strong.
  Precisely, \(R=D<v\) is direct, while \(v<R=D\) is norm. The smallest
  witnesses occur at \(p=13\) and \(p=5\).

## Force the least permitted complement grade

- **Aim.** Use the arithmetically smallest available \(v\) as a universal
  selector.
- **Result.** Failed as a universal rule. At \(p=2521\), the lane \(v=11\)
  requires a divisor \(R\mid6355485\) in one residue class modulo \(44\), and
  none exists below \(p\). The factorization and Lucas certificate in
  core.tex make this failure complete.
- **Surviving use.** It is a negative control for future monotonicity or
  extremal-grade arguments; it is not an Erdős–Straus counterexample because
  other grades and the middle channel remain.

## Infer infinitely many prime members of the sharp family

- **Aim.** Upgrade integer-domain sharpness to a prime-domain sharpness theorem.
- **Result.** Not established. The exact congruence classification is
  \[
  p(n)\equiv289\pmod{840}
  \Longleftrightarrow n\equiv24\ \text{or}\ 164\pmod{210},
  \]
  but this does not prove infinitely many prime values of the cubic.
- **Retained theorem.** Exact integer-source sharpness and the individual prime
  examples \(p=97,929\).

## Present use

The exterior and middle atlases now classify every possible original state at a
fixed prime by exact inverse coordinates. Their union can still be empty.
Future work must establish structural occupancy or certify a genuinely finite
exceptional-prime domain; another localization bound is not a substitute for
that nonvanishing theorem.
