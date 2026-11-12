#!/usr/bin/env python3
"""Figure 4 - UML class diagram of the services (who resolves, plans, executes, verifies, composes).

Each service is a component of Figure 1. Grey boxes are domain classes defined in Figure 3.
Sources: deep dives 1-6, D01 (pipeline, compose answer), D02 (verify loop), D03
(orchestration, no agent-to-agent calls), D05 (model routing: prose on the small model),
D07 (source interface).
"""
from uml_common import Drawer, box_height, HEADER_H

STEM = 'ch6_class_services'
BOX_W, GAP = 218, 96
COLS = [20 + i*(BOX_W+GAP) for i in range(6)]
WIDTH = COLS[-1] + BOX_W + 20
REF_H = HEADER_H + 24

# Service classes: name: (col, row, tier, title, attributes, methods)
SERVICES = {
    'SemanticSupplier': (0, 0, 'integ', '«interface» SemanticSupplier', [
        '«impl» DbtSemanticLayer [295B]', 'precedence over inferred'],
        ['+ definitions(): Binding[]']),
    'StepResult': (3, 0, 'agent', '«value» StepResult', [
        'title: str', 'sql_executed: SQL', 'attempts: int', 'rows_in / rows_out: int',
        'grain: str', 'output_ref: hash', 'sample_rows'], []),
    'SemanticResolver': (0, 1, 'orch', 'SemanticResolver', [
        'margin_threshold: float', 'retrieval: BM25 + embeddings', 'model: ModelClient'],
        ['+ resolve(question): Binding[]', '+ ask(term, candidates)', '+ confirm(term, choice)']),
    'PlanSynthesiser': (1, 1, 'orch', 'PlanSynthesiser', [
        'hop_ceiling: int', 'plan_cache: signature → Plan'],
        ['+ synthesise(q, bindings): Plan', '+ validate(plan): Errors', '+ revise(plan, failure) [295B]']),
    'ModelClient': (2, 1, 'orch', 'ModelClient', [
        "provider: organisation's own key", 'mode: FULL | SCHEMA_ONLY', '        | FILTERED_SAMPLES'],
        ['+ plan(prompt)   frontier', '+ sql(prompt)   frontier', '+ prose(prompt)   small']),
    'SpecialistAgent': (3, 1, 'agent', '«abstract» SpecialistAgent', [
        '«impl» FetchAgent', '«impl» AnalyticsAgent', '«impl» VisualizationAgent [295B]',
        '«impl» MLAgent [295B]', 'loop: reason → act → observe'],
        ['+ run(step): StepResult', '+ repair(sql, error)']),
    'SourceConnector': (4, 1, 'integ', '«interface» SourceConnector', [
        '«impl» PostgresConnector', '«impl» FileConnector  (DuckDB)',
        '«impl» RestJsonConnector [295B]'],
        ['+ describe()', '+ sample(n)', '+ execute(sql)', '+ profile(cols)']),
    'CrossSourceReconciler': (0, 3, 'verify', 'CrossSourceReconciler', [
        'sql via: SourceConnector', 'match: Jaccard + edit distance'],
        ['+ profile_keys(a, b)', '+ propose(a, b): MappingProposal', '+ coverage(a, b)']),
    'HopVerifier': (1, 3, 'verify', 'HopVerifier', [
        'planner · renderer · guard · runner', 'sql via: SourceConnector', 'no model calls; 5 s timeout'],
        ['+ verify_hop(ctx): HopVerdict', '+ rerun_checks(hop): HopVerdict', '+ doubt_signals(inv)']),
    'LineageRecorder': (2, 3, 'verify', 'LineageRecorder', [
        'store: Application + Artifact', 'content-addressed outputs'],
        ['+ record(step, result, checks): Hop', '+ replay(hop): Hop', '+ export(investigation)']),
}
# Referenced domain classes: name: (col, row, title, note)
REFS = {
    'Binding': (0, 0, 'Binding', 'see Figure 3'),
    'Plan': (1, 0, 'Plan', 'see Figure 3'),
    'Provider': (2, 0, 'External model provider', 'frontier: plan, SQL · small: prose'),
    'Source': (4, 0, 'Source', 'see Figure 3'),
    'AuditEvent': (5, 1, 'AuditEvent', 'see Figure 3'),
    'Answer': (3, 3, 'Answer', 'see Figures 3, 5'),
    'PlanApproval': (4, 3, 'PlanApproval', 'see Figure 3'),
    'MappingProposal': (0, 4, 'MappingProposal', 'see Figure 3'),
    'CheckResult': (1, 4, 'HopVerdict + CheckResults', 'see Figure 3'),
    'Hop': (2, 4, 'Hop', 'see Figure 3'),
}
ORCH_ATTRS = ['plan: Plan (approved)   ·   state: RunState   ·   budget / cost_spent   ·   retry_cap: int',
              'every StepResult returns here; agents never call each other']
