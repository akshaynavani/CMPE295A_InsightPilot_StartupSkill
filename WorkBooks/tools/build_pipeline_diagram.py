#!/usr/bin/env python3
"""Chapter 7 figure: evaluation and CI pipeline (SVG, PDF, PNG).

Drawn in the card-and-lane language of Workbook 1 Figure 1 (tinted lanes, white cards with
a bold name, two function lines and a grey tools line, labelled arrows between lanes) using
the shared helpers in uml_common.py. Content follows Chapter 7: the test levels run on
every pull request, the evaluation harness (D08), periodic human evaluation, and release.
"""
from uml_common import Drawer

STEM = 'ch7_pipeline'
WIDTH = 1440
LANE_X, LANE_W = 20, 1400
CARD_H, LANE_H, LANE_GAP = 100, 150, 46

# (title, colour, tint, cards[(name, line1, line2, tools)], dashed)
LANES = [
    ('EVERY PULL REQUEST: GITHUB ACTIONS (ALL JOBS MUST PASS TO MERGE)', '#3974bb', '#eff6ff', [
        ('Static analysis', 'Lint, format, strict types', 'Python and TypeScript', 'ruff · mypy · tsc · eslint'),
        ('Unit and contract', 'Plan schema and validation', 'StepResult, connector contract', 'pytest'),
        ('Integration', 'Real PostgreSQL 16 and DuckDB', 'Read-only enforced; audit written', 'pytest · Docker Compose'),
        ('Agent end-to-end', 'Plan → agents → verify → hop', 'Recorded model responses', 'pytest · model fixtures'),
        ('UI end-to-end', 'Ask, approve, inspect, sign off', 'Accessibility checks', 'Playwright · axe-core'),
        ('Security', 'Secrets, dependencies, images', 'Every write attempt must fail', 'gitleaks · scanners'),
    ], False),
    ('EVALUATION HARNESS: ON EVERY PULL REQUEST AND NIGHTLY', '#c47c20', '#fff7ed', [
        ('Question and defect sets', '30–50 questions, ground truth', '8 seeded-defect classes (D1–D8)', 'YAML + Parquet fixtures'),
        ('Harness runner', 'Replay on PRs (recorded responses)', 'Live nightly: 5 trials per question', 'pytest · Docker Compose'),
        ('System under test', 'Full pipeline, frontier model', 'Verifier on and off (B1)', 'InsightPilot'),
        ('Scoring', 'Accuracy · silent errors · coverage', 'False alarms · pass^k (k = 1–5) · cost', 'Python · bootstrap CIs'),
        ('Gate and report', 'Fails if accuracy, coverage', 'or false-alarm rate regress', 'GitHub Actions'),
    ], False),
    ('RELEASE AND DEPLOYMENT: SINGLE-TENANT, SELF-HOSTED', '#319763', '#f0fdf4', [
        ('Merge to main', 'Reviewed pull request', 'All jobs and harness green', 'GitHub'),
        ('Build and tag images', 'Versioned, pinned images', 'Backup before migrations', 'Docker'),
        ('One-command quickstart', 'docker compose up + demo data', 'Clone to first answer < 30 min', 'Docker Compose'),
        ('Expo demo deployment', 'One organisation per stack', 'Seeded demo schema', 'Docker Compose'),
    ], False),
    ('PERIODIC HUMAN EVALUATION: NOT IN CI', '#64748b', '#f1f5f9', [
        ('Verification-cost study', 'Five analysts, timed sessions', 'Check vs derive (NFR-10)', 'moderated sessions'),
        ('Seeded-defect review', 'Reject planted defects', 'With and without trace (NFR-09)', 'moderated sessions'),
        ('Usability walkthrough', 'Ask, approve, inspect, sign off', 'Findings fed into the backlog', 'think-aloud sessions'),
    ], False),
]
BETWEEN = [  # labels on the arrows from lane i to lane i+1 (down = solid, up = dashed reply)
    ('harness job runs on the same pull request', 'failing test or regression blocks the merge'),
    ('all jobs green: merge and release', 'release candidate under test'),
    ('release used for studies (Dec 7–11)', 'findings become backlog items'),
]


