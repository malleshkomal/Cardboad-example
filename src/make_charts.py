"""Static PNG charts for the README (reads data/dashboard_data.json)."""
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = os.path.join(ROOT, "assets", "charts")
os.makedirs(OUT, exist_ok=True)
D = json.load(open(os.path.join(ROOT, "data", "dashboard_data.json"), encoding="utf-8"))

# Validated categorical order (blue, orange, aqua, yellow) + chrome
BLUE, ORANGE, AQUA, YELLOW = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"
INK, INK2, MUTED, GRID, SURF = "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#fcfcfb"
RAMP = ["#104281", "#256abf", "#5598e7", "#86b6ef"]  # ordinal: A (dark) → D (light)

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 10, "text.color": INK, "axes.labelcolor": INK2,
    "axes.edgecolor": GRID, "xtick.color": MUTED, "ytick.color": INK2, "axes.facecolor": SURF,
    "figure.facecolor": SURF, "axes.spines.top": False, "axes.spines.right": False, "axes.grid": True,
    "grid.color": GRID, "grid.linewidth": 0.6, "axes.axisbelow": True,
})


def fmt_t(v):
    return f"{v/1000:,.0f}k" if abs(v) >= 1000 else f"{v:,.0f}"


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, name), dpi=160)
    plt.close(fig)


def title(ax, t, sub):
    ax.set_title(t, loc="left", fontsize=13, fontweight="bold", pad=22)
    ax.text(0, 1.02, sub, transform=ax.transAxes, fontsize=9, color=INK2)


# 1 Scope split -----------------------------------------------------------
s = D["summary"]
vals = [s["Scope 1"], s["Scope 2 – market-based"], s["Scope 3"]]
labels = ["Scope 1 – direct", "Scope 2 – electricity (MB)", "Scope 3 – value chain"]
tot = sum(vals)
fig, ax = plt.subplots(figsize=(10, 2.6))
left = 0
for v, l, c in zip(vals, labels, [BLUE, ORANGE, AQUA]):
    ax.barh(0, v, left=left, color=c, height=0.5, edgecolor=SURF, linewidth=2)
    ax.text(left + v / 2, 0, f"{l}\n{v/1000:,.0f}k t · {v/tot:.0%}", ha="center", va="center",
            color="white", fontsize=9.5, fontweight="bold")
    left += v
ax.set_xlim(0, tot); ax.set_yticks([]); ax.grid(False)
ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: fmt_t(x)))
ax.spines["left"].set_visible(False)
title(ax, f"Corporate footprint {D['year']}: {tot/1000:,.0f}k t CO₂e", "GHG Protocol · Scope 2 market-based · fictional data")
save(fig, "01_scope_split.png")

# 2 Scope 3 categories ----------------------------------------------------
cats = sorted([c for c in D["scope3_categories"] if c["t_co2e"] > 0], key=lambda c: c["t_co2e"])
fig, ax = plt.subplots(figsize=(10, 4.6))
y = range(len(cats))
ax.barh(list(y), [c["t_co2e"] for c in cats], color=BLUE, height=0.62)
ax.set_yticks(list(y)); ax.set_yticklabels([c["category"] for c in cats])
for i, c in enumerate(cats):
    ax.text(c["t_co2e"], i, f"  {c['t_co2e']/1000:,.1f}k · {c['share']:.0%}", va="center", fontsize=9, color=INK2)
ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: fmt_t(x)))
ax.set_xlim(0, max(c["t_co2e"] for c in cats) * 1.22); ax.grid(axis="y", visible=False)
ax.set_xlabel("t CO₂e")
title(ax, "Scope 3 by category", "Cat 8, 11, 13-15 assessed as not relevant · categories with emissions shown")
save(fig, "02_scope3_categories.png")

# 3 PCF hotspots (small multiples) ----------------------------------------
stage_c = {"A1": BLUE, "A2": ORANGE, "A3": AQUA}
prods = [("board", "Recycled cartonboard", "kg CO₂e / t", 1), ("carton", "Folding carton", "kg CO₂e / t", 1),
         ("gypsum", "Gypsum board", "kg CO₂e / m²", 1000)]
fig, axes = plt.subplots(1, 3, figsize=(15, 5.2))
for ax, (k, name, unit, div) in zip(axes, prods):
    items = sorted([i for i in D["pcf"][k]["items"] if i["kg_co2e"] > 0.5], key=lambda i: i["kg_co2e"])[-8:]
    yy = range(len(items))
    ax.barh(list(yy), [i["kg_co2e"] / div for i in items], color=[stage_c[i["stage"][:2]] for i in items], height=0.62)
    ax.set_yticks(list(yy))
    ax.set_yticklabels([i["input"].split(" (")[0][:40] for i in items], fontsize=8.5)
    ax.grid(axis="y", visible=False)
    total = D["pcf"][k]["total"] / div
    ax.set_title(f"{name}\n{total:,.2f} {unit}" if div > 1 else f"{name}\n{total:,.0f} {unit}", loc="left",
                 fontsize=11, fontweight="bold")
    ax.set_xlabel(unit)
fig.legend(handles=[Patch(color=BLUE, label="A1 Raw materials"), Patch(color=ORANGE, label="A2 Transport"),
                    Patch(color=AQUA, label="A3 Manufacturing")], loc="upper right", ncol=3, frameon=False)
