# 🔁 05_Conditionals_Loops

Welcome to the **Conditionals and Loops** section!  
This section teaches how to control the **flow of your Python programs** — making decisions and repeating actions automatically.  
These are the building blocks for logic, automation, games, and interactive applications.

---

## 📘 Overview

You’ll learn:
- How to use **if**, **elif**, and **else** statements for decision-making.  
- The role of the **match-case** statement (introduced in Python 3.10) for cleaner multi-condition checks.  
- How to create loops using **while** and **for** statements.  
- How to control loop behavior with **break**, **continue**, and **pass**.  
- How to organize and test your understanding with practice exercises.

---

## 🧩 Files Description

| File Name | Description |
|------------|-------------|
| `01_if_elif_else_ladder.py` | Explains how to handle multiple conditions using the if-elif-else ladder structure. |
| `02_match_case.py` | Introduces the `match-case` statement (Python 3.10+) as an alternative to long if-elif chains. |
| `03_while_loop.py` | Covers the basics of `while` loops, including conditions and counters. |
| `04_loop.py` | Demonstrates how loops work in general and how they can automate repetitive tasks. |
| `05_for_loop.py` | Explains `for` loops for iterating over sequences like lists, strings, and ranges. |
| `06_break_continue_statement.py` | Shows how `break` exits a loop early and `continue` skips an iteration. |
| `07_pass_statement.py` | Explains the use of the `pass` keyword as a placeholder in loops or conditionals. |

---

## 📂 Practice Folder

### `Practice_Exercises/`
This folder contains hands-on scripts and mini problems related to **conditionals and loops**.  
It’s designed to help you practice and apply the concepts you’ve learned.

Example challenges include:
- Checking whether a number is even or odd.  
- Finding the largest of three numbers using if-elif-else.  
- Printing multiplication tables using `for` loops.  
- Building simple patterns using nested loops.  
- Using `while` loops to simulate countdowns or menu-driven programs.

---

## 🧠 Example Code

```python
# If-Elif-Else Ladder
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

# For Loop Example
for i in range(1, 6):
    if i == 3:
        continue  # skip number 3
    if i == 5:
        break     # stop the loop at 5
    print("Number:", i)
```

---

**Next Section →** [06_Functions_Recursion](../06_Functions_Recursion/README.md)