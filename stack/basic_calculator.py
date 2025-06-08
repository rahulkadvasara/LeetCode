# 224. Basic Calculator
# Hard

# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

# Example 1:
# Input: s = "1 + 1"
# Output: 2

# Example 2:
# Input: s = " 2-1 + 2 "
# Output: 3

# Example 3:
# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23

# Constraints:
# 1 <= s.length <= 3 * 105
# s consists of digits, '+', '-', '(', ')', and ' '.
# s represents a valid expression.
# '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
# '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
# There will be no two consecutive operators in the input.
# Every number and running calculation will fit in a signed 32-bit integer.



# sol 1 

# class Solution:
#     def calculate(self, s: str) -> int:
#         stack = []
#         result = 0
#         num = 0
#         sign = 1  # 1: pos / -1 neg  
#         i = 0
#         while i < len(s):
#             ch = s[i]
#             if ch.isdigit():
#                 num = num * 10 + int(ch)
#             elif ch == '+' or ch == '-':
#                 result += sign * num
#                 num = 0
#                 sign = 1 if ch == '+' else -1
#             elif ch == '(':
#                 stack.append(result)
#                 stack.append(sign)
#                 result = 0
#                 sign = 1
#             elif ch == ')':
#                 result += sign * num
#                 num = 0
#                 prevSign = stack.pop()
#                 prevRes = stack.pop()
#                 result = prevRes + prevSign * result
#             i += 1  
#         if num:
#             result += sign * num
#         return result
    



# sol 2 

# class Solution:
#   def calculate(self, s: str) -> int:
#     ans = 0
#     num = 0
#     sign = 1
#     stack = [sign] 
#     for c in s:
#       if c.isdigit():
#         num = num * 10 + int(c)
#       elif c == '(':
#         stack.append(sign)
#       elif c == ')':
#         stack.pop()
#       elif c == '+' or c == '-':
#         ans += sign * num
#         sign = (1 if c == '+' else -1) * stack[-1]
#         num = 0
#     return ans + sign * num
  


# sol 2

# class Solution:
#     def calculate(self, s: str) -> int:
#         return (s:=f'({s.replace(" ","")})',all('(' in (s:=re.sub(r'\([^()]+\)',lambda m:str(sum(map(int,findall(r'[+-]?\d+',m[0])))),s).replace('--','+')) for _ in s)) and int(s)
    

# sol 3 

# class Solution:
#     def calculate(self, s: str) -> int:
#         s = f'({s.replace(" ", "")})'
#         f = lambda m: str(sum(map(int, findall(r'[+-]?\d+', m[0]))))
#         while '(' in s:
#             s = re.sub(r'\([^()]+\)', f, s).replace('--', '+')

#         return int(s)
    


# sol 4 

# class Solution:
#     precedence_stack = {
#         '(': 0,
#         '+': 2,
#         '-': 2,
#         '*': 4,
#         '/': 4,
#         'neg': 5,
#     }

#     precedence_input = {
#         '(': 6,
#         ')': 0,
#         '+': 1,
#         '-': 1,
#         '*': 3,
#         '/': 3,
#         'neg': 5,
#     }

#     operators = set("+-*/")

#     def transform(self, s):
#         # The generated postfix expression of s
#         output = []
#         # Wrap `s` with '(' and ')' to make processing easier
#         s = s + ')'
#         stack = ['(']
#         prevC = '('

#         hasNum = False
#         num = 0
#         for c in s:
#             if c == ' ':
#                 continue

#             # c is part of number
#             if c.isdigit():
#                 hasNum = True
#                 num = num * 10 + int(c)
#                 prevC = c
#                 continue
#             # c is operator
#             if hasNum:
#                 hasNum = False
#                 output.append(num)
#                 num = 0

#             # check if is negative unary operator
#             if c == '-' and (prevC == '(' or prevC in self.operators):
#                 c = 'neg'
            
#             # Pop until '('
#             while self.precedence_stack[stack[-1]] >= self.precedence_input[c]:
#                 popped = stack.pop()
#                 if popped != '(':
#                     output.append(popped)
#                 else:
#                     break
#             # push input on to the stack
#             if c != ')':
#                 stack.append(c)

#             prevC = c
        
#         return output

#     def evaluate_postfix(self, postfix):
#         stack = []

#         for each in postfix:
#             # Is number
#             if each not in self.precedence_input:
#                 stack.append(each)
#                 continue

#             # Is operator
#             if each == '+':
#                 stack.append(stack.pop() + stack.pop())
#             elif each == '-':
#                 a, b = stack.pop(), stack.pop()
#                 stack.append(b - a)
#             elif each == '*':
#                 stack.append(stack.pop() * stack.pop())
#             elif each == '/':
#                 a, b = stack.pop(), stack.pop()
#                 stack.append(int(b / a)) # truncate towards zero
#             elif each == 'neg':
#                 stack.append(-stack.pop())

#         return stack[0]

#     def calculate(self, s):
#         postfix = self.transform(s)
#         return self.evaluate_postfix(postfix)
    

