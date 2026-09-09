# Landscape

**What this is** — Every serious approach to "turn a business question into a trustworthy analytical answer," ordered from nearest to farthest from the mechanism in [BRIEF.md](../BRIEF.md): warehouse-native assistants, then BI-embedded copilots, then agentic notebooks, then open-source stacks, then research systems, then the manual and dead options.
**Why it exists** — Without this file the pack asserts a novel mechanism into a space that has been attempted continuously since 2010 and has a real graveyard. The specific failure it prevents: the tech whitepaper claiming Orchestrator-plus-four-agents is new, when the *decomposition* is not new — what is thin is multi-hop execution across heterogeneous sources with an auditable trace. Getting that distinction wrong makes every downstream claim rebuttable by a single reviewer who has used Databricks Genie.
**How to read it** — §1 and §7 carry the argument; the middle sections are evidence. A skeptic should attack §7's white-space claim and §6's reading of the graveyard, which is assembled from acquisition records rather than founder accounts.
**Depends on / feeds** — Inherits the mechanism and vocabulary from [BRIEF.md](../BRIEF.md); cites through [sources.md](sources.md). Feeds [competitors.md](competitors.md) (which turns §2–§4 into a teardown and closes ASSUMPTIONS A6), [capability_table.md](capability_table.md), and phase 2 positioning.

---

## 1. The organising question

The brief's core loop is **question → plan → execute → answer + lineage → follow-up**, spanning fetch, analyze, model and visualize. Almost every system below implements some contiguous slice of that loop. The useful axis is therefore not "does it use AI" but **how many hops of the loop it executes autonomously, and what it hands back with the answer**.

Two structural facts govern the whole landscape and are worth stating before the entries.

**Fact one: the field converged on the semantic layer as the correctness mechanism.** Snowflake requires a hand-authored YAML semantic model `[S36]`; Databricks requires a curated Genie space `[S33]`; Power BI Copilot can only reference measures and columns that already exist in the model `[S42]`; Tableau Pulse operates on pre-defined metric definitions `[S48]`; Wren AI's differentiator is its MDL modelling layer `[S50][S51]`. Independent survey evidence confirms this is a budgeted enterprise priority, not vendor positioning: 59% of decision-makers at organisations above $100M revenue are directing incremental budget to semantic layers, and 24.9% name accuracy and hallucination risk as their single top reservation about GenAI in analytics `[S17]`. The mechanism argument behind the convergence is sound — schema-level errors, meaning wrong column selection and semantic misinterpretation, account for **81.2% of 4,602 analysed incorrect text-to-SQL queries** `[S2]`.

**Fact two: the convergence relocates the cost rather than removing it.** A semantic model is hand-authored and hand-maintained, and Snowflake's is capped at roughly 1 MB, about 32K tokens `[S36]`. Reverse-engineering an existing estate's relationships, metrics and business vocabulary into one is weeks-to-months of work. So the incumbent answer to "why is this correct" is "because a human pre-encoded the correctness, offline, per source." That is a real answer. It is also precisely the fixed overhead the brief says the analyst cannot compress — moved from per-question to per-source, which helps enormously at high query volume against a stable schema and helps not at all for a novel question against a source nobody has modelled yet.

Everything below should be read against those two facts.

## 2. Warehouse-native assistants — nearest neighbours

These sit closest to the brief because they own the data and the compute, and because they are what an enterprise analyst is most likely already licensed for.

### 2.1 Databricks AI/BI Genie

**What it is.** A conversational interface over a curated Genie *space*: a scoped set of tables plus natural-language instructions and example queries supplied by a data team `[S33]`.

**Maps onto the core loop.** question → plan (implicit, single-hop) → execute SQL → chart. No modelling step. Lineage is the generated SQL, which is shown.

**Mechanism.** Retrieval over the space's curated metadata, SQL generation, execution on the lakehouse. In 2026 Databricks added **Inspect** (Beta), which is the most interesting development in this section: Genie re-reads its own generated SQL, authors *smaller SQL statements to verify specific aspects of the query*, and regenerates if verification fails `[S32]`. This is self-verification by decomposition — the same insight the brief's replanning loop rests on, shipped by the incumbent.

