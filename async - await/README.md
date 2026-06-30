# Async Programming in Python (`async`, `await`, `asyncio`)

## What is Asynchronous Programming?

Asynchronous programming allows a program to **start a task, pause while waiting for slow operations (I/O), and continue doing other work instead of blocking the entire program**.

Typical slow operations include:

* API Requests
* Database Queries
* Reading/Writing Files
* Network Calls
* Waiting for User Input

Instead of waiting, Python can switch to another task.

---

# Why Do We Need Async?

Imagine making three API calls.

### Synchronous

```text
API 1 (2 sec)

↓

API 2 (2 sec)

↓

API 3 (2 sec)

Total = 6 seconds
```

Each task waits for the previous one.

---

### Asynchronous

```text
API 1 (2 sec)
API 2 (2 sec)
API 3 (2 sec)

↓

All finish together

Total ≈ 2 seconds
```

Tasks run concurrently while waiting for I/O.

---

# `async`

`async` defines a coroutine (an asynchronous function).

Example:

```python
async def fetch_data():
    ...
```

Calling it does **not** execute it immediately.

It returns a coroutine object.

---

# `await`

`await` pauses the current coroutine until another coroutine finishes.

Example:

```python
result = await fetch_data()
```

While waiting, Python can run other coroutines.

---

# Running an Async Program

Use:

```python
import asyncio

asyncio.run(main())
```

This starts the event loop.

---

# Event Loop

The event loop is the scheduler of async programs.

It continuously checks:

```text
Task Ready?

↓

Run It

↓

Waiting?

↓

Switch to another task
```

Only one thread is used, but many tasks can make progress.

---

# `asyncio.sleep()`

Never use `time.sleep()` inside async code.

Wrong:

```python
time.sleep(2)
```

Blocks the entire program.

Correct:

```python
await asyncio.sleep(2)
```

Only pauses the current coroutine.

---

# `asyncio.gather()`

Runs multiple coroutines concurrently.

Example:

```python
results = await asyncio.gather(
    fetch_user(),
    fetch_orders(),
    fetch_products()
)
```

Instead of waiting one after another, all begin together.

---

# Async Generators

An async generator uses both:

* `async`
* `yield`

Example:

```python
async def stream():
    for i in range(5):
        await asyncio.sleep(1)
        yield i
```

Consume it with:

```python
async for value in stream():
    print(value)
```

---

# Normal Generator vs Async Generator

Normal:

```python
def numbers():
    yield 1
```

Loop:

```python
for n in numbers():
    ...
```

---

Async:

```python
async def numbers():
    yield 1
```

Loop:

```python
async for n in numbers():
    ...
```

---

# `gather()` vs Normal Await

Sequential:

```python
await task1()

await task2()

await task3()
```

Runs one after another.

Concurrent:

```python
await asyncio.gather(
    task1(),
    task2(),
    task3()
)
```

Runs all together.

---

# Real-World Examples

## API Calls

```python
await fetch_weather()

await fetch_news()
```

Better:

```python
await asyncio.gather(
    fetch_weather(),
    fetch_news()
)
```

---

## Database Queries

```python
await db.fetch_user()

await db.fetch_orders()
```

---

## FastAPI

Every request handler is usually:

```python
async def endpoint():
    ...
```

FastAPI uses async to serve many users efficiently.

---

## LLM Streaming

```python
async def stream():
    for token in model.stream():
        yield token
```

Each generated token is immediately sent to the frontend.

---

## Web Scraping

Instead of downloading websites one by one,

download many simultaneously.

---

# Advantages

* Faster for I/O-bound tasks
* Handles many users
* Lower memory usage than many threads
* Ideal for APIs and web servers
* Perfect for streaming responses

---

# Important Notes

Async **does not make CPU-heavy work faster**.

Bad candidates:

* Image Processing
* Machine Learning Training
* Large Matrix Operations

Good candidates:

* API Calls
* Database Queries
* File I/O
* Network Communication

---

# Interview Questions

### What is a coroutine?

A function defined using `async def`.

---

### What does `await` do?

Pauses the current coroutine until another coroutine finishes while allowing the event loop to execute other coroutines.

---

### What is the event loop?

The scheduler that runs asynchronous tasks and switches between them whenever one is waiting.

---

### What does `asyncio.gather()` do?

Runs multiple coroutines concurrently and waits for all of them to complete.

---

### What is an async generator?

A generator created using `async def` and `yield`, consumed using `async for`.

---

### Difference between Threading and Async?

| Threading                | Async                    |
| ------------------------ | ------------------------ |
| Multiple OS threads      | Usually one thread       |
| Context switching by OS  | Event loop scheduling    |
| Good for CPU-bound tasks | Good for I/O-bound tasks |

---

# Quick Revision

```text
async
    ↓
Creates coroutine

await
    ↓
Wait without blocking

asyncio.run()
    ↓
Starts event loop

asyncio.gather()
    ↓
Runs multiple coroutines concurrently

async generator
    ↓
Streams values asynchronously

FastAPI / LLM Streaming
    ↓
Uses async extensively
```

---

# One-Line Summary

> Async programming allows Python to efficiently handle many I/O-bound tasks concurrently by pausing waiting tasks with `await` and letting the event loop execute other work.
