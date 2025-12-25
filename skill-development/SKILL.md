---
name: skill-development
description: MUST BE USED when creating, improving, or reviewing Agent Skills. Use PROACTIVELY when user mentions "create a skill", "new skill", "write a skill", "improve skill", "skill description", or "progressive disclosure". Guides through specification-compliant skill design with three-level progressive disclosure.
category: meta
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

### Skill vs Other Constructs

Skills are one of four Claude Code automation constructs. For guidance on choosing between Skills, Commands, Rules, and Agents, see `references/skill-vs-command-vs-rule-selection.md`.

**Quick reference:**
- **Skill**: Expertise that auto-applies when topics are mentioned
- **Command**: Manually triggered repeatable actions
- **Rule**: Always-on constraints enforced globally
- **Agent**: Autonomous multi-step subprocess

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

### 7. Integration Check

After validating the skill, consider complementary constructs:

**Command Integration:**
- Should a manual command trigger this workflow?
- Document command pattern if users need manual control

**Rule Integration:**
- Should rules enforce constraints mentioned in this skill?
- Reference rule patterns for must-not behaviors

**Agent Integration:**
- Should agents handle autonomous subtasks?
- Document agent delegation patterns

**For complete guidance:** See `references/skill-vs-command-vs-rule-selection.md`

## Example: End-to-End Skill Creation

**User Query**: "I need a skill to fill PDF forms programmatically"

### Step 1 - Understand Use Cases
- **User queries**: "fill PDF form", "populate PDF fields", "PDF form automation"
- **Domain**: PDF form manipulation, field extraction, data population
- **Expertise**: PDF library (pdflib), form field types, validation

### Step 2 - Plan Resources
- `scripts/extract_fields.py` - Extract form field metadata
- `scripts/fill_form.py` - Populate fields with data
- `references/pdflib-api.md` - Library documentation
- `references/field-types.md` - Form field reference

### Step 3 - Write Frontmatter
```yaml
---
name: pdf-form-filler
description: Fills PDF forms programmatically by extracting form fields and populating with data. Use when creating fillable PDF forms or filling existing forms with user data. Supports field validation, dropdown population, checkbox handling, and signature placeholder insertion.
category: pdf-processing
keywords: pdf, form, fill, populate, acroform
---
```

### Step 4 - Write SKILL.md Body
```markdown
# PDF Form Filler

Automates PDF form field extraction and data population.

## Overview
Extracts form field metadata from PDF files and populates fields with provided data values. Handles text fields, checkboxes, dropdowns, and signature placeholders.

## When to Use
- User mentions "fill PDF form" or "populate PDF"
- Creating automated form filling workflows
- Batch processing PDF forms with data

## Workflow
1. Extract fields using `scripts/extract_fields.py`
2. Map data to field names (see `references/field-types.md`)
3. Populate using `scripts/fill_form.py`
4. Validate required fields are filled

## Critical Rules
**MANDATORY**: Read `references/pdflib-api.md` for field type handling
**NEVER**: Assume field naming - always extract first
**ALWAYS**: Validate output PDF is writable

## Resources
- `scripts/extract_fields.py` - Field extraction utility
- `scripts/fill_form.py` - Form population script
- `references/pdflib-api.md` - Complete API documentation
- `references/field-types.md` - Field type reference
```

### Step 5 - Validate
- [x] Frontmatter has `name` and `description`
- [x] Description uses directive language ("Use when")
- [x] Body uses imperative form, not second person
- [x] Body < 500 lines
- [x] All referenced files exist or are planned

### Step 6 - Iterate
After testing: add validation patterns, move API details to `references/`, strengthen triggers for "acroform" queries.

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
| `references/skill-vs-command-vs-rule-selection.md` | Decision framework: Skill vs Command vs Rule vs Agent |
| `references/skill-creator-original.md` | Legacy Anthropic skill-creator reference |
