# Journey — one ordinary day, all touchpoints

**What this is** — A single Tuesday across every actor: Priya using the product, Marcus consuming from it, Dr. Chen reviewing through it, Tom watching it from the outside, and Angela — who never opens it — deciding whether to fund it.
**Why it exists** — The other three journeys each follow one person having a good session. A product is not a session; it is what happens when five people with different stakes touch the same system on a day nobody planned. This file exists to expose the interactions the single-persona journeys hide: the review queue backing up, the security scan nobody scheduled, and the buyer forming an opinion from artifacts rather than usage. It is also where `payer ≠ user` stops being a bullet in [BRIEF.md](../../BRIEF.md) and becomes a sequence of events.
**How to read it** — Follow the clock. A skeptic should attack 11:40, where the review queue nearly recreates the bottleneck the product exists to remove, and §3, which tallies what the day actually cost.
**Depends on / feeds** — All five personas from [strategy/personas.md](../../strategy/personas.md); the sales process from [strategy/sales_roadmap.md](../../strategy/sales_roadmap.md) §4. Feeds [ux_spec.md](../ux_spec.md)'s notification and queue states, and the `validation/` funnel.

---

## Tuesday

### 07:50 — Tom, data platform lead *(the actor who is not a user)*

Not a session. A scheduled quarterly access review.

