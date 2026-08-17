"""Resource namespace clients for the BCTRL public v1 API."""

from __future__ import annotations

from typing import Any, Iterator, Literal, Mapping, Optional
from urllib.parse import quote, urlencode

from .generated.tool_types import BuiltinToolsClient
from .http import V1HttpClient, make_file_part
from .runtime_context import StartedRuntime

JsonObject = dict[str, Any]


def _enc(value: str) -> str:
    return quote(value, safe="")


def _body(values: Mapping[str, Any]) -> JsonObject:
    return {_wire_key(key): value for key, value in values.items() if value is not None}


def _merge_patch(values: Mapping[str, Any]) -> JsonObject:
    """Convert field names while preserving explicit nulls for RFC 7396 patches."""
    return {_wire_key(key): value for key, value in values.items()}


def _wire_key(key: str) -> str:
    if "_" not in key:
        return key
    head, *tail = key.split("_")
    return head + "".join(part[:1].upper() + part[1:] for part in tail if part)


def _iter_pages(list_fn, params: Optional[Mapping[str, Any]] = None) -> Iterator[JsonObject]:
    query = dict(params or {})
    while True:
        page = list_fn(query)
        for item in page.get("data", []):
            yield item
        cursor = page.get("nextCursor")
        if not cursor:
            return
        query["cursor"] = cursor


def _stream_url(base_url: str, path: str, params: Mapping[str, Any]) -> str:
    query: list[tuple[str, str]] = []
    for key, value in params.items():
        if value is None:
            continue
        if isinstance(value, (list, tuple)):
            query.extend((key, str(item)) for item in value if item is not None)
        else:
            query.append((key, str(value)))
    suffix = urlencode(query)
    return f"{base_url}{path}?{suffix}" if suffix else f"{base_url}{path}"


class SpacesClient:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http

    def list(self, **params: Any) -> JsonObject:
        return self._http.request("GET", "/spaces", params=_body(params))

    def iter(self, **params: Any) -> Iterator[JsonObject]:
        return _iter_pages(lambda query: self.list(**query), params)

    def create(self, **request: Any) -> JsonObject:
        return self._http.request("POST", "/spaces", json_body=_body(request))

    def get(self, space_id: str) -> JsonObject:
        return self._http.request("GET", f"/spaces/{_enc(space_id)}")

    def update(self, space_id: str, **request: Any) -> JsonObject:
        return self._http.request("PATCH", f"/spaces/{_enc(space_id)}", json_body=_body(request))

    def delete(self, space_id: str) -> JsonObject:
        return self._http.request("DELETE", f"/spaces/{_enc(space_id)}")

class RuntimesClient:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http

    def list(self, **params: Any) -> JsonObject:
        return self._http.request("GET", "/runtimes", params=_body(params))

    def iter(self, **params: Any) -> Iterator[JsonObject]:
        return _iter_pages(lambda query: self.list(**query), params)

    def create(
        self, *, idempotency_key: Optional[str] = None, **request: Any
    ) -> JsonObject:
        return self._http.request(
            "POST",
            "/runtimes",
            json_body=_body(request),
            idempotency_key=idempotency_key,
        )

    def get(
        self, runtime_id: str, *, include: Optional[Literal["connection"]] = None
    ) -> JsonObject:
        params = {"include": include} if include is not None else {}
        return self._http.request("GET", f"/runtimes/{_enc(runtime_id)}", params=params)

    def update(self, runtime_id: str, **request: Any) -> JsonObject:
        return self._http.request(
            "PATCH", f"/runtimes/{_enc(runtime_id)}", json_body=_body(request)
        )

    def delete(self, runtime_id: str) -> JsonObject:
        return self._http.request("DELETE", f"/runtimes/{_enc(runtime_id)}")

    def start(
        self,
        runtime_id: str,
        *,
        recording: Optional[bool] = None,
        idempotency_key: Optional[str] = None,
    ) -> JsonObject:
        return self._http.request(
            "POST",
            f"/runtimes/{_enc(runtime_id)}/start",
            json_body=_body({"recording": recording}),
            idempotency_key=idempotency_key,
        )

    def stop(self, runtime_id: str) -> JsonObject:
        return self._http.request("POST", f"/runtimes/{_enc(runtime_id)}/stop")

    def started_browser(
        self,
        *,
        idempotency_key: Optional[str] = None,
        **request: Any,
    ) -> StartedRuntime:
        body = _body(request)
        body.setdefault("type", "browser")
        body.setdefault("start", True)
        return StartedRuntime(
            runtimes=self,
            request=body,
            idempotency_key=idempotency_key,
        )


