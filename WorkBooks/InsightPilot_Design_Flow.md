# InsightPilot: Complete Design Flow

> **Purpose of this document:** this flow is here to help you understand the class diagrams (Figs. 3a, 3b and 3c). It follows one question from start to finish and names the class and method that acts at each step, so you can trace every box and arrow in the diagrams to what it does at runtime.

It covers the full design, including the parts scheduled for CMPE 295B, which are marked as such.

| Figure | File | Shows |
|---|---|---|
| Fig. 1 | `Workbook 1 - Group Submission.docx` (figure1.png) | System architecture (function + technology), as submitted |
| Fig. 2 | `assets/ch6_status.png` | As-built status of each architecture component |
| Fig. 3a | `assets/ch6_class_domain.png` | Domain model: what is stored |
| Fig. 3b | `assets/ch6_class_services.png` | Services: who resolves, plans, executes, verifies and composes |
| Fig. 3c | `assets/ch6_class_answer.png` | Answer presentation: what the analyst sees |

Source design documents: `runs/insightpilot/tech/architecture/D01–D10`, `runs/insightpilot/tech/deep_dives.md`, `runs/insightpilot/product/ux_spec.md`.

**Running example:** *"Which customers generated the highest transaction value?"*

---

## 1. Ask

1. **The analyst types the question** in the Investigation Workspace.
   - `Investigation.ask(text)` creates a **Question** (`status = CLARIFYING`).
   - A follow-up is a new Question in the same Investigation and inherits its context.

## 2. Understand the terms

2. **The Orchestrator invokes `SemanticResolver.resolve(question)`.**
   - Existing **Bindings** are checked first. Definitions from the dbt **SemanticSupplier** (CMPE 295B) take precedence over inferred ones.
   - Unknown terms are matched against the schema (BM25 + embeddings via ModelClient), using `SourceConnector.describe()` and `sample()`.
3. **Is any term ambiguous?** For example, "transaction value" could mean debits + credits, or debits only.
   - **If yes:** `ask(term, candidates)`. The analyst picks one on **PlanApproval**, and `confirm()` saves a new **Binding** (`ANALYST_CONFIRMED`), so the same question is never asked twice.
   - **If no:** continue (`status = PLANNING`).

## 3. Plan and approve

4. **The Orchestrator invokes `PlanSynthesiser.synthesise(question, bindings)`.** It reasons via ModelClient on the **frontier** model and produces a **Plan**, a DAG of **PlanSteps**:

   ```
   S1 FETCH      customer_360 totals            (Postgres)
   S2 AGGREGATE  debits + credits per customer   depends_on S1
   S3 RANK       top 20 by total value          depends_on S2
   ```

5. **`Plan.validate()`** checks four things: the sources are connected, inputs exist upstream, there are no cycles, and every column is bound. If validation fails, the plan is refused and the missing piece is named.
6. **The Orchestrator awaits PlanApproval** (`status = AWAITING_APPROVAL`). The analyst can edit a step; `approve()` sets `Plan.status = APPROVED`. **No query runs before approval.**

## 4. Execute and verify, once per step (`status = EXECUTING`)

