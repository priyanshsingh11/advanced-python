
"""
===========================================
Context Managers Practice (code.py)
===========================================

Run one example at a time.

Topics Covered:
1. Basic with statement
2. Exception handling
3. Custom Context Manager (__enter__/__exit__)
4. contextlib.contextmanager
5. Timing execution
"""

# ==========================================================
# Example 1 : Reading a File using "with"
# ==========================================================

print("=" * 50)
print("Example 1 : Reading File")
print("=" * 50)

# Create a sample file
with open("sample.txt", "w") as f:
    f.write("Hello World!\n")
    f.write("Context Managers are awesome!")

# Read the file
with open("sample.txt", "r") as f:
    print(f.read())

print("\n")


# ==========================================================
# Example 2 : Automatic Cleanup after Exception
# ==========================================================

print("=" * 50)
print("Example 2 : Exception Handling")
print("=" * 50)

try:
    with open("sample.txt", "r") as f:
        print(f.readline())

        # Simulate an error
        raise ValueError("Something went wrong!")

except Exception as e:
    print("Caught Exception:", e)

print("Notice: File is already closed automatically.\n")


# ==========================================================
# Example 3 : Creating Your Own Context Manager
# Using __enter__ and __exit__
# ==========================================================

print("=" * 50)
print("Example 3 : Custom Context Manager")
print("=" * 50)


class DatabaseConnection:

    def __enter__(self):
        print("Connecting to Database...")
        return self

    def query(self):
        print("Executing SQL Query...")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing Database Connection")


with DatabaseConnection() as db:
    db.query()

print()


# ==========================================================
# Example 4 : __exit__ runs even after exception
# ==========================================================

print("=" * 50)
print("Example 4 : Cleanup after Exception")
print("=" * 50)

try:

    with DatabaseConnection() as db:
        db.query()
        raise Exception("Database Error!")

except Exception as e:
    print(e)

print()


# ==========================================================
# Example 5 : contextlib.contextmanager
# ==========================================================

print("=" * 50)
print("Example 5 : @contextmanager")
print("=" * 50)

from contextlib import contextmanager


@contextmanager
def my_context():
    print("Setup Resource")

    yield

    print("Cleanup Resource")


with my_context():
    print("Inside with block")

print()


# ==========================================================
# Example 6 : Timer Context Manager
# ==========================================================

print("=" * 50)
print("Example 6 : Timer")
print("=" * 50)

import time


@contextmanager
def timer():
    start = time.time()

    yield

    end = time.time()

    print(f"Execution Time : {end-start:.5f} seconds")


with timer():
    total = sum(range(10000000))

print()


# ==========================================================
# Example 7 : Understanding yield
# ==========================================================

print("=" * 50)
print("Example 7 : yield Position")
print("=" * 50)


@contextmanager
def demo():
    print("Before yield (Setup)")

    yield

    print("After yield (Cleanup)")


with demo():
    print("Running Main Code")

print()


# ==========================================================
# Example 8 : What actually happens internally
# ==========================================================

print("=" * 50)
print("Example 8 : Internal Working")
print("=" * 50)

file = open("sample.txt", "r")

try:
    print(file.readline())

finally:
    file.close()
    print("File Closed (finally block)")

print()


# ==========================================================
# Example 9 : Nested Context Managers
# ==========================================================

print("=" * 50)
print("Example 9 : Nested Context Managers")
print("=" * 50)

with open("sample.txt", "r") as f1, open("copy.txt", "w") as f2:
    for line in f1:
        f2.write(line)

print("File copied successfully!")

print()


# ==========================================================
# Example 10 : Check __enter__ and __exit__
# ==========================================================

print("=" * 50)
print("Example 10 : Understanding Flow")
print("=" * 50)


class Demo:

    def __enter__(self):
        print("__enter__ Called")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("__exit__ Called")


with Demo():
    print("Inside with block")

print()


# ==========================================================
# END
# ==========================================================
