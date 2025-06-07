# 2550. Count Collisions of Monkeys on a Polygon
# Medium

# There is a regular convex polygon with n vertices. The vertices are labeled from 0 to n - 1 in a clockwise direction, and each vertex has exactly one monkey. The following figure shows a convex polygon of 6 vertices.
# Simultaneously, each monkey moves to a neighboring vertex. A collision happens if at least two monkeys reside on the same vertex after the movement or intersect on an edge.
# Return the number of ways the monkeys can move so that at least one collision happens. Since the answer may be very large, return it modulo 109 + 7.

# Example 1:
# Input: n = 3
# Output: 6
# Explanation:
# There are 8 total possible movements.
# Two ways such that they collide at some point are:
# Monkey 1 moves in a clockwise direction; monkey 2 moves in an anticlockwise direction; monkey 3 moves in a clockwise direction. Monkeys 1 and 2 collide.
# Monkey 1 moves in an anticlockwise direction; monkey 2 moves in an anticlockwise direction; monkey 3 moves in a clockwise direction. Monkeys 1 and 3 collide.

# Example 2:
# Input: n = 4
# Output: 14

# Constraints:
# 3 <= n <= 109




# sol 1 

# class Solution:
#     def monkeyMove(self, n: int) -> int:
#         modulo = 1_000_000_007
#         answer = 1
#         exponent = 2
#         while n:
#             if n&1:
#                 answer *= exponent                
#             exponent = (exponent*exponent) % modulo
#             n >>= 1
#         answer += modulo - 2
#         answer %= modulo      
#         return answer
    


# sol 2 

# class Solution:
#     def monkeyMove(self, n: int) -> int:
#         n=bin(n)[2:] #convert n to bin
#         n=n[::-1] 
#         y,a=1,2
#         m=(10**9)+7
#         for i in n:
#             if i=='1':
#                 y=(y*a)%m # Multiplying
#             a=(a*a)%m #Squaring
#         return (y-2)%m        
    


# sol 3 

# class Solution:
#     def monkeyMove(self, n: int) -> int:
#         return (pow(2, n , pow(10, 9) + 7) - 2) % (pow(10, 9) + 7)
    


# sol 4 

# class Solution:
#     def monkeyMove(self, n: int) -> int:
#         Mod = 10**9 + 7
#         def power_of_two(k):
#             if k == 0:
#                 return 1
#             half = power_of_two(k//2)
#             result = (half*half) % Mod
#             if k % 2 != 0:
#                 result = (result * 2) % Mod
#             return result
#         total_ways = power_of_two(n)

#         return (total_ways - 2) % Mod         

        