**Strengths.** Governance, lineage and compute are inherited from Unity Catalog rather than rebuilt. Zero data movement.

**Measured limits.** The Genie Agent table limit was raised from 25 to 30 in 2026 `[S32]` — a hard scoping ceiling, and a revealing one: the product's reliability strategy is to keep the schema small. Quality is a direct function of space curation; where the underlying lakehouse is not well maintained, users get "confident-sounding answers they cannot fully trust" `[S35]`, and enterprise outcomes are described as depending on connector quality and ontology accuracy at messy-enterprise scale `[S34]`. Databricks publishes no execution-accuracy figure on any public benchmark (sources.md, *Named gaps* 2).

**Gap it leaves.** Single warehouse, single hop, no predictive step, and a table ceiling that excludes exactly the wide-schema case where text-to-SQL is measured at 30–36% accuracy `[S2]`.

### 2.2 Snowflake Cortex Analyst

**What it is.** A text-to-SQL API over a hand-authored YAML semantic model, with runtime selection among several underlying models `[S36]`.

**Maps onto the core loop.** question → execute SQL → tabular result. Planning, charting and modelling are the caller's problem; Cortex Analyst is deliberately a component, not an application.

**Mechanism.** The semantic model carries table and column descriptions, synonyms, verified queries and metric definitions; generation is constrained to it.

**Strengths.** The cleanest expression of the semantic-layer thesis, and the clearest pricing in the category: billed per 1,000 messages through the standalone API, on successful responses only, at a fixed cost regardless of token count `[S37][S38]`. That pricing shape matters for the brief's cost model — it prices the *question*, which is exactly the brief's unit of value, rather than the tokens.

**Measured limits.** The semantic model is hand-authored, hand-maintained YAML capped near 1 MB / 32K tokens `[S36]`. Since 2026-04-01 AI is metered on a separate AI Credit at $2.00–$2.20 `[S39]`, and executing the generated SQL bills warehouse compute on top `[S37]` — so a question has at least two cost components.

**Gap it leaves.** Snowflake-only. No orchestration, no modelling, no visualization, no follow-up. It is a fetch agent with a good semantic contract — which is a reasonable read of what the brief's Data Fetch agent should aspire to interoperate with rather than beat.

### 2.3 Microsoft Power BI Copilot

**What it is.** The consolidation target for all natural-language querying in Power BI, replacing Q&A `[S40]`.

**Maps onto the core loop.** question → visual or summary over an existing semantic model. Bounded to what the model already contains.

**Measured limits.** Documented and unusually specific. It cannot compute a metric that does not already exist as a measure or column `[S42]` — the single sharpest constraint in this section, because a genuinely ad-hoc question is by definition one nobody has pre-modelled. It requires dedicated rather than shared capacity `[S42]`. It does not support real-time streaming models, live Analysis Services connections, or models with implicit measures disabled `[S43]`. It is weak at reconciliation-style reasoning — validation and sanity-checking across reports `[S42]` — which is a large fraction of what an analyst actually does before staking their name on a number. Microsoft's own documentation warns it can fabricate data and misinterpret business logic `[S42]`.

**Gap it leaves.** Answers only questions someone already anticipated well enough to model.

### 2.4 Tableau Pulse

**What it is.** Metric monitoring with natural-language explanation, delivered to Slack, email and mobile; the metric definition is the unit `[S48]`.

**Maps onto the core loop.** Inverts it. Pulse pushes changes in subscribed metrics rather than answering asked questions — the *investigation* never starts with a question.

**Measured limits.** Works on single-number metrics with clear dimensions; composite metrics and anything requiring multi-step reasoning — cohort retention curves, attribution-weighted contribution — work poorly. Tuned to the dashboard scorecard layer rather than analyst deep-dive. Tableau Cloud only `[S49]`.

**Gap it leaves.** The entire multi-step class, stated by a competitor but consistent with the metric-centric mechanism.

### 2.5 Amazon Quick (formerly QuickSight Q, then Amazon Q in QuickSight)

