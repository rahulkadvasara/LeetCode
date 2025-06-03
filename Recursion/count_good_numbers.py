# 1922. Count Good Numbers
# Medium

# A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).
# For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime. However, "3245" is not good because 3 is at an even index but is not even.
# Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 109 + 7.
# A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.

# Example 1:
# Input: n = 1
# Output: 5
# Explanation: The good numbers of length 1 are "0", "2", "4", "6", "8".

# Example 2:
# Input: n = 4
# Output: 400

# Example 3:
# Input: n = 50
# Output: 564908303
 
# Constraints:
# 1 <= n <= 1015


# sol 1 

# class Solution:
#     MOD = 10**9 + 7

#     def countGoodNumbers(self, n: int) -> int:
#         even_positions = (n + 1) // 2
#         odd_positions = n // 2

#         even_ways = self.helper(5, even_positions)
#         odd_ways = self.helper(4, odd_positions)

#         return (even_ways * odd_ways) % self.MOD

#     def helper(self, base, power):
#         result = 1
#         base %= self.MOD

#         while power > 0:
#             if power % 2 == 1:
#                 result = (result * base) % self.MOD
#             base = (base * base) % self.MOD
#             power //= 2

#         return result
    


# sol 2 

# class Solution:
#     def countGoodNumbers(self, n: int) -> int:
#         mod = 10**9 + 7
#         even = (n + 1) // 2
#         odd = n // 2
#         return (pow(5, even, mod) * pow(4, odd, mod)) % mod
    

# sol 3

# class Solution:
#     MOD = 10**9 + 7

#     def countGoodNumbers(self, n: int) -> int:
#         def mod_pow(base, exp, mod):
#             result = 1
#             base %= mod
#             while exp > 0:
#                 if exp % 2 == 1:
#                     result = (result * base) % mod
#                 base = (base * base) % mod
#                 exp //= 2
#             return result

#         evens = (n + 1) // 2
#         odds = n // 2

#         return (mod_pow(5, evens, self.MOD) * mod_pow(4, odds, self.MOD)) % self.MOD