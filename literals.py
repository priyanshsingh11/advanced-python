"""
=========================================================
DAY 4 — LITERAL TYPES
File: day4_literal.py
=========================================================

Goal
----
Learn how to restrict a variable or parameter
to a fixed set of allowed values.

Literal is extremely useful in production code.

Examples

• API modes
• HTTP methods
• Log levels
• LLM model names


=========================================================
PART 1 — Why Literal Exists
=========================================================

Suppose an API supports only three modes.


fast

slow

balanced


Without typing


"""


def run(mode):
    print(mode)


run("fast")

run("banana")


"""

Python accepts both.


But "banana" makes no sense.


Literal fixes this.



=========================================================
PART 2 — Creating Literal Types
=========================================================

"""

from typing import Literal


Mode = Literal[
    "fast",
    "slow",
    "balanced"
]


"""

Mode means


Only these values are allowed


"fast"

"slow"

"balanced"



=========================================================
PART 3 — Function Example
=========================================================

"""


def run(mode: Mode) -> None:
    print(f"Running in {mode} mode")


run("fast")

run("balanced")


"""

Allowed


run("fast")

run("slow")

run("balanced")



Not Allowed


run("banana")


mypy catches this.



=========================================================
PART 4 — LLM Models
=========================================================

"""


Model = Literal[
    "gpt-4o",
    "gpt-5.5"
]


def call_llm(model: Model):

    print("Using", model)


call_llm("gpt-5.5")


"""



=========================================================
PART 5 — HTTP Methods
=========================================================

"""


HTTPMethod = Literal[
    "GET",
    "POST",
    "DELETE"
]


def request(method: HTTPMethod):

    print(method)


request("GET")


"""



=========================================================
PART 6 — Log Levels
=========================================================

"""


LogLevel = Literal[
    "INFO",
    "ERROR",
    "DEBUG"
]


def log(message: str,
        level: LogLevel):

    print(f"[{level}] {message}")


log("Connected", "INFO")

log("Failure", "ERROR")


"""



=========================================================
Exercises
=========================================================


Exercise 1


Create


Status


Literal[
"pending",
"approved",
"rejected"
]



Exercise 2


Create


Theme


Literal[
"light",
"dark"
]



=========================================================
Solutions
=========================================================

"""


Status = Literal[
    "pending",
    "approved",
    "rejected"
]


Theme = Literal[
    "light",
    "dark"
]


"""
=========================================================
KEY TAKEAWAYS
=========================================================

✔ Literal restricts values

✔ Great for APIs

✔ Great for enums

✔ mypy catches invalid values

✔ Literal improves autocomplete


=========================================================
"""
