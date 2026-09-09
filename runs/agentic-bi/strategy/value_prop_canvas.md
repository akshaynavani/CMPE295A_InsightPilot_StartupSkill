# Value proposition canvas

**What this is** — Osterwalder's customer profile (jobs / pains / gains) mapped against the value map (pain relievers / gain creators / products and services), for the three personas whose value proposition differs, with the top mappings ranked.
**Why it exists** — The pack now asserts that hop-level lineage is worth having. This file forces that assertion to attach to a *job someone is already trying to get done*, and exposes the places where it does not. Its specific job is to catch the failure where a product's best feature relieves a pain nobody ranked highly — which is what happened to Power BI Q&A, retired in December 2026 after a decade of shipping inside the most widely deployed BI tool on earth `[S40]`. Distribution did not save it; the curation-to-value ratio killed it.
**How to read it** — §5's ranked mapping is the output. A skeptic should attack the *fit strength* column there, and §6, which names the two pains this product does not relieve at all.
**Depends on / feeds** — Inherits personas from [personas.md](personas.md) and the UVP from [positioning.md](positioning.md) §5. Feeds the PRD's feature prioritisation, `narrative/one_pager.md`, and the discovery guide in `validation/`.

---

## 1. Why three personas and not five

[personas.md](personas.md) carries five cards. Two are excluded here deliberately:

- **Marcus (low edge)** shapes the design and does not buy. His questions arrive through Priya. A value proposition written for him is the ThoughtSpot bet, marked down 73.67% `[S46]`.
- **Tom (blocker)** has a veto, not a value proposition. His requirements are security constraints, satisfied by the A5 self-hostable decision.

The three that remain — Priya (user), Angela (buyer), Dr. Chen (high edge, internal credibility) — are the three whose *value* differs. Each gets a profile and a map.

## 2. Priya — senior data analyst *(beachhead)*

### Customer profile

| Jobs to be done | Type |
|---|---|
| Answer the ad-hoc question that just arrived, correctly, without derailing planned work | Functional — the core job |
| **Be able to defend the answer when someone challenges it** | Functional + emotional — the job behind the job |
| Avoid becoming the bottleneck her colleagues route around | Social |
| Reclaim attention for the modelling and instrumentation work she was hired for | Emotional |

| Pains | Severity |
|---|---|
| Fixed per-question overhead that does not amortise — locate, inspect schema, write, debug, clean, join, chart | **High** |
| Context-switching: the question arrives mid-task and the cost is the switch, not the query | **High** |
| The unmodelled source — the carrier CSV nobody has ever joined — costs disproportionately | **High** |
| Her existing copilot cannot compute a metric that is not already a measure `[S42]`, so it helps least exactly when the question is novel | Medium–High |
| Shipping an answer she has not fully checked, in a bad week | **Critical, rare** |

| Gains | Priority |
|---|---|
| An answer she will put her name on, sooner | **Must-have** |
| Seeing exactly what was done, at the grain where she doubts it | **Must-have** |
| Not having to re-derive to check | Must-have |
| The predictive question answered at all | Nice-to-have |
| Fewer "let me look tomorrow" replies | Nice-to-have |

### Value map

| Pain relievers | Relieves |
|---|---|
| Orchestrator plans and executes across her real sources, including the unmodelled CSV, without a pre-authored semantic artifact | Fixed overhead; the unmodelled-source pain; the copilot's bounded-scope wall |
| Per-handoff lineage — sources touched, query run, transform applied, method chosen — each separately inspectable and re-runnable | Verification cost; the checked-it-properly anxiety |
| Replanning when a result invalidates the plan | Silent wrong answers |

| Gain creators | Creates |
|---|---|
| Spot-check the one hop she doubts instead of reading the whole chain | Verified answer sooner |
| An answer that is a defensible artifact, not a number in a Slack message | Defensibility |
| ML agent attempts the predictive question with its choices exposed | The question she does not currently attempt |

**Products and services.** Conversational investigation surface; connectors for CSV/Excel, REST JSON and Postgres; the lineage view; override affordances.

## 3. Angela — VP Data & Analytics *(economic buyer)*

### Customer profile

| Jobs to be done | Type |
|---|---|
| Answer "can we rely on this number" without a two-day investigation | Functional — her actual job |
| Reduce the review burden on senior people | Functional |
| Show progress on the data-trust initiative | Social — she is measured on it |

| Pains | Severity |
|---|---|
| Two teams reporting different numbers to the board | **Critical** |
| Senior people spending hours re-deriving others' work — Dr. Chen's two hours | High |
| AI tools that accelerate output faster than they accelerate trust: 72% prioritise AI-assisted coding against only 24% prioritising AI-assisted testing and observability `[S16]` | High |
| Buying tools that go unused — ≈25% of employees use purchased BI tools, flat over seven years `[S22]` | Medium–High |

| Gains | Priority |
|---|---|
| Provenance answerable on demand | **Must-have** |
| A governance story that survives an audit conversation | Must-have |
| Adoption she can actually observe | Must-have |

### Value map

| Pain relievers | Relieves |
|---|---|
| Lineage as a first-class artifact, retained and queryable | Provenance; the audit conversation |
| Analyst-led adoption — Priya advocates before Angela signs | The shelfware pain |
| Self-hosted, inside her boundary, on her own model key (A5) | The data-egress question that ends deals |

