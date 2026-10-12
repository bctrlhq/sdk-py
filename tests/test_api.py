import asyncio
import unittest

import httpx
from bctrl import AsyncBctrl, Bctrl, types
from bctrl.api import Bctrl as ApiBctrl
from bctrl._generated.errors.forbidden_error import ForbiddenError


class CurrentApiTests(unittest.TestCase):
    def test_default_import_is_the_current_client(self):
        self.assertIs(Bctrl, ApiBctrl)
    def test_generated_builtin_types_are_importable(self):
        # Importing the canonical helper also evaluates recursive and forward
        # type aliases, even though the legacy entrypoint uses frozen helpers.
        from bctrl.generated.tool_types import BuiltinToolsClient
        self.assertTrue(callable(BuiltinToolsClient.create_call))

    def test_scoped_request_and_response_aliases(self):
        requests = []

        def handler(request):
            requests.append(request)
            return httpx.Response(200, json={"data": [], "hasMore": False, "nextCursor": None})

        with httpx.Client(transport=httpx.MockTransport(handler)) as transport:
            client = Bctrl(token="test-key", base_url="https://api.invalid", bctrl_subaccount_id="sub_test", httpx_client=transport)
            page = client.spaces.list(limit=2)
        self.assertIsInstance(page, types.SpaceListResponse)
        self.assertEqual(page.data, [])
        self.assertFalse(page.has_more)
        self.assertIsNone(page.next_cursor)
        self.assertEqual(requests[0].url.path, "/v1/spaces")
        self.assertEqual(requests[0].url.params["limit"], "2")
        self.assertEqual(requests[0].headers["Authorization"], "Bearer test-key")
        self.assertEqual(requests[0].headers["BCTRL-Subaccount-Id"], "sub_test")
        self.assertEqual(requests[0].headers["BCTRL-Version"], "2026-10-03")

    def test_encoded_selector_and_future_permission_error(self):
        requests = []
        body = {"error": {"code": "future.permission_denied", "message": "Denied"}}

        def handler(request):
            requests.append(request)
            return httpx.Response(403, json=body)

        with httpx.Client(transport=httpx.MockTransport(handler)) as transport:
            client = Bctrl(token="test-key", base_url="https://api.invalid", max_retries=0, httpx_client=transport)
            with self.assertRaises(ForbiddenError) as raised:
                client.browsers.get(browser_id="br_a/b")
        self.assertEqual(requests[0].url.raw_path, b"/v1/browsers/br_a%2Fb")
        self.assertEqual(raised.exception.status_code, 403)
        self.assertEqual(raised.exception.body, body)
        self.assertEqual(len(requests), 1)

    def test_async_client_uses_same_contract(self):
        async def run():
            async def handler(request):
                self.assertEqual(request.url.path, "/v1/spaces")
                self.assertEqual(request.headers["Authorization"], "Bearer test-key")
                return httpx.Response(200, json={"data": [], "hasMore": False, "nextCursor": None})

            async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as transport:
                client = AsyncBctrl(token="test-key", base_url="https://api.invalid", httpx_client=transport)
                page = await client.spaces.list()
                self.assertEqual(page.data, [])
        asyncio.run(run())

    def test_explicit_api_version_header_is_preserved(self):
        def handler(request):
            self.assertEqual(request.headers["BCTRL-Version"], "2026-10-01")
            return httpx.Response(200, json={"data": [], "hasMore": False, "nextCursor": None})

        with httpx.Client(transport=httpx.MockTransport(handler)) as transport:
            client = Bctrl(token="test-key", base_url="https://api.invalid", headers={"bctrl-version": "2026-10-01"}, httpx_client=transport)
            client.spaces.list()
