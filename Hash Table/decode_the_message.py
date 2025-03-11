# 2325. Decode the Message
# Easy

# You are given the strings key and message, which represent a cipher key and a secret message, respectively. The steps to decode message are as follows:
# Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
# Align the substitution table with the regular English alphabet.
# Each letter in message is then substituted using the table.
# Spaces ' ' are transformed to themselves.
# For example, given key = "happy boy" (actual key would have at least one instance of each letter in the alphabet), we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').
# Return the decoded message.

# Example 1:
# Input: key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"
# Output: "this is a secret"
# Explanation: The diagram above shows the substitution table.
# It is obtained by taking the first appearance of each letter in "the quick brown fox jumps over the lazy dog".

# Example 2:
# Input: key = "eljuxhpwnyrdgtqkviszcfmabo", message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
# Output: "the five boxing wizards jump quickly"
# Explanation: The diagram above shows the substitution table.
# It is obtained by taking the first appearance of each letter in "eljuxhpwnyrdgtqkviszcfmabo".
 
# Constraints:
# 26 <= key.length <= 2000
# key consists of lowercase English letters and ' '.
# key contains every letter in the English alphabet ('a' to 'z') at least once.
# 1 <= message.length <= 2000
# message consists of lowercase English letters and ' '.


# sol 1 

# class Solution:
#     def decodeMessage(self, key: str, message: str) -> str:
#         key_map = {}
#         for i, c in enumerate(key):
#             if c != ' ' and c not in key_map:
#                 key_map[c] = chr(97 + len(key_map))
#         key_map[' '] = ' '
#         return ''.join([key_map[c] for c in message])
    

# sol 2

# class Solution:
#     def decodeMessage(self, key: str, message: str) -> str:
#         dic_key={}
#         temp=97
#         temp2=""
#         for i in key:
#             if i!=" " and i not in dic_key:
#                 dic_key[i]=chr(temp)
#                 temp=temp+1
#         for j in message:
#             if j in dic_key:
#                 temp2=temp2+dic_key[j]
#             else:
#                 temp2=temp2+" "
#         return temp2
        