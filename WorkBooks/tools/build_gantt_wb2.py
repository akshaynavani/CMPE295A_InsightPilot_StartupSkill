#!/usr/bin/env python3
"""Generate assets/ch9_schedule_wb2.png/.svg: the Workbook 2 Gantt chart with status and re-plan.

Same layout as tools/build_gantt.py (Workbook 1 Figure 2): one row per task grouped by sprint,
bars coloured by member, milestones as red dashed verticals, the winter break as a grey band.
Workbook 2 adds status: done bars carry a tick and date, moved bars show a dashed outline in the
originally planned sprint and a solid bar in the new one, new tasks are marked (new), and a
dotted line marks the Workbook 2 date. Dates follow Chapter 8 (Table 18).

Run:  python3 tools/build_gantt_wb2.py
"""
import os
from datetime import date
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.patches import Patch, Rectangle
from matplotlib.lines import Line2D

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "assets", "ch9_schedule_wb2")

AK, AN, PS, SZ = "Atharva Kulkarni", "Akshay Navani", "Pranjal Shrivastava", "Shantanu Zadbuke"
ALL = "Whole team"
COLOR = {AK: "#1f77b4", AN: "#ff7f0e", PS: "#2ca02c", SZ: "#9467bd", ALL: "#7f7f7f"}

S = {
    "S0":  (date(2026, 9, 14), date(2026, 9, 27)),
    "S1":  (date(2026, 9, 28), date(2026, 10, 11)),
    "S2":  (date(2026, 10, 12), date(2026, 10, 25)),
    "S3":  (date(2026, 10, 26), date(2026, 11, 8)),
    "S4":  (date(2026, 11, 9), date(2026, 11, 22)),
    "S5":  (date(2026, 11, 23), date(2026, 12, 6)),
    "S5b": (date(2026, 12, 7), date(2026, 12, 11)),
    "S6":  (date(2027, 1, 25), date(2027, 2, 7)),
    "S7":  (date(2027, 2, 8), date(2027, 2, 21)),
    "S8":  (date(2027, 2, 22), date(2027, 3, 7)),
    "S9":  (date(2027, 3, 8), date(2027, 3, 21)),
    "S10": (date(2027, 3, 22), date(2027, 4, 4)),
    "S11": (date(2027, 4, 5), date(2027, 4, 18)),
    "S12": (date(2027, 4, 19), date(2027, 5, 2)),
}
TODAY = date(2026, 11, 12)
# Actual start dates where work began before the sprint the bar sits in (given by the team).
ACTUAL_START = {
    "Connector profiling": date(2026, 10, 30),
    "Cross-source reconciler profiling": date(2026, 10, 30),
    "Orchestrator dispatch, budgets, retries": date(2026, 10, 30),
}

