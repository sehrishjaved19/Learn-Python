# 🧮 01_arithmetic_operators.py
# -----------------------------------
# This script demonstrates basic arithmetic operators in Python.
# Arithmetic operators are used to perform mathematical operations
# on numbers (integers or floats).

# Let's start by defining two variables
a = 15
b = 4

# ➕ Addition
# Adds two numbers
addition = a + b
print("Addition (a + b):", addition)

# ➖ Subtraction
# Subtracts the second number from the first
subtraction = a - b
print("Subtraction (a - b):", subtraction)

# ✖️ Multiplication
# Multiplies two numbers
multiplication = a * b
print("Multiplication (a * b):", multiplication)

# ➗ Division
# Divides the first number by the second
# Returns a floating-point result
division = a / b
print("Division (a / b):", division)

# // Floor Division
# Divides and returns the largest integer less than or equal to the result
floor_division = a // b
print("Floor Division (a // b):", floor_division)

# % Modulus
# Returns the remainder of the division
modulus = a % b
print("Modulus (a % b):", modulus)

# ** Exponentiation
# Raises the first number to the power of the second
exponentiation = a ** b
print("Exponentiation (a ** b):", exponentiation)

# 🧠 Tip:
# You can also combine these operators with parentheses to control order of operations (precedence)
# Example:
result = (a + b) * 2
print("Result of (a + b) * 2:", result)
