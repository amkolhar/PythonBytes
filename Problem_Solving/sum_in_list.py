# Atharv Kolhar
# Python Bytes

"""
Given a list of numbers and a number k,
return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""


def check_addition(num_list, k):

    for i in num_list:
        remaining = k - i
        num_list.remove(i)
        if remaining in num_list:
            return True

    return False


print(check_addition([10,1,5,3,7], 14))