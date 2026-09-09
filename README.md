# CMPE 295A — Agentic BI

Working repository for the **Agentic BI** master's capstone (CMPE 295A / 295B, San José State University).

**The project.** Conversational BI for enterprise data analysts: a multi-agent system that turns a business question into a planned, executed and fully traceable analytical workflow. An Orchestrator decomposes a question into an *analysis plan*, shows it before anything runs, and dispatches it to four specialist agents across the analyst's real sources — the warehouse, the operational database, and the file nobody has ever modelled. Every handoff emits its own *lineage*, so the answer arrives with a trace the analyst can check hop by hop.

**The bet.** Not that answers are too slow, but that **a fast answer nobody will stake their name on is not an answer.** The product's design centre is making failure cheap to detect rather than promising it will not happen.

> **This repository contains documents, not code.** No implementation exists yet. The 295A build starts from [`runs/agentic-bi/product/features_prioritized.md`](runs/agentic-bi/product/features_prioritized.md), whose first item is an evaluation harness rather than a feature.

---

## Repository layout

```
cmpe295A/
├── README.md          ← you are here — repo index
├── source/            ← the original proposal this pack was derived from
└── runs/agentic-bi/   ← the generated founder pack (65 artifacts)
    ├── README.md      ← the pack's own front door: reading paths by audience
    ├── BRIEF.md       ← source of truth
    ├── ASSUMPTIONS.md ← decision ledger
    ├── research/  strategy/  product/  tech/
    ├── narrative/  validation/  financials/
    └── audit/         ← coverage report
```

**Two READMEs, two jobs.** This file indexes *what each artifact is*. [`runs/agentic-bi/README.md`](runs/agentic-bi/README.md) is the pack's front door — it gives reading paths by audience (advisor, investor, engineer, operator, practitioner, skeptic) and the 60-second path. Start there if you want to *read* the pack; stay here if you want to *find* something.

## If you only open three files

| | File | Why |
|---|---|---|
| 1 | [`narrative/one_pager.md`](runs/agentic-bi/narrative/one_pager.md) | The whole venture on one page, every figure sourced |
| 2 | [`research/competitors.md`](runs/agentic-bi/research/competitors.md) | The teardown, and §4 the differentiator — where the pack stops being a proposal and becomes an argument |
| 3 | [`research/survey.md`](runs/agentic-bi/research/survey.md) §5.2 | The strongest case *against* this project's own mechanism, stated at full strength and then answered |

---

## Source material

| File | What it is |
|---|---|
| [`source/agentic-bi-project-writeup.pdf`](source/agentic-bi-project-writeup.pdf) | The original project proposal, as submitted for academic discussion. Everything in `runs/` derives from this plus three rounds of founder interrogation |
| [`source/writeup.txt`](source/writeup.txt) | Plain-text extraction of the same proposal, used as the generation input |

## The pack — `runs/agentic-bi/`

### Root

| Artifact | What it is |
|---|---|
| [`README.md`](runs/agentic-bi/README.md) | The pack's front door — status, reading paths by audience, artifact map, the five sharpest claims |
| [`BRIEF.md`](runs/agentic-bi/BRIEF.md) | **The source of truth.** Who the user is, what the mechanism is, which claims are settled and which are deliberately not made. Every other artifact is written against this file, and it fixes the vocabulary the whole pack uses |
| [`ASSUMPTIONS.md`](runs/agentic-bi/ASSUMPTIONS.md) | **The decision ledger** — 13 entries covering every choice made without founder confirmation and every scope decision taken deliberately. It exists so a later reader can tell a *gap* from a *choice*, which is the distinction an audit would otherwise get wrong |

### `research/` — the evidence layer (5)

Everything downstream cites through here. 71 numbered sources, each graded High / Medium / Low.

