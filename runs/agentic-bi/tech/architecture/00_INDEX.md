# Architecture — index

**What this is** — Ten diagrams covering the system end to end, each with a caption naming what a reviewer should notice and what it deliberately omits.
**Why it exists** — [deep_dives.md](../deep_dives.md) describes seven components in isolation; a reviewer needs to see how they compose, where the trust boundaries sit, and where the failure paths go. The specific failure this prevents: the architecture diagram that is boxes labelled "AI" — every diagram here shows a mechanism or it was cut.
**How to read it** — D03 and D08 carry the most weight; D06 is what unblocks the sale. A skeptic should attack D02, which shows the replanning loop that DABstep says is ≈15% reliable on hard tasks, and D09, which describes scalability for a product that has no users.
**Depends on / feeds** — Components from [deep_dives.md](../deep_dives.md); loop and principles from [product/PRD.md](../product/PRD.md); deployment constraint from ASSUMPTIONS A5. Feeds `narrative/` and the deferred visuals phase.

---

## The set

| # | Diagram | Shows | Reviewer should notice |
|---|---|---|---|
| [D01](D01_investigation_pipeline.md) | **Investigation pipeline, end to end** | Question → bindings → plan → execution → answer → export | Approval gates sit *before* execution, not after |
| [D02](D02_verify_replan_loop.md) | **Verify-and-replan closed loop** | The per-hop check, its failure branch, and replanning | The loop has a hard iteration cap and a partial-result exit |
| [D03](D03_agent_orchestration.md) | **Multi-agent orchestration** | Orchestrator and the four specialist agents, with handoff contracts | Agents never call each other — every handoff goes through the Orchestrator |
| [D04](D04_memory_schema.md) | **Durable record and binding store** | What persists per organisation, and what does not | Bindings carry provenance; the flywheel is a data model, not a metaphor |
| [D05](D05_model_routing_cost.md) | **Model routing and cost control** | Which calls go to which model class, and the budget guards | Verification uses *no* model calls — it is SQL |
| [D06](D06_security_trust_boundary.md) | **Security and trust boundary** | What leaves the customer's environment, and what never does | The only egress is to the model provider, and it is configurable to schema-only |
| [D07](D07_connectors_ecosystem.md) | **Connectors and semantic-layer integration** | Source plug-ins and how an existing dbt/Cube layer is consumed | Semantic layers are *suppliers*, above the connector interface |
| [D08](D08_evaluation_harness.md) | **Evaluation, observability and safety** | The harness, the seeded-error path, and what each metric measures | This is feature #1, built before the agents |
| [D09](D09_deployment_scale.md) | **Deployment topology and scale** | Single-tenant self-hosted; where concurrency actually binds | The bottleneck is the analyst's review capacity, not the system |
| [D10](D10_human_in_the_loop.md) | **Human-in-the-loop and escalation** | Every point a human intervenes, by persona | Five distinct intervention points, three of them mandatory |

## Conventions

- **Solid arrows** = data flow. **Dashed** = control, approval or notification.
- **`[[ ]]`** = a durable write. **`{ }`** = a decision point.
- **Red-tinted nodes** = failure paths, drawn deliberately rather than omitted.
- Every diagram is Mermaid and renders natively in a GitHub-flavoured Markdown viewer.

## What the whole set deliberately omits

Named once here rather than repeated in ten captions.

1. **No multi-tenant control plane.** ASSUMPTIONS A5: open-core, self-hostable, single-tenant per deployment. D09 shows the topology this implies and nothing more.
2. **No streaming or real-time path.** PRD non-goal 6.
3. **No write-back path to any source.** PRD non-goal 4 — and its absence is what makes D06's trust boundary defensible.
4. **No fine-tuning or model-training infrastructure.** The system uses frontier models through an API with the customer's own key. Component 7's modelling agent trains *statistical models on customer data*, which is a different thing and appears in D03.
5. **No caching layer for result sets.** Plans are cached (D04); results are not, because a re-run against current data is the point.
