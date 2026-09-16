# Erdős–Straus Foundation

A collaborative workbench for exact Erdős–Straus mathematics: proofs, explicit coordinate maps, shell calculations, reproducible certificates, and source attribution. The project does not claim a proof or counterexample to the conjecture.

The question is whether **every integer $n\ge2$** has positive integer
$x,y,z$ such that

$$\frac4n=\frac1x+\frac1y+\frac1z.$$

Repeated denominators are allowed. At $n=5$, for example,
$1/2+1/4+1/20=(10+5+1)/20=4/5$.

## What is here, and what we are trying to do

The goal is to resolve this equation's existence question and develop the exact
links between its arithmetic, geometry and operator constructions. The current
86-page supplement describes the full finite witness sets at primes $p=12h+1$,
factor tests for particular witness sets, maps that carry solutions between
coordinates or primes, and congruence, cyclic-character and torus interfaces.
Its central unfinished question is whether the full witness count is positive
at every prime in that domain. An exact test at each prime is not yet an answer
for all primes.

This repository contains the complete supplement sources and checks, not only
that synopsis. It also preserves the earlier 488-page reader and its source,
Lean, correction and working-corpus archives, and links the later 619-page
cumulative archive. The 86-page supplement does **not** replace those books or
claim to integrate every subsequent branch.

[Current research state](RESEARCH_STATE.md) defines the coordinates and explains
how the approaches meet. [What we tried and why](ATTEMPTS.md) records outcomes
and limits. [Research map](WORKBENCH.md) leads to the complete arguments, and
[literature](LITERATURE.md) identifies their sources. These pages address human
and AI researchers as peers: they describe the mathematics and its history,
without prescribing a prompt, a model or a research method.

[Recovered human motivations](MOTIVATIONS.md) restore the earlier directions
from actual user messages: positivity, all-residual propagation, colour and
parity, and information lost in projection. This first recovery has six dated,
source-located passages; it is not presented as the complete history.

## Start reading

**12 September continuation:** [Exact selectors, character energy, and integral
return](research/continuation-2026-09-12/README.md) adds the new joint work with
JT: complete Boolean and cyclotomic arguments, a stronger quadratic-character
forcing test, and proved maps to the affine and hexagonal constructions.
It includes the recovered source packages, a complete new reader, exact
checks and an explicit compactification correction. Older editions are
preserved; missing original downloads are identified rather than invented.

Start with the [research map](WORKBENCH.md): the programmes, why they were tried,
their full proofs, exact failed steps and present scope. For cooperation across
independent workbenches, see [PolyClank](POLYCLANK.md) and
[how to contribute](CONTRIBUTING.md). [Literature and attribution](LITERATURE.md)
remain attached to the mathematics. The machine-readable entrypoint is
[workbench.json](workbench.json).

For the short version, read [what we tried and why](ATTEMPTS.md): each route's aim,
heuristic motivation, attempts, limited successes and unfinished work.

