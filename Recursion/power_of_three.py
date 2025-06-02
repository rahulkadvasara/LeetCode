# 326. Power of Three
# Easy

# Given an integer n, return true if it is a power of three. Otherwise, return false.
# An integer n is a power of three, if there exists an integer x such that n == 3x.

# Example 1:
# Input: n = 27
# Output: true
# Explanation: 27 = 33

# Example 2:
# Input: n = 0
# Output: false
# Explanation: There is no x where 3x = 0.

# Example 3:
# Input: n = -1
# Output: false
# Explanation: There is no x where 3x = (-1).

# Constraints:
# -231 <= n <= 231 - 1

# Follow up: Could you solve it without loops/recursion?



# sol 1 

# class Solution:
#     def isPowerOfThree(self, n: int) -> bool:
#         if n <= 0:
#             return False
#         while n % 3 == 0:
#             n //= 3
#         return n == 1


# sol 2

# class Solution:
#     def isPowerOfThree(self, n: int) -> bool:
#         return n > 0 and 1162261467 % n == 0

# sol 3

# class Solution:
#     def isPowerOfThree(self, n: int) -> bool:
#         return n > 0 and 3**19 % n == 0
    
# sol 4

# class Solution:
#     def isPowerOfThree(self, n: int) -> bool:
#         if n == 1:
#             return True
#         if n <= 0 or n % 3 != 0:
#             return False
#         return self.isPowerOfThree(n // 3)
    

# sol 5

# class Solution:
#     def isPowerOfThree(self, n: int) -> bool:
#         if(n<=0):
#             return False
#         while n > 1:
#             if n % 3 != 0:
#                 return False
#                 break
#             n //= 3
#         return True
        
        