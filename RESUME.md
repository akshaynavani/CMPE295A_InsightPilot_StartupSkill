# RESUME — Agentic BI pack run

Not a pack artifact; deliberately outside `runs/agentic-bi/` so it stays out of the manifest. Delete when the run completes.

## Where the run stopped

**Phases 0–7 complete and committed. ALL DOCUMENT PHASES DONE. Only phase 9 (`startup-audit`) remains — no files in `audit/`.**

### Next session: run the audit

1. Read the skill: `C:\Users\019115720\.claude\skills\startup-audit\SKILL.md`, plus `C:\Users\019115720\.claude\references\artifact-manifest.md` and `quality-bar.md`.
2. Run phase 9 → `runs/agentic-bi/audit/COVERAGE.md`.
3. **The audit MUST treat these seven rows as CLOSED BY DECISION, not missing:**
   - **A44** `financials/revenue_build.md`, **A46** `financials/use_of_funds.md`, **A48** `financials/comps_exits.md` — excluded per ASSUMPTIONS **A1** (no revenue, no CAC, no funnel; any projection would be fabricated). All three retained financials files declare this in their scope note.
   - **A49, A50, A51, A52b** (required) and **A52, A56, A57** (optional) — visuals and website, deferred per ASSUMPTIONS **A4**. `node` is not installed on this machine and both skills shell out to it.
4. Also treat as findings rather than defects: the five *Named gaps* in `research/sources.md` (things searched for and not found), and the five `[SPECIFIC:]` placeholders in `narrative/founder_story.md` (deliberate — only the founder can fill them; a fabricated anecdote would fail on the first follow-up).
5. After the audit, the run is complete. Delete this RESUME.md.

### Historical record of the run

Phase 1 wrote the five research files, closed A6 and A9, closed A8 partially, raised A11. Phase 2 wrote the eleven strategy files and closed A5 and A11 by founder decision at the gate. Phase 3 wrote the eight product files and raised A12. Phase 4 wrote nineteen tech files. Phase 5 wrote the six narrative files and passed a forbidden-claim audit. Phase 6 wrote the nine validation files and raised A13. `ASSUMPTIONS.md` and `README.md` refreshed at every checkpoint.

Search budget: **35 web searches + 6 direct page fetches** across all phases, against a 200 limit. Phases 3–6 needed no new searches — all are downstream synthesis. See *Operational lesson* below.

**Cadence agreed with the founder: one phase at a time, commit, report, continue.**

## The pack in one line

**Sixty-two artifacts, twelve untested assumptions, zero customers interviewed.** Say this first in any review — the status line counts documents, not evidence, and `validation/stage_gate.md` places the venture at Customer Discovery, *not exited*.

## Hard constraints — do not violate

- **Never add a git remote to this repo.** `startup-forge` auto-commits *and pushes* at every checkpoint. This run was deliberately moved out of `anavani\startup-skills` because that repo's remote is `github.com/dlmastery/startup-skills`, a third party's public repo. Commit locally; never push. (Verified still remote-free at the phase 1 commit.)
- **Scope is documents only.** Phases 0–7 + audit. Visuals (phase 8) and website (phase 10) are deferred, not cancelled. `node` is not installed on this machine; both deferred phases need it.
- **Financials are cost-side only.** Excluded rows A44 `revenue_build.md`, A46 `use_of_funds.md`, A48 `comps_exits.md`. See ASSUMPTIONS A1. The audit must treat these as closed, not missing.
- **No manufactured 10x claim.** ASSUMPTIONS A2. The differentiator settled in phase 1 is a *positioning* claim and must not be inflated into a 10x — the four constraints attached to A6 travel with it.

## Binding rules phase 1 produced — carry these into every later phase

