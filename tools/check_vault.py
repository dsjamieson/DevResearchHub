#!/usr/bin/env python3
"""Validate the research vault: frontmatter schema, result provenance, links.

Usage: python3 tools/check_vault.py [--stale DAYS]
Exits 1 if any errors are found. Warnings don't fail the check.
Standard library only (Python 3.9+).
"""
import argparse
import datetime as dt
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", ".claude", ".github", ".vscode", "templates", "node_modules"}
SKIP_FILES = {"README.md", "CLAUDE.md", "AGENTS.md"}

REQUIRED = {
    "project": ["title", "owner", "status"],
    "derivation": ["title", "owner", "status"],
    "result": ["title", "owner", "status", "code", "data"],
    "meeting": ["title", "date", "attendees"],
    "log": ["date", "owner"],
    "reference": ["title"],
}
STATUSES = {
    "project": {"active", "paused", "done"},
    "derivation": {"draft", "checked"},
    "result": {"preliminary", "validated", "superseded"},
}
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)|!\[[^\]]*\]\(([^)\s]+)\)")
WIKILINK_RE = re.compile(r"\[\[[^\]]+\]\]")
CODE_FENCE_RE = re.compile(r"```.*?```", re.S)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")


def parse_frontmatter(text):
    """Return (dict, body). Handles simple `key: value` and `key: [a, b]` lines."""
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---", 4)
    if end == -1:
        return None, text
    meta = {}
    for line in text[4:end].splitlines():
        if not line.strip() or line.lstrip().startswith("#") or line.startswith((" ", "-")):
            continue
        if ":" in line:
            k, v = line.split(":", 1)
            v = v.split(" #", 1)[0].strip().strip("'\"")
            meta[k.strip()] = v
    return meta, text[end + 4:]


def iter_notes():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for f in filenames:
            if f.endswith(".md"):
                yield os.path.join(dirpath, f)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stale", type=int, default=0,
                    help="also warn about preliminary results older than DAYS")
    args = ap.parse_args()

    errors, warnings = [], []
    for path in iter_notes():
        rel = os.path.relpath(path, ROOT)
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        meta, body = parse_frontmatter(text)
        name = os.path.basename(path)

        # Frontmatter checks
        if meta is None:
            if name not in SKIP_FILES and not rel.startswith("references" + os.sep):
                errors.append(f"{rel}: missing frontmatter (start from templates/)")
        else:
            ntype = meta.get("type", "")
            if ntype not in REQUIRED:
                errors.append(f"{rel}: unknown or missing type '{ntype}'")
            else:
                for field in REQUIRED[ntype]:
                    if not meta.get(field):
                        errors.append(f"{rel}: {ntype} is missing '{field}'")
                st = meta.get("status")
                if ntype in STATUSES and st and st not in STATUSES[ntype]:
                    errors.append(f"{rel}: status '{st}' not in {sorted(STATUSES[ntype])}")
                if ntype == "result":
                    if os.sep + "results" + os.sep not in os.sep + rel:
                        warnings.append(f"{rel}: result note outside a results/ folder")
                    if st == "superseded" and not meta.get("superseded_by"):
                        errors.append(f"{rel}: superseded result needs 'superseded_by'")
                    for ref in ("superseded_by", "supersedes"):
                        target = meta.get(ref)
                        if target and not os.path.exists(os.path.join(os.path.dirname(path), target)):
                            errors.append(f"{rel}: {ref} points to missing file '{target}'")
                    if args.stale and st == "preliminary" and meta.get("date"):
                        try:
                            age = (dt.date.today() - dt.date.fromisoformat(meta["date"])).days
                            if age > args.stale:
                                warnings.append(f"{rel}: preliminary for {age} days")
                        except ValueError:
                            pass

        # Link checks (ignore fenced code)
        scan = INLINE_CODE_RE.sub("", CODE_FENCE_RE.sub("", body))
        if WIKILINK_RE.search(scan):
            warnings.append(f"{rel}: uses [[wikilinks]]; use relative Markdown links")
        for m in LINK_RE.finditer(scan):
            target = m.group(1) or m.group(2)
            if re.match(r"^[a-z][a-z0-9+.-]*:", target) or target.startswith("#"):
                continue  # URL, mailto, or in-page anchor
            target = target.split("#", 1)[0]
            if not target:
                continue
            if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(path), target))):
                errors.append(f"{rel}: broken link -> {target}")

    for w in warnings:
        print(f"warning: {w}")
    for e in errors:
        print(f"ERROR:   {e}")
    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
