[//]: # "DO NOT CHANGE THIS FILE WITHOUT CHANGING .github/scripts/readme-template.md"

# ⚠️ Archived

This repository has been archived since [`actionlint` now has a its own `pre-commit` hooks](https://github.com/rhysd/actionlint/blob/main/.pre-commit-hooks.yaml).

# actionlint mirror

Mirror of `actionlint` for pre-commit.

For pre-commit: see https://github.com/pre-commit/pre-commit

For actionlint: see https://github.com/rhysd/actionlint

### Using actionlint with pre-commit

Add this to your `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/s-weigand/pre-commit_mirrors-actionlint
    rev: "v1.6.24"
    hooks:
      - id: actionlint
```
