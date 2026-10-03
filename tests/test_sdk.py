"""Transport regressions using typed response fixtures from Fern 1.65.1."""
from __future__ import annotations

import copy
import json
import re
from pathlib import Path
from types import SimpleNamespace

import httpx
import pytest

from bctrl import Bctrl

FIXTURES = json.loads(Path(__file__).with_name("api-fixtures.json").read_text())
BROWSER = json.loads(Path(__file__).with_name("browser.json").read_text())


@pytest.fixture
def sdk():
    requests = []

    def send(request):
        raw = request.read()
        body = json.loads(raw) if raw and request.headers.get("content-type", "").startswith("application/json") else raw or None
        requests.append({"method": request.method, "path": str(request.url.raw_path, "utf8"), "body": body, "headers": request.headers})
        route = request.url.path
        if route.endswith("/content"):
            return httpx.Response(200, content=b"file contents")
        if route.startswith("/v1/browsers") or route == "/v1/runs/run_test":
            browser = copy.deepcopy(BROWSER)
            browser["id"] = "br_test"
            browser["currentRun"]["id"] = "run_test"
            browser["currentRun"]["resourceId"] = "br_test"
            if route.endswith("/runs"):
                response = {"data": [browser["currentRun"]], "nextCursor": None, "hasMore": False}
            elif route == "/v1/runs/run_test":
                response = browser["currentRun"]
                response.pop("connections", None)
            elif request.method == "DELETE":
                response = {"object": "deleted", "id": "br_test", "deleted": True}
            else:
                response = browser
            return httpx.Response(200, json=response)
        if re.fullmatch(r"/v1/tools/[^/]+/call", route):
            return httpx.Response(200, json={"success": True, "action": (body or {}).get("action"), "width": 800, "height": 600})
        for key, value in FIXTURES.items():
            method, template = key.split(" ", 1)
            if method != request.method or not re.fullmatch(re.sub(r"\{[^}]+\}", "[^/]+", template), route):
                continue
            response = copy.deepcopy(value)
            if route == "/v1/api-keys" and method == "POST":
                response["data"].update({"type": "agent", "agent": {"name": body["agent"]["name"]}, "actsFor": {"userId": "person-1"}, "lastUsedAt": None})
            return httpx.Response(200, json=response)
        raise AssertionError(f"Unhandled {request.method} {route}")

    with httpx.Client(transport=httpx.MockTransport(send)) as transport:
        yield Bctrl(token="test-key", base_url="https://api.example.test", httpx_client=transport), requests


def test_computer_actions_preserve_vendor_snake_case_fields(sdk):
    client, requests = sdk
    action = {"action": "scroll", "scroll_direction": "down", "scroll_amount": 2, "coordinate": [20, 30]}
    assert client.tools.call("computer.use", request=action, bctrl_runtime_id="br_test")["width"] == 800
    client.tools.calls.create("computer.use", request=action, bctrl_runtime_id="br_test")
    for request in requests:
        assert request["body"] == action
        assert request["headers"]["BCTRL-Runtime-Id"] == "br_test"


def test_agent_keys_send_identity_and_retain_person_and_usage_metadata(sdk):
    client, requests = sdk
    created = client.api_keys.create(request={"type": "agent", "agent": {"name": "Invoice bot"}})
    assert requests[0]["body"] == {"type": "agent", "agent": {"name": "Invoice bot"}}
    assert created.data.type == "agent"
    assert created.data.agent.name == "Invoice bot"
    assert created.data.acts_for.user_id
    assert hasattr(created.data, "last_used_at")


