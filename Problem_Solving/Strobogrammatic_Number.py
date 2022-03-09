# Atharv Kolhar
# Python Bytes

"""
A strobogrammatic number is a positive number
that appears the same after being rotated 180 degrees.
For example, 16891 is strobogrammatic.

Create a program that finds all strobogrammatic numbers with N digits.
"""


def get_strobogrammatic_numbers(n):

    def helper_func(n, length):
        if n == 0:
            return [""]
        if n == 1:
            return ["1", "8", "0"]

        middle = helper_func(n-2, length)
        results = []
        for mid in middle:
            if n != length:
                results.append("0"+mid+"0")
            results.append("1" + mid + "1")
            results.append("8" + mid + "8")
            results.append("6" + mid + "9")
            results.append("9" + mid + "6")

        return results

    result = helper_func(n, n)

    return result


if __name__ == '__main__':
    print(get_strobogrammatic_numbers(5))
