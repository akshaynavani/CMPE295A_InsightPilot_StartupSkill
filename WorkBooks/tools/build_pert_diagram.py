#!/usr/bin/env python3
"""Chapter 9 PERT charts for CMPE 295A and CMPE 295B (SVG, PDF, PNG).

Each task is a box (name, owner and sprint, status) placed in a column by dependency depth;
arrows are dependencies; the critical path is drawn in red. Done tasks use the status
diagram's green; milestones are red. Drawn with the shared helpers in uml_common.py.
Task status and dates follow Chapter 8 (Table 18) and the Workbook 2 Gantt chart.
"""
from uml_common import Drawer

DONE_FILL, TODO_FILL, MS_FILL = '#e3f1e4', '#ffffff', '#fdecec'
RED, GREY, GREEN = '#c0392b', '#64748b', '#2e7d32'
BOX_W, BOX_H, COL_GAP, ROW_GAP = 188, 66, 40, 22

# node: id -> (name, owner/sprint line, status line, kind)   kind: done | todo | ms
PERT_A = {
    'A': ('Repository, CI, Docker Compose', 'AN · S1', '✓ Oct 4', 'done'),
    'B': ('PostgreSQL connector (SP-1)', 'AN · S1', '✓ Oct 4', 'done'),
    'C': ('CSV / Excel connector (SP-2)', 'AN · S2', '✓ Oct 18', 'done'),
    'D': ('Plan synthesiser (SP-3)', 'AK · S2', '✓ Oct 18', 'done'),
    'E': ('Workspace + plan review', 'SZ · S1–S2', '✓ Oct 18', 'done'),
    'F': ('Orchestrator dispatch', 'AK · S4', '✓ Nov 10', 'done'),
    'G': ('Reconciler profiling', 'AN, PS · S4', '✓ Nov 10', 'done'),
    'H': ('Model client + runtime env', 'AK · S4', 'Nov 9–15', 'todo'),
    'G2': ('Reconciler proposals', 'PS · S4', 'Nov 13–22', 'todo'),
    'I': ('Question set + seeded errors', 'PS · S4', 'Nov 9–18', 'todo'),
    'M': ('Application + binding store', 'AN · S4', 'Nov 9–17', 'todo'),
    'O': ('Semantic resolver', 'AK · S4', 'Nov 13–22', 'todo'),
    'Q': ('Append-only audit log', 'SZ · S4', 'Nov 9–17', 'todo'),
    'J': ('Fetch agent', 'AN · S4', 'Nov 13–18', 'todo'),
    'K': ('Hop verifier (SP-4)', 'PS · S4', 'Nov 14–19', 'todo'),
    'L': ('Lineage recorder (SP-5)', 'SZ · S4', 'Nov 16–22', 'todo'),
    'N': ('Harness in CI (SP-6)', 'PS · S4', 'Nov 22', 'todo'),
    'P': ('Analytics agent', 'PS · S5', 'Nov 23–Dec 6', 'todo'),
    'R': ('Ambiguity interception', 'AK · S5', 'Nov 23–Dec 6', 'todo'),
    'S': ('Export + sign-off state', 'SZ · S5', 'Nov 23–Dec 6', 'todo'),
    'T': ('Quickstart', 'AN · S5', 'Nov 23–Dec 6', 'todo'),
    'U': ('Silent-error rate, coverage', 'PS · S5', 'Nov 23–Dec 6', 'todo'),
    'M2': ('◆ M2 Measurement', 'Nov 22 (was Nov 8)', '', 'ms'),
    'M3': ('◆ M3 Narrow path', 'Dec 6', '', 'ms'),
    'M4': ('◆ M4 Evidence', 'Study Dec 7–11 · Dec 11', '', 'ms'),
}
EDGES_A = [('B', 'D'), ('D', 'E'), ('D', 'F'), ('B', 'G'), ('C', 'G'),
           ('A', 'T'), ('B', 'M'), ('B', 'Q'), ('D', 'O'),
           ('F', 'J'), ('H', 'J'), ('A', 'J'), ('J', 'K'), ('K', 'L'), ('M', 'L'),
           ('I', 'N'), ('K', 'N'), ('N', 'M2'),
           ('J', 'P'), ('O', 'R'), ('L', 'S'), ('Q', 'S'), ('E', 'S'), ('N', 'U'),
           ('S', 'M3'), ('P', 'M3'), ('R', 'M3'), ('G', 'G2'), ('G2', 'M3'), ('T', 'M3'),
           ('M3', 'M4'), ('U', 'M4')]
