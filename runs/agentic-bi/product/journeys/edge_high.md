# Journey — high edge: Dr. Chen is stretched, not bored

**What this is** — The power user being genuinely extended: Dr. Wei Chen, staff data scientist, who reviews other people's analyses for a living, distrusts automated modelling on principle, and can re-derive anything the system produces.
**Why it exists** — [PRD.md](../PRD.md) §4 claims traceability is load-bearing rather than cosmetic, and the person who proves or disproves that is the one who *can* verify everything and therefore has no use for a trace that is merely reassuring. The failure this prevents: a lineage surface designed for people who will never open it, which passes every review by people who cannot tell. If Dr. Chen finds the trace insufficient, ASSUMPTIONS A7's high edge is wrong and the UX spec is built on sand.
**How to read it** — §3 beats 5–8 are the test: the system is caught being wrong by the person best equipped to catch it, and the question is whether that costs him five minutes or two hours. A skeptic should attack §5, where he rejects part of the output, and §6, which lists what would make him stop using it.
**Depends on / feeds** — Persona from [strategy/personas.md](../../strategy/personas.md) §4; the P9 time-box and method-lineage features from [features_prioritized.md](../features_prioritized.md) #32/#39/#40. Feeds [ux_spec.md](../ux_spec.md)'s method-lineage screen.

---

## 1. Profile

**Dr. Wei Chen**, 38, PhD, eight years in industry, staff data scientist and the person the analytics team escalates to. Owns the demand-forecasting model that finance plans against.

**Formative experience.** He spent a year cleaning up a previous team's AutoML pipeline that had quietly leaked target information through a date column. Nobody caught it for eight months. He has been the reason the company distrusts automated modelling ever since, and he considers that a public service.

**Session goal.** Not to produce an analysis — to **review one**. An analyst has brought him a churn-driver investigation produced by this system and asked whether it is sound enough to present to the commercial VP.

**His current cost for this task: two hours**, and the worst outcome is that the analysis turns out to be fine, because then he has spent two hours confirming something and has no way to spend less next time.

## 2. What he is handed

