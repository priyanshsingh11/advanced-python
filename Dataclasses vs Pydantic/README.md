# Dataclasses vs Pydantic

---

# Why do we have both?

Both help define structured data.

Without either


```python
user = {

    "name": "Priyansh",

    "age": 21

}
```

Problems

- No autocomplete
- No validation
- Easy to miss fields
- Harder to maintain


Both Dataclass and Pydantic solve this.


---

# 1. Dataclass

Dataclasses were introduced in Python 3.7.

They automatically generate


```python
__init__()

__repr__()

__eq__()
```


for you.


Example


```python
from dataclasses import dataclass


@dataclass
class User:

    name: str

    age: int


u = User(

    "Priyansh",

    21

)

print(u)
```


Output


```text
User(name='Priyansh', age=21)
```


---

# Dataclass Characteristics


✔ Lightweight

✔ Very fast

✔ Built into Python

✔ Great for internal objects


❌ No validation

❌ No JSON parsing

❌ No environment variables



Example


```python
u = User(

    "Priyansh",

    "21"

)


print(type(u.age))
```


Output


```python
<class 'str'>
```


Dataclass simply stores what you provide.



---

# 2. Pydantic


Pydantic validates data at runtime.



```python
from pydantic import BaseModel


class User(

BaseModel

):


    name: str


    age: int



u = User(

    name="Priyansh",

    age="21"

)
```



Output


```text
User(name='Priyansh', age=21)
```


Pydantic converted


```python
"21"
```


into


```python
21
```



---

Invalid input


```python
User(

name="Priyansh",

age="hello"

)
```



Output


```text
ValidationError
```



---

# 3. What is a Boundary?


A boundary means


Data entering your application

or


Data leaving your application.



Examples


### HTTP Request


```json
{
"name":"Priyansh",
"age":"21"
}
```



### LLM Response


```json
{
"name":"Priyansh",
"score":"95"
}
```



### Environment Variables


```text
DEBUG=True
PORT=8000
```



### Database Payload


```json
{
"id":"10",
"name":"Rahul"
}
```



All of these are boundaries.


Use Pydantic.



---

# 4. Internal Objects


Suppose data is already validated.


```python
@dataclass
class CartItem:

    product_id: int

    quantity: int
```



Application code


```python
item = CartItem(

1,

3

)
```



No validation needed.


Dataclass is enough.



---

# 5. Decision Rule


### Data comes from outside


Use


```python
BaseModel
```



Examples


✔ API Requests

✔ API Responses

✔ LLM Outputs

✔ Kafka Messages

✔ Redis Payloads

✔ Environment Variables



---

### Data stays inside Python


Use


```python
@dataclass
```



Examples


✔ Game Objects

✔ DTOs

✔ Service Layer Objects

✔ Cache Entries

✔ Temporary Structures



---

# 6. Performance


Dataclass


✔ Faster

✔ Less memory




Pydantic


✔ Validation

✔ Parsing

✔ Serialization


Slightly slower


Usually worth it.



---

# Cheat Sheet


| Feature | Dataclass | Pydantic |
|---------|-----------|----------|
| Type Hints | ✅ | ✅ |
| Validation | ❌ | ✅ |
| JSON Parsing | ❌ | ✅ |
| FastAPI | ❌ | ✅ |
| Env Variables | ❌ | ✅ |
| LLM Outputs | ❌ | ✅ |
| Speed | ✅ | ❌ |


---

# Mental Model


```text
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
```


---

# Golden Rule


Dataclass


=

Trusted internal Python data



Pydantic


=

Anything crossing a boundary



Examples of boundaries


✔ HTTP requests

✔ HTTP responses

✔ LLM outputs

✔ Environment variables

✔ Database payloads

✔ Message queues
