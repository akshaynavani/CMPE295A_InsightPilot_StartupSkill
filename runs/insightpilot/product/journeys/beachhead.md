# Journey — beachhead: Priya's first investigation to habitual use

**What this is** — The core use case as a narrative: Priya Raghunathan, senior data analyst, from her first session through to habitual use, with every beat naming the component that fires and what gets written to the durable record.
**Why it exists** — The PRD specifies a *Verify* beat that no competitor has, and a specification cannot show whether that beat is worth its own screen. This narrative is where the claim gets tested against a real ninety minutes of an analyst's Thursday. The failure it prevents: building a Verify surface nobody opens, because in the abstract "lineage" always sounds valuable and in practice it competes with the analyst's own SQL.
**How to read it** — The **component / written** column is the mechanical spine; a skeptic should be able to list which components fired in what order. Attack §3 beat 7, the moment the entire venture rests on, and §5, which states what this journey assumes and has not proven.
**Depends on / feeds** — Persona from [strategy/personas.md](../../strategy/personas.md) §2; loop and principles from [PRD.md](../PRD.md); features by number from [features_flagship.md](../features_flagship.md). Feeds [ux_spec.md](../ux_spec.md) and the `validation/` discovery guide.

---

## 1. Profile

**Priya Raghunathan**, 31, senior data analyst, six years in analytics, three at a 4,000-person logistics company. Fluent SQL, comfortable Python, owns eleven dbt models. Sits in a five-person central analytics team serving finance, ops and commercial.

**Her stack.** Snowflake warehouse (shipments, invoices, customers), operational Postgres (live shipment status), a monthly carrier-cost CSV that arrives by email and has never been modelled, a REST API for the tracking vendor.

**Session goal.** Answer the ops director's question — *why did cost per shipment jump in the Southwest last month* — well enough to defend it, before end of day.

**Her prior.** She has a Copilot licence. She stopped using it after it told her it could not compute cost per shipment, because that is not a measure in the semantic model `[S42]`.

## 2. Session zero — 22 minutes, Wednesday evening

She found the repo in a dbt Slack thread where someone complained about exactly her problem.

