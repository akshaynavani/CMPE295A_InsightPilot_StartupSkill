# Product requirements document — Agentic BI

**Version 0.1 · 2026-09-08 · status: draft for CMPE 295A**

**What this is** — The product definition: the closed core loop, the ten domain principles every feature must map to, the feature superset organised by loop phase, the learning flywheel, the safety and privacy requirements, and the success metrics.
**Why it exists** — The pack now has a differentiator (lineage that makes verification cheap) and a positioning that concedes the bundling advantage permanently. This file is where those become buildable, and where the things that must *not* be built are written down. The specific failure it prevents: a 295A/295B scope that drifts toward automating fetch→analyze→visualize — the crowded, table-stakes part of the loop that Genie, Cortex, Copilot and Hex all already do — because that work is legible and the verification work is not.
**How to read it** — §3 (principles) is the credibility engine; §2 (non-goals) is the part most likely to be quietly violated later. A skeptic should attack §3's claim that every feature maps to a principle, and §7's outcome metric, which measures something no competitor reports.
**Depends on / feeds** — Inherits the mechanism and vocabulary from [BRIEF.md](../BRIEF.md), the principles' evidence from [research/survey.md](../research/survey.md), the personas from [strategy/personas.md](../strategy/personas.md), and the ranked value mappings from [strategy/value_prop_canvas.md](../strategy/value_prop_canvas.md) §5. Feeds [features_flagship.md](features_flagship.md), [features_prioritized.md](features_prioritized.md), the four [journeys](journeys/), [ux_spec.md](ux_spec.md), and the whole `tech/` layer.

---

## 1. Executive summary and vision

### 1.1 The closed core loop

Named in the domain's own verbs. BRIEF.md states the loop as *question → plan → execute → answer + lineage → follow-up*; phase 2 made one beat explicit that was previously folded inside "answer + lineage."

> **ASK → PLAN → EXECUTE → ANSWER → VERIFY → FOLLOW UP**

| Beat | What happens | Component |
|---|---|---|
| **Ask** | A business question arrives in natural language, in context of the *investigation* it belongs to | Investigation surface |
| **Plan** | The Orchestrator decomposes intent into an **analysis plan** — an ordered set of agent tasks over named sources | Orchestrator |
| **Execute** | Specialist agents run their tasks; each **handoff** emits structured output plus its own lineage | Fetch / Analytics / Visualization / ML agents |
| **Answer** | Outputs recombine into an **answer** — never a "dashboard," never a "report" | Orchestrator |
| **Verify** | The analyst inspects the hop they doubt, re-runs it, overrides it, or accepts | Lineage surface |
| **Follow up** | The next question inherits the investigation's context and its established facts | Investigation surface |

**Why VERIFY is a named beat and not an afterthought.** It is the beat that distinguishes this product from every system in [research/landscape.md](../research/landscape.md). Incumbents end at *Answer* and hand the user the SQL. If verification is not a designed beat with its own surface, its own latency budget and its own metric, it becomes the analyst's unpaid work — which is the state they are already in.

### 1.2 Vision

The analytical layer an organisation asks rather than queries, where every answer carries its lineage. The ten-year asset is not the code — it is the accumulated understanding of *this* organisation's schema, metric definitions and vocabulary (ASSUMPTIONS A3: candidate, unevidenced, not claimed as a moat).

### 1.3 What this is, in one sentence

For the enterprise data analyst, the only conversational analytics layer that answers a question spanning their real sources and hands back an investigation they can verify hop by hop.

## 2. Goals and non-goals

### 2.1 Goals

| # | Goal | Measured by |
|---|---|---|
| G1 | An analyst reaches a **verified** answer to a multi-source ad-hoc question faster than they could derive it | Time-to-verified-answer (§7.1) |
| G2 | Verification of an answer costs materially less than re-derivation | Verification cost ratio (§7.1) |
| G3 | The system attempts questions that require no pre-authored semantic artifact | Share of investigations against unmodelled sources |
| G4 | Every answer is reproducible from its lineage by a second person | Re-run success rate |
| G5 | The system publishes its own multi-hop accuracy on a fixed question set | The number exists and is public |