1. **The A6 differentiator, verbatim:** *the investigation, not the query, is the unit — and it ships with a hop-level trace that makes verification cheaper than re-derivation.* Its four constraints (not a 10x; the bar is Hex's notebook not "we show the SQL"; the ML agent is not the differentiator; no head-to-head accuracy claim is permitted) must travel with it. If they get dropped in transit the pack has manufactured the claim A2 forbids.
2. **No artifact may state a requests-per-analyst-per-week figure** (A8). It is not publicly measured. Turnaround time may be cited, always attributed as *reported by IBM, attributed to Sigma*. The circulating "80% of a data team's time" figure is registered as rejected in `sources.md` `[S20]` and supports nothing.
3. **The phrase "crossed a usable threshold" must not appear anywhere** (A9). Use the restated shift 1 wording recorded in ASSUMPTIONS A9 verbatim.
4. **Lead positioning with verifiability, support with latency** (A8 reframe). The trust evidence is High-confidence and current; the latency evidence is Medium and second-hand.
5. **Name Wren AI in every downstream comparison.** It is the nearest neighbour, open source, two years ahead, 13K+ stars. A pack that never names it reads as unaware.

## Additional binding rules produced by phase 2

6. **Deployment is open-core, self-hostable** (A5, founder decision). "Self-hostable" means the *orchestration layer* runs in the customer's environment against **their own frontier-model API key** — never that the system runs on a small local model. Tool-initialisation failure is the leading agent bottleneck and is catastrophic in small models (89% in qwen2.5:3b). Any artifact implying a small-local-model deployment is wrong.
7. **Sizing numbers are fixed: TAM $1.1B / SAM $123M / three-year hypothetical SOM $1.2M / capstone SOM $0.** No artifact may use other figures, and none may present $1.2M as a projection. Re-expanding to the BI market would contradict the market-type declaration.
8. **Only zero-CAC channels are viable at a $900 ACV.** Outbound, field sales, resellers, cloud marketplace and paid acquisition are ruled out by arithmetic in `strategy/channel_plan.md` §3. If a later phase proposes one, that file is the reason to say no.
9. **Lead every demo and narrative artifact with the lineage/verification mapping (rank 1), never with automated fetch→analyze→visualize (rank 4).** Rank 4 is table stakes and invites the head-to-head comparison A6 forbids.
10. **Two product requirements were discovered by strategy and must land in the PRD:** (a) an investigation must be **exportable as a self-contained, readable artifact** — it is the edge in the GTM compounding loop and expensive to retrofit; (b) **reading an existing dbt/Cube semantic layer must be demoable** — it is the only answer to the buyer objection that ends deals.

## Additional binding rules produced by phase 3

11. **The core loop is ASK → PLAN → EXECUTE → ANSWER → VERIFY → FOLLOW UP.** *Verify* is a named beat with its own surface, latency budget and metric. Do not collapse it back into "answer + lineage."
12. **Ten principles in `product/PRD.md` §3 govern every feature.** A feature mapping to none is cut. The two most load-bearing: **P5** (verification cost is the adoption gate, not accuracy) and **P6** (pre-encoded correctness narrows the answerable question set — so consume a semantic layer when present, never require one).
13. **P9 is the principle the tech and narrative layers are most likely to break.** The ML agent is time-boxed in *minutes* and must publish what it did not have time to try. MLE-bench's 36.4% medal rate runs on a **12-hour budget**; promising that behaviour in a conversational loop is a false claim.
14. **Never present a confidence score as accuracy** (P3). The system reports what it checked and what it is unsure about — different claims. A green verification tick must read as "these structural checks passed," never "the answer is right."
15. **Ten non-goals in `product/PRD.md` §2.2 are real renunciations**, including no unsupervised self-service for non-technical users, no semantic layer of our own, no data-quality improvement, and no claim to beat incumbents on single-source single-hop accuracy. Later phases must not quietly re-acquire any of them.
16. **Build order is fixed by `product/features_prioritized.md`:** evaluation harness first (#1), then Postgres/CSV, Orchestrator, plan surface, fetch, analytics, lineage, verification, export. The pre-decided cut list is visualization → REST → ML agent → override re-flow. **Must-not-cut: #1, #2, #9, #10, #13, #15, #11.**

## Additional binding rules produced by phase 4

17. **The mechanism arithmetic totals ≈2.9× (band 1.8×–4.2×)** on multi-source questions against an unmodelled source, and **≈1.0× or below on single-source familiar questions.** Both halves must travel together in every artifact. The conservative corner is 1.8×.
18. **The 13.8× queueing multiplier is forbidden.** Computed in `tech/whitepaper.md` §3.1 and withdrawn in §3.2 because induced demand will consume it. Stated there specifically so no later phase can rediscover it as a headline.
19. **Reflection, self-critique, LLM-as-judge and multi-agent debate are declined by principle** (`tech/techniques/wave3.md` §1). All keep verification inside the model that produced the output; P7 requires verification to run structurally different code. A later phase proposing them is reversing a decision, not adding a feature.
20. **Two HIGH-severity technique gaps must be closed before the Analytics agent ships diagnostic questions:** multiple-comparisons correction (contribution analysis will otherwise name noise as a driver, and no structural check catches it) and calibration measurement (doubt surfacing is otherwise unfalsifiable). Both in `tech/techniques/technique_feature_matrix.md` §4.
21. **`expected_attempts` is the dominant unknown in the cost model.** A cost model assuming one clean pass per investigation will be wrong by a large multiple, since DABstep implies retries are the common case. `financials/` must model cost per attempt × expected attempts and say the second term is unmeasured.

## Additional binding rules produced by phase 5

22. **The narrative layer passed a forbidden-claim audit and later phases must not reintroduce what it excluded.** The 13.8× queueing multiplier appears only as a withdrawal; "10×" only as a denial; no head-to-head accuracy claim against any incumbent; the MLE-bench 36.4% figure appears nowhere. Re-run the audit (`grep` for `13\.8`, `10x|10×`, `more accurate than`, `36\.4`) if any narrative file is edited.
23. **`narrative/founder_story.md` carries five `[SPECIFIC:]` / `[N]` placeholders that only the founder can fill.** They are deliberate, not omissions — the team has no lived analytics experience, so a fabricated origin anecdote would fail on the first follow-up. **Do not fill them by inference in a later phase.** If one cannot be answered truthfully, the instruction in-file is to cut the sentence rather than soften it.
24. **`narrative/pitch_deck.md` names intended visuals that do not exist** (visuals phase deferred, A4). Its `visual:` lines are the future rows of `visuals/visual_manifest.md`; four of them point at Mermaid diagrams already written in `tech/architecture/` that need only rendering.
25. **The vision is a norm, not a market share.** `future_press.md` lands on $74M ARR across 1,900 organisations at 2033 — consistent with the $123M SAM — with the company losing exclusive control of the differentiator to an open format. A later phase must not upgrade this to a hypergrowth story.

## Additional binding rules produced by phase 6

26. **The honest stage placement is Customer Discovery, not exited** — twelve untested assumptions, zero customers interviewed. **Never let the pack's completeness be read as progress.** The sentence to say first in any review is: *"fifty-nine artifacts, twelve untested assumptions, zero customers interviewed."*
27. **Pass/fail thresholds in `validation/experiment_board.md` are declared and must not be revised after seeing data.** The critical ones: verification cost ratio **≤ 0.5 pass / > 0.8 stop**; seeded-defect rejection **≥ 70% and ≥ 2× control**; multi-source share **≥ 25%**; budget line named by **≥ 3 of 5** buyers; multi-hop accuracy **≥ 50%**.
28. **E1 and E2 must both pass, and E2 is the more dangerous.** Passing E1 alone means checking is cheap; passing E2 alone means checking works but costs too much. **The dangerous combination is E1 pass with E2 fail** — cheap verification that does not verify, which ships confident wrong answers wearing an audit trail.
29. **The low-fidelity MVP is a document, not software** — one hand-built exported investigation plus a stopwatch, ~6 founder-hours. It can invalidate the entire high-fidelity build and the reverse is not true, so **it runs first**.
30. **Report E6 (accuracy) and E7 (silent-error rate) together, always.** Accuracy alone is the flattering half; publishing it without the silent-error figure is exactly the selective reporting this pack criticises incumbents for.
31. **Hop-inspection rate has a healthy band of 20–60%, and both extremes are failures.** Near 0% = the trace is decoration; near 100% = re-derivation with a nicer interface. Do not treat it as a metric to maximise.
32. **`pivot_log.md` §4 names the pivot to refuse:** moving to the business-user market after a disappointing analyst result. That is P1 reopened, it was already priced by ThoughtSpot's 73.67% markdown, and it makes the verification problem unsolvable rather than easier.

## Additional binding rules produced by phase 7

33. **Pricing is a threshold, never a forecast.** $900/analyst/year requires **18–30 hours saved per year** to break even (varying with `expected_attempts`); the modelled saving is **38 hours**. Margin is **1.3×–2.1×** — narrow and real. It fails if multi-source share drops below 15%, if attempts exceed 5, or if E1 fails.
34. **Never quote the 87–93% gross margin without §4.2's explanation.** It is high because the customer absorbs inference under self-hosting, not because of operating efficiency. A hosted version would be ~42% at three attempts.
35. **Never quote an LTV:CAC ratio.** At ≈$0 CAC it is arithmetically infinite and analytically meaningless. The metric that matters is **expansion — deployments reaching a second analyst.**
36. **The cost curve is a customer tailwind, not a margin story.** Falling inference prices accrue entirely to the customer; our margin does not contain inference. Do not reproduce the standard "margins expand as inference cheapens" line — it describes a hosted business this one deliberately is not.
37. **No risk mitigates to Low**, and the risk matrix must stay that way. R1's mitigation is a measurement, not a fix. **For the capstone, R1 and R2 are deliverables rather than risks; R8 (time / scope creep) is the dominant capstone risk.**

## Open decisions — none

Every open decision in `ASSUMPTIONS.md` is closed. What remains is A7 (unconfirmed inference on the user spectrum, `kills-pack-if-wrong: yes`), the deliberate scope decisions A1–A4 which the audit must treat as closed rather than missing, and **A12 (raised by phase 3), which is a tracked risk rather than a decision** and closes in phase 6.

## A12 — the risk phase 3 surfaced

**The beachhead captures the least value on any given day.** Across one shared Tuesday: Dr. Chen 2h → 19min, Tom 1.5 days → 8min, Marcus a three-day wait → 90 seconds, Angela gains an investigation she could not previously run — while **Priya absorbs the review burden the other four shed.** Since the entire GTM routes through analyst advocacy, a champion who has been given work while everyone else got leverage does not advocate.

Phase 6 must carry **analyst review-time-per-week as a first-class metric** alongside time-to-verified-answer, and treat review-queue depth as a leading indicator.

## The three untested claims the pack rests on

None require code; all three are conversation-cheap and none is settled. Ranked in `strategy/business_model_canvas.md` rows 2, 1 and 5:

1. **An analyst can accept a correct answer they did not derive faster than they could derive it.** The differentiator. The beachhead's own stated objection denies it. One afternoon, five analysts, a timed task.
2. **A material share of real ad-hoc questions span more than one source.** If not, the neutrality argument is true and worthless and the SAM halves. Ask 10 analysts to classify their last 20 requests.
3. **A budget owner can name a line item this comes from.** If not, the market-type declaration is wrong. One question in five buyer conversations.

## Operational lesson — read before dispatching agents

An earlier session launched 4 research subagents. **Each fanned out into sub-agents of its own — ~10 total — which consumed all 200 web searches and then died on a session rate limit.** Nothing was salvageable.

Phase 1 was then run with searches issued directly, in batches of 3–4 parallel calls per message, and finished the entire layer in 33 searches and 6 fetches. That is the approach to repeat. It also preserved citation fidelity, which mattered — `sources.md` carries 68 numbered entries with exact URLs, access dates and confidence grades, and every `[Sn]` tag in the other four files was verified to resolve.

## Notes for the audit (phase 9)

- Treat A1 exclusions (A44, A46, A48) and A4 deferrals (A49–A52b, A52, A56, A57) as **closed by decision**, not missing.
- `research/sources.md` ends with a *Named gaps* section listing five things searched for and not found. These are findings, not omissions — the audit should not flag them, and a later phase should not re-search them blind.
- Eight source rows (`[S21]`, `[S23]`–`[S28]`, `[S68]`) are registered but uncited in phase 1 by design; `[S25]`–`[S28]` are staged for phase 2's market sizing. Explained in `sources.md` *Reliability notes* 3.
