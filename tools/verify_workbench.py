#!/usr/bin/env python3
"""Verify published file identity and exact statement/proof locators, not mathematics.

Default: python tools/verify_workbench.py
Optional archive comparison: add --archive PATH
Negative tests: add --self-test (all mutations stay in memory).
"""

import argparse
import copy
import json
from pathlib import Path, PurePosixPath
import sys

from build_workbench_index import (
    ROOT, SOURCE, build, digest, json_bytes, load_json, require,
    source_files, verify_archive,
)


def verify_span(data, record):
    start, end = record["byte_start"], record["byte_end_exclusive"]
    require(type(start) is int and type(end) is int and 0 <= start < end <= len(data), "Invalid byte locator")
    require(record["line_start"] == data[:start].count(b"\n") + 1, "Incorrect start line")
    require(record["line_end_inclusive"] == data[:end - 1].count(b"\n") + 1, "Incorrect end line")
    require(record["sha256"] == digest(data[start:end]), "Incorrect span checksum")
    return data[start:end]


def verify(artifacts, claims, files):
    require(artifacts["schema_version"] == claims["schema_version"] == 1, "Unsupported index schema")
    require(artifacts["source_root"] == claims["source_root"] == SOURCE, "Source root differs")
    by_artifact = {}
    paths = set()
    for item in artifacts["artifacts"]:
        require(item["id"] not in by_artifact, "Duplicate artifact identifier")
        path = item["path"]
        require(path.startswith(SOURCE + "/") and ".." not in PurePosixPath(path).parts, "Invalid artifact path")
        require(path not in paths, "Duplicate artifact path")
        paths.add(path)
        name = path[len(SOURCE) + 1:]
        require(name in files, "Missing imported file: " + name)
        data = files[name]
        require(item["bytes"] == len(data) and item["sha256"] == digest(data), "Artifact identity differs: " + name)
        by_artifact[item["id"]] = item
    require(paths == {SOURCE + "/" + name for name in files}, "Inventory does not exactly cover source files")
    require(artifacts["file_count"] == len(files), "Incorrect inventory file count")
    by_claim, theorem_labels, locations = {}, set(), set()
    for claim in claims["claims"]:
        require(claim["id"] not in by_claim, "Duplicate statement identifier")
        require(claim["theorem_label"] not in theorem_labels, "Duplicate theorem label")
        theorem_labels.add(claim["theorem_label"])
        by_claim[claim["id"]] = claim
        source = claim["source"]
        require(source["artifact_id"] in by_artifact, "Unknown source artifact")
        artifact = by_artifact[source["artifact_id"]]
        require(source["path"] == artifact["path"] and source["sha256"] == artifact["sha256"], "Source reference differs")
        require(artifact["canonical_proof_module"], "Statement comes from an editorial copy")
        data = files[source["path"][len(SOURCE) + 1:]]
        exact = verify_span(data, claim["statement_span"])
        require(exact == claim["statement_tex"].encode("utf-8"), "Statement TeX differs from source bytes")
        verify_span(data, claim["enclosing_environment_span"])
        address = (source["path"], claim["statement_span"]["byte_start"])
        require(address not in locations, "Duplicate statement location")
        locations.add(address)
        proof = claim["proof"]
        if proof["kind"] == "explicit_environment":
            proof_bytes = verify_span(data, proof["span"])
            require(proof_bytes.startswith(b"\\begin{proof}") and proof_bytes.endswith(b"\\end{proof}"), "Invalid proof boundary")
        elif proof["kind"] == "theorem_references_in_statement":
            for reference in proof["reference_spans"]:
                verify_span(data, reference)
        else:
            raise ValueError("Unknown proof locator kind")
    require(len(by_claim) == claims["statement_count"] == 72, "Incorrect statement count")
    for claim in claims["claims"]:
        for target in claim["proof"].get("claim_ids", []):
            require(target in by_claim, "Unknown referenced theorem")
        for label in claim["statement_referenced_labels"]:
            require(label in claims["label_locations"], "Unknown referenced TeX label")
    for label, location in claims["label_locations"].items():
        require(location["path"] in paths, "Unknown label source")
        data = files[location["path"][len(SOURCE) + 1:]]
        require(verify_span(data, location["span"]) == ("\\label{" + label + "}").encode("utf-8"), "Label locator differs")
    # Full extraction detects omitted/reordered statements, stale metadata and
    # changes to every cross-reference in all canonical modules.
    expected_artifacts, expected_claims = build(files=files)
    require(artifacts == expected_artifacts, "Artifact inventory is not the canonical rebuild")
    require(claims == expected_claims, "Statement inventory is not the canonical rebuild")


def self_test(artifacts, claims, files):
    """Exercise real failure paths without editing source or repository files."""
    cases = []
    altered_files = dict(files)
    name = "bounded_transport.tex"
    altered_files[name] = b"!" + altered_files[name][1:]
    cases.append(("source_byte_tamper", artifacts, claims, altered_files))
    changed = copy.deepcopy(claims)
    changed["claims"][0]["statement_tex"] += " "
    cases.append(("statement_text_tamper", artifacts, changed, files))
    changed = copy.deepcopy(claims)
    changed["claims"][0]["statement_span"]["byte_start"] += 1
    cases.append(("byte_locator_tamper", artifacts, changed, files))
    changed = copy.deepcopy(claims)
    changed["claims"][1]["id"] = changed["claims"][0]["id"]
    cases.append(("duplicate_claim_identifier", artifacts, changed, files))
    changed = copy.deepcopy(claims)
    implicit = next(claim for claim in changed["claims"] if claim["proof"]["kind"] == "theorem_references_in_statement")
    implicit["proof"]["claim_ids"][0] = "es72:claim:thm:absent"
    cases.append(("dangling_proof_reference", artifacts, changed, files))
    passed = []
    for name, inventory, statements, source in cases:
        try:
            verify(inventory, statements, source)
        except ValueError:
            passed.append(name)
        else:
            raise ValueError("Negative test incorrectly accepted: " + name)
    return passed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, help="Also compare all imported bytes with the pinned published ZIP")
    parser.add_argument("--self-test", action="store_true", help="Run five in-memory tamper tests")
    args = parser.parse_args()
    artifacts = load_json(ROOT / "polyclank/artifacts.json")
    claims = load_json(ROOT / "polyclank/claims.json")
    files = source_files(ROOT)
    verify(artifacts, claims, files)
    for name, value in (("artifacts.json", artifacts), ("claims.json", claims)):
        require((ROOT / "polyclank" / name).read_bytes() == json_bytes(value), "Noncanonical JSON serialization: " + name)
    if args.archive:
        verify_archive(args.archive, files)
    tests = self_test(artifacts, claims, files) if args.self_test else []
    print(json.dumps({"result": "passed", "files": len(files), "canonical_modules": 15,
                      "statements": len(claims["claims"]), "explicit_proofs": claims["proof_environment_count"],
                      "implicit_theorem_reference_records": 1, "archive_compared": bool(args.archive),
                      "negative_tests_rejected": tests,
                      "verification_scope": "source identity, locators and references only; no mathematical replay"}))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, KeyError) as error:
        print("Workbench verification failed: " + str(error), file=sys.stderr)
        sys.exit(1)
