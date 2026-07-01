# Project: Retry & Async Cache Decorators

This project combines multiple advanced Python concepts into two production-style decorators.

Topics Covered:

* Decorators
* Closures
* `*args` and `**kwargs`
* Exception Handling
* Retry Logic
* Async Functions
* Await
* Redis-style Caching
* Time-To-Live (TTL)

---

# Project 1 – Retry Decorator

## Problem

Suppose you're calling an external API.

Sometimes it fails because of:

* Network timeout
* Temporary server error
* Internet issue

Instead of failing immediately, we retry automatically.

Instead of:

```python
call_api()
```

we write

```python
@retry(times=3)
def call_api():
    ...
```

Now Python automatically retries if an exception occurs.

---

# Flow

```text
Call Function

↓

Success?
        │
   Yes ─────► Return Result

        │
       No

↓

Retry

↓

Still Failed?

↓

Retry Again

↓

Maximum Attempts?

↓

Raise Exception
```

---

# Real-World Uses

* OpenAI API
* Anthropic API
* Payment Gateways
* Database Connections
* HTTP Requests

---

# Exponential Backoff

Instead of retrying immediately:

```text
Retry

Retry

Retry
```

Wait longer after each failure.

Example:

```text
Attempt 1

↓

Wait 2 sec

↓

Attempt 2

↓

Wait 4 sec

↓

Attempt 3

↓

Wait 8 sec
```

This prevents overwhelming a busy service.

---

# Project 2 – Async Cache Decorator

## Problem

Suppose an expensive function takes 5 seconds.

```python
await get_user(42)
```

Calling it repeatedly wastes time.

Instead:

```python
@memoize(ttl=60)
async def get_user(id):
    ...
```

The first call executes the function.

The result is stored.

Subsequent calls return the cached value until the TTL expires.

---

# Flow

```text
Call Function

↓

Cache Exists?

│

Yes
↓

Return Cached Result

No
↓

Run Function

↓

Store Result

↓

Return Result
```

---

# TTL (Time To Live)

TTL determines how long cached data remains valid.

Example:

```text
Store Value

↓

60 Seconds

↓

Automatically Expire
```

After expiration, the function runs again and refreshes the cache.

---

# Why Async?

Caching is often used with:

* Redis
* Databases
* APIs

These are I/O operations.

Using async allows the event loop to serve other requests while waiting.

---

# Why Redis?

Redis stores cached data in memory.

Advantages:

* Extremely fast
* Shared across servers
* TTL support
* Reduces database load

---

# Real-World AI Example

Suppose your chatbot asks:

```text
"What is the weather in Delhi?"
```

Without cache:

```text
User 1

↓

Weather API

↓

User 2

↓

Weather API

↓

User 3

↓

Weather API
```

Many identical API calls.

With cache:

```text
User 1

↓

Weather API

↓

Cache Result

↓

User 2

↓

Return Cache

↓

User 3

↓

Return Cache
```

Much faster and cheaper.

---

# Concepts Learned

## Decorators

Wrap another function to extend its behavior without modifying its code.

---

## Closures

The decorator remembers values like:

```python
times=3
backoff=2
ttl=60
```

even after the decorator function has returned.

---

## Async

Allows waiting for I/O without blocking the event loop.

---

## Await

Suspends the coroutine until the async operation completes.

---

## Cache

Avoids repeating expensive work.

---

## Retry

Automatically handles temporary failures.

---

# Interview Questions

### Why use retry decorators?

To automatically recover from temporary failures like network issues or unavailable services.

---

### Why exponential backoff?

To avoid overwhelming a failing service by increasing the wait time between retries.

---

### What is memoization?

Caching the output of a function so repeated calls with the same inputs return instantly.

---

### Why use Redis for caching?

Redis is an in-memory data store that provides very fast reads, writes, and built-in TTL support.

---

### Why make the cache decorator async?

Because cache operations often involve network I/O (Redis), and async avoids blocking other requests.

---

# Quick Revision

```text
retry()
        │
        ├── Catch exception
        ├── Retry automatically
        ├── Optional backoff
        └── Raise if all attempts fail

memoize()
        │
        ├── Check cache
        ├── Return cached value
        ├── Otherwise execute
        ├── Store result
        └── Expire after TTL
```

---

# One-Line Summary

> Retry decorators improve reliability by automatically repeating failed operations, while async cache decorators improve performance by storing expensive results and reusing them until they expire.
