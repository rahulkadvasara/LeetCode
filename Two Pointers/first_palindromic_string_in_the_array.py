# 2108. Find First Palindromic String in the Array
# Easy

# Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".
# A string is palindromic if it reads the same forward and backward.

# Example 1:
# Input: words = ["abc","car","ada","racecar","cool"]
# Output: "ada"
# Explanation: The first string that is palindromic is "ada".
# Note that "racecar" is also palindromic, but it is not the first.

# Example 2:
# Input: words = ["notapalindrome","racecar"]
# Output: "racecar"
# Explanation: The first and only string that is palindromic is "racecar".

# Example 3:
# Input: words = ["def","ghi"]
# Output: ""
# Explanation: There are no palindromic strings, so the empty string is returned.
 
# Constraints:
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists only of lowercase English letters.



# sol 1

# class Solution:
#     def firstPalindrome(self, words: List[str]) -> str:
        
#         for word in words:
#             if word == word[::-1]:
#                 return word
#         return ""
    

# sol 2

# class Solution:
#     def firstPalindrome(self, words: List[str]) -> str:
#         return next((s for s in words if all(s[i]==s[-(i+1)] for i in range(len(s)//2))), "")
    

# sol 3

# class Solution:
#     def firstPalindrome(self, words: List[str]) -> str:
#         return next((s for s in words if s==s[::-1]), "")
        

# sol 4

# class Solution:
#     def check(self, s: str) -> bool:
#         i, j = 0, len(s) - 1
#         while i <= j:
#             if s[i] == s[j]:
#                 i += 1
#                 j -= 1
#             else:
#                 return False
#         return True
    
#     def firstPalindrome(self, words: List[str]) -> str:
#         for word in words:
#             if self.check(word):
#                 return word
#         return ""


