friends=['apple','3.14','aiman',False,'new']
print(friends)

friends.append('sehrish')#this will insert the value at the end of the string
print(friends)

l1=[1,45,654,342,12,98]
l1.sort()#this will sort the values in sequence of incressing order 
print(l1)

l1.reverse()
print(l1)#this will reverse the order
 
l1.insert(3,'shero')
print(l1)#this will insert the shero at index 3

value=(l1.pop(3))
print(value)#this will print the value at index 3
print(l1)#this will print the list excluding the value at index3


# Both pop() and remove() are used to delete elements from a list in Python, but they work differently.

# pop() → Removes by index
# Removes the item at a specific position

# Returns the removed item

# If no index is given, it removes the last item




# remove() → Removes by value
# Removes the first occurrence of a value

# Does not return the item

# If the value is not found, it raises an error

lst = [10, 20, 30, 20]

lst.pop(1)           # Removes item at index 1 → 20
lst.remove(20)       # Removes the first 20 (by value)
print(lst)




