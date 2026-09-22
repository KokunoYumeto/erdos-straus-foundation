# Turn 7: modulo-24 mixed prime-shell trace return

The general existence milestone is still open in this programme. This tranche
proves a source-changing return on a specified original rational source, not
that this source is occupied at every prime.

Main theorem: for p prime, p=1 mod24, a=c*q in the original first-half range,
c in {1,2,3,6}, q>3 prime, every positive rational ES tail pair with integral
sum gives a reconstructed original middle state at the same p. Exterior inputs
use a primitive-ray return that changes u but retains each centred exponent.
Middle inputs use the small original word after a marked complement.

The universal ray-preserving residual-divisor guarantee holds exactly for the
nine coprime rays with r*s dividing6. For other rays the paper proves a reduced
infinite prime-progression obstruction at a supplied source, with separately
constructed ES solutions. This is not a conjectural counterexample.

The exact composition with the literal four-label receiver is proved in
*receiver_bridge.tex*. Every returned middle witness has a nonsingular receiver
with explicit determinant, inverse, and exterior-power bounds. The composite
retains the ray parameters, complement bit, tail permutations, and source
fibre; it does not reverse receiver invertibility into source existence.

Read *workbench.tex* and *core.tex* for all proofs, the complete trace fibres,
scope, and negative controls. *preprint.tex* is a shorter standalone proof of
the mixed source theorem. *MORPHISMS.md* gives each original coordinate
transition.

Reproduce all mathematical tables:
    python run_all.py --bound 10000 --directory reproduced

Or run the independent lanes separately:
    python verify.py --bound 10000 --out reproduced
    python -O verify.py --bound 10000 --out reproduced_optimized
    python check_independent.py --input reproduced --out independent.json

Construct the worked return from exact rational input:
    python repair.py --p 1129 --a 417 --y 6116/7 --z 20714892/7

No extra Koide-chamber restriction is asserted for the returned ray. The exact
r,s and orientation remain available for that separate test.

All Python code uses the standard library. The separate checker imports neither
the main checker nor predecessor software. These are two implementations in this
continuation, not independent human mathematical review. No Lean build is claimed.

The default complete source census has 143 primes1mod24 through10000, 171732
shells and 5616298 original divisor words \(u\mid a^2\). E and M traces are separately
marked and may overlap; M orientations remain separate. The large isolated prime
6975049201 is checked by trial division in one implementation and a complete
p-1 order certificate in the other. No new overall ES verification range or
least-example claim is made. The 34 progression examples have certified CRT
conditions; sample integers in those templates are not asserted prime.

The only external infinite prime-supply input is Dirichlet's theorem, used after
proving the displayed progressions reduced. Source context and exact primary
locators are in source_reading.json and references.tex. No historical-priority
determination is claimed. The prior archive is preserved, not re-audited in full.
