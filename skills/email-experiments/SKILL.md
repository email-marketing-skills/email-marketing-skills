---
name: email-experiments
description: "Measure email campaign outcomes and design useful tests with explicit cohorts, denominators, attribution limits, sample-size constraints, and decision rules. Use for campaign reports, A/B tests, holdouts, ROI questions, or claims that opens prove success."
license: Apache-2.0
metadata:
  author: email-marketing-skills
  version: "1.0.0"
---

# Measure the customer outcome

Read the campaign goal, enrollment rules, observation window, and aggregated results. Keep recipient identifiers out of committed reports. If data is missing, produce a fill-in template and ask for counts; do not substitute invented benchmarks.

## Reconcile the data

Define unique enrolled and eligible contacts, attempted sends, accepted sends, delivered contacts, bounces, complaints, opt-outs, activations, qualified replies, and paid conversions as relevant. Do not mix message counts with contact counts. Explain exclusions and deduplication. Missing is not zero. Zero denominator means unavailable, not 0%.

A signup campaign can use activated eligible users divided by eligible enrolled users within a defined window. An outbound campaign can use unique qualified positive replies divided by unique delivered contacts. Define qualified before reading results. Report counts beside percentages. Opens are diagnostic at most; they are not reliable proof of human attention.

## Choose the learning method

For small audiences, use reply themes and observed product friction. For a controlled test, specify hypothesis, unit of randomization, eligibility, one change, primary metric, baseline evidence, minimum meaningful effect, sample-size method, observation window, and stopping rule before launch. If assumptions or sample size are insufficient, call the test exploratory. Do not infer significance from two percentages.

Distinguish attributed conversions from incremental conversions. A holdout can help estimate lift when assignment, sample, and spillover are handled; before/after changes alone cannot isolate email's effect. Read [worked analysis](references/example.md).

## Deliver and iterate

Save `marketing/review.md`: data quality, facts, uncertainty, reader feedback, one next experiment, and a decision rule. If a delivery or suppression failure exists, investigate it before increasing volume. Prepare draft changes locally; do not activate a campaign or contact recipients without existing scope authorization.

Report what the evidence supports and what it cannot establish. Avoid universal performance promises, statistically unsupported “winners,” and revenue claims that ignore refunds, attribution, or costs.
