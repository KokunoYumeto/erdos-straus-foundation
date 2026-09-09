#!/usr/bin/env python3
"""Build exact source locators; this program does not verify mathematics.

Writing requires the published source archive with its pinned checksum.
Use --check to compare a deterministic rebuild without changing files.
Only Python's standard library is required. No mathematical checker is run.
"""

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys
import zipfile


ROOT = Path(__file__).resolve().parents[1]
SOURCE = "research/expanded-2026-09-08/exact_bounded_transport_72"
ARCHIVE_NAME = "08_Exact_Bounded_Transport_72_Source_and_Checks_2026-09-08.zip"
ARCHIVE_SHA256 = "14795049da1cc08c5e7e599f8167f63ccb833c0fbf7846318db2c693f2754b84"
ARCHIVE_PREFIX = "exact_bounded_transport_72/"
KINDS = ("theorem", "lemma", "proposition", "corollary")
ENV = re.compile(rb"\\(begin|end)\{(theorem|lemma|proposition|corollary|proof)\}")
LABEL = re.compile(rb"\\label\{([^{}]+)\}")
REF = re.compile(rb"\\(?:eqref|ref|autoref)\{([^{}]+)\}")
CLAIM_LABEL = re.compile(r"(?:thm|lem|prop|cor):.+")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def load_json(path):
    return json.loads(path.read_bytes())


def mask_comments(data):
    """Mask TeX comments with spaces while retaining all byte positions."""
    result = bytearray(data)
    for match in re.finditer(rb"%[^\r\n]*", data):
        at = match.start() - 1
        backslashes = 0
        while at >= 0 and data[at] == 92:
            at -= 1
            backslashes += 1
        if backslashes % 2 == 0:
            result[match.start():match.end()] = b" " * (match.end() - match.start())
    return bytes(result)


def span(data, start, end):
    require(0 <= start < end <= len(data), "Invalid source span")
    return {
        "byte_start": start,
        "byte_end_exclusive": end,
        "line_start": data.count(b"\n", 0, start) + 1,
        "line_end_inclusive": data.count(b"\n", 0, end - 1) + 1,
        "sha256": digest(data[start:end]),
    }


def environments(data):
    stack, records = [], []
    for match in ENV.finditer(mask_comments(data)):
        operation, kind = (x.decode("ascii") for x in match.groups())
        if operation == "begin":
            stack.append({"kind": kind, "start": match.start(), "open_end": match.end()})
        else:
            require(stack and stack[-1]["kind"] == kind, "Unbalanced indexed TeX environment")
            item = stack.pop()
            item.update(close_start=match.start(), end=match.end())
            records.append(item)
    require(not stack, "Unclosed indexed TeX environment")
    return sorted(records, key=lambda item: item["start"])


def optional_title(data, start):
    cursor = start
    while cursor < len(data) and data[cursor] in b" \r\n\t":
        cursor += 1
    if data[cursor:cursor + 1] != b"[":
        return None
    begin, depth, braces = cursor + 1, 1, 0
    cursor += 1
    while cursor < len(data):
        char = data[cursor]
        if char == 92:
            cursor += 2
            continue
        if char == 123:
            braces += 1
        elif char == 125:
            braces -= 1
        elif not braces and char == 91:
            depth += 1
        elif not braces and char == 93:
            depth -= 1
            if not depth:
                return data[begin:cursor].decode("utf-8")
        cursor += 1
    raise ValueError("Unterminated theorem title")


def source_files(root):
    directory = root / SOURCE
    require(directory.is_dir(), "Source edition directory is absent")
    paths = sorted(directory.rglob("*"))
    require(not any(path.is_symlink() for path in paths), "Source symlinks are not supported")
    return {path.relative_to(directory).as_posix(): path.read_bytes()
            for path in paths if path.is_file()}


