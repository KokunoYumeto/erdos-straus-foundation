# Original trace defects and factor-sum/Pell returns

This continuation remains at the original-source existence boundary (roadmap
Stage 6--7). It does not prove universal Erdős--Straus occupancy. It uses the
integrated source at `20709bee872ad10e4cc7d7b976d975e24532a803`, rather than an
uncorrected earlier receiver handoff.

Read `workbench.pdf` (complete proof), `core.tex` (integration source), and
`preprint.pdf` (short self-contained account of the factor-sum return, its
prime-square Pell specialization, and the distinct fixed-tail-sum fibre). The
full theorem for arbitrary primitive r, including the target gcd and complete
incoming fibres, is in the workbench. No full Lean build is claimed.

## Results and domains

The complete original rational E/M trace source, with u dividing a^2, has an
exact additive defect c in Z/D, where R=KD, K is the least integer whose square
is divisible by R, and D divides K. The ideal K Z/R has square zero. The complete
original exponent box is partitioned into finite geometric coefficient
polynomials; no original multiplicity or actual factor is replaced by subgroup
membership. Exact mixed-channel laws, coefficient stabilizers, and a sharp
unit-direction saturation threshold are proved.

All original prime-power M trace exponents are classified. For a=q^2 with p and
q prime and p=1 mod24, every proper M trace has both original full gates empty
at that shell and no old fixed-word or fixed-ray residual-divisor return. A new
map retaining h+s and raw r changes h and s oppositely by delta*w. Its exact
quadratic equation, positivity, primitive gcd normalization, and full incoming
fibres are proved. For r=1,h=s=q this equation is Pell. Three isolated hard-prime
examples and a general r=2/gcd=2 example have exact returns. Infinite integer
Pell parameters are constructed; infinite prime values are not asserted.

A complete finite certificate proves that 67369 is the least prime p=1 mod24
whose first rational trace precedes every original full gate. Therefore a
universal repair from every trace cannot require the distinguished denominator
to decrease or stay unchanged. This is a counterexample to that termination
invariant, not to ES.

A second exact classifier retains the numerical tail sum N=Y+Z, rather than
the raw factor sum h+s. Its ordered integral targets are in bijection with the
residual divisors rho of N satisfying one exact discriminant square, positivity
and parity. Splitting rho into its squarefree part gives a Pell lattice with
essential divisibility gates. At p=67369 all 69 proper original trace tags,
with 51 distinct tail sums, have empty integral fixed-sum fibres. The
certificate tests 507 eligible residuals; this does not obstruct maps that
change Y+Z and does not prove or refute ES.

There is also a universal prime-square obstruction inside this fibre. For any
proper E or M trace at a=q^2 with word q or q^3, no integral target retaining
the same numerical tail sum can have residual a proper divisor of the source
residual. The proof exhausts all target words and both channels. It does not
exclude a smaller residual that does not divide the source residual, and it
does not apply after changing the numerical tail sum. A separate finite
checker reconstructs the canonical gcd data and tests every eligible proper
divisor in the serialized prime-square scope.

## Reproduce

Python 3.9 or later, standard library only:

    python run_all.py --directory reproduced

The default scopes are: every original word through p<=10000 in class1 mod24;
all prime-square trace shells through p<=2000000; and the complete first-hit
prefix for every prime1mod24 through67369. The last argument must include the
advertised least example to reproduce that theorem as stated. These finite
scopes are different and are not combined into a new overall ES verification
range. `run_all.py` runs both implementations in ordinary and optimized modes,
compares all eleven mathematical JSON files, and saves commands, elapsed
times, return codes and hashes. It also runs
`check_prime_square_fixed_sum.py` against the regenerated prime-square source
records. Its receipt is not an independent human review.

Return an actual source without a search hypothesis:

    python arithmetic.py --p 27409 --a 6889 --u 83 --channel M
    python arithmetic.py --p 2003761 --a 501034 --u 1916 --channel M

`factor_sum_returns` returns the complete finite arrow set, which can be empty.
`factor_sum_inverse` reconstructs every incoming source of a marked full M
target with squarefree residual. `decode_trace` accepts an actually ordered
rational pair and records only the necessary E swap; M ordering is its word.
`fixed_tail_fibre` returns the complete ordered integral fibre at fixed prime
and numerical tail sum. `fixed_tail_seed` records the larger shifted-factor
Pell point and the exact failed integer-tail gate of a rational trace.

Build the two PDFs with two pdflatex passes each. LaTeX dependencies are the
standard AMS, geometry, lmodern, microtype, natbib, TikZ and hyperref packages. No
primary-source PDFs or font files are included. The two implementations are
separately written in this continuation; neither is independent human review.

See `MORPHISMS.md`, `lean_plan.md`, `source_reading.json`, `claims.json`, and
`HANDOFF_TURN_7_REMAINDER.md` for exact types, dependencies and nonclaims.
