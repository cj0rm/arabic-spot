#!/usr/bin/env python3
"""Dependency-free structural checks for the Arabic spot Agent Skill."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
files = [
    "SKILL.md", "agents/openai.yaml", "README.md", "LICENSE",
    "THIRD_PARTY_NOTICES.md", "references/POETRY.md", "references/PROSODY.md",
    "references/RHETORIC.md", "references/WRITING.md", "references/RECITATION.md",
    "references/SOURCES.md", "docs/INSTALLATION.md", "docs/EXAMPLES.md",
    "web/index.html", "web/styles.css", "scripts/install.sh", "scripts/install.ps1",
]
problems = []
for name in files:
    path = ROOT / name
    if not path.is_file() or path.stat().st_size == 0:
        problems.append(f"Required file missing/empty: {name}")

skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
if not re.search(r"\A---\s*\nname:\s*arabic-spot\s*\n", skill):
    problems.append("SKILL.md must start with name: arabic-spot")
if not re.search(r"^description:\s*.+", skill, flags=re.MULTILINE):
    problems.append("SKILL.md frontmatter needs description")
if skill.count("---") < 2:
    problems.append("SKILL.md has incomplete YAML frontmatter")
for ref in re.findall(r"references/[A-Z_]+\.md", skill):
    if not (ROOT / ref).exists():
        problems.append(f"Broken reference in SKILL.md: {ref}")
if 'lang="ar"' not in (ROOT / "web/index.html").read_text(encoding="utf-8"):
    problems.append("web/index.html should declare Arabic")
if problems:
    print("Arabic spot validation failed:")
    for p in problems:
        print(" -", p)
    sys.exit(1)
print(f"Arabic spot validated: {len(files)} required files checked.")
