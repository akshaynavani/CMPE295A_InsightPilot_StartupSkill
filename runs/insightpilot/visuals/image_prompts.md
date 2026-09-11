# Image prompts

**What this is** — One production text-to-image prompt per manifest row, numbered `P01`–`P64`, each naming its title line, its subject, the data it must embed, and its composition zones.
**Why it exists** — No text-to-image capability was available in the session that built this phase, so every row's raster is `pending-image`. Writing the prompts anyway means a later session, or a human with an image tool, renders from a specification rather than improvising — and it means the manifest's `pending-image` rows have something concrete waiting behind them instead of an intention. The specific failure this prevents: a future session generating fifty-three images that do not match the fifty-three HTML frames, leaving the pack with two visual languages.
**How to read it** — §1 is the usage contract and §2 is the style block every prompt is prepended with. A skeptic should attack §5, which states plainly that a text-to-image model cannot render the table-heavy rows faithfully and that the HTML stays authoritative for them.
**Depends on / feeds** — Every row comes from [visual_manifest.md](visual_manifest.md); every title line is the exact `<h1>` of the matching file in [infographics/](infographics/). Feeds `images/*.png` and, through those, `docimages.json`.

---

## 1. How to use these

**Each prompt is used as `STYLE_BLOCK + "\n\n" + P<ID>`.** The style block in §2 is stated once rather than repeated sixty-four times. That is a deliberate deviation from "fully self-contained per prompt": repeating four hundred characters sixty-four times would make this file unreadable without making any single prompt more complete, and the concatenation rule is mechanical.

**Five rules for whoever renders these.**

1. **The TITLE line must render legibly and match exactly.** It is the stage-2 verification handle: a file of the right size in the right place can still be the wrong picture, and the title is how you tell. A raster whose headline does not match its prompt is worse than a missing one, because nothing downstream will catch it again.
2. **The authoritative composition is the HTML file**, named on every row. Open it before rendering. The prompt is a summary of that file, not a replacement for it.
3. **Every number must come from the named source artifact.** No prompt below introduces a figure that is not already in the pack. If a render produces a number that is not in the prompt, discard it — a plausible invented figure on a polished image is the exact failure mode this pack is built against.
4. **File naming is `images/<ID>_<slug>.png`**, where `<slug>` matches the HTML file's slug exactly, because `build_docimages.js` maps rasters to artifacts by that slug.
5. **Reconcile `visual_manifest.md` from `ls` afterwards.** A row marked rendered without a file on disk is a defect the audit will find.

**Orientation is 1280×720 (16:9) for every row** unless the prompt says otherwise.

## 2. The style block

Prepend this literal text to every prompt below.

```
Extremely information-dense professional infographic, pure white background (#FFFFFF),
elite systems-architect and domain-expert quality, clean modern sans-serif typography with
a clear three-level hierarchy, one bold headline takeaway readable in three seconds, then
3 to 5 labelled information zones that reward thirty seconds, refined minimal iconography,
print-grade, 1280x720 landscape, no watermark, no lorem ipsum, no stock-photo imagery,
no human faces, no 3D renders, no gradients except flat zone washes.
Palette, used consistently: ink #14181F for headlines, body text #3A424E, captions and
source lines #6B7484, dividers #E2E6EC, primary accent #1F5FA8, passed-and-confirmed
states #1E7A54, amber and untested states #B4741A, failure and risk #A3352B, zone wash
#F5F7FA.
Every figure that appears must be one of the figures named in the prompt. Invent no data.
End with a small muted source line in the lower margin, exactly as given.
```

---

## 3. Audience A — users

### P01 · V01 — core loop
**TITLE:** "Verify is a beat in the loop, not a footnote after it"
**SUBJECT.** A six-stage horizontal loop reading ask → plan → execute → answer → verify → follow up, with the verify beat visually heaviest and an arrow closing from follow up back to ask. Each stage carries two or three short mechanism labels.
**DATA.** The loop's six stage names verbatim. Ask: ambiguity interception, bindings shown. Plan: plan shown before execution, hop-count discipline. Execute: four specialist agents, verification after every handoff. Answer: established facts, doubt surfaced. Verify: hop lineage, single-hop re-run, sign-off. Follow up: context inherited, so a follow-up is a short plan.
**ZONES.** (1) the loop itself; (2) why verify is a beat and not an appendix; (3) what the loop refuses to do, namely ship an unreviewed answer.
**SOURCE LINE.** "Source: product/PRD.md · V01"
**AUTHORITATIVE COMPOSITION:** `infographics/V01_core_loop.html`

### P02 · V02 — user spectrum
**TITLE:** "One adaptive system, three edges, and no separate tiers"
**SUBJECT.** Three labelled edges on one horizontal band: low edge (business manager, requester), beachhead (enterprise data analyst), high edge (staff data scientist). The interface adapts; there are no product tiers.
**DATA.** Low edge: plain-language answer, cannot judge correctness, never writes a query; justifies the conversational interface. Beachhead: compress per-question overhead, retain control and verifiability; the user the pack is written for. High edge: audit lineage, override the model's target and algorithm, extend the pipeline; makes traceability load-bearing.
**ZONES.** (1) the three edges; (2) the user is not the payer; (3) the spectrum was inferred rather than supplied, and is the one assumption that invalidates the product layer if wrong.
**SOURCE LINE.** "Source: strategy/personas.md, product/PRD.md · V02"
**AUTHORITATIVE COMPOSITION:** `infographics/V02_user_spectrum.html`

### P03 · V03 — the beachhead's Thursday
**TITLE:** "The 8% join failure that takes twenty minutes to find, surfaced in forty seconds"
**SUBJECT.** Two parallel timelines for the same question, by hand against with a plan, with the amber verification moment marked on the second.
**DATA.** 90 minutes by hand against 31 minutes with the system. Nine of the 31 minutes are verification. Step 3 amber: join preserved 13,061 of 14,201 rows, 8% unmatched, the file has four region codes against the warehouse's six. Coverage after the fix reaches 99.2%. Final answer: cost per shipment rose 11.4%, volume fell 3.1%, rate rose 14.0%, the move is rate and not mix.
**ZONES.** (1) the two timelines; (2) the amber hop rendered as the analyst sees it; (3) the four checkable claims; (4) the honest note that nine of thirty-one minutes are spent verifying.
**SOURCE LINE.** "Source: product/journeys/beachhead.md · V03"
**AUTHORITATIVE COMPOSITION:** `infographics/V03_beachhead_thursday.html`

### P04 · V04 — the low edge's gate
**TITLE:** "He gets an answer in ninety seconds, and he cannot ship it alone"
**SUBJECT.** A short vertical flow: stakeholder asks, answer returns in ninety seconds carrying an amber not-yet-reviewed bar, it is routed for review, an analyst signs off in roughly six minutes, and only then can it be exported.
**DATA.** Ninety seconds to an answer. An amber unreviewed state that blocks export without acknowledgement. About six minutes of an analyst's time rather than ninety. The alternative he had before: a three-day wait, or a guess.
**ZONES.** (1) the gated flow; (2) why gating is not paternalism, since the alternative is guessing, which 76% of businesses already do; (3) the renunciation, that this product is not self-service for people who cannot judge correctness.
**SOURCE LINE.** "Source: product/journeys/edge_low.md · V04"
**AUTHORITATIVE COMPOSITION:** `infographics/V04_low_edge_gate.html`

### P05 · V05 — the high edge's review
**TITLE:** "The largest measured gain in the pack, from one mechanism used alone"
**SUBJECT.** A reviewer's path through an exported investigation, with a large before-and-after pair of durations.
**DATA.** Two hours becomes nineteen minutes. Re-running one hop takes ninety seconds against twenty minutes rebuilding it. The model card carries the target definition in full, an entity-grouped split with a thirty-day embargo, and one feature excluded as a leakage candidate with the reason stated. He catches something the system cannot: a ticket-system migration makes pre-April counts structurally lower, so the data is wrong in a way no schema records.
**ZONES.** (1) the review path; (2) the model card's contents; (3) the catch the system could not make; (4) the note that the gain comes from lineage alone, used by a persona who touches nothing else.
**SOURCE LINE.** "Source: product/journeys/edge_high.md · V05"
**AUTHORITATIVE COMPOSITION:** `infographics/V05_high_edge_review.html`

