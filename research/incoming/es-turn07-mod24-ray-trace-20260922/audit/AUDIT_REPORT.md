# Independent audit of the mod-24 ray-trace continuation

Date: 2026-09-22

## Verdict

The continuation's main mathematical results survive independent derivation and certificate replay. The mixed prime-shell return, complete ray-deletion criterion, nine automatic rays, squarefree fibre description, infinite obstruction outside those rays, and all four finite controls are correct under their stated arithmetic hypotheses.

The intake artifact has one definite displayed-formula error: the automatic E-to-M return lists the second denominator as `pHsJr`; it must be `pHJr`. The implemented certificate and the numerical examples already use the corrected denominator, so this is a TeX/PDF error rather than a failed construction.

Several remaining passages need extra hypotheses, explicit orientation data, or narrower evidence wording before publication. None of those changes proves initial source occupancy. The continuation remains conditional on the existence of an E/M trace in the mixed family or on the existence of a trace on one of the nine automatic rays.

No shared or publication file was changed, and nothing was published.

## Input identity and archive containment

- Pasted text: Codex attachment `3149b935-ee80-42c2-8822-1687cd7ded3a/Pasted text.txt`
  - 21,825 bytes
  - SHA-256 `DF2C94E566267E4066BA1844A2C06C52F253F09C33AD6A2F0A71AC3AB2E825B8`
- Outer archive: `Downloads/ES_Turns6_7_With_Mod24_Ray_Trace_20260922.zip`
  - 20,432,359 bytes
  - SHA-256 `5D87C3BFC34630F7D8C9BE4732FB7FE5412322EDDEED375CB388E246255DAAC4`
- Current nested archive:
  - SHA-256 `8318B1BE87DE7104D77316521C1BE5509D59E0D33E59DF55CC25F602E7E2C7C8`
- Predecessor global-receiver cumulative archive:
  - SHA-256 `BA225DC9F046B1D359DFB16CB5E62D83312CDA978E84B79DD2B6B78CCBA60D6E`

The outer archive has four entries. A recursive in-memory audit reached 18 unique nested archives, read 87,800,726 nested bytes, and found no absolute paths, drive-qualified paths, parent traversal, duplicate member names, symlink members, or suspicious compression ratio above 1000. The current archive contains 33 payload files plus `MANIFEST.json`; every listed size and SHA-256 digest agrees, and no extra payload exists.

`source_history.bundle` passes `git bundle verify`, contains complete history, has head `733f675...`, parent `dcf140...`, and tree `342b...`. Its 25 additive patch files agree with the extracted current files after newline normalization. The integration patch passes `git apply --check` against the present project checkout and was not applied.

## Definite formula correction

Locations in the supplied intake:

- `core.tex:194`
- `preprint.tex:95`
- pasted text near line 251
- rendered `workbench.pdf`, page 3
- rendered `preprint.pdf`, page 2

The automatic return is

\[
(h_M,r_M,s_M,\lambda_M)=(H,s,J,r),\qquad
a_M=HsJ,\qquad u_M=Hs^2.
\]

The general M denominator formula therefore gives

\[
(x_M,y_M,z_M)
=
(a_M,\;p h_M s_M\lambda_M,\;p h_M r_M\lambda_M)
=
(HsJ,\;pHJr,\;pHsr).
\]

The supplied display has `pHsJr` in the second coordinate, with an extra factor `s`. For the `p=6841` example the correct coordinate is `7,867,150`; the erroneous expression gives `23,601,450` and does not satisfy the reciprocal identity. The implementation at `check_independent.py:59` and the numerical output use `pHJr`.

Recommended change: replace `(HsJ, pHsJr, pHsr)` by `(HsJ, pHJr, pHsr)` in both TeX sources, rebuild both PDFs, and add a direct symbolic assertion of all three denominator formulas to the independent checker.

## Remaining TeX and proof changes

### 1. State the radical consequence of the square gate

At `core.tex:108` and `preprint.tex:58`, the proof should not suggest that the square gate gives `R\mid G_c`. What it gives is

\[
R\mid G_c^2\quad\Longrightarrow\quad \operatorname{rad}(R)\mid G_c.
\]

