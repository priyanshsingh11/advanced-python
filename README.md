# Day 1 — Type Hints Masterclass

## Why Types Exist

Without type hints:

```python
def add(a, b):
    return a + b

add(5, "hello")
```

Error occurs only at runtime.

```text
TypeError
```

With type hints:

```python
def add(a: int, b: int) -> int:
    return a + b
```

Benefits

- Better autocomplete
- Earlier bug detection
- Static analysis with mypy
- Production-quality code


---

# Primitive Annotations

```python
name: str = "Priyansh"

age: int = 21

height: float = 5.9

is_student: bool = True
```

---

# Function Annotations

```python
def greet(name: str) -> str:
    return f"Hello {name}"
```

Return types

```python
def square(x: int) -> int:
    return x * x
```

---

# Exercise

Convert this function to use types.


```python
def area(length, width):
    return length * width
```

---

# Solution


```python
def area(
    length: float,
    width: float
) -> float:
    return length * width
```
