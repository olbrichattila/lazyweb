"""Dependency-free integrity check for the static site and release fallbacks."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import xml.etree.ElementTree as ET
import re

ROOT = Path(__file__).resolve().parent.parent
PAGES = [
    "index.html", "features.html", "agents.html", "download.html",
    "roadmap.html", "community.html", "privacy.html", "404.html",
    "docs/index.html",
    "docs/getting-started.html",
    "docs/workspace-layout.html",
    "docs/chat-and-modes.html",
    "docs/project-rules.html",
    "docs/how-the-agent-works.html",
    "docs/tools-reference.html",
    "blog/index.html",
]
CANONICAL_ORIGIN = "https://lazycodingagent.com"
EXPECTED_CANONICALS = {
    "index.html": "https://lazycodingagent.com/",
    "features.html": "https://lazycodingagent.com/features.html",
    "agents.html": "https://lazycodingagent.com/agents.html",
    "download.html": "https://lazycodingagent.com/download.html",
    "roadmap.html": "https://lazycodingagent.com/roadmap.html",
    "community.html": "https://lazycodingagent.com/community.html",
    "privacy.html": "https://lazycodingagent.com/privacy.html",
    "404.html": "https://lazycodingagent.com/404.html",
    "docs/index.html": "https://lazycodingagent.com/docs/",
    "docs/getting-started.html": "https://lazycodingagent.com/docs/getting-started.html",
    "docs/workspace-layout.html": "https://lazycodingagent.com/docs/workspace-layout.html",
    "docs/chat-and-modes.html": "https://lazycodingagent.com/docs/chat-and-modes.html",
    "docs/project-rules.html": "https://lazycodingagent.com/docs/project-rules.html",
    "docs/how-the-agent-works.html": "https://lazycodingagent.com/docs/how-the-agent-works.html",
    "docs/tools-reference.html": "https://lazycodingagent.com/docs/tools-reference.html",
    "blog/index.html": "https://lazycodingagent.com/blog/",
}
INDEXABLE_PAGES = [page for page in PAGES if page != "404.html"]
ARTIFACTS = {
    "windows": "win64-Setup.exe",
    "mac-intel": "x86_64.dmg",
    "mac-arm": "aarch64.dmg",
    "linux-amd64": "amd64.deb",
    "linux-appimage": "x86_64.AppImage",
    "linux-arm64": "arm64.deb",
}


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.urls = []
        self.scripts = []
        self.title = ""
        self.in_title = False
        self.meta = {}
        self.og_urls = []
        self.canonicals = []
        self.h1_count = 0
        self.skip_link = False
        self.main_id = False
        self.images_without_alt = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "title":
            self.in_title = True
        if tag == "h1":
            self.h1_count += 1
        if tag == "meta" and attrs.get("name"):
            self.meta[attrs["name"]] = attrs.get("content", "")
        if tag == "meta" and attrs.get("property", "").casefold() == "og:url":
            self.og_urls.append(attrs.get("content"))
        if tag == "link" and "canonical" in attrs.get("rel", "").casefold().split():
            href = attrs.get("href")
            self.canonicals.append(href)
        if tag == "main" and attrs.get("id") == "main":
            self.main_id = True
        if tag == "img":
            if "alt" not in attrs:
                self.images_without_alt += 1
            if attrs.get("src"):
                self.urls.append(attrs["src"])
        if tag == "script" and attrs.get("src"):
            self.scripts.append(attrs["src"])
            self.urls.append(attrs["src"])
        if tag in ("a", "link") and attrs.get("href"):
            href = attrs["href"]
            self.urls.append(href)
            if tag == "a" and attrs.get("class") == "skip-link" and href.endswith("#main"):
                self.skip_link = True

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data


class ReleaseParser(HTMLParser):
    """Collect explicit release selectors and checksum row content."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.versions = []
        self.links = {}
        self.checksums = {}
        self.scripts = []
        self.release_pages = []
        self.checksum_heading = ""
        self.in_checksum_heading = False
        self.current_row = None
        self.current_code = None
        self.in_version_label = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "strong" and "data-release-version" in attrs:
            self.versions.append({"text": "", "tag": tag})
            self.in_version_label = True
        if tag == "meta" and "data-release-version" in attrs:
            self.versions.append({"text": attrs.get("content", ""), "tag": tag})
        if tag == "script" and attrs.get("src"):
            self.scripts.append(attrs["src"])
        if tag == "a" and "data-release-page" in attrs:
            self.release_pages.append(attrs.get("href", ""))
        if tag == "h2" and "data-checksum-version" in attrs:
            self.in_checksum_heading = True
        if tag == "a" and attrs.get("data-release-asset"):
            self.links.setdefault(attrs["data-release-asset"], []).append(attrs.get("href", ""))
        if tag == "li" and attrs.get("data-checksum"):
            self.current_row = {"id": attrs["data-checksum"], "codes": []}
        if tag == "code" and self.current_row is not None:
            self.current_code = ""

    def handle_data(self, data):
        if self.current_code is not None:
            self.current_code += data
        elif self.in_version_label:
            self.versions[-1]["text"] += data
        elif self.in_checksum_heading:
            self.checksum_heading += data

    def handle_endtag(self, tag):
        if tag == "strong":
            self.in_version_label = False
        if tag == "h2":
            self.in_checksum_heading = False
        if tag == "code" and self.current_code is not None and self.current_row is not None:
            self.current_row["codes"].append(self.current_code.strip())
            self.current_code = None
        if tag == "li" and self.current_row is not None:
            self.checksums[self.current_row["id"]] = self.current_row["codes"]
            self.current_row = None


