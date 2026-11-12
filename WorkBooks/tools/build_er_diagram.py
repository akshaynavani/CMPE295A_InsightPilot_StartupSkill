#!/usr/bin/env python3
"""Database ER diagram of the Application Store (SVG, PDF, PNG).

Visual language follows the AI Agent Marketplace Workbook 2, Figure 5: one box per table
(snake_case), PK / FK rows then grouped columns, red 1 / N cardinalities at each end of a
relationship, dashed boxes for planned tables, explanatory footer. Tier colours follow our
Workbook 1 Figure 1. Tables come from D04 (durable record) and the classes of Fig. 3a.
"""
from uml_common import Drawer, box_height, HEADER_H

STEM = 'ch6_er'
BOX_W, GAP = 212, 72
COLS = [20 + i*(BOX_W+GAP) for i in range(6)]
WIDTH = COLS[-1] + BOX_W + 20
REF_H = HEADER_H + 24

# table: (col, row, tier, columns, dashed)
TABLES = {
    'bindings': (0, 0, 'data', [
        'PK id', 'FK org_id', 'term_normalised, kind', 'expression, provenance',
        'schema_version', 'use_count, override_count', 'confirmed_by, confirmed_at'], False),
    'organisations': (0, 1, 'data', [
        'PK id', 'name, created_at'], False),
    'sources': (0, 2, 'integ', [
        'PK id', 'FK org_id', 'kind, conn_ref / file_path', 'read_only, schema_version'], False),

    'investigations': (1, 0, 'pres', [
        'PK id', 'FK org_id', 'title, requester_role', 'established_facts JSON',
        'source_scope JSON'], False),
    'plan_approvals': (1, 1, 'pres', [
        'PK id', 'FK plan_id (unique)', 'clarifications JSON, edits JSON',
        'approved_by, approved_at'], False),
    'mapping_proposals': (1, 2, 'verify', [
        'PK id', 'FK left_source_id, right_source_id', 'FK verdict_id, FK binding_id',
        'left_key, right_key', 'overlap, coverage, unmatched_pct', 'proposed_map JSON, status'], False),

    'questions': (2, 0, 'pres', [
        'PK id', 'FK investigation_id', 'seq (unique per investigation)', 'text, asked_by, asked_at',
        'status'], False),
    'plans': (2, 1, 'orch', [
        'PK id', 'FK question_id (unique)', 'status, semantic_signature', 'hop_count',
        'diff_from_prior JSON'], False),
    'plan_steps': (2, 2, 'orch', [
        'PK id', 'FK plan_id, FK source_id', 'step_key (unique per plan)', 'step_type, declared_grain',
        'depends_on uuid[]', 'binding_ids uuid[]'], False),

    'answers': (3, 0, 'pres', [
        'PK id', 'FK question_id (unique)', 'FK least_certain_hop_id', 'heading, review_state',
        'created_at'], False),
    'sign_offs': (3, 1, 'data', [
        'PK id', 'FK answer_id (unique)', 'reviewed_by, reviewed_at', 'note'], False),
    'hops': (3, 2, 'verify', [
        'PK id', 'FK step_id (unique)', 'FK replay_of (self)', 'title, statement_issued',
        'rows_in, rows_out', 'grain_declared, grain_actual', 'attempts (SQL repairs)',
        'output_ref, sample_rows JSON'], False),

    'answer_blocks': (4, 0, 'pres', [
        'PK id', 'FK answer_id', 'position (unique per answer)', 'kind', 'content JSON'], False),
    'citations': (4, 1, 'verify', [
        'PK id', 'FK block_id, FK hop_id', 'marker, span'], False),
    'hop_verdicts': (4, 2, 'verify', [
        'PK id', 'FK hop_id', 'attempt (unique per hop)', 'status, doubt_reasons JSON',
        'verifier_version', 'started_at, finished_at'], False),
    'check_results': (5, 2, 'verify', [
        'PK id', 'FK verdict_id', 'kind, status', 'expected, observed, tolerance',
        'sql_text, sql_hash, params', 'elapsed_ms, reason'], False),
    'eval_item_results': (0, 4, 'verify', [
        'PK id', 'FK run_id', 'question_id, trial (unique per run)', 'correct, any_fail, asked',
        'retries, tokens, cost_usd'], False),
    'eval_runs': (1, 4, 'verify', [
        'PK id', 'suite, mode (replay | live | study)', 'trials_k, git_sha, model_id',
        'dataset_version', 'started_at, metrics JSON'], False),
    'seeded_defect_results': (2, 4, 'verify', [
        'PK id', 'FK run_id', 'defect_id, defect_class', 'caught_by text[]', 'escaped (generated)'], False),

    'overrides': (3, 3, 'data', [
        'PK id', 'FK hop_id', 'overridden_by, annotation_type', 'rationale',
        'persisted_to_bindings'], False),
    'model_cards': (4, 3, 'agent', [
        '«planned»', 'PK id', 'FK hop_id (unique)', 'target, features JSON',
        'not_attempted JSON', 'metric_with_uncertainty'], True),
}
FILES = {  # file-based stores, not tables
    'audit_log': (0, 3, 'audit_log.jsonl', 'file, not a table: append-only'),
    'artifacts': (2, 3, 'Artifact Store', 'files keyed by hops.output_ref'),
}

