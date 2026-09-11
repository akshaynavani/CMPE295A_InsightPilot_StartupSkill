# Visual manifest

**What this is** — The complete, ranked list of visuals this pack needs: what each one shows, who it is for, which artifact it draws its data from, what form it takes, and whether it exists yet.
**Why it exists** — Sixty-three artifacts, every one over 400 words, is where readers stop. This file is the plan that turns that wall of prose into something scannable, and it is written **before** any visual is generated so that generation is reconciliation against a list rather than improvisation. It is also the audit's grep target: statuses here are written from `ls`, never from memory.
**How to read it** — §2 declares the shared visual language every file must obey. §3 onward is the ranked table by audience. A skeptic should attack §6, which records what is deliberately not being drawn and why.
**Depends on / feeds** — Sources every row from the pack's own artifacts; no number appears on a visual that does not exist in one. Feeds `infographics/`, `image_prompts.md`, and `docimages.json`.

---

## 1. Status vocabulary

| Status | Meaning |
|---|---|
| `html` | Self-contained HTML infographic exists in `infographics/` and renders |
| `mermaid` | Already shipped as a Mermaid diagram inside its source artifact — **no separate file needed** |
| `pending-image` | HTML/prompt exists; PNG raster not rendered (no text-to-image capability in this session) |
| `planned` | On the list, not yet built |
| `dropped` | Deliberately not built — reason given in §6 |

**Rasters are not blocking.** Per `startup-visuals`, the HTML version carries the content; a PNG is polish. No row waits on one.

## 2. Shared visual language

Every infographic in this set obeys these, so the pack reads as one system rather than forty files.

**Palette**

| Token | Hex | Use |
|---|---|---|
| `ink` | `#14181F` | Headlines, primary text |
| `body` | `#3A424E` | Body text |
| `muted` | `#6B7484` | Captions, source lines |
| `rule` | `#E2E6EC` | Dividers, table borders |
| `paper` | `#FFFFFF` | Background — always white, print-clean |
| `accent` | `#1F5FA8` | Primary accent, this project's marks |
| `verify` | `#1E7A54` | Passed checks, confirmed states |
| `doubt` | `#B4741A` | Amber states, warnings, untested claims |
| `fail` | `#A3352B` | Failure paths, risks, rejected options |
| `wash` | `#F5F7FA` | Zone backgrounds |

**Type scale** — system sans stack (`-apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif`). Headline 30px/700 · zone title 15px/650 · body 13px/400 · label 11px/600 uppercase tracked · source line 10px/400 muted.

**Layout** — 1280×720 (16:9) unless marked A4. One headline takeaway readable in three seconds, then 3–5 information zones that reward thirty. Every file ends with a source line citing its artifact and any `[Sn]` tags.

**The rule that governs all of it:** every number on a visual exists in a pack artifact. No decorative charts, no invented data.

## 3. Audience A — Users (analyst, stakeholder, data scientist)

| ID | Title | Audience | Source | Form | Status |
|---|---|---|---|---|---|
| V01 | The core loop: ask, plan, execute, answer, verify, follow up | users | product/PRD.md | html | html |
| V02 | One system, three edges: who the interface adapts to | users | strategy/personas.md, product/PRD.md | html | html |
| V03 | Priya's Thursday: 90 minutes by hand versus 31 with a plan | users | product/journeys/beachhead.md | html | html |
| V04 | The stakeholder who cannot verify: gated until an analyst signs | users | product/journeys/edge_low.md | html | html |
| V05 | The reviewer's two hours become nineteen minutes | users | product/journeys/edge_high.md | html | html |
| V06 | One ordinary Tuesday across five roles | users | product/journeys/day_in_life.md | html | html |
| V07 | Twelve screens: the interface surface | users | product/ux_spec.md | html | html |
| V08 | The verification tick problem: what green does and does not mean | users | product/ux_spec.md | html | html |

## 4. Audience B — Operators and the build team

