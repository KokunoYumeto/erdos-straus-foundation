# Exact bounded congruence transport and auxiliary-torus interfaces

The Clankers. Expanded edition, 8 September 2026.

This 86-page reading edition contains 72 proved statements in 15 canonical TeX files,
with explicit contributor credit and a bibliography.
It continues the 58-statement, 67-page edition at
[10.5281/zenodo.22666493](https://doi.org/10.5281/zenodo.22666493).
The continuing project reference (a concept DOI, not this edition's version DOI) is
[10.5281/zenodo.20401937](https://doi.org/10.5281/zenodo.20401937).
The [GitHub workbench](https://github.com/KokunoYumeto/erdos-straus-foundation)
provides the project's reading guide, source navigation and continuing work.

## Mathematics in this edition

The arithmetic starts with primes p=12h+1 and all original shells
3h+1 <= a <= 9h, retaining R=4a-p, S=pa, divisor valuations, witness order,
raw square scales and the full finite-code order. The complete proofs develop
bounded congruence gluing, shared-variable Chinese remainder constructions,
integral lattice and cyclic-character maps, arithmetic successor domains and
inverses, and the exact all-shell witness correspondence.

The operator work uses the auxiliary torus matrix J=((3,1),(1,5)) in the
announced Navier-Stokes manuscript. Full covering fibres and character
corrections retain determinant 14 and the original eigenvectors.
Ten new statements prove continuous transfer and its kernels, source mean
corrections, physical evaluation, exact sampling obstructions and reconstruction,
sharp small-denominator constants and Sobolev derivative loss, smooth and
distributional inverses, and parameter-dependent estimates with the source's
actual cutoff remainder retained. The Fourier factor remains 2*pi*i and the
torus has period one. For the stated coordinate C-norms, one directional
inverse needs m+3 input derivatives for m output derivatives.

Four further statements compute every same-shell pair-swap/tag-change candidate,
including rational nonintegral companions, exact obstruction orders, integral
orbit fibres and original code differences. On the completely characterized
occupied residual-three domain, the global first code in both original radices
is 2*(ell_star-1), where ell_star is the least prime divisor of (p+3)/4 congruent
to 2 modulo 3. Failure of that residual-three test does not assert that later
shells are empty.

This is an exploratory mathematical workbench: exact calculations can be
interesting even when a route to a larger conjecture does not close. These
results do not prove or disprove Erdős-Straus, the Riemann hypothesis or the
Yang-Mills mass gap. They do not independently validate the complete announced
Navier-Stokes construction. The auxiliary-operator and arithmetic results have
their own complete proofs and do not assume a fluid blowup theorem.

## Reading and reproduction

Start with the numbered 07 PDF. The numbered 08 ZIP contains the complete TeX
proof graph, portable exact checkers, finite certificates, full mathematical
review and repair records, and source attribution. All ten inherited files
remain unchanged: the earlier 02 PDF is the 58-statement snapshot, not this
expanded edition. The original 619-page archive reader remains file 00.
Protected source papers and private conversation logs are not included in
this new supplement.

From the extracted exact_bounded_transport_72 directory, create output/pdf
if your extractor omits empty directories and run twice:

    pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf publication.tex
    pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf publication.tex

The reading PDF compiles publication.tex, which adds contribution credits and
source-specific citations to the unchanged canonical mathematical proof graph.
PUBLICATION_EDITORIAL_MAP.json records its reversible editorial changes.
The canonical entrypoint bounded_transport.tex remains available separately.
The current reading PDF is identified by qa/PUBLICATION_PDF_QA.json; qa/QA.json
retains the distinct historical canonical-PDF review and does not authenticate
the current reading PDF. No mathematical proof source was edited for publication.

The checkers use Python 3.9 or newer and SymPy 1.13.1. Install the latter with
python -m pip install -r requirements.txt. REPLAY_RECEIPT.json records a fresh
standalone replay of all fourteen commands listed below. Finite computations
corroborate formulas at their stated bounds; the general proofs are in TeX.
FILE_MANIFEST.json authenticates the public source tree. PROVENANCE.json
records unchanged proof hashes and editorial removal of private paths from
review records. Earlier findings remain historical evidence, not assertions
that an old edition already contained the later work.

## Human sources and contributions

The colleague identified by the project author as Reddit **u/UmbrellaCorp_HR**
contributed the original arithmetic, positivity-code and Euclid/prime-production
material relayed into this programme, including the continuation numbered
(71)-(100). The boundary and analytic continuation proofs here are subsequent
work. The earlier mod-107 progression observation remains separately credited
in the inherited archive to **u/CommonCareful3149**.

The arithmetic bibliography retains Christian Elsholtz and Terence Tao's
Egyptian-fraction parametrization work, and divisor-category constructions
of Alain Connes and Caterina Consani. The manuscript bibliography specifies
the articles and passages used.

The fluid source is attributed to OpenAI as its displayed manuscript author.
The files ns_operator_bridge/ATTRIBUTION.md and SOURCES.json identify the two
preserved NS PDF editions, operator loci, and source-specific human credit for
the earlier programme of Diego Córdoba and Luis Martínez-Zoroa, work with
Fan Zheng, and the separate results of Levent Alpöge, Tristan Buckmaster and
Matei P. Coiculescu. Their roles are not collapsed into a single authorship claim.

The [NS manuscript](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf)
is identified by the preserved 166-page SHA-256
0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f
and the separately pinned
[source revision](https://github.com/openai/NavierStokesAndEuler/tree/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538).
Those identifiers are not a claim of complete proof or community validation.

The Clankers is the continuing collective attribution for the human-AI
collaboration. No novelty or priority claim beyond these source credits is made.

## Exact replay commands

    python verify_bounded_crt.py
    python connes_reading/verify_exact.py
    python exact_audit/orchard_partition_fixture.py
    python proof_review/review_checks.py
    python proof_review/boolean_shared_checks.py
    python proof_review/cyclic_incidence_checks.py
    python proof_review/raw_scale_checks.py
    python proof_review/raw_scaled_incidence_fixture.py
    python proof_review/sieve_checks.py
    python counterexample_sieve/check_nohit.py --limit 5000 --certificate
    python ns_operator_bridge/check_torus.py
    python ns_operator_bridge/check_coset.py
    python ns_operator_bridge/check_reverse_transport.py
    python boundary_swap/check_boundary_swap.py --limit 2000
