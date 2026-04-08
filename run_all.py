#!/usr/bin/env python3
"""
run_all.py  –  APE Study: Complete End-to-End Experiment Runner
================================================================
This is the ONLY script you need to run.

What it does:
  1. Runs real API calls for every query × strategy × model combination
  2. Logs EVERY call to logs/raw_calls/<uuid>.json  (proof of real execution)
  3. Evaluates each response with an LLM-as-judge
  4. Computes all paper metrics: HR, Accuracy, Faithfulness, Latency
  5. Runs McNemar's significance tests
  6. Checks super-additive effect
  7. Generates all 6 paper figures as PDF
  8. Writes real-number LaTeX tables
  9. Prints a full summary report

Usage (choose ONE option based on your API access):

  ── Option A: Anthropic (Claude) ───────────────────────────────
  export ANTHROPIC_API_KEY=sk-ant-...
  python run_all.py --model claude-sonnet-4-20250514

  ── Option B: OpenAI (GPT-4o) ──────────────────────────────────
  export OPENAI_API_KEY=sk-...
  python run_all.py --model gpt-4o

  ── Option C: Ollama (FREE, no API key, runs locally) ───────────
  ollama pull llama3:8b          # or: llama3:70b  mistral:7b
  python run_all.py --model llama3:8b

  ── Option D: Multiple models (full paper experiment) ───────────
  python run_all.py \\
      --model gpt-4o gpt-3.5-turbo llama3:70b mistral:7b \\
      --domains all --max-per-domain 15

  ── Quick smoke test (5 queries × 5 strategies = 25 calls) ──────
  python run_all.py --model claude-sonnet-4-20250514 \\
      --domains general --max-per-domain 5

Outputs:
  logs/raw_calls/<uuid>.json     ONE FILE PER API CALL (your proof)
  logs/run_<timestamp>.jsonl     Full run log
  results/all_results.json       All records
  results/summary.json           Aggregate metrics
  results/tables.tex             LaTeX tables with real numbers
  figures/fig1_*.pdf  ...        6 publication figures
"""

import os, sys, json, argparse
from pathlib import Path
from datetime import datetime, timezone
import src.caller as caller_mod

# ── Allow running from any directory ──────────────────────────────────────────
sys.path.insert(0, str(Path(__file__).parent))

from src.dataset     import QUESTIONS
from src.prompts     import STRATEGIES, STRATEGY_LABELS, build_prompt
from src.caller      import call_model, SUPPORTED_MODELS
from src.metrics     import (judge_response, build_summary_tables,
                              check_super_additive, cohens_kappa)
from src.figures     import generate_all as generate_figures
from src.latex_writer import write_latex_tables


DOMAINS = ["general", "finance", "healthcare", "legal"]


# ─────────────────────────────────────────────────────────────────────────────
def parse_args():
    p = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                 description=__doc__)
    p.add_argument("--model",   nargs="+", default=["claude-sonnet-4-20250514"],
                   help="Model(s) to evaluate. See SUPPORTED_MODELS in caller.py")
    p.add_argument("--judge",   default=None,
                   help="Judge model (defaults to same as first --model)")
    p.add_argument("--domains", nargs="+", default=DOMAINS,
                   choices=DOMAINS + ["all"])
    p.add_argument("--strategies", nargs="+", default=STRATEGIES, choices=STRATEGIES)
    p.add_argument("--max-per-domain", type=int, default=15,
                   help="Max queries per domain (default 15 = full dataset)")
    p.add_argument("--temperature", type=float, default=0.0,
                   help="Generation temperature (default 0.0 for determinism)")
    p.add_argument("--max-tokens", type=int, default=1024)
    p.add_argument("--ollama-url", default="http://localhost:11434")
    p.add_argument("--out-dir", default=".", help="Output root directory")
    return p.parse_args()


