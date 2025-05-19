# 1003. Check If Word Is Valid After Substitutions
# Medium

# Given a string s, determine if it is valid.
# A string s is valid if, starting with an empty string t = "", you can transform t into s after performing the following operation any number of times:
# Insert string "abc" into any position in t. More formally, t becomes tleft + "abc" + tright, where t == tleft + tright. Note that tleft and tright may be empty.
# Return true if s is a valid string, otherwise, return false.

# Example 1:
# Input: s = "aabcbc"
# Output: true
# Explanation:
# "" -> "abc" -> "aabcbc"
# Thus, "aabcbc" is valid.

# Example 2:
# Input: s = "abcabcababcc"
# Output: true
# Explanation:
# "" -> "abc" -> "abcabc" -> "abcabcabc" -> "abcabcababcc"
# Thus, "abcabcababcc" is valid.

# Example 3:
# Input: s = "abccba"
# Output: false
# Explanation: It is impossible to get "abccba" using the operation.
 
# Constraints:
# 1 <= s.length <= 2 * 104
# s consists of letters 'a', 'b', and 'c'



# sol 1

# class Solution:
#     def isValid(self, s: str) -> bool:
#         s2 = ""
#         while s != s2:
#             s, s2 = s.replace("abc", ""), s
#         return s == ""



# sol 2

# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         for c in s:
#             stack.append(c)
#             if len(stack) >= 3 and stack[-3:] == ['a', 'b', 'c']:
#                 stack.pop()
#                 stack.pop()
#                 stack.pop()
#         return not stack
    


# sol 3

# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         for i in S:
#             if i == 'c':
#                 if stack[-2:] != ['a', 'b']:
#                     return False
#                 stack.pop()
#                 stack.pop()
#             else:
#                 stack.append(i)
#         return not stack
    

# sol 4

# class Solution:
#     def isValid(self, s: str) -> bool:
#         count = [0, 0, 0]
#         for i in s:
#             count[ord(i) - ord('a')] += 1
#             if not count[0] >= count[1] >= count[2]:
#                 return False
#         return count[0] == count[1] == count[2]


# sol 5

# class Solution:
#     def isValid(self, s: str) -> bool:
#         while s:
#             if "abc" not in s:
#                 return False
#             s = s.replace("abc", "")
#         return True