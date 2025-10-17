# ⚖️ 03_comparison_operators.py
# -----------------------------------
# This script demonstrates how comparison operators work in Python.
# These operators are used to compare two values and return a Boolean result — True or False.

# Let's start with two numbers
a = 10
b = 5

print("a =", a)
print("b =", b)
print()

# == Equal to
# Returns True if both values are equal
print("a == b:", a == b)  # False

# != Not equal to
# Returns True if both values are not equal
print("a != b:", a != b)  # True

# > Greater than
# Returns True if the left operand is greater than the right
print("a > b:", a > b)    # True

# < Less than
# Returns True if the left operand is smaller than the right
print("a < b:", a < b)    # False

# >= Greater than or equal to
# Returns True if the left operand is greater than or equal to the right
print("a >= b:", a >= b)  # True

# <= Less than or equal to
# Returns True if the left operand is smaller than or equal to the right
print("a <= b:", a <= b)  # False

print("\n--- Comparing Strings ---")

# You can also compare strings (alphabetical order, case-sensitive)
name1 = "Apple"
name2 = "Banana"
print("name1 =", name1)
print("name2 =", name2)
print("name1 == name2:", name1 == name2)
print("name1 != name2:", name1 != name2)
print("name1 < name2:", name1 < name2)   # True because 'A' comes before 'B'
print("name1 > name2:", name1 > name2)   # False

print("\n--- Boolean Results in Action ---")

# Use comparisons in conditional statements
if a > b:
    print("a is greater than b ✅")
else:
    print("a is not greater than b ❌")

# Comparing user-defined input (optional interactive part)
# Uncomment the lines below to test with user input
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")

# 🧠 Tip:
# Comparison operators are widely used in conditionals, loops, and sorting algorithms.
# Always remember: comparisons return Boolean values (True or False).
