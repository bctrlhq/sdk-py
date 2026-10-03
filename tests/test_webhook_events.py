import asyncio
import json

import httpx
from bctrl import AsyncBctrl, Bctrl

EVENTS = ["spending_cap.reached", "task.awaiting_input", "future.new_event"]
WEBHOOK = {"object": "webhook", "id": "wh_fixture", "url": "https://example.test/events", "name": None,
           "events": EVENTS, "enabled": True, "subaccountId": None, "secret": "fixture",
           "createdAt": "2026-10-03T00:00:00Z", "updatedAt": "2026-10-03T00:00:00Z"}


def verify(requests):
    assert [(r.method, r.url.path, json.loads(r.content)) for r in requests] == [
        ("POST", "/v1/webhooks", {"events": EVENTS, "url": WEBHOOK["url"]}),
        ("PATCH", "/v1/webhooks/wh_fixture", {"events": EVENTS}),
    ]


def test_sync_webhook_transports_preserve_additive_event_names():
    requests = []

    def send(request):
        requests.append(request)
        return httpx.Response(200, json=WEBHOOK)

    with httpx.Client(transport=httpx.MockTransport(send)) as transport:
        client = Bctrl(token="fixture", httpx_client=transport)
        assert client.webhooks.create(url=WEBHOOK["url"], events=EVENTS).events == EVENTS
        assert client.webhooks.update("wh_fixture", events=EVENTS).events == EVENTS
    verify(requests)


def test_async_webhook_transports_preserve_additive_event_names():
    async def run():
        requests = []

        async def send(request):
            requests.append(request)
            return httpx.Response(200, json=WEBHOOK)

        async with httpx.AsyncClient(transport=httpx.MockTransport(send)) as transport:
            client = AsyncBctrl(token="fixture", httpx_client=transport)
            assert (await client.webhooks.create(url=WEBHOOK["url"], events=EVENTS)).events == EVENTS
            assert (await client.webhooks.update("wh_fixture", events=EVENTS)).events == EVENTS
        verify(requests)

    asyncio.run(run())
