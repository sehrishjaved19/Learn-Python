# 04_debugging_tips.py
# -------------------------------------
# Debugging Techniques in Python
# -------------------------------------
# Debugging is the process of identifying and fixing errors or bugs in your code.
# Here are several useful methods to debug Python programs.

# 🐞 Example 1: Using print() statements
print("Example 1: Debugging with print statements\n")

def divide(a, b):
    print(f"DEBUG: a = {a}, b = {b}")  # helps trace variable values
    return a / b

try:
    result = divide(10, 0)
    print("Result:", result)
except ZeroDivisionError:
    print("❌ Cannot divide by zero.")


# 🧠 Example 2: Using assert statements
print("\nExample 2: Debugging with assert\n")

# The assert keyword tests if a condition is True.
# If not, it raises an AssertionError.
x = -5
assert x > 0, "x must be positive!"


# 🧩 Example 3: Using the built-in breakpoint() for interactive debugging
print("\nExample 3: Using breakpoint() (Python 3.7+)\n")

# breakpoint() opens the Python Debugger (PDB) at that line.
# You can inspect variable values and step through code interactively.

def add_numbers(a, b):
    breakpoint()  # execution will pause here in debugging mode
    return a + b

try:
    sum_result = add_numbers(3, 7)
    print("Sum:", sum_result)
except Exception as e:
    print("Debugger ended:", e)


# 🧰 Example 4: Debugging Tips Summary
print("\nExample 4: Useful Debugging Tips\n")
print("""
✅ Use clear and descriptive variable names.
✅ Run code in small parts to isolate issues.
✅ Add print() or logging statements for tracing.
✅ Use try-except blocks to handle predictable errors.
✅ Use IDE tools (like VS Code debugger or PyCharm breakpoints).
✅ Don't ignore error messages — they guide you to the issue.
""")