class RunsClient:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http
        self.events = RunEventsNamespace(http)
        self.trace = RunTraceNamespace(http)
        self.files = RunFilesNamespace(http)

    def list(self, **params: Any) -> JsonObject:
        return self._http.request("GET", "/runs", params=_body(params))

    def iter(self, **params: Any) -> Iterator[JsonObject]:
        return _iter_pages(lambda query: self.list(**query), params)

    def get(
        self, run_id: str, *, include: Optional[Literal["connection"]] = None
    ) -> JsonObject:
        params = {"include": include} if include is not None else {}
        return self._http.request("GET", f"/runs/{_enc(run_id)}", params=params)

    def stream_url(self, run_id: str, **params: Any) -> str:
        return _stream_url(self._http.base_url, f"/runs/{_enc(run_id)}/stream", _body(params))

    def stream(self, run_id: str, **params: Any) -> Iterator[JsonObject]:
        return self._http.stream_sse(f"/runs/{_enc(run_id)}/stream", params=_body(params))


class RunEventsNamespace:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http

    def list(self, run_id: str, **params: Any) -> JsonObject:
        return self._http.request(
            "GET", f"/runs/{_enc(run_id)}/events", params=_body(params)
        )

    def iter(self, run_id: str, **params: Any) -> Iterator[JsonObject]:
        return _iter_pages(lambda query: self.list(run_id, **query), params)

class RunTraceNamespace:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http

    def list(self, run_id: str, **params: Any) -> JsonObject:
        return self._http.request(
            "GET", f"/runs/{_enc(run_id)}/trace", params=_body(params)
        )

    def iter(self, run_id: str, **params: Any) -> Iterator[JsonObject]:
        return _iter_pages(lambda query: self.list(run_id, **query), params)

class RunFilesNamespace:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http

    def list(self, run_id: str) -> JsonObject:
        return self._http.request("GET", f"/runs/{_enc(run_id)}/files")


class FilesClient:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http

    def list(self, **params: Any) -> JsonObject:
        return self._http.request("GET", "/files", params=_body(params))

    def iter(self, **params: Any) -> Iterator[JsonObject]:
        return _iter_pages(lambda query: self.list(**query), params)

    def get(self, file_id: str) -> JsonObject:
        return self._http.request("GET", f"/files/{_enc(file_id)}")

    def content(self, file_id: str) -> bytes:
        return self._http.request_bytes("GET", f"/files/{_enc(file_id)}/content")

    def update(self, file_id: str, **request: Any) -> JsonObject:
        return self._http.request("PATCH", f"/files/{_enc(file_id)}", json_body=_body(request))

    def delete(self, file_id: str) -> JsonObject:
        return self._http.request("DELETE", f"/files/{_enc(file_id)}")

    def upload(self, *, file: Any, filename: Optional[str] = None, **fields: Any) -> JsonObject:
        return self._http.multipart(
            "/files",
            fields=_body(fields),
            files=[make_file_part("file", file, filename=filename)],
        )


