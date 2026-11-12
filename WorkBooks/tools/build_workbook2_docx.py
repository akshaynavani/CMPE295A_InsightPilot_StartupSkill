"""Build "Workbook 2 - Group Submission Draft.docx" from the submitted Workbook 1 docx.

Writes Chapters 6 and 7 into their placeholders, edits Chapters 8 and 9 in place with every change in bold,
adds the Workbook 2 note to the front matter and Chapter 5, fixes heading spacing, and embeds the figures
from WorkBooks/assets (SVG with PNG fallback; diagrams on landscape pages, text on portrait pages).

Usage (from WorkBooks/):
    rm -rf /tmp/wb2 && mkdir /tmp/wb2 && unzip -q "Workbook 1 - Group Submission.docx" -d /tmp/wb2
    python3 tools/build_workbook2_docx.py /tmp/wb2 assets
    (cd /tmp/wb2 && zip -qXrD "../Workbook 2 - Group Submission Draft.docx" .)   # then move it next to Workbook 1
Regenerate the figures first with the tools/build_*.py scripts and tools/ui_mockup/render.sh.
"""
import shutil, struct, sys
from pathlib import Path
from xml.sax.saxutils import escape

UN = Path(sys.argv[1])            # unpacked docx
ASSETS = Path(sys.argv[2])        # WorkBooks/assets
DOC = UN / 'word' / 'document.xml'
RELS = UN / 'word' / '_rels' / 'document.xml.rels'

PLACEHOLDER_START = 'To be completed in Workbook Assignment 2 (UML class and sequence diagrams'


def t(s):
    return f'<w:t xml:space="preserve">{escape(s)}</w:t>'


def run(s, bold=False):
    return f'<w:r><w:rPr>{"<w:b/>" if bold else ""}</w:rPr>{t(s)}</w:r>'


def h2(s):
    return f'<w:p><w:pPr><w:pStyle w:val="Heading2"/></w:pPr>{run(s)}</w:p>'


def para(text, lead=None):
    body = (run(lead, True) + run(' ' + text)) if lead else run(text)
    return f'<w:p><w:pPr><w:pStyle w:val="IndentedParagraph"/></w:pPr>{body}</w:p>'


def bullet(lead, text):
    return (f'<w:p><w:pPr><w:pStyle w:val="Bullet"/><w:numPr><w:ilvl w:val="0"/><w:numId w:val="14"/></w:numPr></w:pPr>'
            f'{run(lead, True)}{run(" " + text)}</w:p>')


def png_size(path):
    with open(path, 'rb') as f:
        head = f.read(24)
    return struct.unpack('>II', head[16:24])


FIG_ID = [2]   # existing drawings use docPr ids 1 and 2


EMU_IN = 914400
SVG_EXT = ('<a:extLst><a:ext uri="{96DAC541-7B7A-43D3-8B79-37D633B846F1}">'
           '<asvg:svgBlip xmlns:asvg="http://schemas.microsoft.com/office/drawing/2016/SVG/main" r:embed="%s"/>'
           '</a:ext></a:extLst>')


def figure(caption, png, rid, landscape=False, new_page=False):
    """Portrait figures are 6 in wide, as in Chapter 5. Landscape figures use up to the
    8.5 in text width, capped so caption and image fit on one landscape page."""
    w, h = png_size(ASSETS / png)
    width_in = min(8.5, 5.2 * w / h) if landscape else 6.0
    cx = int(width_in * EMU_IN)
    cy = int(cx * h / w)
    FIG_ID[0] += 1
    n = FIG_ID[0]
    brk = '<w:pageBreakBefore/>' if new_page else ''
    cap = f'<w:p><w:pPr><w:pStyle w:val="FigureCaption"/><w:keepNext/>{brk}</w:pPr>{run(caption)}</w:p>'
    img = ('<w:p><w:pPr><w:jc w:val="center"/><w:spacing w:after="200" w:line="259" w:lineRule="auto"/></w:pPr>'
           f'<w:r><w:drawing><wp:inline distT="0" distB="0" distL="0" distR="0"><wp:extent cx="{cx}" cy="{cy}"/>'
           f'<wp:docPr id="{n}" name="Figure {n}"/><a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">'
           '<a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">'
           '<pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">'
           f'<pic:nvPicPr><pic:cNvPr id="{n}" name="Figure {n}"/><pic:cNvPicPr/></pic:nvPicPr>'
           f'<pic:blipFill><a:blip r:embed="{rid}">{SVG_EXT % SVG_RID[rid] if (ASSETS / png.replace(".png", ".svg")).exists() else ""}</a:blip><a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
           f'<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr>'
           '</pic:pic></a:graphicData></a:graphic></wp:inline></w:drawing></w:r></w:p>')
    return cap + img


def cell(text, width, header=False):
    shd = '<w:shd w:val="clear" w:color="auto" w:fill="EDEDED"/>' if header else ''
    b = '<w:b/>' if header else ''
    return (f'<w:tc><w:tcPr><w:tcW w:w="{width}" w:type="dxa"/>{shd}<w:vAlign w:val="top"/></w:tcPr>'
            '<w:p><w:pPr><w:spacing w:after="40" w:line="259" w:lineRule="auto"/></w:pPr>'
            f'<w:r><w:rPr><w:sz w:val="18"/><w:szCs w:val="18"/>{b}</w:rPr>{t(text)}</w:r></w:p></w:tc>')


def table(caption, widths, header, rows):
    assert sum(widths) == 8640
    cap = f'<w:p><w:pPr><w:pStyle w:val="tablecaption"/><w:keepNext/></w:pPr>{run(caption)}</w:p>'
    border = ''.join(f'<w:{s} w:val="single" w:sz="4" w:space="0" w:color="808080"/>'
                     for s in ['top', 'left', 'bottom', 'right', 'insideH', 'insideV'])
    tbl = ('<w:tbl><w:tblPr><w:tblW w:w="8640" w:type="dxa"/>'
           f'<w:tblBorders>{border}</w:tblBorders><w:tblLayout w:type="fixed"/>'
           '<w:tblCellMar><w:top w:w="60" w:type="dxa"/><w:left w:w="90" w:type="dxa"/>'
           '<w:bottom w:w="60" w:type="dxa"/><w:right w:w="90" w:type="dxa"/></w:tblCellMar></w:tblPr>'
           '<w:tblGrid>' + ''.join(f'<w:gridCol w:w="{w}"/>' for w in widths) + '</w:tblGrid>')
    tbl += ('<w:tr><w:trPr><w:tblHeader/><w:cantSplit/></w:trPr>'
            + ''.join(cell(h, w, True) for h, w in zip(header, widths)) + '</w:tr>')
    for r in rows:
        tbl += '<w:tr><w:trPr><w:cantSplit/></w:trPr>' + ''.join(cell(c, w) for c, w in zip(r, widths)) + '</w:tr>'
    tbl += '</w:tbl>'
    # A paragraph after the table keeps the following caption from touching the table.
    return cap + tbl + '<w:p><w:pPr><w:pStyle w:val="IndentedParagraph"/><w:spacing w:after="0"/></w:pPr></w:p>'


FIGS = [  # (png, rId)
    ('ch6_status.png', 'rId903'),
    ('ch6_class_domain.png', 'rId904'),
    ('ch6_class_services.png', 'rId905'),
    ('ch6_class_answer.png', 'rId906'),
    ('ch6_sequence.png', 'rId907'),
    ('ch6_er.png', 'rId908'),
    ('ch7_pipeline.png', 'rId909'),
    ('ch9_pert_295a.png', 'rId910'),
    ('ch9_pert_295b.png', 'rId911'),
    ('ch6_ui_mockup.png', 'rId912'),
]
RID = dict(FIGS)
SVG_RID = {rid: 'rId9%02d' % (13 + i) for i, (_, rid) in enumerate(FIGS)}   # rId913..rId918

