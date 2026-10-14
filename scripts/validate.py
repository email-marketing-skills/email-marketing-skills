#!/usr/bin/env python3
"""Dependency-free validation of this repository's deliberately simple skill metadata."""
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
skills=list((ROOT/"skills").glob("*/SKILL.md"))
assert skills,"No skills found"
for path in skills:
    text=path.read_text();assert text.startswith("---\n"),path
    front,body=text[4:].split("\n---\n",1)
    name=re.search(r"^name: (.+)$",front,re.M).group(1)
    description=json.loads(re.search(r"^description: (.+)$",front,re.M).group(1))
    assert name==path.parent.name and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*",name),path
    assert 0<len(name)<=64 and 0<len(description)<=1024,path
    assert len(text.splitlines())<500,path
    for target in re.findall(r"\]\(([^)]+)\)",text):
        if "://" not in target and not target.startswith("#"):
            resolved=(path.parent/target.split("#")[0]).resolve()
            assert resolved.is_relative_to(path.parent.resolve()) and resolved.is_file(),(path,target)
    assert "license: Apache-2.0" in front,path
config=json.loads((ROOT/"skills.sh.json").read_text())
names={p.parent.name for p in skills}
assert config["groupings"]
for group in config["groupings"]:
    assert group["title"] and group["skills"]
    assert set(group["skills"])<=names
print(f"Validated {len(skills)} skill packages, metadata, local references, and Skills.sh group names.")
