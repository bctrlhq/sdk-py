"""HTTP transport for the BCTRL Python SDK."""

from __future__ import annotations

import json
import mimetypes
import os
import random
import time
import uuid
from dataclasses import dataclass
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any, BinaryIO, Iterable, Iterator, Mapping, Optional
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from .errors import BctrlNetworkError, api_error_for_status
from .version import __version__

BCTRL_PRODUCTION_ORIGIN = "https://api.bctrl.ai"
API_PREFIX = "/v1"
SDK_VERSION = __version__


@dataclass(frozen=True)
class FilePart:
    name: str
    content: bytes
    filename: str
    content_type: str


class V1HttpClient:
    def __init__(
        self,
        *,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: int = 2,
    ) -> None:
        self.api_key = _resolve_api_key(api_key)
        self.base_url = _resolve_base_url(base_url)
        self.timeout = timeout
        self.max_retries = max(0, max_retries)

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Mapping[str, Any]] = None,
        json_body: Any = None,
        headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
        idempotency_key: Optional[str] = None,
    ) -> Any:
        body: Optional[bytes] = None
        request_headers = self._headers(headers, idempotency_key)
        if json_body is not None:
            body = json.dumps(json_body, separators=(",", ":")).encode("utf-8")
            request_headers["content-type"] = "application/json"
        return self._send(
            method,
            path,
            params=params,
            body=body,
            headers=request_headers,
            timeout=timeout,
        )

    def multipart(
        self,
        path: str,
        *,
        fields: Optional[Mapping[str, Any]] = None,
        files: Iterable[FilePart],
        headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
        idempotency_key: Optional[str] = None,
    ) -> Any:
        boundary = f"bctrl-{uuid.uuid4().hex}"
        body = _encode_multipart(boundary, fields or {}, files)
        request_headers = self._headers(headers, idempotency_key)
        request_headers["content-type"] = (
            f"multipart/form-data; boundary={boundary}"
        )
        return self._send("POST", path, body=body, headers=request_headers, timeout=timeout)

    def stream_sse(
        self,
        path: str,
        *,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[dict[str, Any]]:
        request_headers = self._headers({"accept": "text/event-stream", **(headers or {})}, None)
        url = _url(self.base_url, path, params)
        request = Request(url, headers=request_headers, method="GET")
        try:
            resolved_timeout = self.timeout if timeout is None else timeout
            with urlopen(request, timeout=resolved_timeout) as response:
                yield from _iter_sse_response(response)
        except HTTPError as error:
            raw = error.read()
            parsed = _decode_response(raw, error.headers.get("content-type"))
            message, code, request_id = _error_fields(parsed, error)
            raise api_error_for_status(
                error.code,
                message,
                code=code,
                request_id=request_id,
                body=parsed,
            ) from None
        except (TimeoutError, URLError, OSError) as error:
            raise BctrlNetworkError(str(error), context={"cause": repr(error)}) from error

    def _headers(
        self,
        headers: Optional[Mapping[str, str]],
        idempotency_key: Optional[str],
    ) -> dict[str, str]:
        result = {
            "authorization": f"Bearer {self.api_key}",
            "accept": "application/json",
            "user-agent": f"bctrl-python/{SDK_VERSION}",
        }
        if idempotency_key:
            result["idempotency-key"] = idempotency_key
        if headers:
            result.update(headers)
        return result

    def _send(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Mapping[str, Any]] = None,
        body: Optional[bytes] = None,
        headers: Mapping[str, str],
        timeout: Optional[float] = None,
    ) -> Any:
        url = _url(self.base_url, path, params)
        attempts = self.max_retries + 1 if _can_retry_request(method, headers) else 1
        last_error: Optional[BaseException] = None

        for attempt in range(1, attempts + 1):
            request = Request(url, data=body, headers=dict(headers), method=method.upper())
            try:
                resolved_timeout = self.timeout if timeout is None else timeout
                with urlopen(request, timeout=resolved_timeout) as response:
                    raw = response.read()
                    return _decode_response(raw, response.headers.get("content-type"))
            except HTTPError as error:
                raw = error.read()
                parsed = _decode_response(raw, error.headers.get("content-type"))
                if _retryable_status(error.code) and attempt < attempts:
                    time.sleep(_retry_delay(attempt, error.headers.get("retry-after")))
                    continue
                message, code, request_id = _error_fields(parsed, error)
                raise api_error_for_status(
                    error.code,
                    message,
                    code=code,
                    request_id=request_id,
                    body=parsed,
                ) from None
            except (TimeoutError, URLError, OSError) as error:
                last_error = error
                if attempt < attempts:
                    time.sleep(_retry_delay(attempt, None))
                    continue
                raise BctrlNetworkError(str(error), context={"cause": repr(error)}) from error

        raise BctrlNetworkError("Network request failed", context={"cause": repr(last_error)})


def make_file_part(
    name: str,
    file: str | Path | bytes | BinaryIO,
    *,
    filename: Optional[str] = None,
) -> FilePart:
    if isinstance(file, (str, Path)):
        path = Path(file)
        content = path.read_bytes()
        resolved_filename = filename or path.name
    elif isinstance(file, bytes):
        content = file
        resolved_filename = filename or "file"
    else:
        content = file.read()
        resolved_filename = filename or getattr(file, "name", "file")
        resolved_filename = Path(str(resolved_filename)).name
    content_type = mimetypes.guess_type(resolved_filename)[0] or "application/octet-stream"
    return FilePart(
        name=name,
        content=content,
        filename=resolved_filename,
        content_type=content_type,
    )


