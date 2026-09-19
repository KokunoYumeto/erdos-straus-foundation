# Exact channel coupling and primitive pair fibres

This continuation studies how the original exterior and middle divisor channels
interact after the shifted-factor construction has supplied new prime factors.
It proves several exact structural statements, but it does not prove or disprove
the Erdős--Straus conjecture.

For an original shell (R=4a-p) with (4\mid a), the map

\[
u\longmapsto \frac{a}{4u}
\]

is an involution on its complete integral domain
(\operatorname{Div}(a/4)) and exchanges the tagged exterior and middle gates.
For (a=2^eA), (A) odd, the associated exact exponent windows are
([-2e-2,-2]) and ([-e,e]); their union has (3e+3) integer points.  On
the factor class (a=\ell^e r), where (r) is the unique simple quadratic-
nonresidue prime and every factor of (\ell^e) is a residue, these windows
classify the complete channel counts.  When (4\in\langle\ell\rangle_R),

\[
\bigl|\,|E_a|-|M_a|/2\,\bigr|\le 1.
\]

The two channels also share one exact positive integer source,

\[
\mathcal P_R(N)=\{(b,c):b,c\mid pN,\ R\mid b+c\}.
\]

Every primitive labelled state with (h=N/(rs)) has exactly
(2\tau_{\mathrm{div}}(h)) preimages.  Möbius inversion therefore recovers
the exact tagged count (E+M), while positivity is equivalent to the existence
of one original opposite divisor pair.  In the resulting character formula,
the transported Jacobi character used by the preceding factor-production
argument is annihilated by (|1+\chi(p)|^2).  This proves why factor supply alone
does not establish selector occupancy; it does not assign signs to the remaining
character terms.

Two complete finite controls delimit the result.  At (p=12889), all 22 direct
square sources at (q=43,61) and all 22 corresponding reciprocal sources have
empty required gates.  At (p=315361), the displayed canonical six-cycle has
both channels empty at all 17 valid same-vertex square sources, although an
expanded edge reaches a source with genuine hits.  Neither example is a closed
obstruction in the enlarged system or an Erdős--Straus counterexample.

## Proofs and reproduction

- [Complete workbench](workbench.pdf) and its sources: `workbench.tex`,
  `core.tex`, and `channel_windows.tex`.
- [Channel-window preprint](preprint_windows.pdf) and `preprint_windows.tex`.
- [Pair-transform preprint](preprint.pdf) and `preprint.tex`.
- `MORPHISMS.md`: domains, inverses, fibres, kernels, and information loss.
- `HANDOFF_TURN_6.md`: the exact remaining complete-shell positivity problem.
- `source_reading.json`: cited literature and source-specific lineage.
- `certificates/`: the original finite records used by the checkers.

Run with Python 3.9 or later and a standard LaTeX installation:

```sh
python run_all.py --out reproduced
python run_all.py --optimized --out reproduced_optimized
pdflatex -halt-on-error workbench.tex
pdflatex -halt-on-error workbench.tex
pdflatex -halt-on-error preprint_windows.tex
pdflatex -halt-on-error preprint_windows.tex
pdflatex -halt-on-error preprint.tex
pdflatex -halt-on-error preprint.tex
```

The Type I/II coordinates are attributed to Elsholtz--Tao; quadratic
reciprocity to the cited standard source; and the reciprocal master equation to
Chase Bryan's pinned `FAB-DUAL-DESCENT-SYSTEM.md`.  The proofs rederive every
coordinate identity they use.  No universal nonvanishing theorem, new overall
verification range, Lean build, independent human review, or historical-
priority determination is claimed.