COMPONENTS = [
    ('Investigation Workspace', 'Ask questions; follow-ups inherit context; show live hop panels and the answer', 'UX spec §1, §6', 'SZ', 'Done'),
    ('Plan Review & Approval', 'Clarify ambiguous terms; edit and approve the plan before anything runs', 'UX spec §2, §4; D10', 'SZ', 'Done'),
    ('Lineage Inspector & Export', 'Inspect and replay hops; analyst sign-off; export one self-contained file', 'UX spec §7, §9', 'SZ', 'Designed'),
    ('Semantic Resolver', 'Bind business terms to columns and grain; halt and ask when ambiguous', 'Deep dive 1', 'AK', 'Designed'),
    ('Plan Synthesiser', 'Generate the typed plan DAG; validate sources, inputs and cycles', 'Deep dive 2', 'AK', 'Done'),
    ('Orchestrator & Replanner', 'Dispatch every step; hold state, budget and retry caps; compose the answer; replan [295B]', 'D02, D03', 'AK', 'Done'),
    ('Model Client', 'Single route to the language model: model routing, data-egress mode, cost tracking', 'D05, D06', 'AK', 'Designed'),
    ('Fetch / Integration Agent', 'Write and repair SQL against sources; return a step result', 'Deep dive 3', 'AN', 'Designed'),
    ('Analytics Agent', 'Joins, aggregations, KPIs and comparisons over earlier step outputs', 'D03', 'PS', 'Designed'),
    ('Visualization Agent [295B]', 'Choose a chart; return a chart specification and its rationale', 'D03', 'SZ', 'Planned (295B)'),
    ('ML Agent [295B]', 'Time-boxed baseline models with a model card and uncertainty', 'Deep dive 7', 'AK (build), PS (evaluation)', 'Planned (295B)'),
    ('Hop Verifier', 'Row-count, grain, coverage, null, total and range checks per hop, in SQL', 'Deep dive 4', 'PS', 'Designed'),
    ('Cross-source Reconciler', 'Profile join keys and overlap; propose mappings for analyst approval', 'Deep dive 5', 'PS (lead), AN (profiling)', 'Partial: profiling done; proposals S4'),
    ('Lineage Recorder & Replayer', 'Record each hop; replay one hop against current data and report differences', 'Deep dive 6; D04', 'SZ', 'Designed'),
    ('PostgreSQL Connector', 'Describe, sample, execute and profile, read-only, with the source’s own permissions', 'D07', 'AN', 'Done'),
    ('CSV / Excel Connector', 'Query uploaded files through DuckDB; infer and profile their schema', 'D07', 'AN', 'Done'),
    ('REST JSON Connector [295B]', 'Third source type; read-only API access', 'D07', 'AN', 'Planned (295B)'),
    ('Semantic Layer [295B]', 'dbt definitions that take precedence over inferred bindings', 'D07', 'AN', 'Planned (295B)'),
    ('Application Store', 'Bindings, plans, investigations, hops, overrides and sign-off (PostgreSQL 16)', 'D04', 'AN', 'Designed'),
    ('Artifact Store', 'Full step outputs and exports, addressed by hash', 'Chapter 5', 'AN', 'Designed'),
    ('Append-only Audit Log', 'Every statement issued to every source; readable without the application', 'D06; UX spec §12', 'SZ', 'Designed'),
    ('Offline Evaluation Harness', 'Fixed question set and seeded errors; accuracy and verifier coverage', 'D08', 'PS', 'Designed'),
]


