# Global Variables
# Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

# Global variables can be used by everyone, both inside of functions and outside.

#creating variable out side a function and using it oinside a function

x='awesome'#outside func

def myfunc():
    print('Python is ' + x,'\n')#used outside variable inside func


myfunc()#invoking func



# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

# Example
# Create a variable inside a function, with the same name as the global variable

y = "awesome"

def myfunc():
  y = "fantastic"
  print("Python is " + y)

myfunc()
print("Python is " + y)

#Global Keyword
# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

# To create a global variable inside a function, you can use the global keyword.

# Example
# If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global z
  z = "fantastic"

myfunc()

print("Python is " + z)


# Also, use the global keyword if you want to change a global variable inside a function.

# Example
# To change the value of a global variable inside a function, refer to the variable by using the global keyword:

q = "awesome"

def myfunc():
  global q
  q = "fantastic"

myfunc()

print("Python is " + q)

