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
published 86-page supplement describes the full finite witness sets at primes $p=12h+1$,
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

**17--21 September structural continuation:** a seven-turn programme is preserved
in twelve linked records because Turns 6 and 7 have complementary
continuations. Each record retains both the result and the exact limitation
that determines the remaining mathematical question. The
[dated proof bulletin](DAILY_RESULTS_20260919.md) gives stable result IDs and
proof locators without reconstructing a programme timeline.

1. [Simultaneous exterior/middle failure](research/incoming/es-turn01-joint-failure-20260917/README.md)
   classifies the complete original exponent boxes through effective quotient
   order eight, proves every factor-cut inequality, and identifies the exact
   prime-residual index-six normal form.
2. [The complete shifted-factor graph](research/incoming/es-turn02-shifted-graph-20260918/README.md)
   proves the all-edge transition and closure theorem, then gives a genuine
   seven-vertex sink of locally empty selectors at $p=2521$. This disproves the
   proposed local/cycle implication, not Erdős--Straus.
3. [Primitive sextic triangle and square-source escape](research/incoming/es-turn03-primitive-sextic-20260918/README.md)
   gives a certified constant-$C_6$ three-cycle, refuting strict canonical
   descent while proving the corresponding square-source escape statements.
4. [Mixed square-source expansion](research/incoming/es-turn04-square-expansion-20260918/README.md)
   proves that every set of at most five external nonresidue vertices has an
   outside factor among $t\in\{1,3,5,7,9\}$, obtains six reachable vertices in
   at most 25 factorizations, and reduces every fixed-cardinality closed set to
   a finite original cycle--cofactor domain.
5. [Exact channel coupling](research/incoming/es-turn05-channel-coupling-20260919/README.md)
   constructs a genuine exterior/middle involution and sharp joined windows,
   proves the complete $2\tau(h)$ pair fibres and Möbius return, and shows
   exactly why immediate factor and reciprocal-source repairs can still fail.
6. [Complete-shell spectral bounds](research/incoming/es-turn06-full-shell-20260919/README.md)
   proves a quantitative obstruction to principal/adverse-sign domination,
   an exact integer collision lower bound, and proper nonprincipal certificates
   including a five-mode proof of 60 target pairs at $p=944329,R=47$.
7. [Pointwise localization](research/incoming/es-turn06b-pointwise-localization-20260919/README.md)
   bounds every possible original middle and exterior state using the least
   quadratic nonresidue, proves the exact free fourfold fundamental domain, and
   records the corrected equality and endpoint cases. It narrows the remaining
   source but does not prove that it is occupied.
8. [Sharp square-root middle atlas](research/incoming/es-turn07-middle-cutoff-20260919/README.md)
   proves sharp general and hard-prime bounds for the smaller of the two exact
   middle cofactors, constructs a complete disjoint direct/cofactor atlas with
   an explicit inverse, and proves that no fixed prime-independent list of the
   original grades can cover all hard primes. The atlas can still be empty at a
   prescribed prime; universal E/M occupancy remains open.
9. [Exact exterior complement--norm atlas](research/incoming/es-turn07b-exterior-atlas-20260919/README.md)
   proves the strict cubic cutoff for the least of the residual, exterior
   cofactor and complementary divisor; constructs complete disjoint direct,
   reciprocal and norm charts with exact inverses; separates the exterior
   cofactors from the middle square-root bound; and gives an integer family
   attaining the cutoff scale. It does not prove exterior occupancy.
10. [Small-shape rigidity and channel rescue](research/incoming/es-turn07-shape-rigidity-20260919/README.md)
    equips every exterior state with an exact ordered marked cubic and inverse,
    sends every diagonal cofactor state to an original middle state, classifies
    all hard-prime shapes through radius seven, and sends the sole possible
    nonsingular radius-eight shape to a middle state. The natural cubic
    involution is calculated exactly and shown not to preserve the fixed-prime
    source. These are branch reductions, not universal occupancy.
