# Prioritised features — 50, in strict priority order

**What this is** — Fifty features in Now / Next / Later tiers, each with its mechanism, user value, dependencies and effort estimate.
**Why it exists** — [features_flagship.md](features_flagship.md) says what matters; this says what gets built first, and what gets cut when 295A runs short — which it will. The specific failure it prevents: a backlog that is secretly chronological, where "Now" means "the parts we already understand." The ordering below is by **leverage on the riskiest claim**, which puts the evaluation harness ahead of the agents and the lineage surface ahead of three of the four specialist agents.
**How to read it** — The Now tier is the 295A scope. A skeptic should attack the ordering of #1–#6, which spends the first weeks on measurement and one narrow path rather than on visible product, and §4, which names what gets cut first.
**Depends on / feeds** — Principles from [PRD.md](PRD.md) §3; flagship set from [features_flagship.md](features_flagship.md); the two strategy-discovered requirements from [strategy/gtm.md](../strategy/gtm.md) §3 and [strategy/sales_roadmap.md](../strategy/sales_roadmap.md) §4. Feeds `tech/` sequencing and the validation stage gates.

---

## 1. Ordering principle

Not by user visibility and not by build order convenience. **By how much each feature reduces uncertainty on the claim that would kill the venture** — that verification is cheaper than re-derivation (PRD §7.1, O2), and that multi-hop planning is usable at all (P10).

That principle produces one counter-intuitive result, stated up front so it is not mistaken for an error: **the evaluation harness is #1 and three of the four specialist agents are in Next or Later.** A demo with four agents and no measurement cannot tell anyone whether the thing works.

Effort: **S** ≈ days · **M** ≈ 1–3 weeks · **L** ≈ a month or more, for a two-person team.

## 2. NOW — the 295A scope (#1–#18)

| # | Feature | Mechanism | User value | Depends on | Effort |
|---|---|---|---|---|---|
| 1 | **Fixed question set + evaluation harness** | 30–50 questions over a known schema with ground-truth answers; automated execution accuracy scoring | None directly — it is how anyone knows if the rest works. Produces O3, the pack's only publishable number | — | M |
| 2 | **Seeded-error test set** | Investigations with deliberately planted wrong joins, grains and mappings | Measures O4 (silent-error rate), the metric that matters most and is otherwise invisible | 1 | S |
| 3 | **Postgres connector, read-only** | Schema introspection + query execution, credentials in the customer's env | The single source everything else is tested against | — | S |
| 4 | **CSV/Excel ingestion** | Typed load into a working store, with inferred schema shown for correction | The unmodelled source — the case no incumbent attempts `[S32][S36]` | — | S |
| 5 | **Orchestrator v1: plan generation** | Question → ordered agent tasks over named sources | The core mechanism. Nothing exists without it | 3, 4 | L |
| 6 | **Analysis plan shown before execution, approvable** | Human-readable plan, editable, gated on first run per source | Errors caught before they cost a query. Flagship 4 | 5 | M |
| 7 | **Data Fetch/Integration agent** | Executes fetch tasks against connectors, emits structured output + lineage | Makes the plan real | 3, 4, 5 | M |
| 8 | **Analytics agent v1** | Joins, filters, aggregations, period comparison | Answers the majority of real ad-hoc questions | 7 | M |
| 9 | **Hop-level lineage capture** | Every handoff records sources, query, transform, row counts in/out | **The differentiator's substrate.** Flagship 15 | 7, 8 | M |
| 10 | **Lineage surface — inspect a hop** | Renders a hop as a readable step, not a JSON blob | Verification in seconds. The Verify beat | 9 | M |
| 11 | **Ambiguity interception** | Halt-and-ask when a term resolves to >1 column or grain | Attacks P1 directly — 81.2% of failures `[S2]`. Flagship 2 | 5 | M |
| 12 | **Vocabulary binding store + editable chips** | Resolved terms persisted per organisation, correctable | Flywheel seed (PRD §6). Flagship 3 | 11 | M |
| 13 | **Per-hop verification by decomposition** | Cheaper structurally-different check per hop: row counts, grain, null rate, boundary totals | P7. The only feature that improves O4 | 9 | M |
| 14 | **Single-hop re-run** | Re-execute one hop in isolation, diff against stored output | Dr. Chen's two hours → five minutes. Flagship 16 | 9, 10 | S |
| 15 | **Exportable self-contained investigation** | One readable file: question, plan, hops, queries, counts, answer, sign-off | **Four jobs, one artifact** — differentiator proof, GTM loop edge, provenance, O2 instrument | 9, 10 | M |
| 16 | **Investigation thread with context inheritance** | Durable unit holding bindings, scope, established facts | Follow-ups become short plans. Flagships 1, 20 | 5, 12 | M |
| 17 | **Doubt surfacing** | Names least-certain hops and why; no confidence percentages | P3. Flagship 13 | 13 | S |
| 18 | **Audit log of every query issued** | Append-only, readable without the product running | Tom's veto condition ([strategy/sales_roadmap.md](../strategy/sales_roadmap.md) §4 step 5) | 7 | S |

