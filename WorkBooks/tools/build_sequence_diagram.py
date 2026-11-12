#!/usr/bin/env python3
"""UML sequence diagram: answering one question end to end (SVG, PDF, PNG).

Visual language follows the AI Agent Marketplace Workbook 2, Figure 4: participant boxes
with dashed lifelines, numbered messages labelled above the arrow (solid = call, dashed =
return), self-calls as small loops, and dashed combined fragments (alt / opt / loop).
Participants use the tier colours of our Workbook 1 Figure 1. The flow follows
WorkBooks/InsightPilot_Design_Flow.md and the classes of Figures 3-5.
"""
import math
from uml_common import Drawer, TIER, LINE, INK
from reportlab.pdfbase.pdfmetrics import stringWidth

STEM = 'ch6_sequence'
X0, DX = 170, 170
PART = [  # key, label lines, tier
    ('UI', ['Analyst /', 'Workspace'], 'pres'),
    ('OR', ['Orchestrator'], 'orch'),
    ('SR', ['Semantic', 'Resolver'], 'orch'),
    ('PS', ['Plan', 'Synthesiser'], 'orch'),
    ('SA', ['Specialist', 'Agent'], 'agent'),
    ('MC', ['ModelClient', '(to LLM)'], 'orch'),
    ('SC', ['Source', 'Connector'], 'integ'),
    ('HV', ['Hop', 'Verifier'], 'verify'),
    ('LR', ['Lineage', 'Recorder'], 'verify'),
]
X = {k: X0 + i*DX for i, (k, _, _) in enumerate(PART)}
WIDTH = X['LR'] + 110

FRAG_COLOR = {'alt': '#c0392b', 'opt': '#c0392b', 'break': '#c0392b', 'loop': '#4f6db8'}

# ('m', from, to, label) call   ('r', from, to, label) return   ('s', who, label) self-call
# ('[', operator, condition, left_key, right_key)   (']',)
FLOW = [
    ('m', 'UI', 'OR', 'ask(question)'),
    ('m', 'OR', 'SR', 'resolve(question)'),
    ('r', 'SR', 'OR', 'bindings  (analyst asked if a term is ambiguous)'),
    ('m', 'OR', 'PS', 'synthesise(question, bindings)'),
    ('m', 'PS', 'MC', 'plan(prompt)  [frontier]'),
    ('r', 'PS', 'OR', 'validated Plan (DAG of steps)'),
    ('r', 'OR', 'UI', 'show plan for approval'),
    ('m', 'UI', 'OR', 'approve()'),
    ('[', 'loop', 'for each PlanStep in DAG order', 'OR', 'LR'),
    ('m', 'OR', 'SA', 'dispatch(step)'),
    ('m', 'SA', 'MC', 'sql(prompt)  [frontier]'),
    ('m', 'SA', 'SC', 'execute(sql)  read-only'),
    ('r', 'SA', 'OR', 'StepResult'),
    ('m', 'OR', 'HV', 'verify(result)  SQL checks, no model'),
    ('r', 'HV', 'OR', 'HopVerdict: PASS | WARN | FAIL | ERROR'),
    ('m', 'OR', 'LR', 'record(step, result, checks)  -> Hop'),
    (']',),
    ('m', 'OR', 'MC', 'prose(verified facts)  [small]'),
    ('r', 'OR', 'UI', 'Answer  (each fact cites its hop)'),
    ('m', 'UI', 'OR', 'sign off  ->  export()'),
]

STEP, TOP = 40, 70
BOX_W, BOX_H = 140, 48


def layout():
    """Assign a y to every message and compute fragment rectangles."""
    y = TOP + BOX_H + 44
    msgs, frags, stack = [], [], []
    n = 0
    for item in FLOW:
        if item[0] == '[':
            depth = len(stack)
            stack.append({'op': item[1], 'cond': item[2], 'l': item[3], 'r': item[4], 'y0': y - 8, 'depth': depth})
            y += 30
        elif item[0] == ']':
            f = stack.pop()
            f['y1'] = y - 14
            frags.append(f)
            y += 10
        else:
            n += 1
            msgs.append((n, item, y))
            y += STEP + (14 if item[0] == 's' else 0)
    return msgs, frags, y


