import asyncio
import io
import unittest
from unittest.mock import patch

import httpx
from bctrl import AsyncBctrl, Bctrl
from bctrl._generated.core.api_error import ApiError

def failure(code="upstream.unavailable", details=None):
    return {"error": {"code": code, "message": "Unavailable", "requestId": "req_test", "reasonClass": "upstream",
                      **({"details": details} if details is not None else {})}}


class TransportTests(unittest.TestCase):
    def test_unkeyed_writes_are_not_retried(self):
        requests = []

        def handler(request):
            requests.append(request)
            return httpx.Response(503, json=failure())

        with httpx.Client(transport=httpx.MockTransport(handler)) as transport:
            client = Bctrl(token="key", httpx_client=transport, max_retries=3)
            with self.assertRaises(ApiError):
                client.browsers.create()
        self.assertEqual(len(requests), 1)

    def test_keyed_writes_reuse_the_same_key_and_body(self):
        requests = []

        def handler(request):
            requests.append(request)
            if len(requests) == 1:
                return httpx.Response(503, json=failure())
            return httpx.Response(503, json=failure())

        with httpx.Client(transport=httpx.MockTransport(handler)) as transport, patch("time.sleep"):
            client = Bctrl(token="key", httpx_client=transport, max_retries=1)
            with self.assertRaises(ApiError):
                client.browsers.create(recording=False, idempotency_key="create-1")
        self.assertEqual(len(requests), 2)
        self.assertEqual(requests[0].headers["Idempotency-Key"], "create-1")
        self.assertEqual(requests[0].content, requests[1].content)

    def test_unknown_outcomes_and_conflicts_do_not_retry(self):
        for status, body in [(503, failure(details={"status": "unknown"})),
                             (409, {"error": {"code": "request.conflict"}})]:
            requests = []

            def handler(request):
                requests.append(request)
                return httpx.Response(status, json=body)

            with httpx.Client(transport=httpx.MockTransport(handler)) as transport:
                client = Bctrl(token="key", httpx_client=transport, max_retries=2)
                with self.assertRaises(ApiError):
                    client.browsers.create(idempotency_key="create-1")
            self.assertEqual(len(requests), 1)

    def test_multipart_browser_upload_preserves_method_query_and_bytes(self):
        requests = []

        def handler(request):
            requests.append(request)
            return httpx.Response(503, json=failure())

        data = b"\x00\xff\x80"
        with httpx.Client(transport=httpx.MockTransport(handler)) as transport:
            client = Bctrl(token="key", httpx_client=transport)
            with self.assertRaises(ApiError):
                client.browsers.files.upload("name/browser", path="/workspace/input.bin", file=("input.bin", io.BytesIO(data)), idempotency_key="upload-1")
        self.assertEqual(len(requests), 1)
        self.assertEqual(requests[0].method, "PUT")
        self.assertEqual(requests[0].url.path, "/v1/browsers/name/browser/files/content")
        self.assertEqual(requests[0].url.params["path"], "/workspace/input.bin")
        self.assertIn(data, requests[0].content)
        self.assertIn(b'name="file"', requests[0].content)

    def test_auth_redirects_are_refused_even_when_custom_httpx_client_enables_them(self):
        requests = []

        def handler(request):
            requests.append(request)
            return httpx.Response(302, headers={"location": "/v1/leak"})

        with httpx.Client(transport=httpx.MockTransport(handler), follow_redirects=True) as transport:
            client = Bctrl(token="key", httpx_client=transport)
            with self.assertRaises(ApiError):
                client.auth.whoami()
        self.assertEqual(len(requests), 1)

    def test_async_unkeyed_writes_are_not_retried(self):
        async def run():
            requests = []

            async def handler(request):
                requests.append(request)
                return httpx.Response(503, json=failure())

            async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as transport:
                client = AsyncBctrl(token="key", httpx_client=transport, max_retries=3)
                with self.assertRaises(ApiError):
                    await client.browsers.create()
            self.assertEqual(len(requests), 1)
        asyncio.run(run())

    def test_future_server_error_preserves_status_and_body_under_the_common_error_type(self):
        body = failure(code="future.failure")
        with httpx.Client(transport=httpx.MockTransport(lambda request: httpx.Response(503, json=body))) as transport:
            client = Bctrl(token="key", httpx_client=transport, max_retries=0)
            with self.assertRaises(ApiError) as raised:
                client.browsers.create()
        self.assertEqual(raised.exception.status_code, 503)
        returned = raised.exception.body
        if not isinstance(returned, dict):
            returned = returned.dict(by_alias=True, exclude_none=True)
        self.assertEqual(returned, body)

    def test_malformed_error_response_retains_http_context_under_the_common_error_type(self):
        body = {"error": {"code": "future.failure"}}
        with httpx.Client(transport=httpx.MockTransport(lambda request: httpx.Response(503, json=body))) as transport:
            client = Bctrl(token="key", httpx_client=transport, max_retries=0)
            with self.assertRaises(ApiError) as raised:
                client.browsers.create()
        self.assertEqual(raised.exception.status_code, 503)
        self.assertEqual(raised.exception.body, body)