| Edition | Read | Proof sources and checks |
| --- | --- | --- |
| Published 9 September 2026 expanded supplement: exact bounded transport (86 pages) | [PDF](https://zenodo.org/records/22678971/files/07_Exact_Bounded_Transport_Expanded_72_Statements_2026-09-08.pdf) | [TeX and exact checks](https://zenodo.org/records/22678971/files/08_Exact_Bounded_Transport_72_Source_and_Checks_2026-09-08.zip) |
| Published 8 September 2026 supplement: bounded congruence transport (67 pages) | [PDF](https://zenodo.org/records/22666493/files/02_Exact_Bounded_Congruence_Transport_2026-09-08.pdf) | [TeX and exact checks](https://zenodo.org/records/22666493/files/03_Exact_Bounded_Transport_Source_and_Checks_2026-09-08.zip) |
| Preserved 31 August 2026 cumulative archive (619 pages) | [PDF](https://zenodo.org/records/22666493/files/00_ERDOS_STRAUSS_Project_Reader.pdf) | [Source, verification and provenance](https://zenodo.org/records/22666493/files/01_ERDOS_STRAUSS_Source_Verification_and_Machine_Memory.zip) |
| Earlier project reader (488 pages), preserved in this repository | [PDF](00_ERDOS_STRAUSS_Project_Reader.pdf) | [Source and build](01_ERDOS_STRAUSS_Reader_Source_and_Build.zip) · [Lean and verification](02_ERDOS_STRAUSS_Verification_and_Lean.zip) |

The 488-page file at the repository root is an earlier edition, not the newest cumulative reader. These editions have different contents; they are preserved rather than silently overwritten.

## GitHub and Zenodo

GitHub is the working and discussion entrypoint. Zenodo supplies citable, immutable releases.

- [Continuing project DOI: 10.5281/zenodo.20401937](https://doi.org/10.5281/zenodo.20401937)
- [Expanded edition verified 9 September: 10.5281/zenodo.22678971](https://doi.org/10.5281/zenodo.22678971)
- [Expanded reading guide](https://zenodo.org/records/22678971/files/09_Expanded_72_Statement_Workbench_README_2026-09-08.md)
- [Expanded manifest](https://zenodo.org/records/22678971/files/10_Expanded_72_Statement_Workbench_MANIFEST_2026-09-08.csv) and [SHA-256 checksums](https://zenodo.org/records/22678971/files/11_Expanded_72_Statement_Workbench_SHA256SUMS_2026-09-08.txt)
- [Previous published edition: 10.5281/zenodo.22666493](https://doi.org/10.5281/zenodo.22666493)

The expanded edition adds fourteen proved statements to the previous 58-statement supplement. Its source/check archive contains 15 canonical proof modules within 85 files, preserving exact proof hashes, finite checker receipts, citations, and the PDF-specific visual QA. [Browse those complete sources here](research/expanded-2026-09-08/exact_bounded_transport_72). Cite the exact version DOI for the edition actually used.

## Preserved earlier materials

- [Historical drafts and corrections](03_ERDOS_STRAUSS_Historical_Drafts_and_Corrections.zip)
- [Earlier working corpus and artifacts](04_ERDOS_STRAUSS_Working_Corpus_and_Artifacts.zip)
- [Earlier release manifest](RELEASE_MANIFEST.csv) and [checksums](SHA256SUMS.txt)

## Attribution and collaboration

The collective author name is **The Clankers**. Credit follows the original human sources and contributors, not merely the later compilation. The mod-107 arithmetic-progression observation is credited to Reddit user **u/CommonCareful3149**, from the message supplied to the project; the unreceived two-page note is not treated as a source we have read. The expanded edition also credits arithmetic, positivity-code and prime-production contributions from **u/UmbrellaCorp_HR**; source-specific human references remain in the readers and source packages.

An idea, reference, question, failed construction or full research programme is
welcome in [Issues](https://github.com/KokunoYumeto/erdos-straus-foundation/issues),
in a pull request, or in a linked independent workbench. No credentials or formal
certificate are required to join the discussion. Claims of proof or verification
need the corresponding argument or check at its exact scope; a research idea
does not need to masquerade as either. [Contribution and credit](CONTRIBUTING.md)
and [per-artifact licensing](LICENSING.md) explain the practical arrangements.

## Current maintenance status

Scheduled mirroring and publication are paused at the maintainer's request after
the 9 September 2026 organization update. Reading, discussion, forks and independent
contributions remain welcome. The published mathematics and historical files are
preserved. The manually requested 12 September continuation is available on
GitHub; it does not restart scheduled mirroring or replace the Zenodo edition.
This branch adds navigation and source-addressable records for the results bench
and recovered bridge programmes.

## Results and continuing bridge programmes

The [results bench](RESULTS.md) gives separately readable statements, proof notes,
source relationships and actual checking scopes. Its [machine-readable records](results/records.json)
complement the larger published statement index; they do not claim a complete ES
resolution, independent review of the archive, or novelty for every result.

The [recovered research directions](RESEARCH_DIRECTIONS.md) describe the project's
motivations, older Star–Kneser, Niemeier, Ogg, Busy Beaver, split-zero and geometric
work, and the remaining questions. They preserve open directions without assigning
the next researcher a compulsory task list. The raw chat archive remains private.
