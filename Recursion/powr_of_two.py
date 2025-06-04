# 231. Power of Two
# Easy

# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2x.

# Example 1:
# Input: n = 1
# Output: true
# Explanation: 20 = 1

# Example 2:
# Input: n = 16
# Output: true
# Explanation: 24 = 16

# Example 3:
# Input: n = 3
# Output: false

# Constraints:
# -231 <= n <= 231 - 1
 
# Follow up: Could you solve it without loops/recursion?



# sol 1 

# class Solution: 
#     def isPowerOfTwo(self, n: int) -> bool:
#         if not n:
#             return False
#         return n & (-n) == n



# sol 2

# class Solution: #O(logN) time
#     def isPowerOfTwo(self, n: int) -> bool:
#         if n == 1:
#             return True
#         if n % 2 == 1 or not n:
#             return False
#         return self.isPowerOfTwo(n // 2)
        


# sol 3
        
# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         if n==1:
#             return True
#         if n<=0 or n%2!=0:
#             return False
#         return self.isPowerOfTwo(n // 2)    