# Atharv Kolhar
# Python Bytes

"""
List
"""

# Declaration of List
fruits = ["Apple", "Pineapple", "Banana", "Orange", "Mango"]
print(type(fruits))
print(fruits)

# Calling an element with index
print(fruits[2])

# Slicing the list
print(fruits[:3])
print(fruits[3:])

# Functions of List
# Length
print(len(fruits))


# Add a new element
fruits.append("Avocado")
print(fruits)

# Insert a new element at specific location
fruits.insert(2, "Grapes")
print(fruits)

# Sort the list
fruits.sort()
print(fruits)

# Reverse order of the list
fruits.reverse()
print(fruits)

# Remove an element from the end
fruits.pop()
print(fruits)

# Remove a specific element from list
fruits.remove("Mango")
print(fruits)

# Count the number of times an elements repeat in the list
new_list = ['a', 'a', 'a', 'b', 'c', 'd', 'd']
print(new_list.count('a'))
print(new_list.count('b'))

# What are Nested List?
new_list_1 = [1, 2, 'a', 'python']
print(new_list_1)

nest_list = [[1,2,3], ['a','b','c']]
print(nest_list)

# Getting an element in nested list
print(nest_list[1][2])
print(nest_list[0][0])
# End