# ─────────────────────────────────────────────────────────────────────────────
def main():
    args   = parse_args()
    run_id = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")

    # Resolve domains
    domains = DOMAINS if "all" in args.domains else args.domains

    # Setup directories
    out_root = Path(args.out_dir)
    log_dir  = out_root / "logs"
    res_dir  = out_root / "results"
    fig_dir  = out_root / "figures"
    for d in [log_dir / "raw_calls", res_dir, fig_dir]:
        d.mkdir(parents=True, exist_ok=True)

    # Point caller log dir to our location
    caller_mod.LOG_DIR = log_dir / "raw_calls"
    caller_mod.RUNLOG  = log_dir / f"run_{run_id}.jsonl"

    judge_model = args.judge or args.model[0]

    # Filter questions
    questions = [
        q for q in QUESTIONS
        if q["domain"] in domains
    ]
    questions = []
    for d in domains:
        qs = [q for q in QUESTIONS if q["domain"] == d]
        questions.extend(qs[:args.max_per_domain])

    total_calls = len(questions) * len(args.strategies) * len(args.model)

    print(f"""
╔══════════════════════════════════════════════════════════════╗
║         APE HALLUCINATION STUDY  —  EXPERIMENT START         ║
╠══════════════════════════════════════════════════════════════╣
║  Run ID    : {run_id}
║  Models    : {', '.join(args.model)}
║  Judge     : {judge_model}
║  Domains   : {', '.join(domains)}
║  Strategies: {', '.join(args.strategies)}
║  Questions : {len(questions)}  (×{len(args.strategies)} strategies ×{len(args.model)} models)
║  Total gen : {total_calls} API calls  (+{total_calls} judge calls)
║  Logs      : {log_dir}/raw_calls/<uuid>.json
╚══════════════════════════════════════════════════════════════╝
""")

    all_results = []
    done = 0

    for model_id in args.model:
        print(f"\n{'─'*62}")
        print(f"  MODEL: {model_id}")
        print(f"{'─'*62}")

        for strategy in args.strategies:
            s_label = STRATEGY_LABELS[strategy]
            print(f"\n  ▸ Strategy: {s_label}")

            for q in questions:
                done += 1
                total_all = len(questions) * len(args.strategies) * len(args.model)
                print(f"    [{done:3d}/{total_all}] {q['id']} [{q['difficulty']}] {q['query'][:55]}...")

                # ── Build exact prompt ───────────────────────────────────
                messages = build_prompt(q["query"], strategy, q["domain"])

                # ── Real API call ─────────────────────────────────────────
                gen = call_model(
                    messages=messages,
                    model_id=model_id,
                    temperature=args.temperature,
                    max_tokens=args.max_tokens,
                    ollama_url=args.ollama_url,
                )
                if gen.get("error"):
                    print(f"         ⚠ Gen error: {gen['error'][:70]}")

                # ── LLM-as-Judge evaluation ───────────────────────────────
                eval_r = judge_response(
                    query=q["query"],
                    ground_truth=q["ground_truth"],
                    response=gen.get("response_text", ""),
                    judge_model=judge_model,
                    ollama_url=args.ollama_url,
                )

                # ── Full provenance record ────────────────────────────────
                record = {
                    # Query identity
                    "query_id":           q["id"],
                    "query":              q["query"],
                    "ground_truth":       q["ground_truth"],
                    "domain":             q["domain"],
                    "difficulty":         q["difficulty"],
                    "source":             q.get("source", ""),
                    # Experiment config
                    "run_id":             run_id,
                    "model":              model_id,
                    "strategy":           strategy,
                    "strategy_label":     s_label,
                    "temperature":        args.temperature,
                    # Provenance (from generation call)
                    "call_id":            gen["call_id"],
                    "timestamp_utc":      gen["timestamp_utc"],
                    "provider":           gen.get("provider", ""),
                    # Full prompt + response
                    "prompt_messages":    messages,
                    "response_text":      gen.get("response_text", ""),
                    # Token counts (PROOF of real API call)
                    "input_tokens":       gen.get("input_tokens", 0),
                    "output_tokens":      gen.get("output_tokens", 0),
                    "latency_ms":         gen.get("latency_ms", 0),
                    "gen_error":          gen.get("error"),
                    # Evaluation
                    "judge_model":        judge_model,
                    "judge_call_id":      eval_r.get("judge_call_id"),
                    "is_hallucinated":    bool(eval_r.get("is_hallucinated", True)),
                    "is_accurate":        bool(eval_r.get("is_accurate", False)),
                    "faithfulness_score": float(eval_r.get("faithfulness_score", 0.0)),
                    "error_category":     eval_r.get("error_category", "knowledge_gap"),
                    "judge_explanation":  eval_r.get("explanation", ""),
                }

                all_results.append(record)

                # ── Inline status ──────────────────────────────────────────
                marker = "✗ HALLUC" if record["is_hallucinated"] else "✓ OK    "
                tok_in  = record["input_tokens"]
                tok_out = record["output_tokens"]
                lat_s   = record["latency_ms"] / 1000
                print(f"         {marker} | acc={record['is_accurate']} | "
                      f"faith={record['faithfulness_score']:.2f} | "
                      f"{lat_s:.2f}s | {tok_in}+{tok_out}tok")

    # ─────────────────────────────────────────────────────────────────────────
    # Save raw results
    # ─────────────────────────────────────────────────────────────────────────
    results_path = res_dir / "all_results.json"
    with open(results_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\n✔ {len(all_results)} records → {results_path}")

    # ─────────────────────────────────────────────────────────────────────────
    # Compute summary tables
    # ─────────────────────────────────────────────────────────────────────────
    print("\n📐 Computing metrics...")
    summary = build_summary_tables(
        all_results, args.strategies, args.model, domains
    )
    # Add super-additive check
    summary["super_additive"] = check_super_additive(summary["by_strategy"])
    summary["run_timestamp"]  = datetime.now(timezone.utc).isoformat()
    summary["total_records"]  = len(all_results)
    summary["run_id"]         = run_id
    summary["models"]         = args.model
    summary["domains"]        = domains
    summary["strategies"]     = args.strategies

    summary_path = res_dir / "summary.json"
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"✔ Summary → {summary_path}")

    # ─────────────────────────────────────────────────────────────────────────
    # Print full results tables
    # ─────────────────────────────────────────────────────────────────────────
    _print_results(summary, args.strategies, domains)

    # ─────────────────────────────────────────────────────────────────────────
    # Generate figures
    # ─────────────────────────────────────────────────────────────────────────
    generate_figures(all_results, summary, fig_dir)

    # ─────────────────────────────────────────────────────────────────────────
    # Write LaTeX tables
    # ─────────────────────────────────────────────────────────────────────────
    write_latex_tables(summary, res_dir / "real_tables.tex")
    print(f"✔ LaTeX tables → {res_dir}/real_tables.tex")

    # ─────────────────────────────────────────────────────────────────────────
    # Provenance verification summary
    # ─────────────────────────────────────────────────────────────────────────
    raw_files = list((log_dir / "raw_calls").glob("*.json"))
    print(f"""
╔══════════════════════════════════════════════════════════════╗
║              EXPERIMENT COMPLETE — PROOF SUMMARY             ║
╠══════════════════════════════════════════════════════════════╣
║  Run ID         : {run_id}
║  Total records  : {len(all_results)}
║  Raw call logs  : {len(raw_files)} files in logs/raw_calls/
║  Run JSONL      : logs/run_{run_id}.jsonl
║  Results JSON   : results/all_results.json
║  Summary JSON   : results/summary.json
║  LaTeX tables   : results/real_tables.tex
║  Figures        : figures/ (6 PDFs)
╠══════════════════════════════════════════════════════════════╣
║  To verify: python verify_provenance.py
╚══════════════════════════════════════════════════════════════╝
""")
    return summary


