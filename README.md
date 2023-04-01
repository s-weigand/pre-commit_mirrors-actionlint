# actionlint mirror

Mirror of `actionlint` for pre-commit.

For pre-commit: see https://github.com/pre-commit/pre-commit

For actionlint: see https://github.com/rhysd/actionlint

### Using actionlint with pre-commit

Add this to your `.pre-commit-config.yaml`:

```yaml
- repo: https://github.com/s-weigand/pre-commit_mirrors-actionlint
  rev: "v1.6.23"
  hooks:
    - id: actionlint
```