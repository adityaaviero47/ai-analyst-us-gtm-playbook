# US Go-to-Market Playbook: AI Data Analyst for Business Teams

A first-draft organic GTM plan for an AI data analyst that lets business teams ask questions of their SQL data in plain English (the product category Genloop sells). Built from public information and a search-visibility audit I ran on 14 Nov 2026. Everything marked *hypothesis* is meant to be tested in the first weeks, not trusted.

## 1. Where the product stands in search today
I ran 15 buyer-intent searches (category, problem, use-case, competitor, comparison and differentiator queries) plus one brand search, and recorded which sites came back (`data/search_audit.csv`).

- **Genloop appeared in 0 of 15 non-brand searches.** Even for "Genloop AI data analyst", genloop.ai itself did not come back, only third-party listings and a mirror of the site.
- **Four content-led startups (Querio, Bruin, Fabi, Basedash) showed up in 9 of 15 searches.** Querio and Bruin each appeared in 6. They win with "best X tools", "ThoughtSpot alternatives" and per-team use-case pages, the same pages answer engines quote.
- **The gaps are on Genloop's own strengths.** For differentiator searches (self-hosted, air-gapped, self-learning), the content-led players appeared in only 1 of 3, and a competitor (Zenlytic) owns the "self-learning AI data analyst" phrase through press releases. The Spider 2.0 benchmark search did not surface Genloop's claimed result at all.

**So what:** the cheapest win is not more general content. It is owning the searches where Genloop is genuinely different: self-hosted, accuracy-proven, self-learning.

## 2. Ideal customer profile (hypothesis)
Scorecard in `data/icp_segments.csv`, scored by `score_icp.py` (weights: warehouse fit 25%, analyst bottleneck 25%, need for self-hosting 20%, organic reach 15%, sales speed 15%).

| Rank | Segment | Score (of 5) |
|---|---|---|
| 1= | Mid-market B2B SaaS (RevOps and sales ops) | 4.0 |
| 1= | Financial services and insurance (mid-market) | 4.0 |
| 3 | E-commerce and DTC retail | 3.4 |
| 4 | Healthcare providers and payers | 3.2 |
| 5 | Logistics and supply chain | 2.9 |

The two leaders tie, and the tie breaks on one question: **how much does self-hosting matter to buyers?** At a 10% weight SaaS leads (4.25 vs 3.88); at 30%, financial services leads (4.12 vs 3.75). That is the first thing to learn from real conversations.

**Recommendation:** test both for two weeks.
- **SaaS RevOps** for speed: reachable through LinkedIn and RevOps communities, fast cycles, quick feedback on messaging.
- **Mid-market fintech and insurance** for the moat: self-hosted, accurate answers on sensitive data is a reason to choose Genloop over cloud-only tools.

### Buyer personas
| Persona | Pain | What they need to hear |
|---|---|---|
| Head of RevOps / Sales Ops | Reps and leaders wait days for pipeline answers; analysts are a queue | "Your team asks in plain English and gets the number, with the SQL to check it" |
| Head of Data / Analytics | Drowning in ad hoc requests; worried about wrong numbers | "Accuracy you can verify (benchmarks, shown SQL), and it learns your business terms" |
| CIO / CISO (finance, insurance) | Can't send data to a third-party cloud model | "Runs in your environment, including air-gapped" |

## 3. Organic growth engine
| Channel | Plan | Metric |
|---|---|---|
| Founder-led LinkedIn | 3 posts a week from the CEO: one teardown of a real analytics question, one customer or benchmark story, one point of view ("dashboards are failing your business") | Profile visits, DMs, meetings booked from posts |
| AEO / SEO pages | 10 pages in 30 days, aimed at the gaps in section 1: "self-hosted AI data analyst", "air-gapped text to SQL", a plain-English Spider 2.0 benchmark explainer, "Genloop vs ThoughtSpot", "best AI analyst for RevOps", and per-team use-case pages | Appearance in the same 15 searches, rechecked every 2 weeks |
| Third-party lists | Get added to the comparison posts that already rank (Bruin, Basedash, Fabi, Galaxy, Draxlr lists) and to G2 and Capterra categories | Number of ranking lists that mention Genloop |
| Communities | Answer questions (no pitching) in dbt Community Slack, Locally Optimistic, RevOps Co-op and r/dataengineering | Conversations started, inbound DMs |
| Events | Pick 2: Snowflake Summit, Data Council, SaaStr. Book meetings before the event, not at it | Meetings held per event |

## 4. Pipeline and partners
- **Outbound test:** 50 accounts per segment, 3-touch sequence over 10 days (LinkedIn connect, then a value-first email with a one-question demo, then a follow-up with a relevant benchmark or case).
- **Partners:** Snowflake and Databricks consultancies (they already field "can business users ask questions?" requests), and RevOps agencies.
- **Decision rule:** after 2 weeks, double down on the segment with the higher meetings-per-100-accounts rate, as long as it has at least 5 meetings.

Track every account in `templates/pipeline_tracker.csv`: source, segment, persona, stage, next step and date.

## 5. Insight loop
After every customer conversation, fill in `templates/call_notes.md` (segment, current tool, the question they wish they could ask, objections, what made them lean in). Every Friday, roll the notes into one page for the CEO and CRO: top 3 pains, top 3 objections, words customers use (for website copy), and anything worth adding to the investor update.

## 6. AI-native operations
- Account research: an LLM summarises a target account's data stack and recent hiring from public pages into the tracker.
- Content: first drafts of pages and posts from call notes, always edited by a person before publishing.
- Reporting: one weekly sheet pulls posts, page visibility, outreach replies and meetings into a single view.

## First 30 days
| Week | Goal |
|---|---|
| 1 | Finalise ICP test, build 2 lists of 50 accounts, publish the first 3 gap pages, start founder posting |
| 2 | Launch both outreach sequences, join 4 communities, pitch inclusion in 5 ranking lists |
| 3 | Run calls, fill call notes, publish 4 more pages, recheck the 15 searches |
| 4 | Pick the lead segment with the decision rule, write the segment playbook v1, share the insight summary |
