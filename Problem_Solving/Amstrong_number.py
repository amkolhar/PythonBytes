# Atharv Kolhar
# Python Bytes
"""
Armstrong Number
Check if the given number is an Armstrong Number.

A positive integer of n digits is called an Armstrong number of order n
(Order is number of digits) if
abcd ... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) ...

Example:
153 = 1*1*1 + 5*5*5 + 3*3*3

"""


def is_armstrong(number):
    n = len(str(number))

    temp_number = number
    sum = 0

    while temp_number != 0:
        # Get the last digit
        last_digit = temp_number % 10
        sum += pow(last_digit, n)
        temp_number = temp_number // 10

    return sum == number


if __name__ == "__main__":
    print(is_armstrong(number=124))
    print("Test")
