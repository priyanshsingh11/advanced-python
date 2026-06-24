# Day 1 — Type Hints Masterclass
# File: day1_type_hints.py

"""
=========================================================
DAY 1 — TYPE HINTS MASTERCLASS
=========================================================

Goal
----
Learn why type hints exist and how they help us write
safer, more maintainable Python code.

Type hints DO NOT change how Python executes code.

They simply provide additional information to:

• Developers
• IDEs (VS Code, PyCharm)
• Static type checkers such as mypy

---------------------------------------------------------
Without Type Hints
---------------------------------------------------------

Python allows this function:

"""

def add(a, b):
    return a + b


"""
The function works correctly for integers.

"""

print(add(5, 10))

"""

But Python also allows:

"""

# print(add(5, "hello"))

"""

This causes an error only when the program runs.

TypeError:
unsupported operand type(s)

Bugs discovered at runtime can be expensive.

Type hints help catch these mistakes earlier.


=========================================================
PART 1 — Primitive Type Annotations
=========================================================

Basic variable annotations.

"""

name: str = "Priyansh"

age: int = 21

height: float = 5.9

is_student: bool = True


"""
Explanation
-----------

str     → text values
int     → whole numbers
float   → decimal numbers
bool    → True or False


Examples

"""

print(name)
print(age)
print(height)
print(is_student)


"""
=========================================================
PART 2 — Function Type Annotations
=========================================================

Functions can specify

1. Parameter types
2. Return type


Syntax


def function(parameter: type) -> return_type:
    ...


Example
-------

"""


def add(a: int, b: int) -> int:
    """
    Adds two integers.

    Parameters
    ----------
    a : int
    b : int

    Returns
    -------
    int
        Sum of a and b
    """

    return a + b


print(add(10, 20))


"""
=========================================================
PART 3 — Returning Strings
=========================================================

"""


def greet(name: str) -> str:
    """
    Returns a greeting message.
    """

    return f"Hello {name}"


print(greet("Priyansh"))


"""
=========================================================
PART 4 — Returning Numerical Values
=========================================================

"""


def square(x: int) -> int:
    """
    Computes the square of a number.
    """

    return x * x


print(square(5))


"""
=========================================================
PART 5 — Area Example
=========================================================

Exercise


def area(length, width):
    return length * width


Typed Solution

"""


def area(length: float, width: float) -> float:
    """
    Calculates area of a rectangle.
    """

    return length * width


print(area(5.5, 3.2))


"""
=========================================================
EXERCISE 1
=========================================================

Convert this function into a typed version.


def volume(length, width, height):
    return length * width * height


Solution

"""


def volume(
        length: float,
        width: float,
        height: float
) -> float:
    """
    Calculates volume of a cuboid.
    """

    return length * width * height


print(volume(2, 3, 4))


"""
=========================================================
EXERCISE 2
=========================================================


def is_even(number):
    return number % 2 == 0


Solution

"""


def is_even(number: int) -> bool:
    """
    Returns True if number is even.
    """

    return number % 2 == 0


print(is_even(8))
print(is_even(11))


"""
=========================================================
EXERCISE 3
=========================================================


def full_name(first, last):
    return first + " " + last


Solution

"""


def full_name(
        first: str,
        last: str
) -> str:
    """
    Combines first and last names.
    """

    return first + " " + last


print(full_name("Priyansh", "Singh"))


"""
=========================================================
KEY TAKEAWAYS
=========================================================

✔ Type hints do not enforce types at runtime.

✔ They improve readability.

✔ They help IDEs provide better suggestions.

✔ They allow tools like mypy to detect bugs before execution.

✔ Production Python code is usually fully annotated.


Next Topics
-----------

□ Optional[X]

□ Union[X, Y]

□ Literal["a", "b"]

□ list[str]

□ dict[str, int]

□ TypeAlias

□ Generic Types

□ mypy
=========================================================
"""
