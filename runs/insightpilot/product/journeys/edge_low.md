# Journey — low edge: Marcus gets an answer he can defend

**What this is** — The least-supported user succeeding with dignity: Marcus Delgado, regional sales director, who cannot read SQL, cannot judge correctness, and needs a number he can put in front of his boss on Monday.
**Why it exists** — [PRD.md](../PRD.md) non-goal 1 renounces unsupervised self-service for non-technical users — the largest revenue segment in the category, and the bet ThoughtSpot was marked down 73.67% on `[S46]`. A renunciation that leaves Marcus with nothing would be a design failure dressed as discipline. This journey is where the pack proves the low edge is *served by the system's design* rather than abandoned, and it is the file that shows what "one adaptive system, no separate tiers" actually means in pixels.
**How to read it** — Beat 6 is the whole design: the moment the system refuses to let an unverified number leave. A skeptic should attack §4, which argues this is dignity rather than a gate, and §5's admission of what Marcus still cannot do.
**Depends on / feeds** — Persona from [strategy/personas.md](../../strategy/personas.md) §3; the sign-off mechanism from [features_flagship.md](../features_flagship.md) #19/#24. Feeds [ux_spec.md](../ux_spec.md)'s low-edge states and `validation/`.

---

## 1. Profile

**Marcus Delgado**, 44, regional sales director, Southwest, 60 people, owns a P&L. Opens his Power BI dashboard about twice a month and does not trust it — the last time he cited a number from it in a QBR, finance corrected him in front of his boss.

**Session goal.** Before Monday's forecast call, know whether pipeline slippage is genuinely worse this quarter or just feels worse.

**Constraint that defines the journey.** He cannot verify anything. Shown a query, he learns nothing. Shown a confidence score, he would over-trust it — which is exactly why PRD P3 forbids presenting one as accuracy.

**What he does today.** Messages Priya on Thursday, gets an answer Monday if he is lucky, and otherwise builds the slide from memory with hedged language. He is one of the 76% who have made a decision without consulting data because access was too difficult `[S15]`.

## 2. The session — Friday, 8:40am

Priya sent him a link to a shared investigation two weeks ago. He bookmarked it. This is the first time he has typed his own question.

