# 3238. Find the Number of Winning Players
# Easy

# You are given an integer n representing the number of players in a game and a 2D array pick where pick[i] = [xi, yi] represents that the player xi picked a ball of color yi.
# Player i wins the game if they pick strictly more than i balls of the same color. In other words,
# Player 0 wins if they pick any ball.
# Player 1 wins if they pick at least two balls of the same color.
# ...
# Player i wins if they pick at leasti + 1 balls of the same color.
# Return the number of players who win the game.
# Note that multiple players can win the game.

# Example 1:
# Input: n = 4, pick = [[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]]
# Output: 2
# Explanation:
# Player 0 and player 1 win the game, while players 2 and 3 do not win.

# Example 2:
# Input: n = 5, pick = [[1,1],[1,2],[1,3],[1,4]]
# Output: 0
# Explanation:
# No player wins the game.

# Example 3:
# Input: n = 5, pick = [[1,1],[2,4],[2,4],[2,4]]
# Output: 1
# Explanation:
# Player 2 wins the game by picking 3 balls with color 4.

# Constraints:
# 2 <= n <= 10
# 1 <= pick.length <= 100
# pick[i].length == 2
# 0 <= xi <= n - 1 
# 0 <= yi <= 10



# sol 1 

# class Solution:
#     def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
#         ctr = Counter(map(tuple,pick))
#         return len({player for (player,_), count in ctr.items() if count > player})
    


# sol 2

# from typing import List

# class Solution:
#     def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
#         # Step 1: Create a 2D list to count colors picked by each player
#         color_counts = [[0] * 11 for _ in range(n)]

#         # Step 2: Update the color counts based on the picks
#         for player, color in pick:
#             color_counts[player][color] += 1

#         # Step 3: Count the number of winning players
#         count = 0
#         for i in range(n):
#             if any(val > i for val in color_counts[i]):
#                 count += 1

#         return count
    


# sol 3

# class Solution:
#     def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
#         #pick[i] = [xi, yi]
#         # set output = 0
#         # if the player is zero then increment output by 1 everytime we stumble across player 0
#         # for each player keep a note of the player(xi value) and the color(yi value) they choose
#         # Continue going on through the array until the very end
#         # if the player gets the same yi value then increment output by 1
#         # return output
#         counts = [{} for _ in range(n)]
        
#         for xi, yi in pick:
#             if yi not in counts[xi]:
#                 counts[xi][yi] = 0
#             counts[xi][yi] += 1
        
#         output = 0
        
#         for i in range(n):
#             for color_count in counts[i].values():
#                 if color_count > i:
#                     output += 1
#                     break  
#         return output