**Now-tier total: roughly 4 L/M-heavy months for two people.** That is a full 295A and it deliberately contains no Visualization agent, no ML agent and no REST connector. What it does contain is a measurable, verifiable, exportable single-source-plus-CSV investigation — which is enough to test the claim the venture rests on.

## 3. NEXT — 295B core (#19–#36)

| # | Feature | Mechanism | User value | Depends on | Effort |
|---|---|---|---|---|---|
| 19 | **REST JSON connector** | Configurable endpoint + response shaping | Third source type; makes "heterogeneous" real rather than aspirational | 7 | M |
| 20 | **Replanning on invalidation** | Failed verification revises remaining steps | P2. Flagship 10 | 13 | L |
| 21 | **Override a hop, re-flow downstream** | Edit query/join/method; downstream re-executes; correction persists | Flagship 17. **Honest fallback: invalidate and replan when grain changes** | 14, 20 | L |
| 22 | **Visualization agent** | Chart selection justified by data shape | Flagship 12 | 8 | M |
| 23 | **Semantic layer consumption — dbt** | Read metric definitions and join paths; they take precedence | **P6, and the demo that answers Angela's deal-ending objection** | 12 | M |
| 24 | **Sign-off state + unreviewed marking** | Explicit reviewed-by/when; unreviewed answers marked and gated on export | Flagship 19; enforces PRD non-goal 1 | 15 | S |
| 25 | **Plan caching + pinned bindings** | Reuse approved plan by semantic signature | P4 — same question, same answer. Flagship 6 | 6, 12 | M |
| 26 | **Plan-length discipline** | Report hop count; flag long plans; suggest splitting | P2. Flagship 5 | 6 | S |
| 27 | **Established facts in the answer** | Intermediate checkable claims, not one summary | Flagship 14 | 8 | S |
| 28 | **Investigation history, searchable** | By question text and by source touched | Angela's provenance query | 16 | M |
| 29 | **Quickstart: clone → first investigation < 30 min** | Docker compose, seeded demo data, one-page setup | **E1 — below this threshold the sole viable channel fails** ([strategy/channel_plan.md](../strategy/channel_plan.md) §4) | 3, 4, 5 | M |
| 30 | **Row/column permission inheritance from source** | Never re-implement authorisation; inherit and fail closed | Security precondition | 3 | M |
| 31 | **Schema-only mode for model context** | Configurable: send schema without sample values | Tom's second question | 7 | S |
| 32 | **ML agent v1, time-boxed in minutes** | Baseline model, named features, uncertainty, **explicit not-attempted list** | P9. Flagship 11. Never MLE-bench behaviour `[S9]` | 8 | L |
| 33 | **Source scoping UI** | Analyst names/confirms sources in play before planning | P2, P6 — narrows the search space | 6 | S |
| 34 | **Cost and latency preview per plan** | Estimated tokens and wall-clock before approval | B1; stops runaway investigations | 6 | S |
| 35 | **Multi-source join reconciliation report** | Coverage, unmatched rows, key-collision detection across sources | The specific failure mode of cross-source work — the thing that makes step 2 wrong quietly | 19, 13 | M |
| 36 | **Shared investigation link (self-hosted)** | Read-only view inside the deployment | GTM loop step 4 for teams that prefer links to files | 15, 24 | S |

## 4. LATER — post-capstone (#37–#50)

