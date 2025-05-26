# 2073. Time Needed to Buy Tickets
# Easy

# There are n people in a line queuing to buy tickets, where the 0th person is at the front of the line and the (n - 1)th person is at the back of the line.
# You are given a 0-indexed integer array tickets of length n where the number of tickets that the ith person would like to buy is tickets[i].
# Each person takes exactly 1 second to buy a ticket. A person can only buy 1 ticket at a time and has to go back to the end of the line (which happens instantaneously) in order to buy more tickets. If a person does not have any tickets left to buy, the person will leave the line.
# Return the time taken for the person initially at position k (0-indexed) to finish buying tickets.

# Example 1:
# Input: tickets = [2,3,2], k = 2
# Output: 6
# Explanation:
# The queue starts as [2,3,2], where the kth person is underlined.
# After the person at the front has bought a ticket, the queue becomes [3,2,1] at 1 second.
# Continuing this process, the queue becomes [2,1,2] at 2 seconds.
# Continuing this process, the queue becomes [1,2,1] at 3 seconds.
# Continuing this process, the queue becomes [2,1] at 4 seconds. Note: the person at the front left the queue.
# Continuing this process, the queue becomes [1,1] at 5 seconds.
# Continuing this process, the queue becomes [1] at 6 seconds. The kth person has bought all their tickets, so return 6.

# Example 2:
# Input: tickets = [5,1,1,1], k = 0
# Output: 8
# Explanation:
# The queue starts as [5,1,1,1], where the kth person is underlined.
# After the person at the front has bought a ticket, the queue becomes [1,1,1,4] at 1 second.
# Continuing this process for 3 seconds, the queue becomes [4] at 4 seconds.
# Continuing this process for 4 seconds, the queue becomes [] at 8 seconds. The kth person has bought all their tickets, so return 8.

# Constraints:
# n == tickets.length
# 1 <= n <= 100
# 1 <= tickets[i] <= 100
# 0 <= k < n




# sol 1

# class Solution:
#     def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
#         total = 0

#         for i, x in enumerate(tickets):
#             if i <= k:
#                 total += min(tickets[i], tickets[k])
#             else:
#                 total += min(tickets[i], tickets[k] - 1)

#         return total
    


# sol 2

# class Solution:
#     def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
#         return sum([tickets[k] if tickets[i] > tickets[k] else tickets[i] for i in range(len(tickets)) ]) - len([1 for i in range(k + 1 , len(tickets)) if tickets[i] >= tickets[k] ])
    


# sol 3

# class Solution:
#     def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
#         s = tickets[k]
#         o = 0
#         for i in range(len(tickets)):
#             if i<=k:
#                 if tickets[i]>s:
#                     o+=s
#                 else:
#                     o+=tickets[i]
#             else:
#                 if tickets[i]>s-1:
#                     o+=s-1
#                 else:
#                     o+=tickets[i]
#         return o



# sol 4

# from collections import deque

# class Solution:
#     def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
#         q = deque()
#         time = 0

#         # Initialize queue with (index, ticket_count)
#         for i, t in enumerate(tickets):
#             q.append((i, t))

#         while q:
#             i, t = q.popleft()
#             # Simulate 1 ticket being bought
#             t -= 1
#             time += 1

#             # If this person still has tickets left, go to the back of the queue
#             if t > 0:
#                 q.append((i, t))
#             # If this is person k and they just finished, break
#             elif i == k:
#                 break

#         return time
