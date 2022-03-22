# Atharv Kolhar
# Python Bytes

"""
The number 6174 is known as Kaprekar's constant, after the mathematician
who discovered an associated property: for all four-digit numbers with at
least two distinct digits, repeatedly applying a simple procedure eventually
results in this value. The procedure is as follows:

1. For a given input x, create two new numbers that consist of the digits in
    x in ascending and descending order.
2. Subtract the smaller number from the larger number.
For example, this algorithm terminates in three steps when starting from 1234:

4321 - 1234 = 3087
8730 - 0378 = 8352
8532 - 2358 = 6174
Write a function that returns how many steps this will take for a given input N.
"""


def steps_to_reach_kaprekar_constant(n):
    steps = 0
    kaprekar_const = 6174
    difference = n

    while difference != kaprekar_const:
        n_str = str(difference)
        smallest_n = int(''.join(sorted(n_str)))
        largest_n = int(''.join(sorted(n_str, reverse=True)))

        difference = largest_n - smallest_n
        print(f"{largest_n} - {smallest_n} = {difference}")

        steps += 1

    return steps


if __name__ == "__main__":
    print(steps_to_reach_kaprekar_constant(8881))
