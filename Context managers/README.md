# Context Managers (`with` & `contextlib.contextmanager`)

## What is a Context Manager?

A **context manager** is an object that automatically manages the setup and cleanup of a resource.

It ensures that resources are **always released**, even if an exception occurs.

Common resources include:

* Files
* Database connections
* Network connections
* Thread locks
* Temporary files

---

# Why Do We Need It?

Without a context manager, you have to manually clean up resources.

```python
file = open("data.txt")

content = file.read()

file.close()
```

If an exception occurs before `file.close()`, the file remains open, causing a **resource leak**.

Example:

```python
file = open("data.txt")

content = file.read()

raise Exception("Something went wrong")

file.close()      # Never executed
```

---

# Using `with`

The `with` statement automatically handles cleanup.

```python
with open("data.txt") as file:
    content = file.read()
```

Python automatically calls `file.close()` when the block finishes, even if an error occurs.

---

# What Happens Internally?

```python
with open("data.txt") as file:
    print(file.read())
```

is conceptually similar to

```python
file = open("data.txt")

try:
    print(file.read())
finally:
    file.close()
```

The `finally` block guarantees cleanup.

---

# How Context Managers Work

Every context manager implements two special methods:

```python
__enter__()
__exit__()
```

Flow:

```
__enter__()

↓

Execute with block

↓

__exit__()
```

* `__enter__()` → Setup resource
* `__exit__()` → Cleanup resource

---

# Creating a Context Manager

Python provides `contextlib.contextmanager` to easily create one.

```python
from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.time()

    yield

    end = time.time()
    print(f"Execution Time: {end - start:.4f} seconds")
```

Usage:

```python
with timer():
    sum(range(1_000_000))
```

Output:

```
Execution Time: 0.08 seconds
```

---

# Why `yield` is Used

In a context manager:

* Code **before** `yield` → Setup
* Code **after** `yield` → Cleanup

Example:

```python
from contextlib import contextmanager

@contextmanager
def demo():
    print("Setup")

    yield

    print("Cleanup")
```

Usage:

```python
with demo():
    print("Inside Block")
```

Output:

```
Setup
Inside Block
Cleanup
```

---

# Real-World Examples

## Reading Files

```python
with open("users.csv") as file:
    data = file.read()
```

---

## SQLite Database

```python
import sqlite3

with sqlite3.connect("users.db") as conn:
    conn.execute("SELECT * FROM users")
```

---

## Temporary Files

```python
import tempfile

with tempfile.NamedTemporaryFile() as file:
    file.write(b"Hello")
```

---

## Thread Lock

```python
import threading

lock = threading.Lock()

with lock:
    print("Critical Section")
```

The lock is automatically released.

---

# Why Companies Use Context Managers

Imagine an API receiving thousands of requests.

Without cleanup:

```
Open Database Connection

↓

Process Request

↓

Exception

↓

Connection Never Closed ❌
```

After enough requests:

```
Too Many Open Connections

↓

Database Stops Accepting Requests
```

With a context manager:

```
Open Connection

↓

Process Request

↓

Automatically Close Connection ✅
```

No resource leaks.

---

# Advantages

* Automatic cleanup
* Prevents resource leaks
* Exception-safe
* Cleaner and more readable code
* Standard Python practice
* Widely used in production systems

---

# Interview Points

**Q. What is a context manager?**

A context manager is an object that automatically manages resource setup and cleanup using the `with` statement.

---

**Q. Why use `with`?**

It guarantees that resources are released even if an exception occurs.

---

**Q. What methods make an object a context manager?**

* `__enter__()`
* `__exit__()`

---

**Q. What does `@contextmanager` do?**

It lets you create a context manager using a generator function with `yield` instead of manually implementing `__enter__()` and `__exit__()`.

---

# Quick Revision

```
Context Manager
        │
        ├── Manages resources automatically
        ├── Used with the "with" statement
        ├── Calls __enter__()
        ├── Executes your code
        ├── Calls __exit__()
        ├── Cleanup always happens
        └── Prevents resource leaks
```

---

# One-Line Summary

> A context manager guarantees that resources are properly initialized and cleaned up, making code safer, cleaner, and resistant to resource leaks even when exceptions occur.
