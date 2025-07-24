#Recursion is a programming technique where a function calls itself to solve a problem.
#Instead of using loops, recursion breaks a problem into smaller sub-problems of the same type and solves them using repeated function calls.

def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call

print("The factorial is", (factorial(5)))