This is precisely enough for the primewise Legendre-symbol argument. The stronger divisibility is false for proper traces: at `p=1129`, `R=7^2\cdot11` and `G_E=5005=5\cdot7\cdot11\cdot13`, so `R\mid G_E^2` but `R\nmid G_E`.

Recommended replacement: “For every prime `ell\mid R`, the square gate implies `ell\mid G_c`; equivalently `rad(R)\mid G_c`.”

### 2. Include the coprimality used in the deletion converse

At `core.tex:135-137`, the converse multiplies a congruence by `k`. State that `k` is a positive divisor of `R` and

\[
\gcd(k,m)=1,
\]

because `\gcd(R,m)=1`. This makes multiplication by `k` reversible modulo `m=4rs`.

### 3. Include the unit hypothesis in the fibre sufficiency proof

At `core.tex:218-219`, define `A` as the odd part of `T=pr+s` and state

\[
\gcd(A,m)=1.
\]

It follows from `\gcd(T,4rs)=1`. Hence every allowed `t\mid A/\delta` is a unit modulo `m`, and on an automatic ray `t^2\equiv1\pmod m`. This is the missing written justification in the sufficiency direction.

### 4. Make exterior orientation and inverse data explicit

The theorem at `core.tex:16-17` promises explicit inverses for all input orderings. The prose does not fully display them.

For an E input whose original tails were exterior-swapped, the returned M word must also be complemented:

\[
u_M^{\vee}=\frac{a_M^2}{u_M}=HJ^2.
\]

This reverses the returned M tails. The repair implementation already records this orientation bit.

For an M-branch output, retain both the exterior-swap bit `\varepsilon` and the squarefree-fibre parameter `t`. Recover first

\[
u_0=\begin{cases}
u_{\rm out},&\varepsilon=0,\\
a'^2/u_{\rm out},&\varepsilon=1,
\end{cases}
\]

and then recover the source word from `u_0` or `a^2/u_0` according to whether the middle complement was used. Without `t`, the section only recovers the squarefree representative rather than the original trace.

### 5. Expand the middle-complement step

At `core.tex:250`, write the two facts used by the argument:

- complementing `u` to `a^2/u` preserves the middle square gate;
- in the M trace parametrization, `\gcd(R,G_M)=\gcd(R,r+s)`.

This closes the written bridge from the valuation dichotomy to squarefree descent.

### 6. Separate source and target basis notation

At `core.tex:227`, use distinct symbols for the bounded source basis and squarefree target basis, for example

\[
e_{\delta,t}\longmapsto f_\delta,
\qquad
\ker=\left\langle e_{\delta,t}-e_{\delta,1}:t>1\right\rangle.
\]

Writing both as `e` obscures the actual split map. The target section is `f_\delta\mapsto e_{\delta,1}`.

### 7. Narrow three descriptions

- At `core.tex:373`, replace “original integer source” by “original proper E trace source with integral shell coordinates”; its two tails are deliberately nonintegral.
- At `core.tex:420`, replace “243 original square divisors” by “243 divisor words `u\mid a^2`.”
- For the `p=6975049201` shell, say “both original full gates are empty.” Its relaxed E square gate is occupied.

### 8. Keep the `p=9601` conclusion rule-specific

The example refutes the attempted extension of the squarefree-target deletion rule from `c\mid6` to `c=4`. It is not a counterexample to the Erdős–Straus equation, to every source-changing map, or to every residual reduction. Keep that scope in `claims.json`, the TeX prose, captions, and any abstract.

### 9. Repair source links before publication

`references.tex:19-20` names the earlier Trace/Word and divisor-descent sources only by internal identifiers. The project rule requires a clickable public proof file and a precise theorem, equation, or line locator. The sharp-receiver source is currently untracked locally and is not part of this bundle, so no live citation should be claimed until that proof is actually public.

## Independent derivation of the main results

### Rational integral-trace factorization

If positive rational tails `y,z` have integer sum `N` and satisfy

\[
\frac1y+\frac1z=\frac4p-\frac1a=\frac{R}{pa},
\]

then their reduced denominators agree. Writing that denominator as `d`, the product relation gives `d^2\mid R`, more exactly

\[
d^2=\frac{R}{\gcd(R,N)}.
\]

With

\[
b=Ry-pa,\qquad c=Rz-pa,
\]

