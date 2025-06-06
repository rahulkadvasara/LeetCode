# 390. Elimination Game
# Medium

# You have a list arr of all integers in the range [1, n] sorted in a strictly increasing order. Apply the following algorithm on arr:
# Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.
# Repeat the previous step again, but this time from right to left, remove the rightmost number and every other number from the remaining numbers.
# Keep repeating the steps again, alternating left to right and right to left, until a single number remains.
# Given the integer n, return the last number that remains in arr.

# Example 1:
# Input: n = 9
# Output: 6
# Explanation:
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# arr = [2, 4, 6, 8]
# arr = [2, 6]
# arr = [6]

# Example 2:
# Input: n = 1
# Output: 1

# Constraints:
# 1 <= n <= 109




# sol 1 

# class Solution:
#     def lastRemaining(self, n: int) -> int:
#         left = True  # flag to keep track of left-to-right or right-to-left elimination
#         remaining = n  # keep track of the remaining numbers
#         step = 1  # keep track of the step size
#         head = 1  # keep track of the head of the remaining numbers
#         while remaining > 1:
#             # if we're going from left to right or from right to left with an odd number of remaining elements
#             # or from right to left with an even number of remaining elements, then we need to update the head
#             if left or remaining % 2 == 1:
#                 head += step
#             step *= 2  # double the step size
#             remaining //= 2  # divide the remaining elements by 2
#             left = not left  # flip the flag

#         return head


# sol 2

# class Solution:
#     def lastRemaining(self, n: int) -> int:
#         def helper(x,step,cnt,d):
#             if cnt<2:
#                 return x
#             increment = step if d or cnt % 2 else 0
#             return helper(x+increment,step*2,cnt//2,not d)
#         return helper(1,1,n,True)
    

# sol 3

# class Solution:
#     def lastRemaining(self, n: int) -> int:
#         mask = 1
#         while mask <= n:  # left shift mask until mask > n
#             mask <<= 1
#         mask = (mask >> 1) - 1  # we don't want the left most bit
#         return 1 + ((n | 0x55555555) & mask)  # fill all odd bits and apply the mask
    


# sol 4 

# class Solution:
#     def lastRemaining(self, n: int) -> int:
#         N = n   # number of remaining numbers
#         fwd = True   # flag for forward/backward elimination
#         m = 2    # elimination step/interval
#         s = 0   # elimination base

#         while N > 1:
#             if fwd or N % 2 == 1: 
#                 s += m // 2
#             m *= 2
#             N = N // 2
#             fwd = not fwd   # reverse the pass direction
#         return s+1
    


# sol 5

# class Solution:
#     def lastRemaining(self, n: int) -> int:
#         # f: 1 to n; g: n to 1
#         # f(n, left) = 2 * f(n//2, right)
#         # f(n, right) = g(n ,left) = n + 1 - f(n, left)
#         # from the above 2, we have: f(n, left) = 2 * (n//2 + 2 - f(n//2, left))

#         if n == 1:
#             return 1
#         else:
#             return 2 * (1 + n // 2 - self.lastRemaining(n // 2))
        

    
# sol 6

# class Solution:
#     def lastRemaining(self, n: int) -> int:
#         if n == 1:
#             return 1
#         return 2 * (1 + n // 2 - self.lastRemaining(n // 2))