7. **`Orchestrator.run(plan)`** walks the DAG in dependency order. For each PlanStep:

   | # | Who | What happens |
   |---|---|---|
   | a | Orchestrator | **Dispatches** the step to a **SpecialistAgent**: FetchAgent for sources, AnalyticsAgent for earlier steps' outputs |
   | b | SpecialistAgent: **reason** | Builds the context (step goal, bindings, schema) and **reasons via** ModelClient (frontier model) to write the SQL |
   | c | SpecialistAgent: **act** | Checks the SQL is read-only and in scope, then **acts via** `SourceConnector.execute(sql)`. Every statement is logged as an **AuditEvent**. |
   | d | SpecialistAgent: **observe** | If the SQL errors, `repair(sql, error)` sends the error back to the model and retries, up to the Orchestrator's `retry_cap` |
   | e | SpecialistAgent to Orchestrator | **Returns** a **StepResult** (title, SQL executed, attempts, rows in/out, grain, output_ref, sample rows), which the **Orchestrator receives**. It never goes to another agent or straight to the UI. |
   | f | Orchestrator to **HopVerifier** | `verify(result)` runs independent SQL checks with **no model call**, producing **CheckResults** and a hop state of GREEN, AMBER or RED |
   | g | Orchestrator to **LineageRecorder** | `record(step, result, checks)` saves a **Hop**: metadata in the Application Store, the full result in the Artifact Store |
   | h | UI, live | A collapsed panel appears under the question: `▸ ⚠ Top 20 customers by total transaction value [SQL] [rows] [Replay]` |
   | i | Orchestrator | **RED** halts the remaining steps. **AMBER** continues and keeps the warning. **GREEN** continues. |

   **When a step joins two sources** (for example the warehouse and `regions.csv`), the Orchestrator also invokes **`CrossSourceReconciler.propose(a, b)`**. It creates a **MappingProposal** (for example "8% of region codes unmatched"), which becomes a **Binding** (`kind = JOIN_MAP`) once the analyst approves it.

## 5. Compose the answer

8. **When all hops are done,** `Orchestrator.compose_answer()` reads **all** the verified Hops together and builds the **Answer** from **AnswerBlocks**:

   | Block | Made by | Example |
   |---|---|---|
   | **TextBlock** (summary + Key Insights) | **Small model** via `ModelClient.prose()`, using only numbers from verified hops | "Vivek More generated the highest value at ₹2.52M ¹" |
   | **Citation** | Attached to each sentence | ¹ points to Hop S3 |
   | **TableBlock** | **No model.** The actual rows from `Hop S3.output_ref` | Top-20 grid with download |
   | **DoubtBlock** | **No model.** From AMBER/RED CheckResults | "⚠ S2: 3% of rows had no customer_id" |
   | **ChartBlock** + ChartSpec | VisualizationAgent (CMPE 295B) | Bar chart by customer segment |

9. **The Answer appears** below the hop panels (`Question.status = ANSWERED`, `review_state = UNREVIEWED`, shown as an amber banner).

## 6. Review and sign off

10. **The analyst can:**
    - **Click a ¹:** `Citation.open_hop()` shows that hop's SQL, row counts and checks.
    - **Replay a hop:** `LineageRecorder.replay(hop)` re-runs it against current data and diffs the result.
    - **Correct a hop:** an **Override**, which can update a Binding if the analyst chooses.
    - **Sign off:** a **SignOff** (`review_state = REVIEWED`), after which `Answer.export()` produces the self-contained file.

---

## In one line

**Question → Resolver (Bindings) → Synthesiser (Plan) → analyst approves → for each step: Orchestrator dispatches → Agent reasons (model) + acts (SQL) + repairs → StepResult → Orchestrator receives → Verifier (SQL checks) → Recorder (Hop, live panel) → compose_answer (small model, verified facts only) → Answer [Text + Citations, Table, Doubt, Chart 295B] → analyst reviews and signs off → export.**

## Design rules this flow enforces

- **Hub and spoke.** Every handoff goes through the Orchestrator. Agents never call each other.
- **Agents think and act within one step.** Each SpecialistAgent is an LLM-driven tool-use loop (reason via ModelClient, act via SourceConnector, observe and repair), read-only and retry-capped, inside one approved plan step.
- **ModelClient is the only route to a model.** Frontier model for plans and SQL; small model for answer prose. It also enforces schema-only or filtered-sample mode and tracks cost.
- **Checks never use a model.** The HopVerifier and CrossSourceReconciler issue independent SQL through the SourceConnector.
- **Humans gate the irreversible points.** Clarification and plan approval happen before execution; sign-off happens before export.
- **The answer only states verified numbers.** Tables and warnings are copied from hop data and checks; only the insight sentences are model-written, and each one cites its hop.
