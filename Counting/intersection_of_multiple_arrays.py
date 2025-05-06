# 2248. Intersection of Multiple Arrays
# Easy

# Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of integers that are present in each array of nums sorted in ascending order.

# Example 1:
# Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
# Output: [3,4]
# Explanation: 
# The only integers present in each of nums[0] = [3,1,2,4,5], nums[1] = [1,2,3,4], and nums[2] = [3,4,5,6] are 3 and 4, so we return [3,4].

# Example 2:
# Input: nums = [[1,2,3],[4,5,6]]
# Output: []
# Explanation: 
# There does not exist any integer present both in nums[0] and nums[1], so we return an empty list [].

# Constraints:
# 1 <= nums.length <= 1000
# 1 <= sum(nums[i].length) <= 1000
# 1 <= nums[i][j] <= 1000
# All the values of nums[i] are unique.



# sol 1 

# class Solution:
#     def intersection(self, nums: List[List[int]]) -> List[int]:
#         # Create a set to store the intersection
#         intersection_set = set(nums[0])
        
#         # Iterate through the rest of the lists
#         for i in range(1, len(nums)):
#             # Update the intersection set with the current list
#             intersection_set.intersection_update(nums[i])
        
#         # Convert the set to a sorted list and return it
#         return sorted(intersection_set)
    


# sol 2

# class Solution:
#     def intersection(self, nums: List[List[int]]) -> List[int]:
#         # Create a dictionary to count occurrences of each number
#         count = {}
        
#         # Count occurrences of each number in all lists
#         for lst in nums:
#             for num in lst:
#                 if num in count:
#                     count[num] += 1
#                 else:
#                     count[num] = 1
        
#         # Find numbers that appear in all lists
#         result = [num for num, cnt in count.items() if cnt == len(nums)]
        
#         # Sort the result and return it
#         return sorted(result)
    


# sol 3

# class Solution:
#     def intersection(self, nums: List[List[int]]) -> List[int]:
#         res = set(nums[0])
#         for i in range(1, len(nums)):
#             res &= set(nums[i])
#         res = list(res)
#         res.sort()
#         return res