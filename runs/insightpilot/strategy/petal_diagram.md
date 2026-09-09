# Petal diagram

**What this is** — Steve Blank's petal: InsightPilot at the centre, with the five adjacent markets it draws customers *from*, the incumbents in each, and what those customers currently spend.
**Why it exists** — A 2×2 asks where rivals sit. The petal asks a harder and more useful question: **which existing budget and which existing habit does this displace?** Because the buyer already owns a bundled copilot ([positioning.md](positioning.md) §6.2), this venture has no greenfield budget to win — every dollar comes out of a line item that exists. Without this file the GTM plans acquisition from a market that does not exist, and the sales roadmap has no answer to "what does this replace?"
**How to read it** — Petal 1 is where the customers actually come from, and it is the least obvious. A skeptic should attack §4, which argues that the largest petal by spend is the *wrong* one to draw from.
**Depends on / feeds** — Inherits the teardown from [research/competitors.md](../research/competitors.md) and the buyer from [personas.md](personas.md); prices from [market_sizing.md](market_sizing.md) §2.3. Feeds [gtm.md](gtm.md), [channel_plan.md](channel_plan.md) and [sales_roadmap.md](sales_roadmap.md).

---

## 1. The petal

```
                    ┌───────────────────────────────┐
                    │  2. WAREHOUSE-NATIVE           │
                    │     COPILOTS                   │
                    │  Genie · Cortex Analyst        │
                    │  Copilot · Pulse · Spotter     │
                    │  spend: bundled + AI credits   │
                    └───────────────────────────────┘
   ┌────────────────────────┐         ┌────────────────────────────┐
   │ 1. ANALYST TIME        │         │  3. SEMANTIC LAYER /       │
   │    (the real source)   │         │     METRICS TOOLING        │
   │ status quo: SQL by     │         │  dbt SL · Cube · AtScale   │
   │ hand · no vendor       │         │  spend: 59% of $100M+ orgs │
   │ spend: salary,         │         │  adding budget  [S17]      │
   │ unbudgeted             │         └────────────────────────────┘
   └────────────────────────┘
                    ┌───────────────┐
                    │  AGENTIC BI   │
                    └───────────────┘
   ┌────────────────────────┐         ┌────────────────────────────┐
   │ 5. DATA SCIENCE /      │         │  4. ANALYST NOTEBOOKS      │
   │    AutoML              │         │  Hex · Deepnote · Jupyter  │
   │ AutoML platforms ·     │         │  spend: $36–75/editor/mo   │
   │ internal DS headcount  │         │  [S52]                     │
   │ spend: headcount       │         └────────────────────────────┘
   └────────────────────────┘
```

## 2. Petal by petal

### Petal 1 — Analyst time *(the status quo; the real source of customers)*

**Incumbent:** the analyst writing SQL by hand. **Current spend:** salary — unbudgeted as tooling, and therefore invisible in every market-size report.

**What the customer currently does.** Absorbs the queue. Turnaround one to four weeks at enterprise scale `[S15]`, five to ten business days below 500 employees (Forrester, via `[S15]`).

**What would make them switch.** Not speed alone — the analyst's current method never fails on *correctness*, only on latency, and that asymmetry is why it is so durable ([research/competitors.md](../research/competitors.md) §2, row 2). They switch when an answer they did not derive becomes cheaper to *accept* than to write.

**Why this petal is the primary source.** No competing vendor has to lose for this venture to win a customer here, and no procurement cycle is triggered by an analyst installing an open-source tool. **This is the petal the open-core GTM (A5) is designed to harvest.**

**The catch:** there is no budget in this petal. Winning here produces users, not revenue — which is exactly right for a capstone (A1) and would be a real problem for a company.

### Petal 2 — Warehouse-native copilots

**Incumbents:** Databricks Genie, Snowflake Cortex Analyst, Power BI Copilot, Tableau Pulse, ThoughtSpot Spotter. **Current spend:** bundled into platform contracts, plus metered AI consumption — Cortex at ≈$0.134 per message `[S38][S39]`, ThoughtSpot Pro at $50/user/month with Spotter capped at 25 queries `[S44]`, enterprise contracts averaging ≈$137,000/year `[S45]`.

**What would make them switch.** Hitting the bounded-scope wall: a question spanning a source outside the platform, or a metric that is not already a measure `[S42]`. These customers are pre-qualified on the exact pain, which is why [gtm.md](gtm.md) §5 targets analysts who have publicly complained about copilot limits.

**Why this is not the primary petal.** The spend is bundled, so there is nothing to displace — cancelling Genie is not an option when it arrives with the lakehouse. **A customer from petal 2 adds this product; they do not switch to it.** Additive purchases are harder to justify than replacements, which is precisely the objection [market_type.md](market_type.md) §2.3 raises against the whole market-type declaration.

### Petal 3 — Semantic layer / metrics tooling

**Incumbents:** dbt Semantic Layer, Cube, AtScale, Honeydew; warehouse-native semantic views `[S66]`. **Current spend:** 59% of decision-makers at $100M+ organisations directing incremental budget here — 44.5% increasing, 14.4% newly adopting `[S17]`.