### P06 · V06 — one ordinary Tuesday
**TITLE:** "Everyone gains, and the champion gains least"
**SUBJECT.** Five horizontal lanes for five roles across one shared day, each lane showing a before and after duration, with the analyst's lane visually marked as the exception.
**DATA.** Staff data scientist: two hours to nineteen minutes. Platform lead: a day and a half to eight minutes. Business stakeholder: a three-day wait or a guess, to ninety seconds plus a six-minute review. The VP gains an investigation she could not previously run. The analyst absorbs the review burden the other four shed, and her net gain on the day is the smallest of the five.
**ZONES.** (1) the five lanes; (2) the uneven distribution called out explicitly; (3) why it matters, since the whole go-to-market routes through the analyst's advocacy; (4) the two contingent things that make it survivable.
**SOURCE LINE.** "Source: product/journeys/day_in_life.md · V06"
**AUTHORITATIVE COMPOSITION:** `infographics/V06_day_in_life.html`

### P07 · V07 — the interface surface
**TITLE:** "Twelve screens, and three of them are the product"
**SUBJECT.** A twelve-cell grid of named screens, with three cells highlighted as the differentiating surfaces and the rest shown as conventional.
**DATA.** Twelve named screens from the interface specification, with the plan surface, the hop lineage surface and the exported investigation marked as the three that carry the differentiator.
**ZONES.** (1) the twelve-screen grid; (2) the three that matter and why; (3) the overload state, specified deliberately because review load is the champion's risk.
**SOURCE LINE.** "Source: product/ux_spec.md · V07"
**AUTHORITATIVE COMPOSITION:** `infographics/V07_twelve_screens.html`

### P08 · V08 — the verification tick
**TITLE:** "A green tick means these checks passed. It never means the answer is right"
**SUBJECT.** A single enlarged verification tick, annotated with exactly what it asserts and, beside it, an explicit list of what it does not assert.
**DATA.** The structural checks a tick covers: row-count reconciliation, grain assertion, anti-join coverage, null-rate delta, boundary totals. What it cannot cover: that the question was interpreted correctly, that the chosen metric is the right one, that the underlying data is correct, and the semantically plausible defect class where counts are right and meaning is wrong.
**ZONES.** (1) the tick and its claim; (2) the explicit non-claims; (3) the amber state; (4) the note that a tick users over-read is a worse outcome than no tick.
**SOURCE LINE.** "Source: product/ux_spec.md · V08"
**AUTHORITATIVE COMPOSITION:** `infographics/V08_verification_tick.html`

## 4. Audience B — operators and the build team

### P09 · V09 — system map
**TITLE:** "Everything runs inside the customer's boundary, with one arrow leaving"
**SUBJECT.** A dashed boundary box labelled customer environment containing three columns of components, with exactly one arrow crossing out to a model provider.
**DATA.** Inside: investigation surface, semantic resolver, lineage surface, orchestrator as the single writer, four agents (data fetch, analytics, visualization, ML), step verifier, connector layer for PostgreSQL and files through DuckDB and REST services, semantic interface, binding store, lineage store, append-only audit log. Outside: a model provider reached on the customer's own key, with a schema-only mode available. No write path exists. No cross-organisation path exists.
**ZONES.** (1) the boundary and its contents; (2) the single egress; (3) what is absent by design; (4) what it costs, namely that each deployment's binding store starts empty.
**SOURCE LINE.** "Source: tech/architecture/00_INDEX.md and D01–D10 · V09"
**AUTHORITATIVE COMPOSITION:** `infographics/V09_system_map.html`

### P10 · V10 — investigation pipeline
**TITLE:** "Investigation pipeline, end to end"
**RENDER NOTE — read before using this prompt.** This row is satisfied by a Mermaid diagram inside `tech/architecture/D01_investigation_pipeline.md`. **Render the Mermaid source, do not generate this topology with a text-to-image model** — a generative model will produce a plausible graph with wrong edges, which is the exact failure class this pack is built against. The prompt below exists only for a decorative title-card variant, and a decorative variant must never replace the diagram.
**DECORATIVE VARIANT.** A clean left-to-right pipeline of six labelled stages with a verification checkpoint between each pair, no data values, accent-coloured checkpoints.
**SOURCE LINE.** "Source: tech/architecture/D01_investigation_pipeline.md · V10"

### P11 · V11 — verify and replan loop
**TITLE:** "Verify-and-replan closed loop"
**RENDER NOTE.** Mermaid source in `tech/architecture/D02_verify_replan_loop.md`. Render it; do not generate the topology.
**DECORATIVE VARIANT.** A closed cycle of four nodes with one branch returning to the planner on failed verification, failure path in the failure colour.
**SOURCE LINE.** "Source: tech/architecture/D02_verify_replan_loop.md · V11"

### P12 · V12 — agent orchestration
**TITLE:** "Agent orchestration: the star topology"
**RENDER NOTE.** Mermaid source in `tech/architecture/D03_agent_orchestration.md`. Render it. The point of the diagram is that agents never call each other, and a generated graph will draw the edges this architecture deliberately does not have.
**DECORATIVE VARIANT.** A star: one central orchestrator, four peripheral agents, every edge passing through the centre and no edge between peripherals.
**SOURCE LINE.** "Source: tech/architecture/D03_agent_orchestration.md · V12"

### P13 · V13 — durable record and binding store
**TITLE:** "Durable record and binding store"
**RENDER NOTE.** Mermaid source in `tech/architecture/D04_memory_schema.md`. Render it; a generated entity diagram will invent relationships.
**DECORATIVE VARIANT.** Four cylinder shapes labelled investigations, hops, bindings and overrides, with provenance arrows between them.
**SOURCE LINE.** "Source: tech/architecture/D04_memory_schema.md · V13"

### P14 · V14 — model routing
**TITLE:** "Model routing: where the tokens actually go"
**RENDER NOTE.** Mermaid source in `tech/architecture/D05_model_routing_cost.md`. Render it.
**DECORATIVE VARIANT.** A routing fan: planning, term resolution, SQL generation and replanning to a frontier-class lane; prose and chart choice to a small-fast lane; verification and statistical work to a lane labelled zero model tokens in the confirmed colour.
**SOURCE LINE.** "Source: tech/architecture/D05_model_routing_cost.md · V14"

### P15 · V15 — trust boundary
**TITLE:** "Trust boundary: one egress arrow"
**RENDER NOTE.** Mermaid source in `tech/architecture/D06_security_trust_boundary.md`. Render it. The audience for this row is a security reviewer, and an approximated boundary is worthless to him.
**DECORATIVE VARIANT.** A single dashed enclosure with one arrow leaving it, everything else contained, no labels invented.
**SOURCE LINE.** "Source: tech/architecture/D06_security_trust_boundary.md · V15"

### P16 · V16 — connectors and semantic layers
**TITLE:** "Connectors and semantic layers: two interfaces"
**RENDER NOTE.** Mermaid source in `tech/architecture/D07_connectors_ecosystem.md`. Render it.
**DECORATIVE VARIANT.** Two distinct interface bars: one for read-only data sources, one for semantic suppliers whose definitions take hard precedence over inferred bindings.
**SOURCE LINE.** "Source: tech/architecture/D07_connectors_ecosystem.md · V16"

