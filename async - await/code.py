"""
=========================================
Async/Await Practice (code.py)
=========================================

Run this file to understand:
1. async functions
2. await
3. asyncio.run()
4. asyncio.gather()
5. Sequential vs Concurrent execution
6. Async generators
7. Async for
"""

import asyncio
import time


# ==========================================================
# Example 1 : Basic async function
# ==========================================================

async def hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")


print("=" * 50)
print("Example 1")
asyncio.run(hello())


# ==========================================================
# Example 2 : Sequential Execution
# ==========================================================

async def task(name, delay):
    print(f"{name} Started")
    await asyncio.sleep(delay)
    print(f"{name} Finished")


async def sequential():
    await task("Task A", 2)
    await task("Task B", 2)
    await task("Task C", 2)


print("\n" + "=" * 50)
print("Example 2 : Sequential")

start = time.perf_counter()
asyncio.run(sequential())
print(f"Time: {time.perf_counter() - start:.2f} sec")


# ==========================================================
# Example 3 : Concurrent Execution
# ==========================================================

async def concurrent():
    await asyncio.gather(
        task("Task A", 2),
        task("Task B", 2),
        task("Task C", 2),
    )


print("\n" + "=" * 50)
print("Example 3 : Concurrent")

start = time.perf_counter()
asyncio.run(concurrent())
print(f"Time: {time.perf_counter() - start:.2f} sec")


# ==========================================================
# Example 4 : Return Values
# ==========================================================

async def square(x):
    await asyncio.sleep(1)
    return x * x


async def main():
    result = await square(5)
    print("Square:", result)


print("\n" + "=" * 50)
print("Example 4")

asyncio.run(main())


# ==========================================================
# Example 5 : gather() with Return Values
# ==========================================================

async def gather_demo():
    results = await asyncio.gather(
        square(2),
        square(3),
        square(4),
    )

    print(results)


print("\n" + "=" * 50)
print("Example 5")

asyncio.run(gather_demo())


# ==========================================================
# Example 6 : Async Generator
# ==========================================================

async def counter():

    for i in range(5):
        await asyncio.sleep(1)
        yield i


async def generator_demo():

    async for value in counter():
        print(value)


print("\n" + "=" * 50)
print("Example 6")

asyncio.run(generator_demo())


# ==========================================================
# Example 7 : Simulating LLM Token Streaming
# ==========================================================

async def stream_tokens():

    tokens = [
        "Hello",
        ", ",
        "this ",
        "is ",
        "streaming!"
    ]

    for token in tokens:
        await asyncio.sleep(0.5)
        yield token


async def chat():

    async for token in stream_tokens():
        print(token, end="", flush=True)

    print()


print("\n" + "=" * 50)
print("Example 7 : LLM Streaming")

asyncio.run(chat())


# ==========================================================
# Example 8 : Multiple API Calls
# ==========================================================

async def fake_api(name):

    print(f"Calling {name}")

    await asyncio.sleep(2)

    print(f"{name} Completed")


async def api_demo():

    await asyncio.gather(
        fake_api("Users API"),
        fake_api("Orders API"),
        fake_api("Products API"),
    )


print("\n" + "=" * 50)
print("Example 8 : API Calls")

asyncio.run(api_demo())

print("\nFinished All Examples!")
