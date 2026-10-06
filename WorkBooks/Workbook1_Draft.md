# InsightPilot: An Agentic Platform for Conversational Business Intelligence

## Project Workbook

By

Atharva Kulkarni
Akshay Navani
Pranjal Shrivastava
Shantanu Zadbuke

October 8, 2026

Advisor: Professor Vijay Eranti

<<<PAGEBREAK>>>

**Project summary.** InsightPilot is a conversational business-intelligence platform for enterprise data analysts. An Orchestrator turns a business question into an *analysis plan* — an ordered set of tasks over named sources — shows that plan to the analyst before anything executes, and dispatches it to specialist agents for data fetch, analytics, visualization and machine learning. Every handoff emits its own *lineage*: the sources touched, the statement issued, the transform applied and the row counts in and out. Each hop is independently verified by a cheaper, structurally different query rather than by asking the model whether it is confident, so the analyst can inspect the single hop they doubt instead of re-deriving the whole chain. The unit of work is the *investigation* — one business question pursued to a verified answer — not the query. The project repository is [TEAM: repository URL].

**Team responsibilities.** Each member owns one technical area for the whole project and authored the corresponding workbook sections below.

Table 1. Team responsibilities and section ownership

| Member | Primary technical ownership | Workbook sections owned |
|---|---|---|
| Atharva Kulkarni | Orchestration tier: semantic resolver, plan synthesiser, orchestrator and replanner, model client | 1.1 (planning and agents), Ch. 3 requirements, 8.3–8.4 |
| Akshay Navani | Integration tier: Postgres and CSV/Excel connectors, application store, packaging | 1.1 (text-to-SQL), Ch. 5 architecture, 8.1–8.2 |
| Pranjal Shrivastava | Verification and evaluation: hop verifier, cross-source reconciler, evaluation harness | 1.1 (reliability and evaluation), Ch. 4 dependencies, 8.5, Ch. 9 schedule |
| Shantanu Zadbuke | Presentation and delivery: investigation workspace, plan review, lineage inspector and export, audit log | 1.2 state of the art, Ch. 2 justification, Ch. 6 and Ch. 7 planning |

<<<PAGEBREAK>>>

# Chapter 1. Literature Search, State of the Art

## Literature Search

This project sits at the intersection of four research areas: (i) natural-language-to-SQL generation over realistic enterprise schemas; (ii) multi-step planning and data reasoning by LLM agents; (iii) the reliability of agents across chained steps and repeated attempts; and (iv) automated machine learning on tabular data. The review below is organised along those lines and closes with the research gap this project addresses. Bracketed numbers refer to the References section at the end of this chapter.

**Natural language to SQL over realistic schemas.** Accuracy is strong but unevenly so, and the spread across evaluation settings carries more information than any headline figure. The Spider 2.0 benchmark family reports top systems at 96.70% execution accuracy on its Snow setting, 76.23% on Lite and **65.60% on the DBT setting** [1] — a 31-point drop for the same class of system once semantic-layer indirection and real project structure are introduced. BIRD, which evaluates over 12,751 question–SQL pairs across 95 databases, places the leading single model at 80.04% against **92.96% human performance** [2], leaving a residual gap of roughly 13 points on realistic data. A CIDR 2026 analysis of annotation quality [3] finds error rates in these benchmarks high enough that leaderboard differences of a few points carry no reliable meaning, a caution this project adopts directly by measuring its own fixed question set rather than citing leaderboard deltas. Production analysis is harsher: an examination of 4,602 incorrect queries attributes **81.2% of failures to schema-level errors** — wrong column selection and semantic misinterpretation rather than malformed syntax — reports 30–36% accuracy on schemas of roughly 1,000 columns and 54 tables, and records execution accuracy dropping up to 24 points under schema evolution [4]. The same analysis states the failure mode that shapes this project's design: *failure looks like a plausible but incorrect answer*. Execution-feedback reinforcement learning [5] shows that returning database errors to the generator makes smaller models competitive, and is the method adopted for this project's query repair loop.

**Multi-step planning and data reasoning.** This is the capability the Orchestrator depends on and the weakest measured capability in the literature. DABstep [6] draws over 450 tasks from a real financial-analytics workload, classifies 84% as Hard, and reports the best agents at **≈14.55–16% on that Hard split against 76.39% on Easy**, describing tasks that require several reasoning steps as largely unsolved. A survey of data-science automation evaluation [7] maps which capabilities have benchmarks and confirms multi-step analytical reasoning as sparsely measured.

**Agent reliability and error propagation.** Two findings govern any chained architecture. First, consistency degrades faster than capability: τ-bench [8] introduces the `pass^k` metric and shows a function-calling agent above 60% `pass^1` falling **below 25% `pass^8`**, with decay following `pass^k = p^k`. An analyst who asks the same question twice and receives two different answers has been given work, not leverage. Second, errors compound multiplicatively rather than additively; 95% per-step accuracy yields roughly 59% over ten steps and 90% yields about 35% [9]. Two independent taxonomies converge: an agent failure taxonomy spanning memory, reflection, planning, action and system levels identifies **error propagation as the primary reliability bottleneck** [10], and a diagnostic framework for tool invocation finds tool-initialisation failure to be the leading bottleneck, with an 89% error rate in a 3-billion-parameter model and the failure absent in large models [11]. That last result directly bounds this project's deployment design: a self-hosted orchestration layer must call a frontier-class model rather than a small local one.

**Agent task horizon.** METR reports the 50%-reliability task-length horizon doubling roughly every seven months over six years [12], and closer to every four months across 2024–2025 [13]. This is the strongest evidence that the class of system is newly worth attempting. The qualifier matters: the horizon is measured at **50% reliability**, which establishes a trajectory rather than a fitness threshold, since a 50%-reliable analytical answer has no value.

**Automated machine learning on tabular data.** MLE-bench evaluates agents on 75 curated Kaggle competitions scored by the original competition metrics [14], and AutoMLGen reports a **36.4% average medal rate and 18.7% gold under a 12-hour budget** [15]. The capability is real and no business-intelligence product exposes it. The 12-hour budget is the binding constraint: a conversational workflow cannot contain a 12-hour step, so the modelling agent in this project is time-boxed in minutes and publishes what it did not have time to attempt.

**Research gap.** The literature studies generation, planning, reliability and modelling largely in isolation, and the commercial systems surveyed in the next section each constrain correctness by requiring a human-authored semantic artifact before the question is asked. No published system combines (a) planning and replanning across heterogeneous sources with no pre-authored semantic model, (b) per-hop verification performed by a cheaper, structurally different query rather than by model self-critique, (c) hop-level lineage structured so that verification is cheaper than re-derivation, and (d) a published multi-hop execution accuracy and silent-error rate for the result. This project builds and measures such a system for the enterprise data analyst.

## State-of-the-Art Summary

Commercial products converged on one correctness mechanism: **constrain generation to a human-authored semantic artifact**. Snowflake Cortex Analyst generates SQL against a hand-authored YAML semantic model capped near 1 MB, roughly 32K tokens [16]; Databricks AI/BI Genie answers over a curated *space* with a documented ceiling of 30 tables per Genie Agent [17]; Power BI Copilot **cannot compute a metric that is not already a measure or column** [18]; and Tableau Pulse treats a pre-defined metric as the unit, pushing changes rather than answering asked questions [19]. Survey evidence confirms this is funded enterprise priority rather than vendor positioning: 59% of decision-makers at organisations above $100M revenue are directing incremental budget to semantic layers, and 24.9% name accuracy and hallucination risk as their top reservation about generative AI in analytics [20].

