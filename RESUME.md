# RESUME — Agentic BI pack run

Not a pack artifact; deliberately outside `runs/agentic-bi/` so it stays out of the manifest. Delete when the run completes.

## Where the run stopped

**Phase 0 complete and committed. Phase 1 (`startup-research`) not started — no files written to `research/`.**

Stopped because the session exhausted its web search budget (200/200) before any research file was written. Phase 1 requires live search; the skill's first rule is "search the live web, do not rely on training memory."

## Start here in the new session

1. Read `runs/agentic-bi/BRIEF.md` and `runs/agentic-bi/ASSUMPTIONS.md` — the source of truth and the open-decision ledger.
2. Read the skill: `C:\Users\019115720\.claude\skills\startup-research\SKILL.md`, plus `C:\Users\019115720\.claude\references\quality-bar.md`.
3. Run phase 1. Write the five files to `runs/agentic-bi/research/`: `landscape.md`, `competitors.md`, `capability_table.md`, `survey.md`, `sources.md`.
4. Commit. Then continue phases 2 → 7, then 9 (audit).

## Hard constraints — do not violate

- **Never add a git remote to this repo.** `startup-forge` auto-commits *and pushes* at every checkpoint. This run was deliberately moved out of `anavani\startup-skills` because that repo's remote is `github.com/dlmastery/startup-skills`, a third party's public repo. Commit locally; never push.
- **Scope is documents only.** Phases 0–7 + audit. Visuals (phase 8) and website (phase 10) are deferred, not cancelled. `node` is not installed on this machine; both deferred phases need it.
- **Financials are cost-side only.** Excluded rows A44 `revenue_build.md`, A46 `use_of_funds.md`, A48 `comps_exits.md`. See ASSUMPTIONS.md A1. The audit must treat these as closed, not missing.
- **No manufactured 10x claim.** ASSUMPTIONS.md A2 — the founder chose integrated breadth over a single differentiator, knowingly. `startup-critic` will flag it every phase; it is an accepted deviation, logged once.

## Operational lesson — read before dispatching agents

The previous session launched 4 research subagents. **Each fanned out into sub-agents of its own — ~10 total — which consumed all 200 web searches and then died on a session rate limit.** Nothing was salvageable from them.

If using subagents for phase 1: cap the fan-out explicitly and forbid them from spawning further agents. Otherwise run the searches directly — that also keeps citation fidelity, which matters because `sources.md` needs exact URLs and access dates.

## Verified finding to carry forward

The only fact established before the budget ran out. Live fetch of <https://spider2-sql.github.io/>, accessed 2026-09-08:

| Spider 2.0 setting | Top system | Execution accuracy |
|---|---|---|
| Spider 2.0-Snow (547 ex.) | Genloop Sentinel Agent v2 Pro | 96.70% |
| Spider 2.0-Lite (547 ex.) | Tianqiong Data Agent + GLM 5.2 | 76.23% |
| Spider 2.0-DBT (68 ex.) | SignalPilot Agent | 65.60% |

Benchmark's own baseline, same source: *"GPT-4o... only 10.1% on Spider 2.0 tasks, compared to 86.6% on Spider 1.0"*; o1-preview 17.1% on Spider 2.0.

**Why this matters and how to use it.** The naive argument — "benchmarks are easy, real schemas are brutal" — is now weak: top agentic systems clear 96% on Spider 2.0-Snow. The defensible argument is the **spread across settings**: the same class of system falls to 65.6% on the dbt setting, where semantic-layer indirection and real project structure apply. Argue from the spread, not the headline. Note also that the 10.1% baseline is from the original paper and the leaderboard is current — cite both with their dates, never the baseline alone.

## Open items phase 1 must close

- **A6** — the competitive differentiator, deferred to the teardown. Must come from failure mechanisms, not marketing gaps.
- **A8** — problem magnitude (analyst queue latency, ad-hoc request load). Flagged `kills-pack-if-wrong: yes`. If it cannot be sourced, say so explicitly; a documented absence of evidence is a valid finding and beats an invented number.
- **A9** — the two "why now" shifts are founder-asserted and undated. Need dated citations in `survey.md`.
