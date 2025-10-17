# 📦 09_Modules_and_Packages

Welcome to the **Modules and Packages** section!  
In Python, **modules** help you organize your code into reusable files, while **packages** allow you to group related modules together.  
This section introduces Python’s most commonly used **built-in modules** that make development faster and more efficient.

---

## 📘 Overview

You’ll learn:
- What modules and packages are, and how to use them.  
- How to import built-in and custom modules.  
- Practical applications of modules like `datetime`, `math`, `random`, and `re`.  
- How modular programming makes code reusable and easier to maintain.

---
## 🗂️ Folder Structure

```
├── 09_Modules_and_Packages/
│   ├── 01_built_in_modules.py
│   ├── 02_date_time_module.py
│   ├── 03_math_module.py
│   ├── 04_random_num.py
│   ├── 05_regex_module.py
│   ├── Practice_Exercises/
│   └── README.md
```

---


## 🧩 Files Description

| File Name | Description |
|------------|-------------|
| `01_built_in_modules.py` | Introduces Python’s built-in modules and shows how to import and use them (`import`, `from ... import ...`). |
| `02_date_time_module.py` | Demonstrates working with dates and times using the `datetime` module — including current time, formatting, and differences. |
| `03_math_module.py` | Covers mathematical operations and constants using the `math` module (`sqrt`, `pow`, `pi`, etc.). |
| `04_random_num.py` | Explains how to generate random numbers, choices, and shuffles using the `random` module. |
| `05_regex_module.py` | Introduces the `re` (Regular Expression) module for pattern matching and text searching. |

---

## 📂 Practice Folder

### `Practice_Exercises/`
This folder includes hands-on challenges and coding problems to reinforce what you’ve learned.

Example exercises:
- Create a simple **birthday countdown** using the `datetime` module.  
- Build a **math quiz generator** using the `random` module.  
- Extract all email addresses from a paragraph using **regular expressions**.  
- Calculate circle area and perimeter using constants from the `math` module.  

---

## 🧠 Example Code

```python
# Example: Using Built-in Modules

# Math module
import math
radius = 5
area = math.pi * math.pow(radius, 2)
print("Area of circle:", area)

# Datetime module
from datetime import datetime
current_time = datetime.now()
print("Current time:", current_time.strftime("%Y-%m-%d %H:%M:%S"))

# Random module
import random
print("Random number between 1 and 10:", random.randint(1, 10))

# Regex module
import re
text = "My email is example@test.com"
match = re.search(r"\S+@\S+", text)
if match:
    print("Email found:", match.group())
```

---

## 🗂️ Folder Structure

```
├── 09_Modules_and_Packages/
│   ├── 01_built_in_modules.py
│   ├── 02_date_time_module.py
│   ├── 03_math_module.py
│   ├── 04_random_num.py
│   ├── 05_regex_module.py
│   ├── Practice_Exercises/
│   └── README.md
```

---

## 🎯 Learning Goals

By the end of this section, you’ll be able to:

* Understand how Python’s module system works.
* Use built-in modules to perform real-world tasks efficiently.
* Apply modular programming to write clean, reusable code.
* Use regular expressions to search and process text data.

---

**Next Section →** [10_Object_Oriented_Programming](../10_Object_Oriented_Programming/README.md)

---

