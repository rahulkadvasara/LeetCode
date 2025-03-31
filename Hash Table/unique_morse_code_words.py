
# 804. Unique Morse Code Words
# Easy

# International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:
# 'a' maps to ".-",
# 'b' maps to "-...",
# 'c' maps to "-.-.", and so on.
# For convenience, the full table for the 26 letters of the English alphabet is given below:
# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.
# For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.
# Return the number of different transformations among all words we have.

 
# Example 1:
# Input: words = ["gin","zen","gig","msg"]
# Output: 2
# Explanation: The transformation of each word is:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."
# There are 2 different transformations: "--...-." and "--...--.".

# Example 2:
# Input: words = ["a"]
# Output: 1
 
# Constraints:
# 1 <= words.length <= 100
# 1 <= words[i].length <= 12
# words[i] consists of lowercase English letters.



# sol 1

# class Solution:
#     def uniqueMorseRepresentations(self, words: List[str]) -> int:

#         a = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

#         alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#         print(len(a))

#         lst = []

#         for i in range(len(words)):
#             temp = []
#             for k in words[i]:
#                 if k in alp:
#                     index = alp.index(k)
#                 temp.append(a[index])
#             lst.append(''.join(temp))
#         return len(set(lst))


# sol 2

# class Solution:
#     def uniqueMorseRepresentations(self, words: List[str]) -> int:
#         morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
#                       "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
#                       "..-","...-",".--","-..-","-.--","--.."]
        
#         morse_set = set()
        
#         for word in words:
#             morse_word = ''.join(morse_code[ord(char) - ord('a')] for char in word)
#             morse_set.add(morse_word)
        
#         return len(morse_set)
    

# sol 3

# class Solution:
#     def uniqueMorseRepresentations(self, words: List[str]) -> int:
#         # Define the English alphabet
#         letters = "abcdefghijklmnopqrstuvwxyz"
        
#         # Define the corresponding Morse code representations
#         morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

#         # Create a dictionary that maps letters to Morse code
#         morse_dict = dict(zip(letters, morse_code))

#         # Initialize a list to store words converted to Morse code
#         words2 = []

#         # Iterate through each word in the input list
#         for word in words:
#             # Initialize an empty string to store the Morse code for the current word
#             k = ""
            
#             # Iterate through each character in the current word
#             for i in word:
#                 # Append the Morse code representation of the character to the string
#                 k += morse_dict[i]

#             # Append the Morse code for the current word to the list
#             words2.append(k) 

#         # Return the count of unique Morse code representations
#         return len(set(words2))
    

# sol 4

# class Solution:
#     def uniqueMorseRepresentations(self, words: List[str]) -> int:
#         morse = {'a':".-", 'b':"-...", 'c':"-.-.", 'd':"-..", 'e':".", 'f':"..-.", 'g':"--.", 'h':"....", 'i':"..", 'j':".---", 'k':"-.-", 'l':".-..", 'm':"--", 'n':"-.", 'o':"---", 'p':".--.", 'q':"--.-", 'r':".-.", 's':"...", 't':"-", 'u':"..-", 'v':"...-", 'w':".--", 'x':"-..-", 'y':"-.--", 'z':"--.."}
#         fin = set()
#         for word in words:
#             temp = ""
#             for i in range(len(word)):
#                 temp += morse[word[i]]
#             fin.add(temp)
#         return len(fin)
    

# sol 5

# class Solution:
#     def uniqueMorseRepresentations(self, words: List[str]) -> int:

#         morse_codes = {'a': ".-",'b': "-...",'c': "-.-.",'d': "-..",
#         'e': ".",'f': "..-.",'g': "--.",'h': "....",'i': "..",
#         'j': ".---",'k': "-.-",'l': ".-..",'m': "--",'n': "-.",
#         'o': "---",'p': ".--.",'q': "--.-",'r': ".-.",'s': "...",
#         't': "-",'u': "..-",'v': "...-",'w': ".--",'x': "-..-",
#         'y': "-.--",'z':  "--.."}

#         out_set = set()

#         for word in words:
#             trns = ''.join([morse_codes[char] for char in word])
#             out_set.add(trns)

#         return len(out_set)