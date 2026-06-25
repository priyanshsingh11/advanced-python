"""
=========================================================
DAY 1 — DECORATORS
File: day1_decorators.py
=========================================================

Goal
----
Understand decorators from first principles.

Decorators are NOT magic.

A decorator is simply

A function

that takes another function

and returns a new function.


=========================================================
PART 1 — Functions are Objects
=========================================================

Functions can be assigned to variables.

"""


def greet():

    print("Hello")


say_hi = greet


say_hi()


"""
Output


Hello


Functions can also be passed as arguments.


=========================================================
PART 2 — Function Taking Function
=========================================================

"""


def execute(func):

    func()


def hello():

    print("Hello World")


execute(hello)


"""
Output


Hello World


=========================================================
PART 3 — Function Returning Function
=========================================================

"""


def outer():

    def inner():

        print("Inside inner")

    return inner


f = outer()

f()


"""
Output


Inside inner


=========================================================
PART 4 — First Decorator
=========================================================

Decorator syntax


@decorator


is equivalent to


func = decorator(func)



"""


def decorator(func):

    def wrapper():

        print("Before function")

        func()

        print("After function")

    return wrapper



@decorator
def greet():

    print("Hello")


greet()


"""
Output


Before function

Hello

After function


=========================================================
PART 5 — Decorator with *args and **kwargs
=========================================================

Without this,
decorators only work on functions
with zero arguments.


"""


def logger(func):

    def wrapper(*args, **kwargs):

        print("Calling function")

        result = func(*args, **kwargs)

        print("Function finished")

        return result

    return wrapper



@logger
def add(a, b):

    return a + b


print(add(5, 10))


"""
Output


Calling function

Function finished

15


=========================================================
PART 6 — Decorator WITH Arguments
=========================================================

Suppose we want


@repeat(3)


instead of


@repeat



Need three layers.


repeat(3)


↓

decorator


↓

wrapper



"""


def repeat(times):

    def decorator(func):

        def wrapper(*args, **kwargs):

            for _ in range(times):

                func(*args, **kwargs)

        return wrapper

    return decorator



@repeat(3)
def hello():

    print("Hi")


hello()


"""
Output


Hi

Hi

Hi


=========================================================
PART 7 — Timing Decorator
=========================================================

"""


import time



def timer(func):

    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()


        print(

            f"Took {end-start:.4f}s"

        )

        return result


    return wrapper



@timer
def work():

    time.sleep(1)



work()



"""
Output


Took 1.0001s



=========================================================
PART 8 — Authentication Example
=========================================================

Useful in APIs.


"""


def requires_login(func):

    def wrapper(*args, **kwargs):

        logged_in = True


        if not logged_in:

            print("Access denied")

            return


        return func(*args, **kwargs)


    return wrapper



@requires_login
def dashboard():

    print("Dashboard opened")


dashboard()



=========================================================
KEY TAKEAWAYS
=========================================================

Decorators are


Functions

↓

Wrapping Functions


Normal decorator


@decorator


means


func = decorator(func)




Decorator with arguments


@repeat(3)


means


func = repeat(3)(func)




Mental Model


Function


↓

Decorator


↓

Wrapper


↓

New Function


=========================================================
"""
