import asyncio

async def sat_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    task1 = asyncio.create_task(sat_after(1, 'hello'))
    task2 = asyncio.create_task(sat_after(2, 'world'))
    await task1
    await task2
    await use_gather()

async def use_gather():
    await asyncio.gather(
        sat_after(1, 'Task 1'),
        sat_after(2, 'Task 2')
    )

    """
    try:
    await asyncio.wait_for(some_coroutine(), timeout=5)
except asyncio.TimeoutError:
    print("Operation timed out!")

    """



asyncio.run(main())