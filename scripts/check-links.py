# /// script
# requires-python = ">=3.12"
# ///
#
# --- How to run ---
# python3 scripts/check-links.py

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.hrefs: list[tuple[Path, str]] = []
        self.current_file = Path()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        values = dict(attrs)
        href = values.get("href")
        if href:
            self.hrefs.append((self.current_file, href))


def check_file(path: Path) -> list[str]:
    parser = LinkParser()
    parser.current_file = path
    parser.feed(path.read_text(encoding="utf-8"))

    missing: list[str] = []
    for source, href in parser.hrefs:
        if href.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = (source.parent / href).resolve()
        if not target.exists():
            missing.append(f"{source}: {href}")
    return missing


def main() -> int:
    root = Path.cwd()
    missing: list[str] = []
    site_pages = [root / "index.html", *sorted((root / "years").glob("*/index.html"))]
    for html_file in site_pages:
        missing.extend(check_file(html_file))

    if missing:
        print("Missing local links:")
        for item in missing:
            print(f"- {item}")
        return 1

    print("All local HTML links resolve.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
