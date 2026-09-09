# Go-to-market

**What this is** — Channel strategy by segment, the acquisition loop intended to compound, a CAC hypothesis per channel with payback logic, and the 90-day motion: first 10 customers by type, then first 100.
**Why it exists** — The positioning concedes the bundling advantage permanently ([positioning.md](positioning.md) §6.2): every buyer already owns a copilot bundled into a platform they pay for. A GTM that does not start from that concession will plan a motion that cannot run. The failure this prevents is the standard one — a channel list where every channel is equally weighted, which is a way of not deciding.
**How to read it** — §3 is the decision (one channel, first), §5 is the 90-day motion. A skeptic should attack §3's single-channel bet and §4's CAC numbers, which are assumptions with no funnel data behind them and are labelled as such.
**Depends on / feeds** — Inherits the beachhead from [personas.md](personas.md), the price from [market_sizing.md](market_sizing.md) §2.3, and the open-core decision from ASSUMPTIONS A5. Feeds [channel_plan.md](channel_plan.md), which computes the economics, and [sales_roadmap.md](sales_roadmap.md), which maps the buyer.

---

## 1. The constraint every channel decision starts from

Three facts bound this, and all three are decided upstream:

1. **The buyer already owns a competing product**, bundled and paid for. Every conversation starts by explaining why the thing they have is not this thing ([positioning.md](positioning.md) §6.2).
2. **The product is open-core and self-hostable** (A5), which makes the primary channel a repository rather than a sales team — and makes the first conversion an *install*, not a meeting.
3. **This is an academic project with no revenue and no sales function** (A1). The 90-day motion below is what a two-person capstone team can actually run, not what a funded company would.

## 2. Channels by segment

| Segment | Channel | Motion | Why this one |
|---|---|---|---|
| **Beachhead — Priya** | Open-source repository + technical writing | Self-serve: find → install → first successful investigation | She is technical, sceptical of vendors, and has already watched a licensed tool go unused `[S22]`. Wren AI reached 13,000+ stars and 10,000+ cloud users on exactly this motion `[S50]` |
| **Beachhead — Priya** | Analyst communities (dbt Slack, r/dataengineering, locally: the SJSU and Bay Area data meetups) | Participate, publish, do not pitch | Where the beachhead already reads. Requires credibility, which the published accuracy number supplies |
| **Buyer — Angela** | Analyst-led referral | Priya advocates internally; Angela is closed, not prospected | User ≠ payer (BRIEF.md). Prospecting Angela cold means competing with Databricks' account team |
| **Blocker — Tom** | Documentation | Self-hosted deployment guide, credential handling, audit log | He is satisfied by artifacts, not conversations |
| **High edge — Dr. Chen** | Technical depth: the whitepaper and the published benchmark | Credibility, not acquisition | He converts internal scepticism into internal advocacy |
| **Academic (295A/295B)** | Conference/poster + published multi-hop accuracy number | Publication | The one credible artifact the commercial market does not have ([research/sources.md](../research/sources.md), *Named gaps* 2) |

## 3. The acquisition loop that compounds

Most of the channels above do not compound. One does, and the GTM is a bet on it.

```
   Analyst installs the open core
              │
              ▼
   Runs an investigation on THEIR sources
              │
              ▼
   Investigation + lineage is shareable ──────┐
              │                                │
              ▼                                │
   Colleague/manager sees a verifiable         │
   answer, asks where it came from             │
              │                                │
              ▼                                │
   Second analyst installs ───────────────────┘
              │
              ▼
   Enough internal use that Angela is asked to fund it
```

**The loop's engine is that an investigation is a shareable artifact.** A dashboard is shareable and a chat answer is not; an investigation with its lineage is shareable *and* checkable, which is what makes forwarding it a professional act rather than a risk. This is the same mechanism as the differentiator, used as distribution — which is the strongest form of a GTM loop, because improving the product improves the loop.

**Where the loop breaks, honestly.** It requires the artifact to be shareable outside the tool. If lineage is only viewable inside a running instance, the loop has no edge from step 3 to step 4. **This is a product requirement disguised as a GTM requirement, and the PRD must carry it: an investigation must be exportable as a self-contained, readable artifact.** It is the single highest-leverage GTM decision in this file and it costs almost nothing to build early.

## 4. CAC hypothesis by channel

**Every number in this section is an assumption.** There is no funnel, no traffic and no conversion data — per ASSUMPTIONS A1 this venture has none, and inventing precision would violate `quality-bar.md` property 2. These are order-of-magnitude hypotheses stated so they can be falsified, and the payback logic matters more than the values.

