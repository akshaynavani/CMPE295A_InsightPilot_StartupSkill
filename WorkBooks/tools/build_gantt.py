#!/usr/bin/env python3
"""Generate assets/ch9_schedule.png — the Chapter 9 Gantt chart.

Laid out the way the reference workbook's Figure 2 is: one row per task, grouped by
sprint, bars coloured by team member, milestones as red dashed verticals labelled
across the top, the winter break as a grey band, months along the x axis, and a
colour legend underneath.

Run:  python3 tools/build_gantt.py
"""
import os
from datetime import date
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.patches import Patch

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "assets", "ch9_schedule.png")

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

TASKS = [
    ("S0", "Literature review, requirements, architecture", ALL),
    ("S1", "Repository, CI/CD, Docker Compose stack", AN),
    ("S1", "Typed plan schema + model client spike", AK),
    ("S1", "Harness skeleton + fixed question set", PS),
    ("S1", "Workspace skeleton, wireframes", SZ),
    ("S2", "CSV / Excel ingestion, application store", AN),
    ("S2", "Plan synthesiser v1 + static validation", AK),
    ("S2", "Ground truth + seeded-error set", PS),
    ("S2", "Plan review and approval screen", SZ),
    ("S3", "Connector profiling, binding store", AN),
    ("S3", "Semantic resolver, hybrid retrieval", AK),
    ("S3", "Hop verifier checks + coverage run", PS),
    ("S3", "Lineage inspector hop view, replay", SZ),
    ("S4", "Cross-source reconciler profiling", AN),
    ("S4", "Orchestrator dispatch, budgets, retries", AK),
    ("S4", "Harness in CI + first accuracy figure", PS),
    ("S4", "Export artifact + audit log", SZ),
    ("S5", "Quickstart: clone to first investigation", AN),
    ("S5", "Ambiguity interception, doubt surfacing", AK),
    ("S5", "Silent-error rate, verifier coverage", PS),
    ("S5", "Sign-off state, unreviewed marking", SZ),
    ("S5b", "Verification-cost study, 295A report and demo", ALL),
    ("S6", "REST JSON connector", AN),
    ("S6", "Replanning on invalidation", AK),
    ("S6", "Verifier coverage expansion", PS),
    ("S6", "Review queue, searchable history", SZ),
    ("S7", "dbt semantic-layer consumption", AN),
    ("S7", "Hop override with downstream re-flow", AK),
    ("S7", "Cost per investigation by retry count", PS),
    ("S7", "Shared investigation link", SZ),
    ("S8", "Permission inheritance, schema-only mode", AN),
    ("S8", "Plan caching and pinned bindings", AK),
    ("S8", "Evaluation of the modelling step", PS),
    ("S8", "Visualization agent surface", SZ),
    ("S9", "Performance and cost benchmarks", AN),
    ("S9", "Time-boxed ML agent", AK),
    ("S9", "Robustness tests on plans and prompts", PS),
    ("S9", "Model card screen", SZ),
    ("S10", "Load and scale tests", AN),
    ("S10", "Accuracy ablations", AK),
    ("S10", "Usability study with analysts", PS),
    ("S10", "Accessibility and interface polish", SZ),
    ("S11", "Results and paper draft", ALL),
    ("S12", "Final release, docs, demo video, Expo", ALL),
]

MILESTONES = [
    (date(2026, 10, 8), "M1 Architecture"),
    (date(2026, 11, 8), "M2 Measurement"),
    (date(2026, 12, 11), "M3/M4 Narrow path"),
    (date(2027, 3, 7), "M5 Beta"),
    (date(2027, 5, 7), "M6 Final release"),
]


def main():
    fig, ax = plt.subplots(figsize=(11.0, 8.8))
    for i, (sp, task, owner) in enumerate(TASKS):
        start, end = S[sp]
        ax.barh(i, (end - start).days, left=start, height=0.55,
                color=COLOR[owner], edgecolor="none", zorder=3)

    ax.set_yticks(range(len(TASKS)))
    ax.set_yticklabels([f"{sp}  {task}" for sp, task, _ in TASKS], fontsize=8.5)
    ax.invert_yaxis()
    ax.set_ylim(len(TASKS) - 0.4, -2.9)

    ax.axvspan(date(2026, 12, 12), date(2027, 1, 24), color="#e8eaed", zorder=0)
    ax.text(date(2027, 1, 2), 4.0, "Winter\nbreak", ha="center", va="center",
            fontsize=8.5, color="#6b7280")

    for k, (d, label) in enumerate(MILESTONES):
        ax.axvline(d, color="#d62728", linestyle="--", linewidth=1.1, zorder=2)
        # two levels, so a label can never run into its neighbour
        ax.text(d, -1.95 if k % 2 == 0 else -0.95, f"\u25c6 {label}",
                color="#d62728", fontsize=7.5, ha="left", va="center")

    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b\n%Y"))
    ax.set_xlim(date(2026, 9, 7), date(2027, 6, 20))
    ax.tick_params(axis="x", labelsize=8.5)
    ax.grid(axis="x", color="#d7dbe0", linewidth=0.6, zorder=1)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color("#9aa1a9")

    ax.set_title("Project Schedule - 2-week sprints across CMPE 295A (Fall 2026) "
                 "and 295B (Spring 2027)", fontsize=11, fontweight="bold", pad=30)

    handles = [Patch(facecolor=COLOR[m], label=m) for m in (AK, AN, PS, SZ, ALL)]
    ax.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.5, -0.06),
              ncol=5, frameon=False, fontsize=8)

    fig.tight_layout()
    fig.savefig(OUT, dpi=260, facecolor="white")
    print(f"wrote {OUT}  ({len(TASKS)} task rows, {len(MILESTONES)} milestones)")


if __name__ == "__main__":
    main()