def _resolve_api_key(api_key: Optional[str]) -> str:
    value = (api_key or os.environ.get("BCTRL_API_KEY") or "").strip()
    if not value:
        raise ValueError("BCTRL_API_KEY is required. Pass api_key or set BCTRL_API_KEY.")
    return value


def _resolve_base_url(base_url: Optional[str]) -> str:
    raw = (
        base_url
        or os.environ.get("BCTRL_BASE_URL")
        or os.environ.get("BCTRL_API_BASE_URL")
        or BCTRL_PRODUCTION_ORIGIN
    ).strip()
    raw = raw.rstrip("/")
    return raw if raw.endswith(API_PREFIX) else f"{raw}{API_PREFIX}"


def _url(base_url: str, path: str, params: Optional[Mapping[str, Any]]) -> str:
    url = f"{base_url}/{path.lstrip('/')}"
    query = _query(params)
    return f"{url}?{query}" if query else url


def _query(params: Optional[Mapping[str, Any]]) -> str:
    if not params:
        return ""
    pairs: list[tuple[str, str]] = []
    for key, value in params.items():
        if value is None:
            continue
        if isinstance(value, (list, tuple)):
            pairs.extend((key, str(item)) for item in value if item is not None)
        elif isinstance(value, dict):
            continue
        else:
            pairs.append((key, str(value)))
    return urlencode(pairs)


def _decode_response(raw: bytes, content_type: Optional[str]) -> Any:
    if not raw:
        return None
    text = raw.decode("utf-8")
    if content_type and "application/json" not in content_type:
        return text
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return text


def _iter_sse_response(response: Any) -> Iterator[dict[str, Any]]:
    event_type: Optional[str] = None
    event_id: Optional[str] = None
    data_lines: list[str] = []

    for raw_line in response:
        line = raw_line.decode("utf-8").rstrip("\r\n")
        if line == "":
            if data_lines:
                yield _sse_event(event_type, event_id, data_lines)
            event_type = None
            event_id = None
            data_lines = []
            continue
        if line.startswith(":"):
            continue
        field, _, value = line.partition(":")
        if value.startswith(" "):
            value = value[1:]
        if field == "event":
            event_type = value
        elif field == "id":
            event_id = value
        elif field == "data":
            data_lines.append(value)

    if data_lines:
        yield _sse_event(event_type, event_id, data_lines)


def _sse_event(
    event_type: Optional[str],
    event_id: Optional[str],
    data_lines: list[str],
) -> dict[str, Any]:
    data_raw = "\n".join(data_lines)
    try:
        data: Any = json.loads(data_raw)
    except json.JSONDecodeError:
        data = data_raw

    event = {"event": event_type or "message", "data": data}
    if event_id is not None:
        event["id"] = event_id
    return event


def _error_fields(parsed: Any, error: HTTPError) -> tuple[str, str, Optional[str]]:
    if isinstance(parsed, dict):
        message = parsed.get("error") if isinstance(parsed.get("error"), str) else error.reason
        code = parsed.get("code") if isinstance(parsed.get("code"), str) else "api.error"
        request_id = parsed.get("requestId") if isinstance(parsed.get("requestId"), str) else None
        return message, code, request_id
    return str(parsed or error.reason), "api.error", error.headers.get("x-request-id")


def _retryable_status(status_code: int) -> bool:
    return status_code in (408, 429) or status_code >= 500


def _can_retry_request(method: str, headers: Mapping[str, str]) -> bool:
    normalized = method.upper()
    if normalized in {"GET", "HEAD", "OPTIONS"}:
        return True
    return any(
        key.lower() == "idempotency-key" and value.strip()
        for key, value in headers.items()
    )


def _retry_delay(attempt: int, retry_after: Optional[str]) -> float:
    if retry_after:
        try:
            return max(0.0, float(retry_after))
        except ValueError:
            try:
                parsed = parsedate_to_datetime(retry_after)
                return max(0.0, parsed.timestamp() - time.time())
            except (TypeError, ValueError, OverflowError):
                pass
    return min(2.0, 0.25 * (2 ** (attempt - 1))) + random.uniform(0, 0.05)


def _encode_multipart(
    boundary: str,
    fields: Mapping[str, Any],
    files: Iterable[FilePart],
) -> bytes:
    chunks: list[bytes] = []
    for key, value in fields.items():
        if value is None:
            continue
        chunks.extend(
            [
                f"--{boundary}\r\n".encode(),
                f'Content-Disposition: form-data; name="{key}"\r\n\r\n'.encode(),
                str(value).encode(),
                b"\r\n",
            ]
        )
    for part in files:
        chunks.extend(
            [
                f"--{boundary}\r\n".encode(),
                (
                    "Content-Disposition: form-data; "
                    f'name="{part.name}"; filename="{part.filename}"\r\n'
                ).encode(),
                f"Content-Type: {part.content_type}\r\n\r\n".encode(),
                part.content,
                b"\r\n",
            ]
        )
    chunks.append(f"--{boundary}--\r\n".encode())
    return b"".join(chunks)
