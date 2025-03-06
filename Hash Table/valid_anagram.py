# 242. Valid Anagram
# Easy

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?


# sol 1

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)
    

# sol 2

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         return collections.Counter(s) == collections.Counter(t)


# sol 3

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         counter = collections.defaultdict(int)
#         for i in range(len(s)):
#             counter[s[i]] += 1
#             counter[t[i]] -= 1
#         for count in counter.values():
#             if count:
#                 return False
#         return True


# sol 4

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         counter = [0] * 26
#         for i in range(len(s)):
#             counter[ord(s[i]) - ord('a')] += 1
#             counter[ord(t[i]) - ord('a')] -= 1
#         for count in counter:
#             if count:
#                 return False
#         return True
    


# sol 5

# # class Solution:
# #     def isAnagram(self, s: str, t: str) -> bool:  
# #         return Counter(s) == Counter(t)

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:  
#         if len(s) != len(t):
#             return False

#         counter = {}

#         for char in s:
#             counter[char] = counter.get(char, 0) + 1

#         for char in t:
#             if char not in counter or counter[char] == 0:
#                 return False
#             counter[char] -= 1

#         return True
    

# sol 6

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:  
#         if len(s) != len(t):
#             return False

#         count = [0] * 26

#         for char in s:
#             count[ord(char) - ord('a')] += 1

#         for char in t:
#             if count[ord(char) - ord('a')] == 0:
#                 return False
#             count[ord(char) - ord('a')] -= 1

#         return True
    

# sol 7

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:    
#         if len(s) != len(t):
#             return False
        
#         s_count = {}
#         t_count = {}
        
#         for i in range(len(s)):
#             s_count[s[i]] = 1 + s_count.get(s[i], 0)
#             t_count[t[i]] = 1 + t_count.get(t[i], 0)
        
#         return s_count == t_count
    

# sol 8

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:    
#         if len(s) != len(t):
#             return False
        
#         s_count = {}
        
#         for i in range(len(s)):
#             s_count[s[i]] = 1 + s_count.get(s[i], 0)
#             s_count[t[i]] = -1 + s_count.get(t[i], 0)
        
#         return all(value == 0 for value in s_count.values())


# sol 9

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         while s:
#             i = 0
#             while t:
#                 if s[0] == t[i]:
#                     s = s[1:]
#                     t = t[:i] + t[i+1:]
#                     break
#                 else:
#                     i+=1
#                 if i >= len(t):
#                     return False
#         return True


# sol 10

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len (t):
#             return False
#         for c in set(s):
#             if s.count(c) != t.count(c):
#                 return False
#         return True
    

# sol 10

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s)!=len(t):
#             return False
#         for i in set(s):
#             if s.count(i)!=t.count(i):
#                 return False
#         return True
            