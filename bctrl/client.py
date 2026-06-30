"""Top-level BCTRL Python client."""

from __future__ import annotations

from .http import V1HttpClient
from .resources import (
    AccountClient,
    AiClient,
    ApiKeysClient,
    AuthClient,
    BrowserExtensionsClient,
    FilesClient,
    HelpClient,
    ProxiesClient,
    RunsClient,
    RuntimesClient,
    SpacesClient,
    SubaccountsClient,
    ToolCallsClient,
    ToolsetsClient,
    ToolsClient,
    UsageClient,
    VaultClient,
)


class Bctrl:
    """Synchronous client for the BCTRL public v1 API."""

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | None = None,
        timeout: float | None = None,
        max_retries: int = 2,
    ) -> None:
        self._http = V1HttpClient(
            api_key=api_key,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
        )
        self.spaces = SpacesClient(self._http)
        self.runtimes = RuntimesClient(self._http)
        self.runs = RunsClient(self._http)
        self.files = FilesClient(self._http)
        self.tools = ToolsClient(self._http)
        self.toolsets = ToolsetsClient(self._http)
        self.tool_calls = ToolCallsClient(self._http)
        self.ai = AiClient(self._http)
        self.vault = VaultClient(self._http)
        self.browser_extensions = BrowserExtensionsClient(self._http)
        self.proxies = ProxiesClient(self._http)
        self.help = HelpClient(self._http)
        self.account = AccountClient(self._http)
        self.auth = AuthClient(self._http)
        self.api_keys = ApiKeysClient(self._http)
        self.subaccounts = SubaccountsClient(self._http)
        self.usage = UsageClient(self._http)