### P17 · V17 — evaluation harness
**TITLE:** "Evaluation harness and what it measures"
**RENDER NOTE.** Mermaid source in `tech/architecture/D08_evaluation_harness.md`. Render it.
**DECORATIVE VARIANT.** A fixture-driven loop: question set, seeded-error set, run, score, publish. Label the published outputs as execution accuracy and silent-error rate, and nothing else.
**SOURCE LINE.** "Source: tech/architecture/D08_evaluation_harness.md · V17"

### P18 · V18 — deployment topology
**TITLE:** "Deployment topology and the real ceiling"
**RENDER NOTE.** Mermaid source in `tech/architecture/D09_deployment_scale.md`. Render it.
**DECORATIVE VARIANT.** A single-tenant stack repeated three times side by side with no shared control plane between them, and a caption noting that the ceiling is support load rather than infrastructure.
**SOURCE LINE.** "Source: tech/architecture/D09_deployment_scale.md · V18"

### P19 · V19 — human in the loop
**TITLE:** "Human-in-the-loop: three mandatory gates"
**RENDER NOTE.** Mermaid source in `tech/architecture/D10_human_in_the_loop.md`. Render it.
**DECORATIVE VARIANT.** A linear run with three gate symbols interrupting it: term disambiguation, plan approval on first run against a source, and sign-off before export.
**SOURCE LINE.** "Source: tech/architecture/D10_human_in_the_loop.md · V19"

### P20 · V20 — technique decision tree
**TITLE:** "Technique decision tree"
**RENDER NOTE.** Mermaid source in `tech/techniques/decision_tree.md`. Render it; a generated tree will mislabel branches.
**DECORATIVE VARIANT.** A three-level decision tree shape with no text, accent-coloured decision nodes, used only as a section card.
**SOURCE LINE.** "Source: tech/techniques/decision_tree.md · V20"

### P21 · V21 — seven components
**TITLE:** "Five of seven components are engineering. The other two are the venture"
**SUBJECT.** Seven labelled component cards in a row, five in the confirmed colour and two in the failure colour, each with a one-line mechanism.
**DATA.** Semantic resolver, plan synthesiser, query generator with execution-feedback repair, hop verifier, cross-source reconciler, lineage recorder and replayer, time-boxed modelling agent. The two marked research risk are the plan synthesiser's quality on real schemas and the verifier's coverage of plausible failures.
**ZONES.** (1) the seven components; (2) the two structural properties, that agents never call each other and that verification consumes zero model tokens; (3) the two research risks named rather than hidden.
**SOURCE LINE.** "Source: tech/deep_dives.md · V21"
**AUTHORITATIVE COMPOSITION:** `infographics/V21_seven_components.html`

### P22 · V22 — feature roadmap
**TITLE:** "The evaluation harness is feature one. Three of four agents are not in scope"
**SUBJECT.** Three tiers labelled Now, Next and Later as vertical columns, plus a fourth column listing pre-decided cuts.
**DATA.** The harness and the seeded-error set are the first two items, before any agent. Three of the four agents fall outside the near-term scope. The cut list is pre-decided with reasons, and charts and the ML agent are named as the two most tempting additions mid-semester.
**ZONES.** (1) the three tiers; (2) the cut list; (3) the reason the harness leads, which is that every number the pack claims depends on it.
**SOURCE LINE.** "Source: product/features_prioritized.md · V22"
**AUTHORITATIVE COMPOSITION:** `infographics/V22_feature_roadmap.html`

### P23 · V23 — flagship features
**TITLE:** "Nine of the twenty sit in the verify beat, and none of them is defensible alone"
**SUBJECT.** Twenty small feature cards distributed across six loop-phase columns: ask (3), plan (3), execute (6), answer (2), verify (5), follow up (1), with the verify column visually weighted.
**DATA.** The twenty feature names in their phases. Nine cards marked as serving the verification-cost principle, three marked as value asserted rather than demonstrated. Nine of ten principles carry a flagship feature; the tenth carries a practice instead.
**ZONES.** (1) the loop-phase distribution; (2) why the loop and not the feature, since each element makes the next cheaper; (3) the concession, that one untested claim holds four of the features up.
**SOURCE LINE.** "Source: product/features_flagship.md · V23"
**AUTHORITATIVE COMPOSITION:** `infographics/V23_flagship_features.html`

### P24 · V24 — technique by feature matrix
**TITLE:** "The verification layer is well armed. Statistical honesty is not"
**SUBJECT.** A heat-mapped grid, eleven feature rows against eight technique-category columns, cell values as counts, with two cells marked as unsupported gaps in the failure colour.
**DATA.** Structural checks carry seven techniques behind per-hop verification; schema linking carries five behind ambiguity interception. The two high-severity gaps are both on the statistical-method column: no multiple-comparisons correction behind diagnostic questions, and no calibration measurement behind doubt surfacing. 113 techniques across three waves, five orphaned, three features thinly supported.
**ZONES.** (1) the matrix; (2) the two gaps and why both concern statistical honesty rather than mechanics; (3) the note that the differentiator rests on old, well-tested imports.
**SOURCE LINE.** "Source: tech/techniques/technique_feature_matrix.md · V24"
**AUTHORITATIVE COMPOSITION:** `infographics/V24_technique_matrix.html`

### P25 · V25 — three technique waves
**TITLE:** "113 techniques, and the most useful cluster is the one borrowed from other fields"
**SUBJECT.** Three wave panels side by side with counts as large numerals and category breakdowns beneath.
**DATA.** Wave one, established practice: 44 techniques, 43 used. Wave two, advanced and theory-grounded: 38 techniques, 17 used. Wave three, frontier and cross-domain: 31 techniques, 15 used, 8 declined. The cross-domain cluster has the highest hit rate: six used, three candidates, none declined. Five of the eight declines are fashionable techniques, including self-critique loops, multi-agent debate and model-as-judge.
**ZONES.** (1) the three waves; (2) the cross-domain imports, from financial audit, accounting controls, forensics, scientific computing and clinical pre-registration; (3) the eight declines; (4) what this says about novelty, namely that the techniques are old and the composition is not.
**SOURCE LINE.** "Source: tech/techniques/wave1.md, wave2.md, wave3.md · V25"
**AUTHORITATIVE COMPOSITION:** `infographics/V25_technique_waves.html`

### P26 · V26 — stack and the research line
**TITLE:** "Nine of nine near-term items are ordinary engineering. The two that are not are the two the venture needs"
**SUBJECT.** A named stack list on the left; on the right, two facing buckets labelled buildable in one semester and research risk, each item carrying a confidence tag.
**DATA.** Stack: Python 3.12, a custom orchestrator on a typed plan DAG rather than an agent framework, a provider-agnostic model client on the customer's key, DuckDB for files, SQLAlchemy and psycopg, statsmodels STL, scikit-learn and LightGBM, Postgres for the application store, append-only JSONL on disk for the audit log, FastAPI and React, Docker Compose, pytest for the harness. Research risks: the plan synthesiser's quality on real schemas, verifier coverage of plausible failures, whether verification beats re-derivation, override re-flow across a grain change, and useful modelling inside a minutes budget.
**ZONES.** (1) the stack; (2) buildable against research risk; (3) the two stack choices worth defending, no agent framework and DuckDB; (4) what a reviewer should conclude, namely not a wrapper and not solved.
**SOURCE LINE.** "Source: tech/not_vaporware.md · V26"
**AUTHORITATIVE COMPOSITION:** `infographics/V26_stack_and_research_line.html`

### P27 · V27 — ten principles
**TITLE:** "A feature that maps to none of these gets cut, or the list was wrong"
**SUBJECT.** Ten numbered principle cards in two rows, each with its one-line statement and the evidence that grounds it, with the two most load-bearing marked.
**DATA.** The ten principle statements verbatim, including that schema grounding is the dominant failure surface, that error compounds across hops, that failure presents as plausible rather than obviously wrong, that consistency degrades faster than capability, that verification cost is the thing being sold, that pre-encoding narrows scope, that verification must run structurally different code, that access standardised and semantics did not, that modelling does not fit a conversational latency, and that multi-hop reasoning is currently weak.
**ZONES.** (1) the ten principles; (2) the two that carry the most features; (3) the one that deliberately has no feature and carries a practice instead.
**SOURCE LINE.** "Source: product/PRD.md §3 · V27"
**AUTHORITATIVE COMPOSITION:** `infographics/V27_ten_principles.html`

