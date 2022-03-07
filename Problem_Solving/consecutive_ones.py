# Atharv Kolhar
# Python Bytes

"""Given an integer n, return the length of the longest consecutive run
of 1s in its binary representation.

For example, given 156, you should return 3.
"""


def consecutive_ones_binary(num: int):
    bin_num = bin(num)
    print(bin_num)

    count = 0
    max_count = 0

    for bit in bin_num:
        if bit == '1':
            count += 1
            if max_count < count:
                max_count = count

        else:
            count = 0

    return max_count


if __name__ == '__main__':
    print(consecutive_ones_binary(156))