11. [Normalized ES quartic and exact Fable--weighted-conductor bridge](research/incoming/es-fable-zeta-bridge-20260920/README.md)
    maps every positive integral witness at a prime $p\equiv1\pmod {12}$ to a
    quartic whose distinct literal roots are $p,x,y,z$, recovers
    $p=-5u_4/u_3$ from its unmarked coefficients, proves the coefficient
    hypersurface and complete eight-point signed fibre, and transports the
    result through one fixed original weighted conductor. A separate
    seven-state reciprocal suspension retains its different nonproper locus.
    An explicit invertible raw-cell--Lorentz map transports the archived
    three-dimensional tetrahedron, and the odd receiving determinant pulls
    back to a primitive irreducible polynomial on the ES chart with a proved
    positive-real intersection. This is a structural bridge, not an occupancy
    or zeta-zero theorem.
12. [Prime-local Fable fibres and same-prime negative-square transfer](research/incoming/es-turn07-fabel-arithmetic-bridge-20260920/INTEGRATION_AUDIT.md)
    proves that an original exterior state has local fibre algebra
    $\mathbb Q_p^3\times K_{\rm ram}^2$, whereas a middle state gives
    $\mathbb Q_p^3\times K_{\rm unr}^2$; both have three local points, but
    their integral root orders differ by an exact index-$p$ quotient. It also
    constructs original same-prime middle states from negative-four-square
    exterior shapes and retains complete inverse fibres. Its stronger
    fixed-cofactor theorem gives a bijection from the finite divisor set
    (U\mid((h+1)/4)^2, h\mid p+4U) onto every original middle state with
    (Q=h), strictly extending the two selected square words. The received
    archive is preserved byte-for-byte; the linked audit and corrected build
    repair a missing exterior divisibility gate and two scope statements.
13. [Fixed-input cover, finite boundary completion, and odd-moment frame](research/incoming/es-fable-zeta-bridge-20260920/INTEGRATION_AUDIT_20260920.md)
    proves that every positive integral witness at a prime
    \(p\equiv1\pmod {12}\) enters the eight-sheet domain, with explicit
    fixed-\(p\) separation and inverse-coordinate bounds. At fixed nonzero
    \(p\), over
    \(\mathcal B_p=\{(A,C):ACd_p\operatorname{Disc}(g_p)\ne0\}\), the cover
    splits into ranks \(2+6\), has monodromy order \(48\), and has deck group
    \(C_2\times C_2\). The reciprocal signed coordinate
    gives a finite flat rank-eight completion with double-root fibre
    \(\mathbb C[\eta]/(\eta^4)\), while an invertible marked moment frame
    factors the separate odd receiving divisor exactly.
14. [Exact cofactor capacity and fixed-target returns](research/incoming/es-turn07-capacity-completion-20260920/README.md)
    classifies every divisor \(W\mid j^2\) in a fixed class
    \(t\pmod{4j-1}\) into canonical, companion, and finite branches with an
    exact inverse. The finite branch satisfies the sharp bound
    \(h\le t^2-3t+1\); actual hard-prime exterior states attain equality
    infinitely often. Every fixed \(t\ge4\) also occurs on infinitely many
    constructed exterior states whose complete same-grade middle box is
    empty. Those states already solve ES in the exterior channel, so this is
    not an ES counterexample.
15. [Exact ES/Fable/RH multi-track continuation](research/incoming/es-rh-multi-20260920/README.md)
    isolates a unique rank-three crossing on an explicit positive-real ES ray
    and gives the corresponding integral determinant dichotomy. It proves that
    the collision-completed trace pairing is the perfect residue pairing
    composed with multiplication by \(2\eta^3\), including the exact local
    residue-unit correction. It then constructs the typed
    residue-to-native-Gram multiplier and its retained ES relation defect.
    Its inverse-trace and common-parameter Bernstein results are RH-facing
    interfaces, not ES occupancy claims. The received packet, audit repairs,
    541-check replay, figures and reader are preserved together.
16. [Original integral signed completion](research/incoming/es-turn07-integral-completion-20260920/README.md)
    computes the literal-root rank-eight order over (mathbb Z_p), including
    every Smith factor, conductor, inverse lattice and reduction kernel.  The
    exterior and middle indices are (p^2) and (p^9); the Type-I boundary
    has (p) lifts modulo (p^2) and none modulo (p^3).  Its finite-place
    control family proves that the listed gates are not by themselves an
    integral-source certificate; it is not an ES counterexample.
