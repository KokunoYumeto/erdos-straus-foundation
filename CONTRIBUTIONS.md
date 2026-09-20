# Who contributed what: a provisional Erdős–Straus project history

**Compiled 10 September 2026. Non-exhaustive; open to correction.** This is a contribution record, not a ranked author list, a novelty adjudication, or a mathematical verification. It covers initiating suggestions, work developed with AI, criticism, source introductions, and later reuse. A useful initiating observation deserves attribution even when the underlying mathematics was already known.

Read [the history of research directions](PROJECT_HISTORY.md), [the three newly supplied working texts](provenance/2026-09-10/UPLOAD_READING.md), [the machine-readable contribution register](provenance/2026-09-10/contributions.json), [source descriptions](provenance/2026-09-10/sources.json), and [the continuation handoff](provenance/2026-09-10/HANDOFF.md).

## How to read this record

Public posts show what their authors said and shared. Repository and Zenodo acknowledgements show how the project credited or incorporated that input. The owner's present recollection supplies additional motivation and attribution; it is explicitly distinguished from contemporaneous evidence. Uploaded human–AI conversations show proposed formulas and reported outcomes, not independent certification. Several sources contain both human instructions and model-generated mathematics; credit for supplying and developing that work is not a claim that every displayed formula was personally written by the human.

No contribution percentages or importance rankings are assigned. Acknowledgement does not imply endorsement of every later result. Contributors may request a preferred public name, pseudonym, collective attribution, or a correction. Private aliases and private correspondence are not reproduced. Third-party prize decisions are outside this record.

## u/Far-Lifeguard519: the initiating computational investigation