CRIT_A = ['B', 'D', 'F', 'J', 'K', 'L', 'S', 'M3', 'M4']

PERT_B = {
    'START': ('◆ CMPE 295A complete', 'Dec 11, 2026', '', 'ms'),
    'b1': ('REST JSON connector', 'AN · S6', '', 'todo'),
    'b2': ('Replanning on invalidation', 'AK · S6', '', 'todo'),
    'b3': ('Verifier coverage expansion', 'PS · S6', '', 'todo'),
    'b4': ('Review queue, history', 'SZ · S6', '', 'todo'),
    'c1': ('dbt semantic layer', 'AN · S7', '', 'todo'),
    'c2': ('Hop override re-flow', 'AK · S7', '', 'todo'),
    'c3': ('Cost by retry count', 'PS · S7', '', 'todo'),
    'c4': ('Shared investigation link', 'SZ · S7', '', 'todo'),
    'd1': ('Permissions, schema-only', 'AN · S8', '', 'todo'),
    'd2': ('Plan caching, pinned bindings', 'AK · S8', '', 'todo'),
    'd3': ('Modelling-step evaluation', 'PS · S8', '', 'todo'),
    'd4': ('Visualization agent', 'SZ · S8', '', 'todo'),
    'M5': ('◆ M5 Beta', 'Mar 7, 2027', '', 'ms'),
    'e1': ('Performance + cost benchmarks', 'AN · S9', '', 'todo'),
    'e2': ('Time-boxed ML agent', 'AK · S9', '', 'todo'),
    'e3': ('Robustness tests', 'PS · S9', '', 'todo'),
    'e4': ('Model card screen', 'SZ · S9', '', 'todo'),
    'f1': ('Load and scale tests', 'AN · S10', '', 'todo'),
    'f2': ('Accuracy ablations', 'AK · S10', '', 'todo'),
    'f3': ('Usability study', 'PS · S10', '', 'todo'),
    'f4': ('Accessibility, polish', 'SZ · S10', '', 'todo'),
    'g': ('Results and paper draft', 'Whole team · S11', '', 'todo'),
    'h': ('Final release, demo, Expo', 'Whole team · S12', '', 'todo'),
    'M6': ('◆ M6 Final release', 'May 7, 2027', '', 'ms'),
}
EDGES_B = ([('START', x) for x in ('b1', 'b2', 'b3', 'b4')] +
           [('b1', 'c1'), ('b2', 'c2'), ('b3', 'c3'), ('b4', 'c4'),
            ('c1', 'd1'), ('c2', 'd2'), ('c3', 'd3'), ('c4', 'd4')] +
           [(x, 'M5') for x in ('d1', 'd2', 'd3', 'd4')] +
           [('M5', x) for x in ('e1', 'e2', 'e3', 'e4')] +
           [('e1', 'f1'), ('e2', 'f2'), ('e3', 'f3'), ('e4', 'f4')] +
           [(x, 'g') for x in ('f1', 'f2', 'f3', 'f4')] + [('g', 'h'), ('h', 'M6')])
CRIT_B = ['M5', 'g', 'h', 'M6']   # member streams are parallel and equal, so only the shared chain is critical


def layout(nodes, edges):
    """Column = longest dependency depth; row = order of first appearance in that column."""
    depth = {n: 0 for n in nodes}
    for _ in range(len(nodes)):
        for a, b in edges:
            depth[b] = max(depth[b], depth[a] + 1)
    cols = {}
    for n in nodes:
        cols.setdefault(depth[n], []).append(n)
    return depth, cols


