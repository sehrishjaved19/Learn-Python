# 02_finally_else.py
# -------------------------------------
# Using else and finally blocks with try-except in Python
# -------------------------------------

# The 'else' block runs only if no exceptions occur inside the try block.
# The 'finally' block always runs, no matter what happens (success or error).
# 'finally' is often used for cleanup operations like closing files or releasing resources.

print("Example 1: try-except-else-finally\n")

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("❌ Division by zero is not allowed!")
except ValueError:
    print("❌ Invalid input! Please enter numbers only.")
else:
    # This block runs only if no exception occurs
    print("✅ Division successful. Result =", result)
finally:
    # This block always runs — even if an exception is raised
    print("🔚 Execution complete. Cleaning up resources if needed...\n")


print("Example 2: Using finally for file handling\n")

try:
    f = open("sample.txt", "w")
    f.write("Hello from Python File Handling Example!")
except Exception as e:
    print("❌ Error occurred while writing to file:", e)
finally:
    f.close()  # Ensures file is closed even if an error happens
    print("📁 File closed successfully!")