def chapter6():
    x = []
    x.append(para('This chapter documents the design of InsightPilot for both semesters: the design methodology, '
                  'the status of each architecture component as of November 12, 2026, three UML class diagrams '
                  '(the domain model, the services and the answer presentation), a UML sequence diagram of one '
                  'question, and the database design. The class, sequence and database diagrams describe the '
                  'complete design whether or not a part has been built; build status is shown only in Figure 2 '
                  'and Table 9.'))

    x.append(h2('Design Methodology'))
    x.append(para('The design follows three working rules. First, the plan is data: the plan synthesiser produces '
                  'a typed directed acyclic graph of steps, which can be validated, shown, edited, approved and '
                  'cached before any query runs. Second, interfaces come before implementations: the source '
                  'connector interface (describe, sample, execute, profile), the step result every agent returns '
                  'and the hop record are fixed first, so each member builds against a contract while other '
                  'components are still in progress. Third, each feature is delivered as a thin vertical slice, '
                  'from the investigation workspace through the orchestrator and agents to the database, and '
                  'deepened in later sprints. Five principles guide every component:'))
    x.append(bullet('Generation and verification are separate.',
                    'Components that produce an answer may call a language model; components that check one may '
                    'not. The hop verifier and the cross-source reconciler issue independent SQL, so a check cannot '
                    'share the failure mode of the output it checks.'))
    x.append(bullet('Every handoff goes through the orchestrator.',
                    'Agents never call each other. Each step goes out as a task and returns as a step result, which '
                    'makes every hop observable, budgeted and recorded.'))
    x.append(bullet('Agents think and act inside one approved step.',
                    'Each specialist agent is a language-model tool-use loop: it reasons through the model client, '
                    'acts through the source connector, observes the result and repairs its query, read-only and '
                    'within a retry cap.'))
    x.append(bullet('There is one route to the model.',
                    'The model client is the only component that calls a language model. It routes plans and SQL to '
                    'a frontier model and answer prose to a small model, enforces schema-only or filtered-sample '
                    'mode, and counts cost against the investigation’s budget.'))
    x.append(bullet('Humans gate the irreversible points.',
                    'Ambiguous terms are clarified and the plan is approved before any query runs, and an analyst '
                    'signs off before an answer is exported.'))

    x.append(h2('As-Built Component Design'))
    x.append(figure('As-built status of each architecture component (November 12, 2026)', *FIGS[0]))
    x.append(para('Figure 2 marks each component of Figure 1 with its status. Six of the eighteen CMPE 295A '
                  'components are done: the investigation workspace, plan review and approval, the plan '
                  'synthesiser, the orchestrator, and the PostgreSQL and CSV/Excel connectors. The cross-source '
                  'reconciler is partial: key profiling is done and the transform search and mapping proposals '
                  'are built in Sprint 4. The other eleven are designed, each with a specification in the project’s design '
                  'documents, and the four CMPE 295B components are planned. Table 9 lists every component with '
                  'its responsibility, the specification it is built from and its owner; specifications refer to '
                  'the deep dives, the architecture diagrams D01–D10 and the UX specification in the project '
                  'repository.'))
    x.append(table('Component design: responsibility, specification, owner and status',
                   [1700, 3060, 1440, 1100, 1340],
                   ['Component', 'Responsibility', 'Specification', 'Owner', 'Status'],
                   COMPONENTS))

    # Text stays on portrait pages; each diagram gets its own landscape page right after its text.
    x.append(h2('Domain Model (UML Class Diagram)'))
    x.append(para('Figure 3 shows what the system stores. An organisation owns its sources, its bindings and its '
                  'investigations; there is one organisation per deployment. An investigation holds the analyst’s '
                  'questions; each question is planned as a plan of steps and answered by an answer made of blocks. '
                  'The model card is CMPE 295B scope. Four classes carry the design:'))
    x.append(bullet('Binding.', 'What a business term means in the data, with its provenance (semantic layer, '
                    'analyst-confirmed, inferred or stakeholder-unconfirmed) and schema version, so a confirmed '
                    'meaning is reused rather than guessed again. An approved mapping proposal from the reconciler '
                    'becomes a join binding.'))
    x.append(bullet('Plan and PlanStep.', 'The typed directed acyclic graph the analyst approves; each step names '
                    'its type, source, bindings and declared grain, and lists the steps it depends on.'))
    x.append(bullet('Hop.', 'The record of one executed step: the exact statement, row counts, declared and actual '
                    'grain, retry attempts and a reference to its full output. It can be replayed against current data '
                    'and may carry an analyst’s override.'))
    x.append(bullet('HopVerdict and CheckResult.', 'Each verification attempt on a hop is a HopVerdict (PASS, WARN, '
                    'FAIL or ERROR) holding one CheckResult per check with its status (PASS, WARN, FAIL, SKIP or '
                    'ERROR), expected and observed values, tolerance and exact SQL. A re-run adds a new verdict '
                    'instead of overwriting the old one, so differences stay visible.'))
    x.append(bullet('Answer and AnswerBlock.', 'The reply to a question, made of ordered blocks that cite the hops '
                    'they came from, and signed off by an analyst before export.'))
    x.append(SECTION_BREAK_PORTRAIT_FIRST)    # ends the portrait section that starts at Chapter 1
    x.append(figure('UML class diagram of the core domain model', *FIGS[1], landscape=True))
    x.append(SECTION_BREAK_LANDSCAPE)

    x.append(h2('Services (UML Class Diagram)'))
    x.append(para('Figure 4 shows which component does the work and which objects of Figure 3 it creates. The '
                  'orchestrator is the hub: every step goes out through it and every result comes back to it, and '
                  'agents never call each other. Grey boxes in the figure are domain classes from Figure 3.'))
    x.append(bullet('Orchestrator.', 'Invokes the semantic resolver and the plan synthesiser, waits for plan '
                    'approval, dispatches each step to a specialist agent, receives the step result, passes it to '
                    'the hop verifier and the lineage recorder, and finally composes the answer.'))
    x.append(bullet('SemanticResolver and PlanSynthesiser.', 'Create bindings and the plan. A dbt semantic '
                    'supplier (CMPE 295B) provides definitions that take precedence over inferred ones.'))
    x.append(bullet('SpecialistAgent.', 'Fetch and analytics agents (visualization and ML in CMPE 295B). Each '
                    'reasons through the model client, acts through the source connector, repairs a failed query, '
                    'and returns a step result.'))
    x.append(bullet('ModelClient.', 'The only component that calls a language model: plans and SQL go to a '
                    'frontier model, answer prose to a small model, under schema-only or filtered-sample mode.'))
    x.append(bullet('SourceConnector.', 'One read-only interface (describe, sample, execute, profile) implemented '
                    'for PostgreSQL and CSV/Excel, with REST JSON in CMPE 295B; it writes every statement to the '
                    'audit log.'))
    x.append(bullet('HopVerifier, CrossSourceReconciler and LineageRecorder.', 'Produce hop verdicts with '
                    'their check results, mapping proposals and hops. The first two issue independent SQL built '
                    'from the approved plan step, not from the agent’s SQL, and never call a model.'))
    x.append(SECTION_BREAK_PORTRAIT)
    x.append(figure('UML class diagram of the services', *FIGS[2], landscape=True))
    x.append(SECTION_BREAK_LANDSCAPE)

    x.append(h2('Answer Presentation (UML Class Diagram)'))
    x.append(para('Figure 5 expands the answer the analyst sees in the investigation workspace. An answer is an '
                  'ordered list of blocks, each a subclass of AnswerBlock, and every claim carries a citation to '
                  'the hop that produced it, so opening a footnote shows that hop’s statement, row counts and '
                  'checks.'))
    x.append(bullet('TextBlock.', 'The summary and key insights, written by the small model using only numbers '
                    'from verified hops.'))
    x.append(bullet('TableBlock.', 'The actual rows of a hop’s output, read from the artifact store; no model '
                    'rewrites them.'))
    x.append(bullet('DoubtBlock.', 'A WARN or FAIL check from the hop verifier, naming the hop, the check and the '
                    'reason, so the least certain step is visible in the answer itself.'))
    x.append(bullet('ChartBlock and ChartSpec.', 'A chart with its type, axes, colour grouping and rationale, '
                    'produced by the visualization agent; CMPE 295B scope.'))
    x.append(SECTION_BREAK_PORTRAIT)
    x.append(figure('UML class diagram of the answer presentation', *FIGS[3], landscape=True))
    x.append(SECTION_BREAK_LANDSCAPE)

    x.append(h2('Key Interaction (UML Sequence)'))
    x.append(para('Figure 6 follows one question. The orchestrator resolves the question’s terms, has the plan '
                  'synthesised and shows it for approval (steps 1–8). For each step in DAG order it dispatches the '
                  'step to an agent, which writes SQL through the model client and executes it read-only; the step '
                  'result returns to the orchestrator, which has it verified and recorded as a hop (steps 9–15). '
                  'When every hop has passed, the orchestrator has the small model write the insight text from '
                  'verified facts and returns the answer for sign-off (steps 16–18). Four paths are omitted from '
                  'the figure for readability:'))
    x.append(bullet('Clarification.', 'If two candidate meanings of a term score within the margin, the resolver '
                    'halts and the analyst chooses; the choice is saved as a binding and never asked again.'))
    x.append(bullet('SQL repair.', 'If a query fails, the agent returns the database error to the model and '
                    'retries, up to the orchestrator’s retry cap.'))
    x.append(bullet('Cross-source reconciliation.', 'When a step joins two sources, the reconciler profiles both '
                    'keys and proposes a mapping with its coverage; the analyst approves it before use.'))
    x.append(bullet('Halt on red.', 'If any check fails, the remaining steps are skipped and the analyst sees the '
                    'partial result and the failing hop.'))
    x.append(SECTION_BREAK_PORTRAIT)
    x.append(figure('UML sequence diagram of answering one question (main path)', *FIGS[4], landscape=True))
    x.append(SECTION_BREAK_LANDSCAPE)

    x.append(h2('Database Design'))
    x.append(para('Figure 7 shows the Application Store. All durable state lives in one PostgreSQL 16 database per deployment: twenty-one tables, one of '
                  'them (model_cards) CMPE 295B scope, including three tables written by the evaluation harness. Uniqueness constraints enforce correctness in the database '
                  'itself: one question number per investigation, one step key per plan, one block position per '
                  'answer and one verdict per hop attempt; verdicts are never updated, so a re-run inserts a new '
                  'attempt. Full result sets are not stored: a hop keeps its row '
                  'counts, grain and a sample, and the full output is a file in the artifact store addressed by '
                  'the hop’s output reference, because a re-run against current data is the point of replay. The '
                  'audit log is an append-only JSONL file, readable without the application, and credentials never '
                  'enter any table.'))
    x.append(SECTION_BREAK_PORTRAIT)
    x.append(figure('Entity-relationship diagram of the Application Store (PostgreSQL 16)', *FIGS[5], landscape=True))
    x.append(SECTION_BREAK_LANDSCAPE)

    x.append(h2('UI Design'))
    x.append(para('Figure 8 shows the investigation workspace, the screen in which an analyst works (mockup by Pranjal '
                  'Shrivastava, sample data). Its layout follows the conversational pattern analysts already know '
                  'from tools such as Databricks Genie: a context rail on the left and the conversation on the right. '
                  'Each element maps to a class of Figures 3 to 5:'))
    x.append(bullet('Context rail.', 'Investigations with their review state (signed off or awaiting review), the '
                    'connected sources (the read-only warehouse and an uploaded file), the bindings in scope with their '
                    'provenance, and links to the review queue, the audit log and the settings (schema-only mode and the '
                    'budget cap). Classes: Investigation, Source, Binding, SignOff, AuditEvent.'))
    x.append(bullet('Question, clarification and plan.', 'The question, the term the analyst clarified and saved as a '
                    'binding, and the approved plan with its steps, collapsed after approval. Classes: Question, '
                    'PlanApproval, Plan, PlanStep.'))
    x.append(bullet('Executed steps.', 'One collapsible row per hop with its verdict, sources, rows in and out, grain '
                    'and SQL attempts; an expanded step shows the generated SQL, a result preview and each check with '
                    'its expected and observed values, plus replay. Classes: Hop, HopVerdict, CheckResult.'))
    x.append(bullet('Answer.', 'An amber banner until an analyst signs off; the summary and key insights with a '
                    'citation to the step behind each number; the result table; the chart (CMPE 295B); the least '
                    'certain step; actions to inspect lineage, correct a step or export (enabled only after sign-off); '
                    'feedback; and suggested follow-ups. Classes: Answer, TextBlock, Citation, TableBlock, ChartBlock, '
                    'DoubtBlock, SignOff, Override.'))
    x.append(para('Four elements set the screen apart from a generic chat-with-data interface and carry the project’s '
                  'argument: the plan is approved before anything runs, every step shows its verification, every '
                  'claim cites the step it came from, and export waits for an analyst’s sign-off.'))
    x.append(SECTION_BREAK_PORTRAIT)
    x.append(figure('UI mockup of the investigation workspace (sample data)', *FIGS[9], landscape=True))
    x.append(SECTION_BREAK_LANDSCAPE)
    return ''.join(x)


