# _________Tuple Practice__________
print('Creating Tuple')

my_tuple = (1,2,3,"apple","banana",True)
empty_tuple = ()
single_element_tuple = (41,)#remember the comma for single elment tuples!
nested_tuple = ((10,20),(30,40))

print(f"my_tuple: {my_tuple}")
print(f"empty_tuple: {empty_tuple}")
print(f"single_element_tuple: {single_element_tuple}")
print(f"nested_tuple: {nested_tuple}")

# _________Accessing Elements (indexing)__________

print("\n2. Accessing Elements (Indexing):")
print(f"First element of my_tuple: {my_tuple[0]}")
print(f"Last element of my_tuple: {my_tuple[-1]}")
print(f"Element at index 3 of my_tuple: {my_tuple[3]}")
print(f"First element of the first nested tuple: {nested_tuple[0][0]}")

# _________Slicing Tuples__________

print("\n3. Slicing Tuples:")
sliced_tuple_1 = my_tuple[1:4]
sliced_tuple_2 = my_tuple[:3]
sliced_tuple_3 = my_tuple[3:]
sliced_tuple_4 = my_tuple[::2] # Every second element

print(f"my_tuple[1:4]: {sliced_tuple_1}")
print(f"my_tuple[:3]: {sliced_tuple_2}")
print(f"my_tuple[3:]: {sliced_tuple_3}")
print(f"my_tuple[::2]: {sliced_tuple_4}")

# 4. Tuple Immutability (Attempting to modify)
print("\n4. Tuple Immutability:")
try:
    my_tuple[0] = 99
except TypeError as e:
    print(f"Attempting to modify a tuple element (will cause error): {e}")

# 5. Tuple Concatenation
print("\n5. Tuple Concatenation:")
tuple_a = (1, 2, 3)
tuple_b = ("x", "y", "z")
combined_tuple = tuple_a + tuple_b
print(f"tuple_a: {tuple_a}")
print(f"tuple_b: {tuple_b}")
print(f"combined_tuple (tuple_a + tuple_b): {combined_tuple}")

# 6. Tuple Repetition
print("\n6. Tuple Repetition:")
repeated_tuple = (7, 8) * 3
print(f"(7, 8) * 3: {repeated_tuple}")

# 7. Checking Membership (in operator)
print("\n7. Checking Membership ('in' operator):")
print(f"Is 'apple' in my_tuple? {'apple' in my_tuple}")
print(f"Is 'grape' in my_tuple? {'grape' in my_tuple}")

# 8. Iterating through a Tuple
print("\n8. Iterating through a Tuple:")
for item in my_tuple:
    print(f"Item: {item}")

# 9. Tuple Length
print("\n9. Tuple Length:")
print(f"Length of my_tuple: {len(my_tuple)}")
print(f"Length of empty_tuple: {len(empty_tuple)}")

# 10. Tuple Packing and Unpacking
print("\n10. Tuple Packing and Unpacking:")
# Packing
coordinates = (10, 20, 30)
print(f"Packed tuple (coordinates): {coordinates}")

# Unpacking
x, y, z = coordinates
print(f"Unpacked values: x={x}, y={y}, z={z}")

# Swapping variables using tuple unpacking
a = 5
b = 10
print(f"Before swap: a={a}, b={b}")
a, b = b, a
print(f"After swap: a={a}, b={b}")

# Unpacking with * (for multiple elements)
data = (1, 2, 3, 4, 5, 6)
first, *middle, last = data
print(f"Data: {data}")
print(f"First: {first}, Middle: {middle}, Last: {last}")

# 11. Tuple Methods (count, index)
print("\n11. Tuple Methods (count, index):")
another_tuple = (1, 2, 2, 3, 1, 4, 2)
print(f"Another tuple: {another_tuple}")
print(f"Count of 2 in another_tuple: {another_tuple.count(2)}")
print(f"Index of first 3 in another_tuple: {another_tuple.index(3)}")

try:
    print(f"Index of 99 in another_tuple: {another_tuple.index(99)}")
except ValueError as e:
    print(f"Attempting to find index of non-existent element: {e}")

# 12. Tuples as Dictionary Keys
print("\n12. Tuples as Dictionary Keys:")
my_dict = {
    (1, 2): "Value A",
    ("hello", "world"): "Value B"
}
print(f"my_dict: {my_dict}")
print(f"Value for (1, 2): {my_dict[(1, 2)]}")

# 13. Converting between List and Tuple
print("\n13. Converting between List and Tuple:")
my_list = [10, 20, 30]
tuple_from_list = tuple(my_list)
print(f"List: {my_list}, Tuple from list: {tuple_from_list}")

my_new_tuple = (1, 2, 3, 4)
list_from_tuple = list(my_new_tuple)
print(f"Tuple: {my_new_tuple}, List from tuple: {list_from_tuple}")

print("\n--- End of Tuple Practice ---")




