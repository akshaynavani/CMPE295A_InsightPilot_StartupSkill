# Get / Keep / Grow

**What this is** — The funnel per segment: how a user is acquired, what the activation moment is, the habit loop that retains them, the metric that predicts retention, and the mechanism by which one user becomes two.
**Why it exists** — [strategy/channel_plan.md](../strategy/channel_plan.md) concluded that at a $900 ACV **only zero-CAC channels survive**, which means growth has to come from a loop inside the product rather than from spend. This file is where that loop is specified precisely enough to instrument — and where it becomes visible that the loop has one edge that does not exist yet unless a specific feature ships.
**How to read it** — §2's Keep section is the load-bearing part; retention is where this product either works or is a novelty. A skeptic should attack §4, which concedes the funnel's weakest stage, and the target column throughout, which is aspirational by construction.
**Depends on / feeds** — Channels from [strategy/gtm.md](../strategy/gtm.md) §3, economics from [strategy/channel_plan.md](../strategy/channel_plan.md), the export feature from [product/features_flagship.md](../product/features_flagship.md) #18. Feeds [metrics_by_stage.md](metrics_by_stage.md) and [stage_gate.md](stage_gate.md).

---

## 1. The funnel in one line

**Get** an analyst through an open-source repo → **Keep** them through a verification habit that gets cheaper each week → **Grow** through an exported investigation that recruits the next analyst.

**There are no current numbers.** Every "Current" cell below reads `0` or `—` because nothing is deployed. Targets are declared in advance so they can be missed honestly.

## 2. Beachhead — the enterprise data analyst

### GET

| Stage | Metric | Current | Target | Lever |
|---|---|---|---|---|
| Reach | Repo visitors from analyst communities and the published benchmark | 0 | 500 in first 90 days | The **published multi-hop accuracy number** — no commercial product publishes one, so it is the only genuinely novel artifact the project can distribute |
| Interest | `git clone` | 0 | 100 | README answers *"how is this not Genie?"* above the fold. Every visitor arrives with that question |
| Setup | Connector configured | 0 | 60 | Docker Compose; Postgres + CSV only. Fewer choices, fewer failures |
| **ACTIVATION** | **First successful investigation against their own data** | 0 | **40** | Quickstart under 30 minutes — the E8 threshold |

**The activation moment is not the install.** It is the first time the system answers *their* question against *their* data and they believe the answer. Everything before it is setup cost; everything after is the product.

**Why this channel and no other.** At $900 ACV, outbound needs a 4–9 seat account just to repay acquisition ([strategy/channel_plan.md](../strategy/channel_plan.md) §3.1). Wren AI reached 13,000+ stars and 10,000+ cloud users on exactly this motion `[S50]` — proof the channel carries a product of this shape, and a reminder that it is already occupied.

### KEEP

| Stage | Metric | Current | Target | Lever |
|---|---|---|---|---|
| Habit | Investigations per analyst per week | — | ≥ 3 by week 4 | Context inheritance — a follow-up is 3 hops instead of 6 |
| **Trust** | **Hop-inspection rate** — share of investigations where at least one hop is opened | — | **20–60%** | The lineage surface |
| Compounding | **Override rate per source, trend** | — | Falling over 8 weeks | The binding store persisting corrections org-wide |
| Health | Analyst review-time per week | — | **< 4 h and flat** | Sign-off gate design — **A12's tripwire** |
| Retention | Analysts still running investigations at week 8 | — | ≥ 50% of activated | All of the above |

**Hop-inspection rate is the metric that predicts retention, and it is the least obvious one in this file.**

Both extremes are failures. **Near 0%** means the trace is decoration — they are trusting blind, which P3 says is unsafe, and the differentiator delivers nothing. **Near 100%** means they do not trust the system and are checking everything, which is re-derivation wearing a nicer interface. **The healthy band is 20–60%**: they check when something feels off, and the system's doubt surfacing tells them when.

No competitor has an analogous metric, because no competitor has a verify beat to instrument.

**Override-rate trend is the second-order signal.** If it does not fall as bindings accumulate, the flywheel is fictional (R10) and each week costs as much as the last. That is also the only evidence that would ever support the A3 moat candidate.

### GROW

