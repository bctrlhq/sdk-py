"""The generated clients, with browser and conversation helpers on their resources."""
from __future__ import annotations

from ._generated.client import Bctrl as GeneratedBctrl, AsyncBctrl as GeneratedAsyncBctrl
from .lib.browsers import Browsers, AsyncBrowsers
from .lib.conversations import Conversations, AsyncConversations
from .lib.pagination import paginate, async_paginate
from .lib.waits import wait_for, async_wait_for


class Bctrl(GeneratedBctrl):
    @property
    def browsers(self) -> Browsers:
        if not isinstance(self._browsers, Browsers):
            self._browsers = Browsers(client_wrapper=self._client_wrapper)
        return self._browsers

    @property
    def conversations(self) -> Conversations:
        if not isinstance(self._conversations, Conversations):
            self._conversations = Conversations(client_wrapper=self._client_wrapper)
        return self._conversations

    paginate = staticmethod(paginate)
    wait_for = staticmethod(wait_for)


class AsyncBctrl(GeneratedAsyncBctrl):
    @property
    def browsers(self) -> AsyncBrowsers:
        if not isinstance(self._browsers, AsyncBrowsers):
            self._browsers = AsyncBrowsers(client_wrapper=self._client_wrapper)
        return self._browsers

    @property
    def conversations(self) -> AsyncConversations:
        if not isinstance(self._conversations, AsyncConversations):
            self._conversations = AsyncConversations(client_wrapper=self._client_wrapper)
        return self._conversations

    paginate = staticmethod(async_paginate)
    wait_for = staticmethod(async_wait_for)
