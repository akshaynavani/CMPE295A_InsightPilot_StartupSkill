# Unit economics — per investigation and per analyst

**What this is** — The per-unit P&L: CAC by channel with its basis, gross margin including AI compute at current API prices, payback, LTV under stated retention, and what happens to margin as model prices fall.
**Why it exists** — AI-native ventures live or die on compute margin, and this one has an unusual property that inverts the standard analysis: **under self-hosting the customer pays the inference on their own key** (A5). That single fact moves the dominant cost line off our P&L and onto theirs, which makes the honest unit-economics question *"what does this cost the customer to run"* rather than *"what is our gross margin."* A file that reported a flattering 90% margin without saying why would be technically true and materially misleading.
**How to read it** — §2 is the inversion, §3 the arithmetic, §5 the honest weak point. A skeptic should attack §3's `expected_attempts` range, which moves cost by 5× and is unmeasured, and §6's LTV, which rests on a retention figure nobody has observed.
**Depends on / feeds** — Cost shape from [tech/architecture/D05](../tech/architecture/D05_model_routing_cost.md) and [tech/not_vaporware.md](../tech/not_vaporware.md) §3; price from [pricing.md](pricing.md); CAC verdicts from [strategy/channel_plan.md](../strategy/channel_plan.md) §3. Feeds [risk_matrix.md](risk_matrix.md).

> **Scope note.** Cost side only (A1). **A44 `revenue_build.md`, A46 `use_of_funds.md` and A48 `comps_exits.md` are excluded by founder decision and are closed, not missing** — see [pricing.md](pricing.md) for the basis.

---

## 1. The unit

**One investigation** — a business question pursued to a verified answer, including follow-ups. Everything below rolls up from it.

Secondary unit: **one analyst-year**, at 156 investigations *(assumption: 13/month, the ≥3/week target in [validation/get_keep_grow.md](../validation/get_keep_grow.md); unvalidated)*.

## 2. The inversion — who actually pays the compute

Under the open-core self-hosted model (A5), the orchestration layer runs in the customer's environment **against their own frontier-model API key**, and every query runs on their existing warehouse.

| Cost line | Who pays |
|---|---|
| Frontier-model inference (planning, resolution, SQL generation, replanning) | **Customer** |
| Warehouse compute for queries **and for verification** | **Customer** |
| Small-model calls (prose, chart choice) | **Customer** |
| Data storage of bindings and lineage | **Customer** — it is their database |
| Support, documentation, releases | **Us** |
| Hosting | **Nobody** — there is no hosted plane |

**Consequence, stated plainly:** our COGS on the Team tier is support and release engineering. Gross margin is high for structural reasons that have nothing to do with efficiency, and **reporting it as a strength would be misleading.**

**The economically meaningful analysis is the customer's cost to run**, because that is what caps the price and what a buyer will actually interrogate. §3 computes that; §4 computes ours and says why it is uninteresting.

## 3. Cost per investigation — the customer's side

### 3.1 The model

```
cost = (plan synthesis + schema resolution + SQL generation × hops) × expected_attempts
     + small-model calls
     + warehouse compute (queries + verification)
```

| # | Factor | Value | Basis |
|---|---|---|---|
| a | Frontier exchanges per investigation | **8** (1 plan + 1 resolution + 6 SQL) | Six-hop plan ([tech/not_vaporware.md](../tech/not_vaporware.md) §3) |
| b | Cost per frontier exchange | **≈$0.134** | Cortex Analyst per-message economics as a market proxy `[S38][S39]` |
| c | **Expected attempts per step** | **1 / 2 / 3 / 5** | **Unmeasured.** DABstep implies retries are the common case at ≈14.55–16% on hard tasks `[S4]` |
| d | Small-model calls | ≈$0.02 | *(assumption: 2 cheap calls per investigation)* |
| e | Warehouse compute per investigation | **≈$0.05–0.20** | *(assumption: 6 analytical queries + ~12 verification queries on a small warehouse; unsourced)* |

### 3.2 The arithmetic

| Expected attempts | Frontier | Small model | Warehouse | **Total / investigation** | **× 156 = per analyst-year** |
|---|---|---|---|---|---|
| **1.0** | $1.07 | $0.02 | $0.12 | **$1.21** | **$189** |
| **2.0** | $2.14 | $0.02 | $0.12 | **$2.28** | **$356** |
| **3.0** | $3.22 | $0.02 | $0.12 | **$3.36** | **$524** |
| **5.0** | $5.36 | $0.02 | $0.12 | **$5.50** | **$858** |

### 3.3 The two facts that shape this table

**Verification is free in model terms.** All six structural checks are SQL against the customer's own warehouse — no model calls (D05). The differentiating mechanism is the cheapest line in the system, and it costs roughly $0.06 of warehouse compute per investigation. **A verification design built on model self-critique would have made the differentiator scale with token price**; this one scales with compute the customer already buys.

**`expected_attempts` is the whole model.** It moves cost **4.5×** across the range and it is unmeasured. A cost model assuming one clean pass will be wrong by a large multiple, and the honest statement is that **nobody — including every commercial vendor in this category — publishes this number.** It is a byproduct of running the 295A harness ([tech/architecture/D08](../tech/architecture/D08_evaluation_harness.md)).

## 4. Our side — CAC, margin, payback

### 4.1 CAC by channel

All figures are hypotheses; there is no funnel (A1).

