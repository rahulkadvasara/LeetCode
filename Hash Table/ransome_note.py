# 383. Ransom Note
# Easy

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
 
# Constraints:
# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.


# sol 1

# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         for i in set(ransomNote):
#             if ransomNote.count(i) > magazine.count(i):
#                 return False
#         return True


# sol 2

# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         return not collections.Counter(ransomNote) - collections.Counter(magazine)


# sol 3

# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         maga_hash = {}

#         for c in magazine:
#             maga_hash[c] = 1 + maga_hash.get(c, 0)

#         for c in ransomNote:
#             if c not in maga_hash or maga_hash[c] <= 0:
#                 return False
#             maga_hash[c] -= 1
        
#         return True
    

# sol 4

# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         if len(ransomNote) > len(magazine):
#             return False
            
#         for c in set(ransomNote):
#             if magazine.count(c) < ransomNote.count(c):
#                 return False

#         return True
    

# sol 5

# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         if len(ransomNote) > len(magazine):
#             return False
#         for c in set(ransomNote):
#             mc = magazine.count(c)
#             rc = ransomNote.count(c)
#             if mc < rc:
#                 return False
#         return True