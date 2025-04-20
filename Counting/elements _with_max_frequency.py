# 3005. Count Elements With Maximum Frequency
# Easy

# You are given an array nums consisting of positive integers.
# Return the total frequencies of elements in nums such that those elements all have the maximum frequency.
# The frequency of an element is the number of occurrences of that element in the array.
 
# Example 1:
# Input: nums = [1,2,2,3,1,4]
# Output: 4
# Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
# So the number of elements in the array with maximum frequency is 4.

# Example 2:
# Input: nums = [1,2,3,4,5]
# Output: 5
# Explanation: All elements of the array have a frequency of 1 which is the maximum.
# So the number of elements in the array with maximum frequency is 5.
 
# Constraints:
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100



# sol 1 

# class Solution:
#     def maxFrequencyElements(self, nums: List[int]) -> int:
#         freq_counter = Counter(nums)
#         max_frequency = max(freq_counter.values())
#         max_freq_elements = [num for num, freq in freq_counter.items() if freq == max_frequency]
#         total_frequency = max_frequency * len(max_freq_elements)
#         return total_frequency
    


# sol 2

# class Solution:
#     def maxFrequencyElements(self, nums: List[int]) -> int:
#         d = {}
#         c = 0
#         for x in nums:
#             if str(x) in d:
#                 d[str(x)]+=1
#             else:
#                 d[str(x)]=1
#         for freq in d.values():
#             if freq == max(d.values()):
#                 c+=freq
#         return c


# sol 3

# class Solution:
#     def maxFrequencyElements(self, nums: List[int]) -> int:
#         dict={}
#         for i in nums:
#             if i not in dict.keys():
#                 dict[i]=1
#             else:
#                 dict[i]+=1
#         maxi=0
#         for key in dict.keys():
#             freq=dict[key]
#             maxi=max(freq,maxi)
#         count=0
#         for i in dict.keys():
#             if dict[i]==maxi:
#                 count+=dict[i]
#         return count

        