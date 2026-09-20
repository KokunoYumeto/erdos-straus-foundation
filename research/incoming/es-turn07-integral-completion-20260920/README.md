# Turn 7: the original integral signed completion

This tranche incorporates the supplied literal-root rank-eight completion into
its original arithmetic domain. It remains part of the unresolved Turn 7
existence task. No universal ES or Type-II existence statement is assumed.

## Results

For every original E/M state at a prime p = 1 mod 12, the signed completion
Z_p[T,eta]/(H,eta^2-H') has normalization index p^2 in E and p^9 in M. The
original conductors, all eight Smith exponents, T/eta actions, integral inverse
and reduction kernels are explicit. The E boundary point (0,0) has p lifts
modulo p^2 and none modulo p^3. Literal generic local fibres have 0 or 4 rational
points in E, and 4 or 8 in M. These are not the earlier reciprocal cubic fibres.

The labelled prime-only deck sign has a denominator of exact p-order 1 (E) or
2 (M). Its generic existence does not preserve the original integral order.
Literal E/M root interpolation is integral in one direction and has exact
p^2 denominator loss in the other. A reciprocal coordinate change includes a
specified quadratic twist. The supplied analytic Gamma conductor is never
identified with these finite-order conductor ideals.

For any prescribed finite set of primes, an explicit prime progression gives
joint numerical E/M sources with both gates, original size bounds and local
signatures, but one forbidden prime occurrence prevents u from dividing a^2.
Their two rational denominator triples each fail integrality at exactly that
prime. The same primes have separately exhibited genuine integer solutions.
This is a test of a proposed certificate criterion, not an ES counterexample,
not an all-place obstruction, and not a rejection of an adaptive complete
arithmetic test.

## Files

- `workbench.tex`, `core.tex`, `preamble.tex`, `bibliography.tex`: complete proof.
- `preprint.tex`: short standalone normalization/boundary preprint.
- `crt_control_note.tex`: an additional complete CRT-control proof fragment;
  not part of the main manuscript, and not substituted for its simpler joint
  one-prime construction.
- `verify.py`: original square-divisor enumeration and exact local algebra.
- `check_independent.py`: separate primitive-source and all-minors checker;
  imports neither the main verifier nor predecessor software.
- `certificates/`: complete labelled scan rows, exact rational examples,
  full normalization and action matrices, source hashes and check outcomes.
- `MORPHISMS.md`: domains, inverse coordinates, fibres and information loss.
- `HANDOFF_TURN_7_REMAINDER.md`: the remaining original occupancy obligation.
- `source_reading.json`: actual input versions, hashes, primary references
  and content-search scope. No priority claim.
- `claims.json`, `INTEGRATION_AUDIT_20260920.md`: stable claim records and
  the exact cross-chart audit.
- `figures/integral-normalization-smith.pdf`: reproducible visual account of
  the normalization matrix and both Smith-factor lists.
- `antecedent/`: unchanged source snapshots for local reproducibility; these
  are not assertions that all historical work has been independently audited.
- `publication_receipt.json`: actual remote/local publication distinction.

The current literal roots are (p,x,y,z), not (infinity,p/x,p/y,p/z). This
change of arithmetic chart is explicitly calculated; it changes integral
orders and the signed square class.

## Reproduce

Python 3, standard library only:

```
python verify.py --bound 3000 --out certificates
python -O verify.py --bound 3000 --out certificates_optimized
python check_independent.py --input certificates --out certificates/independent.json
```

The complete bound-3000 domain has 99 primes p=1 mod12, 868359 original square
divisors and 4505 labelled states (2451 E, 2054 oriented M). These are verification
inputs, not a new overall ES computational range. The deep matrix examples and
rational-control targets have their own explicit scope.

Build the PDFs with two runs of `pdflatex -interaction=nonstopmode
-halt-on-error workbench.tex`, and likewise for `preprint.tex`. No font files
are distributed. The final release receipt records compilation and fresh
extraction replay separately from mathematical proof.

## Interpretation

Finite flatness preserves rank, not the original integral lattice or the
existence of a section. An added nilpotent boundary state is not an original
square-divisor word. The exact torsion modules measure the loss; they are
modules, not quotient rings. The supplied same-grade capacity theorem remains
valid and complete at its scope. The new results do not repair its genuinely
empty boxes by relabelling an absent divisor.
