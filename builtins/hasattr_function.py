# ============================================================
#                 BUILT-IN FUNCTION — hasattr()
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   This lesson explores Python's hasattr() function:
#     - checking if objects expose attributes
#     - class vs instance attributes
#     - how modules and descriptors participate
#     - interactions with __getattr__ and __getattribute__
#     - guarding attribute access safely
#     - pitfalls when AttributeError is not raised
#
# Each section prints a runtime banner for readability.
# ============================================================


print("\n# -----------------------------")
print("# 1. What hasattr() checks")
print("# -----------------------------\n")

class Car:
    def __init__(self):
        self.make = "Tesla"
        self.model = "Model 3"

car = Car()
print(hasattr(car, "make"))     # True
print(hasattr(car, "year"))     # False


print("\n# -----------------------------")
print("# 2. Instances vs classes")
print("# -----------------------------\n")

class User:
    country = "Moldova"  # class attribute shared by all instances

    def __init__(self, name):
        self.name = name  # instance attribute

alex = User("Alex")

print(hasattr(alex, "name"))      # True (instance)
print(hasattr(User, "country"))   # True (class attribute)
print(hasattr(alex, "country"))   # True (falls back to class)


print("\n# -----------------------------")
print("# 3. Modules, descriptors, and dictionaries")
print("# -----------------------------\n")

import math

print(hasattr(math, "pi"))        # True → attribute defined in module
print(hasattr(math, "tau"))       # True → also attribute
print(hasattr(math, "unknown"))   # False

data = {"pi": 3.14}
print("pi" in data)               # dicts use key membership instead of hasattr

class Profile:
    @property
    def email(self):
        return "user@example.com"

profile = Profile()
print(hasattr(profile, "email"))  # True because property descriptor handles it


print("\n# -----------------------------")
print("# 4. hasattr() triggers attribute lookups")
print("# -----------------------------\n")

class Sensor:
    def __getattr__(self, name):
        print(f"Computing {name} lazily…")
        if name == "temperature":
            return 72
        raise AttributeError(name)

sensor = Sensor()
print(hasattr(sensor, "temperature"))  # True (and prints the message)
print(hasattr(sensor, "humidity"))     # False


print("\n# -----------------------------")
print("# 5. Guarding attribute access")
print("# -----------------------------\n")

class Account:
    def __init__(self, balance, nickname=None):
        self.balance = balance
        if nickname:
            self.nickname = nickname

def describe_account(obj):
    print(f"Balance: {obj.balance}")
    if hasattr(obj, "nickname"):
        print(f"Nickname: {obj.nickname}")
    else:
        print("Nickname not set.")

describe_account(Account(500))
describe_account(Account(800, nickname="Rainy Day"))

# getattr() with a default is an alternative when you only need the value.
print(getattr(Account(1000), "nickname", "Default nickname"))


print("\n# -----------------------------")
print("# 6. Pitfalls when AttributeError is not raised")
print("# -----------------------------\n")

class Broken:
    def __getattr__(self, name):
        raise ValueError("Wrong exception")

try:
    hasattr(Broken(), "thing")
except Exception as exc:
    print(f"hasattr() propagated {type(exc).__name__}")

# Fix: ensure __getattr__ raises AttributeError when attribute is missing.
class Fixed:
    def __getattr__(self, name):
        raise AttributeError(name)

print(hasattr(Fixed(), "thing"))  # False (safe)