**This is the largest active budget in the diagram, and §4 argues it is the wrong one to draw from.**

### Petal 4 — Analyst notebooks

**Incumbents:** Hex, Deepnote, Jupyter. **Current spend:** $36–75 per editor/month `[S52]`; ≈$750/month for a ten-analyst team.

**What would make them switch.** Wanting a plan rather than a canvas. The notebook already delivers auditability structurally — every hop is a visible, re-runnable cell `[S54]` — so this petal's customers have already solved the verification problem by doing the work themselves.

**Why this is the most honest competitive petal.** These customers understand the value proposition immediately and are the hardest to win, because they have a working answer. **The budget here is real, displaceable and correctly priced** at roughly the level [market_sizing.md](market_sizing.md) models. It is the only petal where the spend, the buyer and the price all line up.

### Petal 5 — Data science / AutoML

**Incumbents:** AutoML platforms and internal DS headcount. **Current spend:** headcount, overwhelmingly.

**What would make them switch.** Nothing, in year one. MLE-bench-class agents reach a 36.4% medal rate under a 12-hour budget `[S9]` — real capability on a timescale that is not conversational. Per ASSUMPTIONS A2 the ML agent is deliberately not the differentiator.

**Why it is on the diagram anyway.** It is where the *expansion* revenue would come from if the venture were pursued, and it is the petal Dr. Chen guards. Naming it prevents a later phase from discovering it as if it were new.

## 3. Which petals to draw from, in order

| Rank | Petal | What you get | What it costs |
|---|---|---|---|
| **1** | **Analyst time (1)** | Users, adoption, the compounding loop, and honest product feedback. No procurement, no competitive displacement | No revenue. Wholly appropriate for the capstone (A1); a real constraint for a company |
| **2** | **Analyst notebooks (4)** | The only petal where budget, buyer and price all align. Displaceable spend at the right ACV | The hardest customers to convince — they already have a working answer in Hex `[S54]` |
| **3** | **Warehouse copilots (2)** | Pre-qualified pain, easy to find, loud about their limits | Additive spend, not replacement. Bundled incumbent cannot be cancelled |
| 4 | Semantic layer (3) | The largest active budget `[S17]` | **Wrong budget — see §4** |
| 5 | Data science (5) | Expansion story | Not year one |

## 4. Why the largest budget is the wrong one to draw from

The semantic-layer petal has the most money moving in it right now `[S17]`, which makes it the obvious target and the wrong one.

**Drawing from petal 3 means telling Angela that the thing she is currently funding is unnecessary.** It is not — a semantic layer answers *what does this metric mean*, which this product does not answer and depends on. Positioning against it would be both false and self-defeating: the highest-leverage integration available is **consuming** an existing dbt or Cube layer to inherit correctness work the customer already paid for ([business_model_canvas.md](business_model_canvas.md) row 8).

**The strategic form of the point:** petal 3 is a *supplier petal*, not a source petal. Its budget is large precisely because it buys something adjacent and complementary. A venture that mistakes an adjacent budget for a displaceable one picks a fight with the buyer's existing decision — and Angela's hardest objection is already *"I'm buying a semantic layer for exactly this"* ([personas.md](personas.md) §5). Answering it with "you shouldn't be" loses the deal.

## 5. What the petal says that the 2×2 did not

[positioning.md](positioning.md)'s axes show an empty quadrant. The petal shows something the quadrant map cannot: **the empty quadrant has no budget attached to it.**

Customers come mostly from petal 1, where the spend is salary and invisible; the aligned budget is in petal 4, which is the hardest petal to win; and the largest budget, petal 3, is a supplier rather than a source. That is a coherent picture, and it is a harder one than the quadrant map implies.

Three consequences:

1. **Adoption will precede revenue by a long way**, structurally — because the primary source petal has no budget line. For the capstone that is not a problem; for the venture framing in `narrative/`, it must be stated rather than glossed.
2. **The Hex comparison is the one to prepare for**, not the Genie comparison. Genie is the question everyone asks; Hex is the competitor whose customers have the budget and the understanding.
3. **The buyer conversation is a budget-source conversation**, which is exactly the test in [business_model_canvas.md](business_model_canvas.md) row 5: *if you bought this, what line does it come out of, and what does it displace?*

## Recommended next 3

1. **Target petals 1 and 4 in the first-10 design partners**, not petal 2. [gtm.md](gtm.md) §5 currently leans toward copilot-frustrated analysts because they are easy to find; the petal says notebook users are the more informative conversation.
2. **Make "consumes your existing semantic layer" a first-class product claim**, not an integration footnote. It converts the largest petal from a competitor into a supplier and defuses the buyer's hardest objection.
3. **Put "what line item does this come from" in the discovery guide verbatim.** §5 says the answer is genuinely unclear, and a buyer who cannot name a line has answered the market-type question ([market_type.md](market_type.md) §2.3) more decisively than any survey could.
