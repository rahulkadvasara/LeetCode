# 2586. Count the Number of Vowel Strings in Range
# Easy

# You are given a 0-indexed array of string words and two integers left and right.
# A string is called a vowel string if it starts with a vowel character and ends with a vowel character where vowel characters are 'a', 'e', 'i', 'o', and 'u'.
# Return the number of vowel strings words[i] where i belongs to the inclusive range [left, right].

# Example 1:
# Input: words = ["are","amy","u"], left = 0, right = 2
# Output: 2
# Explanation: 
# - "are" is a vowel string because it starts with 'a' and ends with 'e'.
# - "amy" is not a vowel string because it does not end with a vowel.
# - "u" is a vowel string because it starts with 'u' and ends with 'u'.
# The number of vowel strings in the mentioned range is 2.

# Example 2:
# Input: words = ["hey","aeo","mu","ooo","artro"], left = 1, right = 4
# Output: 3
# Explanation: 
# - "aeo" is a vowel string because it starts with 'a' and ends with 'o'.
# - "mu" is not a vowel string because it does not start with a vowel.
# - "ooo" is a vowel string because it starts with 'o' and ends with 'o'.
# - "artro" is a vowel string because it starts with 'a' and ends with 'o'.
# The number of vowel strings in the mentioned range is 3.
 
# Constraints:
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 10
# words[i] consists of only lowercase English letters.
# 0 <= left <= right < words.length



# sol 1

# class Solution:
#     def vowelStrings(self, words: List[str], left: int, right: int) -> int:
#         c=0
#         for i in range(0,len(words)):
#             if left<=i and i<=right and words[i][0] in "aeiou" and words[i][-1] in "aeiou":
#                 c+=1
#         return c
        


# sol 2

# class Solution:
#     def vowelStrings(self, words: List[str], left: int, right: int) -> int:
#         op=0
#         v=['a','e','i','o','u']
#         for i in range(left,right+1):
#             if((words[i][0] in v) and (words[i][-1] in v)):
#                 op+=1
#         return op