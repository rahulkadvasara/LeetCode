# 1394. Find Lucky Integer in an Array
# Easy

# Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.
# Return the largest lucky integer in the array. If there is no lucky integer return -1.

# Example 1:
# Input: arr = [2,2,3,4]
# Output: 2
# Explanation: The only lucky number in the array is 2 because frequency[2] == 2.

# Example 2:
# Input: arr = [1,2,2,3,3,3]
# Output: 3
# Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.

# Example 3:
# Input: arr = [2,2,2,3,3]
# Output: -1
# Explanation: There are no lucky numbers in the array.

# Constraints:
# 1 <= arr.length <= 500
# 1 <= arr[i] <= 500



# sol 1

# class Solution:
#     def findLucky(self, arr: List[int]) -> int:
#         count = Counter(arr)
#         lucky_numbers = [num for num, freq in count.items() if num == freq]
#         return max(lucky_numbers) if lucky_numbers else -1
    

# sol 2

# class Solution:
#     def findLucky(self, arr: List[int]) -> int:
        
#         # edge case
#         # if the array length is and element is 1 then return 1
#         if len(arr) == 1 and arr[0] == 1:
#             return 1

#         result = []
        
#         arr.sort()
#         cur_elem = arr[0]
#         count = 1

#         # flag to check if the final element needs to be added into the list
#         flag = False

#         n = len(arr)


#         for right in range(1,n):

#             if arr[right] == cur_elem:
#                 count += 1
#                 flag = True
                
#             else:
#                 if cur_elem == count:
#                     result.append(cur_elem)

#                 cur_elem = arr[right]
#                 count = 1
                
#                 flag = False
        
#         # check if the last element count is equal to the value of element
#         if flag and cur_elem == count:
#             result.append(cur_elem)

#         # return the max of values if the list is not empty else -1
#         return max(result) if result else -1
        


# sol 3

# class Solution(object):
#     def findLucky(self, arr):
#         x = Counter(arr)
#         high = -1
#         for item, value in x.items():
#             if item == value:
#                 high = max(value, high)
#         return high