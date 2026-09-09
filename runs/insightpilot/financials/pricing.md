# Pricing — as a falsifiable threshold, not a forecast

**What this is** — The value metric and why, an anchor analysis against sourced competitor prices, tier design, willingness-to-pay logic per persona, and the pricing-power argument — all framed as **a threshold to falsify** rather than a price to project.
**Why it exists** — [ASSUMPTIONS.md](../ASSUMPTIONS.md) A1 excludes revenue projection from this pack because with no revenue, no CAC and no funnel any forecast would be fabricated. What survives that exclusion is the question a capstone *can* answer from its own architecture: **what would have to be true for a given price to clear cost-to-serve, and does the value delivered exceed it?** This file answers that and refuses to answer more.
**How to read it** — §4 is the threshold computation and the only part that resolves to a number. A skeptic should attack §4's assumption chain — six tagged assumptions multiplied — and §6, where the pricing-power argument is deliberately left empty.
**Depends on / feeds** — Price anchors from [research/sources.md](../research/sources.md); the $75 modelling figure and its band from [strategy/market_sizing.md](../strategy/market_sizing.md) §2.3; cost shape from [tech/not_vaporware.md](../tech/not_vaporware.md) §3. Feeds [unit_economics.md](unit_economics.md) and [risk_matrix.md](risk_matrix.md).

> **Scope note for the audit.** This directory contains **three of six** manifest rows by founder decision (A1). Excluded and **closed, not missing**: **A44 `revenue_build.md`**, **A46 `use_of_funds.md`**, **A48 `comps_exits.md`**. Basis: an academic capstone with no revenue, no CAC data and no funnel; `references/quality-bar.md` property 2 treats unsourced numbers as a defect, and a path-to-$100M-ARR table would be exactly that. Retained: **A43** (this file), **A45** [unit_economics.md](unit_economics.md), **A47** [risk_matrix.md](risk_matrix.md) — all three computable from the system's own architecture.

---

## 1. The value metric

> **Price the investigation. Not the seat, not the token, not the query.**

An *investigation* is BRIEF.md's stated unit of value: one business question pursued to a verified answer, including follow-ups. Three reasons it is the right meter:

1. **The market already prices the question.** Snowflake bills Cortex Analyst **per message, on success only, at a fixed cost regardless of token count** `[S37][S38]`. ThoughtSpot caps its Spotter agent at **25 queries per user per month** on the Pro tier and bills overage `[S44]`. Both are question-metered, arrived at independently.
2. **Tokens are the wrong meter because the customer pays them directly.** Under the self-hosted model (A5) inference runs on the customer's own key, so a token-based price would charge twice for the same thing.
3. **Seats are the wrong meter because value is lumpy.** An analyst running three multi-source investigations a week gets far more than one running three a month, and a flat seat charges both the same.

**But the practical recommendation is a seat price anyway**, and §3 explains why the right meter and the right *invoice* differ here.

## 2. Anchor analysis — what budget this comes from

| Product | Price | Meter | Source |
|---|---|---|---|
| **Snowflake Cortex Analyst** | ≈**$0.134 per message** (6.7 credits/100 messages at $2.00–2.20/AI credit); warehouse compute billed separately | Per question | `[S38][S39][S37]` |
| **ThoughtSpot Essentials** | $25/user/month | Seat | `[S44]` |
| **ThoughtSpot Pro** | $50/user/month, **Spotter capped at 25 queries/user/month**, overage extra | Seat + metered agent | `[S44]` |
| **ThoughtSpot Enterprise** | ≈$137,000/year average contract | Negotiated | `[S45]` |
| **Hex** | $36/editor/month entry; ~$75 Team seat; ≈$750/month for ten analysts | Seat + credits | `[S52]` |
| **Julius AI** | Free (15 msgs/mo) · Plus $35 · Pro $45 · Max $200 · Team $50/user/mo | Seat / message | `[S53]` |

**Two readings that matter.**

**The analyst-tool band is $36–75 per seat per month.** Hex at $36–75 `[S52]` and ThoughtSpot Pro at $50 `[S44]` bracket it. A price above that band is not competing in this category; a price below it leaves value on the table for a product that spans sources.

**Which budget line this displaces is genuinely unknown**, and that is the sharpest open question in the pack's commercial story. [strategy/petal_diagram.md](../strategy/petal_diagram.md) §3 ranks the candidate sources: analyst *time* (salary, unbudgeted — the primary source of users, with no line item), analyst notebooks (real, displaceable, correctly priced), and warehouse copilots (bundled, so additive rather than displacing). **[validation/experiment_board.md](../validation/experiment_board.md) E4 tests it directly** — if fewer than 3 of 5 buyers can name a line, this file's premise is wrong before its arithmetic matters.

