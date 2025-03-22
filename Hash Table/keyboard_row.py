# 500. Keyboard Row
# Easy

# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.
# Note that the strings are case-insensitive, both lowercased and uppercased of the same letter are treated as if they are at the same row.
# In the American keyboard:
# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".

# Example 1:
# Input: words = ["Hello","Alaska","Dad","Peace"]
# Output: ["Alaska","Dad"]
# Explanation:
# Both "a" and "A" are in the 2nd row of the American keyboard due to case insensitivity.

# Example 2:
# Input: words = ["omk"]
# Output: []

# Example 3:
# Input: words = ["adsdf","sfd"]
# Output: ["adsdf","sfd"]

# Constraints:
# 1 <= words.length <= 20
# 1 <= words[i].length <= 100
# words[i] consists of English letters (both lowercase and uppercase). 



# sol 1

# class Solution:
#     def findWords(self, words: List[str]) -> List[str]:
#         hashmap = {
#             'q': 1, 'w': 1, 'e': 1, 'r': 1, 't': 1, 'y': 1, 'u': 1, 'i': 1, 'o': 1, 'p': 1,
#             'a': 2, 's': 2, 'd': 2, 'f': 2, 'g': 2, 'h': 2, 'j': 2, 'k': 2, 'l': 2,
#             'z': 3, 'x': 3, 'c': 3, 'v': 3, 'b': 3, 'n': 3, 'm': 3
#         }

#         output = []
#         for word in words:
#             lword = word.lower()
#             row = hashmap[lword[0]]
            
#             if all(hashmap[char] == row for char in lword):
#                 output.append(word)

#         return output
    

# sol 2

# class Solution:
#     def findWords(self, words: List[str]) -> List[str]:
#         rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
#         output = []
#         for word in words:
#             lword = word.lower()
#             row = [r for r in rows if lword[0] in r][0]
            
#             if all(char in row for char in lword):
#                 output.append(word)

#         return output
    

# sol 3

# class Solution:
#     def findWords(self, words: List[str]) -> List[str]:
#         l1="qwertyuiop"
#         l2="asdfghjkl"
#         l3="zxcvbnm"
#         res=[]
#         for word in words:
#             w=word.lower()
#             if len(set(l1+w))==len(l1) or len(set(l2+w))==len(l2) or len(set(l3+w))==len(l3) :
#                 res.append(word)
#         return res


                