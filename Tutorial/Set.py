# Atharv Kolhar
# Python Bytes

"""
Set
"""

# Declare Set
var_set = {1, 2, 3}
print(type(var_set))
print(var_set)

var_set_1 = {1, 2, 3, 4, 1, 2}
print(var_set_1)

# Function of Set
# add element to Set
var_set.add(4)
print(var_set)

# remove element from Set
var_set.remove(2)
print(var_set)

# clear a particular set
var_set.clear()
print(var_set)

# find difference between 2 sets
var_set_1 = {1, 2, 3, 4}
var_set = {1, 2, 3, 5}
var_diff = var_set.difference(var_set_1)
print(var_diff)

var_diff_1 = var_set_1.difference(var_set)
print(var_diff_1)

# find common elements in the set
var_common = var_set.intersection(var_set_1)
print(var_common)

# Join two sets
var_join = var_set.union(var_set_1)
print(var_join)

# Exit

