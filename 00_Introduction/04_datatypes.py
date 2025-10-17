# DataTypes are of two type(Mutable and immutable)
# MUTABLE OBJECT CAN CHANGE ITS STATE OR CONTENTS AND IMMUTABLE OBJECTS CANNOT.

#Number
a =  5
print(a, "is of type ", type(a))
b =  3.0
print(b, "is of type ", type(b))
c =  5 +2j
print(c, "is of type ", type(c))

#string 
s = "This is a string"
print(s, "is of type ", type(s))
s = '''Hello,
This is a multiline string'''
print(s, "is of type ", type(s))

#list
l = [10,"hi",34.6,True]
l[1] = "Hello" # showing list is mutable
print(l, "is of type ", type(l))

#Tuple
t = (5,"new",78.6,1+3j)
print(t, "is of type ", type(t))

#Dictionary (key is immutable but value is mutable)
d = {
    "name" : "Sehrish",
    "age" : 19,
}
print(d)
print(type(d))
print(d["name"])

#set (immutable)
my_set = {1,2,3,6,3,2,1}
print(my_set)
print(type(my_set))








