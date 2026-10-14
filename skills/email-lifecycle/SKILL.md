---
name: email-lifecycle
description: "Design or repair welcome, onboarding, activation, trial-conversion, retention, and winback email flows. Use when users ask for lifecycle automation, drip sequences, trigger rules, stop conditions, or emails after signup; not for one-off copy edits."
license: Apache-2.0
metadata:
  author: email-marketing-skills
  version: "1.0.0"
---

# Lifecycle flows that follow customer state

Read product context, event definitions, existing flows, and the actual first-value action. Ask only for missing entry events or outcomes that change the sequence. File access is useful; no email-provider connection is required to design the flow.

## Build a state map

Map anonymous visitor → interested subscriber → signed-up user → activated user → paying user → inactive/cancelled user only where these states exist. Record the authoritative event and timestamp for each transition. A free account is not necessarily a marketing opt-in, and a cancelled subscription is not necessarily an unsubscribe.

Choose the weakest relevant transition based on evidence. Do not schedule an email for every state just to fill a map. Identify necessary account messages separately from marketing flows.

## Specify the flow

Read [the worked flow](references/worked-flow.md). Create `marketing/lifecycle-map.md` and a detailed spec for the first priority flow. For each message include goal, enrollment trigger, delay/timezone, current-state predicate, exclusions, re-entry policy, copy angle, one CTA, and exit events. Explain why that message belongs there.

Check state immediately before dispatch. Skip setup reminders after setup. Suppress marketing on opt-out, complaint, hard bounce, and any applicable support pause. For outreach, any reply pauses all follow-ups, including out-of-office replies until reviewed. Set a frequency cap across flows; identify which message wins a conflict.

## Implement when asked

Use existing app event and queue patterns. An event ID identifies a source event; a stable recipient+flow-version+step identity identifies a message. Persist them. Handle duplicate events and restart without duplicate messages. For an ambiguous sender timeout, reconcile with the provider before retrying. Verify and deduplicate provider callbacks. Never treat opens as a reliable state transition.

Draft copy can use fictional examples clearly labeled as such, but integration tests use synthetic recipients. Keep secrets out of artifacts. Read current official provider docs for live integration. Do not send or deploy unless already authorized for the exact scope.

## Acceptance and output

Provide the state map, flow spec, implementation or plan status, and a test matrix: duplicated signup, conversion before reminder, consent change while queued, missing name, repeated scheduling, out-of-order event, and reply before follow-up. Include the event trace and due/skipped decision in each case. Mark simulated versus integrated behavior. Finish with one primary outcome and an observation window.
