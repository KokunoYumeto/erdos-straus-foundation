#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (c) 2026 The Clankers
"""Check the peer entrypoint and optionally replay recovered quotation locators.

This does not prove theorems or execute another workbench's code. Python standard
library only. --transcript-dir reads two exact local exports; it never uploads them.
"""

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def require(test, message):
    if not test:
        raise ValueError(message)


def local_path(value):
    path = (ROOT / value).resolve()
    require(path.is_relative_to(ROOT), f"Path leaves repository: {value}")
    require(path.exists(), f"Missing target: {value}")
    return path


def check_transcripts(records, directory):
    sources = {}
    for source in records["sources"]:
        data = (directory / source["export_filename"]).read_bytes()
        require(len(data) == source["bytes"], "Transcript byte count differs")
        require(hashlib.sha256(data).hexdigest() == source["sha256"],
                "Transcript hash differs")
        # Export locators count LF-delimited physical lines, not Unicode
        # separators embedded in the messages.
        lines = data.decode("utf-8").split("\n")
        if lines[-1] == "":
            lines.pop()
        lines = [line.removesuffix("\r") for line in lines]
        require(len(lines) == source["lines"], "Transcript line count differs")
        sources[source["id"]] = lines
    for idea in records["ideas"]:
        lines = sources[idea["source"]]
        start, end = idea["line_start"], idea["line_end"]
        require(1 <= start <= end <= len(lines), "Invalid quote span")
        require(idea["quote"] in "\n".join(lines[start - 1:end]),
                f"Quote differs: {idea['id']}")
        roles = [s for s in lines[:start] if s in ("## Prompt:", "## Response:")]
        require(roles and roles[-1] == "## Prompt:", "Quote outside user block")


def check_elementary_examples():
    # Finite sanity checks; universal identities and prime-class reduction are
    # written explicitly in RESEARCH_STATE.md, not established by this loop.
    count = 0
    for p in range(2, 1001):
        triples = []
        if p % 3 == 2:
            triples.append((p, (p + 1) // 3, p * (p + 1) // 3))
        if p % 4 == 3:
            triples.append(((p + 1) // 4, p * (p + 1) // 2, p * (p + 1) // 2))
        if p % 24 == 13:
            a = (p + 3) // 4
            triples.append((a, p * a // 2, p * a))
        for triple in triples:
            require(all(t > 0 for t in triple), "Nonpositive example")
            require(sum(Fraction(1, t) for t in triple) == Fraction(4, p),
                    f"False witness at {p}")
            count += 1
    return count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--transcript-dir", type=Path)
    args = parser.parse_args()
    descriptor = json.loads((ROOT / "workbench.json").read_text(encoding="utf-8"))
    fields = ("overview", "research_state", "attempt_overview", "human_motivations",
              "contributing", "literature", "licensing", "design")
    docs = [ROOT / "README.md"] + [local_path(descriptor[k]) for k in fields]
    for value in descriptor["records"].values():
        json.loads(local_path(value).read_text(encoding="utf-8"))
    links = 0
    for document in docs:
        text = document.read_text(encoding="utf-8")
        for match in re.finditer(r"\]\(([^)\s]+)\)", text):
            target = urlsplit(match.group(1))
            if target.scheme or not target.path:
                continue
            path = (document.parent / unquote(target.path)).resolve()
            local_path(path.relative_to(ROOT).as_posix())
            line = re.fullmatch(r"L(\d+)", target.fragment)
            if line:
                require(int(line[1]) <= len(path.read_bytes().splitlines()),
                        "Line link outside target")
            links += 1
    records = json.loads((ROOT / descriptor["records"]["human_motivations"])
                         .read_text(encoding="utf-8"))
    ids = [idea["id"] for idea in records["ideas"]]
    require(len(ids) == len(set(ids)) == 6, "Duplicate or missing idea records")
    source_ids = {s["id"] for s in records["sources"]}
    for idea in records["ideas"]:
        require(idea["source"] in source_ids, "Unknown idea source")
        require(all(idea[k] for k in ("quote", "direction", "status")),
                "Incomplete idea")
    if args.transcript_dir:
        check_transcripts(records, args.transcript_dir)
    print(json.dumps({"status": "passed", "local_links": links,
                      "human_direction_records": len(ids),
                      "raw_source_quotes_replayed": bool(args.transcript_dir),
                      "elementary_witness_checks": check_elementary_examples(),
                      "mathematical_scope": "finite examples only; no conjecture or general theorem verification"}))


if __name__ == "__main__":
    main()
