# Atharv Kolhar
# Python Bytes

"""
Conditional Statements
"""

# Comparators
# Equal
print(3 == 3)

# Greater than equal to
print(4 >= 5)

# Less than equal to
print(3 <= 5)

# Not equal to
print(3 != 4)

# Connectors
# and
print((3 == 3) and (3 <= 2))

# T and T == T
# T and F == F
# F and F == F

# or
print((3 == 3) or (3 <= 2))

# T or T == T
# T or F == T
# F or F == F

# Example to understand conditional statement
"""
Let is create a ticket pricing program:

0 - 2  years= Free = $ 0
2 - 12 years = $ 5
12 - 18 years = $ 8
18 - 65 years = $ 10
65 - older = $ 5
"""

age = input("What is your age? ")
age = int(age)

if 0 < age < 2:
    print(" Ticket cost : Free")
elif 2 <= age < 12:
    print("Ticket cost : $ 5")
elif 12 <= age < 18:
    print("Ticket cost : $ 8")
elif 18 <= age < 65:
    print("Ticket cost : $ 10")
else:
    print("Ticket cost : $ 5")

# End
