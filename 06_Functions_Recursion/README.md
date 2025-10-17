# 🧮 06_Functions_Recursion

Welcome to the **Functions and Recursion** section!  
This is one of the most powerful parts of Python — you’ll learn how to structure your code into reusable, organized blocks using **functions**, and how functions can call themselves through **recursion**.  

Functions help make code **modular**, **readable**, and **efficient**, while recursion introduces problem-solving through repeated self-calls.

---

## 📘 Overview

You’ll learn:
- How to **define and call functions** in Python.  
- How to use **parameters** and **return values** to make functions flexible.  
- The difference between **local** and **global** variables.  
- How **recursion** works and when it’s useful.  
- The concept of **base cases** and how to avoid infinite recursion.  

---

## 🧩 Files Description

| File Name | Description |
|------------|-------------|
| `01_functions_basics.py` | Introduces basic function syntax, calling, and organizing reusable blocks of code. |
| `02_return_and_parameters.py` | Explains how to pass arguments to functions and return results. |
| `03_global_variables_functions.py` | Demonstrates local vs global scope and how variables behave inside functions. |
| `04_recursion_basics.py` | Explains recursion with examples like factorial and countdown, showing how a function can call itself. |

---

## 📂 Practice Folder

### `Practice_Exercises/`
This folder contains practical coding challenges based on functions and recursion.  
It’s designed to help you strengthen your understanding through real exercises.  

Example challenges might include:
- Creating a function to calculate factorial or Fibonacci numbers.  
- Writing a recursive function to find the sum of natural numbers.  
- Building small utilities (e.g., greeting users, temperature conversion).  

---

## 🧠 Example Code

```python
# Basic Function Example
def greet(name):
    print(f"Hello, {name}!")

greet("Sehrish")

# Function with Return Value
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum is:", result)

# Recursion Example
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5 is:", factorial(5))
```
---
**Next Section →** [07_File_IO](../07_File_IO/README.md)