"""Dependency-free integrity check for the static site."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent.parent
PAGES = [
    "index.html", "features.html", "agents.html", "download.html",
    "roadmap.html", "community.html", "privacy.html", "404.html",
    "docs/index.html", "blog/index.html",
]


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.urls = []
        self.title = ""
        self.in_title = False
        self.meta = {}
        self.canonical = None
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
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical = attrs.get("href")
        if tag == "main" and attrs.get("id") == "main":
            self.main_id = True
        if tag == "img":
            if "alt" not in attrs:
                self.images_without_alt += 1
            if attrs.get("src"):
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


errors = []
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
    if not parser.canonical or not parser.canonical.startswith("https://lazycodingagent.com/"):
        errors.append(f"{page}: missing canonical URL")
    elif parser.canonical in canonicals:
        errors.append(f"{page}: duplicate canonical URL")
    canonicals.add(parser.canonical)
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

css = (ROOT / "assets/site.css").read_text(encoding="utf-8")
if "prefers-reduced-motion" not in css:
    errors.append("Stylesheet lacks reduced-motion handling")
if "focus-visible" not in css:
    errors.append("Stylesheet lacks visible focus styling")
if errors:
    print("Site checks failed:")
    print("\n".join(f"- {error}" for error in errors))
    raise SystemExit(1)
print(f"Passed local-link, metadata, landmark, and CSS checks for {len(PAGES)} HTML pages.")
