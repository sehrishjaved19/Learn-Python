# 01_try_except.py
# -------------------------------------
# Understanding the try-except block in Python
# -------------------------------------

# In Python, errors that occur during runtime are called *exceptions*.
# If an exception is not handled, the program will crash.
# The try-except block lets us handle errors gracefully.

print("Example 1: Basic try-except\n")

try:
    # Risky code that might cause an error
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("❌ Cannot divide by zero! Please try again.")
except ValueError:
    print("❌ Invalid input! Please enter a valid number.")

print("\nProgram continues after handling the exception.\n")


# Example 2: Multiple except blocks for different errors
print("Example 2: Handling multiple errors separately\n")

try:
    nums = [10, 20, 30]
    index = int(input("Enter an index (0-2): "))
    print("Value:", nums[index])
except IndexError:
    print("❌ Index out of range!")
except ValueError:
    print("❌ Please enter a valid integer for index.")

print("\nAll exceptions handled successfully!")
