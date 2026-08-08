# Object-Oriented Programming in Python

Object-Oriented Programming (OOP) is a programming paradigm where we organize software around **objects**.

An object combines:

* **State** → data/attributes
* **Behavior** → methods

For example, a `BankAccount` object can contain:

```python
account.balance
account.owner
```

and provide behavior:

```python
account.deposit()
account.withdraw()
```

The goal of OOP is not simply to create classes. Good OOP helps us build code that is:

* reusable
* maintainable
* testable
* extensible
* easier to reason about

---

# 1. Classes and Objects

A **class** is a blueprint.

An **object** is an instance of that class.

```python
class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, {self.name}"
```

Create objects:

```python
user1 = User("Priyansh", 21)
user2 = User("Rahul", 22)

print(user1.greet())
print(user2.greet())
```

Output:

```text
Hello, Priyansh
Hello, Rahul
```

Think of it as:

```text
User (class)
   │
   ├── user1 (object)
   │     ├── name = "Priyansh"
   │     └── age = 21
   │
   └── user2 (object)
         ├── name = "Rahul"
         └── age = 22
```

---

# 2. `self`

`self` refers to the current object.

```python
class User:

    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello {self.name}"
```

When we write:

```python
user = User("Priyansh")

user.greet()
```

Python effectively performs:

```python
User.greet(user)
```

Therefore:

```python
self
```

is the object on which the method was called.

---

# 3. Instance Attributes

Instance attributes belong to individual objects.

```python
class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Now:

```python
user1 = User("Priyansh", 21)
user2 = User("Rahul", 22)
```

Each object has its own:

```text
user1.name → Priyansh
user2.name → Rahul
```

Changing one does not change the other:

```python
user1.name = "Alex"

print(user1.name)
print(user2.name)
```

Output:

```text
Alex
Rahul
```

---

# 4. Class Attributes

Class attributes are shared by instances unless overridden.

```python
class User:

    platform = "Ajaia"

    def __init__(self, name):
        self.name = name
```

Now:

```python
user1 = User("Priyansh")
user2 = User("Rahul")

print(user1.platform)
print(user2.platform)
```

Both access:

```python
User.platform
```

You can also access it directly:

```python
print(User.platform)
```

---

# 5. Instance Methods

Instance methods operate on an object.

```python
class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance
```

Usage:

```python
account = BankAccount(1000)

account.deposit(500)

print(account.get_balance())
```

---

# 6. Class Methods

A class method operates on the class rather than a specific instance.

Use:

```python
@classmethod
```

Example:

```python
class User:

    platform = "Ajaia"

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_platform(cls):
        return cls.platform
```

Usage:

```python
print(User.get_platform())
```

`cls` refers to the class.

---

## Alternative Constructors

A very useful pattern is using class methods as alternative constructors.

```python
class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split(",")
        return cls(name, int(age))
```

Now:

```python
user = User.from_string("Priyansh,21")

print(user.name)
print(user.age)
```

This pattern appears frequently in real applications.

---

# 7. Static Methods

A static method does not need access to the instance or class.

```python
class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b
```

Usage:

```python
result = MathUtils.add(10, 20)
```

Static methods are useful when a function logically belongs to a class but doesn't need:

```python
self
```

or:

```python
cls
```

---

# 8. Instance vs Class vs Static Methods

| Method          | First argument | Access instance | Access class |
| --------------- | -------------- | --------------: | -----------: |
| Instance method | `self`         |             Yes |          Yes |
| Class method    | `cls`          |              No |          Yes |
| Static method   | None           |              No |           No |

Example:

```python
class Example:

    def instance_method(self):
        pass

    @classmethod
    def class_method(cls):
        pass

    @staticmethod
    def static_method():
        pass
```

---

# 9. Encapsulation

Encapsulation means keeping an object's internal state and implementation controlled through a defined interface.

Python does not enforce private fields as strictly as languages such as Java or C++.

Instead, Python uses conventions.

### Public

```python
self.name
```

### Protected convention

```python
self._name
```

The `_` means:

> "This is intended for internal use."

### Name mangling

```python
self.__balance
```

Double underscore triggers name mangling.

Example:

```python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance
```

External code should use:

```python
account.get_balance()
```

rather than directly modifying the internal state.

---

# 10. Properties

Properties allow controlled access to attributes.

```python
class User:

    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):

        if value < 0:
            raise ValueError("Age cannot be negative")

        self._age = value
```

Usage:

```python
user = User(21)

print(user.age)

user.age = 22
```

The property looks like an attribute:

```python
user.age
```

but internally executes methods.

This is extremely useful for validation.

---

# 11. Inheritance

Inheritance allows one class to reuse or extend another class.

```python
class Animal:

    def eat(self):
        print("Eating")


