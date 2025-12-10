# ============================================================
#                SPECIAL ATTRIBUTE — __dict__
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   This lesson explains the __dict__ attribute:
#     - where Python stores per-instance state
#     - how class namespaces also use dictionaries
#     - updating __dict__ directly vs setattr()
#     - how __slots__ changes attribute storage
#     - safe patterns for debugging and serialization
#
# Each section prints a runtime banner for clarity.
# ============================================================


print("\n# -----------------------------")
print("# 1. What __dict__ represents")
print("# -----------------------------\n")

class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

p1 = Player("Alex", 5)
print(p1.__dict__)    # {'name': 'Alex', 'level': 5}
print(type(p1.__dict__))  # <class 'dict'>


print("\n# -----------------------------")
print("# 2. Reading and writing instance state")
print("# -----------------------------\n")

p2 = Player("Sam", 3)

# Add new attributes through __dict__
p2.__dict__["guild"] = "Mages"
print("Guild via dot access:", p2.guild) # Guild via dot access: Mages

# setattr() produces the same result without touching __dict__ directly.
setattr(p2, "title", "Archmage")
print("Title stored inside __dict__:", p2.__dict__["title"])


print("\n# -----------------------------")
print("# 3. Class namespaces also have __dict__")
print("# -----------------------------\n")

class Settings:
    theme = "dark"
    timeout = 30

print(Settings.__dict__["theme"])     # Access attributes stored on class
print("__dict__" in Settings.__dict__)  # meta entries live here as well


print("\n# -----------------------------")
print("# 4. Bulk updates and copy safety")
print("# -----------------------------\n")

class Config:
    def __init__(self):
        self.mode = "debug"
        self.port = 8000

cfg = Config()
cfg.__dict__.update({"mode": "prod", "host": "0.0.0.0"})
print(cfg.mode, cfg.host)

# Copy __dict__ before mutating if you need an immutable snapshot.
snapshot = dict(cfg.__dict__)   # create a shallow copy
cfg.mode = "staging"            # mutate original
print("Snapshot:", snapshot)    # Snapshot: {'mode': 'prod', 'port': 8000, 'host': '
print("Current:", cfg.__dict__) # Current: {'mode': 'staging', 'port': 8000, 'host': '0.0.0.0'}


print("\n# -----------------------------")
print("# 5. Objects without __dict__ (using __slots__)")
print("# -----------------------------\n")

class Lightweight:
    __slots__ = ("x", "y") # restrict attributes to x and y only

lw = Lightweight()
lw.x = 10   # valid
lw.y = 20   # valid

print(hasattr(lw, "__dict__"))  # False → slots remove per-instance dict to save memory

try:
    lw.__dict__
except AttributeError as exc:
    print("Accessing __dict__ failed:", exc)


print("\n# -----------------------------")
print("# 6. Debugging and serialization helpers")
print("# -----------------------------\n")

import json

class Job:
    def __init__(self, title, salary):
        self.title = title
        self.salary = salary

job = Job("Engineer", 120_000)
print("Debug:", job.__dict__) # Debug: {'title': 'Engineer', 'salary': 120000}

print("JSON dump:", json.dumps(job.__dict__)) # JSON dump: {"title": "Engineer", "salary": 120000}

# Creating objects from dictionaries
data = {"title": "Manager", "salary": 150_000}
job2 = Job(**data) # unpack dict into constructor
print("job2.__dict__ =", job2.__dict__) # job2.__dict__ = {'title': 'Manager', 'salary': 150000}
