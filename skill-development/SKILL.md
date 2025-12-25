---
name: skill-development
description: MUST BE USED when creating, improving, or reviewing Agent Skills. Use PROACTIVELY when user mentions "create a skill", "new skill", "write a skill", "improve skill", "skill description", "progressive disclosure", or skill structure. Guides through specification-compliant skill design with three-level progressive disclosure (Discovery, Activation, Execution).
category: metaprompting
keywords: skill, agent, progressive-disclosure, SKILL.md, frontmatter
---

# Skill Development

Creates effective Agent Skills following the Universal Agent Skills Specification.

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

## Skill Creation Workflow

### 1. Understand Use Cases

Gather concrete examples of skill usage:
- What user queries should trigger this skill?
- What workflows does the skill support?
- What domain expertise is required?

### 2. Plan Resources

Analyze each use case to identify reusable resources:

| Resource Type | Purpose | Example |
|:--------------|:--------|:--------|
| `scripts/` | Deterministic, repeatable code | `rotate_pdf.py` |
| `references/` | Documentation Claude reads | `api-schema.md` |
| `assets/` | Files used in output | `template.pptx` |

### 3. Write Frontmatter

**CRITICAL**: The `description` field determines skill activation.

```yaml
---
name: lowercase-with-hyphens
description: [Directive] [What it does] [When to activate] [How to behave]
category: domain-category
keywords: keyword1, keyword2
---
```

**Directive Strength by Skill Type:**

| Type | Pattern | Example Prefix |
|:-----|:--------|:---------------|
| Mandatory | Domain-specific expertise | `MUST BE USED when...` |
| Proactive | Auto-activate after tasks | `Use PROACTIVELY for...` |
| On-Demand | User-triggered | `Use when...` |

**MANDATORY**: Read `references/description-templates.md` for complete examples.

### 4. Write SKILL.md Body

**Writing Style:**
- Use imperative/infinitive form (verb-first): "To accomplish X, do Y"
- **NEVER** use second person: ~~"You should do X"~~
- Keep body under 500 lines; move details to `references/`

**Structure:**
```markdown
# Skill Name

## Overview
[2-3 sentences describing purpose]

## When to Use
[Bullet list of triggers]

## Workflow
[Step-by-step instructions]

## Critical Rules
[MANDATORY/NEVER/ALWAYS directives]

## Resources
[References to scripts/, references/, assets/]
```

### 5. Validate

Run through the compliance checklist in `references/compliance-checklist.md`.

**Quick Validation:**
- [ ] Frontmatter has `name` and `description`
- [ ] Description uses directive language (MUST/PROACTIVELY/Use when)
- [ ] Body uses imperative form, not second person
- [ ] Body < 500 lines; detailed content in `references/`
- [ ] All referenced files exist

### 6. Iterate

After using the skill on real tasks:
1. Identify struggles or inefficiencies
2. Strengthen trigger phrases if skill doesn't activate
3. Move long sections to `references/`
4. Add missing examples or scripts

## Critical Rules

**MANDATORY:**
- Read `references/description-templates.md` before writing frontmatter
- Use directive language (MUST BE USED, Use PROACTIVELY) for reliable activation
- Keep SKILL.md body lean; move detailed content to `references/`

**NEVER:**
- Use second person ("You should...", "You need to...")
- Use weak language ("should be used", "recommended for")
- Duplicate content between SKILL.md and references/
- Exceed 500 lines in SKILL.md body

**ALWAYS:**
- Write in third-person for description field
- Include specific trigger phrases users would say
- Reference supporting files so Claude knows they exist

## Resources

### Reference Files

| File | Content |
|:-----|:--------|
| `references/description-templates.md` | Optimal description examples by skill type |
| `references/compliance-checklist.md` | Full validation checklist |
| `references/progressive-disclosure.md` | Deep dive on three-level loading |
| `references/skill-creator-original.md` | Legacy Anthropic skill-creator reference |
