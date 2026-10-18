"""Playwright connections and scoped browser cleanup over generated operations."""
from __future__ import annotations

import asyncio
import json
import time
from contextlib import contextmanager, asynccontextmanager
from typing import Any, Iterator, AsyncIterator, TypeVar

from pydantic import PrivateAttr
from .._generated.browsers.client import BrowsersClient, AsyncBrowsersClient
from .._generated.events.client import EventsClient, AsyncEventsClient
from .._generated.types.browser_resource import BrowserResource
from .._generated.core.pydantic_utilities import parse_obj_as


class BrowserEvents:
    """A browser's Events across its Runs: the one Event log filtered by ``browser``."""

    def __init__(self, events: Any, browser_id: str):
        self._events = events
        self._browser_id = browser_id

    def list(self, **kwargs: Any) -> Any:
        return self._events.list(browser=self._browser_id, **kwargs)

    def stream(self, **kwargs: Any) -> Any:
        return self._events.stream(browser=self._browser_id, **kwargs)


def _cdp_url(browser: BrowserResource) -> str | None:
    """The CDP URL once the browser's Run is active; raises if the Run ended instead."""
    run = browser.current_run
    if run is None:
        return None
    if run.status in ("failed", "ended"):
        raise RuntimeError(f"Browser Run {run.status}: {run.end_reason}")
    return run.connections.cdp_url if run.status == "active" and run.connections else None


def _wait_seconds(deadline: float) -> int:
    return min(60, max(1, int(deadline - time.monotonic())))


class _BrowserHandle(BrowserResource):
    _client: Any = PrivateAttr()

    @property
    def events(self) -> BrowserEvents:
        return BrowserEvents(self._client._events_client(), self.id)


class Browser(_BrowserHandle):
    def wait_until_ready(self, *, timeout: float = 120) -> Browser:
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            browser: Browser = self._client.get(self.id, wait=_wait_seconds(deadline))
            if _cdp_url(browser):
                return browser
            time.sleep(0.25)
        raise TimeoutError("Timed out waiting for browser connections")

    def connect(self, playwright: Any, *, timeout: float = 120) -> Any:
        return playwright.chromium.connect_over_cdp(_cdp_url(self.wait_until_ready(timeout=timeout)))


class AsyncBrowser(_BrowserHandle):
    async def wait_until_ready(self, *, timeout: float = 120) -> AsyncBrowser:
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            browser: AsyncBrowser = await self._client.get(self.id, wait=_wait_seconds(deadline))
            if _cdp_url(browser):
                return browser
            await asyncio.sleep(0.25)
        raise TimeoutError("Timed out waiting for browser connections")

    async def connect(self, playwright: Any, *, timeout: float = 120) -> Any:
        return await playwright.chromium.connect_over_cdp(_cdp_url(await self.wait_until_ready(timeout=timeout)))


class FetchStreamResponse:
    """The site's response as the browser received it: ``status`` and ``headers`` are the upstream's, not the API
    call's. Iterating it yields the body in byte chunks as they arrive, once; use it as a context manager (or call
    ``close``) to stop early."""

    def __init__(self, context: Any, response: Any):
        self._context: Any = context
        self._response = response
        headers = response.headers
        self.status: int = int(headers.get("bctrl-fetch-status", "0"))
        self.headers: dict[str, str] = json.loads(headers.get("bctrl-fetch-headers", "{}"))
        self.event_id: str | None = headers.get("bctrl-event-id")

    @property
    def ok(self) -> bool:
        return 200 <= self.status < 300

    def __iter__(self) -> Iterator[bytes]:
        try:
            yield from self._response.data
        finally:
            self.close()

    def read(self) -> bytes:
        return b"".join(self)

    def close(self) -> None:
        context, self._context = self._context, None
        if context is not None:
            context.__exit__(None, None, None)

    def __enter__(self) -> FetchStreamResponse:
        return self

    def __exit__(self, *_: Any) -> None:
        self.close()


class AsyncFetchStreamResponse(FetchStreamResponse):
    """``FetchStreamResponse`` for the async client: iterate it with ``async for``."""

    async def __aiter__(self) -> AsyncIterator[bytes]:
        try:
            async for chunk in self._response.data:
                if chunk:
                    yield chunk
        finally:
            await self.aclose()

    async def aread(self) -> bytes:
        return b"".join([chunk async for chunk in self])

    async def aclose(self) -> None:
        context, self._context = self._context, None
        if context is not None:
            await context.__aexit__(None, None, None)

    async def __aenter__(self) -> AsyncFetchStreamResponse:
        return self

    async def __aexit__(self, *_: Any) -> None:
        await self.aclose()


_Handle = TypeVar("_Handle", bound=_BrowserHandle)


def _handle(resource: BrowserResource, client: Any, model: type[_Handle]) -> _Handle:
    browser = parse_obj_as(model, resource.dict(by_alias=True))
    browser._client = client
    return browser


class Browsers(BrowsersClient):
    def _events_client(self) -> EventsClient:
        return EventsClient(client_wrapper=self._client_wrapper)

    def create(self, **kwargs: Any) -> Browser:
        return _handle(super().create(**kwargs), self, Browser)

    def get(self, *args: Any, **kwargs: Any) -> Browser:
        return _handle(super().get(*args, **kwargs), self, Browser)

    def fetch_stream(self, browser_id: str, **kwargs: Any) -> FetchStreamResponse:  # type: ignore[override]
        """Send the request from the browser and stream the response back. It is sent once: a failure before the
        first byte raises, and is never retried, since the site may already have acted on it."""
        context = self.with_raw_response.fetch_stream(browser_id, **kwargs)
        return FetchStreamResponse(context, context.__enter__())

    @contextmanager
    def with_browser(self, **kwargs: Any) -> Iterator[Browser]:
        browser = self.create(**kwargs)
        failure: BaseException | None = None
        try:
            yield browser
        except BaseException as error:
            failure = error
            raise
        finally:
            try:
                self.stop(browser.id, wait=60)
            except BaseException as cleanup:
                if failure is not None:
                    raise failure from cleanup
                raise


class AsyncBrowsers(AsyncBrowsersClient):
    def _events_client(self) -> AsyncEventsClient:
        return AsyncEventsClient(client_wrapper=self._client_wrapper)

    async def create(self, **kwargs: Any) -> AsyncBrowser:
        return _handle(await super().create(**kwargs), self, AsyncBrowser)

    async def get(self, *args: Any, **kwargs: Any) -> AsyncBrowser:
        return _handle(await super().get(*args, **kwargs), self, AsyncBrowser)

    async def fetch_stream(self, browser_id: str, **kwargs: Any) -> AsyncFetchStreamResponse:  # type: ignore[override]
        """Send the request from the browser and stream the response back. It is sent once: a failure before the
        first byte raises, and is never retried, since the site may already have acted on it."""
        context = self.with_raw_response.fetch_stream(browser_id, **kwargs)
        return AsyncFetchStreamResponse(context, await context.__aenter__())

    @asynccontextmanager
    async def with_browser(self, **kwargs: Any) -> AsyncIterator[AsyncBrowser]:
        browser = await self.create(**kwargs)
        failure: BaseException | None = None
        try:
            yield browser
        except BaseException as error:
            failure = error
            raise
        finally:
            try:
                await self.stop(browser.id, wait=60)
            except BaseException as cleanup:
                if failure is not None:
                    raise failure from cleanup
                raise