PLACEHOLDER7_START = 'To be completed in Workbook Assignment 2 (test strategy'

TEST_LEVELS = [
    ('Static analysis', 'Lint, formatting and strict typing for Python and TypeScript', 'ruff, mypy --strict, tsc, eslint', 'lint', 'NFR-14', 'All'),
    ('Unit and contract', 'Plan schema and static validation, binding resolution and reuse, follow-up context, plan cache key; contracts for the step result, the hop record and the connector interface', 'pytest', 'unit', 'FR-05, FR-07, FR-08, FR-17, FR-23*, NFR-14', 'AK, AN'),
    ('Integration', 'Connectors against real PostgreSQL 16 and DuckDB in Docker: read-only enforcement, inherited permissions, file schema inference, audit log', 'pytest, Docker Compose', 'integration', 'FR-03, FR-04, FR-16, FR-20*, FR-21*, NFR-01, NFR-03, NFR-05', 'AN'),
    ('Agent end-to-end', 'Question to answer through the orchestrator, agents, verifier and recorder with recorded model responses; replay, override and replanning', 'pytest, recorded model fixtures', 'agent-e2e', 'FR-09, FR-10, FR-11, FR-13, FR-15, FR-18*, FR-19*, FR-24*, FR-25*, NFR-06, NFR-07', 'AK, PS'),
    ('Evaluation harness', 'Fixed question set and seeded-error set through the full pipeline: accuracy, silent errors, verifier coverage, pass^k, attempts and cost', 'pytest, Docker Compose', 'harness', 'FR-01, FR-02, NFR-08, NFR-12', 'PS'),
    ('UI end-to-end', 'Ask, clarify, approve, inspect a hop, export and sign off in the browser; accessibility checks', 'Playwright, axe-core', 'web', 'FR-06, FR-12, FR-14, FR-22*, FR-26*', 'SZ'),
    ('Security and privacy', 'Secret, dependency and image scans; write-attempt probes on every agent path; sensitive columns kept out of model context; no write or alert tools exposed', 'gitleaks, dependency and image scanners', 'security', 'NFR-02, NFR-04, NFR-15', 'AN, SZ'),
    ('Performance and cost', 'Plan latency on the reference schema; tokens, attempts and cost per investigation', 'harness timers, model-client usage records', 'harness (nightly)', 'NFR-11, NFR-12', 'AK'),
    ('Deployment', 'Clean-checkout quickstart, timed on a fresh machine', 'Docker Compose', 'release', 'FR-27*, NFR-13', 'AN'),
    ('Human evaluation', 'Verification-cost study and seeded-defect review with analysts; usability walkthrough', 'moderated, timed sessions', 'none (Dec 7–11)', 'NFR-09, NFR-10', 'PS, SZ'),
]

RESEARCH_QUESTIONS = [
    ('RQ1. How often are multi-hop questions answered correctly?', 'Execution accuracy on the fixed question set', 'B2: single-shot text-to-SQL on the same questions; DABstep Hard 14.55% for context only [6]', 'Measured and published (NFR-08)', 'Harness S1–S4; first figure Nov 22 (SP-6)'),
    ('RQ2. Do per-hop checks catch plausible wrong answers?', 'Silent-error rate; verifier coverage per defect type', 'B1: the same pipeline with the hop verifier off', 'Coverage reported per defect type (FR-02)', 'Protocol ready; measured S5'),
    ('RQ3. Are answers stable across repeated runs?', 'pass^k for k = 1–5 from five live trials [8]', 'B3: pass@1 of the same system', 'Reported alongside accuracy', 'Measured S5'),
    ('RQ4. Is checking an answer cheaper than deriving it?', 'Verification cost ratio', 'B4: the analyst derives the answer unaided', 'Median below 0.5; above 0.8 is a stop trigger (NFR-10)', 'Study Dec 7–11'),
    ('RQ5. Does the trace help analysts reject wrong answers?', 'Share of seeded defects rejected', 'B5: the same answers without the trace', 'At least 70% and twice the control (NFR-09)', 'Study Dec 7–11'),
    ('RQ6. What does an investigation cost, and how fast is the plan?', 'Cost by retry count; time to present the plan', 'Cost model: about $1.10 per six-hop investigation at one attempt', 'Cost reported (NFR-12); plan within 15 s (NFR-11)', 'Measured S4–S5'),
]

B1_PROTOCOL = [
    ('Question', 'Does the hop verifier catch plausible wrong answers that would otherwise reach the analyst?'),
    ('Data', 'The seeded-error set: each investigation in the fixed set with one planted defect from eight classes: D1 wrong join key, D2 fan-out join, D3 wrong grain, D4 off-by-one period boundary, D5 wrong code mapping, D6 dropped filter, D7 null handling and D8 wrong measure. Each is labelled with its class and the hop where it was planted.'),
    ('Treatment', 'The full pipeline with the hop verifier and the cross-source reconciler on.'),
    ('Baseline B1', 'The same pipeline, model and approved plans with the verifier switched off; every hop is recorded as unchecked.'),
    ('Metrics', 'Silent-error rate: defects that reach the answer with no WARN or FAIL on any hop. Verifier coverage: defects flagged by at least one check, reported per defect type and per check.'),
    ('Analysis', 'Paired caught and escaped outcomes per defect compared with McNemar’s test; rates reported with 95% bootstrap confidence intervals.'),
    ('Decision rule', 'A defect class with low coverage gets a new check in CMPE 295B or is listed in the answer’s doubt block as not checked. D8 can pass every structural check and is expected to escape often; it is reported separately rather than hidden. Results are published even if negative.'),
]

TARGETS = [
    ('Plan presented after the question', 'Within 15 s for a six-hop plan (NFR-11)', 'Harness timer from question to plan shown on the reference schema; p50 and p95 over the question set', 'Planned (S4)'),
    ('Statements in the audit log', '100% (NFR-05)', 'Compare every statement the connector logged with the database’s own statement log for a harness run', 'Planned (S4)'),
    ('Write attempts from any agent path', 'None succeed (NFR-01)', 'Probe every agent path with DDL and DML; each must be rejected by the connector and by the database role', 'Planned (S4)'),
    ('Model calls during verification', 'Zero (NFR-06)', 'Count model-client calls attributed to the hop verifier and the reconciler during a harness run', 'Planned (S4)'),
    ('Replay of a recorded hop', 'Same result, or the difference reported (NFR-07)', 'Replay every hop of a harness run and compare output hashes', 'Planned (S4)'),
    ('Execution accuracy', 'Measured and published (NFR-08)', 'Harness over the fixed question set: replay on every pull request, five live trials nightly', 'Planned (S4, SP-6)'),
    ('Verification time per hop', 'Median 1.5 s or less, p95 5 s or less (refines NFR-11)', 'Verifier timing per check kind over the question set in replay mode', 'Planned (S4)'),
    ('Seeded defects rejected by analysts', 'At least 70% and twice the control (NFR-09)', 'Moderated study, with and without the trace', 'Planned (Dec 7–11)'),
    ('Verification cost ratio', 'Median below 0.5; above 0.8 stops (NFR-10)', 'Timed study with five analysts', 'Planned (Dec 7–11)'),
    ('Cost per investigation', 'Reported by retry count (NFR-12)', 'Model-client token usage times provider price, grouped by attempts', 'Planned (S4–S5)'),
    ('Clone to first investigation', 'Median under 30 min (NFR-13)', 'Fresh-machine quickstart, timed, by a member who did not write it', 'Planned (S5)'),
    ('Back-end unit-test coverage', 'At least 70%; harness on every pull request (NFR-14)', 'Coverage report in CI', 'Planned (S4)'),
]


