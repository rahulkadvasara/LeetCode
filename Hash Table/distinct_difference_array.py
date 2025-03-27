# 2670. Find the Distinct Difference Array
# Easy

# You are given a 0-indexed array nums of length n.
# The distinct difference array of nums is an array diff of length n such that diff[i] is equal to the number of distinct elements in the suffix nums[i + 1, ..., n - 1] subtracted from the number of distinct elements in the prefix nums[0, ..., i].
# Return the distinct difference array of nums.
# Note that nums[i, ..., j] denotes the subarray of nums starting at index i and ending at index j inclusive. Particularly, if i > j then nums[i, ..., j] denotes an empty subarray.

# Example 1:
# Input: nums = [1,2,3,4,5]
# Output: [-3,-1,1,3,5]
# Explanation: For index i = 0, there is 1 element in the prefix and 4 distinct elements in the suffix. Thus, diff[0] = 1 - 4 = -3.
# For index i = 1, there are 2 distinct elements in the prefix and 3 distinct elements in the suffix. Thus, diff[1] = 2 - 3 = -1.
# For index i = 2, there are 3 distinct elements in the prefix and 2 distinct elements in the suffix. Thus, diff[2] = 3 - 2 = 1.
# For index i = 3, there are 4 distinct elements in the prefix and 1 distinct element in the suffix. Thus, diff[3] = 4 - 1 = 3.
# For index i = 4, there are 5 distinct elements in the prefix and no elements in the suffix. Thus, diff[4] = 5 - 0 = 5.

# Example 2:
# Input: nums = [3,2,3,4,2]
# Output: [-2,-1,0,2,3]
# Explanation: For index i = 0, there is 1 element in the prefix and 3 distinct elements in the suffix. Thus, diff[0] = 1 - 3 = -2.
# For index i = 1, there are 2 distinct elements in the prefix and 3 distinct elements in the suffix. Thus, diff[1] = 2 - 3 = -1.
# For index i = 2, there are 2 distinct elements in the prefix and 2 distinct elements in the suffix. Thus, diff[2] = 2 - 2 = 0.
# For index i = 3, there are 3 distinct elements in the prefix and 1 distinct element in the suffix. Thus, diff[3] = 3 - 1 = 2.
# For index i = 4, there are 3 distinct elements in the prefix and no elements in the suffix. Thus, diff[4] = 3 - 0 = 3.

# Constraints:
# 1 <= n == nums.length <= 50
# 1 <= nums[i] <= 50



# sol 1 

# class Solution:
#     def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         prefix_count = [0] * 51
#         suffix_count = [0] * 51
#         result = [0] * n
        
#         for num in nums:
#             suffix_count[num] += 1
            
#         for i in range(n):
#             prefix_count[nums[i]] += 1
#             suffix_count[nums[i]] -= 1
            
#             prefix_distinct = sum(1 for count in prefix_count if count > 0)
#             suffix_distinct = sum(1 for count in suffix_count if count > 0)
            
#             result[i] = prefix_distinct - suffix_distinct
            
#         return result
    


# sol 2

# class Solution:
#     def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
#         # prefix nums[0,...,i]
#         # suffix nums[i+1,...,n-1]
#         pref: list[int] = []
#         suff: list[int] = [0] * len(nums)
#         res: list[int] = []

#         nums_set: set[int] = set()
#         for i in range(len(nums)):
#             nums_set.add(nums[i])
#             pref.append(len(nums_set))
        
#         nums_set = set()
#         for i in range(len(nums) - 1, -1, -1):
#             suff[i] = len(nums_set)
#             nums_set.add(nums[i])

#         for i in range(len(nums)):
#             res.append(pref[i] - suff[i])
#         return res