| # | Beat | Component | Written to the durable record |
|---|---|---|---|
| 1 | He types the way he would message Priya: *"is deal slippage worse this quarter than last in my region"* | Investigation surface (#16) | `inv_5120`; requester `marcus.d`, role `stakeholder` |
| 2 | **The interface is the same one Priya uses.** No "business mode," no simplified tier. What differs is what is *expanded by default* | Adaptive surface — PRD §4 | — |
| 3 | *"'Slippage' isn't defined in your organisation's vocabulary. Two things in the data could mean it: deals whose close date moved later (`opportunity.close_date` changes), or deals that missed their forecast quarter. Which did you mean?"* — **in business terms, with no column names in the question itself** | **Ambiguity interception (#11)**, adaptive phrasing | Ambiguity event; both candidates stored |
| 4 | He picks *close date moved later*, which is what he meant and had never had to say precisely before | Vocabulary binding (#12) | Candidate binding, **flagged unconfirmed — created by a non-analyst** |
| 5 | The plan appears **collapsed**: *"4 steps across 2 sources — CRM and the warehouse."* He does not open it. It is there | Plan surface (#6), adaptive default | Plan stored, auto-approved (read-only, pre-scoped sources) |
| 6 | Answer in 50 seconds: *"Yes — 34% of your Q3 deals moved their close date at least once, against 21% in Q2. The increase is concentrated in deals over $50K."* Above it, an **amber bar: "Not yet reviewed by an analyst."** | Answer composition; **sign-off state (#24)** | Answer + established facts; `reviewed: false` |
| 7 | He clicks *Export for my slide*. **The export is blocked, and offers a different action:** *"This answer hasn't been checked by an analyst. Send to Priya for review?"* | **Export gating (#15 + #24)**, PRD non-goal 1 | Export attempt logged |
| 8 | He clicks send. Priya gets it with the full plan, hops and verification results — **not a question, a nearly-finished investigation** | Export (#15), share (#36) | Review request on `inv_5120`, assigned |
| 9 | 11:15am: Priya opens it. Hop 2 verification is green; she checks the close-date-change logic, confirms the binding from beat 4, marks it reviewed. **Six minutes** | Lineage surface (#10), single-hop re-run (#14), sign-off (#24) | `reviewed_by: priya.r`; **binding from beat 4 promoted to confirmed** |
| 10 | Marcus gets a notification. The amber bar is now green: *"Reviewed by Priya Raghunathan, 11:21."* Export unlocks | Sign-off (#24) | Export artifact generated |
| 11 | He puts the number on the slide **and puts Priya's name next to it** | — | — |

**Elapsed for Marcus: 4 minutes of his attention, plus a 2.5-hour wait for review. Elapsed for Priya: 6 minutes.**

Compare to today: a Thursday message, a Monday answer, three days of her queue.

## 3. Components fired, in order

`Investigation surface → Ambiguity interception (adaptive phrasing) → Vocabulary binding (unconfirmed) → Orchestrator → Plan surface (collapsed) → Fetch agent → Analytics agent → Lineage capture → Per-hop verification → Answer composition → Sign-off state (unreviewed) → Export gating → Share/review request → [Priya] Lineage surface → Single-hop re-run → Sign-off → Export`

**Note what is identical to Priya's journey**: every component. Nothing is a simplified variant. What differs is three defaults — the plan renders collapsed, ambiguity is phrased in business terms rather than column names, and export is gated on sign-off. **That is what "one adaptive system, no separate tiers" means operationally**, and it is why the pack has no "business edition" to maintain.

## 4. Why the gate is dignity and not a leash

The obvious criticism: Marcus asked a question and the system told him he was not allowed to use the answer. That reads as paternalistic, and the design has to earn its way out of that.

Three reasons it does.

1. **He was already blocked — by three days instead of two hours.** The gate does not stop him getting an answer; it replaces "wait for Priya to have time to *do the work*" with "wait for Priya to have time to *check the work*." Six minutes against ninety is the actual change in his life.
2. **The alternative failed publicly.** An unverified number that reaches a QBR and gets corrected by finance is the specific humiliation Marcus has already lived through. P3 says failure looks plausible `[S2]` — so an ungated system would hand him confident wrong answers he has no means of doubting. **The gate is the only honest way to serve someone who cannot verify.**
3. **He gets something he never had: attribution he can point at.** Priya's name next to the number is not bureaucracy, it is cover. It is what makes the number usable in a room where he will be challenged.

**The failure mode this design must avoid**, and it is real: if review requests pile into Priya's queue, the gate has recreated the original bottleneck with extra steps. The mitigation is that reviewing is *structurally* cheaper than deriving — six minutes versus ninety — but that is the same untested O2 claim the whole pack rests on. **If verification is not cheap, this journey does not work either.** It is the same bet, seen from the stakeholder's side.

## 5. What Marcus still cannot do

Stated plainly, because a low-edge journey that ends in total success is a marketing document.

1. **He cannot tell a good answer from a plausible wrong one**, and nothing in this design changes that. The system does not make him self-sufficient; it makes his dependence fast and legible.
2. **He cannot use the answer if no analyst is available.** Friday afternoon before a holiday, the gate is a wall. There is a real design question here — a time-boxed escalation, or a "use at your own risk with visible watermark" export — and PRD §9.5 records it as open rather than pretending it is solved.
3. **He cannot correct a binding with authority.** His beat-4 choice is stored unconfirmed and only promoted when Priya agrees. Correct — he defined what *he* meant, not what the organisation means — but it means his second question can hit the same clarification again if Priya has not reviewed the first.
4. **The system cannot tell him his question was the wrong one.** He asked about slippage. If the real story is that his team stopped logging close-date changes in July, the answer is technically correct and completely misleading. **Lineage over bad data is still bad data** (PRD non-goal 3), and this is exactly the shape that failure takes at the low edge.
