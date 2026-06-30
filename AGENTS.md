# python-sdk

Python SDK for the bctrl public v1 API.

Mirrors the TypeScript SDK's route-first resource model, uses snake_case at the
Python boundary, and stays sync-first. Source of truth is
`packages/api-contracts` / public OpenAPI.

Gotcha: not in the pnpm workspace; build and publish separately with
`python -m build`.
