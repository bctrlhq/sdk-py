"""Runtime lifecycle context managers."""

from __future__ import annotations

from dataclasses import dataclass
from types import TracebackType
from typing import Any, Mapping, Optional, Protocol


JsonObject = dict[str, Any]


class RuntimeLifecycleClient(Protocol):
    def create(self, **request: Any) -> JsonObject: ...

    def start(self, runtime_id: str, *, idempotency_key: Optional[str] = None) -> JsonObject: ...

    def stop(self, runtime_id: str) -> JsonObject: ...


@dataclass
class StartedRuntime:
    """Context manager that creates, starts, and stops a browser runtime."""

    runtimes: RuntimeLifecycleClient
    request: Mapping[str, Any]
    idempotency_key: Optional[str] = None

    runtime: JsonObject | None = None
    start: JsonObject | None = None

    def __enter__(self) -> "StartedRuntime":
        if self.runtime is not None:
            raise RuntimeError("Runtime context has already been entered")
        runtime = self.runtimes.create(**dict(self.request))
        start = self.runtimes.start(runtime["id"], idempotency_key=self.idempotency_key)
        self.runtime = runtime
        self.start = start
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        if self.runtime is not None:
            try:
                self.runtimes.stop(self.runtime["id"])
            except Exception:
                if exc_type is None:
                    raise

    @property
    def id(self) -> str:
        return self._runtime_value("id")

    @property
    def runtime_id(self) -> str:
        return self.id

    @property
    def run_id(self) -> str:
        return self._start_value("runId")

    @property
    def connect_url(self) -> str:
        return self._start_value("connectUrl")

    @property
    def protocol(self) -> str:
        return self._start_value("protocol")

    def _runtime_value(self, key: str) -> str:
        if self.runtime is None:
            raise RuntimeError("Runtime context has not been entered")
        value = self.runtime.get(key)
        if not isinstance(value, str):
            raise RuntimeError(f"Runtime response did not include {key}")
        return value

    def _start_value(self, key: str) -> str:
        if self.start is None:
            raise RuntimeError("Runtime context has not been entered")
        value = self.start.get(key)
        if not isinstance(value, str):
            raise RuntimeError(f"Runtime start response did not include {key}")
        return value