def chapter7():
    x = []
    x.append(h2('Quality Assurance Strategy'))
    x.append(para('Testing follows a test pyramid with automated gates on every pull request. The evaluation '
                  'harness, built before the agents, is itself a CI job, so accuracy is measured on every change '
                  'rather than once. Table 10 lists each test level with its scope, tools, CI job and owner, and '
                  'the Chapter 3 requirements it verifies; together the rows cover every functional and '
                  'non-functional requirement. Requirements marked * are Desired or Optional and are tested in CMPE '
                  '295B when the feature is built. Figure 9 shows where each level runs.'))
    x.append(table('Test levels, tools and CI gates',
                   [1150, 2250, 1300, 950, 2090, 900],
                   ['Level', 'Scope', 'Tools', 'CI job', 'Requirements covered', 'Owner'],
                   TEST_LEVELS))
    x.append(SECTION_BREAK_PORTRAIT)
    x.append(figure('Evaluation and CI pipeline', *FIGS[6], landscape=True))
    x.append(SECTION_BREAK_LANDSCAPE)

    x.append(h2('Evaluation Methodology'))
    x.append(para('The evaluation answers six research questions. Each has a metric, an explicit baseline and an '
                  'acceptance threshold from the requirements in Chapter 3.'))
    x.append(table('Research questions, metrics and baselines',
                   [2100, 1800, 2040, 1500, 1200],
                   ['Research question', 'Metric', 'Baseline', 'Target (Chapter 3)', 'Status'],
                   RESEARCH_QUESTIONS))
    x.append(para('A dedicated harness starts its own Docker Compose project from empty volumes, loads the '
                  'synthetic reference schema (orders, shipments, customers and regions across roughly 40 tables) '
                  'into PostgreSQL 16 and the unmodelled CSV file into DuckDB, and runs every question of the fixed '
                  'set (30–50 questions with authored ground truth, covering single-source, cross-source and '
                  'ambiguous-term cases) through the full pipeline. On every pull request it runs in replay mode: '
                  'model responses are read from recorded files, so the run is deterministic and costs nothing, '
                  'and a missing recording fails loudly rather than calling the model. Nightly and before '
                  'milestones it runs live, five trials per question, under a spend cap. Execution accuracy '
                  'compares the answer table with the ground truth after matching columns and allowing a small '
                  'numeric tolerance. '
                  'No customer data is used.', lead='Setup.'))

    x.append(h2('Baseline B1: Verifier On Versus Verifier Off'))
    x.append(para('The project’s central claim is that independent per-hop checks catch plausible wrong answers '
                  'that a single-pass system would deliver. Baseline B1 tests that claim directly by running the '
                  'seeded-error set twice, with and without the hop verifier. Table 12 defines the protocol so '
                  'that a separate test team could run it.'))
    x.append(table('Baseline B1 protocol: verifier on versus verifier off',
                   [1800, 6840], ['Item', 'Protocol'], B1_PROTOCOL))
    x.append(para('No results exist yet: the harness and the seeded-error set are the first prototype '
                  'increments, and the first figures are due with SP-6 on November 22. The outcome decides which '
                  'checks are strengthened in CMPE 295B, and a negative result is reported rather than hidden.',
                  lead='Status and decision.'))

    x.append(h2('Requirement Targets'))
    x.append(para('Table 13 is the acceptance checklist for the measurable requirements. Each row names the '
                  'target from Chapter 3 and exactly how it is measured; the result column records the sprint in '
                  'which the measurement first runs and is replaced by the measured value when it does.'))
    x.append(table('Requirement targets and how each is measured',
                   [2000, 1900, 3240, 1500],
                   ['Metric', 'Target', 'How measured', 'Result'], TARGETS))

    x.append(h2('Evaluation Procedure'))
    x.append(bullet('Accuracy.', 'Every question runs once per replay run and five times per nightly live run; '
                    'execution accuracy is the share of answers that match the ground truth, reported per run '
                    'and on every pull request, and compared with the single-shot baseline B2 on the same '
                    'questions.'))
    x.append(bullet('Silent errors and coverage.', 'The seeded-error set runs with the verifier on and off '
                    '(Table 12); each defect is scored as caught or escaped, per defect type and per check.'))
    x.append(bullet('Consistency.', 'pass^k for k = 1–5, estimated from the five live trials, is the chance of answering '
                    'a question correctly in all k trials [8], '
                    'reported next to accuracy because a system that is right on average can still be '
                    'unreliable.'))
    x.append(bullet('Cost and latency.', 'Tokens and attempts come from the model client’s usage records and '
                    'plan latency from the harness timer; cost is reported grouped by retry count.'))
    x.append(bullet('Human studies.', 'Five analysts each derive one answer unaided and check another produced by '
                    'InsightPilot, in counterbalanced order, giving the verification cost ratio; in a second task '
                    'they accept or reject answers containing seeded defects, with and without the trace.'))
    x.append(bullet('Statistics.', 'Rates are reported with 95% bootstrap confidence intervals, paired pass and '
                    'fail outcomes are compared with McNemar’s test, and every result is published, including '
                    'negative ones.'))

    x.append(h2('Deployment Plan'))
    x.append(para('Four environments are used: local development (Docker Compose on each member’s machine), '
                  'continuous integration (GitHub Actions running every test level and the harness on each pull '
                  'request), the harness environment (an isolated Compose project started from empty volumes, '
                  'also run nightly) and the Expo demo (a single-tenant deployment of the tagged release with '
                  'seeded demo data). There is no shared multi-tenant service: each organisation runs its own '
                  'copy, so a release is a set of versioned, pinned images plus the Compose file and the '
                  'one-command quickstart (NFR-13). Database changes ship as forward-only, versioned migrations '
                  'applied after an automatic backup of the application store, and rollback redeploys the '
                  'previous image tags and restores that backup. Credentials are supplied as environment secrets '
                  'at deploy time and never enter the images, the database or the audit log (NFR-02).'))
    return ''.join(x)


# ---------------------------------------------------------------- Chapter 8 (changes in bold)
import re as _re


def brun(text, size=None):
    """Bold runs for Workbook 2 changes; [CONFIRM: ...] segments are also highlighted yellow."""
    out = []
    for part in _re.split(r'(\[CONFIRM[^\]]*\])', text):
        if not part:
            continue
        hl = '<w:highlight w:val="yellow"/>' if part.startswith('[CONFIRM') else ''
        sz = f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>' if size else ''
        out.append(f'<w:r><w:rPr><w:b/>{hl}{sz}</w:rPr>{t(part)}</w:r>')
    return ''.join(out)


def _table_after(region, caption):
    c = region.index('>' + caption)
    t0 = region.index('<w:tbl>', c)
    return t0, region.index('</w:tbl>', t0) + len('</w:tbl>')


def _cell_text(tc):
    return ''.join(_re.findall(r'<w:t[^>]*>([^<]*)', tc))


def edit_cells(region, caption, edits):
    """edits: {(row_first_cell_prefix, col): ('replace' | 'append', text)}"""
    t0, t1 = _table_after(region, caption)
    tbl = region[t0:t1]
    rows = _re.findall(r'<w:tr>.*?</w:tr>', tbl, _re.S)
    done = set()
    for row in rows:
        cells = _re.findall(r'<w:tc>.*?</w:tc>', row, _re.S)
        first = _cell_text(cells[0])
        new_row = row
        for (key, col), (mode, text) in edits.items():
            if first.startswith(key):
                tc = cells[col]
                p_end = tc.rindex('</w:p>')
                if mode == 'replace':
                    p_start = tc.index('</w:pPr>') + len('</w:pPr>')
                    new_tc = tc[:p_start] + brun(text, 18) + tc[p_end:]
                else:
                    new_tc = tc[:p_end] + brun(text, 18) + tc[p_end:]
                new_row = new_row.replace(tc, new_tc, 1)
                done.add((key, col))
        tbl = tbl.replace(row, new_row, 1)
    missing = set(edits) - done
    assert not missing, missing
    return region[:t0] + tbl + region[t1:]


