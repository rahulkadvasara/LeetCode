# 748. Shortest Completing Word
# Easy

# Given a string licensePlate and an array of strings words, find the shortest completing word in words.
# A completing word is a word that contains all the letters in licensePlate. Ignore numbers and spaces in licensePlate, and treat letters as case insensitive. If a letter appears more than once in licensePlate, then it must appear in the word the same number of times or more.
# For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' twice. Possible completing words are "abccdef", "caaacab", and "cbca".
# Return the shortest completing word in words. It is guaranteed an answer exists. If there are multiple shortest completing words, return the first one that occurs in words.

# Example 1:
# Input: licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]
# Output: "steps"
# Explanation: licensePlate contains letters 's', 'p', 's' (ignoring case), and 't'.
# "step" contains 't' and 'p', but only contains 1 's'.
# "steps" contains 't', 'p', and both 's' characters.
# "stripe" is missing an 's'.
# "stepple" is missing an 's'.
# Since "steps" is the only word containing all the letters, that is the answer.

# Example 2:
# Input: licensePlate = "1s3 456", words = ["looks","pest","stew","show"]
# Output: "pest"
# Explanation: licensePlate only contains the letter 's'. All the words contain 's', but among these "pest", "stew", and "show" are shortest. The answer is "pest" because it is the word that appears earliest of the 3.
 
# Constraints:
# 1 <= licensePlate.length <= 7
# licensePlate contains digits, letters (uppercase or lowercase), or space ' '.
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 15
# words[i] consists of lower case English letters.



# sol 1

# class Solution:
#     def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
#         # Create a frequency dictionary for the letters in the license plate
#         freq = {}
#         for char in licensePlate:
#             if char.isalpha():
#                 char = char.lower()
#                 freq[char] = freq.get(char, 0) + 1
        
#         # Initialize the result with an empty string
#         result = ""
        
#         # Iterate through each word in the list
#         for word in words:
#             # Create a copy of the frequency dictionary for the current word
#             temp_freq = freq.copy()
            
#             # Check if the current word can complete the license plate
#             for char in word:
#                 if char in temp_freq:
#                     temp_freq[char] -= 1
            
#             # If all characters are satisfied, check if it's the shortest
#             if all(count <= 0 for count in temp_freq.values()):
#                 if not result or len(word) < len(result):
#                     result = word
        
#         return result
    


# sol 2

# class Solution:
#     def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
#         licensePlate = ''.join([i.lower() for i in licensePlate if i.isalpha()])
#         words = sorted(words, key=len)
#         for word in words:
#             for i in range(len(licensePlate)):
#                 if word.count(licensePlate[i]) < licensePlate.count(licensePlate[i]):
#                     break
#                 if i == len(licensePlate)-1:
#                     return word
        

# sol 3

# class Solution:
#     def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
#         l=licensePlate.lower()
#         a=[]
#         f=0
#         b=[]
#         for i in l:
#             if i.isalpha():
#                 a.append(i)
#         words = sorted(words, key=len)
#         for i in words:
#             for j in range(len(a)):
#                 if i.count(a[j])<a.count(a[j]):
#                     break
#                 elif j==len(a)-1:
#                     return i

#             #     if j not in i:
#             #         f=f+1
#             #     else:
#             #         i.replace(j,'')
#             # if f==0:
#             #     b.append(i)
#         return b

                