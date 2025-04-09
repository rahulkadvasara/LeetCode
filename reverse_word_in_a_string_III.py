# 557. Reverse Words in a String III
# Easy

# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

# Example 1:
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

# Example 2:
# Input: s = "Mr Ding"
# Output: "rM gniD"

# Constraints:
# 1 <= s.length <= 5 * 104
# s contains printable ASCII characters.
# s does not contain any leading or trailing spaces.
# There is at least one word in s.
# All the words in s are separated by a single space.



# sol 1

# class Solution:
#     def reverseWords(self, s: str) -> str:
#         # Split the input string into words and reverse each word
#         words = s.split()
#         reversed_words = [word[::-1] for word in words]

#         # Join the reversed words to form the final result
#         return ' '.join(reversed_words)
    

# sol 2

# class Solution:
#     def reverseWords(self, s: str) -> str:
#         s = list(s)
#         start = 0

#         for i in range(len(s)):
#             if s[i] == ' ' or i == len(s) - 1:
#                 end = i
#                 if i == len(s) - 1 and s[i] != ' ':
#                     end += 1
#                 # Inline reverse logic
#                 while start < end:
#                     s[start], s[end - 1] = s[end - 1], s[start]
#                     start += 1
#                     end -= 1
#                 start = i + 1

#         return ''.join(s)