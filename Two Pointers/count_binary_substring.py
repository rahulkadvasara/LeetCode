# 696. Count Binary Substrings
# Easy

# Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.
# Substrings that occur multiple times are counted the number of times they occur.

# Example 1:
# Input: s = "00110011"
# Output: 6
# Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
# Notice that some of these substrings repeat and are counted the number of times they occur.
# Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

# Example 2:
# Input: s = "10101"
# Output: 4
# Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
 
# Constraints:
# 1 <= s.length <= 105
# s[i] is either '0' or '1'.



# sol 1

# from collections import defaultdict

# class Solution:
#     def countBinarySubstrings(self, s: str) -> int:
#         count = 0
#         occur = defaultdict(int)
#         prev_char = s[0]

#         for char in s:
#             if char != prev_char:
#                 count += min(occur["0"], occur["1"])
#                 occur[char] = 1
            
#             else:
#                 occur[char] = occur[char] + 1

#             prev_char = char
        
#         count += min(occur["0"], occur["1"])
#         return count
    


# sol 2

# class Solution:
#     def countBinarySubstrings(self, s: str) -> int:
#         groups = [1]  # Initialize the first group count to 1
#         count = 0

#         # Count the length of consecutive groups of '0's and '1's
#         for i in range(1, len(s)):
#             if s[i] == s[i - 1]:
#                 groups[-1] += 1
#             else:
#                 groups.append(1)

#         # Calculate the number of valid substrings
#         for i in range(1, len(groups)):
#             count += min(groups[i], groups[i - 1])

#         return count
    

# sol 3

# class Solution:
#     def countBinarySubstrings(self, s: str) -> int:
#         pre= 0
#         count= 1
#         actual= 0
#         for i in range(1,len(s)):
#             if(s[i]==s[i-1]):
#                 count+=1
#             else:
#                 actual+= min(pre,count)
#                 pre= count
#                 count= 1
#         actual+= min(pre,count)
#         return actual
    

# sol 4

# class Solution:
#     def countBinarySubstrings(self, s: str) -> int:
#         s = list(map(len, s.replace('01', '0 1').replace('10', '1 0').split()))
        
#         answer = 0
#         for i in range(1, len(s)):
#             answer += min(s[i], s[i-1])
        

#         return answer

        