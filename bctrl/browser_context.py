"""Explicit browser lifecycle context manager."""

from __future__ import annotations

from dataclasses import dataclass
from types import TracebackType
from typing import Any, Mapping, Optional, Protocol

JsonObject = dict[str, Any]


class BrowserLifecycleClient(Protocol):
    def create(self, *, idempotency_key: Optional[str] = None, **request: Any) -> JsonObject: ...

    def stop(self, browser_id: str) -> JsonObject: ...


@dataclass
class StartedBrowser:
    """Create and start a browser on entry, then stop its Run on exit."""

    browsers: BrowserLifecycleClient
    request: Mapping[str, Any]
    idempotency_key: Optional[str] = None
    browser: JsonObject | None = None

    def __enter__(self) -> "StartedBrowser":
        if self.browser is not None:
            raise RuntimeError("Browser context has already been entered")
        self.browser = self.browsers.create(wait=60, idempotency_key=self.idempotency_key, **dict(self.request))
        try:
            self._connection_value("cdpUrl")
        except Exception:
            self.browsers.stop(self.id)
            raise
        return self

    def __exit__(self, exc_type: type[BaseException] | None, exc: BaseException | None,
                 traceback: TracebackType | None) -> None:
        if self.browser is not None:
            try:
                self.browsers.stop(self.id)
            except Exception:
                if exc_type is None:
                    raise

    @property
    def id(self) -> str:
        if self.browser is None:
            raise RuntimeError("Browser context has not been entered")
        value = self.browser.get("id")
        if not isinstance(value, str):
            raise RuntimeError("Browser response did not include id")
        return value

    @property
    def run_id(self) -> str:
        value = self._run().get("id")
        if not isinstance(value, str):
            raise RuntimeError("Browser response did not include a current Run id")
        return value

    @property
    def cdp_url(self) -> str:
        return self._connection_value("cdpUrl")

    @property
    def webdriver_url(self) -> str:
        return self._connection_value("webdriverUrl")

    @property
    def live_view_url(self) -> str:
        return self._connection_value("liveViewUrl")

    @property
    def live_view_read_only_url(self) -> str:
        return self._connection_value("liveViewReadOnlyUrl")

    def _run(self) -> JsonObject:
        if self.browser is None:
            raise RuntimeError("Browser context has not been entered")
        run = self.browser.get("currentRun")
        if not isinstance(run, dict):
            raise RuntimeError("Browser response did not include a current Run")
        return run

    def _connection_value(self, key: str) -> str:
        connections = self._run().get("connections")
        if not isinstance(connections, dict):
            raise RuntimeError("Browser current Run did not include connections")
        value = connections.get(key)
        if not isinstance(value, str):
            raise RuntimeError(f"Browser Run connections did not include {key}")
        return value