Included for one reason: the rename chain is itself evidence. QuickSight Q launched in 2021, became Amazon Q in QuickSight, became Amazon Quick Suite in October 2025, became Amazon Quick in 2026; Amazon Q Business closed to new customers on 2026-07-31 `[S55]`. Four repositionings in five years is a product that has not found its shape. **Gap it leaves:** for this pack, none technically — it is a data point about category instability, not a competitor with a distinguishable mechanism.

## 3. Search- and agent-first BI platforms

### 3.1 ThoughtSpot (and Spotter)

**What it is.** The company that made search-first analytics a category, now shipping the Spotter agent.

**Traction signal — the most important single data point in this file.** ThoughtSpot raised at a $4.2B valuation in a Series F in November 2021. In June 2024 a secondary transaction cleared at $6.80 per share against the $25.83 Series F price — a **73.67% markdown**, implying roughly $920M `[S46]`. Third-party estimates put 2024 ARR near $150M against $210.6M for 2023 `[S47]`, though that estimate is low-confidence.

**Why it matters here.** ThoughtSpot is the purest test the market has run of "let non-analysts ask questions of enterprise data in natural language." It was well funded, technically credible, and early. The markdown is the strongest available evidence that the *low-edge* thesis — business users self-serving via natural language — has not paid off at the scale investors priced. This does not invalidate the brief's low edge, which is deliberately not the beachhead (BRIEF.md, *Users & spectrum*), but any downstream artifact that leans on "business users will just ask" must confront this number.

**Pricing.** Essentials $25/user/month, Pro $50/user/month, Enterprise custom and averaging roughly $137,000/year `[S44][S45]`. On Pro the **Spotter agent is capped at 25 queries per user per month**, with overage billed `[S44]`. A 25-question monthly cap is not the pricing of a tool anyone expects to sit in the analyst's core loop; it is the pricing of an occasional-use feature, and it says something about either inference cost or confidence in per-query value.

### 3.2 Tellius, AnswerRocket, Zenlytic

Independent AI-analytics vendors. Tellius has raised approximately $36.1M total `[S61]` — an order of magnitude below the platform incumbents it must sell against. None publishes pricing; all are sales-qualified (sources.md, *Named gaps* 4). **Gap they leave:** they compete on the same single-hop natural-language-to-answer mechanism without owning the warehouse, which is a structurally hard place to stand.

## 4. Agentic notebooks — the analyst-native alternative

This section matters more than its size suggests, because it is where the brief's actual beachhead — the SQL-fluent enterprise analyst — is most likely to go instead.

### 4.1 Hex Notebook Agent

**What it is.** An agent operating inside a SQL-plus-Python notebook with live database connections `[S54]`.

**Maps onto the core loop.** Covers fetch, analyze, model and visualize — the full span the brief claims — but with the human driving cell by cell rather than an Orchestrator planning end to end.

**Mechanism.** The notebook *is* the lineage. Every hop is a cell: visible, editable, re-runnable, diffable. This is the most important observation in this file for the brief's traceability claim — **Hex already solves auditability, structurally, by not hiding the steps**. Any lineage claim the brief makes must be better than "we show you a notebook," and "we show you a notebook" is a high bar.

**Pricing.** From $36 per editor per month, with credit allocations by seat tier and roughly $750/month for a ten-analyst team at the $75 Team seat `[S52]`.

**Gap it leaves.** The analyst still directs. There is no plan produced up front, no automatic replanning when a result invalidates an assumption, and no dispatch across specialist agents. The unit of work is a notebook, not an *investigation* pursued to a verified answer.

### 4.2 Julius AI

Chat-based analysis over uploaded CSV or Excel: upload, ask, get charts and an explanation. Free at 15 messages/month, Plus $35/month, Pro $45/month, Max $200/month, Team $50/user/month `[S53]`. **Gap it leaves.** File-scoped and single-user; no enterprise source connectivity, governance or lineage. Relevant only because the brief's day-one data scope includes CSV/Excel upload — meaning the brief's *weakest* entry point is a solved, cheap, commodity experience. Downstream artifacts must not lead with file upload as a differentiator.

## 5. Open-source stacks and the semantic-layer suppliers

