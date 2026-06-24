"""
=========================================================
DAY 5 — GENERICS
File: day5_generics.py
=========================================================

Goal
----
Understand generic container types.

Generics describe

What type of data exists inside containers.


Examples


list[str]

dict[str,int]

tuple[int,str]

set[float]



=========================================================
PART 1 — Lists
=========================================================

"""


names: list[str] = [

    "Alice",

    "Bob"

]


print(names)



"""

Meaning


A list

containing only strings



=========================================================
PART 2 — Integer Lists
=========================================================

"""


scores: list[int] = [

    90,

    80,

    75

]


print(scores)



"""

Only integers allowed.



=========================================================
PART 3 — Dictionaries
=========================================================

"""


marks: dict[str, int] = {

    "math": 95,

    "physics": 88

}


print(marks)



"""

Meaning


Key

→ str


Value

→ int



=========================================================
PART 4 — Nested Containers
=========================================================

"""


students: dict[str, list[int]] = {

    "Alice": [90, 80],

    "Bob": [70, 60]

}


print(students)



"""

Meaning


Dictionary


Keys


str



Values


list[int]



=========================================================
PART 5 — List of Dictionaries
=========================================================

"""


users: list[dict[str, int]] = [

    {"age": 20},

    {"age": 30}

]


print(users)



=========================================================
PART 6 — Functions
=========================================================

"""


def average(scores: list[int]) -> float:

    return sum(scores) / len(scores)


print(

    average(

        [90, 80, 70]

    )

)



=========================================================
PART 7 — Even More Nested
=========================================================

"""


data: dict[str, list[dict[str, int]]] = {

    "users": [

        {"age": 20},

        {"age": 25}

    ]

}


print(data)



=========================================================
Exercises
=========================================================


Exercise 1


Create


products


list[str]




Exercise 2


Create


inventory


dict[str,int]




Exercise 3


Create


classes


dict[str,list[str]]




=========================================================
Solutions
=========================================================

"""


products: list[str] = [

    "Keyboard",

    "Mouse"

]



inventory: dict[str, int] = {

    "Keyboard": 10,

    "Mouse": 5

}



classes: dict[str, list[str]] = {

    "Math": [

        "Alice",

        "Bob"

    ]

}



"""
=========================================================
KEY TAKEAWAYS
=========================================================

✔ list[str]


List of strings



✔ list[int]


List of integers



✔ dict[str,int]


String keys

Integer values



✔ dict[str,list[int]]


Dictionary


↓

Lists


↓

Integers



✔ Nested generics are common in APIs


=========================================================
"""