def build():
    height = 92 + len(LANES)*LANE_H + (len(LANES)-1)*LANE_GAP + 70
    d = Drawer(WIDTH, height, STEM, 'InsightPilot - evaluation and CI pipeline')
    d.text(WIDTH/2, 34, 'InsightPilot: Evaluation and CI Pipeline', 22, 'b', '#334155', 'middle')
    d.text(WIDTH/2, 58, 'Test levels on every pull request · evaluation harness · release · periodic human evaluation', 13, 'n', '#334155', 'middle')
    y = 80
    for i, (title, colour, tint, cards, dashed) in enumerate(LANES):
        d.rect(LANE_X, y, LANE_W, LANE_H, colour, tint, radius=6, lw=1.4)
        d.text(LANE_X + 12, y + 21, title, 12, 'b', colour, 'start', max_w=LANE_W - 24)
        n = len(cards)
        gap = 22
        cw = (LANE_W - 28 - gap*(n-1)) / n
        for j, (name, l1, l2, tools) in enumerate(cards):
            cx = LANE_X + 14 + j*(cw + gap)
            cy = y + 34
            d.rect(cx, cy, cw, CARD_H, colour, '#ffffff', dashed, radius=3, lw=1.4)
            mid = cx + cw/2
            d.text(mid, cy + 21, name, 13, 'b', '#1f2937', 'middle', max_w=cw - 12)
            d.text(mid, cy + 44, l1, 11.5, 'n', '#334155', 'middle', max_w=cw - 12)
            d.text(mid, cy + 61, l2, 11.5, 'n', '#334155', 'middle', max_w=cw - 12)
            d.text(mid, cy + 86, tools, 10.5, 'n', '#64748b', 'middle', max_w=cw - 12)
            if j < n - 1:   # left-to-right flow inside a lane
                ax = cx + cw + 3
                d.seg([(ax, cy + CARD_H/2), (ax + gap - 6, cy + CARD_H/2)])
                d.poly([(ax + gap - 4, cy + CARD_H/2), (ax + gap - 11, cy + CARD_H/2 - 4),
                        (ax + gap - 11, cy + CARD_H/2 + 4)], '#64748b')
        if i < len(BETWEEN):
            gy = y + LANE_H
            down, up = BETWEEN[i]
            d.seg([(270, gy + 3), (270, gy + LANE_GAP - 4)])
            d.poly([(270, gy + LANE_GAP - 2), (265, gy + LANE_GAP - 10), (275, gy + LANE_GAP - 10)], '#64748b')
            d.text(284, gy + 27, down, 11, 'n', '#334155', 'start')
            d.seg([(760, gy + LANE_GAP - 4), (760, gy + 4)], dashed=True)
            d.poly([(760, gy + 2), (755, gy + 10), (765, gy + 10)], '#64748b')
            d.text(774, gy + 27, up, 11, 'n', '#334155', 'start')
        y += LANE_H + LANE_GAP
    d.text(LANE_X, y + 8, 'KEY: Solid arrow = the run proceeds; dashed arrow = feedback. Cards run left to right within a lane. B1 = verifier-off baseline (Table 12).', 11.5, 'n', '#475569', 'start', max_w=LANE_W)
    d.text(LANE_X, y + 30, 'Requirements: FR-01, FR-02 and NFR-14 (harness in CI on every pull request); NFR-13 and FR-27 (quickstart); NFR-09 and NFR-10 (human studies).', 11, 'i', '#64748b', 'start', max_w=LANE_W)
    d.save()
    print(f'Built {STEM}: {len(LANES)} lanes, {sum(len(l[3]) for l in LANES)} cards')


if __name__ == '__main__':
    build()
