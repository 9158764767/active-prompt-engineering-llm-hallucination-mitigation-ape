"""
latex_writer.py  –  Rewrite Paper Numbers from Real Results
===========================================================
Reads summary.json produced by experiment.py and rewrites the paper's
tables and key numbers using the REAL measured values.
"""

from pathlib import Path
from src.prompts import STRATEGY_LABELS, STRATEGIES


def write_latex_tables(summary: dict, out_path: Path):
    """
    Generate a .tex file containing all tables from the paper,
    populated with real experimental numbers.
    """
    by_s = summary.get("by_strategy", {})
    dav  = summary.get("domain_ape_vs_baseline", {})
    abl  = summary.get("ablation", {})
    tax  = summary.get("error_taxonomy", {})
    lat  = summary.get("latency", {})
    mk   = summary.get("mcnemar", {})
    super_add = summary.get("super_additive", {})

    lines = []
    lines.append("% ════════════════════════════════════════════════════════════")
    lines.append("% AUTO-GENERATED LaTeX TABLES — REAL EXPERIMENTAL DATA")
    lines.append(f"% Run timestamp: {summary.get('run_timestamp','')}")
    lines.append(f"% Total records: {summary.get('total_records','')}")
    lines.append("% ════════════════════════════════════════════════════════════\n")

    # ── Table II: Overall ────────────────────────────────────────────────────
    lines.append("% ── TABLE II: Overall Results ──────────────────────────────")
    lines.append("\\begin{table}[h]\\centering")
    lines.append("\\caption{Overall Results Across Prompt Strategies (Real Experiment)}")
    lines.append("\\label{tab:overall}")
    lines.append("\\begin{tabular}{lccc}\\toprule")
    lines.append("\\textbf{Prompt Strategy} & \\textbf{HR ↓} & \\textbf{Accuracy ↑} & \\textbf{Faithfulness ↑} \\\\\\midrule")
    for s in STRATEGIES:
        m   = by_s.get(s, {})
        lbl = STRATEGY_LABELS[s]
        hr  = m.get("hallucination_rate_pct", 0)
        ac  = m.get("accuracy_pct", 0)
        fa  = m.get("faithfulness_pct", 0)
        bf  = s == "ape"
        w   = lambda x: f"\\textbf{{{x}}}" if bf else str(x)
        lines.append(f"{w(lbl)} & {w(f'{hr:.1f}\\%')} & {w(f'{ac:.1f}\\%')} & {w(f'{fa:.1f}\\%')} \\\\")
    lines.append("\\bottomrule\\end{tabular}\\end{table}\n")

    # ── Table IV: Domain Breakdown ───────────────────────────────────────────
    lines.append("% ── TABLE IV: Domain Breakdown ─────────────────────────────")
    lines.append("\\begin{table}[h]\\centering")
    lines.append("\\caption{Hallucination Rate by Domain: APE vs. Baseline (Real Data)}")
    lines.append("\\label{tab:domain}")
    lines.append("\\begin{tabular}{lccc}\\toprule")
    lines.append("\\textbf{Domain} & \\textbf{Baseline HR} & \\textbf{APE HR} & \\textbf{Reduction} \\\\\\midrule")
    totals = {"b": [], "a": []}
    for d, vals in dav.items():
        b, a, r = vals["baseline_hr"], vals["ape_hr"], vals["reduction_pct"]
        totals["b"].append(b); totals["a"].append(a)
        lines.append(f"{d.capitalize()} & {b:.1f}\\% & {a:.1f}\\% & {r:.1f}\\% \\\\")
    if totals["b"]:
        avg_b = sum(totals["b"]) / len(totals["b"])
        avg_a = sum(totals["a"]) / len(totals["a"])
        avg_r = (avg_b - avg_a) / avg_b * 100 if avg_b > 0 else 0
        lines.append("\\midrule")
        lines.append(f"\\textbf{{Average}} & \\textbf{{{avg_b:.1f}\\%}} & \\textbf{{{avg_a:.1f}\\%}} & \\textbf{{{avg_r:.1f}\\%}} \\\\")
    lines.append("\\bottomrule\\end{tabular}\\end{table}\n")

    # ── Table V: Ablation ────────────────────────────────────────────────────
    lines.append("% ── TABLE V: Ablation Study ─────────────────────────────────")
    lines.append("\\begin{table}[h]\\centering")
    lines.append("\\caption{Ablation Study: Contribution of Each APE Component (Real Data)}")
    lines.append("\\label{tab:ablation}")
    lines.append("\\begin{tabular}{lcc}\\toprule")
    lines.append("\\textbf{Configuration} & \\textbf{HR ↓} & \\textbf{Accuracy ↑} \\\\\\midrule")
    for s in STRATEGIES:
        m  = abl.get(s, {})
        hr = m.get("hallucination_rate_pct", 0)
        ac = m.get("accuracy_pct", 0)
        lbl = STRATEGY_LABELS[s]
        bf  = s == "ape"
        w   = lambda x: f"\\textbf{{{x}}}" if bf else str(x)
        lines.append(f"{w(lbl)} & {w(f'{hr:.1f}\\%')} & {w(f'{ac:.1f}\\%')} \\\\")
    lines.append("\\bottomrule\\end{tabular}\\end{table}\n")

    # ── Table VI: Latency ────────────────────────────────────────────────────
    lines.append("% ── TABLE VI: Latency & Cost-Benefit ───────────────────────")
    lines.append("\\begin{table}[h]\\centering")
    lines.append("\\caption{Latency and Hallucination Rate per Prompt Strategy (Measured)}")
    lines.append("\\label{tab:latency}")
    lines.append("\\begin{tabular}{lcc}\\toprule")
    lines.append("\\textbf{Method} & \\textbf{Avg Latency (s)} & \\textbf{HR} \\\\\\midrule")
    for s in STRATEGIES:
        m   = lat.get(s, {})
        l_s = m.get("avg_latency_s", 0)
        hr  = m.get("hallucination_rate_pct", 0)
        lines.append(f"{STRATEGY_LABELS[s]} & {l_s:.2f} & {hr:.1f}\\% \\\\")
    lines.append("\\bottomrule\\end{tabular}\\end{table}\n")

    # ── Error Taxonomy ───────────────────────────────────────────────────────
    lines.append("% ── Error Taxonomy (APE residuals) ─────────────────────────")
    lines.append("\\begin{table}[h]\\centering")
    lines.append("\\caption{Residual Hallucination Categories (APE Condition, Real Data)}")
    lines.append("\\label{tab:errors}")
    lines.append("\\begin{tabular}{lcc}\\toprule")
    lines.append("\\textbf{Error Type} & \\textbf{Count} & \\textbf{Share} \\\\\\midrule")
    cat_display = {
        "knowledge_gap":            "Knowledge Gap",
        "reasoning_failure":        "Reasoning Failure",
        "prompt_misinterpretation": "Prompt Misinterpretation",
        "ambiguous_query":          "Ambiguous Query",
    }
    for cat, disp in cat_display.items():
        d = tax.get(cat, {})
        lines.append(f"{disp} & {d.get('count',0)} & {d.get('share_pct',0):.1f}\\% \\\\")
    total_h = tax.get("total_analyzed", 0)
    lines.append("\\midrule")
    lines.append(f"\\textbf{{Total}} & \\textbf{{{total_h}}} & \\textbf{{100\\%}} \\\\")
    lines.append("\\bottomrule\\end{tabular}\\end{table}\n")

    # ── Statistical Tests ────────────────────────────────────────────────────
    lines.append("% ── McNemar's Test Results ──────────────────────────────────")
    lines.append("\\begin{table}[h]\\centering")
    lines.append("\\caption{McNemar's Test: APE vs. Each Strategy (Hallucination, Real Data)}")
    lines.append("\\label{tab:mcnemar}")
    lines.append("\\begin{tabular}{lcccc}\\toprule")
    lines.append("\\textbf{Strategy} & \\textbf{$\\chi^2$} & \\textbf{$p$-value} & \\textbf{$p<0.05$} & \\textbf{$p<0.001$} \\\\\\midrule")
    for s, res in mk.items():
        lbl = STRATEGY_LABELS.get(s, s)
        chi2 = res.get("chi2", 0)
        pv   = res.get("p_value", 1)
        s05  = "Yes" if res.get("significant_at_0.05") else "No"
        s001 = "Yes" if res.get("significant_at_0.001") else "No"
        pv_str = f"< 0.001" if pv < 0.001 else f"{pv:.4f}"
        lines.append(f"{lbl} & {chi2:.4f} & {pv_str} & {s05} & {s001} \\\\")
    lines.append("\\bottomrule\\end{tabular}\\end{table}\n")

    # ── Summary paragraph for paper ──────────────────────────────────────────
    base_hr = by_s.get("baseline", {}).get("hallucination_rate_pct", 0)
    ape_hr  = by_s.get("ape",      {}).get("hallucination_rate_pct", 0)
    ape_acc = by_s.get("ape",      {}).get("accuracy_pct", 0)
    total_n = summary.get("total_records", 0)
    red_pct = round((base_hr - ape_hr) / base_hr * 100, 1) if base_hr > 0 else 0
    is_sa   = super_add.get("is_super_additive", False)

    lines.append("% ── Key Numbers for Abstract/Conclusion ─────────────────────")
    lines.append("% Replace hardcoded numbers in the paper with these real values:")
    lines.append(f"% Total records:           {total_n}")
    lines.append(f"% Baseline HR:             {base_hr:.1f}%")
    lines.append(f"% APE HR:                  {ape_hr:.1f}%")
    lines.append(f"% HR reduction:            {red_pct:.1f}%")
    lines.append(f"% APE Accuracy:            {ape_acc:.1f}%")
    lines.append(f"% Super-additive:          {is_sa}")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        f.write("\n".join(lines))
    print(f"  ✔ {out_path.name}")
    return out_path
