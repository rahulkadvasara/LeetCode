# 821. Shortest Distance to a Character
# Easy

# Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.
# The distance between two indices i and j is abs(i - j), where abs is the absolute value function.

# Example 1:
# Input: s = "loveleetcode", c = "e"
# Output: [3,2,1,0,1,0,0,1,2,2,1,0]
# Explanation: The character 'e' appears at indices 3, 5, 6, and 11 (0-indexed).
# The closest occurrence of 'e' for index 0 is at index 3, so the distance is abs(0 - 3) = 3.
# The closest occurrence of 'e' for index 1 is at index 3, so the distance is abs(1 - 3) = 2.
# For index 4, there is a tie between the 'e' at index 3 and the 'e' at index 5, but the distance is still the same: abs(4 - 3) == abs(4 - 5) = 1.
# The closest occurrence of 'e' for index 8 is at index 6, so the distance is abs(8 - 6) = 2.

# Example 2:
# Input: s = "aaab", c = "b"
# Output: [3,2,1,0]

# Constraints:
# 1 <= s.length <= 104
# s[i] and c are lowercase English letters.
# It is guaranteed that c occurs at least once in s.



# sol 1

# class Solution:
#     def shortestToChar(self, s: str, c: str) -> List[int]:
#         n = len(s)
#         ans = [0] * n
#         prev = float('-inf')
        
#         # First pass: from left to right
#         for i in range(n):
#             if s[i] == c:
#                 prev = i
#             ans[i] = i - prev
        
#         # Second pass: from right to left
#         prev = float('inf')
#         for i in range(n - 1, -1, -1):
#             if s[i] == c:
#                 prev = i
#             ans[i] = min(ans[i], prev - i)
        
#         return ans
    

# sol 2

# class Solution:
#     def shortestToChar(self, s: str, c: str) -> List[int]:
#         indices,l=[],[]
#         for ind,itr in enumerate(s):
#             if itr==c:
#                 indices.append(ind)
#         k=0
#         for i in range(len(s)):
#             if i<=indices[0]:
#                 l.append(abs(i-indices[0]))
#             elif i>indices[0] and i<indices[-1]:
#                 min_val=min(abs(i-indices[k]),abs(i-(indices[k+1])))
#                 l.append(min_val)
#                 if min_val==0:
#                     k+=1
#             elif i>=indices[-1]:
#                 l.append(abs(i-indices[-1]))
#         return l
        

        