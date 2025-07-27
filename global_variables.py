# Global Variables
# Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

# Global variables can be used by everyone, both inside of functions and outside.

#creating variable out side a function and using it oinside a function

x='awesome'#outside func

def myfunc():
    print('Python is ' + x)#used outside variable inside func


myfunc()#invoking func