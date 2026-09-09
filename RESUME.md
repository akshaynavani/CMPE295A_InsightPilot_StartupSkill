# RESUME — Agentic BI pack run

Not a pack artifact; deliberately outside `runs/agentic-bi/` so it stays out of the manifest. Delete when the run completes.

## Where the run stopped

**Phases 0, 1 and 2 complete and committed. Phase 3 (`startup-product`) not started — no files in `product/`.**

Phase 1 wrote all five research files, closed A6 and A9, closed A8 partially, and raised A11. Phase 2 wrote all eleven strategy files and closed A5 and A11 together by founder decision at the gate. **Every open decision in the ledger is now closed.** `ASSUMPTIONS.md` and `README.md` were refreshed at both checkpoints.

Search budget: **35 web searches + 6 direct page fetches** across phases 1–2, against a 200 limit. Running searches directly rather than via subagents worked; see *Operational lesson* below.

**Cadence agreed with the founder: one phase at a time, commit, report, continue.**

## Start here in the new session

1. Read `runs/agentic-bi/BRIEF.md` and `runs/agentic-bi/ASSUMPTIONS.md` — source of truth and decision ledger. **The resolutions in A5, A6, A8, A9 and A11 are binding on every later phase and are easy to lose in transit.**
2. Read `runs/agentic-bi/strategy/positioning.md` §5 and §5.1, `personas.md`, and `value_prop_canvas.md` §5 — these are what phase 3 consumes.
3. Read the skill: `C:\Users\019115720\.claude\skills\startup-product\SKILL.md`, plus `C:\Users\019115720\.claude\references\quality-bar.md`.
4. Run phase 3 → `runs/agentic-bi/product/` (8 files). Commit, report. Then phases 4 → 7, then 9 (audit).

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

## Open items — none

Every open decision in `ASSUMPTIONS.md` is now closed. What remains is A7 (unconfirmed inference on the user spectrum, `kills-pack-if-wrong: yes`) and the deliberate scope decisions A1–A4, which the audit must treat as closed rather than missing.

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
