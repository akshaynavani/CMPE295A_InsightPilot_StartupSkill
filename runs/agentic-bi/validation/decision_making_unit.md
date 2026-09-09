# Decision-making unit — who can say no

**What this is** — The buying unit by role: user, payer, champion, saboteur, and everyone holding a veto. Per role: what they want, what they fear, what evidence moves them, and what kills the deal.
**Why it exists** — [strategy/personas.md](../strategy/personas.md) covers who *benefits*. This covers who can *stop it*, which is what actually stalls enterprise deals. The specific failure it prevents: a go-to-market built entirely around delighting the analyst, defeated in week three by a platform lead who was never in a meeting and needed only one sentence to end the process.
**How to read it** — §2's saboteur analysis is the part most likely to be dismissed and most likely to matter. A skeptic should attack §3's claim that the veto holder is satisfied by artifacts rather than conversations, and §5, which names the role this pack has probably underweighted.
**Depends on / feeds** — Roles from [strategy/personas.md](../strategy/personas.md); process from [strategy/sales_roadmap.md](../strategy/sales_roadmap.md). Feeds [discovery_guide.md](discovery_guide.md) §6 question 6 and the objection-handling artifacts the sales roadmap requires.

---

## 1. The unit at a glance

| Role | Who | Power | Can they alone say **yes**? | Can they alone say **no**? |
|---|---|---|---|---|
| **User / champion** | Priya — senior data analyst | Creates the demand that starts everything | **No** | Effectively yes — silence ends it |
| **Payer** | Angela — VP Data & Analytics | Signs | **Yes** | Yes |
| **Veto** | Tom — data platform / security lead | Asymmetric, costs him nothing to exercise | No | **Yes** |
| **Credibility gate** | Dr. Chen — staff data scientist | Angela asks him if it is sound | No | **Effectively yes** |
| **Saboteur** | The analytics manager | Controls his team's time | No | **Yes, quietly** |
| **Beneficiary, no vote** | Marcus — business stakeholder | Generates demand | No | No |

**Two of the six can end it without ever being in a meeting.** That is the file's whole point.

## 2. Role by role

### 2.1 Champion — Priya, senior data analyst

| | |
|---|---|
| **Wants** | An answer she will stake her name on, sooner. Her attention back for the modelling work she was hired for |
| **Fears** | Being handed a tool that generates work rather than removing it. She has watched a licensed rollout go unused before — roughly 25% of employees use the BI tools their employer bought, flat across seven years `[S22]` |
| **Evidence that moves her** | Running one of *her own* real questions against *her own* sources and catching a real defect. Not a demo — the activation moment |
| **What kills it** | Verification costing as much as re-derivation. Her words: *"I read SQL faster than I read explanations"* |
| **Her ask of us** | Do not make me the bottleneck for everyone else's questions |

**Her unusual position: she is the champion who captures the least value on any given day** (A12). Across one modelled Tuesday, the staff scientist goes 2h → 19min and the platform lead 1.5 days → 8min, while she absorbs the review burden the other four shed ([product/journeys/day_in_life.md](../product/journeys/day_in_life.md) §3). **A champion given work while everyone around them gets leverage does not advocate** — and the entire go-to-market routes through her advocacy.

### 2.2 Payer — Angela, VP Data & Analytics

| | |
|---|---|
| **Wants** | To answer *"can we rely on this number"* without a two-day investigation. Progress on a data-trust initiative she is measured on |
| **Fears** | Buying shelfware again. Being unable to explain provenance to the CFO |
| **Evidence that moves her** | Not a demo — **artifacts.** A dozen exported investigations, the platform lead's clean access review, and observable adoption she did not have to ask about |
| **What kills the deal** | *"I'm already buying a semantic layer for exactly this."* 59% of large enterprises are funding semantic layers `[S17]` |
| **Her decisive question** | *"Where does our data go?"* — answered by the self-hosted topology, on her own model key |

**Answering her objection requires a demo of the product reading her dbt layer, not a sentence.** "We consume yours, we do not replace it" is only credible when shown, which makes semantic-layer consumption a *sales* requirement as much as a product one.

### 2.3 Veto — Tom, data platform lead

| | |
|---|---|
| **Wants** | Not to be the person who signed off on the thing that leaked |
| **Fears** | Another agent with broad read access to production data, and his name on the approval. He has approved three AI tools this year and revoked one |
| **Evidence that moves him** | **Artifacts he can read without the product running.** A grep-able audit log; a read-only role he provisioned; a data-flow diagram showing one egress arrow; a configurable schema-only mode |
| **What kills the deal** | An opaque egress path, credentials held outside his boundary, or an audit trail that requires the vendor's UI to inspect |

**He is third in influence and first in sequence.** If security review fires on the first install rather than at purchase, he ends the process before Priya ever gets to advocate. That is the commercial content of the self-hosted decision — **it is a go-to-market decision as much as a positioning one.**

Gartner attributes half of projected 2030 AI-agent deployment failures to insufficient governance runtime enforcement `[S29]`. His caution is well founded, and the audit log is as much his artifact as Priya's.

### 2.4 Credibility gate — Dr. Chen, staff data scientist

