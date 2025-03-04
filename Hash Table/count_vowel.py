# 2062. Count Vowel Substrings of a String
# Easy

# A substring is a contiguous (non-empty) sequence of characters within a string.
# A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.
# Given a string word, return the number of vowel substrings in word.

# Example 1:
# Input: word = "aeiouu"
# Output: 2
# Explanation: The vowel substrings of word are as follows (underlined):
# - "aeiouu"
# - "aeiouu"

# Example 2:
# Input: word = "unicornarihan"
# Output: 0
# Explanation: Not all 5 vowels are present, so there are no vowel substrings.

# Example 3:
# Input: word = "cuaieuouac"
# Output: 7
# Explanation: The vowel substrings of word are as follows (underlined):
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"

# Constraints:
# 1 <= word.length <= 100
# word consists of lowercase English letters only.



# sol 1

# from collections import defaultdict

# class Solution:
#     def countVowelSubstrings(self, word):
#         vowels_map = {'a': True, 'e': True, 'i': True, 'o': True, 'u': True}
        
#         len_word = len(word)
        
#         left_index = 0
#         right_index = 0
#         ret_val = 0
#         char_to_freq_map = defaultdict(int)

#         i = 0
#         while (i < len_word):
#             c = word[i]
#             if c in vowels_map.keys():
#                 char_to_freq_map[c] += 1

#                 while set(char_to_freq_map.keys()) == set(vowels_map.keys()):
#                     c = word[right_index]
#                     char_to_freq_map[c] -= 1
#                     if (char_to_freq_map[c] <= 0):
#                         char_to_freq_map.pop(c)
#                     right_index += 1
#                 ret_val += (right_index - left_index)
#             else:
#                 char_to_freq_map.clear()
#                 left_index = i + 1
#                 right_index = i + 1
#             i += 1
        
#         return ret_val
    


# sol 2

# class Solution:
#     def countVowelSubstrings(self, word: str) -> int:
#         vowels = set('aeiou')
#         n = len(word)
#         ans = 0
#         for i in range(n):
#             for j in range(i, n):
#                 if set(word[i:j+1]) == vowels:
#                     ans += 1
#         return ans
    

# sol 3

# class Solution:
#     def countVowelSubstrings(self, word: str) -> int:
#         ans = 0 
#         freq = defaultdict(int)
#         for i, x in enumerate(word): 
#             if x in "aeiou": 
#                 if not i or word[i-1] not in "aeiou": 
#                     jj = j = i # set anchor
#                     freq.clear()
#                 freq[x] += 1
#                 while len(freq) == 5 and all(freq.values()): 
#                     freq[word[j]] -= 1
#                     j += 1
#                 ans += j - jj
#         return ans 
    

# sol 4

# class Solution:
#     def countVowelSubstrings(self, word: str) -> int:
#         s = set("aeiou")
#         ans, n = 0, len(word)
#         for i in range(n):
#             t = set()
#             for c in word[i:]:
#                 if c not in s:
#                     break
#                 t.add(c)
#                 ans += len(t) >= 5
#         return ans
        