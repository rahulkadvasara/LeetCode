# 409. Longest Palindrome
# Easy

# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome.

# Example 1:
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

# Example 2:
# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.
 
# Constraints:
# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.



# sol 1

# class Solution:
#     def longestPalindrome(self, s: str) -> int:
#         # Initialize a set to keep track of characters with odd frequencies
#         char_set = set()
#         # Initialize the length of the longest palindrome
#         length = 0
        
#         # Iterate over each character in the string
#         for char in s:
#             # If the character is already in the set, remove it and increase the length by 2
#             if char in char_set:
#                 char_set.remove(char)
#                 length += 2
#             # If the character is not in the set, add it to the set
#             else:
#                 char_set.add(char)
        
#         # If there are any characters left in the set, add 1 to the length for the middle character
#         if char_set:
#             length += 1
        
#         # Return the total length of the longest palindrome
#         return length


# sol 2

# class Solution:
#     def longestPalindrome(self, s: str) -> int:
#         c=Counter(s)
#         res=0
#         maxo=0
#         for i,j in c.items():
#             if j%2==0:
#                 res+=j
#             else:
#                 if maxo!=0 and j<maxo:
#                     res+=(j-1)
#                 elif maxo!=0:
#                     res+=(maxo-1)
#                     maxo=max(maxo,j)
#                 else:
#                     maxo=max(maxo,j)
#         return res+maxo