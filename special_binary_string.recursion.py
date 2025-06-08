# 761. Special Binary String
# Hard

# Special binary strings are binary strings with the following two properties:
# The number of 0's is equal to the number of 1's.
# Every prefix of the binary string has at least as many 1's as 0's.
# You are given a special binary string s.
# A move consists of choosing two consecutive, non-empty, special substrings of s, and swapping them. Two strings are consecutive if the last character of the first string is exactly one index before the first character of the second string.
# Return the lexicographically largest resulting string possible after applying the mentioned operations on the string.

# Example 1:
# Input: s = "11011000"
# Output: "11100100"
# Explanation: The strings "10" [occuring at s[1]] and "1100" [at s[3]] are swapped.
# This is the lexicographically largest string possible after some number of swaps.

# Example 2:
# Input: s = "10"
# Output: "10"

# Constraints:
# 1 <= s.length <= 50
# s[i] is either '0' or '1'.
# s is a special binary string.




# sol 1 

# class Solution:
#     def makeLargestSpecial(self, s: str) -> str:
#         count = i = 0
#         res = []
        
#         for j, char in enumerate(s):
#             count += 1 if char == '1' else -1
            
#             if count == 0:  # Found a special substring
#                 # Recursively process the inner substring and prepend '1' and append '0'
#                 res.append('1' + self.makeLargestSpecial(s[i + 1:j]) + '0')
#                 i = j + 1
        
#         # Sort the special substrings in reverse order to get the largest lexicographical order
#         res.sort(reverse=True)
        
#         return ''.join(res)  # Join all parts to form the final result