fig.suptitle("Product carbon footprints – hotspots (cradle-to-gate, top 8 inputs)", x=0.01, ha="left",
             fontsize=13, fontweight="bold")
save(fig, "03_pcf_hotspots.png")

# 4 MACC ---------------------------------------------------------------------
lv = sorted([l for l in D["levers"] if isinstance(l["cost_eur_t"], (int, float))], key=lambda l: l["cost_eur_t"])
scope_c = {"S1": BLUE, "S2": ORANGE, "S3-1": AQUA, "S3-4": AQUA, "Mixed": YELLOW}
fig, ax = plt.subplots(figsize=(12, 5.2))
x = 0
for l in lv:
    w, h = l["reduction_t"], l["cost_eur_t"]
    ax.bar(x, h, width=w, align="edge", color=scope_c[l["scope"]], edgecolor=SURF, linewidth=2)
    if w > 6000:
        ax.text(x + w / 2, h + (12 if h >= 0 else -12), l["id"], ha="center", va="bottom" if h >= 0 else "top", fontsize=9, color=INK2)
    else:
        ax.text(x + w / 2, max(h, 0) + 12, l["id"], ha="center", va="bottom", fontsize=7.5, color=INK2, rotation=90)
    x += w
ax.axhline(0, color="#c3c2b7", linewidth=1)
ax.axhline(100, color=INK2, linewidth=1, linestyle="--")
ax.text(x * 0.33, 108, "Reference CO₂ price 100 EUR/t", ha="center", fontsize=8.5, color=INK2)
ax.set_xlim(0, x * 1.01)
ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, p: fmt_t(v)))
ax.set_xlabel("Cumulative reduction potential (t CO₂e / yr)"); ax.set_ylabel("Abatement cost (EUR / t CO₂e)")
ax.grid(axis="x", visible=False)
ax.legend(handles=[Patch(color=BLUE, label="Scope 1"), Patch(color=ORANGE, label="Scope 2"),
                   Patch(color=AQUA, label="Scope 3"), Patch(color=YELLOW, label="Mixed")], frameon=False, loc="upper left")
title(ax, "Marginal abatement cost curve (MACC)", "Bar width = annual reduction · height = cost per tonne · below zero = net saving")
save(fig, "04_macc.png")

# 5 Supplier scorecard ---------------------------------------------------
sup = sorted(D["suppliers"], key=lambda s: s["score"])
rc = {"A": RAMP[0], "B": RAMP[1], "C": RAMP[2], "D": RAMP[3]}
fig, ax = plt.subplots(figsize=(10, 6))
yy = range(len(sup))
ax.barh(list(yy), [s["score"] for s in sup], color=[rc[s["rating"][0]] for s in sup], height=0.62)
ax.set_yticks(list(yy)); ax.set_yticklabels([f"{s['id']} {s['name']}" for s in sup], fontsize=8.5)
for i, s_ in enumerate(sup):
    ax.text(s_["score"] + 0.8, i, f"{s_['score']:.0f} · {s_['rating'][0]}", va="center", fontsize=8.5, color=INK2)
for t, l in [(40, "C"), (55, "B"), (70, "A")]:
    ax.axvline(t, color=MUTED, linestyle=":", linewidth=1)
    ax.text(t, len(sup) - 0.3, f" {l} ≥ {t}", fontsize=8, color=INK2)
ax.set_xlim(0, 100); ax.grid(axis="y", visible=False); ax.set_xlabel("Weighted ESG score (0-100)")
ax.legend(handles=[Patch(color=rc[k], label=v) for k, v in
                   [("A", "A – Strategic partner"), ("B", "B – Develop"), ("C", "C – Improvement plan"), ("D", "D – Escalate")]],
          frameon=False, loc="lower right", fontsize=8.5)
title(ax, "Supplier ESG scorecard", "EcoVadis themes + climate maturity (SBTi, PCF, ISO 14001/50001)")
save(fig, "05_supplier_scorecard.png")

# 6 Supplier data coverage -------------------------------------------------
basis = ["Supplier-specific", "Secondary (DQR fail)", "Secondary (no PCF)"]
em = [sum(s["t_co2e"] for s in D["suppliers"] if s["data_basis"] == b) for b in basis]
n = [sum(1 for s in D["suppliers"] if s["data_basis"] == b) for b in basis]
fig, ax = plt.subplots(figsize=(10, 2.6))
left, tot = 0, sum(em)
for v, b, c, k in zip(em, basis, [AQUA, ORANGE, "#c3c2b7"], n):
    ax.barh(0, v, left=left, color=c, height=0.5, edgecolor=SURF, linewidth=2)
    ax.text(left + v / 2, 0, f"{b}\n{v/tot:.0%} · {k} suppliers", ha="center", va="center",
            color="white" if c != "#c3c2b7" else INK, fontsize=9.5, fontweight="bold")
    left += v
ax.set_xlim(0, tot); ax.set_yticks([]); ax.grid(False); ax.spines["left"].set_visible(False)
ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: fmt_t(x)))
title(ax, "Cat 1 emissions by data basis (target ≥ 50 % supplier-specific)", "Supplier PCF accepted only if PACT DQR ≤ 3.0")
save(fig, "06_supplier_data_coverage.png")
print(sorted(os.listdir(OUT)))
