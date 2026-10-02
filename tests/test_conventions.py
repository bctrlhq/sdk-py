import io
import json
import unittest
from unittest.mock import patch
from urllib.error import HTTPError

from bctrl.http import V1HttpClient
from bctrl.errors import BctrlPermissionError


class ConventionTests(unittest.TestCase):
    def test_version_and_error_context(self):
        payload = {"error": {
            "message": "Denied", "code": "auth.forbidden", "requestId": "req-test",
            "hint": "Grant the scope.", "reasonClass": "capability_denied",
            "details": {"scope": "computer"}, "future": True,
        }}

        def reject(request, **kwargs):
            self.assertEqual(request.get_header("Bctrl-version"), "2026-10-01")
            raise HTTPError(request.full_url, 403, "Forbidden", {"content-type": "application/json"},
                            io.BytesIO(json.dumps(payload).encode()))

        with patch("bctrl.http.urlopen", side_effect=reject):
            with self.assertRaises(BctrlPermissionError) as raised:
                V1HttpClient(api_key="test-key", max_retries=0).request("GET", "/spaces")
        error = raised.exception
        self.assertEqual(str(error), "Denied")
        self.assertEqual(error.code, "auth.forbidden")
        self.assertEqual(error.request_id, "req-test")
        self.assertEqual(error.hint, "Grant the scope.")
        self.assertEqual(error.reason_class, "capability_denied")
        self.assertEqual(error.details, {"scope": "computer"})
