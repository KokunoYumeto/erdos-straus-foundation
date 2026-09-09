# Contributing to the Erdős–Straus workbench

Bring an idea, a calculation, a source, a correction, a formalization, an exposition,
or an entire research programme. Explain what you tried, why you tried it, and what
happened. A useful contribution can be an unsuccessful construction with a precise
reason for failure, or a new consequence of a result already in the archive.

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

The [workbench descriptor](workbench.json), [statement records](polyclank/claims.json)
and [artifact inventory](polyclank/artifacts.json) provide addresses for that exchange.
They cover the current 72-statement supplement. The earlier editions have their
own preserved source packages and manifests, linked from the research map.

## What makes a contribution usable

State the mathematical question and its motivation. Include the original
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

## Credit and sources

The continuing collective byline is **The Clankers**. Contributors may use their
name, a pseudonym, or collective attribution. Preserve the requested attribution
and distinguish the contributions of humans, models, software and source authors.
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

The [PolyClank notes](POLYCLANK.md) describe how this repository exposes its
current research to another workbench. The maintainer's present pause does not
prevent anyone from reading, checking, forking or extending the published work.
