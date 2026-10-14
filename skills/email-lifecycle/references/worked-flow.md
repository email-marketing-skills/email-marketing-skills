# Example: first report activation

Fictional product assumptions: a user uploads CSV data, creates a report, and can share it. Verify these capabilities before applying the pattern.

| Step | Due | Eligibility at send time | Purpose | Exit |
| --- | --- | --- | --- | --- |
| Start | At signup | Marketing eligible; no report | Create one report from sample data | Report created |
| Remove friction | +24 hours | Still no report; no support pause | Explain one setup obstacle | Report created |
| Apply result | +3 days | Report exists; no share | Share a reviewed report | Report shared |
| Ask for help | +5 days | No report; no open support conversation | Ask what blocked setup | Reply received |

A user who creates a report before the first dispatch skips the first two messages. Do not send a retroactive welcome reminder merely because an event arrived late. A replay of the same signup has the same enrollment identity. A second signup with a different event ID for the same account must not re-enroll unless the documented policy allows it.

Example test trace: signup at hour 0 → welcome preview; activation at hour 12 → day-one reminder skipped; unsubscribe at hour 60 → share message suppressed. This verifies decision logic, not email deliverability.