Reference price: **$75/analyst/month = $900/year** ([market_sizing.md](market_sizing.md) §2.3).

| Channel | CAC hypothesis | Basis | Payback logic |
|---|---|---|---|
| **Open-source self-serve** | **≈$0 direct, high fixed cost** | The cost is engineering time on docs and the quickstart, not per-acquisition spend | Payback is immediate per user and the fixed cost amortises across all installs. **The only channel with sane economics at a $900 ACV** |
| **Analyst-led referral (internal)** | **≈$0** | The loop in §3 | Immediate. The compounding channel |
| **Community participation** | Low, time-denominated | Founder hours, not dollars | Payback in credibility, not directly attributable — do not try to attribute it |
| **Content / technical writing** | Low, front-loaded | One good benchmark write-up outlasts a year of posts | Compounds if it is genuinely technical; near zero if it is marketing |
| **Outbound sales** | **High — likely $3,000–8,000 per closed account** *(assumption: standard B2B enterprise ranges; no data)* | Enterprise sales motion against a bundled incumbent | **Fails at this ACV.** At $900/analyst/year, an account must reach 4–9 seats *just to repay acquisition* before any cost-to-serve. **Do not build this motion** |
| **Paid acquisition** | High, poor intent match | — | Not viable. The beachhead does not find infrastructure tools through ads |

**The conclusion this table forces.** At a $900 ACV, **only zero-CAC channels work.** That is not a preference, it is arithmetic, and it is why the open-core decision (A5) is a GTM decision as much as a positioning one. A managed-service-first product at this price would need outbound to reach the buyer and could not afford it.

## 5. The 90-day motion

### First 10 — by type, not by name

These are the design partners the pack needs; they are described by the properties that make them useful.

| # | Type | Why this one first |
|---|---|---|
| 1–3 | **Analysts inside the team's own network** — SJSU alumni and Bay Area contacts in analytics roles at mid-size companies | Reachable this week. They will give an honest hour, which is exactly what the [business_model_canvas.md](business_model_canvas.md) row 1 and row 2 tests need |
| 4–6 | **Analysts who have publicly complained about a copilot's limits** — in dbt Slack, on r/dataengineering, in issue threads on Wren AI or similar | Pre-qualified on the exact pain. They have already hit the bounded-scope wall `[S42]` and can say what they hit |
| 7–8 | **An analyst at an organisation with a genuinely heterogeneous stack** — warehouse plus operational Postgres plus a file feed | The only type that can test the neutrality argument. If none can be found, that is itself the answer to [positioning.md](positioning.md) §4's residual |
| 9–10 | **One staff data scientist** (Dr. Chen type) and **one analytics leader** (Angela type) | Not users — the credibility test and the budget test. Ask the buyer what line item this comes from ([business_model_canvas.md](business_model_canvas.md) row 5) |

**What "acquired" means for the first 10.** Not payment — a completed conversation plus, for at least four of them, a real question run against their own data. Payment is out of scope (A1).

### First 100

Reached by the §3 loop and one publication, not by sales:

1. **Publish the multi-hop accuracy number** with the fixed question set and the harness. No commercial agentic-BI product publishes one. This is the pack's single most distributable asset and it is a byproduct of the 295A spike rather than extra work.
2. **Ship the quickstart to first-successful-investigation in under 30 minutes**, and instrument it. If the median exceeds 30 minutes the self-serve motion has failed and the real motion is design-partner-led ([business_model_canvas.md](business_model_canvas.md) row 4) — which changes this entire file.
3. **Make the investigation exportable** (§3), so the loop has its edge.
4. **Answer "how is this not Genie" in the README**, above the fold. Every visitor arrives with that question; making them dig for the answer loses most of them.

### What is deliberately not in the 90-day motion

No outbound, no paid acquisition, no partnerships, no conference sponsorship, no landing-page optimisation. Each would consume the capstone's scarcest resource — engineering hours — to buy something the loop is supposed to produce for free. A GTM that lists every channel is not a plan.

## Recommended next 3 moves

1. **Build the export-a-shareable-investigation requirement into the PRD now.** It is the edge in the compounding loop, it is cheap early and expensive to retrofit, and without it §3 does not close.
2. **Run the first-10 conversations before phase 3 (product) is written** — or at minimum before 295B. The row-1 and row-2 tests from [business_model_canvas.md](business_model_canvas.md) live inside these conversations, and both can invalidate the strategy for the cost of ten hours.
3. **Treat the published benchmark as the GTM asset, not a research output.** Scope the 295A spike so the harness, the question set and the write-up are shippable artifacts. It is simultaneously the academic deliverable, the credibility proof for Dr. Chen, and the top of the first-100 funnel.
