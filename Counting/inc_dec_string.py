# 1370. Increasing Decreasing String
# Easy

# You are given a string s. Reorder the string using the following algorithm:
# Remove the smallest character from s and append it to the result.
# Remove the smallest character from s that is greater than the last appended character, and append it to the result.
# Repeat step 2 until no more characters can be removed.
# Remove the largest character from s and append it to the result.
# Remove the largest character from s that is smaller than the last appended character, and append it to the result.
# Repeat step 5 until no more characters can be removed.
# Repeat steps 1 through 6 until all characters from s have been removed.
# If the smallest or largest character appears more than once, you may choose any occurrence to append to the result.
# Return the resulting string after reordering s using this algorithm.

# Example 1:
# Input: s = "aaaabbbbcccc"
# Output: "abccbaabccba"
# Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
# After steps 4, 5 and 6 of the first iteration, result = "abccba"
# First iteration is done. Now s = "aabbcc" and we go back to step 1
# After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
# After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"

# Example 2:
# Input: s = "rat"
# Output: "art"
# Explanation: The word "rat" becomes "art" after re-ordering it with the mentioned algorithm.
 
# Constraints:
# 1 <= s.length <= 500
# s consists of only lowercase English letters.



# sol 1 

# class Solution:
#     def sortString(self, s: str) -> str:
#         from collections import Counter

#         counter = Counter(s)
#         result = []
#         while counter:
#             for c in sorted(counter):
#                 result.append(c)
#                 counter[c] -= 1
#                 if counter[c] == 0:
#                     del counter[c]
#             for c in sorted(counter, reverse=True):
#                 result.append(c)
#                 counter[c] -= 1
#                 if counter[c] == 0:
#                     del counter[c]
#         return ''.join(result)
    


# sol 2

# class Solution:
#     def sortString(self, s: str) -> str:
#         # Count the frequency of each character in the string
#         char_count = collections.Counter(s)
#         result = []
        
#         while char_count:
#             # Append characters in increasing order
#             for char in sorted(char_count.keys()):
#                 result.append(char)
#                 char_count[char] -= 1
#                 if char_count[char] == 0:
#                     del char_count[char]
            
#             # Append characters in decreasing order
#             for char in sorted(char_count.keys(), reverse=True):
#                 result.append(char)
#                 char_count[char] -= 1
#                 if char_count[char] == 0:
#                     del char_count[char]
        
#         return ''.join(result)
    


# sol 3

# from collections import Counter

# class Solution:
#     def sortString(self, s: str) -> str:
#         '''cn = [0]*26

#         for c in s:
#             cn[ord(c)-97] += 1 # idx: 0 -> a, 1 -> b, ... and cn[i] is how many times certain element occurrs. Counter(s)
#         stack, res = [], []
#         for i in range(25, -1, -1):
#             if cn[i] != 0:
#                 stack.append((chr(i+97), cn[i])) # its basically Counter(s)'''
        
#         cn = Counter(s)
#         stack, res = [], []

#         # Convert Counter to stack
#         for char in sorted(cn.keys(), reverse=True):
#             if cn[char] > 0:
#                 stack.append((char, cn[char]))

#         while stack:
#             tmp = []
#             while stack:
#                 ch, n = stack.pop()
#                 res.append(ch)
                
#                 if n > 1:
#                     tmp.append((ch, n-1))
#             stack = tmp

#         return ''.join(res)
    


# sol 4

# class Solution:
#     def sortString(self, s: str) -> str:
#         count = [0] * 26 
#         for ch in s:
#             count[ord(ch) - ord('a')] += 1

#         result = []
#         while len(result) < len(s):
#             for i in range(26):
#                 if count[i] > 0:
#                     result.append(chr(i + ord('a')))
#                     count[i] -= 1
#             for i in range(25, -1, -1):
#                 if count[i] > 0:
#                     result.append(chr(i + ord('a')))
#                     count[i] -= 1

#         return ''.join(result)