# 3184. Count Pairs That Form a Complete Day I
# Easy

# Given an integer array hours representing times in hours, return an integer denoting the number of pairs i, j where i < j and hours[i] + hours[j] forms a complete day.
# A complete day is defined as a time duration that is an exact multiple of 24 hours.
# For example, 1 day is 24 hours, 2 days is 48 hours, 3 days is 72 hours, and so on.

# Example 1:
# Input: hours = [12,12,30,24,24]
# Output: 2
# Explanation:
# The pairs of indices that form a complete day are (0, 1) and (3, 4).

# Example 2:
# Input: hours = [72,48,24,3]
# Output: 3
# Explanation:
# The pairs of indices that form a complete day are (0, 1), (0, 2), and (1, 2).

# Constraints:
# 1 <= hours.length <= 100
# 1 <= hours[i] <= 109



# sol 1

# class Solution:
#     def countCompleteDayPairs(self, hours: List[int]) -> int:
#         count = 0
#         n = len(hours)
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if (hours[i] + hours[j]) % 24 == 0:
#                     count += 1
#         return count
    


# sol 2 

# class Solution:
#     def countCompleteDayPairs(self, hours: List[int]) -> int:
#         from collections import defaultdict
#         remainder_count = defaultdict(int)
#         count = 0
#         for hour in hours:
#             remainder = hour % 24
#             if remainder == 0:
#                 count += remainder_count[0]
#             else:
#                 count += remainder_count[24 - remainder]
#             remainder_count[remainder] += 1
#         return count
    


# sol 3

# class Solution:
#     def countCompleteDayPairs(self, hours: List[int]) -> int:
#         #variant of 2-sum problem
#         #will only store values in range 0 to 24
#         #T(N)=O(N), S(N)=O(HR)=O(24)=O(1)
#         freq_map=dict()
#         res_num_pairs=0
#         for hour in hours:
#             canonical_hour=hour%24
#             target=(24-canonical_hour)%24
#             num_pairs_for_this_hour=freq_map.get(target,0)
#             res_num_pairs+=num_pairs_for_this_hour
#             freq_map[canonical_hour]=freq_map.get(canonical_hour,0)+1
#         return res_num_pairs
            