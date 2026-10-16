"""Rewrite root-relative site references as document-relative paths.

This keeps root-domain deployment working while also allowing pages to open
from disk (where /assets/... would incorrectly resolve to the drive root).
"""
from html.parser import HTMLParser
from pathlib import Path
import posixpath
import re

ROOT = Path(__file__).resolve().parent.parent
PAGES = [
    "index.html", "features.html", "agents.html", "download.html",
    "roadmap.html", "community.html", "privacy.html", "404.html",
    "docs/index.html", "blog/index.html",
]

for page in PAGES:
    file = ROOT / page
    source = file.read_text(encoding="utf-8")
    base = posixpath.dirname(page) or "."

    def rewrite(match):
        attribute, url = match.group(1), match.group(2)
        if url.startswith("//"):
            return match.group(0)
        path, marker, suffix = url.partition("#")
        path, query_marker, query = path.partition("?")
        if path == "/":
            target = "index.html"
        else:
            target = path.lstrip("/")
            if target.endswith("/"):
                target += "index.html"
        relative = posixpath.relpath(target, base)
        rewritten = relative + ("?" + query if query_marker else "") + ("#" + suffix if marker else "")
        return f'{attribute}="{rewritten}"'

    source = re.sub(r'\b(href|src)="(/[^\"]*)"', rewrite, source)
    file.write_text(source, encoding="utf-8", newline="\n")
print(f"Rewrote local-root references in {len(PAGES)} HTML pages.")
