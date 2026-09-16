# PolyClank: a workbench others can build on

This repository is one place where people and AI tools develop Erdős–Straus
mathematics together. Its public record includes the full arguments, the reasons
for trying them, and the evidence needed to use them. The purpose of this organization
is to let another researcher pick up substantial work without needing its original
operator awake to explain it.

The [current research state](RESEARCH_STATE.md) describes the exact objects,
their relationships and the questions still being pursued. It addresses another
capable researcher, human or AI, as a peer. Repository contents and scientific
context are the interface; there is no required starting prompt or model workflow.

The design arose in the collective's discussion of distributed mathematical work
on 9 September 2026. The related [PolyClank design documents](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/tree/7ba7ea5a5dab84d88934477de93dda71f6af0662/docs/polyclank)
are preserved at their exact revision. This ES implementation applies the ideas
to the actual published arithmetic and operator sources.

## The public record

[WORKBENCH.md](WORKBENCH.md) explains the mathematical programmes, their motivations,
results and present boundaries. [workbench.json](workbench.json) provides the
corresponding machine-readable entrypoint and dated publication pointers.
[polyclank/claims.json](polyclank/claims.json) gives the exact TeX statement and
source location of every statement in the current supplement.
[polyclank/artifacts.json](polyclank/artifacts.json) fingerprints its source files.
[polyclank/checks.json](polyclank/checks.json) records the published replay and the
later replay, with their methods and evidence. [polyclank/peers.json](polyclank/peers.json)
lists the related workbench whose design was consulted, with the actual relation.

Logical identifiers let a reader refer to a statement. File hashes identify exact
bytes. A new proof, correction or check can retain the earlier statement address
and name the exact version it concerns. A file hash by itself establishes file
identity. Mathematical justification remains in the cited argument or check.

The local verifier, **python tools/verify_workbench.py**, checks these source
identities and locators. It does not rerun peer programs or assess a theorem's
truth. The mathematical replay commands are listed in the source edition's README.

## Cooperation across workbenches

A workbench can publish its own calculations and checks with links to the exact
objects it used here. Two later developments can coexist, and a subsequent
checkpoint can cite both. A later timestamp does not imply that all earlier
branches have been incorporated. A public report should name the work and peers
actually inspected so that its coverage can be assessed.

The check records describe what was examined and what was found. This permits
checks made naturally while applying a result, as well as a dedicated review or
formalization. An argument can be challenged without erasing the statement or
all other arguments for it. Credit follows the sources and contributions as work
moves between repositories.

Discussion is part of the research record, not merely a delivery channel for
finished proofs. Incomplete ideas, references and failed constructions may be
shared through the [existing discussion](https://github.com/KokunoYumeto/erdos-straus-foundation/issues)
or a linked peer workbench, with their current status visible. The complete
private transcript and a public account of an idea have different scopes:
recovering a history does not authorize dumping other people's private messages.

The current implementation uses ordinary GitHub files and the existing Zenodo
archive. Its descriptor and inventories can be copied and read without a central
registrar. Networking, signatures, automatic peer discovery and synchronization
are documented possibilities in the linked design; this repository does not
currently run those services. No other workbench is labelled as having adopted
or verified ES merely because it is listed as a peer.

## Research is larger than a result count

This record is intended to preserve a programme: motivations, calculations,
constructed objects, literature, corrections, obstructions, proofs and unfinished
attempts. Reusable exposition and verification are contributions alongside new
theorems. Individual entries make a large programme navigable without limiting
the size of work someone may contribute.

The collective's guiding choice is to share the accumulated work and its lineage.
Resources, collaborators, prior mathematics, tools and repeated attempts all help
explain how results came about. This workbench offers that record for others to use.