The originally public [deep-tail post](https://www.reddit.com/r/LLMmathematics/comments/1sysemj/how_gpt55_and_gemini_31_pro_mapped_the_deep_tail/) describes AI-assisted segmented-sieve and divisor-certificate investigations. The owner's [project-history post](https://www.reddit.com/r/LLMmathematics/comments/1szs5wf/comment/olmxr22/) explicitly identifies that post as the source that prompted this project and says it was subsequently deleted. The indexed page remains retrievable through the research tool, which does not establish its present visibility in every Reddit interface.

**Contribution:** making that investigation and its arithmetic questions available, thereby prompting the subsequent analytical and structural programme. The owner's original reply links the first writeup, [Zenodo 19897796](https://zenodo.org/records/19897796), and the proposed lattice investigation. This is a causal attribution, not an award of priority over known congruence reductions or a proof of the conjecture.

The retrieved original says GPT-5.5 and Gemini 3.1 Pro were used. The owner's present recollection is less certain about the precise division between models; no detailed run attribution is invented. The later user recollection includes a modulo-24 lead, while the inspected original emphasizes residuals, divisor certificates and a Jacobi-symbol heuristic. Those descriptions are retained separately. They are not silently turned into a claim about the Mathieu group M24.

**Source status:** deletion reported by the original project history and confirmed by the owner; reason unknown. No deleted body is republished here, no real-world identity is inferred, and no continuing participation or approval is asserted. See the [citation policy](provenance/2026-09-10/CITATION_AND_PRIVACY.md).

## u/TextBackground496: a supersignum proposal later reused in ES

The [Supersignum unit post](https://www.reddit.com/r/wildwestllmmath/comments/1rx677d/supersignum_unit/) proposed a combined circular/hyperbolic formalism. The owner's reply links an AI-assisted exposition at [Zenodo 19099929](https://zenodo.org/records/19099929). The later ES history explicitly credits the original handle when introducing the supersignum/tessarine line.

**Contribution:** the initiating algebraic idea in a separate discussion, before its use in this programme. The owner reports subsequently developing it with AI into a more precise treatment and then reusing that treatment in ES. The proposal, its mathematical reformulation, and its downstream use are separate contributions. Neither the initial post nor this register establishes priority for tessarines or certifies every claim in the initial formulation.

**Remaining link:** identify the exact definitions and passages in the published treatment that were imported into each ES source module.

## u/CivQ17: explicit mathematical suggestions and source figures

The [original comment](https://www.reddit.com/r/LLMmathematics/comments/1szs5wf/comment/olmxr22/) supplies the identity

\[
((2n+1)^2-5)/4=n^2+n-1
\]

and asks the researcher to examine its roots. Subsequent replies connect the discussion to further source leads; the wider thread also contains image contributions and descriptions of phase/cycle patterns. Images were not successfully inspected in this pass, so no theorem is reconstructed from an unread diagram.

**Contribution 1:** the discriminant-five identity/root suggestion and the questions it prompted. **Contribution 2:** supplied visual material. The [5 August edition, version 2026.08.05.16](https://zenodo.org/records/21805460), explicitly reports restoring seven credited CivQ17 figures. **Contribution 3, incompletely mapped:** further suggestions in the discussion that the owner reports were used during synthesis.

The original replies point to [20208683](https://doi.org/10.5281/zenodo.20208683) and [20217969](https://doi.org/10.5281/zenodo.20217969); the main history also names [20208684](https://zenodo.org/records/20208684) and [20250519](https://doi.org/10.5281/zenodo.20250519). These are reading leads as linked, not a silently reconciled version chain.

**Remaining work:** match each figure and suggestion to its actual use, a superseding calculation, or an uncompleted idea. The owner does not claim that every idea was fully integrated. Credit must not depend on the compiler understanding or validating all of it already.

## u/UmbrellaCorp_HR: continuing joint research, criticism, geometry and arithmetic

Use **u/UmbrellaCorp_HR** in public records. The owner identifies this as their continuing collaborator and attributes the three new working texts to that collaborator's human–AI investigations. Other private names and aliases are intentionally not published.

### Circle and number-field constructions

The public [three-theorem post](https://www.reddit.com/r/LLMmathematics/comments/1va0hr5/three_theorems_for_constructing_inversive_circle/) concerns inversive circle packings and generalized Machin formulas over algebraic number fields. The owner's reply identifies downstream sections: *Central-angle field closure*, *Circle-inversion coefficient transformation*, and *Full inverse-circle equation and evaluation covariance*. These section names provide a concrete adoption trail; the screenshots were not independently reviewed in this pass.

### Counterexamples and mathematical auditing

**u/UmbrellaCorp_HR's counterexamples and audits of the work led to significant improvements, including identifying a false positive where an AI claimed a proof that was not correct.** This records the owner's explicit attribution and the acknowledgement in the [project-history post](https://www.reddit.com/r/LLMmathematics/comments/1szs5wf/comment/olmxr22/). The contribution is credited at that scope; identifying a particular withdrawn paper or reconstructing its defective step is not a requirement of this attribution record.

### Positivity codes, prime production, and witness transport

The current [publication bibliography](research/expanded-2026-09-08/exact_bounded_transport_72/publication_bibliography.tex) already credits arithmetic, positivity-code and prime-production input, including equations (71)–(100). The newly supplied text *Untitled 1738.md* contains that numbered continuation: finite hit bits, minimum-code selectors, a constrained CRT construction, cyclotomic prime production, exact witness transport, and an obstruction to one proposed combination of prime generation and transport.

The text explicitly distinguishes constructing larger primes from covering all target primes, and leaves universal positivity and the required predecessor condition unproved. The register preserves those limits without reducing the contribution to 'just a restatement'. [Detailed reading and locators](provenance/2026-09-10/UPLOAD_READING.md#positivity-crt-prime-production-and-transport).

### Orchard descent, induction testing and research direction

*Untitled 1736.md* documents a proposed primitive-ray/orchard descent, subsequent refinement, and a reported execution checkpoint. The later checkpoint retains a decreasing determinant construction and local inheritance argument, but records a counterexample to stronger local-leaf forcing and an unresolved global base obligation. It explicitly reports one assistant, no independent mathematical reviewers, and no theorem promotions. This is evidence of an attempted and refined argument, not a completed proof of ES. [Detailed reading](provenance/2026-09-10/UPLOAD_READING.md#orchard-descent-and-its-recorded-obstruction).

### Full research specification and later unary selectors

*Untitled 1737.md* includes a broad continuation specification and later formulas (143)–(178). It retains the original problem, arithmetic distinctions, failures and audit requirements, and develops explicit p-only selectors. The two-layer universal assertion is labelled unproved in the source. The initial instructions are evidence of the investigation's intended scope, not instructions inherited by the present editor. [Detailed reading](provenance/2026-09-10/UPLOAD_READING.md#research-specification-and-unary-code-continuation).

These files are the **latest supplied portion**, not the whole of this person's contribution. The owner reports substantial joint and private discussion beyond them. Attribution at individual-formula level remains open where human/model or joint authorship cannot be separated from the surviving record.

## u/CommonCareful3149: the mod-107 deficit progression

The owner has now supplied the actual message text, attributing it to this handle. It states that u/UmbrellaCorp_HR suggested contact and describes the case p = 8,803,369, residual 107, with the deficit in Z/53Z

\[
D=\{23+42j\pmod{53}:0\le j\le9\},\qquad |D-D|=19=2|D|-1.
\]

**Contribution:** the arithmetic-progression/difference-set observation and proposed explanation of two-translate saturation. The message expressly makes no novelty claim and says a two-page note had been prepared. Receipt of that note has not been established. The private message is summarized here; its full conversational wording is not republished.

There is already a public reconstruction in the [focused mod-107 workbench](https://github.com/KokunoYumeto/erdos-straus-workbench/blob/240c4e1db1ca8e07d21a7a8a5f9a0a043cb3aa95/work/MC-ES-PACKET-R107-001/r107_deficit_progression.tex). Its title credits this community lead, it reproduces the same progression, and it links [a Reddit post](https://www.reddit.com/r/LLMmathematics/comments/1vy127z/). That permalink could not be retrieved in this pass. The focused workbench's reconstruction and listed Python/Lean certificates are downstream objects, not the missing original note, and were not replayed here.

## u/JGPTech: an upstream marked-factor/pipeline source

The [pipeline discussion](https://www.reddit.com/r/mathematics/comments/1v5sbya/claude_used_my_pipeline_to_find_a_counterexample/) is explicitly cited in the [5 August archive](https://zenodo.org/records/21805460). It belongs in the imported-source history for marked-factor/Fable-coordinate comparisons.

**Scope of attribution:** a cited upstream source, not automatically a direct ES participant. Its headline about the external Jacobian discovery remains the source author's claim; this provenance pass does not establish the causal history of that external result. The source author's contribution, the independently cited mathematical constructions, and later ES transformations must remain separate.

## KokunoYumeto / u/lepthymo: specified research contributions

The owner explicitly confirms that GitHub **KokunoYumeto** and Reddit **u/lepthymo** are the same contributor and authorizes that public association. Speech-transcribed spelling variants are not additional identities. The contribution is not reduced to an organiser label.

The [original reply](https://www.reddit.com/r/LLMmathematics/comments/1sysemj/how_gpt55_and_gemini_31_pro_mapped_the_deep_tail/) records commissioning an analytical treatment with GPT-5.5 and then proposing a lattice investigation motivated by the numbers 24 and 6. The [ongoing history post](https://www.reddit.com/r/LLMmathematics/comments/1szs5wf/erd%C5%91sstraus_conjecture_umbral_moonshine_project/) records the snowflake/star idea, Niemeier and Leech directions, support-sensitive zero constructions, Busy Beaver comparison, bicomplex/Cayley–Dickson/tessarine experiments, source introductions, and demands to derive rather than discard signs. The supersignum and circle-packing replies document further AI-assisted development and integration.

The owner now supplies two additional motivations: pushing Leech-lattice maps so established knowledge might transfer back, and asking for an Ogg-observation comparison. The former is consistent with the contemporaneous Leech direction; the precise knowledge-transfer rationale and Ogg request are marked as current retrospective testimony, not given invented historical timestamps.

**Credit:** proposing these research directions and examples; directing and developing investigations with AI; importing and connecting other people's contributions; specifying proof and source-fidelity requirements; and maintaining the public sequence of outputs. This does not make all generated mathematics a personal theorem of the operator. The model contributions and original mathematical literature retain their own attribution.

## Received collective Turn 7 continuations

The 20 September fixed-input/Fable continuation, cofactor-capacity completion,
five-track ES/Fable/RH continuation, original integral completion,
defining-prime calculation, and four-track arithmetic-frame/descent
continuation were supplied to this repository under the collective attribution
**The Clankers**. The preserved source files do not identify an originating
task or a separable individual contributor. Their exact received bytes,
hashes, mathematical corrections, and integration decisions are recorded in
[the fixed-input audit](research/incoming/es-fable-zeta-bridge-20260920/INTEGRATION_AUDIT_20260920.md)
and [the capacity audit](research/incoming/es-turn07-capacity-completion-20260920/INTEGRATION_AUDIT_20260920.md),
the [multi-track audit](research/incoming/es-rh-multi-20260920/INTEGRATION_AUDIT_20260920.md),
the [integral audit](research/incoming/es-turn07-integral-completion-20260920/INTEGRATION_AUDIT_20260920.md),
the [defining-prime audit](research/incoming/es-defining-prime-continuation-20260920/INTEGRATION_AUDIT.md),
and the [arithmetic-frame audit](research/incoming/es-rh-continuation-b-20260920/INTEGRATION_AUDIT.md).
This register preserves the supplied collective credit and does not infer an
individual name.

The arithmetic parametrizations used in these modules retain their human
literature lineage.  The Type-I/Type-II coordinates are cited to Christian
Elsholtz and Terence Tao, and the character and arithmetic-surface antecedents
are cited to Martin Bright and Daniel Loughran.  Standard local algebra,
Dirichlet and finite-morphism inputs are cited at their exact points of use.
Collective attribution for the new coordinate calculations does not replace
those sources.

## What is deliberately still unresolved

The exact novelty of the first computational observation; each CivQ17 figure's use; full attribution within unshared joint conversations; the original CommonCareful two-page note; and the outcome of several lateral research requests remain incomplete. The [handoff](provenance/2026-09-10/HANDOFF.md) records them as missing links, not reasons to delete credit or invent a completed bridge.
