#!/usr/bin/env python3
"""Offline campaign simulator. Synthetic data only; no network or sending adapter."""
import argparse
import html
import json
import re
from urllib.parse import urlparse
from pathlib import Path
from string import Formatter


def simulate(data):
    people = {}
    for p in data["recipients"]:
        if p["id"] in people:
            raise ValueError("Duplicate recipient id")
        people[p["id"]] = dict(p, enrolled=None, active=False, suppressed=False, paused=False)
    steps = data["steps"]
    if len({s["id"] for s in steps}) != len(steps):
        raise ValueError("Duplicate step id")
    for step in steps:
        if step["when"] not in ("any", "inactive", "active") or step["after_hours"] < 0:
            raise ValueError("Invalid step condition or delay")
        cta = step.get("cta", {})
        if cta.get("type") == "link":
            url = urlparse(cta.get("destination", ""))
            if url.scheme not in ("https", "http") or not url.netloc or any(c.isspace() or c in "{}[]<>" for c in cta["destination"]):
                raise ValueError("Link CTA requires a complete HTTP(S) destination")
        elif cta.get("type") != "reply":
            raise ValueError("Each step requires a link destination or reply CTA")
        if re.search(r"\[[^\]]*\]\(\s*\)", step["body"]):
            raise ValueError("Empty Markdown link destination")
        for field in ("subject", "body"):
            for _, name, spec, conversion in Formatter().parse(step[field]):
                if name is not None and (name != "first_name" or spec or conversion):
                    raise ValueError("Only {first_name} without formatting is supported")
    seen_events, sent = set(), set()
    decisions, messages = [], []
    previous = -1
    for event in data["events"]:
        if event["hour"] < previous:
            raise ValueError("Events must be chronological")
        previous = event["hour"]
        if event["id"] in seen_events:
            continue
        seen_events.add(event["id"])
        kind = event["type"]
        if kind != "tick":
            p = people[event["recipient"]]
            if kind == "signup":
                if p["enrolled"] is None:
                    p["enrolled"] = event["hour"]
            elif kind == "activate":
                p["active"] = True
            elif kind in ("unsubscribe", "complaint", "bounce"):
                p["suppressed"] = True
            elif kind == "reply":
                p["paused"] = True
            else:
                raise ValueError("Unknown event type: " + kind)
            continue
        for p in people.values():
            for step in steps:
                key = (p["id"], step["id"])
                if p["enrolled"] is None or event["hour"] < p["enrolled"] + step["after_hours"]:
                    continue
                reason = "preview"
                if key in sent:
                    reason = "already_previewed"
                elif p["suppressed"] or p.get("marketing_eligible") is not True:
                    reason = "suppressed"
                elif p["paused"]:
                    reason = "reply_pause"
                elif (step["when"] == "inactive" and p["active"]) or (step["when"] == "active" and not p["active"]):
                    reason = "state_mismatch"
                decisions.append({"recipient": p["id"], "step": step["id"], "hour": event["hour"], "decision": reason})
                if reason == "preview":
                    name = p.get("first_name") or "there"
                    messages.append({"recipient": p["id"], "step": step["id"], "subject": step["subject"].format(first_name=name), "body": step["body"].format(first_name=name), "cta": step["cta"]})
                    sent.add(key)
    return {"mode": "offline_preview", "messages": messages, "decisions": decisions}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture", type=Path)
    parser.add_argument("--html", type=Path, help="Write a local, escaped HTML preview")
    args = parser.parse_args()
    try:
        result = simulate(json.loads(args.fixture.read_text()))
    except (ValueError, KeyError, TypeError) as error:
        parser.exit(2, "Invalid fixture: " + str(error) + "\n")
    if args.html:
        cards = "".join("<article><h2>"+html.escape(m["subject"])+"</h2><pre>"+html.escape(m["body"])+"</pre><p>CTA: "+html.escape(m["cta"].get("destination", "Reply to this email"))+"</p></article>" for m in result["messages"])
        args.html.write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Email preview</title><style>body{max-width:48rem;margin:2rem auto;padding:1rem;font:18px/1.6 system-ui}article{border-top:1px solid #aaa;padding:1rem 0}pre{white-space:pre-wrap;font:inherit}</style><h1>Offline email preview</h1><p>Synthetic recipients. Nothing was sent.</p>'+cards+'</html>')
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