| Channel | CAC | Basis | Verdict |
|---|---|---|---|
| **Open-source self-serve** | **≈$0 marginal**, fixed engineering on docs and quickstart | The cost is hours on the quickstart, amortised across every install forever | **The only viable channel** |
| **Analyst-led internal referral** | **≈$0 marginal** | The compounding loop ([validation/get_keep_grow.md](../validation/get_keep_grow.md) §3) | Viable |
| Community + technical content | Founder hours, unattributable | Credibility, not acquisition | Viable, do not attribute revenue |
| Inside sales / outbound | **$3,000–8,000** *(assumption: standard B2B ranges, no data)* | — | **Fails.** At a $9,000 ACV (10 analysts), payback is ~7 months gross *before* any cost-to-serve; at 5 analysts, acquisition exceeds first-year revenue |
| Reseller | 20–35% margin *(assumption)* | — | **Fails on redundancy, not margin.** Paying 28% for a sales motion the product is designed not to need |
| Paid acquisition | High, poor intent | — | Fails |

**The conclusion is arithmetic, not preference: at a $900 ACV only zero-CAC channels survive** ([strategy/channel_plan.md](../strategy/channel_plan.md) §3).

### 4.2 Gross margin

| | Per analyst-year |
|---|---|
| Revenue (Team tier) | **$900** |
| Our COGS — inference | **$0** (customer's key) |
| Our COGS — hosting/storage | **$0** (no hosted plane) |
| Our COGS — support | *(assumption: $60–120/analyst-year at small scale; falls with docs quality and community)* |
| **Gross margin** | **≈87–93%** |

**This number is high for a structural reason and should not be presented as an achievement.** It is high because the customer absorbed the variable cost. **A hosted version of this product would carry the §3 table as COGS**, and at 3 expected attempts that is $524 against $900 — a 42% gross margin, before support. That comparison is the honest way to read this row, and it is a reason the A5 self-hosted decision is an economic decision as much as a positioning one.

### 4.3 Payback and LTV

**Payback: immediate.** With ≈$0 marginal CAC there is no acquisition cost to recover. The meaningful constraint is not payback but **fixed-cost amortisation** — the engineering hours in the quickstart divided across installs — which makes the E8 threshold (clone → first successful investigation under 30 minutes) the real economic gate.

**LTV, stated with its dependency:**

```
LTV = $900/analyst-year × gross margin × expected retention (years)
```

| Retention | LTV per analyst |
|---|---|
| 2 years | ≈$1,620 |
| 3 years | ≈$2,430 |
| 5 years | ≈$4,050 |

*(assumption: 90% gross margin; retention entirely unobserved — no deployment exists.)*

**LTV:CAC is undefined and should stay that way.** With CAC ≈ 0 the ratio is arithmetically infinite and analytically meaningless. Quoting it would be the clearest possible example of a number that looks strong and says nothing. **The metric that actually matters is expansion: deployments reaching a second analyst without founder intervention** ([validation/get_keep_grow.md](../validation/get_keep_grow.md)), because that is what turns a free install into a Team-tier account.

## 5. The cost-curve argument, and why it does not help us

Inference prices fall unevenly but sharply: a fixed benchmark score went from ≈$60 to ≈$0.06 per million tokens between November 2021 and late 2024 `[S63]`, with per-year declines ranging 9×–900× depending on the capability milestone `[S64]`.

**Under self-hosting the entire saving accrues to the customer.** The §3 table shrinks; our §4 margin does not move, because our margin does not contain inference.

| | Effect of falling model prices |
|---|---|
| **Customer TCO** | Improves materially — a 3× decline takes the 3-attempt case from $524 to ~$175/analyst-year |
| **Our gross margin** | **Unchanged** |
| **Our pricing power** | **Unchanged.** A3 declines a moat; falling costs do not create one |
| **Adoption** | Improves — the threshold in [pricing.md](pricing.md) §4.4 clears more comfortably |
| **Competitive position** | **Neutral-to-negative.** Falling costs also make it cheaper for incumbents to widen their bounded scope |

**The honest framing:** the cost curve is a tailwind for the customer and for adoption, and it is **not** a margin story for this venture. A pack claiming the standard "margins expand as inference cheapens" line would be describing a hosted business this one deliberately is not.

**And the counter-pressure worth naming:** `expected_attempts` moves cost more than the price curve does over a two-year horizon. A 3× price decline is worth less than getting retries from 3 to 1.

## 6. What this analysis cannot support

1. **No LTV:CAC ratio.** Undefined at zero CAC, and meaningless if quoted.
2. **No retention figure.** Nothing is deployed. The 2/3/5-year LTV rows are illustrative arithmetic, not estimates.
3. **No revenue model.** Excluded by A1, deliberately (`revenue_build.md`).
4. **No support-cost basis.** The $60–120 figure is a guess; open-source support load is notoriously unpredictable and scales with deployment count rather than revenue ([tech/architecture/D09](../tech/architecture/D09_deployment_scale.md)).
5. **No measured `expected_attempts`** — the dominant term in the only table that matters.

**Four of five resolve with the 295A harness or a first deployment.** None resolves by further analysis, and this file should not be revised until one of them is measured.

## Recommended next 3

1. **Instrument cost per investigation, split by attempt count, from the first harness run.** It is the dominant unknown, it is free to capture, and publishing it would be a first in this category.
2. **Report gross margin only alongside §4.2's explanation.** An 87–93% figure quoted alone implies operating efficiency the venture has not demonstrated and does not possess.
3. **Replace the LTV table with expansion rate as the headline unit metric** — deployments reaching a second analyst. At zero CAC that is the number that decides whether the economics exist at all.
