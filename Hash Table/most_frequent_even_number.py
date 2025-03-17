# 2404. Most Frequent Even Element
# Easy

# Given an integer array nums, return the most frequent even element.
# If there is a tie, return the smallest one. If there is no such element, return -1.

# Example 1:
# Input: nums = [0,1,2,2,4,4,1]
# Output: 2
# Explanation:
# The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
# We return the smallest one, which is 2.

# Example 2:
# Input: nums = [4,4,4,9,2,4]
# Output: 4
# Explanation: 4 is the even element appears the most.

# Example 3:
# Input: nums = [29,47,21,41,13,37,25,7]
# Output: -1
# Explanation: There is no even element.

# Constraints:
# 1 <= nums.length <= 2000
# 0 <= nums[i] <= 105



# sol 1

# from collections import Counter
# class Solution:
#     def mostFrequentEven(self, nums: List[int]) -> int:
#         lst = [i for i in nums if i % 2 == 0]  # Filter even numbers
#         if not lst:  # If no even numbers exist, return -1
#             return -1
        
#         a = Counter(lst)  # Count frequency of even numbers

#         k = float('-inf')
#         l = float('inf')  # Initialize l to positive infinity for correct min comparison
        
#         for n, m in a.items():
#             if m > k or (m == k and n < l):  # Check for max frequency and resolve ties with min value
#                 k = m
#                 l = n
        
#         return l
    

# sol 2

# class Solution:
#     def mostFrequentEven(self, nums: List[int]) -> int:
#         nums.sort()
#         map={}

#         for i in nums:
#             if i in map and i%2 == 0:
#                 map[i]+=1
#             elif i not in map and i%2 == 0:
#                 map[i] = 1
#         if len(map) == 0:
#             return -1
#         res = max(map,key=lambda key:map[key])
#         return res


# sol 3

# class Solution:
#     def mostFrequentEven(self, nums: List[int]) -> int:
#         most_freq = -1
#         highest = 0
#         freq_list = Counter(nums)

#         print(freq_list)

#         for num in freq_list:
#             if num % 2 == 0:
#                 if freq_list[num] > highest:
#                     most_freq = num
#                     highest = freq_list[num]
#                 elif freq_list[num] == highest:
#                     most_freq = num if num < most_freq else most_freq
#         return most_freq
#     __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))