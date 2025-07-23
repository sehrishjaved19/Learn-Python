#functions with Arguments


#A parameter is the variable listed inside the parentheses in a function definition.
# Think of it as a placeholder that accepts a value when the function is called.


#An argument is the actual value passed to the function when you call it.
#This value replaces the parameter inside the function.


# "a function can accept some value it can work with, we can put these values in the parantheses"
def greet(name, ending):
    print('Good Afternoon,'+ name)
    print(ending)
    return 'ok'# this will cause the vaiable to retun ok as an output

greet('Sehrish','Thank You')
#in the above function, name is a variable which will store the the value when function will be called abd provided by the value.
a  = greet('Aiman', 'Thanks')
print(a)
#'a' store a retun value, which is ok defined in the definition



# Default Parameter value
def Greet(Name,Ending='Thank you!'):
    print('Good Evening,'+ Name)
    print(Ending)
    return
Greet('Sehrish','Thanks')
Greet('Aiman')