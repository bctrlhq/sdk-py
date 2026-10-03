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
        for stream in (client.runs.events.stream("run_test", last_event_id="evt_previous"),
                       client.browsers.events.stream("brw_test", after="evt_previous")):
            events = list(stream)
            assert len(events) == 1 and isinstance(events[0], types.Event)
            assert events[0].id == EVENT["id"] and events[0].run_id == EVENT["runId"]

    async def run():
        async with httpx.AsyncClient(transport=httpx.MockTransport(send)) as http:
            client = AsyncBctrl(token="test", httpx_client=http)
            for stream in (client.runs.events.stream("run_test", last_event_id="evt_previous"),
                           client.browsers.events.stream("brw_test", after="evt_previous")):
                events = [event async for event in stream]
                assert len(events) == 1 and isinstance(events[0], types.Event)
                assert events[0].id == EVENT["id"] and events[0].run_id == EVENT["runId"]

    asyncio.run(run())
    for request in (requests[0], requests[2]):
        assert request.url.path == "/v1/runs/run_test/events/stream"
        assert request.headers["Last-Event-ID"] == "evt_previous"
    for request in (requests[1], requests[3]):
        assert request.url.path == "/v1/browsers/brw_test/events/stream"
        assert request.url.params["after"] == "evt_previous"
