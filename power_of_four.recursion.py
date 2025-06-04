# 342. Power of Four
# Easy

# Given an integer n, return true if it is a power of four. Otherwise, return false.
# An integer n is a power of four, if there exists an integer x such that n == 4x.

# Example 1:
# Input: n = 16
# Output: true

# Example 2:
# Input: n = 5
# Output: false

# Example 3:
# Input: n = 1
# Output: true

# Constraints:
# -231 <= n <= 231 - 1
 
# Follow up: Could you solve it without loops/recursion?



# sol 1 

# class Solution:
#     def isPowerOfFour(self, n: int) -> bool:
#         if n==1:
#             return True
#         if n<=0 or n%4!=0:
#             return False
#         return self.isPowerOfFour(n//4)
    


# sol 2

# class Solution:
#     def isPowerOfFour(self, n: int) -> bool:
#         return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0
    

# sol 3

# class Solution:
#     def isPowerOfFour(self, n: int) -> bool:
#         if n <= 0:
#             return False
            
#         return math.log(n, 4).is_integer()
    

# sol 4

# class Solution:
#     def isPowerOfFour(self, n: int) -> bool:
#         if n <= 0:
#             return False
#         if n == 1:
#             return True

#         while n > 1:
#             if n % 4 != 0:
#                 return False
#             n //= 4

#         return True        
    

# sol 5

# class Solution:
#     def isPowerOfFour(self, n: int) -> bool:
#         return n>0 and ((n & (n-1))==0) and (n%3==1)
    


# sol 6

# class Solution:
#     def isPowerOfFour(self, n: int) -> bool:
#         r=0
#         while n>0:
#             r+=n%4
#             n=n//4
#         return r==1
    

# sol 7

# class Solution:
#     def isPowerOfFour(self, n: int) -> bool:
#         if (n>0):
#             x=log(n,4)
#             if (4**int(x)==n):
#                 return True
#         return False
    

# sol 8

# class Solution:
#     def isPowerOfFour(self, num: int) -> bool:  
#         if num != 0:
#             return (num & (num - 1) == 0) & len(bin(num)) % 2 == 1
#         return False
        

    
# sol 9

# import math
# class Solution:
#     def isPowerOfFour(self, n: int) -> bool:
#         if n <= 0:
#             return False
        
#         x = math.log(n) / math.log(4)
        
#         return x.is_integer()
    

# sol 10

# class Solution:
#     def isPowerOfFour(self, n: int) -> bool:
#         return n>0 and n & (-n)==n and (n%3==1)