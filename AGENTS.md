# python-sdk

The official Python library for the bctrl public v1 API: Fern-generated sync and
async clients plus a few hand-written helpers, snake_case at the Python boundary.
Source of truth is the platform repo's public OpenAPI.

- `bctrl/_generated`: generated clients; change generator inputs or adapters in the
  platform repo, then regenerate. Do not edit by hand. Retry safety lives in its transport.
- `bctrl/lib`: hand-written helpers (browser handles, conversation history,
  pagination, waits); `bctrl/_client.py` wires them onto `Bctrl`/`AsyncBctrl`.
- The version lives in `bctrl/_version.py`. Releases: RELEASE.md.

Not in the pnpm workspace. Run pytest, pyright and mypy against the installed package
in Linux (`pip install . pytest pyright mypy`).
