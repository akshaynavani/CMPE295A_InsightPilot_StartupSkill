#!/usr/bin/env python3
"""Figure 5 - UML class diagram of the answer presentation (what the analyst sees).

Expands Answer / AnswerBlock from Figure 3 into the blocks rendered in the Investigation
Workspace: insight text with citations, the data table, the chart [295B] and the doubt
block. Sources: product/ux_spec.md section 6 (answer: established facts, doubt block,
chart, each fact links to its hop), D01 (compose answer), D05 (prose on the small model).
"""
from uml_common import Drawer, box_height, LINE, HEADER_H

STEM = 'ch6_class_answer'
BOX_W, GAP = 218, 96
COLS = [20 + i*(BOX_W+GAP) for i in range(5)]
WIDTH = COLS[-1] + BOX_W + 20
REF_H = HEADER_H + 24

# name: (col, row, tier, title, attributes, methods, dashed)
CLASSES = {
    'Answer': (1, 0, 'pres', 'Answer', [
        'heading: str', 'review_state: ReviewState', 'least_certain_hop: Hop', 'created_at: UTC'],
        ['+ add_block(block)', '+ request_review()', '+ export()'], False),
    'AnswerBlock': (1, 1, 'pres', '«abstract» AnswerBlock', [
        'position: int', 'kind: TEXT | TABLE | CHART | DOUBT'],
        ['+ render(): View'], False),
    'Citation': (4, 1, 'verify', 'Citation', [
        'marker: int  (¹ ² ³)', 'span: text range', 'hop: Hop'],
        ['+ open_hop()'], False),
    'TextBlock': (0, 2, 'pres', 'TextBlock', [
        'markdown: str', 'role: SUMMARY | INSIGHTS', 'written by: small model',
        'only numbers from verified hops'],
        ['+ citations(): Citation[]'], False),
    'TableBlock': (1, 2, 'pres', 'TableBlock', [
        'columns: Column[]', 'rows_ref: Hop.output_ref', 'row_count: int', 'page_size: int'],
        ['+ page(n)', '+ download()'], False),
    'ChartBlock': (2, 2, 'agent', '«planned» ChartBlock', [
        'spec: ChartSpec', 'source_hop: Hop', 'made by: VisualizationAgent'],
        ['+ as_table()', '+ download()', '+ edit_spec()'], True),
    'DoubtBlock': (3, 2, 'verify', 'DoubtBlock', [
        'severity: Severity', 'hop: Hop', 'check: CheckKind', 'reason: str'],
        ['+ inspect()'], False),
    'ChartSpec': (2, 3, 'agent', '«planned» ChartSpec', [
        'chart_type: ChartType', 'x / y: column', 'color_by: column', 'title: str',
        'rationale: str'], [], True),
}
REFS = {
    'Question': (0, 0, 'Question', 'see Figure 3'),
    'SignOff': (2, 0, 'SignOff', 'see Figure 3'),
    'Hop': (4, 2, 'Hop', 'see Figure 3'),
}

EDGES = [
    ('Question', 'Answer', ('r', 40), ('l', 40), '1', '0..1', 'answered by', 'assoc'),
    ('Answer', 'SignOff', ('r', 40), ('l', 40), '1', '0..1', 'reviewed by', 'assoc'),
    ('Answer', 'AnswerBlock', ('b', .5), ('t', .5), '1', '1..*', 'ordered by position', 'comp'),
    ('AnswerBlock', 'Citation', ('r', 50), ('l', 50), '1', '0..*', 'cites', 'comp'),
    ('Citation', 'Hop', ('b', .5), ('t', .5), '0..*', '1', 'points to', 'assoc'),
    ('DoubtBlock', 'Hop', ('r', 26), ('l', 26), '0..*', '1', 'about', 'assoc'),
    ('ChartBlock', 'ChartSpec', ('b', .5), ('t', .5), '1', '1', 'drawn from', 'comp'),
]
CHILDREN = ['TextBlock', 'TableBlock', 'ChartBlock', 'DoubtBlock']