## 5. Audience C — investors, advisor and evaluator

### P28 · V28 — positioning axes
**TITLE:** "The quadrant is empty because the problem is hard, not because nobody looked"
**SUBJECT.** A two-by-two map: horizontal axis hops executed autonomously, vertical axis where correctness is established. Competitors plotted as labelled dots; the target quadrant empty and marked.
**DATA.** Incumbents cluster in the pre-encoded, single-hop corner. The notebook competitor sits in the analyst-directed corner. The empty quadrant is many-hop execution with correctness carried in the answer, and it is empty because multi-step data reasoning measures about 15% on hard tasks.
**ZONES.** (1) the map; (2) why the quadrant is empty, stated as a capability fact rather than a market gap; (3) the prohibition on head-to-head accuracy claims, since no commercial product publishes a figure.
**SOURCE LINE.** "Source: strategy/positioning.md · V28"
**AUTHORITATIVE COMPOSITION:** `infographics/V28_positioning_axes.html`

### P29 · V29 — mechanism arithmetic
**TITLE:** "Ninety minutes becomes thirty-one. That is 2.9x, and it is not 10x"
**SUBJECT.** A friction-decomposition waterfall: six named frictions, four attacked, with minute values and the resulting total.
**DATA.** 90 minutes to 31 minutes, roughly 2.9 times, band 1.8 to 4.2. Cross-source reconciliation is the largest single mechanism at about 4.0 times. On a single-source familiar question the gain is about 1.0 or below, and the analyst should keep writing SQL. A 13.8 times queueing multiplier was computed and withdrawn because induced demand consumes it, and must not appear.
**ZONES.** (1) the waterfall; (2) the conservative and optimistic corners; (3) the explicit withdrawal of the larger figure; (4) the statement that this is not an order-of-magnitude claim.
**SOURCE LINE.** "Source: tech/whitepaper.md §5 · V29"
**AUTHORITATIVE COMPOSITION:** `infographics/V29_mechanism_arithmetic.html`

### P30 · V30 — market sizing
**TITLE:** "This is a small market, and the pack says so rather than reaching"
**SUBJECT.** A bottom-up build shown as a descending funnel from an occupational population to a serviceable figure, with a sensitivity strip of corners beneath.
**DATA.** About 1.24 million beachhead analysts globally and about 74,600 in the US meeting the day-one criteria, built from labour statistics plus three tagged assumptions. At $75 per analyst per month: total $1.1B, serviceable $123M, pessimistic corner $38M. Capstone obtainable market is $0, because monetisation is out of scope.
**ZONES.** (1) the bottom-up build with each factor labelled sourced or assumed; (2) the three figures; (3) the sensitivity corners published rather than buried; (4) the refusal to state a share of a large category.
**SOURCE LINE.** "Source: strategy/market_sizing.md · V30"
**AUTHORITATIVE COMPOSITION:** `infographics/V30_market_sizing.html`

### P31 · V31 — the graveyard
**TITLE:** "Four attempts ended. None of them died of bad technology"
**SUBJECT.** A horizontal timeline with four headstone-free markers, each carrying the attempt, its year, and its mechanism of death.
**DATA.** A discontinued analytics product folded into a reporting suite in 2019, killed by curation burden exceeding value returned. A narration company absorbed into a BI vendor in 2021, because narration is a feature rather than a company. A diagnostic-analytics company that raised about $128.7M and became a warehouse division in 2023. A natural-language query feature inside the most widely deployed BI tool on earth, fully retired by December 2026, for which distribution was never the problem.
**ZONES.** (1) the timeline; (2) the two failure modes, curation-to-value ratio and gravity; (3) the note that both are live for this venture.
**SOURCE LINE.** "Source: research/landscape.md · V31"
**AUTHORITATIVE COMPOSITION:** `infographics/V31_graveyard.html`

### P32 · V32 — competitor teardown
**TITLE:** "The two that win most often are free, and neither is a product"
**SUBJECT.** A nine-row teardown table with columns competitor, mechanism, pricing, where it wins, and where it fails mechanistically. The first two rows, doing nothing and the analyst writing SQL, highlighted as the market leaders.
**DATA.** Doing nothing is free and does not fail. The analyst's own SQL fails on latency and never on correctness. One incumbent caps at 30 tables per agent. One prices at about $0.134 per message with a token-capped hand-authored model. One cannot compute a metric that is not already a measure. One costs $50 per user per month with its agent capped at 25 queries. One notebook competitor charges $36 to $75 per editor. One open-source peer has 13,000+ stars and 10,000+ cloud users. No head-to-head accuracy claim may appear anywhere on this image.
**ZONES.** (1) the table; (2) failure mode one, that pre-encoded correctness cannot answer the unanticipated; (3) failure mode two, that plausible-but-wrong is undetectable at delivery; (4) the statement that no head-to-head accuracy comparison exists.
**SOURCE LINE.** "Source: research/competitors.md · V32"
**AUTHORITATIVE COMPOSITION:** `infographics/V32_competitor_teardown.html`

### P33 · V33 — capability frontier
**TITLE:** "The spread is the finding, not the headline number"
**SUBJECT.** A horizontal bar chart of nine measured capabilities, ordered to show the spread, each bar carrying its figure and a short context note.
**DATA.** 96.7% on a curated text-to-SQL setting; 76.2% on a lighter setting; 65.6% once semantic indirection and real project structure appear, a 31-point drop. 80.0% best single model on another benchmark against 92.96% human performance. 30 to 36% on production-scale wide schemas of about 1,000 columns and 54 tables. Under 25% when eight consecutive attempts must all succeed, against above 60% on one. 76.4% on an easy real-analytics split and about 15% on the hard split, which is 84% of that benchmark's tasks. 36.4% medal rate on automated machine learning, under a twelve-hour budget.
**ZONES.** (1) the bars; (2) why the weakest bar is the argument for the architecture; (3) the caution that benchmark scores are not deployment accuracy; (4) what is genuinely favourable, namely a standardised tool-access layer.
**SOURCE LINE.** "Source: research/capability_table.md · V33"
**AUTHORITATIVE COMPOSITION:** `infographics/V33_capability_frontier.html`

### P34 · V34 — risk matrix
**TITLE:** "Nothing mitigates to low, and the two fatal risks barely move"
**SUBJECT.** A likelihood-by-impact grid with risks plotted twice each, as inherent and residual, joined by short arrows showing how little most of them move.
**DATA.** No residual risk lands below medium. The two fatal risks are that verification is not cheaper than re-derivation and that multi-hop planning is not reliable enough, and both barely move under mitigation because both are measurement problems rather than engineering ones.
**ZONES.** (1) the matrix with inherent-to-residual arrows; (2) the two that do not move; (3) the honest note that a matrix where everything mitigates to low is a matrix nobody believed.
**SOURCE LINE.** "Source: financials/risk_matrix.md · V34"
**AUTHORITATIVE COMPOSITION:** `infographics/V34_risk_matrix.html`

