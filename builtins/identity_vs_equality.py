# ============================================================
#           IDENTITY vs EQUALITY — PYTHON LESSON
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   This lesson explains the difference between:
#       - "=="  (equality — compares values)
#       - "is"  (identity — compares memory references)
#   with clear, runnable examples.
#
# Contents:
#   1. Equality (==)
#   2. Identity (is)
#   3. Mutables vs immutables
#   4. When to use "is"
#   5. Dangerous cases and common mistakes
#   6. Practical examples and diagnostics
# ============================================================


# ============================================================
# 1. EQUALITY USING ==
# ============================================================
print("\n--- SECTION 1: Equality (==) ---")

a = [1, 2]
b = [1, 2]

print("a == b:", a == b)   # True — lists contain the same values
print("a is b:", a is b)   # False — two different list objects


# ============================================================
# 2. IDENTITY USING is
# ============================================================
print("\n--- SECTION 2: Identity (is) ---")

x = [10, 20]
y = x

print("x == y:", x == y)   # True — same content
print("x is y:", x is y)   # True — same object in memory


# ============================================================
# 3. MUTABLE VS IMMUTABLE OBJECTS
# ============================================================
print("\n--- SECTION 3: Mutable vs Immutable ---")

# Immutable values like small integers may be reused internally.
n1 = 100
n2 = 100
print("n1 is n2:", n1 is n2)   # often True (cached small integers)

# Larger integers are not guaranteed to be the same object.
n3 = 1000
n4 = 1000
print("n3 is n4:", n3 is n4)   # often False (different objects)

# Strings may or may not be interned.
s1 = "hello"
s2 = "hello"
print("s1 is s2:", s1 is s2)   # often True (interned)

s3 = "a long string with spaces"
s4 = "a long string with spaces"
print("s3 is s4:", s3 is s4)   # may be False


# ============================================================
# 4. WHEN TO USE "is"
# ============================================================
print("\n--- SECTION 4: Correct usage of 'is' ---")

value = None

print("value is None:", value is None)   # correct
print("value == None:", value == None)   # allowed but not recommended


# ============================================================
# 5. COMMON MISTAKES
# ============================================================
print("\n--- SECTION 5: Common mistakes ---")

print("5 is 5:", 5 is 5)     # may be True but should NOT be relied on
print("5 == 5:", 5 == 5)     # correct way to compare numbers

print('"ab" is "ab":', "ab" is "ab")   # unpredictable
print('"ab" == "ab":', "ab" == "ab")   # correct


# ============================================================
# 6. PRACTICAL DIAGNOSTIC EXAMPLE
# ============================================================
print("\n--- SECTION 6: Practical diagnostic example ---")

try:
    5 / "2"
except Exception as e:
    print("Exception type:", type(e).__name__)
    print("Exception class is TypeError:", type(e) is TypeError)
