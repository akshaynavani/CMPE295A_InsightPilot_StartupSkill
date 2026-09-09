# Positioning

**What this is** — The two axes that actually divide this market, where every competitor sits on them, which quadrant is open, and the one-sentence positioning statement the whole pack inherits.
**Why it exists** — This is where ASSUMPTIONS A5, A6 and A11 all land, and where the phase 1 reframe of A8 changes what the product leads with. Without it, three specific failures follow: the one-pager sells speed when the evidence supports verifiability; the deck compares against Genie on accuracy, which no measurement supports and which A6 forbids; and the whole pack fails to answer *why is this not a Databricks feature*, which is the first question any technical investor or advisor asks.
**How to read it** — §2 (axes) and §5 (the statement) are the output; §4 is the hardest part and the one most likely to be attacked — it answers the gravity question. A skeptic should attack §2.1's claim that these axes are *discovered* rather than convenient, and §6, which lists what this positioning gives up.
**Depends on / feeds** — Inherits the differentiator from [research/competitors.md](../research/competitors.md) §4 with its four constraints, the axes from §3.1 there, the A8 reframe from [research/survey.md](../research/survey.md) §6.3, and the market type from [market_type.md](market_type.md). Feeds every artifact in `narrative/`, the PRD's framing, and [gtm.md](gtm.md).

---

## 1. What this positioning must do

Four jobs, each traceable to a decision already made:

1. **Lead with verifiability, support with latency.** The A8 reframe. The trust evidence is High-confidence, current and from two independent disclosed surveys; the latency evidence is Medium-confidence and second-hand `[S16][S17][S15]`.
2. **Answer the gravity question structurally.** A11, resolved by founder decision: cross-source neutrality, backed by open-core self-hostable deployment (A5).
3. **State the differentiator without inflating it.** A6's four constraints travel with it — not a 10x, the bar is Hex's notebook, the ML agent is not the differentiator, and no head-to-head accuracy claim is permitted.
4. **Sell the distinction, not the category.** The re-segmentation consequence from [market_type.md](market_type.md) §3.

## 2. The two axes

### 2.1 Why these axes and not the obvious ones

The axes a template would supply — price × capability, ease-of-use × power, AI-native × AI-added, cloud × self-hosted — all fail the same test: **they sort this market into groups that behave identically.** Every product in the landscape is AI-native by 2026; every one claims ease of use; price varies by a factor of three across products whose mechanisms are indistinguishable. An axis that does not separate behaviour is decoration.

These two were derived in [research/competitors.md](../research/competitors.md) §3.1 by asking what actually differs in the *failure* column of the teardown — which is the only column where the products genuinely diverge.

**Axis X — hops of the core loop executed autonomously.** From zero, through one, to many.

| Position | Meaning | Who |
|---|---|---|
| **0** | The human executes every hop | Doing nothing; the analyst writing SQL |
| **1** | Question → answer, one query, one source | Cortex Analyst, Genie, Copilot, Spotter, Wren AI, Pulse |
| **Many, human-driven** | Multiple hops, but the human directs each | Hex Notebook Agent |
| **Many, system-planned** | A plan spanning sources, replanned when a result invalidates it | *empty* |

**Axis Y — where correctness is established.**

| Position | Meaning | Who |
|---|---|---|
| **Pre-encoded** | A human authored a semantic artifact before the question was asked | Cortex (YAML), Genie (space), Copilot (model), Pulse (metric), Wren AI (MDL) |
| **Post-hoc by the human** | The human reads the SQL or the notebook and decides | Hex; the analyst's own query |
| **Carried with the answer** | The system emits a trace structured so verification is cheap | *essentially empty* — Genie's Inspect `[S32]` is the nearest move, and it verifies within one query, not across a plan |

**These axes are load-bearing because each one names a mechanism with a documented failure mode.** Axis Y position "pre-encoded" *entails* the bounded-scope failure — 30 tables `[S32]`, ~32K tokens `[S36]`, existing measures only `[S42]`. Axis X position "1" *entails* single-source. Neither is a marketing distinction.

### 2.2 The map