### P35 · V35 — unit economics
**TITLE:** "The margin looks excellent because the customer absorbed the variable cost"
**SUBJECT.** Three panels: a who-pays line list, a retry-sensitivity table, and a margin block with one deliberately unflattering comparison row.
**DATA.** The customer pays frontier inference, warehouse compute for queries and verification, small-model calls and storage; we pay support and releases; nobody pays hosting. Per investigation at one, two, three and five attempts: $1.21, $2.28, $3.36 and $5.50, which is $189, $356, $524 and $858 per analyst-year. Revenue $900 per analyst-year, inference and hosting cost of goods zero, assumed support $60 to $120, gross margin 87 to 93%. The same product hosted at three attempts would be 42% before support. Verification costs about six cents of warehouse compute and zero model tokens. Acquisition: open-source self-serve and internal referral at about zero, inside sales $3,000 to $8,000, reseller 20 to 35%.
**ZONES.** (1) the inversion; (2) the retry table with the 4.5-times spread called out; (3) the margin block with the hosted comparison; (4) what the analysis cannot support, including no lifetime-value ratio and no retention figure.
**SOURCE LINE.** "Source: financials/unit_economics.md · V35"
**AUTHORITATIVE COMPOSITION:** `infographics/V35_unit_economics.html`

### P36 · V36 — pricing threshold
**TITLE:** "The threshold holds by 1.3 to 2.1 times, which is a real result and a narrow one"
**SUBJECT.** A three-row bar comparison of hours that must be saved against hours the mechanism delivers, plus a price-anchor list and a three-tier block.
**DATA.** Anchors: about $0.134 per message, $25 and $50 per user per month with an agent capped at 25 queries, $36 to about $75 per editor, about $137,000 average enterprise contract, $35 to $200 per month for a lighter tool. The analyst-tool band is $36 to $75 per seat per month. Break-even hours at one, three and five attempts: 18.4, 24.2 and 29.9, against 38.4 hours delivered, giving margins of 2.1, 1.6 and 1.3 times. Tiers: open core free, team $75 per analyst per month, enterprise negotiated.
**ZONES.** (1) the anchor list and the band; (2) the break-even bars; (3) the three tiers and why the differentiator ships free; (4) the four falsifiers.
**SOURCE LINE.** "Source: financials/pricing.md · V36"
**AUTHORITATIVE COMPOSITION:** `infographics/V36_pricing_threshold.html`

### P37 · V37 — stage gate
**TITLE:** "A complete artifact pack, twelve untested assumptions, zero customers interviewed"
**SUBJECT.** A four-stage rail with a you-are-here marker on the first stage, an evidence list, and six numbered exit criteria with thresholds.
**DATA.** Nine falsifiable hypotheses stated, zero customers interviewed, no working software, zero of twelve riskiest assumptions tested, problem statement from desk research. Six exit criteria: ten analysts plus five budget owners interviewed; median 25% or more of last-twenty requests spanning two systems; verification cost ratio at or below 0.5 with a hard fail above 0.8; 70% or more of seeded defects rejected and at least twice the control rate; three of five buyers naming a budget line; seven of ten analysts confirming both spectrum edges. About twenty-five founder-hours over four weeks, and no engineering.
**ZONES.** (1) the four-stage rail; (2) the evidence for the placement; (3) the six criteria; (4) the dangerous combination where cheap verification does not verify.
**SOURCE LINE.** "Source: validation/stage_gate.md · V37"
**AUTHORITATIVE COMPOSITION:** `infographics/V37_stage_gate.html`

### P38 · V38 — experiment board
**TITLE:** "Nine thresholds fixed in writing while they are still uncomfortable"
**SUBJECT.** A three-by-three grid of experiment cards, each with a pass/amber/fail threshold strip and a decision-if-fail line, plus a four-wave sequencing strip beneath.
**DATA.** The nine experiments and their thresholds: cost ratio pass at 0.5 or below and fail above 0.8; detection pass at 70% and twice control; source-spanning pass at 25%; budget line three of five; review load under four hours a week and flat; execution accuracy pass at 50%, fail under 30%; verifier coverage 60% overall and 30% on the plausible class; clone to first investigation under thirty minutes; semantic-layer lift of fifteen percentage points. Every result reads planned. Waves: about nineteen founder-hours over three weeks, then six hours over one week, then four weeks of harness work, then ongoing deployed work.
**ZONES.** (1) the nine cards; (2) the wave strip; (3) why the first two experiments are separate, since cheap checking and working checking are different claims; (4) what the board deliberately omits.
**SOURCE LINE.** "Source: validation/experiment_board.md · V38"
**AUTHORITATIVE COMPOSITION:** `infographics/V38_experiment_board.html`

### P39 · V39 — riskiest assumptions
**TITLE:** "The cheapest tests attack the largest risks, and not one has been run"
**SUBJECT.** A scatter plot, consequence-if-wrong on the vertical axis against cost of the cheapest decisive test on the horizontal, with twelve labelled points and a shaded no-code band on the left.
**DATA.** Twelve assumptions with costs of six hours, three weeks, five hours, four hours, free, one week, free, one week, four days, free, free and already answered. Four rows can end the venture and three of them need no code; together they need about nineteen founder-hours over three weeks. Two rows already carry negative evidence.
**ZONES.** (1) the scatter with its quadrant reading; (2) the ranked board with each row's current evidence state; (3) the sequencing that follows; (4) the one row that is a refusal rather than an assumption.
**SOURCE LINE.** "Source: validation/riskiest_assumptions.md · V39"
**AUTHORITATIVE COMPOSITION:** `infographics/V39_riskiest_assumptions.html`

### P40 · V40 — market type
**TITLE:** "The category is old and the capability is not, which is what makes this ambiguous"
**SUBJECT.** Four market-type cards with the chosen one enlarged and accented, then a consequences list and a full-strength counter-case.
**DATA.** Four types with their dominant risks and sales cycles. The declaration is re-segmented by different attribute, on verifiability across sources, with the analyst as beachhead. Four supporting reasons: the low-end play was tried and marked down 73.67%; 59% are funding semantic layers and 24.9% name accuracy as their top reservation and 71% fear wrong output reaching stakeholders; incumbents cannot follow without contradicting their own design; the empty quadrant is empty because the capability measures about 15%. Dominant risk is segment reality rather than competition.
**ZONES.** (1) the four types; (2) the four reasons; (3) the consequences the declaration commits to; (4) the strongest case against, that verification may be a complaint rather than a budget.
**SOURCE LINE.** "Source: strategy/market_type.md · V40"
**AUTHORITATIVE COMPOSITION:** `infographics/V40_market_type.html`

### P41 · V41 — the petal
**TITLE:** "The empty quadrant has no budget attached to it"
**SUBJECT.** A centre badge with five petal cards around it, each labelled with its incumbents, its current spend and what would make a customer switch. One petal marked primary source, one marked budget-aligned, one marked supplier rather than source.
**DATA.** Analyst time, spend is salary and unbudgeted, the primary source. Warehouse-native copilots, bundled plus metered credits, additive rather than a switch. Semantic layers, 59% of large organisations adding budget, the largest active budget and a supplier petal. Analyst notebooks, $36 to $75 per editor per month, the only petal where spend, buyer and price align. Data science and automated ML, headcount, not year one.
**ZONES.** (1) the five petals around the centre; (2) the ranked draw order; (3) why the largest budget is the wrong one to draw from; (4) the three consequences, including that adoption precedes revenue structurally.
**SOURCE LINE.** "Source: strategy/petal_diagram.md · V41"
**AUTHORITATIVE COMPOSITION:** `infographics/V41_petal_diagram.html`

### P42 · V42 — evidence ledger
**TITLE:** "Seventy-one sources, graded, with the weak ones labelled rather than laundered"
**SUBJECT.** A stacked confidence bar across the top, a horizontal bar chart of sources per section, a cautions list, and five named gaps.
**DATA.** 71 sources: 29 high, 24 medium, 12 low-to-medium, 6 low. By section: competitors and pricing 24, benchmarks 14, adoption and market structure 10, problem magnitude 7, enabling technology 7, the graveyard 6, labour-market baseline 3. Eight low-confidence rows are quarantined and one of them supports nothing anywhere. Eight rows are registered and deliberately uncited. Five gaps were searched for and not found.
**ZONES.** (1) the grade distribution with definitions; (2) the section bars; (3) the cautions; (4) the five named gaps.
**SOURCE LINE.** "Source: research/sources.md · V42"
**AUTHORITATIVE COMPOSITION:** `infographics/V42_evidence_ledger.html`

