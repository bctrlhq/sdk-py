from __future__ import annotations

import os
import time
import unittest
from typing import Any, Callable

from bctrl import Bctrl
from pydantic import BaseModel


def _wire(value: Any) -> Any:
    return value.model_dump(mode="json", by_alias=True) if isinstance(value, BaseModel) else value


AI_MODEL = "deepseek/deepseek-v4.1-flash"
LIVE_E2E = os.environ.get("BCTRL_E2E") == "1" and bool(os.environ.get("BCTRL_API_KEY"))


@unittest.skipUnless(LIVE_E2E, "set BCTRL_E2E=1 and BCTRL_API_KEY")
class BctrlLiveE2ETest(unittest.TestCase):
    def test_gateway_agent_conversation_workflow(self) -> None:
        client = Bctrl(
            token=os.environ["BCTRL_API_KEY"],
            base_url=os.environ.get("BCTRL_API_BASE_URL", "https://api.bctrl.ai").rstrip("/").removesuffix("/v1"),
            timeout=60,
        )

        space_id: str | None = None
        runtime_id: str | None = None
        run_id: str | None = None
        conversation_id: str | None = None
        file_id: str | None = None

        try:
            space = _wire(client.spaces.create(name=f"sdk-py-agent-e2e-{int(time.time() * 1000)}"))
            space_id = self._required_string(space, "id")

            file = _wire(client.files.upload(
                file=b"Python SDK gateway workflow fixture\n",
                filename="sdk-py-workflow-fixture.txt",
                space_id=space_id,
                path="e2e/sdk-py-workflow-fixture.txt",
                metadata='{"suite":"sdk-python-gateway-e2e"}',
            ))
            file_id = self._required_string(file, "id")

            files = _wire(client.files.list(space_id=space_id, limit=100))
            self.assertTrue(any(entry.get("id") == file_id for entry in files.get("data", [])))
            self.assertEqual(
                b"".join(client.files.content(file_id)), b"Python SDK gateway workflow fixture\n"
            )

            renamed = _wire(client.files.update(file_id, filename="sdk-py-workflow-fixture-renamed.txt"))
            self.assertEqual(renamed.get("filename"), "sdk-py-workflow-fixture-renamed.txt")

            runtime = _wire(client.browsers.create(
                wait=60,
                space_id=space_id,
                name=f"sdk-py-agent-runtime-{int(time.time() * 1000)}",
                headless=True,
            ))
            runtime_id = self._required_string(runtime, "id")

            started = runtime["currentRun"]
            run_id = self._required_string(started, "id")
            self.assertEqual(started.get("resourceId"), runtime_id)
            self.assertEqual(started.get("status"), "active")

            opened = _wire(client.tools.call(
                "browser.pages.open",
                request={"url": "https://example.com"},
                bctrl_runtime_id=runtime_id,
            ))
            self.assertIsInstance(opened, dict)

            conversation = _wire(client.conversations.create(
                runtime_id=runtime_id,
                model=AI_MODEL,
                title="Python SDK gateway agent workflow",
            ))
            conversation_id = self._required_string(conversation, "id")
            self.assertEqual(conversation.get("model"), AI_MODEL)

            accepted = _wire(client.conversations.messages.create(
                conversation_id,
                text=(
                    "Use the currently open page and report its exact document title. "
                    "Reply with only the title."
                ),
                model=AI_MODEL,
                file_ids=[file_id],
            ))
            turn_id = self._required_string(accepted, "turnId")
            self.assertEqual(accepted.get("status"), "queued")
            self.assertEqual(accepted.get("runId"), run_id)

            completed = self._wait_for_assistant_message(
                client, conversation_id, turn_id, timeout_seconds=360
            )
            assistant = completed["assistant"]
            self.assertEqual(assistant.get("model"), AI_MODEL)
            self.assertIn("example domain", assistant.get("text", "").lower())
            self.assertTrue(
                any(
                    message.get("role") == "user"
                    and message.get("id") == accepted.get("messageId")
                    for message in completed["detail"].get("messages", [])
                )
            )

            run = _wire(client.runs.get(run_id, include="usage"))
            self.assertEqual(run.get("id"), run_id)
            self.assertEqual(run.get("resourceId"), runtime_id)

            trace = _wire(client.runs.trace.list(
                run_id,
                resource_type="agent_turn",
                limit=20,
            ))
            self.assertTrue(
                any(
                    span.get("resourceId") == turn_id and span.get("status") == "succeeded"
                    for span in trace.get("data", [])
                )
            )
        finally:
            if conversation_id:
                self._ignore_failure(lambda: client.conversations.cancel(conversation_id))
            if file_id:
                self._ignore_failure(lambda: client.files.delete(file_id))
            if runtime_id:
                self._ignore_failure(lambda: client.browsers.stop(runtime_id))
                self._ignore_failure(lambda: client.browsers.delete(runtime_id))
            if space_id:
                self._ignore_failure(lambda: client.spaces.delete(space_id))

    @staticmethod
    def _required_string(value: dict[str, Any], key: str) -> str:
        result = value.get(key)
        if not isinstance(result, str) or not result:
            raise AssertionError(f"response did not contain string field {key!r}: {value}")
        return result

    @staticmethod
    def _wait_for_assistant_message(
        client: Bctrl,
        conversation_id: str,
        turn_id: str,
        *,
        timeout_seconds: int,
    ) -> dict[str, Any]:
        deadline = time.monotonic() + timeout_seconds
        while time.monotonic() < deadline:
            detail = _wire(client.conversations.get(conversation_id))
            assistant = next(
                (
                    message
                    for message in detail.get("messages", [])
                    if message.get("role") == "assistant"
                    and message.get("turnId") == turn_id
                    and message.get("text")
                ),
                None,
            )
            if detail.get("status") == "idle" and assistant is not None:
                return {"detail": detail, "assistant": assistant}
            time.sleep(1)
        raise AssertionError(
            f"conversation {conversation_id} did not produce an assistant message in time"
        )

    @staticmethod
    def _ignore_failure(action: Callable[[], Any]) -> None:
        try:
            action()
        except Exception:
            pass


if __name__ == "__main__":
    unittest.main()
