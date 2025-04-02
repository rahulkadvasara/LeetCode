# 442. Find All Duplicates in an Array
# Medium

# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears at most twice, return an array of all the integers that appears twice.
# You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output

# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]

# Example 2:
# Input: nums = [1,1,2]
# Output: [1]

# Example 3:
# Input: nums = [1]
# Output: []
 
# Constraints:
# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n
# Each element in nums appears once or twice.



# sol 1

# class Solution:
#     def findDuplicates(self, nums: List[int]) -> List[int]:
#         result = []
#         for i in range(len(nums)):
#             index = abs(nums[i]) - 1
#             if nums[index] < 0:
#                 result.append(index + 1)
#             else:
#                 nums[index] = -nums[index]
#         return result
    

# sol 2

# class Solution:
#     def findDuplicates(self, nums: List[int]) -> List[int]:
#         zero = [0]*len(nums)
#         res = []
#         for num in nums:
#             idx = num-1
#             if zero[idx] == 1:
#                 res.append(num)
#             else:
#                 zero[idx] = 1
#         return res
    

# sol 3

# class Solution:
#     def findDuplicates(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         freq = [0] * (n + 1)
#         res = []
#         for num in nums:
#             freq[num] += 1
#             if(freq[num] == 2):
#                 res.append(num)
#         return res
    

# sol 4

# class Solution:
#     def findDuplicates(self, nums: List[int]) -> List[int]:
#         seen = set()
#         duplicates = []

#         for num in nums:
#             if num in seen: 
#                 duplicates.append(num)
#             else:
#                 seen.add(num)
        
#         return duplicates