A single exported investigation file (#15) — not a chat log, not a dashboard link. Question, plan, seven hops with queries and row counts, an ML output, an answer, and a sign-off marked *reviewed by the analyst, pending DS review*.

His first act is to open it in a text editor to confirm it is genuinely self-contained. It is. **That is the first thing that makes him willing to spend the next fifteen minutes rather than the next two hours.**

## 3. The review — Tuesday, 9:00am

| # | Beat | Component | Written to the durable record |
|---|---|---|---|
| 1 | Reads the plan first, not the answer. Seven hops: three fetch, two analytics, one ML, one visualization | Plan surface (#6) via export | Review session opened on `inv_5088` |
| 2 | Goes straight to hop 4 — the join between CRM accounts and warehouse usage. **He does not trust joins he did not write** | Lineage surface (#10) | Hop inspection event |
| 3 | Sees the SQL, the grain, and the verification result: *"14,880 → 14,880, grain preserved, 0.3% null on `account_id`"* | Per-hop verification (#13) | — |
| 4 | Re-runs hop 4 alone against current data. Same counts. **Ninety seconds, versus the twenty minutes rebuilding it would cost** | **Single-hop re-run (#14)** | Re-run event, matching output |
| **5** | Opens the ML hop. This is where he expects to find the problem, and he does | Method-level ML lineage (#39) | — |
| 6 | The model card reads: *target `churned_90d`, defined as no usage event in 90 days following the observation date; train/test split by account with a 30-day embargo; 5-fold CV; features listed with importances; **algorithms tried: gradient boosting, logistic regression. Not attempted in budget: feature interactions, hyperparameter search, alternative target windows.*** | **ML agent (#32) under P9**, method lineage (#39) | Model card stored as part of lineage |
| **7** | He checks the one thing that matters: **is `last_login_date` in the feature set?** It is not — it was excluded as a leakage candidate, and the card says so with a reason | Method lineage (#39) | — |
| 8 | *"It caught the thing I would have caught."* He notes that this is one instance and not a guarantee | — | Reviewer note attached |
| **9** | **But he rejects something.** Feature importance ranks `support_ticket_count` third. He knows tickets were migrated to a new system in April, so pre-April counts are structurally lower. **The data is wrong in a way the system had no way to know** | — | — |
| 10 | He overrides: excludes the feature, re-runs the ML hop with the same target and split | **ML override affordances (#40)** | Override recorded, attributed to `wei.c`; **annotated as a data-provenance issue, not a model error** |
| 11 | Rankings shift; the top two drivers hold. The answer's substantive claim survives | Replanning (#20) | Updated model card, prior retained |
| 12 | Marks it reviewed with his note attached | Sign-off (#24) | `ds_reviewed_by: wei.c`; note persisted to the investigation |

**Elapsed: 19 minutes**, against his usual two hours. Roughly seven of those were spent on the ML hop, which is where his expertise actually belongs.

## 4. Where he is stretched rather than bored

The design question for the high edge is not whether he can be *satisfied* — it is whether he is doing work worth his salary.

| Beat | What a lesser design would have done | What this does instead |
|---|---|---|
| 4 | Ask him to trust a green checkmark | Let him re-execute the hop himself and diff it |
| 6 | Report accuracy and stop | Report the **not-attempted list** — the renunciation is what makes the rest credible |
| 7 | Hide feature selection behind "automated feature engineering" | Name the excluded feature and the reason, so his specific expertise has a surface to act on |
| 9–10 | Have no mechanism for "the data is fine but the world changed" | Let him override with an annotation that distinguishes a **data-provenance issue from a model error** — a distinction only he can make |

**Beat 9 is the one that matters.** The system did not fail; it was defeated by a fact about the world that lives in Dr. Chen's head and in no schema — a ticketing migration in April. **No amount of lineage, verification or model capability would have caught it.** What the design can do is make the correction cheap, attributed and durable, so the next investigation touching `support_ticket_count` inherits his annotation.

That is the honest ceiling on this product's ambition, and stating it is what makes the rest believable.

## 5. What he refuses

1. **He will not accept the ML output for a production decision** on this evidence, and says so in his note. A four-minute time-boxed baseline (P9) is a *screening* tool, not a forecasting model. He recommends the analyst use it to decide what to investigate, not what to conclude — **which is exactly what the product should want him to say**, and any narrative artifact claiming more contradicts P9 `[S9]`.
2. **He will not treat green verification ticks as correctness.** He read them as *"these specific structural checks passed,"* which is what per-hop verification actually is (P7). A UI that lets a less careful reviewer read them as "the answer is right" would be a P3 violation, and [ux_spec.md](../ux_spec.md) has to carry that burden.
3. **He does not want the system to become his forecasting stack.** He wants his two hours back on other people's work. That is a smaller ambition than the product might prefer and it is the one that gets adopted.

## 6. Components fired, in order

`Export artifact → Plan surface → Lineage surface → Per-hop verification → Single-hop re-run → Method-level ML lineage → ML override affordances → Replanning → Sign-off`

Note the absence: **no Orchestrator, no agents, no ambiguity interception.** The high edge's journey is almost entirely *read and challenge*. That is a distinct product surface with distinct requirements, and it is the strongest argument that traceability is load-bearing — an entire persona uses nothing else.

## 7. What would make him stop using it

The list that matters most, because he is the internal credibility gate for Angela's purchase ([strategy/sales_roadmap.md](../../strategy/sales_roadmap.md) §2).

1. **One undisclosed leakage incident.** If the model card omits a feature that turns out to matter, the not-attempted list becomes a lie by omission and the whole method-lineage mechanism is worthless. **The card must be exhaustive or it is negative value.**
2. **Verification ticks that turn out to be shallow.** If a green tick sits on a hop with a wrong grain, he will never trust one again — and P3 says exactly that failure is the plausible-looking kind.
3. **Overrides that do not persist.** If his April ticketing annotation is lost and he re-derives it in six weeks, the flywheel (PRD §6) is fictional and the product is a chat interface.
4. **Any claim that this replaces review.** He is not automatable and the product should stop well short of implying it. His two hours becoming nineteen minutes is the entire offer, and it is enough.
