"""
=========================================================
DAY 3 — UNION TYPE HINTS
File: day3_union.py
=========================================================

Goal
----
Learn how to specify that a variable or function
parameter can accept MULTIPLE valid types.

Union is useful when a value can naturally belong
to more than one type.


Examples

• int OR float

• str OR None

• list OR dict

• Path OR string


=========================================================
PART 1 — Why Union Exists
=========================================================

Suppose we want a function that accepts both
integers and floating-point numbers.


Without type hints


"""


def square(x):
    return x * x


"""

This works.


square(5)

square(5.5)


But Python also allows


square("abc")


Result


'abcabc'


Probably not what we intended.


Union lets us clearly specify
which types are acceptable.


=========================================================
PART 2 — Old Syntax
=========================================================

Before Python 3.10


"""

from typing import Union


Number = Union[int, float]


"""

Equivalent to


int OR float



Example


"""


def cube(x: Union[int, float]) -> float:
    return x ** 3


print(cube(2))
print(cube(2.5))


"""

Output


8

15.625


=========================================================
PART 3 — Modern Syntax
=========================================================

Python 3.10 introduced a cleaner syntax.


Instead of


Union[int, float]


write


int | float


No imports required.



=========================================================
PART 4 — Example: stringify
=========================================================

"""


def stringify(value: int | float) -> str:
    """
    Converts numbers into strings.
    """

    return str(value)


print(stringify(10))

print(stringify(3.14))


"""

Output


'10'

'3.14'


=========================================================
PART 5 — Example: square
=========================================================

"""


def square(x: int | float) -> int | float:
    """
    Computes square of integers
    and floating-point numbers.
    """

    return x * x


print(square(5))

print(square(5.5))


"""

Allowed


square(5)

square(5.5)



Not Allowed


square("abc")


Type checkers such as mypy
will report an error.


=========================================================
PART 6 — Union with Collections
=========================================================

Sometimes a function can accept
different container types.


"""


def process(data: list | dict) -> None:
    """
    Processes lists and dictionaries.
    """

    print(type(data))


process([1, 2, 3])

process({"a": 1})


"""

Output


<class 'list'>

<class 'dict'>


=========================================================
PART 7 — Runtime Type Checking
=========================================================

Often we need different logic
for different types.


"""


def describe(value: int | str) -> None:

    if isinstance(value, int):
        print("Integer detected")

    else:
        print("String detected")


describe(10)

describe("Hello")


"""

Output


Integer detected

String detected


=========================================================
PART 8 — Common Mistake
=========================================================

Bad


"""


def bad(x: int | str):

    return x * x


"""

Problem


If x is a string


"abc" * "abc"


TypeError



Correct


"""


def good(x: int | str):

    if isinstance(x, int):
        return x * x

    return x.upper()


print(good(5))

print(good("hello"))


"""

Output


25


HELLO



=========================================================
Exercises
=========================================================


Exercise 1


Write a function


increment(value)


Accept


int | float


Return


value + 1



---------------------------------------------------------


Exercise 2


Write


show(data)


Accept


str | list


Print


Length of object



---------------------------------------------------------


Exercise 3


Create


get_first(item)


Accept


list | tuple


Return first element



=========================================================
Solutions
=========================================================

"""


def increment(value: int | float) -> int | float:
    return value + 1



def show(data: str | list) -> None:
    print(len(data))



def get_first(item: list | tuple):

    return item[0]


print(increment(5))

print(increment(3.5))


show("Python")

show([1, 2, 3])


print(get_first([10, 20, 30]))

print(get_first(("A", "B", "C")))



"""
=========================================================
KEY TAKEAWAYS
=========================================================

✔ Union means one of several valid types

✔ Old syntax


Union[int, str]


✔ Modern syntax


int | str


✔ Prefer modern syntax in Python 3.10+


✔ Use isinstance() when behavior
depends on the actual type.


✔ Optional[str]


is simply


str | None



Next Topics
-----------

□ Literal

□ Generic Types

□ TypeVar

□ list[str]

□ dict[str, int]

□ mypy


=========================================================
"""
