# 2085. Count Common Words With One Occurrence
# Easy

# Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two arrays.

# Example 1:
# Input: words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]
# Output: 2
# Explanation:
# - "leetcode" appears exactly once in each of the two arrays. We count this string.
# - "amazing" appears exactly once in each of the two arrays. We count this string.
# - "is" appears in each of the two arrays, but there are 2 occurrences of it in words1. We do not count this string.
# - "as" appears once in words1, but does not appear in words2. We do not count this string.
# Thus, there are 2 strings that appear exactly once in each of the two arrays.

# Example 2:
# Input: words1 = ["b","bb","bbb"], words2 = ["a","aa","aaa"]
# Output: 0
# Explanation: There are no strings that appear in each of the two arrays.

# Example 3:
# Input: words1 = ["a","ab"], words2 = ["a","a","a","ab"]
# Output: 1
# Explanation: The only string that appears exactly once in each of the two arrays is "ab".

# Constraints:
# 1 <= words1.length, words2.length <= 1000
# 1 <= words1[i].length, words2[j].length <= 30
# words1[i] and words2[j] consists only of lowercase English letters.



# sol 1

# class Solution:
#     def countWords(self, words1: List[str], words2: List[str]) -> int:
#         from collections import Counter
#         count1 = Counter(words1)
#         count2 = Counter(words2)
#         result = 0
#         for word in count1:
#             if count1[word] == 1 and count2[word] == 1:
#                 result += 1
#         return result
    

# sol 2

# class Solution:
#     def countWords(self, words1: List[str], words2: List[str]) -> int:
#         count1 = Counter(words1)
#         count2 = Counter(words2)
#         count = 0
#         for i in count1:
#             if count1[i]==1 and count2.get(i,0)==1:
#                 count+=1
#         return count
        

# sol 3

# class Solution:
#     def countWords(self, words1: List[str], words2: List[str]) -> int:
#         count1 = Counter(words1)
#         count2 = Counter(words2)
#         return sum(1 for i in count1 if count1[i] == 1 and count2[i] == 1)
    

# sol 4

# class Solution:
#     def countWords(self, words1: List[str], words2: List[str]) -> int:
#         count = 0
#         hashmap = {}
#         hashmap2 = {}
#         for i in words1:
#             if i in hashmap:
#                 hashmap[i] += 1
#             else:
#                 hashmap[i] = 1
#         for i in words2:
#             if i in hashmap2:
#                 hashmap2[i] += 1
#             else:
#                 hashmap2[i] = 1
#         for i in hashmap:
#             if hashmap[i] == 1 and i in hashmap2 and hashmap2[i] == 1:
#                 count += 1   
#         return count