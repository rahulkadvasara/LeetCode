# 1961. Check If String Is a Prefix of Array
# Easy

# Given a string s and an array of strings words, determine whether s is a prefix string of words.
# A string s is a prefix string of words if s can be made by concatenating the first k strings in words for some positive k no larger than words.length.
# Return true if s is a prefix string of words, or false otherwise.

# Example 1:
# Input: s = "iloveleetcode", words = ["i","love","leetcode","apples"]
# Output: true
# Explanation:
# s can be made by concatenating "i", "love", and "leetcode" together.

# Example 2:
# Input: s = "iloveleetcode", words = ["apples","i","love","leetcode"]
# Output: false
# Explanation:
# It is impossible to make s using a prefix of arr.

# Constraints:
# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# 1 <= s.length <= 1000
# words[i] and s consist of only lowercase English letters.



# sol 1

# class Solution:
#     def isPrefixString(self, s: str, words: List[str]) -> bool:
#         prefix = ""
#         for word in words:
#             prefix += word
#             if prefix == s:
#                 return True
#             if len(prefix) > len(s):
#                 return False
#         return False
    

# sol 2

# class Solution:
#     def isPrefixString(self, s: str, words: List[str]) -> bool:
#         result = ""

#         for word in words:
#             result += word
#             if result == s:
#                 return True

#         return False
    

# sol 3

# class Solution:
#     def isPrefixString(self, s, words):
#         return s in accumulate(words)