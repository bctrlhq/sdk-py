"""Generated clients with safe retries and browser helpers."""
from __future__ import annotations

from typing import Any
from ._generated.client import Bctrl as GeneratedBctrl, AsyncBctrl as GeneratedAsyncBctrl
from .browser_helpers import Browsers, AsyncBrowsers
from .generated_surface import DEFAULT_API_VERSION
from .pagination import paginate, async_paginate
from .retries import SafeHttpClient, AsyncSafeHttpClient


class Bctrl(GeneratedBctrl):
    def __init__(self, *, max_retries: int = 2, api_version: str = DEFAULT_API_VERSION, **kwargs: Any):
        headers = {"BCTRL-Version": api_version, **kwargs.pop("headers", {})}
        super().__init__(max_retries=0, headers=headers, **kwargs)
        wrapper = self._client_wrapper
        wrapper.httpx_client = SafeHttpClient(wrapper.httpx_client, max_retries)

    @property
    def browsers(self) -> Browsers:
        if self._browsers is None:
            self._browsers = Browsers(client_wrapper=self._client_wrapper)
        return self._browsers

    paginate = staticmethod(paginate)


class AsyncBctrl(GeneratedAsyncBctrl):
    def __init__(self, *, max_retries: int = 2, api_version: str = DEFAULT_API_VERSION, **kwargs: Any):
        headers = {"BCTRL-Version": api_version, **kwargs.pop("headers", {})}
        super().__init__(max_retries=0, headers=headers, **kwargs)
        wrapper = self._client_wrapper
        wrapper.httpx_client = AsyncSafeHttpClient(wrapper.httpx_client, max_retries)

    @property
    def browsers(self) -> AsyncBrowsers:
        if self._browsers is None:
            self._browsers = AsyncBrowsers(client_wrapper=self._client_wrapper)
        return self._browsers

    paginate = staticmethod(async_paginate)