## 3. Tier design

Deliberately simple. Complexity in pricing is a tax paid by a sales team this venture cannot afford ([strategy/channel_plan.md](../strategy/channel_plan.md) §4).

| Tier | Price | Contains | Rationale |
|---|---|---|---|
| **Open core** | **Free** | Orchestrator, Postgres + CSV/Excel connectors, plan surface, per-hop verification, hop-level lineage, single-hop re-run, export, audit log | The entire differentiator ships free. **This is the only channel with viable economics** — the product must be installable without a purchase order |
| **Team** | **$75/analyst/month** *(assumption: top of the observed $36–75 band `[S44][S52]`, justified by spanning sources rather than one warehouse; a threshold to falsify, not a validated willingness to pay)* | Semantic-layer consumption (dbt/Cube), shared review queue, investigation history search, binding-store review UI, cross-source reconciliation reporting | The features that matter when a *team* uses it — and the ones the buyer, not the user, cares about |
| **Enterprise** | Negotiated | Managed deployment, support SLA, SSO, retention controls | Only for buyers who require it. Not a growth vector |

### Why the differentiator is free and the collaboration is paid

The instinct is to paywall the lineage — it is the differentiator. **That would be a mistake**, for a mechanical reason: the exported investigation is the edge in the compounding loop ([validation/get_keep_grow.md](../validation/get_keep_grow.md) §3). Charging for the thing that recruits the next analyst breaks the only channel whose economics work at this ACV.

**What is worth paying for is what a team needs and an individual does not** — the review queue, shared bindings, searchable history, semantic-layer integration. Those are also precisely the artifacts the *buyer* evaluates ([strategy/sales_roadmap.md](../strategy/sales_roadmap.md) §4 step 7), which aligns the paywall with the person holding the budget rather than the person doing the work.

### The open-core boundary is not fully settled

[validation/pivot_log.md](../validation/pivot_log.md) §2 lists this as an open decision, and this file narrows rather than closes it. The line above — *individual capability free, team capability paid* — is a proposal with a rationale, not a founder decision.

## 4. The threshold — what would have to be true

**The question A1 permits: does $900/analyst/year clear its own cost, and is the value delivered larger?**

### 4.1 Assumptions, all tagged

| # | Assumption | Value | Basis |
|---|---|---|---|
| a | Price | **$900/analyst/year** | Top of observed band `[S44][S52]` |
| b | Investigations per active analyst per month | **13** | *(assumption: ≥3/week target in [validation/get_keep_grow.md](../validation/get_keep_grow.md); unvalidated)* |
| c | Frontier-model exchanges per investigation | **8** (1 plan + 1 resolution + 6 SQL generations) | Derived from a six-hop plan ([tech/not_vaporware.md](../tech/not_vaporware.md) §3) |
| d | Cost per frontier exchange | **≈$0.134** | Cortex Analyst's per-message economics as a market-priced proxy `[S38][S39]` |
| e | **Expected attempts per step** | **1 / 2 / 3 / 5** — modelled as a range | **Unmeasured.** DABstep implies retries are the common case at ≈14.55–16% on hard tasks `[S4]`. **This is the dominant unknown** |
| f | Analyst fully-loaded cost | **$120,000/year ≈ $58/hour** | *(assumption: US senior analyst total cost; unsourced)* |

### 4.2 Cost of running it, per analyst per year

```
Model cost per investigation  = 8 exchanges × $0.134 × expected_attempts
Investigations per year       = 13 × 12 = 156
```

| Expected attempts | Cost / investigation | Model cost / analyst / year |
|---|---|---|
| 1.0 | $1.07 | **$167** |
| 2.0 | $2.14 | **$334** |
| 3.0 | $3.22 | **$502** |
| 5.0 | $5.36 | **$836** |

Plus warehouse compute for queries *and* verification, billed to the customer's existing platform. **Verification adds zero model tokens** — it is SQL (D05) — which is the single most favourable fact in this model.

### 4.3 Total cost of ownership, and the break-even

Under self-hosting the customer pays both the licence and the inference:

| Expected attempts | Licence | Model | **Analyst TCO / year** | **Hours that must be saved to break even** (÷ $58) |
|---|---|---|---|---|
| 1.0 | $900 | $167 | **$1,067** | **18.4 h** |
| 2.0 | $900 | $334 | **$1,234** | **21.3 h** |
| 3.0 | $900 | $502 | **$1,402** | **24.2 h** |
| 5.0 | $900 | $836 | **$1,736** | **29.9 h** |