def draw(nodes, edges, critical, stem, title, subtitle, footer):
    depth, cols = layout(nodes, edges)
    ncol = max(cols) + 1
    nrow = max(len(v) for v in cols.values())
    width = 40 + ncol * BOX_W + (ncol - 1) * COL_GAP
    height = 110 + nrow * BOX_H + (nrow - 1) * ROW_GAP + 90
    d = Drawer(width, height, stem, title)
    d.text(width / 2, 34, title, 21, 'b', '#1f2937', 'middle')
    d.text(width / 2, 58, subtitle, 12.5, 'n', '#334155', 'middle')
    top = 84
    area_h = nrow * BOX_H + (nrow - 1) * ROW_GAP
    for c, ids in cols.items():
        col_h = len(ids) * BOX_H + (len(ids) - 1) * ROW_GAP
        y0 = top + (area_h - col_h) / 2
        for r, n in enumerate(ids):
            d.geo[n] = (20 + c * (BOX_W + COL_GAP), y0 + r * (BOX_H + ROW_GAP), BOX_W, BOX_H)
    crit_edges = set(zip(critical, critical[1:]))
    # edges first, critical ones last so they sit on top
    for a, b in sorted(edges, key=lambda e: e in crit_edges):
        ax, ay, aw, ah = d.geo[a]
        bx, by, bw, bh = d.geo[b]
        p1, p2 = (ax + aw, ay + ah / 2), (bx, by + bh / 2)
        crit = (a, b) in crit_edges
        colour = RED if crit else '#94a3b8'
        pts = [p1, ((p1[0] + p2[0]) / 2, p1[1]), ((p1[0] + p2[0]) / 2, p2[1]), p2]
        from reportlab.lib.colors import HexColor
        d.pdf.setStrokeColor(HexColor(colour)); d.pdf.setLineWidth(2.4 if crit else 1.2)
        path = d.pdf.beginPath(); path.moveTo(pts[0][0], d.H - pts[0][1])
        for px, py in pts[1:]:
            path.lineTo(px, d.H - py)
        d.pdf.drawPath(path, stroke=1, fill=0)
        d.svg.append('<polyline points="' + ' '.join(f'{px:.1f},{py:.1f}' for px, py in pts) +
                     f'" fill="none" stroke="{colour}" stroke-width="{2.4 if crit else 1.2}"/>')
        d.poly([p2, (p2[0] - 9, p2[1] - 5), (p2[0] - 9, p2[1] + 5)], colour)
    for n, (name, line1, line2, kind) in nodes.items():
        x, y, w, h = d.geo[n]
        fill = {'done': DONE_FILL, 'todo': TODO_FILL, 'ms': MS_FILL}[kind]
        border = RED if n in critical else (GREEN if kind == 'done' else GREY)
        d.rect(x, y, w, h, border, fill, radius=4, lw=2.4 if n in critical else 1.3)
        colour = RED if kind == 'ms' else '#1f2937'
        if line2:
            d.text(x + w / 2, y + 21, name, 12.5, 'b', colour, 'middle', max_w=w - 12)
            d.text(x + w / 2, y + 40, line1, 11, 'n', '#475569', 'middle', max_w=w - 12)
            d.text(x + w / 2, y + 57, line2, 11, 'b', GREEN if kind == 'done' else '#334155', 'middle', max_w=w - 12)
        else:
            d.text(x + w / 2, y + 28, name, 12.5, 'b', colour, 'middle', max_w=w - 12)
            d.text(x + w / 2, y + 48, line1, 11, 'n', '#475569', 'middle', max_w=w - 12)
    ly = top + area_h + 34
    lx = 20
    for label, fill, border, lw in [('done (date)', DONE_FILL, GREEN, 1.3), ('to do (planned window)', TODO_FILL, GREY, 1.3),
                                    ('critical path', '#ffffff', RED, 2.4), ('milestone', MS_FILL, GREY, 1.3)]:
        d.rect(lx, ly - 12, 30, 16, border, fill, radius=2, lw=lw)
        d.text(lx + 38, ly + 1, label, 11.5, 'n', '#334155', 'start')
        lx += 38 + len(label) * 7 + 40
    d.text(20, ly + 30, footer, 11, 'i', '#64748b', 'start', max_w=width - 40)
    d.save()
    print(f'Built {stem}: {len(nodes)} nodes, {len(edges)} dependencies, critical path {len(critical)} nodes')


if __name__ == '__main__':
    draw(PERT_A, EDGES_A, CRIT_A, 'ch9_pert_295a', 'PERT chart for CMPE 295A (Fall 2026)',
         'Task dependencies and critical path to milestones M2, M3 and M4 · status as of November 12, 2026',
         'Columns follow dependency order, not dates. Critical path: PostgreSQL connector → plan synthesiser → orchestrator dispatch → fetch agent → hop verifier → lineage recorder → export and sign-off → M3 → study → M4. The model client must land before the fetch agent.')
    draw(PERT_B, EDGES_B, CRIT_B, 'ch9_pert_295b', 'PERT chart for CMPE 295B (Spring 2027)',
         'Task dependencies and critical path to milestones M5 Beta and M6 Final release',
         'The four member streams run in parallel with equal duration, so a slip in any one of them delays M5 or the paper; the critical path is the shared chain from all S10 work through the paper and release to M6.')