def test_spaces_and_browser_start_use_current_routes(sdk):
    client, requests = sdk
    secrets = {"allow": ["prod"], "deny": ["prod/root"], "env": {"OPENAI_API_KEY": "secret:prod/api#value@3"}}
    client.spaces.create(name="automation", environment={"secrets": secrets})
    assert requests[0]["body"] == {"name": "automation", "environment": {"secrets": secrets}}
    started = client.browsers.start("br_test", idempotency_key="start-1")
    browser = client.browsers.get("br_test", wait=2)
    run = client.runs.get("run_test", include="usage")
    assert started.current_run.id == "run_test"
    assert requests[1]["headers"]["Idempotency-Key"] == "start-1"
    assert requests[2]["path"] == "/v1/browsers/br_test?wait=2"
    assert requests[3]["path"] == "/v1/runs/run_test?include=usage"
    assert browser.current_run.connections.cdp_url
    assert run.id == "run_test"
    assert run.connections is None


def test_tools_and_conversations_are_first_class(sdk):
    client, requests = sdk
    assert client.tools.call("stagehand.act", request={"instruction": "Click Continue"}, bctrl_runtime_id="br_test")["success"]
    client.conversations.update("conv_test", model="deepseek/deepseek-v4.1-flash")
    client.conversations.messages.create("conv_test", text="Continue", idempotency_key="message-1")
    assert requests[0]["headers"]["BCTRL-Runtime-Id"] == "br_test"
    assert "runtimeId" not in requests[0]["body"]
    assert requests[2]["headers"]["Idempotency-Key"] == "message-1"


def test_scoped_browser_exposes_current_connections_and_stops(sdk):
    client, requests = sdk
    with client.browsers.with_browser(idempotency_key="create-1") as browser:
        assert browser.current_run.id == "run_test"
        assert browser.current_run.connections.cdp_url
    assert [(r["method"], r["path"]) for r in requests] == [("POST", "/v1/browsers"), ("POST", "/v1/browsers/br_test/stop?wait=60")]
    assert requests[0]["headers"]["Idempotency-Key"] == "create-1"
    assert requests[0]["body"] == {}


def test_legacy_execution_namespaces_are_absent(sdk):
    client, _ = sdk
    for name in ("invocations", "vault", "runtimes"):
        assert not hasattr(client, name)
    for name in ("targets", "human_actions"):
        assert not hasattr(client.browsers, name)


def test_browser_lifecycle_keeps_state_controls_and_run_history_separate(sdk):
    client, requests = sdk
    client.browsers.stop("br_test", discard_state=True, idempotency_key="stop-1")
    client.browsers.update("br_test", recording=False)
    assert [run.id for run in client.paginate(client.browsers.runs.list, "br_test", include="usage", status="ended")] == ["run_test"]
    client.browsers.connections.revoke("br_test", idempotency_key="revoke-1")
    client.browsers.delete("br_test")
    assert requests[0]["body"] == {"discardState": True}
    assert requests[0]["headers"]["Idempotency-Key"] == "stop-1"
    assert requests[1]["body"] == {"recording": False}
    assert requests[2]["path"].split("?")[0] == "/v1/browsers/br_test/runs"
    assert requests[3]["body"] == {}
    assert requests[3]["headers"]["Idempotency-Key"] == "revoke-1"
    assert requests[4]["method"] == "DELETE"


def test_scoped_browser_stops_after_connection_failure(sdk):
    client, requests = sdk
    playwright = SimpleNamespace(chromium=SimpleNamespace(connect_over_cdp=lambda _: (_ for _ in ()).throw(RuntimeError("connection failed"))))
    with pytest.raises(RuntimeError, match="connection failed"):
        with client.browsers.with_browser() as browser:
            browser.connect(playwright)
    assert requests[-1]["path"].startswith("/v1/browsers/br_test/stop")


def test_scoped_browser_preserves_body_error_if_stop_also_fails(sdk):
    client, _ = sdk
    client.browsers.stop = lambda *args, **kwargs: (_ for _ in ()).throw(RuntimeError("cleanup failed"))
    with pytest.raises(ValueError, match="body failed") as raised:
        with client.browsers.with_browser():
            raise ValueError("body failed")
    assert str(raised.value.__cause__) == "cleanup failed"