def add_rows(region, caption, rows):
    t0, t1 = _table_after(region, caption)
    tbl = region[t0:t1]
    widths = [int(w) for w in _re.findall(r'<w:gridCol w:w="(\d+)"/>', tbl)]
    new = ''
    for r in rows:
        new += '<w:tr><w:trPr><w:cantSplit/></w:trPr>'
        for text, w in zip(r, widths):
            new += (f'<w:tc><w:tcPr><w:tcW w:w="{w}" w:type="dxa"/><w:vAlign w:val="top"/></w:tcPr>'
                    '<w:p><w:pPr><w:spacing w:after="40" w:line="259" w:lineRule="auto"/></w:pPr>'
                    f'{brun(text, 18)}</w:p></w:tc>')
        new += '</w:tr>'
    tbl = tbl.replace('</w:tbl>', new + '</w:tbl>')
    return region[:t0] + tbl + region[t1:]


def append_to_bullet(region, lead, text):
    i = region.index('>' + lead + '<')
    p_end = region.index('</w:p>', i)
    return region[:p_end] + brun(' ' + text) + region[p_end:]


STATUS_PARAGRAPH = (
    'Status at Workbook 2 (November 12, 2026). Six of the eighteen CMPE 295A components are done: '
    'the investigation workspace, plan review and approval, the plan synthesiser, the orchestrator, and '
    'the PostgreSQL and CSV/Excel connectors; the cross-source reconciler is partial (key profiling done, '
    'transform search and mapping proposals in Sprint 4). The plan path now works end to '
    'end: a question becomes a typed, validated plan that the analyst reviews and approves. The plan '
    'synthesiser was tested with direct calls to the Claude API; the model client that will take over those '
    'calls reads the provider key from the runtime environment, so it is built in Sprint 4 together with '
    'that environment. The execute, verify and record path (the specialist agents, the hop verifier and the '
    'lineage recorder) is designed and scheduled for Sprint 4; when it lands, the narrow vertical slice is '
    'complete. Orchestrator dispatch and reconciler profiling, planned for Sprint 4, are already done, and '
    'spikes SP-4 and SP-5 moved into Sprint 4 alongside the components they exercise. Changes since '
    'Workbook 1 are shown in bold in this chapter and in Chapter 9.')

WORK_COMPLETED = [
    ('Investigation workspace', 'S1 (skeleton)', 'S1 (Oct 4)', 'SZ'),
    ('Wireframes', 'S1', 'S1 (Oct 4)', 'PS (reassigned from SZ)'),
    ('Plan review and approval', 'S2', 'S2 (Oct 18)', 'SZ'),
    ('Plan synthesiser (SP-3)', 'S2', 'S2 (Oct 18)', 'AK'),
    ('Orchestrator dispatch, budgets and retry caps', 'S4', 'S4 (Nov 10)', 'AK'),
    ('Cross-source reconciler profiling', 'S4', 'S4 (Nov 10)', 'PS, AN'),
    ('PostgreSQL connector (SP-1)', 'S1', 'S1 (Oct 4)', 'AN'),
    ('CSV / Excel connector (SP-2)', 'S2', 'S2 (Oct 18)', 'AN'),
]


def update_chapter8(doc):
    a = doc.index('>Implementation Plan and Progress<')
    b = doc.index('>Project Schedule<')
    r = doc[a:b]

    # 1. Status paragraph after the chapter's opening paragraph.
    i = r.index('The early prototype demo requested by the advisor')
    p_end = r.index('</w:p>', i) + len('</w:p>')
    r = r[:p_end] + f'<w:p><w:pPr><w:pStyle w:val="IndentedParagraph"/></w:pPr>{brun(STATUS_PARAGRAPH)}</w:p>' + r[p_end:]

    # 2. Environment status column.
    S = 4
    r = edit_cells(r, 'Programming and execution environment', {
        ('Source control and CI', S): ('replace', 'Repository created; CI running on every pull request since Oct 4'),
        ('Orchestrator', S): ('replace', 'Done: typed plan DAG, dispatch, budget and retry caps'),
        ('Model access', S): ('replace', 'Plan synthesiser tested with direct Claude API calls; model client designed (Chapter 6), built in S4 with the runtime environment'),
        ('Database access', S): ('replace', 'Done: read-only PostgreSQL connector'),
        ('File and CSV engine', S): ('replace', 'Done: CSV / Excel connector'),
        ('Profiling', S): ('replace', 'Done: reconciler key profiling'),
        ('Application store', S): ('replace', 'Schema designed (Figure 7); tables built in S4'),
        ('Audit log', S): ('replace', 'Designed; built in S4'),
        ('API and front end', S): ('replace', 'Done: investigation workspace and plan review'),
        ('Packaging', S): ('replace', 'Done: Docker Compose stack since Oct 4'),
        ('Harness', S): ('replace', 'Designed (Chapter 7); first run Nov 22 (SP-6)'),
    })

    # 3. Prototyping environment bullets.
    r = append_to_bullet(r, 'Local stack.', 'Status: in use by all four members since Oct 4.')
    r = append_to_bullet(r, 'Reference schema.', 'Status: generated and loaded on Oct 18.')
    r = append_to_bullet(r, 'Unmodelled source.', 'Status: used to test the CSV / Excel connector and the reconciler.')
    r = append_to_bullet(r, 'Fixed question set.', 'Status: designed (Chapter 7); built in S4 for SP-6.')
    r = append_to_bullet(r, 'Seeded-error set.', 'Status: protocol defined (Table 12); built in S4.')

    # 4. Spikes: status after the target date.
    T = 3
    r = edit_cells(r, 'Sample programs used to learn each technology', {
        ('SP-1', T): ('append', ' – Done (Oct 4)'),
        ('SP-2', T): ('append', '; done Oct 18'),
        ('SP-3', T): ('append', '; done Oct 18'),
        ('SP-4', T): ('append', '; moved to S4 with the hop verifier'),
        ('SP-5', T): ('append', '; moved to S4–S5 with the lineage recorder'),
        ('SP-6', T): ('append', ' – on track'),
    })

    # 5. Prototype increments: status after the sprint.
    P = 3
    r = edit_cells(r, 'Prototype increments for CMPE 295A', {
        ('1', P): ('append', ' – repository and CI done (Oct 4); harness and question sets moved to S4'),
        ('2', P): ('append', ' – Done'),
        ('3', P): ('append', ' – Done'),
        ('4', P): ('append', '; orchestrator dispatch done, agents in S4'),
        ('5', P): ('append', '; moved to S4'),
        ('6', P): ('append', '; S4–S5'),
        ('7', P): ('append', '; S5'),
    })

    # 6. New section and table before the progress log.
    k = r.index('>Progress Log<')
    h = max(r.rfind('<w:p>', 0, k), r.rfind('<w:p ', 0, k))
    new_section = (
        f'<w:p><w:pPr><w:pStyle w:val="Heading2"/></w:pPr>{brun("Work Completed Since Workbook 1")}</w:p>'
        f'<w:p><w:pPr><w:pStyle w:val="IndentedParagraph"/></w:pPr>{brun("Table 18 lists the components finished since Workbook 1 against the sprint in which Workbook 1 scheduled them. Orchestrator dispatch and reconciler profiling were scheduled for Sprint 4.")}</w:p>'
        + table('Work completed since Workbook 1', [3300, 1900, 2000, 1440],
                ['Component', 'Planned (Workbook 1)', 'Completed', 'Owner'],
                [['', '', '', ''] for _ in WORK_COMPLETED]))
    for row in WORK_COMPLETED:
        for text in row:
            new_section = new_section.replace(
                '<w:r><w:rPr><w:sz w:val="18"/><w:szCs w:val="18"/></w:rPr><w:t xml:space="preserve"></w:t></w:r>',
                brun(text, 18), 1)
    r = r[:h] + new_section + r[h:]

    # 7. Progress log: update open rows and add new ones.
    r = edit_cells(r, 'Implementation progress', {
        ('Sep 28 – Oct 11, 2026', 2): ('replace', 'SP-1, CI and Docker Compose done (Oct 4); SP-2 and SP-3 done in Sprint 2 (Oct 18); harness skeleton and question set moved to S4'),
        ('Oct 2026', 2): ('replace', 'Done'),
        ('Oct 12 – Oct 25, 2026', 2): ('replace', 'Plan synthesis and CSV ingestion done; ground truth, seeded errors and SP-4 moved to S4'),
    })
    r = add_rows(r, 'Implementation progress', [
        ('Oct 26 – Nov 8, 2026', 'Sprint 3: design for Workbook 2 (Chapters 6 and 7) completed Nov 1; semantic resolver, hop verifier and lineage view moved to S4', 'Done'),
        ('Nov 2026', 'Workbook 2 design: as-built status, UML class, sequence and ER diagrams, test plan and evaluation protocol (Chapters 6 and 7); owners added for the fetch agent (AN), analytics agent (PS) and artifact store (AN); wireframes and UI mockups reassigned from SZ to PS', 'Done'),
        ('Nov 9 – Nov 22, 2026', 'Sprint 4: specialist agents, hop verifier (SP-4), lineage recorder (SP-5), model client, application store, harness and first accuracy figure (SP-6)', 'In progress'),
    ])
    return doc[:a] + r + doc[b:]


