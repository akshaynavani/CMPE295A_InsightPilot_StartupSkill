# Market type

**What this is** — A Steve Blank market-type declaration for InsightPilot: one choice among Existing, Re-segmented, New and Clone, defended from the phase 1 evidence, with the strategic consequences that follow from it.
**Why it exists** — Market type determines sales cycle, positioning approach, capital need and dominant risk, and getting it wrong is the most expensive early error a venture makes. The concrete failure it prevents here: treating this as an **existing market** would send the pack chasing feature parity with Databricks Genie and Power BI Copilot — a comparison this product loses on distribution before it starts — while treating it as a **new market** would license the pack to skip competitors entirely and invent adoption numbers. Both are wrong, and they are wrong in opposite directions.
**How to read it** — §2 is the decision; §3 is what it costs you. A skeptic should attack §2.3, which argues against the re-segmentation choice using the strongest counter-case, and §3's *dominant risk* row, which says the thing most likely to kill this is not competition.
**Depends on / feeds** — Inherits [research/competitors.md](../research/competitors.md) and [research/landscape.md](../research/landscape.md); constrained by ASSUMPTIONS [A5](../ASSUMPTIONS.md) and [A11](../ASSUMPTIONS.md), both closed at this gate. Feeds [positioning.md](positioning.md), [market_sizing.md](market_sizing.md), [gtm.md](gtm.md) and the validation layer's stage gates.

---

## 1. The four types, and why the answer is not obvious here

Blank's types are not labels but different *businesses*, each with its own dominant risk:

| Type | You are | Dominant risk | Sales cycle |
|---|---|---|---|
| **Existing** | Faster/better on a known axis, in a market with known buyers and known budget | Losing to incumbents on distribution | Shortest — buyer knows the category |
| **Re-segmented** | Same market, but redrawn — by niche or by a low-end/different-attribute reposition | Segment turns out not to be real, or too small | Medium — you must teach the *distinction*, not the category |
| **New** | Creating demand that did not exist | Nobody wakes up wanting this; adoption, not competition, kills you | Longest — you fund education |
| **Clone** | A proven model transplanted to a new geography or vertical | Execution and local dynamics | Short |

The reason this is genuinely ambiguous for InsightPilot: **the category is old and the capability is not.** Conversational access to enterprise data has been attempted since at least 2014, with a documented graveyard — Watson Analytics discontinued 2019, Narrative Science absorbed 2021, Sisu absorbed 2023, Power BI Q&A fully retired December 2026 `[S59][S58][S56][S57][S40]`. Budget exists, buyers exist, and the words "ask your data a question" need no explanation. That is an existing market by every conventional test.

But the thing being sold is not what that market buys. Every incumbent sells **a constrained answering surface over a pre-modelled source**; this sells **an investigation that spans sources and carries its own verification**. The buyer has budget for the former and no line item for the latter.

## 2. The declaration

> **Re-segmented market — by different attribute, not by low end.** InsightPilot re-segments conversational BI along the attribute of **verifiability across sources**, taking the enterprise data analyst as its beachhead rather than the business user the category has spent a decade failing to serve.

### 2.1 The evidence for re-segmentation

1. **The category's own low-end play has been tried and marked down.** ThoughtSpot is the purest expression of "let non-analysts self-serve via natural language" — well funded, early, technically credible — and cleared a June 2024 secondary at $6.80/share against a $25.83 Series F, a **73.67% markdown implying ≈$920M against a $4.2B November 2021 valuation** `[S46]`. A low-end re-segmentation into the business-user tier is a move this market has already priced. That is why the beachhead is the analyst.
2. **The attribute being re-segmented on is one the market is actively funding.** 59% of decision-makers at $100M+ organisations are directing incremental budget to semantic layers `[S17]`, and 24.9% name accuracy and hallucination risk as their top reservation about GenAI in analytics `[S17]`. Trust in data as a stated priority rose from 66% to 83% in a single year, and 71% of practitioners name incorrect or hallucinated output reaching stakeholders as a top concern `[S16]`. **The budget is moving toward verifiability.** Semantic layers are the market's current answer to that need; this product is a different answer to the same need.
3. **The incumbents cannot follow without contradicting their own design.** Every incumbent buys correctness by bounding scope — 30 tables per Genie Agent `[S32]`, a ~32K-token Cortex semantic model `[S36]`, existing-measures-only in Copilot `[S42]`, single-number metrics in Pulse `[S49]`. Removing those bounds reintroduces the unreliability they were bought to prevent ([research/competitors.md](../research/competitors.md) §3.3). A re-segmentation is durable exactly when the incumbent's strength is what stops it following.
4. **There is an unoccupied quadrant, and it is unoccupied for a reason the pack can state.** Many-hop execution with correctness carried in the answer is empty because multi-step data reasoning measures ≈14.55–16% on DABstep's Hard split against 76.39% Easy `[S4]`. The segment exists; the capability to serve it is marginal. That is the definition of a re-segmentation bet rather than an existing-market bet.

### 2.2 Why not the other three

**Not Existing.** In an existing market you win on a known axis against known competitors, and distribution decides. Power BI Copilot is bundled into the most widely deployed BI tool in the enterprise `[S42]`; Genie and Cortex are bundled into the warehouse the customer already pays for. On the existing market's axis — "answer my question about my warehouse" — this product cannot win, and should not try. No head-to-head accuracy claim is even available: no commercial agentic-BI product publishes a benchmark figure ([research/sources.md](../research/sources.md), *Named gaps* 2).

