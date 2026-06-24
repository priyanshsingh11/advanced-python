"""
=========================================================
DAY 1 — PYDANTIC V2 FUNDAMENTALS
File: day1_pydantic_basics.py
=========================================================

Goal
----
Learn the most important features of Pydantic v2.

Topics covered

✔ BaseModel

✔ Request / Response Models

✔ Field Validators

✔ Field Constraints

✔ BaseSettings

✔ LLM Structured Outputs


Install


pip install pydantic

pip install pydantic-settings


=========================================================
PART 1 — BaseModel
=========================================================

BaseModel is essentially

A dataclass

+

Runtime Validation

+

JSON Parsing

+

Serialization


Without Pydantic


user = {

"name":"Priyansh",

"age":"21"

}


Nothing checks the data.


With Pydantic


"""

from pydantic import BaseModel


class User(BaseModel):

    name: str

    age: int


u = User(

    name="Priyansh",

    age="21"

)


print(u)


"""

Output


User(name='Priyansh', age=21)


Pydantic automatically converts

"21"

into

21



=========================================================
PART 2 — Validation Errors
=========================================================

"""


try:

    User(

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
PART 3 — Request / Response Models
=========================================================


FastAPI heavily relies on these.


Request


"""


class CreateUserRequest(

        BaseModel

):


    name: str


    age: int



Response


"""


class UserResponse(

        BaseModel

):


    id: int


    name: str


    age: int



"""

FastAPI example


@app.post(

"/users",

response_model=UserResponse

)

def create_user(

request: CreateUserRequest

):

    ...


"""


=========================================================
PART 4 — Field Validators
=========================================================

"""


from pydantic import field_validator



class Student(

        BaseModel

):


    age: int



    @field_validator(

        "age"

    )

    @classmethod
    def validate_age(

            cls,

            value

    ):


        if value < 0:

            raise ValueError(

                "Age cannot be negative"

            )


        return value



print(

Student(

age=20

)

)



"""

Try


Student(

age=-5

)


ValidationError



=========================================================
PART 5 — Field Constraints
=========================================================

"""

from pydantic import Field



class Employee(

        BaseModel

):


    name: str = Field(

        min_length=3,

        max_length=30

    )



    age: int = Field(

        gt=0,

        lt=120

    )



emp = Employee(

    name="Priyansh",

    age=21

)


print(emp)



"""

Examples


Field(

gt=0

)


Greater than zero



Field(

ge=0

)


Greater or equal



Field(

lt=100

)


Less than



Field(

le=100

)


Less or equal



=========================================================
PART 6 — BaseSettings
=========================================================

"""


from pydantic_settings import (

BaseSettings

)



class Settings(

BaseSettings

):


    OPENAI_API_KEY: str


    DB_URL: str


    DEBUG: bool = False



"""



.env


OPENAI_API_KEY=abc123


DB_URL=postgres://localhost


DEBUG=True




settings = Settings()



print(

settings.DEBUG

)



Pydantic automatically loads

.env

and converts


"True"


into


True




=========================================================
PART 7 — Serialization
=========================================================

"""


user = User(

    name="Priyansh",

    age=21

)



print(

user.model_dump()

)



"""

Output


{


'name': 'Priyansh',

'age': 21

}



JSON


print(

user.model_dump_json()

)



=========================================================
PART 8 — Parsing JSON
=========================================================

"""


payload = {

"name":"Rahul",

"age":"22"

}



student = User.model_validate(

payload

)



print(

student

)



=========================================================
PART 9 — LLM Structured Outputs
=========================================================

"""


class Resume(

BaseModel

):


    name: str


    years_of_experience: int


    skills: list[str]



"""

Suppose GPT returns


"""

llm_output = {

"name":"Priyansh",

"years_of_experience":2,

"skills":[

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

If GPT returns


"""

{

"name":"Priyansh",

"years_of_experience":"five"

}


"""

Pydantic raises


ValidationError



No bad data enters the system.




=========================================================
PART 10 — Dataclass vs Pydantic
=========================================================


Dataclass


✔ Lightweight

✔ Fast

❌ No validation

❌ No JSON support




Pydantic


✔ Validation

✔ FastAPI integration

✔ Env configs

✔ LLM outputs

✔ JSON parsing




=========================================================
MENTAL MODEL
=========================================================


JSON


↓


Pydantic Model


↓


Validation


↓


Safe Python Object


↓


Business Logic




=========================================================
Exercises
=========================================================


Exercise 1


Create


Product


name


price


stock




Exercise 2


Validate


price > 0




Exercise 3


Create Settings


API_KEY


HOST


PORT




=========================================================
KEY TAKEAWAYS
=========================================================


✔ BaseModel validates data


✔ field_validator adds custom rules


✔ Field provides constraints


✔ BaseSettings loads .env


✔ model_validate parses dictionaries


✔ model_dump converts to dict


✔ model_dump_json returns JSON


✔ Pydantic is the backbone of


FastAPI


and


LLM structured outputs



=========================================================
"""
