import asyncio
import json

import httpx

from bctrl import AsyncBctrl, Bctrl

CAP = {"object": "spending_cap", "amount": 0, "currency": "USD", "scope": "organization", "spaceId": None,
       "status": "reached", "warnAtPercent": 80, "usage": {"amount": 1.25, "currency": "USD"},
       "period": {"start": "2026-10-01T00:00:00Z", "end": "2026-11-01T00:00:00Z"}}


def verify(requests):
    assert [(r.method, r.url.path, json.loads(r.content) if r.content else None) for r in requests] == [
        ("GET", "/v1/account/spending-cap", None),
        ("PATCH", "/v1/account/spending-cap", {"amount": 0, "currency": "USD"}),
        ("GET", "/v1/spaces/team checkout/spending-cap", None),
        ("PATCH", "/v1/spaces/team checkout/spending-cap", {"amount": None, "currency": "USD"}),
    ]
    for request in requests:
        assert request.headers["BCTRL-Version"] == "2026-10-03"
        if request.method == "PATCH":
            assert request.headers["Idempotency-Key"]


def test_generated_sync_cap_transports_preserve_zero_and_explicit_null():
    requests = []

    def send(request):
        requests.append(request)
        return httpx.Response(200, json=CAP)

    with httpx.Client(transport=httpx.MockTransport(send)) as transport:
        client = Bctrl(token="fixture", httpx_client=transport)
        assert client.account.spending_cap.get().usage.amount == 1.25
        client.account.spending_cap.update(amount=0, currency="USD")
        client.spaces.spending_cap.get(space_id="team checkout")
        client.spaces.spending_cap.update(space_id="team checkout", amount=None, currency="USD")
    verify(requests)


def test_generated_async_cap_transports_preserve_zero_and_explicit_null():
    async def run():
        requests = []

        async def send(request):
            requests.append(request)
            return httpx.Response(200, json=CAP)

        async with httpx.AsyncClient(transport=httpx.MockTransport(send)) as transport:
            client = AsyncBctrl(token="fixture", httpx_client=transport)
            assert (await client.account.spending_cap.get()).usage.amount == 1.25
            await client.account.spending_cap.update(amount=0, currency="USD")
            await client.spaces.spending_cap.get(space_id="team checkout")
            await client.spaces.spending_cap.update(space_id="team checkout", amount=None, currency="USD")
        verify(requests)

    asyncio.run(run())