one obtains positive integers satisfying `bc=(pa)^2`. Splitting the `p`-valuation as `(0,2)`, `(1,1)`, or `(2,0)` reconstructs an E word or an M word `u\mid a^2`, up to exterior swap. Thus the factorization exhausts rational tails with integral sum; it does not merely give examples.

The trace sums and square gates are exactly

\[
S_E=\frac{(a+pu)^2}{Ru},
\qquad
S_M=\frac{p(a+u)^2}{Ru}.
\]

### Prime character restriction

For every prime divisor `\ell` of `R`, the square gate forces `\ell\mid G_c`. Multiplying the local symbols, with the centered exponent parity preserved, gives

\[
\left(\frac{u}{p}\right)=-1\quad(E),
\qquad
\left(\frac{u}{p}\right)=-\left(\frac ap\right)\quad(M).
\]

For `p\equiv1\pmod{24}`, both `2` and `3` are quadratic residues. If `a=cq`, `c\mid6`, and `q>3` is prime, then `q` is a nonresidue. In the E case this forces `v_q(u)=1`, so `rs\mid c\mid6` and the source lies on one of the nine automatic rays. In the M case `v_q(u)` is `0` or `2`; complementing when it is `2` produces `u_0\mid c^2\mid36`, hence `4K(u_0)\mid24`, and the squarefree descent gives the full M state.

Properness gives `t>1` and `\delta<R`, so every claimed strict residual decrease is valid.

### Complete ray-preserving deletion criterion

For an E trace on ray `(r,s)`, set

\[
m=4rs,\qquad T=pr+s,
\qquad d=\frac{R}{\gcd(R,T)}.
\]

For a positive `k\mid R`, deletion to residual `R/k` succeeds on the same ray exactly when

\[
d\mid k,
\qquad
k\equiv1\pmod m.
\]

Indeed, `R/k\mid T` is equivalent prime by prime to `d\mid k`. The shell condition is

\[
m\mid p+R/k
\iff m\mid pk+R
\iff m\mid p(k-1)
\iff k\equiv1\pmod m,
\]

using `\gcd(p,m)=\gcd(k,m)=1`. The returned coordinates are

\[
h'=\frac{p+R/k}{m},\quad a'=h'rs,
\quad u'=h'r^2,
\quad \kappa'=\frac{T}{R/k}.
\]

If `k>1`, then `a'<a`; centered divisor-exponent coordinates are unchanged. The group-ring coefficient count is therefore exact.

### Automatic rays and fibres

All unit squares modulo `m=4rs` equal `1` exactly when `m\mid24`. Consequently the primitive automatic rays are precisely the nine coprime ordered pairs with `rs\mid6`.

Write the trace residual as

\[
R=\delta t^2,
\]

with `\delta` squarefree. The trace gate implies `\delta\mid T`. On an automatic ray `t^2\equiv1\pmod m`; since `R\equiv-p\equiv-1\pmod m`, this gives `\delta\equiv-1\pmod m`.

For `A=\operatorname{oddPart}(T)`, the exact fibre is

\[
\delta\mid\operatorname{rad}(A),\quad
\delta\equiv-1\pmod m,
\quad t\mid A/\delta,
\quad \delta t^2<p.
\]

Every such `\delta` is already below `p`, so `t=1` gives the section.

For the squarefree representative, put

\[
H=\frac{\delta+1}{m},\qquad J=\frac{T}{\delta}.
\]

Then

\[
(h_M,r_M,s_M,\lambda_M)=(H,s,J,r),
\]

with

\[
R_M=\frac{s+J}{r},\qquad
a_M=HsJ,\qquad u_M=Hs^2,
\]

and identities

\[
r_M+s_M=rR_M,\qquad
p+4u_M=\delta R_M,\qquad
4a_M-R_M=p,\qquad 0<R_M<p.
\]

Its correct denominators are `(HsJ,pHJr,pHsr)`.

### Infinite obstruction outside the nine rays

The theorem is sound. For a fixed coprime ray with `rs\nmid6`, choose a unit `b\pmod m` with `b^2\not\equiv1\pmod m` and change sign so `b\equiv1\pmod4`. Dirichlet supplies primes

\[
t\equiv b\pmod m,
\qquad
\delta\equiv-b^{-2}\pmod m
\]

