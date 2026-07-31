# Year in Review Design System

## 0. Research Log

- Existing surface: `years/2026/index.html` established the archive UI and content model before this design note existed.
- Direction: quiet academic archive with warm paper tones, teal links/actions, restrained clay accents, and document-like cards.
- Deployment target: static site suitable for `year-in-review.gkt.sh`, updated annually in summer.

## 1. Tokens

- Background: `#f6f4ef`
- Paper: `#fffdf8`
- Panel: `#ffffff`
- Ink: `#202124`
- Muted text: `#626866`
- Line: `#d8d4ca`
- Accent: `#1f6f78`
- Accent dark: `#164e55`
- Clay accent: `#8b4a2f`
- Soft surface: `#ece8df`
- Shadow: `0 18px 42px rgba(32, 33, 36, 0.08)`

## 2. Typography

- Font stack: system sans-serif.
- Hero title: responsive clamp from 42px to 84px, line-height near 1.
- Section title: 22-24px.
- Card title: 17-28px depending on hierarchy.
- Body/meta: 14-19px.

## 3. Layout

- Root content width: `min(1120px or 1180px, calc(100% - 32px))`.
- Page sections use unframed full-width bands with constrained inner content.
- Annual archive pages use filterable card grids.
- Root page uses a hero plus yearly edition cards.

## 4. Components

- Metric card: bordered panel with subtle shadow and a large numeric value.
- Work card: bordered panel with title, metadata, tags, and optional actions.
- Author line: compact muted text directly below the title; `George K. Thiruvathukal` and abbreviated variants receive the accent highlight.
- Action button/link: 44px root page, 36px archive cards; primary uses accent fill.
- Tag: small bordered status chip; green for available PDFs, amber for blocked/no-open status.
- Toolbar: sticky filter/search row on annual archive pages.

## 5. States

- Active filter buttons use accent background and white text.
- Links retain underline affordance.
- Search filters hide nonmatching work cards and empty sections.
- Responsive layout collapses grids to one column below roughly 840px.

## 6. Accessibility

- Use semantic landmarks: `header`, `nav`, `main`, `section`, `footer`.
- Buttons must be real `<button>` elements with `aria-pressed` for filters.
- Search input must have an accessible label.
- Do not rely on color alone: status tags include visible text.

## 7. Annual Update Contract

- Keep one folder per annual edition under `years/YYYY/`.
- Keep the root `index.html` pointed at the latest year.
- Preserve local PDF links relative to each year folder.
- Mark unavailable PDFs clearly and include DOI/publisher links when no local file exists.
- Keep a downloadable full BibTeX file beside each annual HTML page and link it from the root page and annual page.
- For Loyola reporting, books use an expanded scope that includes editions and reissues roughly one year before or after the main reporting window.
- Industry/professional impact items may be included in Other Scholarly Output when they have a public landing page or citable record.