| ID | Title | Audience | Source | Form | Status |
|---|---|---|---|---|---|
| V09 | System map: the whole architecture on one canvas | operators | tech/architecture/00_INDEX.md | html | html |
| V10 | Investigation pipeline, end to end | operators | tech/architecture/D01_investigation_pipeline.md | mermaid | mermaid |
| V11 | Verify-and-replan closed loop | operators | tech/architecture/D02_verify_replan_loop.md | mermaid | mermaid |
| V12 | Agent orchestration: the star topology | operators | tech/architecture/D03_agent_orchestration.md | mermaid | mermaid |
| V13 | Durable record and binding store | operators | tech/architecture/D04_memory_schema.md | mermaid | mermaid |
| V14 | Model routing: where the tokens actually go | operators | tech/architecture/D05_model_routing_cost.md | mermaid | mermaid |
| V15 | Trust boundary: one egress arrow | operators | tech/architecture/D06_security_trust_boundary.md | mermaid | mermaid |
| V16 | Connectors and semantic layers: two interfaces | operators | tech/architecture/D07_connectors_ecosystem.md | mermaid | mermaid |
| V17 | Evaluation harness and what it measures | operators | tech/architecture/D08_evaluation_harness.md | mermaid | mermaid |
| V18 | Deployment topology and the real ceiling | operators | tech/architecture/D09_deployment_scale.md | mermaid | mermaid |
| V19 | Human-in-the-loop: three mandatory gates | operators | tech/architecture/D10_human_in_the_loop.md | mermaid | mermaid |
| V20 | Technique decision tree | operators | tech/techniques/decision_tree.md | mermaid | mermaid |
| V21 | Seven components, five buildable and two research risk | operators | tech/deep_dives.md | html | html |
| V22 | Feature roadmap: Now / Next / Later with the cut list | operators | product/features_prioritized.md | html | html |
| V23 | The twenty flagship features by loop phase | operators | product/features_flagship.md | html | html |
| V24 | Technique × feature matrix, with orphans and gaps | operators | tech/techniques/technique_feature_matrix.md | html | html |
| V25 | Three technique waves: 44 / 38 / 31, and eight declines | operators | tech/techniques/wave1.md, tech/techniques/wave2.md, tech/techniques/wave3.md | html | html |
| V26 | Named stack, and the line between engineering and research | operators | tech/not_vaporware.md | html | html |
| V27 | Ten principles every feature must map to | operators | product/PRD.md | html | html |

## 5. Audience C — Investors, advisor and evaluator

| ID | Title | Audience | Source | Form | Status |
|---|---|---|---|---|---|
| V28 | The two axes that divide this market, and the empty quadrant | investors | strategy/positioning.md | html | html |
| V29 | Mechanism arithmetic: six frictions, four attacked, ≈2.9× | investors | tech/whitepaper.md | html | html |
| V30 | TAM / SAM / SOM built bottom-up, with the pessimistic corner | investors | strategy/market_sizing.md | html | html |
| V31 | The graveyard: four attempts, none died of bad technology | investors | research/landscape.md | html | html |
| V32 | Competitor teardown: where each fails mechanistically | investors | research/competitors.md | html | html |
| V33 | Capability frontier: what the field can and cannot do today | investors | research/capability_table.md | html | html |
| V34 | Risk matrix: no residual below medium | investors | financials/risk_matrix.md | html | html |
| V35 | Unit economics: who actually pays the compute | investors | financials/unit_economics.md | html | planned |
| V36 | Pricing as a falsifiable threshold, not a forecast | investors | financials/pricing.md | html | planned |
| V37 | Stage gate: Customer Discovery, not exited | investors | validation/stage_gate.md | html | planned |
| V38 | Nine experiments with thresholds declared in advance | investors | validation/experiment_board.md | html | planned |
| V39 | Twelve assumptions ranked by kill-power and cost to test | investors | validation/riskiest_assumptions.md | html | planned |
| V40 | Market type: re-segmented, and what that commits us to | investors | strategy/market_type.md | html | planned |
| V41 | The petal: which budgets this draws from | investors | strategy/petal_diagram.md | html | planned |
| V42 | Evidence ledger: 71 sources graded, five named gaps | investors | research/sources.md | html | planned |

## 6. Audience D — Buyers, partners and the security reviewer

