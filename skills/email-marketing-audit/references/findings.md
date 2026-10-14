# Actionable findings

Observed high-priority example: a due-message job reads opt-out state only at enrollment. A user who unsubscribes while queued can still receive the next campaign email. Evidence: named dispatch function and a synthetic queued-opt-out trace. Fix: recheck suppression immediately before sending. Acceptance: queued message skips after opt-out, including after worker restart.

Hypothesis example: activation is low because setup instructions are unclear. Evidence: incomplete onboarding counts without reply examples. Confidence: low. Next evidence: observe the setup path and inspect anonymized support themes. Do not declare the copy defective solely from a low rate.

Every severity should describe consequence and scope. Avoid a list of generic “best practices” without a demonstrated issue or explicit evidence gap.