### 2.2 Non-goals — real renunciations

Each of these is something a reasonable person would expect this product to do, and it will not.

1. **Not a self-service tool for non-technical users.** Business stakeholders consume answers; they do not originate unsupervised ones. An answer reaching a slide passes through an analyst. **This renounces the largest revenue segment in the category** — and it is the bet ThoughtSpot made and was marked down 73.67% on `[S46]`. See [strategy/personas.md](../strategy/personas.md) §3.
2. **Not a semantic layer, and not a replacement for one.** The product *consumes* dbt/Cube definitions where they exist `[S66]`. It will not become the place metric definitions live. Building one would pick a fight with the buyer's existing, funded decision `[S17]`.
3. **Does not improve data quality, and will produce beautifully traceable wrong answers over bad data.** 77% of organisations report data-quality issues and 91% say those issues affect performance `[S15]`. Lineage makes a bad answer *legible*, not correct. Stated as a non-goal because the alternative is letting a buyer assume otherwise.
4. **No write-back to source systems.** Read-only, permanently in scope terms. This is also what makes Tom's security review survivable ([strategy/sales_roadmap.md](../strategy/sales_roadmap.md) §4 step 5).
5. **No autonomous action on an answer.** No alerts that trigger workflows, no decisions executed. The system produces answers; humans act.
6. **No real-time or streaming data.** Batch and request/response only.
7. **No arbitrary source federation in year one.** CSV/Excel, REST JSON, Postgres. Snowflake if time permits.
8. **Not a hosted multi-tenant service.** Open-core, self-hostable, running in the customer's environment against their own model key (ASSUMPTIONS A5).
9. **No claim to beat incumbents on single-source single-hop accuracy.** No commercial agentic-BI product publishes a benchmark ([research/sources.md](../research/sources.md), *Named gaps* 2), so no comparative claim is supportable (A6 constraint 4). On Genie's home turf — one curated lakehouse, ≤30 tables — Genie is expected to win.
10. **No 10x claim.** ASSUMPTIONS A2. The four agents are integrated breadth, knowingly chosen over a single sharp differentiator.

## 3. First-principles grounding — non-negotiable

**Rule: every major feature must map to one or more of these principles. A feature mapping to none is cut, or the principle list was wrong.** Each principle is an empirical finding from [research/survey.md](../research/survey.md), not a design preference.

| # | Principle | Evidence | Design consequence |
|---|---|---|---|
| **P1** | **Schema grounding dominates language understanding.** The hard problem was never parsing English | Schema-level errors — wrong column, semantic misinterpretation — are **81.2% of 4,602 analysed failures** `[S2]` | Spend engineering on schema/semantic grounding and disambiguation, not on conversational polish |
| **P2** | **Error compounds multiplicatively across hops.** Capability and reliability trade against each other | 95% per hop → ≈74% over six hops; 90% → ≈53% `[S13]`. Error propagation is the primary agent bottleneck `[S10]` | Keep plans short. Verify per hop. Replan on invalidation. Never add a hop for elegance |
| **P3** | **Failure is plausible, not obvious.** A wrong answer looks like a right one | *"Failure looks like a plausible but incorrect answer"* `[S2]` | The system must surface *doubt*, not confidence. No confidence scores presented as accuracy |
| **P4** | **Consistency degrades faster than capability.** The same question twice may not give the same answer | `pass^k = p^k`; >60% `pass^1` falls to <25% `pass^8` `[S5]` | Determinism where achievable: cache plans, pin resolved column mappings, make re-runs reproduce |
| **P5** | **Verification cost is the adoption gate**, not answer accuracy | 71% fear hallucinated output reaching stakeholders `[S16]`; 24.9% name accuracy as their top GenAI reservation `[S17]` | Design for cheap checking rather than for autonomy. Optimise the *Verify* beat |
| **P6** | **Pre-encoded correctness narrows the answerable question set.** The tighter the guardrail, the fewer questions attempted | 30 tables per Genie Agent `[S32]`; ~32K-token Cortex YAML `[S36]`; existing-measures-only Copilot `[S42]` | **Consume a semantic layer when present; never require one.** This is the product's core structural bet |
| **P7** | **Verification by decomposition beats verification by assertion** | Genie's *Inspect* authors smaller SQL statements to verify aspects of a query and regenerates `[S32]` — an incumbent arriving at the same insight independently | Check a hop by running a cheaper, different query against it, not by asking the model whether it is confident |
| **P8** | **Tool access is standardised; semantics are not** | MCP shipped 2024-11-25 and was adopted by OpenAI, Google, Microsoft and AWS within thirteen months `[S62]`; it standardises access, not meaning `[S65]` | Connectors are configuration. The real work is mapping an organisation's vocabulary onto its schema |
| **P9** | **Automated modelling exists, but not at conversational latency** | MLE-bench-class agents reach 36.4% medal rate under a **12-hour budget** `[S9]` | The ML agent is **time-boxed in minutes** and states what it did not have time to try. Never promise MLE-bench behaviour |
| **P10** | **Multi-step data reasoning is the field's weakest measured capability** — and this product's core dependency | ≈14.55–16% on DABstep's Hard split vs 76.39% Easy `[S4]` | Build the evaluation harness *first*. Scope the spike to one narrow path. Assume failure is the common case and make it cheap |