| # | Feature | Mechanism | User value | Depends on | Effort |
|---|---|---|---|---|---|
| 37 | Semantic layer consumption — Cube | Same as 23 for Cube's API | Broader P6 coverage | 23 | M |
| 38 | Snowflake connector | Warehouse-native read | The "if time permits" source in BRIEF.md | 7 | M |
| 39 | Method-level ML lineage | Target definition, split, algorithms tried and rejected, with reasons | Dr. Chen's leakage objection answered concretely | 32, 9 | M |
| 40 | ML agent override affordances | Analyst sets target, algorithm, split | Makes the high edge a user rather than a critic | 39 | M |
| 41 | Binding-store review UI | See and edit the organisation's accumulated vocabulary | Makes the flywheel legible and auditable | 12 | M |
| 42 | Override-rate trend reporting | Track override rate per source over time | The **only observable evidence** for the learned-semantic-layer moat candidate (A3) | 21, 41 | S |
| 43 | Scheduled re-run of a verified investigation | Re-execute on a schedule; diff against last accepted | Turns a one-off answer into monitoring without becoming a dashboard | 25 | M |
| 44 | Notebook export | Export an investigation as a runnable notebook | Meets Hex users where they are ([strategy/petal_diagram.md](../strategy/petal_diagram.md) §3) | 15 | M |
| 45 | Multi-analyst investigation collaboration | Two analysts on one investigation with attribution | Team workflow | 36 | L |
| 46 | Question templates from history | Recurring question shapes surfaced as starting points | Reduces time-to-first-value for the second analyst | 28 | S |
| 47 | PII-flagged column exclusion | Never sample flagged columns into model context | Compliance baseline | 31 | S |
| 48 | Model provider abstraction | Swap frontier providers per deployment | A5 — customer's own key, their choice of provider | 5 | M |
| 49 | MCP server compatibility | Consume third-party MCP servers as sources | P8; rides the ecosystem `[S62]` | 19 | M |
| 50 | Cost attribution per investigation | Token and compute spend per investigation, per analyst | B1 for the buyer's cost conversation | 34 | S |

## 5. What gets cut first, and what must not be

A capstone runs short. Deciding this now rather than in week ten is the point of the file.

**Cut in this order:**
1. **#22 Visualization agent.** A table is an acceptable answer. Charts are the most demo-visible and least evidence-bearing feature in the list.
2. **#19 REST connector.** Postgres + CSV already demonstrates heterogeneity. A third source proves nothing new about the mechanism.
3. **#32 ML agent.** The largest L in Next, and ASSUMPTIONS A2 already establishes it is not the differentiator. Painful because it is the widest capability gap in the landscape — and still the right cut, because P9 means the honest version is small and the dishonest version is a 12-hour job dressed as a conversation.
4. **#21 Override re-flow.** Degrade to *invalidate and replan*, which is the honest fallback anyway.

**Must not be cut, at any cost:**

| # | Feature | Why it is load-bearing |
|---|---|---|
| **1, 2** | Evaluation harness and seeded errors | Without them nobody — advisor, reviewer, or the team — can say whether it works. P10 |
| **9, 10** | Lineage capture and surface | Cutting these leaves a worse Genie. It **is** the differentiator |
| **13** | Per-hop verification | The only mechanism that improves O4. Without it the trace is a log |
| **15** | Exportable investigation | Four jobs, one artifact. Retrofitting export onto a stateful UI is expensive |
| **11** | Ambiguity interception | Attacks 81.2% of the failure mass `[S2]`. The highest accuracy-per-effort item in the list |

**The line to hold.** If 295A ships #1–#15 and nothing else, the project has a measurable, verifiable, exportable investigation over two source types and a published accuracy number. **If it ships four agents, charts and no harness, it has a demo and no evidence** — and every claim in this pack stays untested.

## 6. Dependency spine

```
1 harness ──┬─→ 2 seeded errors ──────────────────→ O4
            │
3 postgres ─┼─→ 5 orchestrator ─→ 6 plan shown ─┬─→ 25 caching
4 csv ──────┘        │                          └─→ 26 length discipline
                     ├─→ 11 ambiguity ─→ 12 bindings ─→ 23 dbt ─→ 41 review ─→ 42 trend
                     │
                     └─→ 7 fetch ─→ 8 analytics ─→ 9 lineage ─┬─→ 10 surface ─→ 14 re-run
                                        │                     ├─→ 13 verify ─→ 17 doubt
                                        │                     └─→ 15 export ─→ 24 sign-off ─→ 36 share
                                        ├─→ 22 charts
                                        └─→ 32 ML ─→ 39 method lineage ─→ 40 override
                                              13 ─→ 20 replan ─→ 21 override re-flow
```

**The critical path to a testable claim is `3/4 → 5 → 7 → 8 → 9 → 10 → 15`**, with `1` running alongside from day one. Everything else branches off it.

## Recommended next 3

1. **Start #1 and #3 in parallel in week one.** The harness has no dependencies and gates every judgement afterwards; Postgres is the substrate. Neither is glamorous and both are the fastest route to knowing anything.
2. **Treat #29 (quickstart under 30 minutes) as a Now item if the open-source channel is being tested during 295A.** It is listed in Next because it depends on a working core — but it is the gate on the only viable channel, and discovering at month nine that setup takes two hours would invalidate [strategy/channel_plan.md](../strategy/channel_plan.md).
3. **Write the §5 cut list into the 295A project plan explicitly.** A cut decided in advance is a scope decision; the same cut made in week ten is a failure, and they are otherwise indistinguishable in a final report.
