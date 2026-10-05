import asyncio
import json

import httpx

from bctrl import AsyncBctrl, Bctrl, types

EVENT = {
    "id": "evt_delivered", "object": "event", "type": "run.started", "category": "lifecycle",
    "channel": "platform", "outcome": "ok", "source": "runtime", "seq": 7,
    "actor": {"type": "platform", "id": None, "name": None}, "target": None, "data": {},
    "runId": "run_test", "runtimeId": "brw_test", "conversationId": None, "taskId": None,
    "spaceId": None, "pageId": None, "spanId": None,
    "time": "2026-10-03T00:00:00Z", "timestamp": "2026-10-03T00:00:00Z",
    "createdAt": "2026-10-03T00:00:00Z", "updatedAt": "2026-10-03T00:00:00Z",
}


def test_sync_and_async_event_streams_preserve_event_id_resume():
    requests = []

    def send(request):
        requests.append(request)
        return httpx.Response(200, headers={"content-type": "text/event-stream"},
                              text=f": heartbeat\n\nid: {EVENT['id']}\nevent: {EVENT['type']}\ndata: {json.dumps(EVENT)}\n\n")

    with httpx.Client(transport=httpx.MockTransport(send)) as http:
        client = Bctrl(token="test", httpx_client=http)
        for stream in (client.events.stream(run="run_test", last_event_id="evt_previous"),
                       client.events.stream(browser="brw_test", after="evt_previous")):
            events = list(stream)
            assert len(events) == 1 and isinstance(events[0], types.Event)
            assert events[0].id == EVENT["id"] and events[0].run_id == EVENT["runId"]

    async def run():
        async with httpx.AsyncClient(transport=httpx.MockTransport(send)) as http:
            client = AsyncBctrl(token="test", httpx_client=http)
            for stream in (client.events.stream(run="run_test", last_event_id="evt_previous"),
                           client.events.stream(browser="brw_test", after="evt_previous")):
                events = [event async for event in stream]
                assert len(events) == 1 and isinstance(events[0], types.Event)
                assert events[0].id == EVENT["id"] and events[0].run_id == EVENT["runId"]

    asyncio.run(run())
    for request in (requests[0], requests[2]):
        assert request.url.path == "/v1/events/stream" and request.url.params["run"] == "run_test"
        assert request.headers["Last-Event-ID"] == "evt_previous"
    for request in (requests[1], requests[3]):
        assert request.url.path == "/v1/events/stream" and request.url.params["browser"] == "brw_test"
        assert request.url.params["after"] == "evt_previous"


def test_browser_events_and_conversation_history_read_the_one_log():
    browser = json.loads((__import__("pathlib").Path(__file__).with_name("browser.json")).read_text())
    browser["id"] = "br_1"
    requests = []

    def send(request):
        requests.append(request)
        if request.url.path == "/v1/browsers/br_1":
            return httpx.Response(200, json=browser)
        return httpx.Response(200, json={"data": [EVENT], "hasMore": False, "nextCursor": None})

    with httpx.Client(transport=httpx.MockTransport(send)) as http:
        client = Bctrl(token="test", httpx_client=http)
        listed = client.browsers.get("br_1").events.list(category="control")
        assert [event.id for event in listed.data] == [EVENT["id"]]
        client.conversations.history("conv_1", type="message.created")
    assert requests[1].url.path == "/v1/events"
    assert requests[1].url.params["browser"] == "br_1" and requests[1].url.params["category"] == "control"
    assert requests[2].url.path == "/v1/events"
    assert requests[2].url.params["conversation"] == "conv_1" and requests[2].url.params["order"] == "asc"
