# 🔗 04_logical_operators.py
# -----------------------------------
# This script demonstrates the use of logical operators in Python.
# Logical operators combine multiple conditions and return a Boolean value (True or False).

# There are three main logical operators in Python:
# 1. and
# 2. or
# 3. not

# Let's start with some example variables
a = 10
b = 5
c = 15

print("a =", a)
print("b =", b)
print("c =", c)
print()

# ✅ 'and' Operator
# Returns True only if *both* conditions are True.
print("a > b and a < c:", a > b and a < c)  # True (both True)
print("a > c and b < a:", a > c and b < a)  # False (one condition is False)

# ✅ 'or' Operator
# Returns True if *at least one* condition is True.
print("a > c or b < a:", a > c or b < a)    # True (second condition is True)
print("a < b or b > c:", a < b or b > c)    # False (both False)

# ✅ 'not' Operator
# Reverses the result — True becomes False, and False becomes True.
print("not(a > b):", not(a > b))            # False (because a > b is True)
print("not(b > a):", not(b > a))            # True (because b > a is False)

print("\n--- Combining Logical Operators ---")

# You can combine logical operators for complex conditions.
age = 20
has_id = True

# Example: only allow entry if age >= 18 AND has ID
if age >= 18 and has_id:
    print("Access granted ✅")
else:
    print("Access denied ❌")

# Example: check if a number lies between two values
num = 12
if num > 5 and num < 15:
    print(f"{num} is between 5 and 15.")
else:
    print(f"{num} is not between 5 and 15.")

# 🧠 Tip:
# Logical operators are often used in:
# - Conditional statements (if, elif, else)
# - Loops (while conditions)
# - Input validation
# - Complex decision-making

print("\n--- Quick Truth Table Review ---")
print("True and True  =", True and True)
print("True and False =", True and False)
print("False and True =", False and True)
print("False and False=", False and False)
print()
print("True or True   =", True or True)
print("True or False  =", True or False)
print("False or True  =", False or True)
print("False or False =", False or False)
print()
print("not(True) =", not(True))
print("not(False) =", not(False))
