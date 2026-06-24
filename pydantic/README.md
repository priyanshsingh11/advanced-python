# Pydantic v2 - Quick Revision

---

# Why Pydantic?

Python type hints help IDEs and tools like mypy, but they do **not validate data at runtime**.

```python
def create_user(age: int):
    pass

create_user("21")   # Python allows this
```

Pydantic adds **runtime validation**.

It ensures incoming data actually matches the expected types.

Think of Pydantic as:

```text
Type Hints
        +
Runtime Validation
        +
JSON Parsing
        +
Serialization
```

---

# 1. BaseModel

`BaseModel` is the foundation of Pydantic.

It defines the structure of your data and validates it automatically.

```python
from pydantic import BaseModel


class User(BaseModel):

    name: str
    age: int


user = User(
    name="Priyansh",
    age="21"
)

print(user)
```

Output

```text
User(name='Priyansh', age=21)
```

Pydantic automatically converts `"21"` into `21`.

---

# 2. Validation Errors

Invalid data raises a `ValidationError`.

```python
User(

    name="Priyansh",

    age="hello"

)
```

Output

```text
ValidationError

Input should be a valid integer
```

---

# 3. Request / Response Models

FastAPI uses Pydantic models for API requests and responses.

```python
class CreateUserRequest(BaseModel):

    name: str
    age: int


class UserResponse(BaseModel):

    id: int
    name: str
    age: int
```

FastAPI

```python
@app.post(

"/users",

response_model=UserResponse

)

def create_user(

request: CreateUserRequest

):

    ...
```

Benefits

✔ Automatic validation

✔ OpenAPI documentation

✔ JSON conversion

✔ Type safety


---

# 4. Field Validators

Used for custom validation rules.

Example

Age cannot be negative.

```python
from pydantic import field_validator


class Student(BaseModel):

    age: int


    @field_validator("age")
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
```

---

# 5. Field Constraints

Simple validations can be declared directly.

```python
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
```

Useful constraints


```python
gt=0
```

Greater than


```python
ge=0
```

Greater or equal


```python
lt=100
```

Less than


```python
le=100
```

Less or equal


---

# 6. BaseSettings

Used for application configuration.

Reads environment variables and `.env` files automatically.


```python
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    OPENAI_API_KEY: str

    DB_URL: str

    DEBUG: bool = False


settings = Settings()
```


Example `.env`

```text
OPENAI_API_KEY=abc123

DB_URL=postgres://localhost

DEBUG=True
```


Pydantic converts


```text
"True"
```


into


```python
True
```


---

# 7. Serialization


Object → Dictionary


```python
user.model_dump()
```


Output


```python
{

'name': 'Priyansh',

'age': 21

}
```


Object → JSON


```python
user.model_dump_json()
```


---

# 8. Parsing Dictionaries


Dictionary → Pydantic Object


```python
payload = {

"name":"Rahul",

"age":"22"

}


user = User.model_validate(

payload

)
```


---

# 9. LLM Structured Outputs


One of the biggest reasons AI engineers use Pydantic.


```python
class Resume(BaseModel):

    name: str

    years_of_experience: int

    skills: list[str]
```


LLM Output


```python
output = {

"name":"Priyansh",

"years_of_experience":2,

"skills":[

"Python",

"FastAPI"

]

}
```


Validate


```python
resume = Resume.model_validate(

output

)
```


If GPT returns


```python
{

"name":"Priyansh",

"years_of_experience":"five"

}
```


Pydantic raises


```text
ValidationError
```


No bad data enters your system.


---

# Dataclass vs Pydantic


| Feature | Dataclass | Pydantic |
|---------|-----------|----------|
| Type Hints | ✅ | ✅ |
| Validation | ❌ | ✅ |
| JSON Parsing | ❌ | ✅ |
| FastAPI | ❌ | ✅ |
| .env Support | ❌ | ✅ |
| LLM Outputs | ❌ | ✅ |


---

# Mental Model


```text
JSON

↓

Pydantic Model

↓

Validation

↓

Safe Python Object

↓

Business Logic
```


---

# Cheat Sheet


| Component | Purpose |
|-----------|---------|
| BaseModel | Validation |
| field_validator | Custom rules |
| Field | Constraints |
| BaseSettings | Configuration |
| model_validate() | Dict → Object |
| model_dump() | Object → Dict |
| model_dump_json() | Object → JSON |


---

# Golden Rule

Dataclass

→ Internal Python objects


Pydantic

→ Anything crossing a boundary


Examples


✔ HTTP Requests

✔ HTTP Responses

✔ Database Payloads

✔ Environment Variables

✔ LLM Outputs
