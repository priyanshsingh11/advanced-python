# Decorators - Quick Revision

---

# Why Decorators?

Suppose we want to execute code

Before

and

After

a function call.


Without decorators


```python
def greet():

    print("Hello")


print("Before")

greet()

print("After")
```


Problem

We must repeat this logic for every function.


Decorators solve this.


---

# Functions are Objects


Functions can be assigned to variables.


```python
def hello():

    print("Hello")


f = hello


f()
```


Output


```text
Hello
```


Functions can also be passed as arguments.


```python
def execute(func):

    func()


execute(hello)
```


---

# Functions Returning Functions


```python
def outer():

    def inner():

        print("Inside")

    return inner



f = outer()

f()
```


Output


```text
Inside
```


---

# First Decorator


```python
def decorator(func):


    def wrapper():

        print("Before")

        func()

        print("After")


    return wrapper



@decorator
def greet():

    print("Hello")


greet()
```


Output


```text
Before

Hello

After
```


---

# What Does @decorator Mean?


This


```python
@decorator
def greet():

    print("Hello")
```


is simply


```python
def greet():

    print("Hello")


greet = decorator(greet)
```


Nothing magical.


---

# Decorators with Arguments


Normal decorator


```python
@timer
```


Decorator with arguments


```python
@repeat(3)
```


Need three nested functions.



```python
def repeat(times):


    def decorator(func):


        def wrapper(*args, **kwargs):


            for _ in range(times):

                func(*args, **kwargs)


        return wrapper


    return decorator
```



Usage


```python
@repeat(3)
def hello():

    print("Hi")


hello()
```



Output


```text
Hi

Hi

Hi
```


---

# Why *args and **kwargs?


Without them


```python
def wrapper():

    func()
```


Only works for functions


with zero arguments.



Better


```python
def wrapper(*args, **kwargs):


    return func(

        *args,

        **kwargs

    )
```



Now works for every function.



---

# Real World Examples


Logging


```python
@logger
```



Timing


```python
@timer
```



Authentication


```python
@requires_login
```



Caching


```python
@lru_cache
```



Retry logic


```python
@retry
```



FastAPI


```python
@app.get("/users")
```



Pytest


```python
@pytest.fixture
```



Dataclass


```python
@dataclass
```



---

# Mental Model


Normal function


```text
Function


↓

Execute
```



Decorated function


```text
Function


↓

Decorator


↓

Wrapper


↓

New Function


↓

Execute
```



Decorator with arguments


```text
repeat(3)


↓

decorator


↓

wrapper


↓

hello


↓

execute
```



---

# Cheat Sheet


Normal decorator


```python
@decorator


func = decorator(func)
```



Decorator with arguments


```python
@repeat(3)


func = repeat(3)(func)
```



---

# Golden Rule


Decorators are simply


Functions


Wrapping


Functions



No magic involved.