class Dog(Animal):

    def bark(self):
        print("Barking")
```

Now:

```python
dog = Dog()

dog.eat()
dog.bark()
```

`Dog` inherits from `Animal`.

Relationship:

```text
Animal
   ↑
   │
  Dog
```

This represents an **is-a** relationship:

```text
Dog is an Animal
```

---

# 12. Method Overriding

A child class can replace a parent's behavior.

```python
class Animal:

    def sound(self):
        return "Some sound"


class Dog(Animal):

    def sound(self):
        return "Bark"
```

Now:

```python
dog = Dog()

print(dog.sound())
```

Output:

```text
Bark
```

---

# 13. `super()`

`super()` allows a child class to call functionality from its parent.

```python
class Animal:

    def __init__(self, name):
        self.name = name


class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
```

Without `super()` you would need to duplicate:

```python
self.name = name
```

---

# 14. Multilevel Inheritance

Python supports multiple levels of inheritance.

```python
class Animal:

    def eat(self):
        print("Eating")


class Mammal(Animal):

    def walk(self):
        print("Walking")


class Dog(Mammal):

    def bark(self):
        print("Barking")
```

Now:

```python
dog = Dog()

dog.eat()
dog.walk()
dog.bark()
```

Inheritance chain:

```text
Animal
   ↑
Mammal
   ↑
 Dog
```

However, deep inheritance hierarchies can become difficult to maintain.

Prefer simple inheritance relationships.

---

# 15. Multiple Inheritance

Python allows a class to inherit from multiple classes.

```python
class Logger:

    def log(self):
        print("Logging")


class Serializer:

    def serialize(self):
        print("Serializing")


class Service(Logger, Serializer):
    pass
```

Now:

```python
service = Service()

service.log()
service.serialize()
```

Multiple inheritance can be useful, but should be used carefully.

Mixins are one common legitimate use case.

---

# 16. Method Resolution Order (MRO)

When multiple inheritance exists, Python needs to determine which method to use.

Python uses **Method Resolution Order (MRO)**.

Example:

```python
class A:

    def hello(self):
        print("A")


class B(A):

    def hello(self):
        print("B")


class C(A):

    def hello(self):
        print("C")


class D(B, C):
    pass
```

Now:

```python
d = D()

d.hello()
```

Python searches according to the MRO.

You can inspect it:

```python
print(D.mro())
```

Understanding MRO becomes important when working with frameworks and complex class hierarchies.

---

# 17. Composition

Composition means an object contains another object.

Example:

```python
class Engine:

    def start(self):
        print("Engine started")


class Car:

    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print("Car started")
```

Here:

```text
Car
 └── Engine
```

The relationship is:

```text
Car HAS an Engine
```

---

# 18. Composition vs Inheritance

Inheritance:

```text
Dog IS an Animal
```

```python
class Dog(Animal):
    pass
```

Composition:

```text
Car HAS an Engine
```

```python
class Car:

    def __init__(self):
        self.engine = Engine()
```

A useful rule:

> Prefer composition when you want to combine behavior rather than create a true specialization relationship.

Composition often produces more flexible code.

---

# 19. Polymorphism

Polymorphism means different objects can provide the same interface while implementing behavior differently.

```python
class Dog:

    def speak(self):
        return "Bark"


class Cat:

    def speak(self):
        return "Meow"
```

Now:

```python
def make_sound(animal):
    print(animal.speak())
```

Both work:

```python
make_sound(Dog())
make_sound(Cat())
```

The function doesn't care whether the object is a `Dog` or `Cat`.

It only cares that the object provides:

```python
speak()
```

---

# 20. Duck Typing

Python heavily uses duck typing.

The idea:

> If an object behaves like the required type, use it.

Example:

```python
class Dog:

    def speak(self):
        return "Bark"


class Robot:

    def speak(self):
        return "Beep"
```

We can do:

```python
def make_sound(obj):
    print(obj.speak())
```

Both work:

```python
make_sound(Dog())
make_sound(Robot())
```

Python doesn't require them to share a parent class.

---

# 21. Abstract Base Classes

Sometimes you want to define an interface that subclasses must implement.

Use:

```python
from abc import ABC, abstractmethod
```

Example:

```python
from abc import ABC, abstractmethod


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
```

Now subclasses must implement `pay()`.

```python
class StripeProcessor(PaymentProcessor):

    def pay(self, amount):
        print(f"Processing ${amount}")


class CashfreeProcessor(PaymentProcessor):

    def pay(self, amount):
        print(f"Processing ₹{amount}")
