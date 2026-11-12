#!/usr/bin/env python3
"""Figure 3 - UML class diagram of the core domain model (what is stored).

Design, not build status: solid = CMPE 295A scope, dashed = CMPE 295B scope.
Services that create these objects are in Figure 4 (build_service_diagram.py).
Sources: D04 (entities, attributes), deep dives 2, 4, 5, 6, D01/D10 (gates),
ux_spec section 6 (answer). Question corresponds to TURN in D04.
"""
from uml_common import Drawer, box_height, LINE, MULT, LABEL

STEM = 'ch6_class_domain'
BOX_W, GAP = 218, 96
COLS = [20 + i*(BOX_W+GAP) for i in range(6)]
WIDTH = COLS[-1] + BOX_W + 20

# name: (col, row, tier, title, attributes, methods, dashed)
CLASSES = {
    'Binding': (0, 0, 'data', 'Binding', [
        'term: str  (normalised)', 'kind: TERM | JOIN_MAP', 'expression: SQL',
        'provenance: Provenance', 'schema_version: str', 'use_count / override_count'],
        ['+ invalidate()'], False),
    'Organisation': (1, 0, 'data', '«singleton» Organisation', [
        'id: UUID', 'name: str', 'one per deployment'], [], False),
    'Investigation': (2, 0, 'pres', 'Investigation', [
        'id: UUID', 'title: str', 'requester_role: Role',
        'established_facts: JSON', 'source_scope: Source[]'],
        ['+ ask(text): Question'], False),
    'Question': (3, 0, 'pres', 'Question', [
        'seq: int', 'text: str', 'asked_by / asked_at',
        'status: QuestionStatus', 'narration: str[]'],
        ['+ stream(event)', '+ halt(reason)'], False),
    'Answer': (4, 0, 'pres', 'Answer', [
        'heading: str', 'review_state: ReviewState',
        'least_certain_hop: Hop', 'created_at: UTC'],
        ['+ add_block(block)', '+ request_review()', '+ export()'], False),
    'SignOff': (5, 0, 'data', 'SignOff', [
        'reviewed_by: str', 'reviewed_at: UTC', 'note: str'], [], False),

    'MappingProposal': (0, 1, 'verify', 'MappingProposal', [
        'left_key / right_key: column', 'overlap: float  (Jaccard)',
        'coverage / unmatched_pct', 'proposed_map: value map'],
        ['+ approve()', '+ reject()'], False),
    'Source': (1, 1, 'integ', 'Source', [
        'id: UUID', 'kind: POSTGRES | CSV | EXCEL', 'conn_ref / file_path',
        'read_only = true', 'schema_version: str'],
        ['+ schema_changed(): bool'], False),
    'PlanApproval': (2, 1, 'pres', 'PlanApproval', [
        'clarifications: {term: choice}', 'edits: JSON', 'approved_by / approved_at'],
        ['+ clarify(term)', '+ edit(step)', '+ approve()'], False),
    'Plan': (3, 1, 'orch', 'Plan', [
        'plan_id: str', 'status: PlanStatus', 'semantic_signature  (cache key)',
        'hop_count: int', 'diff_from_prior: JSON'],
        ['+ validate(): Errors', '+ to_dag()'], False),
    'AnswerBlock': (4, 1, 'pres', '«abstract» AnswerBlock', [
        'position: int', 'kind: TEXT | TABLE | CHART | DOUBT', 'cites: Hop[]',
        'CHART kind: [295B]'],
        ['+ render()'], False),

    'AuditEvent': (1, 2, 'data', 'AuditEvent', [
        'actor: str', 'statement: SQL', 'created_at: UTC', 'append-only JSONL'], [], False),
    'PlanStep': (3, 2, 'orch', 'PlanStep', [
        'step_id: str', 'step_type: StepType', 'source: Source',
        'bindings: Binding[]', 'declared_grain: str'],
        ['+ check_inputs()'], False),
    'Hop': (4, 2, 'verify', 'Hop', [
        'title: str', 'statement_issued: SQL', 'rows_in / rows_out: int',
        'grain_declared / grain_actual', 'attempts: int  (SQL repairs)',
        'replay_of: Hop [0..1]', 'output_ref: hash', 'sample_rows'],
        ['+ replay(): Hop', '+ diff(other)'], False),
    'HopVerdict': (5, 2, 'verify', 'HopVerdict', [
        'attempt: int  (re-run adds one)', 'status: VerdictStatus', 'doubt_reasons: str[]',
        'proposal_id: str [0..1]', 'verifier_version: str', 'started_at / finished_at'], [], False),
    'CheckResult': (5, 3, 'verify', 'CheckResult', [
        'kind: CheckKind', 'status: CheckStatus', 'expected / observed', 'tolerance: str',
        'sql: str[] + params', 'elapsed_ms: int', 'reason: str  (SKIP / ERROR)'], [], False),

    'Override': (4, 3, 'data', 'Override', [
        'overridden_by: str', 'annotation_type: str', 'rationale: str',
        'persisted_to_bindings: bool'], [], False),
    'ModelCard': (3, 3, 'agent', '«planned» ModelCard', [
        'target: str', 'features_used / _excluded', 'NOT_attempted_in_budget',
        'metric ± uncertainty'], [], True),
}

