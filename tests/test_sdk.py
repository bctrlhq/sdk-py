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

    def log_message(self, format: str, *args: Any) -> None:
        return

    def _handle(self, method: str) -> None:
        raw = self.rfile.read(int(self.headers.get("content-length", "0")))
        body = json.loads(raw) if raw else None
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
                        "connectUrl": "wss://example.test/devtools",
                        "protocol": "cdp",
                    },
                    "started": True,
                },
            )
        if method == "GET" and route == "/v1/runtimes/rt_test":
            return self._json(200, {"id": "rt_test", "connection": {"connectUrl": "wss://example.test/devtools"}})
        if method == "GET" and route == "/v1/runs/run_test":
            return self._json(200, {"id": "run_test", "connection": {"connectUrl": "wss://example.test/devtools"}})
        if method == "POST" and route == "/v1/tools/stagehand.act/call":
            return self._json(200, {"success": True, "message": "done"})
        if method == "POST" and route == "/v1/tools/code.execute/calls":
            return self._json(202, {"id": "call_code", "status": "queued"})
        if method == "PATCH" and route == "/v1/conversations/conv_test":
            return self._json(200, {"id": "conv_test", **body})
        if method == "POST" and route == "/v1/conversations/conv_test/messages":
            return self._json(202, {"turnId": "turn_test", "status": "queued"})
        return self._json(404, {"error": f"Unhandled route {method} {route}"})

    def _json(self, status: int, body: Any) -> None:
        raw = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("content-type", "application/json")
        self.send_header("content-length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)


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
        conversation = self.client.conversations.update(
            "conv_test", agent="browser-use", model="openai/gpt-5"
        )
        turn = self.client.conversations.messages.create(
            "conv_test", text="Continue", idempotency_key="message-1"
        )
        self.assertTrue(result["success"])
        self.assertEqual(MockHandler.requests[0]["headers"]["Bctrl-Runtime-Id"], "rt_test")
        self.assertNotIn("runtimeId", MockHandler.requests[0]["body"])
        self.assertEqual(conversation["agent"], "browser-use")
        self.assertEqual(turn["status"], "queued")
        self.assertEqual(MockHandler.requests[2]["headers"]["Idempotency-Key"], "message-1")

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


if __name__ == "__main__":
    unittest.main()