```

This is useful when multiple implementations need to follow the same contract.

---

# 22. Dataclasses

Python provides `dataclasses` for classes primarily used to store data.

```python
from dataclasses import dataclass


@dataclass
class User:

    name: str
    age: int
```

Now:

```python
user = User("Priyansh", 21)

print(user)
```

Dataclasses automatically provide useful functionality such as:

* `__init__`
* `__repr__`
* equality comparison

They are useful for internal application data structures.

---

# 23. `__str__` and `__repr__`

Python classes can customize how objects are represented.

```python
class User:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"User: {self.name}"

    def __repr__(self):
        return f"User(name={self.name!r})"
```

`str()` is generally intended for a user-friendly representation.

```python
print(user)
```

`repr()` is intended to provide a more developer-oriented representation.

```python
repr(user)
```

---

# 24. Dunder Methods

Dunder means:

```text
double underscore
```

Examples:

```python
__init__
__str__
__repr__
__len__
__eq__
__lt__
__iter__
__next__
```

These methods allow Python objects to integrate with Python's language features.

Example:

```python
class Team:

    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)
```

Now:

```python
team = Team(["A", "B", "C"])

print(len(team))
```

Python internally calls:

```python
team.__len__()
```

---

# 25. Operator Overloading

Dunder methods can customize operators.

```python
class Money:

    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)
```

Now:

```python
a = Money(100)
b = Money(50)

c = a + b

print(c.amount)
```

The `+` operator invokes:

```python
__add__
```

---

# 26. Dependency Injection with Composition

OOP becomes particularly useful in backend applications.

Instead of hard-coding dependencies:

```python
class UserService:

    def __init__(self):
        self.database = PostgreSQLDatabase()
```

inject the dependency:

```python
class UserService:

    def __init__(self, database):
        self.database = database
```

Now:

```python
database = PostgreSQLDatabase()

service = UserService(database)
```

This makes the service:

* easier to test
* easier to replace
* less tightly coupled

For example, during testing:

```python
fake_database = FakeDatabase()

service = UserService(fake_database)
```

This concept becomes extremely important in FastAPI and production backend development.

---

# 27. Coupling and Cohesion

### High coupling

Classes depend heavily on each other's implementation.

```text
Class A
  ↓↓↓↓↓
Class B
  ↓↓↓↓↓
Class C
```

Changing one can break many others.

### Low coupling

Components communicate through clear interfaces.

```text
Service
   ↓
Interface
   ↓
Database
```

Low coupling is generally desirable.

---

### High cohesion

A class should have a focused responsibility.

Bad:

```python
class User:

    def save_to_database(self):
        ...

    def send_email(self):
        ...

    def generate_pdf(self):
        ...

    def process_payment(self):
        ...
```

This class has too many responsibilities.

Better:

```text
User
UserRepository
EmailService
PDFService
PaymentService
```

This connects directly to the **Single Responsibility Principle**.

---

# 28. SOLID Principles

You should understand the five SOLID principles.

## S — Single Responsibility Principle

A class should have one primary responsibility.

Bad:

```python
class Report:

    def generate(self):
        ...

    def save_to_database(self):
        ...

    def send_email(self):
        ...
```

Better:

```text
ReportGenerator
ReportRepository
EmailService
```

---

## O — Open/Closed Principle

Software should be:

> Open for extension, closed for modification.

Instead of constantly modifying existing payment logic:

```python
if provider == "stripe":
    ...
elif provider == "cashfree":
    ...
elif provider == "paypal":
    ...
```

use a common interface:

```python
class PaymentProcessor:

    def pay(self, amount):
        raise NotImplementedError
```

Then create implementations:

```python
class StripeProcessor(PaymentProcessor):
    ...

class CashfreeProcessor(PaymentProcessor):
    ...

class PayPalProcessor(PaymentProcessor):
    ...
```

---

## L — Liskov Substitution Principle

A subclass should be usable wherever its parent is expected without breaking the program.

If:

```python
Dog
```

inherits from:

```python
Animal
```

then `Dog` should behave correctly anywhere an `Animal` is expected.

---

## I — Interface Segregation Principle

Don't force classes to implement methods they don't need.

Instead of one giant interface:

```python
class Worker:

    def code(self):
        ...

    def design(self):
        ...

    def recruit(self):
        ...

    def manage(self):
        ...
```

prefer smaller interfaces when appropriate.

---

## D — Dependency Inversion Principle

High-level code should depend on abstractions rather than concrete implementations.

Instead of:

```python
class OrderService:

    def __init__(self):
        self.payment = StripePayment()
```

prefer:

```python
class OrderService:

    def __init__(self, payment_processor):
        self.payment = payment_processor
