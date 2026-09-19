# Complete-shell spectral bounds and exact collision certificates

This continuation attacks the complete first-half opposite-divisor-pair sum at
an arbitrary prescribed prime.  It does not prove universal Erdős--Straus
occupancy.  It proves that a broad proposed adverse-sign lower estimate fails
quantitatively, and it gives exact nonprincipal repairs that recover original
solutions in cases missed by the scalar estimate.

For (p\equiv1\pmod4), (p\ge2^{20}), let (I_p=\{a:p/4<a<p/2\}),
(R_a=4a-p), and let (T_a) count ordered pairs (b,c\mid pa) with
(R_a\mid b+c).  The inherited gcd inverse proves

\[
\operatorname{ES}(p)\quad\Longleftrightarrow\quad
\sum_{a\in I_p}T_a>0.
\]

Writing (c_a(g)) for the original divisor multiplicity in a unit residue,
(\mathcal E_a=\sum_g c_a(g)^2), and
(P_a=4\tau_{\mathrm{div}}(a)^2/\varphi(R_a)), the principal/adverse-sign
lower bound is (L_a=2P_a-\mathcal E_a).  The principal-domination theorem
proves

\[
\sum_{a\in I_p}L_a\le-\frac1{24}p\log p.
\]

The statement extends to any shellwise choice of at most (J) even character
modes when (p\ge2^{20}J^3), and an all-exponent divisor bound gives an explicit
obstruction for every fixed sublinear mode budget.  These are upper bounds on a
specified valid lower estimate, not upper bounds on the true target count.  The
true signed character sum cancels the diagonal contribution that this estimate
loses.

A surviving theorem retains actual nonprincipal information.  For any
observation subgroup (B\le(\mathbb Z/R_a\mathbb Z)^\times) containing (-1),
the exact integer coset masses and collision energy give a sharp balanced-
integer lower bound for (T_a), strengthened by a free Klein-four action on the
original target-pair set.  At (p=944329,R=63), an unsaturated cubic quotient
attains (T_a=8).  At (R=47), where no intermediate subgroup is available, a
proper selection of five of the 23 even character modes proves (T_a\ge60),
which is attained; its two nonprincipal energies have independent exact rational
interval certificates.  At (p=87481), every scalar shell bound is nonpositive
although 34 shells are occupied, disproving every nonnegative reweighting of
that scalar certificate family.

## Proofs and reproduction

- [Complete workbench](workbench.pdf), `workbench.tex`, `core.tex`, and
  `references.tex`.
- [Short preprint](preprint.pdf) and `preprint.tex`.
- `ATTEMPT.md` and `HANDOFF_TURN_7.md`: attempted estimates, exact failures,
  surviving sufficient quantities, and the remaining universal inequality.
- `MORPHISMS.md` and `claims.json`: typed maps and claim dependencies.
- `source_reading.json`: exact literature and project lineage.
- `certificates/`: finite full-shell, principal-census, complement, and spectral
  certificates.

```sh
python verify.py --bound 3000 --hard-bound 2000000 --out reproduced
python -O verify.py --bound 3000 --hard-bound 2000000 --out reproduced_optimized
python check_independent.py --input reproduced --out reproduced/independent.json
pdflatex -halt-on-error workbench.tex
pdflatex -halt-on-error workbench.tex
pdflatex -halt-on-error preprint.tex
pdflatex -halt-on-error preprint.tex
```

The finite comparison covers a certificate method, not a new overall ES
verification range.  The universal assertion
(\sum_{a\in I_p}T_a>0) remains unproved.  No Lean build, independent human
review, or historical-priority determination is claimed.