ORCH_METHODS = ['+ run(plan)   ·   + dispatch(step): StepResult   ·   + compose_answer(): Answer   ·   + halt(reason)   ·   + replan()  [295B]']


def cx(col):
    return COLS[col] + BOX_W/2 - 20   # x offset from the Orchestrator's left edge (x = 20)


EDGES = [
    # services to the objects they create or use (top half)
    ('SemanticResolver', 'Binding', ('t', .5), ('b', .5), '', '', '«creates»', 'dep'),
    ('SemanticSupplier', 'Binding', ('b', .5), ('t', .5), '', '', '«supplies» [295B]', 'dep'),
    ('PlanSynthesiser', 'Plan', ('t', .5), ('b', .5), '', '', '«creates»', 'dep'),
    ('ModelClient', 'Provider', ('t', .5), ('b', .5), '', '', '«HTTPS»', 'dep'),
    ('SpecialistAgent', 'StepResult', ('t', .5), ('b', .5), '', '', '«returns»', 'dep'),
    ('SourceConnector', 'Source', ('t', .5), ('b', .5), '1', '1', 'accesses', 'assoc'),
    ('PlanSynthesiser', 'ModelClient', ('r', 60), ('l', 60), '', '', '«uses»', 'dep'),
    ('SpecialistAgent', 'ModelClient', ('l', 60), ('r', 60), '', '', '«reasons via»', 'dep'),
    ('SpecialistAgent', 'SourceConnector', ('r', 60), ('l', 60), '', '', '«acts via»', 'dep'),
    ('SourceConnector', 'AuditEvent', ('r', 60), ('l', 26), '', '', '«writes»', 'dep'),
    # Orchestrator to the services above it
    ('Orchestrator', 'SemanticResolver', ('t', cx(0)), ('b', .5), '', '', '«invokes»', 'dep'),
    ('Orchestrator', 'PlanSynthesiser', ('t', cx(1)), ('b', .5), '', '', '«invokes»', 'dep'),
    ('Orchestrator', 'ModelClient', ('t', cx(2)), ('b', .5), '', '', '«reasons via» prose', 'dep'),
    ('Orchestrator', 'SpecialistAgent', ('t', cx(3)), ('b', .5), '1', '1..*', 'dispatches', 'assoc'),
    # Orchestrator to the services and objects below it
    ('Orchestrator', 'CrossSourceReconciler', ('b', cx(0)), ('t', .5), '', '', '«invokes»', 'dep'),
    ('Orchestrator', 'HopVerifier', ('b', cx(1)), ('t', .5), '', '', '«invokes» per hop', 'dep'),
    ('Orchestrator', 'LineageRecorder', ('b', cx(2)), ('t', .5), '', '', '«invokes» per hop', 'dep'),
    ('Orchestrator', 'Answer', ('b', cx(3)), ('t', .5), '', '', '«creates»', 'dep'),
    ('Orchestrator', 'PlanApproval', ('b', cx(4)), ('t', .5), '', '', '«awaits»', 'dep'),
    ('CrossSourceReconciler', 'MappingProposal', ('b', .5), ('t', .5), '', '', '«creates»', 'dep'),
    ('HopVerifier', 'CheckResult', ('b', .5), ('t', .5), '', '', '«produces»', 'dep'),
    ('LineageRecorder', 'Hop', ('b', .5), ('t', .5), '', '', '«records»', 'dep'),
]