### 5.1 Wren AI

The reference point for the brief's own open-source decision. Open-sourced April 2024; over 13,000 GitHub stars and more than 10,000 cloud users reported by end-2025 `[S50]`. Its architecture is a RAG pipeline anchored by a semantic engine and its own modelling language, MDL, rather than raw schema retrieval `[S51]`; connectors include BigQuery, DuckDB and PostgreSQL `[S50]` — an overlapping but not identical connector set to the brief's CSV/Excel, REST JSON and Postgres.

**Why this entry is uncomfortable and should stay that way.** Wren AI is open source, agentic, semantic-layer-based, multi-warehouse, two years ahead, and has a real community. It is the closest thing in this landscape to the brief's product, and it occupies the same open-source-core position the brief has already committed to (BRIEF.md, *Business model*). The honest difference is scope of the loop — Wren AI is text-to-SQL-plus-charts, with no ML agent and no cross-source replanning — not novelty of approach. Phase 2 positioning must say this out loud rather than let a reviewer discover it.

### 5.2 The semantic-layer market as suppliers, not competitors

dbt Semantic Layer, Cube, AtScale and Honeydew as pure semantic layers; Snowflake Semantic Views and Databricks Metric Views as warehouse-native; LookML, GoodData and MicroStrategy ONE as BI-native `[S66]`. The argument this camp makes is precisely the determinism argument: a human analyst can ask a colleague what "active customer" means, and an agent cannot — so the definition must live somewhere the agent can query or inspect `[S65]`.

**Why this is the most actionable entry in the file.** These are the natural *integration surface* for the brief's Data Fetch/Integration agent, not rivals. A system that can consume an existing dbt or Cube semantic layer inherits the correctness work an organisation already paid for, instead of demanding it be redone. The counter-position is worth holding in view: the data model may already be the semantic layer, and benchmark schemas systematically understate the modelling work a real deployment needs `[S67]`.

## 6. The graveyard — what has already been tried and ended

Post-mortems are required rather than optional here, and the honest caveat comes first: **no founder-written post-mortem of a failed natural-language-BI company was located** (sources.md, *Named gaps* 3). What follows is assembled from acquisition records and retirement notices, which establish *that* attempts ended and only sometimes suggest why.

| Attempt | Era | What it tried | Outcome | The mechanism lesson |
|---|---|---|---|---|
| **IBM Watson Analytics** | 2014–2019 | Natural-language question answering over uploaded business data; the flagship of its generation | Discontinued June 2019, capability folded into Cognos Analytics 11.1 "Exploration" `[S59]`. The wider Watson line sold Watson Health to Francisco Partners for roughly $1B after roughly $5B invested `[S60]` | The canonical overpromise case. The capability demoed well and did not survive contact with real schemas and real users. Directly relevant: the brief's riskiest assumption is the modern form of the same question |
| **Narrative Science** | 2010–2021 | Natural-language *generation* — narrating what a chart shows | Acquired by Salesforce December 2021, folded into Tableau; terms undisclosed `[S58]` | Narration is a feature, not a company. It was absorbed by the platform that owned the data. Any part of the brief that is *explanation of a result* is on this path |
| **Power BI Q&A** | 2015–2026 | Natural-language querying via a curated linguistic schema — synonyms, relationships, "teach Q&A" `[S41]` | Fully retired by end of December 2026; existing Q&A visuals stop working `[S40]` | The most instructive entry. Q&A did not fail from lack of distribution — it shipped inside the most widely deployed BI tool on earth. It failed because the curation burden it placed on modellers exceeded the value returned, and Microsoft replaced it with an LLM approach that inherits the same dependency on a well-prepared model `[S42]` |
| **Sisu Data** | 2018–2023 | Diagnostic decomposition: automatically explaining *why* a metric moved | Raised approximately $128.7M `[S56]`; acquired by Snowflake 2023-10-16; standalone product discontinued and in wind-down as of mid-2026 `[S57]` | The single most cautionary entry for this pack. Sisu attacked the *diagnostic* question — the highest-value part of the loop, and one ASSUMPTIONS A2 names as a defensible 10x candidate the founder declined. Well funded, technically respected, and still ended as a warehouse feature. The lesson is about gravity: standalone analytical intelligence gets absorbed by whoever owns the data |
| **SeekWell** | — | SQL-to-operational-tools automation | Shut down 2026-07-31 `[S57]` | Adjacent, low confidence, recorded for completeness |

