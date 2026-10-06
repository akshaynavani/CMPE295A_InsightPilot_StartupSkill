#!/usr/bin/env python3
"""Build the Workbook .docx from Workbook1_Draft.md, on top of the course template.

The template supplies styles.xml, fonts, numbering and the section setup (US Letter,
1.5" left binding margin -> a 6.0" text column). This script writes word/document.xml
itself, because pandoc's generic style mapping ignores the template's own styles.

Conventions understood in the Markdown:
    <<<PAGEBREAK>>>          page break (each chapter starts on a new page)
    <<<FIGURE:path>>>        image, scaled to the 6.0" text column
    "Table N. Caption"       caption paragraph directly above a Markdown table
    "Figure N. Caption"      caption paragraph directly above a figure
    "1. text" + indented     reference entry with hanging indent; an indented
      continuation line        italic line after it becomes the annotation
    > text                   block quote (used for [TEAM] notes)
    ```...```                fixed-width block
Run:  python3 tools/build_docx.py
"""
import os, re, shutil, zipfile
from xml.sax.saxutils import escape

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
TEMPLATE = os.path.join(ROOT, "Project Workbook Template - development V3.docx")
SOURCE = os.path.join(ROOT, "Workbook1_Draft.md")
OUTPUT = os.path.join(ROOT, "Workbook1_Draft.docx")

TEXT_W = 8640          # 6.0" text column in twips (Letter, 1.5" left + 1.0" right)
EMU_PER_IN = 914400
BODY_SZ, TABLE_SZ, CAPTION_SZ = 24, 18, 20   # half-points: 12pt, 9pt, 10pt

# ---------------------------------------------------------------- inline runs

def runs(text, sz=BODY_SZ, italic_all=False, bold_all=False):
    """Parse **bold**, *italic* and `code` into runs. Markers nest, so `code`
    inside **bold** keeps both the bold and the fixed-width font."""
    out = []
    for part in re.split(r'(\*\*.+?\*\*|\*[^*]+?\*|`[^`]+?`)', text, flags=re.S):
        if not part:
            continue
        if part.startswith('**') and part.endswith('**') and len(part) > 4:
            out.append(runs(part[2:-2], sz, italic_all, True)); continue
        if part.startswith('*') and part.endswith('*') and len(part) > 2:
            out.append(runs(part[1:-1], sz, True, bold_all)); continue
        mono = part.startswith('`') and part.endswith('`') and len(part) > 2
        if mono:
            part = part[1:-1]
        part = re.sub(r'\[([^\]]+)\]\((?:[^)]+)\)', r'\1', part)   # links -> text
        rpr = f'<w:sz w:val="{sz}"/><w:szCs w:val="{sz}"/>'
        if mono:
            rpr = (f'<w:rFonts w:ascii="Courier New" w:hAnsi="Courier New"/>'
                   f'<w:sz w:val="{sz-4}"/><w:szCs w:val="{sz-4}"/>')
        if bold_all:
            rpr += '<w:b/>'
        if italic_all:
            rpr += '<w:i/>'
        out.append(f'<w:r><w:rPr>{rpr}</w:rPr>'
                   f'<w:t xml:space="preserve">{escape(part)}</w:t></w:r>')
    return ''.join(out) or '<w:r><w:t/></w:r>'

def para(content, style=None, spacing="120", ind=None, jc=None, keep=False):
    ppr = ''
    if style:
        ppr += f'<w:pStyle w:val="{style}"/>'
    if keep:
        ppr += '<w:keepNext/>'
    if ind:
        ppr += f'<w:ind {ind}/>'
    if jc:
        ppr += f'<w:jc w:val="{jc}"/>'
    ppr += f'<w:spacing w:after="{spacing}" w:line="259" w:lineRule="auto"/>'
    return f'<w:p><w:pPr>{ppr}</w:pPr>{content}</w:p>'

# ---------------------------------------------------------------- block parse

