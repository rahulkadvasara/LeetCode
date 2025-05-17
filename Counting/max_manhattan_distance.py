# 3443. Maximum Manhattan Distance After K Changes
# Medium

# You are given a string s consisting of the characters 'N', 'S', 'E', and 'W', where s[i] indicates movements in an infinite grid:
# 'N' : Move north by 1 unit.
# 'S' : Move south by 1 unit.
# 'E' : Move east by 1 unit.
# 'W' : Move west by 1 unit.
# Initially, you are at the origin (0, 0). You can change at most k characters to any of the four directions.
# Find the maximum Manhattan distance from the origin that can be achieved at any time while performing the movements in order.
# The Manhattan Distance between two cells (xi, yi) and (xj, yj) is |xi - xj| + |yi - yj|.

# Example 1:
# Input: s = "NWSE", k = 1
# Output: 3
# Explanation:
# Change s[2] from 'S' to 'N'. The string s becomes "NWNE".
# Movement	Position (x, y)	Manhattan Distance	Maximum
# s[0] == 'N'	(0, 1)	0 + 1 = 1	1
# s[1] == 'W'	(-1, 1)	1 + 1 = 2	2
# s[2] == 'N'	(-1, 2)	1 + 2 = 3	3
# s[3] == 'E'	(0, 2)	0 + 2 = 2	3
# The maximum Manhattan distance from the origin that can be achieved is 3. Hence, 3 is the output.

# Example 2:
# Input: s = "NSWWEW", k = 3
# Output: 6
# Explanation:
# Change s[1] from 'S' to 'N', and s[4] from 'E' to 'W'. The string s becomes "NNWWWW".
# The maximum Manhattan distance from the origin that can be achieved is 6. Hence, 6 is the output.

# Constraints:
# 1 <= s.length <= 105
# 0 <= k <= s.length
# s consists of only 'N', 'S', 'E', and 'W'.



# sol 1

# class Solution:
#     def maxDistance(self, s: str, k: int) -> int:
#         res = 0
#         for diag in [{"N", "E"}, {"N", "W"}, {"S", "E"}, {"S", "W"}]:
#             kk, dist = k, 0
#             for ch in s:
#                 if ch in diag or kk:
#                     dist += 1
#                     kk -= ch not in diag
#                 else:
#                     dist -= 1
#                 res = max(res, dist)
#         return res
    


# sol 2

# class Solution:
#     def maxDistance(self, s: str, k: int) -> int:
#         freq = defaultdict(int)
#         ans = 0
#         dirs_sum = 0 
#         for c in s:
#             freq[c] += 1
#             dirs_sum += 1 # dirs_sum = sum(freq.values())
#             num_of_opposite_dirs = min(freq["N"], freq["S"]) + min(freq["W"], freq["E"])
#             # Current manhattan distance can be calculated by subtracting the
#             # 2 * num_of_opposite_dirs from the sum of all directions.
#             # Such direction will cancel the effect of itself
#             # and opposing direction, thus twice the reduction.
#             man_dis = dirs_sum - (2 * num_of_opposite_dirs) 
#             # Simulate changing upto min(k, num_of_opposite_dirs) directions.
#             # Such move will undo the effect done by the opposing direction.
#             man_dis += (2 * min(k, num_of_opposite_dirs))
#             ans = max(ans, man_dis)
#         return ans
    


# sol 3

# from collections import defaultdict

# # Direction mapping
# d_map = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}

# class Solution:
#     def maxDistance(self, s: str, k: int) -> int:
#         n = len(s)
#         # dp[state] = max distance for position (x, y) with 'changes' made after i steps
#         dp = {(0, 0, 0): 0}  # (x, y, changes) -> max_dist

#         for i in range(n):
#             next_dp = dict()
#             current_dir = s[i]

#             for (x, y, changes), dist in dp.items():
#                 for d in 'NSEW':
#                     dx, dy = d_map[d]
#                     new_x = x + dx
#                     new_y = y + dy
#                     new_changes = changes + (d != current_dir)

#                     if new_changes <= k:
#                         new_dist = max(dist, abs(new_x) + abs(new_y))
#                         key = (new_x, new_y, new_changes)

#                         if key not in next_dp or new_dist > next_dp[key]:
#                             next_dp[key] = new_dist

#             dp = next_dp  # move to next step

#         return max(dp.values())


# class Solution:
#     def maxDistance(self, s: str, k: int) -> int:
#         ans = 0 
#         freq = Counter()
#         for ch in s: 
#             freq[ch] += 1
#             v = min(freq['N'], freq['S'])
#             h = min(freq['E'], freq['W'])
#             if v + h <= k: cand = sum(freq.values())
#             elif v <= k: cand = freq['N'] + freq['S'] + max(freq['E'], freq['W']) + 2*(k-v) - h
#             else: cand = max(freq['N'], freq['S']) + 2*k - v + abs(freq['E'] - freq['W'])
#             ans = max(ans, cand)
#         return ans 

# class Solution:
#     def maxDistance(self, s: str, k: int) -> int:
#         ans = 0
#         x, y = 0, 0
#         for i, c in enumerate(s, 1):
#             if c == "S":
#                 y += 1
#             elif c == "N":
#                 y -= 1
#             elif c == "E":
#                 x += 1
#             elif c == "W":
#                 x -= 1
#             d = abs(x) + abs(y) + 2 * k
#             if d > i:
#                 d = i
#             if d > ans:
#                 ans = d
#         return ans