# ---------------------------------------------------------------- Chapter 9 (changes in bold)
REPLAN_PARAGRAPH = (
    'For Workbook 2 the CMPE 295A sprints were re-planned. The source substrate, the plan path, orchestrator '
    'dispatch and reconciler profiling are done (Table 18). The measurement work (harness skeleton, question set '
    'and seeded-error set) and the Sprint 3 build items (binding store, semantic resolver, hop verifier and lineage '
    'view) moved into Sprint 4, so milestone M2 moves from November 8 to November 22; M3, M4 and the '
    'verification-cost study keep their dates, and the CMPE 295B sprints are unchanged. Owners were added for the '
    'fetch agent (AN), the analytics agent (PS) and the artifact store (AN), and the wireframes and UI mockups were '
    'reassigned from SZ to PS. Figure 10 shows the updated schedule, '
    'Table 21 the re-planned assignments, and Figures 11 and 12 the task dependencies and critical paths.')

GANTT_SVG_RID = 'rId930'


def update_chapter9(doc):
    a = doc.index('>Project Schedule<')
    body = _re.findall(r'<w:sectPr>.*?</w:sectPr>', doc, _re.S)[-1]
    b = doc.rindex(body)
    r = doc[a:b]

    # 1. Re-plan paragraph after the chapter's opening paragraph.
    i = r.index('will be added to the schedule once its date is agreed.')
    p_end = r.index('</w:p>', i) + len('</w:p>')
    r = r[:p_end] + f'<w:p><w:pPr><w:pStyle w:val="IndentedParagraph"/></w:pPr>{brun(REPLAN_PARAGRAPH)}</w:p>' + r[p_end:]

    # 2. Milestone dates with status.
    r = edit_cells(r, 'Milestones and exit criteria', {
        ('M1', 1): ('append', ' – achieved'),
        ('M2', 1): ('append', ' → Nov 22, 2026 (harness and seeded-error set moved to S4)'),
        ('M3', 1): ('append', ' – on track'),
        ('M4', 1): ('append', ' – on track'),
        ('M5', 1): ('append', ' – unchanged'),
        ('M6', 1): ('append', ' – unchanged'),
    })

    # 3. Gantt: updated caption and image (PNG replaced in place, SVG added), new aspect ratio.
    i = r.index('>Project schedule by sprint and team member<')
    p_end = r.index('</w:p>', i)
    r = r[:p_end] + brun(' (updated for Workbook 2 with status and re-plan)') + r[p_end:]
    j = r.index('r:embed="rId902"')
    ds = r.rindex('<w:drawing>', 0, j); de = r.index('</w:drawing>', j)
    drawing = r[ds:de]
    w, h = png_size(ASSETS / 'ch9_schedule_wb2.png')
    cx = 5486400; cy = int(cx * h / w)
    drawing = _re.sub(r'<wp:extent cx="\d+" cy="\d+"/>', f'<wp:extent cx="{cx}" cy="{cy}"/>', drawing)
    drawing = _re.sub(r'<a:ext cx="\d+" cy="\d+"/>', f'<a:ext cx="{cx}" cy="{cy}"/>', drawing)
    drawing = drawing.replace('<a:blip r:embed="rId902"/>', f'<a:blip r:embed="rId902">{SVG_EXT % GANTT_SVG_RID}</a:blip>')
    r = r[:ds] + drawing + r[de:]

    # 4. Task assignment per sprint (columns: 1 AK, 2 AN, 3 PS, 4 SZ).
    r = edit_cells(r, 'Task assignment per sprint', {
        ('S1 (', 1): ('append', ' (schema done in S2, Oct 18; model client moved to S4)'),
        ('S1 (', 2): ('append', ' (repository, CI, Docker Compose and SP-1 done Oct 4; DuckDB path done Oct 18)'),
        ('S1 (', 3): ('append', ' (moved to S4); wireframes (reassigned from SZ, done Oct 4)'),
        ('S1 (', 4): ('append', ' (workspace skeleton done Oct 4; wireframes reassigned to PS)'),
        ('S2 (', 1): ('append', ' (done Oct 18)'),
        ('S2 (', 2): ('append', ' (CSV and Excel done Oct 18; application store moved to S4)'),
        ('S2 (', 3): ('append', ' (moved to S4)'),
        ('S2 (', 4): ('append', ' (done Oct 18)'),
        ('S3 (', 1): ('append', ' (moved to S4)'),
        ('S3 (', 2): ('append', ' (profiling done Nov 10; binding store moved to S4)'),
        ('S3 (', 3): ('append', ' (moved to S4)'),
        ('S3 (', 4): ('append', ' (moved to S4)'),
        ('S4 (', 1): ('append', ' (done Nov 10); model client and runtime environment; semantic resolver'),
        ('S4 (', 2): ('append', ' (done Nov 10); fetch agent; application store and binding store'),
        ('S4 (', 3): ('append', '; question set, ground truth and seeded errors; hop verifier (SP-4); reconciler transform search and mapping proposals'),
        ('S4 (', 4): ('append', '; lineage recorder, hop view and replay (SP-5); export moved to S5'),
        ('S5 (', 3): ('append', '; analytics agent'),
        ('S5 (', 4): ('append', '; export artifact'),
        ('Winter break', 3): ('append', '; screen mockups v2 (optional, reassigned from SZ)'),
        ('Winter break', 4): ('append', ' (reassigned to PS)'),
    })

    # 5. Dependencies and critical path: text on the portrait page, each PERT chart on a landscape page.
    r += (f'<w:p><w:pPr><w:pStyle w:val="Heading2"/></w:pPr>{brun("Dependencies and Critical Path")}</w:p>'
          f'<w:p><w:pPr><w:pStyle w:val="IndentedParagraph"/></w:pPr>{brun("Figures 11 and 12 are PERT charts for the two semesters. In CMPE 295A the critical path runs from the PostgreSQL connector through the plan synthesiser, orchestrator dispatch, the fetch agent, the hop verifier, the lineage recorder and export to M3, then through the verification-cost study to M4; the model client must land before the fetch agent. Any slip on that path moves M3, so those tasks are reviewed first at each sprint demo. In CMPE 295B the four member streams run in parallel with equal duration, so a slip in any one of them delays the M5 Beta; after Sprint 10 the critical path is the shared chain through the paper and the release to M6.")}</w:p>'
          + SECTION_BREAK_PORTRAIT
          + figure('PERT chart for CMPE 295A (Fall 2026) with dependencies and critical path', *FIGS[7], landscape=True)
          + figure('PERT chart for CMPE 295B (Spring 2027) with dependencies and critical path', *FIGS[8], landscape=True, new_page=True))

    # The final section now holds only the PERT charts, so it is landscape.
    land = body.replace('<w:pgSz w:w="12240" w:h="15840" w:code="1"/>',
                        '<w:pgSz w:w="15840" w:h="12240" w:orient="landscape" w:code="1"/>')
    assert 'landscape' in land
    return doc[:a] + r + land + doc[b + len(body):]


