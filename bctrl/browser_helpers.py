"""Playwright connections and scoped browser cleanup over generated operations."""
from __future__ import annotations

import asyncio
import time
from contextlib import contextmanager, asynccontextmanager
from typing import Any, Iterator, AsyncIterator

from pydantic import PrivateAttr
from ._generated.browsers.client import BrowsersClient, AsyncBrowsersClient
from ._generated.types.browser_resource import BrowserResource


class Browser(BrowserResource):
    _client: Any = PrivateAttr()

    def wait_until_ready(self, *, timeout: float = 120) -> Browser:
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            browser = self._client.get(self.id, wait=min(60, max(1, int(deadline - time.monotonic()))))
            if browser.current_run and browser.current_run.status in ("failed", "ended"):
                raise RuntimeError(f"Browser Run {browser.current_run.status}: {browser.current_run.end_reason}")
            if browser.current_run and browser.current_run.status == "active" and browser.current_run.connections:
                return browser
            time.sleep(0.25)
        raise TimeoutError("Timed out waiting for browser connections")

    def connect(self, playwright: Any, *, timeout: float = 120) -> Any:
        browser = self.wait_until_ready(timeout=timeout)
        return playwright.chromium.connect_over_cdp(browser.current_run.connections.cdp_url)


class AsyncBrowser(Browser):
    async def wait_until_ready(self, *, timeout: float = 120) -> AsyncBrowser:
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            browser = await self._client.get(self.id, wait=min(60, max(1, int(deadline - time.monotonic()))))
            if browser.current_run and browser.current_run.status in ("failed", "ended"):
                raise RuntimeError(f"Browser Run {browser.current_run.status}: {browser.current_run.end_reason}")
            if browser.current_run and browser.current_run.status == "active" and browser.current_run.connections:
                return browser
            await asyncio.sleep(0.25)
        raise TimeoutError("Timed out waiting for browser connections")

    async def connect(self, playwright: Any, *, timeout: float = 120) -> Any:
        browser = await self.wait_until_ready(timeout=timeout)
        return await playwright.chromium.connect_over_cdp(browser.current_run.connections.cdp_url)


def _handle(resource: BrowserResource, client: Any, model: type[Browser]) -> Any:
    browser = model.model_validate(resource.model_dump(by_alias=True))
    browser._client = client
    return browser


class Browsers(BrowsersClient):
    def create(self, **kwargs: Any) -> Browser:
        return _handle(super().create(**kwargs), self, Browser)

    def get(self, *args: Any, **kwargs: Any) -> Browser:
        return _handle(super().get(*args, **kwargs), self, Browser)

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
    async def create(self, **kwargs: Any) -> AsyncBrowser:
        return _handle(await super().create(**kwargs), self, AsyncBrowser)

    async def get(self, *args: Any, **kwargs: Any) -> AsyncBrowser:
        return _handle(await super().get(*args, **kwargs), self, AsyncBrowser)

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