def check_release_fallback(errors):
    page = ROOT / "download.html"
    source = page.read_text(encoding="utf-8")
    parser = ReleaseParser()
    parser.feed(source)
    visible_versions = [item["text"].strip() for item in parser.versions if item["tag"] == "strong"]
    if len(visible_versions) != 1 or not re.fullmatch(r"\d+\.\d+\.\d+", visible_versions[0]):
        errors.append("download.html: expected one explicit numeric fallback release version")
        return
    version = visible_versions[0]
    expected_ids = set(ARTIFACTS)
    if f"SHA-256 checksums ({version})" not in parser.checksum_heading:
        errors.append("download.html: checksum heading does not match fallback version")
    if len(parser.release_pages) != 1 or f"/releases/tag/v{version}" not in parser.release_pages[0]:
        errors.append("download.html: release-page link does not match fallback version")
    if not parser.scripts or "assets/latest-release.js" not in parser.scripts:
        errors.append("download.html: missing local latest-release script reference")
    if set(parser.links) != expected_ids:
        errors.append("download.html: explicit asset links do not match the six supported artifact IDs")
    if set(parser.checksums) != expected_ids:
        errors.append("download.html: expected one checksum row for each supported artifact")

    for artifact_id, suffix in ARTIFACTS.items():
        links = parser.links.get(artifact_id, [])
        if len(links) != 1:
            errors.append(f"download.html: expected one fallback link for {artifact_id}")
        elif f"/releases/download/v{version}/LazyCodingAgent-{version}-{suffix}" not in links[0]:
            errors.append(f"download.html: {artifact_id} fallback URL/version/name mismatch")
        rows = parser.checksums.get(artifact_id, [])
        if len(rows) != 2:
            errors.append(f"download.html: {artifact_id} checksum row must contain filename and digest")
            continue
        if rows[0] != f"LazyCodingAgent-{version}-{suffix}":
            errors.append(f"download.html: {artifact_id} checksum filename/version mismatch")
        if not re.fullmatch(r"[a-fA-F0-9]{64}", rows[1]):
            errors.append(f"download.html: {artifact_id} fallback digest is not a SHA-256 hex value")

    required_fallback_markers = (
        "data-release-page", "data-checksum-version", "data-release-status",
        "data-asset-status=", "data-checksum-status",
    )
    for marker in required_fallback_markers:
        if marker not in source:
            errors.append(f"download.html: missing release fallback/status structure {marker}")
    if "api.github.com" not in (ROOT / "privacy.html").read_text(encoding="utf-8") and "latest-release API" not in (ROOT / "privacy.html").read_text(encoding="utf-8"):
        errors.append("privacy.html: does not describe the authored GitHub release API request")


errors = []
if set(PAGES) != set(EXPECTED_CANONICALS):
    missing = sorted(set(PAGES) - set(EXPECTED_CANONICALS))
    extra = sorted(set(EXPECTED_CANONICALS) - set(PAGES))
    errors.append(f"Canonical expectation map does not match PAGES (missing={missing}, extra={extra})")
if "404.html" in INDEXABLE_PAGES:
    errors.append("404.html must remain excluded from sitemap indexable pages")

