# 🐞 08_Exceptions_Debugging

Welcome to the **Exceptions and Debugging** section!  
This module focuses on how to **handle errors gracefully** and **find and fix bugs efficiently** in your Python programs.  
By mastering these concepts, you’ll learn how to make your programs more reliable and easier to maintain.

---

## 📘 Overview

In this section, you’ll learn:
- What exceptions are and why they occur.  
- How to handle errors using `try`, `except`, `else`, and `finally` blocks.  
- How to raise custom exceptions when specific conditions are not met.  
- How to debug code using print statements, assertions, and Python’s built-in debugger.

---

## 🗂️ Folder Structure

```
├── 08_Exceptions_Debugging/
│   ├── 01_try_except.py
│   ├── 02_finally_else.py
│   ├── 03_raise_custom_errors.py
│   ├── 04_debugging_tips.py
│   ├── Practice_Exercises/
│   └── README.md
```

---

## 🧩 Files Description

| File Name | Description |
|------------|-------------|
| `01_try_except.py` | Introduces the `try-except` structure for handling runtime errors gracefully. |
| `02_finally_else.py` | Demonstrates the use of `else` and `finally` clauses for cleaner error-handling logic. |
| `03_raise_custom_errors.py` | Shows how to raise user-defined exceptions using the `raise` keyword. |
| `04_debugging_tips.py` | Covers multiple debugging techniques including `print()`, `assert`, and `breakpoint()`. |

---

## 📂 Practice Folder

### `Practice_Exercises/`
This folder includes coding exercises to help you apply what you’ve learned.  
You’ll practice:
- Handling different types of errors (ZeroDivisionError, ValueError, etc.)  
- Writing custom exceptions.  
- Debugging faulty code to identify and fix logical or runtime bugs.  

Example exercises:
- Create a program that divides two numbers safely with `try-except`.  
- Build a temperature converter that raises an exception if invalid input is entered.  
- Debug a function that incorrectly calculates totals using `print()` and `breakpoint()`.

---

## 🧠 Example Code

```python
# Example: Handling Multiple Exceptions
try:
    num = int(input("Enter a number: "))
    print("Result:", 10 / num)
except ValueError:
    print("❌ Please enter a valid number!")
except ZeroDivisionError:
    print("❌ Cannot divide by zero!")
else:
    print("✅ Operation successful!")
finally:
    print("🎯 Execution completed.")
```

---


## 🎯 Learning Goals

By the end of this section, you’ll be able to:

* Write error-free and fault-tolerant programs.
* Identify, handle, and raise exceptions effectively.
* Use debugging tools and techniques to locate and fix issues efficiently.

---

**Next Section →** [09_Modules_and_Packages](../09_Modules_and_Packages/README.md)

---
