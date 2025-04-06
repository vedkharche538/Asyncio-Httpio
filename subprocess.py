import asyncio

async def run_subprocess():
    process = await asyncio.create_subprocess_shell(
        "ls -l",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    stdout, stderr = await process.communicate()

    print(f"stdout: {stdout.decode()}")