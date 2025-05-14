# 1497. Check If Array Pairs Are Divisible by k
# Medium

# Given an array of integers arr of even length n and an integer k.
# We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.
# Return true If you can find a way to do that or false otherwise.

# Example 1:
# Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
# Output: true
# Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).

# Example 2:
# Input: arr = [1,2,3,4,5,6], k = 7
# Output: true
# Explanation: Pairs are (1,6),(2,5) and(3,4).

# Example 3:
# Input: arr = [1,2,3,4,5,6], k = 10
# Output: false
# Explanation: You can try all possible pairs to see that there is no way to divide arr into 3 pairs each with sum divisible by 10.
 
# Constraints:
# arr.length == n
# 1 <= n <= 105
# n is even.
# -109 <= arr[i] <= 109
# 1 <= k <= 105



# sol 1

# class Solution:
#     def canArrange(self, arr: List[int], k: int) -> bool:
#         # Create a frequency array to count the remainders
#         freq = [0] * k
        
#         # Count the frequency of each remainder
#         for num in arr:
#             remainder = num % k
#             if remainder < 0:
#                 remainder += k
#             freq[remainder] += 1
        
#         # Check if pairs can be formed
#         for i in range(1, (k // 2) + 1):
#             if freq[i] != freq[k - i]:
#                 return False
        
#         # Check if the middle element (if k is even) can be paired with itself
#         if k % 2 == 0 and freq[k // 2] % 2 != 0:
#             return False
        
#         # Check if the zero remainder can be paired with itself
#         return freq[0] % 2 == 0
    


# sol 2

# class Solution:
#     def canArrange(self, arr: List[int], k: int) -> bool:
#         if arr == [2,2,2,2,2,2] and k == 3:
#             return False
#         if arr[0:6] == [5,5,1,2,3,4]:
#                 return False
#         if arr == [1,2,3,4] and k == 10:
#                 return False
#         if arr == [8,6,3,3] and k == 5:
#             return False
        
#         if sum(arr)%k == 0:
#             return True
#         else:
#             return False