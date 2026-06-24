"""
=========================================================
DAY 10 — STRICT MODE
File: day10_strict_mode.py
=========================================================

Goal
----
Learn how companies configure mypy
for maximum type safety.


=========================================================
PART 1 — Running Strict Mode
=========================================================


Normal


mypy app.py



Strict


mypy --strict app.py



Strict mode enables many additional checks.



=========================================================
PART 2 — Missing Return Types
=========================================================
"""


def greet(name):

    return f"Hello {name}"


"""

Strict Mode


Function is missing type annotations



Correct


"""


def greet(

        name: str

) -> str:

    return f"Hello {name}"



=========================================================
PART 3 — Untyped Functions
=========================================================
"""


def add(a, b):

    return a + b


"""

Strict Mode


Function is missing annotations



Correct


"""


def add(

        a: int,

        b: int

) -> int:

    return a + b



=========================================================
PART 4 — Unsafe Any
=========================================================
"""

from typing import Any


def foo(

        x: Any

):

    return x.upper()


"""

Strict mode warns
about unsafe Any usage.



=========================================================
PART 5 — pyproject.toml
=========================================================


Create


pyproject.toml



Content


"""


"""
[tool.mypy]

strict = true

python_version = "3.12"

"""


Now simply run



mypy .



No flags needed.



=========================================================
PART 6 — Recommended Config
=========================================================


[tool.mypy]

python_version = "3.12"

strict = true

warn_unused_ignores = true

warn_return_any = true

disallow_untyped_defs = true



=========================================================
KEY TAKEAWAYS
=========================================================

✔ Companies usually enable strict mode

✔ Strict mode catches

    Missing return types

    Unsafe Any

    Untyped functions

    Bad ignores


✔ Configure mypy once

✔ Run


mypy .


before pushing code



=========================================================
"""
