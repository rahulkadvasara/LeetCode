# 633. Sum of Square Numbers
# Medium

# Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

# Example 1:
# Input: c = 5
# Output: true
# Explanation: 1 * 1 + 2 * 2 = 5

# Example 2:
# Input: c = 3
# Output: false

# Constraints:
# 0 <= c <= 231 - 1




# sol 1 

# class Solution:
#     def judgeSquareSum(self, c: int) -> bool:
#         a=1
#         while a<=c**0.5:
#             b=0
#             while b<=c**0.5:
#                 if a*a+b*b==c:
#                     return True
#                 b+=1
#             a+=1
#         return False
    


# sol 2

# class Solution:
#     def judgeSquareSum(self, c: int) -> bool:
#         a=1
#         while a<=c**0.5:
#             b = c - a * a
#             i=1
#             sum=0
#             while sum<b:
#                 sum += i
#                 i += 2
#             if sum == b:
#                 return True
#             a+=1
#         return False
    


# sol 3

# class Solution:
#     def judgeSquareSum(self, c: int) -> bool:
#         a=1
#         while a<=c**0.5:
#             b = (c - a * a)**0.5
#             if b == int(b):
#                 return True
#             a+=1
#         return False
    


# sol 4

# class Solution:
#     def judgeSquareSum(self, c: int) -> bool:
#         def binarySearch(n,l,r):
#             if l>r:
#                 return False
#             mid = l+(r-l)//2
#             if mid*mid==n:
#                 return True
#             elif(mid*mid>n):
#                 return binarySearch(n,l,mid-1)
#             else:
#                 return binarySearch(n,mid+1,r)
        
#         for a in range(int(c**0.5)+1):
#             b=c-a*a
#             if binarySearch(b,0,b):
#                 return True
#         return False



# sol 5

# class Solution:
#     def judgeSquareSum(self, c: int) -> bool:
#         i = 2
#         while i * i <= c:
#             count = 0
#             while c % i == 0:
#                 count += 1
#                 c //= i
#             if i % 4 == 3 and count % 2 != 0:
#                 return False
#             i += 1
#         return c % 4 != 3