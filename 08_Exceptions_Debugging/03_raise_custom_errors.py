# 03_raise_custom_errors.py
# -------------------------------------
# Raising Custom Exceptions in Python
# -------------------------------------

# Sometimes, you want to manually raise an error when a certain condition is not met.
# Python allows you to do this using the 'raise' keyword.

print("Example 1: Basic custom error raising\n")

age = int(input("Enter your age: "))

if age < 0:
    # Raise a built-in exception manually
    raise ValueError("❌ Age cannot be negative!")
elif age < 18:
    print("⚠️ You are under 18. Access restricted.")
else:
    print("✅ Access granted! You are an adult.")


print("\nExample 2: Defining and raising your own custom exception class\n")

# You can define your own custom exception type for more meaningful error messages.
class InsufficientBalanceError(Exception):
    """Custom Exception for low account balance."""
    pass


def withdraw(balance, amount):
    if amount > balance:
        # Raise a custom exception
        raise InsufficientBalanceError("❌ Insufficient balance for withdrawal!")
    else:
        balance -= amount
        print(f"✅ Withdrawal successful. Remaining balance: {balance}")
    return balance


try:
    withdraw(500, 1000)
except InsufficientBalanceError as e:
    print(e)
finally:
    print("🏦 Transaction attempt complete.")
