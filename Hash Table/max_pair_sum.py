# 2815. Max Pair Sum in an Array
# Easy

# You are given an integer array nums. You have to find the maximum sum of a pair of numbers from nums such that the largest digit in both numbers is equal.
# For example, 2373 is made up of three distinct digits: 2, 3, and 7, where 7 is the largest among them.
# Return the maximum sum or -1 if no such pair exists.

# Example 1:
# Input: nums = [112,131,411]
# Output: -1
# Explanation:
# Each numbers largest digit in order is [2,3,4].

# Example 2:
# Input: nums = [2536,1613,3366,162]
# Output: 5902
# Explanation:
# All the numbers have 6 as their largest digit, so the answer is 2536 + 3366 = 5902.

# Example 3:
# Input: nums = [51,71,17,24,42]
# Output: 88
# Explanation:
# Each number's largest digit in order is [5,7,7,4,4].
# So we have only two possible pairs, 71 + 17 = 88 and 24 + 42 = 66.

# Constraints:
# 2 <= nums.length <= 100
# 1 <= nums[i] <= 104



# sol 2 

# class Solution:
#     def maxSum(self, nums: List[int]) -> int:
#         max_by_digit = defaultdict(int)
#         max_sum = -1

#         for num in nums:
#             digit = max(str(num))

#             if digit in max_by_digit:
#                 max_sum = max(max_sum, max_by_digit[digit] + num)

#             max_by_digit[digit] = max(max_by_digit[digit], num)

#         return max_sum
    

# sol 2

# class Solution:
#     def maxSum(self, nums: List[int]) -> int:
        
#         d, ans = defaultdict(list), -1
        
#         for num in nums: d[max(str(num))].append(num)   # <-- 1)
            
#         for ch in d:
#             if len(d[ch]) < 2: continue

#             ans = max(ans, sum(sorted(d[ch])[-2:]))     # <-- 2)

#         return  ans                                     # <-- 3)
    

# sol 3

# class Solution:
#     def maxSum(self, nums: List[int]) -> int:
#         digit_mp = {}
#         for num in nums:
#             num_str = str(num)
#             digit = max(num_str)
#             if digit in digit_mp:
#                 digit_mp[digit].append(num)
#             else:
#                 digit_mp[digit] = [num]
        
#         mx = -1
#         for d in digit_mp:
#             if len(digit_mp[d]) > 1:
#                 digit_mp[d].sort()
#                 mx = max(digit_mp[d][-1] + digit_mp[d][-2], mx)
#         return mx