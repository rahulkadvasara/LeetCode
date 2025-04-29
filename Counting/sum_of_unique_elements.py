# 1748. Sum of Unique Elements
# Easy

# You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.
# Return the sum of all the unique elements of nums.

# Example 1:
# Input: nums = [1,2,3,2]
# Output: 4
# Explanation: The unique elements are [1,3], and the sum is 4.

# Example 2:
# Input: nums = [1,1,1,1,1]
# Output: 0
# Explanation: There are no unique elements, and the sum is 0.

# Example 3:
# Input: nums = [1,2,3,4,5]
# Output: 15
# Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.
 
# Constraints:
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100



# sol 1

# class Solution:
#     def sumOfUnique(self, nums: List[int]) -> int:
#         count = Counter(nums)
#         return sum(num for num, cnt in count.items() if cnt == 1)
    


# sol 2

# class Solution:
#     def sumOfUnique(self, nums: List[int]) -> int:
#         count = Counter(nums)
#         ans = 0
#         for key, val in count.items():
#             if val==1:
#                 ans+=key
#         return ans
    

# sol 3

# class Solution:
#     def sumOfUnique(self, nums: List[int]) -> int:
#         count = []
#         for i in nums:
#             if nums.count(i) == 1 :
#                 count.append(i)
#         return sum(count)

        

# sol 4

# class Solution:
#     def sumOfUnique(self, nums: List[int]) -> int:
#         hashmap = {}
#         for i in nums:
#             if i in hashmap.keys():
#                 hashmap[i] += 1
#             else:
#                 hashmap[i] = 1
#         sum = 0
#         for k, v in hashmap.items():
#             if v == 1: sum += k
#         return sum