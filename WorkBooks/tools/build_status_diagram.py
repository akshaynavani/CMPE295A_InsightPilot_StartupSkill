#!/usr/bin/env python3
"""Build the Workbook 2 as-built status diagram (SVG, PDF, PNG).

It extends Workbook 1 Figure 1 (build_architecture_diagram.py) with the same
tiers, cards, colours and fonts, and adds the status treatment of the AI Agent
Marketplace Workbook 2, Figure 2: a status fill per card, a status badge under
the component name, and a legend.
Requires reportlab and PyMuPDF. No network or application dependencies.
"""
from pathlib import Path
from html import escape
import math
import fitz
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets'
STEM = 'ch6_status'
AS_OF = 'November 12, 2026'

# Status: fill, badge colour, badge label.
DONE, PARTIAL, DESIGNED, PLANNED = 'done', 'partial', 'designed', 'planned'
STATUS = {
    DONE: ('#e3f1e4', '#2e7d32', 'DONE'),
    PARTIAL: ('#e4edf8', '#1f5fa8', 'PARTIAL'),
    DESIGNED: ('#fff3d9', '#8a5a00', 'DESIGNED'),
    PLANNED: ('#ffffff', '#6b7280', 'PLANNED'),
}

# Same tiers and cards as Workbook 1 Figure 1.
# Card: (name, function lines, technology line, status, status note).
TIERS = [
    ('PRESENTATION TIER', '#3974bb', [
        ('Investigation Workspace', ['Ask questions; follow-ups inherit context'], 'React · TypeScript · FastAPI', DONE, None),
        ('Plan Review & Approval', ['Clarify ambiguity; edit and approve plans'], 'React · typed plan DAG', DONE, None),
        ('Lineage Inspector & Export', ['Inspect / replay hops; analyst sign-off'], 'React · self-contained artifact', DESIGNED, 'Spec: UX screens 7 and 9'),
    ]),
    ('ORCHESTRATION TIER: CUSTOM PYTHON 3.12', '#855bc0', [
        ('Semantic Resolver', ['Bind terms to columns / grain', 'Halt and ask when ambiguous'], 'BM25 · embeddings · rank fusion', DESIGNED, 'Spec: deep dive 1'),
        ('Plan Synthesiser', ['Generate typed DAG; validate', 'sources, inputs and cycles'], 'Python · constrained generation', DONE, None),
        ('Orchestrator & Replanner', ['Route all handoffs; own state', 'Budget / retry caps; replan [295B]'], 'Custom Python · DAG execution', DONE, None),
        ('Model Client', ['Plan / SQL / prose model calls', 'Schema-only or filtered samples'], 'Provider-agnostic HTTPS API', DESIGNED, 'Spec: D05'),
    ]),
    ('SPECIALIST AGENT TIER: ALL TASKS AND RESULTS ROUTED THROUGH ORCHESTRATOR', '#319763', [
        ('Fetch / Integration Agent', ['Generate / repair queries', 'Retrieve and prepare data'], 'Python · SQLAlchemy · psycopg', DESIGNED, 'Spec: deep dive 3'),
        ('Analytics Agent', ['Joins, KPIs, comparisons', 'Trends and aggregation'], 'SQL · pandas', DESIGNED, 'Spec: D03 handoff contract'),
        ('Visualization Agent [295B]', ['Choose charts; return chart', 'specification and rationale'], 'Python · chart rendering', PLANNED, 'CMPE 295B'),
        ('ML Agent [295B]', ['Time-boxed baseline models', 'Model card + uncertainty'], 'scikit-learn · LightGBM', PLANNED, 'CMPE 295B'),
    ]),
    ('VERIFICATION & LINEAGE TIER: CHECKS USE SQL / COMPUTE, NEVER LLM SELF-CRITIQUE', '#c47c20', [
        ('Hop Verifier', ['Counts, grain, coverage, nulls', 'Totals and type / range checks'], 'Independent SQL · local compute', DESIGNED, 'Spec: deep dive 4'),
        ('Cross-source Reconciler', ['Profile join keys and overlap', 'Propose mappings for approval'], 'DuckDB SQL · pandas', PARTIAL, 'Profiling done Nov 10; proposals S4'),
        ('Lineage Recorder & Replayer', ['Record query, grain, checks and skips', 'Replay one hop; report differences'], 'Python · PostgreSQL · local files', DESIGNED, 'Spec: deep dive 6 · D04'),
    ]),
    ('INTEGRATION TIER: READ-ONLY SOURCES; SEMANTIC DEFINITIONS TAKE PRECEDENCE', '#c94e67', [
        ('PostgreSQL Connector', ['Describe, sample, execute, profile', 'Inherit source read permissions'], 'SQLAlchemy · psycopg', DONE, None),
        ('CSV / Excel Connector', ['Query uploaded files', 'Infer schema; profile without ETL'], 'DuckDB · Python', DONE, None),
        ('REST JSON Connector [295B]', ['Third source type', 'Read-only API access'], 'Python · HTTP / JSON', PLANNED, 'CMPE 295B'),
        ('Semantic Layer [295B]', ['Definitions override inference', 'dbt semantic layer'], 'Separate semantic interface', PLANNED, 'CMPE 295B'),
    ]),
    ('DATA, AUDIT & EVALUATION TIER', '#64748b', [
        ('Application Store', ['Org bindings, plans, investigations', 'Hop lineage, overrides, sign-off'], 'PostgreSQL 16', DESIGNED, 'Spec: D04 schema'),
        ('Artifact Store', ['Local step outputs and exports', 'Recorded statements / parameters'], 'Local filesystem', DESIGNED, 'Spec: Chapter 5'),
        ('Append-only Audit Log', ['Actor, source, statement, timestamp', 'Readable without application'], 'JSONL · local filesystem', DESIGNED, 'Spec: D06 · UX screen 12'),
        ('Offline Evaluation Harness', ['Ground truth + seeded errors', 'Accuracy and verifier coverage'], 'pytest · question-set fixtures', DESIGNED, 'Spec: D08'),
    ]),
]

