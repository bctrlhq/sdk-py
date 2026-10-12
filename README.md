# BCTRL Python SDK

Sync and async clients for all current BCTRL public API operations: Browsers,
Sandboxes, Tasks, Agents, Spaces, Files, Secrets, Tools, Runs, and account resources.
Requires Python 3.10 or newer; supports Pydantic 1 and 2.

```bash
pip install bctrl
```

```python
import os
from bctrl import Bctrl, AsyncBctrl

client = Bctrl(token=os.environ['BCTRL_API_KEY'])
spaces = client.spaces.list(limit=20)
print(spaces.data)
```

Create a recording-enabled browser and stop its Run:

```python
import uuid

browser = client.browsers.create(
    name='example-browser', recording=True, wait=60,
    idempotency_key=str(uuid.uuid4()),
)
print(browser.id, browser.current_run)
client.browsers.stop(browser.id, wait=60)
```

While a browser has an active Run, upload a file into it:

```python
with open('input.txt', 'rb') as source:
    client.browsers.files.upload(
        'example-browser', path='/workspace/input.txt', file=source,
    )
```

`AsyncBctrl` exposes the same operations with awaitable methods. Models use
snake_case at the Python boundary and preserve the API's wire aliases.
Pagination, binary responses, SSE streaming, and multipart uploads are generated
from the same public contract. `bctrl.api` remains an alias for the current client.

Requests pin `BCTRL-Version: 2026-10-03`. Use `bctrl_space` and
`bctrl_subaccount_id` for authorized scope selectors. Custom `base_url` values
identify the API origin, without a trailing `/v1`.

Read operations retry transient responses. Writes automatically retry only when
an explicit idempotency key is supplied; multipart uploads, conflicts, and unknown
outcomes are not replayed. Authenticated redirects are refused, including with a
custom httpx client. Catch `BctrlError` to inspect HTTP status and error body;
unexpected response shapes retain that HTTP context.

## Migrating to 0.3

The default `Bctrl` import now uses the current generated client and accepts
`token` instead of `api_key`. Migrate Runtime/Toolset/Conversation-message workflows
to Browsers/Sandboxes and Agents/Tasks. Method signatures and the generated API
reference show the request parameters for each operation.

Historical helpers remain under `bctrl.legacy` for callers targeting an older API.
Their retired routes are not supported by the current production API.
