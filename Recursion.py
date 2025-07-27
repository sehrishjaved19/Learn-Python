# Python also accepts function recursion, which means a defined function can call itself.
# Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.


#Recursion is a programming technique where a function calls itself to solve a problem.
#Instead of using loops, recursion breaks a problem into smaller sub-problems of the same type and solves them using repeated function calls.

def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call

print("The factorial is", (factorial(5)))