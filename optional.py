"""
=========================================================
DAY 2 — OPTIONAL TYPE HINTS
File: day2_optional.py
=========================================================

Goal
----
Learn how to represent values that may or may not exist.

Optional is one of the most commonly used type hints
in production code.

Examples

• Database queries
• API responses
• Search results
• User authentication


=========================================================
PART 1 — Why Optional Exists
=========================================================

Imagine a function that searches for a user.

Sometimes the user exists.

Sometimes it doesn't.

Without type hints:

"""


def get_user():
    return None


user = get_user()


"""

Looking at the code, we don't know whether
'user' is always a string or can also be None.


Type hints solve this problem.


=========================================================
PART 2 — Using Optional
=========================================================

Optional[X] means

X
OR
None


Example

"""

from typing import Optional


user: Optional[str] = None


"""

Equivalent to


user: str | None


Both mean exactly the same thing.



Optional[str]

is shorthand for


Union[str, None]


=========================================================
PART 3 — Function Example
=========================================================

"""


def find_user(user_id: int) -> Optional[str]:
    """
    Returns username if found.

    Otherwise returns None.
    """

    users = {
        1: "Priyansh",
        2: "Rahul",
        3: "Ankit"
    }

    return users.get(user_id)


print(find_user(1))
print(find_user(10))


"""

Output


Priyansh

None


=========================================================
PART 4 — Modern Python Syntax
=========================================================

Python 3.10 introduced a cleaner syntax.


"""


def get_email(user_id: int) -> str | None:
    """
    Returns email if available.
    """

    emails = {
        1: "abc@gmail.com",
        2: "xyz@gmail.com"
    }

    return emails.get(user_id)


print(get_email(1))
print(get_email(100))


"""

Both of these are identical.


Optional[str]


str | None


Preferred today


str | None


because

• shorter

• easier to read

• no import required



=========================================================
PART 5 — Checking None Safely
=========================================================

"""


def greet(user: str | None) -> None:

    if user is None:
        print("Guest User")

    else:
        print(f"Hello {user}")


greet("Priyansh")

greet(None)


"""

Output


Hello Priyansh

Guest User


=========================================================
PART 6 — Common Beginner Mistake
=========================================================

Bad


"""


def bad(user: str | None):

    print(user.upper())


"""

Problem


If user is None


None.upper()


AttributeError



Correct way


"""


def good(user: str | None):

    if user is not None:
        print(user.upper())


good("priyansh")

good(None)


"""

Output


PRIYANSH


=========================================================
Exercises
=========================================================


Exercise 1


Convert this function.


"""


def get_age(name):

    data = {
        "Priyansh": 21,
        "Rahul": 22
    }

    return data.get(name)


"""

Expected Return Type


int | None



---------------------------------------------------------


Exercise 2


Write a function


send_email(email)


that accepts


str | None


If None

print


"No email found"


Otherwise


"Sending mail to xyz@gmail.com"



=========================================================
Solutions
=========================================================

"""


def get_age(name: str) -> int | None:

    data = {
        "Priyansh": 21,
        "Rahul": 22
    }

    return data.get(name)



def send_email(email: str | None) -> None:

    if email is None:
        print("No email found")

    else:
        print(f"Sending mail to {email}")


send_email("abc@gmail.com")

send_email(None)



"""
=========================================================
KEY TAKEAWAYS
=========================================================

✔ Optional[X] means X or None

✔ Optional[str] == str | None

✔ Prefer str | None in Python 3.10+

✔ Always check for None before using methods

✔ Optional is heavily used in APIs,
  databases and backend applications


Next Topic
----------

□ Union

□ Literal

□ Generics

□ mypy


=========================================================
"""
