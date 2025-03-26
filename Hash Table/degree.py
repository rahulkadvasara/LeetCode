# 697. Degree of an Array
# Easy

# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

# Example 1:
# Input: nums = [1,2,2,3,1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.

# Example 2:
# Input: nums = [1,2,2,3,1,4,2]
# Output: 6
# Explanation: 
# The degree is 3 because the element 2 is repeated 3 times.
# So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.

# Constraints:
# nums.length will be between 1 and 50,000.
# nums[i] will be an integer between 0 and 49,999.



# sol 1

# class Solution:
#     def findShortestSubArray(self, nums: List[int]) -> int:
#         left, right, count = {}, {}, {}
#         for i, x in enumerate(nums):
#             if x not in left: left[x] = i
#             right[x] = i
#             count[x] = count.get(x, 0) + 1
#         degree = max(count.values())
#         return min(right[x] - left[x] + 1 for x in count if count[x] == degree)
    

# sol 2

# class Solution:
#     def findShortestSubArray(self, nums: List[int]) -> int:
        
#         max_degree = 1
#         repeat_dict = defaultdict(list)

#         for idx,num in enumerate(nums) :
#             repeat_dict[num].append(idx)
        
#         #find max degree of nums
#         for val in repeat_dict.values():
#             max_degree = max(max_degree,len(val))

#         if max_degree == 1 :
#             return 1 
        
#         result = len(nums)
#         for val in repeat_dict.values():
#             if len(val) >= 2 and len(val) == max_degree :
#                 tmp_result = val[-1]-val[0] +1
#                 result = min(result,tmp_result)
        
#         return result