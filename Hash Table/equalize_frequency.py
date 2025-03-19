# 2423. Remove Letter To Equalize Frequency
# Easy

# You are given a 0-indexed string word, consisting of lowercase English letters. You need to select one index and remove the letter at that index from word so that the frequency of every letter present in word is equal.
# Return true if it is possible to remove one letter so that the frequency of all letters in word are equal, and false otherwise.

# Note:
# The frequency of a letter x is the number of times it occurs in the string.
# You must remove exactly one letter and cannot choose to do nothing.

# Example 1:
# Input: word = "abcc"
# Output: true
# Explanation: Select index 3 and delete it: word becomes "abc" and each character has a frequency of 1.

# Example 2:
# Input: word = "aazz"
# Output: false
# Explanation: We must delete a character, so either the frequency of "a" is 1 and the frequency of "z" is 2, or vice versa. It is impossible to make all present letters have equal frequency.
 
# Constraints:
# 2 <= word.length <= 100
# word consists of lowercase English letters only.



# sol 1

# from collections import Counter, defaultdict

# class Solution:
#     def equalFrequency(self, word: str) -> bool:
#         letter_freqs = Counter(word)
#         freq_letters = defaultdict(list)

#         for letter, freq in letter_freqs.items():
#             freq_letters[freq].append(letter)
 
#         if len(freq_letters) == 1:
#             return len(letter_freqs) == len(word) or len(letter_freqs) == 1

#         if len(freq_letters) == 2:
#             freq_1, freq_2 = freq_letters.keys()
#             return (
#                 ((freq_1 == 1 or freq_1 - 1 == freq_2) and len(freq_letters[freq_1]) == 1) or 
#                 ((freq_2 == 1 or freq_2 - 1 == freq_1) and len(freq_letters[freq_2]) == 1)
#             )

#         return False


# sol 2

# class Solution:
#     def equalFrequency(self, word: str) -> bool:
#         c = Counter(word)
#         freq = [v for v in c.values()]
#         for i in range(len(freq)):
#             freq[i] -= 1
#             if len(set(freq)) == 1:
#                 return True
#             if freq[i] == 0:
#                 if len(set(freq)) == 2:
#                     return True
#             freq[i] += 1
#         return False
        


# sol 3

# class Solution:
#     def equalFrequency(self, word: str) -> bool:
#         d = {}
#         for i in word:
#             if i in d:
#                 d[i] += 1
#             else:
#                 d[i] = 1
#         for char in list(d.keys()):
#             d[char] -= 1
#             if d[char] == 0:
#                 del d[char]
#             if len(set(d.values())) == 1:
#                 return True
#             if char in d:
#                 d[char] += 1
#             else:
#                 d[char] = 1
#         return False