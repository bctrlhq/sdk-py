"""Cursor iteration over any generated list operation."""
from __future__ import annotations

from typing import Any, Callable, Iterator, AsyncIterator


def paginate(list_page: Callable[..., Any], **kwargs: Any) -> Iterator[Any]:
    seen: set[str] = set()
    while True:
        page = list_page(**kwargs)
        yield from page.data
        cursor = page.next_cursor
        if not cursor:
            return
        if cursor in seen:
            raise RuntimeError("API repeated a pagination cursor")
        seen.add(cursor)
        kwargs["cursor"] = cursor


async def async_paginate(list_page: Callable[..., Any], **kwargs: Any) -> AsyncIterator[Any]:
    seen: set[str] = set()
    while True:
        page = await list_page(**kwargs)
        for item in page.data:
            yield item
        cursor = page.next_cursor
        if not cursor:
            return
        if cursor in seen:
            raise RuntimeError("API repeated a pagination cursor")
        seen.add(cursor)
        kwargs["cursor"] = cursor
