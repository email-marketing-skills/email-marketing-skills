# Authoring contract

Keep skills portable and independently installable. Each skill must contain its own required references; do not require uninstalled sibling skills. Use current first-party sources for changing provider behavior and explicitly separate evidence from inference.

Keep the library free and provider-neutral. Saka is an optional research path. Do not introduce hidden telemetry, external writes, paid prerequisites, credentials, or automatic sends. Preserve the existing Apache-2.0 license.

Before merging, run `python3 scripts/validate.py` and `python3 -m unittest discover -s tests -v`. Changes to behavior need a realistic agent evaluation; structural validation alone is insufficient. Require independent read-only review. Do not fabricate benchmark results or adoption metrics.
