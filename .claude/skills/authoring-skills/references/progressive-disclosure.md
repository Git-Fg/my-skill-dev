# Progressive Disclosure Design

Skills use progressive disclosure to manage context efficiently. This principle ensures runtimes remain fast and responsive while having access to extensive domain knowledge when needed.

## Three-Level Loading System

### Level 1: Discovery (~100-200 tokens)

At startup or when browsing available skills, runtimes/loaders may initially load only the frontmatter metadata:

```yaml
name: dynamo-xml-analyzer
description: MUST BE USED when analyzing Dynamo (.dyn) XML files...
```

**Purpose:** Enable the runtime to determine which skills are relevant to the current task without loading full instructions.

**Best Practice:** The `description` field must contain sufficient keywords and trigger phrases to enable accurate matching.

### Level 2: Activation (<5000 tokens recommended)

When a task matches a skill's description, the runtime loads the full `SKILL.md` body content:

```markdown
# Dynamo XML Analyzer

## Overview
[Detailed explanation of Dynamo XML structure]

## Critical Rules
**MANDATORY**: Read `references/dynamo-schema.md` before parsing...

## Workflow
1. Validate XML structure
2. Extract Python nodes using `scripts/extract_nodes.py`
...
```

**Purpose:** Provide comprehensive procedural instructions, domain knowledge, and behavioral directives needed to execute the task.

**Best Practice:** Keep SKILL.md under 500 lines. Move extensive reference material to `references/` directory.

### Level 3: Execution (on-demand, unlimited)

During execution, the runtime or executor loads or uses bundled resources as needed:

- **scripts/** - Executed without loading into context (Python, Bash, etc.)
- **references/** - Loaded only when referenced in instructions
- **assets/** - Used in output, not loaded into context

**Purpose:** Provide unlimited domain knowledge, code templates, and resources without bloating the activation context.

**Best Practice:** Use `references/` for large documentation. Include grep patterns in SKILL.md if reference files are large (>10k words).

## Why Progressive Disclosure Matters

| Without Progressive Disclosure | With Progressive Disclosure |
|:-------------------------------|:----------------------------|
| Loading all skills at startup → Slow startup | Loading only metadata at startup → Fast startup |
| All instructions in context → Token bloat | Instructions loaded on-demand → Efficient token usage |
| Reference docs always loaded | Reference docs loaded only when needed |
| Hard to scale beyond ~10 skills | Can support 100+ skills efficiently |

## Design Principles for Each Level

### Level 1 (Discovery) Design

- Focus on **keywords and triggers**
- Use directive language (MUST, USE PROACTIVELY)
- Define scope and boundaries clearly
- Include examples of user queries that should trigger activation

### Level 2 (Activation) Design

- Structure with clear sections (Overview, When to Use, Workflows, Critical Rules)
- Use imperative directives (MANDATORY, NEVER, ALWAYS)
- Include decision trees (if X then Y, if Z then W)
- Reference external resources rather than duplicating content

### Level 3 (Execution) Design

- `scripts/` - Self-contained, well-documented code
- `references/` - One level deep, clearly named
- `assets/` - Templates and resources for output generation

## Example: PDF Processing Skill

```
Startup (Discovery):
├── Load: name + description only
├── Tokens: ~50
└── Decision: "User mentioned PDF → activate pdf-processing skill"

Activation:
├── Load: Full SKILL.md
├── Tokens: ~2,500
└── Contains: Overview, workflows, critical rules, script references

Execution:
├── Load: references/pdflib-api.md (only if API needed)
├── Execute: scripts/rotate_pdf.py (not loaded into context)
└── Assets: templates/form-template.docx (copied to output)
```

## Resource Distribution Guidelines

### What Goes in SKILL.md (Always Loaded)

- Core concepts and overview (2-3 sentences)
- Essential workflows (step-by-step)
- Quick reference tables
- Pointers to references/examples/scripts
- Critical rules (MANDATORY/NEVER/ALWAYS)

**Target: 100-200 lines, max 500 lines**

### What Goes in references/ (On-Demand)

- Detailed patterns and advanced techniques
- Comprehensive API documentation
- Migration guides
- Edge cases and troubleshooting
- Extensive examples and walkthroughs

**Each file can be 2,000-5,000+ words**

### What Goes in scripts/ (Executed)

- Validation tools
- Testing helpers
- Parsing utilities
- Automation scripts

**Should be executable and documented**

### What Goes in assets/ (Output)

- Document templates
- Boilerplate code
- Brand assets
- Configuration templates

**Used in final output, not loaded into context**

## Reference Depth Rule

Keep references **one level deep** from SKILL.md. Avoid deep nesting:

```
✅ Good (one level):
SKILL.md → references/schema.md

❌ Bad (nested):
SKILL.md → references/intro.md → references/details.md
```

Runtimes may use partial reading strategies that miss nested context.

## Large Reference Handling (>10k words)

Include grep patterns in SKILL.md to help find relevant sections:

```markdown
## Database Queries

For API documentation, see `references/api.md`.

**Quick patterns:**
- Authentication: grep "auth" references/api.md
- User endpoints: grep "POST /users" references/api.md
- Error handling: grep "error" references/api.md
```
