"""Render templates to update to new tag."""
import os
from pathlib import Path

import httpx
from jinja2 import Template

HERE = Path(__file__).parent
REPO_ROOT = HERE.parent.parent


def get_latest_tag() -> str:
    """Get latest tag of https://github.com/rhysd/actionlint .

    Returns
    -------
    str
        Latest tag string.
    """
    resp = httpx.get("https://api.github.com/repos/rhysd/actionlint/tags")
    return resp.json()[0]["name"]


def render_templates(tag: str) -> None:
    """Renders templates with new ``tag`` if the value has changed.

    Parameters
    ----------
    tag: str
        _description_
    """
    version_file_path = REPO_ROOT / ".version"
    current_version = version_file_path.read_text(encoding="utf8")
    if tag != current_version:
        hook_template = Template(
            (HERE / ".pre-commit-hooks-template.yaml").read_text(encoding="utf8")
        )
        (REPO_ROOT / ".pre-commit-hooks.yaml").write_text(
            hook_template.render({"tag": tag}), encoding="utf8"
        )
        readme_template = Template(
            (HERE / "readme-template.md").read_text(encoding="utf8")
        )
        (REPO_ROOT / "README.md").write_text(
            readme_template.render({"tag": tag}), encoding="utf8"
        )
        version_file_path.write_text(tag, encoding="utf8")
        gh_output = os.getenv("GITHUB_OUTPUT", None)
        if gh_output is not None:
            with Path(gh_output).open("a", encoding="utf8") as f:
                f.writelines([f"tag={tag}\n", f"current_version={current_version}\n"])


if __name__ == "__main__":
    tag = get_latest_tag()
    render_templates(tag)
