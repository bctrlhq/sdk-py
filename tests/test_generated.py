import asyncio
import json
from pathlib import Path
from types import SimpleNamespace

import httpx
import pytest

from bctrl import Bctrl, AsyncBctrl, ApiError, types

BROWSER = json.loads(Path(__file__).with_name("browser.json").read_text())
UNKNOWN = {"error": {"code": "runtime.unknown", "message": "Lost acknowledgment", "requestId": "req-test",
    "reasonClass": "outcome_unknown", "details": {"status": "unknown"}}}


def test_generated_retries_preserve_one_key_and_the_version_header():
    requests = []

    def send(request):
        requests.append(request)
        return httpx.Response(503, json={"error": {"code": "capacity.unavailable"}}) if len(requests) == 1 else httpx.Response(200, json=BROWSER)

    with httpx.Client(transport=httpx.MockTransport(send)) as transport:
        client = Bctrl(token="test", httpx_client=transport)
        browser = client.browsers.create(name="checkout")
        assert browser.id == BROWSER["id"]
        assert requests[0].headers["Idempotency-Key"] == requests[1].headers["Idempotency-Key"]
        assert requests[0].headers["BCTRL-Version"] == "2026-10-03"
        client.browsers.create(idempotency_key="caller-key")
        assert requests[2].headers["Idempotency-Key"] == "caller-key"


def test_unknown_outcomes_and_lost_acknowledgment_are_not_retried():
    for network in (False, True):
        requests = []

        def send(request):
            requests.append(request)
            if network:
                raise httpx.RemoteProtocolError("Lost acknowledgment")
            return httpx.Response(503, json=UNKNOWN)

        with httpx.Client(transport=httpx.MockTransport(send)) as transport:
            client = Bctrl(token="test", httpx_client=transport, max_retries=5)
            with pytest.raises(httpx.RemoteProtocolError if network else ApiError):
                client.browsers.create(request_options={"max_retries": 4})
        assert len(requests) == 1


def test_cursor_iteration_connect_and_cleanup_use_generated_operations():
    requests = []

    def send(request):
        requests.append(request)
        if request.url.path == "/v1/browsers" and request.method == "GET":
            second = request.url.params.get("cursor") == "cursor-two"
            return httpx.Response(200, json={"data": [{**BROWSER, "name": "second" if second else "first"}],
                "nextCursor": None if second else "cursor-two", "hasMore": not second})
        return httpx.Response(200, json=BROWSER)

    with httpx.Client(transport=httpx.MockTransport(send)) as transport:
        client = Bctrl(token="test", httpx_client=transport)
        assert [browser.name for browser in client.paginate(client.browsers.list, limit=1)] == ["first", "second"]
        assert requests[1].url.params["limit"] == "1"
        browser = client.browsers.create()
        connected = []
        playwright = SimpleNamespace(chromium=SimpleNamespace(connect_over_cdp=lambda url: connected.append(url)))
        browser.connect(playwright)
        assert connected == [BROWSER["currentRun"]["connections"]["cdpUrl"]]
        with pytest.raises(ValueError, match="work failed"):
            with client.browsers.with_browser() as scoped:
                assert scoped.id == browser.id
                raise ValueError("work failed")
        assert requests[-1].url.path == f"/v1/browsers/{browser.id}/stop"


def test_sdk_names_preserve_both_aliases_on_the_wire():
    model = types.AiStoredModelSelection.model_validate({"model": "test", "reasoning_effort": "low", "reasoningEffort": "high",
        "max_tokens": 1, "maxTokens": 2})
    output = model.model_dump(by_alias=True, exclude_none=True)
    assert output["reasoning_effort"] == "low"
    assert output["reasoningEffort"] == "high"
    assert output["max_tokens"] == 1
    assert output["maxTokens"] == 2


def test_async_generated_retries_and_unknown_outcomes():
    async def run():
        requests = []

        async def send(request):
            requests.append(request)
            return httpx.Response(503, json={"error": {"code": "capacity.unavailable"}}) if len(requests) == 1 else httpx.Response(200, json=BROWSER)

        async with httpx.AsyncClient(transport=httpx.MockTransport(send)) as transport:
            client = AsyncBctrl(token="test", httpx_client=transport)
            assert (await client.browsers.create()).id == BROWSER["id"]
            assert requests[0].headers["Idempotency-Key"] == requests[1].headers["Idempotency-Key"]

        async def unknown(request):
            requests.append(request)
            return httpx.Response(503, json=UNKNOWN)

        async with httpx.AsyncClient(transport=httpx.MockTransport(unknown)) as transport:
            client = AsyncBctrl(token="test", httpx_client=transport, max_retries=5)
            with pytest.raises(ApiError):
                await client.browsers.create(request_options={"max_retries": 4})
            assert len(requests) == 3

    asyncio.run(run())
