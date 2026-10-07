#!/usr/bin/env python3
"""Build one layered InsightPilot diagram (SVG, PDF, PNG).
Architecture source: Workbook1_Draft_v2.md Chapter 5.
Requires reportlab and PyMuPDF. No network or application dependencies.
"""
from pathlib import Path
from html import escape
import fitz
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets'
WIDTH, HEIGHT = 1440, 1155
STEM = 'ch5_architecture_v2'

# Title, colour, cards: (name, function lines, technology line, future).
TIERS = [
    ('PRESENTATION TIER', '#3974bb', [
        ('Investigation Workspace', ['Ask questions; follow-ups inherit context'], 'React · TypeScript · FastAPI', False),
        ('Plan Review & Approval', ['Clarify ambiguity; edit and approve plans'], 'React · typed plan DAG', False),
        ('Lineage Inspector & Export', ['Inspect / replay hops; analyst sign-off'], 'React · self-contained artifact', False),
    ]),
    ('ORCHESTRATION TIER: CUSTOM PYTHON 3.12', '#855bc0', [
        ('Semantic Resolver', ['Bind terms to columns / grain', 'Halt and ask when ambiguous'], 'BM25 · embeddings · rank fusion', False),
        ('Plan Synthesiser', ['Generate typed DAG; validate', 'sources, inputs and cycles'], 'Python · constrained generation', False),
        ('Orchestrator & Replanner', ['Route all handoffs; own state', 'Budget / retry caps; replan [295B]'], 'Custom Python · DAG execution', False),
        ('Model Client', ['Plan / SQL / prose model calls', 'Schema-only or filtered samples'], 'Provider-agnostic HTTPS API', False),
    ]),
    ('SPECIALIST AGENT TIER: ALL TASKS AND RESULTS ROUTED THROUGH ORCHESTRATOR', '#319763', [
        ('Fetch / Integration Agent', ['Generate / repair queries', 'Retrieve and prepare data'], 'Python · SQLAlchemy · psycopg', False),
        ('Analytics Agent', ['Joins, KPIs, comparisons', 'Trends and aggregation'], 'SQL · pandas', False),
        ('Visualization Agent [295B]', ['Choose charts; return chart', 'specification and rationale'], 'Python · chart rendering', True),
        ('ML Agent [295B]', ['Time-boxed baseline models', 'Model card + uncertainty'], 'scikit-learn · LightGBM', True),
    ]),
    ('VERIFICATION & LINEAGE TIER: CHECKS USE SQL / COMPUTE, NEVER LLM SELF-CRITIQUE', '#c47c20', [
        ('Hop Verifier', ['Counts, grain, coverage, nulls', 'Totals and type / range checks'], 'Independent SQL · local compute', False),
        ('Cross-source Reconciler', ['Profile join keys and overlap', 'Propose mappings for approval'], 'DuckDB SQL · pandas', False),
        ('Lineage Recorder & Replayer', ['Record query, grain, checks and skips', 'Replay one hop; report differences'], 'Python · PostgreSQL · local files', False),
    ]),
    ('INTEGRATION TIER: READ-ONLY SOURCES; SEMANTIC DEFINITIONS TAKE PRECEDENCE', '#c94e67', [
        ('PostgreSQL Connector', ['Describe, sample, execute, profile', 'Inherit source read permissions'], 'SQLAlchemy · psycopg', False),
        ('CSV / Excel Connector', ['Query uploaded files', 'Infer schema; profile without ETL'], 'DuckDB · Python', False),
        ('REST JSON Connector [295B]', ['Third source type', 'Read-only API access'], 'Python · HTTP / JSON', True),
        ('Semantic Layer [295B]', ['Definitions override inference', 'dbt semantic layer'], 'Separate semantic interface', True),
    ]),
    ('DATA, AUDIT & EVALUATION TIER', '#64748b', [
        ('Application Store', ['Org bindings, plans, investigations', 'Hop lineage, overrides, sign-off'], 'PostgreSQL 16', False),
        ('Artifact Store', ['Local step outputs and exports', 'Recorded statements / parameters'], 'Local filesystem', False),
        ('Append-only Audit Log', ['Actor, source, statement, timestamp', 'Readable without application'], 'JSONL · local filesystem', False),
        ('Offline Evaluation Harness', ['Ground truth + seeded errors', 'Accuracy and verifier coverage'], 'pytest · question-set fixtures', False),
    ]),
]


