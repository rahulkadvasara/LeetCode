# 50. Pow(x, n)
# Medium

# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

# Example 1:
# Input: x = 2.00000, n = 10
# Output: 1024.00000

# Example 2:
# Input: x = 2.10000, n = 3
# Output: 9.26100

# Example 3:
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25

# Constraints:
# -100.0 < x < 100.0
# -231 <= n <= 231-1
# n is an integer.
# Either x is not zero or n > 0.
# -104 <= xn <= 104




# sol 1 

# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if n == 0:
#             return 1
#         elif n < 0:
#             x = 1 / x
#             n = -n
        
#         half = self.myPow(x, n // 2)
        
#         if n % 2 == 0:
#             return half * half
#         else:
#             return half * half * x
        


# sol 2  

# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         def fastPow(x,n): # created a helper function which takes x and n as parameter
#             if n == 0: # if n is equal to 0
#                 return 1.0 # we return 1
#             half = fastPow(x, n // 2) # calculating half until n is equal to 0
#             if n % 2 == 0: # if n gives remainder 0 when divided by 2
#                 return half * half # return half * half
#             else: # if remainder not equal to 0
#                 return half * half * x # we return half * half * x
        
#         if n < 0: # if n is less than zero
#             x = 1 / x # x will be on the denominator
#             n = -n # n will become positive as (-) + (-) = (+)
        
#         return fastPow(x,n) # returning it