def build():
    rows = {}
    for c in CLASSES.values():
        rows.setdefault(c[1], []).append(box_height(c[4], c[5]))
    rows[0].append(REF_H)
    rows[0].append(34 + 26*5)  # legend
    row_y, y = {}, 70
    for r in sorted(rows):
        row_y[r] = y
        y += max(rows[r]) + (110 if r == 1 else 78)   # room for the generalization tree
    footer_y = y - 30
    d = Drawer(WIDTH, footer_y + 96, STEM, 'InsightPilot - UML class diagram of the answer presentation')
    d.text(WIDTH/2, 38, 'UML class diagram - answer presentation (what the analyst sees)', 22, 'b', '#1f2937', 'middle')

    for n, (col, row, tier, title, attrs, methods, dashed) in CLASSES.items():
        d.geo[n] = (COLS[col], row_y[row], BOX_W, box_height(attrs, methods))
    for n, (col, row, title, note) in REFS.items():
        d.geo[n] = (COLS[col], row_y[row], BOX_W, REF_H)
    for e in EDGES:
        d.edge(*e)

    # Generalization tree: each block subclass inherits from AnswerBlock (hollow triangle).
    px, py, pw, ph = d.geo['AnswerBlock']
    apex = (px + pw/2, py + ph)
    base_y = apex[1] + 14
    bus_y = base_y + 24
    tri = [apex, (apex[0]-9, base_y), (apex[0]+9, base_y)]
    d.seg([(apex[0], base_y), (apex[0], bus_y)])
    xs = []
    for c in CHILDREN:
        cx_, cy_, cw_, _ = d.geo[c]
        xs.append(cx_ + cw_/2)
        d.seg([(cx_ + cw_/2, cy_), (cx_ + cw_/2, bus_y)], dashed=False)
    d.seg([(min(xs), bus_y), (max(xs), bus_y)])
    d.poly(tri, '#ffffff')
    d.seg(tri + [tri[0]])
    d.text(apex[0] + 16, base_y + 4, 'is a', 11, 'i', '#64748b', 'start')

    for n, (col, row, tier, title, attrs, methods, dashed) in CLASSES.items():
        x, yy, w, _ = d.geo[n]
        d.class_box(n, x, yy, w, tier, title, attrs, methods, dashed)
    for n, (col, row, title, note) in REFS.items():
        x, yy, w, _ = d.geo[n]
        d.ref_box(n, x, yy, w, title, note)

    lx, ly = COLS[4], row_y[0]
    d.legend(lx, ly, BOX_W, [
        ('solid', 'CMPE 295A scope'), ('dashed', 'CMPE 295B scope'),
        ('ref', 'domain class from Figure 3'), ('comp', 'composition (whole ◆ part)'),
        ('assoc', 'association'),
    ])
    # Generalization sample, drawn by hand under the legend.
    gy = ly + 34 + 26*5 + 22
    d.seg([(lx+12, gy), (lx+36, gy)])
    tri = [(lx+44, gy), (lx+35, gy-6), (lx+35, gy+6)]
    d.poly(tri, '#ffffff'); d.seg(tri + [tri[0]])
    d.text(lx+52, gy+4, 'generalization (subclass to parent)', 11, 'n', '#1f2937', 'start', max_w=BOX_W-60)

    fy = footer_y + 18
    d.text(WIDTH/2, fy, 'Severity = WARN | FAIL     ChartType = BAR | LINE | SCATTER | AREA | PIE     ReviewState = UNREVIEWED | REVIEWED', 12, 'n', '#64748b', 'middle', max_w=WIDTH-40)
    d.text(WIDTH/2, fy+22, 'Built by Orchestrator.compose_answer() (Figure 4): TextBlock sentences by the small model from verified hops only; TableBlock and DoubtBlock copied from Hop output and CheckResults.', 11, 'i', '#64748b', 'middle', max_w=WIDTH-40)
    d.text(WIDTH/2, fy+40, 'Every ¹ marker is a Citation to the Hop that produced the number; opening it shows that hop’s SQL, row counts and checks. ChartBlock is produced by the VisualizationAgent [295B].', 11, 'i', '#64748b', 'middle', max_w=WIDTH-40)
    d.save()
    print(f'Built {STEM}: {len(CLASSES)} classes, {len(REFS)} referenced')


if __name__ == '__main__':
    build()
