# 3527. Find the Most Common Response
# Medium

# You are given a 2D string array responses where each responses[i] is an array of strings representing survey responses from the ith day.
# Return the most common response across all days after removing duplicate responses within each responses[i]. If there is a tie, return the lexicographically smallest response.

# Example 1:
# Input: responses = [["good","ok","good","ok"],["ok","bad","good","ok","ok"],["good"],["bad"]]
# Output: "good"
# Explanation:
# After removing duplicates within each list, responses = [["good", "ok"], ["ok", "bad", "good"], ["good"], ["bad"]].
# "good" appears 3 times, "ok" appears 2 times, and "bad" appears 2 times.
# Return "good" because it has the highest frequency.

# Example 2:
# Input: responses = [["good","ok","good"],["ok","bad"],["bad","notsure"],["great","good"]]
# Output: "bad"
# Explanation:
# After removing duplicates within each list we have responses = [["good", "ok"], ["ok", "bad"], ["bad", "notsure"], ["great", "good"]].
# "bad", "good", and "ok" each occur 2 times.
# The output is "bad" because it is the lexicographically smallest amongst the words with the highest frequency.
 
# Constraints:
# 1 <= responses.length <= 1000
# 1 <= responses[i].length <= 1000
# 1 <= responses[i][j].length <= 10
# responses[i][j] consists of only lowercase English letters



# sol 1

# class Solution:
#     def findCommonResponse(self, responses: List[List[str]]) -> str:
#         from collections import Counter

#         # Create a Counter to count the frequency of each response
#         response_counter = Counter()

#         # Iterate through each day's responses
#         for day_responses in responses:
#             # Use set to remove duplicates and update the counter
#             unique_responses = set(day_responses)
#             response_counter.update(unique_responses)

#         # Find the most common response
#         most_common_response = min(response_counter.items(), key=lambda x: (-x[1], x[0]))

#         return most_common_response[0]
    

# sol 2

# class Solution:
#     def findCommonResponse(self, responses: list[list[str]]) -> str:
#         count = defaultdict(int)

#         for daily in responses:
#             for response in set(daily):
#                 count[response] += 1

#         max_count = max(count.values())
#         most_common = min(response for response, cnt in count.items() if cnt == max_count)

#         return most_common
    


# sol 3

# from collections import defaultdict
# class Solution:
#     def findCommonResponse(self, responses: List[List[str]]) -> str:
    
#         global_hash = {}
#         global_maximum = [0, '']
#         for response in responses:
#             local_hash = set()
#             for curr in response:
#                 if curr in local_hash:
#                     continue
#                 else:
#                     local_hash.add(curr)
#                     if curr in global_hash:
#                         global_hash[curr] += 1
#                     else:
#                         global_hash[curr] = 1
#         for key, value in global_hash.items():
#             if value < global_maximum[0]:
#                 continue
#             elif value > global_maximum[0]:
#                 global_maximum = [value, key]
#             else:
#                 if key < global_maximum[1]:
#                     global_maximum = [value, key]

                
#         return global_maximum[1]
    

# sol 5

# class Solution:
#     def findCommonResponse(self, responses: List[List[str]]) -> str:
#         score = {}
#         for ress in responses:
#             hs = set()
#             for w in ress:
#                 if w not in hs:
#                     hs.add(w)
#                     if w not in score:
#                         score[w] = 0
#                     score[w] += 1

#         maxx = 0
#         res = None
#         for w, cnt in score.items():
#             if cnt > maxx:
#                 maxx = cnt
#                 res = w
#             elif cnt == maxx and res > w:
#                 res = w

#         return res