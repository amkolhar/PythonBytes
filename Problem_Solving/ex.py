"""
On a mysterious island there are magical Dragons which come in three colors:
red, green, and blue.
One power of the Dragon is that if two of them are standing next to each other,
they can transform into a single Dragon of the third color.

Given N Dragons standing in a line, determine the smallest number of them
remaining after any possible sequence of such transformations.

For example, given the input ['R', 'G', 'B', 'G', 'B'],
it is possible to end up with a single Qux through the following steps:

        Arrangement       |   Change
----------------------------------------
['R', 'G', 'B', 'G', 'B'] | (R, G) -> B
['B', 'B', 'G', 'B']      | (B, G) -> R
['B', 'R', 'B']           | (R, B) -> G
['B', 'G']                | (B, G) -> R
['R']                     |
"""

def dragon_power(dragon_1, dragon_2):
    dragon_possible = ['R', 'G', 'B']
    dragon_possible.remove(dragon_1)
    dragon_possible.remove(dragon_2)

    return dragon_possible[0]

dragons = ['R', 'G', 'B', 'G', 'B']
