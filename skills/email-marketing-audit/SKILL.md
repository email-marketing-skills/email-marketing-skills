---
name: email-marketing-audit
description: "Audit an existing email program and prioritize problems across lifecycle coverage, sender setup, list health, automation, copy, frequency, and measurement. Use when email is underperforming, a developer inherits campaigns, or a program needs a systematic review."
license: Apache-2.0
metadata:
  author: email-marketing-skills
  version: "1.0.0"
---

# Audit the program against evidence

Read the product goal, current flows, templates, event definitions, aggregate metrics, and recent changes. Begin read-only. Ask for missing evidence as a bounded list and continue with available artifacts. Never request secrets or assume access to production contacts.

## Inventory and classify

For every flow record owner, audience, purpose, trigger, exit, frequency, status, outcome, and source of evidence. Distinguish configured, exercised, and producing useful results. A configured integration is not evidence of delivery.

Inspect seven areas: sender/authentication evidence; list sources/preferences/suppression; lifecycle gaps; event/deduplication/restart behavior; copy and destinations; cross-flow frequency; and measurement quality. Check actual recipient state transitions where safely reproducible. Use synthetic dry-runs by default.

## Findings that someone can act on

Read [finding format](references/findings.md). Each finding needs severity, source location or evidence, concrete failure scenario, affected audience, confidence, recommended change, acceptance check, and owner. Separate observed defects from hypotheses. Do not invent benchmark gaps or claim missing evidence proves failure.

Prioritize broken suppression, duplicate delivery, incorrect claims, and broken essential flows before aesthetic copy changes. For deliverability conclusions, check current primary provider guidance and actual headers/events. For legal questions, use current authoritative jurisdiction sources; do not certify compliance from a template.

## Deliver

Save `marketing/audit.md`: executive finding, inventory, prioritized findings, missing evidence, and a bounded next-work list. Suggest one first fix with a measurable acceptance condition. Do not modify campaigns, change DNS, or send tests unless those actions are already authorized. If asked to implement, preserve the audit and distinguish fixed, verified, deferred, and blocked items.

A clean audit means no issues found within the inspected evidence and scope. It does not certify inbox placement, legal compliance, or future revenue.