| Artifact | What it is |
|---|---|
| [`landscape.md`](runs/agentic-bi/research/landscape.md) | Every serious approach to the problem, ordered nearest-to-farthest from this project's mechanism — warehouse assistants, BI copilots, agentic notebooks, open source, then §6 **the graveyard**: four prior attempts and how each actually died |
| [`competitors.md`](runs/agentic-bi/research/competitors.md) | Mechanism-level teardown of every alternative including "the analyst writes SQL" and "do nothing" — the two that win most often. §4 settles the differentiator from failure mechanisms rather than marketing gaps |
| [`capability_table.md`](runs/agentic-bi/research/capability_table.md) | Eleven capabilities the mechanism depends on, with measured performance, cost trend and the residual gap on each. This is what makes "why now" defensible — or, in one case, forces it to be restated |
| [`survey.md`](runs/agentic-bi/research/survey.md) | A dated mini survey paper: classical foundations, taxonomy, enabling technology, and §5.2 the eight strongest arguments *against* this project's own mechanism |
| [`sources.md`](runs/agentic-bi/research/sources.md) | The citation register — 71 entries with URLs, access dates and confidence grades, plus five **named gaps**: things searched for and not found, recorded so a later phase does not re-search them blind |

### `strategy/` — positioning and market (11)

| Artifact | What it is |
|---|---|
| [`market_type.md`](runs/agentic-bi/strategy/market_type.md) | Steve Blank market-type declaration — re-segmented, not new or existing — with the strategic consequences and the strongest case against the choice |
| [`positioning.md`](runs/agentic-bi/strategy/positioning.md) | The two axes that actually divide this market, where every competitor sits, the empty quadrant, and the one-sentence positioning statement. §5.1 is the **do-not-say list** |
| [`market_sizing.md`](runs/agentic-bi/strategy/market_sizing.md) | TAM / SAM / SOM built bottom-up from labour statistics × observed price, with a sensitivity table. Concludes the market is small and says so |
| [`personas.md`](runs/agentic-bi/strategy/personas.md) | Five cards — the analyst, the stakeholder, the staff data scientist, the budget owner, the security blocker — each with the objection you must overcome |
| [`lean_canvas.md`](runs/agentic-bi/strategy/lean_canvas.md) | Maurya's nine blocks on one page, with the riskiest cell marked. That cell is *unfair advantage*, and it is deliberately empty |
| [`business_model_canvas.md`](runs/agentic-bi/strategy/business_model_canvas.md) | Osterwalder's nine blocks, each carrying **one falsifiable hypothesis and the cheapest test that would kill it** |
| [`value_prop_canvas.md`](runs/agentic-bi/strategy/value_prop_canvas.md) | Jobs / pains / gains against relievers / creators, per persona, with the top mappings ranked — and §6 where the fit is weak or absent |
| [`gtm.md`](runs/agentic-bi/strategy/gtm.md) | Channel strategy, the acquisition loop intended to compound, CAC hypotheses, and the 90-day motion |
| [`petal_diagram.md`](runs/agentic-bi/strategy/petal_diagram.md) | Blank's petal, not a 2×2: the five adjacent markets customers are drawn *from*, and which budget each actually displaces |
| [`channel_plan.md`](runs/agentic-bi/strategy/channel_plan.md) | Channel **economics** — the margin stack per channel. The arithmetic disqualifies outbound, resellers and paid acquisition outright |
| [`sales_roadmap.md`](runs/agentic-bi/strategy/sales_roadmap.md) | Organisation map, influence map, access map, and the sales process with the artifact required at each step |

### `product/` — what gets built (8)

| Artifact | What it is |
|---|---|
| [`PRD.md`](runs/agentic-bi/product/PRD.md) | The product definition: the closed core loop, **ten domain principles every feature must map to**, ten real non-goals, the learning flywheel, safety requirements and success metrics |
| [`features_flagship.md`](runs/agentic-bi/product/features_flagship.md) | The 20 highest-leverage features — mechanism, principle, and the visible moment the user literally sees — closing with why the power is the closed loop rather than any single feature |
| [`features_prioritized.md`](runs/agentic-bi/product/features_prioritized.md) | 50 features in Now / Next / Later, ordered by **leverage on the riskiest claim rather than by visibility**. Includes the pre-decided cut list and the must-not-cut list |
| [`journeys/beachhead.md`](runs/agentic-bi/product/journeys/beachhead.md) | The core use case as a real Thursday afternoon, every beat naming the component that fires and what gets written to the durable record |
| [`journeys/edge_low.md`](runs/agentic-bi/product/journeys/edge_low.md) | The user who cannot verify anything, succeeding with dignity — and §5, what he still cannot do |
| [`journeys/edge_high.md`](runs/agentic-bi/product/journeys/edge_high.md) | The staff data scientist being genuinely stretched, catching something the system could not, and §7 what would make him stop using it |
| [`journeys/day_in_life.md`](runs/agentic-bi/product/journeys/day_in_life.md) | One ordinary Tuesday across all five actors. §3 tallies who gains what — and surfaced the risk that the champion gains least |
| [`ux_spec.md`](runs/agentic-bi/product/ux_spec.md) | Twelve screens: purpose, hierarchy, states, micro-interactions. §14 names the three places the spec is most likely wrong |

