# 🧮 05_truth_tables.py
# -----------------------------------
# This script displays truth tables for the logical operators:
# AND, OR, and NOT in Python.
# Truth tables are a great way to visualize how logical operators work.

# 🧠 Logical operators recap:
# and → True only if both operands are True
# or  → True if at least one operand is True
# not → Reverses the Boolean value

# Define possible Boolean values
values = [True, False]

# Print headers
print("=" * 40)
print("        🧾 TRUTH TABLES IN PYTHON")
print("=" * 40)

# ---------- AND OPERATOR ----------
print("\n🔹 AND Operator (A and B)")
print("-" * 30)
print("A\t\tB\t\tA and B")
print("-" * 30)
for A in values:
    for B in values:
        print(f"{A}\t{B}\t{A and B}")

# ---------- OR OPERATOR ----------
print("\n🔹 OR Operator (A or B)")
print("-" * 30)
print("A\t\tB\t\tA or B")
print("-" * 30)
for A in values:
    for B in values:
        print(f"{A}\t{B}\t{A or B}")

# ---------- NOT OPERATOR ----------
print("\n🔹 NOT Operator (not A)")
print("-" * 20)
print("A\t\tnot A")
print("-" * 20)
for A in values:
    print(f"{A}\t{not A}")

# 🧩 Bonus Example — Combining Conditions
print("\n🔹 Combined Example")
print("-" * 40)
print("A\t\tB\t\t(A and B) or not A")
print("-" * 40)
for A in values:
    for B in values:
        print(f"{A}\t{B}\t{(A and B) or not A}")

# 🧠 Tip:
# Truth tables help in understanding complex logical expressions.
# They are very useful when debugging or designing decision-making logic.
# For example, in conditionals or AI logic, knowing exact Boolean behavior is essential.
