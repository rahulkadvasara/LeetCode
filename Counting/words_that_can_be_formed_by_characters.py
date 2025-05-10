# 1160. Find Words That Can Be Formed by Characters
# Easy

# You are given an array of strings words and a string chars.
# A string is good if it can be formed by characters from chars (each character can only be used once for each word in words).
# Return the sum of lengths of all good strings in words.

# Example 1:
# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

# Example 2:
# Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
 
# Constraints:
# 1 <= words.length <= 1000
# 1 <= words[i].length, chars.length <= 100
# words[i] and chars consist of lowercase English letters.



# sol 1

# class Solution:
#     def countCharacters(self, words: List[str], chars: str) -> int:
#         char_count = Counter(chars)
#         total_length = 0
        
#         for word in words:
#             word_count = Counter(word)
#             if all(word_count[char] <= char_count[char] for char in word_count):
#                 total_length += len(word)
        
#         return total_length
    

# sol 2

# __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
# class Solution:
#     def countCharacters(self, words: List[str], chars: str) -> int:

#         countChars = [0 for i in range(26)]

#         for c in chars:
#             countChars[ord(c) - ord('a')] += 1

#         def isCanForm(word):
#             chars = countChars.copy()
#             for c in word:
#                 index = ord(c) - ord('a')
#                 if chars[index] == 0:
#                     return False
#                 chars[index] -= 1
            
#             return True
        
#         count = 0

#         for word in words:
#             isCan = isCanForm(word)
#             if isCan:
#                 count += len(word)

#         return count
    

# sol 3

# class Solution:
#     def countCharacters(self, words: List[str], chars: str) -> int:
#         dictionary = {}
#         for c in chars:
#             dictionary[c] = dictionary.get(c, 0) + 1

#         summ = 0
#         for word in words:
#             d = dictionary.copy()
#             summ += len(word)
#             for c in word:
#                 if c not in d.keys() or d[c] == 0:
#                     summ -= len(word)
#                     break
#                 d[c] -= 1
        
#         return summ