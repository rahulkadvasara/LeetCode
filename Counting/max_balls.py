# 1742. Maximum Number of Balls in a Box
# Easy

# You are working in a ball factory where you have n balls numbered from lowLimit up to highLimit inclusive (i.e., n == highLimit - lowLimit + 1), and an infinite number of boxes numbered from 1 to infinity.
# Your job at this factory is to put each ball in the box with a number equal to the sum of digits of the ball's number. For example, the ball number 321 will be put in the box number 3 + 2 + 1 = 6 and the ball number 10 will be put in the box number 1 + 0 = 1.
# Given two integers lowLimit and highLimit, return the number of balls in the box with the most balls.

# Example 1:
# Input: lowLimit = 1, highLimit = 10
# Output: 2
# Explanation:
# Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
# Ball Count:  2 1 1 1 1 1 1 1 1 0  0  ...
# Box 1 has the most number of balls with 2 balls.

# Example 2:
# Input: lowLimit = 5, highLimit = 15
# Output: 2
# Explanation:
# Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
# Ball Count:  1 1 1 1 2 2 1 1 1 0  0  ...
# Boxes 5 and 6 have the most number of balls with 2 balls in each.

# Example 3:
# Input: lowLimit = 19, highLimit = 28
# Output: 2
# Explanation:
# Box Number:  1 2 3 4 5 6 7 8 9 10 11 12 ...
# Ball Count:  0 1 1 1 1 1 1 1 1 2  0  0  ...
# Box 10 has the most number of balls with 2 balls.

# Constraints:
# 1 <= lowLimit <= highLimit <= 105



# sol 1 

# class Solution:
#     def countBalls(self, lowLimit: int, highLimit: int) -> int:
#         box = [0] * 37
#         for i in range(lowLimit, highLimit + 1):
#             box[sum(map(int, str(i)))] += 1
#         return max(box)
    

# sol 2

# class Solution:
#     def countBalls(self, lowLimit: int, highLimit: int) -> int:
#         freq = defaultdict(int)
#         for x in range(lowLimit, highLimit+1):
#             freq[sum(int(xx) for xx in str(x))] += 1
#         return max(freq.values())
    

# sol 3

# class Solution:
#     """
#         map{box_number: ball_count}
#     """
#     def countBalls(self, lowLimit: int, highLimit: int) -> int:
#         boxNumber2Cnt = {}
#         maxBall = 0
#         for i in range(lowLimit, highLimit + 1):
#             boxNumber = self.sumOfNumChar(i)
#             boxNumber2Cnt[boxNumber] = boxNumber2Cnt.get(boxNumber, 0) + 1
#             maxBall = max(maxBall, boxNumber2Cnt[boxNumber])
#         return maxBall
#     def sumOfNumChar(self, num: int) -> int:
#         ans = 0
#         while num != 0:
#             ans += num % 10
#             num = num // 10
#         return ans
    


# sol 4

# class Solution:
#     def countBalls(self, lowLimit: int, highLimit: int) -> int:
#         h = defaultdict(int)
        
#         # find the first box number
#         s = 0
#         temp = lowLimit
#         while temp > 0:
#             s += temp % 10
#             temp = temp // 10
#         h[s] += 1
        
#         x = lowLimit + 1
#         while x <= highLimit:
#             # check rightmost digit
#             if 1 <= x % 10 <= 9:
#                 s = s+1
#             else:
#                 s = s - 8
#                 temp = x // 10
#                 while temp > 0 and temp % 10 == 0:
#                     s -= 9
#                     temp = temp // 10
                    
#             h[s] += 1
#             x += 1
#         return max(h.values())
    


# sol 5

# class Solution:
#     def countBalls(self, lowLimit: int, highLimit: int) -> int:
#         @cache
#         def dfs(i: int, limit_low: bool, limit_high: bool) -> dict[int, int]:
#             if i == n:
#                 return {0: 1}
#             cnt = defaultdict(int)
#             low = int(ll[i]) if limit_low else 0
#             high = int(hl[i]) if limit_high else 9
#             for d in range(low, high + 1):
#                 for s, c in dfs(i + 1, limit_low and d == low, limit_high and d == high).items():
#                     cnt[s + d] += c
#             return cnt

#         hl = str(highLimit)
#         n = len(hl)
#         ll = str(lowLimit).zfill(n)
#         return max(dfs(0, True, True).values())