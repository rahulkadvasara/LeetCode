# 2451. Odd String Difference
# Easy

# You are given an array of equal-length strings words. Assume that the length of each string is n.
# Each string words[i] can be converted into a difference integer array difference[i] of length n - 1 where difference[i][j] = words[i][j+1] - words[i][j] where 0 <= j <= n - 2. Note that the difference between two letters is the difference between their positions in the alphabet i.e. the position of 'a' is 0, 'b' is 1, and 'z' is 25.
# For example, for the string "acb", the difference integer array is [2 - 0, 1 - 2] = [2, -1].
# All the strings in words have the same difference integer array, except one. You should find that string.
# Return the string in words that has different difference integer array.

# Example 1:
# Input: words = ["adc","wzy","abc"]
# Output: "abc"
# Explanation: 
# - The difference integer array of "adc" is [3 - 0, 2 - 3] = [3, -1].
# - The difference integer array of "wzy" is [25 - 22, 24 - 25]= [3, -1].
# - The difference integer array of "abc" is [1 - 0, 2 - 1] = [1, 1]. 
# The odd array out is [1, 1], so we return the corresponding string, "abc".

# Example 2:
# Input: words = ["aaa","bob","ccc","ddd"]
# Output: "bob"
# Explanation: All the integer arrays are [0, 0] except for "bob", which corresponds to [13, -13].

# Constraints:
# 3 <= words.length <= 100
# n == words[i].length
# 2 <= n <= 20
# words[i] consists of lowercase English letters.



# sol 1

# class Solution:
#     def oddString(self, words: List[str]) -> str:
#         d={}
#         for i in words:
#             temp=[]
#             for j in range(1,len(i)):
#                 temp.append(ord(i[j])-ord(i[j-1]))
#             temp=str(temp)
#             if temp in d:
#                 d[temp][1]=True
#             else:
#                 d[temp]=[i,False]
#         for i,j in d.items():
#             if j[1]==False:
#                 return j[0]



# sol 2

# class Solution:
#     def oddString(self, words: List[str]) -> str:
#         def diff_int(word):
#             result = []
#             for i in range(len(word) - 1):
#                 result.append(ord(word[i+1]) - ord(word[i]))
#             return result

#         w0 = diff_int(words[0])
#         w1 = diff_int(words[1])
#         w2 = diff_int(words[2])
#         if w0 != w1 == w2:
#             return words[0]
#         if w0 == w2 != w1:
#             return words[1]
#         if w0 == w1 != w2:
#             return words[2]
#         for word in words:
#             if diff_int(word) != w0:
#                 return word