# Geometry: Figure 1 plus room for the status badge in each card.
CARD_H, TIER_H, TIER_STEP, TIER_Y0 = 116, 160, 192, 114
BOUNDARY_H = TIER_Y0 + 5*TIER_STEP + TIER_H + 20 - 81
WIDTH = 1440
HEIGHT = 81 + BOUNDARY_H + 150


def build():
    OUT.mkdir(exist_ok=True)
    title = 'InsightPilot: As-built Status of the System Architecture'
    pdf = canvas.Canvas(str(OUT / f'{STEM}.pdf'), pagesize=(WIDTH, HEIGHT))
    pdf.setTitle(title)
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">',
           f'<title>{escape(title)}</title>',
           '<desc>Workbook 1 Figure 1 with each component marked done, designed or planned for CMPE 295B.</desc>',
           '<rect width="100%" height="100%" fill="white"/>']

    def rect(x, y, w, h, stroke, fill='#ffffff', dashed=False, radius=6, lw=1.4):
        pdf.setStrokeColor(HexColor(stroke)); pdf.setFillColor(HexColor(fill))
        pdf.setLineWidth(lw); pdf.setDash(6, 4) if dashed else pdf.setDash()
        pdf.roundRect(x, HEIGHT-y-h, w, h, radius, stroke=1 if stroke else 0, fill=1)
        svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="{lw}"' + (' stroke-dasharray="6 4"' if dashed else '') + '/>')
        pdf.setDash()

    def text(x, y, value, size=14, bold=False, color='#334155', align='middle'):
        pdf.setFillColor(HexColor(color)); pdf.setFont('Helvetica-Bold' if bold else 'Helvetica', size)
        (pdf.drawCentredString if align == 'middle' else pdf.drawString)(x, HEIGHT-y, value)
        svg.append(f'<text x="{x}" y="{y}" text-anchor="{"middle" if align == "middle" else "start"}" font-family="Arial, Helvetica, sans-serif" font-size="{size}" font-weight="{700 if bold else 400}" fill="{color}">{escape(value)}</text>')

    def line(x1, y1, x2, y2, dashed=False, arrow=False):
        color = '#64748b'
        pdf.setStrokeColor(HexColor(color)); pdf.setLineWidth(1.5)
        pdf.setDash(4, 3) if dashed else pdf.setDash()
        pdf.line(x1, HEIGHT-y1, x2, HEIGHT-y2)
        svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="1.5"' + (' stroke-dasharray="4 3"' if dashed else '') + '/>')
        pdf.setDash()
        if arrow:
            angle = math.atan2(y2-y1, x2-x1)
            points = [(x2, y2)] + [(x2-8*math.cos(angle+a), y2-8*math.sin(angle+a)) for a in [-.45, .45]]
            pdf.setFillColor(HexColor(color)); path = pdf.beginPath()
            path.moveTo(points[0][0], HEIGHT-points[0][1])
            for px, py in points[1:]:
                path.lineTo(px, HEIGHT-py)
            path.close(); pdf.drawPath(path, stroke=0, fill=1)
            svg.append('<polygon points="' + ' '.join(f'{px},{py}' for px, py in points) + f'" fill="{color}"/>')

    def badge(cx, y, status):
        _, colour, label = STATUS[status]
        w = 9 + len(label)*7.2
        rect(cx-w/2, y, w, 16, colour, colour, radius=2, lw=0.8)
        text(cx, y+12, label, 10, True, '#ffffff')

    counts = {DONE: 0, PARTIAL: 0, DESIGNED: 0, PLANNED: 0}
    text(WIDTH/2, 31, title, 25, True)
    text(WIDTH/2, 56, f'Status as of {AS_OF} · extends Figure 1 · CMPE 295A + 295B scope', 15)
    rect(18, 81, 1147, BOUNDARY_H, '#94a3b8', '#ffffff')
    text(36, 102, 'DEPLOYMENT: ONE ORGANISATION · SELF-HOSTED / DOCKER COMPOSE', 14, True, align='start')
    x, width = 35, 1113
    gaps = [
        ('question + context / analyst-approved plan', 'clarification / plan / answer + evidence'),
        ('typed tasks + input references + budget', 'results + declared grain + lineage'),
        ('per-hop outputs / verification evidence', 'pass / warning / failure to orchestrator'),
        ('independent SQL / profiles over sources', 'schema / row counts / coverage / grain'),
        ('durable bindings, state, lineage and audit', 'replay metadata / evaluation outcomes'),
    ]
    tints = ['#eff6ff', '#f5f3ff', '#f0fdf4', '#fff7ed', '#fff1f2', '#f1f5f9']
    for i, (tier_title, color, cards) in enumerate(TIERS):
        y = TIER_Y0 + i*TIER_STEP
        rect(x, y, width, TIER_H, color, tints[i])
        text(x+12, y+21, tier_title, 13, True, color, align='start')
        gap = 14; cw = (width-28-gap*(len(cards)-1))/len(cards)
        for j, (name, functions, technology, status, note) in enumerate(cards):
            counts[status] += 1
            cx = x+14+j*(cw+gap); cy = y+33
            rect(cx, cy, cw, CARD_H, color, STATUS[status][0], status == PLANNED, 3)
            mid = cx+cw/2
            text(mid, cy+19, name, 14, True)
            badge(mid, cy+26, status)
            fy = cy+58 if len(functions) == 2 else cy+64
            for k, f in enumerate(functions):
                text(mid, fy+k*15, f, 12.5)
            text(mid, cy+90, technology, 11.5, color='#475569')
            if note:
                text(mid, cy+106, note, 11, True, STATUS[status][1])
        if i < len(gaps):
            gy = y+TIER_H
            line(270, gy+2, 270, gy+30, arrow=True)
            text(284, gy+20, gaps[i][0], 11, align='start')
            line(730, gy+30, 730, gy+2, dashed=True, arrow=True)
            text(744, gy+20, gaps[i][1], 11, align='start')

    # The model provider is the single external model egress, as in Figure 1.
    rect(1191, 291, 231, 136, '#855bc0', '#fff7ed')
    text(1306, 315, 'EXTERNAL MODEL PROVIDER', 13, True)
    for k, s in enumerate(['Frontier: planning / SQL', 'Small model: prose / chart choice', "Organisation’s own API key", 'Question + schema; optional samples', 'PII-filtered / schema-only mode']):
        text(1306, 339+k*16, s, 11.5)
    text(1306, 452, 'Outside the deployment', 11.5, True)
    text(1306, 474, 'External service · no status', 11, color='#64748b')
    line(1148, 319, 1191, 319, arrow=True)
    text(1170, 309, 'HTTPS', 9)
    line(1191, 400, 1148, 400, dashed=True, arrow=True)

    # Legend, as in the reference Figure 2.
    ly = 81 + BOUNDARY_H + 34
    items = [(DONE, 'Done (implemented)'), (PARTIAL, 'Partial: part built, rest scheduled'), (DESIGNED, 'Designed: specification complete'), (PLANNED, 'Planned (CMPE 295B)')]
    lx = 35
    for status, label in items:
        fill, colour, _ = STATUS[status]
        rect(lx, ly-13, 30, 16, '#475569' if status == PLANNED else colour, fill, status == PLANNED, 2)
        text(lx+40, ly, label, 13, align='start')
        lx += 40 + len(label)*7.1 + 34
    total_a = counts[DONE] + counts[PARTIAL] + counts[DESIGNED]
    text(35, ly+30, f'SUMMARY: {counts[DONE]} of {total_a} CMPE 295A components done; {counts[PARTIAL]} partial; {counts[DESIGNED]} designed with specifications; {counts[PLANNED]} planned for CMPE 295B.', 12, align='start')
    text(35, ly+54, 'READING: Tiers, cards, arrows and technologies are unchanged from Figure 1; only the status fill, badge and specification line are added.', 11.5, align='start')
    text(35, ly+76, 'Specifications: runs/insightpilot/tech/deep_dives.md, tech/architecture/D01–D10 and product/ux_spec.md in the project repository.', 11, align='start')
    pdf.save()
    svg.append('</svg>')
    (OUT/f'{STEM}.svg').write_text('\n'.join(svg) + '\n')
    doc = fitz.open(OUT/f'{STEM}.pdf')
    doc[0].get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False).save(OUT/f'{STEM}.png')
    print(f'Built {STEM}.svg / .pdf / .png', counts)


if __name__ == '__main__':
    build()
