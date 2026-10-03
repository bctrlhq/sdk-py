from __future__ import annotations
import asyncio
import os
import time
import pytest
from bctrl import Bctrl, AsyncBctrl

LIVE = os.environ.get("BCTRL_E2E") == "1" and bool(os.environ.get("BCTRL_API_KEY"))
PNG = bytes([137, 80, 78, 71, 13, 10, 26, 10])


def options():
    return {"token": os.environ["BCTRL_API_KEY"],
            "base_url": os.environ.get("BCTRL_API_BASE_URL", "https://api.bctrl.ai").rstrip("/").removesuffix("/v1")}


@pytest.mark.skipif(not LIVE, reason="set BCTRL_E2E=1 and BCTRL_API_KEY")
def test_sync_browser_hello_preserves_cookies_after_restart():
    from playwright.sync_api import sync_playwright
    client = Bctrl(**options())
    resource = client.browsers.create(name=f"sdk-py-sync-hello-{int(time.time() * 1000)}", location="auto", wait=60)
    connected = None
    try:
        with sync_playwright() as playwright:
            try:
                connected = resource.connect(playwright)
                context = connected.contexts[0]
                page = context.pages[0] if context.pages else context.new_page()
                page.goto("https://example.com")
                assert "example domain" in page.title().lower()
                context.add_cookies([{"name": "bctrl_sdk_hello", "value": resource.id, "domain": ".example.com", "path": "/",
                                      "secure": True, "expires": time.time() + 86400}])
                image = page.screenshot()
                assert image.startswith(PNG) and len(image) > 1000
                first_run = client.browsers.get(resource.id).current_run.id
                connected.close()
                connected = None
                client.browsers.stop(resource.id, wait=60)
                client.browsers.start(resource.id, wait=60)
                restarted = client.browsers.get(resource.id)
                assert restarted.id == resource.id and restarted.current_run.id != first_run
                connected = restarted.connect(playwright)
                assert any(cookie["name"] == "bctrl_sdk_hello" and cookie["value"] == resource.id
                           for cookie in connected.contexts[0].cookies("https://example.com"))
                connected.close()
                connected = None
            finally:
                if connected:
                    connected.close()
                    connected = None
    finally:
        try:
            if connected:
                connected.close()
        finally:
            try:
                client.browsers.stop(resource.id, wait=60)
            finally:
                client.browsers.delete(resource.id)


@pytest.mark.skipif(not LIVE, reason="set BCTRL_E2E=1 and BCTRL_API_KEY")
def test_async_browser_hello_preserves_cookies_after_restart():
    from playwright.async_api import async_playwright

    async def run():
        client = AsyncBctrl(**options())
        resource = await client.browsers.create(name=f"sdk-py-async-hello-{int(time.time() * 1000)}", location="auto", wait=60)
        connected = None
        try:
            async with async_playwright() as playwright:
                try:
                    connected = await resource.connect(playwright)
                    context = connected.contexts[0]
                    page = context.pages[0] if context.pages else await context.new_page()
                    await page.goto("https://example.com")
                    assert "example domain" in (await page.title()).lower()
                    await context.add_cookies([{"name": "bctrl_sdk_hello", "value": resource.id, "domain": ".example.com", "path": "/",
                                               "secure": True, "expires": time.time() + 86400}])
                    image = await page.screenshot()
                    assert image.startswith(PNG) and len(image) > 1000
                    first_run = (await client.browsers.get(resource.id)).current_run.id
                    await connected.close()
                    connected = None
                    await client.browsers.stop(resource.id, wait=60)
                    await client.browsers.start(resource.id, wait=60)
                    restarted = await client.browsers.get(resource.id)
                    assert restarted.id == resource.id and restarted.current_run.id != first_run
                    connected = await restarted.connect(playwright)
                    assert any(cookie["name"] == "bctrl_sdk_hello" and cookie["value"] == resource.id
                               for cookie in await connected.contexts[0].cookies("https://example.com"))
                    await connected.close()
                    connected = None
                finally:
                    if connected:
                        await connected.close()
                        connected = None
        finally:
            try:
                if connected:
                    await connected.close()
            finally:
                try:
                    await client.browsers.stop(resource.id, wait=60)
                finally:
                    await client.browsers.delete(resource.id)

    asyncio.run(run())
