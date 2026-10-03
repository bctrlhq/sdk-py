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

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.conversations.list()

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

**runtime_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListConversationsRequestStatus]` 
    
</dd>
</dl>

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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversations.<a href="src/bctrl/conversations/client.py">create</a>(...) -> Conversation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an agent conversation bound to an active runtime.
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

client.conversations.create(
    runtime_id="runtimeId",
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

**runtime_id:** `str` — Unique browser identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**toolset_id:** `typing.Optional[str]` — Unique toolset identifier generated by BCTRL.
    
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

<details><summary><code>client.conversations.<a href="src/bctrl/conversations/client.py">get</a>(...) -> ConversationDetail</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a conversation with its durable messages and turns.
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

**message_cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**message_limit:** `typing.Optional[int]` 
    
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

<details><summary><code>client.conversations.<a href="src/bctrl/conversations/client.py">update</a>(...) -> Conversation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the defaults used by future turns in a conversation.
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

**model:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**toolset_id:** `typing.Optional[str]` — Unique toolset identifier generated by BCTRL.
    
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

<details><summary><code>client.conversations.<a href="src/bctrl/conversations/client.py">cancel</a>(...) -> ConversationCancelResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel the active turn in a conversation.
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

client.conversations.cancel(
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

<details><summary><code>client.conversations.<a href="src/bctrl/conversations/client.py">stream</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stream normalized durable conversation events.
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

client.conversations.stream(
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

<details><summary><code>client.conversations.<a href="src/bctrl/conversations/client.py">start</a>(...) -> ConversationStartAccepted</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a conversation and queue its first agent turn in one call, starting the runtime when needed.
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

client.conversations.start(
    runtime_id="runtimeId",
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

**runtime_id:** `str` — Unique browser identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**text:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**file_ids:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_id:** `typing.Optional[str]` — Unique page identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**start_runtime:** `typing.Optional[bool]` — Start the Runtime when it is stopped. When false, a stopped Runtime is rejected with a conflict.
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**toolset_id:** `typing.Optional[str]` — Unique toolset identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[ConversationVariables]` 
    
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

## environments
<details><summary><code>client.environments.<a href="src/bctrl/environments/client.py">list</a>(...) -> EnvironmentsListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List agent Environments visible to the caller.
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

client.environments.list()

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

**order:** `typing.Optional[ListEnvironmentsRequestOrder]` — Order by createdAt and ID. Defaults to desc.
    
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

<details><summary><code>client.environments.<a href="src/bctrl/environments/client.py">create</a>(...) -> Environment</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an agent Environment from an approved image. Returns while the sandbox is provisioning.
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