```
              CORRECTNESS ESTABLISHED
                      ▲
   carried with       │                            ┌──────────────┐
   the answer         │              Genie·Inspect │  AGENTIC BI  │
                      │                    ○       │   (target)   │
                      │                            └──────────────┘
   ─────────────────────────────────────────────────────────────────
   post-hoc by        │                         Hex Notebook Agent
   the human          │   analyst writes SQL ●          ●
                      │
   ─────────────────────────────────────────────────────────────────
   pre-encoded        │   Cortex ● Genie ● Copilot ●
   (semantic model)   │   Pulse ●  Spotter ●  Wren AI ●
                      │
                      └───────────────────────────────────────────▶
                        0 hops        1 hop            many hops
                                  HOPS EXECUTED AUTONOMOUSLY

   ● shipped    ○ partial (verifies within one query, not across a plan)
```

### 2.3 The open quadrant

**Many hops × correctness carried with the answer.** Nothing occupies it.

The honest reason, stated here rather than discovered by a reviewer: **it is empty because it is hard, not because it was overlooked.** Multi-step data reasoning measures ≈14.55–16% on DABstep's Hard split against 76.39% on Easy `[S4]`, and agent consistency falls from above 60% `pass^1` to below 25% `pass^8` `[S5]`. A positioning that claims an empty quadrant without saying why it is empty is claiming everyone else is stupid.

**The inversion that makes it a strategy rather than a hope:** those same numbers are the *argument for* the Y axis. If multi-hop execution were reliable, correctness could stay pre-encoded and nobody would need a trace. Because it is not reliable, the trace is what makes the hops usable at all. **The two axes are not independent — occupying the far end of X requires occupying the top of Y.** That is the whole thesis in one sentence.

## 3. Competitor placement, read as behaviour

| Competitor | X | Y | What the position predicts about them |
|---|---|---|---|
| **Doing nothing** | 0 | n/a | Free, instant, unauditable. Wins whenever expected turnaround is one to four weeks `[S15]` |
| **Analyst writes SQL** | 0 | post-hoc (self) | Fails on latency, never on trust. The analyst *is* the verification step — which is why it is so hard to displace |
| **Snowflake Cortex Analyst** | 1 | pre-encoded | Best-in-class semantic contract; cannot answer what the YAML does not cover `[S36]` |
| **Databricks Genie** | 1 (+Inspect) | pre-encoded → partial | The only incumbent moving up the Y axis. Verifies within a query; capped at 30 tables `[S32]` |
| **Power BI Copilot** | 1 | pre-encoded | Cannot compute a metric that is not already a measure `[S42]` — structurally unable to answer a novel question |
| **Tableau Pulse** | inverted | pre-encoded | Pushes metric changes; an investigation never starts `[S48][S49]` |
| **ThoughtSpot / Spotter** | 1 | pre-encoded | 25 queries/user/month on Pro `[S44]` — priced as occasional use, not a core loop |
| **Hex Notebook Agent** | many (human-driven) | post-hoc | **The real competitor for this positioning.** Already solves auditability structurally `[S54]` |
| **Wren AI** | 1 | pre-encoded (MDL) | Nearest neighbour, open source, 13K+ stars `[S50]`. Differs in scope of loop, not approach |
| **dbt SL / Cube / AtScale** | n/a | pre-encoded (supplier) | Not rivals — the integration surface `[S66]` |

**Two placements deserve emphasis.** Genie is the only incumbent moving toward this quadrant, and it is moving on the Y axis while staying at X=1 `[S32]` — so the competitive question is whether Databricks extends Inspect across a plan before this product gets there. Hex is the one already at the far end of X, and it gets there by keeping the human in every hop `[S54]` — so the competitive question is whether an analyst prefers a plan they review to a notebook they drive.

## 4. Why this is not a Databricks feature — closing A11

The gravity question, answered structurally because there is no empirical answer available.

**The pattern that requires an answer.** Sisu Data raised ≈$128.7M attacking the diagnostic question — the highest-value part of this loop — and became a Snowflake division in October 2023, with the standalone product in wind-down `[S56][S57]`. Narrative Science was folded into Tableau in December 2021 `[S58]`. **Neither failed technically.** Standalone analytical intelligence gets absorbed by whoever owns the data.

