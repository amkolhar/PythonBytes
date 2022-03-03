# Atharv Kolhar
# Python Bytes


"""
Rotate Matrix:
Given an N by N matrix, rotate it by 90 degrees clockwise.

For example, given the following matrix:

[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
you should return:

[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
"""

import numpy as np


def rotate_clockwise(matrix):
    matrix = np.matrix(matrix)

    print(matrix)

    n = len(matrix)

    new_matrix = np.zeros((n, n), int)

    # Operation 1 : Interchanging the elements
    for i in range(n):
        for j in range(n):
            new_matrix[i, j] = matrix[j, i]
        # Operation 2 :Flipping the rows
        new_matrix[i] = np.flip(new_matrix[i])

    return new_matrix


if __name__ == '__main__':
    old_matrix = [[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]]

    turned_matrix = rotate_clockwise(old_matrix)
    print(turned_matrix)
