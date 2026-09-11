# InsightPilot — Founder Brief

**What this is** — The single source of truth for every downstream artifact in this pack: who the user is, what the mechanism is, and which claims are settled versus open.
**Why it exists** — Generators fed a one-line idea produce generic slop. Concretely: without a fixed beachhead and vocabulary here, the PRD would write for "non-technical users," the market sizing would size all of BI, and the tech whitepaper would defend a different product than the one being built. This file prevents those three documents from describing three different companies.
**How to read it** — Read *Users & spectrum* and *Riskiest assumption* first; they constrain the most downstream work. A skeptic should attack *Wedge* and *Mechanism & moat*, which are the weakest sections by deliberate choice.
**Depends on / feeds** — Derived from `../../source/agentic-bi-project-writeup.pdf` plus three rounds of founder interrogation. Feeds every artifact in this pack. Open items are tracked in [ASSUMPTIONS.md](ASSUMPTIONS.md).

---

one-line: **Conversational BI for enterprise data analysts that turns a business question into a planned, executed and fully traceable analytical workflow, via a multi-agent orchestration layer.**

domain: business intelligence / data analytics tooling
stage: idea → design + spike (CMPE 295A), full build (CMPE 295B)

## Problem

Enterprise data analysts absorb a continuous queue of ad-hoc business questions. Each one costs the same manual sequence: locate the source, inspect the schema, write and debug the query, clean and join, choose a chart, interpret, and — when the question is predictive — build a model. The requester waits; the analyst context-switches away from planned work.

The pain is **latency and analyst attention**, not absence of tooling. This beachhead already owns a BI stack and can write SQL. What they cannot compress is the fixed per-question overhead, and what they cannot easily do at all is the modeling step.

Magnitude — queue length, median turnaround, cost per question — is **not quantified here** and must be sourced in phase 1 (`research/`). No number appears in this brief that lacks a source.

## Users & spectrum

One adaptive system, three edges. The interface adapts; there are no separate product tiers.

| Edge | Who | What they need | Why they constrain the design |
|---|---|---|---|
| **Low** | Business manager / requester | Plain-language answer, cannot judge correctness, never writes a query | Justifies the conversational interface. Without this edge, natural language is decorative for a SQL-fluent beachhead. |
| **Beachhead** | Enterprise data analyst | Compress per-question overhead; retain control and verifiability | The user the pack is written for |
| **High** | Staff data scientist | Audit lineage, override the ML agent's target and algorithm choices, extend the pipeline | Justifies traceability and override affordances as load-bearing, not cosmetic |

**User ≠ payer.** The analyst is the user and the champion; the economic buyer is the data/analytics function's budget owner. Monetization is modeled hypothetically only — see *Business model*.

## Why now

Two shifts, both inside roughly the last 18–24 months *(assumption: founder-asserted; the phase 1 survey must date and source both)*:

1. **Tool-use and replanning reliability crossed a usable threshold.** Multi-step agent loops previously compounded errors past the point where a chained fetch→analyze→model→visualize workflow could be trusted without a human validating each hop. The architecture was expressible before; it was not dependable.
2. **Tool access standardized.** MCP and mature agent frameworks turned connector integration into a configuration problem rather than bespoke engineering per source — which is precisely what makes a pluggable connector layer tractable for a small team.

## Wedge & 10-year vision

**Wedge — stated honestly:** all four agents are built together; **no single 10x claim is made.** This is a deliberate decision, not an oversight (see `ASSUMPTIONS.md` A2). The tradeoff was raised and accepted: the pack gains technical breadth appropriate to a two-semester capstone and forgoes a sharp defensible differentiator. Downstream artifacts must not manufacture a 10x claim to fill this gap.

**Not doing in year one:** arbitrary source federation, real-time or streaming data, write-back to source systems, a hosted multi-tenant service.

**10-year vision:** the analytical layer an organization asks rather than queries — where every answer carries its lineage, and the system's accumulated understanding of that organization's schema and metric definitions is the thing of value.

## Mechanism & moat

**Mechanism.** An Orchestrator interprets intent and produces an *analysis plan*, decomposing the question into tasks dispatched to four specialist agents — Data Fetch/Integration, Analytics, Visualization, ML — recombining their outputs into an *answer* carrying its *lineage*. Replanning occurs when an agent's result invalidates the plan.

**Data scope.** CSV/Excel upload, REST JSON APIs, and Postgres at the start. The connector layer sits behind interfaces so additional sources (Snowflake) plug in later if time permits.

**Moat — none declared.** With an open-source core, the code is not the asset. Candidate compounding loops, none yet evidenced:

1. **Learned semantic layer** — accumulated disambiguation of one organization's schema, metric definitions and vocabulary. Strongest candidate: copyable code, non-copyable semantics.
2. **Workflow lock-in** — saved investigations and lineage history raising migration cost.
3. **Connector ecosystem** — community-contributed integrations.

Evidence that would confirm (1): repeat users' answer-acceptance rate rising over time without model changes. Until then this section stays honest and empty.

## Competition & failed alternatives

**Deferred to phase 1 by decision.** Named for teardown: Power BI Copilot, Databricks Genie, ThoughtSpot, Snowflake Cortex Analyst, Tableau Pulse — plus the two alternatives that actually win most often, **the analyst writing SQL** and **doing nothing**. The teardown must establish failure mechanisms, not marketing gaps, and it — not this brief — determines the differentiator (`ASSUMPTIONS.md` A5).

## Business model

**Hypothetical only.** Monetization is out of scope for the academic project. The financials layer covers **cost-to-serve** and the **price threshold that would have to be true**, and excludes revenue projection, use of funds, and exit comparables (`ASSUMPTIONS.md` A1). Open source is decided; self-hosting is not (A4).

## Founder edge

Agent and LLM engineering — hands-on orchestration, tool-calling loops, and the failure modes of multi-step agent systems. This is the part of the build most teams underestimate, and it maps directly onto the riskiest assumption below.

The team claims no domain experience inside an enterprise analytics function. The problem statement is therefore **researched, not lived**, and phase 1 must source it rather than assert it.

## Riskiest assumption

> **Multi-agent planning is reliable enough end-to-end that error compounding across fetch → analyze → model → visualize does not make output untrustworthy.**

If false, nothing above matters: an analyst who must re-verify every answer has been given work, not leverage. This is well matched to the 295A spike, which tests it directly on one narrow path rather than deferring it to 295B.

## Vocabulary

The domain's own nouns. Every artifact in this pack uses these and not their generic equivalents.

| Term | Means |
|---|---|
| **investigation** | The unit of work: one business question pursued to a verified answer, including follow-ups |
| **analysis plan** | The Orchestrator's decomposition of a question into agent tasks |
| **handoff** | One agent passing structured output to another |
| **lineage** | The auditable trace: sources touched, queries run, transforms applied, methods chosen |
| **answer** | What the system returns — never "dashboard", never "report" |
| **core loop** | question → plan → execute → answer + lineage → follow-up |
| **unit of value** | One resolved business question with verifiable lineage |
| **outcome metric** | **Time-to-verified-answer** — wall-clock from question asked to an answer the analyst will stake their name on |
