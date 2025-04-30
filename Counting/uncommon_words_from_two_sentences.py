# 884. Uncommon Words from Two Sentences
# Easy

# A sentence is a string of single-space separated words where each word consists only of lowercase letters.
# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
# Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

# Example 1:
# Input: s1 = "this apple is sweet", s2 = "this apple is sour"
# Output: ["sweet","sour"]
# Explanation:
# The word "sweet" appears only in s1, while the word "sour" appears only in s2.

# Example 2:
# Input: s1 = "apple apple", s2 = "banana"
# Output: ["banana"]

# Constraints:
# 1 <= s1.length, s2.length <= 200
# s1 and s2 consist of lowercase English letters and spaces.
# s1 and s2 do not have leading or trailing spaces.
# All the words in s1 and s2 are separated by a single space.



# sol 1 

# class Solution:
#     def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
#         count = Counter(s1.split()) + Counter(s2.split())
#         return [word for word, freq in count.items() if freq == 1]
    

# sol 2

# def uncommon_from_sentences(s1, s2):
#     set_words = set()
#     dup_set = set()

#     # Split sentences into words
#     words1 = s1.split()
#     words2 = s2.split()

#     # Process words from the first sentence
#     for word in words1:
#         if word not in dup_set:
#             if word in set_words:
#                 set_words.remove(word)
#                 dup_set.add(word)
#             else:
#                 set_words.add(word)

#     # Process words from the second sentence
#     for word in words2:
#         if word not in dup_set:
#             if word in set_words:
#                 set_words.remove(word)
#                 dup_set.add(word)
#             else:
#                 set_words.add(word)

#     return list(set_words)

# # Example usage
# s1 = "this is a test"
# s2 = "test is a test"
# print(uncommon_from_sentences(s1, s2))


# sol 3

# class Solution:
#     def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
#         word_count = {}
#         words = (s1 + " " + s2).split()

#         # Count words
#         for word in words:
#             word_count[word] = word_count.get(word, 0) + 1

#         # Collect words that appear only once
#         return [word for word, count in word_count.items() if count == 1]