### 4.4 Does the value clear it?

From [tech/whitepaper.md](../tech/whitepaper.md) §5: a multi-source question against an unmodelled source goes **90 minutes → 31 minutes**, saving **59 minutes**. Single-source familiar questions save **nothing** (≈1.0× or below).

*(assumption: 25% of an analyst's questions are multi-source — the E3 pass threshold, currently untested.)*

```
Multi-source investigations / year = 156 × 0.25 = 39
Hours saved / year                 = 39 × 59 min = 38.4 h
```

| Expected attempts | Hours needed | Hours delivered | **Margin** |
|---|---|---|---|
| 1.0 | 18.4 | 38.4 | **2.1×** |
| 3.0 | 24.2 | 38.4 | **1.6×** |
| 5.0 | 29.9 | 38.4 | **1.3×** |

**The threshold holds — but by 1.3×–2.1×, not by an order of magnitude.** That is a real result and a narrow one, and it is consistent with A2: automating what a competent analyst already does well yields ordinary gains.

### 4.5 What falsifies this

| If… | Then |
|---|---|
| **Multi-source share < 15%** (E3 fail) | Hours delivered drop to ~23 h/year and the threshold **fails at 3+ attempts.** The price must fall or the product must widen |
| **Expected attempts > 5** | Margin approaches 1.0× and the customer is paying to break even |
| **Verification cost ratio > 0.8** (E1 fail) | The 59-minute saving is fiction — the analyst re-derives anyway — and **the entire computation is void** |
| Analyst fully-loaded cost is $80K, not $120K | Break-even hours rise ~50%; margin at 3 attempts falls to ~1.1× |

**Three of the four are pending experiments.** This is a threshold with its falsifiers named, not a price with a projection attached.

## 5. Willingness to pay, per persona

| Persona | Their frame | What they will pay for | What they will not |
|---|---|---|---|
| **Priya** (analyst, user) | Does not control budget and does not know it. **Her willingness to pay is not a useful signal** and should not be asked ([validation/discovery_guide.md](../validation/discovery_guide.md) §6) | Nothing directly — she advocates | — |
| **Angela** (VP, payer) | Cost per analyst against a data-trust initiative she is measured on | Provenance she can answer on demand; observable adoption; **a governance story** | A tool that goes unused — roughly 25% of employees use the BI tools their employer bought, flat over seven years `[S22]` |
| **Dr. Chen** (staff DS) | His time. 2 h → 19 min is the largest measured gain in the pack | Nothing — he has no budget. But his approval unlocks Angela's | — |
| **Tom** (platform) | Risk, not money | Nothing. **He can only say no** | Anything with an opaque egress path |

**The pricing conversation happens with exactly one person, and she has never used the product.** That is why the paid tier contains the artifacts she evaluates rather than the features the analyst loves.

## 6. Pricing power — deliberately empty

The standard argument here is that price rises as a data moat compounds. **This pack cannot make that argument, and will not.**

ASSUMPTIONS A3 declines to claim a moat. The candidate — a learned semantic layer, where accumulated disambiguation of one organisation's schema makes the system progressively more valuable — is **unevidenced**, and the confirming observation (override rate falling per source with no model change) requires 90+ days of real deployment ([validation/riskiest_assumptions.md](../validation/riskiest_assumptions.md) R10).

**If R10 is later observed, pricing power follows mechanically**: switching costs rise because the accumulated semantics are non-portable, and that is the one asset an open-source competitor cannot copy. Until then this section stays empty, and any downstream artifact asserting pricing power is asserting A3.

**One genuine counter-pressure worth naming.** Inference prices are falling — a fixed benchmark score went from ≈$60 to ≈$0.06 per million tokens between late 2021 and late 2024 `[S63]`, with per-year declines of 9×–900× by capability milestone `[S64]`. Under self-hosting **that saving accrues to the customer, not to us**, so falling model costs improve the customer's TCO and do nothing for our margin. The direction is favourable for adoption and neutral for pricing power.

## Recommended next 3

1. **Run E4 before treating $900 as a price.** If no buyer can name a line item, §4's arithmetic is answering a question nobody is asking.
2. **Measure `expected_attempts` in the 295A harness and publish it.** It moves TCO by a factor of five across the modelled range, nobody in the market publishes it, and it is a byproduct of running the question set.
3. **Settle the open-core boundary explicitly with the founder.** §3 proposes *individual capability free, team capability paid* with a mechanical rationale — but it is a proposal, and [validation/pivot_log.md](../validation/pivot_log.md) §2 still lists it as undecided.