| Gain creators | Creates |
|---|---|
| Cheaper senior review, measurable as time saved | Reduced review burden |
| Consumes an existing dbt or Cube semantic layer rather than replacing it `[S66]` | Protects the investment she is already making |

**The objection this map must survive.** *"I'm already buying a semantic layer for exactly this."* `[S17]` — the hardest commercial objection in the pack ([personas.md](personas.md) §5). The answer is in the last row: **complement, consume, do not replace.** A semantic layer says what a metric means; it does not say what happened, why, or what was done to find out.

## 4. Dr. Chen — staff data scientist *(high edge)*

### Customer profile

| Jobs | Pains | Gains |
|---|---|---|
| Judge whether someone else's analysis is sound | Cannot tell without redoing it — and redoing it takes two hours whether or not it was fine | Spot-check the specific step he doubts |
| Own the models that reach production | Automated modelling that hides target leakage | Target definition, split, and rejected alternatives all visible |
| Be the escalation point without being a bottleneck | Reviewing is invisible work that never ends | Override the ML agent's target and algorithm choices |

### Value map

| Pain reliever / gain creator | Addresses |
|---|---|
| Method-level lineage: target definition, train/test split, algorithms tried and rejected with reasons | The leakage objection — the strongest technical objection in the pack |
| Override affordances on the ML agent's choices | Being reviewed-into-irrelevance; makes him a user, not a critic |
| Re-runnable hops | Two-hour re-derivation becomes a five-minute spot-check |

**Constraint that must not be forgotten.** MLE-bench-class agents reach a 36.4% medal rate under a **12-hour budget** `[S9]` — not a conversational latency budget. The PRD must specify what the ML agent does in *minutes*: a baseline model, a feature suggestion, an honest uncertainty statement. Promising Dr. Chen more than that is promising something the field delivers only with twelve hours.

## 5. Ranked mapping — the fits that matter

Ranked by *pain severity × relief strength*, the only ranking that predicts adoption.

| Rank | Pain | Reliever | Persona | Fit strength |
|---|---|---|---|---|
| **1** | Cannot verify an answer without re-deriving it | Per-handoff, re-runnable lineage | Priya, Dr. Chen, Angela — **all three** | **Strong, and unproven.** The only mapping that serves every persona at once. It is also the exact claim Priya's objection denies, and it is untested |
| **2** | The unmodelled source costs disproportionately | Plan across heterogeneous sources with no pre-authored artifact | Priya | **Strong.** Directly attacks the incumbents' structural limit `[S32][S36][S42]`. Conditional on questions actually spanning sources — the row-1 test in [business_model_canvas.md](business_model_canvas.md) |
| **3** | Provenance not answerable on demand | Lineage retained as a queryable artifact | Angela | **Strong commercially, weak technically** — it is the same mechanism as rank 1, sold to a different buyer. Cheap to serve, and it is what converts a user's enthusiasm into a signature |
| **4** | Fixed per-question overhead | Automated fetch → analyze → visualize | Priya | **Medium.** Real, but this is the crowded part: Genie, Cortex, Copilot and Hex all attack it. Necessary, not differentiating — and A2 already concedes that automating what the analyst can already do is convenience, not leverage |
| **5** | The predictive question is not attempted | ML agent with exposed choices | Priya, Dr. Chen | **Weak-to-medium, high variance.** Widest capability gap in the landscape, and the least trusted by the person who must approve it. Deliberately not the differentiator (A2) |

**What the ranking says.** The top three mappings are all one mechanism — lineage — sold to three different people for three different reasons. That is a coherent value proposition and a concentrated risk: **the pack's top three fits share a single point of failure**, which is rank 1's untested premise.

## 6. Where the fit is weak or absent

Naming these is the file's real value.

1. **This does not relieve Marcus's pain.** The low edge cannot verify, so the product's central gain creator is inaccessible to him. His only path is an analyst's sign-off — which means the system must make sign-off cheap rather than make Marcus self-sufficient. Anything else is the bet the market marked down `[S46]`.
2. **It does not relieve the data-quality pain underneath everything.** 77% of organisations report data-quality issues and 91% say those issues affect performance `[S15]`. Perfect lineage over bad data produces a beautifully traceable wrong answer. **The product should say so** rather than let a buyer assume otherwise.
3. **It does not reduce Angela's headcount**, and pretending it might would be the fastest way to lose credibility with a buyer who has heard it before.
4. **Rank 4 is where competition actually lives.** The crowded pain is the one every incumbent already addresses. A demo that leads with rank 4 is a demo of a worse Genie.

## Recommended next 3

1. **Lead every demo and every narrative artifact with rank 1, never rank 4.** Rank 4 is table stakes and invites the comparison A6 forbids; rank 1 is the only mapping that serves all three personas.
2. **Test rank 1 before the PRD is written.** The top three fits collapse together if it is false, and the timed task in [business_model_canvas.md](business_model_canvas.md) row 2 settles it in an afternoon.
3. **Put §6.2 — lineage over bad data is still wrong data — into the PRD as an explicit non-goal.** Stating the limit is what makes the rest of the claim believable, and it pre-empts the reviewer who would otherwise raise it as a gotcha.
