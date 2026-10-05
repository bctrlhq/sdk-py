"""fetch_stream: the upstream response as an iterator of byte chunks."""
from __future__ import annotations

import asyncio
import json

import httpx
import pytest

from bctrl import ApiError, AsyncBctrl, Bctrl

HEADERS = {
    "bctrl-fetch-status": "404",
    "bctrl-fetch-headers": json.dumps({"content-type": "text/csv", "x-trace": "abc"}),
    "bctrl-event-id": "evt_1",
}


class Chunks(httpx.SyncByteStream, httpx.AsyncByteStream):
    """A body that records how far it was read."""

    def __init__(self, chunks: list[bytes]):
        self.chunks = chunks
        self.pulled = 0

    def __iter__(self):
        for chunk in self.chunks:
            self.pulled += 1
            yield chunk

    async def __aiter__(self):
        for chunk in self.chunks:
            self.pulled += 1
            yield chunk


def test_fetch_stream_yields_chunks_with_the_upstream_head():
    requests = []
    body = Chunks([b"a,b\n", b"1,2\n"])

    def send(request: httpx.Request) -> httpx.Response:
        requests.append({"path": request.url.path, "body": json.loads(request.read())})
        return httpx.Response(200, headers=HEADERS, stream=body)

    with httpx.Client(transport=httpx.MockTransport(send)) as http:
        client = Bctrl(token="test", httpx_client=http)
        response = client.browsers.fetch_stream("br_1", url="https://example.com/report", method="GET")
        assert requests == [{"path": "/v1/browsers/br_1/fetch/stream", "body": {"url": "https://example.com/report", "method": "GET"}}]
        assert (response.status, response.ok, response.event_id) == (404, False, "evt_1")
        assert response.headers["x-trace"] == "abc"
        assert body.pulled == 0, "the body is read only as it is iterated"
        assert b"".join(response) == b"a,b\n1,2\n"


def test_fetch_stream_failure_before_the_body_raises_and_is_not_retried():
    calls = []

    def send(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        return httpx.Response(503, json={"error": {"code": "browser.fetch_failed", "message": "reset", "reasonClass": "upstream"}})

    with httpx.Client(transport=httpx.MockTransport(send)) as http:
        client = Bctrl(token="test", httpx_client=http)
        with pytest.raises(ApiError):
            client.browsers.fetch_stream("br_1", url="https://example.com/")
    assert len(calls) == 1


def test_async_fetch_stream_yields_chunks():
    async def run():
        body = Chunks([b"hello ", b"world"])
        async with httpx.AsyncClient(transport=httpx.MockTransport(lambda request: httpx.Response(200, headers=HEADERS, stream=body))) as http:
            client = AsyncBctrl(token="test", httpx_client=http)
            response = await client.browsers.fetch_stream("br_1", url="https://example.com/")
            assert response.status == 404
            assert [chunk async for chunk in response] == [b"hello ", b"world"]

    asyncio.run(run())
