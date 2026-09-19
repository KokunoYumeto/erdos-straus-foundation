# Turn 7 continuation: actual channel rescue and small-shape rigidity

The universal ES existence milestone remains outstanding. This source does not
advance to Turn 8 under an assumed positive-coefficient theorem.

The new conclusions are coordinate-level. Here a hard prime means
`p mod 840` in `{1,121,169,289,361,529}`:

1. Every diagonal original E state R=D yields an original M state at the same p,
   with a strictly smaller M cofactor and a complete squarefree-part fibre.
2. At a hard prime, every E record with |v-R|,|v-D|<=7 is the singular family
   that already made the previous exterior cutoff sharp. It yields M at the
   same original distinguished denominator, with both orientations retained.
3. At radius8 the only possible nonsingular profile is (8,-4,11), and its grade
   congruence forces a j=3,u=9 middle state. No quartic integral-point theorem is
   required to obtain that positive return. Any hard source in this branch is
   further restricted to `p mod 840` in `{1,121}`.
4. The full marked cubic and its natural rational involution are explicit. The
   latter does not preserve the original prime slice; exact image failures are
   recorded, not replaced by a claim of unrelatedness.

[core.tex](core.tex) is the complete proof. [workbench.tex](workbench.tex)
compiles it, and the [workbench PDF](output/pdf/workbench.pdf) is the readable
full account. [preprint.tex](preprint.tex) and its [short PDF](output/pdf/preprint.pdf)
give a standalone shorter account. [MORPHISMS.md](MORPHISMS.md) retains maps,
fibres and exceptions; [claims.json](claims.json) gives stable machine-readable
claim records.

[PROOF_AUDIT.md](PROOF_AUDIT.md) records the isolated derivation checks and the
repairs made before integration. [source_receipt.json](source_receipt.json)
separates the received packet from the edited repository sources; the exact
received manifest and principal original files remain under [received/](received/).

Reproduce from this directory:
    python verify.py --bound 3000 --out certificates
    python -O verify.py --bound 3000 --out certificates_optimized
    python check_independent.py --input certificates --out independent.json --radius8-s-max 200000

The main verifier enumerates all original first-half exterior square divisors
at primes p=1 mod8 through the specified bound. The strengthened separate checker
imports no main or predecessor module and uses primitive h,r,s enumeration. It
recomputes the hard flags, all 52 radius-seven profiles, all 12 radius-eight
ordered pairs and 16 grade rows, exact denominator order, the fixed quartic
prefix bound, and hashes of every consumed certificate. The scan has no actual
hard radius-seven or radius-eight state below 3000; the universal conditional
classification is proved by the finite profile arguments, not inferred from
that vacuous scan branch. The s<=200000 quartic prefix is not claimed complete
at larger s. Read [integration_verification.json](integration_verification.json)
for the exact local replay and proof-audit receipts, and
[render_receipt.json](render_receipt.json) for the compiled-page checks. The
current file hashes are in [MANIFEST.sha256](MANIFEST.sha256).
File presence or an archive hash is not a mathematical verification receipt.

The original Type I/II equations, the elementary endpoint identities, and the
singular integer family are antecedents. No historical-priority determination,
independent human mathematical review, Lean build, or new overall ES verification
range is asserted. Source and publication scopes are recorded separately.
