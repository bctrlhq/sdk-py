"""Resource namespace clients for the BCTRL public v1 API."""

from __future__ import annotations

import time
from typing import Any, Iterator, Mapping, Optional
from urllib.parse import quote, urlencode

from .http import V1HttpClient, make_file_part
from .runtime_context import StartedRuntime
from .schemas import PydanticModel, parse_output, to_output_schema

JsonObject = dict[str, Any]


def _enc(value: str) -> str:
    return quote(value, safe="")


def _body(values: Mapping[str, Any]) -> JsonObject:
    return {_wire_key(key): value for key, value in values.items() if value is not None}


def _wire_key(key: str) -> str:
    if "_" not in key:
        return key
    head, *tail = key.split("_")
    return head + "".join(part[:1].upper() + part[1:] for part in tail if part)


def _prepare_invocation(
    request: Mapping[str, Any],
    *,
    output_model: Optional[PydanticModel] = None,
) -> JsonObject:
    body = _body(request)
    if "outputModel" in body:
        raise TypeError("Pass output_model as a keyword argument")
    if "schema" in body or "outputSchema" in body:
        raise TypeError("Use output_model=YourPydanticModel for invocation output schemas")
    if output_model is not None:
        body["outputSchema"] = to_output_schema(output_model, label="Invocation output_model")
    return body


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
        self.environment = SpaceEnvironmentNamespace(http)
        self.runtimes = SpaceRuntimesNamespace(http)

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


class SpaceEnvironmentNamespace:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http

    def get(self, space_id: str) -> JsonObject:
        return self._http.request("GET", f"/spaces/{_enc(space_id)}/environment")

    def update(self, space_id: str, **request: Any) -> JsonObject:
        return self._http.request(
            "PATCH", f"/spaces/{_enc(space_id)}/environment", json_body=_body(request)
        )


class SpaceRuntimesNamespace:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http

    def create(self, space_id: str, **request: Any) -> JsonObject:
        return self._http.request(
            "POST", "/runtimes", json_body={**_body(request), "spaceId": space_id}
        )