class NotificationRecipientsClient:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http

    def list(self, **params: Any) -> JsonObject:
        return self._http.request(
            "GET", "/notification-recipients", params=_body(params)
        )

    def iter(self, **params: Any) -> Iterator[JsonObject]:
        return _iter_pages(lambda query: self.list(**query), params)

    def create(self, **request: Any) -> JsonObject:
        return self._http.request(
            "POST", "/notification-recipients", json_body=_body(request)
        )

    def update(self, recipient_id: str, **request: Any) -> JsonObject:
        return self._http.request(
            "PATCH",
            f"/notification-recipients/{_enc(recipient_id)}",
            json_body=_merge_patch(request),
        )

    def delete(self, recipient_id: str) -> JsonObject:
        return self._http.request(
            "DELETE", f"/notification-recipients/{_enc(recipient_id)}"
        )


class ConversationsClient:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http
        self.messages = ConversationMessagesNamespace(http)

    def list(self, **params: Any) -> JsonObject:
        return self._http.request("GET", "/conversations", params=_body(params))

    def iter(self, **params: Any) -> Iterator[JsonObject]:
        return _iter_pages(lambda query: self.list(**query), params)

    def create(self, **request: Any) -> JsonObject:
        return self._http.request("POST", "/conversations", json_body=_body(request))

    def get(self, conversation_id: str, **params: Any) -> JsonObject:
        return self._http.request(
            "GET", f"/conversations/{_enc(conversation_id)}", params=_body(params)
        )

    def update(self, conversation_id: str, **request: Any) -> JsonObject:
        return self._http.request(
            "PATCH",
            f"/conversations/{_enc(conversation_id)}",
            json_body=_merge_patch(request),
        )

    def cancel(self, conversation_id: str) -> JsonObject:
        return self._http.request(
            "POST", f"/conversations/{_enc(conversation_id)}/cancel"
        )

    def stream_url(self, conversation_id: str, **params: Any) -> str:
        return _stream_url(
            self._http.base_url,
            f"/conversations/{_enc(conversation_id)}/stream",
            _body(params),
        )

    def stream(self, conversation_id: str, **params: Any) -> Iterator[JsonObject]:
        return self._http.stream_sse(
            f"/conversations/{_enc(conversation_id)}/stream",
            params=_body(params),
        )


class ConversationMessagesNamespace:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http

    def create(
        self,
        conversation_id: str,
        *,
        idempotency_key: Optional[str] = None,
        **request: Any,
    ) -> JsonObject:
        return self._http.request(
            "POST",
            f"/conversations/{_enc(conversation_id)}/messages",
            json_body=_body(request),
            idempotency_key=idempotency_key,
        )


class BrowserExtensionsClient:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http

    def list(self, **params: Any) -> JsonObject:
        return self._http.request("GET", "/browser/extensions", params=_body(params))

    def iter(self, **params: Any) -> Iterator[JsonObject]:
        return _iter_pages(lambda query: self.list(**query), params)

    def get(self, extension_id: str) -> JsonObject:
        return self._http.request("GET", f"/browser/extensions/{_enc(extension_id)}")

    def update(self, extension_id: str, **request: Any) -> JsonObject:
        return self._http.request(
            "PATCH", f"/browser/extensions/{_enc(extension_id)}", json_body=_body(request)
        )

    def delete(self, extension_id: str) -> JsonObject:
        return self._http.request("DELETE", f"/browser/extensions/{_enc(extension_id)}")

    def upload(self, *, file: Any, filename: Optional[str] = None, **fields: Any) -> JsonObject:
        return self._http.multipart(
            "/browser/extensions",
            fields=_body(fields),
            files=[make_file_part("file", file, filename=filename)],
        )

    def import_url(self, url: str, **request: Any) -> JsonObject:
        return self._http.request(
            "POST",
            "/browser/extensions",
            json_body={**_body(request), "url": url},
        )