**The honest reading of P2 + P5 + P10 together:** this product cannot promise reliable autonomous answers, because the field cannot deliver them. It can promise that when the system is wrong, the analyst finds out in seconds rather than after the number reaches a slide. That is the whole design.

## 4. Target users

Full spectrum, **one adaptive system, no separate tiers.** The interface adapts to what the person can verify; it does not fork into a "business edition." Detail in [strategy/personas.md](../strategy/personas.md).

| Edge | Persona | What the system does differently | Why they constrain the design |
|---|---|---|---|
| **Low** | Marcus, regional sales director | Plain-language answer; lineage collapsed but present; **an explicit "not yet reviewed by an analyst" state** | Justifies the conversational interface. Also the reason for non-goal 1 — the system must make his answer *reviewable*, not make him self-sufficient |
| **Beachhead** | Priya, senior data analyst | Full plan visible before execution; hop-level trace; override at any hop | The user this product is for |
| **High** | Dr. Chen, staff data scientist | Method-level lineage — target definition, split, algorithms tried and rejected; override of the ML agent's choices | Makes traceability load-bearing rather than cosmetic |
| **Buyer** | Angela, VP Data & Analytics | Provenance queryable across investigations; adoption observable | Payer ≠ user. Her requirement is retention and queryability of lineage |
| **Blocker** | Tom, data platform lead | Self-hosted deployment; credentials never leave the boundary; readable audit log of every query issued | Can veto without ever using the product |

**ASSUMPTIONS A7 warning.** This spectrum was derived, not founder-supplied, and is flagged `kills-pack-if-wrong: yes`. This PRD, the UX spec and all four journeys are written against it together.

## 5. Core feature set — superset by loop phase

Each feature carries its principle mapping. Full ranking in [features_prioritized.md](features_prioritized.md); the top 20 are detailed in [features_flagship.md](features_flagship.md).

### ASK

| Feature | Principle |
|---|---|
| Investigation thread — question, follow-ups and established facts as one durable unit | P5 |
| Ambiguity interception: the system asks before guessing when a term resolves to more than one column or grain | **P1**, P3 |
| Vocabulary binding — organisation terms resolved to schema, shown and correctable | **P1**, P8 |
| Source scoping — the analyst names or confirms which sources are in play | P2, P6 |

### PLAN

| Feature | Principle |
|---|---|
| **Analysis plan shown before execution**, editable and approvable | P2, P3, **P5** |
| Plan-length discipline: the Orchestrator states hop count and flags long plans | **P2** |
| Plan caching — the same question reuses its resolved plan | **P4** |
| Cost and latency preview per plan | P9 |

