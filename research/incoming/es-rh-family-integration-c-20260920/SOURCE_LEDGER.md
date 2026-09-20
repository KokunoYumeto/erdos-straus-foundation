# Source ledger and reading boundary

## Received Family C package

The integration source is *General-family control: multiplicities, collisions, source sections, and all mixed minima*, dated 20 September 2026. No individual author is identified in the supplied text.

- preserved source: sources/GENERAL_FAMILY_INPUT.md
- source SHA-256: ec8af51f2ff9c5ce06355e3ec9dda2a84e6216a63b04416093bd98bb0a270a9c
- received archive: received/ES_RH_Family_Integration_20260920_C.zip
- archive SHA-256: 15f8ae123c03ebac60b1e152530777000ecfbdb99ab901cb0b7e94098e5c7a8e
- pasted result: received/PASTED_RESULT.md
- pasted-result SHA-256: d983d699a4ae58967537c8639f466e70189fc3fea42e6bb256039651bfb5d911

The entire 979-line GF source was read. The calculations use GF(3)–GF(18) for the tensor/jet metric and variance, GF(19)–GF(35) for the aggregate and physical source-section realization, GF(36)–GF(39) for the cross Gram and joint minimum, GF(49)–GF(54) for the two-centre evaluation and weighted-minor problem, and GF(55)–GF(60) for the constructed heat scale.

The standalone Programme_General_Families_20260920.zip named inside that note was not included as a separate archive. Family C therefore preserves, cites, and checks the equations actually present in GENERAL_FAMILY_INPUT.md; it does not claim replay of absent files.

## Native Gaussian theorem provider

MR7–MR10, MR14, and JS15 use the proved native compression law NG20 and rank-one identity NG21 from:

- repository: KokunoYumeto/zeta-function-research-reader
- source version: b1f3e2e1879c40f411eb263dde171589cb5f9390
- file: workbenches/splitzero-tandem/continuations/20260920-gaussian-arithmetic-return/NATIVE_GAUSSIAN_TRANSFER.tex
- local verified source: C:/Users/Floris/Documents/math/work/gaussian_arithmetic_publication_20260920/transaction/outgoing/workbenches/splitzero-tandem/continuations/20260920-gaussian-arithmetic-return/NATIVE_GAUSSIAN_TRANSFER.tex
- Git blob: 6122e3b4f165df907a46ddcbc739f4dc159d65c6
- read range used here: NG16–NG22, including the exact hypotheses and the distinction between the canonical and observed minima.

The local file has the recorded Git blob. Family C uses the provider as a theorem dependency; it does not reprove the varying-measure asymptotic or replace it with its finite checkers.

## Erdős–Straus input

ER11–ER15 use only:

1. a sorted positive integral witness
   \[
   4/p=1/x+1/y+1/z,\qquad 0<x\le y\le z;
   \]
2. its retained literal labels \((p,x,y,z)\);
3. the elementary consequence \(x\le3p/4\), proved directly in ER11;
4. the labelled tensor occupations and their exact multinomial weights.

The earlier repository version read during package construction was 34e45e06694c66650ddb4550bbf48c60ce75d8f9. This integration was applied to repository base 5787b359a73edd62130caf76f573a40d607463c1. The publication commit is recorded after integration in the repository history.

For literature provenance, the Type I/Type II arithmetic background was checked against:

- Christian Elsholtz and Terence Tao, “Counting the number of solutions to the Erdős–Straus equation on unit fractions,” Journal of the Australian Mathematical Society 94 (2013), 50–105, arXiv:1107.1010v6, §2.

The witness-to-jet construction in ER is proved in this module. It is not attributed to that paper.

## Linear-algebra and combinatorial references

- Nicholas J. Higham, “What Is the Singular Value Decomposition?”, 13 October 2020. Read for SVD, norm, and singular-space conventions. MR4–MR6 and CP9–CP11 prove the required exterior statements in full.
- NIST Digital Library of Mathematical Functions, §26.3. Read for binomial definitions and generating-function conventions. The multinomial, falling-factorial Vandermonde, and weighted-minor identities are proved at their uses.

## Verification boundary

The exact Python/SymPy programs use explicit exceptions rather than removable assertions. Fresh ordinary and optimized runs execute every suite and compare receipts. They cover finite algebraic identities, synthetic positive metrics, and bounded collision cases. They do not evaluate native zeta moments, prove the NG20–NG21 asymptotic, prove the all-length collision theorem without the written minor argument, or constitute Lean verification.

The predecessor modules remain in their existing repository locations and inside the preserved received archive where supplied. They were not duplicated into this live module.