# (planned sprint, task, owner, status, actual sprint, note)
# status: done | moved | plan | new
TASKS = [
    ("S0", "Literature review, requirements, architecture", ALL, "done", "S0", "Sep 27"),
    ("S1", "Repository, CI/CD, Docker Compose stack", AN, "done", "S1", "Oct 4"),
    ("S1", "PostgreSQL connector (SP-1)", AN, "done", "S1", "Oct 4"),
    ("S1", "Typed plan schema (SP-3)", AK, "done", "S2", "Oct 18"),
    ("S1", "Model client", AK, "moved", "S4", ""),
    ("S1", "Harness skeleton + fixed question set", PS, "moved", "S4", ""),
    ("S1", "Workspace skeleton", SZ, "done", "S1", "Oct 4"),
    ("S1", "Wireframes (reassigned from SZ)", PS, "done", "S1", "Oct 4"),
    ("S2", "CSV / Excel ingestion (SP-2)", AN, "done", "S2", "Oct 18"),
    ("S2", "Application store schema", AN, "moved", "S4", ""),
    ("S2", "Plan synthesiser v1 + static validation", AK, "done", "S2", "Oct 18"),
    ("S2", "Ground truth + seeded-error set", PS, "moved", "S4", ""),
    ("S2", "Plan review and approval screen", SZ, "done", "S2", "Oct 18"),
    ("S3", "Connector profiling", AN, "done", "S4", "Nov 10"),
    ("S3", "Binding store", AN, "moved", "S4", ""),
    ("S3", "Semantic resolver, hybrid retrieval", AK, "moved", "S4", ""),
    ("S3", "Hop verifier checks (SP-4)", PS, "moved", "S4", ""),
    ("S3", "Lineage hop view, replay (SP-5)", SZ, "moved", "S4", ""),
    ("S3", "Workbook 2 design (Chapters 6-7)", ALL, "done", "S3", "Nov 1"),
    ("S4", "Cross-source reconciler profiling", AN, "done", "S4", "Nov 10"),
    ("S4", "Orchestrator dispatch, budgets, retries", AK, "done", "S4", "Nov 10"),
    ("S4", "Fetch agent", AN, "new", "S4", ""),
    ("S4", "Reconciler transform search, proposals", PS, "new", "S4", ""),
    ("S4", "Harness in CI + first accuracy figure (SP-6)", PS, "plan", "S4", ""),
    ("S4", "Append-only audit log", SZ, "plan", "S4", ""),
    ("S4", "Export artifact", SZ, "moved", "S5", ""),
    ("S5", "Quickstart: clone to first investigation", AN, "plan", "S5", ""),
    ("S5", "Ambiguity interception, doubt surfacing", AK, "plan", "S5", ""),
    ("S5", "Silent-error rate, verifier coverage", PS, "plan", "S5", ""),
    ("S5", "Analytics agent", PS, "new", "S5", ""),
    ("S5", "Sign-off state, unreviewed marking", SZ, "plan", "S5", ""),
    ("S5b", "Verification-cost study, 295A report and demo", ALL, "plan", "S5b", ""),
    ("S6", "REST JSON connector", AN, "plan", "S6", ""),
    ("S6", "Replanning on invalidation", AK, "plan", "S6", ""),
    ("S6", "Verifier coverage expansion", PS, "plan", "S6", ""),
    ("S6", "Review queue, searchable history", SZ, "plan", "S6", ""),
    ("S7", "dbt semantic-layer consumption", AN, "plan", "S7", ""),
    ("S7", "Hop override with downstream re-flow", AK, "plan", "S7", ""),
    ("S7", "Cost per investigation by retry count", PS, "plan", "S7", ""),
    ("S7", "Shared investigation link", SZ, "plan", "S7", ""),
    ("S8", "Permission inheritance, schema-only mode", AN, "plan", "S8", ""),
    ("S8", "Plan caching and pinned bindings", AK, "plan", "S8", ""),
    ("S8", "Evaluation of the modelling step", PS, "plan", "S8", ""),
    ("S8", "Visualization agent surface", SZ, "plan", "S8", ""),
    ("S9", "Performance and cost benchmarks", AN, "plan", "S9", ""),
    ("S9", "Time-boxed ML agent", AK, "plan", "S9", ""),
    ("S9", "Robustness tests on plans and prompts", PS, "plan", "S9", ""),
    ("S9", "Model card screen", SZ, "plan", "S9", ""),
    ("S10", "Load and scale tests", AN, "plan", "S10", ""),
    ("S10", "Accuracy ablations", AK, "plan", "S10", ""),
    ("S10", "Usability study with analysts", PS, "plan", "S10", ""),
    ("S10", "Accessibility and interface polish", SZ, "plan", "S10", ""),
    ("S11", "Results and paper draft", ALL, "plan", "S11", ""),
    ("S12", "Final release, docs, demo video, Expo", ALL, "plan", "S12", ""),
]

MILESTONES = [
    (date(2026, 10, 8), "M1 Architecture (achieved)"),
    (date(2026, 11, 22), "M2 Measurement (was Nov 8)"),
    (date(2026, 12, 11), "M3/M4 Narrow path, evidence"),
    (date(2027, 3, 7), "M5 Beta"),
    (date(2027, 5, 7), "M6 Final release"),
]


def label(sp, task, status, actual):
    if status == "moved":
        return f"{sp}  {task}  → {actual}"
    if status == "done" and actual != sp:
        return f"{sp}  {task}  → {actual}"
    if status == "new":
        return f"{actual}  {task}  (new)"
    return f"{sp}  {task}"


