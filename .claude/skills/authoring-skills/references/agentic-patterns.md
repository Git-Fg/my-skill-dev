# Agentic Patterns & Prompt Engineering

To create robust skills, you must embed explicit reasoning and verification structures into the `SKILL.md`.

## 1. Chain of Thought (CoT) Enforcement

Don't just list steps. Force the agent to plan.

**Bad:**
> 1. Read the file.
> 2. Update the date.

**Good (CoT):**
> 1. **Analyze**: Read the target file. Identify the current date format and location.
> 2. **Plan**: Construct the new date string matching the existing format.
> 3. **Execute**: Apply the change.

## 2. Verification Loops (Self-Correction)

Agents make mistakes. Your skill must explicitly tell them how to check their work.

**Pattern:**
> 1. **Action**: Run `scripts/generate_report.py`.
> 2. **Verify**: Read `report_output.json`. Check if the field "status" is "success".
> 3. **Recover**: If "status" is "error", read the "error_msg" field, correct the input parameters, and retry Step 1.

## 3. XML Structuring

Use XML tags to delimit sections in your instructions. This reduces hallucination by clearly separating context.

**Example in SKILL.md:**
```markdown
<workflow>
1. Analyze the input...
2. Run the script...
</workflow>

<critical_constraints>
- NEVER delete files without backup.
</critical_constraints>
```

## 4. State of the World (Context Injection)

Project skills often lack context. Instructions should start by gathering state.

**Pattern:**
> Before making changes, ALWAYS run `ls -R` on the target directory or use `grep` to understand the current file structure. Do not assume file locations.

## 5. Degrees of Freedom: Choosing the Instruction Style

You MUST analyze the "Fragility" of the task to choose the instruction style.

### Scenario A: Low Freedom (Fragile/Deterministic)
*Examples: DB Migrations, API Deployments, Regex parsing.*
- **Strategy**: Rigid Scripts.
- **Prompting**: "Run exactly this script. Do not deviate. Do not attempt to fix manually via text editing."
- **Why**: Small deviations cause catastrophic failure.

### Scenario B: High Freedom (Creative/Contextual)
*Examples: Code Review, Documentation writing, Summarization.*
- **Strategy**: Heuristics & Checklists.
- **Prompting**: "Review against these principles. Use your judgment for phrasing. Ensure X and Y are present."
- **Why**: There is no single "correct" output; the model's intelligence is the asset.
