## Walkthrough: PDF Form Filler (End-to-End)

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

### Step 3 - Frontmatter (example)
```yaml
---
name: pdf-form-filler
description: Fills PDF forms programmatically by extracting form fields and populating with data. Use when creating fillable PDF forms or filling existing forms with user data. Supports field validation, dropdown population, checkbox handling, and signature placeholder insertion.
metadata:
  category: pdf-processing
  keywords: [pdf, form, fill, populate, acroform]
---
```

### Step 4 - SKILL.md Body (outline)
1. Extract fields (`scripts/extract_fields.py`)
2. Map data to field names (see `references/field-types.md`)
3. Populate using `scripts/fill_form.py`
4. Validate required fields are filled

### Step 5 - Critical Rules
- **MANDATORY**: Read `references/pdflib-api.md` for field type handling
- **NEVER**: Assume field naming - always extract first
- **ALWAYS**: Validate output PDF is writable

### Notes
- **MANDATORY**: Validate usage with `scripts/validate_skill.py` before sharing the skill
- **ALWAYS**: Keep large API docs in `references/` not in `SKILL.md`
