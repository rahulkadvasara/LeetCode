# 19. Remove Nth Node From End of List
# Medium

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:
# Input: head = [1], n = 1
# Output: []

# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]

# Constraints:
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next


# sol 1

# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         dummy = ListNode(0)
#         dummy.next = head
#         first = dummy
#         second = dummy
#         for i in range(1, n+2):
#             first = first.next
#         while first:
#             first = first.next
#             second = second.next
#         second.next = second.next.next
#         return dummy.next



# sol 2

# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         dummy = ListNode(0)
#         dummy.next = head
#         length = 0
#         first = head
#         while first:
#             length += 1
#             first = first.next
#         length -= n
#         first = dummy
#         while length > 0:
#             length -= 1
#             first = first.next
#         first.next = first.next.next
#         return dummy.next