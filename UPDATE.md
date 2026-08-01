# Year-in-Review Archive Runbook

This repository is a static archive for annual research, scholarly, creative,
teaching, software/application, and professional-impact work.

The current public site is driven by:

- `index.html`: root landing page and latest-year summary.
- `years/YYYY/index.html`: interactive annual archive page.
- `years/YYYY/README.md`: plain-text manifest for the annual archive.
- `years/YYYY/year-in-review-YYYY.bib`: BibTeX export.
- `years/YYYY/<category>/...`: local PDFs, snapshots, or `NOTE.txt` files.
- `DESIGN.md`: visual and content contract for the static pages.

## Current Year Structure

Each annual folder should use the same top-level categories when applicable:

- `journal/`
- `conference/`
- `workshop/`
- `arxiv-preprint/`
- `books/`
- `other-scholarly-output/`
- `teaching-work/`
- `software-applications/`

Folder naming rules:

- DOI folders replace `/` with `_`, for example `10.1145_3786165.3788438`.
- arXiv folders use `arxiv_<id>`.
- OpenReview folders use a stable venue/title/id slug.
- Books use ISBN folders when possible.
- Teaching and software/application entries use site-based folders.

For each item, record four things in the annual README:

- Work title.
- Date used for the reporting decision.
- DOI, arXiv, ISBN, URL, or other durable identifier.
- Local status: downloaded PDF, snapshot, folder-only, embargoed, blocked, or note.

## Sources to Check

Start from Google Scholar, but do not stop there. Cross-check:

- Google Scholar profile.
- ORCID.
- Crossref and DOI landing pages.
- arXiv.
- OpenReview.
- Loyola eCommons.
- Figshare.
- ACM Digital Library for ACM DOI items.
- IEEE Xplore for IEEE DOI items.
- Publisher pages for books and paywalled papers.
- Public teaching sites.
- Public software/application sites and source repositories.
- Professional impact pages, such as IEEE Future Directions reports.

When a publication is ACM or IEEE, include a visible button on the HTML card for
the appropriate digital library, even when a local author/preprint PDF is also
available.

## Books

Use `Books (All Time)` for authored or edited books, but split the visible
section into:

- `2025-2026 Books` or the equivalent current reporting-window label.
- `Earlier Books`.

Do not add catalog-only books unless they are confirmed real authored or edited
works. If a book has no open version, keep an ISBN folder with a `NOTE.txt`
describing the publisher record and why no PDF is present.

## Backfilling the Previous 1-2 Years

For the previous one or two reporting years, create real annual folders instead
of mixing older work into the current year.

Use academic reporting windows:

- 2025 archive: July 1, 2024 through June 30, 2025.
- 2024 archive: July 1, 2023 through June 30, 2024.

Recommended process:

1. Copy the latest complete year as a scaffold:

   ```bash
   cp -R years/2026 years/2025
   ```

2. Rename the BibTeX file:

   ```bash
   mv years/2025/year-in-review-2026.bib years/2025/year-in-review-2025.bib
   ```

3. Clear year-specific content from the copied folder before refilling it:

   - Remove copied PDFs and snapshots that do not belong to the older window.
   - Keep the category directory shape.
   - Keep HTML/CSS structure and profile links.
   - Replace counts, titles, and date windows.

4. Gather the older-year works from the same sources listed above.

5. Apply the same inclusion rules:

   - Publications must have an in-window publication, online-first, conference,
     preprint, or durable release date.
   - Books remain `Books (All Time)`, but the current-window subsection should
     match the year being backfilled.
   - Teaching/software/application items should have a public page or durable
     source record. If the site predates the window but is important context,
     mark the date honestly and explain it.
   - Industry/professional items need a public landing page or citable record.

6. Update the root `index.html` to list older annual review cards after the
   latest year. Keep the latest-year hero pointed at the newest archive.

7. Verify links and counts before committing.

Backfill quality bar: it is better to have a smaller, well-sourced prior-year
archive than a large one with uncertain dates or guessed metadata.

## Next-Year Workflow

Use this each summer to add the next review year.

1. Copy the prior year folder:

   ```bash
   cp -R years/2026 years/2027
   mv years/2027/year-in-review-2026.bib years/2027/year-in-review-2027.bib
   ```

2. Set the reporting window:

   - 2027 archive: July 1, 2026 through June 30, 2027.

3. Refresh all annual metadata:

   - Page title and heading.
   - Summary counts.
   - Category counts.
   - README title and tables.
   - BibTeX entries.
   - Local folders and filenames.
   - Root `index.html` latest-year card and summary.

4. Rebuild the work list:

   - Start with Google Scholar.
   - Cross-check ORCID, Crossref, arXiv, OpenReview, eCommons, Figshare,
     publisher pages, ACM, IEEE, teaching sites, software apps, and GitHub.
   - Download open PDFs where allowed.
   - Save landing-page snapshots for teaching and software/application entries.
   - Add `NOTE.txt` files for blocked, embargoed, paywalled, or no-open-version
     records.

5. Keep profile links at the top of every public page:

   - Professional website.
   - Loyola profile.
   - Argonne profile.
   - LinkedIn.
   - Google Scholar.
   - GitHub.

6. Verify:

   ```bash
   python3 scripts/check-links.py
   python3 -m http.server 8765 --bind 127.0.0.1
   ```

7. Open the local page and check:

   - Header profile links.
   - Search.
   - Category filters.
   - Summary counts.
   - Local PDF links.
   - DOI/publisher links.
   - ACM/IEEE digital library buttons.
   - Teaching and software/application snapshots.

8. Commit and push only after the local archive passes verification.

## Verification Notes

The current project is static HTML, so the core verification is:

- Parse HTML successfully.
- Check local links.
- Count `article[data-category]` cards and compare to visible metrics.
- Count local PDFs and compare to visible metrics.
- Serve locally and smoke-test the current year page.

If `biome` or `texlab` are not installed, LSP diagnostics may not run. Do not
install global tools silently; either install them intentionally or document that
the static verifier was used instead.