beyond the listed size exclusions. With `R=\delta t^2`, `L=\operatorname{lcm}(840,m)`, and a further prime `e\equiv3\pmod4`, the three CRT conditions are pairwise compatible and form a reduced class modulo `LRe`. Dirichlet then supplies infinitely many primes `p` in that class.

The resulting source

\[
h=\frac{p+R}{m},\qquad a=hrs,\qquad u=hr^2
\]

has exact defect `d=t`. The only deletion candidates are

\[
t, t^2, \delta t, \delta t^2,
\]

and none is `1\pmod m`. The size inequality gives `4K(u)>R`, excluding inherited fixed-word deletions. The complement fails the relaxed E gate modulo `\delta`. Nevertheless the independent endpoint M state

\[
(h_M,r_M,s_M,\lambda_M)=(H,1,J,1),
\quad H=(e+1)/4,
\quad J=(p+1)/e
\]

is exact, has denominators `(HJ,pHJ,pH)`, and has `3\le J+1<p`.

This proves optimality only for the supplied E-ray and inherited residual-divisor guarantees. It does not assert failure of every source-changing mechanism or failure of the Erdős–Straus equation.

## Finite examples and negative controls

### `p=6975049201`, ray `(5,3)`

All displayed arithmetic checks:

\[
R=71\cdot73^2=378359,
\quad h=116257126,
\quad a=1743856890,
\quad u=2906428150.
\]

Moreover

\[
\gcd(R,5p+3)=71\cdot73=5183,
\qquad d=73,
\]

so the source is a proper trace. The complete factorization

\[
5p+3=2^3\cdot71\cdot73\cdot841097
\]

has prime `841097`. The eight odd-divisor residues modulo `60` are

\[
\{1,7,11,13,17,23,31,41\},
\]

which omits `59`; the genuine `(5,3)` ray has no full first-half E residual. The four deletion factors `73,5183,5329,378359` are `13,23,49,59\pmod{60}`, so none is allowed. Directly, `4K(u)=2325142520>R`, which proves the fixed-word obstruction even though this finite prime lies below the coarse threshold in the infinite theorem.

Since

\[
a=2\cdot3\cdot5\cdot293\cdot198391
\]

is squarefree, there are exactly `3^5=243` divisor words `u\mid a^2`; exhaustive enumeration finds neither full gate. The M target is already absent modulo `73`, and the nine E-compatible words modulo `73` all fail modulo `73^2`.

Primality is independently certified from

\[
p-1=2^4\cdot3\cdot5^2\cdot7\cdot830363
\]

using base `11` with full multiplicative order; trial division through `83516` agrees. The alternative middle state `(3,1,634095382,1)` and its three denominators are correct.

### `p=9601`

The source `a=2956`, `R=2223`, `u=8` is a proper M trace of defect `3`. At the squarefree target `a'=2462`, `R'=247`, the complete nine-word residue set is

\[
\{1,2,4,16,32,64,231,239,243\},
\]

omitting E target `185` and M target `8`. The alternative `R=19,u=65` M solution is correct. The complementary source orientation `u^*=1092242` is another proper M orientation; its omission from the isolated certificate is not a mathematical error.

### `p=2521` and `p=3361`

Independent exhaustive counts agree:

- `p=2521`: 194 shells, 1,542 divisor words, 3,084 gate tests, zero mixed traces.
- `p=3361`: 250 shells, 1,998 divisor words, 3,996 gate tests, zero mixed traces.

At `p=3361`, all nine automatic-ray target sets are empty. This does not mean its full atlas is empty: `a=841`, `R=3`, `u=29` gives both a full E and a full M state outside the nine rays. Likewise `p=2521` has an occupied automatic ray `(1,2)` at `R=87`; it lies outside the mixed initial family.

## Certificate replay and evidence limits

`python run_all.py --bound 10000 --directory ...\replay\reproduced` completed all six subprocesses successfully in about ten seconds. It reproduced:

- 143 primes `p\equiv1\pmod{24}` through 10,000;
- 171,732 shells;
- 5,616,298 original words;
- 5,788 E traces and 5,678 M traces;
- 3,637 full E and 3,910 full M states;
- 2,151 proper E and 1,768 proper M traces;
- 806 mixed traces, 254 proper;
- 1,230 automatic-ray traces, 409 proper;
- 126,013 main checks;
- 254,919 independent checks;
- 1,612 ordered interface inputs and two intended rejections.

