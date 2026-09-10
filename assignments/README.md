# CMPE 295A — Assignments

Course deliverables for CMPE 295A. Kept outside `runs/insightpilot/` so the
project pack's coverage audit does not count them as pack artifacts.

| # | Assignment | File | Status |
|---|---|---|---|
| 1 | Project Abstract | [`.docx`](CMPE295A_InsightPilot_Project_Abstract.docx) · [`.pdf`](CMPE295A_InsightPilot_Project_Abstract.pdf) | **Final** — 2 pages confirmed |
| 2 | Project Formation Presentation | [`.pptx`](CMPE295A_InsightPilot_Project_Formation.pptx) | **Final** — names filled; roles deliberately verbal |

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

---

## Assignment 2 — Project Formation Presentation

**Built from the instructor's template** (`Abstract-presentation-template.pptx`)
by editing its slide XML in place. Masters, layouts, notes slides and fonts
are untouched, and **the slide count is unchanged at 4** — the assignment
forbids adding pages.

| Slide | Content |
|---|---|
| 1 | Title, advisor, four team members, methodology (**no roles — see below**) |
| 2 | Project description — 5 bullets |
| 3 | Project deliverables — 5 bullets, none on the excluded list |
| 4 | Dependencies and concerns |

### Rubric targeting

All four criteria are graded by the **advisor**, not the instructor.

- **Team Formation (3 pts)** — the 3-point row requires "each with a specific
  role", and the template ships only a name list. **Roles were drafted and
  then deliberately removed** — see *Deliberate choice* below for the
  reasoning and the accepted cost. This is the weakest criterion in the deck.
- **Project Choice (3 pts)** — the 3-point row reads "no known examples in
  industry or academia". **That claim would be false**: `research/landscape.md`
  documents Genie, Cortex Analyst, Copilot, ThoughtSpot, Wren AI and Hex. The
  deck instead claims the empty quadrant — no shipped system does multi-step
  planning across heterogeneous sources with step-level verifiable lineage —
  which is true and defensible under questioning.
- **Scope (3 pts)** — deliverables are five buildable systems, and slide 4
  names the specific benchmark evidence that makes the scope hard.
- **Negotiation (3 pts)** — graded on the advisor's experience of the team,
  not on slide content. The only slide lever is the methodology declaration.

### Consistency with the abstract

The deck was audited line by line against the submitted abstract. Seven
terminology drifts were corrected ("hop" to "step", "pre-modeled" to
"pre-defined", "approves" to "reviews", and a third data-source taxonomy
unified to the abstract's relational databases / spreadsheets / web services).

**Two invented claims were removed:** "a wrong answer surfaces in seconds"
(the abstract makes no speed claim) and "95% per step is ~74% over six steps"
(the per-step rate was assumed, never measured).

Content that appears only in the deck — deliverables, dependencies, concerns,
the evaluation harness — is legitimate: the abstract has no such sections. The
evaluation harness is the largest addition and is deliberate, since it is the
strongest evidence for the Project Choice criterion.

### Deliberate choice: roles are not on the slide

Slide 1 lists the four team members by name with **no roles and no designated
lead**. This is a decision, not an oversight: the team will discuss the role
split with the advisor live during the presentation, since the split is not
yet settled and stating it as fixed would misrepresent where the team is.

**The cost is known and accepted.** The Team Formation rubric reads:

| Row | Requirement | Status |
|---|---|---|
| 3 pts | Team members identified; **each with a specific role** | not met |
| 2 pts | Team members identified. **Leader chosen** | partially — named, no leader |
| 1 pt | Difficulty following instructions to create a team of 4 | not applicable |

Expected outcome is **1–2 of 3** on this criterion, against 3 of 3 if roles
were printed. That is up to a quarter of the assignment's twelve points, and
it is the only criterion the slide content fully controls — the other three
depend on the project itself and on the advisor relationship.

**Mitigation if this stands:** raise the role split *early and unprompted*
during the presentation rather than waiting to be asked. An advisor who has
to ask has already formed an impression.

A proposed split by architecture layer, mapping onto the components in
`runs/insightpilot/tech/deep_dives.md`, is available if it is wanted later:
Orchestration & Planning · Data Integration & Connectors · Verification &
Lineage · Analytics, ML & Evaluation.

### Before submitting

- [ ] Decide finally whether roles stay off slide 1 (see above)
- [ ] Open in PowerPoint and check slide 4 fits; it carries 9 bullets and
      relies on autofit
- [ ] All team members must attend the presentation
