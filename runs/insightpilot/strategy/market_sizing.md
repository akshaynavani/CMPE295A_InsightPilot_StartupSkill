# Market sizing

**What this is** — TAM, SAM and SOM built bottom-up from analyst headcount × price, with every factor either sourced or tagged as an assumption, a top-down sanity check, and the beachhead sized separately.
**Why it exists** — [market_type.md](market_type.md) declared a re-segmented market, and a re-segmentation declaration is falsified the moment someone writes "1% of a $40B BI market" — that arithmetic describes an existing-market play and would contradict the whole strategy. This file also prevents the narrative layer from quoting a Gartner headline as if it were this venture's opportunity: the BI market is not the market for this product, and the honest number is much smaller.
**How to read it** — §2 is the arithmetic; §5 is the uncomfortable part and the reason this file matters. A skeptic should attack the assumption chain in §2.2 — four multiplied assumptions is where sizing usually becomes fiction — and §5's conclusion that the TAM is small.
**Depends on / feeds** — Inherits the beachhead and the concession in [positioning.md](positioning.md) §6.1; prices anchored to [research/competitors.md](../research/competitors.md). Feeds [gtm.md](gtm.md), [channel_plan.md](channel_plan.md) and the `financials/` price threshold.

---

## 1. Method and its honest limits

Bottom-up: **units × frequency × price**, where the unit is a beachhead analyst and the price is anchored to what comparable products actually charge. Top-down is used only as a sanity check, never as the primary number.

**The methodological problem, stated first because it bounds everything below.** There is **no authoritative headcount for "enterprise data analyst."** BLS has no such SOC code `[S71]`; the role is distributed across data scientists, operations research analysts, management analysts and several computer occupations. What follows is therefore a *floor derived from two clean occupations* plus an extrapolation, and the extrapolation is where the uncertainty lives. Every extrapolated factor carries an explicit tag.

## 2. Bottom-up

### 2.1 The sourced floor

| Factor | Value | Source |
|---|---|---|
| US data scientists, 2025 | 275,600 | `[S69]` |
| US operations research analysts, 2025 | 113,100 | `[S70]` |
| **US sourced floor** | **388,700** | sum |

This is a genuine floor and not the beachhead. It excludes the large population who do this work under titles BLS codes elsewhere, and it includes people who are not the beachhead — a data scientist at a research lab is not an enterprise analyst absorbing an ad-hoc queue.

### 2.2 The assumption chain to a beachhead count

Four factors, multiplied. Each is tagged, and §5.1 shows what happens when they are wrong.

| # | Factor | Value | Basis |
|---|---|---|---|
| a | US sourced floor | 388,700 | `[S69][S70]` |
| b | Share working inside an organisation with a deployed BI stack and an ad-hoc request queue | **60%** | *(assumption: the beachhead is defined in BRIEF.md as already owning a BI stack. The Futurum frame — organisations above $100M revenue `[S17]` — and the observation that roughly 25% of employees use purchased BI tools `[S22]` bracket this loosely. No direct measurement exists.)* |
| c | Under-count correction for analysts coded outside these two SOC codes | **×1.6** | *(assumption: BLS has no data-analyst code `[S71]`; the correction is a judgement, not a measurement. It is the single weakest factor in this file.)* |
| d | US share of the addressable global market | **30%** | *(assumption: standard enterprise-software US-share heuristic. Unsourced.)* |

**Arithmetic.**

```
US beachhead      = 388,700 × 0.60 × 1.6           =   373,152  ≈ 373,000
Global beachhead  = 373,152 ÷ 0.30                 = 1,243,840  ≈ 1,240,000
```

**Global beachhead ≈ 1.24M analysts**, of which **≈373,000 are in the US**. One sourced factor, three assumed.

### 2.3 Price anchors

Real prices from the teardown, not invented:

| Anchor | Price | Source |
|---|---|---|
| Snowflake Cortex Analyst | 6.7 credits per 100 messages, at $2.00 per AI Credit ⇒ **≈$0.134 per message** | `[S38][S39]` |
| ThoughtSpot Pro | $50/user/month, Spotter capped at 25 queries/user/month | `[S44]` |
| ThoughtSpot Enterprise | ≈$137,000/year average contract | `[S45]` |
| Hex | $36–75 per editor/month | `[S52]` |

Two facts these anchors establish. First, **the market already prices the question**, not just the seat — Cortex bills per message on success `[S37][S38]` and ThoughtSpot meters Spotter queries `[S44]`, which validates the brief's *unit of value*. Second, the analyst-tool seat price clusters at **$50–75/month**.

**Chosen modelling price: $75/analyst/month ($900/year)** *(assumption: top of the observed analyst-tool band `[S44][S52]`, justified by spanning sources rather than one warehouse; not a validated willingness to pay, and the `financials/` layer treats it as a falsifiable threshold, not a forecast.)*

### 2.4 TAM, SAM, SOM

**TAM — every beachhead analyst globally, at the modelled price.**

```
1,240,000 analysts × $900/year = $1.116B/year   ≈ $1.1B
```

**SAM — what this product can actually serve.** Three successive restrictions, each traceable to a decision already made:

| Restriction | Factor | Why |
|---|---|---|
| English-language product, day one | ×0.55 | *(assumption: no localisation in scope for a capstone.)* |
| Organisation's questions genuinely span more than one source | **×0.50** | The positioning's load-bearing condition ([positioning.md](positioning.md) §4 residual). **This is the factor most likely to be wrong, in either direction, and it is the one discovery must measure.** *(assumption: unmeasured.)* |
| Data scope reachable at launch — CSV/Excel, REST JSON, Postgres | ×0.40 | From BRIEF.md's stated day-one connector scope. Excludes analysts working solely in Snowflake, BigQuery or Databricks, who are better served by the native assistant |