The convergence is well-founded — a semantic layer attacks exactly the schema-level error class behind 81.2% of failures [4] — but it relocates cost rather than removing it. The artifact is hand-authored, hand-maintained and bounded, so **the better the correctness mechanism, the narrower the set of questions the product will attempt**, and an ad-hoc question is by definition one nobody modelled in advance.

Two further developments matter. Databricks shipped **Inspect** (Beta), in which Genie re-reads its own generated SQL, authors smaller statements to verify specific aspects of it, and regenerates on failure [17] — verification by decomposition, the same insight this project's hop verifier rests on, reached independently by the strongest incumbent, though applied within a single query rather than across a multi-source plan. Separately, the Model Context Protocol, announced in November 2024 [30] and placed under the Linux Foundation's Agentic AI Foundation in December 2025 with support from Google, Microsoft and AWS [31], standardises tool *access* but not *semantics* [21], which makes a pluggable connector layer tractable for a small team while leaving the schema-understanding problem untouched.

The category also has a documented record of failure. IBM Watson Analytics was discontinued in 2019 [22]; Narrative Science was folded into Tableau in 2021 [23]; Sisu Data raised approximately $128.7M attacking automated diagnosis and became a Snowflake division in 2023 [24]; and Power BI Q&A, which shipped inside the most widely deployed BI tool in the enterprise, is **fully retired by the end of December 2026** [25]. None failed for lack of distribution.

Table 2. Leading industry offerings compared with this project

| Offering | Primary customer | What it provides | Gap for the enterprise analyst |
|---|---|---|---|
| Snowflake Cortex Analyst [16] | Snowflake enterprises | Text-to-SQL constrained to a hand-authored YAML semantic model | Snowflake-only; the model is capped near 32K tokens and takes weeks to author; no planning, charting or follow-up |
| Databricks AI/BI Genie [17] | Lakehouse enterprises | Conversational queries over a curated space; Inspect self-verifies within one query | Ceiling of 30 tables per Genie Agent; single warehouse, single hop; no modelling step |
| Power BI Copilot [18] | Any Fabric customer | Natural language over an existing Power BI semantic model | Cannot compute a metric that is not already a measure, so it cannot answer a genuinely ad-hoc question |
| Tableau Pulse [19] | Tableau Cloud | Metric monitoring with natural-language explanation | Inverts the loop by pushing metric changes; composite metrics and multi-step reasoning work poorly |
| Wren AI [26] | Open-source GenBI | Open-source agent with its own modelling language; 13,000+ GitHub stars | Text-to-SQL plus charts; no cross-source replanning and no hop-level verification |
| Hex Notebook Agent [27] | Analyst-native | Agent inside a SQL and Python notebook; every step visible and re-runnable | The analyst still directs every hop; no plan produced up front and no replanning on invalidation |
| **This project** | **Enterprise data analysts** | **Plan-and-replan across Postgres, files and APIs with hop-level lineage, per-hop verification and a published accuracy figure** | **—** |

**Leading-edge techniques adopted:** hybrid schema linking with reciprocal rank fusion and margin-based ambiguity detection; constrained generation into a typed plan DAG with static validation before execution; verification by decomposition in the style of Genie's Inspect [17] but applied across a multi-source plan; execution-feedback query repair [5]; consumption of existing dbt or Cube semantic layers when present rather than requiring a new one; and repeated-trial reliability measurement using `pass^k` [8].

**What no vendor publishes.** No commercial agentic-BI product publishes an execution-accuracy figure on any public benchmark. Every accuracy number in this workbook therefore comes from an academic leaderboard or third-party analysis, never from a vendor's own claim, and no comparative accuracy claim against an incumbent is available to anyone in this category, including this project.

## References

1. Lei, F., Chen, J., Ye, Y., Cao, R., Shin, D., Su, H., Suo, Z., Gao, H., Hu, W., Yin, P., Zhong, V., Xiong, C., Sun, R., Liu, Q., Wang, S., & Yu, T. (2025). Spider 2.0: Evaluating language models on real-world enterprise text-to-SQL workflows. In *International Conference on Learning Representations (ICLR)*. arXiv:2411.07763
   *Peer-reviewed benchmark for enterprise text-to-SQL workflows. The Snow, Lite and DBT accuracy figures quoted are read from the project's public leaderboard, https://spider2-sql.github.io/.*

2. Li, J., Hui, B., Qu, G., Yang, J., Li, B., Li, B., Wang, B., Qin, B., Cao, R., Geng, R., Huo, N., Zhou, X., Ma, C., Li, G., Chang, K. C. C., Huang, F., Cheng, R., & Li, Y. (2023). Can LLM already serve as a database interface? A big bench for large-scale database grounded text-to-SQLs. In *Advances in Neural Information Processing Systems (NeurIPS) 36*. arXiv:2305.03111
   *The BIRD benchmark: 12,751 question-SQL pairs across 95 databases, with the human-performance baseline this workbook compares against.*

