# Technical investor memo — Agentic BI

**Dated 2026-09-09**

**What this is** — The technical memo: thesis, category-by-category demolition of existing approaches, the architecture, two compressed operating scenarios, the argument for why this can win, and the three risks that would sink it.
**Why it exists** — An advisor or technical investor assessing this project will ask *"why hasn't Databricks already done this, and why won't they next quarter?"* This memo is where that question gets answered with named systems and measured limits rather than with positioning language. It exists in a specific constraint: the pack has no customers, no revenue and no accuracy measurement yet, so the memo must persuade on **mechanism and evidence about the field**, never on traction it does not have.
**How to read it** — §2 is the demolition and §6 is the risk section; a reader short on time should read those two. A skeptic should attack §5's recombination argument, which is the memo's least evidenced section, and §6.1, which is the risk that would end it.
**Depends on / feeds** — Arranges [research/competitors.md](../research/competitors.md), [research/landscape.md](../research/landscape.md), [tech/](../tech/whitepaper.md), [product/journeys/](../product/journeys/beachhead.md), [strategy/](../strategy/positioning.md). **Invents nothing** — every figure traces to [research/sources.md](../research/sources.md).

---

## 1. Thesis

Every serious attempt at conversational analytics has converged on the same correctness mechanism: **require a human to pre-encode the semantics before the question is asked.** Snowflake requires a hand-authored YAML model `[S36]`; Databricks requires a curated space capped at 30 tables `[S32]`; Power BI Copilot can only reference measures that already exist `[S42]`. This works, and it is why the market is funding semantic layers — 59% of large enterprises are directing incremental budget there `[S17]`.

**The convergence has a structural cost nobody has priced: the tighter the pre-encoding, the narrower the set of questions the system will attempt.** An ad-hoc question is by construction the one nobody anticipated, so the mechanism that makes these products safe is the mechanism that makes them decline the work.

The alternative is not a better guardrail. It is to accept that a system spanning unmodelled sources will sometimes be wrong, and to make being wrong **cheap to detect**. Multi-step data reasoning measures ≈14.55–16% on hard real-world tasks `[S4]` — so a product promising trustworthy autonomous answers is promising what the field cannot deliver, while a product whose design centre is *making failure legible in seconds* is buildable today and addresses the market's own top-ranked objection `[S16][S17]`.

**The unit of value is the investigation, not the query. It ships with a hop-level trace, and the bet is that verification is cheaper than re-derivation.**

## 2. Why existing approaches are insufficient

Category by category, with named systems and measured limits.

### 2.1 Warehouse-native assistants — Genie, Cortex Analyst, Copilot, Pulse

**What they do well.** Governance, lineage and compute inherited from the platform. Zero data movement. Databricks' *Inspect* is genuinely strong: Genie re-reads its own generated SQL, authors smaller statements to verify specific aspects, and regenerates `[S32]`. That is verification-by-decomposition arrived at independently, and it corroborates the architectural bet here.

**The structural limit.** All four are **single-source and effectively single-hop**, and each is bounded by a pre-authored artifact: 30 tables per Genie Agent `[S32]`, ~1 MB / ~32K tokens of hand-maintained YAML for Cortex `[S36]`, existing-measures-only for Copilot `[S42]`, single-number metrics with clear dimensions for Pulse `[S49]`.

**Why they cannot close the gap.** Removing the bounds reintroduces the unreliability the bounds were bought to prevent. A Genie that spans Postgres, a REST API and an uploaded CSV as equal peers is a feature arguing against Databricks' own data gravity. **The constraint is the product.**

**What the numbers say about the ceiling.** On the Spider 2.0 benchmark family, top systems reach **96.70% on the Snow setting and 65.60% on the DBT setting** `[S1]` — a 31-point drop when semantic-layer indirection and real project structure appear. On production-scale schemas of ~1,000 columns and 54 tables, measured accuracy is **30–36%** `[S2]`. **No commercial agentic-BI product publishes an accuracy figure on any public benchmark** ([research/sources.md](../research/sources.md), *Named gaps* 2) — which is itself informative.

### 2.2 Search-first analytics — ThoughtSpot

**The purest market test of this category, and it was repriced.** ThoughtSpot raised at $4.2B in November 2021. A June 2024 secondary cleared at $6.80/share against a $25.83 Series F price — **a 73.67% markdown implying ≈$920M** `[S46]`.

**What that means.** The "let non-analysts self-serve via natural language" thesis did not pay off at the price it was funded at. Note also that Spotter is **capped at 25 queries per user per month** on the Pro tier `[S44]` — that is the pricing of an occasional-use feature, not of something living in an analyst's core loop.

