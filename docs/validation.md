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
