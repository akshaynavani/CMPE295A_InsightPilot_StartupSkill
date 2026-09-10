# CMPE 295A — Assignments

Course deliverables for CMPE 295A. Kept outside `runs/insightpilot/` so the
project pack's coverage audit does not count them as pack artifacts.

| # | Assignment | File | Status |
|---|---|---|---|
| 1 | Project Abstract | [`.docx`](CMPE295A_InsightPilot_Project_Abstract.docx) · [`.pdf`](CMPE295A_InsightPilot_Project_Abstract.pdf) | **Final** — 2 pages confirmed |

## Assignment 1 — Project Abstract

Two pages, per the assignment specification:

1. **Title page** — project title, four team members with SJSU addresses,
   project advisor, submission month and year.
2. **Abstract page** — title repeated, team members, three double-spaced
   paragraphs.

**Paragraph structure follows the rubric strictly:**

- **Paragraph 1** sets the domain — enterprise analysts answering
  unanticipated questions, and the BI automation vendors now ship.
- **Paragraph 2** describes the problem **and contains no solution.** The
  1-point rubric row names "a solution is discussed in paragraph 2" as the
  specific failure mode, so this paragraph ends on a statement of need,
  mirroring the example abstract's own construction.
- **Paragraph 3** describes the approach and closes on an outcome, opening
  with "In this project, we build…" to match the example's proposal framing
  and avoid asserting a capability that does not yet exist.

**Both statistics are real and attributable**, traced through
`runs/insightpilot/research/sources.md`:

- 81.2 percent of failures, from Omni Analytics' 2026 analysis of 4,602
  faulty text-to-SQL queries.
- 71 percent, from the dbt Labs 2026 State of Analytics Engineering survey,
  which discloses its sample of 363 practitioners.

Attribution is named in the prose without citation markers, matching the
example abstract's handling of its own 85.57 percent figure.

**Readability:** 265 words of body text. Longest sentence 27 words.
Paragraphs run 59 / 104 / 103 words across 3 / 6 / 6 sentences.

## Document hygiene

The original draft was built by editing the instructor's template XML in
place. The current file was rebuilt in Google Docs, which reintroduced two
issues from the template that were then cleared again:

- **Author metadata.** The template carried `harkey` as `dc:creator` with a
  2015 creation date. Both are now the team's own. Note that Word's *Remove
  Person* strips the author but **never** the creation date — that required
  a direct XML edit.
- **Embedded fonts.** A Word save switched on *Embed fonts in the file*,
  adding six `.odttf` parts and inflating the document from 11 KB to
  **2.4 MB**. The fonts, their relationships, the content-type entry and the
  `<w:embedTrueTypeFonts/>` flag were all removed, bringing it to ~17 KB.
  Clearing the flag is what stops Word re-embedding on the next save.

**If the document is ever re-exported from Google Docs, both issues return.**
Do metadata cleanup last.

## Known cosmetic item, not fixed

Paragraph 1 writes **"Business Intelligence automation"** while paragraph 3
writes **"business intelligence"**. The same term, capitalised two ways, one
page apart. It is the last thing a strict reader could mark against Writing
Effectiveness. Left as-is by choice; lowercasing the `I` closes it.

## Rubric self-assessment

| Criterion | Score |
|---|---|
| Paragraph Content | 3 / 3 |
| Writing Effectiveness | 3 / 3 expected · 2 / 3 strictest, on the capitalisation alone |
| **Total** | **6 / 6 expected** |