**The consequence for this memo:** the beachhead here is the analyst, not the business user. That is a deliberate renunciation of the category's largest revenue segment, made on this evidence.

### 2.3 Agentic notebooks — Hex

**The most honest competitor, and the one that matters.** Hex's Notebook Agent covers fetch, analyse, model and visualise `[S54]`, and it **already solves auditability structurally**: every hop is a visible, editable, re-runnable cell. The notebook *is* the lineage.

**The limit.** The analyst still directs. No plan is produced before execution, no replanning when a result invalidates an assumption, no dispatch across specialists. The unit of work is a notebook, not an investigation pursued to a verified answer.

**Why this is named prominently.** Any lineage claim must beat *"we show you every cell"* — and "our trace is prettier" does not. Hex's customers are also the only ones in the landscape where budget, buyer and price all align ([strategy/petal_diagram.md](../strategy/petal_diagram.md) §3).

### 2.4 Open source — Wren AI

**Nearest neighbour, two years ahead.** Open-sourced April 2024; **13,000+ GitHub stars and 10,000+ cloud users by end-2025** `[S50]`; semantic-engine-anchored RAG with its own modelling language `[S51]`.

**The honest difference is scope of loop, not novelty of approach.** Wren AI is text-to-SQL plus charts — no ML agent, no cross-source replanning, no plan-before-execution gate. That is a quantitative difference, and this memo states it rather than letting a reader discover it.

### 2.5 The two that actually win — "the analyst writes SQL" and "do nothing"

**Doing nothing is the market leader.** 76% of businesses have decided without consulting data because access was too hard `[S15]`; 60–73% of enterprise data is never used for analytics `[S15]`; roughly **25% of employees use the BI tools their employer bought, flat across seven years** `[S22]`. Free, instant, and rational when the alternative is a one-to-four-week wait `[S15]`.

**The analyst's own SQL never fails on correctness — only on latency.** She *is* the verification step. That asymmetry is why it is so hard to displace, and it is the reason this product's target is verification cost rather than raw speed.

### 2.6 The graveyard

Four prior attempts, and **none died of bad technology**:

| Attempt | Outcome | Mechanism of death |
|---|---|---|
| **IBM Watson Analytics** | Discontinued June 2019, folded into Cognos `[S59]` | Curation burden exceeded value returned |
| **Power BI Q&A** | Fully retired December 2026 `[S40]` | Shipped inside the most widely deployed BI tool on earth. **Distribution was never its problem** — the linguistic-schema curation it demanded of modellers was `[S41]` |
| **Narrative Science** | Acquired into Tableau, Dec 2021 `[S58]` | Narration is a feature, not a company. Absorbed by whoever owned the data |
| **Sisu Data** | Raised ≈$128.7M; acquired by Snowflake Oct 2023, standalone product in wind-down `[S56][S57]` | Attacked the diagnostic question — the highest-value part of the loop — and was still absorbed by the warehouse |

**Two failure modes, both live for this venture.** Watson and Q&A died of the *curation-to-value ratio*. Narrative Science and Sisu died of *gravity*. §5.3 answers both.

## 3. Core architecture

Seven components. Full detail in [tech/deep_dives.md](../tech/deep_dives.md); diagrams in [tech/architecture/](../tech/architecture/00_INDEX.md).

1. **Semantic resolver** — binds business terms to concrete expressions via hybrid sparse-dense retrieval plus value-based linking; **halts and asks when the top-2 candidates fall within a margin** rather than taking the argmax. This attacks the 81.2% of failures that are schema-level `[S2]`.
2. **Plan synthesiser** — emits a typed, validatable DAG of steps over named sources, **shown and approved before any query runs**. Errors cost an edit, not six executed hops.
3. **Query generator with execution-feedback repair** — constrained to columns a binding named; repairs against real database errors, not model self-assessment `[S14]`.
4. **Hop verifier** — after every handoff, a battery of cheap, structurally *different* SQL checks: row-count reconciliation, grain assertion, anti-join coverage, null-rate delta, boundary totals. **No model calls.**
5. **Cross-source reconciler** — profiles join keys, proposes domain alignments (`SW` / `SOUTHWEST` / `SW-1`), reports coverage as a first-class output. **Proposes, never silently applies.**
6. **Lineage recorder and replayer** — per-handoff record, single-hop deterministic replay, and a self-contained export that opens without the product running.
7. **Time-boxed modelling agent** — baseline model in minutes, with target definition, split strategy, excluded features *with reasons*, and an explicit **not-attempted-in-budget list**.

**Two structural properties worth noting.** Agents never call each other — every handoff routes through the Orchestrator, so there is exactly one place lineage is appended and verification fires. And **verification consumes zero model tokens**, so the differentiating mechanism is the cheapest thing in the system.