## 6. Audience D — buyers, partners and the security reviewer

### P43 · V43 — trust boundary, buyer-facing
**TITLE:** "One arrow leaves, you choose what rides on it, and there is no write path to disable"
**SUBJECT.** Two facing mode panels showing exactly what the single egress carries, a bordered never-leaves panel, and three absence cards.
**DATA.** Mode one, schema only: column names, types, comments and the question text, no values. Mode two: the same plus sampled distinct values, with personal-data-flagged columns excluded, and still no full result sets and no credentials. Never crossing: credentials, result sets, the lineage record, the binding store, the audit log, file contents, flagged columns, anything from another organisation. Three absences: no write path, no cross-organisation path, no re-implemented authorisation. The audit log is append-only on disk and readable without the application running; a quarterly access review took eight minutes against a day and a half.
**ZONES.** (1) the two modes with their trade-offs stated; (2) the never-leaves list; (3) the three absences; (4) three things this does not claim, including that it is not a compliance certification.
**SOURCE LINE.** "Source: tech/architecture/D06_security_trust_boundary.md · V43"
**AUTHORITATIVE COMPOSITION:** `infographics/V43_trust_boundary.html`

### P44 · V44 — the decision-making unit
**TITLE:** "Two of the six can end this without ever being in a meeting"
**SUBJECT.** A six-row table of roles with can-say-yes and can-say-no columns, plus a five-step vertical sequence and an objection-artifact list.
**DATA.** Six roles: the analyst who is champion and whose silence ends it; the VP who alone can say yes and no; the platform lead with an asymmetric veto; the staff scientist as credibility gate; the analytics manager who never says no and allocates no time; the business stakeholder with no vote. The sequence runs platform lead, analyst, manager, scientist, VP, and contains no meeting. Four of five objection artifacts do not exist yet and one is measurable this month with no code.
**ZONES.** (1) the role table; (2) the actual sequence; (3) the objection artifacts with their status; (4) the underweighted role, the analytics manager, and the one-hour correction.
**SOURCE LINE.** "Source: validation/decision_making_unit.md · V44"
**AUTHORITATIVE COMPOSITION:** `infographics/V44_decision_making_unit.html`

### P45 · V45 — get, keep, grow
**TITLE:** "The mechanism that differentiates the product is the same one that distributes it"
**SUBJECT.** Three funnel-stage columns with metric rows, a band gauge for the retention predictor, and a vertical loop with one edge marked fragile.
**DATA.** Get: 500 repo visitors in ninety days, 100 clones, 60 connectors configured, 40 first successful investigations, gated at under thirty minutes. Keep: three investigations per analyst per week by week four; hop-inspection rate between 20% and 60%, where both extremes are failures; override rate falling over eight weeks; review time under four hours and flat; half of activated analysts still running at week eight. Grow: one export per active analyst per week, 20% of deployments reaching a second analyst by week twelve, three analysts per deployment, 10% reaching a budget conversation by week twenty-four. Every current value is zero or unmeasured.
**ZONES.** (1) the three stages; (2) the inspection-rate band with both failure ends; (3) the loop and its fragile edge; (4) the concession that the best growth vector could break retention.
**SOURCE LINE.** "Source: validation/get_keep_grow.md · V45"
**AUTHORITATIVE COMPOSITION:** `infographics/V45_get_keep_grow.html`

### P46 · V46 — channel economics
**TITLE:** "The price disqualifies most channels before any strategy is applied"
**SUBJECT.** An anchor strip of three figures, a nine-row channel table with viability verdicts, and two waterfall blocks.
**DATA.** $900 per analyst per year, a realistic account of five to fifteen analysts, a working contract value of $9,000. Outbound waterfall: $9,000 list, minus $5,500 acquisition, $3,500 gross contribution before cost to serve. Reseller waterfall: $9,000 list, minus 28% partner discount to $6,480, minus a 4% marketplace fee to $6,120, which is 68% of list. Four channels viable at about zero marginal cost; field sales would need a seventeen-seat account; paid acquisition fails on intent.
**ZONES.** (1) the anchor strip; (2) the channel table; (3) the two waterfalls with the reason each fails; (4) the tension, that the only viable channel produces no revenue.
**SOURCE LINE.** "Source: strategy/channel_plan.md · V46"
**AUTHORITATIVE COMPOSITION:** `infographics/V46_channel_economics.html`

### P47 · V47 — two MVPs
**TITLE:** "The first one is a document, and it can invalidate the second one entirely"
**SUBJECT.** Two facing MVP panels with a gate between them, plus a five-criterion earlyvangelist list.
**DATA.** Low fidelity: no software, buildable in a day, about six founder-hours, a hand-built exported investigation plus a stopwatch, in one correct and three defective variants. Falsifiers: median cost ratio above 0.8, or defect rejection under 50%. High fidelity: one question type, two source types, end to end, with the harness; falsifiers are execution accuracy under 30% and near-zero catch on the plausible defect class. Six deliberate omissions including charts, a third connector and the modelling agent. Five earlyvangelist criteria, all required, all about past behaviour.
**ZONES.** (1) the two panels; (2) the gate, where failing the first means the second never starts; (3) the five criteria; (4) what neither MVP tests.
**SOURCE LINE.** "Source: validation/mvp_definition.md · V47"
**AUTHORITATIVE COMPOSITION:** `infographics/V47_two_mvps.html`

## 7. Dossier coverage

### P48 · V48 — the brief in one frame
**TITLE:** "One brief, so the PRD, the market sizing and the whitepaper describe one company"
**SUBJECT.** A document-style frame: the one-line positioning across the top, then three columns covering the spectrum and vocabulary, the problem and mechanism, and the why-now with the riskiest assumption boxed in the failure colour.
**DATA.** The one-line statement verbatim. The three edges and what each constrains. The eight vocabulary terms. The four agents and the six-stage loop. Two why-now shifts, both founder-asserted. Four things not being done in year one. The riskiest assumption stated in full.
**ZONES.** (1) the spectrum and vocabulary; (2) the problem and mechanism; (3) the two deliberately empty sections, no order-of-magnitude claim and no moat; (4) the riskiest assumption.
**SOURCE LINE.** "Source: BRIEF.md · V48"
**AUTHORITATIVE COMPOSITION:** `infographics/V48_brief_one_frame.html`

### P49 · V49 — the decision ledger
**TITLE:** "Six weeks from now, nobody remembers whether an empty section was an oversight or a choice"
**SUBJECT.** A thirteen-row ledger grouped into three categories, each row carrying a state and a kills-the-pack flag, with one row marked yes.
**DATA.** Four deliberate scope decisions, five deferred decisions now closed or raised, four generator inferences. The one row flagged as invalidating downstream work is the inferred three-edge user spectrum. Four standing rules: no requests-per-analyst-per-week figure, no head-to-head accuracy claim, no manufactured order-of-magnitude claim, and one phrase that must not appear anywhere.
**ZONES.** (1) the ledger; (2) the standing rules with the required why-now wording quoted; (3) two naming risks recorded rather than resolved; (4) what the ledger is for, which is letting an advisor tell a gap from a choice.
**SOURCE LINE.** "Source: ASSUMPTIONS.md · V49"
**AUTHORITATIVE COMPOSITION:** `infographics/V49_decision_ledger.html`