| Stage | Metric | Current | Target | Lever |
|---|---|---|---|---|
| Share | Investigations exported or shared | — | ≥ 1 per active analyst per week | **Feature #18 — the exportable self-contained artifact** |
| Referral | Second analyst installs after receiving an export | — | ≥ 20% of deployments reach 2 analysts by week 12 | The export being *readable and checkable* by someone without the tool |
| Expansion | Analysts per deployment | — | 3+ by week 12 | Bindings already resolved make the second analyst faster than the first |
| Buyer | Deployments where a budget owner is asked to fund it | — | ≥ 10% by week 24 | Accumulated exports + audit log as the evidence pack |

## 3. The compounding loop, and the edge that does not exist yet

```
   Analyst installs
        │
        ▼
   Runs an investigation on THEIR sources   ← ACTIVATION
        │
        ▼
   Investigation + lineage exports as one readable file
        │                                    ← THE FRAGILE EDGE
        ▼
   Colleague receives a verifiable answer, asks where it came from
        │
        ▼
   Second analyst installs ──────────► loop closes
        │
        ▼
   Enough internal use that a budget owner is asked to fund it
```

**Why this loop is unusually strong in principle.** A dashboard is shareable but not checkable; a chat answer is neither. An investigation with its lineage is **shareable *and* checkable**, which makes forwarding it a professional act rather than a risk. The mechanism that differentiates the product is the same mechanism that distributes it — so improving one improves the other.

**Why it is fragile in practice.** The edge from *export* to *colleague sees it* **requires the artifact to be readable outside a running instance.** If lineage is only viewable inside the app, the loop has no edge there and growth reverts to whatever the repo can do on its own.

**That makes feature #18 a growth requirement disguised as a product feature** — the single highest-leverage build decision in the funnel, and cheap now versus expensive to retrofit onto a stateful UI.

## 4. Low edge — the business stakeholder

Not a segment to sell to (PRD non-goal 1), but they generate demand and they touch the funnel.

| Stage | Metric | Lever |
|---|---|---|
| Get | Questions submitted by non-analysts | Arrives via an analyst sharing a link, never via direct acquisition |
| **Keep** | **Review turnaround — question submitted to signed off** | Target < 4 hours. **This is the stakeholder's entire experience of the product** |
| Grow | Stakeholder questions per week | Rises as review turnaround falls — and **this is A12's feedback loop running the wrong way** |

**The concession this section has to make.** Stakeholder growth *increases analyst review load*. The funnel's most attractive growth vector is also the mechanism that could break Keep for the beachhead. That tension is unresolved, and [experiment_board.md](experiment_board.md) E5 is where it gets measured before it gets designed around.

## 5. Buyer — the analytics budget owner

| Stage | Metric | Lever |
|---|---|---|
| Get | **Never prospected.** Reached only through an analyst already using it | The evidence pack assembles itself: exports + audit log + review-time data |
| Keep | Provenance questions answerable without a two-day investigation | Investigation history, searchable by source touched |
| Grow | Additional analyst seats funded | Adoption she can observe, which is what her last shelfware purchase lacked `[S22]` |

## 6. What this funnel does not have

1. **No paid acquisition, ever, at this price.** Ruled out by arithmetic, not preference.
2. **No trial-to-paid conversion**, because monetisation is out of scope (A1). The funnel ends at *a buyer is asked to fund it* and stops there honestly.
3. **No virality outside the workplace.** The loop runs inside one organisation. This is not a product where a stranger sees an export and installs it — the artifact contains the customer's data.
4. **No numbers.** Every Current cell is `0` or `—`. **A funnel with invented conversion rates would be the clearest possible violation of this pack's standard**, and there is no traction to report.

## Recommended next 3

1. **Build feature #18 in the first sprint.** It is simultaneously the differentiator's proof, this funnel's only growth edge, the buyer's evidence pack and E1's measurement instrument. Four jobs, one artifact.
2. **Instrument hop-inspection rate from the first deployment.** It is the retention predictor, both extremes are failure states, and nobody else in the category can measure it.
3. **Set the A12 tripwire before the first stakeholder question arrives.** Analyst review-time above 4 h/week or trending upward is the signal that Grow is eating Keep — and by the time it is obvious from complaints, the champion has already stopped advocating.
