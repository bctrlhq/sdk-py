# bctrl

Python SDK for the BCTRL public API.

## Install

```bash
pip install bctrl
```

## Quick Start

```python
from bctrl import Bctrl

bctrl = Bctrl(api_key="bctrl_...")

with bctrl.runtimes.started_browser(name="checkout") as browser:
    print(browser.cdp_url)

    conversation = bctrl.conversations.create(
        runtime_id=browser.runtime_id,
    )
    bctrl.conversations.messages.create(
        conversation["id"],
        text="Extract the invoice number and total.",
    )
    for event in bctrl.conversations.stream(conversation["id"]):
        print(event)
```

Python methods use `snake_case`; the SDK sends the API's camelCase fields on the
wire. For example, `runtime_path` becomes `runtimePath`.

## Human-facing Views

Views are the supported way to share live progress and recordings. The bearer
URL is returned only when the view is created:

```python
view = bctrl.views.create(
    scope={"runtime_id": "runtime_..."},
    components={
        "live": {"control": "none"},
        "recordings": {},
    },
    expires_in_seconds=3600,
)

print(view["url"])
```

Set the `chrome=none` query parameter before the URL fragment when embedding
the complete white-label view in your own application. Organization branding
is managed with `bctrl.account.get()` and `bctrl.account.update(...)`. Signed
event delivery is managed through `bctrl.webhooks`, including secret rotation,
delivery inspection, and redelivery.

## Design

- Sync-first client.
- Route-first namespaces that mirror the API reference.
- Raw response bodies as dictionaries.
- Python context managers for runtime lifecycle cleanup.
- Typed built-in Tool inputs generated from the canonical Tool registry.
- Sync SSE iterators for Conversations and unified Run streams.
- Explicit helpers for pagination and multipart uploads.
- No hidden follow-up requests or stateful resource refreshes.

## License

ISC
