from __future__ import annotations

import json
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any

from pydantic import BaseModel

from bctrl import Bctrl, BctrlApiError, BctrlNotFoundError
from bctrl.http import V1HttpClient


class MockHandler(BaseHTTPRequestHandler):
    requests: list[dict[str, Any]] = []
    route_hits: dict[str, int] = {}

    def do_GET(self) -> None:
        self._handle("GET")

    def do_POST(self) -> None:
        self._handle("POST")

    def do_PATCH(self) -> None:
        self._handle("PATCH")

    def do_DELETE(self) -> None:
        self._handle("DELETE")

    def log_message(self, format: str, *args: Any) -> None:
        return

    def _handle(self, method: str) -> None:
        length = int(self.headers.get("content-length", "0"))
        raw = self.rfile.read(length) if length else b""
        body = _decode_body(raw, self.headers.get("content-type"))
        path = self.path
        route = path.split("?", 1)[0]
        self.requests.append(
            {
                "method": method,
                "path": path,
                "headers": dict(self.headers),
                "body": body,
            }
        )
        self.route_hits[route] = self.route_hits.get(route, 0) + 1

        if method == "POST" and route == "/v1/spaces":
            return self._json(
                201,
                {
                    "id": "space_1",
                    "name": body.get("name"),
                    "createdAt": iso(),
                    "updatedAt": iso(),
                },
            )

        if method == "GET" and route == "/v1/auth/whoami":
            return self._json(
                200,
                {
                    "defaultSpaceId": "space_1",
                    "organizationId": "org_1",
                    "scope": "organization",
                },
            )

        if method == "GET" and route == "/v1/usage":
            return self._json(200, {"organizationId": "org_1", "credits": {"available": 100}})

        if method == "POST" and route == "/v1/runtimes":
            return self._json(
                201,
                {
                    "id": "runtime_1",
                    "type": body.get("type", "browser"),
                    "status": "stopped",
                    "createdAt": iso(),
                    "updatedAt": iso(),
                },
            )

        if method == "POST" and route == "/v1/runtimes/runtime_1/start":
            return self._json(
                200,
                {
                    "runtimeId": "runtime_1",
                    "runId": "run_1",
                    "status": "active",
                    "connectUrl": "wss://example.test/devtools",
                    "protocol": "cdp",
                    "started": True,
                },
            )

        if method == "POST" and route == "/v1/runtimes/runtime_1/stop":
            return self._json(200, {"id": "runtime_1", "status": "stopped"})

        if method == "GET" and route == "/v1/runtimes/runtime_1":
            return self._json(200, {"id": "runtime_1", "status": "active", "activeRunId": "run_1"})

        if method == "GET" and route == "/v1/runtimes/runtime_1/targets":
            return self._json(
                200,
                {
                    "data": [runtime_target()],
                    "nextCursor": None,
                },
            )

        if method == "POST" and route == "/v1/runtimes/runtime_1/targets":
            return self._json(
                201,
                runtime_target(
                    {
                        "uri": body.get("uri", "about:blank"),
                        "active": body.get("activate") is True,
                    }
                ),
            )

        if method == "GET" and route == "/v1/runtimes/runtime_1/targets/target_1":
            return self._json(200, runtime_target())

        if method == "POST" and route == "/v1/runtimes/runtime_1/targets/target_1/activate":
            return self._json(200, runtime_target({"active": True}))

        if method == "DELETE" and route == "/v1/runtimes/runtime_1/targets/target_1":
            return self._json(200, {"id": "target_1", "deleted": True})

        if method == "GET" and route == "/v1/runtimes/missing":
            return self._json(
                404,
                {
                    "error": "Runtime not found",
                    "code": "runtime.not_found",
                    "requestId": "req_1",
                },
            )

        if method == "POST" and route == "/v1/runtimes/runtime_1/invocations":
            return self._json(
                202,
                {
                    "id": "invocation_1",
                    "runtimeId": "runtime_1",
                    "runId": "run_1",
                    "action": body.get("action"),
                    "status": "queued",
                    "createdAt": iso(),
                },
            )

        if method == "POST" and route == "/v1/runtimes/runtime_1/invocations/invocation_1/wait":
            wait_count = len([request for request in self.requests if request["path"] == self.path])
            if wait_count > 1:
                return self._json(
                    200,
                    {
                        "id": "invocation_1",
                        "runtimeId": "runtime_1",
                        "runId": "run_1",
                        "action": "extract",
                        "status": "succeeded",
                        "output": {"invoiceNumber": "INV-123"},
                        "waitStatus": "completed",
                        "createdAt": iso(),
                    },
                )
            return self._json(
                200,
                {
                    "id": "invocation_1",
                    "runtimeId": "runtime_1",
                    "runId": "run_1",
                    "action": "extract",
                    "status": "running",
                    "waitStatus": "timeout",
                    "retryAfterMs": 0,
                    "createdAt": iso(),
                },
            )

        if method == "GET" and route == "/v1/runs/run_1/invocations":
            return self._json(
                200,
                {
                    "data": [
                        {
                            "id": "invocation_1",
                            "runtimeId": "runtime_1",
                            "runId": "run_1",
                        }
                    ],
                    "nextCursor": None,
                },
            )

        if method == "GET" and route == "/v1/runs/run_1/events/stream":
            return self._sse(
                [
                    'event: run.started\ndata: {"runId":"run_1"}\n\n',
                    'id: evt_2\nevent: run.ended\ndata: {"status":"stopped"}\n\n',
                ]
            )

        if method == "GET" and route == "/v1/runs/run_1/activity/stream":
            return self._sse(['event: log\ndata: Browser opened\n\n'])

        if method == "GET" and route == "/v1/vault/secrets/login/totp":
            return self._json(200, {"code": "123456"})

        if route == "/v1/retry-safe":
            if self.route_hits[route] == 1:
                return self._json(503, {"error": "temporarily unavailable"})
            return self._json(200, {"ok": True})

        if route == "/v1/retry-post":
            if self.route_hits[route] == 1:
                return self._json(503, {"error": "temporarily unavailable"})
            return self._json(200, {"ok": True})

        return self._json(
            404,
            {
                "error": f"Unhandled route {method} {route}",
                "code": "test.unhandled",
            },
        )

    def _json(self, status: int, body: Any) -> None:
        raw = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("content-type", "application/json")
        self.send_header("content-length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def _sse(self, chunks: list[str]) -> None:
        self.send_response(200)
        self.send_header("content-type", "text/event-stream")
        self.end_headers()
        for chunk in chunks:
            self.wfile.write(chunk.encode())
            self.wfile.flush()


class BctrlPythonSdkTest(unittest.TestCase):
    def setUp(self) -> None:
        MockHandler.requests = []
        MockHandler.route_hits = {}
        self.server = ThreadingHTTPServer(("127.0.0.1", 0), MockHandler)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.client = Bctrl(
            api_key="test_key",
            base_url=f"http://127.0.0.1:{self.server.server_port}",
        )

    def tearDown(self) -> None:
        self.server.shutdown()
        self.server.server_close()
        self.thread.join(timeout=2)

    def test_root_namespaces_and_raw_responses(self) -> None:
        space = self.client.spaces.create(name="sdk-python")
        whoami = self.client.auth.whoami()
        usage = self.client.usage.get()

        self.assertEqual(space["id"], "space_1")
        self.assertEqual(whoami["defaultSpaceId"], "space_1")
        self.assertEqual(usage["organizationId"], "org_1")
        self.assertEqual(
            paths(),
            ["POST /v1/spaces", "GET /v1/auth/whoami", "GET /v1/usage"],
        )

    def test_start_is_direct_and_idempotent_header_is_explicit(self) -> None:
        started = self.client.runtimes.start("runtime_1", idempotency_key="start-1")

        self.assertEqual(started["connectUrl"], "wss://example.test/devtools")
        self.assertEqual(paths(), ["POST /v1/runtimes/runtime_1/start"])
        self.assertEqual(MockHandler.requests[0]["headers"].get("Idempotency-Key"), "start-1")

    def test_runtime_target_routes(self) -> None:
        listed = self.client.runtimes.targets.list("runtime_1")
        created = self.client.runtimes.targets.create(
            "runtime_1",
            uri="https://example.com",
            activate=True,
        )
        fetched = self.client.runtimes.targets.get("runtime_1", "target_1")
        activated = self.client.runtimes.targets.activate("runtime_1", "target_1")
        deleted = self.client.runtimes.targets.delete("runtime_1", "target_1")

        self.assertEqual(listed["data"][0]["id"], "target_1")
        self.assertEqual(created["uri"], "https://example.com")
        self.assertTrue(fetched["active"])
        self.assertTrue(activated["active"])
        self.assertEqual(deleted, {"id": "target_1", "deleted": True})
        self.assertEqual(
            paths(),
            [
                "GET /v1/runtimes/runtime_1/targets",
                "POST /v1/runtimes/runtime_1/targets",
                "GET /v1/runtimes/runtime_1/targets/target_1",
                "POST /v1/runtimes/runtime_1/targets/target_1/activate",
                "DELETE /v1/runtimes/runtime_1/targets/target_1",
            ],
        )
        self.assertEqual(
            MockHandler.requests[1]["body"],
            {"uri": "https://example.com", "activate": True},
        )

    def test_transport_retries_only_safe_or_idempotent_requests(self) -> None:
        http = V1HttpClient(
            api_key="test_key",
            base_url=f"http://127.0.0.1:{self.server.server_port}",
        )

        self.assertEqual(http.request("GET", "/retry-safe"), {"ok": True})
        self.assertEqual(paths(), ["GET /v1/retry-safe", "GET /v1/retry-safe"])

        MockHandler.requests = []
        MockHandler.route_hits = {}
        with self.assertRaises(BctrlApiError) as raised:
            http.request("POST", "/retry-post", json_body={"name": "unsafe"})
        self.assertEqual(raised.exception.status_code, 503)
        self.assertEqual(paths(), ["POST /v1/retry-post"])

        MockHandler.requests = []
        MockHandler.route_hits = {}
        self.assertEqual(
            http.request("POST", "/retry-post", idempotency_key="retry-post-1"),
            {"ok": True},
        )
        self.assertEqual(paths(), ["POST /v1/retry-post", "POST /v1/retry-post"])

    def test_clients_do_not_expose_fake_crud_routes(self) -> None:
        self.assertFalse(hasattr(self.client.api_keys, "get"))
        self.assertFalse(hasattr(self.client.api_keys, "update"))
        self.assertFalse(hasattr(self.client.subaccounts, "delete"))

        totp = self.client.vault.totp("login")

        self.assertEqual(totp["code"], "123456")
        self.assertEqual(paths(), ["GET /v1/vault/secrets/login/totp"])

    def test_output_model_conversion_and_create_and_wait(self) -> None:
        class Invoice(BaseModel):
            invoiceNumber: str

        invocation = self.client.runtimes.invocations.create_and_wait(
            "runtime_1",
            action="extract",
            instruction="Extract invoice number",
            model="openai/gpt-5",
            output_model=Invoice,
            timeout=5,
            poll_timeout_ms=1000,
        )

        self.assertEqual(invocation["status"], "succeeded")
        self.assertEqual(invocation["parsed_output"].invoiceNumber, "INV-123")
        request_body = MockHandler.requests[0]["body"]
        self.assertEqual(request_body["action"], "extract")
        self.assertEqual(request_body["instruction"], "Extract invoice number")
        self.assertEqual(request_body["model"], "openai/gpt-5")
        self.assertEqual(request_body["outputSchema"]["type"], "object")
        self.assertEqual(
            request_body["outputSchema"]["properties"]["invoiceNumber"]["type"],
            "string",
        )
        self.assertIn("invoiceNumber", request_body["outputSchema"]["required"])
        self.assertEqual(
            paths(),
            [
                "POST /v1/runtimes/runtime_1/invocations",
                "POST /v1/runtimes/runtime_1/invocations/invocation_1/wait",
                "POST /v1/runtimes/runtime_1/invocations/invocation_1/wait",
            ],
        )

    def test_invocation_rejects_non_pydantic_schema_forms(self) -> None:
        class FakeSchema:
            @classmethod
            def model_json_schema(cls) -> dict[str, Any]:
                return {"type": "object"}

        with self.assertRaises(TypeError):
            self.client.runtimes.invocations.create(
                "runtime_1",
                action="extract",
                schema={"type": "object"},
            )

        with self.assertRaises(TypeError):
            self.client.runtimes.invocations.create(
                "runtime_1",
                action="extract",
                outputSchema={"type": "object"},
            )

        with self.assertRaises(TypeError):
            self.client.runtimes.invocations.create(
                "runtime_1",
                action="extract",
                output_model=FakeSchema,
            )

    def test_started_browser_context_manager_stops_runtime(self) -> None:
        with self.client.runtimes.started_browser(name="checkout") as runtime:
            self.assertEqual(runtime.id, "runtime_1")
            self.assertEqual(runtime.runtime_id, "runtime_1")
            self.assertEqual(runtime.run_id, "run_1")
            self.assertEqual(runtime.connect_url, "wss://example.test/devtools")
            self.assertEqual(runtime.protocol, "cdp")

        self.assertEqual(
            paths(),
            [
                "POST /v1/runtimes",
                "POST /v1/runtimes/runtime_1/start",
                "POST /v1/runtimes/runtime_1/stop",
            ],
        )

    def test_sse_stream_iterators_parse_events(self) -> None:
        events = list(self.client.runs.events.stream("run_1"))
        activity = list(self.client.runs.activity.stream("run_1"))

        self.assertEqual(
            events,
            [
                {"event": "run.started", "data": {"runId": "run_1"}},
                {"event": "run.ended", "id": "evt_2", "data": {"status": "stopped"}},
            ],
        )
        self.assertEqual(activity, [{"event": "log", "data": "Browser opened"}])
        self.assertEqual(
            paths(),
            [
                "GET /v1/runs/run_1/events/stream",
                "GET /v1/runs/run_1/activity/stream",
            ],
        )

    def test_typed_not_found_error(self) -> None:
        with self.assertRaises(BctrlNotFoundError) as raised:
            self.client.runtimes.get("missing")

        self.assertEqual(raised.exception.code, "runtime.not_found")
        self.assertEqual(raised.exception.request_id, "req_1")


def paths() -> list[str]:
    return [f"{request['method']} {request['path']}" for request in MockHandler.requests]


def runtime_target(overrides: dict[str, Any] | None = None) -> dict[str, Any]:
    return {
        "id": "target_1",
        "runtimeId": "runtime_1",
        "type": "browser_page",
        "label": "Page 1",
        "uri": "https://example.test/",
        "active": True,
        "metadata": {"title": "Example"},
        **(overrides or {}),
    }


def _decode_body(raw: bytes, content_type: str | None) -> Any:
    if not raw:
        return {}
    text = raw.decode()
    if content_type and "application/json" not in content_type:
        return text
    return json.loads(text)


def iso() -> str:
    return "2026-06-02T00:00:00.000Z"


if __name__ == "__main__":
    unittest.main()
