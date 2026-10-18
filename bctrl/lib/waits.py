"""Read-only polling for generated operation outcomes."""
from __future__ import annotations

import asyncio
import time
from typing import Awaitable, Callable, TypeVar

T = TypeVar("T")
_TERMINAL = frozenset(("succeeded", "failed", "cancelled", "timed_out", "unknown", "awaiting_input", "ended"))


def wait_for(read: Callable[[], T], *, timeout: float = 120, interval: float = 0.25) -> T:
    deadline = time.monotonic() + timeout
    while True:
        result = read()
        if getattr(result, "status", None) in _TERMINAL:
            return result
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise TimeoutError("Timed out waiting for an outcome")
        time.sleep(min(max(0, interval), remaining))


async def async_wait_for(read: Callable[[], Awaitable[T]], *, timeout: float = 120, interval: float = 0.25) -> T:
    deadline = time.monotonic() + timeout
    while True:
        result = await read()
        if getattr(result, "status", None) in _TERMINAL:
            return result
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise TimeoutError("Timed out waiting for an outcome")
        await asyncio.sleep(min(max(0, interval), remaining))
