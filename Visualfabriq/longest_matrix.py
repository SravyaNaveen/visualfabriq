# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 18:56:38 2023

@author: BHARGAV REDDY
"""

def longest_increasing_path(matrix):
    if not matrix:
        return 0

    m, n = len(matrix), len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def dfs(i, j):
        if memo[i][j] != -1:
            return memo[i][j]

        longest_path = 1
        for dx, dy in directions:
            x, y = i + dx, j + dy
            if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                longest_path = max(longest_path, 1 + dfs(x, y))

        memo[i][j] = longest_path
        return longest_path

    memo = [[-1 for _ in range(n)] for _ in range(m)]
    max_length = 0

    for i in range(m):
        for j in range(n):
            max_length = max(max_length, dfs(i, j))

    return max_length

matrix1 = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
print(longest_increasing_path(matrix1))  

matrix2 = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
print(longest_increasing_path(matrix2))  

matrix3 = [[1]]
print(longest_increasing_path(matrix3))