| Beat | What happens | Component | Written to the durable record |
|---|---|---|---|
| 0.1 | `docker compose up`, points it at a read-only Postgres role and drops the carrier CSV in a folder | Quickstart (#29) | Deployment config; **credentials stay in her environment** (A5) |
| 0.2 | Runs the sample question against seeded data. Sees a six-step plan before anything executes | Orchestrator (#5), plan surface (#6) | — |
| 0.3 | Clicks step 3. Reads the actual SQL | Lineage surface (#10) | — |
| 0.4 | Thinks *"okay, it's showing me the query, not asking me to trust it"* | — | — |

**Elapsed: 22 minutes** — inside the E1 threshold (#29). She does not run a real question tonight; she has to check what it sends to the model provider first, which is exactly the behaviour the schema-only mode (#31) exists for.

## 3. First real investigation — Thursday, 4:10pm

The Slack message arrives. She opens a new investigation instead of a query editor, which is itself a small act of faith she has not yet earned.

| # | Beat | Component | Written to the durable record |
|---|---|---|---|
| 1 | She types: *"Why did cost per shipment go up in the Southwest last month?"* | Investigation surface (#16) | Investigation `inv_4471` created; question stored verbatim |
| 2 | **The system stops before planning.** *"'Cost' matches two things: `carrier_invoice.total_usd` (billed, 14,201 rows, Aug 1–31) and `shipment.est_cost` (estimated, 15,003 rows). Which?"* | **Ambiguity interception (#11)** | Ambiguity event logged with both candidates |
| 3 | She picks billed. Then notices the chip: `cost per shipment = SUM(carrier_invoice.total_usd) / COUNT(shipment.id)`. She edits the denominator to `COUNT(DISTINCT shipment.id)` | **Vocabulary binding (#12)** | **Binding persisted org-wide.** No colleague will hit this again |
| 4 | A six-step plan appears. Step 1 warehouse shipments, step 2 the carrier CSV, step 3 join on region, steps 4–6 split and compare. *"6 hops — long plans compound error"* | Plan surface (#6), plan-length discipline (#26) | Plan `plan_a` stored, unapproved |
| 5 | She reads it in about fifteen seconds. Step 2 pulls all twelve months; she edits it to three. **Cost of that correction: one edit, zero queries run** | Plan surface (#6) | Plan `plan_b`, diffed against `plan_a` |
| 6 | Approves. Fetch agent hits Snowflake, then the CSV. Analytics agent joins and splits | Fetch agent (#7), Analytics agent (#8) | Per-hop lineage (#9): source, query, row counts in/out |
| **7** | **Step 3 comes back amber.** *"Join preserved 13,061 of 14,201 rows — 8% of shipments had no matching invoice. Region codes differ: CSV has 4, warehouse has 6."* | **Per-hop verification (#13)** | Verification result stored on the hop |
| 8 | This is the moment. She has seen this exact failure before — it is what made her distrust the last tool. **Here it is surfaced by the system in 40 seconds rather than found by her after the number reached a slide** | Doubt surfacing (#17) | Doubt annotation on hop 3 |
| 9 | She clicks hop 3, reads the join, sees SW/SOUTHWEST/SW-1 are all live in the CSV. Rewrites the mapping | **Override (#21)** | Override recorded; **region mapping persisted to bindings** |
| 10 | Steps 4–6 re-run against corrected output. Coverage 99.2% | Replanning (#20) | New hop outputs; prior versions retained |
| 11 | The answer: *"Cost per shipment rose 11.4%. Volume fell 3.1%. Rate per shipment rose 14.0%. The move is rate, not mix. Two carriers account for 81% of the increase."* Four checkable claims | Answer composition, established facts (#27) | Answer + established facts stored |
| 12 | She spot-checks the rate claim by re-running hop 5 alone. Same number | **Single-hop re-run (#14)** | Re-run event with matching output |
| 13 | Marks it reviewed | **Sign-off (#24)** | `reviewed_by: priya.r`, timestamped |
| 14 | Exports one file, attaches it to the ops director's thread | **Export (#15)** | Self-contained artifact: question, plan, six hops with queries and counts, answer, sign-off |

**Elapsed: 31 minutes.** Her estimate for doing it by hand was ninety, most of it on the CSV region reconciliation — the same twenty minutes the system spent forty seconds surfacing.

**The honest accounting.** Roughly nine of those thirty-one minutes were verification: reading the plan, inspecting hop 3, re-running hop 5. That is the number O2 measures, and **it is only a win because the alternative was ninety minutes, not because nine minutes is cheap.**

## 4. Follow-ups — the same evening

| Beat | Component | Written |
|---|---|---|
| The ops director replies: *"Which carriers?"* She asks it in the same investigation. Three steps, not six — cost definition, region mapping and source scope are already settled | Context inheritance (#16) | Follow-up appended to `inv_4471` |
| *"Is this going to continue?"* The ML agent produces a baseline in four minutes: trend plus seasonality, MAE stated, **and an explicit list of what it did not have time to try** | ML agent (#32), P9 | Model card with the not-attempted list |
| She reads the not-attempted list, decides it is enough to say "probably, with caveats," and says exactly that | — | — |

## 5. Habitual use — six weeks later

| What changed | Mechanism | Evidence it is working |
|---|---|---|
| The carrier CSV now resolves cleanly on first attempt | Bindings accumulated (#12, #21) | **Override rate on that source has fallen** (#42) — the only observable signal for the A3 moat candidate |
| A second analyst installed it after seeing an exported investigation | Export → GTM loop ([strategy/gtm.md](../../strategy/gtm.md) §3) | E5, and the internal-referral path |
| She opens hops on roughly one investigation in three, not all of them | Lineage surface (#10) | **E3 in its healthy band.** Always-open would mean she does not trust it; never-open would mean the trace is decoration |
| She still writes SQL by hand for anything single-source and familiar | — | **Correct, and the product should not fight it** — that is Genie's turf and PRD non-goal 9 concedes it |

## 6. Components fired, in order

`Quickstart → Investigation surface → Ambiguity interception → Vocabulary binding → Orchestrator → Plan surface → Plan-length discipline → Fetch agent → Analytics agent → Lineage capture → Per-hop verification → Doubt surfacing → Lineage surface → Override → Replanning → Answer composition → Single-hop re-run → Sign-off → Export → Context inheritance → ML agent`

## 7. What this journey assumes and has not proven

Named because a journey that reads well is not evidence.

1. **Beat 7 is the venture, and it is fiction until measured.** The per-hop verification catching an 8% join failure is what makes the thirty-one minutes beat ninety. Whether a cheaper structurally-different check reliably catches *plausible* errors is exactly what P3 says is hard and what feature #13 must be prototyped against the seeded-error set (#2) to establish.
2. **Fifteen seconds to read a six-step plan is an assumption.** If it takes two minutes, beat 5's economics change and plan-length discipline becomes a hard ceiling rather than a warning.
3. **Priya's stated objection is not answered here, only assumed away.** She said *"verifying your reasoning is not obviously faster than writing it myself"* ([strategy/personas.md](../../strategy/personas.md) §2). This journey shows her verifying in nine minutes what would have taken ninety to write — but the ninety-minute figure is her own estimate about a task involving an unmodelled CSV. **For a single-source familiar question the ratio probably inverts, and the product should not pretend otherwise.**
4. **The 8% mismatch is a convenient failure** — it is a *countable* one. The failure modes P3 warns about are the ones that produce a clean-looking join with the wrong grain, and this journey does not show one being caught.
