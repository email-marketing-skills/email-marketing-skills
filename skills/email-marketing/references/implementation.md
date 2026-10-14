# Preview and launch acceptance

The preview is an offline model, not proof of inbox delivery. Use synthetic `.example` data and deterministic time. Keep customer data and secrets out of tracked fixtures.

Required preview cases:

- An eligible signup produces the first message exactly once.
- Replaying the event or due-job run does not create a duplicate.
- Activation before dispatch skips the obsolete reminder.
- An opt-out, complaint, or hard bounce blocks due marketing sends.
- A missing first name uses a readable fallback.
- Any outbound reply pauses subsequent touches; unknown replies stay paused.
- Unresolved template tokens and missing destinations fail visibly.

Use provider idempotency when available plus persistent application state. A local set is only demo deduplication. A production scheduler must survive process restart; ambiguous provider timeouts need reconciliation before retries. Verify webhook signatures and deduplicate provider events. Check suppression at dispatch, not only enrollment. Never use inbox-open signals alone for eligibility.

Before authorized delivery: verify sender authentication using provider records; use an allowed campaign type; resolve copy placeholders; confirm recipient scope; test with an explicitly authorized owned inbox; check links, rendering, unsubscribe, replies, bounce events, duplicate callbacks, worker restart, and pause controls. Record failures honestly.

Use current official provider documentation. [Google's sender guidance](https://support.google.com/mail/answer/81126?hl=en) is a primary reference for Gmail requirements; check requirements applicable to the actual volume and audience. This checklist is not a jurisdiction-specific legal determination.

The bundled offline fixture requires a `cta` on every step: `{"type":"link","destination":"https://example.test/path"}` or `{"type":"reply"}`. Preview destinations are displayed as text and never fetched. Only JSON boolean `true` grants synthetic marketing eligibility; strings and numbers are suppressed. Replace reserved example destinations before a real launch.