He filters the audit log (#18) for the last 30 days: every query the system issued, to which source, under which role, for which investigation. 412 queries, all `SELECT`, all under the read-only role he provisioned.

He checks one thing specifically: whether anything hit the `hr_` schema. Nothing did — the role cannot see it, and the log confirms the system never tried.

**Component:** audit log (#18), permission inheritance (#30).
**Written:** access review record, external to the product.
**Elapsed: 8 minutes.** Last quarter's review of a different AI tool took him a day and a half, because it had no readable log and he had to reconstruct activity from warehouse query history. **This is the entire content of his approval** — not a conversation, an artifact.

### 09:15 — Priya, senior analyst

Three requests waiting. She triages by whether she can answer them at all.

| Request | What she does | Component |
|---|---|---|
| *"Q3 cost per shipment by carrier"* | Reopens `inv_4471` from six weeks ago, asks it as a follow-up. Three hops, 90 seconds, bindings already resolved | Context inheritance (#16) |
| *"Which accounts are at churn risk"* | New investigation. She knows this needs Dr. Chen's eyes, so she runs it and sends it on rather than concluding | ML agent (#32), export (#15) |
| *"Why is the West warehouse over-utilised"* | **She writes the SQL herself.** Single source, familiar schema, she knows the answer's shape in advance | — |

**The third row matters more than the first two.** She used the product for two of three requests and correctly bypassed it for the one where her own SQL is faster. **A product that fought that instinct would be worse**, and PRD non-goal 9 concedes the single-source familiar case explicitly.

### 09:52 — Marcus, regional director

Types his forecast question from his phone between meetings. Answer in under a minute, with the amber **"not yet reviewed by an analyst"** bar (#24). He taps *send for review* and goes into his 10:00.

**Written:** `inv_5203`, `reviewed: false`, review request queued to the analytics team.
**His attention cost: 90 seconds.**

### 10:30 — Priya, interrupted

Review request from Marcus arrives. **She does not stop what she is doing** — this is the design working: it is a queued artifact, not a Slack message demanding a context switch.

### 11:40 — the queue moment

Three review requests are now waiting: Marcus's, one from another stakeholder, one from a junior analyst. Priya batches them.

| Review | Time | What happened |
|---|---|---|
| Marcus's forecast question | 5 min | Hops green, binding sensible, signed off |
| Second stakeholder | 4 min | Signed off |
| **Junior analyst's** | **14 min** | Hop 3 verification amber — a fan-out join inflating row counts. She overrides, re-flows, signs off, and messages the junior analyst about the grain |

**Total: 23 minutes for three investigations.**

**This is the beat the whole design is bet on, and it is the one most likely to fail.** Three reviews at 23 minutes works. Fifteen reviews at 23 minutes would not — the gate would have recreated the bottleneck the product exists to remove, with the added insult that Priya is now doing verification instead of analysis.

Two things keep it viable, and both are contingent:

1. **Reviewing is structurally cheaper than deriving** — 5 minutes against 90. That is O2, and it is untested.
2. **The flywheel reduces future review load.** The junior analyst's grain error becomes a persisted binding; the same fan-out will not recur on that source. Override-rate trend (#42) is how anyone would know whether that is real.

**If either fails, this journey is where it shows first** — which makes review-queue depth a metric the validation layer should watch, not just a UX detail.

### 13:20 — Dr. Chen, staff data scientist

Opens the churn investigation Priya sent at 09:15. The full review is [edge_high.md](edge_high.md); here it is one item in a day: **19 minutes**, one override on `support_ticket_count` for the April ticketing migration, signed off with a note.

**Written:** `ds_reviewed_by: wei.c`, override annotated as a data-provenance issue, persisted to bindings.

His calendar afterwards shows a two-hour block he had reserved for this, now free. **He does not attribute that to the product** — he attributes it to the analyst having done the work properly. That misattribution is fine and worth noting: the product's value at the high edge is invisible by design, which makes it hard to measure and easy to under-credit in a renewal conversation.

### 15:00 — Angela, VP Data & Analytics *(the payer, who has still not opened the product)*

Her quarterly data-trust review with the CFO is Thursday. She needs to answer one question: *can we rely on these numbers?*

She does not log in. She asks Priya for evidence, and gets three things:

1. **Twelve exported investigations** from the last month, each self-contained with its plan, hops, queries and sign-off (#15).
2. **Tom's access review** from this morning — 412 queries, all read-only, nothing outside the provisioned role.
3. **A number**: 68% of ad-hoc requests in the last month reached a signed-off answer within one business day, against a prior baseline she remembers as roughly a week.

**Component:** export (#15), audit log (#18), investigation history (#28).
**Written:** nothing — she is a consumer of the record, which is precisely the point.

**Her decision is formed entirely from artifacts.** Not a demo, not a login. This is why feature #15 carries four jobs and why [strategy/sales_roadmap.md](../../strategy/sales_roadmap.md) puts the budget conversation at step 7 rather than step 1 — by the time Angela is asked to pay, the evidence already exists without anyone having assembled it for her.

**Her unresolved objection stands.** *"I'm already buying a semantic layer for exactly this."* Nothing today answered it. It gets answered when the dbt consumption demo (#23) exists — which is why that feature is Next-tier and not Later.

### 17:30 — Priya, end of day

She looks at what she cleared: five investigations run, three reviews signed off, one question answered in raw SQL because that was faster.

The thing she notices is not speed. **It is that she said "let me look tomorrow" zero times today.**

## 2. Every component that fired

| Actor | Components |
|---|---|
| **Tom** | Audit log (#18), permission inheritance (#30) |
| **Priya** | Investigation surface (#16), context inheritance (#16), Orchestrator (#5), plan surface (#6), fetch (#7), analytics (#8), lineage capture (#9), per-hop verification (#13), lineage surface (#10), override (#21), replanning (#20), single-hop re-run (#14), sign-off (#24), export (#15), ML agent (#32) |
| **Marcus** | Investigation surface, ambiguity interception (#11, adaptive phrasing), plan surface (collapsed), answer, **sign-off state (#24)**, export gating, share (#36) |
| **Dr. Chen** | Export artifact (#15), plan surface, lineage surface (#10), single-hop re-run (#14), method-level ML lineage (#39), ML override (#40), sign-off (#24) |
| **Angela** | Export artifacts (#15), audit log (#18), investigation history (#28) — **all read, none authored** |

**Two of five actors never generate an investigation.** Angela and Tom consume the record exclusively. That is a real product surface — the *record* is as much a deliverable as the answering loop — and it is easy to under-build because it serves nobody who is in the room during a demo.

## 3. What the day cost, honestly

| Actor | Time in the product | Prior equivalent |
|---|---|---|
| Priya | ~55 min across 5 investigations + 23 min reviewing | Roughly a full day for the same output, on her own estimates |
| Marcus | 90 seconds + a 2h wait | Three days, or a guess |
| Dr. Chen | 19 min | 2 hours |
| Tom | 8 min, quarterly | 1.5 days for a comparable tool |
| Angela | 0 min | An investigation she could not previously run at all |

**The gain is real and it is not evenly distributed.** Dr. Chen and Tom get order-of-magnitude reductions; Marcus gets a category change from *guess* to *attributed answer*; **Priya gets a smaller gain than anyone**, because she absorbs the review burden the other four shed.

That is worth staring at. **The beachhead — the person the product is built for and sold through — captures the least value on any single day.** Her compensation is the thing she noticed at 17:30 and the flywheel reducing tomorrow's review load. If neither materialises, the champion has been given work while everyone else got leverage, and adoption stalls at exactly the person it needs most.

**This is the sharpest risk in the pack and it is not in the risk register yet.** It belongs there — `validation/` should watch analyst review-time-per-week as a first-class metric, not merely time-to-verified-answer.

## 4. What this day does not show

1. **A bad day.** No source down, no model provider outage, no investigation that runs eleven hops and produces nothing. The failure day would be more informative and belongs in the validation layer's scenarios.
2. **A silent wrong answer surviving review.** O4's failure mode by construction — the day it happens looks exactly like this one, which is why the metric needs seeded errors (#2) rather than observation.
3. **The second analyst.** The GTM loop's whole premise ([strategy/gtm.md](../../strategy/gtm.md) §3) is that an exported investigation recruits a colleague. Nobody was recruited today.
4. **Any monetisation.** Angela formed an opinion; she did not sign anything. Per ASSUMPTIONS A1 that is correct scope, and it means this day contains no revenue event at all.