# ---------------------------------------------------------------- Front matter and Chapter 5 (Workbook 2 notes, bold)
WB2_UPDATE_NOTE = (
    'Workbook 2 update. This submission completes Chapters 6 (Project Design) and 7 (QA, Performance, '
    'Deployment Plan), updates Chapters 8 and 9, and reports implementation progress as of November 12, 2026. '
    'Changes to Chapters 8 and 9 relative to Workbook 1 are shown in bold.')

CH5_UPDATE = (
    'Implementation update (Workbook 2). The structure of the architecture is unchanged. Two details were '
    'settled during design and implementation: the orchestrator also composes the final answer, calling the '
    'small model through the model client to write established facts from verified hops only; and the plan '
    'synthesiser was first tested with direct calls to the Claude API, with the model client and its runtime '
    'environment built in Sprint 4. The as-built status of every component is shown in Chapter 6, Figure 2.')


def update_front_and_ch5(doc):
    h1 = doc.index('<w:pStyle w:val="Heading1"/>')
    front = doc[:h1]
    assert front.count('October 8, 2026') == 1
    front = front.replace('October 8, 2026', 'November 12, 2026')
    front = edit_cells(front, 'Team responsibilities and section ownership', {
        ('Atharva', 2): ('append', '; Ch. 6 services and sequence design; Ch. 8 status'),
        ('Akshay', 2): ('append', '; Ch. 6 database design; Ch. 7 deployment plan'),
        ('Pranjal', 2): ('append', '; Ch. 6 verification design; Ch. 7 test plan and evaluation; UI mockups'),
        ('Shantanu', 2): ('append', '; Ch. 6 answer presentation; Ch. 8 progress log'),
    })
    t = front.index('>Team responsibilities and section ownership<')
    t_end = front.index('</w:tbl>', t) + len('</w:tbl>')
    front = (front[:t_end] + f'<w:p><w:pPr><w:pStyle w:val="IndentedParagraph"/></w:pPr>{brun(WB2_UPDATE_NOTE)}</w:p>'
             + front[t_end:])
    doc = front + doc[h1:]

    # Chapter 5: bold note just before the Chapter 6 heading.
    p6 = doc.index('>Project Design<')
    s6 = doc.rfind('<w:p>', 0, p6)
    doc = doc[:s6] + f'<w:p><w:pPr><w:pStyle w:val="IndentedParagraph"/></w:pPr>{brun(CH5_UPDATE)}</w:p>' + doc[s6:]
    return doc


SECTION_BREAK_PORTRAIT_FIRST = SECTION_BREAK_PORTRAIT = SECTION_BREAK_LANDSCAPE = None


def section_breaks(doc):
    """Build the two section-break paragraphs from the document's own body section properties."""
    import re
    global SECTION_BREAK_PORTRAIT_FIRST, SECTION_BREAK_PORTRAIT, SECTION_BREAK_LANDSCAPE
    body = re.findall(r'<w:sectPr>.*?</w:sectPr>', doc, re.S)[-1]
    assert '<w:pgNumType w:start="1"/>' in body
    portrait = body                                           # keeps the restart at page 1
    landscape = (body.replace('<w:pgNumType w:start="1"/>', '')
                     .replace('<w:pgSz w:w="12240" w:h="15840" w:code="1"/>',
                              '<w:pgSz w:w="15840" w:h="12240" w:orient="landscape" w:code="1"/>'))
    assert 'orient="landscape"' in landscape
    blank = '<w:p><w:pPr><w:pStyle w:val="IndentedParagraph"/><w:spacing w:after="0"/>%s</w:pPr></w:p>'
    SECTION_BREAK_PORTRAIT_FIRST = blank % portrait
    SECTION_BREAK_PORTRAIT = blank % portrait.replace('<w:pgNumType w:start="1"/>', '')
    SECTION_BREAK_LANDSCAPE = blank % landscape
    # The final section continues page numbering instead of restarting it.
    return doc.replace(body, body.replace('<w:pgNumType w:start="1"/>', ''))


def fix_heading_spacing():
    """Headings inherit Normal's exact 28 pt line, which Google Docs and most previewers turn into
    ~2.3x line spacing (large uneven gaps). Give Heading 1 and 2 single line spacing with space
    before/after that adds up to the same 28 pt, so Word looks the same and other viewers stop
    inflating the gaps. Style definitions only; no document text changes."""
    path = UN / 'word' / 'styles.xml'
    st = path.read_bytes().decode('utf-8')        # keep line endings byte-for-byte
    fixes = {
        'Heading1': '<w:spacing w:before="0" w:after="240" w:line="240" w:lineRule="auto"/>',
        'Heading2': '<w:spacing w:before="200" w:after="80" w:line="240" w:lineRule="auto"/>',
    }
    for sid, spacing in fixes.items():
        i = st.index(f'w:styleId="{sid}"')
        end = st.index('</w:pPr>', i)
        assert '<w:spacing' not in st[i:end], sid
        j = st.index('<w:outlineLvl', i)          # schema order: spacing comes before outlineLvl
        assert j < end
        st = st[:j] + spacing + st[j:]
    path.write_bytes(st.encode('utf-8'))


def main():
    fix_heading_spacing()
    doc = DOC.read_text(encoding='utf-8')
    doc = section_breaks(doc)
    i = doc.find(PLACEHOLDER_START)
    assert i > 0 and doc.count(PLACEHOLDER_START) == 1, 'placeholder not found exactly once'
    s = max(doc.rfind('<w:p>', 0, i), doc.rfind('<w:p ', 0, i))
    e = doc.find('</w:p>', i) + len('</w:p>')
    doc = doc[:s] + chapter6() + doc[e:]
    i = doc.find(PLACEHOLDER7_START)
    assert i > 0 and doc.count(PLACEHOLDER7_START) == 1, 'Chapter 7 placeholder not found exactly once'
    s = max(doc.rfind('<w:p>', 0, i), doc.rfind('<w:p ', 0, i))
    e = doc.find('</w:p>', i) + len('</w:p>')
    doc = doc[:s] + chapter7() + doc[e:]
    doc = update_chapter8(doc)
    doc = update_chapter9(doc)
    doc = update_front_and_ch5(doc)
    DOC.write_text(doc, encoding='utf-8')

    rels = RELS.read_text(encoding='utf-8')
    add = ''
    for png, rid in FIGS:
        shutil.copy(ASSETS / png, UN / 'word' / 'media' / png)
        if rid not in rels:
            add += (f'<Relationship Id="{rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/'
                    f'relationships/image" Target="media/{png}"/>')
    for png, rid in FIGS:
        svg = png.replace('.png', '.svg')
        if not (ASSETS / svg).exists():
            continue
        shutil.copy(ASSETS / svg, UN / 'word' / 'media' / svg)
        if SVG_RID[rid] not in rels:
            add += (f'<Relationship Id="{SVG_RID[rid]}" Type="http://schemas.openxmlformats.org/officeDocument/2006/'
                    f'relationships/image" Target="media/{svg}"/>')
    RELS.write_text(rels.replace('</Relationships>', add + '</Relationships>'), encoding='utf-8')
    shutil.copy(ASSETS / 'ch9_schedule_wb2.png', UN / 'word' / 'media' / 'figure2.png')
    shutil.copy(ASSETS / 'ch9_schedule_wb2.svg', UN / 'word' / 'media' / 'ch9_schedule_wb2.svg')
    rels = RELS.read_text(encoding='utf-8')
    if GANTT_SVG_RID not in rels:
        rels = rels.replace('</Relationships>', f'<Relationship Id="{GANTT_SVG_RID}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/ch9_schedule_wb2.svg"/></Relationships>')
        RELS.write_text(rels, encoding='utf-8')
    ct_path = UN / '[Content_Types].xml'
    ct = ct_path.read_text(encoding='utf-8')
    if 'Extension="svg"' not in ct:
        ct = ct.replace('</Types>', '<Default Extension="svg" ContentType="image/svg+xml"/></Types>')
        ct_path.write_text(ct, encoding='utf-8')
    print('Chapters 6, 7, 8 and 9 written:', len(FIGS), 'figures (SVG + PNG fallback); diagrams on landscape pages, text on portrait pages')


if __name__ == '__main__':
    main()
