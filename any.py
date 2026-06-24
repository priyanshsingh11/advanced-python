"""
=========================================================
DAY 6 — ANY
File: day6_any.py
=========================================================

Goal
----
Understand what Any means and why it should be
used sparingly.

Any essentially disables static type checking.

Think of it as telling mypy

"I don't know the type."

or

"I don't care."


=========================================================
PART 1 — Why Any Exists
=========================================================

Sometimes we interact with

• Third-party libraries

• Legacy code

• Dynamic JSON responses


For these situations,
Any can be useful.


=========================================================
PART 2 — Using Any
=========================================================
"""

from typing import Any


def foo(x: Any):

    return x


print(foo(10))
print(foo("Hello"))
print(foo([1, 2, 3]))


"""
All of these work.


Mypy will NOT complain.



=========================================================
PART 3 — Type Safety is Lost
=========================================================
"""


def dangerous(x: Any):

    return x.upper()


print(dangerous("hello"))


"""
Even this passes mypy.


dangerous(10)


Mypy says nothing.


At runtime


AttributeError


10.upper()



=========================================================
PART 4 — Better Alternative
=========================================================
"""


def better(x: str):

    return x.upper()


print(better("hello"))


"""
Now mypy catches


better(10)



=========================================================
PART 5 — Appropriate Uses
=========================================================


Good


response: dict[str, Any]


Bad


name: Any


age: Any


salary: Any



=========================================================
KEY TAKEAWAYS
=========================================================

✔ Any disables type checking

✔ Use only when necessary

✔ Avoid spreading Any everywhere

✔ Senior engineers dislike excessive Any

✔ Prefer precise types whenever possible


=========================================================
"""
