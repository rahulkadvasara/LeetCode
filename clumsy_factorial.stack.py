# # 1006. Clumsy Factorial
# # Medium

# # The factorial of a positive integer n is the product of all positive integers less than or equal to n.
# # For example, factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1.
# # We make a clumsy factorial using the integers in decreasing order by swapping out the multiply operations for a fixed rotation of operations with multiply '*', divide '/', add '+', and subtract '-' in this order.
# # For example, clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1.
# # However, these operations are still applied using the usual order of operations of arithmetic. We do all multiplication and division steps before any addition or subtraction steps, and multiplication and division steps are processed left to right.
# # Additionally, the division that we use is floor division such that 10 * 9 / 8 = 90 / 8 = 11.
# # Given an integer n, return the clumsy factorial of n.

# # Example 1:
# # Input: n = 4
# # Output: 7
# # Explanation: 7 = 4 * 3 / 2 + 1

# # Example 2:
# # Input: n = 10
# # Output: 12
# # Explanation: 12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1

# # Constraints:
# # 1 <= n <= 104



# # sol 1

# # class Solution:
# #     def clumsy(self, n: int) -> int:
# #         stack = [n]
        
# #         turn = 0
# #         # multiplicaiton and division
# #         for num in range(n-1, 0, -1):
# #             if turn % 4 == 0:
# #                 num1 = stack.pop()
# #                 stack.append(num1*num)
# #             elif turn % 4 == 1:
# #                 num1 = stack.pop()
# #                 stack.append(num1//num)
# #             else:
# #                 stack.append(num)
# #             turn += 1
            
# #         # addition and substraction
# #         turn = 0
# #         for i in range(1, len(stack)):
# #             if turn % 2 == 0:
# #                 stack[i] += stack[i-1]
# #             else:
# #                 stack[i] = stack[i-1]-stack[i]
# #             turn += 1
                
# #         return stack[-1]
    


# # sol 2

# # class Solution:
# #     def clumsy(self, n: int) -> int:
# #         res = "" + str(n)
# #         curr_op = 1

# #         for i in range(n - 1, 0, -1):
# #             i = str(i)
# #             if curr_op == 1:
# #                 res += "*" + i
# #                 curr_op += 1
# #             elif curr_op == 2:
# #                 res += "//" + i
# #                 curr_op += 1
# #             elif curr_op == 3:
# #                 res += "+" + i
# #                 curr_op += 1
# #             else:
# #                 res += "-" + i
# #                 curr_op = 1

# #         res = eval(res)
# #         return res
    

# # sol 3

# # class Solution:
# #     def clumsy(self, N: int) -> int:
# #     	return N + ([1,2,2,-1][N % 4] if N > 4 else [0,0,0,3,3][N])


# # sol 4

# # class Solution:
# #     def clumsy(self, N: int) -> int:
# #     	return eval(str(N)+''.join([['*','//','+','-'][(N-i-1)%4]+str(i) for i in range(N-1,0,-1)]))
		

# # sol 5

# # class Solution:
# #     def clumsy(self, N: int) -> int:
# #     	a, n, b = 0, N, N >= 4
# #     	if b: a, n = n*(n-1)//(n-2)+(n-3), n - 4
# #     	while n >= 4: a, n = a - n*(n-1)//(n-2)+(n-3), n - 4
# #     	return a + [0,-1,-2,-6][n]*(2*b-1)
		


# # sol 6

# class Solution:
#     def clumsy(self, n: int) -> int:
#         def apply_group(start):
#             res = start
#             if start - 1 > 0:
#                 res *= start - 1
#             if start - 2 > 0:
#                 res //= start - 2
#             return res

#         result = 0
#         first = True
#         while n > 0:
#             if first:
#                 res = apply_group(n)
#                 if n - 3 > 0:
#                     res += n - 3
#                 result += res
#                 first = False
#             else:
#                 res = apply_group(n)
#                 if n - 3 > 0:
#                     res -= n - 3
#                 result -= res
#             n -= 4
#         return result



# sol 7


# class Solution:
#     def clumsy(self, n: int) -> int:
#         res = 0
#         curr_op = 1  # 1: *, 2: //, 3: +, 4: -
#         temp = n     # start with first number
#         first = True

#         for i in range(n - 1, 0, -1):
#             if curr_op == 1:
#                 temp *= i
#                 curr_op += 1
#             elif curr_op == 2:
#                 temp //= i
#                 curr_op += 1
#             elif curr_op == 3:
#                 if first:
#                     res += temp + i
#                     first = False
#                 else:
#                     res -= temp
#                     res += i
#                 curr_op += 1
#                 temp = 0
#             else:  # curr_op == 4
#                 temp = i
#                 curr_op = 1

#         # If loop ends with temp not added
#         if curr_op == 1 or curr_op == 2:
#             if first:
#                 res += temp
#             else:
#                 res -= temp
#         elif curr_op == 4:
#             res -= temp

#         return res



# sol 8

# class Solution:
#     def clumsy(self, n: int) -> int:
#         if n==4:
#             return 7
#         if n==1:
#             return 1
#         if n==2:
#             return 2
#         if n%4==0:
#             return n+1
#         if n==3:
#             return 6
#         if n%4==3:
#             return n-1
        

#         return n+2
    


# sol 9

# class Solution:
#     def clumsy(self, n: int) -> int:
#         count_operations = n // 4
#         res = 0
#         for i in range(count_operations):
#             if i == 0:
#                 res += ((n * (n-1))//(n-2)) + n-3
#             else:
#                 res -= ((n * (n - 1)) // (n - 2)) - (n - 3)
#             n -= 4

#         if n  != 0:
#             dop = 0
#             for i in range(n % 4):
#                 if i == 0:
#                     dop += n
#                     n -= 1
#                 elif i == 1:
#                     dop *= n
#                     n -= 1
#                 elif i == 2:
#                     dop //= n
#                     n -= 1
#             if count_operations == 0:
#                 res += dop
#             else:
#                 res -= dop
#         return int(res)



# sol 10

# class Solution:
#     def clumsy(self, n: int) -> int:
#         if n == 1: return 1
#         if n == 2: return 2
#         if n == 3: return 6

#         op = 0
#         result = n * (n - 1) // (n - 2)

#         for i in range(n - 3, 0, -4):
#             result += i

#         for i in range(n - 4, 0, -4):
#             if i == 2:
#                 result -= 2
#             elif i == 1:
#                 result -= 1
#             else:
#                 result -= i * (i - 1) // (i - 2)

#         return result
    


# sol 11

# class Solution(object):
#     def clumsy(self, n):
#        if n == 1:
#             return 1
#        elif n == 2:
#             return 2
#        elif n == 3:
#             return 6
#        elif n == 4:
#             return 7
#        else:
#             if n % 4 == 0:
#                 return n + 1
#             elif n % 4 <= 2:
#                 return n + 2
#             else:
#                 return n - 1
            

# sol 12

# class Solution:
#     def clumsy(self, n: int) -> int:
#         if n==4:
#             return 7
#         elif n==1:
#             return 1
#         elif n==2:
#             return 2
#         elif n==3:
#             return 6
#         if n%4==0:
#             return (n+1)
#         elif n%4==1:
#             return (n+2)
#         elif n%4==2:
#             return (n+2)
#         else:
#             return (n-1)
    