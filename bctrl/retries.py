"""Retry middleware around Fern's request/stream implementation."""
from __future__ import annotations

import asyncio
import time
import uuid
from typing import Any


def _unknown(value: Any, depth: int = 0) -> bool:
    if depth > 8:
        return False
    if isinstance(value, dict):
        if value.get("status") == "unknown" or value.get("reasonClass") in ("unknown", "outcome_unknown"):
            return True
        return any(_unknown(child, depth + 1) for child in value.values())
    if isinstance(value, list):
        return any(_unknown(child, depth + 1) for child in value)
    return False


def _request(kwargs: dict[str, Any], default: int) -> tuple[dict[str, Any], int]:
    options = dict(kwargs.get("request_options") or {})
    limit = options.get("max_retries", default)
    options["max_retries"] = 0
    headers = dict(kwargs.get("headers") or {})
    if kwargs["method"].upper() not in ("GET", "HEAD", "OPTIONS"):
        combined = {**headers, **options.get("additional_headers", {})}
        if not any(name.lower() == "idempotency-key" and value is not None for name, value in combined.items()):
            headers["Idempotency-Key"] = str(uuid.uuid4())
    return {**kwargs, "headers": headers, "request_options": options}, limit


def _retry(response: Any, kwargs: dict[str, Any], attempt: int, limit: int) -> bool:
    if attempt >= limit or kwargs.get("files") or kwargs.get("content") is not None:
        return False
    if response.status_code not in (408, 429) and response.status_code < 500:
        return False
    try:
        if _unknown(response.json()):
            return False
    except ValueError:
        pass
    return True


def _delay(response: Any, attempt: int) -> float:
    try:
        seconds = float(response.headers.get("Retry-After", "0"))
    except ValueError:
        seconds = 0
    return min(60, seconds if seconds > 0 else 0.25 * 2**attempt)


class SafeHttpClient:
    def __init__(self, delegate: Any, max_retries: int):
        self._delegate = delegate
        self._max_retries = max_retries

    def __getattr__(self, name: str) -> Any:
        return getattr(self._delegate, name)

    def stream(self, *args: Any, **kwargs: Any) -> Any:
        # A stream cannot be replayed safely. Also neutralize per-request Fern retries.
        request, _ = _request(kwargs, self._max_retries)
        return self._delegate.stream(*args, **request)

    def request(self, *args: Any, **kwargs: Any) -> Any:
        request, limit = _request(kwargs, self._max_retries)
        attempt = 0
        while True:
            response = self._delegate.request(*args, **request)
            if not _retry(response, request, attempt, limit):
                return response
            delay = _delay(response, attempt)
            response.close()
            time.sleep(delay)
            attempt += 1


class AsyncSafeHttpClient(SafeHttpClient):
    async def request(self, *args: Any, **kwargs: Any) -> Any:
        request, limit = _request(kwargs, self._max_retries)
        attempt = 0
        while True:
            response = await self._delegate.request(*args, **request)
            if not _retry(response, request, attempt, limit):
                return response
            delay = _delay(response, attempt)
            await response.aclose()
            await asyncio.sleep(delay)
            attempt += 1
