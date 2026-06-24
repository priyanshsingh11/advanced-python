"""
=========================================================
PYDANTIC V2 — QUICK REVISION
=========================================================

Install

pip install pydantic
pip install pydantic-settings


---------------------------------------------------------
1. BaseModel
---------------------------------------------------------
"""

from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int


u = User(name="Priyansh", age="21")

print(u)

# age becomes 21 automatically


"""
---------------------------------------------------------
2. Validation Errors
---------------------------------------------------------
"""

try:
    User(name="Priyansh", age="hello")

except Exception as e:
    print(e)


# ValidationError


"""
---------------------------------------------------------
3. Field Validators
---------------------------------------------------------
"""

from pydantic import field_validator


class Student(BaseModel):

    age: int

    @field_validator("age")
    @classmethod
    def validate_age(cls, value):

        if value < 0:
            raise ValueError(
                "Age cannot be negative"
            )

        return value


"""
---------------------------------------------------------
4. Field Constraints
---------------------------------------------------------
"""

from pydantic import Field


class Employee(BaseModel):

    name: str = Field(
        min_length=3,
        max_length=30
    )

    age: int = Field(
        gt=0,
        lt=120
    )


"""
---------------------------------------------------------
5. BaseSettings
---------------------------------------------------------
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    OPENAI_API_KEY: str

    DB_URL: str

    DEBUG: bool = False


settings = Settings()


# Reads .env automatically


"""
---------------------------------------------------------
6. Serialization
---------------------------------------------------------
"""

user = User(
    name="Priyansh",
    age=21
)

user.model_dump()

user.model_dump_json()


"""
---------------------------------------------------------
7. Parsing Dictionaries
---------------------------------------------------------
"""

payload = {

    "name": "Rahul",

    "age": "22"

}


user = User.model_validate(
    payload
)


"""
---------------------------------------------------------
8. LLM Structured Outputs
---------------------------------------------------------
"""


class Resume(BaseModel):

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


"""
---------------------------------------------------------
Dataclass vs Pydantic
---------------------------------------------------------

Dataclass

✔ Lightweight
✔ Fast

❌ Validation
❌ JSON Parsing


Pydantic

✔ Validation

✔ FastAPI

✔ .env support

✔ LLM outputs

✔ Serialization


---------------------------------------------------------
Mental Model
---------------------------------------------------------

JSON

↓

Pydantic Model

↓

Validation

↓

Safe Python Object

↓

Business Logic


---------------------------------------------------------
Cheat Sheet
---------------------------------------------------------

BaseModel
    -> Validation

field_validator
    -> Custom rules

Field
    -> Constraints

BaseSettings
    -> .env loader

model_validate()
    -> Dict → Object

model_dump()
    -> Object → Dict

model_dump_json()
    -> Object → JSON


Rule


Dataclass

= internal Python objects


Pydantic

= anything crossing a boundary


HTTP Request

HTTP Response

Database Payload

Environment Variables

LLM Output

=========================================================
"""
