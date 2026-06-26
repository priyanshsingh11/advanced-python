# Generators, yield and Iterators - Quick Revision

---

# Why do Generators Exist?

Suppose we need numbers from 1 to 1,000,000.

Normal approach


```python
numbers = []

for i in range(1_000_000):
    numbers.append(i)
```

Problem

```text
Memory Usage

↓

Huge list

↓

Consumes RAM
```


---

# Lazy Evaluation

Generators produce values

only when requested.


Think


```text
List

↓

Store everything


Generator

↓

Produce one item at a time
```


---

# Iterators


An iterator is an object that supports


```python
__iter__()

__next__()
```


Example


```python
nums = iter([1,2,3])


print(next(nums))

print(next(nums))

print(next(nums))
```



Output


```text
1

2

3
```



---

# What is yield?


Normal function


```python
def numbers():

    return [1,2,3]
```


Generator function


```python
def numbers():

    yield 1

    yield 2

    yield 3
```



---

# How yield Works


```python
def count():

    yield 1

    yield 2

    yield 3
```



Call function


```python
g = count()
```



Nothing runs yet.


Only when


```python
next(g)
```



Output


```text
1
```



Again


```python
next(g)
```



Output


```text
2
```



Again


```python
next(g)
```



Output


```text
3
```



---

# Generator vs List


List


```python
nums = [i for i in range(1_000_000)]
```



Stores


1 million numbers



Generator


```python
nums = (

i

for i in range(1_000_000)

)
```



Stores


Almost nothing



Produces values on demand



---

# Infinite Generator


```python
def infinite():

    i = 0


    while True:

        yield i


        i += 1
```



Usage


```python
g = infinite()


print(next(g))

print(next(g))
```



Output


```text
0


1
```



---

# Streaming Example


Without generator


```python
tokens = []


for token in llm():

    tokens.append(token)


return tokens
```



Need entire response first.



---

With generator


```python
def stream_tokens():


    for token in llm():

        yield token
```



Consumer


```python
for token in stream_tokens():

    print(token)
```



Token appears immediately.


No waiting.


No large memory usage.



---

# Reading Large Files


Bad


```python
data = open(

"big.csv"

).read()
```



Loads entire file.



Good


```python
with open(

"big.csv"

) as f:


    for line in f:

        yield line
```



One line at a time.



---

# FastAPI Example


```python
from fastapi.responses import StreamingResponse


def generate():

    yield "Hello"


    yield "World"



StreamingResponse(

generate()

)
```



Client receives data gradually.



---

# OpenAI Streaming


```python
for chunk in response:


    yield chunk.delta.content
```



No full response stored.



---

# Mental Model


List


```text
Generate Everything


↓

Store in Memory


↓

Consume
```



Generator


```text
Generate One Item


↓

Consume


↓

Generate Next


↓

Consume
```



---

# Cheat Sheet


Iterator


```python
iter()

next()
```



Generator Function


```python
yield
```



Generator Expression


```python
(

x

for x in data

)
```



Infinite Generator


```python
while True:


    yield value
```



---

# Golden Rule


return


↓

Ends function



yield


↓

Pauses function



next()


↓

Resumes function



---

# Why AI Engineers Care


Generators power


✔ Token Streaming


✔ FastAPI StreamingResponse


✔ LangChain Streams


✔ Huge CSV Processing


✔ Kafka Consumers


✔ Async Pipelines


✔ Real-time AI Applications
