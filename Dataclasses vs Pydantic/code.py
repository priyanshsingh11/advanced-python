"""
=========================================================
DATACLASSES vs PYDANTIC
=========================================================

Golden Rule

Dataclass
=
Trusted internal Python objects


Pydantic
=
Anything crossing a boundary


Examples of boundaries

✔ HTTP Requests

✔ HTTP Responses

✔ LLM Outputs

✔ Environment Variables

✔ Database Payloads

✔ Message Queues

=========================================================
PART 1 — Dataclass
=========================================================

Dataclasses are lightweight containers.

Python automatically creates

✔ __init__()

✔ __repr__()

✔ __eq__()

for us.

No validation happens.

"""

from dataclasses import dataclass


@dataclass
class User:

    name: str
    age: int


u = User(

    name="Priyansh",

    age=21

)

print(u)



"""
Output

User(name='Priyansh', age=21)


---------------------------------------------------------

Dataclass trusts whatever you give it.

"""


u = User(

    name="Priyansh",

    age="21"

)

print(type(u.age))


"""
Output


<class 'str'>


No validation occurred.


=========================================================
PART 2 — Pydantic
=========================================================

Pydantic validates data.

It converts compatible types.

Raises ValidationError otherwise.

"""


from pydantic import BaseModel


class PUser(BaseModel):

    name: str

    age: int


u = PUser(

    name="Priyansh",

    age="21"

)


print(u)

print(type(u.age))


"""
Output


PUser(name='Priyansh', age=21)


<class 'int'>


Pydantic converted

"21"

into

21


=========================================================
PART 3 — Validation Errors
=========================================================

"""


try:

    PUser(

        name="Priyansh",

        age="hello"

    )

except Exception as e:

    print(e)



"""
Output


ValidationError


Input should be a valid integer


=========================================================
PART 4 — API Request Example
=========================================================

Data coming from outside the application.

Use Pydantic.

"""


class CreateUserRequest(

        BaseModel

):


    name: str


    age: int



request = CreateUserRequest(

    name="Rahul",

    age="25"

)


print(request)


"""
FastAPI does this automatically.



=========================================================
PART 5 — LLM Output Example
=========================================================

Suppose GPT returns JSON.


Use Pydantic.


"""


class Resume(

        BaseModel

):


    name: str


    years_of_experience: int


    skills: list[str]



llm_output = {

    "name": "Priyansh",

    "years_of_experience": 2,

    "skills": [

        "Python",

        "FastAPI"

    ]

}



resume = Resume.model_validate(

    llm_output

)



print(

    resume.skills

)



"""
Output


['Python', 'FastAPI']


=========================================================
PART 6 — Environment Variables
=========================================================

Pydantic can load .env files.


pip install pydantic-settings


"""


from pydantic_settings import BaseSettings



class Settings(

BaseSettings

):


    API_KEY: str


    DEBUG: bool = False



# settings = Settings()


# print(settings.DEBUG)



"""
=========================================================
PART 7 — Internal Business Objects
=========================================================

After validation,
we usually use dataclasses internally.


"""


@dataclass
class ScoreBreakdown:

    technical: float

    communication: float

    presentation: float



scores = ScoreBreakdown(

    technical=90,

    communication=85,

    presentation=88

)


print(scores)



"""
=========================================================
Cheat Sheet
=========================================================


Dataclass


✔ Lightweight

✔ Fast

✔ Internal objects


❌ Validation

❌ JSON Parsing

❌ .env support




Pydantic


✔ Validation

✔ FastAPI

✔ Serialization

✔ LLM Outputs

✔ .env support


❌ Slightly slower



=========================================================
Mental Model
=========================================================


Outside World


↓

Pydantic


↓

Validated Objects


↓

Business Logic


↓

Dataclasses


↓

Internal Processing


=========================================================
"""
