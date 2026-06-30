# Release

This package is intended to live at `bctrlhq/sdk-py` and publish `bctrl`.

## Publish Setup

1. Create the GitHub repository under `bctrlhq`.
2. Configure PyPI trusted publishing for the package with this repository and the `pypi` environment.
3. Push a tag like `v0.1.1`.

The publish workflow uses GitHub OIDC via `pypa/gh-action-pypi-publish`. Do not add long-lived PyPI tokens.

## Versioning

Update both `pyproject.toml` and `bctrl/version.py` before tagging.
