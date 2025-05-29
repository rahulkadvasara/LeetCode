# 649. Dota2 Senate
# Medium

# In the world of Dota2, there are two parties: the Radiant and the Dire.
# The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:
# Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
# Announce the victory: If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.
# Given a string senate representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party. Then if there are n senators, the size of the given string will be n.
# The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.
# Suppose every senator is smart enough and will play the best strategy for his own party. Predict which party will finally announce the victory and change the Dota2 game. The output should be "Radiant" or "Dire".

# Example 1:
# Input: senate = "RD"
# Output: "Radiant"
# Explanation: 
# The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
# And the second senator can't exercise any rights anymore since his right has been banned. 
# And in round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.

# Example 2:
# Input: senate = "RDD"
# Output: "Dire"
# Explanation: 
# The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
# And the second senator can't exercise any rights anymore since his right has been banned. 
# And the third senator comes from Dire and he can ban the first senator's right in round 1. 
# And in round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.
 
# Constraints:
# n == senate.length
# 1 <= n <= 104
# senate[i] is either 'R' or 'D'.



# sol 1 

# class Solution:
#     def predictPartyVictory(self, senate: str) -> str:
#         r=[]
#         d=[]
#         for i,s in enumerate(senate):
#             if s=='R':
#                 r.append(i)
#             else:
#                 d.append(i)
        
#         while r and d:
#             if r[0]<d[0]:
#                 r.append(r.pop(0)+len(senate))
#                 d.pop(0)
#             else:
#                 d.append(d.pop(0)+len(senate))
#                 r.pop(0)
        
#         return "Radiant" if r else "Dire"
    


# sol 2

# __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
# class Solution:
#     def predictPartyVictory(self, senate: str) -> str:
#         r,d=deque(),deque()
#         for i in range(len(senate)):
#             if senate[i]=='R': r.append(i)
#             else: d.append(i)
#         while r and d:
#             rv,dv=r.popleft(),d.popleft()
#             if rv<dv: r.append(rv+len(senate))
#             else: d.append(dv+len(senate))
#         return "Radiant" if r else "Dire"
    


# sol 3

# class Solution:
#     def __init__(self):
#         self.num_r_silenced = 0
#         self.num_d_silenced = 0
#     def predictPartyVictory(self, senate: str) -> str:
#         if len(set([char for char in senate])) == 1:
#             return "Radiant" if senate[0] == "R" else "Dire"
#         remaining_party = ""
#         for member in senate:
#             if member == "R":
#                 if self.num_r_silenced == 0:
#                     self.num_d_silenced += 1
#                     remaining_party += "R"
#                 else:
#                     self.num_r_silenced -= 1
#             else:
#                 if self.num_d_silenced == 0:
#                     self.num_r_silenced += 1
#                     remaining_party += "D"
#                 else:
#                     self.num_d_silenced -= 1
        
#         return self.predictPartyVictory(remaining_party) 
    


# sol 4

# class Solution:
#     def predictPartyVictory(self, senate: str) -> str:
#         senates = list(senate)
#         counter = Counter(senates)
#         baned_count = {'R':0, 'D':0}
#         need_ban = {'R':0, 'D':0}
#         while baned_count['R'] < counter['R'] and baned_count['D'] < counter['D']:
#             for i in range(len(senates)):
#                 s = senates[i]
#                 if s.islower(): continue
#                 if baned_count['R'] == counter['R']: return 'Dire'
#                 if baned_count['D'] == counter['D']: return 'Radiant'

#                 if need_ban[s] > 0:
#                     need_ban[s] -= 1
#                     senates[i] = s.lower()
#                 else:
#                   b = 'R' if s == 'D' else 'D'
#                   baned_count[b] += 1
#                   need_ban[b] += 1

#         return 'Radiant' if baned_count['D'] == counter['D'] else 'Dire'