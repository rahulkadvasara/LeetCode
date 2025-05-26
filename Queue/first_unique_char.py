# 387. First Unique Character in a String
# Easy

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# Example 1:
# Input: s = "leetcode"
# Output: 0
# Explanation:
# The character 'l' at index 0 is the first character that does not occur at any other index.

# Example 2:
# Input: s = "loveleetcode"
# Output: 2

# Example 3:
# Input: s = "aabb"
# Output: -1

# Constraints:
# 1 <= s.length <= 105
# s consists of only lowercase English letters.



# sol 1

# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         char_count = {}
        
#         # Count occurrences of each character
#         for char in s:
#             if char in char_count:
#                 char_count[char] += 1
#             else:
#                 char_count[char] = 1
        
#         # Find the first unique character
#         for index, char in enumerate(s):
#             if char_count[char] == 1:
#                 return index
        
#         return -1
    


# sol 2 

# class Solution:
#     def firstUniqueChar(self, s: str) -> int:
#         queue = []
#         char_count = {}
#         for char in s:
#             if char in char_count:
#                 char_count[char] += 1
#             else:
#                 char_count[char] = 1
#                 queue.append(char)
#         for index, char in enumerate(queue):
#             if char_count[char] == 1:
#                 return s.index(char)
#         return -1
    

# sol 3

# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         char_count = {}
        
#         # Count the frequency of each character
#         for char in s:
#             char_count[char] = char_count.get(char, 0) + 1
        
#         # Find the index of the first unique character
#         for index, char in enumerate(s):
#             if char_count[char] == 1:
#                 return index
        
#         return -1  # Return -1 if no unique character is found
    


# class Solution(object):
#     def firstUniqChar(self, s):
#          # Create a list to store the frequency of each character
#         frequency = [0] * 26  # Assuming only lowercase letters

#         # Step 1: Count the frequency of each character
#         for char in s:
#             frequency[ord(char) - ord('a')] += 1  # Map 'a' to 0, 'b' to 1, ..., 'z' to 25

#         # Step 2: Find the first character with a frequency of 1
#         for index, char in enumerate(s):
#             if frequency[ord(char) - ord('a')] == 1:
#                 return index  # Return the index of the first unique character

#         # Step 3: If no unique character is found, return -1
#         return -1
    


# sol 4

# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         mp = {}

#         for a in s:
#             mp[a] = mp.get(a, 0) + 1

#         for i in range(len(s)):
#             if mp[s[i]] == 1:
#                 return i

#         return -1



# sol 5

# from collections import Counter
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         n=Counter(s)
#         for k,v in n.items():
#             if v==1:
#                 return s.index(k)
#         return -1
    

# sol 6

# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         from collections import Counter
#         freq = Counter(s)
#         idxmin = len(s)

#         found = False 
#         for l in freq:
#             idx = s.index(l)
#             if freq[l] == 1 and idx < idxmin:
#                 idxmin = idx
#                 found = True 
#         return idxmin if found else -1 
        
                

# sol 7

# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         res = {}
        
#         for i,v in enumerate(s):
#             if v not in res:
#                 res[v] = i
#             else:
#                 res[v] = -1
        
#         for i in res.values():
#             if i > -1:
#                 return i
#         return -1