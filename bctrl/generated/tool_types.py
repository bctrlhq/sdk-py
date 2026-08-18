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
    prompt: str
    responseSchema: NotRequired[JsonObject]

class BuiltinToolRunFilesExportInput(TypedDict):
    fileIds: NotRequired[list[str]]
    name: NotRequired[str]

class BuiltinToolRunFilesExportOutput(TypedDict):
    fileId: str
    name: str
    size: int

class BuiltinToolRuntimeFilesCollectInput(TypedDict):
    name: NotRequired[str]
    path: str

class BuiltinToolRuntimeFilesCollectOutput(TypedDict):
    fileId: str
    name: str
    size: int

class BuiltinToolRuntimeFilesListInput(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]
    path: NotRequired[str]

class BuiltinToolRuntimeFilesListOutput(TypedDict):
    entries: list[dict[str, Any]]
    nextCursor: str | None

class BuiltinToolRuntimeFilesStageInput(TypedDict):
    fileId: str
    path: str

class BuiltinToolRuntimeFilesStageOutput(TypedDict):
    fileId: str
    path: str
    size: int

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

class BuiltinToolVaultSecretsDeleteInput(TypedDict):
    name: str

class BuiltinToolVaultSecretsDeleteOutput(TypedDict):
    deleted: Literal[True]
    name: str

class BuiltinToolVaultSecretsGetInput(TypedDict):
    name: str

class BuiltinToolVaultSecretsGetOutput(TypedDict):
    createdAt: NotRequired[str]
    hasTotp: bool
    label: NotRequired[str]
    name: str
    originPatterns: NotRequired[list[str]]
    origins: NotRequired[list[str]]
    type: Literal["login", "value"]
    updatedAt: NotRequired[str]

class BuiltinToolVaultSecretsListInput(TypedDict):
    cursor: NotRequired[str]
    hasTotp: NotRequired[bool]
    limit: NotRequired[int]
    origin: NotRequired[str]
    prefix: NotRequired[str]

class BuiltinToolVaultSecretsListOutput(TypedDict):
    nextCursor: str | None
    secrets: list[dict[str, Any]]

BuiltinToolVaultSecretsSetInput: TypeAlias = Any

class BuiltinToolVaultSecretsSetOutput(TypedDict):
    createdAt: NotRequired[str]
    hasTotp: bool
    label: NotRequired[str]
    name: str
    originPatterns: NotRequired[list[str]]
    origins: NotRequired[list[str]]
    type: Literal["login", "value"]
    updatedAt: NotRequired[str]

class BuiltinToolVaultSecretsUpdateInput(TypedDict):
    label: NotRequired[str | None]
    name: str
    notes: NotRequired[str | None]
    originPatterns: NotRequired[list[str] | None]
    origins: NotRequired[list[str] | None]
    password: NotRequired[str]
    totpSecret: NotRequired[str | None]
    username: NotRequired[str]
    value: NotRequired[str]

class BuiltinToolVaultSecretsUpdateOutput(TypedDict):
    createdAt: NotRequired[str]
    hasTotp: bool
    label: NotRequired[str]
    name: str
    originPatterns: NotRequired[list[str]]
    origins: NotRequired[list[str]]
    type: Literal["login", "value"]
    updatedAt: NotRequired[str]

class BuiltinToolVaultSecretsValueInput(TypedDict):
    name: str

BuiltinToolVaultSecretsValueOutput: TypeAlias = Any

class BuiltinToolVaultTotpGenerateInput(TypedDict):
    name: str

class BuiltinToolVaultTotpGenerateOutput(TypedDict):
    code: str

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
    def call(self, tool_ref: Literal["captcha.solve"], input: BuiltinToolCaptchaSolveInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> BuiltinToolCaptchaSolveOutput: ...

    @overload
    def call(self, tool_ref: Literal["files.list"], input: BuiltinToolFilesListInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> BuiltinToolFilesListOutput: ...

    @overload
    def call(self, tool_ref: Literal["files.read_text"], input: BuiltinToolFilesReadTextInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> BuiltinToolFilesReadTextOutput: ...

    @overload
    def call(self, tool_ref: Literal["run.files.export"], input: BuiltinToolRunFilesExportInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> BuiltinToolRunFilesExportOutput: ...

    @overload
    def call(self, tool_ref: Literal["runtime.files.collect"], input: BuiltinToolRuntimeFilesCollectInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> BuiltinToolRuntimeFilesCollectOutput: ...

    @overload
    def call(self, tool_ref: Literal["runtime.files.list"], input: BuiltinToolRuntimeFilesListInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> BuiltinToolRuntimeFilesListOutput: ...

    @overload
    def call(self, tool_ref: Literal["runtime.files.stage"], input: BuiltinToolRuntimeFilesStageInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> BuiltinToolRuntimeFilesStageOutput: ...

    @overload
    def call(self, tool_ref: Literal["stagehand.act"], input: BuiltinToolStagehandActInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> BuiltinToolStagehandActOutput: ...

    @overload
    def call(self, tool_ref: Literal["stagehand.extract"], input: BuiltinToolStagehandExtractInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> BuiltinToolStagehandExtractOutput: ...

    @overload
    def call(self, tool_ref: Literal["stagehand.observe"], input: BuiltinToolStagehandObserveInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> BuiltinToolStagehandObserveOutput: ...

    @overload
    def call(self, tool_ref: Literal["vault.secrets.delete"], input: BuiltinToolVaultSecretsDeleteInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> BuiltinToolVaultSecretsDeleteOutput: ...

    @overload
    def call(self, tool_ref: Literal["vault.secrets.get"], input: BuiltinToolVaultSecretsGetInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> BuiltinToolVaultSecretsGetOutput: ...

    @overload
    def call(self, tool_ref: Literal["vault.secrets.list"], input: BuiltinToolVaultSecretsListInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> BuiltinToolVaultSecretsListOutput: ...

    @overload
    def call(self, tool_ref: Literal["vault.secrets.set"], input: BuiltinToolVaultSecretsSetInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> BuiltinToolVaultSecretsSetOutput: ...

    @overload
    def call(self, tool_ref: Literal["vault.secrets.update"], input: BuiltinToolVaultSecretsUpdateInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> BuiltinToolVaultSecretsUpdateOutput: ...

    @overload
    def call(self, tool_ref: Literal["vault.secrets.value"], input: BuiltinToolVaultSecretsValueInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> BuiltinToolVaultSecretsValueOutput: ...

    @overload
    def call(self, tool_ref: Literal["vault.totp.generate"], input: BuiltinToolVaultTotpGenerateInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> BuiltinToolVaultTotpGenerateOutput: ...

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
    def start(self, tool_ref: Literal["captcha.solve"], input: BuiltinToolCaptchaSolveInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> JsonObject: ...

    @overload
    def start(self, tool_ref: Literal["code.execute"], input: BuiltinToolCodeExecuteInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> JsonObject: ...

    @overload
    def start(self, tool_ref: Literal["human.request"], input: BuiltinToolHumanRequestInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> JsonObject: ...

    @overload
    def start(self, tool_ref: Literal["run.files.export"], input: BuiltinToolRunFilesExportInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> JsonObject: ...

    @overload
    def start(self, tool_ref: Literal["runtime.files.collect"], input: BuiltinToolRuntimeFilesCollectInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> JsonObject: ...

    @overload
    def start(self, tool_ref: Literal["runtime.files.stage"], input: BuiltinToolRuntimeFilesStageInput, *, idempotency_key: str | None = None, runtime_id: str | None = None) -> JsonObject: ...

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
