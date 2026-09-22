# Complete mixed-trace fibres and hard-prime middle spectra

Date: 22 September 2026. Collective byline: The Clankers.

## Mathematical basis and scope

The repository was read at `b6825f8faafff4539f93eae9c4ccb9749b32a855` before this
continuation. The current corrected arithmetic return, receiver composite,
sharp-growth proof, ES1--ES15, ES16--ES37, and the integration audit were used.
`READING_AND_DELTA.md` distinguishes the integrated corrections from the new work.

The full bare sorted input fibre is now classified. The receiver matrix together
with its prime label recovers the returned target and the four selected
square-root branches; it does not choose an arithmetic source from a nontrivial
fibre. Separately, a
middle fixed-residual family gives every first singular correction and the
observation hierarchy 0,2,3,9. Two reduced hard-prime progressions show all three
established inverse exponents are sharp already on middle states at
$p\equiv1\pmod {840}$.
No optimality on the smaller mixed-return image, universal ES occupancy,
independent human mathematical review, or historical priority is asserted.

## Files and commands

`workbench.pdf` / `core.tex`: complete coordinate proofs and scopes.
`preprint.pdf` / `preprint.tex`: short, self-contained statement and proofs of the
bare fibre and the hard-middle optimality result; higher-order refinement is in
`core.tex`.

Run with Python 3.10 or later; no package installation or network is required:

    python run_all.py --directory reproduced
    python fibres.py --target 1009 255 24216 686120

The first command performs normal and optimized runs plus a separate checker.
The second enumerates every ordered original mixed input for one *supplied*
sorted middle target. It does not search for an initial witness from p alone.

`verify_fibres.py` uses all original square divisors through the specified bound.
`check_independent.py` imports none of the main or predecessor modules. It uses
literal rational factor pairs and primitive three-factor target enumeration.
`verify_spectrum.py` and `spectrum_exact.py` use Gaussian rational Laurent
arithmetic and full compound-position lists. Their finite parameter checks are
corroboration of the written analytic derivation, not its universal proof.
The large-parameter numerical experiments used privately during derivation are
not certificate inputs, and sample integers are not called primes unless the
arithmetic checker proves that.

Build both PDFs with `pdflatex` (three passes for final cross-references).
The code uses explicit exceptions for checks, so optimization cannot remove them.
JSON integers are exact and may exceed JavaScript's safe-integer range.

`verification.json` is the observed completed execution record.
`verification_20000.json` is the separate larger-range replay: it records
25,277 main arithmetic checks, 31,337 independent checks, 2,003 spectrum
checks, and byte-identical normal and optimized outputs.
`RECEIVED_ARCHIVE.json` records the supplied wrapper and pasted-handoff hashes;
`MANIFEST.json` hashes every admitted module file. Presence of a source script
alone is not a passed execution. The cumulative wrapper was independently
checked against its own member manifest, but this is not a fresh audit of its
entire preserved history.

## Integration

The integrated module is additive below
`research/incoming/es-turn07-fibres-middle-spectrum-20260922/`.
`INTEGRATION_AUDIT.md` records the accepted corrections and independent
mathematical checks. `topic_literature_route.json` gives the exact primary-source
coverage. The public repository retains the cumulative programme and its
nonclaims.
