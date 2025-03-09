# 2287. Rearrange Characters to Make Target String
# Easy

# You are given two 0-indexed strings s and target. You can take some letters from s and rearrange them to form new strings.
# Return the maximum number of copies of target that can be formed by taking letters from s and rearranging them.

# Example 1:
# Input: s = "ilovecodingonleetcode", target = "code"
# Output: 2
# Explanation:
# For the first copy of "code", take the letters at indices 4, 5, 6, and 7.
# For the second copy of "code", take the letters at indices 17, 18, 19, and 20.
# The strings that are formed are "ecod" and "code" which can both be rearranged into "code".
# We can make at most two copies of "code", so we return 2.

# Example 2:
# Input: s = "abcba", target = "abc"
# Output: 1
# Explanation:
# We can make one copy of "abc" by taking the letters at indices 0, 1, and 2.
# We can make at most one copy of "abc", so we return 1.
# Note that while there is an extra 'a' and 'b' at indices 3 and 4, we cannot reuse the letter 'c' at index 2, so we cannot make a second copy of "abc".

# Example 3:
# Input: s = "abbaccaddaeea", target = "aaaaa"
# Output: 1
# Explanation:
# We can make one copy of "aaaaa" by taking the letters at indices 0, 3, 6, 9, and 12.
# We can make at most one copy of "aaaaa", so we return 1.

# Constraints:
# 1 <= s.length <= 100
# 1 <= target.length <= 10
# s and target consist of lowercase English letters.
 
# Note: This question is the same as 1189: Maximum Number of Balloons.



# sol 1

# class Solution:
#     def rearrangeCharacters(self, s: str, target: str) -> int:
#         target_count = Counter(target)
#         s_count = Counter(s)
#         ans = float('inf')
#         for ch in target_count:
#             if ch not in s_count:
#                 return 0
#             ans = min(ans, s_count[ch] // target_count[ch])
#         return ans
    

# sol 2

# class Solution:
#     def rearrangeCharacters(self, s: str, target: str) -> int:
#         target_count = Counter(target)
#         s_count = Counter(s)
#         return min(s_count[ch] // target_count[ch] for ch in target_count)
    

# sol 3

# class Solution:
#     def rearrangeCharacters(self, s: str, target: str) -> int:
#         target_count = Counter(target)
#         s_count = Counter(s)
#         return min(map(lambda x: s_count[x] // target_count[x], target_count))
    

# sol 4

# class Solution:
#     def rearrangeCharacters(self, s: str, target: str) -> int:
#         target_count = {}
#         s_count = {}
        
#         for ch in target:
#             if ch in target_count:
#                 target_count[ch] += 1
#             else:
#                 target_count[ch] = 1
        
#         for ch in s:
#             if ch in s_count:
#                 s_count[ch] += 1
#             else:
#                 s_count[ch] = 1
        
#         ans = float('inf')
#         for ch in target_count:
#             if ch not in s_count:
#                 return 0
#             ans = min(ans, s_count[ch] // target_count[ch])
        
#         return ans
    

# sol 5

# class Solution:
#     def rearrangeCharacters(self, s: str, target: str) -> int:
#         target_count = {}
#         s_count = {}
        
#         for ch in target:
#             target_count[ch] = target_count.get(ch, 0) + 1
        
#         for ch in s:
#             s_count[ch] = s_count.get(ch, 0) + 1
        
#         ans = float('inf')
#         for ch in target_count:
#             if ch not in s_count:
#                 return 0
#             ans = min(ans, s_count[ch] // target_count[ch])
        
#         return ans
    

# sol 6

# class Solution:
#     def rearrangeCharacters(self, s: str, target: str) -> int:
#         freq_s = [0] * 26
#         freq_t = [0] * 26
#         for c in s:
#             freq_s[ord(c) - ord('a')] += 1

#         for c in target:
#             freq_t[ord(c) - ord('a')] += 1
        
#         min_count = float('inf')
#         for i in range(26):
#             if freq_t[i] > 0:
#                 min_count = min(min_count, freq_s[i] // freq_t[i])

#         return min_count

