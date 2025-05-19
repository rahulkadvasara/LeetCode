# 1475. Final Prices With a Special Discount in a Shop
# Easy

# You are given an integer array prices where prices[i] is the price of the ith item in a shop.
# There is a special discount for items in the shop. If you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i]. Otherwise, you will not receive any discount at all.
# Return an integer array answer where answer[i] is the final price you will pay for the ith item of the shop, considering the special discount.

# Example 1:
# Input: prices = [8,4,6,2,3]
# Output: [4,2,4,2,3]
# Explanation: 
# For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4.
# For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2.
# For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4.
# For items 3 and 4 you will not receive any discount at all.

# Example 2:
# Input: prices = [1,2,3,4,5]
# Output: [1,2,3,4,5]
# Explanation: In this case, for all items, you will not receive any discount at all.

# Example 3:
# Input: prices = [10,1,1,6]
# Output: [9,0,1,6]
 
# Constraints:
# 1 <= prices.length <= 500
# 1 <= prices[i] <= 1000



# sol 1

# class Solution:
#     def finalPrices(self, prices: List[int]) -> List[int]:
#         n = len(prices)
#         stack = []
#         for i in range(n):
#             while stack and prices[stack[-1]] >= prices[i]:
#                 prices[stack.pop()] -= prices[i]
#             stack.append(i)
#         return prices
    


# sol 2 

# class Solution:
#     def finalPrices(self, prices: List[int]) -> List[int]:
#         n = len(prices)
#         updated_prices = prices.copy() 

#         for i in range(n):
#             for j in range(i+1, n):
#                 if j > i and prices[i] >= prices[j]:
#                     updated_prices[i] = prices[i]-prices[j]
#                     break


#         return updated_prices
    


# sol 3

# class Solution:
#     def finalPrices(self, prices: List[int]) -> List[int]:
#         n=len(prices)
#         stack=[n-1]
#         ans=[x for x in prices]
#         for i in range(n-2, -1, -1):
#             while stack and prices[i]<prices[stack[-1]]:
#                 stack.pop()
#             if stack: ans[i]-=prices[stack[-1]]
#             stack.append(i)
#         return ans
        