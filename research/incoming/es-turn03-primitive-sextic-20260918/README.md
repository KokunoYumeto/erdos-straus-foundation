# Turn 3: a closed primitive sextic triangle and square-source escape

At the deterministically certified prime `7510085481569082811681`, the complete canonical component `31 -> 223 -> 307 -> 31` has both original E/M selectors empty at every vertex. All full and effective stabilizer indices equal six; all inactive factor boxes saturate their actual stabilizers; every successor is the unique simple nonresidue prime factor. The certificate exhausts all 1215 original divisor vectors. This refutes canonical primitive-cycle closure, not Erdős–Straus.

The separately proved square-source theorem forces, at every vertex of any canonical all-3-mod-4 triangle, an actual nonresidue factor outside the triangle after introducing multiplier 9. No favourable-factor inventory is assumed. A cardinality theorem also shows that primitive closed components of at most six vertices cannot stay closed under square multipliers 1,9,25. This is escape from a specified component, not eventual selector occupancy.

`preprint.tex` is the standalone proof source. `input.json`, `prime_certificates.json`, and `verify_core.py` are a portable exact certificate. Run:

```sh
python verify_core.py
python -O verify_core.py
pdflatex -halt-on-error preprint.tex
pdflatex -halt-on-error preprint.tex
```

The checker uses only the Python standard library. It verifies all 80 recursive prime-proof nodes, all original factorization and divisor data for the triangle, all three square-nine source factorizations, and an independent positive ES solution at the same p. The generated `core_certificate.json` preserves exact integer counts and ordered data. Use an arbitrary-precision JSON parser; numbers exceed 2^53.

The full workbench tranche additionally includes an explicit dual-number CRT, primary/conjugate cubic-symbol tables, fine section carries, a separate full checker and a bounded triangle scan. This public portable checker is intentionally scoped to the central arithmetic certificate, not that larger scan. Preliminary factor discovery used SymPy, but neither final primality nor this replay depends on it.

The triangle has minimum possible cycle length within the all-3-mod-4 vertex type; no least-prime claim is made. No whole-graph enumeration at the large prime, infinite prime-family theorem, universal graph closure, ES proof, Lean build, independent mathematical review, or historical-priority determination is asserted. The collective byline is The Clankers. Antecedents are credited at their actual use in the proof.