client.environments.create(
    image="image",
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

**image:** `str` — Approved Environment image identifier, for example `bctrl-pi-stable`.
    
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

<details><summary><code>client.environments.<a href="src/bctrl/environments/client.py">get</a>(...) -> Environment</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get one agent Environment with its status and qualified capabilities.
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

client.environments.get(
    environment_id="environmentId",
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

**environment_id:** `str` 
    
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

<details><summary><code>client.environments.<a href="src/bctrl/environments/client.py">delete</a>(...) -> EnvironmentDeleteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently delete an Environment that is not bound to a conversation.
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

client.environments.delete(
    environment_id="environmentId",
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

**environment_id:** `str` 
    
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

<details><summary><code>client.environments.<a href="src/bctrl/environments/client.py">start</a>(...) -> Environment</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Ensure an Environment has running compute, keeping its working files.
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

client.environments.start(
    environment_id="environmentId",
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

**environment_id:** `str` 
    
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

<details><summary><code>client.environments.<a href="src/bctrl/environments/client.py">stop</a>(...) -> Environment</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stop Environment compute. Active work is a conflict unless force is set. Working files stay on the host local disk while stopped and are not replicated: if that host is lost, the Environment fails with `environment.host_lost` and its files may be lost.
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

client.environments.stop(
    environment_id="environmentId",
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

**environment_id:** `str` 
    
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

<details><summary><code>client.secrets.<a href="src/bctrl/secrets/client.py">reveal</a>(...) -> SecretRevealResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the values of a Secret version. Only people may reveal: organization or subaccount API keys and dashboard sessions. Agent turns, delegated code and View tokens get 403 `secrets.reveal_forbidden`. Every reveal is audited.
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

**path:** `str` — Secret path, for example `prod/github/bot`. May contain `/`.
    
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

<details><summary><code>client.secrets.<a href="src/bctrl/secrets/client.py">get</a>(...) -> Secret</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read one Secret: its metadata and which fields are set. Secret fields are write-only; use `POST /v1/secrets:reveal` to read values.
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

**path:** `str` — Secret path, for example `prod/github/bot`. May contain `/`.
    
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

<details><summary><code>client.secrets.<a href="src/bctrl/secrets/client.py">put</a>(...) -> Secret</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or replace a Secret. Every write is a new version, returned as `version` and the `ETag` header. Send `If-Match` to write only over a known version. Send `{fromVersion}` alone to roll back to an earlier version.
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

client.secrets.put(
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

**path:** `str` — Secret path, for example `prod/github/bot`. May contain `/`.
    
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

**from_version:** `typing.Optional[int]` — Rollback: make the values of this earlier version the new version. Send it alone.
    
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

**type:** `typing.Optional[SecretPutRequestType]` — `login`: username, password and TOTP seed for a site. `value`: one opaque value.
    
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

**path:** `str` — Secret path, for example `prod/github/bot`. May contain `/`.
    
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

**path:** `str` — Secret path, for example `prod/github/bot`. May contain `/`.
    
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

<details><summary><code>client.spaces.<a href="src/bctrl/spaces/client.py">delete</a>(...) -> SpaceDeleteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a space after its active runtimes have been stopped.
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

**turn_id:** `typing.Optional[str]` 
    
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

Create an organization custom callable tool. Agents can use these tools through space toolsets during hosted work.
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

**modes:** `typing.Optional[typing.List[ToolUpdateRequestModesItem]]` 
    
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

<details><summary><code>client.tools.<a href="src/bctrl/tools/client.py">call</a>(...) -> JsonValue</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call a synchronous tool and wait for its validated result.
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

client.tools.call(
    tool_ref="toolRef",
    request={},
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

**request:** `JsonObject` 
    
</dd>
</dl>

<dl>
<dd>

**bctrl_runtime_id:** `typing.Optional[str]` — Optional Runtime selector for direct Runtime-bound Tool calls. The Control Plane resolves the active Run atomically; callers cannot select a Run directly.
    
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

## toolsets
<details><summary><code>client.toolsets.<a href="src/bctrl/toolsets/client.py">list</a>(...) -> ToolsetListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List reusable tool bundles in a space using the simplified response envelope.
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

client.toolsets.list()

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

**order:** `typing.Optional[ListToolsetsRequestOrder]` — Order by createdAt and ID. Defaults to desc.
    
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

<details><summary><code>client.toolsets.<a href="src/bctrl/toolsets/client.py">create</a>(...) -> Toolset</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an ordered reusable bundle of built-in and custom tools.
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

client.toolsets.create(
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

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[ToolsetCreateRequestSpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**tools:** `typing.Optional[typing.List[ToolsetCreateRequestToolsItem]]` 
    
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

<details><summary><code>client.toolsets.<a href="src/bctrl/toolsets/client.py">get</a>(...) -> Toolset</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get one toolset, including enabled built-in capabilities, custom tool IDs, and metadata.
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

client.toolsets.get(
    toolset_id="toolsetId",
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

**toolset_id:** `str` 
    
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

<details><summary><code>client.toolsets.<a href="src/bctrl/toolsets/client.py">delete</a>(...) -> ToolsetDeleteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a toolset when it should no longer be used for new work.
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

client.toolsets.delete(
    toolset_id="toolsetId",
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

**toolset_id:** `str` 
    
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

<details><summary><code>client.toolsets.<a href="src/bctrl/toolsets/client.py">update</a>(...) -> Toolset</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a reusable tool bundle by changing its name, built-in capabilities, custom tools, or metadata.
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

client.toolsets.update(
    toolset_id="toolsetId",
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

**toolset_id:** `str` 
    
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

**name:** `typing.Optional[ResourceName]` 
    
</dd>
</dl>

<dl>
<dd>

**tools:** `typing.Optional[typing.List[ToolsetUpdateRequestToolsItem]]` 
    
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

**conversation_send:** `typing.Optional[bool]` — Allow sending messages to and cancelling turns in the included conversations. Defaults to the value of control.
    
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
        "run.started"
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

**events:** `typing.List[WebhookCreateRequestEventsItem]` 
    
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

**events:** `typing.Optional[typing.List[WebhookUpdateRequestEventsItem]]` 
    
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

## Conversations Messages
<details><summary><code>client.conversations.messages.<a href="src/bctrl/conversations/messages/client.py">create</a>(...) -> AgentTurnAccepted</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Append a user message and start one agent turn.
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

client.conversations.messages.create(
    conversation_id="conversationId",
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

**conversation_id:** `str` — Unique conversation identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**text:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional retry key for this billable operation. Reusing the same key with the same request replays its stable outcome; credential-bearing results may be freshly issued for the same principal. Reusing it with a different request returns 409.
    
</dd>
</dl>

<dl>
<dd>

**file_ids:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_id:** `typing.Optional[str]` — Unique page identifier generated by BCTRL.
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[ConversationVariables]` 
    
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

## Conversations Turns
<details><summary><code>client.conversations.turns.<a href="src/bctrl/conversations/turns/client.py">get</a>(...) -> AgentTurn</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get one agent turn with its status and execution attribution.
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

client.conversations.turns.get(
    conversation_id="conversationId",
    turn_id="turnId",
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

**turn_id:** `str` — Unique agentTurn identifier generated by BCTRL.
    
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

<details><summary><code>client.conversations.turns.<a href="src/bctrl/conversations/turns/client.py">cancel</a>(...) -> AgentTurn</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel one specific agent turn.
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

client.conversations.turns.cancel(
    conversation_id="conversationId",
    turn_id="turnId",
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

**turn_id:** `str` — Unique agentTurn identifier generated by BCTRL.
    
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

## Environments Connections
<details><summary><code>client.environments.connections.<a href="src/bctrl/environments/connections/client.py">get</a>(...) -> EnvironmentConnection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an Environment connection and whether it has been revoked.
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

client.environments.connections.get(
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

**connection_id:** `str` — Unique environmentConnection identifier generated by BCTRL.
    
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

<details><summary><code>client.environments.connections.<a href="src/bctrl/environments/connections/client.py">delete</a>(...) -> EnvironmentConnection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revoke an Environment connection. An open terminal is closed within seconds.
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

client.environments.connections.delete(
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

**connection_id:** `str` — Unique environmentConnection identifier generated by BCTRL.
    
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

<details><summary><code>client.environments.connections.<a href="src/bctrl/environments/connections/client.py">create</a>(...) -> EnvironmentConnectionCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Open direct terminal access to a ready Environment. Returns a WebSocket URL and a one-time ticket. Refused while a managed conversation turn is using the Environment.
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
from bctrl import Bctrl, EnvironmentConnectionCreateRequest_Terminal
from bctrl.environment import BctrlEnvironment

client = Bctrl(
    token="<token>",
    environment=BctrlEnvironment.PRODUCTION,
)

client.environments.connections.create(
    environment_id="environmentId",
    request=EnvironmentConnectionCreateRequest_Terminal(),
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

**environment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `EnvironmentConnectionCreateRequest` 
    
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

## Environments Execs
<details><summary><code>client.environments.execs.<a href="src/bctrl/environments/execs/client.py">get</a>(...) -> EnvironmentExec</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an Environment execution with its exit code and captured output.
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

client.environments.execs.get(
    exec_id="execId",
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

**exec_id:** `str` — Unique environmentExec identifier generated by BCTRL.
    
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

<details><summary><code>client.environments.execs.<a href="src/bctrl/environments/execs/client.py">cancel</a>(...) -> EnvironmentExec</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel one Environment execution.
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

client.environments.execs.cancel(
    exec_id="execId",
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

**exec_id:** `str` — Unique environmentExec identifier generated by BCTRL.
    
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

<details><summary><code>client.environments.execs.<a href="src/bctrl/environments/execs/client.py">stream</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stream Environment execution output and completion.
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

client.environments.execs.stream(
    exec_id="execId",
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

**exec_id:** `str` — Unique environmentExec identifier generated by BCTRL.
    
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

<details><summary><code>client.environments.execs.<a href="src/bctrl/environments/execs/client.py">create</a>(...) -> EnvironmentExecAccepted</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start a bounded command in an Environment. The command is an argument array, never a shell string.
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

client.environments.execs.create(
    environment_id="environmentId",
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

**environment_id:** `str` 
    
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

## Environments Files
<details><summary><code>client.environments.files.<a href="src/bctrl/environments/files/client.py">list</a>(...) -> EnvironmentFileListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List files in the Environment working directory.
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

client.environments.files.list(
    environment_id="environmentId",
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

**environment_id:** `str` 
    
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

<details><summary><code>client.environments.files.<a href="src/bctrl/environments/files/client.py">collect</a>(...) -> File</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Publish a file from the Environment working directory as a durable File.
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

client.environments.files.collect(
    environment_id="environmentId",
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

**environment_id:** `str` 
    
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

<details><summary><code>client.environments.files.<a href="src/bctrl/environments/files/client.py">stage</a>(...) -> EnvironmentFileStageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Copy a durable File into the Environment working directory.
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

client.environments.files.stage(
    environment_id="environmentId",
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

**environment_id:** `str` 
    
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

## Environments Runtime
<details><summary><code>client.environments.runtime.<a href="src/bctrl/environments/runtime/client.py">attach</a>(...) -> Environment</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Attach one Runtime from the same Space to an Environment.
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

client.environments.runtime.attach(
    environment_id="environmentId",
    runtime_id="runtimeId",
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

**environment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**runtime_id:** `str` — Unique browser identifier generated by BCTRL.
    
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

## Runs Events
<details><summary><code>client.runs.events.<a href="src/bctrl/runs/events/client.py">list</a>(...) -> RunEventListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List raw machine-readable runtime events for a run.
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

client.runs.events.list(
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

**type:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by one or more namespaced event types. Repeat the query parameter for multiple values.
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[typing.Union[ListEventsRequestSourceItem, typing.Sequence[ListEventsRequestSourceItem]]]` — Filter by one or more event sources. Repeat the query parameter for multiple values.
    
</dd>
</dl>

<dl>
<dd>

**span_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_id:** `typing.Optional[str]` 
    
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

## Tools Calls
<details><summary><code>client.tools.calls.<a href="src/bctrl/tools/calls/client.py">create</a>(...) -> ToolCall</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start one durable asynchronous tool call.
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
    request={},
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

**request:** `JsonObject` 
    
</dd>
</dl>

<dl>
<dd>

**bctrl_runtime_id:** `typing.Optional[str]` — Optional Runtime selector for direct Runtime-bound Tool calls. The Control Plane resolves the active Run atomically; callers cannot select a Run directly.
    
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

