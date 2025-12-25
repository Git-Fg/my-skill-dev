# Skill Compliance Checklist

- [ ] Validation script (scripts/validate_skill.py) returns PASS

Verify each item before finalizing a skill.

## Frontmatter (Metadata)

### Name Field
- [ ] Uses lowercase letters, numbers, and hyphens only
- [ ] Max 64 characters
- [ ] Does not start or end with hyphen
- [ ] No consecutive hyphens (`--`)
- [ ] Matches parent directory name
- [ ] Preferably gerund form (e.g., `processing-data`)

### Description Field
- [ ] Written in **third-person** perspective
- [ ] Uses appropriate directive strength:
  - [ ] `MUST BE USED` for domain-specific mandatory tasks
  - [ ] `Use PROACTIVELY` for automatic activation tasks
  - [ ] `Use when` for on-demand skills
- [ ] Avoids weak language ("should be used", "recommended for")
- [ ] Specifies *what* the skill does
- [ ] Specifies *when* to use it (trigger conditions)
- [ ] Contains clear trigger keywords for skill matching
- [ ] Under 1024 characters

### Optional Fields
- [ ] `category` populated if applicable
- [ ] `keywords` include relevant search terms
- [ ] `license` if distributing externally

## Body Content (Instructions)

### Writing Style
- [ ] Uses **imperative/infinitive form** (verb-first)
- [ ] Does **NOT** use second person ("you should", "you need")
- [ ] Uses objective, instructional language

### Structure
- [ ] Organized with clear sections (Overview, When to Use, Workflow, Critical Rules)
- [ ] Contains MANDATORY/NEVER/ALWAYS directives for critical behaviors
- [ ] Includes concrete examples where helpful

### Length
- [ ] Under 500 lines (target: 100-200 lines)
- [ ] Detailed content moved to `references/`
- [ ] Total body under 5000 tokens

## Progressive Disclosure

### Level 1 (Discovery)
- [ ] Description is concise (~100-200 tokens)
- [ ] Contains clear trigger phrases

### Level 2 (Activation)
- [ ] SKILL.md body is comprehensive but lean
- [ ] References external resources rather than duplicating

### Level 3 (Execution)
- [ ] `scripts/` contains self-contained, documented code
- [ ] `references/` files are one level deep, clearly named
- [ ] `assets/` contains templates/resources for output only

## File Organization

### Paths
- [ ] All file references use forward slashes (`/`)
- [ ] All referenced files only one level deep from SKILL.md

### scripts/ (if present)
- [ ] Scripts are self-contained or document dependencies
- [ ] Include shebang and usage documentation
- [ ] Provide helpful error messages

### references/ (if present)
- [ ] Large documentation here, not in SKILL.md
- [ ] No duplication between SKILL.md and references/
- [ ] Grep patterns provided for large files (>10k words)

### assets/ (if present)
- [ ] Output-only files (templates, brand assets)
- [ ] Not documentation or instructions

## Content Quality

### Clarity Test
- [ ] Instructions can be followed without clarification

### Completeness Test
- [ ] Edge cases and error conditions covered

### Directive Test
- [ ] Critical steps marked with MANDATORY/NEVER/ALWAYS

### No Duplication
- [ ] Information lives in SKILL.md **OR** references/, not both

## Testing

- [ ] Skill triggers on expected user queries
- [ ] Content is helpful for intended tasks
- [ ] References load when needed
- [ ] Scripts execute correctly (if present)

## Quick Validation Summary

```
✓ Frontmatter: name + description with directives
✓ Body: imperative form, <500 lines
✓ Resources: scripts/references/assets properly organized
✓ No duplication, no second person
✓ Triggers work in practice
```
