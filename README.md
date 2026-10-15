# Free email marketing skills for AI coding agents

Build an email marketing strategy, lifecycle flows, complete email copy, and a local preview from the app you already have. A practical starting point for developers, solo founders, and small teams who have never run email marketing.

[![skills.sh](https://skills.sh/b/email-marketing-skills/email-marketing-skills)](https://skills.sh/email-marketing-skills/email-marketing-skills)

These are open-source [Agent Skills](https://agentskills.io), licensed under Apache-2.0. The instructions are plain Markdown and the optional preview runs locally with Python. You can use the library without Saka or an email-provider account. Your coding agent and external services may charge separately.

## Use an email marketing bot

[Email Marketing Desk](bots/email-marketing-desk/README.md) combines all nine skills into a repeatable brief, campaign, preview and review workflow. Includes pinned setup, operating instructions and paused routine recipes for Grok Bot. [Start here](https://saka.run/email-marketing-bot). Public template and marketplace availability are tracked separately from the source package.

## Start with one skill

Run in the project you want to market:

```sh
npx skills add email-marketing-skills/email-marketing-skills --skill email-marketing
```

Choose your agent in the installer. For a specific agent:

```sh
npx skills add email-marketing-skills/email-marketing-skills --skill email-marketing --agent claude-code
npx skills add email-marketing-skills/email-marketing-skills --skill email-marketing --agent codex
```

Then ask:

```text
Use the email-marketing skill to build my email marketing strategy from this
project. Map the full lifecycle, propose a useful signup offer, write the
first campaign and a 30-day calendar, and implement a runnable local preview.
Use synthetic recipients. Explain what is missing before live sending.
```

The installer needs Node.js/npm, Git, and network access. Agent tool access varies; file and terminal access are needed for generated implementation and tests. If installation is unavailable, open [the main SKILL.md](skills/email-marketing/SKILL.md) and keep its referenced files together. No proprietary skill loader is required.

[Read the beginner guide](https://saka.run/docs/email-marketing) · [Copy a prompt without installing](https://saka.run/email-marketing) · [See a worked example](examples/reportnest.md)

## What the main skill creates

| Artifact | What it answers |
| --- | --- |
| `marketing/strategy.md` | Who is the first audience, what do they need, and what should we test? |
| `marketing/research.md` | Which facts have evidence and which remain assumptions? |
| `marketing/lifecycle-map.md` | Which flows are relevant, planned, and implemented? |
| `marketing/emails.md` | What is the full copy, trigger, CTA, and stop rule for each message? |
| `marketing/calendar.md` | What should run over the next 30 days without colliding with other messages? |
| `marketing/measurement.md` | Which customer action matters and how will we measure it? |
| `marketing/launch.md` | What ran locally, what remains simulated, and what is needed to launch? |
| Local preview | What would each synthetic recipient receive or skip? |

A complete strategy can map the whole program while implementing one priority campaign first. Planned flows are not labeled live.

## Skill catalog

Install only the specialist needed for the current task. Each is self-contained.

| Skill | Use it for | Example request |
| --- | --- | --- |
| [email-marketing](skills/email-marketing/SKILL.md) | Entire strategy and local preview | “I built an app. Set up my email marketing.” |
| [email-marketing-audit](skills/email-marketing-audit/SKILL.md) | Evidence-based program review | “Audit our flows and prioritize the first fix.” |
| [email-list-growth](skills/email-list-growth/SKILL.md) | Signup offers, forms, consent states | “Help suitable visitors subscribe.” |
| [email-lifecycle](skills/email-lifecycle/SKILL.md) | Triggers, onboarding, activation, retention | “Stop setup reminders after a user activates.” |
| [email-copywriting](skills/email-copywriting/SKILL.md) | Full messages, subjects, preview text, CTAs | “Write five welcome emails from this brief.” |
| [email-calendar](skills/email-calendar/SKILL.md) | 30-day plans and frequency coordination | “Plan a month of useful emails.” |
| [email-deliverability](skills/email-deliverability/SKILL.md) | Authentication and delivery diagnosis | “Diagnose these redacted bounce events.” |
| [email-experiments](skills/email-experiments/SKILL.md) | Metrics, tests, attribution, uncertainty | “Do these results support changing the campaign?” |
| [ai-sdr](skills/ai-sdr/SKILL.md) | Account research and reviewed B2B introductions | “Research ten relevant companies with evidence.” |

```sh
npx skills add email-marketing-skills/email-marketing-skills --list
npx skills add email-marketing-skills/email-marketing-skills --skill email-lifecycle
npx skills update
```

## Try the offline demo

From a clone of this repository, with Python 3.10 or newer:

```sh
python3 skills/email-marketing/scripts/preview.py   skills/email-marketing/assets/preview.json --html preview.html
```

Open `preview.html`. The simulator renders synthetic messages and prints why later steps were skipped. It has no network calls or sending adapter. It illustrates state decisions; it is not a production queue, durable sender, or deliverability test.

## Frequently asked questions

### Are these email marketing skills free?

Yes. The skill files and bundled preview are free under Apache-2.0. Model usage, mailboxes, domains, hosting, verification, and email delivery may have separate costs.

### Which coding agents can use them?

The library uses standard `SKILL.md` packages. The Skills CLI supports agent-specific installation, including Claude Code and Codex. Tool availability and generated code quality depend on the agent. See [compatibility and limitations](docs/compatibility.md) for what has actually been checked.

### Does the skill automatically send emails?

No. It drafts and builds local artifacts by default. Live sending requires an appropriate provider, eligible recipients, sender configuration, tested suppression/reply handling, and the user's authorization. It never treats a public email address as newsletter consent.

### Can I build an AI SDR with this?

The `ai-sdr` skill researches businesses, qualifies evidence, and drafts introductions. A persistent sender, scheduler, and reply workflow are separate integrations. [Saka](https://saka.run) is an optional business-data source; new production records use prepaid credit.

### Is this a newsletter tool or an email service provider?

It is a collection of instructions and local tools for your coding agent. You own the generated strategy and code. Connect your chosen service when ready to deliver campaigns.

### Can it guarantee customers, rankings, or a setup time?

No. It helps you build a concrete campaign and learn from customer actions. Performance depends on the product, audience, offer, execution, and available tools. We publish validation evidence without treating it as a guarantee.

## Quality and contribution

Run `python3 scripts/validate.py` and `python3 -m unittest discover -s tests -v`. See [evaluation cases](evals/evals.json), [validation evidence](docs/validation.md), and [contributing](CONTRIBUTING.md). Report a concrete failure with synthetic or redacted inputs through [GitHub issues](https://github.com/email-marketing-skills/email-marketing-skills/issues).

[Sources and acknowledgments](docs/sources.md) · [License](LICENSE) · [Project home](https://github.com/email-marketing-skills) · [Saka developer documentation](https://saka.run/developers)
