# AUTO-GENERATED FILE - DO NOT EDIT
# Generated from: openapi/sdk-openapi.json
# Run `pnpm generate:sdk-contracts` to regenerate.

from __future__ import annotations

from typing import Any, Literal, Mapping, TypeAlias, TypedDict, overload
from typing_extensions import NotRequired, Required
from urllib.parse import quote

JsonObject: TypeAlias = dict[str, Any]

class BuiltinToolBrowserPagesActivateInput(TypedDict):
    pageId: str

class BuiltinToolBrowserPagesActivateOutput(TypedDict):
    active: bool
    id: str
    title: str
    url: str

class BuiltinToolBrowserPagesCloseInput(TypedDict):
    pageId: str

class BuiltinToolBrowserPagesCloseOutput(TypedDict):
    active: bool
    id: str
    title: str
    url: str

class BuiltinToolBrowserPagesGetInput(TypedDict):
    pageId: str

class BuiltinToolBrowserPagesGetOutput(TypedDict):
    active: bool
    id: str
    title: str
    url: str

class BuiltinToolBrowserPagesListInput(TypedDict):
    pass

BuiltinToolBrowserPagesListOutput: TypeAlias = list[dict[str, Any]]

class BuiltinToolBrowserPagesOpenInput(TypedDict):
    url: NotRequired[str]

class BuiltinToolBrowserPagesOpenOutput(TypedDict):
    active: bool
    id: str
    title: str
    url: str

class BuiltinToolBrowserSetInputFilesInput(TypedDict):
    fileIds: list[str]
    pageId: NotRequired[str]
    selector: str

class BuiltinToolBrowserSetInputFilesOutput(TypedDict):
    files: list[dict[str, Any]]

class BuiltinToolCaptchaSolveInput(TypedDict):
    pageId: NotRequired[str]
    timeoutMs: NotRequired[int]

class BuiltinToolCaptchaSolveOutput(TypedDict):
    artifact: NotRequired[Any]
    duration: NotRequired[float]
    error: NotRequired[str]
    kind: NotRequired[Literal["token", "fields", "cookie", "text", "click_points", "grid", "browser_state"]]
    reason: NotRequired[Literal["no_captcha", "unsupported", "rate_limited", "page_not_attached", "solve_failed", "apply_failed"]]
    success: bool
    token: NotRequired[str]
    type: NotRequired[Literal["recaptcha_v2", "recaptcha_v3", "turnstile", "hcaptcha", "geetest_v3", "geetest_v4", "arkose", "prosopo", "mtcaptcha", "lemin", "friendly_captcha", "amazon_waf", "altcha", "datadome", "basilisk", "yidun", "tendi"]]
    workerUserAgent: NotRequired[str]

class BuiltinToolCaptchaStatusInput(TypedDict):
    pageId: NotRequired[str]

class BuiltinToolCaptchaStatusOutput(TypedDict):
    enabled: bool
    pages: list[dict[str, Any]]

class BuiltinToolCaptchaWaitInput(TypedDict):
    pageId: NotRequired[str]
    timeoutMs: NotRequired[int]

class BuiltinToolCaptchaWaitOutput(TypedDict):
    enabled: bool
    pages: list[dict[str, Any]]

class BuiltinToolCodeExecuteInput(TypedDict):
    input: NotRequired[JsonObject]
    language: NotRequired[Literal["typescript"]]
    maxLogBytes: NotRequired[int]
    source: str
    timeoutMs: NotRequired[int]

class BuiltinToolFilesListInput(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]
    prefix: NotRequired[str]

class BuiltinToolFilesListOutput(TypedDict):
    files: list[dict[str, Any]]
    nextCursor: str | None

class BuiltinToolFilesReadTextInput(TypedDict):
    fileId: str
    maxBytes: NotRequired[int]
    maxLines: NotRequired[int]

class BuiltinToolFilesReadTextOutput(TypedDict):
    bytes: int
    fileId: str
    lines: int
    text: str
    truncated: bool

class BuiltinToolHumanRequestInput(TypedDict):
    expiresInSeconds: NotRequired[int]
    handoff: NotRequired[bool]
    prompt: str
    responseSchema: NotRequired[JsonObject]
    view: NotRequired[dict[str, Any]]

class BuiltinToolRunFilesAddInput(TypedDict):
    fileId: str

class BuiltinToolRunFilesAddOutput(TypedDict):
    binding: dict[str, Any] | None
    createdAt: str
    fileId: str
    name: str
    role: Literal["input", "output"]
    runtimePath: str | None
    size: int
    sourcePath: str | None
    spacePath: str

class BuiltinToolRunFilesCollectInput(TypedDict):
    name: NotRequired[str]
    path: NotRequired[str]
    runtimePath: str

class BuiltinToolRunFilesCollectOutput(TypedDict):
    binding: dict[str, Any] | None
    createdAt: str
    fileId: str
    name: str
    role: Literal["input", "output"]
    runtimePath: str | None
    size: int
    sourcePath: str | None
    spacePath: str

class BuiltinToolRunFilesExportInput(TypedDict):
    fileIds: NotRequired[list[str]]
    name: NotRequired[str]

