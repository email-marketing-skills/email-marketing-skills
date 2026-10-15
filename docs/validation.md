# Validation evidence

Initial release checks, 2026-10-14:

- Nine packages pass metadata, local-reference, naming, and catalog validation.
- Eleven deterministic bundled-preview tests pass: state changes, opt-outs, replies, duplicate events, missing and malformed eligibility, unresolved templates and destinations, event ordering, and explicit link/reply CTAs.
- One paired fictional ReportNest evaluation used the same supplied facts with and without the main skill. The skill-assisted output met 7/7 predefined assertions; the baseline met 5/7. Both respected unknown permission and avoided unsupported outcome claims. The baseline lacked event-replay acceptance tests and a full 30-day campaign calendar. This is one case, graded by the delivery agent, not a statistically reliable comparison.
- The generated skill-assisted preview passed its own 10 tests; the baseline passed its own 5 tests. These are different test suites, not a comparison of test quality.
- A separate reviewer completed bounded inline specialist evaluations: AI SDR 4/4 assertions (including hostile source instructions and an unknown contact), email experiments 3/3 (including refusal to declare a winner from 2/20 versus 3/20 replies). These are instruction-following cases, not production runtime benchmarks.
- Independent review found malformed eligibility and missing-destination handling in the bundled preview. Both were corrected, regression-tested, and reviewed again with no remaining actionable findings in that scope.

Evaluation prompts are in [evals/evals.json](../evals/evals.json). Run the structural validator and preview tests using the commands in [CONTRIBUTING.md](../CONTRIBUTING.md).

These checks do not establish production deliverability, legal compliance, marketing outcomes, universal agent compatibility, or a setup-time benchmark. Model timing and token usage were not recorded. Specialist skills beyond the two cases above have structural validation and editorial review, not paired behavioral evaluations.

## Email Marketing Desk source package — 2026-10-15

- Nine package validation and all 11 existing offline-preview tests pass. The pinned library remains revision `2e21c764e28fcd16ff0c78c4334c78c250e8576d`; no skill behavior changed.
- Independent read-only review of the bot package and companion Saka page found no blockers.
- An independent agent loaded the actual bot instructions and relevant skills/references and exercised EVALUATION.md cases 2–4. All 11 assertions passed: hostile CSV content treated as data, no secret exposure, no consent inference, consent-safe alternative, no external write; correct counts/percentages, uncertainty, bounded next test, no silent scheduling; receipt reconciliation and reply stop. These are three bounded instruction-following evaluations, not a runtime benchmark or native Grok acceptance.
- Local synthetic demo rendered two welcome messages; the reminder was suppressed for the opted-out recipient and skipped after activation for the other recipient. Replay did not duplicate the welcome.
- Native Grok setup, fresh template import and curated marketplace acceptance require separate evidence. No live sender is included or qualified.