def build():
    msgs, frags, end_y = layout()
    height = end_y + 120
    d = Drawer(WIDTH, height, STEM, 'InsightPilot - UML sequence diagram')
    d.text(WIDTH/2, 38, 'UML sequence diagram - answering one question (main path)', 21, 'b', INK, 'middle', max_w=WIDTH-40)

    # Participants and lifelines.
    for key, lines, tier in PART:
        border, tint = TIER[tier]
        x = X[key]
        d.rect(x - BOX_W/2, TOP, BOX_W, BOX_H, border, tint, radius=5, lw=2)
        for i, ln in enumerate(lines):
            yy = TOP + (29 if len(lines) == 1 else 21 + i*17)
            d.text(x, yy, ln, 13, 'b', INK, 'middle', max_w=BOX_W-10)
        d.seg([(x, TOP + BOX_H), (x, end_y + 10)], dashed=True)

    # Fragments (drawn first so arrows sit on top).
    for f in sorted(frags, key=lambda f: f['depth']):
        inset = 10*f['depth']
        x0 = X[f['l']] - 82 + inset
        x1 = X[f['r']] + 82 - inset
        color = FRAG_COLOR[f['op']]
        _frame(d, x0, f['y0'], x1, f['y1'], color)
        d.text(x0 + 7, f['y0'] + 16, f"{f['op']} [{f['cond']}]", 12.5, 'b', color, 'start')

    # Messages.
    for n, item, y in msgs:
        kind = item[0]
        if kind == 's':
            x = X[item[1]]
            d.seg([(x, y), (x + 34, y), (x + 34, y + 18), (x + 4, y + 18)])
            _head(d, (x + 34, y + 18), (x + 4, y + 18), filled=True)
            _label(d, x + 42, y + 13, f'{n}  {item[2]}', 'start')
            continue
        a, b, label = X[item[1]], X[item[2]], item[3]
        ret = kind == 'r'
        d.seg([(a, y), (b - (4 if b > a else -4), y)], dashed=ret)
        _head(d, (a, y), (b, y), filled=not ret)
        _label(d, (a + b)/2, y - 7, f'{n}  {label}', 'middle')

    # Footer notes; step numbers are looked up from the flow so they stay correct.
    def num(text):
        return next(n for n, item, _ in msgs if text in item[-1])
    loop = [n for n, item, y in msgs if any(f['op'] == 'loop' and f['y0'] < y < f['y1'] for f in frags)]
    fy = end_y + 40
    d.text(WIDTH/2, fy, f'Steps {loop[0]}-{loop[-1]} repeat for every PlanStep. Every StepResult returns to the Orchestrator; verification ({num("verify(")}) never calls a model. Plan ({num("plan(prompt)")}) and SQL ({num("sql(prompt)")}) use the frontier model, prose ({num("prose(")}) the small one.', 12, 'n', '#64748b', 'middle', max_w=WIDTH-40)
    d.text(WIDTH/2, fy + 22, 'Not drawn, described in the text: clarifying an ambiguous term, SQL repair on error, cross-source reconciliation, and halting on a RED hop.', 12, 'n', '#64748b', 'middle', max_w=WIDTH-40)
    d.text(WIDTH/2, fy + 44, 'Solid arrow = call; dashed arrow = return or reply.', 11, 'i', '#64748b', 'middle', max_w=WIDTH-40)
    d.save()
    print(f'Built {STEM}: {len(PART)} participants, {len(msgs)} messages, {len(frags)} fragments, {WIDTH}x{height}')


def _label(d, x, y, text, align):
    """Message label on a white background, so lifelines do not run through the text."""
    from uml_common import FS
    w = stringWidth(text, 'Helvetica', 12*FS)
    left = x - w/2 if align == 'middle' else x
    left = max(left, 6)
    d.rect(left - 3, y - 11, w + 6, 15, '#ffffff', '#ffffff', radius=0, lw=0.1)
    d.text(left, y, text, 12, 'n', INK, 'start')


def _frame(d, x0, y0, x1, y1, color):
    d.pdf.setDash(6, 4)
    for seg in [[(x0, y0), (x1, y0)], [(x1, y0), (x1, y1)], [(x1, y1), (x0, y1)], [(x0, y1), (x0, y0)]]:
        _colored_seg(d, seg, color)
    d.pdf.setDash()


def _colored_seg(d, pts, color):
    from reportlab.lib.colors import HexColor
    p = d.pdf
    p.setStrokeColor(HexColor(color)); p.setLineWidth(1.6); p.setDash(6, 4)
    p.line(pts[0][0], d.H - pts[0][1], pts[1][0], d.H - pts[1][1]); p.setDash()
    d.svg.append(f'<line x1="{pts[0][0]}" y1="{pts[0][1]}" x2="{pts[1][0]}" y2="{pts[1][1]}" stroke="{color}" stroke-width="1.6" stroke-dasharray="6 4"/>')


def _head(d, p1, p2, filled):
    ang = math.atan2(p2[1] - p1[1], p2[0] - p1[0])
    tip = p2
    wing = [(tip[0] - 10*math.cos(ang + s), tip[1] - 10*math.sin(ang + s)) for s in (-.4, .4)]
    if filled:
        d.poly([tip, wing[0], wing[1]], LINE)
    else:
        d.seg([wing[0], tip, wing[1]])


if __name__ == '__main__':
    build()
