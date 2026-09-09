# Sales roadmap

**What this is** — Blank's Customer Validation Phase 1 set: the **organisation map** (who sits where in the buyer), the **influence map** (who actually sways the decision), the **access map** (how a stranger reaches them), and the sales process with the artifact required at each step.
**Why it exists** — [channel_plan.md](channel_plan.md) concluded that the only viable channel produces users rather than revenue, which means every dollar this venture could earn arrives through **internal expansion** — an analyst persuading a budget owner. That is a sales process whether or not anyone is called a salesperson, and it is the one this pack has not yet described. Without it, the first-10 conversations get run without knowing who in the room can say no, and the buyer objection that ends deals gets discovered in the meeting rather than before it.
**How to read it** — §2 (influence map) is the useful part; §4 is the process. A skeptic should attack §2's claim that the analyst, not the buyer, is the decisive actor, and §5, which states what is unknowable before discovery.
**Depends on / feeds** — Inherits the five actors from [personas.md](personas.md), the motion from [gtm.md](gtm.md) and the economics from [channel_plan.md](channel_plan.md). Feeds `validation/discovery_guide.md` and the `narrative/` objection handling.

---

## 1. Organisation map — who sits where

A representative mid-size enterprise buyer (2,000–5,000 employees, central analytics team of five to fifteen). Titles vary; the *positions* do not.

```
                          CFO  /  COO
                               │  budget authority above ~$50K
                               ▼
                    ┌──────────────────────┐
                    │  VP Data & Analytics │   ← ANGELA · economic buyer
                    │  owns ~$3.1M budget  │      signs; does not use
                    └──────────┬───────────┘
                    ┌──────────┴────────────┬─────────────────────┐
                    ▼                       ▼                     ▼
      ┌─────────────────────┐   ┌──────────────────┐   ┌──────────────────┐
      │ Analytics Manager   │   │ Data Platform    │   │ Staff Data       │
      │ runs the queue      │   │ Lead — TOM       │   │ Scientist — CHEN │
      │ · day-to-day owner  │   │ · security veto  │   │ · technical      │
      └──────────┬──────────┘   │ · no budget      │   │   credibility    │
                 ▼              └──────────────────┘   └──────────────────┘
      ┌─────────────────────┐
      │ Data Analysts       │   ← PRIYA · user and champion
      │ (5–15)              │      installs; advocates; cannot buy
      └─────────────────────┘

   Business stakeholders (MARCUS et al.) sit outside this tree entirely.
   They generate the demand and have no say in the purchase.
```

**Two structural facts.** The person who feels the pain most acutely (Priya) has no budget authority, and the person with budget authority (Angela) never experiences the product. That gap is the sale. Second: **Tom can end the process without being in it** — a security veto needs no budget and no meeting.

## 2. Influence map — who actually sways the decision

Organisation charts show authority; they do not show influence. Ranked by ability to change the outcome:

| Rank | Actor | Power | How it is exercised | What they need from you |
|---|---|---|---|---|
| **1** | **Priya (analyst)** | **Decisive** — creates the demand that starts everything | She is already using it. The purchase request originates with her; nothing happens without it | An answer she will stake her name on, and a trace she can show |
| **2** | **Angela (VP)** | Authority — signs | Approves, or does not | A budget line this comes from, and a governance story |
| **3** | **Tom (platform/security)** | **Veto** — asymmetric | One "I'm not comfortable with this having read access to production" ends it | Self-hosted deployment, credentials that never leave the boundary, readable audit log |
| **4** | **Dr. Chen (staff DS)** | Credibility gate | Angela asks him whether it is sound. His answer is the technical due diligence | Method-level lineage, override affordances, and no leakage |
| **5** | **Analytics Manager** | Practical gatekeeper | Owns the queue and the team's time; can starve a rollout by not allocating any | Evidence it reduces the queue rather than adding a tool to learn |
| — | **Marcus (business stakeholder)** | None in the purchase | Generates demand; is never consulted | — |

**The claim this map makes, and it is contestable.** The analyst is ranked above the budget owner. The justification: in an open-core self-serve motion the product is already in use before any purchase conversation exists ([gtm.md](gtm.md) §3), so Angela is not deciding whether to *try* something — she is deciding whether to formalise something her team already relies on. That is a materially easier decision and a materially different sale.

**Where the claim breaks.** If the security veto (rank 3) fires before adoption spreads, the analyst never gets the chance to advocate. **Tom is therefore the first actor to satisfy, chronologically, despite being third by influence** — which is the commercial content of the A5 self-hostable decision, and the reason it is a GTM decision and not only a positioning one.

## 3. Access map — how a stranger reaches each actor

Cold access to Angela is not available to this team and should not be attempted; it means competing for attention with Databricks' account team. Every viable path runs through the product.

