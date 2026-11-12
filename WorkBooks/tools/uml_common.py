"""Shared drawing helpers for the Workbook 2 UML class diagrams (PDF, SVG, PNG).

Visual language follows the AI Agent Marketplace Workbook 2, Figure 3: three-part class
boxes with a tinted header, red multiplicities, filled composition diamonds, italic role
labels, dashed boxes for planned scope. Palette and fonts follow our Workbook 1 Figure 1.
"""
from pathlib import Path
from html import escape
import math
import fitz
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase.pdfmetrics import stringWidth

OUT = Path(__file__).resolve().parents[1] / 'assets'

TIER = {
    'pres': ('#3974bb', '#e4edf8'),
    'orch': ('#855bc0', '#eee8f7'),
    'agent': ('#319763', '#e3f2e9'),
    'verify': ('#c47c20', '#f8ecdc'),
    'integ': ('#c94e67', '#f7e3e7'),
    'data': ('#64748b', '#e9edf2'),
    'ref': ('#94a3b8', '#f1f5f9'),
}
LINE, MULT, LABEL, INK = '#4b5563', '#b83a3a', '#64748b', '#1f2937'
HEADER_H, LINE_H = 31, 18
FS = 1.12   # font scale: larger text so diagrams stay readable at page width
FONTS = {'b': 'Helvetica-Bold', 'i': 'Helvetica-Oblique', 'n': 'Helvetica'}


def box_height(attrs, methods):
    h = HEADER_H + 8 + LINE_H*len(attrs) + 4
    if methods:
        h += 6 + LINE_H*len(methods) + 2
    return h + 4