17. [Defining-prime normalization and local signed characters](research/incoming/es-defining-prime-continuation-20260920/README.md)
    extends the original E/M calculation to every closer-pair collision
    stratum, proves the translated chart is an exact quadratic twist, and
    gives the fixed-prime rank-(2+6) fibre product.  Its signed-label
    representation satisfies the exact conductor-index identity, including
    the retained (p=1201) Frobenius calculation.
18. [Arithmetic frame nonsingularity and signed descent](research/incoming/es-rh-continuation-b-20260920/README.md)
    proves a three-character sufficient condition for nonsingularity of the
    original odd receiving frame on exactly (3456) reduced classes modulo
    (521220).  The actual witness ((13;4,18,468)) has no original signed
    point over (mathbb F_{61}), eight over (mathbb F_{61^2}), and eight
    points on its specified nonsquare twist over (mathbb F_{61}).  Its two
    adjacent tracks prove the sharp determinant return and finite heat
    remainders while retaining their separate metric and verification scope.
19. [Global trace integrality and exact raw-source fibres](research/incoming/es-turn07-trace-rigidity-20260920/README.md)
    proves that, for rational ES denominators, two integral power traces force
    all three denominators to be integers.  On the complete raw integer gate,
    one integral literal trace recovers the original divisor budget and its
    E/M channel; the only two-point fibres are the retained middle
    orientations.  The package also classifies every possible common
    denominator at length three, computes the square-part obstruction when the
    gate is removed, and constructs the exact irrational algebraic boundary
    showing why rationality cannot be dropped.  The three-page preprint,
    ten-page workbench, illustration and independent executable replay are
    included.
20. [General-family source geometry, ES-labelled jets, and collision exponents](research/incoming/es-rh-family-integration-c-20260920/README.md)
    proves the exact mixed-source minimum and its kernel/observation determinant
    allocation, a certified positive-range inverse, the common reducing space
    and centre--length covariance of the ES-labelled tensor action, and the
    complete two-regime collision exponent diagram. Its canonical/constructed
    metric separation and heat-scale split consume the pinned NG20--NG21
    theorem on a stipulated off-line quartet. They do not assert such a zero,
    an RH conclusion, universal ES occupancy, or a new integer witness.
