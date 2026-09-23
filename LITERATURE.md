# Literature and intellectual lineage

The full [bibliography](research/expanded-2026-09-08/exact_bounded_transport_72/publication_bibliography.tex)
records the sources used by the current reader and the role of each citation.
The guide below gives a starting route into that evidence. It covers the current
supplement; earlier editions retain their own bibliographies.

| Research route | Source and exact location | Role in the work |
| --- | --- | --- |
| Egyptian-fraction coordinates | Christian Elsholtz and Terence Tao, *Counting the number of solutions to the Erdős–Straus equation on unit fractions*, [arXiv:1107.1010, Proposition 2.2](https://arxiv.org/pdf/1107.1010#page=12) and [Proposition 2.6](https://arxiv.org/pdf/1107.1010#page=14) | Type-I/II parametrization lineage. The divisor-descent, global-receiver, and signed-pairing modules rederive their specialized marked normalizations and cite the exact inherited coordinate results. The repository preserves the [original author TeX](research/incoming/es-turn07-global-receiver-determinant-20260921/literature/Elsholtz_Tao_2013_arxiv_1107.1010v6/egyptian-count18.tex), version, hash and read lines; the signed-pairing use is recorded separately in its [source ledger](research/incoming/es-third-defect-signed-pairing-20260923/source_reading.json). |
| Boolean product and character-resolved divisor opposition | JT and The Clankers, *Boolean product formulation and exact cyclotomic reconstruction*, [reconstructed proof source](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/a8cefe028e383d1967cc8876fbbdd9325db9bfb8/research/continuation-2026-09-12/reconstructed/boolean_cyclotomic.tex), BP15--BP16 and the following complete divisor-pair fibre | Supplies the unweighted signed opposition sum and multiplicative-character antecedent. The later [signed-pairing module](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/13cdd6c8d1236b078bb503af698d132017ed99d7/research/incoming/es-third-defect-signed-pairing-20260923/core.tex#L45-L205) derives the full weighted fibre over the original E/M words, retains the factor $\chi(-1)$, and proves the parity and degree-operator formulas. It does not attribute the new weighted theorem to the earlier source. |
| Exterior congruence coordinates | K. Yamamoto, *On the Diophantine equation (4/n=1/x+1/y+1/z)*, [Lemma 2, equation (4), printed page 38](https://www.jstage.jst.go.jp/article/kyushumfs/19/1/19_1_37/_pdf) | Human-source lineage for the inherited exterior congruences used by the square-zero and mixed-order continuations. The current modules rederive their exact specialized identities and record the PDF page actually read. |
| Hard residue class and solution-form context | Miguel Angel Lopez, *A Complete Congruence System for the Erdős–Straus Conjecture*, [arXiv:2404.01508](https://arxiv.org/abs/2404.01508), author TeX lines 33--58, 76--127 and 171--190 in the local source record | Literature context for Type II and Type A/B forms and the (p\equiv1\pmod {24}) class. No current theorem assumes the paper's proposed coverage system. [Exact reading record](research/incoming/es-turn07-mixed-order-upward-20260923/source_reading.json). |
| Primes in reduced arithmetic progressions | Andrew V. Sutherland, *18.785 Lecture 18: Dirichlet L-functions, primes in arithmetic progressions*, [Theorem 18.1](https://math.mit.edu/classes/18.785/2017fa/LectureNotes18.pdf#page=1) | Supplies infinitely many prime members only after each progression is proved reduced. This is used both in the divisor-descent constructions and in the sharpness proof that every odd quotient $N>3$ has infinitely many prime-shell uncovered colour orbits. |
| Embedded ordered groups and reciprocal-divisor locus | Alain Connes and Caterina Consani, *Hochschild homology, trace map and zeta-cycles*, [DOI 10.1090/pspum/105/01896](https://doi.org/10.1090/pspum/105/01896), Proposition 3.1 and equation (3.2) | Source for the ordered-group/divisor comparison. The ES finite integral maps are proved in the supplement. |
| Cyclic and pericyclic constructions | Alain Connes and Caterina Consani, *Cyclic theory and the pericyclic category*, [DOI 10.1090/pspum/105/01897](https://doi.org/10.1090/pspum/105/01897), §7.4, Lemma 7.7 and Proposition 7.8 | Source for the cyclic-category comparison; the retained translations and finite incidence maps are explicit in the ES sources. |
| Auxiliary torus and directional operators | OpenAI, *Finite Time Blowup for Navier–Stokes*, 166-page edition identified in [the attribution record](research/expanded-2026-09-08/exact_bounded_transport_72/ns_operator_bridge/ATTRIBUTION.md), §6.1 and Lemma 6.2 | The exact auxiliary construction supplies the operator coordinates studied here. Both preserved PDF versions, passage comparisons and source revision are identified. |

The original arithmetic, positivity-code and prime-production contributions were
relayed by **u/UmbrellaCorp_HR**, including the continuation numbered (71)–(100).
The earlier mod-107 deficit observation was contributed by **u/CommonCareful3149**.
The later calculations cite those contributions alongside the published literature.

The 23 September third-defect intake is a source object with separate
provenance, not a literature attribution. Its supplied four-page proof and
constructor are preserved byte-for-byte in
[`received/`](research/incoming/es-third-defect-signed-pairing-20260923/received/),
with source locators and hashes in
[`RECEIVED_INPUT.json`](research/incoming/es-third-defect-signed-pairing-20260923/RECEIVED_INPUT.json).
The independently reconstructed proof credits Elsholtz--Tao for the inherited
Type-I/II coordinates and JT for the Boolean-pair antecedent; it makes no
historical-priority claim for the odd-quotient or cyclic-obstruction results.

The [fluid attribution record](research/expanded-2026-09-08/exact_bounded_transport_72/ns_operator_bridge/ATTRIBUTION.md)
also records the preceding programme of Diego Córdoba and Luis Martínez-Zoroa,
work with Fan Zheng, and the separately attributed manuscripts of Levent Alpöge,
Tristan Buckmaster and Matei P. Coiculescu. It distinguishes the passages inspected,
the sources of particular constructions, and the full proofs not independently
audited in that source review. Its accompanying
[source records](research/expanded-2026-09-08/exact_bounded_transport_72/ns_operator_bridge/SOURCES.json)
preserve exact versions and reading scopes.

For an extension, record which theorem or construction you actually use and
where. A relevant title is a reading lead; a borrowed argument needs its precise
location and hypotheses. Public links and authored expositions can be shared
without redistributing a private source library.
