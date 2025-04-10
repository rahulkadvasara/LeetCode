# 1089. Duplicate Zeros
# Easy

# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
# Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

# Example 1:
# Input: arr = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

# Example 2:
# Input: arr = [1,2,3]
# Output: [1,2,3]
# Explanation: After calling your function, the input array is modified to: [1,2,3]
 
# Constraints:
# 1 <= arr.length <= 104
# 0 <= arr[i] <= 9



# sol 1

# class Solution:
#     def duplicateZeros(self, arr: List[int]) -> None:
#         zeroes = arr.count(0)
#         n = len(arr)
#         for i in range(n-1, -1, -1):
#             if i + zeroes < n:
#                 arr[i + zeroes] = arr[i]
#             if arr[i] == 0: 
#                 zeroes -= 1
#                 if i + zeroes < n:
#                     arr[i + zeroes] = 0


# sol 2

# class Solution:
#     def duplicateZeros(self, arr) -> None:
#         """
#         Do not return anything, modify arr in-place instead.
#         """
#         len_lst = len(arr)
#         new_lst = []
#         for i in arr:
#             if i == 0:
#                 new_lst.append(0)
#             new_lst.append(i)


#         arr.clear()
#         arr.extend(new_lst[:len_lst])
            
        

# sol 3

# class Solution:
#     def duplicateZeros(self, arr: List[int]) -> None:
#         """
#         Do not return anything, modify arr in-place instead.

#         """
#         n=len(arr)
#         i=0
#         while i<n:
#             if arr[i]==0:
#                 arr.insert(i+1,0)
#                 i+=2
#             else:
#                 i+=1
#         arr[:]=arr[:n]



# sol 4

# class Solution:
#     def duplicateZeros(self, arr: List[int]) -> None:
#         """
#         Do not return anything, modify arr in-place instead.
#         """
#         n = len(arr)
#         count = 0
#         for i in range(n):
#             if arr[i] == 0:
#                 count += 1
#         for i in range(n-1, -1, -1):
#             if i + count < n:
#                 arr[i + count] = arr[i]
#             if arr[i] == 0:
#                 count -= 1
#                 if i + count < n:
#                     arr[i + count] = 0