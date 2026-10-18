# Release

The Python `bctrl` package and `@bctrl/sdk` release together under one version.

1. In the platform repo, set the version and regenerate both SDKs:
   `node scripts/generate/fern-clients.mjs --release 3.1.0` (with `BCTRL_SDK_JS_DIR`, `BCTRL_SDK_PY_DIR` and
   `BCTRL_CLI_DIR` pointing at checkouts of `sdk-js`, this repo and `cli`). The version lives in `bctrl/_version.py`.
2. Merge the resulting changes here and in `sdk-js` after CI passes.
3. Publish a GitHub release tagged `v3.1.0` on the merge commit (`gh release create v3.1.0 --generate-notes`).
   The Publish workflow verifies the tag against the package version and publishes through PyPI trusted publishing.

PyPI trusted publishing must name this repository, the `publish.yml` workflow and the `pypi` environment.
