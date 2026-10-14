---
name: email-deliverability
description: "Diagnose email delivery, authentication, bounces, complaints, suppression, and sender setup. Use when messages land in spam, delivery changes after migration, or a developer needs a launch checklist. Requires current provider evidence for production conclusions."
license: Apache-2.0
metadata:
  author: email-marketing-skills
  version: "1.0.0"
---

# Diagnose delivery before changing copy

Separate provider acceptance, recipient-server delivery, inbox placement, and opens. A 200 API response does not prove inbox delivery. Ask for redacted provider events, affected domains/time range, recent changes, and sample headers; do not request credentials or raw recipient exports.

## Triage in order

1. Scope: one recipient domain or all, one campaign or all, first occurrence, volume changes, and provider incident evidence.
2. Authentication: inspect SPF/DKIM results and DMARC alignment from actual headers and current DNS evidence. Compare against the sending provider's current instructions. Do not invent DNS records or overwrite existing records blindly.
3. Sender/provider state: rejection codes, account limits, suppression, recent domain/IP changes, and documented provider incidents.
4. List health: source/permission quality, old addresses, bounce/complaint events, re-enrollment, and unsubscribe behavior.
5. Message: broken links, invalid MIME, misleading content, inaccessible rendering, and campaign/provider policy mismatch.

Use [evidence checklist](references/evidence.md). Browse current authoritative provider guidance before recommending production changes. If network tools are unavailable, label the diagnosis provisional. Do not treat a drop in opens alone as proof of spam placement.

## Remediation

Write `marketing/deliverability.md` with observed facts, likely causes, alternative explanations, priority, exact next verification, and rollback. Pause affected delivery when suppression or authentication is broken. Keep recipient opt-outs effective. Recommend truthful identity and appropriate sending practices; never recommend fabricated engagement, automated fake replies, or rotating domains to evade enforcement.

Prepare DNS/config diffs only from provider-supplied values. Live changes and test sends require the user's scoped authorization. Preserve unrelated DNS records and existing transactional traffic. Verify after an authorized change using new message headers and real delivery events; a DNS lookup alone does not prove end-to-end alignment.

## Completion

Return a bounded diagnosis, supported next action, and missing evidence. Mark delivered/inbox/engagement evidence independently. No guaranteed inbox placement or universal warmup duration.
