# 2531. Make Number of Distinct Characters Equal
# Medium

# You are given two 0-indexed strings word1 and word2.
# A move consists of choosing two indices i and j such that 0 <= i < word1.length and 0 <= j < word2.length and swapping word1[i] with word2[j].
# Return true if it is possible to get the number of distinct characters in word1 and word2 to be equal with exactly one move. Return false otherwise.

# Example 1:
# Input: word1 = "ac", word2 = "b"
# Output: false
# Explanation: Any pair of swaps would yield two distinct characters in the first string, and one in the second string.

# Example 2:
# Input: word1 = "abcc", word2 = "aab"
# Output: true
# Explanation: We swap index 2 of the first string with index 0 of the second string. The resulting strings are word1 = "abac" and word2 = "cab", which both have 3 distinct characters.

# Example 3:
# Input: word1 = "abcde", word2 = "fghij"
# Output: true
# Explanation: Both resulting strings will have 5 distinct characters, regardless of which indices we swap.

# Constraints:
# 1 <= word1.length, word2.length <= 105
# word1 and word2 consist of only lowercase English letters.



# sol 1

# class Solution:
#     def isItPossible(self, word1: str, word2: str) -> bool:
#         freq1 = Counter(word1)
#         freq2 = Counter(word2)
#         sz1, sz2 = len(freq1), len(freq2)
#         for c1 in ascii_lowercase: 
#             for c2 in ascii_lowercase: 
#                 if freq1[c1] and freq2[c2]: 
#                     if c1 == c2: 
#                         if sz1 == sz2: return True 
#                     else: 
#                         cnt1, cnt2 = sz1, sz2 
#                         if freq1[c1] == 1: cnt1 -= 1
#                         if freq1[c2] == 0: cnt1 += 1
#                         if freq2[c1] == 0: cnt2 += 1
#                         if freq2[c2] == 1: cnt2 -= 1
#                         if cnt1 == cnt2: return True 
#         return False 
    


# sol 2

# class Solution:
#     def isItPossible(self, word1: str, word2: str) -> bool:
#         c1,c2=Counter(word1),Counter(word2)
#         num1,num2=len(c1),len(c2)
#         for k1,v1 in c1.items():
#             for k2,v2 in c2.items():
#                 cur1,cur2 =num1,num2
#                 if v1==1 and k1!=k2:
#                     cur1-=1
#                 if v2 == 1 and k1 !=k2:
#                     cur2-=1
#                 if k1 not in c2:
#                     cur2+=1
#                 if k2 not in c1:
#                     cur1 +=1
#                 if cur1 ==cur2:
#                     return True
#         return False
    


# sol 3

# class Solution:
    
#     def insertAndRemove(self, mp, toInsert, toRemove): 
#         mp[toInsert]+=1
#         mp[toRemove]-=1
        
#         if(mp[toRemove]==0):
#             del mp[toRemove]     # if freq of that char reaches zero, then remove the key from dict
        
        
#     def isItPossible(self, word1: str, word2: str) -> bool:
        
#         mp1, mp2 = Counter(word1), Counter(word2)  # Get freq of chars using Counter
	
#         """
#         # If you are not familiar with Counters, you can simply do this:
#         mp1=defaultdict(int)
#         mp2=defaultdict(int)

#         for w1 in word1:
#             mp1[w1]+=1;   #store freq of chars in word1 in mp1

#         for w2 in word2:
#             mp2[w2]+=1;  #store freq of chars in word2 in mp2
#         """
		
#         for c1 in string.ascii_lowercase:         # this for loop iterates through c1='a' to c1='z'
#             for c2 in string.ascii_lowercase:     # this for loop iterates through c2='a' to c2='z'
                
#                 if c1 not in mp1 or c2 not in mp2:  # if any of the char is not present then skip
#                     continue

#                 self.insertAndRemove(mp1, c2, c1); # insert c2 to word1 and remove c1 from word1
#                 self.insertAndRemove(mp2, c1, c2); # insert c1 to word2 and remove c2 from word2
                
#                 if len(mp1)== len(mp2):  # if size of both dicts are equal then possible return true
#                     return True
				
#                 # reset back the maps
#                 self.insertAndRemove(mp1, c1, c2); # insert c1 back to word1 and remove c2 from word1         
#                 self.insertAndRemove(mp2, c2, c1); # insert c2 back to word2 and remove c1 from word2                
#         return False
    


# sol 4

# class Solution:
#     def isItPossible(self, word1: str, word2: str) -> bool:
#         a = Counter(word1)
#         b = Counter(word2)
#         difference = len(b) - len(a)
#         if abs(difference) > 2:
#             return False
#         for aChoice in a:
#             outerDifference = difference
#             if a[aChoice] == 1:
#                 outerDifference += 1
#             for bChoice in b:
#                 innerDifference = outerDifference
#                 if aChoice == bChoice:
#                     innerDifference = difference
#                 else:
#                     if aChoice not in b:
#                         innerDifference += 1
#                     if bChoice not in a:
#                         innerDifference -= 1
#                     if b[bChoice] == 1:
#                         innerDifference -= 1
#                 if innerDifference == 0:
#                     return True
#         return False