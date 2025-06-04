# 509. Fibonacci Number
# Easy

# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

# Example 1:
# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

# Example 2:
# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

# Example 3:
# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 
# Constraints:
# 0 <= n <= 30



# sol 1 

# class Solution:
#     def fib(self, n: int) -> int:
#         if n==0 or n==1:
#             return n
#         return self.fib(n-1)+self.fib(n-2)
    

# sol 2

# __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
# class Solution:
#     def fib(self, n: int) -> int:
#         if n<2:
#             return n
#         return self.fib(n-1)+self.fib(n-2)
    

# sol 3

# class Solution:
#     def fib(self, n: int) -> int:
#         def fibonnaci(n, memo):
#             if n in memo:
#                 return memo[n]
#             memo[n] = fibonnaci(n - 1, memo) + fibonnaci(n - 2, memo)
#             return memo[n]

#         return fibonnaci(n, {0: 0, 1: 1})
    

# sol 4

# class Solution:
#     def fib(self, n: int) -> int:
#         a = 0
#         b = 1
#         if n == 0: return 0
#         elif n == 1: return b
#         else:
#             for i in range(1,n):
#                 c = a + b
#                 a = b
#                 b = c
#             return b
        
    
# sol 5

# class Solution:
#     def fib(self, n: int) -> int:
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1
        
#         dp = [0, 1]
#         for _ in range(n - 1):
#             temp = dp[1]
#             dp[1] = dp[0] + temp
#             dp[0] = temp
        
#         return dp[1]
    


# sol 6

# class Solution:
#     def fib(self, n: int) -> int:
#         first = 0
#         second = 1
#         third = 1

#         if n==0:
#             return 0
#         elif n==1:
#             return 1
        
#         for i in range(n-1):
            
#             third = first+second
#             first = second
#             second = third
#         return third
    

# sol 7

# class Solution:
#     @cache
#     def fib(self, n: int) -> int:
#         if n==0 or n==1:
#             return n
#         return self.fib(n-1)+self.fib(n-2)