Normal and optimized JSON agree. Windows line endings change raw byte hashes, but universal-newline canonicalization reproduces the supplied LF hashes for all five mathematical output files and makes the repair/interface artifacts byte-identical. Timing fields are the only expected differences in summary files.

A third checker, written without importing the supplied implementation, independently reproduced 806 mixed traces and 254 proper traces, verified the `2521`, `3361`, `9601`, and `6975049201` controls, and exposed the erroneous displayed E-to-M denominator in 141 automatic E cases with `s>1`.

Evidence wording should nevertheless be narrowed:

- `examples.json` stores 444 shell records with `traces: []`; it does not serialize every failed candidate word and residue. Replace “full original tables” by “complete shell list with empty-trace results, reproducibly enumerated by the verifier,” or serialize the full failures.
- The isolated `p=9601` loop checks all entries in its supplied target list but does not prove inside that block that the list is complete. Either enumerate all divisors from the factorization in that block or say the completeness is established by the main exhaustive verifier.
- The isolated `p=9601` and large-prime blocks do not directly assert the source square gates. Add those assertions.
- The large-prime primality output should serialize the modular powers and gcd witnesses that its checker recomputes, if the JSON is intended as a standalone certificate.

## Relation to the existing receiver modules

### Global-sign receiver

The current global-sign theorem is at

`research/incoming/es-turn07-global-receiver-determinant-20260921/core.tex:12-39`.

It applies to every existing integral witness for `p\equiv1\pmod{12}` and supplies the stated determinant/inverse bounds; in the `p\equiv1\pmod{24}` branch it uses

\[
c_{24}=\frac{327448292668}{47045881}.
\]

The mod-24 continuation supplies an integral M state from a trace on an automatic ray and, in the mixed E branch, also supplies an integral E state. After that return, the global-sign theorem applies literally. It does not apply to the nonintegral tails before repair and cannot force an initial trace or an occupied source shell.

### Sharp receiver and growth

The current sharp theorem is at

`research/incoming/es-turn07-sharp-receiver-growth-20260921/core.tex:75-103`.

It uses

\[
c=\frac{80}{6279^4}
\]

and proves the quoted bounds for the inverse norm, exterior powers, determinant inverse, and rank-one remainder. Once the mod-24 return has produced an integral witness with a unique smallest first-half denominator, those bounds apply.

For an automatic E-source middle output, since `J>s`, sort the returned tails as

\[
Y=pHsr,\qquad Z=pHJr.
\]

Then the sharp-receiver parameters are

\[
b=Hsr,\qquad c=HJr,\qquad R=R_M,\qquad w=p/R_M.
\]

The accompanying returned E state has residual `\delta` and `w=p/\delta`. For an M-source squarefree output the residual is likewise `\delta` and `w=p/\delta`.

There is no converse implication: both receiver modules start from an existing integral witness. They do not establish occupancy of the mixed family or of an automatic ray. In addition, the sharp module's exponent-optimality families lie in `p\equiv13\pmod{24}`, so its optimality conclusion must not be advertised as an optimality theorem internal to `p\equiv1\pmod{24}`.

The sharp module is untracked in the present checkout and absent from the mod-24 bundle's history. The mod-24 patch is additive in a separate directory, so there is no file-level conflict, but a later integration needs an explicit public cross-reference once both proofs are published.

## Publication gate

Before this continuation is merged or published:

1. Correct the E-to-M denominator in both TeX sources and rebuild both PDFs.
2. Replace the square-gate wording by the radical statement.
3. Add the coprimality, fibre-unit, complement-preservation, orientation, and retained-`t` steps listed above.
4. Tighten the example and certificate descriptions to their actual scope.
5. Add direct symbolic denominator and source-gate assertions to the independent checker.
6. Add public, pinned proof links and exact locators for the earlier modules when those links exist.

After these changes, the continuation is mathematically fit as a conditional trace-to-integral-return theorem with exact finite controls. It is not a proof that every unresolved prime has a trace source, nor a proof of the full Erdős–Straus conjecture.
