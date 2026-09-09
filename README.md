# Erdős–Straus Foundation

A collaborative workbench for exact Erdős–Straus mathematics: proofs, explicit coordinate maps, shell calculations, reproducible certificates, and source attribution. The project does not claim a proof or counterexample to the conjecture.

## Start reading

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

Please use [Issues](https://github.com/KokunoYumeto/erdos-straus-foundation/issues) or pull requests for corrections and contributions. Include the exact edition, theorem or equation, hypotheses, domains, codomains, and a reproducible calculation. Finite computations retain their finite scope; coordinate correspondences are not silently promoted to global conjecture resolutions.

## Current maintenance status

Scheduled mirroring and publication are paused at the maintainer's request after
the 9 September 2026 organization update. Reading, discussion, forks and independent
contributions remain welcome. The published mathematics and historical files are
preserved; this update adds navigation and source-addressable records.
