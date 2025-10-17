# 🧾 02_assignment_operators.py
# -----------------------------------
# This script demonstrates the use of assignment operators in Python.
# Assignment operators are used to assign values to variables
# and update them efficiently.

# Start with a base value
x = 10
print("Initial value of x:", x)

# ➕= Add AND assignment
# Adds the right operand to x and assigns the result back to x
x += 5   # Equivalent to: x = x + 5
print("After x += 5:", x)

# ➖= Subtract AND assignment
# Subtracts the right operand and assigns the result back to x
x -= 3   # Equivalent to: x = x - 3
print("After x -= 3:", x)

# ✖️= Multiply AND assignment
# Multiplies and reassigns the result
x *= 2   # Equivalent to: x = x * 2
print("After x *= 2:", x)

# ➗= Divide AND assignment
# Divides and reassigns the result (returns float)
x /= 4   # Equivalent to: x = x / 4
print("After x /= 4:", x)

# //= Floor divide AND assignment
# Performs floor division and updates x
x //= 2  # Equivalent to: x = x // 2
print("After x //= 2:", x)

# %=: Modulus AND assignment
# Takes remainder and assigns it back
x %= 3   # Equivalent to: x = x % 3
print("After x %= 3:", x)

# **= Exponentiation AND assignment
# Raises x to the power of the right operand and assigns result back
x **= 2  # Equivalent to: x = x ** 2
print("After x **= 2:", x)

# 🧠 Tip:
# Assignment operators save time when you want to update a variable repeatedly.
# They’re commonly used in loops and counters.
# Example:
count = 0
count += 1  # Increases count by 1
print("Counter Example -> count:", count)