### EXECUTE

| Feature | Principle |
|---|---|
| Data Fetch/Integration agent — CSV/Excel, REST JSON, Postgres | P8 |
| **Semantic layer consumption** — reads existing dbt/Cube definitions when present | **P6**, P1 |
| Analytics agent — joins, aggregation, comparison, decomposition of a metric movement | P1 |
| Visualization agent — chart selection justified by data shape | P3 |
| **ML agent, time-boxed in minutes**, reporting what it did not have time to try | **P9** |
| Per-hop verification: a cheaper, structurally different query checks each hop's result | **P7**, P2 |
| Replanning on invalidation | **P2** |

### ANSWER

| Feature | Principle |
|---|---|
| Answer with its established facts, not a chart alone | P3 |
| **Doubt surfacing** — the system names which hops it is least sure of and why | **P3**, P5 |
| No confidence percentages presented as accuracy | **P3** |

### VERIFY

| Feature | Principle |
|---|---|
| **Hop-level lineage** — sources touched, query run, transform applied, method chosen | **P5** |
| Re-run any single hop in isolation | **P4**, P7 |
| Override a hop and let the plan re-flow downstream | P2, P5 |
| **Exportable self-contained investigation artifact** | **P5** |
| Sign-off state — an investigation is marked reviewed, by whom, when | P5 |

### FOLLOW UP

| Feature | Principle |
|---|---|
| Context inheritance — the next question keeps resolved bindings and established facts | P1, P4 |
| Investigation history, searchable by question and by source touched | P5 |

## 6. Data and learning flywheel

**What the system remembers, per organisation:**

1. **Resolved vocabulary bindings** — "cost per shipment" → this expression over these tables, confirmed by this analyst on this date.
2. **Corrected joins and grains** — every override an analyst makes on a hop.
3. **Verified investigations** — questions that reached sign-off, with their plans.
4. **Rejected plans** — what the Orchestrator proposed that a human threw away, which is the higher-signal half.

**How it compounds.** Each correction narrows the schema-grounding problem that causes 81.2% of failures `[S2]`. A second analyst asking a related question inherits the first analyst's confirmed bindings, so the marginal question against a given source gets cheaper to verify — not because the model improved, but because the organisation's semantics accumulated.

**The honest limit, and why ASSUMPTIONS A3 declines to call this a moat.** This is the *learned semantic layer* candidate, and it is **unevidenced**. The confirming observation would be repeat users' answer-acceptance rate rising over time with no model change — which requires a real deployment over months. Until then it is a design intention, and no artifact may present it as an achieved advantage.

**Privacy constraint on the flywheel.** Learning is per-organisation and stays inside the customer's deployment. Nothing crosses tenancy boundaries — which is automatic under the self-hosted model (A5) and must remain true if a managed option is ever added.

## 7. Success metrics

### 7.1 Outcome metrics — the domain's real "did it work"

| # | Metric | Definition | Why it is first |
|---|---|---|---|
| **O1** | **Time-to-verified-answer** | Wall-clock from question asked to an answer the analyst will stake their name on | The brief's outcome metric. Contains both halves — speed and trust — and cannot be gamed by answering fast and wrong |
| **O2** | **Verification cost ratio** | Minutes to accept/reject an answer ÷ minutes to derive it from scratch | **The differentiator, expressed as a number.** Target < 0.5. Priya's objection says it may exceed 1.0, and that has not been tested |
| **O3** | **Multi-hop execution accuracy** on a fixed question set | Standard execution-accuracy measurement, published | No commercial competitor publishes one. Baseline to beat: DABstep Hard ≈14.55–16% `[S4]` |
| **O4** | **Silent-error rate** | Wrong answers accepted by an analyst without the trace catching them | **The metric that matters most and is hardest to measure.** Requires seeded-error testing, because P3 says failure looks plausible |

### 7.2 Engagement metrics