### P50 · V50 — survey, for and against
**TITLE:** "The case against is stronger on reliability and weaker on whether the position is worth occupying"
**SUBJECT.** A balance layout: six supporting items on the left, eight opposing items on the right, with a verdict block beneath the heavier side.
**DATA.** Six for, including that the strongest incumbent independently confirms decompose-then-verify, that the connector layer is now configuration, that demand for verifiability is measured at 71% and 24.9% and a rise from 66% to 83%, and that 44% of data-engineer time on pipelines was measured before this cycle. Eight against, including roughly 15% on hard tasks, compounding arithmetic, a 73.67% markdown, an open-source peer two years ahead, a $35-a-month commodity at the entry point, and forecasts that cut both ways.
**ZONES.** (1) for; (2) against; (3) the assessment and the architectural inversion; (4) the three consequences that bind downstream work.
**SOURCE LINE.** "Source: research/survey.md · V50"
**AUTHORITATIVE COMPOSITION:** `infographics/V50_survey_for_against.html`

### P51 · V51 — lean canvas
**TITLE:** "The riskiest cell is empty, and it is empty on purpose"
**SUBJECT.** A ten-block canvas in the conventional lean-canvas arrangement, with the unfair-advantage block outlined in the failure colour and flagged, and the revenue block washed grey as hypothetical.
**DATA.** Each block's three bullets, including one-to-four-week turnaround and 76% deciding without data; the three existing alternatives; the four agents and the open-core deployment; the three key metrics; the value proposition stated as not faster but checkable; the empty advantage block with its one candidate; the channels; about 74,600 US analysts; the cost structure with zero storage cost; and the $75 per analyst per month threshold.
**ZONES.** (1) the canvas; (2) why the empty cell is the risk, for the opposite of the usual reason; (3) the instruction not to fill it later; (4) the three blocks this canvas drops.
**SOURCE LINE.** "Source: strategy/lean_canvas.md · V51"
**AUTHORITATIVE COMPOSITION:** `infographics/V51_lean_canvas.html`

### P52 · V52 — business model canvas
**TITLE:** "Nine blocks, each carrying the cheapest test that would kill it"
**SUBJECT.** A nine-row table with columns for block, falsifiable hypothesis, cheapest killing test and when it can run, with two rows shaded as strategy-ending and one as the venture itself.
**DATA.** Nine hypotheses and nine tests. Seven cost days rather than months. Two can each independently invalidate the strategy and neither needs code. The second row is the venture. Four blocks are the ones the shorter canvas drops.
**ZONES.** (1) the nine rows; (2) the three reading notes; (3) what the canvas concedes, including that the team holds capability rather than assets.
**SOURCE LINE.** "Source: strategy/business_model_canvas.md · V52"
**AUTHORITATIVE COMPOSITION:** `infographics/V52_business_model_canvas.html`

### P53 · V53 — the five ranked fits
**TITLE:** "The top three fits are one mechanism sold to three people for three reasons"
**SUBJECT.** Five ranked fit cards, each with pain, reliever, persona and a fit-strength bar, beside a compact beachhead profile of jobs, pains and gains.
**DATA.** Rank one: cannot verify without re-deriving, relieved by re-runnable lineage, serving all three personas, strong and unproven. Rank two: the unmodelled source, strong. Rank three: provenance on demand, strong commercially. Rank four: fixed per-question overhead, medium, and the crowded part. Rank five: the predictive question, weak to medium. Four places the fit is weak or absent, including that perfect lineage over bad data produces a traceable wrong answer.
**ZONES.** (1) the beachhead profile; (2) the five fits; (3) where fit is absent; (4) the rule to lead with the first fit and never the fourth.
**SOURCE LINE.** "Source: strategy/value_prop_canvas.md · V53"
**AUTHORITATIVE COMPOSITION:** `infographics/V53_value_prop_fits.html`

### P54 · V54 — the go-to-market loop
**TITLE:** "Most of the channels do not compound. One does, and the plan is a bet on it"
**SUBJECT.** Three constraint cards across the top, a channels-by-segment list, a six-step vertical loop with one step marked as the break point, and a ninety-day motion panel.
**DATA.** Six channels by segment with the reason for each. The loop's six steps, with the export-to-colleague edge marked fragile. First ten design partners described by type in four groups. Four moves for the first hundred, including publishing the accuracy number and a quickstart under thirty minutes. Five things deliberately excluded from the ninety-day motion.
**ZONES.** (1) the three constraints; (2) the channels; (3) the loop and its break point; (4) the ninety-day motion and what is excluded from it.
**SOURCE LINE.** "Source: strategy/gtm.md · V54"
**AUTHORITATIVE COMPOSITION:** `infographics/V54_gtm_loop.html`

### P55 · V55 — sales roadmap
**TITLE:** "The person who feels the pain has no budget, and the person with budget never uses it"
**SUBJECT.** A four-level organisation tree on the left, a ranked influence list in the centre, an access map on the right, and an eight-step process strip along the bottom.
**DATA.** The tree: finance above, the VP as economic buyer, three siblings of analytics manager, platform lead and staff scientist, and five to fifteen analysts beneath, with business stakeholders outside the tree entirely. Influence ranked one to five with the analyst first and the veto third. The access map shows exactly one cold-reachable actor. The eight-step process with step three marked pivotal and step seven marked the commercial failure point.
**ZONES.** (1) the tree and its two structural facts; (2) the influence ranking and where its claim breaks; (3) the access map and its one door; (4) the eight-step process with its required artifacts.
**SOURCE LINE.** "Source: strategy/sales_roadmap.md · V55"
**AUTHORITATIVE COMPOSITION:** `infographics/V55_sales_roadmap.html`

### P56 · V56 — metrics by stage
**TITLE:** "This product's most flattering metrics are its least informative ones"
**SUBJECT.** Four stage columns, each split into a track list and a visually distinct ignore list in the failure wash, plus a band gauge and a warning panel.
**DATA.** Discovery tracks five metrics including a surprise count above zero per three interviews, and ignores five including stars and interview count. Validation tracks five including a silent-error rate to be reported regardless, and ignores five including accuracy on the easy subset. Creation tracks four and ignores three. One metric is fixed now for the far horizon. The inspection band runs 20 to 60% with both extremes as failures.
**ZONES.** (1) the four stages with track against ignore; (2) the band with both failure ends; (3) the metric the team will most want to report and should not, namely a working demo.
**SOURCE LINE.** "Source: validation/metrics_by_stage.md · V56"
**AUTHORITATIVE COMPOSITION:** `infographics/V56_metrics_by_stage.html`

### P57 · V57 — pivot log
**TITLE:** "A trigger written after a disappointing result is a rationalisation, so all ten are fixed now"
**SUBJECT.** Two ranked lists side by side, ten closed roads with what would reopen each and ten armed triggers with their deadlines, plus a boxed refusal panel.
**DATA.** Ten closed roads, each with its reopening condition, including two that reopen on nothing. Ten triggers with deadlines at weeks three, four, five, twelve and the two semester ends, with three marked stop-or-halt. Four things explicitly not yet decided. The tempting pivot is named and refused with three reasons.
**ZONES.** (1) the closed roads; (2) the armed triggers; (3) the pivot to refuse; (4) the log format, where a decision without a reopening condition is a mood.
**SOURCE LINE.** "Source: validation/pivot_log.md · V57"
**AUTHORITATIVE COMPOSITION:** `infographics/V57_pivot_log.html`

### P58 · V58 — discovery guide
**TITLE:** "Three venture-ending questions are answerable by talking to about fifteen people"
**SUBJECT.** A banner stating the one rule, then screening criteria, a question list with two questions highlighted, a boxed timed-task protocol, and an anti-pattern list.
**DATA.** The one rule: ask about the past, never about the future. Screening targets of ten analysts, five buyers, three scientists, three stakeholders, with the analyst criteria all five required. The highlighted questions are the last-twenty-requests count and how they decide whether to trust an analysis they did not do. The protocol's two conditions, what to record including what they did not look at, the pass threshold of 0.5 and fail above 0.8, and the instruction that confusion is data. Five anti-patterns.
**ZONES.** (1) the one rule; (2) screening; (3) the questions; (4) the protocol and the anti-patterns.
**SOURCE LINE.** "Source: validation/discovery_guide.md · V58"
**AUTHORITATIVE COMPOSITION:** `infographics/V58_discovery_guide.html`