```

Now Stripe can be replaced without modifying `OrderService`.

---

# 29. When NOT to Use OOP

Not every Python program needs classes.

For example:

```python
def calculate_tax(amount):
    return amount * 0.18


def calculate_total(amount):
    return amount + calculate_tax(amount)
```

This can be perfectly good procedural/functional code.

Don't create:

```python
class TaxCalculator:
    ...
```

just because you learned OOP.

Use OOP when objects, state, relationships, or interchangeable implementations make the design clearer.

---

# 30. Production Example

Consider a payment system.

A poor design:

```python
def process_payment(provider, amount):

    if provider == "stripe":
        ...

    elif provider == "cashfree":
        ...

    elif provider == "paypal":
        ...
```

A more extensible OOP design:

```python
from abc import ABC, abstractmethod


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class StripeProcessor(PaymentProcessor):

    def pay(self, amount):
        return f"Stripe payment: {amount}"


class CashfreeProcessor(PaymentProcessor):

    def pay(self, amount):
        return f"Cashfree payment: {amount}"


class PaymentService:

    def __init__(self, processor):
        self.processor = processor

    def process(self, amount):
        return self.processor.pay(amount)
```

Now:

```python
processor = StripeProcessor()

service = PaymentService(processor)

print(service.process(1000))
```

To switch providers:

```python
processor = CashfreeProcessor()

service = PaymentService(processor)
```

`PaymentService` doesn't need to change.

This demonstrates:

* abstraction
* inheritance
* polymorphism
* composition
* dependency injection
* low coupling
* SOLID principles

---

# 31. OOP Mental Model

You should be able to visualize OOP like this:

```text
                    OOP
                     │
       ┌─────────────┼─────────────┐
       ↓             ↓             ↓
    Classes       Objects       Methods
       │
       ├── Encapsulation
       │
       ├── Inheritance
       │
       ├── Polymorphism
       │
       └── Composition
              │
              ↓
        Better Design
              │
       ┌──────┴──────┐
       ↓             ↓
   Low Coupling   High Cohesion
       │
       ↓
     SOLID
       │
       ↓
Production Software
```

---

# OOP Checklist

Before considering OOP complete, you should be able to explain and implement:

* [ ] Classes
* [ ] Objects
* [ ] `self`
* [ ] `__init__`
* [ ] Instance attributes
* [ ] Class attributes
* [ ] Instance methods
* [ ] `@classmethod`
* [ ] `@staticmethod`
* [ ] Encapsulation
* [ ] `_private` conventions
* [ ] Name mangling
* [ ] `@property`
* [ ] Inheritance
* [ ] Method overriding
* [ ] `super()`
* [ ] Multiple inheritance
* [ ] MRO
* [ ] Composition
* [ ] Polymorphism
* [ ] Duck typing
* [ ] Abstract classes
* [ ] `ABC`
* [ ] `@abstractmethod`
* [ ] Dataclasses
* [ ] Dunder methods
* [ ] Operator overloading
* [ ] Dependency injection
* [ ] Coupling
* [ ] Cohesion
* [ ] SOLID principles
* [ ] When to use OOP
* [ ] When NOT to use OOP

---

# Practical Exercises

After learning the concepts, implement these without copying tutorials.

### Exercise 1 — Bank Account

Implement:

```python
BankAccount
```

Features:

```text
deposit()
withdraw()
get_balance()
```

Requirements:

* prevent negative deposits
* prevent overdrafts
* use encapsulation
* create custom exceptions

---

### Exercise 2 — Payment System

Create:

```text
PaymentProcessor
├── StripeProcessor
├── CashfreeProcessor
└── PayPalProcessor
```

Requirements:

* abstract base class
* polymorphism
* composition
* dependency injection

---

### Exercise 3 — Notification System

Create:

```text
NotificationService
├── EmailNotification
├── SMSNotification
└── PushNotification
```

The service should be able to work with any notification implementation.

---

### Exercise 4 — Production Mini Project

Build:

```text
Task Management System
```

Classes:

```text
User
Task
Project
TaskManager
TaskRepository
```

Requirements:

* composition
* inheritance where appropriate
* polymorphism
* custom exceptions
* type hints
* dataclasses
* dependency injection
* clean separation of responsibilities

The goal is not to create the biggest project.

The goal is to make the architecture clean.

---

# Final Rule

Do not memorize:

```python
class
```

or:

```python
inheritance
```

Instead, learn to answer:

> **Why should this be a class?**

> **Why should this use composition instead of inheritance?**

> **Why should this dependency be injected?**

> **Why is this class violating Single Responsibility?**

> **Why would polymorphism make this system easier to extend?**

If you can answer those questions and implement the examples from scratch, you have moved beyond basic Python OOP into **production-level OOP thinking**.