titles = set()
canonicals = set()
for page in PAGES:
    file = ROOT / page
    if not file.is_file():
        errors.append(f"Missing page: {page}")
        continue
    parser = PageParser()
    parser.feed(file.read_text(encoding="utf-8"))
    if not parser.title.strip():
        errors.append(f"{page}: missing title")
    elif parser.title in titles:
        errors.append(f"{page}: duplicate title")
    titles.add(parser.title)
    if not parser.meta.get("description"):
        errors.append(f"{page}: missing meta description")
    expected_canonical = EXPECTED_CANONICALS.get(page)
    if len(parser.canonicals) != 1:
        errors.append(f"{page}: expected exactly one canonical link, found {len(parser.canonicals)}")
    if len(parser.canonicals) == 1:
        canonical = parser.canonicals[0]
        if not canonical:
            errors.append(f"{page}: canonical link is missing href")
        else:
            parsed_canonical = urlsplit(canonical)
            if (parsed_canonical.scheme != "https"
                    or parsed_canonical.netloc != urlsplit(CANONICAL_ORIGIN).netloc
                    or parsed_canonical.query
                    or parsed_canonical.fragment):
                errors.append(f"{page}: canonical must be an absolute HTTPS URL on lazycodingagent.com without query or fragment")
            if expected_canonical is None or canonical != expected_canonical:
                errors.append(f"{page}: canonical URL {canonical!r} does not match expected {expected_canonical!r}")
            if canonical in canonicals:
                errors.append(f"{page}: duplicate canonical URL")
            canonicals.add(canonical)

    if len(parser.og_urls) != 1:
        errors.append(f"{page}: expected exactly one og:url value, found {len(parser.og_urls)}")
    elif parser.og_urls[0] != expected_canonical:
        errors.append(f"{page}: og:url {parser.og_urls[0]!r} does not match expected canonical {expected_canonical!r}")
    if not parser.main_id:
        errors.append(f"{page}: missing main landmark with id=main")
    if not parser.skip_link:
        errors.append(f"{page}: missing skip link")
    if parser.images_without_alt:
        errors.append(f"{page}: {parser.images_without_alt} image(s) missing alt attribute")
    if parser.h1_count != 1:
        errors.append(f"{page}: expected one h1, found {parser.h1_count}")

    for url in parser.urls:
        parsed = urlsplit(url)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        if parsed.path.startswith("/"):
            target = ROOT / parsed.path.lstrip("/")
        else:
            target = (file.parent / parsed.path).resolve()
        if target.is_dir():
            target /= "index.html"
        if not target.exists():
            errors.append(f"{page}: broken local URL {url}")

check_release_fallback(errors)
sitemap_path = ROOT / "sitemap.xml"
try:
    sitemap_root = ET.parse(sitemap_path).getroot()
except (ET.ParseError, OSError) as exc:
    errors.append(f"sitemap.xml: could not parse sitemap ({exc})")
else:
    namespace = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
    sitemap_locs = [loc.text.strip() if loc.text else "" for loc in sitemap_root.findall(f".//{namespace}loc")]
    if not sitemap_locs:
        errors.append("sitemap.xml: no <loc> entries found")
    seen_locs = set()
    expected_indexable_locs = {EXPECTED_CANONICALS[page] for page in INDEXABLE_PAGES if page in EXPECTED_CANONICALS}
    for location in sitemap_locs:
        parsed_location = urlsplit(location)
        if (parsed_location.scheme != "https"
                or parsed_location.netloc != urlsplit(CANONICAL_ORIGIN).netloc
                or parsed_location.query
                or parsed_location.fragment):
            errors.append(f"sitemap.xml: <loc> must be an absolute HTTPS URL on lazycodingagent.com without query or fragment: {location!r}")
        if location in seen_locs:
            errors.append(f"sitemap.xml: duplicate <loc> {location!r}")
        seen_locs.add(location)
        if location not in expected_indexable_locs:
            errors.append(f"sitemap.xml: <loc> {location!r} is not an intended indexable page canonical")

    for missing_location in sorted(expected_indexable_locs - seen_locs):
        errors.append(f"sitemap.xml: missing indexable page canonical {missing_location!r}")

css = (ROOT / "assets/site.css").read_text(encoding="utf-8")
if "prefers-reduced-motion" not in css:
    errors.append("Stylesheet lacks reduced-motion handling")
if "focus-visible" not in css:
    errors.append("Stylesheet lacks visible focus styling")
if errors:
    print("Site checks failed:")
    print("\n".join(f"- {error}" for error in errors))
    raise SystemExit(1)
print(f"Passed local-link, metadata, landmark, CSS, and release-fallback checks for {len(PAGES)} HTML pages.")
