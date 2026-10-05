# Reference
<details><summary><code>client.<a href="src/bctrl/client.py">help</a>(...) -> HelpResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return global API, SDK, and CLI help, or help for one named topic. Use query parameters so help is easy to call from browsers, CLI tools, SDKs, and plain HTTP clients.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.help()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**topic:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**audience:** `typing.Optional[HelpRequestAudience]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## account
<details><summary><code>client.account.<a href="src/bctrl/account/client.py">get</a>() -> Account</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get organization settings and their fully resolved values.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.account.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.account.<a href="src/bctrl/account/client.py">update</a>(...) -> Account</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update organization settings using JSON Merge Patch semantics. Pass dryRun=true to validate and resolve without persisting.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.account.update()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dry_run:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**branding:** `typing.Optional[BrandingPatch]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## agents
<details><summary><code>client.agents.<a href="src/bctrl/agents/client.py">list</a>(...) -> AgentsListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Agent definitions visible in the selected Space or tenant, with their promoted immutable version.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.agents.list(
    name="Production browser",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListAgentsRequestOrder]` — Order by createdAt and ID. Defaults to desc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[ResourceName]` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/bctrl/agents/client.py">create</a>(...) -> Agent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an Agent and its first immutable, promoted version in a Space.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.agents.create(
    model="model",
    name="Production browser",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**model:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `ResourceName` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**instructions:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**memory:** `typing.Optional[AgentCreateRequestMemory]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[JsonObject]` 
    
</dd>
</dl>

<dl>
<dd>

**require_approval_for_promotion:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[AgentCreateRequestScope]` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[str]` — Opaque resource ID or unique resource name in the selected Space or tenant.
    
</dd>
</dl>

<dl>
<dd>

