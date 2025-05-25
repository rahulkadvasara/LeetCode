# 2866. Beautiful Towers II
# Medium

# You are given a 0-indexed array maxHeights of n integers.
# You are tasked with building n towers in the coordinate line. The ith tower is built at coordinate i and has a height of heights[i].
# A configuration of towers is beautiful if the following conditions hold:
# 1 <= heights[i] <= maxHeights[i]
# heights is a mountain array.
# Array heights is a mountain if there exists an index i such that:
# For all 0 < j <= i, heights[j - 1] <= heights[j]
# For all i <= k < n - 1, heights[k + 1] <= heights[k]
# Return the maximum possible sum of heights of a beautiful configuration of towers.

# Example 1:
# Input: maxHeights = [5,3,4,1,1]
# Output: 13
# Explanation: One beautiful configuration with a maximum sum is heights = [5,3,3,1,1]. This configuration is beautiful since:
# - 1 <= heights[i] <= maxHeights[i]  
# - heights is a mountain of peak i = 0.
# It can be shown that there exists no other beautiful configuration with a sum of heights greater than 13.

# Example 2:
# Input: maxHeights = [6,5,3,9,2,7]
# Output: 22
# Explanation: One beautiful configuration with a maximum sum is heights = [3,3,3,9,2,2]. This configuration is beautiful since:
# - 1 <= heights[i] <= maxHeights[i]
# - heights is a mountain of peak i = 3.
# It can be shown that there exists no other beautiful configuration with a sum of heights greater than 22.

# Example 3:
# Input: maxHeights = [3,2,5,5,2,3]
# Output: 18
# Explanation: One beautiful configuration with a maximum sum is heights = [2,2,5,5,2,2]. This configuration is beautiful since:
# - 1 <= heights[i] <= maxHeights[i]
# - heights is a mountain of peak i = 2. 
# Note that, for this configuration, i = 3 can also be considered a peak.
# It can be shown that there exists no other beautiful configuration with a sum of heights greater than 18.
 
# Constraints:
# 1 <= n == maxHeights.length <= 105
# 1 <= maxHeights[i] <= 109



# sol 1

# class Solution:
#     def maximumSumOfHeights(self, maxHeights: List[int]) -> int:

#         # for each possible peek, compute maximum sum of heights;
#         # this is achieved by maintaining a monotonic stack with 
#         # heights and counts 
        
#         def find_peak(arr):

#             stack, acc = [], 0
#             peeks = []

#             for height in arr:
#                 count = 1
#                 while stack and height <= stack[-1][0]:
#                     h, c = stack.pop()
#                     acc -= h * c
#                     count += c
#                 stack.append((height, count))
#                 acc += height * count
#                 peeks.append(acc)
#             return peeks

#         # precompute sums both from both tails (forward and reverse)
#         fwd = [0] + find_peak(maxHeights)
#         rev = find_peak(maxHeights[::-1])[::-1] + [0]

#         # the answer is the maximum sum for two tails
#         return max(f + r for f, r in zip(fwd, rev))
    


# sol 2

# class Solution:
#     def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
#         n = len(maxHeights)
#         sums = [0 for _ in maxHeights]
#         stack = [-1]
#         total = 0

#         for i in range(0,n):
#             while stack[-1] != -1 and maxHeights[stack[-1]] >= maxHeights[i]:
#                 total -= (stack[-1] - stack[-2]) * maxHeights[stack[-1]]
#                 stack.pop()
#             stack.append(i)
#             total += (stack[-1] - stack[-2]) * maxHeights[stack[-1]]
#             sums[i] += total
        
#         # do the same for right side
#         stack.clear()
#         stack.append(n)
#         total = 0
#         for i in range(n-1,-1,-1):
#             while stack[-1] != n and maxHeights[stack[-1]] >= maxHeights[i]:
#                 total -= (stack[-2] - stack[-1]) * maxHeights[stack[-1]]
#                 stack.pop()
#             stack.append(i)
#             total += (stack[-2] - stack[-1]) * maxHeights[stack[-1]]
#             sums[i] += total

#         # the sums counted the top maxHeight[i] twice
#         # so we subtract it
#         for i in range(0,n):
#             sums[i] -= maxHeights[i]
            
#         return max(sums)
    


# sol 3

# class Solution:
#     def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
#         n = len(maxHeights)
#         left = [0]*n
#         leftSum = 0
#         stack = [-1]
#         for i in range(n):
#             while len(stack)>1 and maxHeights[i]<maxHeights[stack[-1]]:
#                 j = stack.pop()
#                 leftSum -= (j-stack[-1])*maxHeights[j]
#             leftSum += maxHeights[i]*(i-stack[-1])
#             stack.append(i)
#             left[i]=leftSum
#         '''
#         below is an example of what the above code does
#         it computes what the sum is if we consider
#         maxHeights[i]
#         i.e. at i=1, we consider 3 to be the peak thus we'd sum
#         3 and 3 not 5&3 otherwise it wont be monotonically increasing

#         if you understand this part then youd understand the below code
#         '''
#         # maxHeights: [5, 3, 7, -2, -1]
#         # left: [5, 6, 10, 4, 5]
        
#         right = [0]*n
#         rightSum = 0
#         stack = [n]
#         for i in range(n-1,-1,-1):
#             while len(stack)>1 and maxHeights[stack[-1]]>maxHeights[i]:
#                 j = stack.pop()
#                 rightSum -= (j-stack[-1])*maxHeights[j]
#             rightSum += maxHeights[i]*(i-stack[-1])
#             stack.append(i)
#             right[i]=-1*rightSum
#         res = 0
#         for i in range(n):
#             res = max(res, left[i]+right[i]-maxHeights[i])
#         return res

        

# sol 4

# class Solution:
#     def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
#         n = len(maxHeights)
#         stack = []
#         left = [0]*n
#         right = [0]*n

#         for i in range(n):
#             while stack and maxHeights[stack[-1]] > maxHeights[i]:
#                 stack.pop()
#             left[i] = maxHeights[i]*(i+1) if not stack else maxHeights[i]*(i-stack[-1]) + left[stack[-1]]
#             stack.append(i)
    
#         stack.clear()
#         for i in range(n-1, -1, -1):
#             while stack and maxHeights[stack[-1]] > maxHeights[i]:
#                 stack.pop()
#             right[i] = maxHeights[i]*(n-i) if not stack else maxHeights[i]*(stack[-1] - i) + right[stack[-1]]
#             stack.append(i)
        
#         return max(l + r - h for l, r, h in zip(left, right, maxHeights))