def build():
    # Row heights.
    h_of = {n: box_height(s[4], s[5]) for n, s in SERVICES.items()}
    rows = {r: [REF_H] for r in range(5)}
    for n, s in SERVICES.items():
        rows[s[1]].append(h_of[n])
    orch_h = box_height(ORCH_ATTRS, ORCH_METHODS)
    rows[2] = [orch_h]
    rows[0].append(34 + 26*5)  # legend
    rows[0].append(h_of['SemanticSupplier'] + 46 + REF_H)  # supplier above the Binding reference
    row_y, y = {}, 70
    for r in range(5):
        row_y[r] = y
        y += max(rows[r]) + 72
    footer_y = y - 30
    d = Drawer(WIDTH, footer_y + 70, STEM, 'InsightPilot - UML class diagram of the services')
    d.text(WIDTH/2, 38, 'UML class diagram - services: who resolves, plans, executes, verifies and composes', 22, 'b', '#1f2937', 'middle')

    # Geometry. Row-0 references sit on the row's bottom edge, so their links stay short.
    for n, (col, row, *_r) in SERVICES.items():
        yy = row_y[row] + (max(rows[0]) - h_of[n] if row == 0 and n != 'SemanticSupplier' else 0)
        d.geo[n] = (COLS[col], yy, BOX_W, h_of[n])
    for n, (col, row, title, note) in REFS.items():
        yy = row_y[row] + (max(rows[0]) - REF_H if row == 0 else 0)
        d.geo[n] = (COLS[col], yy, BOX_W, REF_H)
    d.geo['Orchestrator'] = (20, row_y[2], WIDTH-40, orch_h)

    for e in EDGES:
        d.edge(*e)

    # Orchestrator ··> StepResult «receives»: routed up the gap right of SpecialistAgent,
    # then left into StepResult, so it does not cross the agent box.
    sx, sy, sw, sh = d.geo['StepResult']
    xg = COLS[3] + BOX_W + 30
    ys = sy + sh*0.72
    d.seg([(xg, row_y[2]), (xg, ys), (sx + sw, ys)], dashed=True)
    d.seg([(sx + sw + 10, ys - 5), (sx + sw, ys), (sx + sw + 10, ys + 5)])
    d.text(xg + 7, row_y[2] - 14, '«receives»', 11, 'i', '#64748b', 'start')

    for n, (col, row, tier, title, attrs, methods) in SERVICES.items():
        x, yy, w, _ = d.geo[n]
        d.class_box(n, x, yy, w, tier, title, attrs, methods, dashed=(n == 'SemanticSupplier'))
    for n, (col, row, title, note) in REFS.items():
        x, yy, w, _ = d.geo[n]
        d.ref_box(n, x, yy, w, title, note)
    d.class_box('Orchestrator', 20, row_y[2], WIDTH-40, 'orch', 'Orchestrator', ORCH_ATTRS, ORCH_METHODS, inline=True)

    d.legend(COLS[5], row_y[0], BOX_W, [
        ('solid', 'service class (Figure 1 component)'), ('dashed', 'CMPE 295B scope'),
        ('ref', 'domain class from Figure 3'),
        ('dep', 'dependency «invokes» «creates» «uses»'), ('assoc', 'association'),
    ])

    fy = footer_y + 18
    d.text(WIDTH/2, fy, 'Flow: resolve terms → synthesise plan → analyst approval → dispatch steps → StepResult → verify (SQL) → record Hop → compose_answer (small model via ModelClient) → Answer.', 12, 'n', '#64748b', 'middle', max_w=WIDTH-40)
    d.text(WIDTH/2, fy+22, 'Checks never use a model: HopVerifier and CrossSourceReconciler issue independent SQL through SourceConnector. Answer text is written only from verified hops, each sentence citing its hop.', 11, 'i', '#64748b', 'middle', max_w=WIDTH-40)
    d.save()
    print(f'Built {STEM}: {len(SERVICES)+1} service classes, {len(REFS)} referenced, {len(EDGES)} relationships')


if __name__ == '__main__':
    build()
