# 1189. Maximum Number of Balloons
# Easy

# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
# You can use each character in text at most once. Return the maximum number of instances that can be formed.

# Example 1:
# Input: text = "nlaebolko"
# Output: 1

# Example 2:
# Input: text = "loonbalxballpoon"
# Output: 2

# Example 3:
# Input: text = "leetcode"
# Output: 0

# Constraints:
# 1 <= text.length <= 104
# text consists of lower case English letters only.
 


# sol 1 

# class Solution:
#     def maxNumberOfBalloons(self, text: str) -> int:
#         # Count the occurrences of each character in the text
#         char_count = {}
#         for char in text:
#             if char in "balloon":
#                 char_count[char] = char_count.get(char, 0) + 1
        
#         # Calculate the maximum number of "balloon" that can be formed
#         # 'b' and 'a' appear once, 'l' appears twice, 'o' appears twice, 'n' appears once
#         return min(char_count.get('b', 0), 
#                    char_count.get('a', 0), 
#                    char_count.get('l', 0) // 2, 
#                    char_count.get('o', 0) // 2, 
#                    char_count.get('n', 0))
    


# sol 2

# class Solution:
#     def maxNumberOfBalloons(self, text: str) -> int:
#         count = defaultdict(int)
#         for x in text:
#             if x in "balon":
#                 count[x] += 1
#         count['l'] //= 2
#         count['o'] //= 2
#         return min(count['b'], count['a'], count['l'], count['o'], count['n'])       