class Drawer:
    def __init__(self, width, height, stem, title):
        self.W, self.H, self.stem = width, height, stem
        OUT.mkdir(exist_ok=True)
        self.pdf = canvas.Canvas(str(OUT / f'{stem}.pdf'), pagesize=(width, height))
        self.pdf.setTitle(title)
        self.svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
                    f'<title>{escape(title)}</title>', '<rect width="100%" height="100%" fill="white"/>']
        self.geo = {}

    # primitives ---------------------------------------------------------
    def rect(self, x, y, w, h, stroke, fill, dashed=False, radius=2, lw=2.0):
        p = self.pdf
        p.setStrokeColor(HexColor(stroke)); p.setFillColor(HexColor(fill)); p.setLineWidth(lw)
        p.setDash(6, 4) if dashed else p.setDash()
        p.roundRect(x, self.H-y-h, w, h, radius, stroke=1, fill=1); p.setDash()
        self.svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="{lw}"' + (' stroke-dasharray="6 4"' if dashed else '') + '/>')

    def hline(self, x1, x2, y, color, lw=1.2):
        p = self.pdf
        p.setStrokeColor(HexColor(color)); p.setLineWidth(lw); p.setDash()
        p.line(x1, self.H-y, x2, self.H-y)
        self.svg.append(f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{color}" stroke-width="{lw}"/>')

    def text(self, x, y, value, size=11.5, style='n', color=INK, align='start', max_w=None):
        f = FONTS[style]
        size = size * FS
        while max_w and stringWidth(value, f, size) > max_w and size > 8:
            size -= 0.25
        p = self.pdf
        p.setFillColor(HexColor(color)); p.setFont(f, size)
        {'start': p.drawString, 'middle': p.drawCentredString, 'end': p.drawRightString}[align](x, self.H-y, value)
        italic = ' font-style="italic"' if style == 'i' else ''
        self.svg.append(f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{align}" font-family="Arial, Helvetica, sans-serif" font-size="{size}" font-weight="{700 if style == "b" else 400}"{italic} fill="{color}">{escape(value)}</text>')

    def poly(self, pts, fill):
        p = self.pdf
        p.setFillColor(HexColor(fill))
        path = p.beginPath(); path.moveTo(pts[0][0], self.H-pts[0][1])
        for px, py in pts[1:]:
            path.lineTo(px, self.H-py)
        path.close(); p.drawPath(path, stroke=0, fill=1)
        self.svg.append('<polygon points="' + ' '.join(f'{px:.1f},{py:.1f}' for px, py in pts) + f'" fill="{fill}"/>')

    def seg(self, pts, dashed=False):
        p = self.pdf
        p.setStrokeColor(HexColor(LINE)); p.setLineWidth(1.5)
        p.setDash(5, 4) if dashed else p.setDash()
        path = p.beginPath(); path.moveTo(pts[0][0], self.H-pts[0][1])
        for px, py in pts[1:]:
            path.lineTo(px, self.H-py)
        p.drawPath(path, stroke=1, fill=0); p.setDash()
        self.svg.append('<polyline points="' + ' '.join(f'{px:.1f},{py:.1f}' for px, py in pts) + f'" fill="none" stroke="{LINE}" stroke-width="1.5"' + (' stroke-dasharray="5 4"' if dashed else '') + '/>')

    # UML parts ----------------------------------------------------------
    def class_box(self, name, x, y, w, tier, title, attrs, methods, dashed=False, inline=False):
        """inline=True centres each compartment line (for a wide box such as Orchestrator)."""
        border, tint = TIER[tier]
        h = box_height(attrs, methods)
        self.geo[name] = (x, y, w, h)
        rule = border if not dashed else '#cbd5e1'
        self.rect(x, y, w, h, border, '#ffffff', dashed)
        self.rect(x+1, y+1, w-2, HEADER_H-1, tint, tint, False, 1, 0.1)
        self.text(x+w/2, y+21, title, 13.5, 'b', INK, 'middle', max_w=w-16)
        self.hline(x, x+w, y+HEADER_H, rule)
        ty = y+HEADER_H+8
        align, ax = ('middle', x+w/2) if inline else ('start', x+8)
        for a in attrs:
            ty += LINE_H
            self.text(ax, ty-4, a, 11.5, 'n', INK, align, max_w=w-14)
        if methods:
            ty += 6
            self.hline(x, x+w, ty, rule, 1)
            ty += 2
            for m in methods:
                ty += LINE_H
                self.text(ax, ty-4, m, 11.5, 'i', INK, align, max_w=w-14)
        return h

    def ref_box(self, name, x, y, w, title, note='see Fig. 3a'):
        """A domain class referenced from another figure: header and a one-line note."""
        border, tint = TIER['ref']
        h = HEADER_H + 24
        self.geo[name] = (x, y, w, h)
        self.rect(x, y, w, h, border, '#ffffff', lw=1.4)
        self.rect(x+1, y+1, w-2, HEADER_H-1, tint, tint, False, 1, 0.1)
        self.text(x+w/2, y+21, title, 13, 'b', '#475569', 'middle', max_w=w-16)
        self.hline(x, x+w, y+HEADER_H, border, 1)
        self.text(x+w/2, y+HEADER_H+17, note, 10.5, 'i', LABEL, 'middle')
        return h

    def anchor(self, name, side, frac):
        x, y, w, h = self.geo[name]
        if frac > 1:   # pixel offset from the top / left edge
            return {'l': (x, y+frac), 'r': (x+w, y+frac), 't': (x+frac, y), 'b': (x+frac, y+h)}[side]
        return {'l': (x, y+h*frac), 'r': (x+w, y+h*frac), 't': (x+w*frac, y), 'b': (x+w*frac, y+h)}[side]

    def edge(self, frm, to, fa, ta, fm='', tm='', label='', kind='assoc'):
        """kind: assoc | comp (diamond at frm) | dep (dashed, open arrow at to)."""
        p1, p2 = self.anchor(frm, *fa), self.anchor(to, *ta)
        ang = math.atan2(p2[1]-p1[1], p2[0]-p1[0]); ux, uy = math.cos(ang), math.sin(ang)
        start = p1
        if kind == 'comp':
            d = [p1, (p1[0]+8*ux-5*uy, p1[1]+8*uy+5*ux), (p1[0]+16*ux, p1[1]+16*uy), (p1[0]+8*ux+5*uy, p1[1]+8*uy-5*ux)]
            start = (p1[0]+16*ux, p1[1]+16*uy)
        self.seg([start, p2], dashed=(kind == 'dep'))
        if kind == 'comp':
            self.poly(d, LINE)
        if kind == 'dep':
            a = [(p2[0]-11*math.cos(ang+s), p2[1]-11*math.sin(ang+s)) for s in (-.42, .42)]
            self.seg([a[0], p2, a[1]])
        nx, ny = -uy, ux
        off = 26 if kind == 'comp' else 14
        mx, my = (p1[0]+p2[0])/2, (p1[1]+p2[1])/2
        if abs(ux) > .9:          # horizontal: label above, multiplicities below
            if fm: self.text(p1[0]+off*ux, p1[1]+17, fm, 11.5, 'b', MULT, 'middle')
            if tm: self.text(p2[0]-14*ux, p2[1]+17, tm, 11.5, 'b', MULT, 'middle')
            if label: self.text(mx, my-7, label, 11, 'i', LABEL, 'middle')
        elif abs(uy) > .9:        # vertical: multiplicities left, label right
            if fm: self.text(p1[0]-12, p1[1]+off*uy+4, fm, 11.5, 'b', MULT, 'end')
            if tm: self.text(p2[0]-12, p2[1]-14*uy+4, tm, 11.5, 'b', MULT, 'end')
            if label: self.text(mx+9, my+4, label, 11, 'i', LABEL, 'start')
        else:                     # diagonal: put each label on the side away from its own box
            def place(p, dx, dy, name, dist):
                q = (p[0] + dist*dx, p[1] + dist*dy)
                bx, by, bw, bh = self.geo[name]
                c = (bx + bw/2, by + bh/2)
                a = (q[0] + 12*nx, q[1] + 12*ny)
                b = (q[0] - 12*nx, q[1] - 12*ny)
                return max((a, b), key=lambda s: (s[0]-c[0])**2 + (s[1]-c[1])**2)
            if fm:
                x_, y_ = place(p1, ux, uy, frm, off + 8)
                self.text(x_, y_+4, fm, 11.5, 'b', MULT, 'middle')
            if tm:
                x_, y_ = place(p2, -ux, -uy, to, 22)
                self.text(x_, y_+4, tm, 11.5, 'b', MULT, 'middle')
            if label: self.text(mx+10, my+4, label, 11, 'i', LABEL, 'start')

    def legend(self, x, y, w, items):
        """items: list of (kind, text); kind in solid | dashed | ref | comp | assoc | dep."""
        h = 34 + 26*len(items)
        self.rect(x, y, w, h, '#cbd5e1', '#f8fafc', radius=4, lw=1)
        self.text(x+12, y+22, 'Legend', 13, 'b', '#334155')
        ly = y+36
        for kind, label in items:
            if kind in ('solid', 'dashed'):
                self.rect(x+12, ly, 30, 16, '#475569', '#ffffff', kind == 'dashed', lw=2)
            elif kind == 'ref':
                self.rect(x+12, ly, 30, 16, TIER['ref'][0], TIER['ref'][1], lw=1.2)
            elif kind == 'comp':
                self.poly([(x+12, ly+8), (x+20, ly+3), (x+28, ly+8), (x+20, ly+13)], LINE)
                self.seg([(x+28, ly+8), (x+44, ly+8)])
            elif kind == 'assoc':
                self.seg([(x+12, ly+8), (x+44, ly+8)])
            elif kind == 'dep':
                self.seg([(x+12, ly+8), (x+44, ly+8)], dashed=True)
                self.seg([(x+36, ly+3), (x+44, ly+8), (x+36, ly+13)])
            self.text(x+52, ly+13, label, 11, 'n', INK, 'start', max_w=w-60)
            ly += 26
        return h

    def save(self):
        self.pdf.save()
        self.svg.append('</svg>')
        (OUT/f'{self.stem}.svg').write_text('\n'.join(self.svg) + '\n')
        doc = fitz.open(OUT/f'{self.stem}.pdf')
        doc[0].get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False).save(OUT/f'{self.stem}.png')