3. Jin, T., Choi, Y., Zhu, Y., & Kang, D. (2026). Text-to-SQL benchmarks are broken: An in-depth analysis of annotation errors. In *Conference on Innovative Data Systems Research (CIDR '26)*, January 18-21, 2026, Chaminade, USA.
   *Peer-reviewed analysis establishing that small leaderboard differences are not meaningful; the reason this project measures its own fixed question set.*

4. Omni Analytics. (2026, April 8). Why text-to-SQL fails. https://omni.co/blog/why-text-to-sql-fails
   *Industry analysis of 4,602 incorrect queries; source of the 81.2% schema-error figure and the "plausible but incorrect" characterisation of failure.*
5. Snowflake. (2025). Arctic-Text2SQL-R1: SQL generation benchmark. https://www.snowflake.com/en/blog/engineering/arctic-text2sql-r1-sql-generation-benchmark/
   *Execution-feedback reinforcement learning for SQL generation; the basis for this project's query repair loop.*
6. Egg, A., Iglesias Goyanes, M., Kingma, F., Mora, A., von Werra, L., & Wolf, T. (2025). DABstep: Data agent benchmark for multi-step reasoning. arXiv:2506.23719
   *450+ real analytics tasks; the ~14.55-16% Hard-split result that is this project's central risk expressed as a benchmark.*

7. Testini, I., Hernández-Orallo, J., & Pacchiardi, L. (2025). Measuring data science automation: A survey of evaluation tools for AI assistants and agents. arXiv:2506.08800
   *Survey of the data-science-agent evaluation landscape; shows which capabilities have benchmarks and which do not.*

8. Yao, S., Shinn, N., Razavi, P., & Narasimhan, K. (2024). τ-bench: A benchmark for tool-agent-user interaction in real-world domains. arXiv:2406.12045
   *Introduces the pass^k reliability metric and the collapse from above 60% pass^1 to below 25% pass^8.*

9. Zartis. The compounding errors problem: Why multi-agent systems fail. https://www.zartis.com/the-compounding-errors-problem-why-multi-agent-systems-fail-and-the-architecture-that-fixes-it/
   *Worked compounding arithmetic across chained steps; the framing is vendor-authored and only the arithmetic is used.*
10. Zhu, K., Liu, Z., Li, B., Tian, M., Yang, Y., Zhang, J., Han, P., Xie, Q., Cui, F., Zhang, W., Ma, X., Yu, X., Ramesh, G., Wu, J., Liu, Z., Lu, P., Zou, J., & You, J. (2025). Where LLM agents fail and how they can learn from failures. arXiv:2509.25370
    *Agent error taxonomy across memory, reflection, planning, action and system levels, identifying error propagation as the primary reliability bottleneck.*

11. Huang, D., Malwe, G., & Wang, Z. (2026). When agents fail to act: A diagnostic framework for tool invocation reliability in multi-agent LLM systems. In *9th International Conference on Artificial Intelligence and Big Data (ICAIBD)*. arXiv:2601.16280
    *Twelve-category error taxonomy; the 89% tool-initialisation error rate in small models that bounds this project's deployment model.*

12. METR. (2025, March 19). Measuring AI ability to complete long tasks. https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/
    *Task-horizon doubling approximately every seven months; research-organisation report rather than a peer-reviewed paper.*
13. METR. (2026, January 29). Time horizon 1.1. https://metr.org/blog/2026-1-29-time-horizon-1-1/
    *Updated horizon estimate placing the 2024–2025 doubling closer to every four months.*
14. Chan, J. S., Chowdhury, N., Jaffe, O., Aung, J., Sherburn, D., Mays, E., Starace, G., Liu, K., Maksin, L., Patwardhan, T., Weng, L., & Mądry, A. (2024). MLE-bench: Evaluating machine learning agents on machine learning engineering. arXiv:2410.07095
    *75 Kaggle competitions scored by original competition metrics; the standard harness for autonomous ML engineering.*

15. Du, S., Yan, X., Jiang, D., Yuan, J., Hu, Y., Li, X., He, L., Zhang, B., & Bai, L. (2025). AutoMLGen: Navigating fine-grained optimization for coding agents. arXiv:2510.08511
    *36.4% medal rate and 18.7% gold on MLE-bench under a 12-hour budget; the result that forces a minutes-long time box.*

16. Snowflake. Cortex Analyst documentation. https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst
    *Vendor documentation of the semantic-model-first mechanism and its ~1 MB / 32K-token ceiling.*
17. Databricks. AI/BI and Genie release notes 2026. https://docs.databricks.com/aws/en/ai-bi/release-notes/2026
    *Vendor documentation of the Inspect self-verification feature and the 30-table Genie Agent limit.*
18. NeuralFlow. (2026). Power BI Copilot in 2026: Cost, setup, and honest review. https://neuralflow.es/en/blog/power-bi-copilot-guide/
    *Third-party review documenting the existing-measures-only constraint and weakness at reconciliation reasoning.*
19. Tableau. Tableau metrics and natural language query evolve with Tableau Pulse. https://www.tableau.com/blog/tableau-metrics-and-natural-language-query-evolve-tableau-pulse
    *Vendor description of the metric-as-unit mechanism and its push semantics.*
20. Futurum Group. (2026). Enterprise data analytics survey (n=818). https://futurumgroup.com/press-release/enterprise-data-analytics-survey-finds-59-investing-in-semantic-layers-as-critical-ai-infrastructure/
    *Named survey with disclosed sample; the 59% semantic-layer investment and 24.9% accuracy-reservation figures.*
21. Model Context Protocol. (2025). *Specification, version 2025-11-25.* https://modelcontextprotocol.io/specification/2025-11-25
    *The authoritative protocol definition; the basis for the claim that MCP standardises tool access rather than meaning.*

22. IBM Community. (2019). IBM Watson Analytics free edition trial has expired. https://community.ibm.com/community/user/discussion/ibm-watson-analytics-free-edition-trial-has-expired
    *Record of the discontinuation of the flagship natural-language BI product of its generation.*
23. TechTarget. (2021). Tableau completes acquisition of Narrative Science. https://www.techtarget.com/searchbusinessanalytics/news/252511067/Tableau-completes-acquisition-of-Narrative-Science
    *Acquisition record for a natural-language-generation company absorbed by the platform that owned the data.*
24. Crunchbase. Snowflake acquires Sisu Data. https://www.crunchbase.com/acquisition/snowflake-computing-acquires-sisu-data--ea3bc847
    *Records approximately $128.7M raised before acquisition by the warehouse vendor.*
25. Microsoft Fabric. (2026). Deprecating Power BI Q&A. https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Deprecating-Power-BI-Q-amp-A/ba-p/5173970
    *Full retirement of Q&A by the end of December 2026, with users directed to Copilot.*
26. Canner. WrenAI repository. https://github.com/Canner/WrenAI
    *Open-source GenBI agent with 13,000+ stars; the nearest open-source neighbour to this project.*
27. Hex. (2026). How Hex's Notebook Agent changed pricing analysis. https://hex.tech/blog/notebook-agent-pricing-analysis/
    *The notebook-as-lineage mechanism that sets the bar any traceability claim must beat.*
28. dbt Labs. (2026). State of analytics engineering (n=363, fielded December 2025 – February 2026). https://www.getdbt.com/resources/state-of-analytics-engineering-2026
    *Trust in data rising from 66% to 83% year over year; 71% cite hallucinated output reaching stakeholders as a top concern.*
29. IBM. (2026, March 30). Data delivery delays are slowing decisions more than you think. https://www.ibm.com/think/insights/data-access-delays-slowing-decisions
    *Reports one-to-four-week enterprise data-request turnaround (attributed to Sigma Computing) and that 76% of businesses have decided without consulting data because access was too difficult (attributed to Sisense). A citation chain rather than a primary study, and cited as such.*
30. Anthropic. (2024, November 25). Introducing the Model Context Protocol. https://www.anthropic.com/news/model-context-protocol
    *The announcement that dates the protocol's release, with reference servers including Postgres among the originals.*
31. Linux Foundation. (2025, December 9). Linux Foundation announces the formation of the Agentic AI Foundation. https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation
    *Records the transfer of MCP to a neutral foundation co-founded by Anthropic, Block and OpenAI, with support from Google, Microsoft and AWS.*

<<<PAGEBREAK>>>

# Chapter 2. Project Justification

**The problem.** An enterprise data analyst absorbs a continuous queue of ad-hoc business questions, each costing the same manual sequence: locate the source, inspect the schema, write and debug the query, reconcile across sources, chart, interpret and verify. Reported enterprise turnaround for a data request is one to four weeks, and 76% of businesses report having made a decision without consulting data because access was too difficult [29]. The organisation's most common response to a slow analytics function is to decide without it.

**Why speed is not the binding constraint.** Every major vendor has shipped natural-language querying, and the measured evidence says trust rather than latency is what blocks adoption. Practitioner survey data shows trust in data rising from 66% to 83% as a stated priority in a single year, with **71% naming incorrect or hallucinated output reaching stakeholders as a top concern** [28], and 24.9% naming accuracy and hallucination risk as their top reservation about generative AI in analytics [20]. The failure mode is specific and documented: wrong answers are *plausible*, with schema-level errors accounting for 81.2% of analysed failures [4]. A fast answer nobody will stake their name on is not an answer.

**Why now.** Three conditions hold that did not hold two years ago. Agent task horizons have been doubling every four to seven months [12][13]; tool access has been standardised by MCP, announced in November 2024 [30] and now stewarded by the Linux Foundation's Agentic AI Foundation with support from Google, Microsoft and AWS [31], which turns connector integration into a configuration problem; and single-hop text-to-SQL on realistic schemas now reaches 96.70% on the strongest benchmark setting [1], which makes the individual steps of a plan worth composing. What has *not* arrived is reliable multi-step composition, measured at ≈14.55–16% on hard real-world tasks [6] — which is why this project's design centre is making failure cheap to detect rather than promising it will not occur.

**Why this approach and not a better semantic layer.** Every incumbent establishes correctness by requiring a human-authored artifact before the question is asked, and that artifact is bounded: 30 tables per Genie Agent [17], roughly 32K tokens of YAML [16], existing measures only [18]. The tighter the guardrail, the narrower the answerable question set, and an ad-hoc question is by construction one nobody anticipated. This project inverts the arrangement: the plan is produced at question time from whatever sources are connected, each hop is checked by a cheaper structurally different query, and the resulting trace is structured so the analyst inspects the one hop they doubt rather than re-deriving the chain. The system *consumes* a dbt or Cube semantic layer when one exists but never requires one.

**Why it is academically worthwhile.** The project's central dependency is the field's weakest measured capability [6], and **no commercial agentic-BI product publishes an execution-accuracy figure on any public benchmark**. A capstone that builds an evaluation harness with a fixed question set and a seeded-error set, then publishes both its multi-hop execution accuracy and its silent-error rate, produces a measurement the entire commercial category currently withholds. That is a contribution independent of whether the product succeeds commercially, and it is the basis for a derivative paper.

**Why it is worth two semesters.** CMPE 295A delivers the measurement infrastructure and one narrow path: the harness and question set, Postgres and CSV connectors, plan generation with an approval gate, fetch and analytics agents, lineage capture, hop verification and an exportable investigation record. CMPE 295B extends to replanning, hop override, a third source type, semantic-layer consumption and the time-boxed modelling agent. Each semester has a defensible deliverable, and the first does not depend on the second succeeding.

**Publication and funding potential.** The target derivative paper is on measuring verification cost and silent-error rate for cross-source agentic business intelligence, reporting multi-hop execution accuracy, verifier coverage against a seeded-error set, and the cost per investigation split by retry count — none of which any vendor in this category publishes. [TEAM: confirm candidate venues with the advisor.] The working prototype, the published question set and the measured results make the project suitable for presentation at the SJSU Expo.

**What this project does not claim.** The mechanism arithmetic comes to approximately **2.9× on work time for a multi-source question, not 10×**, with a plausible band of 1.8×–4.2×, and approximately 1.0× — no gain — on a single-source familiar question where the analyst should keep writing SQL. No comparative accuracy claim is made against any incumbent, because none publishes a figure to compare against. The project's riskiest assumption — that verifying an answer you did not derive is cheaper than deriving it — is untested, and measuring it is the first task of CMPE 295A.

<<<PAGEBREAK>>>

# Chapter 3. Project Requirements

## Actors and scope

Table 3. Actors

| Actor | Description | Main goals |
|---|---|---|
| Data analyst (primary user) | Enterprise analyst who already writes SQL and absorbs an ad-hoc request queue | Reach a verified answer to a multi-source question faster than deriving it; retain control and the ability to override |
| Business stakeholder | Non-technical requester who consumes answers and cannot verify them | Get a plain-language answer with its provenance, clearly marked when not yet reviewed |
| Staff data scientist | Senior reviewer who audits method and lineage | Inspect method-level detail, override modelling choices, catch what the system could not |
| Analytics budget owner | Economic buyer; not a user | Provenance retained and queryable across investigations; adoption observable |
| Data platform lead | Security and governance gate; can veto without using the product | Read-only access, credentials inside the boundary, a readable audit log of every query issued |
| External data sources | Postgres, CSV/Excel files, REST JSON APIs, dbt/Cube semantic layers | Accessed read-only through connectors with inherited permissions |
| Model provider | Frontier LLM API reached with the customer's own key | Used for planning, term resolution and SQL generation only; never for verification |

## Use cases

Table 4. Use-case catalogue

| ID | Use case | Primary actor | Summary |
|---|---|---|---|
| UC-01 | Connect a data source | Analyst | Register a read-only Postgres connection or upload a CSV/Excel file; inferred schema shown for correction |
| UC-02 | Ask a question | Analyst | Pose a business question inside an investigation that retains context and established facts |
| UC-03 | Resolve ambiguous terms | System / Analyst | When a term maps to more than one column or grain, halt and ask rather than guess; confirmed bindings persist |
| UC-04 | Review and approve a plan | Analyst | Inspect the generated analysis plan, edit it, and approve before anything executes |
| UC-05 | Execute an investigation | System | Specialist agents run plan steps; each handoff emits structured output and lineage |
| UC-06 | Verify a hop | System | Each step is checked by a cheaper, structurally different query; failures surface immediately |
| UC-07 | Replan on invalidation | System | A failed check invalidates the remaining sub-plan, which is regenerated with the failure as context |
| UC-08 | Inspect lineage | Analyst / Data scientist | Open any hop to see sources touched, statement issued, transform applied and row counts in and out |
| UC-09 | Re-run or override a hop | Analyst | Re-execute one hop in isolation and diff against the stored result, or override it and re-flow downstream |
| UC-10 | Export an investigation | Analyst | Produce one self-contained artifact that renders without the application running |
| UC-11 | Sign off an answer | Analyst | Mark an investigation reviewed, by whom and when; unreviewed answers are gated on export |
| UC-12 | Audit queries issued | Platform lead | Read an append-only log of every statement issued to every source, without the product running |
| UC-13 | Measure accuracy | Team | Run the fixed question set and the seeded-error set through the harness and publish the results |

## Functional requirements

Priorities follow the template: **E = Essential** (required for a working system at the end of CMPE 295B), **D = Desired** (planned and scheduled), **O = Optional** (stretch goals). Each requirement is uniquely identified, verifiable by the acceptance criterion given, and traceable to a use case, following the characteristics of a good SRS in IEEE 830 section 4.3.

Table 5. Functional requirements

| ID | User story | Pri. | Trace | Acceptance criterion |
|---|---|---|---|---|
| FR-01 | As a team, we want a fixed question set with ground-truth answers and an automated harness, so accuracy can be measured rather than asserted. | E | UC-13 | 30–50 questions execute unattended; execution accuracy reported per run and on every merge |
| FR-02 | As a team, we want a seeded-error set with planted wrong joins, grains and mappings, so silent errors can be counted. | E | UC-13 | Each seeded defect is labelled; the harness reports which were caught and which escaped every check |
| FR-03 | As an analyst, I want a read-only Postgres connection, so the system can query the warehouse without write access. | E | UC-01 | Connection rejects any DDL or DML; schema introspection lists tables, columns, types and foreign keys |
| FR-04 | As an analyst, I want to upload CSV or Excel files and see the inferred schema, so unmodelled sources are usable. | E | UC-01 | File loads via DuckDB with no ETL step; inferred types shown and correctable before use |
| FR-05 | As an analyst, I want the system to produce an ordered analysis plan over named sources, so the approach is explicit before execution. | E | UC-02 | Plan is a typed DAG; static validation rejects cycles, unknown sources and unresolved columns |
| FR-06 | As an analyst, I want to see, edit and approve the plan before anything runs, so errors are caught before they cost a query. | E | UC-04 | No query executes before approval on first run against a source; edits persist into execution |
| FR-07 | As an analyst, I want ambiguous terms intercepted rather than guessed, so I do not receive a plausible wrong answer. | E | UC-03 | When top candidates fall within the margin or differ in grain, execution halts and candidates are shown with evidence |
| FR-08 | As an analyst, I want confirmed term bindings stored and reused, so the same clarification is not requested twice. | E | UC-03 | Binding persists per organisation with provenance; later questions reuse it; stale bindings flagged on schema change |
| FR-09 | As an analyst, I want fetch and analytics agents that execute plan steps, so questions are actually answered. | E | UC-05 | Joins, filters, aggregations and period comparison produce results with row counts and declared grain |
| FR-10 | As an analyst, I want every handoff to record its lineage, so the answer arrives with a trace. | E | UC-05 | Each hop records sources, exact statement, parameters, transform, grain and row counts in and out |
| FR-11 | As an analyst, I want each hop verified by a different, cheaper query, so failures surface at the hop that caused them. | E | UC-06 | Row-count, grain, coverage, null-rate and boundary-total checks run per applicable step; results stored with the hop |
| FR-12 | As an analyst, I want to open a hop and read it as a step rather than a JSON blob, so verification takes seconds. | E | UC-08 | Hop view shows statement, inputs, outputs, counts and check results on one screen |
| FR-13 | As an analyst, I want to re-run a single hop in isolation and diff it, so I can confirm reproducibility. | E | UC-09 | Re-run uses the recorded statement and parameters; differences are shown rather than silently overwritten |
| FR-14 | As an analyst, I want to export a self-contained investigation artifact, so the result can be checked without the product. | E | UC-10 | Single file renders in a browser or text editor with question, plan, hops, statements, counts and answer |
| FR-15 | As an analyst, I want the system to name the hops it is least certain about, so doubt is visible. | E | UC-06 | Doubt block lists least-certain hops with reasons; no confidence percentage is presented as accuracy |
| FR-16 | As a platform lead, I want an append-only log of every query issued, so the system can be audited independently. | E | UC-12 | JSONL file on disk readable without the application; records timestamp, source, statement and actor |
| FR-17 | As an analyst, I want an investigation thread that inherits context, so follow-ups do not restate everything. | E | UC-02 | Established facts, source scope and bindings carry into the next question in the thread |
| FR-18 | As an analyst, I want the plan regenerated when a check fails, so a bad step does not propagate. | D | UC-07 | Failed verification invalidates the remaining sub-DAG and triggers one bounded regeneration with the failure as context |
| FR-19 | As an analyst, I want to override a hop and have downstream steps re-flow, so I can correct the system. | D | UC-09 | Override persists as a binding; downstream steps re-execute, or the plan is invalidated and replanned if the grain changes |
| FR-20 | As an analyst, I want a REST JSON connector, so a third source type is usable. | D | UC-01 | Configurable endpoint and response shaping; results enter the plan as an ordinary source |
| FR-21 | As an analyst, I want dbt or Cube definitions consumed when present, so existing correctness work is inherited. | D | UC-03 | Where a semantic-layer definition exists for a term it takes precedence over any inferred binding |
| FR-22 | As a stakeholder, I want unreviewed answers clearly marked and gated, so an unverified number does not reach a slide. | D | UC-11 | Export of an unreviewed investigation requires explicit acknowledgement; sign-off records reviewer and time |
| FR-23 | As an analyst, I want the same question to reuse its approved plan, so answers are reproducible. | D | UC-04 | Plan cache keyed on normalised question, bindings, source set and schema version; a schema change misses the cache |
| FR-24 | As a data scientist, I want a time-boxed modelling step with a model card, so predictions are reviewable. | D | UC-05 | Model card states target definition, split strategy, features used and excluded with reasons, and an explicit not-attempted list |
| FR-25 | As an analyst, I want a chart chosen and justified by data shape, so results are presentable. | O | UC-05 | Chart type is named with the reason; a table is an acceptable fallback |
| FR-26 | As an analyst, I want cost and latency previewed per plan, so expensive investigations are visible before running. | O | UC-04 | Estimated token cost and wall-clock shown at the approval gate |
| FR-27 | As a new user, I want to reach a first successful investigation quickly from a clean checkout. | O | UC-01 | Docker Compose quickstart with seeded demo data; median clone-to-first-investigation under 30 minutes |

## Non-functional requirements

Table 6. Non-functional requirements

| ID | Category | Requirement (measurable) | Pri. |
|---|---|---|---|
| NFR-01 | Security | All source access is read-only; no DDL, DML or write-back is possible from any agent path | E |
| NFR-02 | Security | Credentials remain inside the deployment boundary; the orchestration layer uses the customer's own frontier-model key and never logs secrets | E |
| NFR-03 | Security | Row- and column-level permissions are inherited from the source and never re-implemented; access failures fail closed | E |
| NFR-04 | Privacy | Columns flagged sensitive are excluded from value sampling and from model context; a schema-only mode is configurable | E |
| NFR-05 | Auditability | 100% of statements issued to any source appear in the append-only audit log, readable without the application running | E |
| NFR-06 | Reliability | Verification runs as plain SQL against the source and never as a model call, so it cannot share the failure mode it checks | E |
| NFR-07 | Reproducibility | A re-run of a recorded hop reproduces the stored result, or reports the difference; approved plans are reused for identical questions | E |
| NFR-08 | Accuracy | Multi-hop execution accuracy on the fixed question set is measured and published; baseline for comparison is ≈14.55–16% on DABstep Hard [6] | E |
| NFR-09 | Accuracy | At least 70% of seeded defects are rejected by the analyst with the trace, and at least twice the rate of a no-trace control | E |
| NFR-10 | Usability | Verification cost ratio — minutes to accept or reject an answer divided by minutes to derive it — has a median below 0.5; above 0.8 is a declared stop trigger | E |
| NFR-11 | Performance | The plan is presented within 15 seconds of the question for a six-hop plan on the reference schema | D |
| NFR-12 | Cost | Cost per investigation is recorded and reported split by retry count, since expected attempts dominate the cost model | D |
| NFR-13 | Portability | The full stack starts locally with one `docker compose up`; median clone to first successful investigation under 30 minutes | D |
| NFR-14 | Maintainability | The harness runs in CI on every pull request; back-end unit-test coverage at or above 70% | D |
| NFR-15 | Compliance | The system produces answers only; it takes no autonomous action, sends no alerts that trigger workflows and makes no write-back | E |

## Constraints and assumptions

- All development and evaluation use public or synthetic datasets loaded into a local Postgres instance; no customer or confidential data is used at any point.
- Frontier-model usage is funded through provider credits and paid team accounts, with a spend ceiling enforced per environment.
- The system requires a frontier-class model API. A fully local small-model deployment is out of scope, because tool-initialisation failure reaches an 89% error rate in a 3-billion-parameter model [11].
- The project is a research prototype evaluated offline; it is not offered as a service and makes no availability guarantee.
- The team has four members; scope is sized to one narrow end-to-end path plus the measurement infrastructure in CMPE 295A.

<<<PAGEBREAK>>>

# Chapter 4. Dependencies and Deliverables

## Dependencies

Only showstopper dependencies — those that would halt the project if unavailable — are listed, each with a mitigation and an owner.

Table 7. Showstopper dependencies (AK = Atharva Kulkarni, AN = Akshay Navani, PS = Pranjal Shrivastava, SZ = Shantanu Zadbuke)

| ID | Dependency | Why it is a showstopper | Mitigation | Owner |
|---|---|---|---|---|
| D-01 | Frontier-model API access and budget | Planning, term resolution and SQL generation all require a frontier-class model; there is no viable local substitute, since tool-initialisation failure reaches 89% in a 3B model [11] | Provider-agnostic client so a second provider can be substituted; verification is pure SQL and consumes no tokens, which caps exposure | AK |
| D-02 | A realistic Postgres schema with a public or synthetic dataset | Every accuracy figure depends on a fixed question set over a known schema; a toy schema would make results meaningless, since accuracy falls to 30–36% on wide schemas [4] | Generate a synthetic dataset locally — seeded orders, shipments and an unmodelled carrier CSV — so no customer data is required and there is no external dependency once it is loaded | AN |
| D-03 | Ground-truth answers for the fixed question set | Without ground truth there is no execution-accuracy measurement, and that measurement is the project's primary publishable result | Authored by the team alongside the question set in Sprint 1; scoped work rather than an external dependency, but the project stalls without it | PS |
| D-04 | A reproducible environment every member can run | With four people working in parallel, anyone whose environment does not run the full stack is blocked | Docker Compose from the first sprint so the environment is reproducible rather than hand-configured | AN |
| D-05 | Analyst participants for the verification-cost study | The riskiest claim — that verification is cheaper than re-derivation — is measured with people, not code, and it gates the value of the whole architecture | Recruit five analysts from the SJSU MS cohort and professional networks; the task needs one hour per participant and no software | SZ |
| D-06 | Advisor approval of scope and evaluation plan | Work cannot be accepted for credit without it, and the evaluation design determines what the semester produces | Review requirements, architecture and the measurement plan with Prof. Eranti in October 2026 | All |

## Deliverables

Table 8. Project deliverables

| # | Deliverable | Description |
|---|---|---|
| 1 | Evaluation harness | Automated runner scoring multi-hop execution accuracy over a fixed question set, executed in CI on every merge |
| 2 | Fixed question set with ground truth | 30–50 questions over a known schema with authored expected results, published alongside the code |
| 3 | Seeded-error test set | Investigations with deliberately planted wrong joins, grains and mappings, used to measure silent-error rate |
| 4 | Connectors | Read-only Postgres connector and CSV/Excel ingestion through DuckDB, with inferred schema correction |
| 5 | Orchestrator and plan surface | Typed plan DAG with static validation, plus the review and approval gate shown before execution |
| 6 | Specialist agents | Data fetch/integration and analytics agents emitting structured output and lineage per handoff |
| 7 | Verification layer | Hop verifier with row-count, grain, coverage, null-rate and boundary-total checks, and the cross-source reconciler |
| 8 | Lineage store and inspector | Hop-level records with content-addressed step outputs, single-hop replay, and the readable hop view |
| 9 | Exportable investigation artifact | One self-contained file rendering without the application, carrying question, plan, hops, statements, counts and sign-off |
| 10 | Audit log | Append-only JSONL record of every statement issued to every source, readable without the product running |
| 11 | Published measurements | Multi-hop execution accuracy, silent-error rate and verifier coverage, reported with method and failure cases |
| 12 | Verification-cost study result | The timed task with five analysts, reported including if the result is negative |
| 13 | Derivative research paper | Paper on measuring verification cost and silent-error rate for cross-source agentic BI, submitted to a peer-reviewed workshop or conference, subject to advisor agreement |
| 14 | Documentation and demo | Architecture and setup documentation, a quickstart, a demo video and the Expo prototype |

<<<PAGEBREAK>>>

# Chapter 5. Project Architecture

Figure 1. System architecture showing each component's function and technology

<<<FIGURE:assets/ch5_architecture.png>>>

**Architectural style.** Six layered tiers inside a single-tenant deployment, with a strict separation between generation and verification: everything that *produces* an answer may call a language model, and everything that *checks* an answer may not. Checks run as independent SQL or local compute, because a model asked to review its own output shares the failure mode that produced it [17]. Two rules govern the whole figure. **All tasks and results are routed through the orchestrator — there are no direct agent-to-agent calls** — so every handoff is observable, budgeted and recorded. And **the arrows summarise tier interactions rather than execution order**: verification applies to each hop as it completes, not once at the end of the plan.

**Presentation tier.** The *investigation workspace* is where a question is asked and follow-ups inherit context. *Plan review and approval* is where ambiguity is clarified and the typed plan is edited and approved before anything executes; it converts the cost of a wrong plan from queries run and a wrong answer delivered into a single edit, and it is the only intervention that acts on error compounding before it begins. The *lineage inspector and export* replays individual hops and carries the analyst's sign-off into a self-contained artifact. React and TypeScript over a FastAPI service.

**Orchestration tier — custom Python 3.12.** The *semantic resolver* binds terms to columns and grain using BM25 over column names and comments fused with dense embedding retrieval, plus value-based linking against sampled values; where candidates are close or disagree on grain it halts and asks rather than guessing, because a silent argmax samples directly from the error class behind 81.2% of analysed failures [4]. The *plan synthesiser* uses constrained generation to emit a typed, cacheable plan DAG, and statically validates sources, inputs and cycles before execution — the plan is a data structure rather than free-text reasoning, which is why no off-the-shelf agent framework is used: most make the plan implicit in control flow and forfeit the approval gate. The *orchestrator and replanner* routes every task and handoff, owns execution state, and enforces budgets and retry caps; capped replanning with a partial-result exit is 295B scope. The *model client* is provider-agnostic and supports a schema-only or filtered-sample mode.

**Specialist agent tier.** The *fetch and integration agent* generates and repairs queries and prepares the data; the *analytics agent* performs joins, KPIs, trends, aggregation and comparison in SQL and pandas. The *visualization agent*, which returns a chart specification with its rationale, and the *ML agent*, which produces time-boxed baseline models with a model card and an uncertainty statement, are both 295B.

**Verification and lineage tier.** The *hop verifier* checks counts, grain, coverage, nulls, totals and type or range on each hop, using independent SQL rather than model self-critique. The *cross-source reconciler* profiles join keys and value overlap and **proposes** mappings for approval rather than applying them, since a region-code mapping is a business fact and not a string-similarity result. The *lineage recorder and replayer* records the query, grain, checks and any skipped checks for every hop, and replays a single hop to report differences. A failed check halts downstream work rather than letting a bad hop propagate.

**Integration tier — read-only.** A *PostgreSQL connector* that describes, samples, executes and profiles while inheriting the source's own read permissions, and a *CSV and Excel connector* that queries uploaded files through DuckDB, inferring and profiling schema with no ETL step. A *REST JSON connector* is 295B. *Semantic suppliers* — dbt in 295B, Cube later — sit on a separate interface, and their definitions take precedence over any inferred binding.

**Data, audit and evaluation tier.** The *application store* on PostgreSQL 16 holds bindings, plans, investigations, hop lineage, overrides and sign-off. The *artifact store* keeps recorded statements, step outputs and exports on the local filesystem. The *append-only audit log* records actor, source, statement and timestamp as JSONL that is readable without the application running. The *offline evaluation harness* runs the ground-truth question set and the seeded-error set under pytest to produce the accuracy and verifier-coverage figures this project publishes.

**What sits outside the customer environment.** Only the external model provider. A frontier model serves planning and SQL generation and a smaller model serves prose and chart choice, called over a provider-agnostic HTTPS API with the customer's own key; the request carries the question and schema with optional samples, and a PII-filtered or schema-only mode is configurable. Data-source access never leaves the deployment.

**Key flow — one investigation.** (1) The analyst asks a question spanning a warehouse table and an uploaded CSV. (2) The semantic resolver binds the terms, halting once to ask which of two columns means "region". (3) The plan synthesiser emits a typed DAG that static validation accepts. (4) The analyst reviews the plan, narrows one fetch, and approves it. (5) The orchestrator dispatches the first task to the fetch agent and receives its result; nothing passes directly between agents. (6) That hop's output is verified — counts, grain and coverage — before the next task is dispatched. (7) The coverage check finds 8% of region codes unmatched and surfaces it immediately instead of letting it propagate; the analyst accepts the proposed mapping, which persists as a binding. (8) The orchestrator dispatches the join and aggregation to the analytics agent, and each of those hops is verified in turn. (9) The answer is returned with its established facts and a doubt block naming the least certain hop, and after sign-off the investigation is exported as one self-contained file.

**Deployment.** One organisation per deployment, self-hosted with Docker Compose; the same Compose file is the basis of the under-30-minute quickstart. There is no hosted multi-tenant plane by design: the orchestration layer runs inside the customer's environment against their own model key.

<<<PAGEBREAK>>>

# Chapter 6. Project Design

To be completed in Workbook Assignment 2 (UML class and sequence diagrams for the plan DAG and the verification path, UI mockups for the investigation surface, plan review and lineage inspector, the database ER diagram for bindings and investigation records, and the plan and lineage schemas).

<<<PAGEBREAK>>>

# Chapter 7. QA, Performance, Deployment Plan

To be completed in Workbook Assignment 2 (test strategy, the harness as a continuous evaluation loop, the seeded-error protocol and verifier-coverage measurement, performance budgets per loop beat, cost benchmarking by retry count, and the deployment pipeline).

<<<PAGEBREAK>>>

# Chapter 8. Implementation Plan and Progress

Implementation follows a **measurement-first walking skeleton**: build the harness and the fixed question set before any agent, then make the thinnest end-to-end path work — connect a source, plan a question, execute two hops, verify them, record lineage and export the result — and deepen each component afterwards. The ordering is deliberate and is the opposite of demo-first: a system with four agents and no measurement cannot tell anyone whether it works. Status values below reflect the state of the repository on the date of this workbook.

## Programming and Execution Environment

Table 9. Programming and execution environment

| Layer | Technology (version) | Purpose | Owner | Status |
|---|---|---|---|---|
| Source control and CI | GitHub repository, GitHub Actions | Code hosting, pull-request review, harness run on every merge | AN | Repository created; CI in Sprint 1 |
| Language and runtime | Python 3.12 | All orchestration, agent and verification code | AK | Installed and verified by all four members |
| Orchestrator | Custom typed plan DAG (no agent framework) | The plan must be validatable, diffable and cacheable | AK | Sprint 1 spike |
| Model access | Provider-agnostic client; customer's own key | Planning, term resolution and SQL generation | AK | Sprint 1 spike |
| Database access | SQLAlchemy, psycopg | Read-only Postgres introspection and execution | AN | Sprint 1 |
| File and CSV engine | DuckDB | Query CSV, Excel and Parquet directly with no ETL step | AN | Sprint 1 |
| Profiling | DuckDB SQL, pandas | Cardinality, uniqueness, overlap and null-rate profiling | PS | Sprint 2 |
| Application store | PostgreSQL 16 | Bindings, investigation records, sign-off state | AN | Sprint 1 |
| Audit log | Append-only JSONL on disk | Readable without the application running | SZ | Sprint 2 |
| API and front end | FastAPI, React, TypeScript | Investigation surface, plan review, lineage inspector | SZ | Sprint 2 |
| Modelling (295B) | scikit-learn, LightGBM | Time-boxed baseline models within a minutes budget | PS | CMPE 295B |
| Packaging | Docker, Docker Compose | Reproducible local stack; later the quickstart | AN | Sprint 1 |
| Harness | pytest with a question-set fixture | Execution-accuracy and seeded-error measurement | PS | Sprint 1 |

## Development Tools per Team Member

Table 10. Development tools acquired per member (all installed and verified)

| Tool | Atharva Kulkarni | Akshay Navani | Pranjal Shrivastava | Shantanu Zadbuke |
|---|---|---|---|---|
| IDE with Python, TypeScript and Docker extensions | Yes | Yes | Yes | Yes |
| Python 3.12 toolchain and pytest | Yes | Yes | Yes | Yes |
| Docker Desktop and Docker Compose | Yes | Yes | Yes | Yes |
| PostgreSQL 16 locally or in Docker | Yes | Yes | Yes | Yes |
| DuckDB CLI and Python package | Yes | Yes | Yes | Yes |
| Frontier-model API key through the shared project account | Yes | Yes | Yes | Yes |
| Node and the front-end toolchain | Yes | Yes | Yes | Yes |
| Database client for schema inspection | Yes | Yes | Yes | Yes |
| GitHub Projects board for task tracking | Yes | Yes | Yes | Yes |

## Prototyping and Simulation Environment

The project is software-only, so the prototyping environment is a reproducible simulated analytics estate rather than hardware:

- **Local stack.** Docker Compose running PostgreSQL, the application services and the harness, so all four members run an identical environment.
- **Reference schema.** A synthetic dataset generated by the team and loaded into local Postgres, wide enough to be realistic — benchmark evidence shows accuracy falls to 30–36% on schemas of roughly 1,000 columns and 54 tables [4], so a narrow schema would flatter the system and teach nothing. The generator seeds orders, shipments, customers and regions across roughly 40 tables, plus a carrier CSV deliberately absent from the warehouse schema.
- **Unmodelled source.** A CSV file deliberately not represented in the warehouse schema, queried through DuckDB, providing the cross-source case no incumbent attempts.
- **Fixed question set.** 30–50 questions with authored ground truth covering single-source, cross-source and ambiguous-term cases.
- **Seeded-error set.** The same investigations with deliberately planted wrong joins, grains and region mappings, used to measure what escapes every check.

## Sample Programs and Technology Spikes

Table 11. Sample programs used to learn each technology (owner initials as in Table 7)

| Spike | Goal and what it proves | Owner | Target |
|---|---|---|---|
| SP-1 Postgres read path | Connect read-only, introspect the schema, execute a parameterised query and return row counts and grain | AN | Oct 11, 2026 |
| SP-2 DuckDB file path | Query a CSV directly with SQL, infer and correct types, and join it to a Postgres result | AN | Oct 11, 2026 |
| SP-3 Typed plan object | One model call returns a plan that parses into the typed DAG and passes static validation; an invalid plan is rejected with field-level errors | AK | Oct 11, 2026 |
| SP-4 Hop verification | Run row-count, grain and coverage checks against a deliberately broken join and confirm the failure is caught and reported | PS | Oct 25, 2026 |
| SP-5 Lineage record and replay | Record a hop, re-execute it from the record alone, and diff the result | SZ | Nov 8, 2026 |
| SP-6 Harness run | Execute five questions end to end with ground-truth comparison and print an accuracy figure | PS | Nov 22, 2026 |

A plan step as it appears in the typed DAG used by SP-3 (simplified):

```
step_id: s3
op: join
inputs: [s1, s2]
left_key: shipments.region_code
right_key: carrier_csv.region
declared_grain: [region_code, month]
checks: [row_count_reconciliation, grain_assertion, coverage]
expected_coverage_min: 0.95
```

## Prototype Implementation Plan

Table 12. Prototype increments for CMPE 295A

| Step | Increment | Technologies exercised | Sprint |
|---|---|---|---|
| 1 | Measurement first: repository, CI, harness skeleton, fixed question set with ground truth, seeded-error set | GitHub Actions, pytest, PostgreSQL | S1 |
| 2 | Source substrate: read-only Postgres connector and CSV/Excel ingestion with inferred schema | SQLAlchemy, psycopg, DuckDB | S1–S2 |
| 3 | Plan path: question to typed plan DAG, static validation, plan shown and approved | Provider-agnostic model client, Pydantic | S2–S3 |
| 4 | Execute path: fetch and analytics agents run approved steps and emit structured output | Python agents, SQL | S3 |
| 5 | Verify path: hop verifier checks each step; failures surface at the hop that caused them | SQL checks, DuckDB | S3–S4 |
| 6 | Lineage path: hop records, readable hop view, single-hop re-run and diff | PostgreSQL, FastAPI, React | S4 |
| 7 | Export and audit: self-contained investigation artifact and append-only audit log | JSONL, templating | S4–S5 |
| 8 | Grounding quality: ambiguity interception, binding store, doubt surfacing | BM25, embeddings, reciprocal rank fusion | S5 |
| 9 | Measure and report: execution accuracy, silent-error rate, verifier coverage, cost per investigation by retry count | Harness, seeded-error set | S5–S6 |

**Parallel non-code track.** The verification-cost study runs alongside Sprint 1 rather than after the build. It needs five analysts and one hour each, no software, and it gates the entire architecture: if verifying an answer costs as much as deriving it, a more accurate planner does not help. Discovering that in month four would invalidate the build rather than merely delay it.

**Pre-decided cut list.** Declared now so that a cut made under time pressure is a scope decision rather than a failure: (1) Visualization agent — a table is an acceptable answer; (2) REST connector — Postgres plus CSV already demonstrates heterogeneity; (3) ML agent — the widest capability gap but explicitly not the differentiator; (4) hop override re-flow, degraded to invalidate-and-replan, which is the honest fallback anyway. The harness, seeded-error set, lineage capture, hop verification, export and ambiguity interception are not cuttable at any point.

## Progress Log

Table 13. Implementation progress

| Date | Item | Status |
|---|---|---|
| Sep 14, 2026 | Project repository created with README, concept and roadmap | Done |
| Sep 2026 | Project concept and abstract agreed with the advisor | Done |
| Sep 2026 | Python 3.12 environment and dependencies installed and verified by all four members | Done |
| Sep–Oct 2026 | Literature search, state of the art, requirements and architecture (this workbook) | Done |
| Sep 28 – Oct 11, 2026 | Sprint 1: repository, CI, Docker Compose, harness skeleton, question set, spikes SP-1 to SP-3 | In progress |
| Oct 12 – Oct 25, 2026 | Sprint 2: plan synthesis, CSV ingestion, ground truth and seeded errors, spike SP-4 | Planned |


<<<PAGEBREAK>>>

# Chapter 9. Project Schedule

The project runs on **two-week sprints** from the day the repository was created, 14 September 2026, through the end of CMPE 295B, tracked on a GitHub Projects board. Each sprint ends with a demo to the team and an update to the progress log in Chapter 8. **Every member owns one stream of work in every sprint, so tasks do not overlap**; integration is done jointly in the last two days of each sprint. Class assignments are deliberately excluded from this schedule, which covers project work only.

## Milestones

Table 14. Milestones and exit criteria

| Milestone | Date | Exit criteria |
|---|---|---|
| M1 Requirements and architecture baseline | Oct 8, 2026 | Literature search, requirements, architecture and schedule complete and reviewed with the advisor; Workbook 1 submitted |
| M2 Measurement baseline | Nov 8, 2026 | Harness, fixed question set and seeded-error set run in CI on every merge; first multi-hop accuracy figure recorded |
| M3 Narrow path end to end | Dec 6, 2026 | One question spanning Postgres and an uploaded CSV is planned, approved, executed, verified per hop and exported as a self-contained artifact |
| M4 Evidence for the central claim | Dec 11, 2026 | Verification-cost study run with five analysts; silent-error rate and verifier coverage reported, including a negative result |
| M5 Beta | Mar 7, 2027 | Replanning, hop override, REST connector, dbt consumption, sign-off and export working on the staging environment |
| M6 Final release | May 7, 2027 | Hardened system, published accuracy and coverage figures, paper draft, demo video and Expo prototype |

Figure 2. Project schedule by sprint and team member

<<<FIGURE:assets/ch9_schedule.png>>>

## Sprint plan and task assignment

Table 15. Task assignment per sprint (AK = Atharva Kulkarni, AN = Akshay Navani, PS = Pranjal Shrivastava, SZ = Shantanu Zadbuke)

| Sprint (dates) | Atharva Kulkarni | Akshay Navani | Pranjal Shrivastava | Shantanu Zadbuke |
|---|---|---|---|---|
| S0 (Sep 14 – Sep 27) | Agent and planning literature; requirements | Text-to-SQL literature; architecture | Reliability and evaluation literature; dependencies | State of the art; justification; screen sketches |
| S1 (Sep 28 – Oct 11) | Typed plan schema; model client spike (SP-3) | Repository, CI, Docker Compose; Postgres connector (SP-1); DuckDB path (SP-2) | Harness skeleton; fixed question set drafted | Investigation workspace skeleton; wireframes |
| S2 (Oct 12 – Oct 25) | Plan synthesiser v1 with static validation | CSV and Excel ingestion; application store schema | Ground-truth answers; seeded-error set; hop-check spike (SP-4) | Plan review and approval screen |
| S3 (Oct 26 – Nov 8) | Semantic resolver: hybrid retrieval and margin threshold | Connector profiling; binding store persistence | Hop verifier checks; first verifier-coverage run | Lineage inspector hop view; replay spike (SP-5) |
| S4 (Nov 9 – Nov 22) | Orchestrator dispatch; budgets and retry caps | Cross-source reconciler profiling | Harness in CI; first published accuracy figure (SP-6) | Export artifact; append-only audit log |
| S5 (Nov 23 – Dec 6) | Ambiguity interception; doubt surfacing | Quickstart: clone to first investigation under 30 minutes | Silent-error measurement; verifier coverage reported | Sign-off state; unreviewed-answer marking |
| Dec 7 – Dec 11 | Verification-cost study, five analysts — joint | 295A report and demo — joint | Results write-up — joint | Demo preparation — joint |
| Winter break (Dec 12 – Jan 24) | Design notes for Workbook 2 (optional) | Deployment notes (optional) | Seeded-error expansion (optional) | Screen mockups v2 (optional) |
| S6 (Jan 25 – Feb 7, 2027) | Replanning on invalidation | REST JSON connector | Verifier coverage expansion | Review queue; searchable history |
| S7 (Feb 8 – Feb 21) | Hop override with downstream re-flow | dbt semantic-layer consumption | Cost per investigation by retry count | Shared investigation link |
| S8 (Feb 22 – Mar 7) | Plan caching and pinned bindings | Permission inheritance; schema-only mode | Evaluation of the modelling step | Visualization agent surface |
| S9 (Mar 8 – Mar 21) | Time-boxed ML agent | Performance and cost benchmarks | Robustness tests on plans and prompts | Model card screen |
| S10 (Mar 22 – Apr 4) | Accuracy ablations | Load and scale tests | Usability study with analysts | Accessibility and interface polish |
| S11 (Apr 5 – Apr 18) | Paper: method and results | Paper: systems and cost | Paper: evaluation and coverage | Paper: figures and user study |
| S12 (Apr 19 – May 2) | Final hardening | Release packaging and runbooks | Final measurement run | Demo video and Expo booth |

**How the schedule is kept honest.** Each sprint closes with the progress log in Chapter 8 updated from what actually merged, not from what was planned. The pre-decided cut list in §8.4 names what is dropped first if a sprint runs short, so a cut is a scope decision rather than a failure discovered in the final week.
