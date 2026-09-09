# Primary-source attribution for the Navier–Stokes operator bridge

Audit date: 8 September 2026. This record identifies the source statements, attribution, declared formal dependencies, and two exact passage comparisons used by the existing Erdős–Straus investigation. It does not certify either complete fluid proof. No Lean, Lake, or Elan process was started. `SOURCES.json` records 28 source receipts, the individual SHA-256 hashes, the actual reading scopes, and the comparison recipe.

## The Navier–Stokes source and its two preserved versions

The title page of *Finite Time Blowup for Navier–Stokes* names **OpenAI** as author. The pinned repository metadata also names OpenAI. The manuscript is available at the [primary PDF URL](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf); the formal source inspected here is [commit 8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538](https://github.com/openai/NavierStokesAndEuler/tree/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538).

The same PDF URL served two different preserved files during this investigation:

| Source receipt | Pages | Bytes | SHA-256 |
| --- | ---: | ---: | --- |
| `ns_pdf_165` | 165 | 2,955,931 | `8c8a94ad9ac824c8b605b9827cadf7beaca48bd10b380de3cfc872a2c37afa81` |
| `ns_pdf_166` | 166 | 2,959,204 | `0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f` |

Both original files remain preserved by the Navier–Stokes programme. The incoming release receipt reports the second file's HTTP Last-Modified value as 8 September 2026, 19:09:35 GMT. Its length, page count and SHA-256 were independently checked from the local file in this subtask. The URL alone is therefore insufficient as a version identifier. No equivalence of the entire PDFs or alignment of the new PDF with every declaration in the pinned repository is asserted.

Theorem 1.1, p. 1, states the following for every original viscosity \(\nu>0\). There exist

\[
f\in C_c^\infty(\mathbb R^3\times(0,\infty);\mathbb R^3),\qquad K\subset\mathbb R^3\text{ compact},
\]

and smooth velocity and pressure \(u,p\) on \(\mathbb R^3\times[0,1)\), such that

\[
\partial_tu+(u\cdot\nabla)u-\nu\Delta u+\nabla p=f,
\qquad \nabla\cdot u=0,
\qquad u(\cdot,0)=0,
\]

\[
\operatorname{supp}u(\cdot,t)\cup\operatorname{supp}p(\cdot,t)\subset K
\quad(0\le t<1),\qquad
\sup_{0\le t<1}\|u(t)\|_{L^2(\mathbb R^3)}<\infty,
\qquad
\limsup_{t\uparrow1}\|u(t)\|_{L^\infty(\mathbb R^3)}=\infty.
\]

The asserted consequence is absence of a smooth solution with the same force and initial datum on \(\mathbb R^3\times[0,\infty)\) satisfying

\[
\sup_{t\ge0}\frac12\int_{\mathbb R^3}|u(x,t)|^2\,dx<\infty.
\]

Corollary 10.6, pp. 125–126 of the 165-page file, asserts the corresponding statement for every \(\nu>0\) on \(\mathbb T^3=\mathbb R^3/\mathbb Z^3\): a smooth force, compactly supported in time, and zero initial velocity produce a solution smooth for \(0\le t<1\) whose velocity has infinite \(L^\infty\) limsup at time 1, with no global smooth periodic competitor with the same force and datum. The manuscript identifies these consequences with Clay alternatives (C) and (D). These are recorded manuscript claims; this attribution audit has not supplied their complete independent proofs.

The new 166-page version adds material in §1.1, pp. 2–3, crediting **Diego Córdoba and Luis Martínez-Zoroa** for forced Euler and IPM layer-amplification constructions and **Córdoba, Martínez-Zoroa, and Fan Zheng** for the hypodissipative Navier–Stokes construction. References [6]–[8], p. 165, identify those papers. That material was absent from the inspected historical-context and reference passages of the 165-page file. The new discussion describes a shared use of amplification across scales while assigning a mean-momentum-flux role to its own oscillatory pulses. This is the manuscript's account of its relation to the preceding work, not an independently completed dependency analysis.

## Alpöge, Buckmaster, Coiculescu, and the earlier programme

[Buckmaster's primary statement](https://cims.nyu.edu/~tristanb/statement.pdf), p. 1, identifies the collaboration with **Levent Alpöge**, names smooth-forced IPM, Boussinesq, and three-dimensional Euler results, and gives foundational intellectual credit for the forced-blowup programme to **Diego Córdoba and Luis Martínez-Zoroa**. It reports that the hypodissipative Navier–Stokes work was not yet being released and that its Lean verification was unfinished. This audit records those claims with their original scope. The statement's p. 4 expressly limits what Buckmaster knows about the OpenAI proof and possible data use. It does not establish private access, theft, or a code-dependency claim.

The actual companion manuscripts add precision that is lost by attributing every result merely to “Alpöge and colleagues”:

| Primary manuscript | Authorship evidence | Attribution and theorem locations actually inspected |
| --- | --- | --- |
| [IPM manuscript](https://cims.nyu.edu/~tristanb/ipm.pdf) | The title page lists **Levent Alpöge, Tristan Buckmaster, and Matei P. Coiculescu**. | pp. 1–3 credit Córdoba–Martínez-Zoroa and distinguish uniformly spatially smooth forcing on \(\mathbb R^2\) from the new jointly space-time smooth forcing on \(\mathbb T^2\). Theorem 2.1 is on p. 3. |
| [Boussinesq manuscript](https://cims.nyu.edu/~tristanb/boussinesq.pdf) | The title page lists **Levent Alpöge and Tristan Buckmaster**. | pp. 1–3 credit the Córdoba–Martínez-Zoroa IPM programme and the Boussinesq work of **Córdoba, Andrés Laín-Sanclemente, and Martínez-Zoroa**. Theorem 1.1 is on p. 3; acknowledgments and references are on p. 76. |
| [Euler manuscript](https://cims.nyu.edu/~tristanb/euler.pdf) | The inspected title page contains no author line. Joint Alpöge–Buckmaster manuscript authorship is recorded in the pinned `fluid_lean/euler-blowup/formalization.yaml` and the companion IPM account; no author line is invented. | Theorem 1.1, p. 2; coordinate and force identities, Lemma 2.1, p. 3; research genealogy, pp. 1–3; references, p. 112. |

The original IPM coordinates and constants are material to identification of the result: the companion paper takes \(\mathbb T^2=(\mathbb R/2\pi\mathbb Z)^2\), Fourier coefficient factor \((2\pi)^{-2}\), and velocity multiplier

\[
\widehat{u_{\mathbb T}(\rho)}(k)=2\pi
\left(\frac{k_1k_2}{|k|^2},-\frac{k_1^2}{|k|^2}\right)\widehat\rho(k)
\quad(k\ne0),\qquad
\widehat{u_{\mathbb T}(\rho)}(0)=0.
\]

This is the source's exact convention, not the unit-period torus of the Navier–Stokes auxiliary construction. Its Theorem 2.1 is stated for a smooth odd, zero-mean initial density and force \(F\in C^\infty([0,1]\times\mathbb T^2)\), a classical solution before time 1, convergence to one terminal density in every \(C^\eta\), \(0\le\eta<1\), and divergence of both the density-gradient and velocity-gradient sup norms. No terminal smooth state is asserted.

The Boussinesq acknowledgments, p. 76, also credit helpful conversations with **Mehmet Demirtaş** and **Federico Pasqualotto**, and work by **Ralph Furman**, **Eric Price**, and other Anthropic collaborators on capabilities used by the collaboration. These acknowledgments do not add them to the manuscript's author line.

The earlier primary bibliographic anchors are [Córdoba–Martínez-Zoroa, forced Euler, arXiv:2309.08495v1](https://arxiv.org/abs/2309.08495v1), [Córdoba–Martínez-Zoroa, IPM, arXiv:2410.22920v3](https://arxiv.org/abs/2410.22920v3), and [Córdoba–Martínez-Zoroa–Zheng, hypodissipative Navier–Stokes, arXiv:2407.06776v2](https://arxiv.org/abs/2407.06776v2). Their title, author, abstract and submission records were read. Their complete proofs were not audited here.

## What the formal repositories actually attribute

The `fluid_lean` revision resolved during the live check was [d0124689230b58b4f86e7b90ac59de06404b3b6b](https://github.com/tristanbuckmaster/fluid_lean/tree/d0124689230b58b4f86e7b90ac59de06404b3b6b), with commit time 8 September 2026, 04:07:52 UTC. Its README and metadata identify Lean code generation by Claude under Levent Alpöge's direction. The Euler metadata gives Alpöge and Buckmaster as manuscript authors, lists Claude in the formal-project author field, and records Alpöge's review of the challenge statement. The Boussinesq and `affinecore` metadata list Alpöge in the project author field and mark statement review unreviewed; `affinecore` also records a pending Comparator run. These are source-maintainer declarations, not new verification results from this subtask. They must not be collapsed into one undifferentiated certification claim.

The repository's `affinecore` directory describes another Boussinesq formalization. The directory name does not identify a formal certificate for the IPM manuscript. This audit has not established a one-to-one match between that IPM manuscript and a complete formal proof in the inspected tree. Moreover, the inspected IPM manuscript p. 3 still contains placeholder strings for two announced formal-artifact SHA-256 values. Those strings are not usable version pins; the independently resolved repository revision above is a separate provenance record.

At OpenAI's pinned revision, `formalization.yaml` declares a formalization of the two OpenAI manuscripts, marks its review self-assessed, and acknowledges Lean, Mathlib, Formal Conjectures, Lake, Comparator, lean4export, nanoda and associated tools. It explicitly records the [Formal Conjectures Navier–Stokes statement](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/Millenium/NavierStokes.lean) as the reference basis for the Comparator alternatives (C) and (D). The declared direct Lake dependencies are Mathlib and Comparator; the local manifest pins them to `85e3a25e006c35636f0e53b0e9296caca2685bc0` and `19e111e2141cf333c7daff0f64c5f24acc91dd2e`, respectively. `NavierStokes/ComparatorSolution.lean` exposes the two breakdown adapters. This is a checked declaration of source relationships, not a complete transitive proof or code-provenance audit.

The preserved [OpenAI announcement](https://openai.com/index/navier-stokes-solution/), under “Concurrent work”, explicitly recognizes Alpöge and Buckmaster's priority for forced Euler. Its account and Buckmaster's account are attributed to their respective authors. Neither statement by itself resolves disputed private chronology or access.

## Exact source locations used by the current operator bridge

The current local mathematical work independently derives the auxiliary-torus constructions. For source provenance, the following limited comparison was performed between the two original PDFs:

| Delimited passage | 165-page version | 166-page version | Result after removing only running page headers |
| --- | --- | --- | --- |
| §6.1, from its title to the §6.2 title, including (6.1)–(6.7) | pp. 62–64 | pp. 62–64 | Extracted text exactly equal; 4,346 characters; empty line diff |
| Lemma 6.2 and its proof, ending before the paragraph beginning “Fields are defined on the extended domain” | p. 67 | p. 67 | Extracted text exactly equal; 1,425 characters; empty line diff |

The respective SHA-256 values of these UTF-8 extracted blocks are `04e05287e9b04c920c7618430ea433010d0a579af89935ecd80a785cacb18c1a` and `5d64e2786ad26e5a267bfdc3f7aaff70cc386e56d3533a1008dc7f0f48552b42`. The procedure removes only full-line running headers, delimits the same named passages, and leaves all mathematical characters, line contents, and original PDFs intact. `SOURCES.json` records the exact recipe. It does not replace either source or establish equality of their other sections.

For the companion programme, Euler §1.2, p. 2, expressly points to the Alpöge–Buckmaster Boussinesq local two-field wave calculation. Its reference names Lemma 2.1, whereas the current Boussinesq PDF places that calculation in **Lemma 3.1, p. 8**; §2 is now the AI statement. This is a concrete numbering mismatch to retain when citing the current artifacts, not a conclusion about the validity of the mathematical construction. Euler's own coordinate and force identities are **Lemma 2.1, p. 3**. No theorem from either fluid manuscript is used here as an already independently verified solution of the Erdős–Straus problem.
