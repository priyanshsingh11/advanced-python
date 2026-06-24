"""
=========================================================
DAY 8 — THE MENTAL MODEL
File: day8_mental_model.py
=========================================================

Goal
----
Develop intuition for Python typing.


Think of every type as a set.


=========================================================
PART 1 — int
=========================================================


int


Contains


1

2

3

4

5

...



Any integer belongs to this set.



=========================================================
PART 2 — str
=========================================================


str


Contains


"hello"

"abc"

"python"



=========================================================
PART 3 — Optional
=========================================================


str | None


Contains


"hello"

"abc"

None



=========================================================
PART 4 — Union
=========================================================


int | float


Contains


1

2

3.14

7.5



=========================================================
PART 5 — Literal
=========================================================


Literal["GET", "POST"]


Contains exactly


"GET"

"POST"



Nothing else.



=========================================================
PART 6 — Generic Containers
=========================================================


list[int]


Contains


[1]

[1, 2]

[5, 7, 9]



But NOT


["A"]

["A", "B"]




dict[str, int]


Contains


{"age": 20}

{"score": 95}



But NOT


{1: "Alice"}



=========================================================
PART 7 — Any
=========================================================


Any


Contains


Everything


Numbers


Strings


Lists


Functions


Objects


None



It is the universal set.


=========================================================
KEY TAKEAWAYS
=========================================================

Think of types as sets.


int


↓

all integers



str | None


↓

all strings

+

None



Literal["GET","POST"]


↓

exactly two values



Any


↓

everything



This mindset makes advanced topics

like TypeVar,

Protocols,

and Generics

much easier.


=========================================================
"""