def main():
    fig, ax = plt.subplots(figsize=(11.0, 10.2))
    for i, (sp, task, owner, status, actual, note) in enumerate(TASKS):
        c = COLOR[owner]
        if actual != sp:   # dashed outline where it was originally planned
            s0, e0 = S[sp]
            ax.add_patch(Rectangle((mdates.date2num(s0), i - 0.275), (e0 - s0).days, 0.55,
                                   facecolor="none", edgecolor=c, linestyle=(0, (3, 2)),
                                   linewidth=1.0, zorder=3))
        start, end = S[actual]
        start = ACTUAL_START.get(task, start)
        if status == "done":   # a finished task's bar stops on its completion date, not at the sprint end
            from datetime import datetime
            end = datetime.strptime(f"{note} 2026", "%b %d %Y").date()
            end = max(end, start + (date(2026, 1, 2) - date(2026, 1, 1)))
        ax.barh(i, (end - start).days, left=start, height=0.55, color=c, edgecolor="none", zorder=4)
        if status == "done":
            ax.text(end + (date(2026, 1, 3) - date(2026, 1, 1)), i, f"✓ {note}",
                    va="center", ha="left", fontsize=7.2, color="#1f2937", zorder=5)

    ax.set_yticks(range(len(TASKS)))
    ax.set_yticklabels([label(sp, t, st, a) for sp, t, _, st, a, _ in TASKS], fontsize=8.2)
    for tick, (_, _, _, st, _, _) in zip(ax.get_yticklabels(), TASKS):
        if st in ("moved", "new"):
            tick.set_fontweight("bold")
    ax.invert_yaxis()
    ax.set_ylim(len(TASKS) - 0.4, -2.9)

    ax.axvspan(date(2026, 12, 12), date(2027, 1, 24), color="#e8eaed", zorder=0)
    ax.text(date(2027, 1, 2), 6.0, "Winter\nbreak", ha="center", va="center", fontsize=8.5, color="#6b7280")

    ax.axvline(TODAY, color="#111827", linestyle=":", linewidth=1.3, zorder=2)
    ax.text(TODAY, len(TASKS) - 0.9, " Workbook 2\n Nov 12", fontsize=7.5, color="#111827",
            ha="left", va="bottom")

    for k, (d, lab) in enumerate(MILESTONES):
        ax.axvline(d, color="#d62728", linestyle="--", linewidth=1.1, zorder=2)
        ax.text(d, -1.95 if k % 2 == 0 else -0.95, f"◆ {lab}", color="#d62728",
                fontsize=7.5, ha="left", va="center")

    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b\n%Y"))
    ax.set_xlim(date(2026, 9, 7), date(2027, 6, 20))
    ax.tick_params(axis="x", labelsize=8.5)
    ax.grid(axis="x", color="#d7dbe0", linewidth=0.6, zorder=1)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color("#9aa1a9")

    ax.set_title("Project Schedule - 2-week sprints across CMPE 295A (Fall 2026) and 295B (Spring 2027)\n"
                 "updated for Workbook 2 with status and re-plan", fontsize=11, fontweight="bold", pad=30)

    handles = [Patch(facecolor=COLOR[m], label=m) for m in (AK, AN, PS, SZ, ALL)]
    handles += [
        Line2D([], [], color="none", marker="$✓$", markersize=8, markeredgecolor="#1f2937", label="done (date)"),
        Patch(facecolor="none", edgecolor="#6b7280", linestyle=(0, (3, 2)), label="originally planned sprint"),
        Line2D([], [], color="#111827", linestyle=":", label="Workbook 2 (Nov 12)"),
    ]
    ax.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.45, -0.06), ncol=4,
              frameon=False, fontsize=8)

    fig.tight_layout()
    fig.savefig(OUT + ".png", dpi=260, facecolor="white")
    fig.savefig(OUT + ".svg", facecolor="white")
    print(f"wrote {OUT}.png/.svg  ({len(TASKS)} rows)")


if __name__ == "__main__":
    main()