def parse(md):
    lines = md.split('\n')
    blocks, i = [], 0
    while i < len(lines):
        ln = lines[i]
        s = ln.strip()
        if s == '<<<PAGEBREAK>>>':
            blocks.append(('pagebreak', None)); i += 1
        elif s.startswith('<<<FIGURE:'):
            blocks.append(('figure', s[10:-3])); i += 1
        elif s.startswith('```'):
            code, i = [], i + 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code.append(lines[i]); i += 1
            blocks.append(('code', code)); i += 1
        elif s.startswith('#'):
            level = len(s) - len(s.lstrip('#'))
            blocks.append((f'h{level}', s.lstrip('#').strip())); i += 1
        elif s.startswith('|'):
            rows, caption = [], None
            if blocks and blocks[-1][0] == 'p' and re.match(r'^(Table|Figure) \d+\.', blocks[-1][1]):
                caption = blocks.pop()[1]
            while i < len(lines) and lines[i].strip().startswith('|'):
                row = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-{2,}:?', c) for c in row):
                    rows.append(row)
                i += 1
            blocks.append(('table', (caption, rows)))
        elif s.startswith('> '):
            buf = []
            while i < len(lines) and lines[i].strip().startswith('>'):
                buf.append(lines[i].strip().lstrip('>').strip()); i += 1
            blocks.append(('quote', ' '.join(buf)))
        elif s.startswith('- '):
            blocks.append(('bullet', s[2:])); i += 1
        elif re.match(r'^\d+\. ', s):
            num = re.match(r'^(\d+)\. ', s).group(1)
            body, i = s[len(num) + 2:], i + 1
            annotation = None
            while i < len(lines) and lines[i].startswith('   ') and lines[i].strip():
                t = lines[i].strip()
                (annotation := t) if t.startswith('*') else (body := body + ' ' + t)
                i += 1
            blocks.append(('ref', (num, body, annotation)))
        elif s:
            blocks.append(('p', s)); i += 1
        else:
            i += 1
    return blocks

# ---------------------------------------------------------------- table build

