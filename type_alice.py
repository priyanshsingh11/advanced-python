"""
=========================================================
DAY 7 — TYPE ALIASES
File: day7_type_aliases.py
=========================================================

Goal
----
Make complicated types easier to read.

Without aliases,
large type annotations become unreadable.


=========================================================
PART 1 — The Problem
=========================================================
"""


def average(
    scores: dict[str, list[int]]
):
    pass


"""
This works.


But imagine seeing this
twenty times in a project.


dict[str,list[int]]

dict[str,list[int]]

dict[str,list[int]]



Messy.


=========================================================
PART 2 — Type Alias
=========================================================
"""


StudentScores = dict[str, list[int]]


"""
StudentScores now means


dict[str,list[int]]



=========================================================
PART 3 — Cleaner Functions
=========================================================
"""


def average(
        scores: StudentScores
):

    pass


"""
Much easier to read.



=========================================================
PART 4 — Real Example
=========================================================
"""


StudentScores = {

    "Alice": [

        90,

        85

    ],

    "Bob": [

        70,

        60

    ]

}


def compute_average(
        scores: StudentScores
):

    for name, marks in scores.items():

        avg = sum(marks) / len(marks)

        print(

            name,

            avg

        )


compute_average(StudentScores)



=========================================================
PART 5 — Modern Syntax
=========================================================

Python 3.12


from typing import TypeAlias


StudentScores: TypeAlias = \
dict[str,list[int]]



More explicit.



=========================================================
KEY TAKEAWAYS
=========================================================

✔ Type aliases improve readability

✔ Reuse complex types

✔ Great for APIs

✔ Great for nested dictionaries


=========================================================
"""
