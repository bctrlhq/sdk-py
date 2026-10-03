import asyncio
from types import SimpleNamespace

import pytest

from bctrl import async_wait_for, wait_for


@pytest.mark.parametrize("status", ["succeeded", "failed", "cancelled", "timed_out", "unknown", "awaiting_input", "ended"])
def test_terminal_outcomes_do_not_poll_again(status):
    calls = []
    result = SimpleNamespace(status=status)

    def read():
        calls.append(True)
        return result

    assert wait_for(read, timeout=0) is result
    assert len(calls) == 1

    async def run():
        async def read_async():
            calls.append(True)
            return result
        assert await async_wait_for(read_async, timeout=0) is result

    asyncio.run(run())
    assert len(calls) == 2


def test_nonterminal_polling_and_deadline():
    results = iter([SimpleNamespace(status="running"), SimpleNamespace(status="awaiting_input")])
    assert wait_for(lambda: next(results), interval=0).status == "awaiting_input"
    with pytest.raises(TimeoutError):
        wait_for(lambda: SimpleNamespace(status="running"), timeout=0)

    async def run():
        results = iter([SimpleNamespace(status="running"), SimpleNamespace(status="unknown")])
        async def read():
            return next(results)
        assert (await async_wait_for(read, interval=0)).status == "unknown"
        async def running():
            return SimpleNamespace(status="running")
        with pytest.raises(TimeoutError):
            await async_wait_for(running, timeout=0)

    asyncio.run(run())
