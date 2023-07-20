# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 18:51:51 2023

@author: BHARGAV REDDY
"""

def rotate(matrix):
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to get the final result (clockwise rotation)
    for i in range(n):
        matrix[i] = matrix[i][::-1]

    return matrix

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(matrix1)
print(matrix1)

matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
rotate(matrix2)
print(matrix2)