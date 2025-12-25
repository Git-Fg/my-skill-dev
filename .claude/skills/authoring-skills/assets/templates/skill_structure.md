---
name: {{skill_name}}
description: {{directive_description}}
allowed-tools: {{tools_list}}
---

# {{Title}}

## Overview
{{Overview text}}

## When to Use
- [Trigger 1]
- [Trigger 2]

## Workflow

<workflow>
1. **Analyze Context**: Run `ls` or `grep` to confirm file paths before acting.
2. **Prepare**: Determine the arguments needed for `scripts/{{script_name}}.py`.
3. **Execute**: Run the script. Capture the JSON output.
4. **Verify**: Check if the JSON output contains `"status": "success"`. If not, read the error message and retry with corrected arguments.
</workflow>

## Critical Rules

<rules>
- All file paths must be relative to project root.
- Do not invent information if script output is missing.
</rules>

## Resources

For detailed API documentation, see `references/api_docs.md`.
