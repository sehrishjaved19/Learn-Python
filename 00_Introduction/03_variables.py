# Variables in Python
# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.
x=5
y='Sehrish'
print(x)
print(y)

x = 4 
x = 'sweet'
print(x) # sweet will be printed

x = str(3) #x will be '3'
y = int(3) #y will be 3
z =float(3) #z will be 3.0
print(x,y,z)

x=5
y='Sehrish'
z= 3.5
print(type(x))
print(type(y))
print(type(z)) # type() function is used to print the data type of the variable

# String variables can be declared either by using single or double quotes, can also use triple quotation marks to print multiple lines.
x = "Ania"
y = 'Ania'
z = '''Ania'''
print(x,y,z)

# Variable names are case-sensitive
a = 4
A = "Sehrish" #A will not overwrite a
print(a,A)

# Rules for Python variables:

# A variable name must starts with a letter or underscore character.
# A variable name  cannot starts with a number.
# A variable name  can only contain alphanumeric characters and underscore.
# A variable names are case-sensitive
# A variav;le name cannot be any of the Python keywords
myvar = 'ayat'
my_var = 'alina'
_my_var = 'asifa'
myVar = 'azqa'
MYVAR = 'AINA'
myvar2 = 'aniqa'
print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

# Pythin allows you to assign values to multiple variables in one line:
x = y = z = 'orange', 'banana', ' charry'
print(x)
print(y)
print(z)

#the python print()function is often used to output variables 
x = "Python"
y = "is"
z = "awesome"
print(x,y,z)

# Golbal variables can be used by everyone, both inside and outside of functions 
x = "awesome"
def myfunc():
    x="Fantastic"
    print("Python is "+ x)

myfunc()
print("Python is"+ x)

# another example#
def myfunc():
    global x
    x= "Fantastic"

myfunc()
print("Python is"+ x)








