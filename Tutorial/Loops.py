# Atharv Kolhar
# Python Bytes

"""
Loops
"""

# What is Range?
a = range(10)
print(a)
print(list(a))

b = range(1, 10, 2)
print(list(b))

# For loop

for i in range(10):
    print(i)

# For loop with list
rainbow = ['Voilet', 'Indigo', 'Blue', 'Green', 'Yellow', 'Orange', 'Red']

for color in rainbow:
    print(color)

# For loop with Dictionary
world = {'USA': 'Washington',
         'India': 'New Delhi',
         'England': 'London',
         'France': 'Paris',
         'Egypt': 'Cairo'}

for k in world.keys():
    print(k)

for v in world.values():
    print(v)

for k,v in world.items():
    print(f"{v} is capital of  {k}")

# While loop

n = 0

while n < 5:
    print(n)
    n += 1
    if n == 3:
        break
else:
    print("While loop ended")


# End