### P59 · V59 — mission and values
**TITLE:** "A value phrased as a virtue costs nothing. Each of these names what is given up"
**SUBJECT.** A mission panel and a vision panel across the top, then five value columns, each with a trade-off line, an already-decided line, a what-it-costs line in the failure wash and a why-we-accept-it line in the confirmed wash.
**DATA.** The mission and vision verbatim. Five values: publish the number that makes us look worse; refuse the question rather than guess at it; verify with different code; the person who cannot verify does not get to ship unverified; consume what the customer already built. Each with its cost stated, including losing the impressive headline, a worse demo, looking less sophisticated, renouncing the largest revenue segment, and depending on artifacts we do not control.
**ZONES.** (1) mission and vision; (2) the five values as trade-offs; (3) why we exist, and the evidence that speed was not the binding constraint; (4) what would make us abandon this.
**SOURCE LINE.** "Source: narrative/mission_vision.md · V59"
**AUTHORITATIVE COMPOSITION:** `infographics/V59_mission_values.html`

### P60 · V60 — the one-pager
**TITLE:** "InsightPilot"
**SUBJECT.** A document-style one-page layout: the product name and positioning line in a masthead with the one-line statement opposite, then three columns, then a bottom band carrying the ask and a boxed riskiest-thing panel. **This is the only row whose headline is the product name rather than a claim** — the masthead must read as a front door, and the positioning line sits immediately beneath it.
**DATA.** One to four weeks turnaround; 76% deciding without data; 81.2% of analysed failures schema-level; 71% fearing wrong output; trust rising from 66% to 83%; a thirty-table cap, a token-capped model and measures-only as the three incumbent bounds; 90 to 31 minutes at roughly 2.9 times with a band of 1.8 to 4.2 and about 1.0 on familiar single-source questions; about 1.24 million analysts globally and 74,600 in the US; total $1.1B, serviceable $123M, pessimistic $38M; three asks.
**ZONES.** (1) the problem and why the obvious fix fails; (2) what we do and why now; (3) thin evidence, market and team edge; (4) the ask and the riskiest thing.
**SOURCE LINE.** "Source: narrative/one_pager.md · V60"
**AUTHORITATIVE COMPOSITION:** `infographics/V60_one_pager.html`

### P61 · V61 — the memo
**TITLE:** "The mechanism that makes these products safe is the mechanism that makes them decline the work"
**SUBJECT.** A thesis band across the top, then a category-by-category demolition column, a graveyard column, and a risks column with three cards, one bordered in the failure colour.
**DATA.** Five competitor categories with what each does well, its measured limit and why it cannot close the gap. Four graveyard entries with mechanisms of death. Three honest risks with mitigations, plus an explicit statement that competition is not the top risk. Four things that would change the memo.
**ZONES.** (1) the thesis; (2) the demolition; (3) the graveyard and the gravity answer; (4) the three risks and the four things that would change the memo.
**SOURCE LINE.** "Source: narrative/vc_memo.md · V61"
**AUTHORITATIVE COMPOSITION:** `infographics/V61_vc_memo.html`

### P62 · V62 — working backwards
**TITLE:** "Written in 2026, dated 2033, and the good ending is losing control of the differentiator"
**SUBJECT.** A press-release column on the left with a dateline and three pull quotes, a metrics row and a seven-year timeline in the centre, and four consistency checks on the right.
**DATA.** Adoption past 50% among large data organisations. Median verification cost ratio 0.31 against a baseline near 1.0. About $74M annual recurring revenue across 1,900 organisations. Timeline entries for 2026 through 2033, with 2026 and 2028 marked critical. Four consistency checks: no hypergrowth, no order-of-magnitude claim, the moat evidenced in 2029 rather than asserted, and losing exclusivity as the good ending.
**ZONES.** (1) the release and its quotes; (2) the metric that did not exist and the timeline; (3) the four checks; (4) the branch where the premise was false, and the one-paragraph release for it.
**SOURCE LINE.** "Source: narrative/future_press.md · V62"
**AUTHORITATIVE COMPOSITION:** `infographics/V62_future_press.html`

### P63 · V63 — founder-market fit
**TITLE:** "The standard founder story is unavailable here, and pretending otherwise would be the fastest way to lose a room"
**SUBJECT.** A first-person narrative column, a three-item counter-intuitive-failure-modes column, and a boxed gap panel in the failure colour beside a dashed placeholder panel in the amber colour.
**DATA.** Compounding arithmetic at 95% and 90% per step, labelled arithmetic rather than a measurement of this system. 81.2% of analysed failures schema-level; 71% fearing wrong output. Three counter-intuitive failure modes: adding capability reduces reliability, self-critique is not verification, consistency degrades faster than capability. Three reasons the missing domain experience is confronted rather than papered over, including the rejected headline figure. Four bracketed placeholders only the founder can fill.
**ZONES.** (1) the story; (2) why the next ten years, and the temperament edge; (3) the gap and its three answers; (4) the placeholders, with the instruction to cut rather than soften.
**SOURCE LINE.** "Source: narrative/founder_story.md · V63"
**AUTHORITATIVE COMPOSITION:** `infographics/V63_founder_fit.html`

### P64 · V64 — the deck arc
**TITLE:** "Fourteen slides, every title a claim rather than a category, and three of them concede"
**SUBJECT.** A five-by-three grid of fourteen slide cards, colour-coded by arc: four teardown cards in the failure wash, one hinge card outlined in the accent, three mechanism cards in the confirmed wash, three concession cards outlined in amber, and the rest plain.
**DATA.** The fourteen slide titles verbatim, each with a one-line payload. The arc notes: the teardown takes a third of the time; slide five is the hinge and nothing after it lands if the room does not follow the inversion; three slides concede where a normal deck inflates. Two numbers that must never appear: the withdrawn queueing multiplier and any head-to-head accuracy claim.
**ZONES.** (1) the fourteen cards with arc colour coding; (2) the arc notes; (3) the two forbidden numbers.
**SOURCE LINE.** "Source: narrative/pitch_deck.md · V64"
**AUTHORITATIVE COMPOSITION:** `infographics/V64_deck_arc.html`

---

## 8. What these prompts cannot do

Stated plainly, because a prompt file that implies rasters can replace the HTML would mislead whoever renders them.

1. **A text-to-image model cannot render a dense table faithfully.** Roughly a third of the rows here are tables or matrices with exact figures in every cell, and generative renderers transpose digits, duplicate rows and invent plausible labels. **For every row marked with an authoritative composition, the HTML file is the deliverable and the PNG is decoration.** A raster that disagrees with its HTML must be deleted, not reconciled.
2. **The eleven Mermaid rows must not be generated at all.** Their value is the exact topology, and an approximated graph is worse than none: a reader cannot tell a generated edge from a real one. Render the Mermaid source instead.
3. **No prompt here introduces a number.** Every figure appears in the named source artifact. That makes the prompts verifiable and it also means they cannot be made more impressive without breaking the pack's own rule.
4. **Stage-2 verification is not optional.** The TITLE line on each prompt is the handle: open the rendered file and confirm the headline matches before marking any row rendered. A wrong picture of the right size in the right place is the one defect the audit cannot catch later.

## Recommended next 3

1. **Render the three highest-traffic rows first** and check them against their HTML before batching anything: the one-pager, the mechanism arithmetic and the capability frontier. If those three come back with garbled figures, stop, and keep the HTML as the only visual deliverable.
2. **Never render the Mermaid rows.** Add a CLI render of the eleven diagrams instead, which produces exact output and is the cheaper path to the same coverage.
3. **Reconcile `visual_manifest.md` from `ls` in the same session as any rendering,** and re-run `build_docimages.js` afterwards. A raster that exists but is not mapped is invisible to the reader, which is the same outcome as not having rendered it.
