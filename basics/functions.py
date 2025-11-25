# ==========================================
#                 FUNCTIONS
# ==========================================
# This file explains Python functions:
#   - defining and calling functions
#   - parameters and return values
#   - default parameters
#   - multiple returns
#   - scope and global variables
#   - *args and **kwargs
#   - lambda functions
#   - type hints
#   - function aliases
#   - functions as arguments
#   - nested functions
#   - closures and nonlocal
#   - recursion
#   - positional-only and keyword-only parameters
#   - function stubs (pass, ...)
#   - docstring examples (PEP-257)
#
# Every section includes separators so the output
# is easy to read when you run the file.


# ==========================================
# 1. BASIC FUNCTION DEFINITION
# ==========================================

print("\n--- SECTION 1: Basic function definition ---")

def greet():
    """Prints a simple greeting"""
    print("Hello, world!")

greet()


# ==========================================
# 2. FUNCTIONS WITH PARAMETERS
# ==========================================

print("\n--- SECTION 2: Parameters ---")

def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alex")


# ==========================================
# 3. RETURN VALUES
# ==========================================

print("\n--- SECTION 3: Return values ---")

def add(a, b):
    return a + b

print(add(3, 5))


# ==========================================
# 4. DEFAULT PARAMETERS
# ==========================================

print("\n--- SECTION 4: Default parameters ---")

def greet_default(name="friend"):
    print(f"Hello, {name}!")

greet_default()
greet_default("Michael")


# ==========================================
# 5. MULTIPLE RETURNS (TUPLE)
# ==========================================

print("\n--- SECTION 5: Multiple returns ---")

def stats(numbers):
    total = sum(numbers)
    biggest = max(numbers)
    smallest = min(numbers)
    return total, biggest, smallest

print(stats([2, 5, 7, 1]))


# ==========================================
# 6. SCOPE (LOCAL VS GLOBAL)
# ==========================================

print("\n--- SECTION 6: Scope (local/global) ---")

a = 5  # global variable

def modify_global():
    # global allows modifying a variable outside the function
    global a
    a = a + 2

modify_global()
print(a)  # now 7

# Better alternative: return the value instead of modifying globals
counter = 0

def increase(value):
    return value + 1

counter = increase(counter)
print(counter)


# ==========================================
# 7. *args — MULTIPLE POSITIONAL ARGUMENTS
# ==========================================

print("\n--- SECTION 7: *args (multiple positional arguments) ---")

def total_sum(*numbers):
    return sum(numbers)

print(total_sum(1, 2, 3))
print(total_sum(10, 20, 30, 40))


# ==========================================
# 8. **kwargs — MULTIPLE NAMED ARGUMENTS
# ==========================================

print("\n--- SECTION 8: **kwargs (multiple named arguments) ---")

def print_info(**data):
    for key, value in data.items():
        print(f"{key}: {value}")

print_info(name="Alex", age=30, country="Moldova")


# ==========================================
# 9. COMBINING *args AND **kwargs
# ==========================================

print("\n--- SECTION 9: Combining *args and **kwargs ---")

def debug_example(*args, **kwargs):
    print("Positional:", args)
    print("Named:", kwargs)

debug_example(1, 2, 3, mode="test", verbose=True)


# ==========================================
# 10. LAMBDA FUNCTIONS
# ==========================================

print("\n--- SECTION 10: lambda functions ---")

double = lambda x: x * 2
print(double(5))


# ==========================================
# 11. TYPE HINTS
# ==========================================

print("\n--- SECTION 11: Type hints ---")

def multiply(a: int, b: int) -> int:
    return a * b

print(multiply(3, 4))


# ==========================================
# 12. FUNCTION ALIASES
# ==========================================

print("\n--- SECTION 12: Function aliases ---")

def shout(text):
    return text.upper()

yell = shout  # alias
print(yell("hello"))


# ==========================================
# 13. FUNCTIONS AS ARGUMENTS
# ==========================================

print("\n--- SECTION 13: Functions as arguments ---")

def apply(func, value):
    return func(value)

def square(x):
    return x * x

print(apply(square, 5))


# ==========================================
# 14. NESTED FUNCTIONS
# ==========================================

print("\n--- SECTION 14: Nested functions ---")

def outer():
    print("Outer start")

    def inner():
        print("Inner called")

    inner()

outer()


# ==========================================
# 15. CLOSURES (REMEMBER VALUES)
# ==========================================

print("\n--- SECTION 15: Closures ---")

def multiplier(n):
    def inner(x):
        return x * n
    return inner

double = multiplier(2)
print(double(10))


# ==========================================
# 16. NONLOCAL
# ==========================================

print("\n--- SECTION 16: nonlocal keyword ---")

def counter_factory():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

inc = counter_factory()
print(inc())
print(inc())


# ==========================================
# 17. RECURSION
# ==========================================

print("\n--- SECTION 17: Recursion ---")

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))


# ==========================================
# 18. POSITIONAL-ONLY & KEYWORD-ONLY PARAMETERS
# ==========================================

print("\n--- SECTION 18: Positional-only & keyword-only parameters ---")

def pos_only(a, b, /):
    return a + b

print(pos_only(3, 4))

def kw_only(*, a, b):
    return a * b

print(kw_only(a=2, b=3))

def mixed(a, b, /, *, c, d):
    return a + b + c + d

print(mixed(1, 2, c=3, d=4))


# ==========================================
# 19. FUNCTION STUBS
# ==========================================

print("\n--- SECTION 19: Function stubs ---")

# 'pass' = empty function (common during development)
def todo():
    pass

# '...' = ellipsis, also used as a placeholder
# Must be inside the function body, NOT in the parameters.
def future_feature():
    ...

print("Stub functions executed (no output).")

# ==========================================
# 20. DOCSTRING FORMAT EXAMPLE
# ==========================================

print("\n--- SECTION 20: Docstrings (PEP-257) ---")

def divide(a: float, b: float) -> float:
    """
    Divide a by b.

    Parameters:
        a (float): Numerator
        b (float): Denominator

    Returns:
        float: The division result

    Raises:
        ZeroDivisionError: If b is zero
    """
    return a / b

print(divide(10, 2))