EDGES = [
    ('Organisation', 'Binding', ('l', 60), ('r', 60), '1', '0..*', 'accumulates', 'comp'),
    ('Organisation', 'Investigation', ('r', 60), ('l', 60), '1', '0..*', 'contains', 'comp'),
    ('Organisation', 'Source', ('b', .5), ('t', .5), '1', '0..*', 'connects', 'comp'),
    ('Investigation', 'Question', ('r', 75), ('l', 75), '1', '1..*', 'asks', 'comp'),
    ('Question', 'Answer', ('r', 75), ('l', 75), '1', '0..1', 'answered by', 'assoc'),
    ('Question', 'Plan', ('b', .5), ('t', .5), '1', '0..1', 'planned as', 'assoc'),
    ('Answer', 'SignOff', ('r', 60), ('l', 60), '1', '0..1', 'reviewed by', 'assoc'),
    ('Answer', 'AnswerBlock', ('b', .5), ('t', .5), '1', '1..*', 'ordered blocks', 'comp'),
    ('Plan', 'PlanApproval', ('l', 70), ('r', 70), '1', '0..1', 'gated by', 'assoc'),
    ('Plan', 'PlanStep', ('b', .5), ('t', .5), '1', '1..*', 'orders', 'comp'),
    ('MappingProposal', 'Source', ('r', 70), ('l', 70), '0..*', '2', 'reconciles', 'assoc'),
    ('MappingProposal', 'Binding', ('t', .5), ('b', .5), '0..1', '0..1', 'becomes', 'assoc'),
    ('Source', 'AuditEvent', ('b', .5), ('t', .5), '1', '0..*', 'statements logged', 'assoc'),
    ('PlanStep', 'Hop', ('r', 70), ('l', 70), '1', '0..1', 'executed as', 'assoc'),
    ('AnswerBlock', 'Hop', ('b', .5), ('t', .5), '0..*', '1..*', 'cites', 'assoc'),
    ('Hop', 'HopVerdict', ('r', 60), ('l', 60), '1', '1..*', 'verified as', 'comp'),
    ('HopVerdict', 'CheckResult', ('b', .5), ('t', .5), '1', '1..*', 'one per check', 'comp'),
    ('Hop', 'Override', ('b', .5), ('t', .5), '1', '0..*', 'may carry', 'assoc'),
    ('Hop', 'ModelCard', ('l', .92), ('r', .3), '1', '0..1', 'if ML hop', 'assoc'),
]


def build():
    rows = {}
    for c in CLASSES.values():
        rows.setdefault(c[1], []).append(box_height(c[4], c[5]))
    row_y, y = {}, 70
    for r in sorted(rows):
        row_y[r] = y
        y += max(rows[r]) + 78
    footer_y = y - 30
    d = Drawer(WIDTH, footer_y + 134, STEM, 'InsightPilot - UML class diagram of the core domain model')
    d.text(WIDTH/2, 38, 'UML class diagram - core domain model (CMPE 295A scope solid, CMPE 295B scope dashed)', 22, 'b', '#1f2937', 'middle')

    # Register geometry first so edges are drawn under the boxes.
    for name, (col, row, tier, title, attrs, methods, dashed) in CLASSES.items():
        d.geo[name] = (COLS[col], row_y[row], BOX_W, box_height(attrs, methods))
    for e in EDGES:
        d.edge(*e)

    # PlanStep self-association: depends_on (makes the plan a DAG).
    x, y0, w, h = d.geo['PlanStep']
    b = y0 + h
    d.seg([(x+w*.25, b), (x+w*.25, b+26), (x+w*.6, b+26), (x+w*.6, b)])
    d.poly([(x+w*.6, b), (x+w*.6-5, b+9), (x+w*.6+5, b+9)], LINE)
    d.text(x+w*.425, b+42, 'depends_on', 11, 'i', LABEL, 'middle')
    d.text(x+w*.25-16, b+20, '0..*', 11.5, 'b', MULT, 'middle')
    d.text(x+w*.6+18, b+20, '0..*', 11.5, 'b', MULT, 'middle')

    for name, (col, row, tier, title, attrs, methods, dashed) in CLASSES.items():
        d.class_box(name, COLS[col], row_y[row], BOX_W, tier, title, attrs, methods, dashed)

    d.legend(COLS[5], row_y[1], BOX_W, [
        ('solid', 'CMPE 295A scope'), ('dashed', 'CMPE 295B scope'),
        ('comp', 'composition (whole ◆ part)'), ('assoc', 'association'),
    ])

    fy = footer_y + 20
    for line in [
        'PlanStatus = DRAFT | CLARIFYING | APPROVED | EXECUTING | DONE | HALTED     QuestionStatus = CLARIFYING | PLANNING | AWAITING_APPROVAL | EXECUTING | ANSWERED | HALTED',
        'VerdictStatus = PASS | WARN | FAIL | ERROR     CheckStatus = PASS | WARN | FAIL | SKIP | ERROR     ReviewState = UNREVIEWED | REVIEWED',
        'StepType = FETCH | FILTER | JOIN | AGGREGATE | COMPARE | DERIVE | MODEL [295B] | RENDER [295B]     Provenance = SEMANTIC_LAYER | ANALYST_CONFIRMED | INFERRED | STAKEHOLDER_UNCONFIRMED',
        'CheckKind = ROW_COUNT | GRAIN_UNIQUE | JOIN_FANOUT | JOIN_COVERAGE | NULL_RATE | BOUNDARY_TOTAL | PERIOD_BOUNDS | VALUE_RANGE',
    ]:
        d.text(WIDTH/2, fy, line, 12, 'n', '#64748b', 'middle', max_w=WIDTH-40)
        fy += 21
    d.text(WIDTH/2, fy+6, 'Question corresponds to TURN in D04. PlanStep.source and PlanStep.bindings are associations to Source and Binding, shown as typed attributes. Services that create these objects: Figure 4.', 11, 'i', '#64748b', 'middle', max_w=WIDTH-40)
    d.save()
    print(f'Built {STEM}: {len(CLASSES)} classes, {len(EDGES)+1} relationships')


if __name__ == '__main__':
    build()
