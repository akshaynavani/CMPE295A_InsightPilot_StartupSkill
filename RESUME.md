# RESUME — Agentic BI pack run

Not a pack artifact; deliberately outside `runs/agentic-bi/` so it stays out of the manifest. Delete when the run completes.

## Where the run stopped

**Phases 0 and 1 complete and committed. Phase 2 (`startup-strategy`) not started — no files in `strategy/`.**

Phase 1 wrote all five files to `runs/agentic-bi/research/`, closed A6 and A9, closed A8 partially, and raised A11. `ASSUMPTIONS.md` and `README.md` were both refreshed at the checkpoint.

Search budget used in the phase 1 session: **33 web searches + 6 direct page fetches** — well inside the 200 limit. Running searches directly rather than via subagents worked; see *Operational lesson* below.

## Start here in the new session

1. Read `runs/agentic-bi/BRIEF.md` and `runs/agentic-bi/ASSUMPTIONS.md` — source of truth and open-decision ledger. **The three resolutions recorded in A6, A8 and A9 are binding on phase 2 and are easy to lose.**
2. Read `runs/agentic-bi/research/competitors.md` §4 and `survey.md` §6 — these two sections are what phase 2 consumes.
3. Read the skill: `C:\Users\019115720\.claude\skills\startup-strategy\SKILL.md`, plus `C:\Users\019115720\.claude\references\quality-bar.md`.
4. Run phase 2 → `runs/agentic-bi/strategy/` (11 files). Commit. Then phases 3 → 7, then 9 (audit).

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

## Open items phase 2 must close

- **A5** — self-hosting undecided. Closes in `strategy/positioning.md`.
- **A11** (new, raised by phase 1) — the gravity question: why does this not end as a Databricks or Snowflake feature? Sisu raised ≈$128.7M attacking the highest-value part of this loop and became a Snowflake division; Narrative Science was folded into Tableau; neither failed technically. The only structural answer the research supports is cross-source neutrality. **A5 and A11 must resolve together** — a managed-only product has no neutrality argument.

## Operational lesson — read before dispatching agents

An earlier session launched 4 research subagents. **Each fanned out into sub-agents of its own — ~10 total — which consumed all 200 web searches and then died on a session rate limit.** Nothing was salvageable.

Phase 1 was then run with searches issued directly, in batches of 3–4 parallel calls per message, and finished the entire layer in 33 searches and 6 fetches. That is the approach to repeat. It also preserved citation fidelity, which mattered — `sources.md` carries 68 numbered entries with exact URLs, access dates and confidence grades, and every `[Sn]` tag in the other four files was verified to resolve.

## Notes for the audit (phase 9)

- Treat A1 exclusions (A44, A46, A48) and A4 deferrals (A49–A52b, A52, A56, A57) as **closed by decision**, not missing.
- `research/sources.md` ends with a *Named gaps* section listing five things searched for and not found. These are findings, not omissions — the audit should not flag them, and a later phase should not re-search them blind.
- Eight source rows (`[S21]`, `[S23]`–`[S28]`, `[S68]`) are registered but uncited in phase 1 by design; `[S25]`–`[S28]` are staged for phase 2's market sizing. Explained in `sources.md` *Reliability notes* 3.
