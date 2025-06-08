# 60. Permutation Sequence
# Hard

# The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.

# Example 1:
# Input: n = 3, k = 3
# Output: "213"

# Example 2:
# Input: n = 4, k = 9
# Output: "2314"

# Example 3:
# Input: n = 3, k = 1
# Output: "123"

# Constraints:
# 1 <= n <= 9
# 1 <= k <= n!





# sol 1 

# class Solution:    
#     def getPermutation(self, n: int, k: int) -> str:
#         # Create a list of numbers to get permutations from
#         nums = [str(i) for i in range(1, n + 1)]
#         # Initialize the result
#         result = []
#         # Adjust k to be zero-indexed
#         k -= 1
        
#         # Calculate factorials for the numbers
#         factorials = [1] * n
#         for i in range(1, n):
#             factorials[i] = factorials[i - 1] * i
        
#         # Generate the permutation
#         for i in range(n):
#             index = k // factorials[n - 1 - i]
#             result.append(nums[index])
#             nums.pop(index)
#             k %= factorials[n - 1 - i]
        
#         return ''.join(result)