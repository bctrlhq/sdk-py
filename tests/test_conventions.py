import httpx
import pytest
from bctrl import Bctrl
from bctrl._generated.errors.forbidden_error import ForbiddenError


def test_version_and_error_context():
    payload = {"error": {"message": "Denied", "code": "auth.forbidden", "requestId": "req-test", "hint": "Grant the scope.", "reasonClass": "capability_denied", "details": {"scope": "computer"}, "future": True}}

    def reject(request):
        assert request.headers["BCTRL-Version"] == "2026-10-03"
        return httpx.Response(403, json=payload)

    with httpx.Client(transport=httpx.MockTransport(reject)) as transport:
        with pytest.raises(ForbiddenError) as raised:
            Bctrl(token="test-key", max_retries=0, httpx_client=transport).spaces.list()
    assert raised.value.status_code == 403
    assert raised.value.body == payload