class BuiltinToolRunFilesExportOutput(TypedDict):
    fileId: str
    name: str
    size: int

class BuiltinToolRunFilesListInput(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]
    role: NotRequired[Literal["input", "output"]]

class BuiltinToolRunFilesListOutput(TypedDict):
    data: list[dict[str, Any]]
    nextCursor: str | None

class BuiltinToolRuntimeFilesListInput(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]
    path: NotRequired[str]

class BuiltinToolRuntimeFilesListOutput(TypedDict):
    entries: list[dict[str, Any]]
    nextCursor: str | None

class BuiltinToolSecretsFillInput(TypedDict):
    field: NotRequired[Literal["username", "password", "value"]]
    frameId: NotRequired[str]
    pageId: NotRequired[str]
    passwordSelector: NotRequired[str]
    secret: str
    selector: NotRequired[str]
    usernameSelector: NotRequired[str]

class BuiltinToolSecretsFillOutput(TypedDict):
    filled: list[Literal["username", "password", "value"]]
    origin: str

class BuiltinToolSecretsListInput(TypedDict):
    cursor: NotRequired[str]
    delimiter: NotRequired[Literal["/"]]
    limit: NotRequired[int]
    prefix: NotRequired[str]
    type: NotRequired[Literal["login", "value"]]

class BuiltinToolSecretsListOutput(TypedDict):
    data: list[dict[str, Any]]
    folders: list[str]
    nextCursor: str | None

class BuiltinToolStagehandActInput(TypedDict):
    instruction: str
    pageId: NotRequired[str]
    timeoutMs: NotRequired[int]

class BuiltinToolStagehandActOutput(TypedDict):
    actionDescription: str
    actions: list[dict[str, Any]]
    cacheStatus: NotRequired[Literal["HIT", "MISS"]]
    message: str
    success: bool

class BuiltinToolStagehandExtractInput(TypedDict):
    instruction: str
    pageId: NotRequired[str]
    schema: NotRequired[JsonObject]
    timeoutMs: NotRequired[int]

class BuiltinToolStagehandExtractOutput(TypedDict):
    cacheStatus: NotRequired[Literal["HIT", "MISS"]]
    value: JsonValue

class BuiltinToolStagehandObserveInput(TypedDict):
    instruction: str
    pageId: NotRequired[str]
    timeoutMs: NotRequired[int]

class BuiltinToolStagehandObserveOutput(TypedDict):
    actions: list[dict[str, Any]]
    cacheStatus: NotRequired[Literal["HIT", "MISS"]]

class JsonObject(TypedDict):
    pass

JsonValue: TypeAlias = Any


