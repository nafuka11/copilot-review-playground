---
name: naming-convention
description: Python function naming convention requiring fnD_ prefix for all functions defined with def
---

# Function Naming Convention

All Python function names MUST start with the prefix `fnD_`.

Examples of correct names:
- `fnD_calculate_total`
- `fnD_get_user`
- `fnD_process_data`

Examples of incorrect names (must be flagged in code review):
- `calculate_total` (missing `fnD_` prefix)
- `get_user` (missing `fnD_` prefix)
- `process_data` (missing `fnD_` prefix)

This rule applies to all functions defined with `def` in Python files.
