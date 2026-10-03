from __future__ import annotations

import json
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any

from bctrl import Bctrl, StartedBrowser
from unittest.mock import Mock


def browser_response(browser_id: str, run_id: str, prefix: str = "") -> dict:
    return {"id": browser_id, "object": "browser", "status": "running",
            "currentRun": {"id": run_id, "object": "run", "resourceId": browser_id,
                           "resourceType": "browser", "status": "active",
                           "connections": {"cdpUrl": f"wss://example.test/{prefix}devtools",
                                           "webdriverUrl": f"https://example.test/{prefix}webdriver",
                                           "liveViewUrl": f"https://example.test/{prefix}view",
                                           "liveViewReadOnlyUrl": f"https://example.test/{prefix}read"}}}

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

        if method == "POST" and route == "/v1/tools/computer.use/call":
            return self._json(200, {"action": body["action"], "width": 800, "height": 600})
        if method == "POST" and route == "/v1/tools/computer.use/calls":
            return self._json(202, {"id": "call_computer", "status": "queued"})

        if method == "POST" and route == "/v1/api-keys":
            return self._json(201, {"data": {"id": "key-agent", "type": "agent", "agent": body["agent"],
                                          "actsFor": {"userId": "person-1"}, "lastUsedAt": None}, "secret": "test-only-secret"})
        if method == "POST" and route == "/v1/spaces":
            return self._json(201, {"id": "sp_test", "name": body["name"]})
        if method == "POST" and route == "/v1/files":
            return self._json(201, {"id": "file_uploaded", "name": "fixture.txt"})
        if method == "POST" and route == "/v1/browsers":
            return self._json(201, browser_response("br_context", "run_context", "context/"))
        if method == "POST" and route == "/v1/browsers/br_context/stop":
            return self._json(200, {"id": "br_context", "currentRun": None, "status": "idle"})
        if route == "/v1/conversations/conv_test/turns/turn_test" and method == "GET":
            return self._json(200, {"id": "turn_test", "status": "succeeded"})
        if route == "/v1/conversations/conv_test/turns/turn_test/cancel" and method == "POST":
            return self._json(200, {"id": "turn_test", "status": "cancelled"})
        if route == "/v1/tool-calls/call_code/result" and method == "GET":
            return self._json(202, {"id": "call_code", "status": "running"})
        if method == "POST" and route == "/v1/browsers/br_test/start":
            return self._json(200, browser_response("br_test", "run_test"))
        if method == "GET" and route == "/v1/browsers/br_test":
            return self._json(200, browser_response("br_test", "run_test"))
        if method == "GET" and route == "/v1/browsers/br_test/runs":
            return self._json(200, {"data": [browser_response("br_test", "run_test")["currentRun"]],
                                    "nextCursor": None, "hasMore": False})
        if route in ("/v1/browsers/br_test/stop", "/v1/browsers/br_test/connections/revoke") or (
            route == "/v1/browsers/br_test" and method in ("PATCH", "DELETE")
        ):
            return self._json(200, browser_response("br_test", "run_test"))
        if method == "GET" and route == "/v1/runs/run_test":
            return self._json(200, browser_response("br_test", "run_test")["currentRun"] )
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
        if method == "GET" and route == "/v1/locations":
            return self._json(200, {"data": [{"id": "us-east", "object": "location"}], "nextCursor": None, "hasMore": False})
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
    def test_computer_actions_preserve_vendor_snake_case_fields(self) -> None:
        action = {"action": "scroll", "scroll_direction": "down", "scroll_amount": 2, "coordinate": [20, 30]}
        self.client.tools.call("computer.use", action, runtime_id="br_test")
        self.client.tools.start("computer.use", action, runtime_id="br_test")
        for request in MockHandler.requests:
            self.assertEqual(request["body"], action)
            self.assertEqual(request["headers"]["Bctrl-Runtime-Id"], "br_test")

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

    def test_agent_keys_send_identity_and_retain_person_and_usage_metadata(self) -> None:
        created = self.client.api_keys.create(type="agent", agent={"name": "Invoice bot"})
        self.assertEqual(MockHandler.requests[0]["body"], {"type": "agent", "agent": {"name": "Invoice bot"}})
        self.assertEqual(created["data"]["actsFor"], {"userId": "person-1"})
        self.assertEqual(created["data"]["agent"]["name"], "Invoice bot")
        self.assertIsNone(created["data"]["lastUsedAt"])

    def test_spaces_and_browser_start_use_current_routes(self) -> None:
        secrets = {"allow": ["prod"], "deny": ["prod/root"],
                   "env": {"OPENAI_API_KEY": "secret:prod/api#value@3"}}
        space = self.client.spaces.create(name="automation", environment={"secrets": secrets})
        self.assertEqual(MockHandler.requests[0]["body"],
                         {"name": "automation", "environment": {"secrets": secrets}})
        started = self.client.browsers.start("br_test", idempotency_key="start-1")
        runtime = self.client.browsers.get("br_test", wait=2)
        run = self.client.runs.get("run_test", include="usage")
        self.assertEqual(space["id"], "sp_test")
        self.assertEqual(started["currentRun"]["id"], "run_test")
        self.assertEqual(MockHandler.requests[1]["headers"]["Idempotency-Key"], "start-1")
        self.assertEqual(MockHandler.requests[2]["path"], "/v1/browsers/br_test?wait=2")
        self.assertEqual(MockHandler.requests[3]["path"], "/v1/runs/run_test?include=usage")
        self.assertIn("connections", runtime["currentRun"])
        self.assertIn("connections", run)

    def test_tools_and_conversations_are_first_class(self) -> None:
        result = self.client.tools.call(
            "stagehand.act",
            {"instruction": "Click Continue"},
            runtime_id="br_test",
        )
        conversation = self.client.conversations.update("conv_test", model="openai/gpt-5")
        turn = self.client.conversations.messages.create(
            "conv_test", text="Continue", idempotency_key="message-1"
        )
        self.assertTrue(result["success"])
        self.assertEqual(MockHandler.requests[0]["headers"]["Bctrl-Runtime-Id"], "br_test")
        self.assertNotIn("runtimeId", MockHandler.requests[0]["body"])
        self.assertNotIn("agent", conversation)
        self.assertEqual(turn["status"], "queued")
        self.assertEqual(MockHandler.requests[2]["headers"]["Idempotency-Key"], "message-1")

    def test_started_browser_uses_create_and_exposes_current_connections(self) -> None:
        with self.client.browsers.started_browser(idempotency_key="create-1") as runtime:
            self.assertEqual(runtime.id, "br_context")
            self.assertEqual(runtime.run_id, "run_context")
            self.assertEqual(runtime.cdp_url, "wss://example.test/context/devtools")
            self.assertEqual(runtime.webdriver_url, "https://example.test/context/webdriver")
            self.assertEqual(runtime.live_view_url, "https://example.test/context/view")

        self.assertEqual(MockHandler.requests[0]["path"], "/v1/browsers?wait=60")
        self.assertEqual(MockHandler.requests[0]["headers"]["Idempotency-Key"], "create-1")
        self.assertEqual(MockHandler.requests[0]["body"], {})
        self.assertEqual(MockHandler.requests[1]["path"], "/v1/browsers/br_context/stop")

    def test_legacy_execution_namespaces_are_absent(self) -> None:
        self.assertFalse(hasattr(self.client, "invocations"))
        self.assertFalse(hasattr(self.client, "vault"))
        self.assertFalse(hasattr(self.client, "runtimes"))
        self.assertFalse(hasattr(self.client.browsers, "targets"))
        self.assertFalse(hasattr(self.client.browsers, "human_actions"))

    def test_browser_lifecycle_keeps_state_controls_and_run_history_separate(self) -> None:
        self.client.browsers.stop("br_test", discard_state=True, idempotency_key="stop-1")
        self.client.browsers.update("br_test", recording=False, space_id="default")
        runs = list(self.client.browsers.iter_runs("br_test", include="usage", status="ended"))
        self.assertEqual(runs[0]["id"], "run_test")
        self.client.browsers.revoke_connections("br_test", idempotency_key="revoke-1")
        self.client.browsers.delete("br_test")
        self.assertEqual([request["path"] for request in MockHandler.requests], [
            "/v1/browsers/br_test/stop", "/v1/browsers/br_test?spaceId=default",
            "/v1/browsers/br_test/runs?include=usage&status=ended",
            "/v1/browsers/br_test/connections/revoke", "/v1/browsers/br_test",
        ])
        self.assertEqual(MockHandler.requests[0]["body"], {"discardState": True})
        self.assertEqual(MockHandler.requests[0]["headers"]["Idempotency-Key"], "stop-1")
        self.assertEqual(MockHandler.requests[1]["body"], {"recording": False})
        self.assertEqual(MockHandler.requests[3]["body"], {})
        self.assertEqual(MockHandler.requests[3]["headers"]["Idempotency-Key"], "revoke-1")

    def test_browser_context_stops_when_entry_has_no_connection_urls(self) -> None:
        lifecycle = Mock()
        lifecycle.create.return_value = {"id": "br_starting", "currentRun": {"id": "run_starting", "connections": None}}
        with self.assertRaisesRegex(RuntimeError, "did not include connections"):
            with StartedBrowser(browsers=lifecycle, request={}):
                self.fail("unavailable connections cannot enter a started context")
        lifecycle.stop.assert_called_once_with("br_starting")

    def test_browser_context_preserves_the_body_error_when_stop_also_fails(self) -> None:
        lifecycle = Mock()
        lifecycle.create.return_value = browser_response("br_context", "run_context")
        lifecycle.stop.side_effect = RuntimeError("cleanup failed")
        with self.assertRaisesRegex(ValueError, "body failed"):
            with StartedBrowser(browsers=lifecycle, request={}):
                raise ValueError("body failed")
        lifecycle.stop.assert_called_once_with("br_context")

    def test_code_execute_uses_async_tool_call_route(self) -> None:
        result = self.client.tools.start(
            "code.execute",
            {"source": "export default async () => ({ ok: true });", "input": {"value": 1}},
            runtime_id="br_test",
            idempotency_key="code-execute-1",
        )

        self.assertEqual(result["id"], "call_code")
        request = MockHandler.requests[0]
        self.assertEqual(request["path"], "/v1/tools/code.execute/calls")
        self.assertEqual(request["headers"]["Bctrl-Runtime-Id"], "br_test")
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
        self.assertEqual(list(self.client.locations.iter(limit=1, order="asc"))[0]["id"], "us-east")

        self.assertEqual(MockHandler.requests[0]["path"], "/v1/files/file_test/content")
        self.assertEqual(MockHandler.requests[1]["path"], "/v1/notification-recipients?limit=10")
        self.assertEqual(MockHandler.requests[2]["body"]["type"], "email")
        self.assertEqual(MockHandler.requests[3]["body"]["enabled"], False)
        self.assertEqual(MockHandler.requests[4]["method"], "DELETE")
        self.assertEqual(MockHandler.requests[5]["path"], "/v1/proxies/geo?country=US&type=city")
        self.assertEqual(MockHandler.requests[6]["path"], "/v1/proxies/locations?pool=pool1")
        self.assertEqual(MockHandler.requests[7]["path"], "/v1/subaccounts/sub_test?include=usage")
        self.assertEqual(MockHandler.requests[8]["path"], "/v1/locations?limit=1&order=asc")

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
        self.client.runs.files.collect("run_test", "downloads/r.pdf", filename="r.pdf")
        self.client.browsers.stop("br_test", discard_state=True)

        self.assertEqual(
            [(request["method"], request["path"]) for request in MockHandler.requests],
            [
                ("GET", "/v1/runs/run_test/files?role=input"),
                ("POST", "/v1/runs/run_test/files"),
                ("POST", "/v1/runs/run_test/files/upload"),
                ("POST", "/v1/runs/run_test/files/file_test/retry"),
                ("DELETE", "/v1/runs/run_test/files/file_test"),
                ("POST", "/v1/runs/run_test/files/collect"),
                ("POST", "/v1/browsers/br_test/stop"),
            ],
        )
        self.assertEqual(MockHandler.requests[1]["body"], {"fileId": "file_test"})
        self.assertEqual(MockHandler.requests[2]["headers"]["Idempotency-Key"], "up-1")
        self.assertIn(b'name="path"', MockHandler.requests[2]["body"])
        self.assertEqual(
            MockHandler.requests[5]["body"], {"runtimePath": "downloads/r.pdf", "filename": "r.pdf"}
        )
        self.assertEqual(MockHandler.requests[6]["body"], {"discardState": True})

    def test_file_upload_scopes_space_in_query(self) -> None:
        uploaded = self.client.files.upload(
            file=b"fixture",
            filename="fixture.txt",
            space_id="sp_test",
        )

        self.assertEqual(uploaded["id"], "file_uploaded")
        self.assertEqual(MockHandler.requests[0]["path"], "/v1/files?spaceId=sp_test")


if __name__ == "__main__":
    unittest.main()