# ─────────────────────────────────────────────────────────────────────────────
def _print_results(summary, strategies, domains):
    by_s  = summary.get("by_strategy", {})
    mk    = summary.get("mcnemar", {})
    sa    = summary.get("super_additive", {})
    dav   = summary.get("domain_ape_vs_baseline", {})

    print("\n" + "═"*66)
    print("  TABLE II: Overall Results by Strategy")
    print("═"*66)
    print(f"  {'Strategy':<26} {'HR ↓':>7} {'Acc ↑':>8} {'Faith ↑':>9} {'N':>5}")
    print("  " + "─"*60)
    for s in strategies:
        m = by_s.get(s, {})
        marker = " ◀" if s == "ape" else ""
        print(f"  {STRATEGY_LABELS[s]:<26} "
              f"{m.get('hallucination_rate_pct',0):>6.1f}% "
              f"{m.get('accuracy_pct',0):>7.1f}% "
              f"{m.get('faithfulness_pct',0):>8.1f}% "
              f"{m.get('n',0):>5}{marker}")
    base_hr = by_s.get("baseline",{}).get("hallucination_rate_pct",0)
    ape_hr  = by_s.get("ape",{}).get("hallucination_rate_pct",0)
    red     = (base_hr - ape_hr) / base_hr * 100 if base_hr > 0 else 0
    print(f"\n  ► APE reduces hallucination by {red:.1f}% relative to baseline")
    print(f"  ► Super-additive: {sa.get('is_super_additive', '?')}")

    print("\n" + "═"*60)
    print("  TABLE IV: Domain Breakdown — Baseline vs. APE")
    print("═"*60)
    print(f"  {'Domain':<14} {'Base HR':>9} {'APE HR':>9} {'Reduction':>11}")
    print("  " + "─"*46)
    for d in domains:
        v = dav.get(d, {})
        print(f"  {d.capitalize():<14} "
              f"{v.get('baseline_hr',0):>8.1f}% "
              f"{v.get('ape_hr',0):>8.1f}% "
              f"{v.get('reduction_pct',0):>10.1f}%")

    if mk:
        print("\n" + "═"*60)
        print("  McNemar's Test: APE vs. Each Strategy")
        print("═"*60)
        print(f"  {'Strategy':<24} {'χ²':>8} {'p-value':>12} {'p<0.001':>9}")
        print("  " + "─"*56)
        for s, res in mk.items():
            pv  = res.get("p_value", 1)
            pv_str = "< 0.001" if pv < 0.001 else f"{pv:.5f}"
            sig = "Yes ✓" if res.get("significant_at_0.001") else "No"
            print(f"  {STRATEGY_LABELS.get(s,s):<24} "
                  f"{res.get('chi2',0):>8.4f} "
                  f"{pv_str:>12} "
                  f"{sig:>9}")


if __name__ == "__main__":
    main()
