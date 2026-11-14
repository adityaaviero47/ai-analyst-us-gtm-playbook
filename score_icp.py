"""Weighted ICP scorecard. Scores (1-5) and weights are hypotheses to test with outreach, not measurements."""
import csv, json

WEIGHTS = {"warehouse_fit": 0.25, "analyst_bottleneck": 0.25, "needs_self_hosting": 0.20,
           "organic_reach": 0.15, "sales_speed": 0.15}

def rank(weights):
    rows = list(csv.DictReader(open("data/icp_segments.csv")))
    for r in rows:
        r["score"] = round(sum(float(r[k]) * w for k, w in weights.items()), 2)
    return sorted(rows, key=lambda r: -r["score"])

base = rank(WEIGHTS)
with open("results/icp_ranking.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["rank", "segment", "score"])
    for i, r in enumerate(base, 1): w.writerow([i, r["segment"], r["score"]])

# Sensitivity: how the leader changes if the self-hosting edge matters more or less
sens = {}
for sh in (0.10, 0.20, 0.30):
    rest = (1 - sh) / (1 - WEIGHTS["needs_self_hosting"])
    wts = {k: (sh if k == "needs_self_hosting" else v * rest) for k, v in WEIGHTS.items()}
    top = rank(wts)[:2]
    sens[f"self_hosting_weight_{sh}"] = [(r["segment"], r["score"]) for r in top]

out = {"weights": WEIGHTS, "ranking": [(r["segment"], r["score"]) for r in base], "sensitivity_top2": sens}
json.dump(out, open("results/icp_summary.json", "w"), indent=2)
print(json.dumps(out, indent=2))
