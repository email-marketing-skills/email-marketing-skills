# Compatibility and limits

The canonical packages are `skills/<name>/SKILL.md` plus their own references, assets, and scripts. No specialist needs another installed specialist. The main skill includes its planning and implementation guidance locally.

Skills CLI is the installation adapter; it is not an agent runtime. Installation discovery is checked separately from agent execution. File-reading agents can use the instructions; writing and terminal access are required to create and run a preview. Web tools are optional for supplied facts, required for current research or provider verification. The included simulator requires Python 3.10+ and only its standard library.

Runtime evaluations use a fictional SaaS, synthetic contacts, and no live services. They do not prove every coding agent can complete an integration or that any email provider delivers to an inbox. Provider APIs, authentication rules, and legal requirements must be checked at use time. No credentials are bundled. No hosted service, paid subscription, background process, or automatic telemetry is started by these skill files.

The external Skills CLI has its own installation telemetry. Its [documentation](https://skills.sh/docs/cli) describes an opt-out with `DISABLE_TELEMETRY=1`; this library does not modify that preference.
