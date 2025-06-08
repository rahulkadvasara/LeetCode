# 1106. Parsing A Boolean Expression
# Hard

# A boolean expression is an expression that evaluates to either true or false. It can be in one of the following shapes:
# 't' that evaluates to true.
# 'f' that evaluates to false.
# '!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
# '&(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical AND of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
# '|(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical OR of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
# Given a string expression that represents a boolean expression, return the evaluation of that expression.
# It is guaranteed that the given expression is valid and follows the given rules.

# Example 1:
# Input: expression = "&(|(f))"
# Output: false
# Explanation: 
# First, evaluate |(f) --> f. The expression is now "&(f)".
# Then, evaluate &(f) --> f. The expression is now "f".
# Finally, return false.

# Example 2:
# Input: expression = "|(f,f,f,t)"
# Output: true
# Explanation: The evaluation of (false OR false OR false OR true) is true.

# Example 3:
# Input: expression = "!(&(f,t))"
# Output: true
# Explanation: 
# First, evaluate &(f,t) --> (false AND true) --> false --> f. The expression is now "!(f)".
# Then, evaluate !(f) --> NOT false --> true. We return true.

# Constraints:
# 1 <= expression.length <= 2 * 104
# expression[i] is one following characters: '(', ')', '&', '|', '!', 't', 'f', and ','.




# sol 1

# class Solution:
#     def parseBoolExpr(self, expression: str) -> bool:
#         st = deque()
#         for c in expression:
#             if c == "," or c == "(":
#                 continue
#             if c in ["t", "f", "!", "&", "|"]:
#                 st.append(c)
#             elif c == ")":
#                 has_true = False
#                 has_false = False
#                 while st[-1] not in ["!", "&", "|"]:
#                     top_value = st.pop()
#                     if top_value == "t":
#                         has_true = True
#                     elif top_value == "f":
#                         has_false = True
#                 op = st.pop()
#                 if op == "!":
#                     st.append("t" if not has_true else "f")
#                 elif op == "&":
#                     st.append("f" if has_false else "t")
#                 else:
#                     st.append("t" if has_true else "f")
#         return st[-1] == "t"
    


# sol 2 

# class Solution:
#     def parseBoolExpr(self, expression: str) -> bool:
#         def f(i, j):
#             if i == j:
#                 if expression[i] == 't': return True
#                 return False

#             op = expression[i]

#             if op == '!':
#                 return not f(i+2, j-1)

#             elif op == '&':
#                 ans = True
#             elif op == '|':
#                 ans = False

#             start = i+2
#             paren = 0

#             for end in range(i+2, j+1) :
#                 if expression[end] == ',' or end == j:
#                     if paren == 0:
#                         if op == '|':
#                             ans = ans or f(start, end-1)
#                             if ans:
#                                 return True

#                         elif op == '&':
#                             ans = ans and f(start, end-1)
#                             if not ans:
#                                 return False
                                
#                         start = end+1

#                 elif expression[end] == '(':
#                     paren += 1

#                 elif expression[end] == ')':
#                     paren -= 1

#             return ans

#         n = len(expression)
#         return f(0, n-1)
    


# sol 3

# class Solution:
#     def parseBoolExpr(self, expression: str) -> bool:
#         ret = expression
#         while len(ret) > 1:
#             last_open = ret.rfind('(')
#             first_close = ret.find(')', last_open)
#             op = last_open - 1
#             v = ret[last_open:first_close+1]
#             if ret[op] == '!':
#                 ret = ret.replace(ret[op] + v, nope(v[1]))
#             elif ret[op] == '&':
#                 ret = ret.replace(ret[op] + v, amp(v))
#             elif ret[op] == '|':
#                 ret = ret.replace(ret[op]+v, bar(v))
#         return False if ret == 'f' else True


# def nope(v):
#     if v == 'f':
#         return 't'
#     else:
#         return 'f'

# def amp(v):
#     if 'f' in v:
#         return 'f'
#     else:
#         return 't'

# def bar(v):
#     if 't' in v:
#         return 't'
#     else:
#         return 'f'
    

# sol 3

# class Solution:
#     def _evaluate(self, op, values):
#         if op == '!':
#             return not values[0]
#         elif op == '&':
#             return all(values)
#         elif op == '|':
#             return any(values)

#     def _parse(self, expression, i=0):
#         stack = []
#         while i < len(expression):
#             c = expression[i]
#             if c == 't':
#                 stack.append(True)
#             elif c == 'f':
#                 stack.append(False)
#             elif c in '!&|':
#                 res, i = self._parse(expression, i + 2)
#                 boolean = self._evaluate(c, res)
#                 stack.append(boolean)
#             elif c == ')':
#                 break
#             i += 1
#         return stack, i

#     def parseBoolExpr(self, expression: str) -> bool:
#         return self._parse(expression)[0][0]
    


# sol 4

# class Solution:
#     def _evaluate(self, op, values):
#         if op == '!':
#             return not values[0]
#         elif op == '&':
#             return all(values)
#         elif op == '|':
#             return any(values)

#     def _parse(self, expression, i=0):
#         stack = []
#         while i < len(expression):
#             c = expression[i]
#             if c == 't':
#                 stack.append(True)
#             elif c == 'f':
#                 stack.append(False)
#             elif c in '!&|':
#                 res, i = self._parse(expression, i + 2)
#                 boolean = self._evaluate(c, res)
#                 stack.append(boolean)
#             elif c == ')':
#                 break
#             i += 1
#         return stack, i

#     def parseBoolExpr(self, expression: str) -> bool:
#         return self._parse(expression)[0][0]