**The pattern across all five.** None died of bad technology. Watson and Q&A died of the curation-to-value ratio; Narrative Science and Sisu died of gravity — absorbed by the platform holding the data. Both failure modes apply to this brief. The curation risk is answered by consuming existing semantic layers rather than demanding new ones (§5.2). The gravity risk is not answered anywhere in phase 0, and phase 2 positioning must confront it: **why does this not end as a feature of Databricks or Snowflake?** The only structural answer visible from this research is cross-source neutrality — being the layer that spans Postgres, files and APIs precisely because it belongs to no warehouse — which is exactly what the brief's connector-layer design implies but does not yet claim.

## 7. Where the white space actually is

Ranked by how defensible each gap is, most defensible first. This is the input phase 2 consumes; the differentiator itself is settled in [competitors.md](competitors.md) §4, which closes ASSUMPTIONS A6.

1. **Multi-hop execution across heterogeneous sources.** Every system in §2 is single-warehouse and effectively single-hop. Genie's Inspect decomposes for *verification* within one query `[S32]`; nothing decomposes a question into a *plan* that spans a Postgres table, an uploaded file and a REST API. This is the brief's actual mechanism and the clearest structural gap. Note the cost: DABstep measures the best agents at roughly 14.55–16% on its Hard split against 76.39% Easy `[S4]`, so the gap exists because multi-step data reasoning is genuinely hard, not because nobody thought of it.
2. **The predictive step.** Not one product in §2–§4 will build a model as part of answering a question. MLE-bench-class agents reach a 36.4% medal rate under a 12-hour budget `[S9]` — real capability, unshipped in BI. This is the widest capability-to-product gap in the landscape and, per ASSUMPTIONS A2, the 10x candidate the founder knowingly declined to lead with.
3. **Hop-level lineage as the unit of output.** Incumbents show the generated SQL; Hex shows the notebook `[S54]`. Nobody ships an *investigation* whose every handoff is separately inspectable and re-runnable. Given that 71% of practitioners name incorrect or hallucinated outputs reaching stakeholders as a top concern `[S16]` and 24.9% name accuracy and hallucination as their top GenAI reservation `[S17]`, this is where demand and gap coincide most sharply.
4. **Consuming an existing semantic layer instead of demanding a new one.** Every incumbent requires its own curated artifact — Genie space, Cortex YAML, Power BI model, Pulse metric. A system that reads dbt or Cube definitions inherits work already paid for `[S66]`. This is an integration decision, not an invention, which is exactly why it is achievable inside a capstone.
5. **Question-priced economics.** Cortex Analyst prices per message `[S37][S38]`; ThoughtSpot caps Spotter at 25 queries per user per month `[S44]`. Both price the question, matching the brief's stated unit of value. Weakest of the five — a pricing observation, not a technical gap — but it belongs in the financials layer.

## Recommended next 3

1. **Run the teardown against failure mechanisms and settle A6 from gap 1 plus gap 3, not gap 2.** Multi-hop-plus-auditable-trace is defensible on this evidence; leading with the ML agent contradicts the accepted A2 decision and invites the "why not just AutoML" question the pack cannot yet answer. → [competitors.md](competitors.md).
2. **Make phase 2 answer the gravity question explicitly.** Sisu and Narrative Science both ended inside the platform that owned the data `[S56][S58]`. Cross-source neutrality is the only structural answer this research supports, and it is currently implied by the connector layer rather than claimed. → `strategy/positioning.md`, jointly with ASSUMPTIONS A5 on self-hosting.
3. **Treat Wren AI as the named baseline in every downstream comparison.** It is the nearest neighbour, it is open source, and it is two years ahead `[S50]`. A pack that never names it reads as unaware; a pack that names it and states the scope difference reads as informed. → [competitors.md](competitors.md) and `tech/` whitepaper.