| ID | Title | Audience | Source | Form | Status |
|---|---|---|---|---|---|
| V43 | What leaves your environment, and what never does | buyers | tech/architecture/D06_security_trust_boundary.md | html | planned |
| V44 | The decision-making unit: who can say no | buyers | validation/decision_making_unit.md | html | planned |
| V45 | Get / keep / grow, and the loop's one fragile edge | buyers | validation/get_keep_grow.md | html | planned |
| V46 | Channel economics: why only zero-CAC channels survive | buyers | strategy/channel_plan.md | html | planned |
| V47 | Two MVPs, and why the first one is a document | buyers | validation/mvp_definition.md | html | planned |

## 7. Dossier coverage — artifacts not yet cited by any row above

Per the A52b contract, no substantive artifact over ~400 words should be left with zero illustrations. These rows exist to close that gap.

| ID | Title | Audience | Source | Form | Status |
|---|---|---|---|---|---|
| V48 | The brief in one frame: user, mechanism, and what is not claimed | operators | BRIEF.md | html | planned |
| V49 | The decision ledger: what was chosen, deferred and refused | operators | ASSUMPTIONS.md | html | planned |
| V50 | Survey in one frame: the case for and against this mechanism | investors | research/survey.md | html | planned |
| V51 | Lean canvas, with the riskiest cell marked | investors | strategy/lean_canvas.md | html | planned |
| V52 | Business model canvas: nine blocks, nine killing tests | investors | strategy/business_model_canvas.md | html | planned |
| V53 | Value proposition: the five ranked fits | investors | strategy/value_prop_canvas.md | html | planned |
| V54 | Go-to-market: the compounding loop | buyers | strategy/gtm.md | html | planned |
| V55 | Sales roadmap: organisation, influence and access maps | buyers | strategy/sales_roadmap.md | html | planned |
| V56 | Metrics by stage, and the vanity metrics to ignore | operators | validation/metrics_by_stage.md | html | planned |
| V57 | Pivot log: ten roads closed, ten triggers armed | investors | validation/pivot_log.md | html | planned |
| V58 | Discovery guide: the questions that ask about the past | operators | validation/discovery_guide.md | html | planned |
| V59 | Mission and five values stated as trade-offs | investors | narrative/mission_vision.md | html | planned |
| V60 | The one-pager, as a frame | investors | narrative/one_pager.md | html | planned |
| V61 | Memo in one frame: thesis, demolition, risks | investors | narrative/vc_memo.md | html | planned |
| V62 | Working backwards from 2033 | investors | narrative/future_press.md | html | planned |
| V63 | Founder-market fit, and the gap named openly | investors | narrative/founder_story.md | html | planned |
| V64 | The deck arc: teardown first, concede three times | investors | narrative/pitch_deck.md | html | planned |

## 8. Deliberately not drawn

Recorded with reasons, per the skill's instruction that rows are dropped only with a stated reason.

| Row from the standard set | Why not |
|---|---|
| **Use-of-funds milestone map** | `financials/use_of_funds.md` does not exist and will not — excluded by ASSUMPTIONS A1, since there is no raise. Drawing a use-of-funds map would invent the artifact the pack deliberately refused |
| **Revenue build / path-to-$100M chart** | Same basis. A1 excludes `revenue_build.md`; a hockey stick would be fabrication |
| **Exit comparables corridor** | Same basis. A1 excludes `comps_exits.md` |
| **UX collages in product chrome** | Deferred, not dropped. The UX spec is a text specification with no rendered screens; a mock collage would assert an interface that has not been designed. Revisit when screens exist |
| **PNG rasters for every row** | No text-to-image capability in this session. Every row keeps its HTML, which carries the content. Prompts are written in `image_prompts.md` so a later session or a human can render them |

## 9. Honest state of this phase

- **64 rows.** 11 are already satisfied by Mermaid diagrams inside their source artifacts and need no separate file.
- **53 rows need an HTML infographic.** Status is written from `ls` at the end of every working session, never from memory.
- **0 rasters, and that is expected.** `docimages.json` maps PNGs only, so it will report zero placements until a session with image generation runs `image_prompts.md`. The HTML files are the deliverable; the rasters are polish.
- **This manifest is the contract.** A visual that is not on this list should not exist, and a row that is marked `html` without a file on disk is a defect the audit will catch.