**The answer: the value is in spanning, and no warehouse vendor can sell spanning.** A Databricks feature that fetches from Postgres, an uploaded file and a REST API, and treats them as equal peers, is a feature arguing against Databricks' own gravity. Genie's design says this out loud — its reliability strategy is a curated space of at most 30 tables inside the lakehouse `[S32]`. Snowflake's Cortex Analyst is Snowflake-only by construction `[S36]`. Neither is a limitation the vendor wants to remove; both are the product.

**What makes the answer credible rather than convenient — the deployment decision (A5).** Open-core and self-hostable, running inside the customer's own boundary against their own model API key. Neutrality asserted by a hosted service that sees all the customer's data is a claim; neutrality backed by code the customer runs themselves is a property. This is also why the A5 and A11 decisions had to be made together — a managed-only product has no neutrality argument to make.

**One constraint that travels with A5, and must not be misstated anywhere:** self-hostable means the *orchestration layer* runs in the customer's environment, not that the system runs on a small local model. Tool-initialisation failure is the leading agent reliability bottleneck and is catastrophic in small models — an 89% error rate in qwen2.5:3b, absent in large models `[S11]`.

**The residual, stated not buried.** Neutrality is a structural answer, not an empirical one. It has not been tested that a real customer's questions actually span sources. **If the first serious customer's data all lives in one warehouse anyway, this argument is true and worthless.** That is a discovery question, carried to the validation layer, and it is the dominant risk named in [market_type.md](market_type.md) §3.

## 5. The positioning statement

> **For the enterprise data analyst, InsightPilot is the only conversational analytics layer that answers a question spanning their real sources and hands back an investigation they can verify hop by hop — because the Orchestrator plans and replans across a pluggable connector layer, and every handoff emits its own inspectable, re-runnable lineage.**

Read against the required form: *beachhead* = the enterprise data analyst; *category* = conversational analytics layer; *key benefit* = an answer spanning real sources that can be verified hop by hop; *mechanism* = plan-and-replan over a pluggable connector layer with lineage emitted per handoff.

**Supporting line, for use where one sentence is not enough:** *Every other tool makes you trust it or check it yourself. This one is built to be checked — which is what makes an answer you did not derive worth having.*

### 5.1 What this statement deliberately does not say

- **Not "10x faster" or "10x anything."** ASSUMPTIONS A2 stands; A6's first constraint forbids it.
- **Not "more accurate than Genie / Cortex / Copilot."** No commercial agentic-BI product publishes an accuracy benchmark ([research/sources.md](../research/sources.md), *Named gaps* 2), so no comparative claim is supportable. A6 constraint 4.
- **Not "for anyone to ask questions of data."** The low edge earns the conversational interface as a design constraint; it is not the first customer. The ThoughtSpot markdown is why `[S46]`.
- **Not "AI-powered."** Everything in this market is. It separates nothing.
- **Not led by machine learning.** The ML agent is the widest capability gap in the landscape and, per A2, deliberately not the differentiator.

## 6. What this positioning gives up

Naming the costs is what distinguishes a position from a wish.

1. **The whole business-user market**, which is where the category's revenue and attention are. Deliberate, and the ThoughtSpot markdown `[S46]` is the justification — but it means the TAM in [market_sizing.md](market_sizing.md) is smaller than the BI market by a lot, and the pack must not quietly re-expand it later.
2. **The bundling advantage**, permanently. The buyer already owns Copilot or Genie. Every sale starts by explaining why a thing they already have is not this thing.
3. **The easy accuracy story.** Leading with verifiability means conceding, out loud, that answers will sometimes be wrong. That is honest and it is a harder sale than "our AI is accurate."
4. **Simplicity.** "Hop-level lineage across heterogeneous sources" needs a demo, and a positioning that needs a demo has a longer top of funnel — which [gtm.md](gtm.md) must plan around rather than assume away.

## Recommended next 3

1. **Take §5's statement verbatim into every narrative artifact**, with §5.1 attached as the do-not-say list. The one-pager, the memo and the deck all inherit it; if the constraints are dropped in transit, the pack has manufactured the claim A2 forbids.
2. **Size the beachhead in [market_sizing.md](market_sizing.md) against §6.1's concession.** The number must be built bottom-up from analysts, not from the BI market — a top-down slice would contradict the re-segmentation declaration.
3. **Make §4's residual — do real questions span sources? — a named discovery question in [validation](../validation/)**, alongside the verification-cost experiment. It is the cheapest possible test of the argument this entire position rests on.