| | |
|---|---|
| **Wants** | His two hours back from reviewing other people's analyses |
| **Fears** | Automated modelling shipping target leakage into production. He spent a year cleaning up exactly that |
| **Evidence that moves him** | A model card with the target definition in full, the split strategy, features excluded **with reasons**, and an exhaustive **not-attempted-in-budget** list |
| **What kills it** | **One undisclosed omission in that list.** It converts an honest renunciation into a lie by omission, and he will never trust a card again |

**He cannot approve a purchase and he can end one**, because Angela asks him whether it is sound and his answer is the technical due diligence. He is also the persona with the largest measured gain in the pack (2h → 19min) from a single mechanism — which is the strongest available evidence that lineage is load-bearing rather than cosmetic.

### 2.5 Saboteur — the analytics manager

**The role this pack has spent the least time on and the one most likely to stall a deployment quietly.**

| | |
|---|---|
| **Wants** | Predictable throughput from a team of five to fifteen. To hit commitments |
| **Fears** | A new tool consuming his team's time during a busy quarter. Being accountable for a rollout he did not choose. His senior analyst's attention going to a side project |
| **How he says no** | **He never says no.** He allocates no time, deprioritises the pilot, and it dies of neglect — indistinguishable from disinterest |
| **What kills it** | Any evidence the tool adds work before it removes it. **A12 is precisely this risk seen from his chair** |
| **Evidence that moves him** | Review-time-per-week flat or falling; the queue visibly shortening; and *his analyst asking for it*, not being assigned it |

**Why he is the saboteur and not a beneficiary.** His incentive is throughput this quarter. Every adoption cost lands in his quarter and every benefit lands later. He is not hostile — he is correctly optimising for something the product makes worse before it makes better.

**The mitigation is the same one A12 needs**: reviewing must be cheaper than deriving, and the flywheel must reduce review load over time. Both are contingent, and E5's threshold — under 4 h/week, flat or falling — is as much his tripwire as Priya's.

### 2.6 Beneficiary with no vote — Marcus, business stakeholder

Generates demand and is never consulted in the purchase. Worth listing because **his enthusiasm is the most misleading signal available** — he benefits most visibly (a three-day wait or a guess becomes 90 seconds plus a six-minute review) and he has no influence whatsoever on whether the tool is bought.

## 3. The sequence that actually happens

```
Tom (veto)  ──── satisfied by ARTIFACTS, before any conversation
     │            self-hosted topology · grep-able audit log · read-only role
     ▼
Priya (champion) ── installs, runs a real question, catches a real defect
     │
     ▼
Analytics manager (saboteur) ── allocates time, or quietly does not
     │
     ▼
Dr. Chen (gate) ── reviews an ML output, tells Angela it is sound
     │
     ▼
Angela (payer) ── forms her view from accumulated artifacts, then signs
```

**Note what is absent: a meeting.** Nobody is prospected, nothing is pitched, and four of the five roles are convinced by artifacts rather than conversations. That is a direct consequence of the only viable channel being open-source self-serve at a $900 ACV ([strategy/channel_plan.md](../strategy/channel_plan.md) §4) — the product has to sell itself because nothing else can afford to.

## 4. Objection-handling artifacts required

Each is a *thing to build*, not a talking point.

| Role | Objection | Required artifact | Exists? |
|---|---|---|---|
| Tom | *"Another agent with read access to production"* | Self-hosted deployment guide, data-flow diagram, grep-able audit log sample, schema-only egress mode | Diagram written ([tech/architecture/D06](../tech/architecture/D06_security_trust_boundary.md)); **guide and sample log not built** |
| Angela | *"I'm already buying a semantic layer for exactly this"* | **A live demo of the product reading her dbt layer** | **Not built** — 295B (feature #23) |
| Dr. Chen | *"Automated modelling ships leakage"* | Model card with exhaustive not-attempted list, on a real output | **Not built** — 295B (features #32, #39) |
| Priya | *"Verifying isn't faster than rewriting"* | **The E1 timed-task result** | **Not measured** — the low-fidelity MVP produces it |
| Manager | *"This will eat my team's time"* | Review-time-per-week data, flat or falling | **Not measured** — E5, needs deployment |

**Four of five do not exist yet, and one of them (Priya's) is measurable this month with no code.**

## 5. What this pack has probably underweighted

**The analytics manager.** He appears nowhere in [strategy/personas.md](../strategy/personas.md), has no journey, and no artifact is built for him — yet he controls the time of the person the entire go-to-market depends on, and his failure mode is silence rather than objection, which makes it invisible until the pilot is already dead.

**The correction is cheap and belongs in discovery:** add one screening question for analysts — *"who decides what you spend your week on, and how would they react to you piloting a new tool?"* — and one manager-level interview to the discovery plan. It costs an hour and it tests a role the pack currently assumes away.

## Recommended next 3

1. **Build Tom's artifact set before the first external install**, not before the first purchase conversation. His veto is asymmetric, costs him nothing, and fires early in the sequence rather than late.
2. **Add the analytics manager to [discovery_guide.md](discovery_guide.md) §2 as a fourth screening category.** He is the one role that can end a deployment without anyone noticing, and the pack currently has no evidence about him at all.
3. **Treat Priya's objection artifact as the highest-priority build in the table** — it is the only one obtainable this month, it needs no software, and every other row assumes its answer.