21. [Exact original-divisor descent and the nine-word boundary](research/incoming/es-turn07-divisor-descent-20260921/README.md)
    classifies every same-channel return from a rational positive trace source
    that keeps the original divisor word and replaces its residual by a divisor.
    The complete positive domain is
    \(k\mid R\), \(d\mid k\), \(k\equiv1\pmod{4K(u)}\), with
    \(R'=R/k\) and \(a'=(p+R')/4\); its global inverse fibres and free-abelian
    kernel are explicit.  A uniform strict descent exists for exactly the nine
    words \(u\mid36\).  For every other word a reduced CRT/Dirichlet family
    gives infinitely many proper middle trace sources with no same-word return,
    even after the middle complement.  Separate endpoint solutions show that
    these are method obstructions, not Erdős--Straus counterexamples.
22. [Global sign for the literal odd receiving determinant](research/incoming/es-turn07-global-receiver-determinant-20260921/README.md)
    proves, for every positive integral witness at every prime
    \(p\equiv1\pmod {12}\), the strict bound
    \(\mathfrak N<-(125873811/262144)p^8\).  For
    \(p\equiv1\pmod {24}\), the constant improves to
    \(327448292668/47045881\).  It keeps the original complex receiver,
    determinant phase, root labels and square-root signs and obtains
    \(|\det O|>4cp^8/S^3\) and
    \(\|O^{-1}\|_2<360S^9/(cp^8)\).  Its exact real counterdomain has one
    collision-free singularity outside both integral coordinate domains.
    [Pinned theorem and complete proof](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6bdfce25724b95a4b30e97f0df69879a87793302/research/incoming/es-turn07-global-receiver-determinant-20260921/core.tex#L1-L488).
23. [Sharp receiver growth, exact defect, and finite heat limits](research/incoming/es-turn07-sharp-receiver-growth-20260921/README.md)
    strengthens the global sign to uniform compound-inverse bounds
    \(\|O^{-1}\|_2<360p\sqrt w/\gamma\),
    \(\|\wedge^2O^{-1}\|_2<180/\gamma\), and
    \(\|\wedge^3O^{-1}\|_2<41/(4\gamma p^2)\), where
    \(\gamma=80/6279^4\).  Thus at most one inverse singular direction can
    become unbounded.  Two actual prime families prove the exponents sharp;
    the exact exceptional divisor in the enlarged distinct-positive-root
    receiver space has rank three with explicit kernel and cokernel and is
    disjoint from the integral witness locus. A fixed-\(c\) family supplies all four first singular
    corrections and the scalar-observation powers \(0,2,3,15\).
    [Readable PDF](output/pdf/ES_Sharp_Receiver_Growth_20260922.pdf); [pinned
    main theorem and proof](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/e713c342fc16e361e104de3322790ca0cee7281d/research/incoming/es-turn07-sharp-receiver-growth-20260921/core.tex#L75-L636).
24. [Modulo-24 mixed trace return and primitive-ray boundary](research/incoming/es-turn07-mod24-ray-trace-20260922/README.md)
    starts with a positive rational trace source at a prime
    \(p\equiv1\pmod {24}\) whose first denominator is \(a=cq\), with
    \(c\mid6\) and \(q>3\) prime, and constructs an original integral middle
    witness at the same prime.  The exterior branch has a complete
    ray-preserving deletion criterion, nine automatic primitive rays, exact
    squarefree fibres and an inverse retaining the old square factor.  Every
    nonautomatic ray has an infinite reduced progression obstructing this
    universal return rule, while a separately constructed middle witness
    keeps that obstruction distinct from an ES counterexample.  The complete
    trace-return/receiver composite has explicit domain, codomain, fibres,
    determinant and exterior-power bounds.
    [Readable PDF](output/pdf/ES_Mod24_Ray_Trace_and_Receiver_20260922.pdf);
    [pinned mixed theorem and exact coordinates](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/e713c342fc16e361e104de3322790ca0cee7281d/research/incoming/es-turn07-mod24-ray-trace-20260922/core.tex#L9-L322).
25. [Complete mixed-return fibres and hard-middle spectra](research/incoming/es-turn07-fibres-middle-spectrum-20260922/README.md)
    closes the bare sorted M-origin fibre left open by item 24. For every
    supplied sorted middle target it gives the complete disjoint E/M inverse,
    including every square-factor parameter, carrier test, tail order,
    complementary word and cross-channel collision. Its receiver theorem
    reconstructs the target and the four selected square-root branches from
    the full labelled matrix without selecting a unique arithmetic preimage.
    A fixed-positive-\((R,u)\) middle family has singular powers
    \(9,4,3/2,-3/2\), every first relative coefficient, and the exhaustive
    observation powers \(0,2,3,9\). Two reduced prime progressions in
    \(1\bmod840\) prove that the inherited inverse powers
    \(p^{3/2},1,p^{-2}\) are sharp already on middle witnesses.
    [Short PDF](output/pdf/ES_Complete_Mixed_Fibres_20260922.pdf);
    [complete workbench PDF](output/pdf/ES_Mixed_Fibres_and_Hard_Middle_Spectra_20260922.pdf);
    [pinned coordinate proofs](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/687d16739a10788b6f1b079d0c079cc68cbfc5f7/research/incoming/es-turn07-fibres-middle-spectrum-20260922/core.tex#L74-L641).
26. [Original trace defects and factor-sum/Pell returns](research/incoming/es-turn07-square-zero-pell-20260922/README.md)
    constructs the complete square-zero fine-defect coordinate from the original
    E/M divisor boxes, proves its mixed-channel law and sharp unit-direction
    saturation threshold, and classifies every prime-power middle trace. Its
    factor-sum map has exact positivity, gcd reduction, inverse fibres and a Pell
    specialization. A distinct fixed-tail-sum classifier proves that every
    proper prime-square trace with word `q` or `q^3` has no same-sum integral
    target whose residual is a proper divisor of the source residual, even when
    channel and word change. The least-prefix certificate at `p=67369` refutes
    universal nonincreasing trace repair, not Erdős--Straus.
    [Complete PDF](research/incoming/es-turn07-square-zero-pell-20260922/workbench.pdf);
    [pinned proofs](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6c064a07298cdba38352998364ce6b7cb3efa973/research/incoming/es-turn07-square-zero-pell-20260922/core.tex#L340-L1046).
27. [Affine channels, mixed-order sections, and upward return](research/incoming/es-turn07-mixed-order-upward-20260923/README.md)
    proves the exact common-trace locus and affine E/M shift, then identifies the
    labelled two-channel count as an injective odd-order lattice operator with
    an alternating inverse and an orbit-parity cokernel. A partial radix chain
    reduces the remaining problem to an exact quotient-support cover and proves
    that two channel labels cannot replace a missing final radix when the
    residual steps stay in a proper subgroup. The complete mixed-order decoder
    and divisor-DAG criterion retain every bounded exponent and cyclic carry.
    Separately, the labelled `4a+s` fibre crosses the `p=67369` obstruction by
    an exact upward shell return and extends along a reduced prime progression.
    [Complete PDF](research/incoming/es-turn07-mixed-order-upward-20260923/workbench.pdf);
    [short PDF](research/incoming/es-turn07-mixed-order-upward-20260923/preprint.pdf);
    [pinned affine and quotient proofs](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6125e74b1aadb860965964e2ae3587c902dbbab8/research/incoming/es-turn07-mixed-order-upward-20260923/core.tex#L101-L365);
    [pinned factor-exchange proof](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6125e74b1aadb860965964e2ae3587c902dbbab8/research/incoming/es-turn07-mixed-order-upward-20260923/core.tex#L611-L786).

The first four steps produce and transport factors; the fifth couples the
original $E/M$ channels; the packaged sixth attacks their complete first-half
positive pair sum; its parallel pointwise continuation localizes every possible
original state; the Turn 7 continuations give sharp finite atlases for the
complete middle and exterior sources, then remove the diagonal and every
hard-prime radius-at-most-eight exterior branch by explicit original middle
returns. The eleventh result then places every occupied exterior state in the
generic signed Fable cover and a fixed weighted conductor with all fibres and
information loss explicit; the exact elementary transform to the reciprocal
suspension has a one-scale fibre and a proved 14-point signed fibre product.
The twelfth computes the prime-local fibre and integral-order difference
between the two channels, changes the arithmetic target on an exact
negative-square family, and completes the entire fixed-(Q=h) middle fibre.
The thirteenth removes the exterior-only restriction from the distinct-root
domain theorem, computes the fixed-input monodromy and deck actions, and
retains collision fibres without cancelling the original meromorphic pole.
The fourteenth solves the fixed-target divisor capacity problem, identifies
its sharp finite boundary, and shows exactly when same-grade repair can fail
despite an existing exterior state.
The fifteenth locates the exact odd-frame rank loss on a positive-real solution
ray, separates perfect residue duality from trace degeneration, and returns the
finite algebra to the native moment metric through a proved multiplier and
defect. Its final two tracks improve RH-side conditioning and certificate
propagation without being counted as ES occupancy progress.
The sixteenth and seventeenth identify the complete integral lattice defect at
the defining prime, prove the exact relationship between the two received
presentations, and carry the collision data into local signed characters.
The eighteenth excludes the receiving-frame divisor on an explicit infinite
set of prime classes and gives a fully typed arithmetic-descent example; it
does not turn failed character tests into singularity claims.
The twentieth continuation determines how the supplied finite tensor sections
sit inside the original physical source. It separates the constructed and
canonical metrics, resolves the kernel/observation allocation of the joint
minimum, computes the full ES-labelled reducing enlargement and mixed
covariance, and evaluates every two-centre collision exponent. The finite
source and collision theorems are unconditional at their stated inputs; the
metric asymptotics retain their explicit dependence on NG20--NG21.
The twenty-first continuation acts earlier in the arithmetic pipeline: it
starts from a rational positive tail pair with integral trace, computes every
residual-divisor arrow back into the original integral source, and proves the
exact fixed-word boundary of that arrow.  It strengthens the trace-rigidity
and fixed-target capacity results without manufacturing the still-missing
initial trace source at an arbitrary prime.
The twenty-second continuation closes the odd-receiver singularity question
on the complete integral witness domain.  Its exterior and middle polynomial
certificates remove the earlier three-character restriction and give an
explicit inverse bound.  The theorem is conditional only in the literal sense
that it starts from an existing Erdős--Straus witness; it does not force the
first occupied source at a prescribed prime.  The unique positive-real
singularity and a failed-gate rational source record the two exact boundaries.
The twenty-third continuation determines sharp inverse-side conditioning:
at most one inverse singular direction can diverge, and an
explicit prime family attains that growth. The
three compound scales have sharp exponents, and the singular divisor in the
enlarged distinct-positive-root space has an explicit rank-three defect and
does not meet the integral witness locus. The fixed-\(c\) calculation then
resolves every first correction and the finite heat hierarchy without changing
the receiver or its label metric.
The twenty-fourth continuation moves back upstream.  Its mixed trace theorem
changes a rational source into an integral original witness on a specified
prime-shell domain, and its exact composite then carries that witness into the
now-controlled receiver.  The nine-ray theorem is maximal for the universal
ray-preserving rule; this does not prove that a required trace source exists at
each hard prime.
The twenty-fifth continuation computes the entire arithmetic fibre that the
twenty-fourth left open, then separates that finite source multiplicity from
the sixteen receiver frames. Its fixed-residual middle calculation supplies
new first corrections and a different exhaustive observation hierarchy, and
its two hard-prime progressions prove all three inherited inverse exponents
sharp inside the class \(1\bmod840\). These are post-witness and inverse-fibre
results; they do not force a first trace source at every hard prime.
The twenty-sixth continuation returns to the unoccupied source itself. It
constructs the square-zero defect without replacing the original divisor box,
proves two complete source-changing classifiers, and supplies exact
counterexamples to nonincreasing or fixed-tail termination rules. The
twenty-seventh then proves what combining the E/M labels can and cannot do:
the affine pairing retains the full coefficient vector through a signed
inverse, while a partial chain succeeds only through a genuine quotient-support
cover. This is the current structural target; finite census size is not treated
as evidence for arbitrary-prime occupancy.
After composing the earlier diagonal and radius-eight returns, every residual
exterior state has shape radius at least nine. These results isolate, but do
not prove, the remaining unbounded-shape occupancy statement. None asserts the
still-missing universal positivity theorem.
Each directory contains the complete proof, exact maps, executable certificates,
source lineage, negative controls, and an explicit handoff where one was made.
The [20 September proof bulletin](DAILY_RESULTS_20260920.md) gives stable IDs for
the quartic, fibre, conductor, monodromy, boundary and root-algebra results.
The [21 September proof bulletin](DAILY_RESULTS_20260921.md) gives stable IDs
for the trace descent, complete arrow fibres, nine-word classification,
optimality construction, global receiver sign, inverse bound and exact real
counterdomain.
The [22 September proof bulletin](DAILY_RESULTS_20260922.md) records the sharp
receiver exponents, singular defect, first corrections, mixed trace return,
nine-ray boundary, obstruction families, exact receiver composite, complete
mixed-return fibres, fixed-residual middle spectrum and hard-middle sharpness.
The [23 September proof bulletin](DAILY_RESULTS_20260923.md) records the
square-zero obstructions, affine channel operator, mixed-order section,
quotient-support criterion and upward factor exchange.

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
| Current GitHub cumulative ES/Fable reader (124 pages) | [PDF](research/incoming/es-fable-zeta-bridge-20260920/output/pdf/ES_FABLE_ZETA_CROSSWALK.pdf) | [TeX, exact checkers and audit](research/incoming/es-fable-zeta-bridge-20260920/README.md) |
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
preserved. The manually requested 12--20 September continuations are available
on GitHub; they do not restart scheduled mirroring or replace the Zenodo edition.
This branch adds navigation and source-addressable records for the results bench,
the recovered bridge programmes, and the seven-turn structural continuation.

## Results and continuing bridge programmes

The [results bench](RESULTS.md) gives separately readable statements, proof notes,
source relationships and actual checking scopes. Its [machine-readable records](results/records.json)
complement the larger published statement index; they do not claim a complete ES
resolution, independent review of the archive, or novelty for every result.

The [recovered research directions](RESEARCH_DIRECTIONS.md) describe the project's
motivations, older Star–Kneser, Niemeier, Ogg, Busy Beaver, split-zero and geometric
work, and the remaining questions. They preserve open directions without assigning
the next researcher a compulsory task list. The raw chat archive remains private.
