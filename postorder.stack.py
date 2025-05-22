# 590. N-ary Tree Postorder Traversal
# Easy

# Given the root of an n-ary tree, return the postorder traversal of its nodes' values.
# Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

# Example 1:
# Input: root = [1,null,3,2,4,null,5,6]
# Output: [5,6,3,2,4,1]

# Example 2:
# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
 
# Constraints:
# The number of nodes in the tree is in the range [0, 104].
# 0 <= Node.val <= 104
# The height of the n-ary tree is less than or equal to 1000.

# Follow up: Recursive solution is trivial, could you do it iteratively?



# sol 1

# """
# # Definition for a Node.
# class Node:
#     def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
#         self.val = val
#         self.children = children
# """

# class Solution:
#     def postorder(self, root: 'Node') -> List[int]:
#         if not root:
#             return []
#         stack = [root]
#         result = []
#         while stack:
#             node = stack.pop()
#             stack.extend(node.children)
#             result.append(node.val)
#         return reversed(result)
    


# sol 2

# class Solution:
#     def postorder(self, root: 'Node') -> List[int]:
#         # To store the output result...
#         output = []
#         self.traverse(root, output)
#         return output
#     def traverse(self, root, output):
#         # Base case: If root is none...
#         if root is None: return
#         # Recursively traverse each node in the children array...
#         for child in root.children:
#             self.traverse(child, output)
#         # Append the value of the root node to the output...
#         output.append(root.val)



# sol 3

# class Solution:
#     def postorder(self, root: 'Node') -> List[int]:
#         # To store the output result...
#         output = []
#         # To store the stack...
#         stack = []
#         # If root is not none...
#         if root is not None:
#             # Append the root node to the stack...
#             stack.append(root)
#         # While the stack is not empty...
#         while len(stack) > 0:
#             # Pop the last element from the stack...
#             node = stack.pop()
#             # Append the value of the root node to the output...
#             output.append(node.val)
#             # For each child in the children array...
#             for child in node.children:
#                 # Append the child node to the stack...
#                 stack.append(child)
#         # Reverse the output list and return it...
#         return output[::-1]
    


# sol 4

# class Solution:
#     def postorder(self, root: 'Node') -> List[int]:
#         # To store the output result...
#         output = []
#         # To store the stack...
#         stack = []
#         # If root is not none...
#         if root is not None:
#             # Append the root node to the stack...
#             stack.append(root)
#         # While the stack is not empty...
#         while len(stack) > 0:
#             # Pop the last element from the stack...
#             node = stack.pop()
#             # For each child in the children array...
#             for child in node.children:
#                 # Append the child node to the stack...
#                 stack.append(child)
#             # Append the value of the root node to the output...
#             output.append(node.val)
#         # Reverse the output list and return it...
#         return output[::-1]
    


# sol 5

# class Solution:
#     def postorder(self, root: 'Node') -> List[int]:
#         # If the root is None, return an empty list
#         if not root:
#             return []

#         res = []

#         # Define the DFS function
#         def dfs(root):
#             # Recursively call dfs for each child of the current node
#             for x in root.children:
#                 dfs(x)
#             # Append the value of the current node to the result list
#             res.append(root.val)

#         # Start DFS from the root
#         dfs(root)

#         # Return the result list containing node values in post-order
#         return res
    


# sol 6

# """
# # Definition for a Node.
# class Node:
#     def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
#         self.val = val
#         self.children = children
# """

# class Solution:
#     def postorder(self, root: 'Node') -> List[int]:
#         res = []
#         if not root: return res
        
#         def traverse(node,op):
#             if not node: return
#             for i in node.children:
#                 traverse(i,op)
#             op.append(node.val)
        
#         traverse(root,res)
#         return res