class ProxiesClient:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http
        self.geo = ProxyGeoNamespace(http)
        self.locations = ProxyLocationsNamespace(http)
        self.pools = ProxyPoolsNamespace(http)

    def list(self, **params: Any) -> JsonObject:
        return self._http.request("GET", "/proxies", params=_body(params))

    def iter(self, **params: Any) -> Iterator[JsonObject]:
        return _iter_pages(lambda query: self.list(**query), params)

    def create(self, **request: Any) -> JsonObject:
        return self._http.request("POST", "/proxies", json_body=_body(request))

    def get(self, proxy_id: str) -> JsonObject:
        return self._http.request("GET", f"/proxies/{_enc(proxy_id)}")

    def update(self, proxy_id: str, **request: Any) -> JsonObject:
        return self._http.request(
            "PATCH", f"/proxies/{_enc(proxy_id)}", json_body=_body(request)
        )

    def delete(self, proxy_id: str) -> JsonObject:
        return self._http.request("DELETE", f"/proxies/{_enc(proxy_id)}")

    def test(self, proxy_id: str) -> JsonObject:
        return self._http.request("POST", f"/proxies/{_enc(proxy_id)}/test")


class ProxyGeoNamespace:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http

    def list(self, **params: Any) -> JsonObject:
        return self._http.request("GET", "/proxies/geo", params=_body(params))

    def iter(self, **params: Any) -> Iterator[JsonObject]:
        return _iter_pages(lambda query: self.list(**query), params)


class ProxyLocationsNamespace:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http

    def list(self, **params: Any) -> JsonObject:
        return self._http.request("GET", "/proxies/locations", params=_body(params))

    def iter(self, **params: Any) -> Iterator[JsonObject]:
        return _iter_pages(lambda query: self.list(**query), params)


class ProxyPoolsNamespace:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http

    def list(self, **params: Any) -> JsonObject:
        return self._http.request("GET", "/proxies/pools", params=_body(params))

    def get(self, pool_id: str) -> JsonObject:
        return self._http.request("GET", f"/proxies/pools/{_enc(pool_id)}")


class ToolsClient(BuiltinToolsClient):
    def __init__(self, http: V1HttpClient) -> None:
        super().__init__(http)

    def list(self, **params: Any) -> JsonObject:
        return self._http.request("GET", "/tools", params=_body(params))

    def iter(self, **params: Any) -> Iterator[JsonObject]:
        return _iter_pages(lambda query: self.list(**query), params)

    def create(self, **request: Any) -> JsonObject:
        return self._http.request("POST", "/tools", json_body=_body(request))

    def get(self, tool_ref: str) -> JsonObject:
        return self._http.request("GET", f"/tools/{_enc(tool_ref)}")

    def update(self, tool_ref: str, **request: Any) -> JsonObject:
        return self._http.request("PATCH", f"/tools/{_enc(tool_ref)}", json_body=_body(request))

    def delete(self, tool_ref: str) -> JsonObject:
        return self._http.request("DELETE", f"/tools/{_enc(tool_ref)}")

class AiModelsClient:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http

    def list(self, **params: Any) -> JsonObject:
        return self._http.request("GET", "/ai/models", params=_body(params))


class AiCredentialsClient:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http

    def list(self, **params: Any) -> JsonObject:
        return self._http.request("GET", "/ai/credentials", params=_body(params))

    def iter(self, **params: Any) -> Iterator[JsonObject]:
        return _iter_pages(lambda query: self.list(**query), params)

    def create(self, **request: Any) -> JsonObject:
        return self._http.request("POST", "/ai/credentials", json_body=_body(request))

    def get(self, credential_id: str) -> JsonObject:
        return self._http.request("GET", f"/ai/credentials/{_enc(credential_id)}")

    def update(self, credential_id: str, **request: Any) -> JsonObject:
        return self._http.request(
            "PATCH", f"/ai/credentials/{_enc(credential_id)}", json_body=_body(request)
        )

    def delete(self, credential_id: str) -> JsonObject:
        return self._http.request("DELETE", f"/ai/credentials/{_enc(credential_id)}")

    def test(self, credential_id: str) -> JsonObject:
        return self._http.request("POST", f"/ai/credentials/{_enc(credential_id)}/test")


class AiClient:
    def __init__(self, http: V1HttpClient) -> None:
        self.models = AiModelsClient(http)
        self.credentials = AiCredentialsClient(http)


