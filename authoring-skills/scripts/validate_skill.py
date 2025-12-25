#!/usr/bin/env python3
"""validate_skill.py

Validate a skill folder's SKILL.md against the required rules.
"""
import argparse
import json
import os
import re
from pathlib import Path
from typing import Dict, List, Tuple

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
DIRECTIVE_RE = re.compile(r"\b(MUST|MUST BE USED|PROACTIVELY|Use when)\b", re.I)
BANNED_WEAK = re.compile(r"\b(should be used|recommended for)\b", re.I)
SECOND_PERSON = re.compile(r"\byou\s+(should|need|must|can)\b", re.I)


def read_skill_md(path: Path) -> Tuple[Dict[str, str], List[str]]:
    if not path.exists():
        raise FileNotFoundError(str(path))
    text = path.read_text()
    # parse frontmatter between first two '---'
    if not text.startswith("---"):
        raise ValueError("Missing YAML frontmatter (no leading '---')")
    parts = text.split("---")
    if len(parts) < 3:
        raise ValueError("Malformed frontmatter")
    fm_text = parts[1].strip()
    body_text = "---".join(parts[2:]).lstrip('\n')
    front = {}
    current_key = None
    # simple YAML-like parse
    for line in fm_text.splitlines():
        if ':' in line:
            k, v = line.split(':', 1)
            front[k.strip()] = v.strip()
            current_key = k.strip()
        elif line.strip().startswith('-') and current_key:
            # append to a csv-like value
            front[current_key] = (front.get(current_key, '') + ' ' + line.strip().lstrip('- ')).strip()
        elif line.strip().startswith('#'):
            continue
    return front, body_text.splitlines()


def validate(path: Path) -> Tuple[bool, List[str]]:
    errors: List[str] = []
    # Determine SKILL.md path
    if path.is_dir():
        skill_md = path / "SKILL.md"
    else:
        skill_md = path
    if not skill_md.exists():
        return False, [f"SKILL.md not found at {skill_md}"]

    try:
        front, body_lines = read_skill_md(skill_md)
    except Exception as e:
        return False, [f"Error parsing SKILL.md: {e}"]

    # frontmatter checks
    if 'name' not in front:
        errors.append("Missing 'name' in frontmatter")
    else:
        name = front['name']
        if not NAME_RE.match(name):
            errors.append("Invalid 'name' format (must be lowercase, numbers and hyphens only)")
        # name equals directory?
        parent = skill_md.parent.name
        if name != parent:
            errors.append(f"Frontmatter 'name' ('{name}') does not match parent directory name ('{parent}')")

    if 'description' not in front:
        errors.append("Missing 'description' in frontmatter")
    else:
        desc = front['description']
        if len(desc) > 1024:
            errors.append("'description' longer than 1024 characters")
        if not DIRECTIVE_RE.search(desc):
            errors.append("'description' should include directive language (e.g., 'MUST', 'Use PROACTIVELY', or 'Use when')")
        if BANNED_WEAK.search(desc):
            errors.append("Avoid weak directive language like 'should be used' or 'recommended for' in description")

    # metadata checks (look for 'metadata:' in frontmatter keys or 'metadata' key)
    # Our simplistic parser does not handle nested keys, so check for literally 'metadata' or presence of 'category' and 'keywords'
    if 'metadata' not in front and not ('category' in front and 'keywords' in front):
        errors.append("Frontmatter missing 'metadata' mapping with 'category' and 'keywords'")

    # body checks
    if len(body_lines) > 500:
        errors.append("SKILL.md body exceeds 500 lines")

    body_text = '\n'.join(body_lines)
    if SECOND_PERSON.search(body_text):
        errors.append("Avoid second-person phrasing (e.g., 'you should') in SKILL.md body")

    if errors:
        return False, errors
    return True, ["PASS"]


def format_output(result: Tuple[bool, List[str]], out_format: str) -> str:
    ok, messages = result
    if out_format == 'json':
        return json.dumps({'pass': ok, 'messages': messages}, indent=2)
    return '\n'.join(messages)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True, help="Path to a skill folder or SKILL.md file")
    parser.add_argument("--format", default="text", choices=("text", "json"))
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors (if implemented)")
    args = parser.parse_args()

    path = Path(args.path)
    ok, messages = validate(path)
    out = format_output((ok, messages), args.format)
    print(out)
    if ok:
        raise SystemExit(0)
    else:
        raise SystemExit(2)


if __name__ == '__main__':
    main()
