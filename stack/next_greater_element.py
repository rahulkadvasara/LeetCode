# 496. Next Greater Element I
# Easy

# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

# Example 1:
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
# - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

# Example 2:
# Input: nums1 = [2,4], nums2 = [1,2,3,4]
# Output: [3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
# - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
 
# Constraints:
# 1 <= nums1.length <= nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 104
# All integers in nums1 and nums2 are unique.
# All the integers of nums1 also appear in nums2.
 
# Follow up: Could you find an O(nums1.length + nums2.length) solution?




# sol 1 

# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         stack = []
#         res = {}
#         for i in range(len(nums2)):
#             while stack and stack[-1] < nums2[i]:
#                 res[stack.pop()] = nums2[i]
#             stack.append(nums2[i])
#         return [res.get(i, -1) for i in nums1]
    


# sol 2

# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         n2res = {}
#         stk = []
#         for n in nums2:
#             while stk and n > stk[-1]:
#                 n2res[stk.pop()] = n
            
#             stk.append(n)
#         res = []
#         for n in nums1:
#             res.append(n2res.get(n, -1))
#         return res 



# sol 3

# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         n2 = len(nums2)
#         ans = [-1] * n2       # Stores next greater element for each index in nums2
#         stack = []

#         # Step 1: Precompute next greater elements for nums2
#         for i in range(n2 - 1, -1, -1):  # Traverse from right to left
#             # Pop elements from the stack smaller than or equal to current
#             while stack and nums2[i] > stack[-1]:
#                 stack.pop()
#             # Top of the stack is the next greater element
#             if stack:
#                 ans[i] = stack[-1]
#             # Push current element to stack
#             stack.append(nums2[i])

#         # Step 2: Create the result for nums1 using precomputed values
#         res = []
#         for num in nums1:
#             for j in range(n2):
#                 if nums2[j] == num:
#                     res.append(ans[j])  # Get the precomputed next greater
#                     break

#         return res