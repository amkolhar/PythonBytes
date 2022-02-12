# Atharv Kolhar
# Python Bytes

"""
Dictionary
"""

# Declare a Dictionary
friends = {'Monica': 'Chef',
           'Rachel': 'Fashion',
           'Chandler': 'Works with numbers',
           'Joey': 'Actor'}

print(friends)

# Add a new key-value pair
friends['Ross'] = 'Paleontologist'

print(friends)

# get all the keys in Dictionary

key_dict = friends.keys()
print(key_dict)

# get all the values in the Dictionary
value_dict = friends.values()
print(value_dict)

# Rewrite a value of key in Dictionary
friends['Rachel'] = 'Waitress'

print(friends)

# Nested Dictionary
friends_apt = {'apt_girls': {'Monica': 'Chef',
                             'Rachel': 'Fashion'},
               'apt_boys': {'Chandler': 'Works with numbers',
                            'Joey': 'Actor'}}

print(friends_apt)

print(friends_apt['apt_boys']['Joey'])

# End
