# Reproducible setup

This is a source package for configuring a bot, not an undocumented native import format. Requires Git, Python 3.10+, file/terminal access and network access for the initial download. No API key is needed for the offline preview. Agent usage may cost separately.

Use a new directory in the bot's workspace. Never overwrite an existing clone or customer files. The immutable library revision below contains all nine skills and their references:

```sh
git clone https://github.com/email-marketing-skills/email-marketing-skills.git email-marketing-library
cd email-marketing-library
git checkout --detach 2e21c764e28fcd16ff0c78c4334c78c250e8576d
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 skills/email-marketing/scripts/preview.py skills/email-marketing/assets/preview.json --html ../email-marketing-demo.html
```

If that directory exists, inspect its origin, revision and local modifications first. Reuse it only when it is the same clean pinned source; otherwise choose a fresh directory. Do not reset or clean existing work. Verify `git rev-parse HEAD` matches the pin before executing scripts. Read the scripts before execution. Save the resolved path and revision in the user's private marketing/launch.md. Load the chosen skill directly from `skills/<name>/SKILL.md`; retain its references, scripts and assets. There is no dependency on a proprietary skill loader.

The bundled demo is fictional and offline. Open its HTML, verify rendered copy and due/skipped results, and label it synthetic. For a real product, adapt the fixture and campaign rather than showing the demo as customer work. If a computer resets, repeat setup in a fresh folder and restore only user-approved private artifacts. Never imply lost state has been recovered.

For future upgrades, inspect the upstream diff, choose a new immutable revision, rerun checks and behavioral evaluations, then update the pin. No silent update from a moving branch.

## Grok Bot publication

Create a dedicated bot named Email Marketing Desk. Add INSTRUCTIONS.md as its operating instructions, and SETUP.md and ROUTINES.md as reusable skills or library instructions using the app's supported controls. Keep all nine upstream packages available through setup. Run the fictional evaluation in EVALUATION.md on this bot.

Use Settings → Share as Template, review View Details, and choose public sharing only after checking every included memory, skill, routine and integration. Include only generic instructions and paused routine recipes. Exclude all customer data, creator conversations, credentials, account connections and test outputs. Publish and record the actual template link in listing.json. Test that link using a fresh bot; confirm the pinned library can be restored and the preview works.

A public template link does not prove placement in the curated marketing category. Check the current marketplace submission controls or obtain the publisher's instructions. Record submission and acceptance separately. Never fabricate an Add to Grok link.

Source: https://x.ai/bot/guides/templates-for-grok-bot (checked 2026-10-15). The guide documents template sharing, not a guaranteed marketplace listing or public submission API.
