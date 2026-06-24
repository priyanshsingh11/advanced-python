# Python Type Hints — Quick Revision Sheet

---

# 1. Basic Type Hints

```python
name: str = "Priyansh"
age: int = 21
height: float = 5.9
is_student: bool = True
```

Functions

```python
def add(a: int, b: int) -> int:
    return a + b
```

Remember

- Parameter types go inside ()
- Return type comes after `->`

---

# 2. Optional

Represents

```text
X OR None
```

Old syntax

```python
from typing import Optional

name: Optional[str]
```

Modern syntax (Preferred)

```python
name: str | None
```

Example

```python
def get_user() -> str | None:
    return None
```

Always check

```python
if name is not None:
    print(name.upper())
```

---

# 3. Union

Represents

```text
Multiple valid types
```

Old

```python
Union[int, str]
```

Modern

```python
int | str
```

Example

```python
def square(x: int | float):
    return x * x
```

Allowed

```python
square(5)
square(5.5)
```

Not allowed

```python
square("abc")
```

---

# 4. Literal

Restricts values.

```python
from typing import Literal

Mode = Literal[
    "fast",
    "slow",
    "balanced"
]
```

Example

```python
def run(mode: Mode):
    pass
```

Valid

```python
run("fast")
```

Invalid

```python
run("banana")
```

Examples

```python
Literal["GET", "POST"]

Literal["INFO", "ERROR"]

Literal["gpt-4o", "gpt-5.5"]
```

---

# 5. Generics

Lists

```python
names: list[str]
```

Integers

```python
scores: list[int]
```

Dictionary

```python
marks: dict[str, int]
```

Nested

```python
students: dict[str, list[int]]
```

List of dictionaries

```python
users: list[dict[str, int]]
```

---

# 6. Any

Avoid when possible.

```python
from typing import Any

def foo(x: Any):
    return x
```

Problem

```text
Mypy gives up.

No checking.
```

Equivalent to

```text
Turn off type safety
```

Prefer precise types.

---

# 7. Type Aliases

Instead of

```python
dict[str, list[int]]
```

Do

```python
StudentScores = dict[str, list[int]]
```

Then

```python
def average(
        scores: StudentScores
):
    pass
```

Cleaner.

---

# 8. Mental Model

Think of types as sets.


int

contains


1
2
3
4



str | None

contains


"abc"

"hello"

None



Literal["GET","POST"]

contains exactly


GET

POST



Any

contains everything


---

# 9. mypy

Install

```bash
pip install mypy
```

Run

```bash
mypy test.py
```

Example

```python
def add(
        a: int,
        b: int
) -> int:

    return a+b


x = add(5, "10")
```

mypy

```text
Argument 2 has incompatible type "str"

expected "int"
```

Optional example

```python
def get_name() -> str | None:
    return None


name = get_name()

print(name.upper())
```

mypy

```text
Item "None"

has no attribute "upper"
```

---

# 10. Strict Mode

Run

```bash
mypy --strict app.py
```

Catches

✔ Missing return types

✔ Untyped functions

✔ Unsafe Any

✔ Unused ignores


---

# pyproject.toml

```toml
[tool.mypy]

strict = true

python_version = "3.12"
```

Now simply run

```bash
mypy .
```

---

# Cheat Sheet

| Concept | Preferred Syntax |
|---------|------------------|
| Optional | `str | None` |
| Union | `int | str` |
| Literal | `Literal["GET","POST"]` |
| List | `list[str]` |
| Dict | `dict[str,int]` |
| Nested | `dict[str,list[int]]` |
| Alias | `StudentScores = dict[str,list[int]]` |
| Any | Avoid |
| Type Checker | `mypy` |
| Strict Checking | `mypy --strict .` |

---

# Golden Rules

✔ Annotate everything

✔ Prefer `|` over `Optional` and `Union`

✔ Use `Literal` for fixed values

✔ Avoid `Any`

✔ Create aliases for ugly nested types

✔ Run `mypy --strict`

✔ Think of types as sets
