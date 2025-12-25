# Core Principles and Detailed Workflow

## Philosophy: The Autonomous Project Skill

Skills enable agents to execute tasks autonomously. The goal is to create skills that work without human intervention while maintaining reliability through self-correction and verification loops.

## Core Requirements for Generated Skills

1.  **Project-Root Awareness**: All paths in instructions and scripts must be relative to the project root.
2.  **Self-Correction**: Instructions must include steps for the agent to verify its own output.
3.  **Robust Scripting**: Scripts must handle arguments via CLI, never interactively.
4.  **Structured Prompting**: Use XML tags in instructions for complex logic.

## Core Concepts

### Progressive Disclosure (Three Levels)

| Level | Phase | Tokens | Content |
|:------|:------|:-------|:--------|
| 1 | Discovery | ~100-200 | Frontmatter `name` + `description` only |
| 2 | Activation | <5000 | Full `SKILL.md` body |
| 3 | Execution | Unlimited | `scripts/`, `references/`, `assets/` on-demand |

### Directory Structure

```text
skill-name/
├── SKILL.md          # Required: frontmatter + instructions
├── scripts/          # Optional: executable code (not loaded into context)
├── references/       # Optional: documentation (loaded on-demand)
└── assets/           # Optional: templates, resources (used in output)
```

### Where to Create Skills

- **Personal / Global Skills**: `~/.claude/skills/` (if clearly asked for)
- **Project-Specific / Shared Skills**: `.claude/skills/` (in project root, per default)

## Detailed Skill Creation Workflow

### 1. Analyze Degrees of Freedom
Refer to `references/agentic-patterns.md`. Determine if the task is:
- **Low Freedom** (Fragile): Use rigid scripts and precise instructions.
- **High Freedom** (Creative): Use heuristics and checklists.

### 2. Define Security Scope
Refer to `references/security-best-practices.md`.
Determine the required `allowed-tools` for your skill (Read-Only vs Execution vs MCP).

### 3. Plan & Strategy (Evaluation First)
Before searching for solutions, define what success looks like. CREATE `evaluation_plan.md` using `assets/templates/evaluation_plan.md`.
Define 3 scenarios: Baseline (Happy path), Edge Case (Error handling), and Safety.

### 4. Apply Agentic Patterns (MANDATORY)
Refer to `references/agentic-patterns.md`. The skill MUST incorporate:
- **Chain of Thought**: Force the agent to "Think" before "Acting"
- **Verification Loops**: "Run script → Check Output → If Error, Read Log → Fix"

### 5. Use Golden Templates
- For Python scripts, you MUST use `assets/templates/robust_script.py` as a base.
- For SKILL.md structure, refer to `assets/templates/skill_structure.md`.

### 6. Plan Resources
Analyze each use case to identify reusable resources (scripts, references, assets).

### 7. Write Frontmatter
**CRITICAL**: The `description` field determines skill activation.
Use directive language (MUST BE USED, Use PROACTIVELY) as per `references/description-templates.md`.

### 8. Write SKILL.md Body
- Use imperative/infinitive form.
- NEVER use second person.
- Keep body under 500 lines.
- Follow the structure: Overview, When to Use, Workflow, Critical Rules, Resources.

### 9. Validate
Run through the compliance checklist in `references/compliance-checklist.md`.

### 10. Iterate
Identify struggles, strengthen triggers, move long sections to references, and ensure scripts are robust.

### 11. Integration Check
Verify triggers, tool authorization, and runtime compatibility.
