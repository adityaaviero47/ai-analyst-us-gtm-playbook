"""Share of search visibility for an AI data-analyst product's buyer-intent queries.

Input: data/search_audit.csv, one row per query with the domains returned by a web search
(recorded 14 Nov 2026 with a single search engine, so treat it as a snapshot, not a ranking study).
Output: results/share_of_voice.csv, results/summary.json, results/share_of_voice.png
"""
import csv, json
from collections import Counter
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

VENDORS = {  # vendor domains (analytics / BI / AI-analyst products), as opposed to media or research
    "querio.ai": "Querio", "getbruin.com": "Bruin", "basedash.com": "Basedash", "fabi.ai": "Fabi",
    "thoughtspot.com": "ThoughtSpot", "actian.com": "Actian", "scoopanalytics.com": "Scoop",
    "databox.com": "Databox", "knowi.com": "Knowi", "getgalaxy.io": "Galaxy", "databricks.com": "Databricks",
    "domo.com": "Domo", "qlik.com": "Qlik", "luzmo.com": "Luzmo", "snowflake.com": "Snowflake",
    "wisdom.ai": "WisdomAI", "hex.tech": "Hex", "genloop.ai": "Genloop", "genloop.substack.com": "Genloop",
}

rows = list(csv.DictReader(open("data/search_audit.csv")))
non_brand = [r for r in rows if r["intent"] != "brand"]
presence = Counter()
for r in non_brand:
    seen = {VENDORS[d] for d in r["domains_in_results"].split(";") if d in VENDORS}
    presence.update(seen)

n = len(non_brand)
table = sorted(((v, c, round(c / n, 3)) for v, c in presence.items()), key=lambda x: (-x[1], x[0]))
with open("results/share_of_voice.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["vendor", "queries_present", "share_of_queries"]); w.writerows(table)

content_led = ["Querio", "Bruin", "Basedash", "Fabi"]
covered = sum(1 for r in non_brand
              if any(VENDORS.get(d) in content_led for d in r["domains_in_results"].split(";")))
by_intent = Counter(r["intent"] for r in non_brand)
covered_by_intent = Counter(r["intent"] for r in non_brand
                            if any(VENDORS.get(d) in content_led for d in r["domains_in_results"].split(";")))
summary = {
    "queries_non_brand": n,
    "genloop_present_non_brand": presence.get("Genloop", 0),
    "genloop_present_brand_query": any(d.startswith("genloop") for d in rows[-1]["domains_in_results"].split(";")),
    "genloop_own_site_in_brand_query": "genloop.ai" in rows[-1]["domains_in_results"].split(";"),
    "top_vendors": table[:6],
    "queries_with_a_content_led_startup": covered,
    "content_led_share": round(covered / n, 3),
    "queries_by_intent": dict(by_intent),
    "content_led_present_by_intent": {k: f"{covered_by_intent.get(k, 0)} of {v}" for k, v in by_intent.items()},
}
json.dump(summary, open("results/summary.json", "w"), indent=2)

top = table[:8]
plt.figure(figsize=(7, 3.6))
plt.barh([t[0] for t in top][::-1], [t[1] for t in top][::-1], color="#4352E0")
plt.xlabel(f"Buyer-intent queries where the vendor appears (of {n})")
plt.title("Who shows up when US buyers search for an AI data analyst")
plt.tight_layout(); plt.savefig("results/share_of_voice.png", dpi=150)
print(json.dumps(summary, indent=2))
