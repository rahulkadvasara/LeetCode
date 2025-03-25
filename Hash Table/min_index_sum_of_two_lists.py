# 599. Minimum Index Sum of Two Lists
# Easy

# Given two arrays of strings list1 and list2, find the common strings with the least index sum.
# A common string is a string that appeared in both list1 and list2.
# A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.
# Return all the common strings with the least index sum. Return the answer in any order.

# Example 1:
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# Output: ["Shogun"]
# Explanation: The only common string is "Shogun".

# Example 2:
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
# Output: ["Shogun"]
# Explanation: The common string with the least index sum is "Shogun" with index sum = (0 + 1) = 1.

# Example 3:
# Input: list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]
# Output: ["sad","happy"]
# Explanation: There are three common strings:
# "happy" with index sum = (0 + 1) = 1.
# "sad" with index sum = (1 + 0) = 1.
# "good" with index sum = (2 + 2) = 4.
# The strings with the least index sum are "sad" and "happy".
 
# Constraints:
# 1 <= list1.length, list2.length <= 1000
# 1 <= list1[i].length, list2[i].length <= 30
# list1[i] and list2[i] consist of spaces ' ' and English letters.
# All the strings of list1 are unique.
# All the strings of list2 are unique.
# There is at least a common string between list1 and list2.



# sol 1

# class Solution:
#     def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
#         d = {}
#         for i, r in enumerate(list1):
#             d[r] = i
#         ans = []
#         min_sum = float('inf')
#         for i, r in enumerate(list2):
#             if r in d:
#                 if i + d[r] < min_sum:
#                     min_sum = i + d[r]
#                     ans = [r]
#                 elif i + d[r] == min_sum:
#                     ans.append(r)
#         return ans



# sol 2

# class Solution:
#     def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
#         map1 = {}

#         for i in range(len(list1)):
#             word = list1[i]
#             if not word in map1:
#                 map1[word] = i

#         index_sum = None
#         common_words = []
#         for i in range(len(list2)):
#             word = list2[i]
#             if word in map1:
#                 j = map1[word]
#                 if (index_sum is None) or ((i + j) < index_sum):
#                     index_sum = i + j
#                     common_words = [word]
#                 elif (i + j) == index_sum:
#                     common_words.append(word)

#         return common_words