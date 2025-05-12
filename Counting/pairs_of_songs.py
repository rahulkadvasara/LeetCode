# 1010. Pairs of Songs With Total Durations Divisible by 60
# Medium

# You are given a list of songs where the ith song has a duration of time[i] seconds.
# Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

# Example 1:
# Input: time = [30,20,150,100,40]
# Output: 3
# Explanation: Three pairs have a total duration divisible by 60:
# (time[0] = 30, time[2] = 150): total duration 180
# (time[1] = 20, time[3] = 100): total duration 120
# (time[1] = 20, time[4] = 40): total duration 60

# Example 2:
# Input: time = [60,60,60]
# Output: 3
# Explanation: All three pairs have a total duration of 120, which is divisible by 60.
 
# Constraints:
# 1 <= time.length <= 6 * 104
# 1 <= time[i] <= 500



# sol 1

# class Solution:
#     def numPairsDivisibleBy60(self, time: List[int]) -> int:
#         count = 0
#         remainder_count = [0] * 60
        
#         for t in time:
#             remainder = t % 60
#             complement = (60 - remainder) % 60
#             count += remainder_count[complement]
#             remainder_count[remainder] += 1
            
#         return count
    


# sol 2

# from collections import defaultdict
# class Solution:
#     def numPairsDivisibleBy60(self, time: List[int]) -> int:
#         d = defaultdict(int)
        
#         for i in time:
#             d[i%60] += 1
#         ans = 0
#         for i in d.keys():
#             if i == 0 or i == 30:
#                 ans += d[i] * (d[i] - 1) // 2
                
#             elif d[i] != -1 and i in d.keys() and (60 - i) in d.keys():
#                 ans += d[i] * d[60 - i]
#                 d[i] = -1
#                 d[60 - i] = -1
#         return ans