### `tech/` — the deep-tech layer (19)

| Artifact | What it is |
|---|---|
| [`whitepaper.md`](runs/agentic-bi/tech/whitepaper.md) | The mechanism arithmetic: six frictions decomposed, a multiplier with a confidence band per mechanism, and §5 what they total when multiplied back together |
| [`deep_dives.md`](runs/agentic-bi/tech/deep_dives.md) | The seven algorithmic components with real method names, inputs and outputs, the key design choice behind each, and its failure modes. Two are labelled research risk rather than presented as solved |
| [`architecture/00_INDEX.md`](runs/agentic-bi/tech/architecture/00_INDEX.md) | Index to the ten diagrams, with what a reviewer should notice in each and what the whole set deliberately omits |
| [`architecture/D01`–`D10`](runs/agentic-bi/tech/architecture/) | Ten Mermaid diagrams, each with a caption: the investigation pipeline · the verify-and-replan loop · agent orchestration · the durable record · model routing and cost · the security trust boundary · connectors and semantic layers · the evaluation harness · deployment and scale · human-in-the-loop |
| [`techniques/wave1.md`](runs/agentic-bi/tech/techniques/wave1.md) | 44 established techniques from data engineering, database theory and applied statistics, clustered by sub-discipline |
| [`techniques/wave2.md`](runs/agentic-bi/tech/techniques/wave2.md) | 38 advanced and theory-grounded techniques — program synthesis, reliability engineering, decision theory, queueing — with three gaps surfaced |
| [`techniques/wave3.md`](runs/agentic-bi/tech/techniques/wave3.md) | 31 frontier and cross-domain techniques, including **eight explicit declines**. The cross-domain cluster — audit, four-eyes, chain of custody — has the highest hit rate |
| [`techniques/decision_tree.md`](runs/agentic-bi/tech/techniques/decision_tree.md) | Which technique fires when, the priority order when conditions collide, and what the tree cannot decide |
| [`techniques/technique_feature_matrix.md`](runs/agentic-bi/tech/techniques/technique_feature_matrix.md) | Techniques × features, flagging orphan techniques and **unsupported features** — both are findings |
| [`not_vaporware.md`](runs/agentic-bi/tech/not_vaporware.md) | Named stack, the continuous evaluation loop, cost model at current API prices, and an explicit line between what two people build in a semester and what is research risk |

### `narrative/` — the persuasion layer (6)

Arranges evidence that already exists elsewhere. Invents nothing.

| Artifact | What it is |
|---|---|
| [`one_pager.md`](runs/agentic-bi/narrative/one_pager.md) | The single page: problem, mechanism, why now, evidence, market, team edge, and the ask |
| [`vc_memo.md`](runs/agentic-bi/narrative/vc_memo.md) | The technical memo — thesis, category-by-category demolition, architecture, two operating scenarios, and §6 the three risks that would sink it |
| [`pitch_deck.md`](runs/agentic-bi/narrative/pitch_deck.md) | 14 slides, every title a claim rather than a category. Slides 9, 10 and 13 are where a normal deck inflates and this one concedes |
| [`future_press.md`](runs/agentic-bi/narrative/future_press.md) | Working-backwards press release dated 2033, plus the timeline of how it happened — and a check that the vision does not contradict the pack's own sizing |
| [`founder_story.md`](runs/agentic-bi/narrative/founder_story.md) | Founder-market fit in first person, confronting the missing domain experience rather than finessing it. **Carries five placeholders only the founder can fill** |
| [`mission_vision.md`](runs/agentic-bi/narrative/mission_vision.md) | Mission, vision, and five values each stated as a **trade-off the company will actually make**, checked against a decision already in the ledger |

### `validation/` — what we do not yet know (9)