class ToolsetsClient:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http

    def list(self, **params: Any) -> JsonObject:
        return self._http.request("GET", "/toolsets", params=_body(params))

    def iter(self, **params: Any) -> Iterator[JsonObject]:
        return _iter_pages(lambda query: self.list(**query), params)

    def create(self, **request: Any) -> JsonObject:
        return self._http.request("POST", "/toolsets", json_body=_body(request))

    def get(self, toolset_id: str) -> JsonObject:
        return self._http.request("GET", f"/toolsets/{_enc(toolset_id)}")

    def update(self, toolset_id: str, **request: Any) -> JsonObject:
        return self._http.request(
            "PATCH", f"/toolsets/{_enc(toolset_id)}", json_body=_body(request)
        )

    def delete(self, toolset_id: str) -> JsonObject:
        return self._http.request("DELETE", f"/toolsets/{_enc(toolset_id)}")


class ToolCallsClient:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http

    def list(self, **params: Any) -> JsonObject:
        return self._http.request("GET", "/tool-calls", params=_body(params))

    def iter(self, **params: Any) -> Iterator[JsonObject]:
        return _iter_pages(lambda query: self.list(**query), params)

    def get(self, tool_call_id: str) -> JsonObject:
        return self._http.request("GET", f"/tool-calls/{_enc(tool_call_id)}")

    def cancel(self, tool_call_id: str) -> JsonObject:
        return self._http.request("POST", f"/tool-calls/{_enc(tool_call_id)}/cancel")

    def respond(self, tool_call_id: str, response: Any) -> JsonObject:
        return self._http.request(
            "POST",
            f"/tool-calls/{_enc(tool_call_id)}/respond",
            json_body=response,
        )

    def result(self, tool_call_id: str, **params: Any) -> Any:
        return self._http.request(
            "GET",
            f"/tool-calls/{_enc(tool_call_id)}/result",
            params=_body(params),
        )


class AccountClient:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http
        self.api_keys = ApiKeysClient(http)
        self.notification_recipients = NotificationRecipientsClient(http)
        self.subaccounts = SubaccountsClient(http)
        self.usage = UsageClient(http)

    def get(self) -> JsonObject:
        return self._http.request("GET", "/account")

    def update(
        self,
        *,
        branding: Mapping[str, Any] | None,
        dry_run: bool = False,
    ) -> JsonObject:
        body = {
            "branding": None if branding is None else _merge_patch(branding),
        }
        return self._http.request(
            "PATCH",
            "/account",
            params={"dryRun": True} if dry_run else None,
            json_body=body,
        )


class ViewsClient:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http

    def list(self, **params: Any) -> JsonObject:
        return self._http.request("GET", "/views", params=_body(params))

    def iter(self, **params: Any) -> Iterator[JsonObject]:
        return _iter_pages(lambda query: self.list(**query), params)

    def create(
        self,
        *,
        scope: Mapping[str, Any],
        components: Mapping[str, Any] | None = None,
        presentation: Mapping[str, Any] | None = None,
        expires_in_seconds: int | None = None,
    ) -> JsonObject:
        body: JsonObject = {"scope": _body(scope)}
        if components is not None:
            body["components"] = _body(components)
        if presentation is not None:
            body["presentation"] = _body(presentation)
        if expires_in_seconds is not None:
            body["expiresInSeconds"] = expires_in_seconds
        return self._http.request("POST", "/views", json_body=body)

    def get(self, view_id: str) -> JsonObject:
        return self._http.request("GET", f"/views/{_enc(view_id)}")

    def delete(self, view_id: str) -> JsonObject:
        return self._http.request("DELETE", f"/views/{_enc(view_id)}")