def build():
    OUT.mkdir(exist_ok=True)
    pdf = canvas.Canvas(str(OUT / f'{STEM}.pdf'), pagesize=(WIDTH, HEIGHT))
    pdf.setTitle('InsightPilot: System Architecture (Function + Technology)')
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">',
           '<title>InsightPilot: proposed layered system architecture</title>',
           '<desc>Six tiers show components, functions and technologies; future scope uses dashed borders. External model provider is outside the deployment boundary.</desc>',
           '<rect width="100%" height="100%" fill="white"/>']

    def rect(x, y, w, h, stroke, fill='#ffffff', dashed=False, radius=6):
        pdf.setStrokeColor(HexColor(stroke)); pdf.setFillColor(HexColor(fill))
        pdf.setLineWidth(1.4); pdf.setDash(6, 4) if dashed else pdf.setDash()
        pdf.roundRect(x, HEIGHT-y-h, w, h, radius, stroke=1, fill=1)
        svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="1.4"' + (' stroke-dasharray="6 4"' if dashed else '') + '/>')
        pdf.setDash()

    def text(x, y, value, size=14, bold=False, color='#334155', align='middle'):
        pdf.setFillColor(HexColor(color)); pdf.setFont('Helvetica-Bold' if bold else 'Helvetica', size)
        (pdf.drawCentredString if align=='middle' else pdf.drawString)(x, HEIGHT-y, value)
        svg.append(f'<text x="{x}" y="{y}" text-anchor="{align if align=="middle" else "start"}" font-family="Arial, Helvetica, sans-serif" font-size="{size}" font-weight="{700 if bold else 400}" fill="{color}">{escape(value)}</text>')

    def line(x1, y1, x2, y2, dashed=False, arrow=False):
        color='#64748b'
        pdf.setStrokeColor(HexColor(color)); pdf.setLineWidth(1.5)
        pdf.setDash(4, 3) if dashed else pdf.setDash()
        pdf.line(x1, HEIGHT-y1, x2, HEIGHT-y2)
        svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="1.5"' + (' stroke-dasharray="4 3"' if dashed else '') + '/>')
        pdf.setDash()
        if arrow:
            import math
            angle=math.atan2(y2-y1,x2-x1)
            points=[(x2,y2)] + [(x2-8*math.cos(angle+a),y2-8*math.sin(angle+a)) for a in [-.45,.45]]
            pdf.setFillColor(HexColor(color)); path=pdf.beginPath()
            path.moveTo(points[0][0], HEIGHT-points[0][1])
            for x,y in points[1:]:path.lineTo(x,HEIGHT-y)
            path.close();pdf.drawPath(path,stroke=0,fill=1)
            svg.append('<polygon points="'+' '.join(f'{x},{y}' for x,y in points)+f'" fill="{color}"/>')

    text(WIDTH/2, 31, 'InsightPilot: System Architecture (Function + Technology)', 25, True)
    text(WIDTH/2, 56, 'Proposed design · Layered, agent-orchestrated architecture · CMPE 295A + 295B scope', 15)
    rect(18, 81, 1147, 965, '#94a3b8', '#ffffff')
    text(36, 102, 'DEPLOYMENT: ONE ORGANISATION · SELF-HOSTED / DOCKER COMPOSE', 14, True, align='start')
    x, width, height = 35, 1113, 122
    gaps = [
        ('question + context / analyst-approved plan', 'clarification / plan / answer + evidence'),
        ('typed tasks + input references + budget', 'results + declared grain + lineage'),
        ('per-hop outputs / verification evidence', 'pass / warning / failure to orchestrator'),
        ('independent SQL / profiles over sources', 'schema / row counts / coverage / grain'),
        ('durable bindings, state, lineage and audit', 'replay metadata / evaluation outcomes'),
    ]
    for i, (title, color, cards) in enumerate(TIERS):
        y = 114 + i*154
        # Soft band tint, keeping card text dark and readable in print.
        tint = ['#eff6ff','#f5f3ff','#f0fdf4','#fff7ed','#fff1f2','#f1f5f9'][i]
        rect(x, y, width, height, color, tint)
        text(x+12,y+21,title,13,True,color,align='start')
        gap=14; cw=(width-28-gap*(len(cards)-1))/len(cards)
        for j,(name, functions, technology, future) in enumerate(cards):
            cx=x+14+j*(cw+gap); cy=y+33
            rect(cx,cy,cw,78,color,'#ffffff',future,3)
            text(cx+cw/2,cy+19,name,14,True)
            for k,f in enumerate(functions):
                text(cx+cw/2,cy+38+k*15,f,12.5)
            text(cx+cw/2,cy+69,technology,12,color='#475569')
        if i<len(gaps):
            gy=y+height
            line(270,gy+2,270,gy+30,arrow=True)
            text(284,gy+20,gaps[i][0],11,align='start')
            line(730,gy+30,730,gy+2,dashed=True,arrow=True)
            text(744,gy+20,gaps[i][1],11,align='start')

    # The model provider is the single external model egress.
    rect(1191, 291, 231, 136, '#855bc0', '#fff7ed')
    text(1306,315,'EXTERNAL MODEL PROVIDER',13,True)
    for k,s in enumerate(['Frontier: planning / SQL','Small model: prose / chart choice',"Organisation’s own API key",'Question + schema; optional samples','PII-filtered / schema-only mode']):
        text(1306,339+k*16,s,11.5)
    text(1306,452,'Outside the deployment',11.5,True)
    line(1148,319,1191,319,arrow=True)
    text(1170,309,'HTTPS',9)
    line(1191,400,1148,400,dashed=True,arrow=True)
    text(1306,481,'Returned plan / SQL / prose',11)
    text(1306,503,'Data-source access stays local',11)

    text(35,1072,'KEY: Solid box = 295A scope; dashed box + [295B] = 295B scope. Solid arrow = requests/data; dashed arrow = control/response.',12,align='start')
    text(35,1096,'AGENT CONTROL: No direct agent-to-agent calls. Failed checks halt downstream work; 295B adds capped replanning / partial-result exit.',12,align='start')
    text(35,1120,'READING: Arrows summarise tier interactions, not execution order. Analyst sign-off precedes export. DAG = directed acyclic graph; PII = personal information.',11.5,align='start')
    pdf.save()
    svg.append('</svg>')
    (OUT/f'{STEM}.svg').write_text('\n'.join(svg)+'\n')
    doc=fitz.open(OUT/f'{STEM}.pdf')
    doc[0].get_pixmap(matrix=fitz.Matrix(2,2),alpha=False).save(OUT/f'{STEM}.png')
    print(f'Built one diagram: {STEM}.svg / .pdf / .png')


if __name__=='__main__':
    build()