**tools:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/bctrl/agents/client.py">get</a>(...) -> Agent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read an Agent by ID or scoped name, including its promoted version and latest draft number.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.agents.get(
    agent_id="agentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/bctrl/agents/client.py">delete</a>(...) -> AgentsDeleteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Archive an Agent definition. Existing Tasks and immutable version history remain available.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.agents.delete(
    agent_id="agentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/bctrl/agents/client.py">update</a>(...) -> Agent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Append an immutable Agent version. Tasks keep their selected version and the promoted version changes only on promotion.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.agents.update(
    agent_id="agentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**instructions:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**memory:** `typing.Optional[AgentUpdateRequestMemory]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[JsonObject]` 
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[ResourceName]` 
    
</dd>
</dl>

<dl>
<dd>

**require_approval_for_promotion:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[AgentUpdateRequestScope]` 
    
</dd>
</dl>

<dl>
<dd>

**tools:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ApiKeys
<details><summary><code>client.api_keys.<a href="src/bctrl/api_keys/client.py">list</a>(...) -> ApiKeyListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List active API keys. Use subaccountId to filter tenant keys.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.api_keys.list(
    subaccount_id="V1StGXR8_Z5jdHi6B-myT",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListApiKeysRequestOrder]` — Order by createdAt and ID. Defaults to desc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**subaccount_id:** `typing.Optional[SubaccountId]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[ListApiKeysRequestType]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.api_keys.<a href="src/bctrl/api_keys/client.py">create</a>(...) -> ApiKeyCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an organization or subaccount API key. The secret is returned once in the response. To rotate a key, create its replacement first, cut traffic over, then revoke the old key — key prefixes identify which key made a request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl, ApiKeyCreateRequestZero
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.api_keys.create(
    request=ApiKeyCreateRequestZero(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `ApiKeyCreateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.api_keys.<a href="src/bctrl/api_keys/client.py">delete</a>(...) -> ApiKeyDeleteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revoke an API key immediately. Rotation is create-then-revoke: create the replacement, cut over, then revoke the old key.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.api_keys.delete(
    key_id="keyId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## auth
<details><summary><code>client.auth.<a href="src/bctrl/auth/client.py">whoami</a>() -> AuthWhoamiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the API key actor for the current request. Use this to validate CLI credentials and show whether the key is scoped to an organization or subaccount.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.auth.whoami()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## browsers
<details><summary><code>client.browsers.<a href="src/bctrl/browsers/client.py">list</a>(...) -> BrowserListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List browser resources visible in the selected Space. A browser is running while it has a current Run and idle otherwise. Responses include the current Run and its connections when available.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.list(
    name="Production browser",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListBrowsersRequestOrder]` — Order by createdAt and ID. Defaults to desc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[ListBrowsersRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[ResourceName]` 
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[LocationRequest]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListBrowsersRequestStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.browsers.<a href="src/bctrl/browsers/client.py">create</a>(...) -> BrowserResource</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a reusable browser and durably request its first Run. Use wait to wait up to 60 seconds for startup; currentRun is null until a Run is admitted and connections appear after the browser starts.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**wait:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**auto_upgrade:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**captcha:** `typing.Optional[BrowserCreateRequestCaptcha]` 
    
</dd>
</dl>

<dl>
<dd>

**expire_after_idle_days:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**extensions:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**force_open_shadow_roots:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**gpu:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**headless:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[LocationRequest]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[JsonObject]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[ResourceName]` 
    
</dd>
</dl>

<dl>
<dd>

**network_traffic:** `typing.Optional[BrowserNetworkTrafficConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**proxy:** `typing.Optional[BrowserCreateRequestProxy]` 
    
</dd>
</dl>

<dl>
<dd>

**recording:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[BrowserCreateRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**standby_after_seconds:** `typing.Optional[float]` — Standby is currently disabled; use 0.
    
</dd>
</dl>

<dl>
<dd>

**stealth:** `typing.Optional[BrowserCreateRequestStealth]` 
    
</dd>
</dl>

<dl>
<dd>

**timeout_seconds:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**viewport:** `typing.Optional[BrowserCreateRequestViewport]` 
    
</dd>
</dl>

<dl>
<dd>

**web_rtc_proxy_only:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.browsers.<a href="src/bctrl/browsers/client.py">get</a>(...) -> BrowserResource</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read a browser and its current Run. Use wait to wait for an accepted start or stop. Saved state remains private to the browser and is restored on its next Run.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.get(
    browser_id="browserId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[GetBrowsersRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**wait:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.browsers.<a href="src/bctrl/browsers/client.py">delete</a>(...) -> BrowsersDeleteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the browser configuration and saved state, cancelling queued starts and stopping its current Run. Retained Run records remain readable.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.delete(
    browser_id="browserId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[DeleteBrowsersRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.browsers.<a href="src/bctrl/browsers/client.py">update</a>(...) -> BrowserResource</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update configuration used by the next Run. Changing stealth or viewport requires an idle browser without saved state or a queued start; stop with discardState first.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.update(
    browser_id="browserId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[UpdateBrowsersRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**auto_upgrade:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**captcha:** `typing.Optional[BrowsersUpdateRequestCaptcha]` 
    
</dd>
</dl>

<dl>
<dd>

**expire_after_idle_days:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**extensions:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**force_open_shadow_roots:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**gpu:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**headless:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[LocationRequest]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[JsonObject]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[ResourceName]` 
    
</dd>
</dl>

<dl>
<dd>

**network_traffic:** `typing.Optional[BrowserNetworkTrafficConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**proxy:** `typing.Optional[BrowsersUpdateRequestProxy]` 
    
</dd>
</dl>

<dl>
<dd>

**recording:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**standby_after_seconds:** `typing.Optional[float]` — Standby is currently disabled; use 0.
    
</dd>
</dl>

<dl>
<dd>

**stealth:** `typing.Optional[BrowsersUpdateRequestStealth]` 
    
</dd>
</dl>

<dl>
<dd>

**timeout_seconds:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**viewport:** `typing.Optional[BrowsersUpdateRequestViewport]` 
    
</dd>
</dl>

<dl>
<dd>

**web_rtc_proxy_only:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.browsers.<a href="src/bctrl/browsers/client.py">fetch</a>(...) -> BrowserFetchResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send an HTTP request from the browser itself: it carries the browser's cookies, proxy and TLS/HTTP2 fingerprint and is not subject to CORS. The response body is returned base64 encoded up to maxBytes (truncated is true beyond it). Human control blocks it; the Run's Events record the URL without its query, the status and the byte count. An interrupted request returns unknown and must not be repeated automatically.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.fetch(
    browser_id="browserId",
    url="url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[FetchBrowsersRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**body:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**body_encoding:** `typing.Optional[BrowserFetchRequestBodyEncoding]` 
    
</dd>
</dl>

<dl>
<dd>

**headers:** `typing.Optional[typing.Dict[str, str]]` 
    
</dd>
</dl>

<dl>
<dd>

**max_bytes:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**method:** `typing.Optional[BrowserFetchRequestMethod]` 
    
</dd>
</dl>

<dl>
<dd>

**timeout_ms:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.browsers.<a href="src/bctrl/browsers/client.py">fetch_stream</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send an HTTP request from the browser itself, like fetch, and stream the response body back as it arrives, of any size and with bounded memory at every hop; a slow reader slows the upstream read. The upstream status is in BCTRL-Fetch-Status and its headers (JSON) in BCTRL-Fetch-Headers. A failure before the first byte is an error response; a failure after it aborts the stream, and the Run's completion Event records unknown. Human control blocks it.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.fetch_stream(
    browser_id="browserId",
    url="url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[FetchStreamBrowsersRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**body:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**body_encoding:** `typing.Optional[BrowserFetchStreamRequestBodyEncoding]` 
    
</dd>
</dl>

<dl>
<dd>

**headers:** `typing.Optional[typing.Dict[str, str]]` 
    
</dd>
</dl>

<dl>
<dd>

**method:** `typing.Optional[BrowserFetchStreamRequestMethod]` 
    
</dd>
</dl>

<dl>
<dd>

**timeout_ms:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.browsers.<a href="src/bctrl/browsers/client.py">start</a>(...) -> BrowserResource</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Durably request a new Run of this browser, restoring its saved state. If a previous Run is stopping or saving, startup waits for it. An existing current Run is returned without starting another browser.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.start(
    browser_id="browserId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[StartBrowsersRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**wait:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.browsers.<a href="src/bctrl/browsers/client.py">stop</a>(...) -> BrowserResource</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Request the current Run to stop. State saving continues in the background after the browser exits. Set discardState to erase saved state and skip saving this Run. Use wait to wait for the requested stop.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.stop(
    browser_id="browserId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[StopBrowsersRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**wait:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**discard_state:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## conversations
<details><summary><code>client.conversations.<a href="src/bctrl/conversations/client.py">list</a>(...) -> ConversationListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List durable agent conversations.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment
import datetime

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.conversations.list(
    from_=datetime.datetime.fromisoformat("2026-07-26T12:00:00+00:00"),
    to=datetime.datetime.fromisoformat("2026-07-26T12:00:00+00:00"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListConversationsRequestOrder]` — Order by createdAt and ID. Defaults to desc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[str]` — Filter by a prefixed space ID, or pass `default` to use the caller default space.
    
</dd>
</dl>

<dl>
<dd>

**agent:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[Rfc3339Timestamp]` 
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[Rfc3339Timestamp]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversations.<a href="src/bctrl/conversations/client.py">get</a>(...) -> ConversationRecord</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a runtime-free Conversation record; read its events for history.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.conversations.get(
    conversation_id="conversationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — Unique conversation identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversations.<a href="src/bctrl/conversations/client.py">delete</a>(...) -> ConversationDeleteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an idle Conversation and retire its workspace.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.conversations.delete(
    conversation_id="conversationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — Unique conversation identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversations.<a href="src/bctrl/conversations/client.py">update</a>(...) -> ConversationRecord</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a Conversation title and metadata.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.conversations.update(
    conversation_id="conversationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — Unique conversation identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[JsonObject]` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## events
<details><summary><code>client.events.<a href="src/bctrl/events/client.py">list</a>(...) -> EventListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List immutable Events visible in the organization, subaccount and selected Space: every kind of Event, read in one place. Filter by browser, sandbox, Run, Task, Conversation (its history), agent, category (audit logs are the always-on categories), type, actor, channel, outcome or time.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment
import datetime

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.events.list(
    from_=datetime.datetime.fromisoformat("2026-07-26T12:00:00+00:00"),
    to=datetime.datetime.fromisoformat("2026-07-26T12:00:00+00:00"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser:** `typing.Optional[str]` — Events of this browser, across its Runs.
    
</dd>
</dl>

<dl>
<dd>

**sandbox:** `typing.Optional[str]` — Events of this sandbox.
    
</dd>
</dl>

<dl>
<dd>

**run:** `typing.Optional[str]` — Events of this Run.
    
</dd>
</dl>

<dl>
<dd>

**task:** `typing.Optional[str]` — Events of this Task.
    
</dd>
</dl>

<dl>
<dd>

**conversation:** `typing.Optional[str]` — A Conversation history: its Events.
    
</dd>
</dl>

<dl>
<dd>

**agent:** `typing.Optional[str]` — Events of Tasks run by this agent.
    
</dd>
</dl>

<dl>
<dd>

**category:** `typing.Optional[ListEventsRequestCategory]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**actor:** `typing.Optional[str]` — Actor ID.
    
</dd>
</dl>

<dl>
<dd>

**actor_type:** `typing.Optional[ListEventsRequestActorType]` 
    
</dd>
</dl>

<dl>
<dd>

**channel:** `typing.Optional[ListEventsRequestChannel]` 
    
</dd>
</dl>

<dl>
<dd>

**outcome:** `typing.Optional[ListEventsRequestOutcome]` 
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[Rfc3339Timestamp]` 
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[Rfc3339Timestamp]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListEventsRequestOrder]` — Order by createdAt and ID. Defaults to desc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.events.<a href="src/bctrl/events/client.py">get</a>(...) -> Event</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read one Event by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.events.get(
    event_id="eventId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**event_id:** `str` — Unique runEvent identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.events.<a href="src/bctrl/events/client.py">stream</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stream the same Events as they are committed, with the same filters. Resume after an Event ID with Last-Event-ID or after: the stream is in commit order, so a resumed stream has no gaps.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment
import datetime

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.events.stream(
    from_=datetime.datetime.fromisoformat("2026-07-26T12:00:00+00:00"),
    to=datetime.datetime.fromisoformat("2026-07-26T12:00:00+00:00"),
    after="evt_uAAAAAAAAAAAAAAAAAAAAAA",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser:** `typing.Optional[str]` — Events of this browser, across its Runs.
    
</dd>
</dl>

<dl>
<dd>

**sandbox:** `typing.Optional[str]` — Events of this sandbox.
    
</dd>
</dl>

<dl>
<dd>

**run:** `typing.Optional[str]` — Events of this Run.
    
</dd>
</dl>

<dl>
<dd>

**task:** `typing.Optional[str]` — Events of this Task.
    
</dd>
</dl>

<dl>
<dd>

**conversation:** `typing.Optional[str]` — A Conversation history: its Events.
    
</dd>
</dl>

<dl>
<dd>

**agent:** `typing.Optional[str]` — Events of Tasks run by this agent.
    
</dd>
</dl>

<dl>
<dd>

**category:** `typing.Optional[StreamEventsRequestCategory]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**actor:** `typing.Optional[str]` — Actor ID.
    
</dd>
</dl>

<dl>
<dd>

**actor_type:** `typing.Optional[StreamEventsRequestActorType]` 
    
</dd>
</dl>

<dl>
<dd>

**channel:** `typing.Optional[StreamEventsRequestChannel]` 
    
</dd>
</dl>

<dl>
<dd>

**outcome:** `typing.Optional[StreamEventsRequestOutcome]` 
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[Rfc3339Timestamp]` 
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[Rfc3339Timestamp]` 
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Resume after this Event ID (as Last-Event-ID does).
    
</dd>
</dl>

<dl>
<dd>

**last_event_id:** `typing.Optional[str]` — Optional last delivered event identifier used to resume an SSE stream.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## files
<details><summary><code>client.files.<a href="src/bctrl/files/client.py">list</a>(...) -> FileListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the canonical durable File resource. Runtime file endpoints operate on a live machine disk: collect turns a machine file into a durable File, while stage performs the reverse. Use source, type, runId, runtimeId, path, prefix, and createdAfter filters here.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment
import datetime

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.files.list(
    created_after=datetime.datetime.fromisoformat("2026-07-26T12:00:00+00:00"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**space_id:** `typing.Optional[str]` — Filter by a prefixed space ID, or pass `default` to use the caller default space.
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[ListFilesRequestSource]` 
    
</dd>
</dl>

<dl>
<dd>

**path:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**prefix:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**run_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**runtime_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by one or more file artifact types. Repeat the query parameter for multiple values.
    
</dd>
</dl>

<dl>
<dd>

**created_after:** `typing.Optional[Rfc3339Timestamp]` 
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[ListFilesRequestInclude]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListFilesRequestOrder]` — Order by createdAt and ID. Defaults to desc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/bctrl/files/client.py">upload</a>(...) -> File</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload a file into a space and return the canonical file resource.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.files.upload(
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file:** `core.File` — File bytes to upload.
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[str]` — Filter by a prefixed space ID, or pass `default` to use the caller default space.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**filename:** `typing.Optional[str]` — Optional display filename.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[str]` — Optional JSON object string with caller-owned file metadata.
    
</dd>
</dl>

<dl>
<dd>

**path:** `typing.Optional[str]` — Optional relative destination path. Must not be absolute or contain . or .. path segments.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/bctrl/files/client.py">get</a>(...) -> File</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get one file metadata record using the canonical file resource.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.files.get(
    file_id="fileId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `str` — Unique file identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**run_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/bctrl/files/client.py">delete</a>(...) -> FileDeleteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete one uploaded or collected file.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.files.delete(
    file_id="fileId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `str` — Unique file identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/bctrl/files/client.py">update</a>(...) -> File</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update one file display name or caller-owned metadata.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.files.update(
    file_id="fileId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `str` — Unique file identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**filename:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[JsonObject]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/bctrl/files/client.py">content</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Download the bytes for one file.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.files.content(
    file_id="fileId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `str` — Unique file identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**run_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## locations
<details><summary><code>client.locations.<a href="src/bctrl/locations/client.py">list</a>(...) -> LocationsListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List deployed compute locations and current admission availability. Runtime location auto resolves to an allowed live location; homeRegions identifies compatible data homes. Catalog entries are ordered by their immutable ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.locations.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListLocationsRequestOrder]` — Order by createdAt and ID. Defaults to desc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## NotificationRecipients
<details><summary><code>client.notification_recipients.<a href="src/bctrl/notification_recipients/client.py">list</a>(...) -> NotificationRecipientsListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List notification receivers used for input requests. Use BCTRL-Subaccount-Id to scope the request to a subaccount.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.notification_recipients.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListNotificationRecipientsRequestOrder]` — Order by createdAt and ID. Defaults to desc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[ListNotificationRecipientsRequestType]` 
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notification_recipients.<a href="src/bctrl/notification_recipients/client.py">create</a>(...) -> NotificationRecipient</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a notification receiver. Use BCTRL-Subaccount-Id to create it for a subaccount. Supported receiver types are email, SMS, and WhatsApp.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.notification_recipients.create(
    type="email",
    value="value",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `NotificationRecipientCreateRequestType` 
    
</dd>
</dl>

<dl>
<dd>

**value:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[ResourceName]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notification_recipients.<a href="src/bctrl/notification_recipients/client.py">delete</a>(...) -> NotificationRecipientDeleteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete one notification receiver. Historical delivery records are kept.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.notification_recipients.delete(
    recipient_id="recipientId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**recipient_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notification_recipients.<a href="src/bctrl/notification_recipients/client.py">update</a>(...) -> NotificationRecipient</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update one notification receiver value, label, or enabled state.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.notification_recipients.update(
    recipient_id="recipientId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**recipient_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[ResourceName]` 
    
</dd>
</dl>

<dl>
<dd>

**value:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## proxies
<details><summary><code>client.proxies.<a href="src/bctrl/proxies/client.py">list</a>(...) -> ProxyListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List saved proxies using the simplified response envelope.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.proxies.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListProxiesRequestOrder]` — Order by createdAt and ID. Defaults to desc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.proxies.<a href="src/bctrl/proxies/client.py">create</a>(...) -> Proxy</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a saved proxy configuration for browser runtimes.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl, ProxyCreateRequest_Custom
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.proxies.create(
    request=ProxyCreateRequest_Custom(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `ProxyCreateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.proxies.<a href="src/bctrl/proxies/client.py">get</a>(...) -> Proxy</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get one saved proxy using the simplified proxy resource shape.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.proxies.get(
    proxy_id="proxyId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**proxy_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.proxies.<a href="src/bctrl/proxies/client.py">delete</a>(...) -> ProxyDeleteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a saved proxy that should no longer be used.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.proxies.delete(
    proxy_id="proxyId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**proxy_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.proxies.<a href="src/bctrl/proxies/client.py">update</a>(...) -> Proxy</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update one saved proxy. Future browser runtimes can use the updated proxy configuration.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.proxies.update(
    proxy_id="proxyId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**proxy_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**auto_renew:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**city:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**device:** `typing.Optional[ProxyUpdateRequestDevice]` 
    
</dd>
</dl>

<dl>
<dd>

**dns_resolution:** `typing.Optional[ProxyUpdateRequestDnsResolution]` 
    
</dd>
</dl>

<dl>
<dd>

**geo_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**host:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**ip_family:** `typing.Optional[ProxyUpdateRequestIpFamily]` 
    
</dd>
</dl>

<dl>
<dd>

**isp:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[ResourceName]` 
    
</dd>
</dl>

<dl>
<dd>

**password:** `typing.Optional[str]` — The proxy password, or a secret reference such as `secret:proxies/office#password`.
    
</dd>
</dl>

<dl>
<dd>

**pool:** `typing.Optional[ProxyLocationPool]` 
    
</dd>
</dl>

<dl>
<dd>

**port:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**preference:** `typing.Optional[ProxyUpdateRequestPreference]` 
    
</dd>
</dl>

<dl>
<dd>

**protocol:** `typing.Optional[ProxyUpdateRequestProtocol]` 
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**rotation:** `typing.Optional[ProxyUpdateRequestRotation]` 
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sticky_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**udp_mode:** `typing.Optional[ProxyUpdateRequestUdpMode]` 
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**username:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.proxies.<a href="src/bctrl/proxies/client.py">test</a>(...) -> ProxyTestResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Test a saved proxy configuration before using it with browser runtimes.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.proxies.test(
    proxy_id="proxyId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**proxy_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## runs
<details><summary><code>client.runs.<a href="src/bctrl/runs/client.py">list</a>(...) -> RunListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List runs across visible runtime work using the simplified run resource.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment
import datetime

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.runs.list(
    from_=datetime.datetime.fromisoformat("2026-07-26T12:00:00+00:00"),
    to=datetime.datetime.fromisoformat("2026-07-26T12:00:00+00:00"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListRunsRequestOrder]` — Order by createdAt and ID. Defaults to desc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[ListRunsRequestStatusItem, typing.Sequence[ListRunsRequestStatusItem]]]` — Filter by one or more run statuses. Repeat the query parameter for multiple values.
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**resource_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**resource_type:** `typing.Optional[ListRunsRequestResourceType]` 
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[Rfc3339Timestamp]` 
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[Rfc3339Timestamp]` 
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[ListRunsRequestInclude]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.runs.<a href="src/bctrl/runs/client.py">get</a>(...) -> Run</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get one run using the simplified run resource.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.runs.get(
    run_id="runId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` — Unique run identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[GetRunsRequestInclude]` 
    
</dd>
</dl>

<dl>
<dd>

**wait:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.runs.<a href="src/bctrl/runs/client.py">delete</a>(...) -> RunsDeleteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Purge the artifacts of an ended Run while retaining its lifecycle and usage record. Active Runs must be stopped and their native execution retired before purging.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.runs.delete(
    run_id="runId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` — Unique run identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.runs.<a href="src/bctrl/runs/client.py">stream</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stream ordered trace and runtime events for a run.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.runs.stream(
    run_id="runId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` — Unique run identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[StreamRunsRequestInclude]` 
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**last_event_id:** `typing.Optional[str]` — Optional last delivered event identifier used to resume an SSE stream.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## sandboxes
<details><summary><code>client.sandboxes.<a href="src/bctrl/sandboxes/client.py">list</a>(...) -> SandboxesListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List sandboxes visible to the caller.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.sandboxes.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**space_id:** `typing.Optional[str]` — Filter by a prefixed space ID, or pass `default` to use the caller default space.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListSandboxesRequestOrder]` — Order by createdAt and ID. Defaults to desc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.<a href="src/bctrl/sandboxes/client.py">create</a>(...) -> Sandbox</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a sandbox from an approved image. Returns while it is provisioning.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.sandboxes.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**from_snapshot:** `typing.Optional[str]` — Start as a fork of this snapshot (memory and disk), on the node that holds it. The image comes from the snapshot.
    
</dd>
</dl>

<dl>
<dd>

**image:** `typing.Optional[str]` — An approved image identifier such as `bctrl-pi-stable`, or any OCI image reference such as `python:3.12` or `ghcr.io/acme/tools@sha256:…`.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[ResourceName]` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[str]` — Opaque resource ID or unique resource name in the selected Space or tenant.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.<a href="src/bctrl/sandboxes/client.py">get</a>(...) -> Sandbox</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get one sandbox with its status and qualified capabilities.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.sandboxes.get(
    sandbox_id="sandboxId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.<a href="src/bctrl/sandboxes/client.py">delete</a>(...) -> SandboxDeleteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently delete a sandbox that is not bound to a conversation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.sandboxes.delete(
    sandbox_id="sandboxId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.<a href="src/bctrl/sandboxes/client.py">start</a>(...) -> Sandbox</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Ensure a sandbox has running compute, keeping its disk.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.sandboxes.start(
    sandbox_id="sandboxId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.<a href="src/bctrl/sandboxes/client.py">stop</a>(...) -> Sandbox</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stop sandbox compute. Active processes are a conflict unless force is set. The disk stays on the host while stopped and is not replicated: if that host is lost, the sandbox fails with `environment.host_lost` and its files may be lost.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.sandboxes.stop(
    sandbox_id="sandboxId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**force:** `typing.Optional[bool]` — Cancel active executions before stopping. Without it, active work is a conflict.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## secrets
<details><summary><code>client.secrets.<a href="src/bctrl/secrets/client.py">list</a>(...) -> SecretList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Secrets by path. `prefix` narrows to paths starting with it; `delimiter=/` groups deeper paths into `folders`, like S3. Secret values are never listed.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.secrets.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**prefix:** `typing.Optional[str]` — Only paths starting with this prefix.
    
</dd>
</dl>

<dl>
<dd>

**delimiter:** `typing.Optional[ListSecretsRequestDelimiter]` — Group paths below the next `/` after the prefix into `folders`.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[ListSecretsRequestType]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListSecretsRequestOrder]` — Order by createdAt and ID. Defaults to desc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.secrets.<a href="src/bctrl/secrets/client.py">create</a>(...) -> Secret</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a Secret at a new path. The returned ID addresses it; paths remain reference keys.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.secrets.create(
    path="path",
    type="login",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**path:** `str` — Secret path, for example `prod/github/bot`. May contain `/`.
    
</dd>
</dl>

<dl>
<dd>

**type:** `SecretCreateRequestType` — `login`: username, password and TOTP seed for a site. `value`: one opaque value.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**label:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — Free-form notes. Write-only.
    
</dd>
</dl>

<dl>
<dd>

**origins:** `typing.Optional[typing.List[str]]` — Origins a `login` may be filled into: `https://host[:port]`, or `https://*.host` for any subdomain.
    
</dd>
</dl>

<dl>
<dd>

**password:** `typing.Optional[str]` — Password of a `login`. Write-only.
    
</dd>
</dl>

<dl>
<dd>

**totp:** `typing.Optional[str]` — TOTP seed (base32) of a `login`. Write-only.
    
</dd>
</dl>

<dl>
<dd>

**username:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**value:** `typing.Optional[str]` — The value of a `value` secret. Write-only.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.secrets.<a href="src/bctrl/secrets/client.py">get</a>(...) -> Secret</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read one Secret: its metadata and which fields are set. Secret fields are write-only; use `POST /v1/secrets/{secret}/reveal` to read values.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.secrets.get(
    secret="secret",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**secret:** `str` — Unique secret identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.secrets.<a href="src/bctrl/secrets/client.py">delete</a>(...) -> SecretDeleteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a Secret and all its versions. Supports `If-Match`. The audit trail is kept.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.secrets.delete(
    secret="secret",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**secret:** `str` — Unique secret identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**if_match:** `typing.Optional[str]` — Apply the write only if the current version (the ETag) is this one, for example `"3"`. Returns 412 otherwise.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.secrets.<a href="src/bctrl/secrets/client.py">update</a>(...) -> Secret</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Change some fields of a Secret; `null` clears one. Creates a new version. Supports `If-Match`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.secrets.update(
    secret="secret",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**secret:** `str` — Unique secret identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**if_match:** `typing.Optional[str]` — Apply the write only if the current version (the ETag) is this one, for example `"3"`. Returns 412 otherwise.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**from_version:** `typing.Optional[int]` — Restore values of this version; send alone.
    
</dd>
</dl>

<dl>
<dd>

**label:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — Free-form notes. Write-only.
    
</dd>
</dl>

<dl>
<dd>

**origins:** `typing.Optional[typing.List[str]]` — Origins a `login` may be filled into: `https://host[:port]`, or `https://*.host` for any subdomain.
    
</dd>
</dl>

<dl>
<dd>

**password:** `typing.Optional[str]` — Password of a `login`. Write-only.
    
</dd>
</dl>

<dl>
<dd>

**totp:** `typing.Optional[str]` — TOTP seed (base32) of a `login`. Write-only.
    
</dd>
</dl>

<dl>
<dd>

**username:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**value:** `typing.Optional[str]` — The value of a `value` secret. Write-only.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.secrets.<a href="src/bctrl/secrets/client.py">reveal</a>(...) -> SecretRevealResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the values of a Secret version. Only people may reveal: organization or subaccount API keys and dashboard sessions. Task agents, delegated code and View tokens get 403 `secrets.reveal_forbidden`. Every reveal is audited.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.secrets.reveal(
    secret="secret",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**secret:** `str` — Unique secret identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` — Defaults to the current version.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.secrets.<a href="src/bctrl/secrets/client.py">versions</a>(...) -> SecretVersionList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List version metadata by secret ID. Values and ciphertext are never returned.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.secrets.versions(
    secret="secret",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**secret:** `str` — Unique secret identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[VersionsSecretsRequestOrder]` — Order by createdAt and ID. Defaults to desc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## spaces
<details><summary><code>client.spaces.<a href="src/bctrl/spaces/client.py">list</a>(...) -> SpaceListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List complete spaces visible to the current API key.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.spaces.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListSpacesRequestOrder]` — Order by createdAt and ID. Defaults to desc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.spaces.<a href="src/bctrl/spaces/client.py">create</a>(...) -> Space</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a space. Name, region, and environment are optional; omitted values use server defaults.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.spaces.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**capability_scopes:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**environment:** `typing.Optional[EnvironmentMounts]` 
    
</dd>
</dl>

<dl>
<dd>

**expire_after_idle_days:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[ResourceName]` 
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[SpaceCreateRequestRegion]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.spaces.<a href="src/bctrl/spaces/client.py">get</a>(...) -> Space</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get one complete space, including its environment.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.spaces.get(
    space_id="spaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**space_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.spaces.<a href="src/bctrl/spaces/client.py">delete</a>(...) -> Space</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a Space and everything in it: its browsers and sandboxes are stopped and destroyed, and its agents, Tasks, Conversations, files and views deleted. Run records, usage and Events stay with the organization. The deletion runs in the background; the Space shows status deleting until it is gone. Pass wait to block until then.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.spaces.delete(
    space_id="spaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**space_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**wait:** `typing.Optional[int]` — Seconds to wait for the deletion to finish before answering.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.spaces.<a href="src/bctrl/spaces/client.py">update</a>(...) -> Space</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a space name or environment.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.spaces.update(
    space_id="spaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**space_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**capability_scopes:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**environment:** `typing.Optional[SpaceEnvironmentPatch]` 
    
</dd>
</dl>

<dl>
<dd>

**expire_after_idle_days:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[ResourceName]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Subaccounts
<details><summary><code>client.subaccounts.<a href="src/bctrl/subaccounts/client.py">list</a>(...) -> SubaccountListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List subaccounts using the simplified response envelope. Pass include=usage to inline current usage.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.subaccounts.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListSubaccountsRequestOrder]` — Order by createdAt and ID. Defaults to desc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[ListSubaccountsRequestIncludeItem, typing.Sequence[ListSubaccountsRequestIncludeItem]]]` — Include optional subaccount expansions. Repeat the query parameter for multiple values.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListSubaccountsRequestStatus]` — Filter subaccounts by lifecycle status.
    
</dd>
</dl>

<dl>
<dd>

**external_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subaccounts.<a href="src/bctrl/subaccounts/client.py">create</a>(...) -> Subaccount</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a subaccount for a tenant, customer, environment, or team. Optional limits can be provided inline.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.subaccounts.create(
    name="Production browser",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `ResourceName` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**external_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**limits:** `typing.Optional[SubaccountLimitsUpdateRequest]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[JsonObject]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subaccounts.<a href="src/bctrl/subaccounts/client.py">get</a>(...) -> Subaccount</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get one subaccount. Pass include=usage to inline current usage and quota state.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.subaccounts.get(
    subaccount_id="V1StGXR8_Z5jdHi6B-myT",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subaccount_id:** `GetSubaccountsRequestSubaccountId` 
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[GetSubaccountsRequestIncludeItem, typing.Sequence[GetSubaccountsRequestIncludeItem]]]` — Include optional subaccount expansions. Repeat the query parameter for multiple values.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subaccounts.<a href="src/bctrl/subaccounts/client.py">update</a>(...) -> Subaccount</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update one subaccount name, external identifier, metadata, or configured limits.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.subaccounts.update(
    subaccount_id="V1StGXR8_Z5jdHi6B-myT",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subaccount_id:** `UpdateSubaccountsRequestSubaccountId` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**external_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**limits:** `typing.Optional[SubaccountLimitsUpdateRequest]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[JsonObject]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[ResourceName]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subaccounts.<a href="src/bctrl/subaccounts/client.py">archive</a>(...) -> SubaccountArchiveResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Archive a subaccount so it can no longer be used for new work.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.subaccounts.archive(
    subaccount_id="V1StGXR8_Z5jdHi6B-myT",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subaccount_id:** `ArchiveSubaccountsRequestSubaccountId` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## tasks
<details><summary><code>client.tasks.<a href="src/bctrl/tasks/client.py">list</a>(...) -> TasksListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Tasks by Agent, Conversation, status and time in the selected tenant or Space.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment
import datetime

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.tasks.list(
    from_=datetime.datetime.fromisoformat("2026-07-26T12:00:00+00:00"),
    to=datetime.datetime.fromisoformat("2026-07-26T12:00:00+00:00"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListTasksRequestOrder]` — Order by createdAt and ID. Defaults to desc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**agent:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**conversation:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListTasksRequestStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[Rfc3339Timestamp]` 
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[Rfc3339Timestamp]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tasks.<a href="src/bctrl/tasks/client.py">create</a>(...) -> Task</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Run an Agent on the input in a new or existing idle Conversation. The Task starts queued; read or wait on it with GET /v1/tasks/{taskId}.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.tasks.create(
    agent="agent",
    input="input",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent:** `str` — Opaque resource ID or unique resource name in the selected Space or tenant.
    
</dd>
</dl>

<dl>
<dd>

**input:** `TaskInput` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**conversation:** `typing.Optional[str]` — Unique conversation identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[JsonObject]` 
    
</dd>
</dl>

<dl>
<dd>

**output_schema:** `typing.Optional[JsonObject]` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[str]` — Opaque resource ID or unique resource name in the selected Space or tenant.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tasks.<a href="src/bctrl/tasks/client.py">get</a>(...) -> Task</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read Task status, structured output, artifacts, input request, Browser Runs and usage. Wait ends when the Task finishes or requests input.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.tasks.get(
    task_id="taskId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `str` — Unique task identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**wait:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tasks.<a href="src/bctrl/tasks/client.py">cancel</a>(...) -> Task</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel the Task and revoke its delegated credential. Its Conversation remains busy until native cleanup is acknowledged.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.tasks.cancel(
    task_id="taskId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `str` — Unique task identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tasks.<a href="src/bctrl/tasks/client.py">input</a>(...) -> Task</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Answer its current input request by requestId, or steer a running Task. Approval applies only its immutable stored proposal.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.tasks.input(
    task_id="taskId",
    input={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `str` — Unique task identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**input:** `JsonValue` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ToolCalls
<details><summary><code>client.tool_calls.<a href="src/bctrl/tool_calls/client.py">list</a>(...) -> ToolCallListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List durable tool execution lifecycle and audit records.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.tool_calls.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**runtime_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**run_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**task_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**tool:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListToolCallsRequestStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListToolCallsRequestOrder]` — Order by createdAt and ID. Defaults to desc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[str]` — Filter by a prefixed space ID, or pass `default` to use the caller default space.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tool_calls.<a href="src/bctrl/tool_calls/client.py">get</a>(...) -> ToolCall</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get one tool call audit record by the same tool call id that appears in webhook payloads and run events.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.tool_calls.get(
    tool_call_id="toolCallId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tool_call_id:** `str` — Unique toolCall identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**wait:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tool_calls.<a href="src/bctrl/tool_calls/client.py">cancel</a>(...) -> ToolCall</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel one active cancellable tool call.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.tool_calls.cancel(
    tool_call_id="toolCallId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tool_call_id:** `str` — Unique toolCall identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tool_calls.<a href="src/bctrl/tool_calls/client.py">respond</a>(...) -> ToolCall</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provide bounded input requested by a suspended tool call.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.tool_calls.respond(
    tool_call_id="toolCallId",
    request={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tool_call_id:** `str` — Unique toolCall identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**request:** `JsonValue` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tool_calls.<a href="src/bctrl/tool_calls/client.py">result</a>(...) -> JsonValue</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the result for an authorized tool call; a pending call returns its current state so callers can poll again.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.tool_calls.result(
    tool_call_id="toolCallId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tool_call_id:** `str` — Unique toolCall identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**wait:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## tools
<details><summary><code>client.tools.<a href="src/bctrl/tools/client.py">list</a>(...) -> ToolListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List built-in and custom tools available in a space.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.tools.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**space_id:** `typing.Optional[str]` — Filter by a prefixed space ID, or pass `default` to use the caller default space.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListToolsRequestOrder]` — Order by createdAt and ID. Defaults to desc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/bctrl/tools/client.py">create</a>(...) -> Tool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an organization custom callable tool. Agents select these tools in their immutable version definitions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl, ToolCreateRequestZero, ToolCreateRequestZeroImplementation
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.tools.create(
    request=ToolCreateRequestZero(
        implementation=ToolCreateRequestZeroImplementation(
            type="webhook",
            url="url",
        ),
        input_schema={},
        name="name",
        output_schema={},
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `ToolCreateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/bctrl/tools/client.py">get</a>(...) -> Tool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get one custom tool definition, including its schemas, execution method, status, and metadata.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.tools.get(
    tool_ref="toolRef",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tool_ref:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/bctrl/tools/client.py">delete</a>(...) -> ToolDeleteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an organization custom tool. This removes the definition, not historical tool call records.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.tools.delete(
    tool_ref="toolRef",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tool_ref:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/bctrl/tools/client.py">update</a>(...) -> Tool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a custom tool definition. Changes apply to future tool use while existing tool call records remain available.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.tools.update(
    tool_ref="toolRef",
    current_revision_id="currentRevisionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tool_ref:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**current_revision_id:** `str` — Unique toolRevision identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**implementation:** `typing.Optional[ToolUpdateRequestImplementation]` 
    
</dd>
</dl>

<dl>
<dd>

**input_schema:** `typing.Optional[JsonObject]` 
    
</dd>
</dl>

<dl>
<dd>

**output_schema:** `typing.Optional[JsonObject]` 
    
</dd>
</dl>

<dl>
<dd>

**runtime_types:** `typing.Optional[typing.List[ToolUpdateRequestRuntimeTypesItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Usage
<details><summary><code>client.usage.<a href="src/bctrl/usage/client.py">get</a>() -> AccountUsage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get current organization credit usage and balance.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.usage.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## views
<details><summary><code>client.views.<a href="src/bctrl/views/client.py">list</a>(...) -> ViewsListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List active view resources visible to the current API-key actor.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.views.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListViewsRequestOrder]` — Order by createdAt and ID. Defaults to desc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.views.<a href="src/bctrl/views/client.py">create</a>(...) -> ViewCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Mint a scoped, component-gated hosted page or origin-restricted iframe composition. The response contains the bearer token once; keep it private.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl, ViewScopeSpaceInput
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.views.create(
    scope=ViewScopeSpaceInput(
        space_id="spaceId",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scope:** `ViewScopeInput` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**components:** `typing.Optional[ViewComponentsInput]` — Optional content and notification surfaces for the View.
    
</dd>
</dl>

<dl>
<dd>

**control:** `typing.Optional[bool]` — Allow live browser interaction and actions from the notification center.
    
</dd>
</dl>

<dl>
<dd>

**conversation_send:** `typing.Optional[bool]` — Allow giving input to and cancelling Tasks in the included conversations. Defaults to the value of control.
    
</dd>
</dl>

<dl>
<dd>

**expires_in_seconds:** `typing.Optional[int]` — View lifetime in seconds. Defaults to 8 hours; maximum 30 days.
    
</dd>
</dl>

<dl>
<dd>

**presentation:** `typing.Optional[ViewPresentation]` — Hosted presentation by default; use embedded with explicit allowed origins.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.views.<a href="src/bctrl/views/client.py">get</a>(...) -> ViewBootstrap</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read a view resource. Bearer view tokens may read only their own resource.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.views.get(
    view_id="viewId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**view_id:** `str` — Public view resource id. It is safe to expose in URLs and logs.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.views.<a href="src/bctrl/views/client.py">delete</a>(...) -> ViewDeleteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revoke a view and immediately invalidate its bearer token.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.views.delete(
    view_id="viewId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**view_id:** `str` — Public view resource id. It is safe to expose in URLs and logs.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## webhooks
<details><summary><code>client.webhooks.<a href="src/bctrl/webhooks/client.py">list</a>(...) -> WebhooksListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List webhook endpoints visible to the current organization or subaccount scope.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.webhooks.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListWebhooksRequestOrder]` — Order by createdAt and ID. Defaults to desc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/bctrl/webhooks/client.py">create</a>(...) -> WebhookCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a signed webhook endpoint. The signing secret is returned once; store it securely and verify every delivery signature.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.webhooks.create(
    events=[
        "events"
    ],
    url="url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**events:** `typing.List[str]` 
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[ResourceName]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/bctrl/webhooks/client.py">get</a>(...) -> Webhook</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get one webhook endpoint without exposing its signing secret.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.webhooks.get(
    webhook_id="webhookId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**webhook_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/bctrl/webhooks/client.py">delete</a>(...) -> WebhookDeleteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a webhook endpoint. Historical delivery records remain in the audit ledger.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.webhooks.delete(
    webhook_id="webhookId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**webhook_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/bctrl/webhooks/client.py">update</a>(...) -> Webhook</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a webhook destination, event subscriptions, label, or enabled state.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.webhooks.update(
    webhook_id="webhookId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**webhook_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**events:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[ResourceName]` 
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/bctrl/webhooks/client.py">rotate_secret</a>(...) -> WebhookRotateSecretResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replace a webhook signing secret immediately. The new secret is returned once.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.webhooks.rotate_secret(
    webhook_id="webhookId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**webhook_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/bctrl/webhooks/client.py">test</a>(...) -> WebhookDelivery</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Queue a signed test event for a webhook endpoint and return its delivery record.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.webhooks.test(
    webhook_id="webhookId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**webhook_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Account SpendingCap
<details><summary><code>client.account.spending_cap.<a href="src/bctrl/account/spending_cap/client.py">get</a>() -> SpendingCap</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read the current UTC calendar-month limit and accrued usage in USD cents. Warning occurs once per month at 80%; at 100%, new billable starts are refused and running work is stopped within at most one minute of additional usage.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.account.spending_cap.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.account.spending_cap.<a href="src/bctrl/account/spending_cap/client.py">update</a>(...) -> SpendingCap</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

People may set a whole-cent USD limit; null disables it and zero refuses new billable starts. Raising the limit permits starts once it exceeds current usage. The UTC calendar month resets usage; raising or disabling a cap does not reset its warning marker.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.account.spending_cap.update(
    currency="USD",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `SpendingCapPatchRequest` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agents A2A
<details><summary><code>client.agents.a2a.<a href="src/bctrl/agents/a2a/client.py">rpc</a>(...) -> A2AJsonRpcResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A2A v1.0 JSON-RPC: SendMessage starts or continues a Task (blocking unless configuration.returnImmediately), GetTask, ListTasks and CancelTask read and cancel this Agent’s Tasks. Send the A2A-Version: 1.0 header. Errors are JSON-RPC errors with HTTP 200.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.agents.a2a.rpc(
    agent_id="agentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**jsonrpc:** `typing.Optional[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**method:** `typing.Optional[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**params:** `typing.Optional[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.a2a.<a href="src/bctrl/agents/a2a/client.py">card</a>(...) -> A2AAgentCard</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The Agent2Agent (A2A v1.0) card of this Agent: its JSON-RPC interface, capabilities and bearer API-key security.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.agents.a2a.card(
    agent_id="agentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agents Versions
<details><summary><code>client.agents.versions.<a href="src/bctrl/agents/versions/client.py">list</a>(...) -> AgentsVersionsListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List immutable versions of an Agent in creation order.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.agents.versions.list(
    agent_id="agentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListVersionsRequestOrder]` — Order by createdAt and ID. Defaults to desc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.versions.<a href="src/bctrl/agents/versions/client.py">get</a>(...) -> AgentVersion</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read the immutable definition of one numbered Agent version.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.agents.versions.get(
    agent_id="agentId",
    version=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.versions.<a href="src/bctrl/agents/versions/client.py">promote</a>(...) -> Agent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Select an immutable version for future Tasks. When approval is required, a person must promote it or answer the stored Task approval request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.agents.versions.promote(
    agent_id="agentId",
    version=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Ai Credentials
<details><summary><code>client.ai.credentials.<a href="src/bctrl/ai/credentials/client.py">list</a>(...) -> AiCredentialListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List saved BYOK AI credentials. Use credentials only when a model selection should run against a customer-owned provider key.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.ai.credentials.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**provider:** `typing.Optional[ListCredentialsRequestProvider]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListCredentialsRequestStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListCredentialsRequestOrder]` — Order by createdAt and ID. Defaults to desc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ai.credentials.<a href="src/bctrl/ai/credentials/client.py">create</a>(...) -> AiCredential</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a saved BYOK AI credential. Name is optional and defaults server-side; pass test=true to verify credentials before saving.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.ai.credentials.create(
    provider="openai",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**provider:** `AiCredentialCreateRequestProvider` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**api_key:** `typing.Optional[str]` — The provider API key, or a secret reference such as `secret:ai/openai#value`.
    
</dd>
</dl>

<dl>
<dd>

**base_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**default_model:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[ResourceName]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[AiCredentialCreateRequestStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**test:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ai.credentials.<a href="src/bctrl/ai/credentials/client.py">get</a>(...) -> AiCredential</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get one saved BYOK AI credential.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.ai.credentials.get(
    credential_id="credentialId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**credential_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ai.credentials.<a href="src/bctrl/ai/credentials/client.py">delete</a>(...) -> AiCredentialDeleteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a saved AI credential that should no longer be used.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.ai.credentials.delete(
    credential_id="credentialId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**credential_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ai.credentials.<a href="src/bctrl/ai/credentials/client.py">update</a>(...) -> AiCredential</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an AI credential label, stored key, default model, custom endpoint, or enabled state.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.ai.credentials.update(
    credential_id="credentialId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**credential_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**api_key:** `typing.Optional[str]` — The provider API key, or a secret reference such as `secret:ai/openai#value`.
    
</dd>
</dl>

<dl>
<dd>

**base_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**default_model:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[ResourceName]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[AiCredentialUpdateRequestStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ai.credentials.<a href="src/bctrl/ai/credentials/client.py">test</a>(...) -> AiCredentialTestResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Test a saved AI credential before using it in hosted work.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.ai.credentials.test(
    credential_id="credentialId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**credential_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Ai Models
<details><summary><code>client.ai.models.<a href="src/bctrl/ai/models/client.py">list</a>(...) -> AiModelListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List curated AI models available for hosted execution, including managed availability and capability metadata.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.ai.models.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**provider:** `typing.Optional[ListModelsRequestProvider]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListModelsRequestStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**managed:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListModelsRequestOrder]` — Order by createdAt and ID. Defaults to desc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Browser Extensions
<details><summary><code>client.browser.extensions.<a href="src/bctrl/browser/extensions/client.py">list</a>(...) -> BrowserExtensionListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List managed browser extensions using the simplified response envelope.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browser.extensions.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListExtensionsRequestOrder]` — Order by createdAt and ID. Defaults to desc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[ListExtensionsRequestFormat]` 
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[ListExtensionsRequestSource]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.browser.extensions.<a href="src/bctrl/browser/extensions/client.py">create</a>(...) -> BrowserExtension</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a browser extension from an uploaded package or Chrome Web Store URL.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browser.extensions.create(
    url="url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.browser.extensions.<a href="src/bctrl/browser/extensions/client.py">get</a>(...) -> BrowserExtension</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get one managed browser extension using the simplified browser extension resource.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browser.extensions.get(
    extension_id="extensionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**extension_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.browser.extensions.<a href="src/bctrl/browser/extensions/client.py">delete</a>(...) -> BrowserExtensionDeleteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a managed browser extension that should no longer be used by browser runtimes.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browser.extensions.delete(
    extension_id="extensionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**extension_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.browser.extensions.<a href="src/bctrl/browser/extensions/client.py">update</a>(...) -> BrowserExtension</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update customer-controlled browser extension metadata such as the display name.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browser.extensions.update(
    extension_id="extensionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**extension_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[ResourceName]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Browsers Computer
<details><summary><code>client.browsers.computer.<a href="src/bctrl/browsers/computer/client.py">batch</a>(...) -> ComputerBatchResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Execute up to twenty desktop actions in order on one current Browser Run. Every action is validated before acceptance. Execution stops at the first uncertain result and returns unknown with null data; earlier actions may have taken effect. Reusing the same Idempotency-Key replays the terminal result without repeating the batch.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl, ComputerActionRequest_Screenshot
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.computer.batch(
    browser_id="browserId",
    actions=[
        ComputerActionRequest_Screenshot()
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**actions:** `typing.List[ComputerActionRequest]` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[BatchComputerRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.browsers.computer.<a href="src/bctrl/browsers/computer/client.py">click</a>(...) -> ComputerResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Click the current Browser Run at screenshot-pixel coordinates, or at the cursor when omitted. Button defaults to left; two or three clicks require the left button. An interrupted action returns unknown and must not be repeated automatically.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.computer.click(
    browser_id="browserId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[ClickComputerRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**button:** `typing.Optional[BrowsersComputerClickRequestButton]` 
    
</dd>
</dl>

<dl>
<dd>

**click_count:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**coordinate:** `typing.Optional[typing.List[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**modifiers:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.browsers.computer.<a href="src/bctrl/browsers/computer/client.py">cursor</a>(...) -> ComputerResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read the cursor position and desktop dimensions of the current Browser Run. The result carries its canonical Event ID. Human control blocks automation; interrupted execution returns unknown.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.computer.cursor(
    browser_id="browserId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[CursorComputerRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.browsers.computer.<a href="src/bctrl/browsers/computer/client.py">double_click</a>(...) -> ComputerResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Double-click the left mouse button in the current Browser Run. Coordinates use screenshot pixels; omission uses the current cursor. An interrupted action returns unknown with its accepted Event ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.computer.double_click(
    browser_id="browserId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[DoubleClickComputerRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**coordinate:** `typing.Optional[typing.List[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**modifiers:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.browsers.computer.<a href="src/bctrl/browsers/computer/client.py">drag</a>(...) -> ComputerResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Drag the left mouse button in the current Browser Run to the requested coordinates, with an optional starting position and bounded path. Human control blocks automation. An interrupted action returns unknown.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.computer.drag(
    browser_id="browserId",
    coordinate=[],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**coordinate:** `typing.List[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[DragComputerRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**modifiers:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**path:** `typing.Optional[typing.List[typing.List[typing.Any]]]` 
    
</dd>
</dl>

<dl>
<dd>

**start_coordinate:** `typing.Optional[typing.List[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.browsers.computer.<a href="src/bctrl/browsers/computer/client.py">key</a>(...) -> ComputerResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send one bounded key chord to the current Browser Run, with an optional repeat count. Human control blocks automation. An interrupted action returns unknown with its accepted Event ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.computer.key(
    browser_id="browserId",
    keys="keys",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**keys:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[KeyComputerRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**repeat:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.browsers.computer.<a href="src/bctrl/browsers/computer/client.py">move</a>(...) -> ComputerResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Move the cursor in the current Browser Run to screenshot-pixel coordinates. Human control blocks automation. An interrupted action returns unknown with its accepted Event ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.computer.move(
    browser_id="browserId",
    coordinate=[],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**coordinate:** `typing.List[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[MoveComputerRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.browsers.computer.<a href="src/bctrl/browsers/computer/client.py">screenshot</a>(...) -> ComputerResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Capture the headed desktop of the current Browser Run as a JPEG. The result carries its canonical Event ID. An interrupted capture returns unknown with null data.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.computer.screenshot(
    browser_id="browserId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[ScreenshotComputerRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.browsers.computer.<a href="src/bctrl/browsers/computer/client.py">scroll</a>(...) -> ComputerResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Scroll the current Browser Run in the requested direction by a bounded amount, optionally at screenshot-pixel coordinates. Human control blocks automation. An interrupted action returns unknown.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.computer.scroll(
    browser_id="browserId",
    amount=1,
    direction="up",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**amount:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**direction:** `BrowsersComputerScrollRequestDirection` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[ScrollComputerRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**coordinate:** `typing.Optional[typing.List[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**modifiers:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.browsers.computer.<a href="src/bctrl/browsers/computer/client.py">type</a>(...) -> ComputerResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Type text into the focused control in the current Browser Run. Text is excluded from canonical capability Events and replay results are encrypted. Human control blocks automation; an interrupted action returns unknown.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.computer.type(
    browser_id="browserId",
    text="text",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**text:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[TypeComputerRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.browsers.computer.<a href="src/bctrl/browsers/computer/client.py">wait</a>(...) -> ComputerResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Wait up to ten seconds in the current Browser Run. Human control blocks automation. The result carries its canonical Event ID; interrupted execution returns unknown.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.computer.wait(
    browser_id="browserId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[WaitComputerRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**duration:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Browsers Connections
<details><summary><code>client.browsers.connections.<a href="src/bctrl/browsers/connections/client.py">revoke</a>(...) -> BrowserResource</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Invalidate every existing connection URL for the current Run and issue connections in a new credential generation. Refresh the browser before reconnecting.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.connections.revoke(
    browser_id="browserId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[RevokeConnectionsRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Browsers Control
<details><summary><code>client.browsers.control.<a href="src/bctrl/browsers/control/client.py">get</a>(...) -> BrowserControl</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read desired control and native confirmation for the current Browser Run. The holder credential is never returned. A human hold persists across restarts, while old viewer credentials cannot control a newer Run.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.control.get(
    browser_id="browserId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[GetControlRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.browsers.control.<a href="src/bctrl/browsers/control/client.py">release</a>(...) -> BrowserControlResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Release control held by the supplied current viewer. Another viewer cannot release its hold. A stale epoch or ended Run is refused before mutation. Automation remains blocked until the native applied ACK. Interrupted delivery returns unknown with its canonical Event ID and must not be retried automatically.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.control.release(
    browser_id="browserId",
    viewer_id="viewerId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `BrowserControlChangeRequest` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[ReleaseControlRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.browsers.control.<a href="src/bctrl/browsers/control/client.py">take</a>(...) -> BrowserControlResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Give a current input-enabled viewer human control of the Browser. The viewer credential must belong to this Browser and current Run, and its parent View must still permit input. The hold ends with that viewer. The result names the canonical control Event; an unconfirmed native ACK returns unknown. Reusing the same Idempotency-Key never repeats the transition.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.control.take(
    browser_id="browserId",
    viewer_id="viewerId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `BrowserControlChangeRequest` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[TakeControlRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Browsers Files
<details><summary><code>client.browsers.files.<a href="src/bctrl/browsers/files/client.py">list</a>(...) -> BrowserFileListResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List a directory of the current Browser Run. The top level holds /downloads, /files (the Run's Space files, read only) and /workspace; nothing else of the machine is reachable. Pages are ordered by name and a cursor belongs to its Run.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.files.list(
    browser_id="browserId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**path:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[ListFilesRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.browsers.files.<a href="src/bctrl/browsers/files/client.py">delete</a>(...) -> BrowserFileDeleteResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a file or directory of the current Browser Run; a non-empty directory needs recursive. Top-level directories and /files cannot be deleted. An interrupted deletion returns unknown.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.files.delete(
    browser_id="browserId",
    path="path",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**recursive:** `typing.Optional[DeleteFilesRequestRecursive]` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[DeleteFilesRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.browsers.files.<a href="src/bctrl/browsers/files/client.py">download</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Download one file of the current Browser Run (at most 1 GiB) as bytes. Headers carry its size and SHA-256.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.files.download(
    browser_id="browserId",
    path="x",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[DownloadFilesRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.browsers.files.<a href="src/bctrl/browsers/files/client.py">upload</a>(...) -> BrowserFileUploadResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload one file into /downloads or /workspace of the current Browser Run from multipart field file (at most 25 MiB). The file is written atomically; set overwrite to replace an existing file and createParents to create missing directories. An interrupted upload returns unknown.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.files.upload(
    browser_id="browserId",
    path="path",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**overwrite:** `typing.Optional[UploadFilesRequestOverwrite]` 
    
</dd>
</dl>

<dl>
<dd>

**create_parents:** `typing.Optional[UploadFilesRequestCreateParents]` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[UploadFilesRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.browsers.files.<a href="src/bctrl/browsers/files/client.py">move</a>(...) -> BrowserFileMoveResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Move or rename a file or directory of the current Browser Run within /downloads and /workspace. Set overwrite to replace the destination. An interrupted move returns unknown.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.files.move(
    browser_id="browserId",
    destination_path="destinationPath",
    source_path="sourcePath",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**destination_path:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**source_path:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[MoveFilesRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**overwrite:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Browsers Pages
<details><summary><code>client.browsers.pages.<a href="src/bctrl/browsers/pages/client.py">list</a>(...) -> PagesResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the open pages of the current Browser Run, ordered by Page ID. A cursor belongs to the Run that produced it. The result carries its canonical Event ID; interrupted execution returns unknown.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.pages.list(
    browser_id="browserId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[ListPagesRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.browsers.pages.<a href="src/bctrl/browsers/pages/client.py">open</a>(...) -> PageResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Open a new page in the current Browser Run at an HTTP(S) URL or about:blank, activated by default. Human control blocks automation. An interrupted action returns unknown and must not be repeated automatically.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.pages.open(
    browser_id="browserId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[OpenPagesRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**activate:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.browsers.pages.<a href="src/bctrl/browsers/pages/client.py">get</a>(...) -> PageResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read one open page of the current Browser Run: its URL, title and whether it is active. The result carries its canonical Event ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.pages.get(
    browser_id="browserId",
    page_id="pageId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page_id:** `str` — Unique page identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[GetPagesRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.browsers.pages.<a href="src/bctrl/browsers/pages/client.py">close</a>(...) -> PageDeleteResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Close one page of the current Browser Run. Human control blocks automation. An interrupted action returns unknown and must not be repeated automatically.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.pages.close(
    browser_id="browserId",
    page_id="pageId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page_id:** `str` — Unique page identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[ClosePagesRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.browsers.pages.<a href="src/bctrl/browsers/pages/client.py">activate</a>(...) -> PageResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Bring one page of the current Browser Run to the front. Activation is confirmed by the browser, never assumed. Human control blocks automation; an interrupted action returns unknown.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.pages.activate(
    browser_id="browserId",
    page_id="pageId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page_id:** `str` — Unique page identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[ActivatePagesRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.browsers.pages.<a href="src/bctrl/browsers/pages/client.py">navigate</a>(...) -> PageResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Navigate one page of the current Browser Run to an HTTP(S) URL and wait up to timeoutMs for its document. Human control blocks automation. An interrupted navigation returns unknown and must not be repeated automatically.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.pages.navigate(
    browser_id="browserId",
    page_id="pageId",
    url="url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page_id:** `str` — Unique page identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[NavigatePagesRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**timeout_ms:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.browsers.pages.<a href="src/bctrl/browsers/pages/client.py">pdf</a>(...) -> PagePdfResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Print one page of the current Browser Run to PDF. The document is returned base64 encoded. Interrupted execution returns unknown with null data.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.pages.pdf(
    browser_id="browserId",
    page_id="pageId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page_id:** `str` — Unique page identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[PdfPagesRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**landscape:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**print_background:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**scale:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.browsers.pages.<a href="src/bctrl/browsers/pages/client.py">screenshot</a>(...) -> PageScreenshotResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Capture one page of the current Browser Run as PNG or JPEG, optionally the full page. The image is returned base64 encoded. Interrupted execution returns unknown with null data.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.pages.screenshot(
    browser_id="browserId",
    page_id="pageId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page_id:** `str` — Unique page identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[ScreenshotPagesRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[BrowsersPagesScreenshotRequestFormat]` 
    
</dd>
</dl>

<dl>
<dd>

**full_page:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Browsers Recording
<details><summary><code>client.browsers.recording.<a href="src/bctrl/browsers/recording/client.py">get</a>(...) -> Recording</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read capture and MP4 export progress for the current Browser Run. Completed recordings are read through the historical Run recording routes. A succeeded recording includes a direct standalone MP4 URL, expiry, SHA-256 and byte size. Partial capture is reported explicitly. Download URLs expire within five minutes and never outlive a View.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.recording.get(
    browser_id="browserId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Browsers Runs
<details><summary><code>client.browsers.runs.<a href="src/bctrl/browsers/runs/client.py">list</a>(...) -> BrowsersRunsListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the retained Runs belonging to this browser, including ended and failed Runs, using cursor pagination.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment
import datetime

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.runs.list(
    browser_id="browserId",
    from_=datetime.datetime.fromisoformat("2026-07-26T12:00:00+00:00"),
    to=datetime.datetime.fromisoformat("2026-07-26T12:00:00+00:00"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListRunsRequestOrder]` — Order by createdAt and ID. Defaults to desc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[ListRunsRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListRunsRequestStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[Rfc3339Timestamp]` 
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[Rfc3339Timestamp]` 
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[ListRunsRequestInclude]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Browsers Computer Clipboard
<details><summary><code>client.browsers.computer.clipboard.<a href="src/bctrl/browsers/computer/clipboard/client.py">read</a>(...) -> ComputerClipboardReadResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read the system clipboard of the current Browser Run as text (at most 256 KiB of UTF-8). Reading has no effect on the page. The result carries its canonical Event ID; interrupted execution returns unknown.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.computer.clipboard.read(
    browser_id="browserId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[ReadClipboardRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.browsers.computer.clipboard.<a href="src/bctrl/browsers/computer/clipboard/client.py">write</a>(...) -> ComputerClipboardWriteResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replace the system clipboard of the current Browser Run with text (at most 256 KiB of UTF-8, no NUL); empty text clears it. Nothing is pasted. The text is excluded from Events. Human control blocks automation; an interrupted write returns unknown.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.browsers.computer.clipboard.write(
    browser_id="browserId",
    text="text",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**browser_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**text:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[WriteClipboardRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Proxies Geo
<details><summary><code>client.proxies.geo.<a href="src/bctrl/proxies/geo/client.py">list</a>(...) -> ProxyLocationListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search provider-backed managed proxy geo targets. Use geoId results when creating dynamic managed rotating proxies.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.proxies.geo.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListGeoRequestOrder]` — Order by createdAt and ID. Defaults to desc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[ListGeoRequestType]` 
    
</dd>
</dl>

<dl>
<dd>

**pool:** `typing.Optional[ProxyLocationPool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Proxies Locations
<details><summary><code>client.proxies.locations.<a href="src/bctrl/proxies/locations/client.py">list</a>(...) -> ProxyLocationListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search customer-facing managed proxy locations. Use geoId results for dynamic managed rotating proxy targeting.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.proxies.locations.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListLocationsRequestOrder]` — Order by createdAt and ID. Defaults to desc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[ListLocationsRequestType]` 
    
</dd>
</dl>

<dl>
<dd>

**pool:** `typing.Optional[ProxyLocationPool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Proxies Pools
<details><summary><code>client.proxies.pools.<a href="src/bctrl/proxies/pools/client.py">list</a>(...) -> ProxyPoolListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List customer-facing managed proxy pools. Use this to discover static proxy pools before creating a managed static proxy.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.proxies.pools.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListPoolsRequestOrder]` — Order by createdAt and ID. Defaults to desc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**category:** `typing.Optional[ListPoolsRequestCategory]` 
    
</dd>
</dl>

<dl>
<dd>

**available:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.proxies.pools.<a href="src/bctrl/proxies/pools/client.py">get</a>(...) -> ProxyPool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get one managed proxy pool by id before creating a managed static proxy.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.proxies.pools.get(
    pool_id="poolId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pool_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Runs Files
<details><summary><code>client.runs.files.<a href="src/bctrl/runs/files/client.py">list</a>(...) -> RunFilesListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List a Run's files: inputs bound to the Run with their copy state in its cell, and outputs the Run produced.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.runs.files.list(
    run_id="runId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` — Unique run identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListFilesRequestOrder]` — Order by createdAt and ID. Defaults to desc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**role:** `typing.Optional[RunFileRole]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.runs.files.<a href="src/bctrl/runs/files/client.py">add</a>(...) -> RunFile</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Bind an existing Space File to the Run. The Run's cell keeps a copy at the returned runtimePath.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.runs.files.add(
    run_id="runId",
    file_id="fileId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` — Unique run identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `str` — Unique file identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.runs.files.<a href="src/bctrl/runs/files/client.py">get</a>(...) -> RunFile</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get one Run file.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.runs.files.get(
    run_id="runId",
    file_id="fileId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` — Unique run identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `str` — Unique file identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.runs.files.<a href="src/bctrl/runs/files/client.py">remove</a>(...) -> RunFile</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove a Run input from the Run's cell. The Space File is kept.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.runs.files.remove(
    run_id="runId",
    file_id="fileId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` — Unique run identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `str` — Unique file identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.runs.files.<a href="src/bctrl/runs/files/client.py">retry</a>(...) -> RunFile</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Copy a failed Run input into the cell again.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.runs.files.retry(
    run_id="runId",
    file_id="fileId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` — Unique run identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `str` — Unique file identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.runs.files.<a href="src/bctrl/runs/files/client.py">collect</a>(...) -> RunFile</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Save a file from the Run's workspace as an output File.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.runs.files.collect(
    run_id="runId",
    runtime_path="runtimePath",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` — Unique run identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**runtime_path:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**filename:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**path:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.runs.files.<a href="src/bctrl/runs/files/client.py">upload</a>(...) -> RunFile</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload one durable Space File (at path, default uploads/<filename>) and bind it to this Run. The Run's cell keeps a copy at the returned runtimePath; binding.state reports when it is ready.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.runs.files.upload(
    run_id="runId",
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` — Unique run identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**file:** `core.File` — File bytes to upload.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**filename:** `typing.Optional[str]` — Optional display filename.
    
</dd>
</dl>

<dl>
<dd>

**path:** `typing.Optional[str]` — Space path for the new File. Defaults to uploads/<filename>.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Runs Recordings
<details><summary><code>client.runs.recordings.<a href="src/bctrl/runs/recordings/client.py">list</a>(...) -> RecordingsList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read the whole-Run recording, including export progress and a direct standalone MP4 download with its SHA-256 when succeeded. Preserves historical Run access after Browser deletion. Purged artifacts are excluded. Download URLs expire within five minutes and never outlive a View.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.runs.recordings.list(
    run_id="runId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` — Unique run identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListRecordingsRequestOrder]` — Order by createdAt and ID. Defaults to desc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.runs.recordings.<a href="src/bctrl/runs/recordings/client.py">get</a>(...) -> Recording</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read one recording belonging to this Run. A succeeded recording includes a direct standalone MP4 download URL, expiry, SHA-256 and byte size. Partial capture is reported explicitly. Download URLs expire within five minutes and never outlive a View.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.runs.recordings.get(
    run_id="runId",
    recording_id="recordingId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` — Unique run identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**recording_id:** `str` — Unique recording identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Runs Trace
<details><summary><code>client.runs.trace.<a href="src/bctrl/runs/trace/client.py">list</a>(...) -> TraceSpanListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List structured trace spans for a run.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.runs.trace.list(
    run_id="runId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` — Unique run identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**parent_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**kind:** `typing.Optional[typing.Union[ListTraceRequestKindItem, typing.Sequence[ListTraceRequestKindItem]]]` — Filter by one or more trace span kinds. Repeat the query parameter for multiple values.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[ListTraceRequestStatusItem, typing.Sequence[ListTraceRequestStatusItem]]]` — Filter by one or more trace span statuses. Repeat the query parameter for multiple values.
    
</dd>
</dl>

<dl>
<dd>

**resource_type:** `typing.Optional[ListTraceRequestResourceType]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListTraceRequestOrder]` — Order by createdAt and ID. Defaults to desc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Sandboxes Browser
<details><summary><code>client.sandboxes.browser.<a href="src/bctrl/sandboxes/browser/client.py">attach</a>(...) -> Sandbox</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Attach one browser from the same Space to a sandbox.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.sandboxes.browser.attach(
    sandbox_id="sandboxId",
    browser_id="browserId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**browser_id:** `str` — Unique browser identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Sandboxes Connections
<details><summary><code>client.sandboxes.connections.<a href="src/bctrl/sandboxes/connections/client.py">create</a>(...) -> SandboxConnectionCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Open an interactive terminal (PTY) to a ready sandbox. Returns a WebSocket URL and a one-time ticket. Refused while a Task is using the sandbox.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl, SandboxConnectionCreateRequest_Terminal
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.sandboxes.connections.create(
    sandbox_id="sandboxId",
    request=SandboxConnectionCreateRequest_Terminal(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `SandboxConnectionCreateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.connections.<a href="src/bctrl/sandboxes/connections/client.py">get</a>(...) -> SandboxConnection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a sandbox connection and whether it has been revoked.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.sandboxes.connections.get(
    sandbox_id="sandboxId",
    connection_id="connectionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**connection_id:** `str` — Unique sandboxConnection identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.connections.<a href="src/bctrl/sandboxes/connections/client.py">delete</a>(...) -> SandboxConnection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revoke a sandbox connection. An open terminal is closed within seconds.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.sandboxes.connections.delete(
    sandbox_id="sandboxId",
    connection_id="connectionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**connection_id:** `str` — Unique sandboxConnection identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Sandboxes Files
<details><summary><code>client.sandboxes.files.<a href="src/bctrl/sandboxes/files/client.py">list</a>(...) -> SandboxFileListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List files in the sandbox working directory.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.sandboxes.files.list(
    sandbox_id="sandboxId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**path:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.files.<a href="src/bctrl/sandboxes/files/client.py">collect</a>(...) -> File</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Publish a file from the sandbox working directory as a durable File.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.sandboxes.files.collect(
    sandbox_id="sandboxId",
    path="path",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.files.<a href="src/bctrl/sandboxes/files/client.py">stage</a>(...) -> SandboxFileStageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Copy a durable File into the sandbox working directory.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.sandboxes.files.stage(
    sandbox_id="sandboxId",
    file_id="fileId",
    path="path",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `str` — Unique file identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**overwrite:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Sandboxes Ports
<details><summary><code>client.sandboxes.ports.<a href="src/bctrl/sandboxes/ports/client.py">list</a>(...) -> SandboxesPortsListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The ports of the sandbox that have an open, unexpired preview, with the preview connections of each.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.sandboxes.ports.list(
    sandbox_id="sandboxId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.ports.<a href="src/bctrl/sandboxes/ports/client.py">create</a>(...) -> SandboxPortCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

An authenticated HTTPS URL that forwards to a TCP port inside the sandbox until it expires or is deleted.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.sandboxes.ports.create(
    sandbox_id="sandboxId",
    port=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**port:** `int` — A TCP port a process in the sandbox listens on (127.0.0.1).
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**expires_in_seconds:** `typing.Optional[int]` — How long the preview URL works.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.ports.<a href="src/bctrl/sandboxes/ports/client.py">delete</a>(...) -> SandboxPortDeleted</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revokes every open preview of the port; their URLs stop working at once.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.sandboxes.ports.delete(
    sandbox_id="sandboxId",
    port=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**port:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Sandboxes Processes
<details><summary><code>client.sandboxes.processes.<a href="src/bctrl/sandboxes/processes/client.py">create</a>(...) -> SandboxProcessAccepted</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start a bounded process in a sandbox. The command is an argument array, never a shell string. For an interactive PTY, open a terminal connection.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.sandboxes.processes.create(
    sandbox_id="sandboxId",
    command=[
        "command"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**command:** `typing.List[str]` — Program and arguments. Never interpreted by a host shell.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**cwd:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**timeout_seconds:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.processes.<a href="src/bctrl/sandboxes/processes/client.py">get</a>(...) -> SandboxProcess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a sandbox process with its exit code and captured output.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.sandboxes.processes.get(
    sandbox_id="sandboxId",
    process_id="processId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**process_id:** `str` — Unique sandboxProcess identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.processes.<a href="src/bctrl/sandboxes/processes/client.py">cancel</a>(...) -> SandboxProcess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel one sandbox process.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.sandboxes.processes.cancel(
    sandbox_id="sandboxId",
    process_id="processId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**process_id:** `str` — Unique sandboxProcess identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.processes.<a href="src/bctrl/sandboxes/processes/client.py">stream</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stream sandbox process output and completion.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.sandboxes.processes.stream(
    sandbox_id="sandboxId",
    process_id="processId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**process_id:** `str` — Unique sandboxProcess identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**last_event_id:** `typing.Optional[str]` — Optional last delivered event identifier used to resume an SSE stream.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Sandboxes Snapshots
<details><summary><code>client.sandboxes.snapshots.<a href="src/bctrl/sandboxes/snapshots/client.py">list</a>(...) -> SandboxesSnapshotsListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the snapshots taken of a sandbox, newest first.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.sandboxes.snapshots.list(
    sandbox_id="sandboxId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.snapshots.<a href="src/bctrl/sandboxes/snapshots/client.py">create</a>(...) -> SandboxSnapshot</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Snapshot a running sandbox with its memory and disk; it keeps running. The snapshot stays on the node that runs the sandbox, and `POST /sandboxes` with `fromSnapshot` forks it there.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.sandboxes.snapshots.create(
    sandbox_id="sandboxId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[ResourceName]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.snapshots.<a href="src/bctrl/sandboxes/snapshots/client.py">get</a>(...) -> SandboxSnapshot</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a sandbox snapshot.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.sandboxes.snapshots.get(
    sandbox_id="sandboxId",
    snapshot_id="snapshotId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**snapshot_id:** `str` — Unique sandboxSnapshot identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.snapshots.<a href="src/bctrl/sandboxes/snapshots/client.py">delete</a>(...) -> SandboxSnapshotDeleteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a sandbox snapshot from its node. Sandboxes already forked from it keep running.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.sandboxes.snapshots.delete(
    sandbox_id="sandboxId",
    snapshot_id="snapshotId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**snapshot_id:** `str` — Unique sandboxSnapshot identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Sandboxes SshSessions
<details><summary><code>client.sandboxes.ssh_sessions.<a href="src/bctrl/sandboxes/ssh_sessions/client.py">create</a>(...) -> SandboxSshSession</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Short-lived SSH credentials (host, port, one-time password) for a shell or commands in the sandbox. Revoke with DELETE /v1/sandboxes/{sandboxId}/connections/{id}.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.sandboxes.ssh_sessions.create(
    sandbox_id="sandboxId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**expires_in_seconds:** `typing.Optional[int]` — How long the session may stay open.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Spaces SpendingCap
<details><summary><code>client.spaces.spending_cap.<a href="src/bctrl/spaces/spending_cap/client.py">get</a>(...) -> SpendingCap</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read this Space’s UTC calendar-month limit and accrued usage in USD cents. Both the organization and Space limits apply. Warning occurs once per month at 80%; at 100%, running work is stopped within at most one minute of additional usage.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.spaces.spending_cap.get(
    space_id="spaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**space_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.spaces.spending_cap.<a href="src/bctrl/spaces/spending_cap/client.py">update</a>(...) -> SpendingCap</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

People may set this Space’s whole-cent USD limit; null disables it and zero refuses new billable starts here. Other Spaces are unaffected. Raising it allows starts when both this limit and the organization limit exceed current usage.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.spaces.spending_cap.update(
    space_id="spaceId",
    currency="USD",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**space_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `SpendingCapPatchRequest` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Subaccounts Usage
<details><summary><code>client.subaccounts.usage.<a href="src/bctrl/subaccounts/usage/client.py">list</a>(...) -> SubaccountUsageListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List current usage snapshots for subaccounts. Prefer GET /v1/subaccounts?include=usage when you also need subaccount metadata.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.subaccounts.usage.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListUsageRequestOrder]` — Order by createdAt and ID. Defaults to desc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tasks Trace
<details><summary><code>client.tasks.trace.<a href="src/bctrl/tasks/trace/client.py">list</a>(...) -> TasksTraceListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Page spans across the Runs opened by this Task, retaining each Run and parent span ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.tasks.trace.list(
    task_id="taskId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `str` — Unique task identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**parent_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**kind:** `typing.Optional[ListTraceRequestKind]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListTraceRequestStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**resource_type:** `typing.Optional[ListTraceRequestResourceType]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListTraceRequestOrder]` — Order by createdAt and ID. Defaults to desc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tools Calls
<details><summary><code>client.tools.calls.<a href="src/bctrl/tools/calls/client.py">create</a>(...) -> ToolCall</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a durable ToolCall and optionally wait for its status.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.tools.calls.create(
    tool_ref="toolRef",
    input={},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tool_ref:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**input:** `JsonObject` 
    
</dd>
</dl>

<dl>
<dd>

**wait:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**runtime_id:** `typing.Optional[str]` — Unique browser identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Webhooks Deliveries
<details><summary><code>client.webhooks.deliveries.<a href="src/bctrl/webhooks/deliveries/client.py">list</a>(...) -> WebhookDeliveriesListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List delivery attempts for one webhook endpoint, including response status and retry state.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.webhooks.deliveries.list(
    webhook_id="webhookId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**webhook_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListDeliveriesRequestOrder]` — Order by createdAt and ID. Defaults to desc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.deliveries.<a href="src/bctrl/webhooks/deliveries/client.py">redeliver</a>(...) -> WebhookDelivery</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reset one delivery and queue it for another signed delivery attempt.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from bctrl import Bctrl
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.webhooks.deliveries.redeliver(
    webhook_id="webhookId",
    delivery_id="deliveryId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**webhook_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**delivery_id:** `str` — Unique webhookDelivery identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

