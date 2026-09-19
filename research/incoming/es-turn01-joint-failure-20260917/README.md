# Turn 1: simultaneous E/M failure on the complete original boxes

**Collective byline:** The Clankers. **Status:** proved structural reduction;
Erdős--Straus remains unresolved.

For every original first-half shell at a prime \(p\equiv1\pmod4\), this
tranche keeps the complete centered divisor box, both exterior/middle
channels, every prime exponent, and the actual support stabilizer. It proves
the exact three-labelled-target collision law, inequalities at every actual
factor cut, and all joint-failure normal forms whose effective quotient has
order at most eight. In those small quotients, removing at most two original
prime occurrences leaves an inactive factor \(B\) with \(W(B)=K\); this is
proved saturation, not unrestricted subgroup generation.

The effective quotient \(\Gamma/K\) and the full ambient index are retained
separately. The arithmetic phase and labelled forbidden targets are

    eta = z^2 product_i g_i^(e_i),
    F = {alpha, alpha*eta, alpha*eta^(-1)}.

All three labels remain typed even when two occupy the same class. For every
active factor and every nonempty actual factor cut \(J\), the proof gives

    ord(g_i) > 2 e_i + 1,
    2 sum_active e_i <= |Gamma/K| - 1 - |F|,
    2 sum_(i in J) e_i <= |C_J| - 1 - max(1, |F_J|).

At a prime residual \(q\equiv3\pmod4\), an effective-index-six failure has
one simple exceptional prime \(r\), a saturated inactive block, and the exact
edge \(p+q=4Br\). The two arithmetic phases and the nonsplit section cocycle
are retained. This determines the next factor edge; it does not prove that
the next selector succeeds.

## Read and reproduce

- [**workbench.pdf**](workbench.pdf), **core.tex**, **workbench.tex**, and
  **references.tex**: complete proof,
  first-half completeness, ordered denominator returns, and citations.
- [**preprint.pdf**](preprint.pdf) and **preprint.tex**: compact proof with the malformed active-index subscript in
  the received package corrected.
- **MORPHISMS.md** / **MORPHISMS.json**: exact maps, inverses, fibres, kernels,
  and retained distinctions.
- **HANDOFF_TURN_2.md**: the precise shifted-factor input and remaining
  obligation.
- **source_reading.json**: exact human-source and local-lineage locators.

Run with Python 3.9 or later; the programs use only the standard library:

    python verify.py --bound 3000 --out certificates
    python -O verify.py --bound 3000 --out certificates_optimized
    python check_independent.py --input certificates --out certificates/independent.json
    python verify_examples.py --out certificates/examples_standalone.json
    pdflatex -halt-on-error workbench.tex
    pdflatex -halt-on-error workbench.tex
    pdflatex -halt-on-error preprint.tex
    pdflatex -halt-on-error preprint.tex

The fresh intake replay passed with 2,153,122 named check calls plus eight
negative-control rejections, 73,798 first-half shells, 1,877,004 original
divisor vectors, and row digest
**fba08200386904e44f52990b22ee5ed058a36246cbf30f6ee3df098d193c0170**.
The separate checker passed 494,215 checks; it independently recomputes the
arithmetic of every supplied ledger row but does not independently enumerate
or certify completeness of that ledger. The standalone displayed-example
checker passed 2,534 checks.

**verification.json** preserves the received execution chronology. Its first
two main-run records name the pre-repair independent-checker hash; the later
independent-run records and this repository contain the repaired checker. The
main verifier does not import that checker. The public integration additionally
corrects the generated scan schema label from **target_classes** to
**collision_count**; the row values and mathematical digest are unchanged.

The inherited prime-shift and ambient-index-six results are credited directly
to Chase Bryan's pinned centl sources. The original Type I/II coordinates are
credited to Elsholtz--Tao, and the Kneser antecedent to DeVos. No historical
priority determination is made.

No universal occupancy theorem, Erdős--Straus proof or counterexample, new
prime-verification range, uniform bound on all effective indices, Lean build,
or independent human mathematical review is claimed.
