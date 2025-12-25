# Skill vs Command vs Rule Selection Guide

## Overview

Choosing the right construct for automation needs is critical for effective Claude Code development. This guide provides decision frameworks and comparison criteria.

## Quick Decision Matrix

| Scenario | Use This | Rationale |
|:---------|:---------|:----------|
| Manual trigger for repeatable task | **Command** | User initiates with explicit action |
| Auto-apply expertise on topic mention | **Skill** | Triggers automatically by context |
| Always-on constraint for every interaction | **Rule** | Enforced globally across all interactions |
| Autonomous multi-step subprocess | **Agent** | Independent task execution |

## Detailed Comparison

| Aspect | **Skill** | **Command** | **Rule** | **Agent** |
|:-------|:----------|:------------|:---------|:----------|
| **Trigger** | Automatic on topic mention | Manual via user action | Automatic on tool/event | Automatic via description |
| **Best For** | Domain expertise, QA workflows | Repeatable manual actions | Always-on constraints | Complex autonomous tasks |
| **Scope** | Topic-specific | Single action | Global/project-wide | Multi-step workflows |
| **User Intent** | "Help me understand X" | "Do this specific thing" | "Never/Always do Y" | "Handle this complex task" |

## Decision Framework

### The Decision Framework

**Create a Command** for manually triggering specific, repeatable actions.
- *Analogy:* A keyboard shortcut or macro button.
- *Example:* Running tests, fixing linting, triggering builds.

**Create a Skill** for automatically applying complex expertise when relevant topics come up.
- *Analogy:* An expert consultant who walks in when their specialty is mentioned.
- *Example:* Flutter widget patterns, pharmaceutical data analysis, database operations.

**Create a Rule** for always-on instructions that must be followed for every interaction.
- *Analogy:* The project's "Constitution" or "Employee Handbook."
- *Example:* Always use TypeScript, never use placeholders, specific coding standards.

**Create an Agent** for autonomous multi-step workflows requiring independent reasoning.
- *Analogy:* A specialist who takes ownership of complex tasks.
- *Example:* Security analysis, comprehensive test generation, project planning.

### Decision Tree

```
START
│
├─ Does the user MANUALLY trigger this?
│  └─ YES → Create a **Command**
│          Pattern: "I want to run X manually"
│
├─ Should this apply to EVERY interaction?
│  └─ YES → Create a **Rule**
│          Pattern: "Never/Always do Y"
│
├─ Is this autonomous multi-step work?
│  └─ YES → Create an **Agent**
│          Pattern: "Handle this complex process independently"
│
└─ Default → Create a **Skill**
            Pattern: "Apply expertise when X is mentioned"
```

## Deep Dive: When to Use Each

### Skills: The Expert Consultant

**Use Skills when:**
- Domain-specific expertise needs to be applied
- Capability should auto-activate on topic mention
- Multiple workflows or patterns exist within one domain
- Quality assurance should run after certain tasks

**Characteristics:**
- Progressive disclosure (lightweight activation)
- Proactive triggering (MUST BE USED, Use PROACTIVELY)
- Context-specific scope

**Examples:**
- `skill-development` - Meta-guidance for creating skills
- `implementing-shadcn-ui` - UI component expertise
- `working-with-drift-db` - Database operations guidance

### Commands: The Keyboard Shortcut

**Use Commands when:**
- User manually triggers a specific, repeatable action
- Single-purpose workflow or script execution
- Quick access to complex prompts
- User-controlled timing and context

**Characteristics:**
- Manual trigger only
- Reactive execution
- Atomic, focused actions

**Examples:**
- `/commit` - Run git commit with quality gates
- `/test` - Execute specific test suite
- `/review` - Code review workflow

### Rules: The Project Constitution

**Use Rules when:**
- Behavior must be enforced across ALL interactions
- Blocking or warning about dangerous operations
- Always-on quality or security constraints
- Checklist requirements before completion

