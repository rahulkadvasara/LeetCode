# 819. Most Common Word
# Easy

# Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.
# The words in paragraph are case-insensitive and the answer should be returned in lowercase.

# Example 1:
# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
# Output: "ball"
# Explanation: 
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"), 
# and that "hit" isn't the answer even though it occurs more because it is banned.

# Example 2:
# Input: paragraph = "a.", banned = []
# Output: "a"
 
# Constraints:
# 1 <= paragraph.length <= 1000
# paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
# 0 <= banned.length <= 100
# 1 <= banned[i].length <= 10
# banned[i] consists of only lowercase English letters.



# sol 1 

# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         # Convert the paragraph to lowercase and replace punctuation with spaces
#         for c in "!?',;.":
#             paragraph = paragraph.replace(c, ' ')
#         words = paragraph.lower().split()
        
#         # Count the frequency of each word
#         word_count = Counter(words)
        
#         # Remove banned words from the count
#         for word in banned:
#             if word in word_count:
#                 del word_count[word]
        
#         # Find the most common word
#         return word_count.most_common(1)[0][0]  # Return the most common word only
    


# sol 2

# from collections import defaultdict
# import re

# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         # Convert banned list to a set for quick lookup
#         banned_set = set(word.lower() for word in banned)
        
#         # Split paragraph into words using regex and normalize to lowercase
#         words = re.split(r'[^A-Za-z]+', paragraph.lower())
        
#         # Count word frequencies
#         counter = defaultdict(int)
#         max_count = 0
#         result = ""

#         for word in words:
#             if word and word not in banned_set:
#                 counter[word] += 1
#                 if counter[word] > max_count:
#                     max_count = counter[word]
#                     result = word
        
#         return result
    


# sol 3

# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         freq_dict = {}
#         max_word = None
#         max_count = 0
#         banned = set(banned)
#         for word in re.findall(r'\w+', paragraph.lower()):
#             if word not in banned:
#                 if word not in freq_dict:
#                     freq_dict[word]=1
#                     if max_count == 0:
#                         max_count = 1
#                         max_word = word
#                 else:
#                     freq_dict[word]+=1
#                     if max_count < freq_dict[word]:
#                         max_count = freq_dict[word]
#                         max_word = word
#         return max_word
        

    
# sol 4

# import string 
# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         # Remove punctuation
#         for ch in string.punctuation:
#             paragraph = paragraph.replace(ch, " ")

#         words = paragraph.lower().split()
#         words = [word for word in words if word not in banned]
#         word_counts = Counter(words)
#         return word_counts.most_common(1)[0][0]


