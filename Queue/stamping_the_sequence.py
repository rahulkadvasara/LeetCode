# 936. Stamping The Sequence
# Hard

# You are given two strings stamp and target. Initially, there is a string s of length target.length with all s[i] == '?'.
# In one turn, you can place stamp over s and replace every letter in the s with the corresponding letter from stamp.
# For example, if stamp = "abc" and target = "abcba", then s is "?????" initially. In one turn you can:
# place stamp at index 0 of s to obtain "abc??",
# place stamp at index 1 of s to obtain "?abc?", or
# place stamp at index 2 of s to obtain "??abc".
# Note that stamp must be fully contained in the boundaries of s in order to stamp (i.e., you cannot place stamp at index 3 of s).
# We want to convert s to target using at most 10 * target.length turns.
# Return an array of the index of the left-most letter being stamped at each turn. If we cannot obtain target from s within 10 * target.length turns, return an empty array.

# Example 1:
# Input: stamp = "abc", target = "ababc"
# Output: [0,2]
# Explanation: Initially s = "?????".
# - Place stamp at index 0 to get "abc??".
# - Place stamp at index 2 to get "ababc".
# [1,0,2] would also be accepted as an answer, as well as some other answers.

# Example 2:
# Input: stamp = "abca", target = "aabcaca"
# Output: [3,0,1]
# Explanation: Initially s = "???????".
# - Place stamp at index 3 to get "???abca".
# - Place stamp at index 0 to get "abcabca".
# - Place stamp at index 1 to get "aabcaca".

# Constraints:
# 1 <= stamp.length <= target.length <= 1000
# stamp and target consist of lowercase English letters.




# sol 1 

# from typing import List
# from collections import deque

# class Solution:
#     def movesToStamp(self, stamp: str, target: str) -> List[int]:
#         m, n = len(stamp), len(target)
#         stamp = list(stamp)
#         target = list(target)
        
#         # Helper function to check if we can stamp at position i
#         def can_stamp(i):
#             for j in range(m):
#                 if target[i + j] != '?' and target[i + j] != stamp[j]:
#                     return False
#             return True
        
#         # Helper function to apply stamp at position i
#         def apply_stamp(i):
#             for j in range(m):
#                 target[i + j] = '?'
        
#         # Track visited positions and the stamping process
#         stamped = [False] * n
#         result = []
#         queue = deque()
        
#         # Initial queue fill
#         for i in range(n - m + 1):
#             if can_stamp(i):
#                 queue.append(i)
#                 apply_stamp(i)
#                 result.append(i)
#                 stamped[i] = True
        
#         # Process the queue
#         while queue:
#             pos = queue.popleft()
#             for i in range(max(0, pos - m + 1), min(n - m + 1, pos + m)):
#                 if can_stamp(i):
#                     if not stamped[i]:
#                         queue.append(i)
#                         apply_stamp(i)
#                         result.append(i)
#                         stamped[i] = True
        
#         # Verify that all characters in target are stamped
#         if all(c == '?' for c in target):
#             return result[::-1]
#         else:
#             return []




# sol 2

# class Solution:
#     def movesToStamp(self, stamp: str, target: str) -> List[int]:
#         N,M = len(target),len(stamp)
#         move = 0
#         maxmove = 10*N
#         ans = []
#         def check(string):
#             for i in range(M):
#                 if string[i] == stamp[i] or string[i] == '?':
#                     continue
#                 else:
#                     return False
#             return True
        
#         while move < maxmove:
#             premove = move
#             for i in range(N-M+1):
#                 if check(target[i:i+M]):
#                     move += 1
#                     ans.append(i)
#                     target = target[:i] + "?"*M + target[i+M:]
#                     if target == "?"*N : return ans[::-1]
#             if premove == move:return []
#         return []
    


# sol 3

# class Solution:
#     def movesToStamp(self, stamp: str, target: str) -> List[int]:
        
#         stamp, target = list(stamp), list(target)
#         m, n = len(stamp), len(target)
#         res = []
#         visited = [False]  * (n-m+1)
#         total_visited = 0

#         def can_stamp(i):
#             changed = False
#             for j in range(m):
#                 if target[i+j] == '?':
#                     continue
#                 if target[i+j] != stamp[j]:
#                     return False
#                 changed = True
#             return changed
        
#         def do_stamp(i):
#             nonlocal total_visited
#             for j in range(m):
#                 if target[i+j] != '?':
#                     target[i+j] = '?'
#                     total_visited += 1


#         while total_visited < n:
#             changed = False
#             for i in range(n-m+1):
#                 if not visited[i] and can_stamp(i):
#                     do_stamp(i)
#                     visited[i] = True
#                     changed = True
#                     res.append(i)
#             if not changed:
#                 return []
#         return res[::-1]

        

# sol 4