class WebhookDeliveriesNamespace:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http

    def list(self, webhook_id: str, **params: Any) -> JsonObject:
        return self._http.request(
            "GET",
            f"/webhooks/{_enc(webhook_id)}/deliveries",
            params=_body(params),
        )

    def iter(self, webhook_id: str, **params: Any) -> Iterator[JsonObject]:
        return _iter_pages(lambda query: self.list(webhook_id, **query), params)

    def redeliver(self, webhook_id: str, delivery_id: str) -> JsonObject:
        return self._http.request(
            "POST",
            f"/webhooks/{_enc(webhook_id)}/deliveries/{_enc(delivery_id)}/redeliver",
        )


class WebhooksClient:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http
        self.deliveries = WebhookDeliveriesNamespace(http)

    def list(self, **params: Any) -> JsonObject:
        return self._http.request("GET", "/webhooks", params=_body(params))

    def iter(self, **params: Any) -> Iterator[JsonObject]:
        return _iter_pages(lambda query: self.list(**query), params)

    def create(self, **request: Any) -> JsonObject:
        return self._http.request("POST", "/webhooks", json_body=_body(request))

    def get(self, webhook_id: str) -> JsonObject:
        return self._http.request("GET", f"/webhooks/{_enc(webhook_id)}")

    def update(self, webhook_id: str, **request: Any) -> JsonObject:
        return self._http.request(
            "PATCH",
            f"/webhooks/{_enc(webhook_id)}",
            json_body=_merge_patch(request),
        )

    def delete(self, webhook_id: str) -> JsonObject:
        return self._http.request("DELETE", f"/webhooks/{_enc(webhook_id)}")

    def rotate_secret(self, webhook_id: str) -> JsonObject:
        return self._http.request("POST", f"/webhooks/{_enc(webhook_id)}/rotate-secret")

    def test(self, webhook_id: str) -> JsonObject:
        return self._http.request("POST", f"/webhooks/{_enc(webhook_id)}/test")


class AuthClient:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http

    def whoami(self) -> JsonObject:
        return self._http.request("GET", "/auth/whoami")


class ApiKeysClient:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http

    def list(self, **params: Any) -> JsonObject:
        return self._http.request("GET", "/api-keys", params=_body(params))

    def iter(self, **params: Any) -> Iterator[JsonObject]:
        return _iter_pages(lambda query: self.list(**query), params)

    def create(self, **request: Any) -> JsonObject:
        return self._http.request("POST", "/api-keys", json_body=_body(request))

    def delete(self, key_id: str) -> JsonObject:
        return self._http.request("DELETE", f"/api-keys/{_enc(key_id)}")


class SubaccountsClient:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http
        self.usage = SubaccountUsageNamespace(http)

    def list(self, **params: Any) -> JsonObject:
        return self._http.request("GET", "/subaccounts", params=_body(params))

    def iter(self, **params: Any) -> Iterator[JsonObject]:
        return _iter_pages(lambda query: self.list(**query), params)

    def create(self, **request: Any) -> JsonObject:
        return self._http.request("POST", "/subaccounts", json_body=_body(request))

    def get(self, subaccount_id: str, **params: Any) -> JsonObject:
        return self._http.request(
            "GET", f"/subaccounts/{_enc(subaccount_id)}", params=_body(params)
        )

    def update(self, subaccount_id: str, **request: Any) -> JsonObject:
        return self._http.request(
            "PATCH", f"/subaccounts/{_enc(subaccount_id)}", json_body=_body(request)
        )

    def archive(self, subaccount_id: str) -> JsonObject:
        return self._http.request("POST", f"/subaccounts/{_enc(subaccount_id)}/archive")


class SubaccountUsageNamespace:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http

    def list(self, **params: Any) -> JsonObject:
        return self._http.request("GET", "/subaccounts/usage", params=_body(params))

    def get(self, subaccount_id: str) -> JsonObject:
        return self._http.request(
            "GET",
            f"/subaccounts/{_enc(subaccount_id)}",
            params={"include": "usage"},
        )


class UsageClient:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http

    def get(self) -> JsonObject:
        return self._http.request("GET", "/usage")


class HelpClient:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http

    def get(self, **params: Any) -> JsonObject:
        return self._http.request("GET", "/help", params=_body(params))
