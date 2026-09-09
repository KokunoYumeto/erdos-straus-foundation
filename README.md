# Erdős–Straus Foundation

This repository is a versioned, readable workbench for the Erdős–Straus conjecture and its verified adjacent constructions.

The conjecture asks whether every integer (n\ge 2) admits a decomposition

\[
\frac4n=\frac1x+\frac1y+\frac1z,
\qquad x,y,z\in\mathbb Z_{>0}.
\]

The current release does **not** claim a proof or a counterexample. It preserves the complete reader, source package, verification materials, historical drafts, working corpus, and their checksums. Claims are retained at their proved scope and are labelled as theorem, exact computation, imported result, conjecture, open obligation, or nonclaim.

## Current release

- `00_ERDOS_STRAUSS_Project_Reader.pdf` — the readable project reader (488 pages).
- `01_ERDOS_STRAUSS_Reader_Source_and_Build.zip` — source TeX, figures, build instructions, and provenance log.
- `02_ERDOS_STRAUSS_Verification_and_Lean.zip` — verification and formal-material package.
- `03_ERDOS_STRAUSS_Historical_Drafts_and_Corrections.zip` — retained historical editions and corrections.
- `04_ERDOS_STRAUSS_Working_Corpus_and_Artifacts.zip` — working corpus and reproducible artifacts.
- `RELEASE_MANIFEST.csv` and `SHA256SUMS.txt` — exact release identities and hashes.

The canonical release concept DOI is 10.5281/zenodo.20401937. This GitHub copy is the continuous, inspectable workbench; prior files are retained rather than replaced.

## Provenance and status

The release is attributed to “The Clankers” as a collective working name. Source papers, local research notes, formal checks, and community contributions are cited in the reader and provenance files. The project distinguishes sourced mathematics from independent calculations and from open research directions. In particular, a finite shell calculation, a coordinate transport, or a representation-theoretic analogy is not silently promoted to a global solution of the conjecture.

Issues and pull requests should include the exact file, statement or equation label, hypotheses, coordinate domains and codomains, and a reproducible check. Please preserve signs, orientations, exceptional loci, and nonclaims.
