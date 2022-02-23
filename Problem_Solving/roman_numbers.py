# Atharv Kolhar
# Python Bytes

"""
Write a Program to convert Integers to Roman Symbols
Between number 1 to 1000
"""


def integer_to_roman(number):
    n = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    rn = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']

    roman_num = ""

    i = len(n) - 1

    remainder = number

    while remainder != 0:
        quotient = remainder // n[i]
        remainder = remainder % n[i]

        roman_num += quotient * rn[i]

        i -= 1  # i = i - 1

    return roman_num


print(integer_to_roman(2022))