| # | Metric | Threshold |
|---|---|---|
| E1 | Clone → first successful investigation, median | **< 30 minutes** — [strategy/business_model_canvas.md](../strategy/business_model_canvas.md) row 4; below this the sole viable channel fails |
| E2 | Investigations per analyst per week | Directional only |
| E3 | **Hop-inspection rate** — share of investigations where the analyst opened at least one hop | If near zero, the trace is decoration. If near 100%, the answers are not trusted. Both extremes are failures |
| E4 | Override rate, and its trend over time | Should *fall* per source as the flywheel accumulates (§6) |
| E5 | Export/share events | The GTM loop's edge ([strategy/gtm.md](../strategy/gtm.md) §3) |

### 7.3 Business metrics

Reported for completeness; monetisation is out of scope per ASSUMPTIONS A1, and these carry no targets.

| # | Metric |
|---|---|
| B1 | Cost-to-serve per investigation — inference across agents, hops and retries. Anchor: Cortex Analyst at ≈$0.134 per message `[S38][S39]` |
| B2 | Analyst seats active per deployment (drives the account-size question in [strategy/channel_plan.md](../strategy/channel_plan.md) §4) |
| B3 | Self-hosted deployments reaching a second analyst — the internal-referral conversion |

## 8. Oversight, safety, privacy, compliance

| Requirement | Rationale |
|---|---|
| **Read-only access to all sources.** No write-back, no DDL | Non-goal 4; the precondition for Tom's approval |
| **Credentials never leave the customer boundary**; the orchestration layer runs in their environment against their own model key | ASSUMPTIONS A5. Note this means *frontier-model API key*, not a small local model — tool-initialisation failure is catastrophic in small models, 89% in qwen2.5:3b `[S11]` |
| **Complete audit log of every query issued to every source**, readable without the product running | Tom's stated requirement. Gartner attributes half of projected 2030 agent deployment failures to insufficient governance runtime enforcement `[S29]` |
| **Row-level and column-level permissions inherited from the source**, never re-implemented | Re-implementing authorisation is how an analytics tool becomes a data breach |
| **Schema and sample data sent to the model provider must be disclosed and configurable**, including a mode that sends schema only | The question Tom asks second |
| **Unreviewed answers are visibly marked** and cannot be exported without an explicit acknowledgement | P3 + non-goal 1. The mechanism that keeps a low-edge user from putting an unverified number on a slide |
| **Lineage retained for the life of the investigation**, queryable independently of the chat | Angela's provenance requirement |
| **PII handling: the system does not sample columns flagged as sensitive** into model context | Baseline expectation; not a compliance certification, which is out of scope |

## 9. Open product questions

1. **Does hop-level lineage actually make verification cheaper than re-derivation?** (O2.) Unmeasured anywhere in the literature; the product's premise. → `validation/`
2. **What is the right hop-count ceiling?** P2 says short; P10 says hard questions need depth. The tradeoff is empirical and the spike should measure it.
3. **How much does consuming a dbt semantic layer actually improve accuracy?** ([strategy/business_model_canvas.md](../strategy/business_model_canvas.md) row 8.) If large, P6 becomes the roadmap's centre; if small, the semantic-layer story is weaker than assumed.
4. **What does the ML agent usefully do in five minutes?** P9 forbids the 12-hour behaviour; nobody has specified the five-minute version.
5. **What is the right default for the unreviewed-answer state at the low edge** — blocked, watermarked, or routed to an analyst?

## Recommended next 3

1. **Build the evaluation harness and the fixed question set before any agent.** P10 makes this the highest-leverage first artifact, O3 is the pack's only publishable number, and every later scoping decision needs it to be measurable.
2. **Specify the exportable investigation artifact in [ux_spec.md](ux_spec.md) and build it early.** It carries O2's measurement, E5's GTM loop and Angela's provenance requirement simultaneously — one artifact, three jobs.
3. **Time-box the ML agent explicitly in [features_prioritized.md](features_prioritized.md) and hold the line.** P9 is the principle a capstone team is most likely to violate, because MLE-bench results are seductive and the 12-hour footnote is easy to forget.