# class Solution:
#     def movesToStamp(self, s: str, t: str) -> List[int]:
#         options = {i*'*' + s[i:j] + (len(s)-j)*'*' for i in range(len(s)) for j in range(i, len(s)+1)} - {'*'*len(s)}
#         res = []
#         target = list(t)
        
#         updates = -1
#         while updates:
#             i = updates = 0
#             t = ''.join(target)
#             while i <= len(t) - len(s):
#                 if t[i:i+len(s)] in options:
#                     res.append(i)
#                     target[i:i+len(s)] = ['*']*len(s)
#                     updates += 1
#                 i += 1
                
#         return res[::-1] if set(target) == {'*'} else []
    


# sol 5

# from typing import List


# class Solution:
#     def movesToStamp(self, stamp: str, target: str) -> List[int]:
#         # The stamp and target must start with the same letter and end with the same letter
#         if stamp[0] != target[0] or stamp[-1] != target[-1]:
#             return []

#         # The target must contain at least one occurrence of the full stamp
#         idx = target.rfind(stamp)
#         if idx == -1:
#             return []

#         res = [idx]
#         stampSize = len(stamp)
#         rightTargetOffset = idx + stampSize
#         leftTarget, rightTarget = target[:idx], target[rightTargetOffset:]

#         # Handle the right-most part that doesn't contain the full stamp; for it, the stamp can only spread further to the left
#         while rightTarget:
#             # Try reduction by the left
#             rightTargetSize = len(rightTarget)
#             for stampStartIdx in range(max(1, stampSize - rightTargetSize), stampSize):
#                 if rightTarget.startswith(stamp[stampStartIdx:]):
#                     res.append(rightTargetOffset - stampStartIdx)
#                     subStampSize = stampSize - stampStartIdx
#                     rightTargetOffset += subStampSize
#                     rightTarget = rightTarget[subStampSize:]
#                     break
#             else:
#                 # No reduction possible, so the problem is impossible
#                 return []

#         while True:
#             # Find the next right-most occurrence of the full stamp, if any
#             idx = leftTarget.rfind(stamp)
#             if idx == -1:
#                 break

#             res.append(idx)
#             rightTargetOffset = idx + stampSize
#             leftTarget, rightTarget = leftTarget[:idx], leftTarget[rightTargetOffset:]

#             # Handle a middle part that doesn't contain the full stamp; for it, the stamp can spread further both to the left and to the right
#             while rightTarget:
#                 rightTargetSize = len(rightTarget)

#                 # If the part is shorter than the stamp, then we can check whether the stamp contains it
#                 if rightTargetSize < stampSize:
#                     idx = stamp.rfind(rightTarget)
#                     if idx != -1:
#                         res.append(rightTargetOffset - idx)
#                         rightTarget = ""  # Not needed but just for clarity
#                         break

#                 # Otherwise, try maximum reduction by the right first and then by the left
#                 for subStampSize in range(min(stampSize - 1, rightTargetSize), 0, -1):
#                     # Try reduction by the right first
#                     stampEndIdx = subStampSize
#                     if rightTarget.endswith(stamp[:stampEndIdx]):
#                         res.append(rightTargetOffset + rightTargetSize - stampEndIdx)
#                         rightTarget = rightTarget[:-stampEndIdx]
#                         break
#                     # And then by the left
#                     stampStartIdx = stampSize - subStampSize
#                     if rightTarget.startswith(stamp[stampStartIdx:]):
#                         res.append(rightTargetOffset - stampStartIdx)
#                         subStampSize = stampSize - stampStartIdx
#                         rightTargetOffset += subStampSize
#                         rightTarget = rightTarget[subStampSize:]
#                         break
#                 else:
#                     # No reduction possible at all, so the problem is impossible
#                     return []

#         # Handle the left-most part that doesn't contain the full stamp; for it, the stamp can only spread further to the right
#         while leftTarget:
#             # Try reduction by the right
#             leftTargetSize = len(leftTarget)
#             for stampEndIdx in range(min(stampSize - 1, leftTargetSize), 0, -1):
#                 if leftTarget.endswith(stamp[:stampEndIdx]):
#                     res.append(leftTargetSize - stampEndIdx)
#                     leftTarget = leftTarget[:-stampEndIdx]
#                     break
#             else:
#                 # No reduction possible, so the problem is impossible
#                 return []

#         res.reverse()
#         return res
    


# sol 6

# class Solution:
#     def movesToStamp(self, stamp: str, target: str) -> List[int]:
#         ls=len(stamp)
#         lt=len(target)
#         s="?"*lt
#         res=[]
#         temp=set()
#         for i in range(ls):
#             for j in range(ls-i):
#                 temp.add('?'*i+stamp[i:ls-j]+'?'*j)
#         while target!=s:
#             f=False
#             for i in range(lt-ls,-1,-1):
#                 if target[i:i+ls] in temp:
#                     target=target[:i]+'?'*ls+target[i+ls:]
#                     res.append(i)
#                     f=True
#             if not f:
#                 return []
#         return res[::-1]