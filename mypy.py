"""
=========================================================
DAY 9 — MYPY
File: day9_mypy.py
=========================================================

Goal
----
Learn how to use mypy to detect type errors
before running Python code.

Python itself ignores type hints.

Mypy reads them and performs static analysis.


=========================================================
PART 1 — Installation
=========================================================

Install mypy


pip install mypy


Check installation


mypy --version



=========================================================
PART 2 — First Example
=========================================================

File


test.py


"""


def add(
        a: int,
        b: int
) -> int:

    return a + b


x = add(

    5,

    "10"

)


"""

Python allows this file to exist.

But mypy reports an error.


Run


mypy test.py



Output


error:

Argument 2 to "add"

has incompatible type

"str";

expected "int"



=========================================================
PART 3 — Optional Example
=========================================================
"""


def get_name() -> str | None:

    return None


name = get_name()


print(

    name.upper()

)


"""

Run


mypy test.py



Output


Item "None"

has no attribute

"upper"



Why?


name


might be


None



Correct


"""


def get_name() -> str | None:

    return None


name = get_name()


if name is not None:

    print(

        name.upper()

    )


"""

Now mypy is happy.



=========================================================
PART 4 — Another Example
=========================================================
"""


def square(x: int) -> int:

    return x * x


square(

    "abc"

)


"""

Mypy


Argument 1

has incompatible type


str


expected


int



=========================================================
PART 5 — Checking Entire Projects
=========================================================


Single file


mypy app.py



Entire folder


mypy .



=========================================================
Exercises
=========================================================


Exercise 1


Find the error


"""


def divide(

        a: int,

        b: int

) -> float:

    return a / b


result = divide(

    10,

    "2"

)



"""
Expected


mypy should complain.



=========================================================
KEY TAKEAWAYS
=========================================================

✔ Python ignores type hints

✔ mypy enforces them

✔ Catch bugs before execution

✔ Very common in production


=========================================================
"""