**Not New.** Tempting, and wrong. The words need no explanation, the budget line exists, and the graveyard proves demand was repeatedly *found* — Watson, Q&A and Sisu did not fail from nobody wanting the thing. Claiming a new market would license the pack to skip the teardown and invent an adoption curve, which is exactly the failure `quality-bar.md` property 3 exists to prevent. **A new-market claim would also be an admission of no evidence**, and the evidence here is good.

**Not Clone.** No proven model is being transplanted.

### 2.3 The strongest case against this declaration

Stated at full strength, because a market-type choice defended only by its supporting evidence is a rationalisation.

**The case:** re-segmenting on verifiability assumes verification cost is a purchase driver. It may be a *complaint* rather than a *budget*. The 71% who fear hallucinated output `[S16]` and the 24.9% who name accuracy as their top reservation `[S17]` are describing a reservation about adopting GenAI — not a stated willingness to buy a separate product to fix it. Note what those same buyers actually did with their money: **they funded semantic layers** `[S17]`, which is the incumbents' answer, inside the platforms they already own. The observed spending behaviour supports the incumbents' re-segmentation, not this one.

**The answer, and its limit.** The semantic-layer spend is evidence that verifiability is budgeted — which is the load-bearing half of the claim, and more than most re-segmentations can show. It is not evidence that it is budgeted *outside the incumbent platform*, and this pack cannot close that gap from desk research. **This is the first thing customer discovery must test**, and it is why [validation](../validation/) leads with verification cost rather than answer accuracy. Recorded as an open risk, not resolved here.

## 3. Strategic consequences of the choice

What re-segmentation commits this venture to. Each row is a decision the rest of the pack must honour.

| Dimension | Consequence for InsightPilot |
|---|---|
| **Sales cycle** | Medium. The buyer does not need the *category* explained — they have Copilot or Genie already. They need the **distinction** explained: why an answer that spans sources and carries a hop-level trace is a different purchase from a chat box over one warehouse. Expect the first conversation to be spent on "how is this not Genie," and budget for it in every narrative artifact. |
| **Positioning approach** | Against the *attribute*, never against the product. "The only conversational analytics layer that spans your sources and hands back a trace you can check hop by hop" — not "better than Genie." Comparative accuracy claims are forbidden (A6 constraint 4); there is no measurement to support one. |
| **Capital needs** | Moderate, and this is the type's advantage. Re-segmentation does not fund category education (new market) or a distribution war (existing market). For a two-semester capstone with no revenue this is the only type that is honestly executable — which is a reason to be suspicious of the choice, and the reason §2.3 is stated. |
| **Dominant risk** | **Not competition. Segment reality.** The named risk is that the segment "analysts who need cross-source verified answers" is smaller than it looks — because a real customer's questions turn out to live inside one warehouse anyway, in which case neutrality is true and worthless (ASSUMPTIONS A11 residual). Second is that verification is a complaint rather than a budget (§2.3). |
| **Pricing implication** | Price the **investigation**, not the seat or the token. Both incumbent shapes already point this way: Cortex Analyst bills per message on success only `[S37][S38]`, and ThoughtSpot caps Spotter at 25 queries per user per month `[S44]`. Carried to [financials](../financials/) as the price-threshold frame. |
| **Beachhead consequence** | The analyst, not the business manager. Non-negotiable, and the ThoughtSpot markdown `[S46]` is the evidence. The low edge in BRIEF.md's spectrum stays a *design constraint* that earns the conversational interface — it is not the first customer. |
| **What proves the type was right** | Analysts accepting an answer they did not derive, faster than they could re-derive it, on a question spanning at least two sources. That single observation validates the segment, the attribute and the differentiator together. It is the validation layer's first experiment. |
| **What would force a re-declaration** | If discovery shows analysts want a *faster single-warehouse* answer and do not value cross-source or lineage, this collapses to an Existing-market play against bundled incumbents — which is unwinnable on distribution, and would be a reason to change the product, not the marketing. |

## 4. Decision

**Re-segmented market, by different attribute (verifiability across sources), beachhead = enterprise data analyst.** Every downstream artifact inherits this. The three decisions it forces and which must not be quietly reversed later:

1. **Sell the distinction, not the category or the comparison.** No head-to-head claims.
2. **The analyst is the first customer.** The business manager is a design constraint, not a segment to sell to first.
3. **Segment reality is the dominant risk**, ahead of any competitor. Validation spends its first budget there.

## Recommended next 3

1. **Carry the attribute — verifiability across sources — into [positioning.md](positioning.md) as the axis**, and check it against the two axes phase 1 derived. If the positioning axes and the re-segmentation attribute disagree, one of them is wrong.
2. **Size the beachhead separately and bottom-up in [market_sizing.md](market_sizing.md)**, because the re-segmented segment — not the BI market — is the number that matters. A "1% of a $40B BI market" figure would falsify this whole declaration by implying an Existing-market play.
3. **Make §2.3 an explicit hypothesis on the business model canvas**, with its killing test: does any analyst pay for verifiability outside the platform they already own? It is the cheapest way to find out the market type is wrong before five more phases are built on it.
