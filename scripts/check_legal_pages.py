#!/usr/bin/env python3
"""Verify legal page paths exist and include anti-index meta tags."""

from __future__ import annotations

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "legal_pages.yaml"
STATIC = ROOT / "static"
SNIPPET = ROOT / "scripts" / "legal-head-meta.snippet"
REQUIRED_MARKERS = (
    'content="noindex, nofollow, noarchive, nosnippet, noimageindex, noai, noimageai"',
    'name="GPTBot"',
    'name="ClaudeBot"',
    'name="Google-Extended"',
)


def load_paths() -> list[str]:
    paths: list[str] = []
    in_paths = False
    for line in DATA.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("paths:"):
            in_paths = True
            continue
        if in_paths:
            if stripped.startswith("- "):
                paths.append(stripped[2:].strip().strip("'\""))
                continue
            if stripped and not stripped.startswith("#"):
                break
    return paths


def path_to_file(url_path: str) -> pathlib.Path:
    rel = url_path.strip("/")
    return STATIC / rel / "index.html"


def main() -> int:
    errors: list[str] = []
    paths = load_paths()

    if not SNIPPET.exists():
        errors.append(f"Missing snippet: {SNIPPET}")

    for url_path in paths:
        html_file = path_to_file(url_path)
        if not html_file.exists():
            errors.append(f"Missing page for {url_path}: {html_file}")
            continue
        content = html_file.read_text(encoding="utf-8")
        for marker in REQUIRED_MARKERS:
            if marker not in content:
                errors.append(f"{url_path} missing meta marker: {marker}")

    if errors:
        print("Legal page check failed:\n", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print(f"OK: {len(paths)} legal pages configured and protected.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())