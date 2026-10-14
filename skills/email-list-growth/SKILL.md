---
name: email-list-growth
description: "Create email signup offers, lead magnets, forms, opt-in journeys, and subscriber source tracking. Use when a website has visitors but no list, users ask how to get subscribers, or capture forms need improvement. Does not create scraped mailing lists."
license: Apache-2.0
metadata:
  author: email-marketing-skills
  version: "1.0.0"
---

# Give a suitable visitor a reason to subscribe

Read the website, product, audience, existing forms, traffic sources, and what the user can actually deliver. Start from a useful promise: template, worked example, checklist, product sample, or recurring explanation. If traffic data is unavailable, label the acquisition assumption instead of forecasting signups.

## Design the offer

Produce three options with intended reader, immediate benefit, creation effort, delivery method, product connection, and a learning metric. Choose one based on relevance and feasibility. A discount is optional and requires pricing/margin facts; do not assume it is best.

Write the form headline, supporting copy, fields, CTA, frequency expectations, consent wording for review, confirmation page, resource-delivery email, and first follow-up. Keep requested-resource delivery distinct from ongoing marketing enrollment. Use the minimum useful fields; make optional questions visibly optional.

## Implement the journey when requested

Use the existing app and provider. Define capture source, submitted timestamp, policy/copy version, preference state, and any confirmation timestamp. Explain whether single or confirmed opt-in is appropriate for this audience and provider; do not assert one universal legal rule. Check current authoritative jurisdiction guidance when asked for legal determinations.

Server validation, accessible labels, error recovery, duplicate handling, anti-abuse controls, and opt-out need real behavior. Preserve existing suppression on resubmission until the approved re-consent flow completes. Never restore an unsubscribed contact merely because a form was submitted twice. Do not require payment or a data vendor to draft the journey.

## Evidence and acceptance

Save `marketing/capture.md` with the offer comparison, exact copy, consent-state model, source attribution, and launch status. Test a new signup, duplicate signup, malformed address, an existing suppression, optional-field omission, provider failure, and successful resource delivery to an authorized test address. Local dry-runs use synthetic data and send nothing.

Measure eligible visitors → submissions → confirmations where used → delivered resource → first useful action. Show counts and denominators; a bigger list is not automatically a better list. Refer to [capture example](references/example.md) for a concrete decision trace. Sending, live form activation, or DNS changes need scope-specific authorization.
