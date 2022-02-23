# Atharv Kolhar
# Python Bytes

"""
Palindrome:
Create a function to find if the given string is Palindrome

Wiki Definition:
a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

Eg:
'abcba'
'MALAYALAM'
'22022022' - > This is the date when the code is written
"""

from datetime import datetime


def simple_check_palindrome(input_string):
    """
    :param input_string: str
    :return: Boolean True or False
    a"""
    palindrome = True

    input_string = input_string.upper()

    str_to_list = list(input_string)
    str_to_list.reverse()
    reversed_string = ''.join(str_to_list)

    palindrome = (input_string == reversed_string)

    return palindrome


def intelligent_check_palindrome(input_string):
    """
    Intelligent Solution
    :param input_string: str
    :return: Boolean True or False
    """
    palindrome = True
    input_string = input_string.upper()

    len_str = len(input_string)

    for i in range(len_str//2):
        if input_string[i] == input_string[len_str-i-1]:
            continue
        else:
            palindrome = False
            break

    return palindrome


input_str = 'Malayalam'
start_time = datetime.now()
print(simple_check_palindrome(input_str))
required_time = datetime.now() - start_time
print(required_time)

start_time = datetime.now()
print(intelligent_check_palindrome(input_str))
required_time = datetime.now() - start_time
print(required_time)