## 4. Concrete operating examples

### 4.1 The beachhead — Priya, 4:10pm Thursday

*"Why did cost per shipment go up in the Southwest last month?"* The answer needs the warehouse joined to a carrier-cost CSV that has never been modelled — the exact case Copilot declines, because cost-per-shipment-by-carrier-by-region is not an existing measure `[S42]`.

The system halts before planning: *"'Cost' matches billed invoice total and estimated shipment cost. Which?"* She picks billed, corrects the denominator to `COUNT(DISTINCT shipment.id)` — **and that correction persists org-wide.** A six-step plan appears; she deletes an over-broad fetch in fifteen seconds, before a single query runs.

**Step 3 returns amber: *"join preserved 13,061 of 14,201 rows — 8% unmatched. CSV has 4 region codes, warehouse has 6."*** She has seen this failure before; it is what made her distrust the last tool. Here it surfaced in **40 seconds** instead of the 20 minutes it takes to find by hand. She fixes the mapping, downstream re-runs, coverage reaches 99.2%.

Answer: *"Cost per shipment rose 11.4%. Volume fell 3.1%. Rate rose 14.0%. The move is rate, not mix."* Four checkable claims. She re-runs one hop to spot-check, signs off, exports one file.

**31 minutes against her own 90-minute estimate. Nine of those 31 were verification.**

### 4.2 The high edge — Dr. Chen, staff data scientist

He is not producing analysis; he is **reviewing** one. His usual cost is two hours, and the worst outcome is that it turns out fine — because then he has spent two hours confirming something with no way to spend less next time.

He opens the exported investigation in a text editor first, to confirm it is genuinely self-contained. It is. He goes straight to the join he did not write, re-runs that single hop against current data — **ninety seconds versus twenty minutes rebuilding it**. Then the model card: target definition in full, entity-grouped split with a 30-day embargo, **`last_login_date` excluded as a leakage candidate, with the reason stated.**

Then he catches something the system could not: feature importance ranks `support_ticket_count` third, and he knows tickets migrated systems in April, so pre-April counts are structurally lower. **The data is wrong in a way no schema records.** He overrides, annotates it as a data-provenance issue rather than a model error, re-runs. Top two drivers hold.

**19 minutes against two hours.** The largest single ratio in the pack — and it comes from one mechanism, lineage, used by a persona who touches nothing else.

## 5. Why this can win where others have not

### 5.1 The recombination

None of the seven components is novel alone. Genie verifies within a query `[S32]`; Cortex reads a semantic model `[S36]`; Hex shows every step `[S54]`; Wren AI is open source with a modelling layer `[S50]`.

**What is not copyable piecemeal is the closure:** the plan is visible before it runs, so errors cost an edit. Each hop is verified by a *different* query, so failures surface rather than propagate. Failure triggers replanning rather than continuation. The trace is emitted per handoff and re-runnable in isolation, so checking costs seconds. An override corrects the organisation's semantics permanently, so the next question is cheaper. The whole thing exports as one artifact.

Each element makes the next cheaper. **A competitor shipping hop-level lineage without the plan-first, verify-per-hop, override-persisting structure has shipped a log file.**

**This is a positioning claim, not a 10× claim.** The arithmetic totals ≈2.9× on multi-source questions and ≈1.0× or below on single-source familiar ones ([tech/whitepaper.md](../tech/whitepaper.md) §5). The memo does not inflate it.

### 5.2 The intellectual ancestor

The differentiator is not new; it is imported. **Financial audit solved "how do you trust a result you did not derive" centuries ago, and its answer was to make the trail the deliverable** — the workpaper, not the number. Add the four-eyes principle from accounting controls, chain of custody from forensics, and reproducible-research practice from scientific computing.

Saying this is stronger than implying novelty: it means the mechanism has a long track record, and it gives the buyer a vocabulary they already have.

### 5.3 Why this does not become a Databricks feature

The gravity question that killed Sisu and Narrative Science.

**The value is in spanning, and no warehouse vendor can sell spanning.** A Databricks feature treating Postgres, a file and a REST API as equal peers to the lakehouse argues against Databricks' own gravity. Genie's design says so out loud — its reliability strategy is a curated space of at most 30 tables `[S32]`. Cortex Analyst is Snowflake-only by construction `[S36]`.

**Open-core and self-hostable is what makes the claim credible rather than convenient.** Neutrality asserted by a hosted service that sees all the customer's data is a claim; neutrality backed by code the customer runs in their own environment, on their own model key, is a property.

**The honest residual:** neutrality is a structural answer, not an empirical one. If the first serious customer's questions all live in one warehouse anyway, the argument is true and worthless. That is §6.2.