```
SAM = $1.116B × 0.55 × 0.50 × 0.40 = $122.8M/year   ≈ $123M
```

**SOM — realistically obtainable.** Stated honestly for what this is: an academic project with no revenue, no sales function and no customers.

**Three-year SOM if the venture were pursued commercially: $1.2M ARR** — approximately **1% of SAM**, or ≈1,370 paying analyst seats. *(assumption: a bottom-up capacity estimate, not a forecast. It is what a small open-source-led team could plausibly convert, and it is stated as a target to be falsified rather than a projection.)*

**SOM for CMPE 295A/295B: $0.** Per ASSUMPTIONS A1, monetisation is out of scope; the financials layer covers cost-to-serve and a price threshold, not revenue. **No artifact in this pack may present the $1.2M figure as a projection.**

## 3. Top-down sanity check

The BI market is estimated at $39.79B–$50.4B for 2026 with CAGRs from 8.67% to 14.98%, depending on the firm `[S26][S27][S28]` — a spread wide enough that the disagreement is itself the finding, and the reason to report a range rather than pick one.

**The check:** a $1.1B TAM is **2.2–2.8% of the 2026 BI market**. Is that plausible for "analyst-seat tooling for cross-source verified investigations"?

Yes, and the direction of error is informative. The BI market's revenue is dominated by platform licences and warehouse consumption sold to organisations, not by analyst-seat tools. A single-digit-percent slice for a niche analyst tool is the right order of magnitude. **If this number had come out at 20% of the BI market, the sizing would be wrong** — that would be an existing-market claim, which [market_type.md](market_type.md) explicitly rejects.

## 4. The beachhead, sized separately

Per the skill's requirement and because the re-segmentation stands or falls here.

**Definition.** Enterprise data analysts who (i) already own a BI stack and write SQL, (ii) absorb an ad-hoc request queue, (iii) work across at least one source outside the primary warehouse, and (iv) are at an organisation where a wrong answer reaching a stakeholder carries a real cost.

```
Beachhead = 373,000 US analysts × 0.50 (multi-source) × 0.40 (day-one connector fit)
          = 74,600 analysts
          × $900/year
          = $67.1M/year US beachhead opportunity
```

**Initial obtainable beachhead — the number that matters for 295A/295B.** The first cohort is not sized in dollars but in conversations: **the first 10 design partners** come from this population, and [gtm.md](gtm.md) names them by type. The relevant sizing question for the capstone is not "how big is the market" but "are there 10 analysts who will give us an hour" — which is a discovery task, not an arithmetic one.

## 5. What this sizing actually says

### 5.1 Sensitivity — where the number breaks

Three of four factors in §2.2 are assumptions, and they multiply. Testing the two that matter most:

| Scenario | Change | TAM | SAM |
|---|---|---|---|
| **Base** | as modelled | $1.12B | $123M |
| Under-count correction is 1.0, not 1.6 | c: 1.6 → 1.0 | $0.70B | $77M |
| Only 25% of organisations have genuinely multi-source questions | SAM factor: 0.50 → 0.25 | $1.12B | $61M |
| Both | | $0.70B | $38M |
| Price is $50/month, not $75 | | $0.74B | $82M |

**The pessimistic-but-plausible corner is a $38M SAM.** That is the honest downside, and it is stated here rather than left for a reviewer to compute.

### 5.2 The conclusion, which is uncomfortable and should stay in

**This is a small market by venture standards.** A $1.1B TAM and a $123M SAM will not support a venture-scale outcome on the analyst-seat model alone, and the pessimistic corner is a third of that.

Three responses are available, and the pack should be explicit about which it takes:

1. **Accept it.** This is a CMPE 295A/295B capstone with monetisation deliberately out of scope (A1). A $123M SAM is far more than sufficient to justify a two-semester build, and the honest small number is worth more to an advisor than an inflated large one.
2. **Note where the larger market would be, without claiming it.** The value is per *investigation*, not per seat — and the incumbents already price that way `[S37][S38][S44]`. Consumption pricing across an organisation's whole question volume is a materially larger market than 1.24M seats. **It is not sized here because no volume data exists to size it with**, and inventing one would violate `quality-bar.md` property 2.
3. **Reject the sizing and re-expand to the BI market.** This would contradict [market_type.md](market_type.md) and [positioning.md](positioning.md) §6.1 and must not happen quietly.

**This pack takes response 1, and records response 2 as an unsized observation.** Response 3 is named so that a later phase cannot drift into it without noticing.

## 6. Decision

1. **TAM $1.1B / SAM $123M / SOM $1.2M three-year hypothetical, $0 for the capstone.** These are the only sizing numbers any artifact in this pack may use.
2. **Modelling price $75/analyst/month**, treated as a falsifiable threshold rather than a forecast, and carried to `financials/`.
3. **The multi-source factor (0.50) is the sizing's dominant uncertainty** and is the same open question as [positioning.md](positioning.md) §4's residual. One discovery finding moves both.

## Recommended next 3

1. **Take the $75/month anchor into `financials/pricing.md` as the threshold to falsify**, phrased as "what would have to be true for an analyst-seat at $900/year to clear cost-to-serve" — which is computable from the architecture, unlike a revenue forecast.
2. **Make the multi-source factor the first quantitative question in customer discovery.** It is the single input that moves SAM by 2× and simultaneously decides whether the positioning's neutrality argument has content.
3. **Put §5.2's response-1 framing into the advisor-facing narrative explicitly.** A capstone that says "this market is $123M and that is enough for what we are doing" is more credible than one claiming a slice of $40B, and it pre-empts the obvious challenge.
