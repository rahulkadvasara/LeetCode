# 2133. Check if Every Row and Column Contains All Numbers
# Easy

# An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).
# Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.

# Example 1:
# Input: matrix = [[1,2,3],[3,1,2],[2,3,1]]
# Output: true
# Explanation: In this case, n = 3, and every row and column contains the numbers 1, 2, and 3.
# Hence, we return true.

# Example 2:
# Input: matrix = [[1,1,1],[1,2,3],[1,2,3]]
# Output: false
# Explanation: In this case, n = 3, but the first row and the first column do not contain the numbers 2 or 3.
# Hence, we return false.
 
# Constraints:
# n == matrix.length == matrix[i].length
# 1 <= n <= 100
# 1 <= matrix[i][j] <= n



# sol 1

# class Solution:
#     def checkValid(self, matrix: List[List[int]]) -> bool:
#         n = len(matrix)
#         for i in range(n):
#             row = set(matrix[i])
#             col = set(matrix[j][i] for j in range(n))
#             if row != set(range(1, n + 1)) or col != set(range(1, n + 1)):
#                 return False
#         return True



# sol 2

# class Solution:
#     def checkValid(self, matrix):
#         m = len(matrix)
#         n = len(matrix[0])

#         for i in range(0, m):
#             row = matrix[i]
#             if (set(range(1, n+1)).difference(set(row)) != set()):
#                 return False

#         for j in range(0, n):
#             col = [matrix[i][j] for i in range(0, m)]
#             if (set(range(1, n+1)).difference(set(col)) != set()):
#                 return False
        
#         return True
    

# sol 3

# class Solution:
#     def checkValid(self, matrix: List[List[int]]) -> bool:
#         n=len(matrix)
#         for row in matrix:
#             if len(set(row))!=n: return False

#         transposed=list(zip(*matrix))
#         for column in transposed:
#             if len(set(column))!=n: return False
#         return True