class RuntimesClient:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http
        self.files = RuntimeFilesNamespace(http)
        self.runs = RuntimeRunsNamespace(http)
        self.invocations = RuntimeInvocationsNamespace(http)
        self.targets = RuntimeTargetsNamespace(http)

    def list(self, **params: Any) -> JsonObject:
        return self._http.request("GET", "/runtimes", params=_body(params))

    def iter(self, **params: Any) -> Iterator[JsonObject]:
        return _iter_pages(lambda query: self.list(**query), params)

    def create(self, **request: Any) -> JsonObject:
        return self._http.request("POST", "/runtimes", json_body=_body(request))

    def get(self, runtime_id: str) -> JsonObject:
        return self._http.request("GET", f"/runtimes/{_enc(runtime_id)}")

    def update(self, runtime_id: str, **request: Any) -> JsonObject:
        return self._http.request(
            "PATCH", f"/runtimes/{_enc(runtime_id)}", json_body=_body(request)
        )

    def delete(self, runtime_id: str) -> JsonObject:
        return self._http.request("DELETE", f"/runtimes/{_enc(runtime_id)}")

    def start(self, runtime_id: str, *, idempotency_key: Optional[str] = None) -> JsonObject:
        return self._http.request(
            "POST", f"/runtimes/{_enc(runtime_id)}/start", idempotency_key=idempotency_key
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
        return StartedRuntime(
            runtimes=self,
            request=body,
            idempotency_key=idempotency_key,
        )


class RuntimeTargetsNamespace:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http

    def list(self, runtime_id: str) -> JsonObject:
        return self._http.request("GET", f"/runtimes/{_enc(runtime_id)}/targets")

    def create(self, runtime_id: str, **request: Any) -> JsonObject:
        return self._http.request(
            "POST", f"/runtimes/{_enc(runtime_id)}/targets", json_body=_body(request)
        )

    def get(self, runtime_id: str, target_id: str) -> JsonObject:
        return self._http.request(
            "GET", f"/runtimes/{_enc(runtime_id)}/targets/{_enc(target_id)}"
        )

    def activate(self, runtime_id: str, target_id: str) -> JsonObject:
        return self._http.request(
            "POST", f"/runtimes/{_enc(runtime_id)}/targets/{_enc(target_id)}/activate"
        )

    def delete(self, runtime_id: str, target_id: str) -> JsonObject:
        return self._http.request(
            "DELETE", f"/runtimes/{_enc(runtime_id)}/targets/{_enc(target_id)}"
        )


class RuntimeRunsNamespace:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http

    def list(self, runtime_id: str, **params: Any) -> JsonObject:
        return self._http.request(
            "GET", f"/runtimes/{_enc(runtime_id)}/runs", params=_body(params)
        )

    def iter(self, runtime_id: str, **params: Any) -> Iterator[JsonObject]:
        return _iter_pages(lambda query: self.list(runtime_id, **query), params)


class RuntimeFilesNamespace:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http

    def list(self, runtime_id: str, **params: Any) -> JsonObject:
        return self._http.request(
            "GET", f"/runtimes/{_enc(runtime_id)}/files", params=_body(params)
        )

    def iter(self, runtime_id: str, **params: Any) -> Iterator[JsonObject]:
        return _iter_pages(lambda query: self.list(runtime_id, **query), params)

    def stage(self, runtime_id: str, *, file_id: str, **request: Any) -> JsonObject:
        return self._http.request(
            "POST",
            f"/runtimes/{_enc(runtime_id)}/files/stage",
            json_body={**_body(request), "fileId": file_id},
        )

    def collect(self, runtime_id: str, *, runtime_path: str, **request: Any) -> JsonObject:
        return self._http.request(
            "POST",
            f"/runtimes/{_enc(runtime_id)}/files/collect",
            json_body={**_body(request), "runtimePath": runtime_path},
        )

    def upload(
        self,
        runtime_id: str,
        *,
        file: Any,
        filename: Optional[str] = None,
        **fields: Any,
    ) -> JsonObject:
        return self._http.multipart(
            f"/runtimes/{_enc(runtime_id)}/files/upload",
            fields=_body(fields),
            files=[make_file_part("file", file, filename=filename)],
        )


class RuntimeInvocationsNamespace:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http
        self.stagehand = StagehandInvocationsNamespace(self)
        self.browser_use = BrowserUseInvocationsNamespace(self)

    def create(
        self,
        runtime_id: str,
        request: Optional[Mapping[str, Any]] = None,
        *,
        idempotency_key: Optional[str] = None,
        output_model: Optional[PydanticModel] = None,
        **kwargs: Any,
    ) -> JsonObject:
        request_body = {**dict(request or {}), **kwargs}
        body = _prepare_invocation(request_body, output_model=output_model)
        return self._http.request(
            "POST",
            f"/runtimes/{_enc(runtime_id)}/invocations",
            json_body=body,
            idempotency_key=idempotency_key,
        )

    def wait(self, runtime_id: str, invocation_id: str, **request: Any) -> JsonObject:
        return self._http.request(
            "POST",
            f"/runtimes/{_enc(runtime_id)}/invocations/{_enc(invocation_id)}/wait",
            json_body=_body(request),
        )

    def cancel(self, runtime_id: str, invocation_id: str) -> JsonObject:
        return self._http.request(
            "POST", f"/runtimes/{_enc(runtime_id)}/invocations/{_enc(invocation_id)}/cancel"
        )

    def create_and_wait(
        self,
        runtime_id: str,
        request: Optional[Mapping[str, Any]] = None,
        *,
        timeout: Optional[float] = None,
        poll_timeout_ms: Optional[int] = None,
        idempotency_key: Optional[str] = None,
        output_model: Optional[PydanticModel] = None,
        **kwargs: Any,
    ) -> JsonObject:
        invocation = self.create(
            runtime_id,
            request,
            idempotency_key=idempotency_key,
            output_model=output_model,
            **kwargs,
        )
        deadline = None if timeout is None else time.monotonic() + timeout
        while True:
            remaining_ms = (
                None
                if deadline is None
                else max(1, int((deadline - time.monotonic()) * 1000))
            )
            if deadline is not None and remaining_ms <= 1:
                raise TimeoutError(f"Invocation {invocation['id']} did not finish before timeout")
            timeout_ms = (
                poll_timeout_ms
                if remaining_ms is None
                else min(poll_timeout_ms or remaining_ms, remaining_ms)
            )
            result = self.wait(runtime_id, invocation["id"], timeoutMs=timeout_ms)
            if result.get("waitStatus") == "completed":
                if (
                    output_model is not None
                    and result.get("status") == "succeeded"
                    and result.get("output") is not None
                ):
                    result = dict(result)
                    result["parsed_output"] = parse_output(output_model, result["output"])
                return result
            sleep_ms = result.get("retryAfterMs") or 1000
            if deadline is not None:
                sleep_ms = min(sleep_ms, max(0, int((deadline - time.monotonic()) * 1000)))
            time.sleep(sleep_ms / 1000)


class StagehandInvocationsNamespace:
    def __init__(self, invocations: RuntimeInvocationsNamespace) -> None:
        self._invocations = invocations

    def act(self, runtime_id: str, instruction: str, **kwargs: Any) -> JsonObject:
        return self._invocations.create(runtime_id, action="act", instruction=instruction, **kwargs)

    def observe(self, runtime_id: str, instruction: str, **kwargs: Any) -> JsonObject:
        return self._invocations.create(
            runtime_id, action="observe", instruction=instruction, **kwargs
        )

    def extract(
        self,
        runtime_id: str,
        instruction: Optional[str] = None,
        **kwargs: Any,
    ) -> JsonObject:
        return self._invocations.create(
            runtime_id, action="extract", instruction=instruction, **kwargs
        )

    def agent(self, runtime_id: str, instruction: str, **kwargs: Any) -> JsonObject:
        return self._invocations.create(
            runtime_id, action="stagehandAgent", instruction=instruction, **kwargs
        )


class BrowserUseInvocationsNamespace:
    def __init__(self, invocations: RuntimeInvocationsNamespace) -> None:
        self._invocations = invocations

    def agent(self, runtime_id: str, instruction: str, **kwargs: Any) -> JsonObject:
        return self._invocations.create(
            runtime_id, action="browserUse", instruction=instruction, **kwargs
        )


class RunsClient:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http
        self.events = RunEventsNamespace(http)
        self.activity = RunActivityNamespace(http)
        self.files = RunFilesNamespace(http)
        self.invocations = RunInvocationsNamespace(http)

    def list(self, **params: Any) -> JsonObject:
        return self._http.request("GET", "/runs", params=_body(params))

    def iter(self, **params: Any) -> Iterator[JsonObject]:
        return _iter_pages(lambda query: self.list(**query), params)

    def get(self, run_id: str) -> JsonObject:
        return self._http.request("GET", f"/runs/{_enc(run_id)}")

    def wait(self, run_id: str, **request: Any) -> JsonObject:
        return self._http.request("POST", f"/runs/{_enc(run_id)}/wait", json_body=_body(request))

    def usage(self, run_id: str) -> JsonObject:
        return self._http.request("GET", f"/runs/{_enc(run_id)}/usage")

    def live(self, run_id: str, **request: Any) -> JsonObject:
        return self._http.request(
            "POST", f"/runs/{_enc(run_id)}/live", json_body=_body(request)
        )

    def recording(self, run_id: str, **request: Any) -> JsonObject:
        return self._http.request(
            "POST", f"/runs/{_enc(run_id)}/recording", json_body=_body(request)
        )


class RunEventsNamespace:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http

    def list(self, run_id: str, **params: Any) -> JsonObject:
        return self._http.request(
            "GET", f"/runs/{_enc(run_id)}/events", params=_body(params)
        )

    def iter(self, run_id: str, **params: Any) -> Iterator[JsonObject]:
        return _iter_pages(lambda query: self.list(run_id, **query), params)

    def stream_url(self, run_id: str, **params: Any) -> str:
        return _stream_url(
            self._http.base_url,
            f"/runs/{_enc(run_id)}/events/stream",
            _body(params),
        )

    def stream(self, run_id: str, **params: Any) -> Iterator[JsonObject]:
        return self._http.stream_sse(
            f"/runs/{_enc(run_id)}/events/stream",
            params=_body(params),
        )


class RunActivityNamespace:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http

    def list(self, run_id: str, **params: Any) -> JsonObject:
        return self._http.request(
            "GET", f"/runs/{_enc(run_id)}/activity", params=_body(params)
        )

    def iter(self, run_id: str, **params: Any) -> Iterator[JsonObject]:
        return _iter_pages(lambda query: self.list(run_id, **query), params)

    def stream_url(self, run_id: str, **params: Any) -> str:
        return _stream_url(
            self._http.base_url,
            f"/runs/{_enc(run_id)}/activity/stream",
            _body(params),
        )

    def stream(self, run_id: str, **params: Any) -> Iterator[JsonObject]:
        return self._http.stream_sse(
            f"/runs/{_enc(run_id)}/activity/stream",
            params=_body(params),
        )


class RunFilesNamespace:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http

    def list(self, run_id: str, **params: Any) -> JsonObject:
        return self._http.request(
            "GET", f"/runs/{_enc(run_id)}/files", params=_body(params)
        )

    def iter(self, run_id: str, **params: Any) -> Iterator[JsonObject]:
        return _iter_pages(lambda query: self.list(run_id, **query), params)

    def export(self, run_id: str, **request: Any) -> JsonObject:
        return self._http.request(
            "POST", f"/runs/{_enc(run_id)}/files/export", json_body=_body(request)
        )


class RunInvocationsNamespace:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http

    def list(self, run_id: str, **params: Any) -> JsonObject:
        return self._http.request(
            "GET", f"/runs/{_enc(run_id)}/invocations", params=_body(params)
        )

    def iter(self, run_id: str, **params: Any) -> Iterator[JsonObject]:
        return _iter_pages(lambda query: self.list(run_id, **query), params)

    def get(self, run_id: str, invocation_id: str) -> JsonObject:
        return self._http.request(
            "GET", f"/runs/{_enc(run_id)}/invocations/{_enc(invocation_id)}"
        )


class FilesClient:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http

    def list(self, **params: Any) -> JsonObject:
        return self._http.request("GET", "/files", params=_body(params))

    def iter(self, **params: Any) -> Iterator[JsonObject]:
        return _iter_pages(lambda query: self.list(**query), params)

    def get(self, file_id: str) -> JsonObject:
        return self._http.request("GET", f"/files/{_enc(file_id)}")

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


class BrowserExtensionsClient:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http

    def list(self, **params: Any) -> JsonObject:
        return self._http.request("GET", "/browser-extensions", params=_body(params))

    def iter(self, **params: Any) -> Iterator[JsonObject]:
        return _iter_pages(lambda query: self.list(**query), params)

    def get(self, extension_id: str) -> JsonObject:
        return self._http.request("GET", f"/browser-extensions/{_enc(extension_id)}")

    def update(self, extension_id: str, **request: Any) -> JsonObject:
        return self._http.request(
            "PATCH", f"/browser-extensions/{_enc(extension_id)}", json_body=_body(request)
        )

    def delete(self, extension_id: str) -> JsonObject:
        return self._http.request("DELETE", f"/browser-extensions/{_enc(extension_id)}")

    def upload(self, *, file: Any, filename: Optional[str] = None, **fields: Any) -> JsonObject:
        return self._http.multipart(
            "/browser-extensions/upload",
            fields=_body(fields),
            files=[make_file_part("file", file, filename=filename)],
        )

    def import_url(self, url: str, **request: Any) -> JsonObject:
        return self._http.request(
            "POST",
            "/browser-extensions/import",
            json_body={**_body(request), "url": url},
        )


class ProxiesClient:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http
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


class ProxyPoolsNamespace:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http

    def list(self, **params: Any) -> JsonObject:
        return self._http.request("GET", "/proxies/pools", params=_body(params))

    def get(self, pool_id: str) -> JsonObject:
        return self._http.request("GET", f"/proxies/pools/{_enc(pool_id)}")


class ToolsClient:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http

    def list(self, **params: Any) -> JsonObject:
        return self._http.request("GET", "/tools", params=_body(params))

    def iter(self, **params: Any) -> Iterator[JsonObject]:
        return _iter_pages(lambda query: self.list(**query), params)

    def create(self, **request: Any) -> JsonObject:
        return self._http.request("POST", "/tools", json_body=_body(request))

    def get(self, tool_id: str) -> JsonObject:
        return self._http.request("GET", f"/tools/{_enc(tool_id)}")

    def update(self, tool_id: str, **request: Any) -> JsonObject:
        return self._http.request("PATCH", f"/tools/{_enc(tool_id)}", json_body=_body(request))

    def delete(self, tool_id: str) -> JsonObject:
        return self._http.request("DELETE", f"/tools/{_enc(tool_id)}")

    def test(self, tool_id: str, **request: Any) -> JsonObject:
        return self._http.request("POST", f"/tools/{_enc(tool_id)}/test", json_body=_body(request))

    def list_versions(self, tool_id: str, **params: Any) -> JsonObject:
        return self._http.request(
            "GET", f"/tools/{_enc(tool_id)}/versions", params=_body(params)
        )

    def create_version(self, tool_id: str, **request: Any) -> JsonObject:
        return self._http.request(
            "POST", f"/tools/{_enc(tool_id)}/versions", json_body=_body(request)
        )

    def get_version(self, tool_id: str, version_id: str) -> JsonObject:
        return self._http.request("GET", f"/tools/{_enc(tool_id)}/versions/{_enc(version_id)}")

    def promote_version(self, tool_id: str, version_id: str) -> JsonObject:
        return self._http.request(
            "POST", f"/tools/{_enc(tool_id)}/versions/{_enc(version_id)}/promote"
        )


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


class VaultClient:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http

    def list(self, **params: Any) -> JsonObject:
        return self._http.request("GET", "/vault/secrets", params=_body(params))

    def iter(self, **params: Any) -> Iterator[JsonObject]:
        return _iter_pages(lambda query: self.list(**query), params)

    def get(self, key: str) -> JsonObject:
        return self._http.request("GET", f"/vault/secrets/{_enc(key)}")

    def value(self, key: str) -> JsonObject:
        return self._http.request("GET", f"/vault/secrets/{_enc(key)}/value")

    def upsert(self, key: str, **request: Any) -> JsonObject:
        return self._http.request("PUT", f"/vault/secrets/{_enc(key)}", json_body=_body(request))

    def update(self, key: str, **request: Any) -> JsonObject:
        return self._http.request(
            "PATCH", f"/vault/secrets/{_enc(key)}", json_body=_body(request)
        )

    def totp(self, key: str) -> JsonObject:
        return self._http.request("GET", f"/vault/secrets/{_enc(key)}/totp")

    def delete(self, key: str) -> JsonObject:
        return self._http.request("DELETE", f"/vault/secrets/{_enc(key)}")


class AccountClient:
    def __init__(self, http: V1HttpClient) -> None:
        self._http = http
        self.api_keys = ApiKeysClient(http)
        self.subaccounts = SubaccountsClient(http)
        self.usage = UsageClient(http)


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
        return self._http.request("GET", f"/subaccounts/{_enc(subaccount_id)}/usage")


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