| Actor | Cold-reachable? | Actual access path | Cost |
|---|---|---|---|
| **Priya** | **Yes** | Open-source repository; dbt Slack, r/dataengineering; analyst meetups; the published benchmark. **This is the only cold-access path in the whole map** | Founder hours |
| **Tom** | No | Reached through documentation before he is reached through conversation. He evaluates artifacts, not pitches | Docs engineering |
| **Dr. Chen** | Weakly — via technical publication | The whitepaper and the published multi-hop accuracy number. He is convinced by method, not by demo | Comes free with the 295A spike |
| **Angela** | **No** | Introduced by Priya after internal use is established. Never prospected | Time — 3–9 months from first install *(assumption)* |
| **Analytics Manager** | No | Through Priya, or through observing the queue shorten | — |

**The single conclusion.** There is exactly one door: the analyst, reached through open-source distribution and technical credibility. Everything else in this map is reached *after* that door opens. That is why [channel_plan.md](channel_plan.md) runs one channel and why outbound is ruled out — there is no second door to spend money on.

## 4. The sales process, with required artifacts

| # | Step | Who | Artifact required | How you know it worked |
|---|---|---|---|---|
| 1 | **Discovery of the tool** | Priya | README that answers *"how is this not Genie?"* above the fold; a quickstart under 30 minutes | Clone → first successful investigation, instrumented ([business_model_canvas.md](business_model_canvas.md) row 4) |
| 2 | **First real investigation** | Priya | Working connectors for CSV/Excel, REST JSON, Postgres; the lineage view | She runs a *real* question, not the sample |
| 3 | **Verification moment** | Priya | Hop-level trace she can spot-check | **She accepts an answer she did not derive.** The pivotal event in the entire funnel — everything downstream depends on it, and it is the untested claim |
| 4 | **Sharing** | Priya → colleague | **Exportable, self-contained investigation artifact** | A second analyst installs. The loop closes ([gtm.md](gtm.md) §3) |
| 5 | **Security review** | Tom | Self-hosted deployment guide; credential-handling doc; audit log; data-flow diagram | No veto. Note Gartner attributes half of projected 2030 agent deployment failures to insufficient governance runtime enforcement `[S29]` — his caution is well founded |
| 6 | **Technical due diligence** | Dr. Chen | Whitepaper; published multi-hop accuracy number; method-level lineage on an ML output | He tells Angela it is sound |
| 7 | **Budget conversation** | Priya → Angela | **Objection-handling artifact for "I'm already buying a semantic layer"**; a governance story; usage evidence from steps 2–4 | Angela names a line item |
| 8 | **Close** | Angela | Pricing at the seat level; open-core boundary stated clearly | Signature |

### The two steps most likely to fail

**Step 3** is the venture. If Priya will not accept an answer she did not derive, steps 4 through 8 never occur — and her stated objection is precisely that verifying is not faster than rewriting ([personas.md](personas.md) §2). It is testable in an afternoon and has not been tested.

**Step 7** is the commercial failure point. Angela's objection — *"I'm already buying a semantic layer for exactly this"* `[S17]` — is the hardest in the pack, and the answer (complement, consume, do not replace) needs to be **a demo of the product reading her dbt layer**, not a sentence. That is a product requirement arising from the sales process, and it belongs in the PRD.

## 5. What this roadmap cannot know yet

Stated plainly, because a sales roadmap written before any customer contact is a hypothesis about a process, not a process.

1. **Whether the analyst-to-buyer path actually converts.** The entire model rests on internal advocacy, and no instance of it has been observed. The 3–9 month estimate is an assumption with nothing behind it.
2. **Whether Tom fires early or late.** If security review is triggered by the first install rather than by the purchase, step 5 moves to position 2 and the whole process becomes slower and harder. Self-hosting is the mitigation; whether it is sufficient is unknown.
3. **Whether accounts are 10 analysts or 50.** [channel_plan.md](channel_plan.md) §3.1 rules out outbound at a $9,000 ACV; a 50-analyst central team would change that verdict. One question, one conversation.
4. **Whether Angela has a line item at all.** [market_type.md](market_type.md) §2.3 raises this as the case against the market-type declaration itself. A buyer who cannot name a budget source has answered it.

All four are discovery questions, and all four are answerable in the first ten conversations ([gtm.md](gtm.md) §5).

## Recommended next 3

1. **Build the security artifact set for step 5 before the first external install**, not after. Tom's veto is asymmetric — it costs nothing to exercise and ends the process — and the artifacts are cheap to produce alongside the deployment work.
2. **Make "read my existing dbt semantic layer" a demoable capability**, because step 7's objection cannot be answered with words. It is also the highest-leverage integration in [business_model_canvas.md](business_model_canvas.md) row 8, so one build serves two purposes.
3. **Instrument step 3 as an explicit event**, not an inference from usage. *Analyst accepted an answer they did not derive* is the pack's central claim, the pivotal funnel event, and the metric the validation layer needs — and it is invisible unless it is deliberately captured.
