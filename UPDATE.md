# Annual Update Workflow

Use this each summer to add a new review year.

1. Copy the prior year folder:

   ```bash
   cp -R years/2026 years/2027
   ```

2. Replace the copied archive metadata and PDFs for the new reporting window.

3. Keep the same category structure:

   - `journal/`
   - `conference/`
   - `workshop/`
   - `arxiv-preprint/`
   - `books/`
   - `other-scholarly-output/`

4. Update the new year page:

   - page title and date window
   - summary counts
   - category counts
   - DOI, arXiv, OpenReview, and publisher links
   - local PDF paths
   - expanded Loyola book scope: check publisher pages for editions and reissues roughly one year before or after the reporting window
   - industry/professional impact items with public landing pages or citable records
   - `year-in-review-YYYY.bib`

5. Update the root `index.html`:

   - hero date window
   - latest edition button
   - BibTeX download button
   - summary counts
   - annual review card list

6. Verify:

   ```bash
   python3 scripts/check-links.py
   ```

7. Open `index.html` locally and click through the latest year, search, category filters, DOI links, publisher links, and a few local PDFs.
