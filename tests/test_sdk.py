from __future__ import annotations

import json
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any

from bctrl import Bctrl


class MockHandler(BaseHTTPRequestHandler):
    requests: list[dict[str, Any]] = []

    def do_GET(self) -> None:
        self._handle("GET")

    def do_POST(self) -> None:
        self._handle("POST")

    def do_PATCH(self) -> None:
        self._handle("PATCH")

    def do_PUT(self) -> None:
        self._handle("PUT")

    def do_DELETE(self) -> None:
        self._handle("DELETE")

    def log_message(self, format: str, *args: Any) -> None:
        return

    def _handle(self, method: str) -> None:
        raw = self.rfile.read(int(self.headers.get("content-length", "0")))
        content_type = self.headers.get("content-type", "")
        if raw and content_type.startswith("multipart/"):
            body = raw
        elif raw:
            body = json.loads(raw)
        else:
            body = None
        route = self.path.split("?", 1)[0]
        self.requests.append(
            {
                "method": method,
                "path": self.path,
                "body": body,
                "headers": dict(self.headers),
            }
        )

        if method == "POST" and route == "/v1/spaces":
            return self._json(201, {"id": "sp_test", "name": body["name"]})
        if method == "POST" and route == "/v1/files":
            return self._json(201, {"id": "file_uploaded", "name": "fixture.txt"})
        if method == "POST" and route == "/v1/runtimes":
            return self._json(
                201,
                {
                    "id": "rt_context",
                    "connection": {
                        "runId": "run_context",
                        "recording": {"enabled": False},
                        "cdpUrl": "wss://example.test/context/devtools",
                        "webDriverUrl": "https://example.test/context/webdriver",
                        "webMcpUrl": "https://example.test/context/mcp",
                    },
                },
            )
        if method == "POST" and route == "/v1/runtimes/rt_context/stop":
            return self._json(200, {"runtimeId": "rt_context", "status": "stopped"})
        if route == "/v1/conversations/conv_test/turns/turn_test" and method == "GET":
            return self._json(200, {"id": "turn_test", "status": "succeeded"})
        if route == "/v1/conversations/conv_test/turns/turn_test/cancel" and method == "POST":
            return self._json(200, {"id": "turn_test", "status": "cancelled"})
        if route == "/v1/tool-calls/call_code/result" and method == "GET":
            return self._json(202, {"id": "call_code", "status": "running"})
        if self.path == "/v1/runtimes/rt_test/start?wait=0" and method == "POST":
            return self._json(202, {"runtimeId": "rt_test", "runId": "run_test", "status": "starting"})
        if method == "POST" and route == "/v1/runtimes/rt_test/start":
            return self._json(
                200,
                {
                    "runtimeId": "rt_test",
                    "runId": "run_test",
                    "status": "active",
                    "connection": {
                        "runId": "run_test",
                        "recording": {"enabled": True},
                        "cdpUrl": "wss://example.test/devtools",
                        "webDriverUrl": "https://example.test/webdriver",
                        "webMcpUrl": "https://example.test/mcp",
                    },
                    "started": True,
                },
            )
        if method == "GET" and route == "/v1/runtimes/rt_test":
            return self._json(200, {"id": "rt_test", "connection": {"cdpUrl": "wss://example.test/devtools"}})
        if method == "GET" and route == "/v1/runs/run_test":
            return self._json(200, {"id": "run_test", "connection": {"cdpUrl": "wss://example.test/devtools"}})
        if route.startswith("/v1/runs/run_test/files"):
            return self._json(201 if method == "POST" else 200, {"fileId": "file_test", "role": "input"})
        if method == "GET" and route == "/v1/files/file_test/content":
            return self._bytes(200, b"file contents")
        if method == "GET" and route == "/v1/notification-recipients":
            return self._json(200, {"data": [], "nextCursor": None})
        if method == "POST" and route == "/v1/notification-recipients":
            return self._json(201, {"id": "nrec_test", **body})
        if method == "PATCH" and route == "/v1/notification-recipients/nrec_test":
            return self._json(200, {"id": "nrec_test", **body})
        if method == "DELETE" and route == "/v1/notification-recipients/nrec_test":
            return self._json(200, {"id": "nrec_test", "deleted": True})
        if route == "/v1/secrets:reveal" and method == "POST":
            return self._json(200, {"id": body["path"], "version": 3, "username": "bot", "password": "p"})
        if route.startswith("/v1/secrets/") or route == "/v1/secrets":
            if method == "DELETE":
                return self._json(200, {"id": "prod/github/bot", "deleted": True})
            if method == "GET" and route == "/v1/secrets":
                return self._json(200, {"data": [], "folders": ["prod/"], "nextCursor": None})
            return self._json(200, {"id": "prod/github/bot", "version": 4})
        if method == "GET" and route == "/v1/proxies/geo":
            return self._json(200, {"data": [], "nextCursor": None})
        if method == "GET" and route == "/v1/proxies/locations":
            return self._json(200, {"data": [], "nextCursor": None})
        if method == "GET" and route == "/v1/subaccounts/sub_test":
            return self._json(200, {"id": "sub_test", "usage": {}})
        if method == "POST" and route == "/v1/tools/stagehand.act/call":
            return self._json(200, {"success": True, "message": "done"})
        if method == "POST" and route == "/v1/tools/code.execute/calls":
            return self._json(202, {"id": "call_code", "status": "queued"})
        if method == "PATCH" and route == "/v1/conversations/conv_test":
            return self._json(200, {"id": "conv_test", **body})
        if method == "POST" and route == "/v1/conversations/conv_test/messages":
            return self._json(202, {"turnId": "turn_test", "status": "queued"})
        return self._json(404, {"message": f"Unhandled route {method} {route}"})

    def _json(self, status: int, body: Any) -> None:
        raw = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("content-type", "application/json")
        self.send_header("content-length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def _bytes(self, status: int, body: bytes) -> None:
        self.send_response(status)
        self.send_header("content-type", "application/octet-stream")
        self.send_header("content-length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


class BctrlPythonSdkTest(unittest.TestCase):
    def setUp(self) -> None:
        MockHandler.requests = []
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

    def test_async_waits_preserve_handles_and_use_query_parameters(self) -> None:
        started = self.client.runtimes.start("rt_test", wait=0, recording=False)
        self.assertEqual(started, {"runtimeId": "rt_test", "runId": "run_test", "status": "starting"})
        self.client.runtimes.get("rt_test", wait=60, include="connection")
        self.client.conversations.turns.get("conv_test", "turn_test", wait=1)
        self.client.conversations.turns.cancel("conv_test", "turn_test")
        self.client.tool_calls.result("call_code", wait=0)
        self.assertEqual(MockHandler.requests[0]["body"], {"recording": False})
        self.assertEqual([request["path"] for request in MockHandler.requests], [
            "/v1/runtimes/rt_test/start?wait=0",
            "/v1/runtimes/rt_test?include=connection&wait=60",
            "/v1/conversations/conv_test/turns/turn_test?wait=1",
            "/v1/conversations/conv_test/turns/turn_test/cancel",
            "/v1/tool-calls/call_code/result?wait=0",
        ])

    def test_spaces_and_runtime_start_use_current_routes(self) -> None:
        space = self.client.spaces.create(name="automation")
        started = self.client.runtimes.start("rt_test", idempotency_key="start-1")
        runtime = self.client.runtimes.get("rt_test", include="connection")
        run = self.client.runs.get("run_test", include="connection")
        self.assertEqual(space["id"], "sp_test")
        self.assertEqual(started["runId"], "run_test")
        self.assertEqual(MockHandler.requests[1]["headers"]["Idempotency-Key"], "start-1")
        self.assertEqual(MockHandler.requests[2]["path"], "/v1/runtimes/rt_test?include=connection")
        self.assertEqual(MockHandler.requests[3]["path"], "/v1/runs/run_test?include=connection")
        self.assertIn("connection", runtime)
        self.assertIn("connection", run)

    def test_tools_and_conversations_are_first_class(self) -> None:
        result = self.client.tools.call(
            "stagehand.act",
            {"instruction": "Click Continue"},
            runtime_id="rt_test",
        )
        conversation = self.client.conversations.update("conv_test", model="openai/gpt-5")
        turn = self.client.conversations.messages.create(
            "conv_test", text="Continue", idempotency_key="message-1"
        )
        self.assertTrue(result["success"])
        self.assertEqual(MockHandler.requests[0]["headers"]["Bctrl-Runtime-Id"], "rt_test")
        self.assertNotIn("runtimeId", MockHandler.requests[0]["body"])
        self.assertNotIn("agent", conversation)
        self.assertEqual(turn["status"], "queued")
        self.assertEqual(MockHandler.requests[2]["headers"]["Idempotency-Key"], "message-1")

    def test_started_browser_uses_create_and_exposes_current_connections(self) -> None:
        with self.client.runtimes.started_browser(idempotency_key="create-1") as runtime:
            self.assertEqual(runtime.id, "rt_context")
            self.assertEqual(runtime.run_id, "run_context")
            self.assertEqual(runtime.cdp_url, "wss://example.test/context/devtools")
            self.assertEqual(runtime.web_driver_url, "https://example.test/context/webdriver")
            self.assertEqual(runtime.web_mcp_url, "https://example.test/context/mcp")

        self.assertEqual(MockHandler.requests[0]["path"], "/v1/runtimes")
        self.assertEqual(MockHandler.requests[0]["headers"]["Idempotency-Key"], "create-1")
        self.assertTrue(MockHandler.requests[0]["body"]["start"])
        self.assertEqual(MockHandler.requests[1]["path"], "/v1/runtimes/rt_context/stop")

    def test_legacy_execution_namespaces_are_absent(self) -> None:
        self.assertFalse(hasattr(self.client, "invocations"))
        self.assertFalse(hasattr(self.client, "vault"))
        self.assertFalse(hasattr(self.client.runtimes, "targets"))
        self.assertFalse(hasattr(self.client.runtimes, "human_actions"))

    def test_code_execute_uses_async_tool_call_route(self) -> None:
        result = self.client.tools.start(
            "code.execute",
            {"source": "export default async () => ({ ok: true });", "input": {"value": 1}},
            runtime_id="rt_test",
            idempotency_key="code-execute-1",
        )

        self.assertEqual(result["id"], "call_code")
        request = MockHandler.requests[0]
        self.assertEqual(request["path"], "/v1/tools/code.execute/calls")
        self.assertEqual(request["headers"]["Bctrl-Runtime-Id"], "rt_test")
        self.assertEqual(request["headers"]["Idempotency-Key"], "code-execute-1")
        self.assertEqual(request["body"]["input"], {"value": 1})

    def test_files_notifications_proxy_catalog_and_subaccount_usage_use_current_routes(self) -> None:
        self.assertEqual(self.client.files.content("file_test"), b"file contents")
        self.client.notification_recipients.list(limit=10)
        self.client.notification_recipients.create(type="email", value="user@example.com")
        self.client.notification_recipients.update("nrec_test", enabled=False)
        self.client.notification_recipients.delete("nrec_test")
        self.client.proxies.geo.list(country="US", type="city")
        self.client.proxies.locations.list(pool="pool1")
        self.client.subaccounts.usage.get("sub_test")

        self.assertEqual(MockHandler.requests[0]["path"], "/v1/files/file_test/content")
        self.assertEqual(MockHandler.requests[1]["path"], "/v1/notification-recipients?limit=10")
        self.assertEqual(MockHandler.requests[2]["body"]["type"], "email")
        self.assertEqual(MockHandler.requests[3]["body"]["enabled"], False)
        self.assertEqual(MockHandler.requests[4]["method"], "DELETE")
        self.assertEqual(MockHandler.requests[5]["path"], "/v1/proxies/geo?country=US&type=city")
        self.assertEqual(MockHandler.requests[6]["path"], "/v1/proxies/locations?pool=pool1")
        self.assertEqual(MockHandler.requests[7]["path"], "/v1/subaccounts/sub_test?include=usage")

    def test_secrets_keep_slashes_and_send_if_match(self) -> None:
        self.client.secrets.list(prefix="prod/", delimiter="/")
        self.client.secrets.get("prod/github/bot")
        self.client.secrets.put("prod/github/bot", type="login", password="p", if_match=3)
        self.client.secrets.put("prod/github/bot", from_version=2)
        self.client.secrets.update("prod/github/bot", totp=None)
        self.client.secrets.delete("prod/github/bot", if_match=4)
        revealed = self.client.secrets.reveal("prod/github/bot")

        requests = MockHandler.requests
        self.assertEqual(requests[0]["path"], "/v1/secrets?prefix=prod%2F&delimiter=%2F")
        self.assertEqual(requests[1]["path"], "/v1/secrets/prod/github/bot")
        self.assertEqual(requests[2]["method"], "PUT")
        self.assertEqual(requests[2]["headers"].get("If-Match"), '"3"')
        self.assertEqual(requests[2]["body"], {"type": "login", "password": "p"})
        self.assertEqual(requests[3]["body"], {"fromVersion": 2})
        self.assertNotIn("If-Match", requests[3]["headers"])
        self.assertEqual(requests[4]["body"], {"totp": None})
        self.assertEqual(requests[5]["headers"].get("If-Match"), '"4"')
        self.assertEqual(requests[6]["path"], "/v1/secrets:reveal")
        self.assertEqual(requests[6]["body"], {"path": "prod/github/bot"})
        self.assertEqual(revealed["password"], "p")

    def test_run_files_use_the_run_file_routes(self) -> None:
        self.client.runs.files.list("run_test", role="input")
        self.client.runs.files.add("run_test", "file_test")
        self.client.runs.files.upload(
            "run_test", file=b"x", filename="a.txt", path="docs/a.txt", idempotency_key="up-1"
        )
        self.client.runs.files.retry("run_test", "file_test")
        self.client.runs.files.remove("run_test", "file_test")
        self.client.runs.files.collect("run_test", "downloads/r.pdf", name="r.pdf")
        self.client.runtimes.start("rt_test", files=[{"fileId": "file_test"}])

        self.assertEqual(
            [(request["method"], request["path"]) for request in MockHandler.requests],
            [
                ("GET", "/v1/runs/run_test/files?role=input"),
                ("POST", "/v1/runs/run_test/files"),
                ("POST", "/v1/runs/run_test/files/upload"),
                ("POST", "/v1/runs/run_test/files/file_test/retry"),
                ("DELETE", "/v1/runs/run_test/files/file_test"),
                ("POST", "/v1/runs/run_test/files/collect"),
                ("POST", "/v1/runtimes/rt_test/start"),
            ],
        )
        self.assertEqual(MockHandler.requests[1]["body"], {"fileId": "file_test"})
        self.assertEqual(MockHandler.requests[2]["headers"]["Idempotency-Key"], "up-1")
        self.assertIn(b'name="path"', MockHandler.requests[2]["body"])
        self.assertEqual(
            MockHandler.requests[5]["body"], {"runtimePath": "downloads/r.pdf", "name": "r.pdf"}
        )
        self.assertEqual(MockHandler.requests[6]["body"], {"files": [{"fileId": "file_test"}]})

    def test_file_upload_scopes_space_in_query(self) -> None:
        uploaded = self.client.files.upload(
            file=b"fixture",
            filename="fixture.txt",
            space_id="sp_test",
            name="fixture.txt",
        )

        self.assertEqual(uploaded["id"], "file_uploaded")
        self.assertEqual(MockHandler.requests[0]["path"], "/v1/files?spaceId=sp_test")


if __name__ == "__main__":
    unittest.main()