def verify_archive(path, files):
    require(digest(path.read_bytes()) == ARCHIVE_SHA256, "Published archive checksum mismatch")
    archived = {}
    with zipfile.ZipFile(path) as archive:
        for item in archive.infolist():
            if item.is_dir():
                continue
            require(item.filename.startswith(ARCHIVE_PREFIX), "Unexpected archive root")
            name = item.filename[len(ARCHIVE_PREFIX):]
            require(name and not PurePosixPath(name).is_absolute()
                    and ".." not in PurePosixPath(name).parts, "Unsafe archive member")
            require(name not in archived, "Duplicate archive member")
            archived[name] = archive.read(item)
    require(set(archived) == set(files), "Archive and imported file sets differ")
    for name in sorted(files):
        require(files[name] == archived[name], "Imported bytes differ from archive: " + name)
    return len(archived)


def build(root=ROOT, files=None):
    files = source_files(root) if files is None else files
    provenance = json.loads(files["PROVENANCE.json"])
    pins = provenance["proof_hashes"]
    require(len(pins) == provenance["proof_count"] == 15, "Expected 15 canonical proof modules")
    require(provenance["statement_count"] == 72, "Unexpected source statement count")
    for name, expected in pins.items():
        require(name in files and digest(files[name]) == expected, "Canonical source hash mismatch: " + name)

    artifacts = {
        "schema_version": 1,
        "record_type": "source_artifact_inventory",
        "scope": "Every file imported from the published 72-statement supplement source archive.",
        "edition": provenance["edition"],
        "source_root": SOURCE,
        "source_archive": {"filename": ARCHIVE_NAME, "sha256": ARCHIVE_SHA256,
                           "member_prefix": ARCHIVE_PREFIX},
        "file_count": len(files),
        "canonical_proof_module_count": len(pins),
        "artifacts": [{"id": "es72:artifact:" + name, "path": SOURCE + "/" + name,
                       "archive_member": ARCHIVE_PREFIX + name,
                       "bytes": len(data), "sha256": digest(data),
                       "canonical_proof_module": name in pins}
                      for name, data in sorted(files.items())],
    }

    claims, label_locations = [], {}
    for name in pins:
        data = files[name]
        clean = mask_comments(data)
        for match in LABEL.finditer(clean):
            label = match[1].decode("utf-8")
            require(label not in label_locations, "Duplicate TeX label: " + label)
            label_locations[label] = {"path": SOURCE + "/" + name,
                                      "span": span(data, match.start(), match.end())}
        envs = environments(data)
        statements = [item for item in envs if item["kind"] in KINDS]
        proofs = [item for item in envs if item["kind"] == "proof"]
        used_proofs = set()
        for number, item in enumerate(statements, 1):
            next_start = statements[number]["start"] if number < len(statements) else len(data)
            nested = [proof for proof in proofs if item["start"] < proof["start"] < item["end"]]
            following = [proof for proof in proofs if item["end"] <= proof["start"] < next_start]
            require(len(nested) <= 1 and len(following) <= 1, "Ambiguous proof association: " + name)
            attached = nested or following
            statement_end = nested[0]["start"] if nested else item["end"]
            statement_data = data[item["start"]:statement_end]
            statement_labels = [match[1].decode("utf-8") for match in LABEL.finditer(mask_comments(statement_data))]
            theorem_labels = [label for label in statement_labels if CLAIM_LABEL.fullmatch(label)]
            require(len(theorem_labels) == 1, "Expected one theorem label per statement: " + name)
            label = theorem_labels[0]
            refs = list(dict.fromkeys(match[1].decode("utf-8") for match in REF.finditer(mask_comments(statement_data))))
            claim = {
                "id": "es72:claim:" + label,
                "environment": item["kind"],
                "theorem_label": label,
                "title_tex": optional_title(data, item["open_end"]),
                "ordinal_in_source": number,
                "source": {"artifact_id": "es72:artifact:" + name,
                           "path": SOURCE + "/" + name, "sha256": digest(data)},
                "enclosing_environment_span": span(data, item["start"], item["end"]),
                "statement_span": span(data, item["start"], statement_end),
                "statement_tex": statement_data.decode("utf-8"),
                "statement_labels": statement_labels,
                "statement_referenced_labels": refs,
                "status": "published_source_statement; no new mathematical verification asserted",
            }
            if attached:
                proof = attached[0]
                require(proof["start"] not in used_proofs, "Proof reused by distinct statements")
                used_proofs.add(proof["start"])
                claim["proof"] = {"kind": "explicit_environment",
                                  "placement": "nested" if nested else "following",
                                  "span": span(data, proof["start"], proof["end"])}
            else:
                require(label == "cor:global-r3-r7", "Unrecorded implicit proof: " + label)
                require(refs == ["thm:r3-factor-sieve", "thm:r7-factor-sieve"], "Implicit theorem references changed")
                claim["proof"] = {
                    "kind": "theorem_references_in_statement",
                    "note": "The source supplies theorem references within the corollary and no separate proof environment.",
                    "claim_ids": ["es72:claim:" + ref for ref in refs],
                    "reference_spans": [span(data, match.start(), match.end())
                                        for match in REF.finditer(clean, item["start"], statement_end)],
                }
            claims.append(claim)
        require(used_proofs == {proof["start"] for proof in proofs}, "Unassigned proof environment: " + name)

    require(len(claims) == 72, "Expected exactly 72 statements")
    ids = [claim["id"] for claim in claims]
    require(len(set(ids)) == len(ids), "Duplicate claim identifier")
    # Verify every literal cross-reference in all 15 modules, not only theorem titles.
    for name in pins:
        for match in REF.finditer(mask_comments(files[name])):
            require(match[1].decode("utf-8") in label_locations, "Unresolved canonical TeX reference: " + match[1].decode("utf-8"))
    for claim in claims:
        for target in claim["proof"].get("claim_ids", []):
            require(target in ids, "Unresolved proof claim reference: " + target)
    claims_document = {
        "schema_version": 1,
        "record_type": "exact_published_source_statement_index",
        "edition": provenance["edition"],
        "source_root": SOURCE,
        "canonical_modules": [SOURCE + "/" + name for name in pins],
        "statement_count": len(claims),
        "proof_environment_count": sum(claim["proof"]["kind"] == "explicit_environment" for claim in claims),
        "span_convention": "Zero-based UTF-8 byte offsets [byte_start, byte_end_exclusive); one-based inclusive line numbers; LF bytes delimit lines. Span SHA-256 hashes exact source bytes.",
        "statement_convention": "Exact bytes from the theorem environment opening through its closing token; when a proof is nested, the statement ends immediately before that proof opening. The enclosing environment span retains the whole original environment.",
        "scope": "The 15 PROVENANCE.json proof_hashes modules only. Editorial publication copies are inventoried as artifacts and are not counted again. Locators do not replace the complete source definitions, hypotheses, surrounding calculations or proofs.",
        "verification_scope": "File identity, deterministic extraction and reference consistency only; no new proof review, mathematical replay or Lean verification is asserted.",
        "claims": claims,
        "label_locations": dict(sorted(label_locations.items())),
    }
    return artifacts, claims_document


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, help="Published source ZIP, required when writing")
    parser.add_argument("--check", action="store_true", help="Compare existing indexes without writing")
    args = parser.parse_args()
    files = source_files(ROOT)
    if args.archive:
        verify_archive(args.archive, files)
    require(args.check or args.archive, "Writing requires --archive with the pinned published ZIP")
    artifacts, claims = build(ROOT, files)
    for name, document in (("artifacts.json", artifacts), ("claims.json", claims)):
        target = ROOT / "polyclank" / name
        expected = json_bytes(document)
        if args.check:
            require(target.read_bytes() == expected, "Index differs from deterministic rebuild: " + name)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(expected)
    print(json.dumps({"result": "passed", "mode": "check" if args.check else "build",
                      "archive_compared": bool(args.archive), "files": len(files),
                      "canonical_modules": 15, "statements": len(claims["claims"]),
                      "verification_scope": "source identity and locators only"}))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, KeyError, zipfile.BadZipFile) as error:
        print("Index build failed: " + str(error), file=sys.stderr)
        sys.exit(1)
