# Description Templates by Skill Type

The `description` field is the most critical field for skill activation. Use directive language to ensure reliable triggering.

## Pattern Structure

```
[Directive] [What it does] [When to activate] [How to behave (optional)]
```

## Templates by Activation Type

### 1. Domain-Specific Mandatory Skills (MUST BE USED)

For specialized file formats or domain knowledge that general-purpose systems cannot handle reliably.

#### Basic Structure

```yaml
description: MUST BE USED when analyzing [file type/domain]. Use PROACTIVELY to [action]. You are a specialized [role]. Your purpose is to [mission].
allowed-tools: [Read, Grep, Glob] # Optional: restrict tools for safety
compatibility: "python>=3.11"      # Optional: specify runtime requirements
```

**Examples:**

```yaml
# Dynamo XML Analysis
description: MUST BE USED when analyzing Dynamo (.dyn) XML files. Use PROACTIVELY to extract Python nodes, custom packages, and workflow summaries. You are a specialized Dynamo XML analysis expert. Your purpose is to analyze Dynamo XML files and extract comprehensive information about Python nodes, custom packages, and workflow logic.

# Salesforce Metadata
description: MUST BE USED when working with Salesforce metadata (.md) XML files or retrieving object definitions. Use PROACTIVELY to parse Salesforce metadata, extract field definitions, validation rules, and relationships. You are a Salesforce metadata expert specializing in XML structure analysis and object relationship mapping.

# Flutter/Dart Architecture
description: MUST BE USED when scaffolding new features in this Flutter project. Use PROACTIVELY when user mentions "new feature", "add screen", "create widget". You are a Flutter architecture expert following clean architecture patterns with Riverpod state management and Drift database.
```

### 2. Proactive Quality Assurance Skills (Use PROACTIVELY)

Auto-activate after certain task completions to ensure quality.

```yaml
description: Use PROACTIVELY for [task] after completing [trigger]. MUST BE USED when user mentions [keywords]. You are [role] focusing on [areas].
```

**Examples:**

```yaml
# Code Quality
description: Use PROACTIVELY for code quality assurance after completing any significant code changes. MUST BE USED when user mentions "review", "check quality", or requests code validation. You are an expert code reviewer focusing on security vulnerabilities, performance issues, and maintainability concerns.

# Documentation Validation
description: Use PROACTIVELY after generating documentation to validate completeness, accuracy, and formatting. MUST BE USED when user asks to review, audit, or improve documentation quality.

# Test Coverage
description: Use PROACTIVELY after implementing features to verify test coverage. MUST BE USED when user mentions "tests", "coverage", or "missing tests".
```

### 3. On-Demand Specialized Skills (Use when)

Activate when user explicitly requests the capability.

```yaml
description: [What it does]. Use when [scenarios]. Supports [capabilities].
```

**Examples:**

```yaml
# PDF Processing
description: Fills PDF forms programmatically by extracting form fields and populating with data. Use when creating fillable PDF forms or filling existing forms with user data. Supports field validation, dropdown population, checkbox handling, and signature placeholder insertion.

# DOCX Redlining
description: Creates tracked changes (redlines) in Microsoft Word documents for legal and business document review. Use when editing contracts, agreements, or any document requiring change tracking. Supports insertions, deletions, formatting changes, and comment annotations.

# Excel Reports
description: Generates Excel spreadsheets with complex formatting, formulas, charts, and pivot tables from data. Use when creating financial reports, data analysis dashboards, or automated reporting solutions.
```

### 4. Workflow Orchestration Skills

Coordinate multi-step processes or subprocess coordination.

```yaml
description: Orchestrates [workflow]. Coordinate [components]. Use when [trigger]. MANDATORY: [critical behavior].
```

**Examples:**

```yaml
# Spec-Driven Development
description: Orchestrates spec-driven development workflow (Requirements → Design → Tasks → Implementation). Coordinate subprocesses through approval gates for enterprise-grade feature planning. Use when user mentions "requirements", "design doc", "implementation plan", or needs structured feature development. MANDATORY: Never create documents directly; always launch appropriate subprocesses.

# Code Review Pipeline
description: Orchestrates comprehensive code review process across multiple analysis dimensions (security, performance, maintainability, testing). Coordinate specialized review processes and aggregate findings into actionable feedback.
```

### 5. MCP Orchestrator Skills

Skills that coordinate external MCP tools alongside local scripts.

**Template:**
```yaml
description: Orchestrates database migration using Postgres MCP and local validation. Use when user asks to "migrate db" or "update schema". Requires `Postgres:query_tool` and `Postgres:schema_tool`.
allowed-tools: Postgres:*, Bash, Read
```

**Instruction Pattern:**
1. **Fetch State**: Use `Postgres:schema_tool` to get current state.
2. **Plan**: Generate SQL migration file locally.
3. **Execute**: Use `Postgres:query_tool` to apply changes.

### 6. Prompt Engineering / Meta Skills

Help create, review, or optimize system prompts.

```yaml
description: Use this skill when the user needs to [operations]. This includes [scope]. Examples: "[example 1]", "[example 2]". You are [expertise].
```

**Examples:**

```yaml
# Prompt Engineer
description: Use this skill when the user needs to create, modify, review, or optimize system prompts. This includes requests to improve prompt effectiveness, add specific behaviors, refine instructions, or evaluate existing prompts for clarity and performance. Examples: "review this customer service prompt", "create a system prompt for summarizing documentation". You are an expert prompt engineer specializing in crafting, reviewing, and optimizing system prompts.

# Skill Creator
description: MUST BE USED when creating, improving, or reviewing Skills. Use PROACTIVELY when user mentions "create a skill", "new skill", "write a skill", "improve skill". Guides through specification-compliant skill design with three-level progressive disclosure.
```

## Directive Strength Reference

| Phrase | Impact | Use When |
|:-------|:-------|:---------|
| `MUST BE USED` | Skill **always** activates when trigger matches | Domain-specific tasks requiring expertise |
| `Use PROACTIVELY` | Skill **automatically** activates without waiting | Quality assurance, validation, review tasks |
| `Use when` | Skill activates **on relevant mention** | General-purpose skills, optional tools |
| `Should be used` | **WEAK** - skill may skip | **AVOID** |

## Anti-Patterns (Avoid These)

```yaml
# ❌ Too vague - the runtime can't determine relevance
description: Helps with PDF files.

# ❌ First person - violates spec
description: I extract text from PDFs and analyze them.

# ❌ Passive/weak language
description: This skill should be used when working with Dynamo files.

# ❌ No triggers
description: Analyzes XML files and provides summaries.

# ❌ Critical info buried in long text
description: This skill provides comprehensive support for a wide variety of document processing tasks including but not limited to PDF manipulation, DOCX editing, image extraction...
```

## Quick Reference Table

| Skill Type | Key Phrase | Template |
|:-----------|:-----------|:---------|
| Domain expert | `MUST BE USED when...` | `MUST BE USED when [domain]. You are a specialized [role].` |
| Proactive QA | `Use PROACTIVELY for...` | `Use PROACTIVELY for [task]. MUST BE USED when [triggers].` |
| On-demand tool | `Use when...` | `[What]. Use when [scenarios]. Supports [features].` |
| Orchestrator | `Orchestrates...` | `Orchestrates [workflow]. Coordinate [components].` |
| Multi-example | `Examples: "..."` | `[Operations]. Examples: "[query1]", "[query2]".` |
