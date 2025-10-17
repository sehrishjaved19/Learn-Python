# 🔁 05_Conditionals_Loops

Welcome to the **Conditionals and Loops** section!  
This section teaches how to control the **flow of your Python programs** — making decisions and repeating actions automatically.  
These are the core building blocks for logic, automation, games, and interactive applications.

---

## 📘 Overview

In this section, you will learn:

- How to use **if**, **elif**, and **else** statements for decision-making.  
- The role of the **match-case** statement (introduced in Python 3.10) for cleaner multi-condition checks.  
- How to create loops using **while** and **for** statements.  
- How to control loop behavior using **break**, **continue**, and **pass**.  
- How to practice and test your understanding with exercises and challenges.

---

## 🧩 Folder Structure

```

├── 05_Conditionals_Loops/
│   ├── 01_if_elif_else_ladder.py
│   ├── 02_match_case.py
│   ├── 03_while_loop.py
│   ├── 04_loop.py
│   ├── 05_for_loop.py
│   ├── 06_break_continue_statement.py
│   ├── 07_pass_statement.py
│   ├── Practice_Exercises/
│   └── README.md

```

---

## 📂 Files Description

| File Name | Description |
|------------|-------------|
| `01_if_elif_else_ladder.py` | Demonstrates how to handle multiple conditions using the **if-elif-else** ladder structure. |
| `02_match_case.py` | Introduces the **match-case** statement (Python 3.10+) as a clean alternative to long if-elif chains. |
| `03_while_loop.py` | Covers the basics of **while loops**, including counters and conditions. |
| `04_loop.py` | Explains how loops work conceptually and automate repetitive tasks. |
| `05_for_loop.py` | Shows how **for loops** iterate over sequences like lists, strings, and ranges. |
| `06_break_continue_statement.py` | Explains how **break** exits a loop early and **continue** skips an iteration. |
| `07_pass_statement.py` | Describes the **pass** keyword as a placeholder in loops or conditionals. |

---

## 🧠 Example Programs

```python
# If-Elif-Else Ladder Example
marks = 85
if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
else:
    print("Keep improving!")

# Match-Case Example (Python 3.10+)
choice = 2
match choice:
    case 1:
        print("You chose Option 1")
    case 2:
        print("You chose Option 2")
    case _:
        print("Invalid choice")

# While Loop Example
count = 0
while count < 3:
    print("Count is:", count)
    count += 1

# For Loop Example with break and continue
for i in range(1, 6):
    if i == 3:
        continue  # Skip number 3
    if i == 5:
        break     # Stop the loop at 5
    print("Number:", i)
```

---

## 🧩 Practice Exercises

The `Practice_Exercises/` folder includes small projects and logic-building challenges related to **conditionals and loops**.

### Example Challenges:

* Check whether a number is even or odd.
* Find the largest of three numbers using `if-elif-else`.
* Print multiplication tables using `for` loops.
* Generate simple patterns using nested loops.
* Create a countdown or menu-driven program using `while` loops.

---

## 🚀 Next Section

Continue your learning journey with **[06_Functions_Recursion →](../06_Functions_Recursion/README.md)**

---