class BuiltinToolsClient:
    """Generated, exactly typed built-in Tool operations."""

    def __init__(self, http: Any) -> None:
        self._http = http

    @overload
    def call(self, tool_ref: Literal["browser.pages.activate"], input: BuiltinToolBrowserPagesActivateInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> BuiltinToolBrowserPagesActivateOutput: ...

    @overload
    def call(self, tool_ref: Literal["browser.pages.close"], input: BuiltinToolBrowserPagesCloseInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> BuiltinToolBrowserPagesCloseOutput: ...

    @overload
    def call(self, tool_ref: Literal["browser.pages.get"], input: BuiltinToolBrowserPagesGetInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> BuiltinToolBrowserPagesGetOutput: ...

    @overload
    def call(self, tool_ref: Literal["browser.pages.list"], input: BuiltinToolBrowserPagesListInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> BuiltinToolBrowserPagesListOutput: ...

    @overload
    def call(self, tool_ref: Literal["browser.pages.open"], input: BuiltinToolBrowserPagesOpenInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> BuiltinToolBrowserPagesOpenOutput: ...

    @overload
    def call(self, tool_ref: Literal["browser.setInputFiles"], input: BuiltinToolBrowserSetInputFilesInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> BuiltinToolBrowserSetInputFilesOutput: ...

    @overload
    def call(self, tool_ref: Literal["captcha.solve"], input: BuiltinToolCaptchaSolveInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> BuiltinToolCaptchaSolveOutput: ...

    @overload
    def call(self, tool_ref: Literal["captcha.status"], input: BuiltinToolCaptchaStatusInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> BuiltinToolCaptchaStatusOutput: ...

    @overload
    def call(self, tool_ref: Literal["captcha.wait"], input: BuiltinToolCaptchaWaitInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> BuiltinToolCaptchaWaitOutput: ...

    @overload
    def call(self, tool_ref: Literal["files.list"], input: BuiltinToolFilesListInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> BuiltinToolFilesListOutput: ...

    @overload
    def call(self, tool_ref: Literal["files.read_text"], input: BuiltinToolFilesReadTextInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> BuiltinToolFilesReadTextOutput: ...

    @overload
    def call(self, tool_ref: Literal["run.files.add"], input: BuiltinToolRunFilesAddInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> BuiltinToolRunFilesAddOutput: ...

    @overload
    def call(self, tool_ref: Literal["run.files.collect"], input: BuiltinToolRunFilesCollectInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> BuiltinToolRunFilesCollectOutput: ...

    @overload
    def call(self, tool_ref: Literal["run.files.export"], input: BuiltinToolRunFilesExportInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> BuiltinToolRunFilesExportOutput: ...

    @overload
    def call(self, tool_ref: Literal["run.files.list"], input: BuiltinToolRunFilesListInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> BuiltinToolRunFilesListOutput: ...

    @overload
    def call(self, tool_ref: Literal["runtime.files.list"], input: BuiltinToolRuntimeFilesListInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> BuiltinToolRuntimeFilesListOutput: ...

    @overload
    def call(self, tool_ref: Literal["secrets.fill"], input: BuiltinToolSecretsFillInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> BuiltinToolSecretsFillOutput: ...

    @overload
    def call(self, tool_ref: Literal["secrets.list"], input: BuiltinToolSecretsListInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> BuiltinToolSecretsListOutput: ...

    @overload
    def call(self, tool_ref: Literal["stagehand.act"], input: BuiltinToolStagehandActInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> BuiltinToolStagehandActOutput: ...

    @overload
    def call(self, tool_ref: Literal["stagehand.extract"], input: BuiltinToolStagehandExtractInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> BuiltinToolStagehandExtractOutput: ...

    @overload
    def call(self, tool_ref: Literal["stagehand.observe"], input: BuiltinToolStagehandObserveInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> BuiltinToolStagehandObserveOutput: ...

    @overload
    def call(self, tool_ref: str, input: Mapping[str, Any] | None = None, *, idempotency_key: str | None = None, runtime_id: str | None = None, **kwargs: Any) -> Any: ...

    def call(self, tool_ref: str, input: Mapping[str, Any] | None = None, *, idempotency_key: str | None = None, runtime_id: str | None = None, **kwargs: Any) -> Any:
        return self._http.request(
            "POST",
            f"/tools/{quote(tool_ref, safe='')}/call",
            json_body=_body({**dict(input or {}), **kwargs}),
            idempotency_key=idempotency_key,
            headers={"BCTRL-Runtime-Id": runtime_id} if runtime_id else None,
        )

    @overload
    def start(self, tool_ref: Literal["browser.pages.activate"], input: BuiltinToolBrowserPagesActivateInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> JsonObject: ...

    @overload
    def start(self, tool_ref: Literal["browser.pages.close"], input: BuiltinToolBrowserPagesCloseInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> JsonObject: ...

    @overload
    def start(self, tool_ref: Literal["browser.pages.open"], input: BuiltinToolBrowserPagesOpenInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> JsonObject: ...

    @overload
    def start(self, tool_ref: Literal["browser.setInputFiles"], input: BuiltinToolBrowserSetInputFilesInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> JsonObject: ...

    @overload
    def start(self, tool_ref: Literal["captcha.solve"], input: BuiltinToolCaptchaSolveInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> JsonObject: ...

    @overload
    def start(self, tool_ref: Literal["code.execute"], input: BuiltinToolCodeExecuteInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> JsonObject: ...

    @overload
    def start(self, tool_ref: Literal["human.request"], input: BuiltinToolHumanRequestInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> JsonObject: ...

    @overload
    def start(self, tool_ref: Literal["run.files.add"], input: BuiltinToolRunFilesAddInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> JsonObject: ...

    @overload
    def start(self, tool_ref: Literal["run.files.collect"], input: BuiltinToolRunFilesCollectInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> JsonObject: ...

    @overload
    def start(self, tool_ref: Literal["run.files.export"], input: BuiltinToolRunFilesExportInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> JsonObject: ...

    @overload
    def start(self, tool_ref: Literal["stagehand.act"], input: BuiltinToolStagehandActInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> JsonObject: ...

    @overload
    def start(self, tool_ref: Literal["stagehand.extract"], input: BuiltinToolStagehandExtractInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> JsonObject: ...

    @overload
    def start(self, tool_ref: Literal["stagehand.observe"], input: BuiltinToolStagehandObserveInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> JsonObject: ...

    @overload
    def start(self, tool_ref: str, input: Mapping[str, Any] | None = None, *, idempotency_key: str | None = None, runtime_id: str | None = None, **kwargs: Any) -> JsonObject: ...

    def start(self, tool_ref: str, input: Mapping[str, Any] | None = None, *, idempotency_key: str | None = None, runtime_id: str | None = None, **kwargs: Any) -> JsonObject:
        return self._http.request(
            "POST",
            f"/tools/{quote(tool_ref, safe='')}/calls",
            json_body=_body({**dict(input or {}), **kwargs}),
            idempotency_key=idempotency_key,
            headers={"BCTRL-Runtime-Id": runtime_id} if runtime_id else None,
        )


def _body(values: Mapping[str, Any]) -> JsonObject:
    return {_wire_key(key): value for key, value in values.items() if value is not None}


def _wire_key(key: str) -> str:
    head, *tail = key.split("_")
    return head + "".join(part[:1].upper() + part[1:] for part in tail if part)