| Artifact | What it is |
|---|---|
| [`riskiest_assumptions.md`](runs/agentic-bi/validation/riskiest_assumptions.md) | Twelve load-bearing assumptions ranked by *kills-company × cheapness to test*. Status on every row is `untested` |
| [`experiment_board.md`](runs/agentic-bi/validation/experiment_board.md) | Nine experiments with **pass/fail thresholds declared before any data exists**, including the branch where the answer is no |
| [`discovery_guide.md`](runs/agentic-bi/validation/discovery_guide.md) | The interview kit: screening criteria, questions that ask only about the past, the timed-task protocol, and the synthesis template |
| [`get_keep_grow.md`](runs/agentic-bi/validation/get_keep_grow.md) | The funnel per segment, the activation moment, the metric that predicts retention, and the compounding loop's one fragile edge |
| [`stage_gate.md`](runs/agentic-bi/validation/stage_gate.md) | Where the venture honestly sits — Customer Discovery, **not exited** — and the six numbered criteria required to pass the next gate |
| [`metrics_by_stage.md`](runs/agentic-bi/validation/metrics_by_stage.md) | What to track at each stage and, equally, **the vanity metrics to ignore** — including the one this team will most want to report |
| [`pivot_log.md`](runs/agentic-bi/validation/pivot_log.md) | Ten roads already closed with what would reopen each, ten standing pivot triggers, and §4 the pivot to refuse |
| [`mvp_definition.md`](runs/agentic-bi/validation/mvp_definition.md) | Two MVPs kept distinct — the low-fidelity one is a **document**, not software — plus the earlyvangelist definition |
| [`decision_making_unit.md`](runs/agentic-bi/validation/decision_making_unit.md) | The buying unit by **who can say no**: user, payer, champion, saboteur, veto. Surfaced a role the persona set was missing |

### `financials/` — cost side only (3)

Three of six manifest rows. Revenue build, use of funds and exit comparables are **excluded by founder decision** — with no revenue, no CAC and no funnel, any projection would be fabricated.

| Artifact | What it is |
|---|---|
| [`pricing.md`](runs/agentic-bi/financials/pricing.md) | The value metric, sourced competitor anchors, tier design, and pricing as a **falsifiable threshold**: what would have to be true for the price to clear cost-to-serve |
| [`unit_economics.md`](runs/agentic-bi/financials/unit_economics.md) | Cost per investigation and per analyst-year, CAC by channel, and why self-hosting **inverts** the usual gross-margin analysis |
| [`risk_matrix.md`](runs/agentic-bi/financials/risk_matrix.md) | Eight risks with leading indicators and honest residuals — no risk mitigates to Low — and capstone exposure separated from venture exposure |

### `audit/` — the completeness check (1)

| Artifact | What it is |
|---|---|
| [`COVERAGE.md`](runs/agentic-bi/audit/COVERAGE.md) | Row-by-row status against the artifact manifest, the eleven defects found and fixed, three deviations accepted with reasons, and the priority draw order for what to do next |

---

## Conventions used throughout

- **Every artifact opens with a four-line orientation block** — what it is, why it exists, how to read it, what it depends on and feeds. This is checked mechanically by the audit.
- **Every number carries a source or a flag.** Figures cite `[Sn]` into [`research/sources.md`](runs/agentic-bi/research/sources.md); estimates carry an explicit `(assumption: …)` tag.
- **Artifacts end by naming their own limits** — what they assume, what would falsify them, or what they deliberately do not claim.
- **Deliberate exclusions are logged, not silent.** [`ASSUMPTIONS.md`](runs/agentic-bi/ASSUMPTIONS.md) records every scope decision so an audit can tell a choice from a gap.

## Honest state

**The pack is finished. The venture is not started.** Sixty-five artifacts, twelve untested assumptions, zero customers interviewed.

Four of those assumptions can end the project, and three of the four are answerable in roughly twenty-five founder-hours **without writing any code**. The cheapest single action is a timed task with five analysts and a stopwatch, testing whether an analyst can accept an answer they did not derive faster than they could derive it — the claim everything else rests on. See [`audit/COVERAGE.md`](runs/agentic-bi/audit/COVERAGE.md) §8 for the full draw order.

The visuals and website phases are **deferred, not cancelled** — `node` is not installed on this machine and both require it. Their prerequisites are fully satisfied, and eleven Mermaid diagrams already exist in `tech/architecture/` to reduce that work when it resumes.
