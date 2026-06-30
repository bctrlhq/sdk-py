"""Typed exceptions raised by the BCTRL Python SDK."""

from __future__ import annotations

from typing import Any, Optional


class BctrlError(Exception):
    """Base class for SDK errors."""

    def __init__(
        self,
        message: str,
        *,
        code: str = "bctrl.error",
        context: Optional[dict[str, Any]] = None,
    ) -> None:
        super().__init__(message)
        self.code = code
        self.context = context or {}


class BctrlApiError(BctrlError):
    """The BCTRL API returned a non-2xx response."""

    def __init__(
        self,
        message: str,
        *,
        status_code: int,
        code: str = "api.error",
        request_id: Optional[str] = None,
        body: Any = None,
    ) -> None:
        super().__init__(
            message,
            code=code,
            context={"status_code": status_code, "request_id": request_id, "body": body},
        )
        self.status_code = status_code
        self.request_id = request_id
        self.body = body


class BctrlAuthenticationError(BctrlApiError):
    pass


class BctrlPermissionError(BctrlApiError):
    pass


class BctrlNotFoundError(BctrlApiError):
    pass


class BctrlConflictError(BctrlApiError):
    pass


class BctrlRateLimitError(BctrlApiError):
    pass


class BctrlValidationError(BctrlApiError):
    pass


class BctrlNetworkError(BctrlError):
    """The request failed before a response was received."""


def api_error_for_status(
    status_code: int,
    message: str,
    *,
    code: str = "api.error",
    request_id: Optional[str] = None,
    body: Any = None,
) -> BctrlApiError:
    cls: type[BctrlApiError]
    if status_code == 401:
        cls = BctrlAuthenticationError
    elif status_code == 403:
        cls = BctrlPermissionError
    elif status_code == 404:
        cls = BctrlNotFoundError
    elif status_code == 409:
        cls = BctrlConflictError
    elif status_code == 429:
        cls = BctrlRateLimitError
    elif status_code in (400, 422):
        cls = BctrlValidationError
    else:
        cls = BctrlApiError
    return cls(message, status_code=status_code, code=code, request_id=request_id, body=body)
