# Project Skills Constraints (.claude/skills)

These skills live in a shared Git repository. They must be environment-agnostic.

## 1. Path Handling
- **Constraint**: Scripts and instructions must assume execution from the **Project Root**.
- **Anti-Pattern**: Hardcoding `/Users/name/...` or assuming `cd .claude/skills/my-skill` has happened.
- **Best Practice**: Use language-specific methods to resolve paths relative to the script location if accessing internal assets.

## 2. Dependency Management
- **Constraint**: You cannot assume the user has specific libraries installed globally.
- **Solution**: 
    1. Prefer standard libraries (e.g., Python `json`, `os`, `sys`).
    2. If external libs are needed (`pandas`, `requests`), the skill description MUST state: "Requires `pip install X`".
    3. Better: Provide a `scripts/setup.py` or check imports in your main script and fail with a clear message: "Please run `pip install X`".

## 3. Git Hygiene
- **Constraint**: Generated files (logs, temp files) must not pollute the repo.
- **Solution**: Instructions should direct output to `.gitignore`d folders (like `tmp/` or `build/`) or clean up after themselves.

## 4. No Human-in-the-Loop (No HITL)
- **Constraint**: Scripts must run non-interactively.
- **Forbidden**: `input("Press Enter")`, `confirm = input()`.
- **Allowed**: CLI arguments (`--force`, `--dry-run`).