### 5.4 Why now

**Tool access standardised, on the record.** MCP announced 2024-11-25 with a Postgres reference server; OpenAI March 2025; Google DeepMind and Microsoft mid-2025; AWS late 2025; donated to the Linux Foundation's Agentic AI Foundation December 2025 `[S62]`. Four named adopters, a neutral steward, inside eighteen months.

**Agentic tool-use became reliable enough to build and measure — not to trust unverified.** The horizon trend is real and dated: 50%-reliability task length doubling every ~7 months over six years, closer to every 4 months across 2024–2025 `[S6][S7]`. But DABstep puts multi-step data reasoning at ≈14.55–16% on hard tasks `[S4]` and τ-bench shows agents above 60% `pass^1` falling below 25% `pass^8` `[S5]`.

**That gap is the argument for the product, not against it.** If multi-hop execution were reliable, correctness could stay pre-encoded and nobody would need a trace.

### 5.5 Moat — none declared

With an open-source core the code is not the asset, and this memo does not claim a moat ([ASSUMPTIONS.md](../ASSUMPTIONS.md) A3). The strongest candidate is a **learned semantic layer** — the accumulated disambiguation of one organisation's schema, metric definitions and vocabulary. Copyable code, non-copyable semantics.

**The confirming evidence would be override rate falling per source as bindings accumulate, with no model change.** The data model captures it from day one ([tech/architecture/D04](../tech/architecture/D04_memory_schema.md)). It has not been observed, and until it is, this section stays empty.

## 6. Honest risks

### 6.1 Verification may not be cheaper than re-derivation — **this ends it**

The entire model rests on one untested claim. The beachhead's own words: *"Verifying your reasoning is not obviously faster than writing it myself. I read SQL faster than I read explanations."*

**That objection is correct as stated.** It is unmeasured anywhere in the literature ([research/survey.md](../research/survey.md) §8.1). If it holds, the plan gate and the verifier deliver an answer the analyst cannot use, and the arithmetic collapses to 1.0× regardless of how fast the answer arrived.

**Mitigation.** It is testable in one afternoon with five analysts and a timed task — same question, two conditions, minutes to a confident accept/reject. It is the first experiment in the validation layer, and it precedes further building rather than following it.

### 6.2 The planner may not be reliable enough on real schemas

≈14.55–16% on DABstep's Hard split against 76.39% Easy, over 450+ tasks from a real financial-analytics workload `[S4]`. This is the field's weakest measured capability and this product's core dependency.

**Mitigation, and its limit.** Typed plan DAGs, static validation, short plans with a hop-count ceiling, and per-hop verification. These are mitigations, not solutions — and [tech/deep_dives.md](../tech/deep_dives.md) labels the planner research risk rather than presenting it as solved. **The 295A spike measures it on a fixed question set and publishes the number**, which is more than any commercial competitor does.

### 6.3 The champion may capture the least value

Across one modelled day: the staff scientist goes from 2 hours to 19 minutes, the platform lead from 1.5 days to 8 minutes, the stakeholder from a three-day wait to 90 seconds — **while the analyst absorbs the review burden the other four shed** ([product/journeys/day_in_life.md](../product/journeys/day_in_life.md) §3).

Since the entire go-to-market routes through analyst advocacy, **a champion given work while everyone around them got leverage does not advocate.** This is a plausible mechanism for adoption stalling at exactly the person it cannot stall at.

**Mitigation.** Two things keep it viable and both are contingent: reviewing must be structurally cheaper than deriving (the same §6.1 claim), and the flywheel must reduce future review load. Analyst review-time-per-week is tracked as a first-class metric, with review-queue depth as its leading indicator.

### 6.4 What is not a risk, and should not be presented as one

**Competition is not the top risk.** The dominant risk is **segment reality** — whether enough real questions genuinely span sources, and whether any buyer can name a budget line this comes out of ([strategy/market_type.md](../strategy/market_type.md) §3). Both are answerable in ten conversations and neither requires a line of code.

## 7. What would change this memo

- **Analysts accept answers they did not derive, faster than re-deriving.** → §6.1 closes; the thesis is validated.
- **Fewer than a quarter of real requests span sources.** → §5.3's neutrality argument is true and worthless; SAM halves; the product should be rescoped.
- **No buyer can name a budget line.** → the market-type declaration is wrong and this is a feature, not a company.
- **The published multi-hop accuracy number lands near DABstep's Hard baseline.** → the architecture's mitigations do not work, and §6.2 is realised.

**Each is cheap to test and none has been tested.** A memo claiming otherwise at this stage would be the graveyard's next entry.