def test_code_execute_uses_async_tool_call_route(sdk):
    client, requests = sdk
    client.tools.calls.create("code.execute", request={"source": "export default async () => ({ ok: true });", "input": {"value": 1}}, bctrl_runtime_id="br_test", idempotency_key="code-execute-1")
    assert requests[0]["path"] == "/v1/tools/code.execute/calls"
    assert requests[0]["headers"]["BCTRL-Runtime-Id"] == "br_test"
    assert requests[0]["headers"]["Idempotency-Key"] == "code-execute-1"
    assert requests[0]["body"]["input"] == {"value": 1}


def test_files_notifications_proxy_catalog_and_subaccounts_use_current_routes(sdk):
    client, requests = sdk
    assert b"".join(client.files.content("file_test")) == b"file contents"
    client.notification_recipients.list(limit=10)
    client.notification_recipients.create(type="email", value="user@example.com")
    client.notification_recipients.update("nrec_test", enabled=False)
    client.notification_recipients.delete("nrec_test")
    client.proxies.geo.list(country="US", type="city")
    client.proxies.locations.list(pool="pool1")
    client.subaccounts.get("sub_test", include="usage")
    client.locations.list(limit=1, order="asc")
    assert requests[2]["body"]["type"] == "email"
    assert requests[3]["body"]["enabled"] is False
    assert requests[4]["method"] == "DELETE"
    assert requests[5]["path"] == "/v1/proxies/geo?country=US&type=city"
    assert requests[6]["path"] == "/v1/proxies/locations?pool=pool1"
    assert requests[7]["path"] == "/v1/subaccounts/sub_test?include=usage"


def test_secrets_use_stable_ids_and_preserve_write_only_fields(sdk):
    client, requests = sdk
    secret = "sec_u1234567890123456789012"
    client.secrets.list(prefix="prod/", delimiter="/")
    client.secrets.create(path="prod/github/bot", type="login", password="p")
    client.secrets.get(secret)
    client.secrets.update(secret, password="p", if_match='"3"')
    client.secrets.update(secret, from_version=2)
    client.secrets.update(secret, totp=None)
    client.secrets.delete(secret, if_match='"4"')
    client.secrets.reveal(secret, version=3)
    client.secrets.versions(secret, limit=5)
    assert requests[1]["body"] == {"path": "prod/github/bot", "type": "login", "password": "p"}
    assert requests[3]["headers"]["If-Match"] == '"3"'
    assert requests[4]["body"] == {"fromVersion": 2}
    assert requests[5]["body"] == {"totp": None}
    assert requests[6]["headers"]["If-Match"] == '"4"'
    assert requests[7]["path"] == f"/v1/secrets/{secret}/reveal"
    assert requests[7]["body"] == {"version": 3}
    assert requests[8]["path"] == f"/v1/secrets/{secret}/versions?limit=5"


def test_run_files_use_the_run_file_routes(sdk):
    client, requests = sdk
    client.runs.files.list("run_test", role="input")
    client.runs.files.add("run_test", file_id="file_test")
    client.runs.files.upload("run_test", file=b"x", filename="a.txt", path="docs/a.txt", idempotency_key="up-1")
    client.runs.files.retry("run_test", "file_test")
    client.runs.files.remove("run_test", "file_test")
    client.runs.files.collect("run_test", runtime_path="downloads/r.pdf", filename="r.pdf")
    client.browsers.stop("br_test", discard_state=True)
    assert requests[1]["body"] == {"fileId": "file_test"}
    assert requests[2]["headers"]["Idempotency-Key"] == "up-1"
    assert b'name="path"' in requests[2]["body"]
    assert requests[5]["body"] == {"runtimePath": "downloads/r.pdf", "filename": "r.pdf"}
    assert requests[6]["body"] == {"discardState": True}


def test_file_upload_scopes_space_in_query(sdk):
    client, requests = sdk
    client.files.upload(file=b"fixture", filename="fixture.txt", space_id="sp_test")
    assert requests[0]["path"] == "/v1/files?spaceId=sp_test"
    assert b"fixture" in requests[0]["body"]
