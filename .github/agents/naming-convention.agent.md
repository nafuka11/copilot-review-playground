---
name: naming-convention
description: Enforces Python function naming convention requiring fnF_ prefix for all functions defined with def
---

# Function Naming Convention

All Python function names MUST start with the prefix `fnF_`.

Examples of correct names:
- `fnF_calculate_total`
- `fnF_get_user`
- `fnF_process_data`

Examples of incorrect names (must be flagged in code review):
- `calculate_total` (missing `fnF_` prefix)
- `get_user` (missing `fnF_` prefix)
- `process_data` (missing `fnF_` prefix)

This rule applies to all functions defined with `def` in Python files.