# (a, b, a_anchor, b_anchor, a_card, b_card)
RELS = [
    ('organisations', 'bindings', ('t', .5), ('b', .5), '1', 'N'),
    ('organisations', 'sources', ('b', .5), ('t', .5), '1', 'N'),
    ('organisations', 'investigations', ('r', .3), ('l', .8), '1', 'N'),
    ('investigations', 'questions', ('r', 50), ('l', 50), '1', 'N'),
    ('questions', 'answers', ('r', 50), ('l', 50), '1', '1'),
    ('answers', 'answer_blocks', ('r', 50), ('l', 50), '1', 'N'),
    ('questions', 'plans', ('b', .5), ('t', .5), '1', '1'),
    ('plans', 'plan_approvals', ('l', 50), ('r', 50), '1', '1'),
    ('plans', 'plan_steps', ('b', .5), ('t', .5), '1', 'N'),
    ('answers', 'sign_offs', ('b', .5), ('t', .5), '1', '1'),
    ('answer_blocks', 'citations', ('b', .5), ('t', .5), '1', 'N'),
    ('citations', 'hops', ('b', .3), ('t', .8), 'N', '1'),
    ('plan_steps', 'hops', ('r', 50), ('l', 50), '1', '1'),
    ('hops', 'hop_verdicts', ('r', 50), ('l', 50), '1', 'N'),
    ('hop_verdicts', 'check_results', ('r', 50), ('l', 50), '1', 'N'),
    ('eval_runs', 'eval_item_results', ('l', 50), ('r', 50), '1', 'N'),
    ('eval_runs', 'seeded_defect_results', ('r', 50), ('l', 50), '1', 'N'),
    ('hops', 'overrides', ('b', .5), ('t', .5), '1', 'N'),
    ('hops', 'model_cards', ('r', .9), ('l', .3), '1', '1'),
    ('mapping_proposals', 'sources', ('l', 50), ('r', 50), 'N', '2'),
    ('sources', 'audit_log', ('b', .5), ('t', .5), '1', 'N'),
    ('hops', 'artifacts', ('l', .9), ('r', .4), '1', '1'),
]


def build():
    rows = {}
    for t in TABLES.values():
        rows.setdefault(t[1], []).append(box_height(t[3], []))
    rows[3].append(REF_H)
    rows.setdefault(4, [])
    row_y, y = {}, 70
    for r in sorted(rows):
        row_y[r] = y
        y += max(rows[r]) + 64
    footer_y = y - 24
    d = Drawer(WIDTH, footer_y + 96, STEM, 'InsightPilot - database ER diagram')
    d.text(WIDTH/2, 38, 'Database ER diagram - Application Store, PostgreSQL 16 (one database per deployment)', 21, 'b', '#1f2937', 'middle', max_w=WIDTH-40)

    for n, (col, row, tier, cols, dashed) in TABLES.items():
        d.geo[n] = (COLS[col], row_y[row], BOX_W, box_height(cols, []))
    for n, (col, row, title, note) in FILES.items():
        d.geo[n] = (COLS[col], row_y[row], BOX_W, REF_H)
    for a, b, aa, ba, ac, bc in RELS:
        d.edge(a, b, aa, ba, ac, bc, '', 'assoc')

    for n, (col, row, tier, cols, dashed) in TABLES.items():
        x, yy, w, _ = d.geo[n]
        d.class_box(n, x, yy, w, tier, n, cols, [], dashed)
    for n, (col, row, title, note) in FILES.items():
        x, yy, w, _ = d.geo[n]
        d.ref_box(n, x, yy, w, title, note)

    d.legend(COLS[5], row_y[0], BOX_W, [
        ('solid', 'table (CMPE 295A)'), ('dashed', 'planned table (CMPE 295B)'),
        ('ref', 'file-based store, not a table'), ('assoc', 'foreign key, 1 / N at each end'),
    ])

    fy = footer_y + 14
    for i, line in enumerate([
        'All tables are scoped to the single organisation of the deployment. plan_steps.depends_on holds the DAG edges and plan_steps.binding_ids the bindings a step uses (uuid arrays).',
        'Unique: bindings (org_id, term_normalised, kind); questions (investigation_id, seq); plan_steps (plan_id, step_key); answer_blocks (answer_id, position); hop_verdicts (hop_id, attempt); eval_item_results (run_id, question_id, trial).',
        'Verdicts are never updated: a re-run inserts a new attempt. Full result sets are not stored: hops keep counts, grain and a sample; outputs live in the Artifact Store. Evaluation tables are written by the harness.',
    ]):
        d.text(WIDTH/2, fy + i*20, line, 11.5, 'n' if i < 2 else 'i', '#64748b', 'middle', max_w=WIDTH-40)
    d.save()
    print(f'Built {STEM}: {len(TABLES)} tables, {len(FILES)} file stores, {len(RELS)} relationships')


if __name__ == '__main__':
    build()
