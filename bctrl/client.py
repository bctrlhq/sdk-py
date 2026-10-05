"""Generated clients with safe retries and browser helpers."""
from __future__ import annotations

from typing import Any
from ._generated.client import Bctrl as GeneratedBctrl, AsyncBctrl as GeneratedAsyncBctrl
from .browser_helpers import Browsers, AsyncBrowsers
from .conversation_helpers import Conversations, AsyncConversations
from .generated_surface import DEFAULT_API_VERSION
from .pagination import paginate, async_paginate
from .retries import SafeHttpClient, AsyncSafeHttpClient
from .waits import wait_for, async_wait_for


class Bctrl(GeneratedBctrl):
    def __init__(self, *, max_retries: int = 2, api_version: str = DEFAULT_API_VERSION, **kwargs: Any):
        headers = {"BCTRL-Version": api_version, **(kwargs.pop("headers", None) or {})}
        super().__init__(max_retries=0, headers=headers, **kwargs)
        wrapper = self._client_wrapper
        wrapper.httpx_client = SafeHttpClient(wrapper.httpx_client, max_retries)

    @property
    def browsers(self) -> Browsers:
        if self._browsers is None:
            self._browsers = Browsers(client_wrapper=self._client_wrapper)
        return self._browsers

    @property
    def conversations(self) -> Conversations:
        if self._conversations is None:
            self._conversations = Conversations(client_wrapper=self._client_wrapper)
        return self._conversations

    paginate = staticmethod(paginate)
    wait_for = staticmethod(wait_for)


class AsyncBctrl(GeneratedAsyncBctrl):
    def __init__(self, *, max_retries: int = 2, api_version: str = DEFAULT_API_VERSION, **kwargs: Any):
        headers = {"BCTRL-Version": api_version, **(kwargs.pop("headers", None) or {})}
        super().__init__(max_retries=0, headers=headers, **kwargs)
        wrapper = self._client_wrapper
        wrapper.httpx_client = AsyncSafeHttpClient(wrapper.httpx_client, max_retries)

    @property
    def browsers(self) -> AsyncBrowsers:
        if self._browsers is None:
            self._browsers = AsyncBrowsers(client_wrapper=self._client_wrapper)
        return self._browsers

    @property
    def conversations(self) -> AsyncConversations:
        if self._conversations is None:
            self._conversations = AsyncConversations(client_wrapper=self._client_wrapper)
        return self._conversations

    paginate = staticmethod(async_paginate)
    wait_for = staticmethod(async_wait_for)