def build_table(caption, rows):
    if not rows:
        return ''
    ncols = max(len(r) for r in rows)
    rows = [r + [''] * (ncols - len(r)) for r in rows]
    weights = []
    for c in range(ncols):
        longest = max(len(re.sub(r'[*`]', '', r[c])) for r in rows)
        weights.append(max(longest, 8) ** 0.62)        # damp very long columns
    total = sum(weights)
    widths = [max(int(TEXT_W * w / total), 860) for w in weights]
    widths[-1] += TEXT_W - sum(widths)                  # make the row sum exact
    borders = ('<w:tblBorders>' + ''.join(
        f'<w:{e} w:val="single" w:sz="4" w:space="0" w:color="808080"/>'
        for e in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV')) + '</w:tblBorders>')
    xml = []
    if caption:
        # The template's tablecaption style carries numbering (numId 8, 'Table %1.'),
        # so the number must NOT be written here or Word prints it twice.
        rest = re.sub(r'^(?:Table|Figure) \d+\.\s*', '', caption)
        xml.append(para(runs(rest, sz=CAPTION_SZ),
                        style='tablecaption', spacing="60", keep=True))
    xml.append(f'<w:tbl><w:tblPr><w:tblW w:w="{TEXT_W}" w:type="dxa"/>{borders}'
               '<w:tblLayout w:type="fixed"/><w:tblCellMar>'
               '<w:top w:w="60" w:type="dxa"/><w:left w:w="90" w:type="dxa"/>'
               '<w:bottom w:w="60" w:type="dxa"/><w:right w:w="90" w:type="dxa"/>'
               '</w:tblCellMar></w:tblPr><w:tblGrid>'
               + ''.join(f'<w:gridCol w:w="{w}"/>' for w in widths) + '</w:tblGrid>')
    for ri, row in enumerate(rows):
        head = ri == 0
        trpr = '<w:trPr><w:tblHeader/><w:cantSplit/></w:trPr>' if head else '<w:trPr><w:cantSplit/></w:trPr>'
        cells = []
        for ci, cell in enumerate(row):
            shd = '<w:shd w:val="clear" w:color="auto" w:fill="EDEDED"/>' if head else ''
            if re.fullmatch(r'[A-Z]{1,4}-\d{1,3}', cell.strip()):
                cell = cell.strip().replace('-', '\u2011')   # non-breaking hyphen
            body = runs(cell, sz=TABLE_SZ, bold_all=head)
            cells.append(f'<w:tc><w:tcPr><w:tcW w:w="{widths[ci]}" w:type="dxa"/>{shd}'
                         '<w:vAlign w:val="top"/></w:tcPr>'
                         + para(body, spacing="40") + '</w:tc>')
        xml.append(f'<w:tr>{trpr}{"".join(cells)}</w:tr>')
    xml.append('</w:tbl>')
    xml.append(para('<w:r><w:t/></w:r>', spacing="0"))   # spacer after table
    return ''.join(xml)

# ---------------------------------------------------------------- document

def build(blocks, image_rel, image_px):
    out, title_done = [], False
    figure_no = 0
    i = 0
    # --- title page: everything before the first page break
    while i < len(blocks) and blocks[i][0] != 'pagebreak':
        kind, val = blocks[i]
        if kind == 'h1':
            out.append(para(runs(val, sz=32, bold_all=True), style='ProjectTitle',
                            jc='center', spacing="360"))
        elif kind == 'h2':
            out.append(para(runs(val, sz=28), style='Centered', jc='center', spacing="1200"))
        elif kind == 'p':
            out.append(para(runs(val, sz=BODY_SZ), style='Centered', jc='center', spacing="200"))
        i += 1
    title_done = True
    for idx, (kind, val) in enumerate(blocks[i:]):
        if kind == 'pagebreak':
            # Skip it when a chapter heading follows: Heading1 already breaks the page,
            # and two breaks in a row would leave a genuinely blank page between them.
            nxt = blocks[i + idx + 1] if (i + idx + 1) < len(blocks) else (None, None)
            if not (nxt[0] == 'h1' and str(nxt[1]).startswith('Chapter ')):
                out.append('<w:p><w:pPr><w:spacing w:after="0"/></w:pPr>'
                           '<w:r><w:br w:type="page"/></w:r></w:p>')
        elif kind == 'h1':
            # The template's Heading1 style supplies "Chapter N. " itself (numbering
            # numId 6, lvlText 'Chapter %1. ') and carries pageBreakBefore. So emit the
            # title only, in ONE paragraph, or Word prints the number twice and strands
            # the first line on a page of its own.
            title = re.sub(r'^Chapter \d+\.\s*', '', val)
            out.append(para(runs(title, sz=28, bold_all=True), style='Heading1',
                            spacing="240", keep=True))
        elif kind == 'h2':
            out.append(para(runs(val, sz=26, bold_all=True), style='Heading2',
                            spacing="120", keep=True))
        elif kind == 'h3':
            out.append(para(runs(val, sz=24, bold_all=True), style='Heading3',
                            spacing="120", keep=True))
        elif kind == 'p':
            m = re.match(r'^Figure \d+\.\s*(.*)$', val)
            if m:                                   # figure caption, above the image
                out.append(para(runs(m.group(1), sz=CAPTION_SZ),
                                style='FigureCaption', spacing="60", keep=True))
            else:
                out.append(para(runs(val)))
        elif kind == 'bullet':
            out.append(para('<w:r><w:rPr><w:sz w:val="24"/></w:rPr><w:t xml:space="preserve">•  </w:t></w:r>'
                            + runs(val), style='Bullet',
                            ind='w:left="360" w:hanging="360"', spacing="80"))
        elif kind == 'quote':
            out.append(para(runs(val, sz=22, italic_all=False), style='BlockQuote',
                            ind='w:left="360" w:right="360"', spacing="160"))
        elif kind == 'code':
            for line in val:
                out.append(para(f'<w:r><w:rPr><w:rFonts w:ascii="Courier New" w:hAnsi="Courier New"/>'
                                f'<w:sz w:val="18"/></w:rPr>'
                                f'<w:t xml:space="preserve">{escape(line)}</w:t></w:r>',
                                style='Code', ind='w:left="360"', spacing="0"))
            out.append(para('<w:r><w:t/></w:r>', spacing="120"))
        elif kind == 'ref':
            num, body, annotation = val
            out.append(para(runs(f'{num}.  ' + body, sz=22), style='ReferenceEntry',
                            ind='w:left="720" w:hanging="720"', spacing="40"))
            if annotation:
                out.append(para(runs(annotation.strip('*'), sz=22, italic_all=True),
                                ind='w:left="720"', spacing="140"))
        elif kind == 'figure':
            figure_no += 1
            px_w, px_h = image_px[val]
            cx = int(6.0 * EMU_PER_IN)
            cy = int(cx * px_h / px_w)
            out.append(para(
                '<w:r><w:drawing><wp:inline distT="0" distB="0" distL="0" distR="0">'
                f'<wp:extent cx="{cx}" cy="{cy}"/><wp:docPr id="{figure_no}" name="Figure {figure_no}"/>'
                '<a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">'
                '<a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">'
                '<pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">'
                f'<pic:nvPicPr><pic:cNvPr id="{figure_no}" name="Figure {figure_no}"/><pic:cNvPicPr/></pic:nvPicPr>'
                f'<pic:blipFill><a:blip r:embed="{image_rel[val]}"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
                f'<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm>'
                '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr>'
                '</pic:pic></a:graphicData></a:graphic></wp:inline></w:drawing></w:r>',
                jc='center', spacing="200"))
        elif kind == 'table':
            out.append(build_table(*val))
    sect = ('<w:sectPr><w:pgSz w:w="12240" w:h="15840" w:code="1"/>'
            '<w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="2160" '
            'w:header="720" w:footer="720" w:gutter="0"/>'
            '<w:pgNumType w:start="1"/><w:cols w:space="720"/></w:sectPr>')
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<w:document '
            'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
            'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" '
            'xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" '
            'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
            'xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">'
            f'<w:body>{"".join(out)}{sect}</w:body></w:document>')

# ---------------------------------------------------------------- package

def main():
    md = open(SOURCE, encoding='utf-8').read()
    blocks = parse(md)
    figs = [v for k, v in blocks if k == 'figure']
    image_rel, image_px, media = {}, {}, {}
    for n, fig in enumerate(figs, 1):
        path = os.path.join(ROOT, fig)
        with open(path, 'rb') as fh:
            head = fh.read(32)
        image_px[fig] = (int.from_bytes(head[16:20], 'big'), int.from_bytes(head[20:24], 'big'))
        image_rel[fig] = f'rId90{n}'
        media[fig] = (f'figure{n}.png', path)
    doc = build(blocks, image_rel, image_px)

    src = zipfile.ZipFile(TEMPLATE)
    if os.path.exists(OUTPUT):
        os.remove(OUTPUT)
    with zipfile.ZipFile(OUTPUT, 'w', zipfile.ZIP_DEFLATED) as out:
        for item in src.namelist():
            data = src.read(item)
            if item == 'word/document.xml':
                data = doc.encode('utf-8')
            elif item == 'word/_rels/document.xml.rels':
                x = data.decode('utf-8')
                rels = ''.join(
                    f'<Relationship Id="{image_rel[f]}" Type="http://schemas.openxmlformats.org/'
                    f'officeDocument/2006/relationships/image" Target="media/{media[f][0]}"/>'
                    for f in figs)
                data = x.replace('</Relationships>', rels + '</Relationships>').encode('utf-8')
            elif item == '[Content_Types].xml':
                x = data.decode('utf-8')
                if 'Extension="png"' not in x:
                    x = x.replace('<Types ', '<Types ', 1).replace(
                        '</Types>', '<Default Extension="png" ContentType="image/png"/></Types>')
                data = x.encode('utf-8')
            out.writestr(item, data)
        for f in figs:
            out.write(media[f][1], 'word/media/' + media[f][0])
    print(f"wrote {OUTPUT}")
    print(f"  blocks: {len(blocks)}  tables: {sum(1 for k, _ in blocks if k == 'table')}"
          f"  refs: {sum(1 for k, _ in blocks if k == 'ref')}  figures: {len(figs)}")

if __name__ == '__main__':
    main()
