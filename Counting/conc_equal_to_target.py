# 2023. Number of Pairs of Strings With Concatenation Equal to Target
# Medium

# Given an array of digit strings nums and a digit string target, return the number of pairs of indices (i, j) (where i != j) such that the concatenation of nums[i] + nums[j] equals target.

# Example 1:
# Input: nums = ["777","7","77","77"], target = "7777"
# Output: 4
# Explanation: Valid pairs are:
# - (0, 1): "777" + "7"
# - (1, 0): "7" + "777"
# - (2, 3): "77" + "77"
# - (3, 2): "77" + "77"

# Example 2:
# Input: nums = ["123","4","12","34"], target = "1234"
# Output: 2
# Explanation: Valid pairs are:
# - (0, 1): "123" + "4"
# - (2, 3): "12" + "34"

# Example 3:
# Input: nums = ["1","1","1"], target = "11"
# Output: 6
# Explanation: Valid pairs are:
# - (0, 1): "1" + "1"
# - (1, 0): "1" + "1"
# - (0, 2): "1" + "1"
# - (2, 0): "1" + "1"
# - (1, 2): "1" + "1"
# - (2, 1): "1" + "1"
 
# Constraints:
# 2 <= nums.length <= 100
# 1 <= nums[i].length <= 100
# 2 <= target.length <= 100
# nums[i] and target consist of digits.
# nums[i] and target do not have leading zeros.



# sol 1 

# class Solution:
#     def numOfPairs(self, nums: List[str], target: str) -> int:
#         freq = Counter(nums)
#         ans = 0 
#         for k, v in freq.items(): 
#             if target.startswith(k): 
#                 suffix = target[len(k):]
#                 ans += v * freq[suffix]
#                 if k == suffix: ans -= freq[suffix]
#         return ans 
    


# sol 2

# class Solution:
#     def numOfPairs(self, nums: List[str], target: str) -> int:
#         ct = Counter(nums)
#         res = 0

#         for i in range(1, len(target)):
#             prefix = target[:i] # divide target in two
#             suffix = target[i:]

#             if prefix in ct and suffix in ct: 
#                 if prefix == suffix:
#                     res += ct[prefix] * (ct[prefix] - 1)
#                 else:
#                     res += ct[prefix] * ct[suffix]
        
#         return res