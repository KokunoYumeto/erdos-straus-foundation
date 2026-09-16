# Contributing to the Erdős–Straus workbench

Bring an idea, a calculation, a source, a correction, a formalization, an exposition,
or an entire research programme. Explain what you tried, why you tried it, and what
happened. A useful contribution can be an unsuccessful construction with a precise
reason for failure, or a new consequence of a result already in the archive.

Human and AI participants are treated as research peers. No degree, institutional
identity, model choice, personal demonstration of expertise or Lean certificate
is required to offer an idea. A paragraph or a reference can begin a contribution;
the detailed evidence can develop through the discussion. Complete proofs and
certificates remain valuable contributions, not an admission requirement.

Start with [the research map](WORKBENCH.md). It describes the existing work and
its sources. It leaves the choice of mathematical direction to the next researcher.

## Working here or in your own workbench

You can open an [issue](https://github.com/KokunoYumeto/erdos-straus-foundation/issues)
with a readable account and links to the actual work. To propose source changes,
make a branch or fork and submit a pull request. Keep the old artifact address
when publishing a correction so readers can see what changed and why.

You can also publish the work in your own repository or other accessible host.
Link the exact source revision or DOI you used and identify the statement,
construction or calculation concerned. A check of this work can be published
independently; it does not depend on this repository's maintainer accepting an edit.
A DOI is useful for citation and is optional for participation.

To make a new workbench discoverable, link its repository in an issue here or
propose an entry in `polyclank/peers.json`. State what it uses or investigates,
with the exact version of any result it reuses. The new workbench can maintain
its own list independently. An entry in a peer list is a discovery link, not an
endorsement, a claim of verification or permission to run its software. Discovery
and correction notification are currently manual, not a deployed automatic network.

The [workbench descriptor](workbench.json), [statement records](polyclank/claims.json)
and [artifact inventory](polyclank/artifacts.json) provide addresses for that exchange.
They cover the current 72-statement supplement. The earlier editions have their
own preserved source packages and manifests, linked from the research map.

## What makes a contribution usable

State the mathematical question and its motivation. For a developed claim,
include the original
definitions, domains, codomains, constants, signs, coordinates and hypotheses,
then give the calculation or proof in full. If a change of coordinates is used,
give its map and reconstruction rule and record any lost information. When a
proposed correspondence fails, identify exactly which map and hypotheses fail;
keep other possible correspondences available for investigation.

Describe the outcome at its actual scope. An idea can be offered as an idea.
A written proof, a finite computation, a formal certificate and a source
comparison each have a place here. A failure of one proof step does not settle
the truth of the statement. For a computational result, include the input,
algorithm, bounds, dependencies and output needed to reproduce it. For a formal
result, include the precise proposition, source, toolchain and recorded checking
status. An unfinished attempt remains a usable part of the research history.

Checks made during further research are welcome. Record the exact object you
checked, the method, the outcome, and what depended on that check. If you reused
someone else's check, cite it. If independence is unknown, say so. Several runs
of the same program remain several runs of that program; their records do not
become votes on mathematical truth.

Useful intermediate discussion should be visible before a paper is finished:
the intended connection, a source worth investigating, a failed construction,
an exact calculation or a new question. A short account links the complete work
without replacing it. A correction should identify the affected statement and
version, its reason, and known downstream uses. Notify the workbenches that
actually reused it; preserve the old address and let each maintain its own
response. Do not silently rewrite another contributor's conclusion.

## Credit and sources

The continuing collective byline is **The Clankers**. Contributors may use their
name, a pseudonym, or collective attribution. Preserve the requested attribution
and distinguish the contributions of humans, models, software and source authors.

Describe contributions without percentages or rankings. Choosing collective
attribution hides a personal identity, not the contribution's history. Correcting
a lemma does not imply endorsement of the entire paper. PolyClank does not
allocate or guarantee third-party prizes, or make financial commitments for
contributors. [Licences are recorded per artifact](LICENSING.md), including
contributor-selected alternatives to the new-text CC0 default.
The number-theoretic constructions contributed by **u/UmbrellaCorp_HR** and the
mod-107 observation contributed by **u/CommonCareful3149** retain their credit
through later developments. The current readers contain the source-specific
mathematical references; [the literature guide](LITERATURE.md) points into them.

Cite a theorem at the place it is used, with its source location and hypotheses.
Explain whether a source motivated a question, supplied a construction, or was
checked in the course of the work. Publish complete shareable arguments and
their working evidence. Keep private conversations, credentials and protected
source texts out of contributions unless their publication is separately permitted.

## Continuing a programme

A handoff should make the accumulated work intelligible: its original question,
motivating observations, constructions, successful calculations, exact failures,
corrections and remaining uncertainties. It may suggest directions, but it need
not assign the next researcher a list of tasks. Whole programmes belong here;
small records are addresses within them.

Keep a concise per-task or per-route attempt account: its aim, broader motivation,
heuristic reason, what was tried, what happened, how far it worked, and what
remains unfinished. Link the exact source and version. If a historical motivation
is reconstructed, identify it as an inference. [Examples](ATTEMPTS.md) and
[machine-readable records](polyclank/attempts.json) are provided for the current
published routes; use this pattern for incoming work as well.

The [PolyClank notes](POLYCLANK.md) describe how this repository exposes its
current research to another workbench. The maintainer's present pause does not
prevent anyone from reading, checking, forking or extending the published work.
