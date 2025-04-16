# 1768. Merge Strings Alternately
# Easy

# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.

# Example 1:
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r

# Example 2:
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s

# Example 3:
# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d
 
# Constraints:
# 1 <= word1.length, word2.length <= 100
# word1 and word2 consist of lowercase English letters.



# sol 1

# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         merged = []
#         i = 0
#         while i < len(word1) and i < len(word2):
#             merged.append(word1[i])
#             merged.append(word2[i])
#             i += 1
#         merged.append(word1[i:])
#         merged.append(word2[i:])
#         return ''.join(merged)
    


# sol 2

# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#             lw1=len(word1)-1
#             lw2=len(word2)-1
#             n=max(len(word1),len(word2))
#             ans=""
#             for i in range(n):
#                 if i >lw1:
#                    ans+=word2[i:]
#                    return ans
#                 elif i>lw2:
#                    ans+=word1[i:]
#                    return ans
#                 elif i<=lw1 and i<=lw2:
#                    ans+=word1[i]+word2[i]
#             return ans 
 
        