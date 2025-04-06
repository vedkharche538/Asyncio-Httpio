import asyncio
from concurrent.futures import ThreadPoolExecutor


def cpu_bound_task(n):
    return sum(i*i for i  in range(n))



async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, cpu_bound_task, 1000000)

    print(result)

asyncio.run(main())