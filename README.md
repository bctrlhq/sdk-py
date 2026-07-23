# bctrl

Python SDK for the BCTRL public API.

## Install

```bash
pip install bctrl
```

## Quick Start

```python
from bctrl import Bctrl
from pydantic import BaseModel, ConfigDict


class Invoice(BaseModel):
    model_config = ConfigDict(extra="forbid")

    invoiceNumber: str
    total: float

bctrl = Bctrl(api_key="bctrl_...")

with bctrl.runtimes.started_browser(name="checkout") as browser:
    print(browser.connect_url)

    invocation = bctrl.runtimes.invocations.create_and_wait(
        browser.runtime_id,
        action="extract",
        instruction="Extract the invoice number and total.",
        output_model=Invoice,
    )

    invoice = invocation["parsed_output"]
    print(invoice.invoiceNumber, invoice.total)

    for event in bctrl.runs.events.stream(browser.run_id):
        print(event)
```

Python methods use `snake_case`; the SDK sends the API's camelCase fields on the
wire. For example, `runtime_path` becomes `runtimePath`.

## Human-facing Views

Views are the supported way to share live progress, recordings, activity, and
human actions. The bearer URL is returned only when the view is created:

```python
view = bctrl.views.create(
    scope={"runtime_id": "runtime_..."},
    components={
        "live": {"control": "none"},
        "recordings": {},
        "activity": {},
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
- Pydantic model support for invocation output schemas.
- Python context managers for runtime lifecycle cleanup.
- Sync SSE iterators for run events and activity.
- Explicit helpers for pagination, multipart uploads, and `create_and_wait`.
- No hidden follow-up requests or stateful resource refreshes.

## License

ISC
