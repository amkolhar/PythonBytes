# Atharv Kolhar
# Python Bytes

# https://www.youtube.com/channel/UC71nPTNDEG7oyusXTifvB7g?sub_confirmation=1

"""
Tuple
"""

# Declaration
var_tuple = (1, 2, 3)
print(var_tuple)
print(type(var_tuple))

var_tuple_1 = 1, 2, 3
print(var_tuple_1)
print(type(var_tuple_1))

# Function for Tuples
# Counting the element repeated in the tuple
var_tuple_2 = (1, 1, 2, 3, 2, 1, 4, 1)
print(var_tuple_2.count(1))
print(var_tuple_2.count(4))

# Index finding
print(var_tuple_2.index(1))
print(var_tuple_2.index(1, 2, 6))

# Changing the Data Type

# Tuple to List
var_list_from_tuple = list(var_tuple_2)
print(var_list_from_tuple)
print(type(var_list_from_tuple))


# List to Tuple
var_tuple_from_list = tuple(var_list_from_tuple)
print(var_tuple_from_list)
print(type(var_tuple_from_list))


# End