**Characteristics:**
- Always-on enforcement
- Global scope
- Blocking or warning actions

**Examples:**
- Block `print()` statements in code
- Warn about editing sensitive files
- Require tests before stopping
- Prevent dangerous commands

### Agents: The Autonomous Worker

**Use Agents when:**
- Complex multi-step workflows need autonomy
- Task requires independent reasoning and decision-making
- Subprocess coordination with its own context
- Specialized expertise for extended operations

**Characteristics:**
- Independent execution
- Multi-step workflows
- Specialized context

**Examples:**
- `code-reviewer` - Deep security analysis
- `test-generator` - Comprehensive test creation
- `planner` - Complex project planning

## Integration Patterns

### Skill + Command

The Skill provides expertise; the Command triggers manual workflows.

**Example: Quality Gates**
```
Skill: validating-quality-gates
- Auto-activates before commits
- Contains zero-warning policy documentation
- Provides comprehensive QA workflow

Command: /commit
- Manually triggers quality gate workflow
- Runs tests, analysis, fixes
- Creates git commit
```

### Skill + Rule

The Skill provides how-to; the Rule enforces must-not.

**Example: Logger Service**
```
Skill: maintaining-code-quality
- Contains LoggerService usage patterns
- Explains why print() is forbidden
- Shows proper logging implementation

Rule: block-print-statement
- Blocks any print() statement in code
- Warns user about LoggerService requirement
- Enforced across all file edits
```

### Skill + Agent

The Skill provides guidance; the Agent executes complex workflows.

**Example: Code Review**
```
Skill: code-review-standards
- Defines review criteria
- Contains security checklist
- Provides output format templates

Agent: security-analyzer
- Autonomous deep-dive analysis
- Multi-file vulnerability scanning
- Independent report generation
```

## Common Anti-Patterns

### Don't Use a Skill When:

**Bad:** Creating a skill for manually triggered actions
```yaml
# Wrong: Skills are for auto-activation
name: run-tests
description: Manually run the test suite
```
**Correct:** Use a Command instead

**Bad:** Creating a skill for global constraints
```yaml
# Wrong: Rules are for always-on enforcement
name: no-console-log
description: Never use console.log in code
```
**Correct:** Use a Rule instead

### Don't Use a Command When:

**Bad:** Manual command for expertise that should auto-apply
```markdown
# Wrong: Should auto-activate on topic
description: Apply Flutter architecture patterns
```
**Correct:** Use a Skill

### Don't Use a Rule When:

**Bad:** Rule for domain-specific guidance
```
# Wrong: Rules are constraints, not tutorials
event: prompt
pattern: how to.*flutter
```
**Correct:** Use a Skill

## At Skill Creation: Integration Check

After completing skill design, evaluate complementary constructs:

1. **Should a Command trigger this workflow manually?**
   - Ask: Would users want manual control over this?
   - If yes: Document that a command pattern should be considered

2. **Should a Rule enforce related constraints?**
   - Ask: Are there must-not behaviors this skill implies?
   - If yes: Document that a rule pattern should be considered

3. **Should an Agent handle autonomous subtasks?**
   - Ask: Are there complex multi-step subtasks?
   - If yes: Document that an agent delegation pattern should be considered

**For complete guidance on implementing each construct type, refer to the respective documentation for that construct.**

## Quick Reference: By User Intent

| User says... | Create... | Example |
|:-------------|:----------|:---------|
| "I need a keyboard shortcut for X" | **Command** | `/deploy` |
| "When I mention Y, apply Z" | **Skill** | `dart-analysis` |
| "Never allow pattern P" | **Rule** | Block dangerous commands |
| "Handle this complex multi-step task" | **Agent** | `security-reviewer` |
| "Teach Claude about X domain" | **Skill** | `drizzle-orm` |
| "Run these tests every time I commit" | **Command** + **Rule** | `/commit` + pre-commit rule |
