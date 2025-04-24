#!/usr/bin/env python3
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """Run wait_random n times concurrently with the given max_delay.
    Returns list of delays sorted in ascending order, without using sort().
    """
    delays = []
    for coroutine in asyncio.as_completed([wait_random(max_delay) for _ in range(n)]):
        delay = await coroutine
        delays.append(delay)
    return delays

